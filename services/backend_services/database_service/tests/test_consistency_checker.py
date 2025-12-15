
import pytest
from unittest.mock import MagicMock, patch, AsyncMock
from sqlalchemy import text

import sys
import os

# Add service root to path so 'app' module can be found
service_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if service_root not in sys.path:
    sys.path.insert(0, service_root)

from app.consistency_checker import ConsistencyChecker
from app.models import ModelInfo

@pytest.fixture
def mock_engine():
    engine = MagicMock()
    
    # Connection mock
    conn = AsyncMock()
    conn.execute = AsyncMock()
    
    # Context manager mock that returns the connection
    cm = AsyncMock()
    cm.__aenter__.return_value = conn
    cm.__aexit__.return_value = None
    
    # Engine methods return the context manager
    engine.connect.return_value = cm
    engine.begin.return_value = cm
    
    return engine

@pytest.fixture
def checker(mock_engine):
    return ConsistencyChecker(mock_engine)

@pytest.mark.asyncio
async def test_check_missing_table(checker, mock_engine):
    # Setup: No existing tables
    # _get_existing_tables queries information_schema
    conn = mock_engine.connect.return_value.__aenter__.return_value
    result_mock = MagicMock()
    result_mock.fetchall.return_value = [] # No tables
    conn.execute.return_value = result_mock

    definitions = [
        ModelInfo(
            name="TestModel",
            table_name="test_table",
            fields={"id": "int", "name": "str"},
            relationships=[]
        )
    ]

    issues = await checker.run_check(definitions)
    
    if issues and issues[0].category == "system_error":
        print(f"DEBUG: System Error: {issues[0].description}")

    assert len(issues) == 1
    assert issues[0].category == "schema_drift"
    assert "missing in database schema" in issues[0].description
    assert issues[0].location == "analytics_data.test_table"

@pytest.mark.asyncio
async def test_check_missing_column(checker, mock_engine):
    # Setup: Table exists but missing 'name' column
    conn = mock_engine.connect.return_value.__aenter__.return_value
    result_mock = MagicMock()
    # Returns (table_name, column_name)
    result_mock.fetchall.return_value = [("test_table", "id")] 
    conn.execute.return_value = result_mock

    definitions = [
        ModelInfo(
            name="TestModel",
            table_name="test_table",
            fields={"id": "int", "name": "str"},
            relationships=[]
        )
    ]

    issues = await checker.run_check(definitions)
    
    if issues and issues[0].category == "system_error":
        print(f"DEBUG: System Error: {issues[0].description}")

    assert len(issues) == 1
    assert issues[0].category == "schema_drift"
    assert "Column 'name' missing" in issues[0].description
    assert issues[0].location == "analytics_data.test_table.name"

@pytest.mark.asyncio
async def test_check_orphaned_table(checker, mock_engine):
    # Setup: Extra table in DB
    conn = mock_engine.connect.return_value.__aenter__.return_value
    result_mock = MagicMock()
    result_mock.fetchall.return_value = [("test_table", "id"), ("orphaned_table", "id")]
    conn.execute.return_value = result_mock

    definitions = [
        ModelInfo(
            name="TestModel",
            table_name="test_table",
            fields={"id": "int"},
            relationships=[]
        )
    ]

    issues = await checker.run_check(definitions)
    
    # Expect 1 issue for orphaned table
    assert len(issues) == 1
    assert issues[0].category == "schema_drift"
    assert "Orphaned table 'orphaned_table'" in issues[0].description

@pytest.mark.asyncio
async def test_auto_repair_missing_table(checker, mock_engine):
    # Setup: Missing table
    conn = mock_engine.connect.return_value.__aenter__.return_value
    result_mock = MagicMock()
    result_mock.fetchall.return_value = []
    conn.execute.return_value = result_mock
    
    # Mock begin() context for repair operations
    trans_conn = mock_engine.begin.return_value.__aenter__.return_value
    
    definitions = [
        ModelInfo(
            name="TestModel",
            table_name="test_table",
            fields={"name": "str"},
            relationships=[]
        )
    ]

    await checker.reconcile(definitions, auto_repair=True)
    
    # Verify CREATE TABLE was called
    # We expect ensure_schema first, then CREATE TABLE
    assert trans_conn.execute.call_count >= 1
    
    # Check arguments of execute calls to find CREATE TABLE
    create_called = False
    for call in trans_conn.execute.call_args_list:
        sql = str(call[0][0])
        if "CREATE TABLE IF NOT EXISTS analytics_data.test_table" in sql:
            create_called = True
            break
            
    assert create_called

@pytest.mark.asyncio
async def test_auto_repair_missing_column(checker, mock_engine):
    # Setup: Missing column
    conn = mock_engine.connect.return_value.__aenter__.return_value
    result_mock = MagicMock()
    result_mock.fetchall.return_value = [("test_table", "id")]
    conn.execute.return_value = result_mock
    
    trans_conn = mock_engine.begin.return_value.__aenter__.return_value
    
    definitions = [
        ModelInfo(
            name="TestModel",
            table_name="test_table",
            fields={"id": "int", "new_col": "str"},
            relationships=[]
        )
    ]

    await checker.reconcile(definitions, auto_repair=True)
    
    # Verify ALTER TABLE was called
    alter_called = False
    for call in trans_conn.execute.call_args_list:
        sql = str(call[0][0])
        if "ALTER TABLE analytics_data.test_table ADD COLUMN IF NOT EXISTS new_col" in sql:
            alter_called = True
            break
            
    assert alter_called
