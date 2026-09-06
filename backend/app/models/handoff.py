import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Text, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from app.models.patient import Patient


class Handoff(Base):
    """One nurse-to-nurse handoff record for a patient.

    Week 1: manual/structured fields only. transcript/summary/SBAR fields
    stay nullable until speech-to-text (Week 6) and NLP/LLM steps land.
    """

    __tablename__ = "handoffs"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    patient_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("patients.id"), nullable=False)
    nurse_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"), nullable=True)

    audio_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    transcript: Mapped[str | None] = mapped_column(Text, nullable=True)

    sbar_situation: Mapped[str | None] = mapped_column(Text, nullable=True)
    sbar_background: Mapped[str | None] = mapped_column(Text, nullable=True)
    sbar_assessment: Mapped[str | None] = mapped_column(Text, nullable=True)
    sbar_recommendation: Mapped[str | None] = mapped_column(Text, nullable=True)
    summary: Mapped[str | None] = mapped_column(Text, nullable=True)

    is_complete: Mapped[bool] = mapped_column(default=False)
    missing_fields: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    patient: Mapped["Patient"] = relationship(back_populates="handoffs")
