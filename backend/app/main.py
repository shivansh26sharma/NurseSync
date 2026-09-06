from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(health_router)


@app.get("/")
def root():
    return {"message": f"{settings.PROJECT_NAME} backend is running"}
