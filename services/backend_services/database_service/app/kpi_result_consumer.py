"""
KPI Result Consumer for Database Service.

Subscribes to calculated KPI results from the Calculation Engine Service,
persists them to TimescaleDB, and forwards to the Archival Service.
"""

import logging
import json
from typing import Dict, Any, Optional
from datetime import datetime

from .database_manager import DatabaseManager
from .messaging_client import MessagingClient
from .telemetry import trace_method, add_span_attributes

logger = logging.getLogger(__name__)


class KPIResultConsumer:
    """
    Consumer for calculated KPI results.
    
    Subscribes to Redis pub/sub channel for KPI calculation results and:
    1. Persists results to TimescaleDB (kpi_results table)
    2. Publishes to archival channel for long-term storage
    """
    
    CHANNEL_KPI_CALCULATED = "kpi.calculated"
    CHANNEL_ARCHIVE_KPI = "archive.kpi_results"
    
    def __init__(
        self,
        database_manager: DatabaseManager,
        messaging_client: MessagingClient
    ):
        self.database_manager = database_manager
        self.messaging_client = messaging_client
        self.running = False
    
    async def start(self):
        """Start consuming KPI results."""
        if self.running:
            return
        
        self.running = True
        logger.info("Starting KPI result consumer...")
        
        try:
            await self.messaging_client.subscribe(
                topic=self.CHANNEL_KPI_CALCULATED,
                callback=self._handle_kpi_result
            )
            logger.info(f"Subscribed to {self.CHANNEL_KPI_CALCULATED} channel")
        except Exception as e:
            logger.error(f"Failed to start KPI result consumer: {e}")
            self.running = False
            raise
    
    async def stop(self):
        """Stop consuming KPI results."""
        if not self.running:
            return
        
        self.running = False
        logger.info("Stopped KPI result consumer")
    
    @trace_method(name="kpi_result_consumer.handle_kpi_result")
    async def _handle_kpi_result(self, event_data: Dict[str, Any]):
        """
        Handle a calculated KPI result.
        
        1. Persist to kpi_results table in TimescaleDB
        2. Forward to archival service via messaging
        """
        try:
            kpi_code = event_data.get("kpi_code")
            entity_id = event_data.get("entity_id")
            period = event_data.get("period")
            value = event_data.get("value")
            unit = event_data.get("unit")
            timestamp = event_data.get("timestamp")
            calculated_at = event_data.get("calculated_at")
            metadata = event_data.get("metadata", {})
            
            add_span_attributes({
                "event_type": "kpi.calculated",
                "kpi_code": kpi_code,
                "entity_id": entity_id,
                "period": period,
            })
            
            # Build record for database
            record = {
                "kpi_code": kpi_code,
                "entity_id": entity_id,
                "period": period,
                "value": value,
                "unit": unit,
                "calculated_at": self._parse_timestamp(calculated_at),
                "timestamp": self._parse_timestamp(timestamp),
                "metadata": json.dumps(metadata) if metadata else None,
            }
            
            # Persist to TimescaleDB
            await self._persist_kpi_result(record)
            
            # Forward to archival service
            await self._forward_to_archival(event_data)
            
            logger.debug(f"Processed KPI result: {kpi_code}={value}")
            
        except Exception as e:
            logger.error(f"Failed to handle KPI result: {e}")
    
    async def _persist_kpi_result(self, record: Dict[str, Any]):
        """Persist KPI result to TimescaleDB."""
        try:
            await self.database_manager.insert_record("kpi_results", record)
        except Exception as e:
            logger.error(f"Failed to persist KPI result: {e}")
            raise
    
    async def _forward_to_archival(self, event_data: Dict[str, Any]):
        """Forward KPI result to archival service via messaging."""
        try:
            await self.messaging_client.publish_event(
                event_type=self.CHANNEL_ARCHIVE_KPI,
                payload={
                    "source": "database_service",
                    "data_type": "kpi_result",
                    "data": event_data,
                    "forwarded_at": datetime.utcnow().isoformat(),
                }
            )
            logger.debug(f"Forwarded KPI result to archival: {event_data.get('kpi_code')}")
        except Exception as e:
            logger.warning(f"Failed to forward KPI result to archival: {e}")
    
    def _parse_timestamp(self, ts: Optional[str]) -> Optional[datetime]:
        """Parse ISO timestamp string to datetime."""
        if not ts:
            return None
        try:
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            return None
