"""
Simulation Data Consumer for Database Service.

Subscribes to simulation entity events from the Data Simulator Service
and persists them to TimescaleDB.
"""

import logging
import json
from typing import Dict, Any, Optional
from datetime import datetime

from .database_manager import DatabaseManager
from .messaging_client import MessagingClient
from .telemetry import trace_method, add_span_attributes

logger = logging.getLogger(__name__)


class SimulationDataConsumer:
    """
    Consumer for simulation entity events.
    
    Subscribes to Redis pub/sub channels for simulation events and
    persists entity data to TimescaleDB.
    """
    
    # Event channels to subscribe to
    CHANNEL_ENTITY_CREATED = "simulation.entity.created"
    CHANNEL_ENTITY_UPDATED = "simulation.entity.updated"
    CHANNEL_ENTITY_DEACTIVATED = "simulation.entity.deactivated"
    
    def __init__(
        self,
        database_manager: DatabaseManager,
        messaging_client: MessagingClient
    ):
        self.database_manager = database_manager
        self.messaging_client = messaging_client
        self.running = False
    
    async def start(self):
        """Start consuming simulation events."""
        if self.running:
            return
        
        self.running = True
        logger.info("Starting simulation data consumer...")
        
        try:
            # Subscribe to entity events
            await self.messaging_client.subscribe(
                topic=self.CHANNEL_ENTITY_CREATED,
                callback=self._handle_entity_created
            )
            await self.messaging_client.subscribe(
                topic=self.CHANNEL_ENTITY_UPDATED,
                callback=self._handle_entity_updated
            )
            await self.messaging_client.subscribe(
                topic=self.CHANNEL_ENTITY_DEACTIVATED,
                callback=self._handle_entity_deactivated
            )
            
            logger.info("Subscribed to simulation entity event channels")
        except Exception as e:
            logger.error(f"Failed to start simulation data consumer: {e}")
            self.running = False
            raise
    
    async def stop(self):
        """Stop consuming simulation events."""
        if not self.running:
            return
        
        self.running = False
        logger.info("Stopped simulation data consumer")
    
    @trace_method(name="simulation_consumer.handle_entity_created")
    async def _handle_entity_created(self, event_data: Dict[str, Any]):
        """Handle entity created event."""
        try:
            entity_name = event_data.get("entity_name")
            entity_id = event_data.get("entity_id")
            attributes = event_data.get("attributes", {})
            timestamp = event_data.get("timestamp")
            simulation_id = event_data.get("simulation_id")
            
            add_span_attributes({
                "event_type": "simulation.entity.created",
                "entity_name": entity_name,
                "entity_id": entity_id,
                "simulation_id": simulation_id,
            })
            
            # Build record for database
            record = {
                "id": entity_id,
                "simulation_id": simulation_id,
                **attributes,
            }
            
            # Parse timestamp if string
            if isinstance(timestamp, str):
                record["created_at"] = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
            
            # Insert into database
            table_name = self._get_table_name(entity_name)
            await self.database_manager.insert_record(table_name, record)
            
            logger.debug(f"Persisted entity created: {entity_name}/{entity_id}")
            
        except Exception as e:
            logger.error(f"Failed to handle entity created event: {e}")
    
    @trace_method(name="simulation_consumer.handle_entity_updated")
    async def _handle_entity_updated(self, event_data: Dict[str, Any]):
        """Handle entity updated event."""
        try:
            entity_name = event_data.get("entity_name")
            entity_id = event_data.get("entity_id")
            attributes = event_data.get("attributes", {})
            simulation_id = event_data.get("simulation_id")
            
            add_span_attributes({
                "event_type": "simulation.entity.updated",
                "entity_name": entity_name,
                "entity_id": entity_id,
            })
            
            # Update record in database
            table_name = self._get_table_name(entity_name)
            await self.database_manager.update_record(table_name, entity_id, attributes)
            
            logger.debug(f"Persisted entity update: {entity_name}/{entity_id}")
            
        except Exception as e:
            logger.error(f"Failed to handle entity updated event: {e}")
    
    @trace_method(name="simulation_consumer.handle_entity_deactivated")
    async def _handle_entity_deactivated(self, event_data: Dict[str, Any]):
        """Handle entity deactivated event."""
        try:
            entity_name = event_data.get("entity_name")
            entity_id = event_data.get("entity_id")
            attributes = event_data.get("attributes", {})
            timestamp = event_data.get("timestamp")
            
            add_span_attributes({
                "event_type": "simulation.entity.deactivated",
                "entity_name": entity_name,
                "entity_id": entity_id,
            })
            
            # Update with inactive_date
            update_data = {"inactive_date": timestamp}
            if "inactive_date" in attributes:
                update_data["inactive_date"] = attributes["inactive_date"]
            
            table_name = self._get_table_name(entity_name)
            await self.database_manager.update_record(table_name, entity_id, update_data)
            
            logger.debug(f"Persisted entity deactivation: {entity_name}/{entity_id}")
            
        except Exception as e:
            logger.error(f"Failed to handle entity deactivated event: {e}")
    
    def _get_table_name(self, entity_name: str) -> str:
        """Get table name from entity name."""
        # Convert entity name to table name (lowercase, underscores)
        return entity_name.lower().replace(" ", "_").replace("-", "_")
