
import pytest
from unittest.mock import MagicMock, patch, AsyncMock
import sys
import os
import asyncio

# Mock app.telemetry before importing app.event_publisher
# This avoids dependency issues with opentelemetry if it's not fully configured or installed
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

# Now we can safely import app.event_publisher
from app.event_publisher import EventPublisher
from app.config import Settings
from redis.exceptions import BusyLoadingError, ConnectionError, TimeoutError

@pytest.fixture
def mock_settings():
    return Settings(
        REDIS_URL="redis://localhost:6379/0",
        REDIS_MAX_CONNECTIONS=10,
        REDIS_RETRY_ON_TIMEOUT=True,
        REDIS_SOCKET_KEEPALIVE=True
    )

@pytest.fixture
def publisher(mock_settings):
    return EventPublisher(
        redis_url=mock_settings.redis_url,
        max_connections=mock_settings.redis_max_connections,
        retry_on_timeout=mock_settings.redis_retry_on_timeout,
        socket_keepalive=mock_settings.redis_socket_keepalive
    )

@pytest.mark.asyncio
async def test_event_publisher_initialization_config(publisher):
    """Test that EventPublisher initializes Redis pool with correct configuration."""
    with patch("redis.asyncio.ConnectionPool.from_url") as mock_pool_cls, \
         patch("redis.asyncio.Redis") as mock_redis_cls:
        
        mock_client = AsyncMock()
        mock_redis_cls.return_value = mock_client
        
        await publisher.initialize()
        
        # Verify ConnectionPool was created with correct args
        mock_pool_cls.assert_called_once()
        call_kwargs = mock_pool_cls.call_args[1]
        
        assert call_kwargs["max_connections"] == 10
        assert call_kwargs["retry_on_timeout"] is True
        assert call_kwargs["socket_keepalive"] is True
        
        # Verify Redis client was created with the pool
        mock_redis_cls.assert_called_once_with(connection_pool=mock_pool_cls.return_value)
        
        # Verify ping was called
        mock_client.ping.assert_awaited_once()

@pytest.mark.asyncio
async def test_event_publisher_retry_logic(publisher):
    """Test that initialize retries on BusyLoadingError."""
    with patch("redis.asyncio.ConnectionPool.from_url"), \
         patch("redis.asyncio.Redis") as mock_redis_cls, \
         patch("asyncio.sleep", new_callable=AsyncMock) as mock_sleep:
        
        mock_client = AsyncMock()
        # Fail twice with BusyLoadingError, then succeed
        mock_client.ping.side_effect = [BusyLoadingError("Loading"), BusyLoadingError("Loading"), True]
        mock_redis_cls.return_value = mock_client
        
        await publisher.initialize()
        
        # Should have called ping 3 times
        assert mock_client.ping.call_count == 3
        # Should have slept twice
        assert mock_sleep.call_count == 2

@pytest.mark.asyncio
async def test_event_publisher_health_check_healthy(publisher):
    """Test health check when Redis is healthy."""
    publisher.redis_client = AsyncMock()
    publisher.redis_client.ping.return_value = True
    publisher.redis_client.info.return_value = {
        "used_memory": 1024,
        "connected_clients": 5
    }
    publisher.active_channels = {"chan1", "chan2"}
    
    health = await publisher.health_check()
    
    assert health["status"] == "healthy"
    assert health["redis_connected"] is True
    assert health["redis_memory_usage"] == 1024
    assert health["redis_connected_clients"] == 5
    assert health["active_channels"] == 2

@pytest.mark.asyncio
async def test_event_publisher_health_check_unhealthy(publisher):
    """Test health check when Redis is disconnected."""
    publisher.redis_client = AsyncMock()
    publisher.redis_client.ping.side_effect = ConnectionError("Connection lost")
    
    health = await publisher.health_check()
    
    assert health["status"] == "unhealthy"
    assert health["redis_connected"] is False
    assert "error" in health

@pytest.mark.asyncio
async def test_event_publisher_publish_retry_handling(publisher):
    """Test that publish_message handles errors correctly (EventPublisher doesn't implement retry itself for publish, but relies on redis-py's retry or raises)."""
    # Note: EventPublisher configuration sets up retry in the pool, but individual publish calls 
    # in the code currently catch Exception and re-raise after logging.
    
    publisher.redis_client = AsyncMock()
    publisher.redis_client.publish.side_effect = TimeoutError("Timeout")
    
    with pytest.raises(TimeoutError):
        await publisher.publish_message("test-channel", {"data": "test"})
    
    assert publisher.failed_count == 1
