import enum
import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import JSON, DateTime, Enum, Float, ForeignKey, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from app.models.patient import Patient


class RiskLevel(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class RiskPrediction(Base):
    """An experimental deterioration-risk score for a patient.

    Decision-support only — see the proposal's safety boundaries.
    Populated starting in the ML stage of the roadmap; the table exists
    now so later weeks don't need a schema migration to add it.

    contributing_factors uses the generic JSON type (rather than
    Postgres-only JSONB) so the same model works against both the
    Postgres dev database and the SQLite in-memory DB used in CI tests.
    """

    __tablename__ = "risk_predictions"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    patient_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("patients.id"), nullable=False)

    risk_level: Mapped[RiskLevel] = mapped_column(Enum(RiskLevel, name="risk_level"), nullable=False)
    probability: Mapped[float | None] = mapped_column(Float, nullable=True)
    model_version: Mapped[str] = mapped_column(String(50), nullable=False)
    contributing_factors: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    predicted_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    patient: Mapped["Patient"] = relationship(back_populates="risk_predictions")
