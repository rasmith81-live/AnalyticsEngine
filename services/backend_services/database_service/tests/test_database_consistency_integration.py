
import pytest
from unittest.mock import MagicMock, patch, AsyncMock
import sys
import os

# Add service root to path so 'app' module can be found
service_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if service_root not in sys.path:
    sys.path.insert(0, service_root)

from app.database_manager import DatabaseManager
from app.config import DatabaseServiceSettings
from app.consistency_checker import ConsistencyChecker
from app.models import ModelInfo

@pytest.fixture
def mock_settings():
    settings = MagicMock(spec=DatabaseServiceSettings)
    settings.database_url = "postgresql+asyncpg://user:pass@localhost/db"
    settings.connection_pool_size = 5
    settings.connection_pool_max_overflow = 10
    settings.connection_pool_timeout = 30
    settings.connection_pool_recycle = 3600
    settings.run_migrations_on_startup = False
    settings.enable_query_cache = False
    return settings

@pytest.fixture
def mock_db_manager(mock_settings):
    # Patch using app path
    with patch('app.database_manager.create_async_engine'), \
         patch('app.database_manager.create_engine'), \
         patch('app.database_manager.redis.from_url'):
        
        manager = DatabaseManager(mock_settings)
        # Mock engine and session factory
        manager.async_engine = AsyncMock()
        manager.session_factory = MagicMock()
        
        # Mock ConsistencyChecker directly to verify interactions
        manager.consistency_checker = AsyncMock(spec=ConsistencyChecker)
        
        return manager

@pytest.mark.asyncio
async def test_register_models_calls_reconcile(mock_db_manager):
    """Test that register_models properly calls the consistency checker."""
    
    models = [
        {
            "name": "TestModel",
            "table_name": "test_table",
            "fields": {"id": "int", "name": "str"}
        }
    ]
    
    await mock_db_manager.register_models(
        service_name="test_service",
        models=models,
        auto_create_tables=True
    )
    
    # Verify reconcile was called
    mock_db_manager.consistency_checker.reconcile.assert_called_once()
    
    # Check arguments
    call_args = mock_db_manager.consistency_checker.reconcile.call_args
    assert call_args.kwargs['auto_repair'] is True
    
    definitions = call_args.kwargs['entity_definitions']
    assert len(definitions) == 1
    assert isinstance(definitions[0], ModelInfo)
    assert definitions[0].name == "TestModel"
    assert definitions[0].table_name == "test_table"

@pytest.mark.asyncio
async def test_check_consistency_calls_run_check(mock_db_manager):
    """Test that check_consistency properly calls the consistency checker."""
    
    models = [
        {
            "name": "TestModel",
            "table_name": "test_table",
            "fields": {"id": "int", "name": "str"}
        }
    ]
    
    await mock_db_manager.check_consistency(
        service_name="test_service",
        models=models
    )
    
    # Verify run_check was called
    mock_db_manager.consistency_checker.run_check.assert_called_once()
    
    definitions = mock_db_manager.consistency_checker.run_check.call_args[0][0]
    assert len(definitions) == 1
    assert definitions[0].table_name == "test_table"

@pytest.mark.asyncio
async def test_register_models_invalid_input(mock_db_manager):
    """Test register_models with invalid input."""
    
    # Missing fields
    models = [
        {"name": "InvalidModel"} 
    ]
    
    result = await mock_db_manager.register_models(
        service_name="test_service",
        models=models
    )
    
    # Should skip invalid model and not call reconcile if no valid models
    assert result == []
    mock_db_manager.consistency_checker.reconcile.assert_not_called()
