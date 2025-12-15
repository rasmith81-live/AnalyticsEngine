import sys
import os
import unittest
import asyncio
from datetime import datetime
from typing import Dict, Any, List

# Add the service directory to sys.path
service_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if service_dir not in sys.path:
    sys.path.insert(0, service_dir)

# Mock missing dependencies from OTHER services
from unittest.mock import MagicMock
sys.modules["backend_services"] = MagicMock()
sys.modules["backend_services.messaging_service"] = MagicMock()
sys.modules["backend_services.messaging_service.app"] = MagicMock()
sys.modules["backend_services.messaging_service.app.event_publisher"] = MagicMock()

# Import the code to test
from app.engine.dependency_graph import DependencyGraph
from app.orchestrator import CalculationOrchestrator
from app.base_handler import BaseCalculationHandler, CalculationParams, CalculationResult

class MockHandler(BaseCalculationHandler):
    def __init__(self, code):
        super().__init__(
            value_chain_code=code,
            database_service_url="http://mock-db",
            messaging_service_url="http://mock-msg",
            metadata_service_url="http://mock-meta"
        )
    
    async def validate_params(self, params: CalculationParams):
        """Mock validation."""
        if not params.kpi_code:
            raise ValueError("KPI code required")

    def get_cache_key(self, params: CalculationParams) -> str:
        """Mock cache key."""
        return f"{params.kpi_code}:{params.time_period}"

    async def calculate(self, params: CalculationParams) -> CalculationResult:
        return CalculationResult(
            kpi_code=params.kpi_code,
            value=100.0,
            unit="percent",
            timestamp=datetime.utcnow(),
            calculation_time_ms=50.0,
            metadata={"mock": True}
        )

class TestCalculationOrchestration(unittest.TestCase):
    def test_dependency_graph_ordering(self):
        """Test topological sorting of dependencies."""
        print("\nTesting Dependency Graph...")
        graph = DependencyGraph()
        
        # A depends on B and C
        # B depends on D
        # C depends on D
        graph.add_dependency("A", "B")
        graph.add_dependency("A", "C")
        graph.add_dependency("B", "D")
        graph.add_dependency("C", "D")
        
        # D is independent (or depends on raw data, not another metric in this graph)
        graph.add_metrics(["A", "B", "C", "D"])
        
        order = graph.get_calculation_order(["A"])
        print(f"   Calculation Order: {order}")
        
        # Expected layers:
        # 1. [D] (independent)
        # 2. [B, C] (depend only on D)
        # 3. [A] (depends on B, C)
        
        self.assertEqual(len(order), 3)
        self.assertIn("D", order[0])
        self.assertTrue("B" in order[1] and "C" in order[1])
        self.assertIn("A", order[2])
        print("✅ Topological sort correct")

    def test_circular_dependency(self):
        """Test circular dependency detection."""
        print("\nTesting Circular Dependency Detection...")
        graph = DependencyGraph()
        graph.add_dependency("A", "B")
        graph.add_dependency("B", "A")
        
        with self.assertRaises(ValueError):
            graph.get_calculation_order(["A"])
        print("✅ Circular dependency detected")

    async def async_test_orchestrator(self):
        """Async test for orchestrator execution."""
        print("\nTesting Calculation Orchestrator...")
        orch = CalculationOrchestrator()
        
        # Register a handler
        handler = MockHandler("SUPPLY_CHAIN")
        orch.register_handler("SUPPLY_CHAIN", handler)
        
        # Map KPI to handler (normally loaded from metadata)
        orch.kpi_to_handler_map["PERFECT_ORDER"] = "SUPPLY_CHAIN"
        
        from datetime import datetime
        # Execute single calculation
        params = CalculationParams(
            kpi_code="PERFECT_ORDER",
            time_period="monthly",
            start_date=datetime(2025, 1, 1)
        )
        
        result = await orch.calculate_single(params)
        
        self.assertEqual(result.value, 100.0)
        self.assertEqual(result.kpi_code, "PERFECT_ORDER")
        print("✅ Orchestrator execution successful")

        # Execute batch calculation
        print("\nTesting Orchestrator Batch Calculation...")
        params_list = [
            CalculationParams(kpi_code="PERFECT_ORDER", time_period="monthly", start_date=datetime(2025, 1, 1)),
            CalculationParams(kpi_code="PERFECT_ORDER", time_period="monthly", start_date=datetime(2025, 2, 1))
        ]
        
        results = await orch.calculate_batch(params_list)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].value, 100.0)
        self.assertEqual(results[1].value, 100.0)
        print("✅ Orchestrator batch execution successful")

    def test_orchestrator(self):
        """Wrapper to run async test."""
        asyncio.run(self.async_test_orchestrator())

if __name__ == "__main__":
    unittest.main()
