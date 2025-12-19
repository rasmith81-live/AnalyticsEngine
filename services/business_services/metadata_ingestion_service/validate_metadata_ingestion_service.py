import unittest
import asyncio
from unittest.mock import MagicMock, AsyncMock, patch
from fastapi.testclient import TestClient
import sys
import os

# Add parent directory to path to allow importing app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.main import app
from app.industry_knowledge_base import NAICClassificationIterator
from app.semantic_mapping import KPIDecomposer

class TestMetadataIngestionService(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.naic = NAICClassificationIterator()
        self.decomposer = KPIDecomposer(entity_resolution_service_url="http://mock-service")

    def test_health_check(self):
        """Test health check endpoint."""
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "healthy")

    def test_industry_iterator(self):
        """Test NAIC industry iteration logic."""
        print("\nTesting Industry Iterator...")
        
        async def run_test():
            industries = []
            async for ind in self.naic.iterate_industries():
                industries.append(ind)
            return industries
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(run_test())
        loop.close()
        
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0]["code"], "524114")
        print("✅ Industry Iterator verified")

    def test_value_chain_generation(self):
        """Test value chain generation logic."""
        print("\nTesting Value Chain Generation...")
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(self.naic.generate_value_chain_set("524114"))
        loop.close()
        
        self.assertEqual(result["industry_code"], "524114")
        self.assertIn("Sales", result["modules"])
        print("✅ Value Chain Generation verified")

    def test_semantic_decomposition(self):
        """Test KPI formula decomposition."""
        print("\nTesting Semantic Decomposition...")
        
        formula = "(Revenue - Cost) / Revenue"
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(self.decomposer.decompose_formula(formula))
        loop.close()
        
        self.assertEqual(result["original_formula"], formula)
        self.assertIn("Revenue", result["identified_attributes"])
        self.assertIn("Cost", result["identified_attributes"])
        print("✅ Semantic Decomposition verified")

    @patch('app.semantic_mapping.KPIDecomposer.resolve_components')
    def test_decompose_endpoint(self, mock_resolve):
        """Test decompose API endpoint."""
        print("\nTesting Decompose API...")
        
        # Mock resolution
        mock_resolve.return_value = {"Revenue": "Canonical_Revenue"}
        
        payload = {"formula": "Revenue * 1.2"}
        response = self.client.post("/mapping/decompose", json=payload)
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        
        self.assertIn("Revenue", data["decomposed"]["identified_attributes"])
        print("✅ Decompose API verified")

    @patch('httpx.AsyncClient')
    def test_excel_upload_and_commit(self, mock_httpx_client):
        """Test Excel upload and commit flow."""
        print("\nTesting Excel Upload & Commit Flow...")
        
        # 1. Create dummy CSV
        csv_content = "KPI,Definition,Standard Formula\nTest KPI,A test metric,Revenue / Cost"
        files = {"file": ("test.csv", csv_content, "text/csv")}
        
        # 2. Upload
        response_upload = self.client.post("/import/upload", files=files)
        self.assertEqual(response_upload.status_code, 200)
        result_upload = response_upload.json()
        
        self.assertIn("importId", result_upload)
        self.assertEqual(result_upload["totalRows"], 1)
        self.assertEqual(result_upload["validRows"], 1)
        self.assertEqual(result_upload["preview"][0]["Name"], "Test KPI")
        
        import_id = result_upload["importId"]
        
        # 3. Mock Metadata Service Call for Commit
        # We need to mock the context manager structure of httpx.AsyncClient
        
        # Create a sync Mock for the response object
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"ids": ["uuid-1"]}
        
        # The post method is async, so it returns a coroutine that resolves to mock_response
        mock_post = AsyncMock()
        mock_post.return_value = mock_response
        
        mock_client_instance = AsyncMock()
        mock_client_instance.post = mock_post
        mock_httpx_client.return_value.__aenter__.return_value = mock_client_instance
        
        # 4. Commit
        # Note: TestClient runs in a sync context, but the app is async. 
        # Since we are mocking the async client used internally, it should be fine.
        response_commit = self.client.post(f"/import/{import_id}/commit")
        
        if response_commit.status_code != 200:
            print(f"\n❌ Commit failed with status {response_commit.status_code}")
            print(f"Response: {response_commit.text}")
        
        self.assertEqual(response_commit.status_code, 200)
        result_commit = response_commit.json()
        
        self.assertTrue(result_commit["success"])
        self.assertEqual(result_commit["count"], 1)
        self.assertEqual(result_commit["ids"], ["uuid-1"])
        
        print("✅ Excel Upload & Commit Flow verified")

    def test_formula_safety_validation(self):
        """Test that unsafe formulas are rejected."""
        print("\nTesting Formula Safety Validation...")
        
        # Create CSV with unsafe formula
        # Note: We must quote the formula because it contains commas
        csv_content = 'KPI,Definition,Standard Formula\nBad KPI,Unsafe,"VLOOKUP(A1, B:C, 2, FALSE)"\nGood KPI,Safe,Revenue / 2'
        files = {"file": ("unsafe.csv", csv_content, "text/csv")}
        
        response = self.client.post("/import/upload", files=files)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        
        # Should have 1 error (Bad KPI) and 1 valid (Good KPI)
        self.assertEqual(result["totalRows"], 2)
        self.assertEqual(result["validRows"], 1)
        self.assertEqual(len(result["errors"]), 1)
        
        error = result["errors"][0]
        self.assertIn("Unsupported Excel function", error["message"])
        self.assertIn("VLOOKUP", error["message"])
        
        print("✅ Formula Safety Validation verified")

if __name__ == "__main__":
    unittest.main()
