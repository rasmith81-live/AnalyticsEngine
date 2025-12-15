"""Configuration for business metadata service.

Extends DatabaseServiceSettings to inherit database, Redis, and telemetry config.
"""

import sys
from pathlib import Path

# Add backend services to path
backend_services_path = Path(__file__).parent.parent.parent / "backend_services"
sys.path.insert(0, str(backend_services_path))

from database_service.app.config import DatabaseServiceSettings


class BusinessMetadataSettings(DatabaseServiceSettings):
    """Business metadata service settings.
    
    Inherits from DatabaseServiceSettings:
    - database_url
    - connection_pool_size
    - redis_host, redis_port
    - telemetry settings
    - etc.
    """
    
    # Service identification
    service_name: str = "business_metadata"
    service_port: int = 8023
    
    # Metadata-specific settings
    cache_ttl: int = 3600  # 1 hour default for metadata cache
    enable_versioning: bool = True  # Track version history
    enable_event_publishing: bool = True  # Publish metadata change events
    max_graph_depth: int = 5  # Max depth for relationship graph traversal
    
    # Event topics
    event_topic_prefix: str = "metadata"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance
settings = BusinessMetadataSettings()
