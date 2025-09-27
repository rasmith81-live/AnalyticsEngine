# Strategy Service

## Overview

Service A - Business logic service demonstrating CQRS and event-driven architecture.

This service:
- Uses Database Service for all CQRS operations
- Uses Messaging Service for event publishing and subscription
- Implements business logic for item management
- Demonstrates real-time processing and analytics

## Data Models

### `ItemBase`

Base item model.

**Fields:**

- `name`: `str`
- `description`: `Optional[str]`
- `status`: `ItemStatus`
- `priority`: `ItemPriority`
- `metadata`: `Dict[str, Any]`

### `ItemUpdate`

Item update model.

**Fields:**

- `name`: `Optional[str]`
- `description`: `Optional[str]`
- `status`: `Optional[ItemStatus]`
- `priority`: `Optional[ItemPriority]`
- `metadata`: `Optional[Dict[str, Any]]`

### `ItemListResponse`

Item list response model.

**Fields:**

- `items`: `List[ItemResponse]`
- `total_count`: `int`
- `page`: `int`
- `page_size`: `int`
- `has_next`: `bool`

### `ItemAnalytics`

Item analytics model.

**Fields:**

- `total_items`: `int`
- `items_by_status`: `Dict[str, int]`
- `items_by_priority`: `Dict[str, int]`
- `recent_activity`: `List[Dict[str, Any]]`
- `trends`: `Dict[str, Any]`
- `created_at`: `datetime`

### `ItemMetrics`

Item metrics model.

**Fields:**

- `service_name`: `str`
- `timestamp`: `datetime`
- `total_items`: `int`
- `active_items`: `int`
- `items_created_today`: `int`
- `items_updated_today`: `int`
- `avg_processing_time`: `float`
- `error_rate`: `float`

### `ItemEvent`

Item domain event model.

**Fields:**

- `event_type`: `str`
- `item_id`: `int`
- `item_uuid`: `str`
- `event_data`: `Dict[str, Any]`
- `correlation_id`: `Optional[str]`
- `metadata`: `Dict[str, Any]`

### `EventCallback`

Event callback payload model.

**Fields:**

- `subscription_id`: `str`
- `message_id`: `str`
- `channel`: `str`
- `payload`: `Union[Dict[str, Any], str]`
- `metadata`: `Dict[str, Any]`
- `delivery_attempt`: `int`
- `delivered_at`: `datetime`

### `CreateItemCommand`

Command to create an item.

**Fields:**

- `command_type`: `str`
- `data`: `ItemCreate`
- `correlation_id`: `Optional[str]`
- `metadata`: `Dict[str, Any]`

### `UpdateItemCommand`

Command to update an item.

**Fields:**

- `command_type`: `str`
- `item_id`: `int`
- `data`: `ItemUpdate`
- `correlation_id`: `Optional[str]`
- `metadata`: `Dict[str, Any]`

### `DeleteItemCommand`

Command to delete an item.

**Fields:**

- `command_type`: `str`
- `item_id`: `int`
- `correlation_id`: `Optional[str]`
- `metadata`: `Dict[str, Any]`

### `GetItemQuery`

Query to get an item by ID.

**Fields:**

- `query_type`: `str`
- `item_id`: `int`
- `include_metadata`: `bool`

### `ListItemsQuery`

Query to list items with filters.

**Fields:**

- `query_type`: `str`
- `status`: `Optional[ItemStatus]`
- `priority`: `Optional[ItemPriority]`
- `search`: `Optional[str]`
- `page`: `int`
- `page_size`: `int`
- `sort_by`: `str`
- `sort_order`: `str`

### `GetAnalyticsQuery`

Query to get analytics data.

**Fields:**

- `query_type`: `str`
- `start_date`: `Optional[datetime]`
- `end_date`: `Optional[datetime]`
- `include_trends`: `bool`
- `group_by`: `Optional[str]`

### `DependencyStatus`

Dependency status model.

**Fields:**

- `service_name`: `str`
- `url`: `str`
- `status`: `str`
- `response_time_ms`: `float`
- `last_check`: `datetime`
- `error`: `Optional[str]`

### `ServiceHealth`

Service health status model.

**Fields:**

- `status`: `str`
- `timestamp`: `datetime`
- `dependencies`: `List[DependencyStatus]`
- `active_subscriptions`: `int`
- `uptime_seconds`: `float`
- `version`: `str`
- `error`: `Optional[str]`

### `ErrorResponse`

Error response model.

**Fields:**

- `error`: `str`
- `error_code`: `Optional[str]`
- `timestamp`: `datetime`
- `request_id`: `Optional[str]`
- `details`: `Optional[Dict[str, Any]]`

### `ValidationError`

Validation error model.

**Fields:**

- `field`: `str`
- `message`: `str`
- `value`: `Any`

