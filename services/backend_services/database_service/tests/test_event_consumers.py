
import pytest
from unittest.mock import MagicMock, patch, AsyncMock
import sys
import os
from datetime import datetime

# Add service root to path so 'app' module can be found
service_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if service_root not in sys.path:
    sys.path.insert(0, service_root)

from app.telemetry_consumers import TelemetryEventConsumer
from app.database_manager import DatabaseManager
from app.messaging_client import MessagingClient

@pytest.fixture
def mock_db_manager():
    return MagicMock(spec=DatabaseManager)

@pytest.fixture
def mock_messaging_client():
    return AsyncMock(spec=MessagingClient)

@pytest.mark.asyncio
async def test_telemetry_consumer_dependency_ingestion(mock_db_manager, mock_messaging_client):
    consumer = TelemetryEventConsumer(mock_db_manager, mock_messaging_client)
    
    event_data = {
        "dependency": {
            "service": "test-service",
            "name": "test-dependency",
            "type": "database",
            "target": "postgres",
            "duration_ms": 10.5,
            "success": True,
            "timestamp": datetime.utcnow().isoformat()
        },
        "correlation_id": "test-correlation-id"
    }
    
    # Configure mock to be awaitable
    mock_db_manager.store_dependency_data = AsyncMock()
    
    await consumer._handle_dependency_ingestion(event_data)
    
    mock_db_manager.store_dependency_data.assert_called_once_with(event_data["dependency"])
