from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings."""
    
    # Base
    APP_NAME: str = "FODMAP Helper API"
    DEBUG: bool = False
    
    # Database
    DATABASE_URL: str = "sqlite:///./fodmap.db"
    
    # API
    API_V1_PREFIX: str = "/api/v1"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings() 