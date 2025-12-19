
import unittest
import sys
import os
import json
from datetime import datetime, timedelta
from unittest.mock import MagicMock, patch, AsyncMock

# Add service dir to path
service_dir = os.path.dirname(os.path.abspath(__file__))
if service_dir not in sys.path:
    sys.path.insert(0, service_dir)

# Import attempts - these might fail if files don't exist yet
try:
    from app.engine.pricing import PricingCalculator
except ImportError:
    PricingCalculator = None

try:
    from app.engine.licensing import LicenseKeyGenerator, LicenseValidator
except ImportError:
    LicenseKeyGenerator = None
    LicenseValidator = None

try:
    from app.engine.scheduling import Scheduler, TimelineGenerator
except ImportError:
    Scheduler = None
    TimelineGenerator = None

try:
    from app.engine.scenarios import ScenarioManager
except ImportError:
    ScenarioManager = None

import logging

# Configure logging to see app logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app.main")
logger.setLevel(logging.INFO)

class TestDemoConfigService(unittest.TestCase):
    
    def test_pricing_calculator(self):
        """Validate PricingCalculator logic."""
        print("\nTesting PricingCalculator...")
        if not PricingCalculator:
            print("❌ PricingCalculator not implemented")
            self.fail("PricingCalculator not implemented")
            return

        calculator = PricingCalculator()
        estimate = calculator.calculate_proposal(
            num_objects=10,
            integration_method="realtime",
            hourly_rate=150.0
        )
        
        self.assertIn("estimated_cost", estimate)
        self.assertIn("estimated_hours", estimate)
        self.assertIn("timeline_weeks", estimate)
        print("✅ PricingCalculator logic valid")

    def test_license_management(self):
        """Validate License Management."""
        print("\nTesting License Management...")
        if not LicenseKeyGenerator or not LicenseValidator:
            print("❌ License components not implemented")
            self.fail("License components not implemented")
            return

        # Generate
        generator = LicenseKeyGenerator(secret_key="secret")
        key = generator.generate_key(
            client_id="client_1",
            modules=["mod_a", "mod_b"],
            expiration_date=datetime.utcnow() + timedelta(days=365)
        )
        self.assertIsNotNone(key)
        
        # Validate
        validator = LicenseValidator(secret_key="secret")
        is_valid, claims = validator.validate_key(key)
        
        if not is_valid:
            print(f"❌ License validation failed: {claims.get('error')}")
            # print token for debugging
            print(f"Token: {key}")
        
        self.assertTrue(is_valid, f"License validation failed: {claims.get('error')}")
        self.assertEqual(claims["client_id"], "client_1")
        self.assertIn("mod_a", claims["modules"])
        print("✅ License Generation & Validation successful")

    def test_resource_scheduling(self):
        """Validate Resource Scheduling."""
        print("\nTesting Resource Scheduling...")
        if not Scheduler:
            print("❌ Scheduler not implemented")
            self.fail("Scheduler not implemented")
            return

        scheduler = Scheduler()
        tasks = [
            {"id": "t1", "effort_hours": 40, "dependencies": []},
            {"id": "t2", "effort_hours": 20, "dependencies": ["t1"]}
        ]
        resources = [
            {"id": "r1", "availability_hours_per_week": 40}
        ]
        
        schedule = scheduler.generate_schedule(tasks, resources)
        self.assertIsNotNone(schedule)
        self.assertIn("start_date", schedule)
        self.assertIn("end_date", schedule)
        print("✅ Resource Scheduling logic valid")

    def test_scenario_manager(self):
        """Validate Scenario Manager."""
        print("\nTesting Scenario Manager...")
        if not ScenarioManager:
            print("❌ ScenarioManager not implemented")
            self.fail("ScenarioManager not implemented")
            return

        manager = ScenarioManager()
        # Mock database service for persistence
        manager.database_service = MagicMock()
        
        scenario_config = {
            "name": "Growth Scenario",
            "kpis": ["revenue"],
            "parameters": {"growth_rate": 0.1}
        }
        
        # Should generate data and return confirmation
        result = manager.generate_scenario(scenario_config)
        self.assertTrue(result["success"])
        print("✅ Scenario generation logic valid")

class TestDemoConfigAPI(unittest.TestCase):
    def setUp(self):
        from app.main import app
        from fastapi.testclient import TestClient
        self.client = TestClient(app)
        
    def test_custom_kpi_api(self):
        """Test Custom KPI API."""
        print("\nTesting Custom KPI API...")
        # 1. Create Client
        client_res = self.client.post("/api/configs", json={
            "client_name": "KPI Test Client",
            "selected_kpis": ["KPI_1"]
        })
        client_id = client_res.json()["client_id"]
        
        # 2. Create Custom KPI
        kpi_payload = {
            "kpi_code": "CUSTOM_ROI",
            "source_kpi_code": "ROI",
            "name": "Custom ROI",
            "formula": "ROI * 1.1",
            "unit": "Percentage",
            "created_by": "tester"
        }
        res = self.client.post(f"/api/configs/{client_id}/custom-kpis", json=kpi_payload)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["kpi_code"], "CUSTOM_ROI")
        print("✅ Custom KPI creation successful")
        
    def test_demo_data_api(self):
        """Test Demo Data Generation API."""
        print("\nTesting Demo Data API...")
        
        # Mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"name": "Test KPI", "unit": "USD"}
        
        # Mock client instance
        # We need the client to be an async context manager
        mock_client = MagicMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=None)
        mock_client.get = AsyncMock(return_value=mock_response)
        
        # Patch httpx.AsyncClient to return our mock instance
        with patch("app.main.httpx.AsyncClient", return_value=mock_client):
            payload = {
                "kpi_codes": ["KPI_TEST"],
                "data_points": 10
            }
            res = self.client.post("/api/demo/generate", json=payload)
            self.assertEqual(res.status_code, 200)
            data = res.json()
            
            if "KPI_TEST" not in data.get("data", {}):
                print(f"❌ API Response Data: {data}")
            
            self.assertIn("KPI_TEST", data["data"])
            self.assertEqual(len(data["data"]["KPI_TEST"]["time_series"]), 10)
            print("✅ Demo Data generation successful")
            
    def test_proposal_api(self):
        """Test Service Proposal API."""
        print("\nTesting Proposal API...")
        # Mock metadata analysis
        with patch("app.main.analyze_required_objects") as mock_analyze:
            mock_analyze.return_value = MagicMock(
                required_objects=["obj1", "obj2", "obj3"]
            )
            # Make the mock object awaitable since the function is async
            async def async_return(*args, **kwargs):
                return mock_analyze.return_value
            
            # We need to patch the function itself in app.main, but if it's called directly...
            # The route calls `analyze_required_objects`.
            # Let's verify if `analyze_required_objects` is imported or defined in main.
            # It is defined in main. So patch "app.main.analyze_required_objects".
            # But wait, analyze_required_objects is an async function, so the mock should return a coroutine or be AsyncMock.
            
            mock_analyze.side_effect = async_return 
            # Or just use AsyncMock if available, or configure MagicMock
            
            payload = {
                "client_id": "test_client",
                "kpi_codes": ["KPI_A", "KPI_B"],
                "integration_method": "realtime"
            }
            # We also need to patch httpx in analyze_required_objects if we didn't mock the function entirely.
            # But we are trying to mock the function entirely.
            
            # Actually, `analyze_required_objects` in main.py uses httpx internally.
            # If we mock `app.main.analyze_required_objects`, we bypass the httpx call.
            
            with patch("app.main.analyze_required_objects", new_callable=AsyncMock) as mock_analyze_func:
                mock_analyze_func.return_value = MagicMock(
                    required_objects=["obj1", "obj2", "obj3"]
                )
                
                res = self.client.post("/api/proposals", json=payload)
                self.assertEqual(res.status_code, 200)
                data = res.json()
                self.assertGreater(data["estimated_cost"], 0)
                self.assertEqual(len(data["required_objects"]), 3)
                print("✅ Service Proposal generation successful")

if __name__ == "__main__":
    unittest.main()
