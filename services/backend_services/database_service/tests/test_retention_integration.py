
import pytest
from unittest.mock import MagicMock, patch, AsyncMock, ANY
import sys
import os
from datetime import datetime, timedelta
from sqlalchemy import text

# Add service root to path so 'app' module can be found
service_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if service_root not in sys.path:
    sys.path.insert(0, service_root)

from app.retention_manager import RetentionManager
from app.models import ArchivalStatus, RetentionPolicy
from app.config import DatabaseServiceSettings

@pytest.fixture
def mock_settings():
    settings = MagicMock(spec=DatabaseServiceSettings)
    settings.retention_period_days = 30
    return settings

@pytest.fixture
def mock_engine():
    engine = MagicMock()
    
    # Create the connection mock
    connection = AsyncMock()
    
    # Create a mock for the context manager returned by engine.begin()
    # When 'async with engine.begin() as conn' is called:
    # 1. engine.begin() is called, returning cm
    # 2. cm.__aenter__() is awaited, returning connection
    cm = AsyncMock()
    cm.__aenter__.return_value = connection
    engine.begin.return_value = cm
    
    return engine

@pytest.fixture
def mock_messaging_client():
    client = AsyncMock()
    return client

@pytest.fixture
def retention_manager(mock_engine, mock_messaging_client):
    # Patch get_settings to return predictable retention period
    with patch("app.retention_manager.get_settings") as mock_get_settings:
        mock_get_settings.return_value.retention_period_days = 30
        manager = RetentionManager(mock_engine, mock_messaging_client)
        return manager

@pytest.mark.asyncio
async def test_initialization(retention_manager):
    assert retention_manager.retention_period_days == 30
    assert retention_manager._running is False

@pytest.mark.asyncio
async def test_identify_and_publish_archival_event(retention_manager, mock_engine, mock_messaging_client):
    """Test identifying chunks and publishing archival event."""
    
    # 1. Mock _get_hypertables_with_retention
    # Return one table enabled for retention
    with patch.object(retention_manager, '_get_hypertables_with_retention') as mock_get_tables:
        mock_get_tables.return_value = [
            ("test_hypertable", RetentionPolicy(enabled=True, retention_period_days=30))
        ]
        
        # 2. Mock DB query for identifying chunks in _identify_chunks_for_archival
        # We need to mock the result of conn.execute
        # The result must be iterable (for row in result)
        mock_result = MagicMock()
        mock_result.__iter__.return_value = [
            MagicMock(chunk_name="chunk_1", range_start=datetime(2023, 1, 1), range_end=datetime(2023, 1, 8))
        ]
        
        # Configure the connection returned by the context manager
        connection = mock_engine.begin.return_value.__aenter__.return_value
        connection.execute.return_value = mock_result
        
        # 3. Run process
        await retention_manager._process_retention_policies()
        
        # 4. Verify DB query was made to find chunks
        # Should query timescaledb_information.chunks
        assert connection.execute.called
        query_text = str(connection.execute.call_args[0][0])
        assert "timescaledb_information.chunks" in query_text
        
        # 5. Verify Archival Event published
        mock_messaging_client.publish_event.assert_called_once()
        call_args = mock_messaging_client.publish_event.call_args[1]
        assert call_args['topic'] == "archival.events"
        assert call_args['event_type'] == "data.archival.requested"
        
        payload = call_args['payload']
        assert payload['table_name'] == "test_hypertable"
        assert len(payload['chunks']) == 1
        assert payload['chunks'][0]['chunk_name'] == "chunk_1"
        
        # 6. Verify event stored in local tracking
        assert len(retention_manager._archival_confirmations) == 1
        event_id = payload['event_id']
        assert event_id in retention_manager._archival_confirmations

@pytest.mark.asyncio
async def test_handle_archival_confirmation_and_drop_chunks(retention_manager, mock_engine):
    """Test handling confirmation and dropping chunks."""
    
    # 1. Setup pending confirmation
    event_id = "test-event-123"
    retention_manager._archival_confirmations[event_id] = {
        'table_name': 'test_hypertable',
        'chunks': [{'chunk_name': 'chunk_1'}, {'chunk_name': 'chunk_2'}],
        'timestamp': datetime.utcnow()
    }
    
    # 2. Mock confirmation message
    message = {
        'event_id': event_id,
        'status': ArchivalStatus.COMPLETED,
        'completed_at': datetime.utcnow(),
        'lakehouse_path': 'azure://container/path'
    }
    
    # 3. Handle confirmation
    await retention_manager._handle_archival_confirmation(message)
    
    # 4. Verify chunks dropped via DB execution
    connection = mock_engine.begin.return_value.__aenter__.return_value
    assert connection.execute.call_count == 2
    
    # Check SQL calls
    calls = connection.execute.call_args_list
    # Note: calls[0] is (args, kwargs), args[0] is the query text object
    assert "drop_chunks('chunk_1'" in str(calls[0][0][0])
    assert "drop_chunks('chunk_2'" in str(calls[1][0][0])
    
    # 5. Verify tracking cleared
    assert event_id not in retention_manager._archival_confirmations

@pytest.mark.asyncio
async def test_handle_archival_confirmation_failed(retention_manager, mock_engine):
    """Test handling failed confirmation (should NOT drop chunks)."""
    
    # 1. Setup pending confirmation
    event_id = "test-event-fail"
    retention_manager._archival_confirmations[event_id] = {
        'table_name': 'test_hypertable',
        'chunks': [{'chunk_name': 'chunk_1'}],
        'timestamp': datetime.utcnow()
    }
    
    # 2. Mock confirmation message with FAILED status
    message = {
        'event_id': event_id,
        'status': ArchivalStatus.FAILED,
        'completed_at': datetime.utcnow(),
        'error_message': 'Upload failed'
    }
    
    # 3. Handle confirmation
    await retention_manager._handle_archival_confirmation(message)
    
    # 4. Verify NO DB execution
    connection = mock_engine.begin.return_value.__aenter__.return_value
    assert not connection.execute.called
    
    # 5. Verify tracking cleared (even on failure, we stop tracking this specific attempt)
    assert event_id not in retention_manager._archival_confirmations
