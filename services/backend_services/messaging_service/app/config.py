"""
Configuration settings for the Messaging Service.
"""

import os
from functools import lru_cache
from typing import List, Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    # Redis Configuration
    redis_url: str = Field(
        default="redis://localhost:6379/0",
        env="REDIS_URL",
        description="Redis connection URL"
    )
    redis_max_connections: int = Field(
        default=20,
        env="REDIS_MAX_CONNECTIONS",
        description="Maximum Redis connections in pool"
    )
    redis_retry_on_timeout: bool = Field(
        default=True,
        env="REDIS_RETRY_ON_TIMEOUT",
        description="Retry Redis operations on timeout"
    )
    redis_socket_keepalive: bool = Field(
        default=True,
        env="REDIS_SOCKET_KEEPALIVE",
        description="Enable Redis socket keepalive"
    )
    redis_socket_keepalive_options: dict = Field(
        default_factory=dict,
        env="REDIS_SOCKET_KEEPALIVE_OPTIONS",
        description="Redis socket keepalive options"
    )
    
    # Service Configuration
    service_name: str = Field(
        default="messaging_service",
        env="SERVICE_NAME",
        description="Name of this service"
    )
    version: str = Field(
        default="1.0.0",
        env="SERVICE_VERSION",
        description="Service version"
    )
    environment: str = Field(
        default="development",
        env="DEPLOYMENT_ENVIRONMENT",
        description="Deployment environment (development, staging, production)"
    )
    service_host: str = Field(
        default="0.0.0.0",
        env="SERVICE_HOST",
        description="Service host address"
    )
    service_port: int = Field(
        default=8001,
        env="SERVICE_PORT",
        description="Service port"
    )
    
    # Message Configuration
    default_message_ttl: int = Field(
        default=3600,
        env="DEFAULT_MESSAGE_TTL",
        description="Default message TTL in seconds"
    )
    max_message_size: int = Field(
        default=1048576,  # 1MB
        env="MAX_MESSAGE_SIZE",
        description="Maximum message size in bytes"
    )
    enable_message_compression: bool = Field(
        default=True,
        env="ENABLE_MESSAGE_COMPRESSION",
        description="Enable message compression"
    )
    
    # Channel Configuration
    default_channel_prefix: str = Field(
        default="app",
        env="DEFAULT_CHANNEL_PREFIX",
        description="Default channel prefix"
    )
    max_channels_per_service: int = Field(
        default=100,
        env="MAX_CHANNELS_PER_SERVICE",
        description="Maximum channels per service"
    )
    
    # Subscription Configuration
    subscription_heartbeat_interval: int = Field(
        default=30,
        env="SUBSCRIPTION_HEARTBEAT_INTERVAL",
        description="Subscription heartbeat interval in seconds"
    )
    subscription_timeout: int = Field(
        default=300,
        env="SUBSCRIPTION_TIMEOUT",
        description="Subscription timeout in seconds"
    )
    max_subscriptions_per_service: int = Field(
        default=50,
        env="MAX_SUBSCRIPTIONS_PER_SERVICE",
        description="Maximum subscriptions per service"
    )
    
    # Event Processing Configuration
    enable_event_persistence: bool = Field(
        default=True,
        env="ENABLE_EVENT_PERSISTENCE",
        description="Enable event persistence"
    )
    event_batch_size: int = Field(
        default=100,
        env="EVENT_BATCH_SIZE",
        description="Event processing batch size"
    )
    event_processing_timeout: int = Field(
        default=30,
        env="EVENT_PROCESSING_TIMEOUT",
        description="Event processing timeout in seconds"
    )
    
    # Dead Letter Queue Configuration
    enable_dlq: bool = Field(
        default=True,
        env="ENABLE_DLQ",
        description="Enable dead letter queue"
    )
    dlq_max_retries: int = Field(
        default=3,
        env="DLQ_MAX_RETRIES",
        description="Maximum retries before sending to DLQ"
    )
    dlq_retry_delay: int = Field(
        default=60,
        env="DLQ_RETRY_DELAY",
        description="Retry delay in seconds"
    )
    
    # Monitoring Configuration
    enable_metrics: bool = Field(
        default=True,
        env="ENABLE_METRICS",
        description="Enable metrics collection"
    )
    metrics_retention_days: int = Field(
        default=7,
        env="METRICS_RETENTION_DAYS",
        description="Metrics retention in days"
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
    
    # Health Check Configuration
    health_check_interval: int = Field(
        default=30,
        env="HEALTH_CHECK_INTERVAL",
        description="Health check interval in seconds"
    )
    health_check_timeout: int = Field(
        default=5,
        env="HEALTH_CHECK_TIMEOUT",
        description="Health check timeout in seconds"
    )
    
    # Prometheus Metrics Configuration
    observability_service_url: Optional[str] = Field(
        default="http://observability_service:8000",
        env="OBSERVABILITY_SERVICE_URL",
        description="Observability service URL for metrics export (leave empty to disable)"
    )
    enable_prometheus_metrics: bool = Field(
        default=True,
        env="ENABLE_PROMETHEUS_METRICS",
        description="Enable Prometheus metrics collection"
    )
    prometheus_push_gateway: Optional[str] = Field(
        default="http://prometheus-pushgateway:9091",
        env="PROMETHEUS_PUSH_GATEWAY",
        description="Prometheus push gateway URL (leave empty to disable)"
    )
    metrics_push_interval: int = Field(
        default=15,
        env="METRICS_PUSH_INTERVAL",
        description="Metrics push interval in seconds"
    )
    metrics_export_job_name: str = Field(
        default="messaging_service",
        env="METRICS_EXPORT_JOB_NAME",
        description="Job name for metrics export"
    )
    metrics_export_timeout: int = Field(
        default=2,
        env="METRICS_EXPORT_TIMEOUT",
        description="Timeout in seconds for metrics export operations"
    )
    
    # Distributed Tracing Configuration
    enable_distributed_tracing: bool = Field(
        default=True,
        env="ENABLE_DISTRIBUTED_TRACING",
        description="Enable distributed tracing"
    )
    otlp_endpoint: Optional[str] = Field(
        default="https://observability_service:4317",
        env="OTEL_EXPORTER_OTLP_ENDPOINT",
        description="OpenTelemetry collector endpoint for trace export (leave empty to disable)"
    )
    trace_sample_rate: float = Field(
        default=1.0,
        env="TRACE_SAMPLE_RATE",
        description="Sampling rate for traces (0.0 to 1.0)"
    )
    propagate_correlation_id: bool = Field(
        default=True,
        env="PROPAGATE_CORRELATION_ID",
        description="Propagate correlation ID across service boundaries"
    )
    tracing_export_timeout: int = Field(
        default=2,
        env="TRACING_EXPORT_TIMEOUT",
        description="Timeout in seconds for trace export operations"
    )
    tracing_max_queue_size: int = Field(
        default=1000,
        env="TRACING_MAX_QUEUE_SIZE",
        description="Maximum queue size for trace export batch processor"
    )
    tracing_max_export_batch_size: int = Field(
        default=100,
        env="TRACING_MAX_EXPORT_BATCH_SIZE",
        description="Maximum batch size for trace export"
    )
    tracing_schedule_delay_ms: int = Field(
        default=5000,
        env="TRACING_SCHEDULE_DELAY_MS",
        description="Schedule delay in milliseconds for trace export batch processor"
    )
    otlp_max_export_batch_size: int = Field(
        default=50,
        env="OTLP_MAX_EXPORT_BATCH_SIZE",
        description="Maximum batch size for OTLP exporter"
    )
    otlp_max_retry_attempts: int = Field(
        default=3,
        env="OTLP_MAX_RETRY_ATTEMPTS",
        description="Maximum retry attempts for OTLP exporter"
    )
    otlp_retry_delay_seconds: float = Field(
        default=5.0,
        env="OTLP_RETRY_DELAY_SECONDS",
        description="Delay between retry attempts for OTLP exporter in seconds"
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
