
import pytest
from unittest.mock import MagicMock, patch, AsyncMock
import sys
import os
from datetime import datetime

# Add service root to path so 'app' module can be found
service_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if service_root not in sys.path:
    sys.path.insert(0, service_root)

from app.query_builder import QueryBuilder
from app.database_manager import DatabaseManager
from app.config import DatabaseServiceSettings

@pytest.fixture
def query_builder():
    return QueryBuilder()

@pytest.fixture
def mock_settings():
    settings = MagicMock(spec=DatabaseServiceSettings)
    settings.enable_query_cache = True
    settings.cache_ttl = 300
    settings.redis_url = "redis://localhost:6379"
    # Add other required settings if DatabaseManager init needs them
    settings.database_url = "postgresql+asyncpg://user:pass@localhost/db"
    settings.connection_pool_size = 5
    settings.connection_pool_max_overflow = 10
    settings.connection_pool_timeout = 30
    settings.connection_pool_recycle = 3600
    settings.run_migrations_on_startup = False
    settings.enforce_timescaledb = False
    return settings

@pytest.fixture
def mock_db_manager(mock_settings):
    with patch('services.backend_services.database_service.app.database_manager.create_async_engine'), \
         patch('services.backend_services.database_service.app.database_manager.create_engine'), \
         patch('services.backend_services.database_service.app.database_manager.redis.from_url') as mock_redis_cls:
        
        manager = DatabaseManager(mock_settings)
        # Mock Redis client instance
        manager.redis_client = AsyncMock()
        # Mock Session factory
        manager.session_factory = MagicMock()
        # Mock Async Session
        session_mock = AsyncMock()
        # Mock execute result
        result_mock = MagicMock()
        result_mock.fetchall.return_value = []
        result_mock.keys.return_value = []
        session_mock.execute.return_value = result_mock
        
        # Context manager for session
        cm = AsyncMock()
        cm.__aenter__.return_value = session_mock
        manager.session_factory.return_value = cm
        
        return manager

def test_query_builder_simple_select(query_builder):
    sql, params = query_builder.build_select(
        table_name="test_table",
        columns=["id", "name"],
        limit=10
    )
    
    assert "SELECT id, name FROM test_table" in sql
    assert "LIMIT :limit" in sql
    assert params['limit'] == 10

def test_query_builder_with_filters(query_builder):
    filters = [
        {"field": "status", "op": "eq", "value": "active"},
        {"field": "age", "op": "gte", "value": 18}
    ]
    
    sql, params = query_builder.build_select(
        table_name="users",
        filters=filters
    )
    
    assert "WHERE status = :filter_0 AND age >= :filter_1" in sql
    assert params['filter_0'] == "active"
    assert params['filter_1'] == 18

def test_query_builder_security(query_builder):
    # Test invalid table name
    with pytest.raises(ValueError):
        query_builder.build_select(table_name="users; DROP TABLE users")
        
    # Test invalid column name
    with pytest.raises(ValueError):
        query_builder.build_select(table_name="users", columns=["id; --"])

def test_query_builder_schema_qualified_table(query_builder):
    """Test that table names with schemas (e.g. analytics_data.table) are allowed."""
    sql, params = query_builder.build_select(
        table_name="analytics_data.metrics",
        columns=["id", "value"],
        limit=5
    )
    assert "SELECT id, value FROM analytics_data.metrics" in sql

@pytest.mark.asyncio
async def test_database_manager_caching(mock_db_manager):
    query = "SELECT * FROM users"
    params = {}
    
    # 1. Test Cache Miss
    mock_db_manager.redis_client.get.return_value = None
    
    await mock_db_manager.execute_query(query, params, service_name="test")
    
    # Verify DB was queried
    mock_db_manager.session_factory.assert_called()
    # Verify result was cached
    mock_db_manager.redis_client.setex.assert_called_once()
    assert mock_db_manager.cache_stats["misses"] == 1
    
    # 2. Test Cache Hit
    cached_data = {
        "rows": [{"id": 1, "name": "Test"}],
        "column_names": ["id", "name"],
        "row_count": 1,
        "execution_time": 0.01,
        "timestamp": datetime.utcnow().isoformat(),
        "service_name": "test",
        "correlation_id": "123"
    }
    import json
    mock_db_manager.redis_client.get.return_value = json.dumps(cached_data)
    
    result = await mock_db_manager.execute_query(query, params, service_name="test")
    
    # Verify DB was NOT queried (session factory count should remain same)
    # Note: session_factory was called once in first step.
    # In this step, it should NOT be called again if cache hit works and returns early.
    assert mock_db_manager.session_factory.call_count == 1 
    
    assert result == cached_data
    assert mock_db_manager.cache_stats["hits"] == 1

@pytest.mark.asyncio
async def test_integration_builder_and_manager(query_builder, mock_db_manager):
    """Test using QueryBuilder output with DatabaseManager."""
    
    # Build Query
    sql, params = query_builder.build_select(
        table_name="metrics",
        filters=[{"field": "service", "op": "eq", "value": "auth"}],
        limit=5
    )
    
    # Mock DB Result
    session_mock = mock_db_manager.session_factory.return_value.__aenter__.return_value
    result_mock = MagicMock()
    result_mock.fetchall.return_value = [(1, "auth", 100)]
    result_mock.keys.return_value = ["id", "service", "value"]
    result_mock.rowcount = 1
    session_mock.execute.return_value = result_mock
    
    # Execute
    result = await mock_db_manager.execute_query(sql, params, service_name="test_integration")
    
    # Verify
    session_mock.execute.assert_called_once()
    # Check that the sql passed to execute matches what builder produced
    args = session_mock.execute.call_args
    # args[0] is (text(sql), params) or similar depending on how text() is used
    # DatabaseManager does: stmt = text(query); await session.execute(stmt, parameters)
    # so call_args[0][0] is the TextClause object. str(obj) gives SQL.
    executed_sql = str(args[0][0])
    
    assert "SELECT * FROM metrics" in executed_sql
    assert "WHERE service = :filter_0" in executed_sql
    assert params['filter_0'] == "auth"
    
    assert result['row_count'] == 1
    assert result['rows'][0]['service'] == 'auth'

# --- API Endpoint Tests ---

from fastapi.testclient import TestClient
from app.main import app, get_database_manager

@pytest.fixture
def client(mock_db_manager):
    app.dependency_overrides[get_database_manager] = lambda: mock_db_manager
    yield TestClient(app)
    app.dependency_overrides.clear()

def test_adhoc_query_endpoint(client, mock_db_manager):
    """Test POST /database/query/adhoc endpoint."""
    
    # Setup mock result
    mock_result = {
        "rows": [{"id": 1, "name": "Test Item"}],
        "column_names": ["id", "name"],
        "row_count": 1,
        "execution_time": 0.05,
        "timestamp": datetime.utcnow().isoformat(),
        "service_name": "test_service",
        "correlation_id": "123"
    }
    
    # Configure execute_query mock
    # execute_query is async, so we need to ensure the mock behaves correctly when awaited if it wasn't already
    # In mock_db_manager fixture, execute_query calls are on the manager object.
    # The endpoint calls db_manager.execute_query.
    mock_db_manager.execute_query = AsyncMock(return_value=mock_result)
    
    payload = {
        "table_name": "items",
        "columns": ["id", "name"],
        "filters": [{"field": "id", "op": "eq", "value": 1}],
        "service_name": "test_service"
    }
    
    response = client.post("/database/query/adhoc", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["data"]["rows"][0]["name"] == "Test Item"
    
    # Verify execute_query was called with built SQL
    mock_db_manager.execute_query.assert_called_once()
    call_args = mock_db_manager.execute_query.call_args[1]
    assert "SELECT id, name FROM items" in call_args["query"]
    assert "WHERE id = :filter_0" in call_args["query"]
    assert call_args["parameters"]["filter_0"] == 1

def test_adhoc_query_invalid_table(client):
    """Test ad-hoc query with invalid table name (security check)."""
    payload = {
        "table_name": "items; DROP TABLE items",
        "service_name": "test_service"
    }
    
    response = client.post("/database/query/adhoc", json=payload)
    
    assert response.status_code == 400
    assert "Invalid table name" in response.json()["detail"]
