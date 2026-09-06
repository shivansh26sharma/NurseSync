from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central app configuration, loaded from environment variables / .env."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    PROJECT_NAME: str = "NurseSync AI"
    ENVIRONMENT: str = "development"

    DATABASE_URL: str = "postgresql+psycopg://nursesync:nursesync@localhost:5432/nursesync"
    SECRET_KEY: str = "change-me-in-week-2-when-auth-is-added"


settings = Settings()
