# MSU-IIT KlinikaQ requirements

## 1a. Describe your setting and the problem


**Setting:** MSU-IIT University clinic, weekday mornings and afternoons.
**People who wait:** Students and faculty needing checkups or certificates. See *Mark* in [docs/week3/personas.md](week3/personas.md).
**People who serve:** Clinic staff and student assistants managing the queue. See *Leo* in [docs/week3/personas.md](week3/personas.md).

**Problem statement:** A student who visits the clinic between classes needs a way to know when it is their turn without standing in line, because they lose their place and waste time whenever they step out.

## 1b. Functional requirements

| ID | Requirement | Priority | Stores data? | Status |
| --- | --- | --- | --- | --- |
| FR-01 | A student can join the queue for a service by entering their name and email. | Must | **Yes** | Built (Week 3) |
| FR-02 | A student can see their ticket number, status, and how many people are ahead of them. | Must | **Yes** | Built (Week 3) |
| FR-03 | A staff member can call the next waiting ticket for a service. | Must | **Yes** | Built (Week 3) |
| FR-04 | A staff member can mark a called ticket as served or no-show. | Must | **Yes** | Built (Week 3) |
| FR-05 | A student can leave the queue before being called. | Must | **Yes** | Built (Week 3) |
| FR-06 | A staff member can add, rename and switch off a service. | Must | **Yes** | This week |
| FR-07 | A staff member can see how many people left before being served, per service, per day. | Should | **Yes** | Later |
| FR-08 ★ | A senior citizen or person with a disability can join a priority lane that is served first. | Should | **Yes** | This week |
| FR-09 ★ | A student can request priority status for PWD or Senior Citizen when joining. | Must | **Yes** | This week |
| FR-10 ★ | A staff member can confirm or reject a priority request. | Must | **Yes** | This week |
| FR-11 | A student/user can switch the page to a larger text size. | Could | No | Later |

## 1c. Non-functional requirements

| ID | Requirement | Category | Priority |
| --- | --- | --- | --- |
| NFR-01 | No ticket is lost when the server or the database restarts. | Reliability | Must |
| NFR-02 | Two people can never get the same ticket, even if they join at the same moment. | Data integrity | Must |
| NFR-03 | My place loads in under 2 seconds on mobile data. | Performance | Should |
| NFR-04 | Every screen scores 90 or higher in the Lighthouse accessibility check. | Accessibility | Must |
| NFR-05 | No password or secret key is stored in the repository. | Security | Must |

## 1d. MVP

- **MVP:** FR-01, FR-02, FR-03, FR-04, FR-05, FR-06, FR-08, FR-09, FR-10. 
This is the smallest version that solves the problem: students can join, view their place, and staff can manage the queue with priority handling. 
- **Out of scope:** 
  - SMS notifications: Requires a paid API. Email is enough for the MVP.
  - Integration with medical records: Privacy concerns; the queue app should not store sensitive health data.

## 1e. Check requirements with a real person

| Who (role only) | What they said | What I changed |
| --- | --- | --- |
| Student | "I also want to know if the clinic is currently open or closed before I walk there or join." | Added a *Could* requirement for clinic status (FR-12). |
| Clinic staff member | "We need to know if a priority ticket was a Senior or a PWD so we can prepare the right assistance." | Added a `priority_reason` field to the tickets table (FR-08, FR-09). |

