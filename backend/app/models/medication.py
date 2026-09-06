import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from app.models.patient import Patient


class Medication(Base):
    """A medication administered to (or prescribed for) a patient."""

    __tablename__ = "medications"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    patient_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("patients.id"), nullable=False)
    handoff_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("handoffs.id"), nullable=True)

    name: Mapped[str] = mapped_column(String(120), nullable=False)
    dose: Mapped[str | None] = mapped_column(String(60), nullable=True)
    frequency: Mapped[str | None] = mapped_column(String(60), nullable=True)

    administered_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    patient: Mapped["Patient"] = relationship(back_populates="medications")
