
import pytest
from unittest.mock import MagicMock, patch, AsyncMock
from fastapi.testclient import TestClient
import sys
import os
from datetime import datetime

# Add service root to path so 'app' module can be found
service_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if service_root not in sys.path:
    sys.path.insert(0, service_root)

from app.main import app, get_retention_manager
from app.retention_manager import RetentionManager

@pytest.fixture
def mock_retention_manager():
    manager = MagicMock(spec=RetentionManager)
    # Mock async methods
    manager.get_retention_status = AsyncMock()
    manager.manually_trigger_archival = AsyncMock()
    return manager

@pytest.fixture
def client(mock_retention_manager):
    # Override dependency
    app.dependency_overrides[get_retention_manager] = lambda: mock_retention_manager
    yield TestClient(app)
    # Clean up
    app.dependency_overrides.clear()

def test_get_retention_status(client, mock_retention_manager):
    """Test GET /database/retention/status endpoint."""
    
    # Setup mock return value
    expected_status = {
        "retention_period_days": 30,
        "hypertables": [
            {
                "table_name": "test_table",
                "total_chunks": 10,
                "archivable_chunks": 2,
                "oldest_data": "2023-01-01T00:00:00",
                "newest_data": "2023-01-10T00:00:00"
            }
        ]
    }
    mock_retention_manager.get_retention_status.return_value = expected_status
    
    # Make request
    response = client.get("/database/retention/status")
    
    # Verify response
    assert response.status_code == 200
    assert response.json() == expected_status
    mock_retention_manager.get_retention_status.assert_called_once()

def test_trigger_archival_all_tables(client, mock_retention_manager):
    """Test POST /database/retention/trigger-archival for all tables."""
    
    # Setup mock return value
    expected_result = {
        "success": True,
        "message": "Archival triggered",
        "results": []
    }
    mock_retention_manager.manually_trigger_archival.return_value = expected_result
    
    # Make request (no query params)
    response = client.post("/database/retention/trigger-archival")
    
    # Verify response
    assert response.status_code == 200
    assert response.json() == expected_result
    mock_retention_manager.manually_trigger_archival.assert_called_once_with(None)

def test_trigger_archival_specific_table(client, mock_retention_manager):
    """Test POST /database/retention/trigger-archival for specific table."""
    
    # Setup mock return value
    expected_result = {
        "success": True,
        "message": "Archival triggered for table",
        "results": []
    }
    mock_retention_manager.manually_trigger_archival.return_value = expected_result
    
    # Make request
    response = client.post("/database/retention/trigger-archival?table_name=my_table")
    
    # Verify response
    assert response.status_code == 200
    assert response.json() == expected_result
    mock_retention_manager.manually_trigger_archival.assert_called_once_with("my_table")

def test_get_retention_status_error(client, mock_retention_manager):
    """Test error handling in retention status endpoint."""
    
    # Setup mock to raise exception
    mock_retention_manager.get_retention_status.side_effect = Exception("Database error")
    
    # Make request
    response = client.get("/database/retention/status")
    
    # Verify error response
    assert response.status_code == 400
    assert "Retention status failed" in response.json()["detail"]

def test_trigger_archival_error(client, mock_retention_manager):
    """Test error handling in trigger archival endpoint."""
    
    # Setup mock to raise exception
    mock_retention_manager.manually_trigger_archival.side_effect = Exception("Trigger failed")
    
    # Make request
    response = client.post("/database/retention/trigger-archival")
    
    # Verify error response
    assert response.status_code == 400
    assert "Archival trigger failed" in response.json()["detail"]
