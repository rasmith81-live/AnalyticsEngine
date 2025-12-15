
import pytest
from unittest.mock import MagicMock, patch, AsyncMock
import sys
import os
import json
import uuid
import asyncio
from datetime import datetime, timezone

# Mock app.telemetry before importing app.subscription_manager
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
mock_telemetry.extract_trace_context = MagicMock(return_value={})

sys.modules["app.telemetry"] = mock_telemetry

# Add service root to path
service_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if service_root not in sys.path:
    sys.path.insert(0, service_root)

# Clean up sys.modules to ensure we import real modules, but keep app.telemetry mock
for module in list(sys.modules.keys()):
    if module.startswith("app.") and module != "app.telemetry":
        del sys.modules[module]

from app.subscription_manager import SubscriptionManager, Subscription, SubscriptionStatus
from app.models import MessageDelivery, MessageMetadata

@pytest.fixture
def mock_redis():
    mock = MagicMock()
    mock.pipeline = MagicMock(return_value=AsyncMock())
    return mock

@pytest.fixture
def manager():
    mgr = SubscriptionManager(redis_url="redis://localhost:6379/0")
    mgr.redis_client = AsyncMock()
    mgr.pubsub_client = AsyncMock()
    mgr.pubsub = AsyncMock()
    mgr.http_session = AsyncMock()
    return mgr

@pytest.mark.asyncio
async def test_create_subscription(manager):
    """Test creating a subscription."""
    service_name = "test-service"
    callback_url = "http://test-service/webhook"
    channel = "test-channel"
    
    # Mock internal methods to avoid actual redis calls or background tasks
    with patch.object(manager, '_subscribe_to_channel', new_callable=AsyncMock) as mock_sub, \
         patch.object(manager, '_process_subscription_messages', new_callable=AsyncMock), \
         patch.object(manager, '_subscription_heartbeat', new_callable=AsyncMock):
        
        sub_id, created_at, status = await manager.create_subscription(
            service_name=service_name,
            callback_url=callback_url,
            channel=channel
        )
        
        assert sub_id is not None
        assert status == SubscriptionStatus.ACTIVE
        assert sub_id in manager.subscriptions
        
        sub = manager.subscriptions[sub_id]
        assert sub.service_name == service_name
        assert sub.callback_url == callback_url
        assert sub.channel_pattern == channel
        
        mock_sub.assert_awaited_once_with(channel)

@pytest.mark.asyncio
async def test_handle_message_routing(manager):
    """Test that received messages are routed to correct subscriptions."""
    # Setup subscription
    sub = Subscription(
        subscription_id="sub-1",
        channel_pattern="events.*",
        service_name="test-service"
    )
    manager.subscriptions["sub-1"] = sub
    manager.channel_subscriptions["events.*"] = {"sub-1"}
    
    # Mock delivery method
    with patch.object(manager, '_deliver_message_to_subscription', new_callable=AsyncMock) as mock_deliver:
        
        # Simulate incoming redis message
        channel = "events.user.created"
        payload = {"user_id": "123"}
        message_data = json.dumps({
            "payload": payload,
            "metadata": {"message_id": "msg-1"}
        }).encode('utf-8')
        
        redis_message = {
            "type": "message",
            "channel": channel.encode('utf-8'),
            "data": message_data
        }
        
        await manager._handle_message(redis_message)
        
        # Verify delivery called
        mock_deliver.assert_awaited_once()
        args = mock_deliver.call_args
        assert args[0][0].subscription_id == "sub-1" # subscription arg
        assert args[0][1] == channel # channel arg
        assert args[0][2] == payload # payload arg

@pytest.mark.asyncio
async def test_deliver_via_webhook_success(manager):
    """Test successful webhook delivery."""
    sub = Subscription(
        subscription_id="sub-1",
        channel_pattern="test",
        service_name="test-service",
        callback_url="http://webhook"
    )
    
    msg = MessageDelivery(
        message_id="msg-1",
        subscription_id="sub-1",
        channel="test",
        payload={"data": "test"},
        metadata=MessageMetadata(message_id="msg-1"),
        delivery_attempt=1,
        max_attempts=3,
        delivered_at=datetime.now(timezone.utc)
    )
    
    # Mock http session post
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.__aenter__.return_value = mock_response
    mock_response.__aexit__.return_value = None
    
    # Configure post to be a MagicMock (synchronous) that returns the context manager
    manager.http_session.post = MagicMock(return_value=mock_response)
    
    success = await manager._deliver_via_webhook(sub, msg)
    
    assert success is True
    manager.http_session.post.assert_called_once()
    
    # Verify payload contains expected fields
    call_kwargs = manager.http_session.post.call_args[1]
    json_body = call_kwargs['json']
    assert json_body['message_id'] == "msg-1"
    assert json_body['payload'] == {"data": "test"}

@pytest.mark.asyncio
async def test_deliver_via_webhook_failure(manager):
    """Test webhook delivery failure."""
    sub = Subscription(
        subscription_id="sub-1",
        channel_pattern="test",
        service_name="test-service",
        callback_url="http://webhook"
    )
    
    msg = MessageDelivery(
        message_id="msg-1",
        subscription_id="sub-1",
        channel="test",
        payload={"data": "test"},
        metadata=MessageMetadata(message_id="msg-1"),
        delivery_attempt=1,
        max_attempts=3,
        delivered_at=datetime.now(timezone.utc)
    )
    
    # Mock http session post to fail
    mock_response = AsyncMock()
    mock_response.status = 500
    mock_response.text.return_value = "Internal Server Error"
    mock_response.__aenter__.return_value = mock_response
    mock_response.__aexit__.return_value = None
    
    manager.http_session.post = MagicMock(return_value=mock_response)
    
    success = await manager._deliver_via_webhook(sub, msg)
    
    assert success is False

@pytest.mark.asyncio
async def test_retry_logic(manager):
    """Test retry logic when ack timeout occurs."""
    sub = Subscription(
        subscription_id="sub-1",
        channel_pattern="test",
        service_name="test-service",
        max_delivery_attempts=3,
        ack_timeout=0.1 # Short timeout
    )
    
    msg = MessageDelivery(
        message_id="msg-1",
        subscription_id="sub-1",
        channel="test",
        payload={"data": "test"},
        metadata=MessageMetadata(message_id="msg-1"),
        delivery_attempt=1,
        max_attempts=3,
        delivered_at=datetime.now(timezone.utc)
    )
    
    # Setup pending message
    sub.pending_messages["msg-1"] = {
        "timestamp": datetime.now(timezone.utc).timestamp(),
        "attempts": 1
    }
    
    # Mock queue put (re-queueing) and asyncio.sleep
    with patch.object(sub.message_queue, 'put', new_callable=AsyncMock) as mock_put, \
         patch('asyncio.sleep', new_callable=AsyncMock) as mock_sleep:
        await manager._handle_ack_timeout(sub, msg)
        
        # Should be re-queued with incremented attempt
        mock_put.assert_awaited_once()
        args = mock_put.call_args[0]
        queued_msg = args[0]
        assert queued_msg.delivery_attempt == 2

@pytest.mark.asyncio
async def test_dlq_logic_max_attempts(manager):
    """Test logic when max attempts reached (DLQ behavior)."""
    sub = Subscription(
        subscription_id="sub-1",
        channel_pattern="test",
        service_name="test-service",
        max_delivery_attempts=3
    )
    
    msg = MessageDelivery(
        message_id="msg-1",
        subscription_id="sub-1",
        channel="test",
        payload={"data": "test"},
        metadata=MessageMetadata(message_id="msg-1"),
        delivery_attempt=3, # Already at max
        max_attempts=3,
        delivered_at=datetime.now(timezone.utc)
    )
    
    # Setup pending message
    sub.pending_messages["msg-1"] = {
        "timestamp": datetime.now(timezone.utc).timestamp(),
        "attempts": 3
    }
    
    # Mock acknowledge_message and asyncio.sleep to avoid waiting
    with patch.object(manager, 'acknowledge_message', new_callable=AsyncMock) as mock_ack, \
         patch.object(sub.message_queue, 'put', new_callable=AsyncMock) as mock_put, \
         patch('asyncio.sleep', new_callable=AsyncMock) as mock_sleep:
        
        await manager._handle_ack_timeout(sub, msg)
        
        # Should NOT be re-queued
        mock_put.assert_not_awaited()
        
        # Should be acknowledged as failed
        mock_ack.assert_awaited_once_with("sub-1", "msg-1", False, "Max delivery attempts exceeded")
