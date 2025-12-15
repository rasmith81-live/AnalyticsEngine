"""
Archival processor for handling TimescaleDB chunk archival operations.

This module contains the core logic for processing archival events, extracting data from
TimescaleDB chunks, writing to Azure Data Lake Storage, and sending confirmation events.
"""

import asyncio
import logging
import uuid
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Union

import pandas as pd
from azure.storage.blob.aio import BlobServiceClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from .lakehouse_client import LakehouseClient
from .config import settings
from .database import get_db_session
from .models import ArchivalConfirmation, ArchivalEvent, ArchivalStatus
from .monitoring import PerformanceTracker, get_monitor
from .redis_client import RedisClient
from .telemetry import trace_method, add_span_attributes, traced_span

# Configure logging
logger = logging.getLogger(__name__)


class ArchivalProcessor:
    """Processor for archival events."""
    
    def __init__(self, redis_client: RedisClient):
        """Initialize the archival processor.
        
        Args:
            redis_client: Redis client for publishing confirmation events.
        """
        self.redis_client = redis_client
        self.lakehouse_client = None
        self.monitor = get_monitor()
    
    @trace_method(name="ArchivalProcessor.initialize", kind="INTERNAL")
    async def initialize(self):
        """Initialize the archival processor."""
        # Initialize Lakehouse client
        try:
            self.lakehouse_client = LakehouseClient(
                storage_account=settings.azure_storage_account_name,
                container_name=settings.azure_storage_container,
                connection_string=settings.azure_storage_connection_string
            )
            
            # Add span attributes for storage context
            add_span_attributes({
                "storage.system": "azure_datalake",
                "storage.container": settings.azure_storage_container,
                "storage.operation": "initialize"
            })
            
            # Test connection (optional, or ensure container exists)
            # LakehouseClient handles container creation implicitly in write_data logic or we can add it here
            logger.info("Lakehouse client initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Lakehouse client: {str(e)}")
            raise
    
    @trace_method(name="ArchivalProcessor.process_archival_event", kind="CONSUMER")
    async def process_archival_event(self, event: ArchivalEvent):

        """Process an archival event.
        
        Args:
            event: The archival event to process.
        """
        # Add span attributes for event context
        add_span_attributes({
            "event_id": event.event_id,
            "table_name": event.table_name,
            "schema_name": event.schema_name,
            "chunk_id": event.chunk_id,
            "archival.operation": "process_event"
        })
        
        chunk_size_bytes = None
        error_message = None
        
        async with PerformanceTracker(f"archive_chunk_{event.chunk_id}") as tracker:
            try:
                logger.info(f"Processing archival event for chunk {event.chunk_id} of table {event.table_name}")
                
                # Extract data from the chunk
                chunk_data, chunk_size_bytes = await self._extract_chunk_data(event)
                
                # Write data to Azure Data Lake Storage
                await self._write_to_lakehouse(event, chunk_data)
                
                # Send confirmation event
                await self._send_confirmation(
                    event=event,
                    status=ArchivalStatus.SUCCESS,
                    message="Archival completed successfully"
                )
                
                logger.info(
                    f"Successfully archived chunk {event.chunk_id} of table {event.table_name} "
                    f"({chunk_size_bytes} bytes)"
                )
            except Exception as e:
                error_message = str(e)
                logger.error(
                    f"Failed to archive chunk {event.chunk_id} of table {event.table_name}: {error_message}"
                )
                
                # Send failure confirmation
                await self._send_confirmation(
                    event=event,
                    status=ArchivalStatus.FAILED,
                    message=f"Archival failed: {error_message}"
                )
            finally:
                # Record metrics
                await self.monitor.record_event(
                    event_id=event.event_id,
                    chunk_id=event.chunk_id,
                    table_name=event.table_name,
                    status=ArchivalStatus.SUCCESS if error_message is None else ArchivalStatus.FAILED,
                    processing_time_ms=tracker.duration_ms,
                    chunk_size_bytes=chunk_size_bytes,
                    error_message=error_message
                )
    
    @trace_method(name="ArchivalProcessor._extract_chunk_data", kind="CLIENT")
    async def _extract_chunk_data(self, event: ArchivalEvent) -> Tuple[pd.DataFrame, int]:
        """Extract data from a TimescaleDB chunk.
        
        Args:
            event: The archival event containing chunk information.
            
        Returns:
            Tuple containing:
                - DataFrame with the chunk data
                - Size of the chunk data in bytes
        """
        # Add span attributes for database operation
        add_span_attributes({
            "db.system": "timescaledb",
            "db.name": "timescaledb",
            "db.operation": "extract_chunk_data",
            "db.table": event.table_name,
            "db.schema": event.schema_name,
            "chunk_id": event.chunk_id,
            "time_range.start": str(event.chunk_start_time),
            "time_range.end": str(event.chunk_end_time)
        })
        
        async with get_db_session() as session:
            # Construct query to extract data from the chunk
            query = text(f"""
                SELECT * FROM {event.schema_name}.{event.table_name}
                WHERE {event.time_column} >= :start_time
                AND {event.time_column} < :end_time
            """)
            
            # Execute query
            result = await session.execute(
                query,
                {
                    "start_time": event.chunk_start_time,
                    "end_time": event.chunk_end_time
                }
            )
            
            # Convert to DataFrame
            rows = result.fetchall()
            if not rows:
                logger.warning(f"No data found in chunk {event.chunk_id}")
                return pd.DataFrame(), 0
            
            df = pd.DataFrame(rows)
            
            # Calculate approximate size
            chunk_size_bytes = df.memory_usage(deep=True).sum()
            
            logger.info(
                f"Extracted {len(df)} rows ({chunk_size_bytes} bytes) from chunk {event.chunk_id}"
            )
            
            return df, chunk_size_bytes
    
    @trace_method(name="ArchivalProcessor._write_to_lakehouse", kind="CLIENT")
    async def _write_to_lakehouse(self, event: ArchivalEvent, df: pd.DataFrame):
        """Write data to Azure Data Lake Storage.
        
        Args:
            event: The archival event.
            df: DataFrame containing the chunk data.
        """
        # Add span attributes for storage operation
        add_span_attributes({
            "storage.system": "azure_datalake",
            "storage.container": settings.azure_storage_container,
            "storage.operation": "write_to_lakehouse",
            "chunk_id": event.chunk_id,
            "table_name": event.table_name,
            "schema_name": event.schema_name,
            "row_count": len(df) if not df.empty else 0
        })
        
        if df.empty:
            logger.warning(f"No data to write for chunk {event.chunk_id}")
            return
        
        # Generate blob path with {year}/{month}/{day} structure
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        date_obj = event.chunk_start_time
        if isinstance(date_obj, str):
            date_obj = datetime.fromisoformat(date_obj)
            
        blob_path = (
            f"{event.schema_name}/{event.table_name}/"
            f"{date_obj.year}/{date_obj.month:02d}/{date_obj.day:02d}/"
            f"{event.chunk_id}_{timestamp}.parquet"
        )
        
        # Write data using Lakehouse Client
        success = await self.lakehouse_client.write_data(
            path=blob_path,
            data=df,
            format="parquet",
            correlation_id=event.event_id
        )
        
        if success:
            logger.info(
                f"Uploaded chunk {event.chunk_id} to {blob_path}"
            )
        else:
            raise Exception(f"Failed to write chunk {event.chunk_id} to lakehouse at {blob_path}")
    
    @trace_method(name="ArchivalProcessor._send_confirmation", kind="PRODUCER")
    async def _send_confirmation(
        self,
        event: ArchivalEvent,
        status: ArchivalStatus,
        message: str
    ):
        """Send a confirmation event.
        
        Args:
            event: The original archival event.
            status: The status of the archival operation.
            message: Additional message about the archival operation.
        """
        # Add span attributes for confirmation context
        add_span_attributes({
            "event_id": event.event_id,
            "chunk_id": event.chunk_id,
            "table_name": event.table_name,
            "schema_name": event.schema_name,
            "archival.status": status.value,
            "messaging.system": "redis",
            "messaging.destination": settings.redis_confirmation_topic,
            "messaging.destination_kind": "topic",
            "messaging.operation": "publish"
        })
        
        confirmation = ArchivalConfirmation(
            confirmation_id=str(uuid.uuid4()),
            event_id=event.event_id,
            chunk_id=event.chunk_id,
            table_name=event.table_name,
            schema_name=event.schema_name,
            status=status,
            message=message,
            processed_at=datetime.utcnow().isoformat()
        )
        
        # Publish confirmation event
        await self.redis_client.publish_event(
            topic=settings.redis_confirmation_topic,
            event_type="archival_confirmation",
            payload=confirmation.model_dump()
        )
        
        logger.info(
            f"Sent confirmation for chunk {event.chunk_id} with status {status.value}"
        )
