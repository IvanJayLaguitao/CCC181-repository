# Schema Self-Review

## Entry 1: Coverage & Data Integrity
- **Works well:** Every requirement marked *Stores data = Yes* has a corresponding table and column. For example, FR-06 (switching off a service) is handled by `services.service_name` and `services.active`.
- **Problem:** Users might accidentally double-tap the "Join" button, creating duplicate user accounts and tickets in the database.
- **Change:** We added a `UNIQUE` constraint to `users.email`. If a user tries to join twice with the same email, the database will reject the duplicate user account, keeping the data clean.

## Entry 2: Facts, Not Results (Normalization)
- **Works well:** The `tickets` table does not store a "position" number. Instead, it stores `created_at`. The position is computed dynamically in the backend by counting how many tickets were created before this one.
- **Problem:** I initially wanted to store the ticket number as a string (e.g., "N-001"). However, this mixes the priority type with the daily sequence number, making it a computed result.
- **Change:** I separated the data into two raw facts: `priority_type` (N or P) and `ticket_number` (an integer like 1, 2, 3). The backend now generates the "N-001" string for the HTML, keeping the database pure.

## Entry 3: ID Types for Different Roles
- **Works well:** The system supports students, faculty, and staff all in one `users` table.
- **Problem:** Students have a Student ID (e.g., `2024-1234`), but faculty and staff use a similar-looking Employee ID, which is not technically a "student" ID. Strictly requiring a `student_id` could cause errors if a user doesn't have one.
- **Change:** We kept the column named `student_id` for simplicity (since students are the primary users), but made it **nullable** for faculty and staff to avoid triggering a database error.

## Entry 4: Deletes and History
- **Works well:** We use `ON DELETE RESTRICT` for both `user_id` and `service_id` in the tickets table.
- **Problem:** If a staff member tries to delete a clinic service (like "Dental") that has existing tickets, the database will block the deletion.
- **Change:** This is intentional. The clinic needs the ticket history for reports and audits. Instead of deleting a discontinued service, the staff should use the `active = False` feature to hide it from the join form.