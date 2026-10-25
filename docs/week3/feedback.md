## Screen 1: Join the Queue

**Works well:** The emergency notice at the top is highly visible, fulfilling the requirement that emergencies go straight to staff. The form is simple, asking only for the essentials (Name, Reason, Service), which follows Mark's rule that joining must take under 1 minute.

**Problem:** The "Request Priority" checkbox does not ask for a reason. If a student checks it, the staff might have to ask them why they requested it, which slows down the line (match with the real world).

**Change:** I will add a dropdown that appears only if the Priority box is checked, allowing the user to select so the staff can verify it instantly.

---

## Screen 2: My Place

**Works well:** The ticket number (C-007) and the number of people ahead (4) are the largest elements on the screen. This perfectly follows Mark's rule that he needs to see his position at a glance while walking around campus. The status "Waiting" is also clearly visible.

**Problem:** The "Cancel ticket" button is very large and right next to the reminder input. A user might accidentally tap it while trying to adjust their reminder (error prevention).

**Change:** I will make the "Cancel ticket" button smaller, maybe as a text link at the very bottom of the screen, and change its color to red in the final CSS to signify it is a destructive action. 

---

## Screen 3: Staff Dashboard

**Works well:** The "Call Next" button is the biggest element on the screen, and the "Now Serving" box is front and center. This perfectly follows Leo's rule that he needs to manage the queue quickly while talking to patients.

**Problem:** The waiting list shows the names and reasons, but it doesn't clearly highlight who is a Priority (PWD/Senior) in the list itself.

**Change:** I will add a colored badge next to the ticket numbers in the waiting list table so Leo can spot them instantly.