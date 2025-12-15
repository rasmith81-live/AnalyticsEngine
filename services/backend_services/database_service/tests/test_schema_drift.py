
import pytest
from unittest.mock import MagicMock, patch, AsyncMock, call
import sys
import os
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy import text

# Add service root to path so 'app' module can be found
service_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if service_root not in sys.path:
    sys.path.insert(0, service_root)

# Define project root for finding alembic env
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))

from app.consistency_checker import ConsistencyChecker
from app.models import ModelInfo

# Mock alembic context before importing env.py
from unittest.mock import MagicMock
import sys
import types

# Create mock alembic module
mock_alembic = types.ModuleType("alembic")
mock_context = MagicMock()
mock_context.config = MagicMock()
mock_context.config.config_file_name = None # Avoid fileConfig call
mock_alembic.context = mock_context
sys.modules["alembic"] = mock_alembic

# Now dynamically load env.py
import importlib.util
env_path = os.path.join(project_root, 'alembic', 'env.py')
spec = importlib.util.spec_from_file_location("alembic_env", env_path)
alembic_env = importlib.util.module_from_spec(spec)
sys.modules["alembic_env"] = alembic_env
spec.loader.exec_module(alembic_env)
include_object = alembic_env.include_object

@pytest.fixture
def mock_engine():
    engine = AsyncMock(spec=AsyncEngine)
    # Mock connect/begin context managers
    connection = AsyncMock()
    # Important: The result of execute() (when awaited) should be a MagicMock (synchronous), 
    # not an AsyncMock, because fetchall() is synchronous.
    result_mock = MagicMock()
    connection.execute.return_value = result_mock
    
    engine.begin.return_value.__aenter__.return_value = connection
    engine.connect.return_value.__aenter__.return_value = connection
    return engine

@pytest.fixture
def checker(mock_engine):
    return ConsistencyChecker(mock_engine)

@pytest.mark.asyncio
async def test_zone1_governance_alembic_exclusion():
    """
    Test Zone 1/2 Governance:
    Verify include_object excludes 'analytics_data' schema tables from Alembic.
    """
    # Mock objects
    table_obj = MagicMock()
    table_obj.schema = "analytics_data"
    
    # Test exclusion
    assert include_object(table_obj, "some_table", "table", False, None) is False
    
    # Test inclusion of public schema
    table_obj.schema = "public"
    assert include_object(table_obj, "some_table", "table", False, None) is True
    
    # Test inclusion of other types
    assert include_object(None, "some_index", "index", False, None) is True

@pytest.mark.asyncio
async def test_detect_missing_table(checker, mock_engine):
    """Test detection of missing tables in Zone 2."""
    # Setup
    definitions = [
        ModelInfo(
            name="TestModel",
            table_name="test_table",
            fields={"col1": "str"},
            relationships=[],
            source_file=""
        )
    ]
    
    # Mock existing tables (return empty)
    conn_mock = mock_engine.connect.return_value.__aenter__.return_value
    # execute() is an AsyncMock, so it returns a coroutine. 
    # That coroutine returns return_value (result_mock).
    # result_mock.fetchall is a MagicMock (sync), returns empty list.
    conn_mock.execute.return_value.fetchall.return_value = []
    
    # Run check
    issues = await checker.run_check(definitions)
    
    # Verify
    assert len(issues) == 1
    assert issues[0].category == "schema_drift"
    assert "missing in database schema" in issues[0].description
    assert issues[0].location == "analytics_data.test_table"

@pytest.mark.asyncio
async def test_detect_missing_column(checker, mock_engine):
    """Test detection of missing columns in Zone 2."""
    # Setup
    definitions = [
        ModelInfo(
            name="TestModel",
            table_name="test_table",
            fields={"col1": "str", "col2": "int"},
            relationships=[],
            source_file=""
        )
    ]
    
    # Mock existing tables (test_table has only col1)
    conn_mock = mock_engine.connect.return_value.__aenter__.return_value
    conn_mock.execute.return_value.fetchall.return_value = [
        ("test_table", "col1")
    ]
    
    # Run check
    issues = await checker.run_check(definitions)
    
    # Verify
    assert len(issues) == 1
    assert issues[0].category == "schema_drift"
    assert "Column 'col2' missing" in issues[0].description

@pytest.mark.asyncio
async def test_detect_orphaned_table(checker, mock_engine):
    """Test detection of orphaned tables."""
    # Setup - No definitions
    definitions = []
    
    # Mock existing tables (has orphan_table)
    conn_mock = mock_engine.connect.return_value.__aenter__.return_value
    conn_mock.execute.return_value.fetchall.return_value = [
        ("orphan_table", "col1")
    ]
    
    # Run check
    issues = await checker.run_check(definitions)
    
    # Verify
    assert len(issues) == 1
    assert "Orphaned table 'orphan_table'" in issues[0].description

@pytest.mark.asyncio
async def test_auto_repair_missing_table(checker, mock_engine):
    """Test auto-repair functionality for missing table."""
    # Setup
    definitions = [
        ModelInfo(
            name="TestModel",
            table_name="test_table",
            fields={"col1": "str"},
            relationships=[],
            source_file=""
        )
    ]
    
    # Mock finding missing table issue
    # We patch run_check to return a specific issue
    with patch.object(checker, 'run_check') as mock_check:
        from app.models import ValidationIssue
        mock_check.return_value = [
            ValidationIssue(
                severity="high", 
                category="schema_drift", 
                description="missing in database schema", 
                location="analytics_data.test_table"
            )
        ]
        
        # Run reconcile with auto_repair=True
        await checker.reconcile(definitions, auto_repair=True)
        
        # Verify CREATE TABLE executed
        conn_mock = mock_engine.begin.return_value.__aenter__.return_value
        assert conn_mock.execute.called
        
        # Check if any call matches our expectation
        found_create = False
        for call_obj in conn_mock.execute.call_args_list:
            args, _ = call_obj
            if args and "CREATE TABLE IF NOT EXISTS analytics_data.test_table" in str(args[0]):
                found_create = True
                break
        
        assert found_create, "CREATE TABLE statement not found in execute calls"
