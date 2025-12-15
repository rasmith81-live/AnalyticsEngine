"""
Period-Based Stream Publisher for Database Service
Publishes KPI updates from TimescaleDB continuous aggregates to messaging service
"""
import asyncio
import logging
from typing import Dict, Optional, Set
from datetime import datetime, timedelta
import json
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from .subscriber_manager import SubscriberManager
from .messaging_client import MessagingClient

logger = logging.getLogger(__name__)


class StreamPublisher:
    """
    Publishes KPI values from TimescaleDB continuous aggregates to messaging service
    
    Monitors continuous aggregates and publishes updates when new data is available.
    Only publishes for streams that have active subscribers.
    """
    
    def __init__(
        self,
        db_session_factory,
        messaging_client: MessagingClient,
        subscriber_manager: SubscriberManager,
        poll_interval_seconds: int = 30
    ):
        """
        Initialize stream publisher
        
        Args:
            db_session_factory: Factory function to create database sessions
            messaging_client: Client for publishing to messaging service
            subscriber_manager: Manager for tracking subscribers
            poll_interval_seconds: How often to check for new data
        """
        self.db_session_factory = db_session_factory
        self.messaging_client = messaging_client
        self.subscriber_manager = subscriber_manager
        self.poll_interval_seconds = poll_interval_seconds
        
        # Track active publishing tasks
        self._active_publishers: Dict[str, asyncio.Task] = {}
        
        # Track last published timestamp for each stream
        self._last_published: Dict[str, datetime] = {}
        
        # Control flag for graceful shutdown
        self._running = False
        
        # Background task for cleanup
        self._cleanup_task: Optional[asyncio.Task] = None
        
        logger.info(f"StreamPublisher initialized with {poll_interval_seconds}s poll interval")
    
    async def start(self):
        """Start the stream publisher"""
        self._running = True
        
        # Start cleanup task
        self._cleanup_task = asyncio.create_task(self._cleanup_loop())
        
        logger.info("StreamPublisher started")
    
    async def stop(self):
        """Stop the stream publisher and all active streams"""
        self._running = False
        
        # Cancel all active publishers
        for stream_key, task in self._active_publishers.items():
            logger.info(f"Stopping publisher for stream: {stream_key}")
            task.cancel()
        
        # Wait for all tasks to complete
        if self._active_publishers:
            await asyncio.gather(*self._active_publishers.values(), return_exceptions=True)
        
        # Cancel cleanup task
        if self._cleanup_task:
            self._cleanup_task.cancel()
            try:
                await self._cleanup_task
            except asyncio.CancelledError:
                pass
        
        logger.info("StreamPublisher stopped")
    
    async def start_stream(self, kpi_code: str, entity_id: str, period: str) -> bool:
        """
        Start publishing for a specific KPI stream
        
        Args:
            kpi_code: KPI code to publish
            entity_id: Entity ID for the KPI
            period: Time period ('minute', 'hour', 'day')
            
        Returns:
            True if stream was started, False if already running
        """
        stream_key = f"{kpi_code}:{entity_id}:{period}"
        
        if stream_key in self._active_publishers:
            logger.warning(f"Stream already active: {stream_key}")
            return False
        
        # Create and start publishing task
        task = asyncio.create_task(
            self._publish_loop(kpi_code, entity_id, period)
        )
        self._active_publishers[stream_key] = task
        
        logger.info(f"Started stream publisher for: {stream_key}")
        return True
    
    async def stop_stream(self, kpi_code: str, entity_id: str, period: str) -> bool:
        """
        Stop publishing for a specific KPI stream
        
        Args:
            kpi_code: KPI code
            entity_id: Entity ID
            period: Time period
            
        Returns:
            True if stream was stopped, False if not running
        """
        stream_key = f"{kpi_code}:{entity_id}:{period}"
        
        if stream_key not in self._active_publishers:
            logger.warning(f"Stream not active: {stream_key}")
            return False
        
        # Cancel the publishing task
        task = self._active_publishers[stream_key]
        task.cancel()
        
        try:
            await task
        except asyncio.CancelledError:
            pass
        
        # Remove from active publishers
        if stream_key in self._active_publishers:
            del self._active_publishers[stream_key]
        
        # Remove last published timestamp
        if stream_key in self._last_published:
            del self._last_published[stream_key]
        
        logger.info(f"Stopped stream publisher for: {stream_key}")
        return True
    
    async def _publish_loop(self, kpi_code: str, entity_id: str, period: str):
        """
        Main publishing loop for a specific stream
        
        Continuously polls the continuous aggregate and publishes updates
        """
        stream_key = f"{kpi_code}:{entity_id}:{period}"
        
        logger.info(f"Publishing loop started for: {stream_key}")
        
        try:
            while self._running:
                # Check if stream still has subscribers
                subscriber_count = await self.subscriber_manager.get_subscriber_count(
                    kpi_code, entity_id, period
                )
                
                if subscriber_count == 0:
                    logger.info(f"No subscribers for {stream_key}, stopping publisher")
                    break
                
                # Fetch and publish latest data
                try:
                    await self._fetch_and_publish(kpi_code, entity_id, period)
                except Exception as e:
                    logger.error(f"Error publishing {stream_key}: {e}", exc_info=True)
                
                # Wait before next poll
                await asyncio.sleep(self.poll_interval_seconds)
        
        except asyncio.CancelledError:
            logger.info(f"Publishing loop cancelled for: {stream_key}")
            raise
        
        except Exception as e:
            logger.error(f"Publishing loop error for {stream_key}: {e}", exc_info=True)
        
        finally:
            # Clean up
            if stream_key in self._active_publishers:
                del self._active_publishers[stream_key]
            logger.info(f"Publishing loop ended for: {stream_key}")
    
    async def _fetch_and_publish(self, kpi_code: str, entity_id: str, period: str):
        """
        Fetch latest data from continuous aggregate and publish to messaging service
        
        Args:
            kpi_code: KPI code
            entity_id: Entity ID
            period: Time period
        """
        stream_key = f"{kpi_code}:{entity_id}:{period}"
        
        # Determine which continuous aggregate to query
        table_name = f"kpi_values_{period}"
        
        # Get last published timestamp
        last_published = self._last_published.get(stream_key)
        
        # Build query
        if last_published:
            # Only fetch data newer than last published
            query = text(f"""
                SELECT 
                    bucket,
                    kpi_code,
                    entity_id,
                    avg_value,
                    min_value,
                    max_value,
                    sum_value,
                    data_points,
                    stddev_value
                FROM {table_name}
                WHERE kpi_code = :kpi_code
                  AND entity_id = :entity_id
                  AND bucket > :last_published
                ORDER BY bucket DESC
                LIMIT 10
            """)
            params = {
                "kpi_code": kpi_code,
                "entity_id": entity_id,
                "last_published": last_published
            }
        else:
            # First fetch - get latest value
            query = text(f"""
                SELECT 
                    bucket,
                    kpi_code,
                    entity_id,
                    avg_value,
                    min_value,
                    max_value,
                    sum_value,
                    data_points,
                    stddev_value
                FROM {table_name}
                WHERE kpi_code = :kpi_code
                  AND entity_id = :entity_id
                ORDER BY bucket DESC
                LIMIT 1
            """)
            params = {
                "kpi_code": kpi_code,
                "entity_id": entity_id
            }
        
        # Execute query
        async with self.db_session_factory() as session:
            result = await session.execute(query, params)
            rows = result.fetchall()
        
        if not rows:
            logger.debug(f"No new data for {stream_key}")
            return
        
        # Publish each row
        for row in rows:
            message = {
                "timestamp": row.bucket.isoformat() if row.bucket else None,
                "kpi_code": row.kpi_code,
                "entity_id": row.entity_id,
                "period": period,
                "avg_value": float(row.avg_value) if row.avg_value is not None else None,
                "min_value": float(row.min_value) if row.min_value is not None else None,
                "max_value": float(row.max_value) if row.max_value is not None else None,
                "sum_value": float(row.sum_value) if row.sum_value is not None else None,
                "data_points": int(row.data_points) if row.data_points is not None else 0,
                "stddev_value": float(row.stddev_value) if row.stddev_value is not None else None,
                "published_at": datetime.utcnow().isoformat()
            }
            
            # Publish to messaging service
            channel = f"kpi.stream.{kpi_code}.{entity_id}.{period}"
            
            try:
                await self.messaging_client.publish_message(
                    channel=channel,
                    message=message,
                    message_type="kpi_stream_update"
                )
                
                logger.debug(f"Published update for {stream_key}: {message['timestamp']}")
                
                # Update last published timestamp
                if row.bucket:
                    self._last_published[stream_key] = row.bucket
            
            except Exception as e:
                logger.error(f"Failed to publish message for {stream_key}: {e}")
    
    async def _cleanup_loop(self):
        """
        Background task to clean up inactive subscribers and stop unused streams
        """
        logger.info("Cleanup loop started")
        
        try:
            while self._running:
                await asyncio.sleep(60)  # Run every minute
                
                # Clean up inactive subscribers
                streams_to_stop = await self.subscriber_manager.cleanup_inactive_subscribers()
                
                # Stop streams with no subscribers
                for stream_key in streams_to_stop:
                    details = await self.subscriber_manager.get_stream_details(stream_key)
                    if details:
                        kpi_code, entity_id, period = details
                        await self.stop_stream(kpi_code, entity_id, period)
        
        except asyncio.CancelledError:
            logger.info("Cleanup loop cancelled")
            raise
        
        except Exception as e:
            logger.error(f"Cleanup loop error: {e}", exc_info=True)
    
    async def get_status(self) -> Dict:
        """
        Get status of all active streams
        
        Returns:
            Dict with stream status information
        """
        active_streams = {}
        
        for stream_key, task in self._active_publishers.items():
            details = await self.subscriber_manager.get_stream_details(stream_key)
            if details:
                kpi_code, entity_id, period = details
                subscriber_count = await self.subscriber_manager.get_subscriber_count(
                    kpi_code, entity_id, period
                )
                
                active_streams[stream_key] = {
                    "kpi_code": kpi_code,
                    "entity_id": entity_id,
                    "period": period,
                    "subscriber_count": subscriber_count,
                    "last_published": self._last_published.get(stream_key).isoformat() 
                        if stream_key in self._last_published else None,
                    "is_running": not task.done()
                }
        
        return {
            "running": self._running,
            "active_stream_count": len(self._active_publishers),
            "active_streams": active_streams,
            "poll_interval_seconds": self.poll_interval_seconds
        }
