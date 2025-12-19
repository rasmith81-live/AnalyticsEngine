
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Conversation Service"
    API_V1_STR: str = "/api/v1"
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8004
    
    # LLM Provider
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    AZURE_OPENAI_API_KEY: str = os.getenv("AZURE_OPENAI_API_KEY", "")
    AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT", "")
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "openai")  # openai or azure
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-4-turbo-preview")
    
    # Messaging
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://redis:6379/0")
    
    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
