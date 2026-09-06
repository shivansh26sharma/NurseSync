import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Float, ForeignKey, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from app.models.patient import Patient


class Vitals(Base):
    """A single vitals reading tied to a patient (and optionally the
    handoff during which it was recorded).
    """

    __tablename__ = "vitals"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    patient_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("patients.id"), nullable=False)
    handoff_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("handoffs.id"), nullable=True)

    heart_rate: Mapped[float | None] = mapped_column(Float, nullable=True)
    blood_pressure_systolic: Mapped[float | None] = mapped_column(Float, nullable=True)
    blood_pressure_diastolic: Mapped[float | None] = mapped_column(Float, nullable=True)
    temperature: Mapped[float | None] = mapped_column(Float, nullable=True)
    oxygen_saturation: Mapped[float | None] = mapped_column(Float, nullable=True)
    respiratory_rate: Mapped[float | None] = mapped_column(Float, nullable=True)

    recorded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    patient: Mapped["Patient"] = relationship(back_populates="vitals")
