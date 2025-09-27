# Messaging Service

## Overview

Messaging Service - Centralized Redis pub/sub messaging for microservices.

This service consolidates all messaging functionality:
- Event publishing and subscription management
- Redis pub/sub operations
- Message routing and delivery
- Webhook notifications
- Dead letter queue handling

## Data Models

### `MessageMetadata`

Message metadata.

**Fields:**

- `message_id`: `str`
- `correlation_id`: `Optional[str]`
- `reply_to`: `Optional[str]`
- `content_type`: `str`
- `content_encoding`: `Optional[str]`
- `priority`: `MessagePriority`
- `ttl`: `Optional[int]`
- `timestamp`: `datetime`
- `headers`: `Dict[str, Any]`

### `PublishMessageRequest`

Request to publish a message.

**Fields:**

- `channel`: `str`
- `payload`: `Union[Dict[str, Any], str, bytes]`
- `metadata`: `Optional[MessageMetadata]`
- `service_name`: `str`
- `persistent`: `bool`

### `PublishMessageResponse`

Response from publishing a message.

**Fields:**

- `success`: `bool`
- `message_id`: `str`
- `channel`: `str`
- `timestamp`: `datetime`
- `correlation_id`: `str`
- `error`: `Optional[str]`

### `BulkPublishRequest`

Request to publish multiple messages.

**Fields:**

- `messages`: `List[PublishMessageRequest]`
- `service_name`: `str`
- `fail_on_error`: `bool`

### `BulkPublishResponse`

Response from bulk publishing.

**Fields:**

- `success`: `bool`
- `published_count`: `int`
- `failed_count`: `int`
- `results`: `List[PublishMessageResponse]`

### `SubscriptionRequest`

Request to create a subscription.

**Fields:**

- `service_name`: `str`
- `callback_url`: `str`
- `channel`: `Optional[str]`
- `channel_pattern`: `Optional[str]`
- `filter_criteria`: `Optional[Dict[str, Any]]`
- `headers`: `Optional[Dict[str, str]]`
- `max_retries`: `int`
- `retry_delay`: `int`

### `SubscriptionResponse`

Response from creating a subscription.

**Fields:**

- `success`: `bool`
- `subscription_id`: `str`
- `channel`: `Optional[str]`
- `channel_pattern`: `Optional[str]`
- `service_name`: `str`
- `status`: `SubscriptionStatus`
- `created_at`: `datetime`
- `error`: `Optional[str]`

### `SubscriptionInfo`

Subscription information.

**Fields:**

- `subscription_id`: `str`
- `channel_pattern`: `str`
- `service_name`: `str`
- `status`: `SubscriptionStatus`
- `callback_url`: `Optional[str]`
- `max_delivery_attempts`: `int`
- `ack_timeout`: `int`
- `batch_size`: `int`
- `auto_ack`: `bool`
- `created_at`: `datetime`
- `last_activity`: `Optional[datetime]`
- `message_count`: `int`
- `error_count`: `int`

### `MessageAcknowledgment`

Message acknowledgment.

**Fields:**

- `message_id`: `str`
- `subscription_id`: `str`
- `success`: `bool`
- `error`: `Optional[str]`

### `MessageDelivery`

Message delivery information.

**Fields:**

- `message_id`: `str`
- `subscription_id`: `str`
- `channel`: `str`
- `payload`: `Union[Dict[str, Any], str]`
- `metadata`: `MessageMetadata`
- `delivery_attempt`: `int`
- `max_attempts`: `int`
- `delivered_at`: `datetime`

### `ChannelInfo`

Channel information.

**Fields:**

- `name`: `str`
- `subscriber_count`: `int`
- `message_count`: `int`
- `last_activity`: `Optional[datetime]`
- `created_at`: `datetime`

### `ChannelStats`

Channel statistics.

**Fields:**

- `name`: `str`
- `messages_published`: `int`
- `messages_delivered`: `int`
- `messages_failed`: `int`
- `active_subscriptions`: `int`
- `avg_delivery_time`: `float`
- `last_24h_activity`: `int`

### `EventRequest`

Request to publish an event.

**Fields:**

- `event_type`: `str`
- `source_service`: `str`
- `event_data`: `Dict[str, Any]`
- `correlation_id`: `Optional[str]`
- `metadata`: `Dict[str, Any]`

### `EventResponse`

Response from publishing an event.

**Fields:**

- `success`: `bool`
- `event_id`: `str`
- `event_type`: `str`
- `published_at`: `datetime`
- `channels`: `List[str]`
- `error`: `Optional[str]`

### `PublishCommandRequest`

Request to publish a command.

**Fields:**

- `command_type`: `str`
- `payload`: `Dict[str, Any]`
- `service_name`: `str`
- `correlation_id`: `Optional[str]`
- `metadata`: `Optional[Dict[str, Any]]`

### `CommandReceipt`

Receipt for a successfully published command.

**Fields:**

- `success`: `bool`
- `command_id`: `str`
- `timestamp`: `datetime`
- `correlation_id`: `str`
- `error`: `Optional[str]`

### `HealthResponse`

Health check response.

**Fields:**

- `status`: `str`
- `timestamp`: `datetime`
- `redis_connected`: `bool`
- `active_subscriptions`: `int`
- `active_channels`: `int`
- `uptime_seconds`: `float`
- `version`: `str`
- `environment`: `str`
- `service_name`: `str`
- `error`: `Optional[str]`
- `correlation_id`: `str`

### `MetricsResponse`

Metrics response.

**Fields:**

- `service_name`: `str`
- `timestamp`: `datetime`
- `total_messages_published`: `int`
- `total_messages_delivered`: `int`
- `total_messages_failed`: `int`
- `active_subscriptions`: `int`
- `active_channels`: `int`
- `redis_memory_usage`: `Optional[int]`
- `avg_message_size`: `float`
- `messages_per_second`: `float`
- `error_rate`: `float`

### `ErrorResponse`

Error response.

**Fields:**

- `error`: `str`
- `error_code`: `Optional[str]`
- `timestamp`: `datetime`
- `request_id`: `Optional[str]`
- `details`: `Optional[Dict[str, Any]]`

