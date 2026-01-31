# =============================================================================
# Connector Service Messaging Package
# Redis Streams command processing for event-driven communication
# =============================================================================
"""
Messaging components for connector_service.

Components:
- ConnectorCommandConsumer: Processes data fetch commands from Redis Streams
"""

from .command_consumer import ConnectorCommandConsumer

__all__ = ["ConnectorCommandConsumer"]
