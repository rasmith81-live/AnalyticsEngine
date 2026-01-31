# =============================================================================
# Shared Events Package
# Event-Driven Service Communication Infrastructure
# =============================================================================
"""
Shared event schemas and utilities for Redis Streams/Pub/Sub communication.

This package provides:
- ServiceCommand/ServiceResponse schemas
- BaseEventClient for sending commands
- BaseCommandConsumer for processing commands
- Stream naming conventions and utilities
"""

from .schemas import (
    ServiceCommand,
    ServiceResponse,
    CommandType,
    ResponseType,
    StreamConfig,
)
from .redis_client import BaseEventClient
from .consumer import BaseCommandConsumer

__all__ = [
    # Schemas
    "ServiceCommand",
    "ServiceResponse",
    "CommandType",
    "ResponseType",
    "StreamConfig",
    # Client
    "BaseEventClient",
    # Consumer
    "BaseCommandConsumer",
]
