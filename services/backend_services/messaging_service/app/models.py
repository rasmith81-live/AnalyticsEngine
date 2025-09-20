"""
Pydantic models for the Messaging Service API.
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field, model_validator, validator


class MessagePriority(str, Enum):
    """Message priority levels."""
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    CRITICAL = "critical"


class MessageStatus(str, Enum):
    """Message processing status."""
    PENDING = "pending"
    PROCESSING = "processing"
    DELIVERED = "delivered"
    FAILED = "failed"
    EXPIRED = "expired"


class SubscriptionStatus(str, Enum):
    """Subscription status."""
    ACTIVE = "active"
    PAUSED = "paused"
    CANCELLED = "cancelled"
    ERROR = "error"


# Message Models
class MessageMetadata(BaseModel):
    """Message metadata."""
    message_id: str = Field(..., description="Unique message identifier")
    correlation_id: Optional[str] = Field(None, description="Correlation identifier")
    reply_to: Optional[str] = Field(None, description="Reply-to channel")
    content_type: str = Field(default="application/json", description="Content type")
    content_encoding: Optional[str] = Field(None, description="Content encoding")
    priority: MessagePriority = Field(default=MessagePriority.NORMAL, description="Message priority")
    ttl: Optional[int] = Field(None, description="Time to live in seconds")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Message timestamp")
    headers: Dict[str, Any] = Field(default_factory=dict, description="Custom headers")


class PublishMessageRequest(BaseModel):
    """Request to publish a message."""
    channel: str = Field(..., description="Target channel")
    payload: Union[Dict[str, Any], str, bytes] = Field(..., description="Message payload")
    metadata: Optional[MessageMetadata] = Field(None, description="Message metadata")
    service_name: str = Field(..., description="Publishing service name")
    persistent: bool = Field(default=True, description="Whether to persist the message")
    
    @validator('channel')
    def validate_channel(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError("Channel cannot be empty")
        return v.strip()


class PublishMessageResponse(BaseModel):
    """Response from publishing a message."""
    success: bool = Field(..., description="Whether publish was successful")
    message_id: str = Field(..., description="Generated message ID")
    channel: str = Field(..., description="Target channel")
    timestamp: datetime = Field(..., description="Publish timestamp")
    correlation_id: str = Field(..., description="Correlation ID for distributed tracing")
    error: Optional[str] = Field(None, description="Error message if failed")


class BulkPublishRequest(BaseModel):
    """Request to publish multiple messages."""
    messages: List[PublishMessageRequest] = Field(..., description="Messages to publish")
    service_name: str = Field(..., description="Publishing service name")
    fail_on_error: bool = Field(default=False, description="Fail entire batch on first error")


class BulkPublishResponse(BaseModel):
    """Response from bulk publishing."""
    success: bool = Field(..., description="Whether bulk publish was successful")
    published_count: int = Field(..., description="Number of successfully published messages")
    failed_count: int = Field(..., description="Number of failed messages")
    results: List[PublishMessageResponse] = Field(..., description="Individual publish results")


# Subscription Models
class SubscriptionRequest(BaseModel):
    """Request to create a subscription."""
    service_name: str = Field(..., description="Subscribing service name")
    callback_url: str = Field(..., description="HTTP callback URL for the subscription.")
    channel: Optional[str] = Field(default=None, description="The specific channel to subscribe to.")
    channel_pattern: Optional[str] = Field(default=None, description="A pattern to subscribe to multiple channels.")
    filter_criteria: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Criteria to filter messages.")
    headers: Optional[Dict[str, str]] = Field(default_factory=dict, description="Headers to be sent with webhook calls.")
    max_retries: int = Field(default=3, ge=0, description="Maximum number of retry attempts for message delivery.")
    retry_delay: int = Field(default=5, ge=1, description="Delay in seconds between retry attempts.")

    @model_validator(mode='before')
    @classmethod
    def check_channel_or_pattern(cls, values):
        if not values.get('channel') and not values.get('channel_pattern'):
            raise ValueError('Either \'channel\' or \'channel_pattern\' must be provided.')
        if values.get('channel') and values.get('channel_pattern'):
            raise ValueError('Only one of \'channel\' or \'channel_pattern\' can be provided.')
        return values


class SubscriptionResponse(BaseModel):
    """Response from creating a subscription."""
    success: bool = Field(..., description="Whether subscription was successful")
    subscription_id: str = Field(..., description="Generated subscription ID")
    channel: Optional[str] = Field(None, description="The specific channel subscribed to.")
    channel_pattern: Optional[str] = Field(None, description="The subscribed channel pattern.")
    service_name: str = Field(..., description="Subscribing service name")
    status: SubscriptionStatus = Field(..., description="Subscription status")
    created_at: datetime = Field(..., description="Subscription creation time")
    error: Optional[str] = Field(None, description="Error message if failed")

    @model_validator(mode='before')
    @classmethod
    def check_channel_or_pattern(cls, values):
        if 'channel' not in values and 'channel_pattern' not in values:
            return values # Allow validation to fail downstream if both are missing
        if not values.get('channel') and not values.get('channel_pattern'):
            raise ValueError('Either \'channel\' or \'channel_pattern\' must be provided in the response.')
        if values.get('channel') and values.get('channel_pattern'):
            raise ValueError('Only one of \'channel\' or \'channel_pattern\' can be provided in the response.')
        return values


class SubscriptionInfo(BaseModel):
    """Subscription information."""
    subscription_id: str = Field(..., description="Subscription ID")
    channel_pattern: str = Field(..., description="Channel pattern")
    service_name: str = Field(..., description="Service name")
    status: SubscriptionStatus = Field(..., description="Current status")
    callback_url: Optional[str] = Field(None, description="Callback URL")
    max_delivery_attempts: int = Field(..., description="Maximum delivery attempts")
    ack_timeout: int = Field(..., description="Acknowledgment timeout")
    batch_size: int = Field(..., description="Message batch size")
    auto_ack: bool = Field(..., description="Auto acknowledgment enabled")
    created_at: datetime = Field(..., description="Creation timestamp")
    last_activity: Optional[datetime] = Field(None, description="Last activity timestamp")
    message_count: int = Field(default=0, description="Total messages received")
    error_count: int = Field(default=0, description="Total error count")


class MessageAcknowledgment(BaseModel):
    """Message acknowledgment."""
    message_id: str = Field(..., description="Message ID to acknowledge")
    subscription_id: str = Field(..., description="Subscription ID")
    success: bool = Field(default=True, description="Whether processing was successful")
    error: Optional[str] = Field(None, description="Error message if processing failed")


class MessageDelivery(BaseModel):
    """Message delivery information."""
    message_id: str = Field(..., description="Message ID")
    subscription_id: str = Field(..., description="Subscription ID")
    channel: str = Field(..., description="Source channel")
    payload: Union[Dict[str, Any], str] = Field(..., description="Message payload")
    metadata: MessageMetadata = Field(..., description="Message metadata")
    delivery_attempt: int = Field(..., description="Current delivery attempt")
    max_attempts: int = Field(..., description="Maximum delivery attempts")
    delivered_at: datetime = Field(..., description="Delivery timestamp")


# Channel Models
class ChannelInfo(BaseModel):
    """Channel information."""
    name: str = Field(..., description="Channel name")
    subscriber_count: int = Field(..., description="Number of active subscribers")
    message_count: int = Field(..., description="Total messages published")
    last_activity: Optional[datetime] = Field(None, description="Last activity timestamp")
    created_at: datetime = Field(..., description="Channel creation timestamp")


class ChannelStats(BaseModel):
    """Channel statistics."""
    name: str = Field(..., description="Channel name")
    messages_published: int = Field(..., description="Messages published count")
    messages_delivered: int = Field(..., description="Messages delivered count")
    messages_failed: int = Field(..., description="Messages failed count")
    active_subscriptions: int = Field(..., description="Active subscriptions count")
    avg_delivery_time: float = Field(..., description="Average delivery time in seconds")
    last_24h_activity: int = Field(..., description="Activity in last 24 hours")


# Event Models
class EventRequest(BaseModel):
    """Request to publish an event."""
    event_type: str = Field(..., description="Event type")
    source_service: str = Field(..., description="Source service name")
    event_data: Dict[str, Any] = Field(..., description="Event data")
    correlation_id: Optional[str] = Field(None, description="Correlation ID")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    
    @validator('event_type')
    def validate_event_type(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError("Event type cannot be empty")
        return v.strip()


class EventResponse(BaseModel):
    """Response from publishing an event."""
    success: bool = Field(..., description="Whether event publish was successful")
    event_id: str = Field(..., description="Generated event ID")
    event_type: str = Field(..., description="Event type")
    published_at: datetime = Field(..., description="Publish timestamp")
    channels: List[str] = Field(..., description="Channels the event was published to")
    error: Optional[str] = Field(None, description="Error message if failed")


# Command Models
class PublishCommandRequest(BaseModel):
    """Request to publish a command."""
    command_type: str = Field(..., description="Type of the command, e.g., 'CreateItemCommand'")
    payload: Dict[str, Any] = Field(..., description="Command payload")
    service_name: str = Field(..., description="Name of the service publishing the command")
    correlation_id: Optional[str] = Field(None, description="Correlation ID for distributed tracing")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional metadata")

    @validator('command_type')
    def validate_command_type(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError("Command type cannot be empty")
        return v.strip()


class CommandReceipt(BaseModel):
    """Receipt for a successfully published command."""
    success: bool = Field(..., description="Whether the command was successfully published")
    command_id: str = Field(..., description="Generated ID for the command")
    timestamp: datetime = Field(..., description="Timestamp of when the command was received")
    correlation_id: str = Field(..., description="Correlation ID for distributed tracing")
    error: Optional[str] = Field(None, description="Error message if publishing failed")


# Health and Monitoring Models
class HealthResponse(BaseModel):
    """Health check response."""
    status: str = Field(..., description="Service status")
    timestamp: datetime = Field(..., description="Health check timestamp")
    redis_connected: bool = Field(..., description="Redis connection status")
    active_subscriptions: int = Field(..., description="Number of active subscriptions")
    active_channels: int = Field(..., description="Number of active channels")
    uptime_seconds: float = Field(..., description="Service uptime in seconds")
    version: str = Field(..., description="Service version")
    environment: str = Field(..., description="Deployment environment")
    service_name: str = Field(..., description="Name of the service")
    error: Optional[str] = Field(None, description="Error message if unhealthy")
    correlation_id: str = Field(..., description="Correlation ID for distributed tracing")


class MetricsResponse(BaseModel):
    """Metrics response."""
    service_name: str = Field(..., description="Service name")
    timestamp: datetime = Field(..., description="Metrics timestamp")
    total_messages_published: int = Field(..., description="Total messages published")
    total_messages_delivered: int = Field(..., description="Total messages delivered")
    total_messages_failed: int = Field(..., description="Total messages failed")
    active_subscriptions: int = Field(..., description="Active subscriptions count")
    active_channels: int = Field(..., description="Active channels count")
    redis_memory_usage: Optional[int] = Field(None, description="Redis memory usage in bytes")
    avg_message_size: float = Field(..., description="Average message size in bytes")
    messages_per_second: float = Field(..., description="Messages per second rate")
    error_rate: float = Field(..., description="Error rate percentage")


# Error Models
class ErrorResponse(BaseModel):
    """Error response."""
    error: str = Field(..., description="Error message")
    error_code: Optional[str] = Field(None, description="Error code")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Error timestamp")
    request_id: Optional[str] = Field(None, description="Request ID for tracking")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional error details")
