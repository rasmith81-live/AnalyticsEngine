"""
Configuration settings for Data Governance Service.
"""

from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings for Data Governance Service."""
    
    # Service Configuration
    service_name: str = Field(
        default="data_governance_service",
        env="SERVICE_NAME",
        description="Name of this service"
    )
    service_host: str = Field(
        default="0.0.0.0",
        env="SERVICE_HOST",
        description="Service host address"
    )
    service_port: int = Field(
        default=8013,
        env="SERVICE_PORT",
        description="Service port"
    )
    
    # Database Service Configuration
    database_service_url: str = Field(
        default="http://database_service:8000",
        env="DATABASE_SERVICE_URL",
        description="URL for the backend_services/database_service"
    )
    
    # Messaging Service Configuration
    messaging_service_url: str = Field(
        default="http://messaging_service:8001",
        env="MESSAGING_SERVICE_URL",
        description="URL for the backend_services/messaging_service"
    )
    
    # Distributed Tracing Configuration
    enable_distributed_tracing: bool = Field(
        default=True,
        env="ENABLE_DISTRIBUTED_TRACING",
        description="Enable OpenTelemetry distributed tracing"
    )
    otlp_endpoint: str = Field(
        default="http://observability_service:4317",
        env="OTLP_ENDPOINT",
        description="OpenTelemetry collector endpoint for trace export"
    )
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
