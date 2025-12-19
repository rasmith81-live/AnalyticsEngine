import unittest
import sys
import os
import asyncio
from unittest.mock import MagicMock, patch, AsyncMock
from datetime import datetime

# Add parent directory to path to allow importing app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models import MLModelResponse, TrainingJobResponse, ServiceHealth, DependencyStatus
from app.api.endpoints import get_model, get_job_status, get_service_status

class TestMachineLearningService(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        # Mock dependencies
        self.mock_db_client = AsyncMock()
        self.mock_messaging_client = AsyncMock()
        
        # Setup common return values
        self.mock_model_data = {
            "id": "model_123",
            "name": "Test Model",
            "description": "A test model",
            "type": "classification",
            "metadata": {"accuracy": 0.95},
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "latest_version": "1.0.0"
        }
        
        self.mock_job_data = {
            "id": "job_123",
            "model_id": "model_123",
            "dataset_id": "dataset_001",
            "status": "completed",
            "started_at": datetime.utcnow(),
            "finished_at": datetime.utcnow(),
            "hyperparameters": {"learning_rate": 0.01},
            "progress": 100
        }

    async def test_get_model(self):
        """Test retrieving a model by ID."""
        print("\nTesting Get Model...")
        
        # Setup mock behavior
        self.mock_db_client.get_model.return_value = self.mock_model_data
        
        # Call endpoint
        response = await get_model(
            model_id="model_123", 
            database_client=self.mock_db_client
        )
        
        # Verify response
        self.assertIsInstance(response, MLModelResponse)
        self.assertEqual(response.id, "model_123")
        self.assertEqual(response.name, "Test Model")
        
        # Verify client call
        self.mock_db_client.get_model.assert_called_once_with("model_123")
        print("✅ Get Model verified")

    async def test_get_job_status(self):
        """Test retrieving a training job status."""
        print("\nTesting Get Job Status...")
        
        # Setup mock behavior
        self.mock_db_client.get_job.return_value = self.mock_job_data
        
        # Call endpoint
        response = await get_job_status(
            job_id="job_123",
            database_client=self.mock_db_client
        )
        
        # Verify response
        self.assertIsInstance(response, TrainingJobResponse)
        self.assertEqual(response.id, "job_123")
        self.assertEqual(response.status, "completed")
        
        # Verify client call
        self.mock_db_client.get_job.assert_called_once_with("job_123")
        print("✅ Get Job Status verified")

    async def test_service_health(self):
        """Test service health check with dependencies."""
        print("\nTesting Service Health...")
        
        # Setup mock behavior
        self.mock_db_client.check_health.return_value = {"status": "healthy"}
        self.mock_messaging_client.check_health.return_value = {"status": "healthy"}
        
        # Setup mock attributes
        self.mock_db_client.base_url = "http://db-service"
        self.mock_messaging_client.base_url = "http://messaging-service"
        
        # Mock get_service_uptime
        with patch("app.api.endpoints.get_service_uptime", return_value=3600):
            response = await get_service_status(
                messaging_client=self.mock_messaging_client,
                database_client=self.mock_db_client
            )
            
            # Verify response
            self.assertIsInstance(response, ServiceHealth)
            self.assertEqual(response.status, "healthy")
            self.assertEqual(response.uptime_seconds, 3600)
            
            # Check dependencies
            db_dep = next(d for d in response.dependencies if d.service_name == "database_service")
            self.assertEqual(db_dep.status, "healthy")
            
        print("✅ Service Health verified")

if __name__ == "__main__":
    unittest.main()
