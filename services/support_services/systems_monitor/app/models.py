"""
Pydantic models for Service A API.
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field, validator


class ItemStatus(str, Enum):
    """Item status enumeration."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    ARCHIVED = "archived"


class ItemPriority(str, Enum):
    """Item priority enumeration."""
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    CRITICAL = "critical"


# Domain Models
class ItemBase(BaseModel):
    """Base item model."""
    name: str = Field(..., description="Item name", min_length=1, max_length=255)
    description: Optional[str] = Field(None, description="Item description", max_length=1000)
    status: ItemStatus = Field(default=ItemStatus.ACTIVE, description="Item status")
    priority: ItemPriority = Field(default=ItemPriority.NORMAL, description="Item priority")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    
    @validator('name')
    def validate_name(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError("Name cannot be empty")
        return v.strip()


class ItemCreate(ItemBase):
    """Item creation model."""
    pass


class ItemUpdate(BaseModel):
    """Item update model."""
    name: Optional[str] = Field(None, description="Item name", min_length=1, max_length=255)
    description: Optional[str] = Field(None, description="Item description", max_length=1000)
    status: Optional[ItemStatus] = Field(None, description="Item status")
    priority: Optional[ItemPriority] = Field(None, description="Item priority")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")
    
    @validator('name')
    def validate_name(cls, v):
        if v is not None and (not v or len(v.strip()) == 0):
            raise ValueError("Name cannot be empty")
        return v.strip() if v else v


class ItemResponse(ItemBase):
    """Item response model."""
    id: int = Field(..., description="Item ID")
    uuid: str = Field(..., description="Item UUID")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    version: int = Field(default=1, description="Item version for optimistic locking")


class ItemListResponse(BaseModel):
    """Item list response model."""
    items: List[ItemResponse] = Field(..., description="List of items")
    total_count: int = Field(..., description="Total number of items")
    page: int = Field(..., description="Current page number")
    page_size: int = Field(..., description="Page size")
    has_next: bool = Field(..., description="Whether there are more pages")


# Analytics Models
class ItemAnalytics(BaseModel):
    """Item analytics model."""
    total_items: int = Field(..., description="Total number of items")
    items_by_status: Dict[str, int] = Field(..., description="Items grouped by status")
    items_by_priority: Dict[str, int] = Field(..., description="Items grouped by priority")
    recent_activity: List[Dict[str, Any]] = Field(..., description="Recent activity")
    trends: Dict[str, Any] = Field(..., description="Trend data")
    created_at: datetime = Field(..., description="Analytics generation timestamp")


class ItemMetrics(BaseModel):
    """Item metrics model."""
    service_name: str = Field(..., description="Service name")
    timestamp: datetime = Field(..., description="Metrics timestamp")
    total_items: int = Field(..., description="Total items count")
    active_items: int = Field(..., description="Active items count")
    items_created_today: int = Field(..., description="Items created today")
    items_updated_today: int = Field(..., description="Items updated today")
    avg_processing_time: float = Field(..., description="Average processing time in seconds")
    error_rate: float = Field(..., description="Error rate percentage")


# Event Models
class ItemEvent(BaseModel):
    """Item domain event model."""
    event_type: str = Field(..., description="Event type")
    item_id: int = Field(..., description="Item ID")
    item_uuid: str = Field(..., description="Item UUID")
    event_data: Dict[str, Any] = Field(..., description="Event data")
    correlation_id: Optional[str] = Field(None, description="Correlation ID")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Event metadata")
    
    @validator('event_type')
    def validate_event_type(cls, v):
        allowed_types = [
            "item.created", "item.updated", "item.deleted",
            "item.status_changed", "item.priority_changed"
        ]
        if v not in allowed_types:
            raise ValueError(f"Event type must be one of: {allowed_types}")
        return v


class EventCallback(BaseModel):
    """Event callback payload model."""
    subscription_id: str = Field(..., description="Subscription ID")
    message_id: str = Field(..., description="Message ID")
    channel: str = Field(..., description="Source channel")
    payload: Union[Dict[str, Any], str] = Field(..., description="Event payload")
    metadata: Dict[str, Any] = Field(..., description="Event metadata")
    delivery_attempt: int = Field(..., description="Delivery attempt number")
    delivered_at: datetime = Field(..., description="Delivery timestamp")


# Command Models (CQRS)
class CreateItemCommand(BaseModel):
    """Command to create an item."""
    command_type: str = Field(default="create_item", description="Command type")
    data: ItemCreate = Field(..., description="Item creation data")
    correlation_id: Optional[str] = Field(None, description="Correlation ID")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Command metadata")


class UpdateItemCommand(BaseModel):
    """Command to update an item."""
    command_type: str = Field(default="update_item", description="Command type")
    item_id: int = Field(..., description="Item ID to update")
    data: ItemUpdate = Field(..., description="Item update data")
    correlation_id: Optional[str] = Field(None, description="Correlation ID")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Command metadata")


class DeleteItemCommand(BaseModel):
    """Command to delete an item."""
    command_type: str = Field(default="delete_item", description="Command type")
    item_id: int = Field(..., description="Item ID to delete")
    correlation_id: Optional[str] = Field(None, description="Correlation ID")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Command metadata")


# Query Models (CQRS)
class GetItemQuery(BaseModel):
    """Query to get an item by ID."""
    query_type: str = Field(default="get_item", description="Query type")
    item_id: int = Field(..., description="Item ID")
    include_metadata: bool = Field(default=True, description="Include metadata in response")


class ListItemsQuery(BaseModel):
    """Query to list items with filters."""
    query_type: str = Field(default="list_items", description="Query type")
    status: Optional[ItemStatus] = Field(None, description="Filter by status")
    priority: Optional[ItemPriority] = Field(None, description="Filter by priority")
    search: Optional[str] = Field(None, description="Search term")
    page: int = Field(default=1, description="Page number", ge=1)
    page_size: int = Field(default=20, description="Page size", ge=1, le=100)
    sort_by: str = Field(default="created_at", description="Sort field")
    sort_order: str = Field(default="desc", description="Sort order")
    
    @validator('sort_order')
    def validate_sort_order(cls, v):
        if v not in ['asc', 'desc']:
            raise ValueError("Sort order must be 'asc' or 'desc'")
        return v


class GetAnalyticsQuery(BaseModel):
    """Query to get analytics data."""
    query_type: str = Field(default="get_analytics", description="Query type")
    start_date: Optional[datetime] = Field(None, description="Start date for analytics")
    end_date: Optional[datetime] = Field(None, description="End date for analytics")
    include_trends: bool = Field(default=True, description="Include trend analysis")
    group_by: Optional[str] = Field(None, description="Group analytics by field")


# Health and Status Models
class DependencyStatus(BaseModel):
    """Dependency status model."""
    service_name: str = Field(..., description="Dependency service name")
    url: str = Field(..., description="Service URL")
    status: str = Field(..., description="Connection status")
    response_time_ms: float = Field(..., description="Response time in milliseconds")
    last_check: datetime = Field(..., description="Last health check timestamp")
    error: Optional[str] = Field(None, description="Error message if unhealthy")


class ServiceHealth(BaseModel):
    """Service health status model."""
    status: str = Field(..., description="Service status")
    timestamp: datetime = Field(..., description="Health check timestamp")
    dependencies: List[DependencyStatus] = Field(..., description="List of dependency statuses")
    active_subscriptions: int = Field(..., description="Number of active event subscriptions")
    uptime_seconds: float = Field(..., description="Service uptime in seconds")
    version: str = Field(..., description="Service version")
    error: Optional[str] = Field(None, description="Error message if unhealthy")


# Error Models
class ErrorResponse(BaseModel):
    """Error response model."""
    error: str = Field(..., description="Error message")
    error_code: Optional[str] = Field(None, description="Error code")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Error timestamp")
    request_id: Optional[str] = Field(None, description="Request ID for tracking")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional error details")


class ValidationError(BaseModel):
    """Validation error model."""
    field: str = Field(..., description="Field with validation error")
    message: str = Field(..., description="Validation error message")
    value: Any = Field(None, description="Invalid value")


class ValidationErrorResponse(ErrorResponse):
    """Validation error response model."""
    validation_errors: List[ValidationError] = Field(..., description="List of validation errors")
