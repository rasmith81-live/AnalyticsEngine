"""
Event Publisher - Consolidated Redis event publishing functionality.
"""

import asyncio
import json
import logging
import time
import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Union

import redis.asyncio as redis
from redis.exceptions import BusyLoadingError
from redis.asyncio.retry import Retry
from redis.backoff import ExponentialBackoff

from .models import MessageMetadata, MessagePriority
from .telemetry import trace_method, add_span_attributes, inject_trace_context, traced_span

logger = logging.getLogger(__name__)


class EventPublisher:
    """Redis-based event publisher with advanced features."""
    
    def __init__(
        self,
        redis_url: str,
        max_connections: int = 20,
        retry_on_timeout: bool = True,
        socket_keepalive: bool = True,
        default_ttl: int = 3600,
        enable_compression: bool = True,
        max_message_size: int = 1048576  # 1MB
    ):
        self.redis_url = redis_url
        self.max_connections = max_connections
        self.retry_on_timeout = retry_on_timeout
        self.socket_keepalive = socket_keepalive
        self.default_ttl = default_ttl
        self.enable_compression = enable_compression
        self.max_message_size = max_message_size
        
        # Connection pool
        self.redis_pool: Optional[redis.ConnectionPool] = None
        self.redis_client: Optional[redis.Redis] = None
        
        # Metrics
        self.published_count = 0
        self.failed_count = 0
        self.total_bytes_sent = 0
        self.start_time = time.time()
        
        # Channel tracking
        self.active_channels: set = set()
        
    @trace_method(name="event_publisher_initialize", kind="INTERNAL")
    async def initialize(self):
        """Initialize the event publisher with retry logic."""
        max_retries = 5
        retry_delay = 1  # initial delay in seconds

        for attempt in range(max_retries):
            try:
                # Create connection pool
                self.redis_pool = redis.ConnectionPool.from_url(
                    self.redis_url,
                    max_connections=self.max_connections,
                    retry_on_timeout=self.retry_on_timeout,
                    socket_keepalive=self.socket_keepalive,
                    retry=Retry(ExponentialBackoff(), 3),
                    decode_responses=False  # We handle encoding ourselves
                )
                
                # Create Redis client
                self.redis_client = redis.Redis(connection_pool=self.redis_pool)
                
                # Test connection
                await self.redis_client.ping()
                logger.info("Event publisher initialized successfully")
                return # Success, so exit the loop
                
            except BusyLoadingError:
                logger.warning(f"Redis is loading data. Retrying in {retry_delay}s... (Attempt {attempt + 1}/{max_retries})")
                await asyncio.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff
            except Exception as e:
                logger.error(f"Failed to initialize event publisher on attempt {attempt + 1}: {e}")
                raise
        
        logger.error("Failed to initialize event publisher after multiple retries.")
        raise ConnectionError("Failed to initialize event publisher after multiple retries.")
    
    @trace_method(name="publish_message", kind="PRODUCER")
    async def publish_message(
        self,
        channel: str,
        payload: Union[Dict[str, Any], str, bytes],
        metadata: Optional[MessageMetadata] = None,
        persistent: bool = True,
        correlation_id: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> str:
        """Publish a message to a channel."""
        if not self.redis_client:
            raise RuntimeError("Event publisher not initialized")
        
        try:
            # Generate message ID if not provided
            message_id = metadata.message_id if metadata else str(uuid.uuid4())
            
            # Add span attributes for message context
            add_span_attributes({
                "messaging.system": "redis_pubsub",
                "messaging.destination": channel,
                "messaging.destination_kind": "channel",
                "messaging.message_id": message_id,
                "correlation_id": correlation_id or "not_provided"
            })
            
            # Create or update metadata with correlation ID and headers
            if not metadata:
                metadata = MessageMetadata(message_id=message_id)
            
            # Add correlation ID to metadata if provided
            if correlation_id and not hasattr(metadata, "correlation_id"):
                metadata.correlation_id = correlation_id
                
            # Add headers to metadata if provided
            if headers:
                metadata.headers = headers
            
            # Prepare message
            message = await self._prepare_message(payload, metadata)
            
            # Check message size
            message_size = len(message)
            if message_size > self.max_message_size:
                raise ValueError(f"Message size ({message_size}) exceeds maximum ({self.max_message_size})")
            
            # Publish to channel
            subscriber_count = await self.redis_client.publish(channel, message)
            
            # Store for persistence if enabled
            if persistent:
                await self._store_message(channel, message_id, message, metadata)
            
            # Update metrics
            self.published_count += 1
            self.total_bytes_sent += message_size
            self.active_channels.add(channel)
            
            logger.debug(f"Published message {message_id} to channel {channel} ({subscriber_count} subscribers)")
            return message_id
            
        except Exception as e:
            self.failed_count += 1
            logger.error(f"Failed to publish message to {channel}: {e}")
            raise
    
    @trace_method(name="publish_event", kind="PRODUCER")
    async def publish_event(
        self,
        event_type: str,
        source_service: str,
        event_data: Dict[str, Any],
        correlation_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """Publish a structured event."""
        # Create event payload
        event_payload = {
            "event_id": str(uuid.uuid4()),
            "event_type": event_type,
            "source_service": source_service,
            "event_data": event_data,
            "correlation_id": correlation_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "metadata": metadata or {}
        }
        
        # Determine channels based on event type
        channels = self._get_event_channels(event_type, source_service)
        
        # Prepare metadata for publishing
        publish_metadata = MessageMetadata(
            message_id=event_payload["event_id"],
            correlation_id=correlation_id,
            headers=headers or {},
            **(metadata or {})
        )

        # Publish to all relevant channels
        published_channels = []
        for channel in channels:
            try:
                # Publish the message with tracing context
                await self.publish_message(
                    channel=channel,
                    payload=event_payload,
                    metadata=publish_metadata,
                    persistent=True,
                    correlation_id=correlation_id,
                    headers=headers
                )
                published_channels.append(channel)
            except Exception as e:
                logger.error(f"Failed to publish event to channel {channel}: {e}")
        
        return {
            "event_id": event_payload["event_id"],
            "published_channels": published_channels,
            "timestamp": event_payload["timestamp"]
        }
    
    @trace_method(name="publish_bulk", kind="PRODUCER")
    async def publish_bulk(
        self,
        messages: List[Dict[str, Any]],
        fail_on_error: bool = False,
        correlation_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Publish multiple messages in bulk."""
        if not self.redis_client:
            raise RuntimeError("Event publisher not initialized")
        
        results = []
        published_count = 0
        failed_count = 0
        
        # Use pipeline for better performance
        async with self.redis_client.pipeline() as pipe:
            for msg_data in messages:
                try:
                    # Extract message details
                    channel = msg_data["channel"]
                    payload = msg_data["payload"] or msg_data["message"]
                    metadata = msg_data.get("metadata")
                    persistent = msg_data.get("persistent", True)
                    headers = msg_data.get("headers", {})
                    msg_correlation_id = msg_data.get("correlation_id", correlation_id)
                    
                    if not channel or payload is None:
                        raise ValueError(f"Message {msg_data} missing required fields")
                        
                    # Add message-specific correlation ID to headers if provided
                    if msg_correlation_id and "X-Correlation-ID" not in headers:
                        headers["X-Correlation-ID"] = msg_correlation_id
                    
                    # Prepare message
                    message_id = metadata.message_id if metadata else str(uuid.uuid4())
                    message = await self._prepare_message(payload, metadata or MessageMetadata(message_id=message_id))
                    
                    # Add to pipeline
                    pipe.publish(channel, message)
                    
                    results.append({
                        "success": True,
                        "message_id": message_id,
                        "channel": channel
                    })
                    
                except Exception as e:
                    failed_count += 1
                    results.append({
                        "success": False,
                        "error": str(e),
                        "channel": msg_data.get("channel", "unknown")
                    })
                    
                    if fail_on_error:
                        break
            
            # Execute pipeline
            if not fail_on_error or failed_count == 0:
                try:
                    await pipe.execute()
                    published_count = len([r for r in results if r["success"]])
                except Exception as e:
                    logger.error(f"Bulk publish pipeline failed: {e}")
                    # Mark all as failed
                    for result in results:
                        if result["success"]:
                            result["success"] = False
                            result["error"] = str(e)
                            failed_count += 1
                            published_count -= 1
        
        # Update metrics
        self.published_count += published_count
        self.failed_count += failed_count
        
        # Add span attributes for bulk operation
        add_span_attributes({
            "messaging.system": "redis_pubsub",
            "messaging.operation": "bulk_publish",
            "messaging.message_count": len(messages),
            "correlation_id": correlation_id or "not_provided"
        })
        
        return {
            "published_count": published_count,
            "failed_count": failed_count,
            "results": results
        }
    
    @trace_method(name="prepare_message", kind="INTERNAL")
    async def _prepare_message(self, payload: Union[Dict[str, Any], str, bytes], metadata: MessageMetadata) -> bytes:
        """Prepare message for publishing."""
        # Create message envelope
        envelope = {
            "metadata": {
                "message_id": metadata.message_id,
                "correlation_id": metadata.correlation_id,
                "reply_to": metadata.reply_to,
                "content_type": metadata.content_type,
                "content_encoding": metadata.content_encoding,
                "priority": metadata.priority.value,
                "ttl": metadata.ttl or self.default_ttl,
                "timestamp": metadata.timestamp.isoformat(),
                "headers": metadata.headers
            },
            "payload": payload
        }
        
        # Serialize to JSON
        message_str = json.dumps(envelope, default=str, ensure_ascii=False)
        
        # Encode to bytes
        message_bytes = message_str.encode('utf-8')
        
        # Apply compression if enabled and beneficial
        if self.enable_compression and len(message_bytes) > 1024:  # Only compress larger messages
            try:
                import gzip
                compressed = gzip.compress(message_bytes)
                if len(compressed) < len(message_bytes):
                    # Add compression header
                    envelope["metadata"]["content_encoding"] = "gzip"
                    message_bytes = compressed
            except ImportError:
                logger.warning("gzip not available for compression")
        
        return message_bytes
    
    @trace_method(name="store_message", kind="INTERNAL")
    async def _store_message(self, channel: str, message_id: str, message: bytes, metadata: Optional[MessageMetadata]) -> None:
        """Store message for persistence."""
        if not self.redis_client:
            return
        
        try:
            # Store in Redis with TTL
            ttl = (metadata.ttl if metadata and metadata.ttl is not None else self.default_ttl)
            key = f"message:{channel}:{message_id}"
            
            await self.redis_client.setex(key, ttl, message)
            
            # Add to channel message list
            list_key = f"channel:{channel}:messages"
            await self.redis_client.lpush(list_key, message_id)
            await self.redis_client.expire(list_key, ttl)
            
        except Exception as e:
            logger.error(f"Failed to store message {message_id}: {e}")
    
    def _get_event_channels(self, event_type: str, source_service: str) -> List[str]:
        """Get channels for an event type."""
        # Standard event routing patterns
        channels = [
            f"events.{event_type}",  # Type-specific channel
            f"events.{source_service}.{event_type}",  # Service + type specific
            f"events.{source_service}.*",  # All events from service
            "events.*"  # Global events channel
        ]
        
        return channels
    
    @trace_method(name="get_channel_info", kind="CLIENT")
    async def get_channel_info(self, channel: str) -> Dict[str, Any]:
        """Get information about a channel."""
        if not self.redis_client:
            raise RuntimeError("Event publisher not initialized")
        
        try:
            # Get subscriber count
            subscriber_count = await self.redis_client.pubsub_numsub(channel)
            subscriber_count = subscriber_count[0][1] if subscriber_count else 0
            
            # Get message count from stored list
            list_key = f"channel:{channel}:messages"
            message_count = await self.redis_client.llen(list_key)
            
            # Get last activity (if we track it)
            last_activity_key = f"channel:{channel}:last_activity"
            last_activity = await self.redis_client.get(last_activity_key)
            
            return {
                "name": channel,
                "subscriber_count": subscriber_count,
                "message_count": message_count,
                "last_activity": last_activity.decode() if last_activity else None,
                "is_active": channel in self.active_channels
            }
            
        except Exception as e:
            logger.error(f"Failed to get channel info for {channel}: {e}")
            raise
    
    @trace_method(name="get_metrics", kind="INTERNAL")
    async def get_metrics(self) -> Dict[str, Any]:
        """Get publisher metrics."""
        uptime = time.time() - self.start_time
        
        return {
            "published_count": self.published_count,
            "failed_count": self.failed_count,
            "total_bytes_sent": self.total_bytes_sent,
            "active_channels_count": len(self.active_channels),
            "uptime_seconds": uptime,
            "messages_per_second": self.published_count / uptime if uptime > 0 else 0,
            "error_rate": (self.failed_count / (self.published_count + self.failed_count)) * 100 if (self.published_count + self.failed_count) > 0 else 0,
            "avg_message_size": self.total_bytes_sent / self.published_count if self.published_count > 0 else 0
        }
    
    @trace_method(name="health_check", kind="INTERNAL")
    async def health_check(self) -> Dict[str, Any]:
        """Perform health check."""
        if not self.redis_client:
            return {"status": "unhealthy", "error": "Not initialized"}
        
        try:
            # Test Redis connection
            await self.redis_client.ping()
            
            # Get Redis info
            redis_info = await self.redis_client.info()
            
            return {
                "status": "healthy",
                "redis_connected": True,
                "redis_memory_usage": redis_info.get("used_memory", 0),
                "redis_connected_clients": redis_info.get("connected_clients", 0),
                "active_channels": len(self.active_channels)
            }
            
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return {
                "status": "unhealthy",
                "redis_connected": False,
                "error": str(e)
            }
    
    @trace_method(name="close", kind="INTERNAL")
    async def close(self):
        """Close the event publisher."""
        if self.redis_client:
            await self.redis_client.close()
        if self.redis_pool:
            await self.redis_pool.disconnect()
        logger.info("Event publisher closed")
