import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Integer, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from app.models.handoff import Handoff
    from app.models.medication import Medication
    from app.models.risk import RiskPrediction
    from app.models.timeline import TimelineEvent
    from app.models.vitals import Vitals


class Patient(Base):
    """A patient record. Uses synthetic/de-identified data only for this
    student prototype — see the proposal's safety boundaries section.
    """

    __tablename__ = "patients"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    gender: Mapped[str] = mapped_column(String(20), nullable=False)
    ward: Mapped[str] = mapped_column(String(50), nullable=False)
    doctor: Mapped[str] = mapped_column(String(120), nullable=True)
    diagnosis: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    handoffs: Mapped[list["Handoff"]] = relationship(back_populates="patient")
    vitals: Mapped[list["Vitals"]] = relationship(back_populates="patient")
    medications: Mapped[list["Medication"]] = relationship(back_populates="patient")
    timeline_events: Mapped[list["TimelineEvent"]] = relationship(back_populates="patient")
    risk_predictions: Mapped[list["RiskPrediction"]] = relationship(back_populates="patient")
