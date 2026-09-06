from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check():
    """Liveness check — does the API process respond at all."""
    return {"status": "ok"}


@router.get("/health/db")
def health_check_db(db: Session = Depends(get_db)):
    """Readiness check — can the API actually reach PostgreSQL."""
    db.execute(text("SELECT 1"))
    return {"status": "ok", "database": "connected"}
