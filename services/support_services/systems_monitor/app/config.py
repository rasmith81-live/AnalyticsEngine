"""
Configuration settings for Systems Monitor.
"""

import os
from functools import lru_cache
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings for Systems Monitor."""
    
    # Service Configuration
    service_name: str = Field(
        default="systems_monitor",
        env="SERVICE_NAME",
        description="Name of this service"
    )
    service_host: str = Field(
        default="0.0.0.0",
        env="SERVICE_HOST",
        description="Service host address"
    )
    service_port: int = Field(
        default=8002,
        env="SERVICE_PORT",
        description="Service port"
    )
    
    # Database Service Configuration
    database_service_url: str = Field(
        default="http://database_service:8000",
        env="DATABASE_SERVICE_URL",
        description="URL for the backend_services/database_service"
    )
    database_service_timeout: int = Field(
        default=30,
        env="DATABASE_SERVICE_TIMEOUT",
        description="Database service request timeout in seconds"
    )
    database_service_retries: int = Field(
        default=3,
        env="DATABASE_SERVICE_RETRIES",
        description="Database service request retries"
    )
    
    # Messaging Service Configuration
    messaging_service_url: str = Field(
        default="http://messaging_service:8001",
        env="MESSAGING_SERVICE_URL",
        description="URL for the backend_services/messaging_service"
    )
    messaging_service_timeout: int = Field(
        default=30,
        env="MESSAGING_SERVICE_TIMEOUT",
        description="Messaging service request timeout in seconds"
    )
    messaging_service_retries: int = Field(
        default=3,
        env="MESSAGING_SERVICE_RETRIES",
        description="Messaging service request retries"
    )
    
    # Business Logic Configuration
    enable_real_time_processing: bool = Field(
        default=True,
        env="ENABLE_REAL_TIME_PROCESSING",
        description="Enable real-time data processing"
    )
    batch_processing_size: int = Field(
        default=100,
        env="BATCH_PROCESSING_SIZE",
        description="Batch processing size"
    )
    processing_interval_seconds: int = Field(
        default=60,
        env="PROCESSING_INTERVAL_SECONDS",
        description="Processing interval in seconds"
    )
    
    # Event Configuration
    publish_events: bool = Field(
        default=True,
        env="PUBLISH_EVENTS",
        description="Enable event publishing"
    )
    subscribe_to_events: bool = Field(
        default=True,
        env="SUBSCRIBE_TO_EVENTS",
        description="Enable event subscription"
    )
    event_callback_url: str = Field(
        default="http://systems_monitor:8002/events/callback",
        env="EVENT_CALLBACK_URL",
        description="Callback URL for event subscriptions"
    )
    
    # Cache Configuration
    enable_caching: bool = Field(
        default=True,
        env="ENABLE_CACHING",
        description="Enable response caching"
    )
    cache_ttl_seconds: int = Field(
        default=300,
        env="CACHE_TTL_SECONDS",
        description="Cache TTL in seconds"
    )
    
    # Health Check Configuration
    health_check_interval: int = Field(
        default=30,
        env="HEALTH_CHECK_INTERVAL",
        description="Health check interval in seconds"
    )
    dependency_health_timeout: int = Field(
        default=5,
        env="DEPENDENCY_HEALTH_TIMEOUT",
        description="Dependency health check timeout in seconds"
    )
    
    # CORS Configuration
    cors_origins: List[str] = Field(
        default=["*"],
        env="CORS_ORIGINS",
        description="CORS allowed origins"
    )
    cors_allow_credentials: bool = Field(
        default=True,
        env="CORS_ALLOW_CREDENTIALS",
        description="CORS allow credentials"
    )
    cors_allow_methods: List[str] = Field(
        default=["*"],
        env="CORS_ALLOW_METHODS",
        description="CORS allowed methods"
    )
    cors_allow_headers: List[str] = Field(
        default=["*"],
        env="CORS_ALLOW_HEADERS",
        description="CORS allowed headers"
    )
    
    # Logging Configuration
    log_level: str = Field(
        default="INFO",
        env="LOG_LEVEL",
        description="Logging level"
    )
    log_format: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        env="LOG_FORMAT",
        description="Logging format"
    )
    enable_json_logging: bool = Field(
        default=False,
        env="ENABLE_JSON_LOGGING",
        description="Enable JSON logging"
    )
    
    # Security Configuration
    enable_authentication: bool = Field(
        default=False,
        env="ENABLE_AUTHENTICATION",
        description="Enable authentication"
    )
    jwt_secret_key: str = Field(
        default="your-secret-key-change-in-production",
        env="JWT_SECRET_KEY",
        description="JWT secret key"
    )
    jwt_algorithm: str = Field(
        default="HS256",
        env="JWT_ALGORITHM",
        description="JWT algorithm"
    )
    jwt_expire_minutes: int = Field(
        default=30,
        env="JWT_EXPIRE_MINUTES",
        description="JWT expiration time in minutes"
    )
    
    # Metrics Configuration
    observability_service_url: str = Field(
        default="http://observability_service:8000",
        env="OBSERVABILITY_SERVICE_URL",
        description="Observability service URL for metrics export"
    )
    enable_prometheus_metrics: bool = Field(
        default=True,
        env="ENABLE_PROMETHEUS_METRICS",
        description="Enable Prometheus metrics collection"
    )
    prometheus_push_gateway: str = Field(
        default="http://prometheus-pushgateway:9091",
        env="PROMETHEUS_PUSH_GATEWAY",
        description="Prometheus push gateway URL"
    )
    metrics_push_interval: int = Field(
        default=15,
        env="METRICS_PUSH_INTERVAL",
        description="Metrics push interval in seconds"
    )
    metrics_export_job_name: str = Field(
        default="systems_monitor",
        env="METRICS_EXPORT_JOB_NAME",
        description="Job name for metrics export"
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
    trace_sample_rate: float = Field(
        default=1.0,
        env="TRACE_SAMPLE_RATE",
        description="Trace sampling rate (0.0 to 1.0)"
    )
    propagate_correlation_id: bool = Field(
        default=True,
        env="PROPAGATE_CORRELATION_ID",
        description="Propagate correlation ID across service boundaries"
    )
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
