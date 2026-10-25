# MSU-IIT KlinikaQ

**MSU-IIT KlinikaQ** is a proposed queue management system for the MSU-IIT university clinic. Students and faculty can join the queue online for the clinic's services and follow their place in line from their phone, without having to wait inside the clinic.

Built with Flask for **CCC181 Week 2: Git, GitHub & Flask Foundations**.

## Services

- Consultation
- Dental Services
- General Checkup
- Medical Certificate

## Features

- **Join the queue online.** Choose a service and receive a ticket number such as `N-001`.
- **My Place page.** See your current position in the queue and your ticket status.
- **Reminder notification.** Get notified when people are ahead of you (3 by default), so you can step out and come back in time.
- **Two queue levels.** *Priority* (critical cases, senior citizens, and persons with disabilities) and *Normal* (routine visits). Priority is confirmed by clinic staff, and critical status is assigned by staff only.
- **Staff controls.** Call the next ticket, mark called tickets served, or record a no-show. Confirmed priority tickets appear first, and the dashboard shows waiting counts for each service.

> **Staff access is currently open:** the `/staff` dashboard has no login protection yet. Staff authentication will be added in a later week.


## Project structure

```text
CCC181-repository/
├── app.py        
├── requirements.txt   
├── .gitignore         
├── .venv/             
├── templates/         
│   ├── base.html       
│   ├── index.html      
│   └── ticket.html     
└── static/             
    ├── css/style.css
    └── js/main.js
```

## Routes

| URL | View function | What you see |
|---|---|---|
| `/` | `index()` | "Hello, Ana!" and a list of tickets, rendered with `index.html` |
| `/queue/<ticket_id>` | `ticket()` | A page for that ticket, e.g. `/queue/N-001` |
| `/staff` | `staff_dashboard()` | Open staff dashboard with service filters and queue controls |
| `/hello` | `hello()` | The plain text "Hello, CCC181!" |

Unknown ticket IDs return a 404.

## Getting started

### 1. Set up the Python environment

```bash
# create (once per project)
python -m venv .venv

# activate (every new terminal)
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS/Linux

# install the packages
pip install -r requirements.txt
```

Your prompt shows `(.venv)` when the environment is active. Some systems use `python3` or `py` instead of `python`.

If PowerShell blocks the activate script, run the following once, or use Command Prompt instead:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

If you add more packages later, record them with:

```bash
pip freeze > requirements.txt
```

### 2. Run the app

```bash
flask --app app run --debug
```

Open <http://127.0.0.1:5000>. With `--debug`, the server reloads every time you save a file. Never use debug mode in production.

## Git and GitHub workflow

### Once per computer

```bash
git config --global user.name "Your Name"
git config --global user.email you@g.msuiit.edu.ph   # same email as your GitHub account
git config --list
```

### Create the local repository and make the first commit

```bash
git init
git branch -M main
git status              # .venv should NOT appear, thanks to .gitignore
git add .
git commit -m "Add Flask starter app"
```

### Connect to GitHub and push

1. On GitHub, create a new **empty** repository (no README, no .gitignore).
2. Copy its URL, then run:

```bash
git remote add origin <repo-url>
git push -u origin main
```

GitHub does not accept your account password for Git over HTTPS. Sign in through Git Credential Manager or the GitHub CLI, or use a personal access token or an SSH key.

### Everyday loop

```bash
git pull origin main     # before you start working
git status
git add <file>
git commit -m "Add join-queue form"
git push origin main     # when you have commits to share
```

### Commit message tips

- Write a short summary in the imperative: "Add...", "Fix...".
- Make one logical change per commit.
- Commit early and often.
- Good: "Add join-queue form". Unhelpful: "update", "asdf", "final na talaga".

## Lab: ship it through a pull request

1. On GitHub, open an issue: **"Set up Flask starter app"**.
2. Pull the latest `main`, then create a branch:
   ```bash
   git switch main
   git pull origin main
   git switch -c feature/flask-setup
   ```
3. Create `.venv`, install Flask, and write `requirements.txt` and `.gitignore`.
4. Build `app.py` with a home route and one dynamic route, rendered with `base.html` and `index.html`.
5. Commit in small steps, then push the branch:
   ```bash
   git push -u origin feature/flask-setup
   ```
6. On GitHub, click **Compare & pull request** and write `Closes #N` in the description (N is your issue number). Merge it, then:
   ```bash
   git switch main
   git pull origin main
   ```

**Early finishers:** add another static CSS rule linked with `url_for`, or add a third route based on one Must feature from your project milestone.