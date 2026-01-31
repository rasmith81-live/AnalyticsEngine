# =============================================================================
# Messaging Package for Multi-Agent Service
# Redis-based communication for L1-L2 service interaction
# =============================================================================
"""
Messaging components for event-driven communication.

Components:
- CommandConsumer: Consumes commands from Redis Streams
- ResponsePublisher: Publishes responses via Pub/Sub
"""

from .command_consumer import (
    CommandConsumer,
    CommandType,
    ResponseType,
    Command,
    get_command_consumer,
)

__all__ = [
    "CommandConsumer",
    "CommandType",
    "ResponseType",
    "Command",
    "get_command_consumer",
]
