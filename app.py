"""CCC181 Week 2: a "Hello, Flask" starter app.

Run it with:
    flask --app app run --debug
then open http://127.0.0.1:5000
"""
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

# Sample data for the demo. A real app would load this from a database later.
SERVICES = [
    {"id": 1, "name": "Consultation & Treatment"},
    {"id": 2, "name": "Emergency Response"},
    {"id": 3, "name": "Physical Fitness Certification"},
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
        "priority": "priority", "priority_reason": "Senior Citizen", 
        "priority_confirmed": True, "remind_ahead": 1, 
        "created_at": datetime.now(), "called_at": None, "completed_at": None
    },
    # 3. EMERGENCY
    {
        "ticket_number": "E-003", "name": "Carlo", "email": "carlo@school.edu", 
        "service_id": 1, "reason": "Deep cut on hand", "status": "waiting", 
        "priority": "emergency", "priority_reason": "Severe bleeding", 
        "priority_confirmed": True, "remind_ahead": 0, 
        "created_at": datetime.now(), "called_at": None, "completed_at": None
    }
]

@app.route("/")
def index():
    # render_template looks inside the templates/ folder and passes
    # keyword arguments to the template as variables.
    return render_template("index.html", name="Ana", tickets=TICKETS)


@app.route("/queue/<ticket_id>")
def ticket(ticket_id):
    # I removed <int:> so it can accept strings like "N-001"
    return render_template("ticket.html", ticket_id=ticket_id)


@app.route("/hello")
def hello():
    # The plain-string version from the Routes slide.
    return "Hello, CCC181!"


if __name__ == "__main__":
    # Lets you also start the app with: python app.py
    app.run(debug=True)
