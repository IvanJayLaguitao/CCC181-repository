"""CCC181 Week 2: a "Hello, Flask" starter app.

Run it with:
    flask --app app run --debug
then open http://127.0.0.1:5000
"""
from datetime import datetime
from flask import Flask, abort, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "dev-only-change-me"

SERVICES = [
    {"id": 1, "name": "Consultation & Treatment"},
    {"id": 2, "name": "Emergency Response"},
    {"id": 3, "name": "Medical Certificate"},
    {"id": 4, "name": "Dental Services"},
    {"id": 5, "name": "Laboratory Tests"},
]

TICKETS = [
    # 1. NORMAL
    {
        "ticket_number": "N-001", "name": "Ana", "email": "ana@school.edu", 
        "service_id": 1, "reason": "Headache and Fever", "status": "waiting", 
        "priority": "normal", "priority_reason": None, 
        "priority_confirmed": False, "remind_ahead": 3, 
        "created_at": datetime.now(), "called_at": None, "completed_at": None
    },
    # 2. PRIORITY
    {
        "ticket_number": "P-002", "name": "Ben", "email": "ben@school.edu", 
        "service_id": 2, "reason": "Toothache", "status": "waiting", 
        "priority": "PWD", "priority_reason": "PWD", 
        "priority_confirmed": True, "remind_ahead": 1, 
        "created_at": datetime.now(), "called_at": None, "completed_at": None
    }
]

@app.route("/")
def index():
    # We just render the welcome page now
    return render_template("index.html")

@app.get("/join")
def join_form():
    return render_template("join.html", services=SERVICES, form={})

@app.post("/join")
def join():
    form = request.form
    name = form.get("name", "").strip()
    email = form.get("email", "").strip().lower()
    service_id = form.get("service_id", type=int)
    reason = form.get("reason", "").strip()
    priority = form.get("priority", "normal")

    errors = {}
    if not name:
        errors["name"] = "Enter your name."
    if "@" not in email:
        errors["email"] = "Enter a valid email address."
    if service_id not in [s["id"] for s in SERVICES]:
        errors["service_id"] = "Choose a service."
    if not reason:
        errors["reason"] = "Enter a reason for your visit."
    if priority not in ["normal", "PWD", "Senior Citizen"]:
        errors["priority"] = "Invalid priority."
        
    if errors:
        flash("Please fix the highlighted fields.", "danger")
        return render_template("join.html", services=SERVICES, form=form, errors=errors), 400

    # Generate the next sequential number
    number = int(TICKETS[-1]["ticket_number"].split("-")[1]) + 1 if TICKETS else 1
    
    # Decide the prefix (N for Normal, P for PWD/Senior)
    prefix = "N" if priority == "normal" else "P"
    new_ticket_number = f"{prefix}-{number:03d}"

    # Save the ticket with ALL fields
    TICKETS.append({
        "ticket_number": new_ticket_number, 
        "name": name, 
        "email": email,
        "service_id": service_id, 
        "reason": reason, 
        "status": "waiting", 
        "priority": priority, 
        "priority_reason": priority if priority != "normal" else None, 
        "priority_confirmed": False,
        "remind_ahead": 3, 
        "created_at": datetime.now(), 
        "called_at": None, 
        "completed_at": None
    })

    flash(f"You joined the queue. Your ticket is {new_ticket_number}.", "success")
    return redirect(url_for("ticket", ticket_id=new_ticket_number))

@app.get("/queue/<ticket_id>")
def ticket(ticket_id):
    ticket_index = next(
        (index for index, item in enumerate(TICKETS)
         if item["ticket_number"] == ticket_id),
        None,
    )
    if ticket_index is None:
        abort(404)

    current_ticket = TICKETS[ticket_index]

    service = next(
        (item for item in SERVICES if item["id"] == current_ticket["service_id"]),
        None,
    )
    if service is None:
        abort(500)

    people_ahead = sum(
        1 for item in TICKETS[:ticket_index]
        if item["service_id"] == current_ticket["service_id"]
        and item["status"] == "waiting"
    )
    return render_template(
        "ticket.html",
        ticket=current_ticket,
        service=service,
        people_ahead=people_ahead,
    )


@app.post("/queue/<ticket_id>/leave")
def leave_queue(ticket_id):
    current_ticket = next(
        (item for item in TICKETS if item["ticket_number"] == ticket_id),
        None,
    )
    if current_ticket is None:
        abort(404)

    if current_ticket["status"] == "waiting":
        current_ticket["status"] = "no-show"
        flash("You have left the queue.", "success")
    else:
        flash("This ticket is no longer waiting in the queue.", "info")
    return redirect(url_for("index"))


@app.post("/queue/<ticket_id>/reminder")
def update_reminder(ticket_id):
    current_ticket = next(
        (item for item in TICKETS if item["ticket_number"] == ticket_id),
        None,
    )
    if current_ticket is None:
        abort(404)

    remind_ahead = request.form.get("remind_ahead", type=int)
    if current_ticket["status"] != "waiting":
        flash("Reminders are only available while your ticket is waiting.", "danger")
    elif remind_ahead is None or remind_ahead < 0:
        flash("Enter a reminder threshold of zero or more.", "danger")
    else:
        current_ticket["remind_ahead"] = remind_ahead
        flash("Your reminder preference was saved.", "success")
    return redirect(url_for("ticket", ticket_id=ticket_id))


@app.route("/staff")
def staff_dashboard():
    return "Staff dashboard coming soon"

if __name__ == "__main__":
    app.run(debug=True)