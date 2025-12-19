import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add the service directory to sys.path
service_dir = os.path.dirname(os.path.abspath(__file__))
if service_dir not in sys.path:
    sys.path.insert(0, service_dir)

from app.connection_manager import ConnectionManager, ConnectionProfile, ConnectionType
from app.schema_discovery import SchemaDiscoveryEngine, TableDefinition, ColumnDefinition

class TestConnectorService(unittest.TestCase):

    def test_connection_manager_sql(self):
        """Test SQL connection testing logic."""
        print("\nTesting SQL Connection Manager...")
        manager = ConnectionManager()
        profile = ConnectionProfile(
            id="test-1",
            name="Test DB",
            type=ConnectionType.SQL_POSTGRES,
            host="localhost",
            port=5432,
            database="testdb",
            username="user",
            password="password"
        )
        
        with patch("sqlalchemy.create_engine") as mock_engine:
            mock_conn = MagicMock()
            mock_engine.return_value.connect.return_value.__enter__.return_value = mock_conn
            
            result = manager._test_sql(profile)
            self.assertTrue(result)
            mock_engine.assert_called_once()
            
        print("✅ SQL Connection test passed")

    def test_connection_manager_api(self):
        """Test REST API connection testing logic."""
        print("\nTesting API Connection Manager...")
        manager = ConnectionManager()
        profile = ConnectionProfile(
            id="test-2",
            name="Test API",
            type=ConnectionType.REST_API,
            api_url="http://api.example.com"
        )
        
        with patch("requests.get") as mock_get:
            mock_get.return_value.status_code = 200
            
            result = manager._test_api(profile)
            self.assertTrue(result)
            mock_get.assert_called_with("http://api.example.com", timeout=5)
            
        print("✅ API Connection test passed")

    def test_schema_discovery_sql(self):
        """Test SQL Schema Discovery."""
        print("\nTesting SQL Schema Discovery...")
        engine = SchemaDiscoveryEngine()
        
        with patch("app.schema_discovery.sqlalchemy.create_engine") as mock_create_engine, \
             patch("app.schema_discovery.inspect") as mock_inspect:
            
            mock_inspector = MagicMock()
            mock_inspect.return_value = mock_inspector
            
            # Mock tables
            mock_inspector.get_table_names.return_value = ["users"]
            
            # Mock columns
            mock_inspector.get_columns.return_value = [
                {"name": "id", "type": "INTEGER", "nullable": False},
                {"name": "name", "type": "VARCHAR", "nullable": True}
            ]
            
            # Mock PK
            mock_inspector.get_pk_constraint.return_value = {
                "constrained_columns": ["id"]
            }
            
            schema = engine.discover("sql", {"connection_string": "sqlite:///:memory:"})
            
            self.assertEqual(len(schema), 1)
            table = schema[0]
            self.assertEqual(table.name, "users")
            self.assertEqual(len(table.columns), 2)
            
            col_id = next(c for c in table.columns if c.name == "id")
            self.assertTrue(col_id.is_primary_key)
            self.assertEqual(col_id.data_type, "INTEGER")
            
        print("✅ SQL Schema Discovery passed")

    def test_schema_discovery_rest(self):
        """Test REST API Schema Discovery (Inference)."""
        print("\nTesting REST Schema Discovery...")
        engine = SchemaDiscoveryEngine()
        
        with patch("requests.get") as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = [
                {"id": 1, "name": "Alice", "active": True}
            ]
            
            schema = engine.discover("rest", {
                "base_url": "http://api.example.com",
                "endpoint": "users"
            })
            
            self.assertEqual(len(schema), 1)
            table = schema[0]
            self.assertEqual(table.name, "users")
            
            col_names = [c.name for c in table.columns]
            self.assertIn("id", col_names)
            self.assertIn("name", col_names)
            self.assertIn("active", col_names)
            
            # Verify type inference
            col_active = next(c for c in table.columns if c.name == "active")
            self.assertEqual(col_active.data_type, "bool")
            
        print("✅ REST Schema Discovery passed")

if __name__ == "__main__":
    unittest.main()
