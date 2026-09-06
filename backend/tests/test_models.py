import uuid

from app.models.handoff import Handoff
from app.models.medication import Medication
from app.models.patient import Patient
from app.models.risk import RiskLevel, RiskPrediction
from app.models.timeline import TimelineEvent
from app.models.vitals import Vitals


def test_create_patient(db_session):
    patient = Patient(name="Test Patient", age=64, gender="male", ward="ICU")
    db_session.add(patient)
    db_session.commit()

    fetched = db_session.query(Patient).filter_by(id=patient.id).one()
    assert fetched.name == "Test Patient"
    assert fetched.age == 64


def test_patient_relationships(db_session):
    patient = Patient(name="Jane Doe", age=45, gender="female", ward="Ward 3")
    db_session.add(patient)
    db_session.commit()

    handoff = Handoff(patient_id=patient.id, summary="Stable overnight.")
    vitals = Vitals(patient_id=patient.id, heart_rate=78, oxygen_saturation=97)
    medication = Medication(patient_id=patient.id, name="Ceftriaxone", dose="1g")
    event = TimelineEvent(patient_id=patient.id, event_type="medication", description="Ceftriaxone given")
    risk = RiskPrediction(
        patient_id=patient.id,
        risk_level=RiskLevel.LOW,
        probability=0.12,
        model_version="v0-baseline",
    )
    db_session.add_all([handoff, vitals, medication, event, risk])
    db_session.commit()

    db_session.refresh(patient)
    assert len(patient.handoffs) == 1
    assert len(patient.vitals) == 1
    assert len(patient.medications) == 1
    assert len(patient.timeline_events) == 1
    assert len(patient.risk_predictions) == 1
    assert patient.risk_predictions[0].risk_level == RiskLevel.LOW


def test_handoff_defaults_to_incomplete(db_session):
    patient = Patient(name="Sam Lee", age=30, gender="male", ward="Ward 5")
    db_session.add(patient)
    db_session.commit()

    handoff = Handoff(patient_id=patient.id)
    db_session.add(handoff)
    db_session.commit()

    assert handoff.is_complete is False
    assert isinstance(handoff.id, uuid.UUID)
