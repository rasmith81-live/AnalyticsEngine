"""
Messaging Client for Data Simulator Service.

Publishes simulation events to Redis pub/sub for consumption by:
- Database Service (persists data)
- Calculation Engine Service (real-time KPI calculation)
"""

import asyncio
import json
import logging
from datetime import datetime
from typing import Any, Dict, Optional

import redis.asyncio as redis

logger = logging.getLogger(__name__)


class SimulatorMessagingClient:
    """
    Messaging client for publishing simulation events.
    
    Publishes to channels that the Database Service and Calculation Engine
    subscribe to for data persistence and real-time KPI calculation.
    """
    
    # Event type constants
    EVENT_ENTITY_CREATED = "simulation.entity.created"
    EVENT_ENTITY_UPDATED = "simulation.entity.updated"
    EVENT_ENTITY_DEACTIVATED = "simulation.entity.deactivated"
    EVENT_SIMULATION_TICK = "simulation.tick"
    
    def __init__(
        self,
        redis_url: str,
        service_name: str = "data_simulator"
    ):
        self.redis_url = redis_url
        self.service_name = service_name
        self._redis: Optional[redis.Redis] = None
        self._connected = False
    
    async def connect(self) -> None:
        """Connect to Redis."""
        if self._connected:
            return
        
        try:
            self._redis = redis.Redis.from_url(
                self.redis_url,
                decode_responses=True,
                max_connections=10
            )
            await self._redis.ping()
            self._connected = True
            logger.info(f"SimulatorMessagingClient connected to Redis")
        except Exception as e:
            logger.error(f"Failed to connect to Redis: {e}")
            raise
    
    async def disconnect(self) -> None:
        """Disconnect from Redis."""
        if self._redis:
            await self._redis.close()
            self._connected = False
            logger.info("SimulatorMessagingClient disconnected")
    
    def is_connected(self) -> bool:
        return self._connected and self._redis is not None
    
    def _serialize_value(self, value: Any) -> Any:
        """Serialize a value for JSON."""
        if isinstance(value, datetime):
            return value.isoformat()
        return value
    
    def _serialize_dict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Serialize a dictionary for JSON."""
        return {k: self._serialize_value(v) for k, v in data.items()}
    
    async def publish_entity_event(
        self,
        entity_name: str,
        event_type: str,
        entity_id: str,
        attributes: Dict[str, Any],
        simulated_time: datetime,
        simulation_id: str
    ) -> bool:
        """
        Publish an entity event.
        
        Args:
            entity_name: Entity type (e.g., "customers")
            event_type: "create", "update", or "deactivate"
            entity_id: Entity ID
            attributes: Entity attributes
            simulated_time: Simulated timestamp
            simulation_id: Simulation ID
        """
        if not self.is_connected():
            return False
        
        try:
            # Map event type to channel
            if event_type == "create":
                channel = self.EVENT_ENTITY_CREATED
            elif event_type == "update":
                channel = self.EVENT_ENTITY_UPDATED
            else:
                channel = self.EVENT_ENTITY_DEACTIVATED
            
            message = {
                "source": self.service_name,
                "simulation_id": simulation_id,
                "entity_name": entity_name,
                "event_type": event_type,
                "entity_id": entity_id,
                "attributes": self._serialize_dict(attributes),
                "timestamp": simulated_time.isoformat(),
                "published_at": datetime.utcnow().isoformat(),
            }
            
            await self._redis.publish(channel, json.dumps(message))
            
            # Also publish to entity-specific channel for targeted subscriptions
            entity_channel = f"simulation.entity.{entity_name}.{event_type}"
            await self._redis.publish(entity_channel, json.dumps(message))
            
            return True
        except Exception as e:
            logger.error(f"Failed to publish entity event: {e}")
            return False
    
    async def publish_tick(
        self,
        simulation_id: str,
        tick_number: int,
        simulated_time: datetime,
        entity_counts: Dict[str, int],
        event_count: int
    ) -> bool:
        """Publish a simulation tick event."""
        if not self.is_connected():
            return False
        
        try:
            message = {
                "source": self.service_name,
                "simulation_id": simulation_id,
                "tick_number": tick_number,
                "simulated_time": simulated_time.isoformat(),
                "entity_counts": entity_counts,
                "event_count": event_count,
                "published_at": datetime.utcnow().isoformat(),
            }
            
            await self._redis.publish(self.EVENT_SIMULATION_TICK, json.dumps(message))
            return True
        except Exception as e:
            logger.error(f"Failed to publish tick: {e}")
            return False
