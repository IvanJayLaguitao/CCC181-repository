# Proposed Application: MSU-IIT KlinikaQ

| | |
|---|---|
| **Student name** | Laguitao, Ivan Jay A. |
| **Section** | CS3A |
| **GitHub username** | IvanJayLaguitao |
| **Date submitted** | 2026-10-22 |

---

## 1. Problem Statement

### 1.1 Background

The MSU-IIT university clinic serves students and faculty for consultations, dental services, general checkups, and medical certificates. Patients currently have to physically stay in the waiting area to keep their place in line, because there is no way to know how close their turn is. This wastes time that students could spend in class and that faculty could spend working, and it crowds a small waiting area, especially at busy hours. 

### 1.2 Evidence from research

| Method | Who / where | Key finding |
|---|---|---|
| Interview | A 3rd-year student who visited the clinic | "I had a 3 PM class, but I had to sit in the clinic for half an hour for my checkup because I had a headache. I didn't want to leave because I was scared I'd lose my spot. But I was afraid of missing my class, so I left and just decided to come back early the next day." |
| Interview | A 1st-year freshman who visited the clinic for an ROTC medical certificate | "I went to the clinic 2 PM because I needed a medical certificate for ROTC. They gave me a number and I just sat there. I couldn't leave because I didn't know what time my number would be called." |
| Observation | Clinic waiting area, Friday around 4 PM| The waiting area was full (approx. 6 people). |
| Document review | The clinic's current paper logbook | The staff manually write the patient's name, and time of arrival. |

### 1.3 Point-of-view (POV) statement

**Students and faculty who visit the MSU-IIT clinic** need **a way to wait for their turn without staying in the waiting area** because **they lose class or work time in line and have no way of knowing how close their turn is.**

### 1.4 "How might we...?" question

How might we let clinic visitors know when their turn is near, so they can use their waiting time elsewhere and still not miss it?

### 1.5 Self-check

- [x] Names a real user group
- [x] States a need, not a feature
- [x] Rests on an insight from research (complete after you fill in section 1.2)
- [x] Is narrow enough to act on and open enough to allow different ideas

---

## 2. Target-User Profile

### 2.1 Primary persona

Fictional persona 
| | |
|---|---|
| **Name, age** | Alice, 20 |
| **Role / background** | 1st-year BS Marine Biology student with a full class schedule |
| **Goals** | Get a medical certificate or consultation quickly without missing class |
| **Frustrations / pain points** | Has to line up early and stay in the waiting area; cannot tell how long the wait will be; sometimes gives up and returns another day |
| **Context of use** | Uses a smartphone between classes, on campus Wi-Fi or mobile data; checks the app in short moments |
| **Accessibility considerations** | Needs a simple, mobile-friendly layout that works on slow connections; large buttons and short, plain-language text; the system must also work for senior and PWD patients, who may need larger text or help from staff |
| **Current workaround** | Lines up in person and waits, asks a friend to hold her place, or skips the visit |

### 2.2 User groups and stakeholders

| Group | Who | Relationship to the app |
|---|---|---|
| Primary users | Students and faculty/staff who visit the clinic | Join the queue, track their place, and receive reminders |
| Secondary users | Clinic nurses, doctors, and aides | Call, skip, and complete tickets; confirm priority requests |
| Stakeholders | Clinic head, university administration, data privacy officer | Approve, maintain, and are affected by how patient data is handled |

### 2.3 Organizational needs

- **Mission and service quality:** The clinic needs an orderly, fair queue that gives priority to critical cases, senior citizens, and persons with disabilities.
- **Privacy and compliance:** Health-related information is sensitive under the Data Privacy Act of 2012 (RA 10173). The system should collect only what the queue needs, show only ticket numbers on public screens, and store no diagnoses or medical history.
- **Existing systems and reporting:** The queue system should stay separate from the clinic's medical records, and should record timestamps so the clinic can review waiting times and busy hours.
- **Budget:** The system must run on free or low-cost hosting.
- **Possible conflict and how to handle it:** Patients want to request priority from their phones, but the clinic must prevent abuse. Priority requests stay unverified, and count as normal, until clinic staff confirm them on arrival. Only staff can assign critical status.

---

## 3. Proposed Application

### 3.1 Concept

MSU-IIT KlinikaQ is a web-based queue management system for the university clinic. A student like Ana opens it on her phone, chooses a service such as Consultation, Dental Services, or Laboratory Tests, and receives a ticket number. On the My Place page she sees how many people are ahead of her, and she can choose how many people ahead should trigger a reminder. When that point is reached, she gets a notification and heads back to the clinic. Clinic staff use their own view to call the next ticket, skip no-shows, and complete visits.

### 3.2 Value proposition

For **students and faculty of MSU-IIT** who **need to see the clinic without wasting hours in the waiting area**, **KlinikaQ** is a **web-based queue management system** that **lets them join the line remotely, see their place, and get reminded when their turn is near**. Unlike **the current walk-in line, where people must stay and wait**, it **lets patients wait anywhere and gives the clinic an orderly queue with verified priority handling**.

### 3.3 Value Proposition Canvas

| User side | Product side |
|---|---|
| **Jobs:** Get a consultation, checkup, dental service, or certificate without disrupting classes or work | **Features:** Online join, ticket number, My Place page, adjustable reminder (`remind_ahead`) |
| **Pains:** Long waits in a crowded area; not knowing the remaining wait; fear of missing their turn if they leave | **Pain relievers:** Live position in the queue; reminder when the chosen number of people are ahead; grace period before a ticket is skipped |
| **Gains:** Saved time; predictability; fairer treatment for seniors, PWDs, and urgent cases | **Gain creators:** Two-level queue (priority and normal) confirmed by staff; ticket numbers instead of names on public screens |

### 3.4 Existing applications (from your application analysis)

| Existing app | What it does well | Where it falls short | How your app differs |
|---|---|---|---|
| Manual walk-in line and logbook (current clinic process) | Needs no technology and is familiar to everyone | Patients must stay physically present; no position or wait information; no timestamps for reports | Remote joining, live position, reminders, and automatic timestamps |
| General queue services (e.g., Qminder, Waitwhile) | Mature remote queueing and notifications | Generic and typically subscription-based; not built around a university clinic's priority rules or privacy needs | Built for the clinic's services, with staff-confirmed priority and minimal data collection |

### 3.5 Technology choice

**Options considered:** Web application (Flask), native mobile app, SMS-based queue.

**Weighted decision matrix** (scores 1-5, higher is better):

| Option | Solves the problem ×3 | Team skills ×2 | Cost ×2 | Privacy ×2 | Time to MVP ×1 | Total /50 |
|---|---|---|---|---|---|---|
| Web app (Flask, mobile-friendly) | 5 | 5 | 5 | 4 | 5 | 48 |
| Native mobile app | 4 | 2 | 3 | 4 | 2 | 32 |
| SMS-based queue | 4 | 3 | 2 | 3 | 3 | 31 |

**Chosen technology and rationale:** A mobile-friendly web application built with Flask. It needs no app-store installation, works on any phone with a browser, uses skills learned in this course, and costs nothing to host at small scale. Email handles the reminder in the MVP, which addresses the main pain of not knowing when the turn is near. No emerging technology is needed.

---

## 4. Preliminary Requirements

### 4.1 Functional requirements (user stories)

| ID | User story | Priority (MoSCoW) |
|---|---|---|
| FR-01 | As a patient, I want to join the queue for a clinic service so that I get a ticket number without standing or sitting in line. | Must |
| FR-02 | As a patient, I want to see my position on the My Place page so that I know how long I still have to wait. | Must |
| FR-03 | As a patient, I want to choose how many people ahead of me trigger a reminder so that I have enough time to return to the clinic. | Must |
| FR-04 | As clinic staff, I want to call the next ticket, skip a no-show, and complete a visit so that the line keeps moving in order. | Must |
| FR-05 | As clinic staff, I want to confirm or reject a patient's senior or PWD request, and mark critical cases, so that priority is given fairly. | Should |
| FR-06 | As a patient, I want to cancel my ticket so that I do not block others if I cannot come. | Should |
| FR-07 | As clinic staff, I want to log in securely so that only authorized people can manage the queue. | Should |
| FR-08 | As a visitor, I want a public "Now Serving" screen so that I can see which number is being called. | Could |
| FR-09 | As a patient, I want to receive reminders by SMS so that I am notified even without internet. | Won't (this time) |

### 4.2 Non-functional requirements

| ID | Category | Requirement |
|---|---|---|
| NFR-01 | Performance | A patient's queue position updates within 5 seconds of any change, and pages load in under 3 seconds on a mobile connection |
| NFR-02 | Usability | A new patient can join the queue in 3 steps or fewer, in under 1 minute, on a phone |
| NFR-03 | Security / privacy | Public views show only ticket numbers; visit reasons and priority notes are visible to staff only; no diagnoses or medical history are stored; priority changes are recorded with the staff ID and time |
| NFR-04 | Compatibility | Works on the latest versions of Chrome, Firefox, Safari, and Edge, on screens 360 px wide and up |
| NFR-05 | Reliability | The reminder is sent within 1 minute of a patient reaching their chosen number of people ahead |

### 4.3 MoSCoW summary

- **Must have:** Join queue and get a ticket number; My Place position page; adjustable reminder; staff call, skip, and complete
- **Should have:** Staff-confirmed priority (critical, senior, PWD); cancel ticket; staff login
- **Could have:** Waiting-time reports; public "Now Serving" screen
- **Won't have (this time):** SMS reminders; integration with medical records

---

## 5. Minimum Viable Product (MVP)

The smallest version that still solves the core problem for Ana: she can join the queue remotely, see her place, and be reminded when her turn is near.

### 5.1 MVP features

1. Join the queue for a service and receive a ticket number (e.g., `C-001`)
2. My Place page showing the current position and ticket status
3. Adjustable reminder (`remind_ahead`, default 3) sent by email
4. Staff view to call the next ticket, skip, and complete

### 5.2 Out of scope

- SMS or push notifications: email is enough to prove the concept, and SMS adds cost
- Medical records and diagnoses: the queue app should not store sensitive health data
- Public "Now Serving" screen and reports: useful, but not needed to solve the core problem
- Aging or ratio rules for priority: start with two levels and review real waiting data first

### 5.3 Constraints and assumptions

- **Constraints:** One semester; free hosting tier; Flask with in-memory data first, then a database (e.g., SQLite) if time allows
- **Assumptions:** Patients have a smartphone with internet access and a school email; clinic staff are willing to use the staff view; the clinic provides its own list of critical cases; true emergencies go directly to staff instead of the queue

### 5.4 Feasibility check (TELOS)

| Dimension | Key question | Your assessment |
|---|---|---|
| Technical | Can I build it with my skills and tools? | Yes. Flask, templates, and simple status logic are covered in the course; email sending is the least familiar part |
| Economic | Do the benefits justify the costs? | Yes. Free tools and hosting; the benefit is saved time for patients and less crowding |
| Legal | Does it comply with law and policy (e.g., RA 10173)? | Feasible with care: collect minimum data, show no names publicly, and add a short privacy notice when joining |
| Operational | Will people use it, and can it be run? | Likely, if staff are trained and a clear "emergencies go straight to the clinic" notice is shown |
| Schedule | Can I deliver the MVP this semester? | Yes, since the MVP is limited to four features |

**Verdict:** Feasible, if the scope stays within the four MVP features and the data privacy points above are followed.

---

## Submission Checklist

- [x] File saved as `activities/proposed-application/README.md` in my CCC181 repository
- [x] All `TODO` items replaced
- [x] Sections 1-5 complete
- [ ] Images (if any) placed in `images/` and displaying correctly on GitHub