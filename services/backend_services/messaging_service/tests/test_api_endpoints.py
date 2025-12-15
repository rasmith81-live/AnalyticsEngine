
import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, AsyncMock, patch
import sys
import os
from datetime import datetime, timezone

# Add service root to path
service_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if service_root not in sys.path:
    sys.path.insert(0, service_root)

# Remove app modules if they were already loaded
for module in list(sys.modules.keys()):
    if module.startswith("app."):
        del sys.modules[module]

# Mock app.telemetry
mock_telemetry = MagicMock()
def mock_trace_method(name, kind="INTERNAL"):
    def decorator(func):
        return func
    return decorator

def mock_traced_span(name, kind="INTERNAL", attributes=None):
    return MagicMock()

mock_telemetry.trace_method = mock_trace_method
mock_telemetry.traced_span = mock_traced_span
mock_telemetry.add_span_attributes = MagicMock()
mock_telemetry.inject_trace_context = MagicMock()
mock_telemetry.extract_correlation_id_from_headers = MagicMock(return_value="test-correlation-id")
mock_telemetry.extract_correlation_id = MagicMock(return_value="test-correlation-id")
mock_telemetry.instrument_fastapi = MagicMock()

sys.modules["app.telemetry"] = mock_telemetry

# Mock app.metrics
mock_metrics = MagicMock()

def passthrough_decorator(func):
    return func

def mock_track_redis_op(operation_name=None, operation=None):
    return passthrough_decorator

def mock_track_message_proc(subscription_id=None):
    return passthrough_decorator

mock_metrics.track_endpoint_execution = passthrough_decorator
mock_metrics.track_redis_operation = mock_track_redis_op
mock_metrics.track_message_processing = mock_track_message_proc
mock_metrics.track_message_publish = passthrough_decorator
mock_metrics.update_system_metrics = MagicMock()
mock_metrics.update_redis_connection_metrics = MagicMock()
mock_metrics.export_metrics_to_observability = AsyncMock()
mock_metrics.metrics = MagicMock()

sys.modules["app.metrics"] = mock_metrics

# Mock other dependencies to avoid importing real logic
sys.modules["app.event_publisher"] = MagicMock()
sys.modules["app.subscription_manager"] = MagicMock()

from app.main import app, get_event_publisher, get_subscription_manager
from app.models import MessageMetadata

client = TestClient(app)

# Fixtures for mocked dependencies
@pytest.fixture
def mock_event_publisher():
    publisher = MagicMock()
    # Explicitly set AsyncMocks for methods called with await
    publisher.publish = AsyncMock(return_value="msg-123")
    publisher.publish_message = AsyncMock(return_value="msg-123")
    publisher.publish_bulk = AsyncMock(return_value={
        "published_count": 2,
        "failed_count": 0,
        "results": [{"success": True, "message_id": "msg-1", "channel": "chan1"}, 
                   {"success": True, "message_id": "msg-2", "channel": "chan2"}]
    })
    publisher.publish_event = AsyncMock(return_value={
        "event_id": "evt-123",
        "published_channels": ["events.test"],
        "timestamp": datetime.now(timezone.utc).isoformat()
    })
    publisher.get_channel_info = AsyncMock(return_value={
        "name": "test-channel",
        "subscriber_count": 5,
        "message_count": 100,
        "last_activity": datetime.now(timezone.utc).isoformat(),
        "is_active": True
    })
    publisher.get_metrics = AsyncMock(return_value={
        "published_count": 100,
        "failed_count": 1,
        "total_bytes_sent": 1000,
        "active_channels_count": 5,
        "uptime_seconds": 3600,
        "messages_per_second": 10.0,
        "error_rate": 0.01,
        "avg_message_size": 100
    })
    publisher.health_check = AsyncMock(return_value={
        "status": "healthy",
        "redis_connected": True,
        "active_channels": 5
    })
    publisher.max_message_size = 1024 * 1024
    return publisher

@pytest.fixture
def mock_subscription_manager():
    manager = MagicMock()
    # Explicitly set AsyncMocks
    manager.create_subscription = AsyncMock(return_value=("sub-123", datetime.now(timezone.utc), "active"))
    manager.cancel_subscription = AsyncMock(return_value={"success": True})
    manager.get_subscription_info = AsyncMock(return_value={
        "subscription_id": "sub-123",
        "channel_pattern": "test",
        "service_name": "test-service",
        "status": "active",
        "callback_url": "http://webhook",
        "max_delivery_attempts": 3,
        "ack_timeout": 30,
        "batch_size": 1,
        "auto_ack": False,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "message_count": 10,
        "error_count": 0,
        "pending_messages": 0
    })
    manager.list_subscriptions = AsyncMock(return_value=[])
    manager.acknowledge_message = AsyncMock(return_value={"success": True})
    manager.get_metrics = AsyncMock(return_value={
        "total_subscriptions": 10,
        "active_subscriptions": 8,
        "total_messages_delivered": 500,
        "total_messages_failed": 5
    })
    manager.health_check = AsyncMock(return_value={
        "status": "healthy",
        "active_subscriptions": 8
    })
    return manager

@pytest.fixture
def override_dependencies(mock_event_publisher, mock_subscription_manager):
    app.dependency_overrides[get_event_publisher] = lambda: mock_event_publisher
    app.dependency_overrides[get_subscription_manager] = lambda: mock_subscription_manager
    yield
    app.dependency_overrides = {}

def dump_error(response, test_name):
    if response.status_code != 200:
        with open(f"test_error_{test_name}.log", "w") as f:
            f.write(f"Status: {response.status_code}\n")
            f.write(f"Response: {response.json()}\n")

def test_health_check(override_dependencies):
    response = client.get("/health")
    dump_error(response, "health_check")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["redis_connected"] is True

def test_publish_message(override_dependencies, mock_event_publisher):
    payload = {
        "channel": "test-channel",
        "payload": {"key": "value"},
        "service_name": "test-service"
    }
    response = client.post("/messaging/publish", json=payload)
    dump_error(response, "publish_message")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["message_id"] == "msg-123"
    
    # Verify publisher call
    mock_event_publisher.publish_message.assert_awaited_once()

def test_publish_bulk(override_dependencies, mock_event_publisher):
    payload = {
        "messages": [
            {"channel": "chan1", "payload": "msg1", "service_name": "svc"},
            {"channel": "chan2", "payload": "msg2", "service_name": "svc"}
        ],
        "service_name": "svc"
    }
    response = client.post("/messaging/publish/bulk", json=payload)
    dump_error(response, "publish_bulk")
    assert response.status_code == 200
    data = response.json()
    assert data["published_count"] == 2
    
    mock_event_publisher.publish_bulk.assert_awaited_once()

def test_publish_event(override_dependencies, mock_event_publisher):
    payload = {
        "event_type": "user.created",
        "source_service": "user-service",
        "event_data": {"user_id": 1}
    }
    response = client.post("/messaging/events/publish", json=payload)
    dump_error(response, "publish_event")
    assert response.status_code == 200
    data = response.json()
    assert data["event_id"] == "evt-123"
    
    mock_event_publisher.publish_event.assert_awaited_once()

def test_publish_command(override_dependencies, mock_event_publisher):
    payload = {
        "command_type": "CreateUser",
        "payload": {"username": "testuser"},
        "service_name": "user-service"
    }
    response = client.post("/messaging/commands/publish", json=payload)
    dump_error(response, "publish_command")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["command_id"] == "msg-123"
    
    # Verify publisher call
    mock_event_publisher.publish_message.assert_awaited_once()
    # Check channel formatting
    call_kwargs = mock_event_publisher.publish_message.call_args.kwargs
    assert call_kwargs['channel'] == "commands.CreateUser"

def test_create_subscription(override_dependencies, mock_subscription_manager):
    payload = {
        "service_name": "test-service",
        "callback_url": "http://webhook",
        "channel": "test-channel"
    }
    response = client.post("/messaging/subscriptions", json=payload)
    dump_error(response, "create_subscription")
    assert response.status_code == 200
    data = response.json()
    assert data["subscription_id"] == "sub-123"
    assert data["status"] == "active"
    
    mock_subscription_manager.create_subscription.assert_awaited_once()

def test_get_subscription_info(override_dependencies, mock_subscription_manager):
    response = client.get("/messaging/subscriptions/sub-123")
    dump_error(response, "get_subscription_info")
    assert response.status_code == 200
    data = response.json()
    assert data["subscription_id"] == "sub-123"
    
    mock_subscription_manager.get_subscription_info.assert_awaited_once_with("sub-123")

def test_acknowledge_message(override_dependencies, mock_subscription_manager):
    payload = {
        "message_id": "msg-1",
        "subscription_id": "sub-1",
        "success": True
    }
    response = client.post("/messaging/acknowledge", json=payload)
    dump_error(response, "acknowledge_message")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    
    mock_subscription_manager.acknowledge_message.assert_awaited_once()

def test_get_metrics(override_dependencies):
    response = client.get("/messaging/metrics")
    dump_error(response, "get_metrics")
    assert response.status_code == 200
    data = response.json()
    assert "total_messages_published" in data
    assert "active_subscriptions" in data
