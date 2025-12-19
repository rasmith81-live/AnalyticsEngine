import unittest
import sys
import os
import asyncio
from datetime import datetime
import pandas as pd
from unittest.mock import MagicMock, AsyncMock, patch

# Add the service directory to sys.path
service_dir = os.path.dirname(os.path.abspath(__file__))
if service_dir not in sys.path:
    sys.path.insert(0, service_dir)

from app.pipeline import PipelineOrchestrator, IngestionJob
from app.transformation_engine import TransformationEngine

class TestIngestionService(unittest.TestCase):
    
    def setUp(self):
        self.orchestrator = PipelineOrchestrator()
        self.transformer = TransformationEngine()

    def test_pipeline_job_creation(self):
        """Test creating an ingestion job."""
        print("\nTesting Job Creation...")
        
        job = IngestionJob(
            job_id="job_1",
            connection_id="conn_1",
            target_entity="customers",
            schedule="immediate",
            status="PENDING"
        )
        
        # Run async method
        asyncio.run(self.orchestrator.create_job(job))
        
        self.assertIn("job_1", self.orchestrator.jobs)
        self.assertEqual(self.orchestrator.jobs["job_1"].status, "PENDING")
        print("✅ Job creation verified")

    def test_pipeline_job_execution(self):
        """Test running an ingestion job."""
        print("\nTesting Job Execution...")
        
        # Mock extractor to avoid network calls
        self.orchestrator.extractor.extract_data = AsyncMock(return_value=[{"id": 1, "val": "A"}])
        
        job = IngestionJob(
            job_id="job_2",
            connection_id="conn_2",
            target_entity="orders",
            schedule="immediate",
            status="PENDING"
        )
        self.orchestrator.jobs["job_2"] = job
        
        status = asyncio.run(self.orchestrator.run_job("job_2"))
        
        self.assertEqual(status, "COMPLETED")
        self.assertEqual(self.orchestrator.jobs["job_2"].status, "COMPLETED")
        print("✅ Job execution verified")

    def test_transformation_sql(self):
        """Test SQL-like transformation (pandas eval)."""
        print("\nTesting Transformation (SQL/Eval)...")
        
        df = pd.DataFrame({
            'price': [10, 20, 30],
            'quantity': [2, 1, 3]
        })
        
        rules = [{
            'type': 'sql_expression',
            'target_column': 'total',
            'expression': 'price * quantity'
        }]
        
        result_df = asyncio.run(self.transformer.apply_transformations(df, rules))
        
        self.assertTrue('total' in result_df.columns)
        self.assertEqual(result_df.iloc[0]['total'], 20)
        self.assertEqual(result_df.iloc[2]['total'], 90)
        print("✅ SQL/Eval transformation verified")

    def test_transformation_python(self):
        """Test custom Python script transformation."""
        print("\nTesting Transformation (Python Script)...")
        
        df = pd.DataFrame({
            'name': ['Alice', 'Bob']
        })
        
        # Script that adds a column
        script = """
df['greeting'] = 'Hello ' + df['name']
"""
        
        rules = [{
            'type': 'python_script',
            'script': script
        }]
        
        result_df = asyncio.run(self.transformer.apply_transformations(df, rules))
        
        self.assertTrue('greeting' in result_df.columns)
        self.assertEqual(result_df.iloc[0]['greeting'], 'Hello Alice')
        print("✅ Python script transformation verified")

if __name__ == "__main__":
    unittest.main()
