# backend/app/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://collector:collectorpass@localhost/collections"
    REDIS_URL: str = "redis://localhost:6379/0"
    DEBUG: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
