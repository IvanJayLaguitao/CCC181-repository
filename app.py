import os
from datetime import datetime, timezone, timedelta
from sqlalchemy import case, func
from sqlalchemy.exc import IntegrityError
from dotenv import load_dotenv
from flask import Flask, abort, flash, redirect, render_template, request, url_for
from flask_migrate import Migrate

from models import db, User, Service, Ticket

load_dotenv()

app = Flask(__name__)
app.secret_key = "dev-only-change-me"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
db.init_app(app)
migrate = Migrate(app, db)

PH_TIME = timezone(timedelta(hours=8))

@app.template_filter("local")
def local_time(value):
    return value.astimezone(PH_TIME).strftime("%b %d, %I:%M %p") if value else ""

# --- HELPERS ---

def all_services():
    return db.session.scalars(db.select(Service).order_by(Service.service_name)).all()

def active_services():
    return db.session.scalars(db.select(Service).filter_by(active=True).order_by(Service.service_name)).all()

def queue_order_clause():
    return (
        case(
            ((Ticket.priority_type == "P") & (Ticket.priority_confirmed.is_(True)), 0),
            else_=1,
        ),
        Ticket.created_at.asc(),
        Ticket.id.asc(),
    )



def waiting_position_for_ticket(ticket):
    if ticket.status != "waiting":
        return None
    queue = db.session.scalars(
        db.select(Ticket)
        .where(Ticket.service_id == ticket.service_id)
        .where(Ticket.status == "waiting")
        .order_by(*queue_order_clause())
    ).all()
    for index, queued_ticket in enumerate(queue):
        if queued_ticket.id == ticket.id:
            return index + 1
    return None

# --- ROUTES ---

@app.route("/")
def index():
    return render_template("index.html")

@app.get("/join")
def join_form():
    return render_template("join.html", services=active_services(), form={})

@app.get("/queue/<int:ticket_id>")
def ticket(ticket_id):
    t = db.get_or_404(Ticket, ticket_id)
    position = waiting_position_for_ticket(t)

    if position is not None:
        ahead = (position - 1)  
    else: 
        ahead = 0
    est_wait = ahead * t.service.avg_minutes

    ready_time = datetime.now() + timedelta(minutes=est_wait)
    ready_time_str = ready_time.strftime("%I:%M %p")

    return render_template("ticket.html", ticket=t, service=t.service, ahead=ahead, position=position, est_wait=est_wait, ready_time=ready_time_str)

@app.post("/join")
def join():
    form = request.form
    name = form.get("name", "").strip()
    email = form.get("email", "").strip().lower()
    service_id = form.get("service_id", type=int)
    reason = form.get("reason", "").strip()
    priority_choice = form.get("priority", "normal")

    if priority_choice == "normal":
        priority_type = "N"
        priority_reason = None
    else:
        priority_type = "P"
        priority_reason = priority_choice

    errors = {}
    if not name or len(name) > 80:
        errors["name"] = "Enter your name (up to 80 characters)."
    if "@" not in email or len(email) > 120:
        errors["email"] = "Enter a valid email address (up to 120 characters)."
    service = db.session.get(Service, service_id)
    
    if not service or not service.active:
        errors["service_id"] = "Choose a valid service."
    if not reason:
        errors["reason"] = "Enter a reason for your visit."

    if errors:
        flash("Please fix the highlighted fields.", "danger")
        return render_template("join.html", services=active_services(), form=form, errors=errors), 400

    user = db.session.scalar(db.select(User).filter_by(email=email))
    if not user:
        user = User(name=name, email=email)
        db.session.add(user)

    count_today = db.session.scalar(
        db.select(func.count(Ticket.id)).where(
            func.date(Ticket.created_at.op('AT TIME ZONE')('Asia/Manila')) ==
            func.date(func.now().op('AT TIME ZONE')('Asia/Manila'))
        )
    )
    next_number = (count_today or 0) + 1

    ticket = Ticket(
        user=user,
        service=service,
        reason=reason,
        priority_type=priority_type,
        priority_reason=priority_reason,
        ticket_number=next_number,
        status="waiting",
    )
    db.session.add(ticket)
    db.session.commit()

    flash(f"You joined the queue. Your ticket is {ticket.priority_type}-{ticket.ticket_number:03d}.", "success")
    return redirect(url_for("ticket", ticket_id=ticket.id))

@app.get("/queue/<int:ticket_id>/status.json")
def ticket_status(ticket_id):
    t = db.get_or_404(Ticket, ticket_id)
    position = waiting_position_for_ticket(t)

    if position is None:
        return {"status": t.status, "ahead": 0, "position": None, "est_wait": 0}
    
    ahead = position - 1
    est_wait = ahead * t.service.avg_minutes

    ready_time = datetime.now(PH_TIME) + timedelta(minutes=est_wait)
    ready_time_str = ready_time.strftime("%I:%M %p")


    return {"status": t.status, "ahead": ahead, "position": position, "est_wait": est_wait, "ready_time": ready_time_str}

@app.post("/queue/<int:ticket_id>/leave")
def leave_queue(ticket_id):
    t = db.get_or_404(Ticket, ticket_id)
    if t.status == "waiting":
        t.status = "left"
        db.session.commit()
        flash("You have left the queue.", "info")
    return redirect(url_for("index"))

@app.post("/queue/<int:ticket_id>/reminder")
def update_reminder(ticket_id):
    t = db.get_or_404(Ticket, ticket_id)
    remind_ahead = request.form.get("remind_ahead", type=int)

    if t.status != "waiting":
        flash("Reminders are only available while your ticket is waiting", "danger")
    elif remind_ahead is None or remind_ahead < 0:
        flash("Invalid reminder", "danger")
    else:
        t.remind_ahead = remind_ahead
        db.session.commit()
        flash("Reminder preference saved", "success")
    return redirect(url_for("ticket", ticket_id=ticket_id))

@app.get("/staff")
def staff_dashboard():
    service_id = request.args.get("service_id", type=int)
    stmt = db.select(Ticket).where(Ticket.status.in_(["waiting", "called", "left", "no-show"]))
    
    if service_id is not None:
        stmt = stmt.where(Ticket.service_id == service_id)

    active_first = case(
        (Ticket.status.in_(["waiting", "called"]), 0),
        else_=1
    )

    stmt = stmt.order_by(active_first, *queue_order_clause())
    queue = db.session.scalars(stmt).all()
    services = all_services()

    next_ticket = next((t for t in queue if t.status == "waiting"), None)
    current_ticket = next((t for t in queue if t.status == "called"), None)

    return render_template("staff.html", queue=queue, services=services, selected=service_id, next_ticket=next_ticket, current_ticket=current_ticket)


@app.post("/staff/tickets/<int:ticket_id>/<action>")
def staff_action(ticket_id, action):
    t = db.get_or_404(Ticket, ticket_id)
    service_id = request.form.get("service_id", type=int)

    if action == "call":
        t.status = "called"
        t.called_at = func.now()
    elif action == "serve":
        t.status = "served"
    elif action == "confirm-priority":
        t.priority_confirmed = True
        flash(f"Priority confirmed for ticket {ticket_id}.", "success")
    elif action == "reject-priority":
        t.priority_confirmed = False
        t.priority_type = "N"
        t.priority_reason = None
        flash(f"Priority rejected for ticket {ticket_id}.", "warning")
    elif action == "no-show":
        t.status = "no-show"
    elif action == "delete":
        db.session.delete(t)
        db.session.commit()
        flash(f"Ticket {ticket_id} deleted.", "warning")
        return redirect(url_for("staff_dashboard", service_id=service_id) if service_id is not None else url_for("staff_dashboard"))
    else:
        abort(404)

    db.session.commit()
    flash(f"Ticket updated to {t.status}.", "info")
    return redirect(url_for("staff_dashboard", service_id=service_id) if service_id is not None else url_for("staff_dashboard"))

@app.post("/staff/tickets/<int:ticket_id>/delete")
def delete_ticket(ticket_id):
    t = db.get_or_404(Ticket, ticket_id)
    db.session.delete(t)  # hard delete: the row is gone for good
    db.session.commit()
    flash(f"Ticket #{ticket_id} was deleted.", "warning")
    return redirect(url_for("staff_dashboard"))

@app.get("/staff/services")
def services_list():
    services = db.session.scalars(db.select(Service).order_by(Service.service_name)).all()
    return render_template("services.html", services=services)

@app.post("/staff/services")
def service_create():
    name = request.form.get("name", "").strip()
    minutes = request.form.get("avg_minutes", type=int)
    if not name or len(name) > 60 or not minutes or minutes <= 0:
        flash("Enter a name (up to 60 characters) and minutes greater than 0.", "danger")
        return redirect(url_for("services_list"))
    db.session.add(Service(service_name=name, avg_minutes=minutes))
    try:
        db.session.commit()
        flash(f"Service '{name}' added.", "success")
    except IntegrityError:
        db.session.rollback()
        flash(f"A service named '{name}' already exists.", "danger")
    return redirect(url_for("services_list"))

@app.post("/staff/services/<int:service_id>/delete")
def service_delete(service_id):
    s = db.get_or_404(Service, service_id)
    if s.tickets:
        flash(f"'{s.service_name}' has tickets, so it cannot be deleted. Turn it off instead.", "danger")
        return redirect(url_for("services_list"))
    db.session.delete(s)
    db.session.commit()
    flash(f"Service '{s.service_name}' deleted.", "warning")
    return redirect(url_for("services_list"))

@app.cli.command("seed")
def seed():
    """Add the starting services if they are not there yet."""
    starting = [
        ("Consultation & Treatment", 15),
        ("Dental Services", 20),
        ("Medical Certificate", 5),
        ("Laboratory Tests", 10),
    ]
    for name, minutes in starting:
        exists = db.session.scalar(db.select(Service).filter_by(service_name=name))
        if exists is None:
            db.session.add(Service(service_name=name, avg_minutes=minutes))
    db.session.commit()
    print("Services are ready.")

if __name__ == "__main__":
    app.run(debug=True)