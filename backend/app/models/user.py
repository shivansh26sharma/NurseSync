import enum
import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class UserRole(str, enum.Enum):
    NURSE = "nurse"
    ADMIN = "admin"


class User(Base):
    """A nurse or admin who can log into NurseSync AI.

    Login/auth endpoints land in Week 2 — this week only defines the table
    so Handoff can reference who recorded it.
    """

    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    full_name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_role"), default=UserRole.NURSE, nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
