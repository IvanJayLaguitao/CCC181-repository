# MSU-IIT KlinikaQ

KlinikaQ is a Flask prototype for managing visits to the MSU-IIT university
clinic. Patients can request a clinic service, receive a queue ticket, and check
their status and position from a ticket page. Clinic staff can review the active
queue, handle priority requests, and update ticket statuses from a dashboard.

This is a coursework prototype, not a production clinic system. Tickets are
stored in memory, so changes are lost when the app restarts.

## What the app does

- Lets patients join one of five services: Consultation & Treatment, Emergency
  Response, Medical Certificate, Dental Services, or Laboratory Tests.
- Validates the patient's name, reason for visit, service, priority category,
  and `@msuiit.edu` email address before creating a ticket.
- Issues sequential ticket numbers with an `N-` prefix for normal requests and
  a `P-` prefix for priority requests.
- Shows the ticket's service and status, along with the number of earlier
  waiting tickets for that service. The ticket page polls for status and
  position updates every ten seconds.
- Lets patients set a reminder threshold and leave the queue. The threshold is
  saved as a preference, but the prototype does not send notifications.
- Gives clinic staff a service filter, waiting counts, and controls to call,
  serve, or mark tickets as no-shows. Staff can confirm or decline priority
  requests; confirmed priority tickets are ordered first.

The app starts with four sample tickets in `app.py` so the queue and staff
dashboard have data to demonstrate.

## Routes

| Method | URL | Purpose |
|---|---|---|
| `GET` | `/` | Home page with a link to join the queue |
| `GET` | `/join` | Display the patient registration form |
| `POST` | `/join` | Validate the form, create a ticket, and redirect to it |
| `GET` | `/queue/<ticket_id>` | Display a ticket's status and queue position |
| `GET` | `/queue/<ticket_id>/status.json` | Return the ticket status and number of people ahead |
| `POST` | `/queue/<ticket_id>/leave` | Mark a waiting ticket as a no-show |
| `POST` | `/queue/<ticket_id>/reminder` | Save the ticket's reminder threshold |
| `GET` | `/staff` | Display the staff dashboard; optionally filter with `service_id` |
| `POST` | `/staff/tickets/<ticket_id>/<action>` | Apply a staff action: `call`, `serve`, `no-show`, `confirm-priority`, or `reject-priority` |

Unknown ticket IDs return a 404. Invalid status transitions and repeated
priority decisions return a 409.

## Project structure

```text
CCC181-repository/
├── app.py                         # Flask app, sample data, routes, and queue logic
├── requirements.txt               # Python dependencies
├── .gitignore                     # Files excluded from Git
├── templates/
│   ├── base.html                  # Shared page layout and navigation
│   ├── index.html                 # Home page
│   ├── join.html                  # Patient registration form
│   ├── staff.html                 # Staff queue dashboard
│   └── ticket.html                # Patient ticket and live status display
├── static/
│   ├── css/style.css              # App styles
│   ├── images/favicon.svg         # Browser icon
│   └── js/main.js                 # Form submission and confirmation behavior
├── .vscode/
│   └── settings.json              # Workspace editor settings
├── activities/
│   ├── git-exercises/             # CCC181 Git exercise materials
│   └── proposed-application/      # Project proposal materials
└── docs/
    └── week3/                     # Interface report, research, and design assets
```

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
flask --app app run --debug
```

Open <http://127.0.0.1:5000>. The debug server is for local development only;
do not use it in production.

## Prototype limitations

- Queue data and ticket changes live only in the Python process; there is no
  database or durable storage.
- The staff dashboard has no authentication, so anyone who can access the app
  can use its staff controls.
- Reminder thresholds are stored but do not trigger notifications.
- The app uses seeded demonstration patients and a development-only Flask
  secret key. It is not ready for real patient information or production use.
