# Persistence Test

## 11a. Restart Test
I created 5 tickets, called one, served one, and marked one as a no-show. 
After stopping Docker and Flask, and restarting them, all 5 tickets, statuses, and timestamps were exactly as before. This proves NFR-01 passed.

**Before Restart:**
![Before restart](screenshot/before_restart.png)
![Before restart SQL](screenshot/before-restart-sql.png)

**After Restart:**
![After restart](screenshot/after_restart.png)
![After restart SQL](screenshot/after-restart-sql.png)

## 11b. Rebuild from scratch
I ran `docker compose down -v`, followed by `up -d`, `flask db upgrade`, and `flask db seed`. 
The app successfully rebuilt the database, loaded the services on the Join form, and allowed new tickets to be created.