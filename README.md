# MSU-IIT KlinikaQ

KlinikaQ is a Flask prototype for managing visits to the MSU-IIT university
clinic. Patients can request a clinic service, receive a queue ticket, and check
their status and position from a ticket page. Clinic staff can review the active
queue, handle priority requests, and update ticket statuses from a dashboard.

This is a coursework prototype, not a production clinic system.

**Week 4 update:** The app now uses a PostgreSQL database running in Docker.
Tickets, users, and services are saved permanently and survive server restarts.

## What the app does

- Lets patients join one of five services: Consultation & Treatment, Emergency
  Response, Medical Certificate, Dental Services, or Laboratory Tests.
- Validates the patient's name, reason for visit, service, priority category,
  and `@msuiit.edu` email address before creating a ticket.
- Issues sequential ticket numbers (for example `N-001` and `P-002`) that reset
  daily, with an `N-` prefix for normal requests and a `P-` prefix for priority
  requests.
- Shows the ticket's service and status, the number of people ahead, and an
  estimated wait time based on the service's average duration. The ticket page
  polls for status and position updates every ten seconds.
- Lets patients set a reminder threshold and leave the queue (soft delete). The
  threshold is saved as a preference, but the prototype does not send
  notifications.
- Gives clinic staff a service filter, waiting counts, and controls to call,
  serve, or mark tickets as no-shows. Staff can confirm or decline priority
  requests; confirmed priority tickets automatically move to the top of the
  queue.
- Includes a "Manage Services" page where staff can add, rename, or deactivate
  clinic services.

## Routes

| Method | URL | Purpose |
|---|---|---|
| `GET` | `/` | Home page with a link to join the queue |
| `GET` | `/join` | Display the patient registration form |
| `POST` | `/join` | Validate the form, create a ticket, and redirect to it |
| `GET` | `/queue/<ticket_id>` | Display a ticket's status, queue position, and wait time |
| `GET` | `/queue/<ticket_id>/status.json` | Return the live ticket status and number of people ahead |
| `POST` | `/queue/<ticket_id>/leave` | Mark a waiting ticket as left (soft delete) |
| `POST` | `/queue/<ticket_id>/reminder` | Save the ticket's reminder threshold |
| `GET` | `/staff` | Display the staff dashboard; optionally filter with `service_id` |
| `POST` | `/staff/tickets/<ticket_id>/<action>` | Apply a staff action: `call`, `serve`, `no-show`, `confirm-priority`, `reject-priority`, or `delete` |
| `GET` | `/staff/services` | Manage clinic services (add, edit, deactivate) |

Unknown ticket IDs return a 404. Invalid status transitions and repeated
priority decisions return a 409.

## Project structure

```text
CCC181-repository/
├── app.py                         # Flask app, routes, and queue logic
├── models.py                      # SQLAlchemy database models
├── compose.yaml                   # Docker configuration for PostgreSQL
├── .env.example                   # Template for environment variables
├── .env                           # Local secrets (NOT committed to Git)
├── requirements.txt               # Python dependencies
├── .gitignore                     # Files excluded from Git
├── migrations/                    # Database migration scripts
├── templates/
│   ├── base.html                  # Shared page layout and navigation
│   ├── index.html                 # Home page
│   ├── join.html                  # Patient registration form
│   ├── staff.html                 # Staff queue dashboard
│   ├── services.html              # Manage services page
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
    ├── requirements.md            # Living list of project requirements
    ├── week3/                     # Interface report, research, and design assets
    └── week4/                     # Database schema, ERD, and report
```

## Run locally

### 1. Start the database

Make sure Docker Desktop is running, then start the PostgreSQL container:

```powershell
docker compose up -d
```

Wait until the container reports `healthy`:

```powershell
docker compose ps
```

### 2. Set up the environment

Copy `.env.example` to `.env` and fill in your values, then install the
dependencies:

```powershell
Copy-Item .env.example .env
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### 3. Build the database tables

```powershell
flask --app app db upgrade
flask --app app seed
```

### 4. Run the app

```powershell
flask --app app run --debug
```

Open <http://127.0.0.1:5000>. The debug server is for local development only;
do not use it in production.

## Prototype limitations

- The staff dashboard has no authentication, so anyone who can access the app
  can use its staff controls.
- Reminder thresholds are stored but do not trigger notifications, push
  messages, or SMS.
- The app uses a development-only Flask secret key. It is not ready for real
  patient information or production use.

> **Staff access is currently open:** the `/staff` dashboard has no login protection yet. 

## Requirements

See [docs/requirements.md](docs/requirements.md) for the full list of functional and non-functional requirements.