from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint, DateTime, ForeignKey, String, func, true
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[str | None] = mapped_column(String(20), unique=True)
    name: Mapped[str] = mapped_column(String(80))
    email: Mapped[str] = mapped_column(String(120), unique=True)
    role: Mapped[str] = mapped_column(String(20), default="student", server_default="student")
    tickets: Mapped[list["Ticket"]] = relationship(back_populates="user")

    __table_args__ = (
        CheckConstraint("role IN ('student', 'faculty', 'staff')", name="ck_users_role"),
    )


class Service(db.Model):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(primary_key=True)
    service_name: Mapped[str] = mapped_column(String(80), unique=True)
    avg_minutes: Mapped[int] = mapped_column(default=10, server_default="10")
    active: Mapped[bool] = mapped_column(default=True, server_default=true())
    tickets: Mapped[list["Ticket"]] = relationship(back_populates="service")


class Ticket(db.Model):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    priority_type: Mapped[str] = mapped_column(String(1), default="N", server_default="N")
    priority_reason: Mapped[str | None] = mapped_column(String(50))

    priority_confirmed: Mapped[bool] = mapped_column(default=False, server_default="false")

    ticket_number: Mapped[int] = mapped_column(default=1)    
    reason: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(20), default="waiting", server_default="waiting")
    remind_ahead: Mapped[int] = mapped_column(default=3, server_default="3")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    called_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"))
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id", ondelete="RESTRICT"))
    user: Mapped["User"] = relationship(back_populates="tickets")
    service: Mapped["Service"] = relationship(back_populates="tickets")

    __table_args__ = (
        CheckConstraint("status IN ('waiting', 'called', 'served', 'no-show', 'left')", name="ck_tickets_status"),
        CheckConstraint("priority_type IN ('N', 'P')", name="ck_tickets_priority_type"),
        CheckConstraint
        (
            "(priority_type = 'P' AND priority_reason IN ('PWD', 'Senior citizen', 'Pregnant', 'Others')) OR "
            "(priority_type = 'N' AND priority_reason IS NULL)",
            name="ck_tickets_priority_reason"
        ),
    )