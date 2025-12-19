
import sys
import os
import unittest
from unittest.mock import MagicMock, AsyncMock, patch
from datetime import datetime
import uuid

# Add service directory to sys.path
service_dir = os.path.dirname(os.path.abspath(__file__))
if service_dir not in sys.path:
    sys.path.insert(0, service_dir)

from app.models import ClientConfigCreate, ClientConfigUpdate, ClientConfigResponse
from fastapi.testclient import TestClient
from app.main import app

class TestClientConfiguration(unittest.TestCase):
    
    def setUp(self):
        self.client = TestClient(app)
        
    def test_client_config_models(self):
        """Test ClientConfig Pydantic models."""
        print("\nTesting ClientConfig Models...")
        
        # Test Create
        create_data = {
            "client_name": "Test Client",
            "selected_kpis": ["KPI_1", "KPI_2"],
            "data_sources": [{"type": "csv", "path": "/data.csv"}]
        }
        config_create = ClientConfigCreate(**create_data)
        self.assertEqual(config_create.client_name, "Test Client")
        print("✅ ClientConfigCreate model valid")
        
        # Test Update
        update_data = {
            "selected_kpis": ["KPI_3"]
        }
        config_update = ClientConfigUpdate(**update_data)
        self.assertEqual(config_update.selected_kpis, ["KPI_3"])
        print("✅ ClientConfigUpdate model valid")

    def test_create_and_get_config(self):
        """Test creating and retrieving client config via API."""
        print("\nTesting Create/Get Config API...")
        
        # Create
        payload = {
            "client_name": "API Test Client",
            "selected_kpis": ["KPI_A"],
            "deployment_config": {"env": "prod"}
        }
        response = self.client.post("/api/configs", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["client_name"], "API Test Client")
        self.assertIsNotNone(data["id"])
        
        client_id = data["client_id"]
        print(f"✅ Created config for client_id: {client_id}")
        
        # Get
        response = self.client.get(f"/api/configs/{client_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["client_id"], client_id)
        print("✅ Retrieved config successfully")
        
        return client_id

    def test_update_config_cascade(self):
        """Test updating config and verifying cascading logic (Mocked)."""
        print("\nTesting Update Config & Cascade Logic...")
        
        # First create a client
        payload = {"client_name": "Update Test", "selected_kpis": ["OLD_KPI"]}
        create_res = self.client.post("/api/configs", json=payload)
        client_id = create_res.json()["client_id"]
        
        # Mock the event publisher (cascading logic)
        # We patch the internal helper function _publish_config_change
        
        with patch("app.main._publish_config_change", new_callable=AsyncMock) as mock_publish:
            
            update_payload = {"selected_kpis": ["NEW_KPI"]}
            response = self.client.put(f"/api/configs/{client_id}", json=update_payload)
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()["selected_kpis"], ["NEW_KPI"])
            print("✅ Config updated successfully")
            
            # Check for cascade
            if mock_publish.called:
                print("✅ Cascade event published")
                # Verify arguments
                args = mock_publish.call_args
                self.assertEqual(args[0][0], client_id)
                self.assertIn("selected_kpis", args[0][1])
            else:
                print("⚠️  Cascade logic (event publishing) appears missing")
                self.fail("Cascade logic missing")

if __name__ == "__main__":
    unittest.main()
