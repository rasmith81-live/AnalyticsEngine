"""Configuration for Process Simulation Service."""

from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Service Info
    service_name: str = "process_simulation_service"
    service_version: str = "1.0.0"
    debug: bool = False
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8027
    
    # Database Service
    database_service_url: str = "http://database_service:8000"
    database_service_timeout: int = 30
    database_service_retries: int = 3
    
    # Messaging Service
    messaging_service_url: str = "http://messaging_service:8001"
    messaging_service_timeout: int = 30
    messaging_service_retries: int = 3
    subscribe_to_events: bool = True
    
    # Business Metadata Service
    business_metadata_url: str = "http://business_metadata:8020"
    
    # Machine Learning Service (for KPI predictions)
    ml_service_url: str = "http://machine_learning_service:8030"
    
    # Simulation Settings
    default_replications: int = 10
    max_replications: int = 100
    default_simulation_hours: int = 168  # 1 week
    max_simulation_hours: int = 8760  # 1 year
    default_warm_up_hours: int = 24
    
    # Observability
    enable_distributed_tracing: bool = True
    otlp_endpoint: str = "http://observability_service:4317"
    enable_prometheus_metrics: bool = True
    observability_service_url: str = "http://observability_service:8080"
    prometheus_push_gateway: str = "http://prometheus-pushgateway:9091"
    metrics_push_interval: int = 30
    metrics_export_job_name: str = "process_simulation_service"
    
    # CORS
    cors_origins: list = ["*"]
    
    class Config:
        env_prefix = "PROCESS_SIM_"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
