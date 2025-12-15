
import pytest
from unittest.mock import MagicMock, patch, AsyncMock
import sys
import io
import os

# Add service root to path so 'app' module can be found
service_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if service_root not in sys.path:
    sys.path.insert(0, service_root)

from app.migration_manager import AutomatedMigrationManager, MigrationResult, MigrationPhase

@pytest.fixture
def mock_settings():
    return {
        "database_url": "postgresql+asyncpg://user:pass@localhost:5432/test_db",
        "alembic_config_path": "alembic.ini"
    }

@pytest.fixture
def migration_manager(mock_settings):
    with patch("app.migration_manager.create_async_engine") as mock_async_engine, \
         patch("app.migration_manager.create_engine") as mock_sync_engine:
        
        manager = AutomatedMigrationManager(
            database_url=mock_settings["database_url"],
            alembic_config_path=mock_settings["alembic_config_path"]
        )
        
        # Setup mock engines
        manager.async_engine = mock_async_engine.return_value
        manager.sync_engine = mock_sync_engine.return_value
        
        return manager

@pytest.mark.asyncio
async def test_initialization(mock_settings):
    with patch("app.migration_manager.create_async_engine") as mock_async_engine, \
         patch("app.migration_manager.create_engine") as mock_sync_engine:
        
        manager = AutomatedMigrationManager(
            database_url=mock_settings["database_url"],
            alembic_config_path=mock_settings["alembic_config_path"]
        )
        
        await manager.initialize()
        
        assert manager.async_engine is not None
        assert manager.sync_engine is not None
        mock_async_engine.assert_called_once()
        mock_sync_engine.assert_called_once()

@pytest.mark.asyncio
async def test_offline_migration_sql_generation(migration_manager):
    """Test that dry_run=True generates SQL output."""
    
    # Mock alembic config and command
    with patch("app.migration_manager.Config") as mock_config, \
         patch("app.migration_manager.ScriptDirectory") as mock_script_dir, \
         patch("app.migration_manager.MigrationContext") as mock_context, \
         patch("app.migration_manager.command") as mock_command:
            
        # Setup mocks
        mock_context.configure.return_value.get_current_revision.return_value = "base"
        
        # Mock sys.stdout to verify capture
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            # We need to mock the command.upgrade to write to stdout like alembic does
            def side_effect_upgrade(config, revision, sql=False):
                if sql:
                    print("CREATE TABLE test_table (id SERIAL PRIMARY KEY);")
            
            mock_command.upgrade.side_effect = side_effect_upgrade
            
            # Execute (synchronous method)
            migration_manager._execute_alembic_migration(target_revision="head", dry_run=True)
            
            # Verify command called with sql=True
            mock_command.upgrade.assert_called_with(mock_config.return_value, "head", sql=True)

@pytest.mark.asyncio
async def test_rollback_logic(migration_manager):
    """Test that rollback calls downgrade with correct revision."""
    
    # Mock alembic stuff
    with patch("app.migration_manager.Config") as mock_config, \
         patch("app.migration_manager.command") as mock_command:
        
        # Set start revision
        migration_manager.start_revision = "rev123"
        result = MigrationResult()
        
        await migration_manager._rollback_migration(result)
        
        # Verify downgrade called
        # We need to match the Config object which is instantiated inside the method
        # So we check if downgrade was called with ANY config and the correct revision
        args, _ = mock_command.downgrade.call_args
        assert args[1] == "rev123"
        assert result.rollback_point == "rev123"

@pytest.mark.asyncio
async def test_full_execution_flow(migration_manager):
    """Test the full flow of execute_migrations."""
    
    # Use real async functions for mocking to ensure they are awaitable and detected as coroutines
    async def async_noop(*args, **kwargs): pass
    def sync_noop(*args, **kwargs): pass
    
    # Mock all phase methods
    with patch.object(migration_manager, '_validate_environment', side_effect=async_noop) as mock_validate, \
         patch.object(migration_manager, '_create_backup', side_effect=async_noop) as mock_backup, \
         patch.object(migration_manager, '_execute_alembic_migration', side_effect=sync_noop) as mock_alembic, \
         patch.object(migration_manager, '_setup_hypertables', side_effect=async_noop) as mock_hyper, \
         patch.object(migration_manager, '_setup_continuous_aggregates', side_effect=async_noop) as mock_agg, \
         patch.object(migration_manager, '_create_indexes', side_effect=async_noop) as mock_idx, \
         patch.object(migration_manager, '_create_constraints', side_effect=async_noop) as mock_cstr, \
         patch.object(migration_manager, '_verify_migration', side_effect=async_noop) as mock_verify, \
         patch.object(migration_manager, '_cleanup', side_effect=async_noop) as mock_cleanup:
    
        result = await migration_manager.execute_migrations(dry_run=False)
        
        assert result.success is True
        assert MigrationPhase.VALIDATION in result.phases_completed
        assert MigrationPhase.BACKUP in result.phases_completed
        assert MigrationPhase.SCHEMA_MIGRATION in result.phases_completed
        assert MigrationPhase.HYPERTABLE_SETUP in result.phases_completed
        assert MigrationPhase.CLEANUP in result.phases_completed
        
        mock_validate.assert_called_once()
        mock_backup.assert_called_once()
        mock_alembic.assert_called_once()
        mock_hyper.assert_called_once()
