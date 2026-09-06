"""Import all models here so Alembic's autogenerate can discover them
through Base.metadata, and so `from app.db.base import Base` gives you
a fully populated metadata object in one place.
"""

from app.db.base_class import Base  # noqa: F401
from app.models.handoff import Handoff  # noqa: F401
from app.models.medication import Medication  # noqa: F401
from app.models.patient import Patient  # noqa: F401
from app.models.risk import RiskPrediction  # noqa: F401
from app.models.timeline import TimelineEvent  # noqa: F401
from app.models.user import User  # noqa: F401
from app.models.vitals import Vitals  # noqa: F401
