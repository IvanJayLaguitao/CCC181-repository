## Nurse Leo, the clinic staff member

"I used to hate sitting in the clinic for half an hour just to get a checkup for my headache, so I'd leave and come back the next day. Now that I work the front desk, I see students doing the exact same thing every day. I want a system that lets them wait somewhere else so they don't miss their classes." (interview / observation)


| | |
| --- | --- |
| **Photo or sketch** | |
| **Age, role and background** | 21, 3rd-year Nursing student assigned as staff assistant. *(observation)* |
| **Goals** | 1. Keep the clinic line moving quickly and fairly. 2. Ensure emergencies and PWDs are prioritized correctly. 3. Manage the queue without getting distracted from assisting patients. |
| **Frustrations** | 1. The waiting area gets full and messy. 2. The current paper logbook is hard to read and track. 3. Patients constantly ask him how long the wait is, which slows down his work. |
| **Devices and context** | Uses a desktop computer at the clinic front desk, often multitasking between checking patients, answering the phone, and updating records. |
| **Tech comfort** | High. Uses web applications and hospital systems comfortably. |
| **Accessibility needs** | Needs a clear, high-contrast dashboard with large buttons because he is often glancing at the screen quickly while talking to patients face-to-face. |

### Scenario

It is 3:00 PM and the clinic waiting area is full. Leo opens the KlinikaQ Staff Dashboard on the desktop. He sees a list of waiting tickets. He notices a senior citizen (P-002) and a student with a headache (N-001). He clicks the "Call Next" button for P-002, which updates the lobby screen and the patient's phone. He handles the visit, clicks "Served," and immediately moves to the next ticket, keeping the line moving efficiently.

### Top tasks in the app

| Task | Screen | Requirement ID |
| --- | --- | --- |
| View the waiting list in order | Staff dashboard | FR-04 |
| Call the next ticket | Staff dashboard | FR-04 |
| Mark a ticket as served or no-show | Staff dashboard | FR-04 |
| Confirm or reject a priority request | Staff dashboard | FR-05 |

### What this means for my interface

1. Because Leo is often multitasking between the front desk and patient care, the "Call Next" and "Serve" buttons must be large and easy to click at a glance.
2. Because he needs to handle emergencies fairly, the staff dashboard must visually highlight Emergency and Priority tickets at the top of the list.
3. Because he needs to keep the line moving quickly, the dashboard must load instantly and not require refreshing the page to see new patients who joined remotely.

---

    ## Mark, the freshman needing a certificate

    > "I went to the clinic 2 PM because I needed a medical certificate for ROTC. They gave me a number and I just sat there. I couldn't leave because I didn't know what time my number would be called." *(interview)*

    | | |
    | --- | --- |
    | **** |  |
    | **Age, role and background** | 18, 1st-year student. Needs a medical certificate for ROTC requirements. *(interview)* |
    | **Goals** | 1. Get his medical certificate for ROTC as fast as possible. 2. Avoid wasting his whole afternoon sitting in the clinic. 3. Know exactly when to come back so he doesn't lose his place in line. |
    | **Frustrations** | 1. Being stuck sitting in the clinic without knowing when his number will be called. 2. The long wait time. 3. Not being able to do other school requirements while waiting. |
    | **Devices and context** | Uses a smartphone while walking around the campus, usually juggling multiple errands and requirements. |
    | **Tech comfort** | High. Very comfortable with mobile web apps. |
    | **Accessibility needs** | Needs clear, readable text on a small phone screen and a fast-loading page so he doesn't waste his mobile data. |

    ### Scenario

    Mark needs to submit his ROTC medical certificate by the end of the day. He goes to the clinic at 2:00 PM and sees a long line. Instead of sitting down and waiting for an hour, he opens KlinikaQ on his phone. He joins the "Physical Fitness Certification" queue and gets ticket N-002. He decides to walk to the registrar's office to finish another errand. When KlinikaQ alerts him that he is next, he walks back to the clinic, gets his certificate, and makes it to his next class on time.

    ### Top tasks in the app

    | Task | Screen | Requirement ID |
    | --- | --- | --- |
    | Join the queue for Physical Fitness Certification | Join | FR-01 |
    | Check how many people are ahead | My place | FR-02 |
    | See when it is his turn | My place | FR-04 |

    ### What this means for my interface

    1. Because Mark is running multiple errands and doesn't want to waste time sitting, the "My place" screen must clearly show his exact position in line at a glance.
    2. Because he only has a short time between errands, the "Join" form must be quick and simple (3 steps or fewer) so he can get his ticket in under a minute.
    3. Because he might be anywhere around campus, the app must clearly show how many patients are ahead of him and send a reminder when it is almost his turn, so he knows exactly when to head back to the clinic.

