# =============================================================================
# Business Metadata Messaging Package
# Redis Streams command processing for event-driven communication
# =============================================================================
"""
Messaging components for business_metadata service.

Components:
- MetadataCommandConsumer: Processes commands from Redis Streams
"""

from .command_consumer import MetadataCommandConsumer

__all__ = ["MetadataCommandConsumer"]
