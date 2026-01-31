# =============================================================================
# Service Clients Package for Multi-Agent Service
# Redis-based clients for event-driven communication with business services
# =============================================================================
"""
Service clients for multi_agent_service to communicate with business services.

All clients use Redis Streams for commands and Pub/Sub for responses.
"""

from .metadata_client import MetadataEventClient, get_metadata_client
from .calculation_client import CalculationEventClient, get_calculation_client
from .connector_client import ConnectorEventClient, get_connector_client

__all__ = [
    "MetadataEventClient",
    "get_metadata_client",
    "CalculationEventClient",
    "get_calculation_client",
    "ConnectorEventClient",
    "get_connector_client",
]
