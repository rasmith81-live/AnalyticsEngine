"""
Configuration settings for the Observability Service.

This module provides configuration settings for the Observability Service
using Pydantic v2 for validation.
"""

from pydantic import Field, ConfigDict, field_validator
from pydantic_settings import BaseSettings
from typing import List, Optional, Union
import json
from functools import lru_cache


class Settings(BaseSettings):
    """
    Configuration settings for the Observability Service.
    """
    # Service configuration
    service_name: str = Field("observability_service", description="Name of the service")
    version: str = Field("0.1.0", description="Service version")
    environment: str = Field("development", description="Deployment environment")
    debug: bool = Field(False, description="Debug mode")
    host: str = Field("0.0.0.0", description="Service host")
    port: int = Field(8000, description="Service port")
    service_url: str = Field("http://localhost:8080", description="URL of the service itself")
    api_prefix: str = Field("/api/v1", description="API prefix for all endpoints")
    log_level: str = Field("INFO", description="Logging level")
    
    # Database Service configuration
    database_service_url: str = Field("http://database_service:8000", description="Database Service URL")
    database_service_timeout: int = Field(30, description="Database Service request timeout in seconds")
    database_service_retries: int = Field(3, description="Number of retries for Database Service requests")
    
    # Messaging Service configuration
    messaging_service_url: str = Field("http://messaging_service:8000", description="Messaging Service URL")
    messaging_service_timeout: int = Field(30, description="Messaging Service request timeout in seconds")
    messaging_service_retries: int = Field(3, description="Number of retries for Messaging Service requests")
    subscribe_to_events: bool = Field(True, description="Whether to subscribe to events")
    
    # Redis configuration (for direct access if needed)
    redis_url: str = Field("redis://redis:6379/0", description="Redis connection string")
    
    # OpenTelemetry configuration
    enable_telemetry: bool = Field(True, description="Enable OpenTelemetry telemetry")
    enable_distributed_tracing: bool = Field(True, description="Enable distributed tracing")
    otlp_endpoint: str = Field("0.0.0.0:4317", description="OpenTelemetry collector endpoint")
    opentelemetry_endpoint: str = Field("0.0.0.0:4317", description="OpenTelemetry collector endpoint (alias)")
    otlp_insecure: bool = Field(True, description="Whether to use insecure connection to OTLP endpoint")
    
    # Prometheus configuration
    enable_prometheus_metrics: bool = Field(True, description="Enable Prometheus metrics")
    prometheus_push_gateway: str = Field("http://prometheus:9091", description="Prometheus push gateway URL")
    metrics_push_interval: int = Field(15, description="Interval in seconds to push metrics")
    
    # API configuration
    api_prefix: str = Field("/api/v1", description="API prefix")
    
    # Rate limiting
    rate_limit_per_minute: int = Field(100, description="API rate limit per minute")
    
    # CORS configuration
    allowed_origins: Union[List[str], str] = Field(default=["*"], description="Allowed origins for CORS")

    @field_validator("allowed_origins", mode="before")
    @classmethod
    def assemble_allowed_origins(cls, v: Union[str, List[str]]) -> List[str]:
        if isinstance(v, str):
            return [item.strip() for item in v.split(',')]
        return v
    
    # Data retention configuration
    trace_retention_days: int = Field(30, description="Number of days to retain trace data")
    metrics_retention_days: int = Field(90, description="Number of days to retain metrics data")
    
    # Elasticsearch configuration (optional)
    elasticsearch_url: Optional[str] = Field(None, description="Elasticsearch connection string")
    logs_index: str = Field("service-logs", description="Elasticsearch logs index name")
    
    model_config = ConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra='ignore'
    )


@lru_cache()
def get_settings() -> Settings:
    """
    Get settings instance with caching.
    
    Returns:
        Settings: Settings instance
    """
    return Settings()


# Create settings instance for direct import
settings = get_settings()
