"""
Subscription Manager - Handles Redis pub/sub subscriptions and message delivery.
"""

import asyncio
import json
import logging
import time
import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Set, Callable

import redis.asyncio as redis
import aiohttp
from redis.asyncio.retry import Retry
from redis.backoff import ExponentialBackoff
from opentelemetry import trace
from opentelemetry.trace.status import Status, StatusCode

from .models import SubscriptionStatus, MessageDelivery, MessageMetadata, MessagePriority
from .telemetry import trace_method, add_span_attributes, extract_trace_context, inject_trace_context, traced_span

logger = logging.getLogger(__name__)


class Subscription:
    """Individual subscription information."""
    
    def __init__(
        self,
        subscription_id: str,
        channel_pattern: str,
        service_name: str,
        callback_url: Optional[str] = None,
        webhook_headers: Optional[Dict[str, str]] = None,
        max_delivery_attempts: int = 3,
        ack_timeout: int = 30,
        batch_size: int = 1,
        auto_ack: bool = False
    ):
        self.subscription_id = subscription_id
        self.channel_pattern = channel_pattern
        self.service_name = service_name
        self.callback_url = callback_url
        self.webhook_headers = webhook_headers or {}
        self.max_delivery_attempts = max_delivery_attempts
        self.ack_timeout = ack_timeout
        self.batch_size = batch_size
        self.auto_ack = auto_ack
        
        # Status tracking
        self.status = SubscriptionStatus.ACTIVE
        self.created_at = datetime.now(timezone.utc)
        self.last_activity = None
        self.message_count = 0
        self.error_count = 0
        
        # Message processing
        self.pending_messages: Dict[str, Dict] = {}
        self.message_queue: asyncio.Queue = asyncio.Queue()
        
        # Tasks
        self.processor_task: Optional[asyncio.Task] = None
        self.heartbeat_task: Optional[asyncio.Task] = None


class SubscriptionManager:
    """Manages Redis pub/sub subscriptions and message delivery."""
    
    def __init__(
        self,
        redis_url: str,
        max_connections: int = 20,
        heartbeat_interval: int = 30,
        subscription_timeout: int = 300,
        max_subscriptions_per_service: int = 50
    ):
        self.redis_url = redis_url
        self.max_connections = max_connections
        self.heartbeat_interval = heartbeat_interval
        self.subscription_timeout = subscription_timeout
        self.max_subscriptions_per_service = max_subscriptions_per_service
        
        # Redis connections
        self.redis_pool: Optional[redis.ConnectionPool] = None
        self.redis_client: Optional[redis.Redis] = None
        self.pubsub_client: Optional[redis.Redis] = None
        self.pubsub: Optional[redis.client.PubSub] = None
        
        # Subscriptions
        self.subscriptions: Dict[str, Subscription] = {}
        self.service_subscriptions: Dict[str, Set[str]] = {}
        self.channel_subscriptions: Dict[str, Set[str]] = {}
        
        # HTTP session for webhooks
        self.http_session: Optional[aiohttp.ClientSession] = None
        
        # Tasks
        self.message_listener_task: Optional[asyncio.Task] = None
        self.cleanup_task: Optional[asyncio.Task] = None
        
        # Metrics
        self.total_messages_received = 0
        self.total_messages_delivered = 0
        self.total_messages_failed = 0
        self.start_time = time.time()
    
    @trace_method(name="subscription_manager_initialize", kind="INTERNAL")
    async def initialize(self):
        """Initialize the subscription manager."""
        try:
            # Create connection pool
            self.redis_pool = redis.ConnectionPool.from_url(
                self.redis_url,
                max_connections=self.max_connections,
                retry_on_timeout=True,
                socket_keepalive=True,
                retry=Retry(ExponentialBackoff(), 3),
                decode_responses=False
            )
            
            # Create Redis clients
            self.redis_client = redis.Redis(connection_pool=self.redis_pool)
            self.pubsub_client = redis.Redis(connection_pool=self.redis_pool)
            
            # Create pub/sub instance
            self.pubsub = self.pubsub_client.pubsub()
            
            # Create HTTP session for webhooks
            self.http_session = aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=30)
            )
            
            # Test connection
            await self.redis_client.ping()
            
            # Start background tasks
            self.message_listener_task = asyncio.create_task(self._message_listener())
            self.cleanup_task = asyncio.create_task(self._cleanup_expired_subscriptions())
            
            logger.info("Subscription manager initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize subscription manager: {e}")
            raise
    
    def _handle_subscription_operation(operation_name: str):
        def decorator(func: Callable):
            async def wrapper(self, *args, **kwargs):
                start_time = datetime.now(timezone.utc)
                current_span = trace.get_current_span()

                try:
                    return await func(self, *args, **kwargs)
                except Exception as e:
                    end_time = datetime.now(timezone.utc)
                    duration_ms = (end_time - start_time).total_seconds() * 1000

                    if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
                        current_span.set_attribute("timestamp.end", end_time.isoformat())
                        current_span.set_attribute("duration_ms", duration_ms)
                        current_span.set_attribute("error.type", e.__class__.__name__)
                        current_span.set_attribute("error.message", str(e))
                        current_span.set_attribute("success", False)
                        current_span.set_status(Status(StatusCode.ERROR, str(e)))
                        current_span.record_exception(e)

                    logger.error(f"Failed during {operation_name}: {e}")
                    return {
                        "success": False,
                        "error": str(e),
                        "correlation_id": kwargs.get("correlation_id") or str(uuid.uuid4())
                    }
            return wrapper
        return decorator

    @trace_method(name="create_subscription", kind="SERVER")
    @_handle_subscription_operation("create_subscription")
    async def create_subscription(
        self,
        service_name: str,
        callback_url: str,
        channel: Optional[str] = None,
        channel_pattern: Optional[str] = None,
        filter_criteria: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        max_retries: int = 3,
        retry_delay: int = 5,
        correlation_id: Optional[str] = None,
        **kwargs
    ) -> str:
        """Create a new subscription."""
        start_time = datetime.now(timezone.utc)
        transaction_id = str(uuid.uuid4())  # Generate unique transaction ID for this operation
        
        # Determine the channel identifier to use for the subscription
        identifier = channel_pattern if channel_pattern else channel
        if not identifier:
            raise ValueError("Either 'channel' or 'channel_pattern' must be provided.")

        # Get current span and add detailed attributes
        current_span = trace.get_current_span()
        if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
            # Add operation context attributes
            current_span.set_attribute("correlation_id", correlation_id or str(uuid.uuid4()))
            current_span.set_attribute("transaction_id", transaction_id)
            current_span.set_attribute("messaging.system", "redis_pubsub")
            current_span.set_attribute("messaging.operation", "create_subscription")
            current_span.set_attribute("messaging.channel_identifier", identifier)
            current_span.set_attribute("messaging.service_name", service_name)
            current_span.set_attribute("timestamp.start", start_time.isoformat())
            
            # Add subscription configuration attributes
            current_span.set_attribute("subscription.max_retries", max_retries)
            current_span.set_attribute("subscription.retry_delay", retry_delay)

        if callback_url:
            current_span.set_attribute("subscription.callback_url", callback_url)
        
        with traced_span("check_subscription_limit", attributes={
            "correlation_id": correlation_id or str(uuid.uuid4()),
            "messaging.service_name": service_name,
            "subscription.current_count": len(self.service_subscriptions.get(service_name, set())),
            "subscription.max_allowed": self.max_subscriptions_per_service
        }) as limit_span:
            service_subs = self.service_subscriptions.get(service_name, set())
            if len(service_subs) >= self.max_subscriptions_per_service:
                limit_span.set_status(Status(StatusCode.ERROR, "Subscription limit exceeded"))
                raise ValueError(f"Service {service_name} has reached maximum subscriptions limit of {self.max_subscriptions_per_service}")
        
        # Generate subscription ID
        subscription_id = str(uuid.uuid4())
        
        if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
            current_span.set_attribute("messaging.subscription_id", subscription_id)
        
        # Create subscription with tracing
        with traced_span("initialize_subscription", attributes={
            "correlation_id": correlation_id or str(uuid.uuid4()),
            "messaging.subscription_id": subscription_id,
            "messaging.channel_pattern": channel_pattern,
            "messaging.service_name": service_name
        }) as init_span:
            # Create subscription object
            subscription = Subscription(
                subscription_id=subscription_id,
                channel_pattern=identifier,
                service_name=service_name,
                callback_url=callback_url,
                webhook_headers=headers,
                max_delivery_attempts=max_retries,
                ack_timeout=30,  # Default or from params
                batch_size=1, # Default or from params
                auto_ack=False # Default or from params
            )
            
            # Store subscription
            self.subscriptions[subscription_id] = subscription
            
            # Update service tracking
            if service_name not in self.service_subscriptions:
                self.service_subscriptions[service_name] = set()
            self.service_subscriptions[service_name].add(subscription_id)
            
            # Update channel tracking
            if identifier not in self.channel_subscriptions:
                self.channel_subscriptions[identifier] = set()
            self.channel_subscriptions[identifier].add(subscription_id)
        
        # Subscribe to Redis channel with tracing
        with traced_span("redis_channel_subscribe", attributes={
            "correlation_id": correlation_id or str(uuid.uuid4()),
            "messaging.subscription_id": subscription_id,
            "messaging.channel_identifier": identifier,
            "messaging.operation": "subscribe"
        }) as redis_span:
            subscribe_start = time.time()
            await self._subscribe_to_channel(identifier)
            subscribe_duration_ms = (time.time() - subscribe_start) * 1000
            redis_span.set_attribute("operation.duration_ms", subscribe_duration_ms)
        
        # Start tasks with tracing
        with traced_span("start_subscription_tasks", attributes={
            "correlation_id": correlation_id or str(uuid.uuid4()),
            "messaging.subscription_id": subscription_id
        }) as tasks_span:
            # Start subscription processor
            subscription.processor_task = asyncio.create_task(
                self._process_subscription_messages(subscription)
            )
            
            # Start heartbeat
            subscription.heartbeat_task = asyncio.create_task(
                self._subscription_heartbeat(subscription)
            )
        
        # Record successful completion
        end_time = datetime.now(timezone.utc)
        duration_ms = (end_time - start_time).total_seconds() * 1000
        
        if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
            current_span.set_attribute("timestamp.end", end_time.isoformat())
            current_span.set_attribute("duration_ms", duration_ms)
            current_span.set_attribute("success", True)
            current_span.set_status(Status(StatusCode.OK))
        
        logger.info(f"Created subscription {subscription_id} for service {service_name} on pattern {identifier}")
        return subscription_id, subscription.created_at, subscription.status
        
        
        # Add subscription details to validation span
        validation_span.set_attribute("messaging.channel_pattern", subscription.channel_pattern)
        validation_span.set_attribute("messaging.service_name", subscription.service_name)
        validation_span.set_attribute("subscription.status", subscription.status.value)
    
        try:
            # Update subscription status with tracing
            with traced_span("update_subscription_status", attributes={
                "correlation_id": correlation_id or str(uuid.uuid4()),
                "messaging.subscription_id": subscription_id,
                "messaging.operation": "update_status",
                "subscription.previous_status": subscription.status.value,
                "subscription.new_status": SubscriptionStatus.CANCELLED.value
            }) as status_span:
                subscription.status = SubscriptionStatus.CANCELLED
            
            # Cancel tasks with tracing
            with traced_span("cancel_subscription_tasks", attributes={
                "correlation_id": correlation_id or str(uuid.uuid4()),
                "messaging.subscription_id": subscription_id,
                "messaging.operation": "cancel_tasks"
            }) as tasks_span:
                if subscription.processor_task:
                    tasks_span.set_attribute("task.processor_active", not subscription.processor_task.done())
                    subscription.processor_task.cancel()
                
                if subscription.heartbeat_task:
                    tasks_span.set_attribute("task.heartbeat_active", not subscription.heartbeat_task.done())
                    subscription.heartbeat_task.cancel()
            
            # Update tracking with tracing
            with traced_span("update_subscription_tracking", attributes={
                "correlation_id": correlation_id or str(uuid.uuid4()),
                "messaging.subscription_id": subscription_id,
                "messaging.service_name": subscription.service_name,
                "messaging.channel_pattern": subscription.channel_pattern
            }) as tracking_span:
                # Remove from service tracking
                service_subs = self.service_subscriptions.get(subscription.service_name, set())
                service_subs.discard(subscription_id)
                tracking_span.set_attribute("service.remaining_subscriptions", len(service_subs))
                
                # Remove from channel tracking
                channel_subs = self.channel_subscriptions.get(subscription.channel_pattern, set())
                channel_subs.discard(subscription_id)
                tracking_span.set_attribute("channel.remaining_subscriptions", len(channel_subs))
            
            # Unsubscribe from Redis if no more subscriptions
            if not channel_subs:
                with traced_span("redis_channel_unsubscribe", attributes={
                    "correlation_id": correlation_id or str(uuid.uuid4()),
                    "messaging.subscription_id": subscription_id,
                    "messaging.channel_pattern": subscription.channel_pattern,
                    "messaging.operation": "unsubscribe"
                }) as redis_span:
                    unsubscribe_start = time.time()
                    # Use synchronous version or handle in the async method
                    self._schedule_unsubscribe(subscription.channel_pattern)
                    redis_span.set_attribute("unsubscribe.duration_ms", (time.time() - unsubscribe_start) * 1000)

            # Record successful completion
            end_time = datetime.now(timezone.utc)
            duration_ms = (end_time - start_time).total_seconds() * 1000
            
            if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
                current_span.set_attribute("timestamp.end", end_time.isoformat())
                current_span.set_attribute("duration_ms", duration_ms)
                current_span.set_attribute("success", True)
                current_span.set_status(Status(StatusCode.OK))
            
            return {
                "success": True,
                "subscription_id": subscription_id,
                "correlation_id": correlation_id or str(uuid.uuid4())
            }
        
        except Exception as e:
            # Record error details
            end_time = datetime.now(timezone.utc)
            duration_ms = (end_time - start_time).total_seconds() * 1000
            
            if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
                current_span.set_attribute("timestamp.end", end_time.isoformat())
                current_span.set_attribute("duration_ms", duration_ms)
                current_span.set_attribute("error.type", e.__class__.__name__)
                current_span.set_attribute("error.message", str(e))
                current_span.set_attribute("success", False)
                current_span.set_status(Status(StatusCode.ERROR, str(e)))
                current_span.record_exception(e)
            
            logger.error(f"Failed to cancel subscription {subscription_id}: {e}")
            return {
                "success": False, 
                "error": str(e),
                "subscription_id": subscription_id,
                "correlation_id": correlation_id or str(uuid.uuid4())
            }
        
        # Remove subscription with tracing
        with traced_span("remove_subscription", attributes={
            "correlation_id": correlation_id or str(uuid.uuid4()),
            "messaging.subscription_id": subscription_id
        }):
                del self.subscriptions[subscription_id]
        
        # Record successful completion
        end_time = datetime.now(timezone.utc)
        duration_ms = (end_time - start_time).total_seconds() * 1000
        
        if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
            current_span.set_attribute("timestamp.end", end_time.isoformat())
            current_span.set_attribute("duration_ms", duration_ms)
            current_span.set_attribute("success", True)
            current_span.set_status(Status(StatusCode.OK))
        
        logger.info(f"Cancelled subscription {subscription_id}")
        return {
            "success": True, 
            "subscription_id": subscription_id,
            "correlation_id": correlation_id or str(uuid.uuid4())
        }

    
    @trace_method(name="cancel_subscription", kind="SERVER")
    @_handle_subscription_operation("cancel_subscription")
    async def cancel_subscription(self, subscription_id: str, correlation_id: Optional[str] = None) -> Dict[str, Any]:
        """Cancel a subscription."""
        start_time = datetime.now(timezone.utc)
        transaction_id = str(uuid.uuid4())  # Generate unique transaction ID for this operation
        
        # Get current span and add detailed attributes
        current_span = trace.get_current_span()
        if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
            # Add operation context attributes
                current_span.set_attribute("correlation_id", correlation_id or str(uuid.uuid4()))
                current_span.set_attribute("transaction_id", transaction_id)
                current_span.set_attribute("messaging.system", "redis_pubsub")
                current_span.set_attribute("messaging.operation", "cancel_subscription")
                current_span.set_attribute("messaging.subscription_id", subscription_id)
                current_span.set_attribute("timestamp.start", start_time.isoformat())
                current_span.set_attribute("service.name", "messaging_service")
        
        # Check if subscription exists with tracing
        with traced_span("validate_subscription", attributes={
            "correlation_id": correlation_id or str(uuid.uuid4()),
            "messaging.subscription_id": subscription_id,
            "messaging.operation": "validate_subscription"
        }) as validation_span:
            subscription = self.subscriptions.get(subscription_id)
            validation_span.set_attribute("subscription.exists", subscription is not None)
            
            if not subscription:
                validation_span.set_attribute("error.type", "SubscriptionNotFound")
                validation_span.set_attribute("error.message", f"Subscription {subscription_id} not found")
                
            if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
                current_span.set_attribute("error.type", "SubscriptionNotFound")
                current_span.set_attribute("error.message", f"Subscription {subscription_id} not found")
                current_span.set_attribute("success", False)
                current_span.set_status(Status(StatusCode.ERROR, "Subscription not found"))
                
                logger.warning(f"Attempted to cancel non-existent subscription {subscription_id}")
                return {
                    "success": False, 
                    "error": "Subscription not found", 
                    "correlation_id": correlation_id or str(uuid.uuid4())
                }
            
            # Add subscription details to validation span
            validation_span.set_attribute("messaging.channel_pattern", subscription.channel_pattern)
            validation_span.set_attribute("messaging.service_name", subscription.service_name)
            validation_span.set_attribute("subscription.status", subscription.status.value)
        
        # Update subscription status with tracing
        with traced_span("update_subscription_status", attributes={
            "correlation_id": correlation_id or str(uuid.uuid4()),
            "messaging.subscription_id": subscription_id,
            "messaging.operation": "update_status",
            "subscription.previous_status": subscription.status.value,
            "subscription.new_status": SubscriptionStatus.CANCELLED.value
        }) as status_span:
                subscription.status = SubscriptionStatus.CANCELLED
        
        # Cancel tasks with tracing
        with traced_span("cancel_subscription_tasks", attributes={
            "correlation_id": correlation_id or str(uuid.uuid4()),
            "messaging.subscription_id": subscription_id,
            "messaging.operation": "cancel_tasks"
        }) as tasks_span:
                if subscription.processor_task:
                    tasks_span.set_attribute("task.processor_active", not subscription.processor_task.done())
                    subscription.processor_task.cancel()
            
                if subscription.heartbeat_task:
                    tasks_span.set_attribute("task.heartbeat_active", not subscription.heartbeat_task.done())
                    subscription.heartbeat_task.cancel()
        
        # Update tracking with tracing
        with traced_span("update_subscription_tracking", attributes={
            "correlation_id": correlation_id or str(uuid.uuid4()),
            "messaging.subscription_id": subscription_id,
            "messaging.service_name": subscription.service_name,
            "messaging.channel_pattern": subscription.channel_pattern
        }) as tracking_span:
                # Remove from service tracking
                service_subs = self.service_subscriptions.get(subscription.service_name, set())
                service_subs.discard(subscription_id)
                tracking_span.set_attribute("service.remaining_subscriptions", len(service_subs))
            
                # Remove from channel tracking
                channel_subs = self.channel_subscriptions.get(subscription.channel_pattern, set())
                channel_subs.discard(subscription_id)
                tracking_span.set_attribute("channel.remaining_subscriptions", len(channel_subs))
        
        # Unsubscribe from Redis if no more subscriptions
        if not channel_subs:
            with traced_span("redis_channel_unsubscribe", attributes={
                "correlation_id": correlation_id or str(uuid.uuid4()),
                "messaging.subscription_id": subscription_id,
                "messaging.channel_pattern": subscription.channel_pattern,
                "messaging.operation": "unsubscribe"
            }) as redis_span:
                unsubscribe_start = time.time()
                await self._unsubscribe_from_channel(subscription.channel_pattern)
                unsubscribe_duration_ms = (time.time() - unsubscribe_start) * 1000
                redis_span.set_attribute("operation.duration_ms", unsubscribe_duration_ms)
        
            # Remove subscription with tracing
        with traced_span("remove_subscription", attributes={
            "correlation_id": correlation_id or str(uuid.uuid4()),
            "messaging.subscription_id": subscription_id
        }):
                del self.subscriptions[subscription_id]
        
        # Record successful completion
        end_time = datetime.now(timezone.utc)
        duration_ms = (end_time - start_time).total_seconds() * 1000
        
        if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
            current_span.set_attribute("timestamp.end", end_time.isoformat())
            current_span.set_attribute("duration_ms", duration_ms)
            current_span.set_attribute("success", True)
            current_span.set_status(Status(StatusCode.OK))
        
        logger.info(f"Cancelled subscription {subscription_id}")
        return {
            "success": True, 
            "subscription_id": subscription_id,
            "correlation_id": correlation_id or str(uuid.uuid4())
        }
        
    
    @trace_method(name="get_subscription_info", kind="SERVER")
    async def get_subscription_info(self, subscription_id: str, correlation_id: Optional[str] = None) -> Dict[str, Any]:
        """Get subscription information with detailed tracing."""
        start_time = datetime.now(timezone.utc)
        transaction_id = str(uuid.uuid4())  # Generate unique transaction ID for this operation
        
        # Get current span and add detailed attributes
        current_span = trace.get_current_span()
        if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
            # Add operation context attributes
                current_span.set_attribute("correlation_id", correlation_id or str(uuid.uuid4()))
                current_span.set_attribute("transaction_id", transaction_id)
                current_span.set_attribute("messaging.system", "redis_pubsub")
                current_span.set_attribute("messaging.operation", "get_subscription_info")
                current_span.set_attribute("messaging.subscription_id", subscription_id)
                current_span.set_attribute("timestamp.start", start_time.isoformat())
                current_span.set_attribute("service.name", "messaging_service")
        
        # Check if subscription exists
        subscription = self.subscriptions.get(subscription_id)
        if not subscription:
                if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
                    current_span.set_attribute("error.type", "SubscriptionNotFound")
                    current_span.set_attribute("error.message", f"Subscription {subscription_id} not found")
                    current_span.set_attribute("success", False)
                current_span.set_status(Status(StatusCode.ERROR, "Subscription not found"))
            
        return None
        
        try:
            # Add subscription details to span
            if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
                current_span.set_attribute("messaging.channel_pattern", subscription.channel_pattern)
                current_span.set_attribute("messaging.service_name", subscription.service_name)
                current_span.set_attribute("subscription.status", subscription.status.value)
                current_span.set_attribute("subscription.message_count", subscription.message_count)
                current_span.set_attribute("subscription.error_count", subscription.error_count)
                current_span.set_attribute("subscription.pending_messages", len(subscription.pending_messages))
            
            # Create subscription info with tracing
            with traced_span("build_subscription_info", attributes={
                "correlation_id": correlation_id or str(uuid.uuid4()),
                "messaging.subscription_id": subscription_id,
                "messaging.operation": "build_info"
            }) as info_span:
                info = {
                    "subscription_id": subscription.subscription_id,
                    "channel_pattern": subscription.channel_pattern,
                    "service_name": subscription.service_name,
                    "status": subscription.status.value,
                    "callback_url": subscription.callback_url,
                    "max_delivery_attempts": subscription.max_delivery_attempts,
                    "ack_timeout": subscription.ack_timeout,
                    "batch_size": subscription.batch_size,
                    "auto_ack": subscription.auto_ack,
                    "created_at": subscription.created_at.isoformat(),
                    "last_activity": subscription.last_activity.isoformat() if subscription.last_activity else None,
                    "message_count": subscription.message_count,
                    "error_count": subscription.error_count,
                    "pending_messages": len(subscription.pending_messages),
                    "correlation_id": correlation_id or str(uuid.uuid4())
                }
            
            # Record successful completion
            end_time = datetime.now(timezone.utc)
            duration_ms = (end_time - start_time).total_seconds() * 1000
            
            if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
                current_span.set_attribute("timestamp.end", end_time.isoformat())
                current_span.set_attribute("duration_ms", duration_ms)
                current_span.set_attribute("success", True)
                current_span.set_status(Status(StatusCode.OK))
            
            return info
        
        except Exception as e:
            # Record error details
            end_time = datetime.now(timezone.utc)
            duration_ms = (end_time - start_time).total_seconds() * 1000
            
            if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
                current_span.set_attribute("timestamp.end", end_time.isoformat())
                current_span.set_attribute("duration_ms", duration_ms)
                current_span.set_attribute("error.type", e.__class__.__name__)
                current_span.set_attribute("error.message", str(e))
                current_span.set_attribute("success", False)
                current_span.set_status(Status(StatusCode.ERROR, str(e)))
                current_span.record_exception(e)
            
            logger.error(f"Failed to get subscription info for {subscription_id}: {e}")
            return None
    
    @trace_method(name="acknowledge_message", kind="SERVER")
    async def acknowledge_message(self, subscription_id: str, message_id: str, success: bool = True, error: Optional[str] = None, correlation_id: Optional[str] = None) -> Dict[str, Any]:
        """Acknowledge message processing with detailed tracing."""
        start_time = datetime.now(timezone.utc)
        transaction_id = str(uuid.uuid4())  # Generate unique transaction ID for this operation
        
        # Get current span and add detailed attributes
        current_span = trace.get_current_span()
        if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
            # Add operation context attributes
            current_span.set_attribute("correlation_id", correlation_id or str(uuid.uuid4()))
            current_span.set_attribute("transaction_id", transaction_id)
            current_span.set_attribute("messaging.system", "redis_pubsub")
            current_span.set_attribute("messaging.operation", "acknowledge_message")
            current_span.set_attribute("messaging.subscription_id", subscription_id)
            current_span.set_attribute("messaging.message_id", message_id)
            current_span.set_attribute("messaging.success", success)
            current_span.set_attribute("timestamp.start", start_time.isoformat())
            current_span.set_attribute("service.name", "messaging_service")
            
            if error:
                current_span.set_attribute("messaging.error", error)
        
        # Check if subscription exists with tracing
        with traced_span("validate_subscription", attributes={
            "correlation_id": correlation_id or str(uuid.uuid4()),
            "messaging.subscription_id": subscription_id,
            "messaging.message_id": message_id,
            "messaging.operation": "validate_subscription"
        }) as validation_span:
            subscription = self.subscriptions.get(subscription_id)
            validation_span.set_attribute("subscription.exists", subscription is not None)
            
            if not subscription:
                validation_span.set_attribute("error.type", "SubscriptionNotFound")
                validation_span.set_attribute("error.message", f"Subscription {subscription_id} not found")
                
            if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
                current_span.set_attribute("error.type", "SubscriptionNotFound")
                current_span.set_attribute("error.message", f"Subscription {subscription_id} not found")
                current_span.set_attribute("success", False)
                current_span.set_status(Status(StatusCode.ERROR, "Subscription not found"))
                
                logger.warning(f"Acknowledgment for unknown subscription {subscription_id}")
                return {
                    "success": False, 
                    "error": "Subscription not found", 
                    "correlation_id": correlation_id or str(uuid.uuid4())
                }
        
        try:
            # Process acknowledgment with tracing
            with traced_span("process_acknowledgment", attributes={
                "correlation_id": correlation_id or str(uuid.uuid4()),
                "messaging.subscription_id": subscription_id,
                "messaging.message_id": message_id,
                "messaging.success": success,
                "messaging.operation": "process_acknowledgment"
            }) as ack_span:
                # Check if message exists in pending messages
                message_exists = message_id in subscription.pending_messages
                ack_span.set_attribute("message.exists", message_exists)
                
                if message_exists:
                    # Remove from pending messages
                    del subscription.pending_messages[message_id]
                    
                    # Update metrics
                    if success:
                        self.total_messages_delivered += 1
                        ack_span.set_attribute("metrics.total_delivered", self.total_messages_delivered)
                    else:
                        self.total_messages_failed += 1
                        subscription.error_count += 1
                        ack_span.set_attribute("metrics.total_failed", self.total_messages_failed)
                        ack_span.set_attribute("metrics.subscription_errors", subscription.error_count)
                        ack_span.set_attribute("error.message", error or "Unknown error")
                        logger.warning(f"Message {message_id} processing failed: {error}")
                else:
                    ack_span.set_attribute("error.type", "MessageNotFound")
                    ack_span.set_attribute("error.message", f"Message {message_id} not found in pending messages")
            
            # Record successful completion
            end_time = datetime.now(timezone.utc)
            duration_ms = (end_time - start_time).total_seconds() * 1000
            
            if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
                current_span.set_attribute("timestamp.end", end_time.isoformat())
                current_span.set_attribute("duration_ms", duration_ms)
                current_span.set_attribute("success", True)
                current_span.set_status(Status(StatusCode.OK))
            
            return {
                "success": True,
                "correlation_id": correlation_id or str(uuid.uuid4())
            }
        
        except Exception as e:
            # Record error details
            end_time = datetime.now(timezone.utc)
            duration_ms = (end_time - start_time).total_seconds() * 1000
            
            if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
                current_span.set_attribute("timestamp.end", end_time.isoformat())
                current_span.set_attribute("duration_ms", duration_ms)
                current_span.set_attribute("error.type", e.__class__.__name__)
                current_span.set_attribute("error.message", str(e))
                current_span.set_attribute("success", False)
                current_span.set_status(Status(StatusCode.ERROR, str(e)))
                current_span.record_exception(e)
            
            logger.error(f"Failed to acknowledge message {message_id}: {e}")
            return {
                "success": False, 
                "error": str(e),
                "correlation_id": correlation_id or str(uuid.uuid4())
            }
    
    @trace_method(name="deliver_message", kind="SERVER")
    async def deliver_message(self, subscription_id: str, message: Dict[str, Any], correlation_id: Optional[str] = None) -> Dict[str, Any]:
        """Deliver a message to a subscription with comprehensive distributed tracing."""
        start_time = datetime.now(timezone.utc)
        transaction_id = str(uuid.uuid4())  # Generate unique transaction ID for this operation
        message_id = message.get("id") or str(uuid.uuid4())
        
        # Get current span and add detailed attributes
        current_span = trace.get_current_span()
        if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
            # Add operation context attributes
                current_span.set_attribute("correlation_id", correlation_id or str(uuid.uuid4()))
                current_span.set_attribute("transaction_id", transaction_id)
                current_span.set_attribute("messaging.system", "redis_pubsub")
                current_span.set_attribute("messaging.operation", "deliver_message")
                current_span.set_attribute("messaging.subscription_id", subscription_id)
                current_span.set_attribute("messaging.message_id", message_id)
                current_span.set_attribute("timestamp.start", start_time.isoformat())
                current_span.set_attribute("service.name", "messaging_service")
        
        # Check if subscription exists with tracing
        with traced_span("validate_subscription", attributes={
            "correlation_id": correlation_id or str(uuid.uuid4()),
            "messaging.subscription_id": subscription_id,
            "messaging.message_id": message_id,
            "messaging.operation": "validate_subscription"
        }) as validation_span:
            subscription = self.subscriptions.get(subscription_id)
            validation_span.set_attribute("subscription.exists", subscription is not None)
            
            if not subscription:
                validation_span.set_attribute("error.type", "SubscriptionNotFound")
                validation_span.set_attribute("error.message", f"Subscription {subscription_id} not found")
                
            if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
                current_span.set_attribute("error.type", "SubscriptionNotFound")
                current_span.set_attribute("error.message", f"Subscription {subscription_id} not found")
                current_span.set_attribute("success", False)
                current_span.set_status(Status(StatusCode.ERROR, "Subscription not found"))
                
                logger.warning(f"Delivery attempt for unknown subscription {subscription_id}")
                return {
                    "success": False, 
                    "error": "Subscription not found", 
                    "correlation_id": correlation_id or str(uuid.uuid4())
                }
            
            # Check subscription status
            if subscription.status != SubscriptionStatus.ACTIVE:
                validation_span.set_attribute("error.type", "SubscriptionInactive")
                validation_span.set_attribute("error.message", f"Subscription {subscription_id} is {subscription.status.value}")
                validation_span.set_attribute("subscription.status", subscription.status.value)
                
                if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
                    current_span.set_attribute("error.type", "SubscriptionInactive")
                    current_span.set_attribute("error.message", f"Subscription {subscription_id} is {subscription.status.value}")
                    current_span.set_attribute("subscription.status", subscription.status.value)
                    current_span.set_attribute("success", False)
                    current_span.set_status(Status(StatusCode.ERROR, f"Subscription is {subscription.status.value}"))
                
                logger.warning(f"Delivery attempt for inactive subscription {subscription_id} with status {subscription.status.value}")
                return {
                    "success": False, 
                    "error": f"Subscription is {subscription.status.value}", 
                    "correlation_id": correlation_id or str(uuid.uuid4())
                }
        
        try:
            # Prepare message for delivery with tracing
            with traced_span("prepare_message", attributes={
                "correlation_id": correlation_id or str(uuid.uuid4()),
                "messaging.subscription_id": subscription_id,
                "messaging.message_id": message_id,
                "messaging.operation": "prepare_message"
            }) as prepare_span:
                # Add message to pending messages
                delivery_attempt = {
                    "message": message,
                    "attempt": 1,
                    "first_attempt": datetime.now(timezone.utc).isoformat(),
                    "last_attempt": datetime.now(timezone.utc).isoformat(),
                    "subscription_id": subscription_id,
                    "correlation_id": correlation_id or str(uuid.uuid4()),
                    "transaction_id": transaction_id
                }
                
                subscription.pending_messages[message_id] = delivery_attempt
                prepare_span.set_attribute("message.prepared", True)
                prepare_span.set_attribute("message.channel", message.get("channel", "unknown"))
                prepare_span.set_attribute("message.priority", message.get("priority", "normal"))
            
            # Deliver message via webhook with tracing
            with traced_span("webhook_delivery", attributes={
                "correlation_id": correlation_id or str(uuid.uuid4()),
                "messaging.subscription_id": subscription_id,
                "messaging.message_id": message_id,
                "messaging.operation": "webhook_delivery",
                "messaging.callback_url": subscription.callback_url
            }) as webhook_span:
                if not subscription.callback_url:
                    webhook_span.set_attribute("error.type", "NoCallbackUrl")
                    webhook_span.set_attribute("error.message", "No callback URL configured for subscription")
                    
                    if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
                        current_span.set_attribute("error.type", "NoCallbackUrl")
                        current_span.set_attribute("error.message", "No callback URL configured for subscription")
                        current_span.set_attribute("success", False)
                        current_span.set_status(Status(StatusCode.ERROR, "No callback URL configured"))
                    
                    logger.warning(f"No callback URL for subscription {subscription_id}")
                    return {
                        "success": False, 
                        "error": "No callback URL configured", 
                        "correlation_id": correlation_id or str(uuid.uuid4())
                    }
                
                # Prepare headers with trace context injection
                headers = dict(subscription.webhook_headers or {})
                headers["Content-Type"] = "application/json"
                headers["X-Correlation-ID"] = correlation_id or str(uuid.uuid4())
                headers["X-Transaction-ID"] = transaction_id
                headers["X-Message-ID"] = message_id
                headers["X-Subscription-ID"] = subscription_id
                
                # Inject trace context into headers
                inject_trace_context(headers)
                webhook_span.set_attribute("headers.injected", True)
                
                # Prepare payload
                payload = {
                    "message": message,
                    "metadata": {
                        "message_id": message_id,
                        "subscription_id": subscription_id,
                        "correlation_id": correlation_id or str(uuid.uuid4()),
                        "transaction_id": transaction_id,
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                        "delivery_attempt": 1
                    }
                }
                
                # Send webhook request with timeout
                try:
                    webhook_span.set_attribute("webhook.request_start", datetime.now(timezone.utc).isoformat())
                    async with self.http_session.post(
                            subscription.callback_url,
                        json=payload,
                        headers=headers,
                        timeout=aiohttp.ClientTimeout(total=30)
                    ) as response:
                        webhook_span.set_attribute("webhook.status_code", response.status)
                        webhook_span.set_attribute("webhook.request_end", datetime.now(timezone.utc).isoformat())
                        
                        # Process response
                        if 200 <= response.status < 300:
                            webhook_span.set_attribute("webhook.success", True)
                            
                            # Auto-acknowledge if configured
                            if subscription.auto_ack:
                                # Remove from pending messages
                                if message_id in subscription.pending_messages:
                                    del subscription.pending_messages[message_id]
                                
                                # Update metrics
                                self.total_messages_delivered += 1
                                subscription.message_count += 1
                                subscription.last_activity = datetime.now(timezone.utc)
                                
                                webhook_span.set_attribute("message.auto_acknowledged", True)
                                webhook_span.set_attribute("metrics.total_delivered", self.total_messages_delivered)
                                webhook_span.set_attribute("metrics.subscription_messages", subscription.message_count)
                        else:
                            # Handle error response
                            error_text = await response.text()
                            webhook_span.set_attribute("webhook.success", False)
                            webhook_span.set_attribute("error.type", "WebhookError")
                            webhook_span.set_attribute("error.message", f"Webhook failed with status {response.status}: {error_text}")
                            webhook_span.set_attribute("error.http_status", response.status)
                            
                            # Update metrics
                            self.total_messages_failed += 1
                            subscription.error_count += 1
                            
                            webhook_span.set_attribute("metrics.total_failed", self.total_messages_failed)
                            webhook_span.set_attribute("metrics.subscription_errors", subscription.error_count)
                            
                            logger.warning(f"Webhook delivery failed for message {message_id} to subscription {subscription_id}: {response.status} {error_text}")
                            
                            # Keep in pending messages for retry or manual acknowledgment
                except asyncio.TimeoutError as e:
                    webhook_span.set_attribute("webhook.success", False)
                    webhook_span.set_attribute("error.type", "WebhookTimeout")
                    webhook_span.set_attribute("error.message", "Webhook request timed out")
                    
                    # Update metrics
                    self.total_messages_failed += 1
                    subscription.error_count += 1
                    
                    webhook_span.set_attribute("metrics.total_failed", self.total_messages_failed)
                    webhook_span.set_attribute("metrics.subscription_errors", subscription.error_count)
                    
                    logger.warning(f"Webhook delivery timed out for message {message_id} to subscription {subscription_id}")
                    webhook_span.record_exception(e)
                except Exception as e:
                    webhook_span.set_attribute("webhook.success", False)
                    webhook_span.set_attribute("error.type", e.__class__.__name__)
                    webhook_span.set_attribute("error.message", str(e))
                    
                    # Update metrics
                    self.total_messages_failed += 1
                    subscription.error_count += 1
                    
                    webhook_span.set_attribute("metrics.total_failed", self.total_messages_failed)
                    webhook_span.set_attribute("metrics.subscription_errors", subscription.error_count)
                    
                    logger.error(f"Webhook delivery error for message {message_id} to subscription {subscription_id}: {e}")
                    webhook_span.record_exception(e)
            
            # Record successful completion
            end_time = datetime.now(timezone.utc)
            duration_ms = (end_time - start_time).total_seconds() * 1000
            
            if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
                current_span.set_attribute("timestamp.end", end_time.isoformat())
                current_span.set_attribute("duration_ms", duration_ms)
                current_span.set_attribute("success", True)
                current_span.set_status(Status(StatusCode.OK))
            
            return {
                "success": True,
                "message_id": message_id,
                "subscription_id": subscription_id,
                "correlation_id": correlation_id or str(uuid.uuid4()),
                "auto_acknowledged": subscription.auto_ack
            }
        
        except Exception as e:
            # Record error details
            end_time = datetime.now(timezone.utc)
            duration_ms = (end_time - start_time).total_seconds() * 1000
            
            if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
                current_span.set_attribute("timestamp.end", end_time.isoformat())
                current_span.set_attribute("duration_ms", duration_ms)
                current_span.set_attribute("error.type", e.__class__.__name__)
                current_span.set_attribute("error.message", str(e))
                current_span.set_attribute("success", False)
                current_span.set_status(Status(StatusCode.ERROR, str(e)))
                current_span.record_exception(e)
            
            logger.error(f"Failed to deliver message {message_id} to subscription {subscription_id}: {e}")
            return {
                "success": False, 
                "error": str(e),
                "message_id": message_id,
                "subscription_id": subscription_id,
                "correlation_id": correlation_id or str(uuid.uuid4())
            }
    
    @trace_method(name="list_subscriptions", kind="SERVER")
    async def list_subscriptions(self, service_name: Optional[str] = None) -> List[Dict[str, Any]]:
        """List all subscriptions, optionally filtered by service."""
        subscriptions = []
        
        for subscription in self.subscriptions.values():
            if service_name and subscription.service_name != service_name:
                continue
                
            info = await self.get_subscription_info(subscription.subscription_id)
            if info:
                subscriptions.append(info)
        
        return subscriptions
    
    @trace_method(name="subscribe_to_channel", kind="INTERNAL")
    async def _subscribe_to_channel(self, channel_pattern: str) -> None:
        """Subscribe to a Redis channel pattern."""
        if not self.pubsub:
            raise RuntimeError("PubSub not initialized")
        
        try:
            if '*' in channel_pattern or '?' in channel_pattern or '[' in channel_pattern:
                # Pattern subscription
                await self.pubsub.psubscribe(channel_pattern)
            else:
                # Exact channel subscription
                await self.pubsub.subscribe(channel_pattern)
                
            logger.debug(f"Subscribed to channel pattern: {channel_pattern}")
            
        except Exception as e:
            logger.error(f"Failed to subscribe to channel {channel_pattern}: {e}")
            raise
    
    @trace_method(name="unsubscribe_from_channel", kind="INTERNAL")
    async def _unsubscribe_from_channel(self, channel_pattern: str) -> None:
        """Unsubscribe from a Redis channel pattern."""
        if not self.pubsub:
            return
        
        try:
            if '*' in channel_pattern or '?' in channel_pattern or '[' in channel_pattern:
                await self.pubsub.punsubscribe(channel_pattern)
            else:
                await self.pubsub.unsubscribe(channel_pattern)
                
            logger.debug(f"Unsubscribed from channel pattern: {channel_pattern}")
            
        except Exception as e:
            logger.error(f"Failed to unsubscribe from channel {channel_pattern}: {e}")
    
    @trace_method(name="message_listener", kind="CONSUMER")
    async def _message_listener(self) -> None:
        """Listen for Redis pub/sub messages."""
        if not self.pubsub:
            return
        
        try:
            async for message in self.pubsub.listen():
                if message['type'] in ('message', 'pmessage'):
                    await self._handle_message(message)
                    
        except asyncio.CancelledError:
            logger.info("Message listener cancelled")
        except Exception as e:
            logger.error(f"Message listener error: {e}")
    
    @trace_method(name="handle_message", kind="CONSUMER")
    async def _handle_message(self, redis_message: Dict[str, Any]) -> None:
        """Handle incoming Redis message."""
        try:
            # Extract message details
            channel = redis_message["channel"].decode()
            data = redis_message["data"]
            
            # Add span attributes for message context
            add_span_attributes({
                "messaging.system": "redis_pubsub",
                "messaging.destination": channel,
                "messaging.destination_kind": "channel",
                "messaging.operation": "receive"
            })
            
            # Decode message data
            try:
                message_bytes = data
                message_dict = json.loads(message_bytes.decode())
                data = data.decode('utf-8')
            except Exception as e:
                logger.error(f"Failed to decode message data: {e}")
                return
            
            # Parse message
            try:
                message_envelope = json.loads(data)
                metadata = message_envelope.get('metadata', {})
                payload = message_envelope.get('payload')
            except json.JSONDecodeError:
                # Handle plain text messages
                message_envelope = {
                    'metadata': {
                        'message_id': str(uuid.uuid4()),
                        'timestamp': datetime.now(timezone.utc).isoformat(),
                        'content_type': 'text/plain'
                    },
                    'payload': data
                }
                metadata = message_envelope['metadata']
                payload = data
            
            # Find matching subscriptions
            matching_subscriptions = self._find_matching_subscriptions(channel)
            
            # Deliver to each subscription
            for subscription_id in matching_subscriptions:
                subscription = self.subscriptions.get(subscription_id)
                if subscription and subscription.status == SubscriptionStatus.ACTIVE:
                    await self._deliver_message_to_subscription(subscription, channel, payload, metadata)
            
            self.total_messages_received += 1
            
        except Exception as e:
            logger.error(f"Failed to handle message: {e}")
    
    def _find_matching_subscriptions(self, channel: str) -> Set[str]:
        """Find subscriptions that match the channel."""
        matching = set()
        
        for pattern, subscription_ids in self.channel_subscriptions.items():
            if self._channel_matches_pattern(channel, pattern):
                matching.update(subscription_ids)
        
        return matching
    
    def _channel_matches_pattern(self, channel: str, pattern: str) -> bool:
        """Check if channel matches pattern."""
        if pattern == channel:
            return True
        
        # Simple pattern matching (extend as needed)
        if '*' in pattern:
            import fnmatch
            return fnmatch.fnmatch(channel, pattern)
        
        return False
    
    @trace_method(name="deliver_message_to_subscription", kind="INTERNAL")
    async def _deliver_message_to_subscription(self, subscription: Subscription, channel: str, payload: Any, metadata: Dict[str, Any]) -> None:
        """Deliver message to a specific subscription."""
        try:
            # Create message delivery object
            message_delivery = MessageDelivery(
                message_id=metadata.get('message_id', str(uuid.uuid4())),
                subscription_id=subscription.subscription_id,
                channel=channel,
                payload=payload,
                metadata=MessageMetadata(**metadata) if isinstance(metadata, dict) else metadata,
                delivery_attempt=1,
                max_attempts=subscription.max_delivery_attempts,
                delivered_at=datetime.now(timezone.utc)
            )
            
            # Add to subscription queue
            await subscription.message_queue.put(message_delivery)
            subscription.message_count += 1
            subscription.last_activity = datetime.now(timezone.utc)
            
        except Exception as e:
            logger.error(f"Failed to deliver message to subscription {subscription.subscription_id}: {e}")
    
    @trace_method(name="process_subscription_messages", kind="INTERNAL")
    async def _process_subscription_messages(self, subscription: Subscription) -> None:
        """Process messages for a subscription."""
        try:
            while subscription.status == SubscriptionStatus.ACTIVE:
                try:
                    # Get message from queue
                    message = await asyncio.wait_for(
                            subscription.message_queue.get(),
                        timeout=1.0
                    )
                    
                    # Process message
                    await self._process_message(subscription, message)
                    
                except asyncio.TimeoutError:
                    continue
                except Exception as e:
                    logger.error(f"Error processing message for subscription {subscription.subscription_id}: {e}")
                    
        except asyncio.CancelledError:
            logger.info(f"Message processor cancelled for subscription {subscription.subscription_id}")
        except Exception as e:
            logger.error(f"Message processor error for subscription {subscription.subscription_id}: {e}")
    
    @trace_method(name="process_message", kind="INTERNAL")
    async def _process_message(self, subscription: Subscription, message: MessageDelivery) -> None:
        """Process a single message."""
        try:
            # Add to pending messages
            subscription.pending_messages[message.message_id] = {
                "timestamp": time.time(),
                "attempts": message.delivery_attempt
            }
            
            # Deliver via webhook if configured
            if subscription.callback_url:
                success = await self._deliver_via_webhook(subscription, message)
                
                # Auto-acknowledge if configured
                if subscription.auto_ack:
                    await self.acknowledge_message(subscription.subscription_id, message.message_id, success)
                else:
                    # Set up timeout handler
                    asyncio.create_task(self._handle_ack_timeout(subscription, message))
        except Exception as e:
            logger.error(f"Failed to process message {message.message_id}: {e}")
            await self.acknowledge_message(subscription.subscription_id, message.message_id, False, str(e))
    
    @trace_method(name="deliver_via_webhook", kind="CLIENT")
    async def _deliver_via_webhook(self, subscription: Subscription, message: MessageDelivery) -> bool:
        """Deliver message via HTTP webhook."""
        if not self.http_session or not subscription.callback_url:
            return False
        
        try:
            if not self.http_session:
                self.http_session = aiohttp.ClientSession()
                
            # Prepare headers
            headers = dict(subscription.webhook_headers or {})
            headers["Content-Type"] = "application/json"
            headers["X-Subscription-ID"] = subscription.subscription_id
            headers["X-Message-ID"] = message.message_id
            
            # Add span attributes for webhook delivery
            add_span_attributes({
                "messaging.system": "webhook",
                "messaging.destination": subscription.callback_url,
                "messaging.destination_kind": "webhook",
                "messaging.message_id": message.message_id,
                "messaging.subscription_id": subscription.subscription_id,
                "http.url": subscription.callback_url,
                "http.method": "POST"
            })
            
            # Extract correlation ID from message metadata if available
            correlation_id = None
            if hasattr(message, "metadata") and message.metadata:
                correlation_id = message.metadata.get("correlation_id")
                if correlation_id:
                    headers["X-Correlation-ID"] = correlation_id
            
            # Inject trace context into outgoing request headers
            inject_trace_context(headers)
            
            # Prepare webhook payload
            webhook_payload = {
                "subscription_id": subscription.subscription_id,
                "message_id": message.message_id,
                "channel": message.channel,
                "payload": message.payload,
                "metadata": message.metadata.dict() if hasattr(message.metadata, 'dict') else message.metadata,
                "delivery_attempt": message.delivery_attempt,
                "delivered_at": message.delivered_at.isoformat()
            }
            
            # Send webhook
            async with self.http_session.post(
                    subscription.callback_url,
                json=webhook_payload,
                headers=headers
            ) as response:
                if response.status == 200:
                    return True
                else:
                    logger.warning(f"Webhook returned status {response.status} for message {message.message_id}")
                    return False
                    
        except Exception as e:
            logger.error(f"Webhook delivery failed for message {message.message_id}: {e}")
            return False
    
    @trace_method(name="handle_ack_timeout", kind="INTERNAL")
    async def _handle_ack_timeout(self, subscription: Subscription, message: MessageDelivery) -> None:
        """Handle acknowledgment timeout."""
        await asyncio.sleep(subscription.ack_timeout)
        
        # Check if message is still pending
        if message.message_id in subscription.pending_messages:
            pending_info = subscription.pending_messages[message.message_id]
            pending_info["attempts"] += 1
            
            if pending_info["attempts"] >= subscription.max_delivery_attempts:
                # Max attempts reached, mark as failed
                await self.acknowledge_message(subscription.subscription_id, message.message_id, False, "Max delivery attempts exceeded")
            else:
                # Retry delivery
                message.delivery_attempt = pending_info["attempts"] + 1
                await subscription.message_queue.put(message)
    
    @trace_method(name="subscription_heartbeat", kind="INTERNAL")
    async def _subscription_heartbeat(self, subscription: Subscription) -> None:
        """Send periodic heartbeat for subscription."""
        try:
            while subscription.status == SubscriptionStatus.ACTIVE:
                await asyncio.sleep(self.heartbeat_interval)
                
                # Update last activity
                subscription.last_activity = datetime.now(timezone.utc)
                
                # Check for expired pending messages
                current_time = datetime.now(timezone.utc)
                expired_messages = []
                
                for message_id, pending_info in subscription.pending_messages.items():
                    age = (current_time - pending_info["timestamp"]).total_seconds()
                    if age > subscription.ack_timeout * 2:  # Double timeout for safety
                        expired_messages.append(message_id)
                
                # Clean up expired messages
                for message_id in expired_messages:
                    await self.acknowledge_message(subscription.subscription_id, message_id, False, "Message expired")
                    
        except asyncio.CancelledError:
            logger.info(f"Heartbeat cancelled for subscription {subscription.subscription_id}")
        except Exception as e:
            logger.error(f"Heartbeat error for subscription {subscription.subscription_id}: {e}")
    
    @trace_method(name="cleanup_expired_subscriptions", kind="INTERNAL")
    async def _cleanup_expired_subscriptions(self) -> None:
        """Clean up expired subscriptions."""
        try:
            while True:
                await asyncio.sleep(60)  # Check every minute
                
                current_time = datetime.now(timezone.utc)
                expired_subscriptions = []
                
                for subscription in self.subscriptions.values():
                    if subscription.last_activity:
                        age = (current_time - subscription.last_activity).total_seconds()
                        if age > self.subscription_timeout:
                            expired_subscriptions.append(subscription.subscription_id)
                
                # Cancel expired subscriptions
                for subscription_id in expired_subscriptions:
                    logger.info(f"Cancelling expired subscription {subscription_id}")
                    await self.cancel_subscription(subscription_id)
                    
        except asyncio.CancelledError:
            logger.info("Cleanup task cancelled")
        except Exception as e:
            logger.error(f"Cleanup task error: {e}")
    
    @trace_method(name="get_metrics", kind="INTERNAL")
    async def get_metrics(self) -> Dict[str, Any]:
        """Get subscription manager metrics."""
        uptime = time.time() - self.start_time
        
        return {
            "total_subscriptions": len(self.subscriptions),
            "active_subscriptions": len([s for s in self.subscriptions.values() if s.status == SubscriptionStatus.ACTIVE]),
            "total_messages_received": self.total_messages_received,
            "total_messages_delivered": self.total_messages_delivered,
            "total_messages_failed": self.total_messages_failed,
            "uptime_seconds": uptime,
            "messages_per_second": self.total_messages_received / uptime if uptime > 0 else 0,
            "delivery_rate": (self.total_messages_delivered / self.total_messages_received) * 100 if self.total_messages_received > 0 else 0
        }
    
    @trace_method(name="health_check", kind="INTERNAL")
    async def health_check(self) -> Dict[str, Any]:
        """Perform health check."""
        if not self.redis_client:
            return {"status": "unhealthy", "error": "Not initialized"}
        
        try:
            # Test Redis connection
            await self.redis_client.ping()
            
            return {
                "status": "healthy",
                "redis_connected": True,
                "active_subscriptions": len([s for s in self.subscriptions.values() if s.status == SubscriptionStatus.ACTIVE]),
                "total_subscriptions": len(self.subscriptions)
            }
            
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return {
                "status": "unhealthy",
                "redis_connected": False,
                "error": str(e)
            }
    
    @trace_method(name="close", kind="INTERNAL")
    async def close(self) -> None:
        """Close the subscription manager."""
        # Cancel all tasks
        if self.message_listener_task:
            self.message_listener_task.cancel()
        if self.cleanup_task:
            self.cleanup_task.cancel()
        
        # Cancel all subscription tasks
        for subscription in self.subscriptions.values():
            if subscription.processor_task:
                subscription.processor_task.cancel()
            if subscription.heartbeat_task:
                subscription.heartbeat_task.cancel()
        
        # Close HTTP session
        if self.http_session:
            await self.http_session.close()
        
        # Close Redis connections
        if self.pubsub:
            await self.pubsub.close()
        if self.pubsub_client:
            await self.pubsub_client.close()
        if self.redis_client:
            await self.redis_client.close()
        if self.redis_pool:
            await self.redis_pool.disconnect()
        
        logger.info("Subscription manager closed")
