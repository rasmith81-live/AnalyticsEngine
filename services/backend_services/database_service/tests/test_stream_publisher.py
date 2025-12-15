
import pytest
from unittest.mock import MagicMock, patch, AsyncMock
import asyncio
from datetime import datetime, timedelta

import sys
import os

# Add service root to path so 'app' module can be found
service_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if service_root not in sys.path:
    sys.path.insert(0, service_root)

from app.stream_publisher import StreamPublisher
from app.subscriber_manager import SubscriberManager
from app.messaging_client import MessagingClient

@pytest.fixture
def mock_messaging_client():
    return AsyncMock(spec=MessagingClient)

@pytest.fixture
def mock_session_factory():
    # Create a factory that returns an async context manager (session)
    session_mock = AsyncMock()
    
    # Mock result for execute
    result_mock = MagicMock()
    
    # Create rows with required attributes
    row = MagicMock()
    row.bucket = datetime.utcnow()
    row.kpi_code = "KPI_1"
    row.entity_id = "ENT_1"
    row.avg_value = 10.5
    row.min_value = 5.0
    row.max_value = 15.0
    row.sum_value = 105.0
    row.data_points = 10
    row.stddev_value = 1.2
    
    result_mock.fetchall.return_value = [row]
    session_mock.execute.return_value = result_mock
    
    # Factory context manager
    cm = AsyncMock()
    cm.__aenter__.return_value = session_mock
    
    factory = MagicMock(return_value=cm)
    return factory

@pytest.mark.asyncio
async def test_subscriber_manager_logic():
    """Test SubscriberManager add/remove logic."""
    manager = SubscriberManager(timeout_seconds=60)
    
    # Add first subscriber
    is_first = await manager.add_subscriber("sub1", "KPI_1", "ENT_1", "minute")
    assert is_first is True
    assert await manager.get_subscriber_count("KPI_1", "ENT_1", "minute") == 1
    
    # Add second subscriber to same stream
    is_first = await manager.add_subscriber("sub2", "KPI_1", "ENT_1", "minute")
    assert is_first is False
    assert await manager.get_subscriber_count("KPI_1", "ENT_1", "minute") == 2
    
    # Remove second subscriber
    stopped = await manager.remove_subscriber("sub2", "KPI_1", "ENT_1", "minute")
    assert len(stopped) == 0
    assert await manager.get_subscriber_count("KPI_1", "ENT_1", "minute") == 1
    
    # Remove first subscriber (last one)
    stopped = await manager.remove_subscriber("sub1", "KPI_1", "ENT_1", "minute")
    assert "KPI_1:ENT_1:minute" in stopped
    assert await manager.get_subscriber_count("KPI_1", "ENT_1", "minute") == 0

@pytest.mark.asyncio
async def test_stream_publisher_flow(mock_session_factory, mock_messaging_client):
    """Test StreamPublisher starting stream and publishing data."""
    sub_manager = SubscriberManager()
    
    publisher = StreamPublisher(
        db_session_factory=mock_session_factory,
        messaging_client=mock_messaging_client,
        subscriber_manager=sub_manager,
        poll_interval_seconds=0.1 # Fast poll for testing
    )
    
    # Start publisher
    await publisher.start()
    assert publisher._running is True
    
    # Add subscriber (simulating what the API would do)
    await sub_manager.add_subscriber("sub1", "KPI_1", "ENT_1", "minute")
    
    # Start stream
    started = await publisher.start_stream("KPI_1", "ENT_1", "minute")
    assert started is True
    assert "KPI_1:ENT_1:minute" in publisher._active_publishers
    
    # Let it run for a bit to process at least one poll cycle
    await asyncio.sleep(0.2)
    
    # Verify DB query
    mock_session_factory.assert_called()
    
    # Verify message published
    mock_messaging_client.publish_message.assert_called()
    call_args = mock_messaging_client.publish_message.call_args[1]
    assert call_args['channel'] == "kpi.stream.KPI_1.ENT_1.minute"
    assert call_args['message_type'] == "kpi_stream_update"
    assert call_args['message']['kpi_code'] == "KPI_1"
    
    # Stop stream
    stopped = await publisher.stop_stream("KPI_1", "ENT_1", "minute")
    assert stopped is True
    assert "KPI_1:ENT_1:minute" not in publisher._active_publishers
    
    # Stop publisher
    await publisher.stop()
    assert publisher._running is False

@pytest.mark.asyncio
async def test_cleanup_inactive_subscribers(mock_session_factory, mock_messaging_client):
    """Test cleanup of inactive subscribers."""
    # Use short timeout
    timeout_sec = 0.1
    sub_manager = SubscriberManager(timeout_seconds=timeout_sec)
    
    publisher = StreamPublisher(
        db_session_factory=mock_session_factory,
        messaging_client=mock_messaging_client,
        subscriber_manager=sub_manager,
        poll_interval_seconds=0.1
    )
    
    try:
        # Start publisher (which starts cleanup loop)
        await publisher.start()
        
        # Add subscriber and start stream
        await sub_manager.add_subscriber("sub1", "KPI_1", "ENT_1", "minute")
        await publisher.start_stream("KPI_1", "ENT_1", "minute")
        
        # Verify stream running
        assert "KPI_1:ENT_1:minute" in publisher._active_publishers
        
        # Wait for timeout + buffer to ensure expiration
        # We do NOT patch asyncio.sleep here because we want real time to pass
        await asyncio.sleep(0.8)
        
        # Manual trigger to verify logic (since the background loop runs every 60s)
        streams_to_stop = await sub_manager.cleanup_inactive_subscribers()
        
        assert "KPI_1:ENT_1:minute" in streams_to_stop
        assert await sub_manager.get_subscriber_count("KPI_1", "ENT_1", "minute") == 0
        
    finally:
        await publisher.stop()
