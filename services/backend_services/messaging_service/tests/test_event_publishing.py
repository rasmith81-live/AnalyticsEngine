
import pytest
from unittest.mock import MagicMock, patch, AsyncMock
import sys
import os
import json
import gzip
import uuid
from datetime import datetime

# Mock app.telemetry before importing app.event_publisher
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

sys.modules["app.telemetry"] = mock_telemetry

# Add service root to path so 'app' module can be found
service_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if service_root not in sys.path:
    sys.path.insert(0, service_root)

# Clean up sys.modules to ensure we import real modules
for module in list(sys.modules.keys()):
    if module.startswith("app.") and module != "app.telemetry":
        del sys.modules[module]

from app.event_publisher import EventPublisher
from app.models import MessageMetadata
from app.config import Settings

@pytest.fixture
def mock_settings():
    return Settings(
        REDIS_URL="redis://localhost:6379/0",
        REDIS_MAX_CONNECTIONS=10,
        ENABLE_MESSAGE_COMPRESSION=True
    )

@pytest.fixture
def publisher(mock_settings):
    pub = EventPublisher(
        redis_url=mock_settings.redis_url,
        max_connections=mock_settings.redis_max_connections,
        enable_compression=mock_settings.enable_message_compression
    )
    # Mock internal redis client
    pub.redis_client = AsyncMock()
    # Mock pool as well to avoid errors if accessed
    pub.redis_pool = AsyncMock()
    return pub

@pytest.mark.asyncio
async def test_publish_message_basic(publisher):
    """Test basic message publishing."""
    channel = "test-channel"
    payload = {"key": "value"}
    
    # Mock publish return value (subscriber count)
    publisher.redis_client.publish.return_value = 1
    
    msg_id = await publisher.publish_message(channel, payload, persistent=False)
    
    assert msg_id is not None
    publisher.redis_client.publish.assert_called_once()
    
    # Check arguments
    call_args = publisher.redis_client.publish.call_args
    assert call_args[0][0] == channel
    
    # Check payload is valid JSON bytes
    sent_payload = call_args[0][1]
    decoded = json.loads(sent_payload)
    assert decoded["payload"] == payload
    assert decoded["metadata"]["message_id"] == msg_id

@pytest.mark.asyncio
async def test_publish_message_with_correlation_id(publisher):
    """Test publishing with correlation ID."""
    channel = "test-channel"
    payload = "data"
    correlation_id = "corr-123"
    
    publisher.redis_client.publish.return_value = 1
    
    await publisher.publish_message(
        channel, 
        payload, 
        persistent=False,
        correlation_id=correlation_id
    )
    
    call_args = publisher.redis_client.publish.call_args
    sent_payload = call_args[0][1]
    decoded = json.loads(sent_payload)
    
    assert decoded["metadata"]["correlation_id"] == correlation_id

@pytest.mark.asyncio
async def test_publish_message_compression(publisher):
    """Test message compression for large payloads."""
    channel = "test-channel"
    # Create large payload > 1KB
    payload = "x" * 2048
    
    publisher.redis_client.publish.return_value = 1
    
    await publisher.publish_message(channel, payload, persistent=False)
    
    call_args = publisher.redis_client.publish.call_args
    sent_payload = call_args[0][1]
    
    # Verify it is gzipped (starts with magic bytes 1f 8b)
    assert sent_payload.startswith(b'\x1f\x8b')
    
    # Decompress and verify content
    decompressed = gzip.decompress(sent_payload)
    decoded = json.loads(decompressed)
    assert decoded["payload"] == payload
    assert decoded["metadata"]["content_encoding"] == "gzip"

@pytest.mark.asyncio
async def test_publish_message_no_compression_small_payload(publisher):
    """Test that small payloads are not compressed."""
    channel = "test-channel"
    payload = "small"
    
    publisher.redis_client.publish.return_value = 1
    
    await publisher.publish_message(channel, payload, persistent=False)
    
    call_args = publisher.redis_client.publish.call_args
    sent_payload = call_args[0][1]
    
    # Should not be gzipped (checking against magic bytes just in case, but easier to check it's plain JSON)
    assert not sent_payload.startswith(b'\x1f\x8b')
    
    decoded = json.loads(sent_payload)
    assert decoded["payload"] == payload
    assert decoded["metadata"]["content_encoding"] is None

@pytest.mark.asyncio
async def test_publish_bulk(publisher):
    """Test bulk publishing pipeline."""
    messages = [
        {"channel": "chan1", "payload": "msg1"},
        {"channel": "chan2", "payload": "msg2"}
    ]
    
    # Mock pipeline object
    mock_pipeline = MagicMock()
    # Configure pipeline context manager
    mock_pipeline.__aenter__.return_value = mock_pipeline
    mock_pipeline.__aexit__.return_value = None
    
    # Configure execute to be awaitable
    mock_pipeline.execute = AsyncMock()
    
    # Configure publish to be synchronous
    mock_pipeline.publish = MagicMock()
    
    # IMPORTANT: pipeline() method on redis client is synchronous and returns the pipeline object
    # Since publisher.redis_client is AsyncMock, we must override pipeline to be MagicMock
    publisher.redis_client.pipeline = MagicMock(return_value=mock_pipeline)
    
    result = await publisher.publish_bulk(messages)
    
    assert result["published_count"] == 2
    assert result["failed_count"] == 0
    
    # Check pipeline interactions
    assert mock_pipeline.publish.call_count == 2
    mock_pipeline.execute.assert_called_once()

@pytest.mark.asyncio
async def test_publish_bulk_partial_failure(publisher):
    """Test bulk publishing with mixed validity."""
    # Note: The bulk implementation doesn't fail on individual publish calls inside the loop unless logic error
    # It adds to pipeline. Failure happens at execute() or if logic prevents adding.
    
    # Let's verify data validation failure inside loop
    messages = [
        {"channel": "chan1", "payload": "msg1"},
        {"channel": "", "payload": "msg2"}  # Invalid channel
    ]
    
    mock_pipeline = MagicMock()
    mock_pipeline.__aenter__.return_value = mock_pipeline
    mock_pipeline.__aexit__.return_value = None
    mock_pipeline.execute = AsyncMock()
    mock_pipeline.publish = MagicMock()
    
    publisher.redis_client.pipeline = MagicMock(return_value=mock_pipeline)
    
    result = await publisher.publish_bulk(messages)
    
    assert result["published_count"] == 1
    assert result["failed_count"] == 1
    assert result["results"][1]["success"] is False
    
    # Pipeline should have only 1 publish call
    assert mock_pipeline.publish.call_count == 1
    mock_pipeline.execute.assert_called_once()
