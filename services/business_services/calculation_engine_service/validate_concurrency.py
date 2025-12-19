
import unittest
import asyncio
from unittest.mock import MagicMock, AsyncMock
import sys
import os
import logging
from datetime import datetime

# Add service dir to path
service_dir = os.path.dirname(os.path.abspath(__file__))
if service_dir not in sys.path:
    sys.path.insert(0, service_dir)

from app.orchestrator import CalculationOrchestrator
from app.base_handler import BaseCalculationHandler, CalculationParams, CalculationResult

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MockSlowHandler(BaseCalculationHandler):
    def __init__(self):
        super().__init__("TEST_CHAIN", "db", "msg", "meta", cache_enabled=False)
        self.call_count = 0
        
    async def calculate(self, params: CalculationParams) -> CalculationResult:
        self.call_count += 1
        logger.info(f"Handler executing calculation (Call #{self.call_count})")
        # Simulate work
        await asyncio.sleep(0.5)
        return CalculationResult(
            kpi_code=params.kpi_code,
            value=100.0,
            unit="USD",
            timestamp=datetime.utcnow(),
            calculation_time_ms=500
        )

    async def validate_params(self, params):
        return True
        
    def get_cache_key(self, params):
        return "key"

class TestHighConcurrency(unittest.TestCase):
    
    def test_request_coalescing(self):
        """Test Single-flight/Request Coalescing logic."""
        print("\nTesting Request Coalescing (Single-flight)...")
        
        async def run_test():
            orchestrator = CalculationOrchestrator()
            handler = MockSlowHandler()
            
            # Register handler
            orchestrator.register_handler("TEST_CHAIN", handler)
            # Mock mapping
            orchestrator.kpi_to_handler_map["KPI_1"] = "TEST_CHAIN"
            
            params = CalculationParams(kpi_code="KPI_1")
            
            # Launch 5 concurrent identical requests
            tasks = [orchestrator.calculate_single(params) for _ in range(5)]
            
            logger.info("Launching 5 concurrent requests...")
            results = await asyncio.gather(*tasks)
            
            # Verify results
            self.assertEqual(len(results), 5)
            self.assertEqual(results[0].value, 100.0)
            
            # CRITICAL: Handler should have been called ONLY ONCE
            print(f"Handler called {handler.call_count} times")
            self.assertEqual(handler.call_count, 1, "Request coalescing failed: Handler called multiple times")
            print("✅ Request coalescing successful: 5 requests -> 1 execution")
            
        asyncio.run(run_test())

    def test_hierarchical_query_logic(self):
        """Verify Hierarchical Query Logic (via TimescaleManager)."""
        print("\nTesting Hierarchical Query Logic...")
        from app.engine.timescale_manager import TimescaleManager
        from datetime import timedelta
        
        manager = TimescaleManager()
        now = datetime.utcnow()
        
        # Test cases
        cases = [
            (timedelta(days=1), "raw_table", "1m"),  # Short duration -> Raw
            (timedelta(days=10), "raw_table_hourly_agg", "1 hour"), # > 1 week -> Hourly
            (timedelta(days=40), "raw_table_daily_agg", "1 day"),   # > 1 month -> Daily
            (timedelta(days=400), "raw_table_monthly_agg", "1 month") # > 1 year -> Monthly
        ]
        
        for duration, expected_table, expected_interval in cases:
            table, interval = manager.get_optimal_query_source(
                "raw_table", 
                (now - duration, now), 
                "1m" # Requested resolution
            )
            print(f"Duration {duration.days} days -> {table} ({interval})")
            self.assertEqual(table, expected_table)
            self.assertEqual(interval, expected_interval)
            
        print("✅ Hierarchical query selection correct")

if __name__ == "__main__":
    unittest.main()
