# =============================================================================
# Calculation Engine Messaging Package
# Redis Streams command processing for event-driven communication
# =============================================================================
"""
Messaging components for calculation_engine_service.

Components:
- CalculationCommandConsumer: Processes calculation commands from Redis Streams
"""

from .command_consumer import CalculationCommandConsumer

__all__ = ["CalculationCommandConsumer"]
