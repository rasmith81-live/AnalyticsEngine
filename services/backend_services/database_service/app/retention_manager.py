"""
Data Retention Manager for TimescaleDB.

This module handles data lifecycle policies including:
1. Identifying data for archival based on age
2. Publishing archival events via Redis messaging service
3. Managing TimescaleDB retention policies
4. Executing chunk dropping after successful archival confirmation
"""
import asyncio
import json
import logging
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Any, Optional

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine

from app.config import get_settings
from app.models import ArchivalEvent, ArchivalStatus, RetentionPolicy, ArchivalConfirmation
from app.messaging_client import MessagingClient
from app.telemetry import trace_method, add_span_attributes, create_span

logger = logging.getLogger(__name__)

class RetentionManager:
    """Manages data retention policies for TimescaleDB hypertables."""
    
    def __init__(self, engine: AsyncEngine, messaging_client: MessagingClient):
        """Initialize the retention manager.
        
        Args:
            engine: AsyncEngine for database connections
            messaging_client: Client for Redis messaging service
        """
        self.engine = engine
        self.messaging_client = messaging_client
        self.retention_period_days = get_settings().retention_period_days or 730  # Default 2 years
        self._running = False
        self._task = None
        self._archival_confirmations = {}
    
    async def start(self):
        """Start the retention manager background task."""
        if self._running:
            return
        
        # Subscribe to archival confirmation events
        await self.messaging_client.subscribe(
            topic="archival.confirmations",
            callback=self._handle_archival_confirmation
        )
        
        self._running = True
        self._task = asyncio.create_task(self._run_retention_cycle())
        logger.info("RetentionManager started")
    
    async def stop(self):
        """Stop the retention manager background task."""
        if not self._running:
            return
        
        self._running = False
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
        
        # Unsubscribe from archival confirmation events
        await self.messaging_client.unsubscribe(
            topic="archival.confirmations"
        )
        
        logger.info("RetentionManager stopped")
    
    @trace_method(name="retention_manager._run_retention_cycle")
    async def _run_retention_cycle(self):
        """Run the retention cycle periodically."""
        while self._running:
            start_time = datetime.utcnow()
            
            # Add span attributes for context
            add_span_attributes({
                "timestamp.start": start_time.isoformat()
            })
            
            try:
                await self._process_retention_policies()
                
                # Add span attributes for success
                end_time = datetime.utcnow()
                add_span_attributes({
                    "timestamp.end": end_time.isoformat(),
                    "duration_ms": (end_time - start_time).total_seconds() * 1000,
                    "success": True
                })
            except Exception as e:
                # Add span attributes for error
                end_time = datetime.utcnow()
                add_span_attributes({
                    "timestamp.end": end_time.isoformat(),
                    "duration_ms": (end_time - start_time).total_seconds() * 1000,
                    "error.type": e.__class__.__name__,
                    "error.message": str(e),
                    "success": False
                })
                logger.error(f"Error in retention cycle: {e}", exc_info=True)
            
            # Run once per day
            await asyncio.sleep(86400)
    
    @trace_method(name="retention_manager._process_retention_policies")
    async def _process_retention_policies(self):
        """Process all retention policies."""
        start_time = datetime.utcnow()
        correlation_id = str(uuid.uuid4())
        
        # Add span attributes for context
        add_span_attributes({
            "correlation_id": correlation_id,
            "timestamp.start": start_time.isoformat(),
            "retention_period_days": self.retention_period_days
        })
        
        try:
            # Get all hypertables with retention policies
            hypertables = await self._get_hypertables_with_retention()
            
            tables_processed = 0
            tables_with_chunks = 0
            total_chunks = 0
            
            for table_name, policy in hypertables:
                try:
                    # Skip if policy is not enabled
                    if not policy.enabled:
                        continue
                    
                    tables_processed += 1
                    
                    # Identify chunks for archival
                    chunks = await self._identify_chunks_for_archival(table_name)
                    
                    if chunks:
                        # Publish archival event
                        event_id = await self._publish_archival_event(table_name, chunks)
                        
                        # Store for confirmation tracking
                        self._archival_confirmations[event_id] = {
                            'table_name': table_name,
                            'chunks': chunks,
                            'timestamp': datetime.utcnow()
                        }
                        
                        tables_with_chunks += 1
                        total_chunks += len(chunks)
                        logger.info(f"Published archival event {event_id} for {table_name} with {len(chunks)} chunks")
                except Exception as e:
                    logger.error(f"Error processing retention for {table_name}: {e}", exc_info=True)
            
            # Add span attributes for response
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "tables_processed": tables_processed,
                "tables_with_chunks": tables_with_chunks,
                "total_chunks": total_chunks,
                "success": True
            })
        except Exception as e:
            # Add span attributes for error
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "error.type": e.__class__.__name__,
                "error.message": str(e),
                "success": False
            })
            logger.error(f"Error processing retention policies: {e}", exc_info=True)
    
    @trace_method(name="retention_manager._get_hypertables_with_retention")
    async def _get_hypertables_with_retention(self) -> List[Tuple[str, RetentionPolicy]]:
        """Get all hypertables with retention policies.
        
        Returns:
            List of (table_name, retention_policy) tuples
        """
        start_time = datetime.utcnow()
        
        # Add span attributes for context
        add_span_attributes({
            "timestamp.start": start_time.isoformat(),
            "retention_period_days": self.retention_period_days
        })
        
        try:
            async with self.engine.begin() as conn:
                # Query TimescaleDB catalog for hypertables
                result = await conn.execute(text("""
                    SELECT 
                        table_name, 
                        jsonb_build_object(
                            'enabled', true,
                            'retention_period_days', 
                            CASE 
                                WHEN EXISTS (
                                    SELECT 1 
                                    FROM _timescaledb_config.bgw_job 
                                    WHERE proc_name = 'policy_retention' 
                                    AND hypertable_id = h.id
                                ) 
                                THEN (
                                    SELECT EXTRACT(EPOCH FROM (config->>'drop_after')::interval) / 86400
                                    FROM _timescaledb_config.bgw_job
                                    WHERE proc_name = 'policy_retention' 
                                    AND hypertable_id = h.id
                                )
                                ELSE :default_retention
                            END
                        ) as policy
                    FROM _timescaledb_catalog.hypertable h
                """), {"default_retention": int(self.retention_period_days)})
                
                hypertables = []
                for row in result:
                    policy = RetentionPolicy(**row.policy)
                    hypertables.append((row.table_name, policy))
                
                # Add span attributes for success
                end_time = datetime.utcnow()
                add_span_attributes({
                    "timestamp.end": end_time.isoformat(),
                    "duration_ms": (end_time - start_time).total_seconds() * 1000,
                    "hypertables_found": len(hypertables),
                    "success": True
                })
                
                return hypertables
        except Exception as e:
            # Add span attributes for error
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "error.type": e.__class__.__name__,
                "error.message": str(e),
                "success": False
            })
            raise
    
    @trace_method(name="retention_manager._identify_chunks_for_archival")
    async def _identify_chunks_for_archival(self, table_name: str, retention_period_days: int) -> List[Dict[str, Any]]:
        """Identify chunks that are ready for archival.
        
        Args:
            table_name: Name of the hypertable
            
        Returns:
            List of chunk metadata dictionaries
        """
        start_time = datetime.utcnow()
        
        # Add span attributes for context
        add_span_attributes({
            "timestamp.start": start_time.isoformat(),
            "table_name": table_name,
            "retention_period_days": self.retention_period_days
        })
        
        try:
            cutoff_date = datetime.utcnow() - timedelta(days=retention_period_days)
            
            async with self.engine.begin() as conn:
                # Query for chunks older than retention period
                result = await conn.execute(text("""
                    SELECT chunk_name, 
                           range_start,
                           range_end
                    FROM timescaledb_information.chunks
                    WHERE hypertable_name = :table_name
                    AND range_end < :cutoff_date
                    ORDER BY range_end ASC
                """), {"table_name": table_name, "cutoff_date": cutoff_date})
                
                chunks = []
                for row in result:
                    chunks.append({
                        "chunk_name": row.chunk_name,
                        "range_start": row.range_start.isoformat() if row.range_start else None,
                        "range_end": row.range_end.isoformat() if row.range_end else None
                    })
                
                # Add span attributes for response
                end_time = datetime.utcnow()
                add_span_attributes({
                    "timestamp.end": end_time.isoformat(),
                    "duration_ms": (end_time - start_time).total_seconds() * 1000,
                    "chunks_found": len(chunks),
                    "success": True
                })
                
                return chunks
        except Exception as e:
            # Add span attributes for error
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "error.type": e.__class__.__name__,
                "error.message": str(e),
                "success": False
            })
            raise
    
    @trace_method(name="retention_manager._publish_archival_event")
    async def _publish_archival_event(self, table_name: str, chunks: List[Dict[str, Any]]) -> str:
        """Publish an archival event to the messaging service.
        
        Args:
            table_name: Name of the hypertable
            chunks: List of chunk metadata
            
        Returns:
            Event ID for tracking
        """
        start_time = datetime.utcnow()
        event_id = str(uuid.uuid4())
        
        # Add span attributes for context
        add_span_attributes({
            "timestamp.start": start_time.isoformat(),
            "table_name": table_name,
            "chunks_count": len(chunks),
            "event_id": event_id
        })
        
        try:
            # Create the archival event
            event = ArchivalEvent(
                event_id=event_id,
                table_name=table_name,
                chunks=chunks,
                status=ArchivalStatus.PENDING,
                created_at=datetime.utcnow()
            )
            
            # Publish to the archival events topic
            await self.messaging_client.publish_event(
                topic="archival.events",
                event_type="data.archival.requested",
                payload=event.model_dump(),
                service_name="database_service"
            )
            
            # Add span attributes for response
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "event_topic": "archival.events",
                "success": True
            })
            
            logger.info(f"Published archival event {event_id} for {table_name} with {len(chunks)} chunks")
            return event_id
        except Exception as e:
            # Add span attributes for error
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "error.type": e.__class__.__name__,
                "error.message": str(e),
                "success": False
            })
            raise
    
    @trace_method(name="retention_manager._handle_archival_confirmation")
    async def _handle_archival_confirmation(self, message: Dict[str, Any]):
        """Handle archival confirmation messages from the Archival Service.
        
        Args:
            message: The confirmation message
        """
        start_time = datetime.utcnow()
        event_id = message.get('event_id')
        
        # Add span attributes for context
        add_span_attributes({
            "timestamp.start": start_time.isoformat(),
            "event_id": event_id,
            "confirmation_status": message.get('status'),
            "confirmation_timestamp": message.get('timestamp')
        })
        
        try:
            # Parse the confirmation
            confirmation = ArchivalConfirmation(**message)
            
            # Check if we have this event in our tracking
            if event_id not in self._archival_confirmations:
                logger.warning(f"Received confirmation for unknown event: {event_id}")
                
                # Add span attributes for unknown event
                end_time = datetime.utcnow()
                add_span_attributes({
                    "timestamp.end": end_time.isoformat(),
                    "duration_ms": (end_time - start_time).total_seconds() * 1000,
                    "success": False,
                    "error.type": "UnknownEventID",
                    "error.message": f"Unknown event ID: {event_id}"
                })
                
                return
            
            # Get the original archival request
            event_data = self._archival_confirmations[event_id]
            table_name = event_data['table_name']
            chunks = event_data['chunks']
            
            # Add table info to span
            add_span_attributes({
                "table_name": table_name,
                "chunks_count": len(chunks)
            })
            
            # If archival was successful, drop the chunks
            if confirmation.status == ArchivalStatus.COMPLETED:
                await self._drop_archived_chunks(table_name, chunks)
            
            # Clean up tracking
            del self._archival_confirmations[event_id]
            
            # Add span attributes for response
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "success": True
            })
        except Exception as e:
            # Add span attributes for error
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "error.type": e.__class__.__name__,
                "error.message": str(e),
                "success": False
            })
            logger.error(f"Error handling archival confirmation: {e}", exc_info=True)
            raise
    
    @trace_method(name="retention_manager._drop_archived_chunks")
    async def _drop_archived_chunks(self, table_name: str, chunks: List[Dict[str, Any]]):
        """Drop chunks that have been successfully archived.
        
        Args:
            table_name: Name of the hypertable
            chunks: List of chunk metadata
        """
        start_time = datetime.utcnow()
        
        # Add span attributes for context
        add_span_attributes({
            "timestamp.start": start_time.isoformat(),
            "table_name": table_name,
            "chunks_count": len(chunks)
        })
        
        try:
            chunk_ids = [chunk["chunk_name"] for chunk in chunks]
            
            async with self.engine.begin() as conn:
                for chunk_id in chunk_ids:
                    await conn.execute(text(f"SELECT drop_chunks('{chunk_id}', cascade_to_materializations => false)"))
                
                # Add span attributes for success
                end_time = datetime.utcnow()
                add_span_attributes({
                    "timestamp.end": end_time.isoformat(),
                    "duration_ms": (end_time - start_time).total_seconds() * 1000,
                    "chunks_dropped": len(chunk_ids),
                    "success": True
                })
                
                logger.info(f"Dropped {len(chunk_ids)} archived chunks from {table_name}")
        except Exception as e:
            # Add span attributes for error
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "error.type": e.__class__.__name__,
                "error.message": str(e),
                "success": False
            })
            raise
    
    @trace_method(name="retention_manager.get_retention_status")
    async def get_retention_status(self):
        """Get the current status of retention policies.
        
        Returns:
            Dictionary with retention status information
        """
        start_time = datetime.utcnow()
        
        # Add span attributes for context
        add_span_attributes({
            "timestamp.start": start_time.isoformat(),
            "retention_period_days": self.retention_period_days
        })
        
        try:
            hypertables = await self._get_hypertables_with_retention()
            
            status = {
                "retention_period_days": self.retention_period_days,
                "hypertables": []
            }
            
            for table_name, policy in hypertables:
                async with self.engine.begin() as conn:
                    # Get chunk statistics
                    # Use f-string for interval part to avoid parameter binding issues with TimescaleDB
                    retention_days = self.retention_period_days
                    result = await conn.execute(text(f"""
                        SELECT 
                            COUNT(*) as total_chunks,
                            SUM(CASE WHEN range_end < NOW() - INTERVAL '{retention_days} days' THEN 1 ELSE 0 END) as archivable_chunks,
                            MIN(range_start) as oldest_data,
                            MAX(range_end) as newest_data
                        FROM timescaledb_information.chunks
                        WHERE hypertable_name = :table_name
                    """), {"table_name": table_name})
                    
                    stats = result.fetchone()
                    
                    table_status = {
                        "table_name": table_name,
                        "retention_policy": policy.model_dump(),
                        "total_chunks": stats.total_chunks or 0,
                        "archivable_chunks": stats.archivable_chunks or 0,
                        "oldest_data": stats.oldest_data.isoformat() if stats.oldest_data else None,
                        "newest_data": stats.newest_data.isoformat() if stats.newest_data else None
                    }
                    
                    status["hypertables"].append(table_status)
            
            # Add span attributes for response
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "hypertable_count": len(status["hypertables"]),
                "total_archivable_chunks": sum(h["archivable_chunks"] or 0 for h in status["hypertables"]),
                "success": True
            })
            
            return status
        except Exception as e:
            # Add span attributes for error
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "error.type": e.__class__.__name__,
                "error.message": str(e),
                "success": False
            })
            raise
    
    @trace_method(name="retention_manager.manually_trigger_archival")
    async def manually_trigger_archival(self, table_name: Optional[str] = None, retention_period_days: Optional[int] = None) -> Dict[str, Any]:
        """Manually trigger the archival process.
        
        Args:
            table_name: Optional table name to process, or all tables if None
            
        Returns:
            Dictionary with results of the operation
        """
        start_time = datetime.utcnow()
        correlation_id = str(uuid.uuid4())
        
        # Add span attributes for request context
        add_span_attributes({
            "correlation_id": correlation_id,
            "timestamp.start": start_time.isoformat(),
            "specific_table": table_name is not None,
            "table_name": table_name if table_name else "all_tables",
            "retention_period_days": self.retention_period_days
        })
        
        try:
            if table_name:
                # Process specific table
                hypertables = [(table_name, RetentionPolicy(enabled=True, retention_period_days=self.retention_period_days))]
            else:
                # Process all tables
                hypertables = await self._get_hypertables_with_retention()
            
            results = []
            total_chunks = 0
            tables_with_chunks = 0
            
            retention_days = retention_period_days if retention_period_days is not None else self.retention_period_days

            for table, policy in hypertables:
                chunks = await self._identify_chunks_for_archival(table, retention_days)
                if chunks:
                    event_id = await self._publish_archival_event(table, chunks)
                    
                    # Store for confirmation tracking
                    self._archival_confirmations[event_id] = {
                        'table_name': table,
                        'chunks': chunks,
                        'timestamp': datetime.utcnow()
                    }
                    
                    results.append({
                        "table_name": table,
                        "chunks_to_archive": len(chunks),
                        "event_id": event_id,
                        "status": "published"
                    })
                    
                    total_chunks += len(chunks)
                    tables_with_chunks += 1
                else:
                    results.append({
                        "table_name": table,
                        "chunks_to_archive": 0,
                        "status": "no_chunks_to_archive"
                    })
            
            # Add span attributes for response
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "tables_processed": len(hypertables),
                "tables_with_chunks": tables_with_chunks,
                "total_chunks_to_archive": total_chunks,
                "success": True
            })
            
            return {
                "success": True,
                "message": f"Archival events published for {len(results)} tables",
                "results": results
            }
        except Exception as e:
            # Add span attributes for error
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "error.type": e.__class__.__name__,
                "error.message": str(e),
                "success": False
            })
            
            logger.error(f"Error triggering archival: {e}", exc_info=True)
            return {
                "success": False,
                "message": f"Error triggering archival: {str(e)}"
            }
