import sys
import os
import unittest
import asyncio
from unittest.mock import MagicMock, AsyncMock, patch
from typing import Dict, Any, List
import uuid

# Mock opentelemetry modules before they are imported by dependencies
sys.modules["opentelemetry"] = MagicMock()
sys.modules["opentelemetry.trace"] = MagicMock()
sys.modules["opentelemetry.instrumentation"] = MagicMock()
sys.modules["opentelemetry.instrumentation.httpx"] = MagicMock()
sys.modules["opentelemetry.instrumentation.fastapi"] = MagicMock()
sys.modules["opentelemetry.instrumentation.sqlalchemy"] = MagicMock()
sys.modules["opentelemetry.instrumentation.aiohttp_client"] = MagicMock()  # Added this
sys.modules["opentelemetry.instrumentation.redis"] = MagicMock()  # Added this
sys.modules["opentelemetry.sdk"] = MagicMock()
sys.modules["opentelemetry.sdk.trace"] = MagicMock()
sys.modules["opentelemetry.sdk.trace.sampling"] = MagicMock()  # Added this
sys.modules["opentelemetry.sdk.resources"] = MagicMock()
sys.modules["opentelemetry.sdk.trace.export"] = MagicMock()
sys.modules["opentelemetry.exporter"] = MagicMock()
sys.modules["opentelemetry.exporter.otlp"] = MagicMock()
sys.modules["opentelemetry.exporter.otlp.proto"] = MagicMock()
sys.modules["opentelemetry.exporter.otlp.proto.grpc"] = MagicMock()
sys.modules["opentelemetry.exporter.otlp.proto.grpc.trace_exporter"] = MagicMock()
sys.modules["opentelemetry.trace.propagation"] = MagicMock() # Often used
sys.modules["opentelemetry.trace.propagation.tracecontext"] = MagicMock() # Added this
sys.modules["opentelemetry.context"] = MagicMock() # Often used

# Add the directory ABOVE business_metadata to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import models
from business_metadata.ontology_models import (
    InterviewSessionDefinition,
    UtteranceDefinition,
    BusinessIntentDefinition,
    CompanyValueChainModelDefinition
)

# Import Service to test
from business_metadata.services.metadata_service import MetadataService
from business_metadata.services.metadata_instantiation_service import MetadataInstantiationService

class TestConversationModeling(unittest.TestCase):
    def setUp(self):
        # Mock repositories
        self.mock_write_repo = AsyncMock()
        self.mock_query_repo = AsyncMock()
        self.instantiation_service = MetadataInstantiationService()
        
        # Initialize service with mocks
        self.metadata_service = MetadataService(
            write_repo=self.mock_write_repo,
            query_repo=self.mock_query_repo,
            instantiation_service=self.instantiation_service
        )

    def test_model_definitions(self):
        """Test basic Pydantic model instantiation."""
        print("\nTesting Conversation Modeling Models...")
        
        # 1. Interview Session
        session = InterviewSessionDefinition(
            kind="interview_session_definition",
            id="sess_123",
            name="Session 123",
            company_id="comp_acme",
            participants=["user_bob", "bot_cascade"],
            started_at="2025-01-01T10:00:00Z"
        )
        self.assertEqual(session.id, "sess_123")
        print("✅ InterviewSessionDefinition created")
        
        # 2. Derived Value Chain Model
        model = CompanyValueChainModelDefinition(
            kind="company_value_chain_model_definition",
            id="model_v1",
            name="Acme Supply Chain Model",
            company_id="comp_acme",
            session_id="sess_123",
            derived_from="conversation",
            included_nodes=["node_supplier", "node_warehouse"],
            applied_patterns=["pat_supply_chain_optimization"]
        )
        self.assertEqual(model.derived_from, "conversation")
        print("✅ CompanyValueChainModelDefinition created")

    def test_persist_generated_model(self):
        """Test logic for persisting a generated value chain model."""
        print("\nTesting Persistence Logic...")
        
        # Mock Input Data (from Conversation Service)
        session_id = "sess_test_123"
        user_id = "user_test"
        model_data = {
            "name": "Generated Supply Chain",
            "nodes": [
                {
                    "id": "node_1",
                    "name": "Receive Goods",
                    "type": "Process",
                    "description": "Receiving inventory at dock"
                },
                {
                    "id": "node_2",
                    "name": "Inventory Accuracy",
                    "type": "Metric",
                    "description": "Percentage of accurate counts"
                }
            ],
            "links": [
                {
                    "source_id": "node_1",
                    "target_id": "node_2",
                    "type": "measures"
                }
            ]
        }
        
        # Mock create_definition to return a UUID
        self.mock_write_repo.create_definition.return_value = uuid.uuid4()
        
        # Run async test
        async def run_test():
            await self.metadata_service.persist_generated_model(
                session_id=session_id,
                user_id=user_id,
                model_data=model_data
            )
        
        asyncio.run(run_test())
        
        # Verify Interactions
        
        # 1. Verify Nodes were created (2 nodes + 1 container model = 3 calls)
        # However, persist_generated_model calls create_definition (Service method) which calls write_repo.create_definition
        # We mocked write_repo.
        # MetadataService.create_definition handles the translation to write_repo calls.
        
        # Check calls to write_repo.create_definition
        self.assertEqual(self.mock_write_repo.create_definition.call_count, 3)
        
        calls = self.mock_write_repo.create_definition.call_args_list
        
        # Inspect created definitions
        created_kinds = [call.kwargs['kind'] for call in calls]
        print(f"Created Kinds: {created_kinds}")
        
        self.assertIn("business_process_definition", created_kinds)
        self.assertIn("metric_definition", created_kinds)
        self.assertIn("company_value_chain_model_definition", created_kinds)
        
        # 2. Verify Relationships were created
        # One link in input -> One relationship created
        self.mock_write_repo.create_relationship.assert_called_once()
        rel_kwargs = self.mock_write_repo.create_relationship.call_args.kwargs
        self.assertEqual(rel_kwargs['relationship_type'], "measures")
        print("✅ Relationships created")
        
        print("✅ persist_generated_model logic verified")

if __name__ == "__main__":
    unittest.main()
