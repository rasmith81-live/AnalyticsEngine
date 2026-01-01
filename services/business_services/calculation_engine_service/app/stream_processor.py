"""
Stream Processor for Calculation Engine
Subscribes to data streams and calculates KPIs in real-time
"""
import asyncio
import logging
import json
from typing import Dict, Optional, Set, Callable, Any
from datetime import datetime
import redis.asyncio as redis
import httpx

from .base_handler import CalculationParams, CalculationResult
from .orchestrator import CalculationOrchestrator
from .engine.stream_aggregator import StreamAggregator
from .engine.storage_sync import StorageSyncManager
from .clients import DatabaseClient, MessagingClientWrapper

logger = logging.getLogger(__name__)


class StreamProcessor:
    """
    Processes incoming data streams and calculates KPIs in real-time
    
    Responsibilities:
    - Subscribe to data streams from database service
    - Listen for stream updates via messaging service
    - Ingest high-velocity data into StreamAggregator (Redis TimeSeries)
    - Calculate KPIs when new data arrives
    - Publish calculation results back to messaging service
    - Manage stream subscriptions lifecycle
    - Sync in-memory data to TimescaleDB (Write-Behind)
    """
    
    def __init__(
        self,
        orchestrator: CalculationOrchestrator,
        database_client: DatabaseClient,
        messaging_client: MessagingClientWrapper,
        redis_url: str,
        subscriber_id: Optional[str] = None,
        database_service_url: Optional[str] = None
    ):
        """
        Initialize stream processor
        
        Args:
            orchestrator: Calculation orchestrator for KPI calculations
            database_client: Database client for queries
            messaging_client: Messaging client for events
            redis_url: Redis connection URL for StreamAggregator
            subscriber_id: Optional subscriber ID (generated if not provided)
            database_service_url: URL for database service (for heartbeat)
        """
        self.orchestrator = orchestrator
        self.database_client = database_client
        self.messaging_client = messaging_client
        self.redis_url = redis_url
        self.subscriber_id = subscriber_id or f"calc_engine_{id(self)}"
        self.database_service_url = database_service_url or database_client.base_url
        
        # HTTP client for direct API calls (heartbeat, subscriptions)
        self._http_client: Optional[httpx.AsyncClient] = None
        
        # Initialize Stream Aggregator
        self.aggregator = StreamAggregator(redis_url=redis_url)
        
        # Initialize Storage Sync Manager (Write-Behind)
        self.sync_manager = StorageSyncManager(
            stream_aggregator=self.aggregator,
            database_client=database_client
        )
        
        # Track active subscriptions: stream_key -> subscription_info
        self._active_subscriptions: Dict[str, Dict] = {}
        
        # Track message consumers: channel -> consumer_task
        self._message_consumers: Dict[str, asyncio.Task] = {}
        
        # Control flag
        self._running = False
        
        # Heartbeat task
        self._heartbeat_task: Optional[asyncio.Task] = None
        
        logger.info(f"StreamProcessor initialized with subscriber_id: {self.subscriber_id}")
    
    async def start(self):
        """Start the stream processor"""
        self._running = True
        
        # Initialize HTTP client for API calls
        self._http_client = httpx.AsyncClient(timeout=30.0)
        
        # Start heartbeat task
        self._heartbeat_task = asyncio.create_task(self._heartbeat_loop())
        
        # Start Sync Manager
        await self.sync_manager.start()
        
        logger.info("StreamProcessor started")
    
    async def stop(self):
        """Stop the stream processor and cleanup all subscriptions"""
        self._running = False
        
        # Stop Sync Manager
        await self.sync_manager.stop()
        
        # Unsubscribe from all streams
        for stream_key in list(self._active_subscriptions.keys()):
            await self.unsubscribe_from_stream(stream_key)
        
        # Cancel all message consumers
        for channel, task in self._message_consumers.items():
            logger.info(f"Cancelling consumer for channel: {channel}")
            task.cancel()
        
        if self._message_consumers:
            await asyncio.gather(*self._message_consumers.values(), return_exceptions=True)
        
        # Cancel heartbeat task
        if self._heartbeat_task:
            self._heartbeat_task.cancel()
            try:
                await self._heartbeat_task
            except asyncio.CancelledError:
                pass
        
        # Close HTTP client
        if self._http_client:
            await self._http_client.aclose()
        
        logger.info("StreamProcessor stopped")
    
    async def subscribe_to_stream(
        self,
        kpi_code: str,
        entity_id: str,
        period: str,
        calculation_params: Optional[Dict[str, Any]] = None
    ) -> Dict:
        """
        Subscribe to a KPI data stream
        
        Args:
            kpi_code: KPI code to calculate
            entity_id: Entity ID for the KPI
            period: Time period ('minute', 'hour', 'day')
            calculation_params: Optional additional parameters for calculation
            
        Returns:
            Subscription details
        """
        stream_key = f"{kpi_code}:{entity_id}:{period}"
        
        if stream_key in self._active_subscriptions:
            logger.warning(f"Already subscribed to stream: {stream_key}")
            return self._active_subscriptions[stream_key]
        
        try:
            # Subscribe to stream via pub/sub messaging
            # The channel follows the pattern: stream.{kpi_code}.{entity_id}.{period}
            channel = f"stream.{kpi_code}.{entity_id}.{period}"
            
            # Publish subscription request via messaging
            await self.messaging_client.publish_event(
                event_type="stream.subscribe",
                payload={
                    "kpi_code": kpi_code,
                    "entity_id": entity_id,
                    "period": period,
                    "subscriber_id": self.subscriber_id,
                    "channel": channel
                }
            )
            
            subscription_info = {
                "channel": channel,
                "kpi_code": kpi_code,
                "entity_id": entity_id,
                "period": period
            }
            
            # Store subscription info
            self._active_subscriptions[stream_key] = {
                **subscription_info,
                "calculation_params": calculation_params or {},
                "subscribed_at": datetime.utcnow().isoformat()
            }
            
            # Start message consumer for this stream
            await self._start_message_consumer(channel, kpi_code, entity_id, period, calculation_params)
            
            # Register for write-behind sync
            await self.sync_manager.register_stream(kpi_code, entity_id)
            
            logger.info(f"Subscribed to stream: {stream_key} on channel: {channel}")
            
            return subscription_info
        
        except Exception as e:
            logger.error(f"Failed to subscribe to stream {stream_key}: {e}")
            raise
    
    async def unsubscribe_from_stream(self, stream_key: str) -> bool:
        """
        Unsubscribe from a KPI data stream
        
        Args:
            stream_key: Stream key (kpi_code:entity_id:period)
            
        Returns:
            True if unsubscribed successfully
        """
        if stream_key not in self._active_subscriptions:
            logger.warning(f"Not subscribed to stream: {stream_key}")
            return False
        
        subscription = self._active_subscriptions[stream_key]
        channel = subscription["channel"]
        
        try:
            # Stop message consumer
            if channel in self._message_consumers:
                task = self._message_consumers[channel]
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass
                del self._message_consumers[channel]
            
            # Unsubscribe via pub/sub messaging
            parts = stream_key.split(":")
            if len(parts) == 3:
                kpi_code, entity_id, period = parts
                await self.messaging_client.publish_event(
                    event_type="stream.unsubscribe",
                    payload={
                        "subscriber_id": self.subscriber_id,
                        "kpi_code": kpi_code,
                        "entity_id": entity_id,
                        "period": period,
                        "channel": channel
                    }
                )
            
            # Remove from active subscriptions
            del self._active_subscriptions[stream_key]
            
            logger.info(f"Unsubscribed from stream: {stream_key}")
            return True
        
        except Exception as e:
            logger.error(f"Failed to unsubscribe from stream {stream_key}: {e}")
            return False
    
    async def _start_message_consumer(
        self,
        channel: str,
        kpi_code: str,
        entity_id: str,
        period: str,
        calculation_params: Optional[Dict[str, Any]]
    ):
        """
        Start a message consumer for a specific channel
        
        Args:
            channel: Redis channel to subscribe to
            kpi_code: KPI code
            entity_id: Entity ID
            period: Time period
            calculation_params: Additional calculation parameters
        """
        if channel in self._message_consumers:
            logger.warning(f"Consumer already exists for channel: {channel}")
            return
        
        # Create consumer task
        task = asyncio.create_task(
            self._consume_messages(channel, kpi_code, entity_id, period, calculation_params)
        )
        self._message_consumers[channel] = task
        
        logger.info(f"Started message consumer for channel: {channel}")
    
    async def _consume_messages(
        self,
        channel: str,
        kpi_code: str,
        entity_id: str,
        period: str,
        calculation_params: Optional[Dict[str, Any]]
    ):
        """
        Consume messages from a Redis channel and calculate KPIs
        """
        logger.info(f"Message consumer started for channel: {channel}")
        
        redis_client = None
        pubsub = None
        
        try:
            # Connect to Redis
            redis_client = redis.from_url(self.redis_url, decode_responses=True)
            pubsub = redis_client.pubsub()
            await pubsub.subscribe(channel)
            
            logger.info(f"Subscribed to Redis channel: {channel}")
            
            while self._running:
                try:
                    message = await pubsub.get_message(ignore_subscribe_messages=True, timeout=1.0)
                    
                    if message:
                        try:
                            data = json.loads(message["data"])
                            await self._process_stream_update(
                                data, kpi_code, entity_id, period, calculation_params
                            )
                        except json.JSONDecodeError:
                            logger.warning(f"Received invalid JSON on channel {channel}: {message['data']}")
                        except Exception as e:
                            logger.error(f"Error processing message on channel {channel}: {e}")
                    
                    # Small sleep to yield control if no message (though get_message with timeout handles waiting)
                    if not message:
                        await asyncio.sleep(0.01)
                
                except asyncio.CancelledError:
                    raise
                
                except Exception as e:
                    logger.error(f"Error consuming messages from {channel}: {e}")
                    await asyncio.sleep(5)  # Back off on error
        
        except asyncio.CancelledError:
            logger.info(f"Message consumer stopped for channel: {channel}")
            raise
        
        except Exception as e:
            logger.error(f"Message consumer failed for channel {channel}: {e}")
            
        finally:
            if pubsub:
                await pubsub.unsubscribe(channel)
                await pubsub.close()
            if redis_client:
                await redis_client.close()
    
    async def _process_stream_update(
        self,
        message: Dict,
        kpi_code: str,
        entity_id: str,
        period: str,
        calculation_params: Optional[Dict[str, Any]]
    ):
        """
        Process a stream update message and calculate KPI
        
        Args:
            message: Stream update message
            kpi_code: KPI code to calculate
            entity_id: Entity ID
            period: Time period
            calculation_params: Additional calculation parameters
        """
        try:
            logger.debug(f"Processing stream update for {kpi_code}:{entity_id}:{period}")
            
            # Extract data from message
            timestamp = message.get("timestamp")
            avg_value = message.get("avg_value")
            
            # Ingest into In-Memory Stream Aggregator (Redis TimeSeries)
            # This allows for high-velocity lookups and sub-second windowing before DB persistence
            if avg_value is not None:
                await self.aggregator.add_sample(
                    metric_name=kpi_code,
                    value=float(avg_value),
                    dimensions={"entity_id": entity_id, "period": period}
                )
            
            # Create calculation parameters
            params = CalculationParams(
                kpi_code=kpi_code,
                entity_id=entity_id,
                start_date=timestamp,
                end_date=timestamp,
                filters=calculation_params.get("filters", {}),
                aggregation=calculation_params.get("aggregation", "average")
            )
            
            # Calculate KPI
            result = await self.orchestrator.calculate_single(params)
            
            # Publish result to messaging service
            await self._publish_calculation_result(result, kpi_code, entity_id, period)
            
            logger.debug(f"Calculated {kpi_code} for {entity_id}: {result.value}")
        
        except Exception as e:
            logger.error(f"Failed to process stream update: {e}")
    
    async def _publish_calculation_result(
        self,
        result: CalculationResult,
        kpi_code: str,
        entity_id: str,
        period: str
    ):
        """
        Publish calculation result to messaging service.
        
        Publishes to:
        - kpi.calculated (general channel for database service to persist/archive)
        - kpi.calculated.{kpi_code} (specific channel for subscribers)
        
        Args:
            result: Calculation result
            kpi_code: KPI code
            entity_id: Entity ID
            period: Time period
        """
        try:
            message = {
                "source": "calculation_engine",
                "kpi_code": kpi_code,
                "entity_id": entity_id,
                "period": period,
                "value": result.value,
                "unit": result.unit,
                "timestamp": result.timestamp.isoformat() if result.timestamp else None,
                "calculated_at": datetime.utcnow().isoformat(),
                "metadata": result.metadata
            }
            
            # Publish via messaging client to standard channel
            # Database service subscribes to this for persistence and archival
            await self.messaging_client.publish_event(
                event_type="kpi.calculated",
                payload=message
            )
            
            # Also publish to KPI-specific channel for targeted subscribers
            await self.messaging_client.publish_event(
                event_type=f"kpi.calculated.{kpi_code}",
                payload=message
            )
            
            logger.debug(f"Published KPI result: {kpi_code}={result.value}")
        
        except Exception as e:
            logger.error(f"Failed to publish calculation result: {e}")
    
    async def _heartbeat_loop(self):
        """Send periodic heartbeats via pub/sub to keep subscriptions alive"""
        logger.info("Heartbeat loop started")
        
        try:
            while self._running:
                await asyncio.sleep(60)  # Send heartbeat every minute
                
                try:
                    # Publish heartbeat via messaging service
                    await self.messaging_client.publish_event(
                        event_type="stream.heartbeat",
                        payload={
                            "subscriber_id": self.subscriber_id,
                            "active_subscriptions": list(self._active_subscriptions.keys()),
                            "timestamp": datetime.utcnow().isoformat()
                        }
                    )
                    logger.debug(f"Heartbeat sent for subscriber: {self.subscriber_id}")
                
                except Exception as e:
                    logger.error(f"Failed to send heartbeat: {e}")
        
        except asyncio.CancelledError:
            logger.info("Heartbeat loop cancelled")
            raise
        
        except Exception as e:
            logger.error(f"Heartbeat loop failed: {e}")
    
    async def get_status(self) -> Dict:
        """
        Get status of stream processor
        
        Returns:
            Status information
        """
        return {
            "running": self._running,
            "subscriber_id": self.subscriber_id,
            "active_subscriptions": len(self._active_subscriptions),
            "active_consumers": len(self._message_consumers),
            "subscriptions": {
                stream_key: {
                    "channel": sub["channel"],
                    "subscriber_count": sub.get("subscriber_count", 0),
                    "subscribed_at": sub["subscribed_at"]
                }
                for stream_key, sub in self._active_subscriptions.items()
            }
        }
    
    async def subscribe_to_simulation_events(
        self,
        kpi_codes: Optional[Set[str]] = None
    ):
        """
        Subscribe to simulation entity events for real-time KPI calculation.
        
        The Data Simulator Service publishes entity events to Redis pub/sub.
        This method subscribes to those events and triggers KPI calculations.
        
        Args:
            kpi_codes: Optional set of KPI codes to calculate. If None, calculates all.
        """
        channel = "simulation.entity.created"
        
        if channel in self._message_consumers:
            logger.warning(f"Already subscribed to simulation events")
            return
        
        # Create consumer task for simulation events
        task = asyncio.create_task(
            self._consume_simulation_events(channel, kpi_codes)
        )
        self._message_consumers[channel] = task
        
        logger.info(f"Subscribed to simulation entity events")
    
    async def _consume_simulation_events(
        self,
        channel: str,
        kpi_codes: Optional[Set[str]]
    ):
        """Consume simulation entity events and calculate KPIs."""
        logger.info(f"Simulation event consumer started for channel: {channel}")
        
        redis_client = None
        pubsub = None
        
        try:
            redis_client = redis.from_url(self.redis_url, decode_responses=True)
            pubsub = redis_client.pubsub()
            await pubsub.subscribe(channel)
            
            while self._running:
                try:
                    message = await pubsub.get_message(ignore_subscribe_messages=True, timeout=1.0)
                    
                    if message:
                        try:
                            data = json.loads(message["data"])
                            await self._process_simulation_entity_event(data, kpi_codes)
                        except json.JSONDecodeError:
                            logger.warning(f"Invalid JSON in simulation event")
                        except Exception as e:
                            logger.error(f"Error processing simulation event: {e}")
                    
                    if not message:
                        await asyncio.sleep(0.01)
                
                except asyncio.CancelledError:
                    raise
                except Exception as e:
                    logger.error(f"Error consuming simulation events: {e}")
                    await asyncio.sleep(5)
        
        except asyncio.CancelledError:
            logger.info("Simulation event consumer stopped")
            raise
        finally:
            if pubsub:
                await pubsub.unsubscribe(channel)
                await pubsub.close()
            if redis_client:
                await redis_client.close()
    
    async def _process_simulation_entity_event(
        self,
        event: Dict,
        kpi_codes: Optional[Set[str]]
    ):
        """
        Process a simulation entity event and trigger KPI calculations.
        
        Args:
            event: Entity event from simulation
            kpi_codes: Optional filter for which KPIs to calculate
        """
        try:
            entity_name = event.get("entity_name")
            entity_id = event.get("entity_id")
            attributes = event.get("attributes", {})
            timestamp = event.get("timestamp")
            simulation_id = event.get("simulation_id")
            
            logger.debug(f"Processing simulation event: {entity_name}/{entity_id}")
            
            # Ingest into Stream Aggregator for real-time windowing
            # Extract numeric values from attributes for aggregation
            for attr_name, attr_value in attributes.items():
                if isinstance(attr_value, (int, float)):
                    metric_name = f"{entity_name}.{attr_name}"
                    await self.aggregator.add_sample(
                        metric_name=metric_name,
                        value=float(attr_value),
                        dimensions={"entity_id": entity_id, "simulation_id": simulation_id}
                    )
            
            # TODO: Trigger KPI calculations based on entity type
            # This would look up which KPIs use this entity and calculate them
            
        except Exception as e:
            logger.error(f"Failed to process simulation entity event: {e}")
