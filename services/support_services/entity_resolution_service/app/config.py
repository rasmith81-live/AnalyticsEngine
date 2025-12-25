"""
Configuration settings for Entity Resolution Service.
"""

from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings for Entity Resolution Service."""
    
    # Service Configuration
    service_name: str = Field(
        default="entity_resolution_service",
        env="SERVICE_NAME",
        description="Name of this service"
    )
    service_host: str = Field(
        default="0.0.0.0",
        env="SERVICE_HOST",
        description="Service host address"
    )
    service_port: int = Field(
        default=8012,  # Correct port per docker-compose
        env="SERVICE_PORT",
        description="Service port"
    )
    
    # Business Logic Configuration
    MATCHING_THRESHOLD: float = Field(
        default=0.85, 
        env="MATCHING_THRESHOLD",
        description="Threshold for fuzzy matching (0.0 - 1.0)"
    )
    
    # External Service URLs
    business_metadata_url: str = Field(
        default="http://business_metadata:8000",
        env="BUSINESS_METADATA_URL",
        description="URL of Business Metadata Service for value chain queries"
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

