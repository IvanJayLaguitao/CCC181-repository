# Validation in Three Layers

## 1. Browser Layer
- The Join form uses HTML `required` attributes on Name, Email, Service, and Reason, `type="email"` to ensure valid formatting, and `maxlength="80"` to match the database column limit.

## 2. Flask Layer
I bypassed the browser using `curl` to send bad data directly to the server.

| Rule | Layer | How I tested it | What happened |
| --- | --- | --- | --- |
| Name, Email, and Service validation | Flask | `curl.exe -X POST ... -d "name=" -d "email=not-an-email" -d "service_id=999"` | `HTTP/1.1 400 BAD REQUEST`. The page reloaded with error messages. No data was saved. |
| Name length limit | Flask | `curl.exe -X POST ... -d "name=AAA...(200 chars)"` | `HTTP/1.1 400 BAD REQUEST`. The validation caught it before hitting the database. |
| Reason required | Flask | `curl.exe -X POST ... -d "reason="` | `HTTP/1.1 400 BAD REQUEST`. The form rejected the missing reason. |

## 3. Database Layer
I bypassed Flask entirely and tried to insert bad data directly into PostgreSQL using `psql`. **Every one of these commands failed**, proving the constraints are working.

| Rule | Layer | How I tested it | What happened |
| --- | --- | --- | --- |
| Service must exist | Database | `INSERT INTO tickets ... service_id 999` | `ERROR: violates foreign key constraint "tickets_service_id_fkey"` |
| Status must be valid | Database | `UPDATE tickets SET status = 'lost'` | `ERROR: new row for relation "tickets" violates check constraint "ck_tickets_status"` |
| Email must be unique | Database | `INSERT INTO users ... duplicate email` | `ERROR: duplicate key value violates unique constraint "users_email_key"` |
| Avg minutes must be > 0 | Database | `INSERT INTO services ... avg_minutes 0` | `ERROR: new row for relation "services" violates check constraint "ck_services_avg_minutes"` |
| Cannot delete service with tickets | Database | `DELETE FROM services WHERE id = 1` | `ERROR: update or delete on table "services" violates foreign key constraint "tickets_service_id_fkey"` |

## 4. SQL Injection Check
I ran `git grep -nE "f[\"'].*(SELECT|INSERT|UPDATE|DELETE)" -- "*.py"` to ensure no raw SQL was built using f-strings. The command returned nothing, confirming the code is safe from SQL injection.