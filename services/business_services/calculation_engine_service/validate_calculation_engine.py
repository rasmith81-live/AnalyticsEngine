import sys
import os
import unittest
import ast
from datetime import datetime, timedelta
from typing import Dict, Any, List

# Add the service directory to sys.path
service_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if service_dir not in sys.path:
    sys.path.insert(0, service_dir)

# Import the code to test
from app.engine.parser import FormulaParser
from app.engine.sql_generator import SQLGenerator
from app.engine.timescale_manager import TimescaleManager
from app.stream_processor import StreamProcessor
from app.orchestrator import CalculationOrchestrator

# Mock httpx and redis for StreamProcessor
from unittest.mock import AsyncMock, MagicMock
sys.modules["httpx"] = MagicMock()
sys.modules["redis.asyncio"] = MagicMock()

class TestCalculationEngine(unittest.TestCase):
    
    # --- Stream Processor Tests ---
    
    def test_stream_processor_init(self):
        """Test StreamProcessor initialization."""
        print("\nTesting Stream Processor Init...")
        orchestrator = MagicMock(spec=CalculationOrchestrator)
        processor = StreamProcessor(
            orchestrator=orchestrator,
            database_service_url="http://db",
            messaging_service_url="http://msg",
            redis_url="redis://localhost"
        )
        self.assertIsNotNone(processor.subscriber_id)
        print("✅ StreamProcessor initialized")

    async def async_test_stream_subscription(self):
        """Async test for stream subscription."""
        print("\nTesting Stream Subscription...")
        orchestrator = MagicMock(spec=CalculationOrchestrator)
        
        # Mock httpx client
        mock_client = AsyncMock()
        mock_response = MagicMock()
        mock_response.json.return_value = {"channel": "test_channel"}
        mock_client.post.return_value = mock_response
        
        processor = StreamProcessor(
            orchestrator=orchestrator,
            database_service_url="http://db",
            messaging_service_url="http://msg",
            redis_url="redis://localhost"
        )
        processor._http_client = mock_client
        
        # Mock message consumer starter to avoid background tasks in test
        processor._start_message_consumer = AsyncMock()
        
        sub = await processor.subscribe_to_stream(
            kpi_code="KPI_1",
            entity_id="ENT_1",
            period="1m"
        )
        
        self.assertEqual(sub["channel"], "test_channel")
        self.assertIn("KPI_1:ENT_1:1m", processor._active_subscriptions)
        print("✅ Stream subscription successful")

    def test_stream_subscription(self):
        """Wrapper to run async test."""
        import asyncio
        asyncio.run(self.async_test_stream_subscription())

    # --- Stream Aggregator Tests ---

    async def async_test_stream_aggregator_add(self):
        """Test adding samples to StreamAggregator."""
        print("\nTesting Stream Aggregator Add...")
        from app.engine.stream_aggregator import StreamAggregator
        
        # Mock Redis client
        mock_redis = MagicMock()
        mock_redis.execute_command = AsyncMock()
        
        aggregator = StreamAggregator(redis_url="redis://localhost")
        aggregator.client = mock_redis
        
        await aggregator.add_sample(
            metric_name="temperature",
            value=25.5,
            dimensions={"sensor_id": "s1", "location": "room1"}
        )
        
        # Verify TS.ADD command
        args = mock_redis.execute_command.call_args[0]
        self.assertEqual(args[0], "TS.ADD")
        # Check key generation (sorted dimensions)
        self.assertIn("ts:temperature{location=room1,sensor_id=s1}", args[1])
        self.assertEqual(args[3], 25.5) # Value check
        print("✅ StreamAggregator TS.ADD correct")

    def test_stream_aggregator(self):
        """Wrapper for StreamAggregator async tests."""
        import asyncio
        asyncio.run(self.async_test_stream_aggregator_add())

    # --- Dynamic Calculation Engine Tests ---
    
    def test_formula_parser(self):
        """Test parsing KPI formulas."""
        print("\nTesting Formula Parser...")
        parser = FormulaParser()
        
        formula = "(Revenue - Cost) / Revenue"
        result = parser.parse(formula)
        
        self.assertIn("Revenue", result["variables"])
        self.assertIn("Cost", result["variables"])
        self.assertIsInstance(result["ast"], ast.Expression)
        print("✅ Formula parsed successfully")

    def test_sql_generator_basic(self):
        """Test SQL generation for basic formulas."""
        print("\nTesting SQL Generator (Basic)...")
        parser = FormulaParser()
        generator = SQLGenerator()
        
        formula = "Revenue - Cost"
        parsed = parser.parse(formula)
        
        sql = generator.generate_query(parsed, table_name="financials", bucket_interval="1 day")
        print(f"   Generated SQL: {sql}")
        
        self.assertIn("bucket", sql)
        self.assertIn("(Revenue - Cost)", sql)
        self.assertIn("FROM financials", sql)
        self.assertIn("GROUP BY bucket", sql)
        print("✅ Basic SQL generated correctly")

    def test_sql_generator_aggregation(self):
        """Test SQL generation with aggregation functions."""
        print("\nTesting SQL Generator (Aggregation)...")
        parser = FormulaParser()
        generator = SQLGenerator()
        
        formula = "sum(Revenue) / count(Orders)"
        parsed = parser.parse(formula)
        
        sql = generator.generate_query(parsed, table_name="sales_data")
        print(f"   Generated SQL: {sql}")
        
        self.assertIn("SUM(Revenue)", sql)
        self.assertIn("COUNT(Orders)", sql)
        self.assertIn("/", sql)
        print("✅ Aggregation SQL generated correctly")

    def test_sql_generator_approximate(self):
        """Test SQL generation with approximate functions."""
        print("\nTesting SQL Generator (Approximate)...")
        parser = FormulaParser()
        generator = SQLGenerator()
        
        formula = "count_distinct(UserId)"
        parsed = parser.parse(formula)
        
        # approximate=True
        sql = generator.generate_query(parsed, table_name="events", approximate=True)
        print(f"   Generated SQL: {sql}")
        
        self.assertIn("distinct_count(hyperloglog(UserId))", sql)
        print("✅ Approximate SQL generated correctly")

    def test_sql_generator_last(self):
        """Test SQL generation with LAST function (TimescaleDB specific)."""
        print("\nTesting SQL Generator (LAST)...")
        parser = FormulaParser()
        generator = SQLGenerator()
        
        formula = "last(price, time)"
        parsed = parser.parse(formula)
        
        sql = generator.generate_query(parsed, table_name="stock_prices")
        print(f"   Generated SQL: {sql}")
        
        self.assertIn("LAST(price, time)", sql)
        print("✅ LAST function SQL generated correctly")

    # --- TimescaleDB Integration Tests ---

    def test_query_router(self):
        """Test QueryRouter logic for selecting optimal table."""
        print("\nTesting Query Router...")
        manager = TimescaleManager()
        
        now = datetime.utcnow()
        
        # Case 1: Short range -> Raw table
        source, interval = manager.get_optimal_query_source(
            "readings", 
            (now - timedelta(days=1), now), 
            "1m"
        )
        self.assertEqual(source, "readings")
        
        # Case 2: > 1 week -> Hourly agg
        source, interval = manager.get_optimal_query_source(
            "readings", 
            (now - timedelta(days=10), now), 
            "1h"
        )
        self.assertEqual(source, "readings_hourly_agg")
        self.assertEqual(interval, "1 hour")
        
        # Case 3: > 1 month -> Daily agg
        source, interval = manager.get_optimal_query_source(
            "readings", 
            (now - timedelta(days=40), now), 
            "1d"
        )
        self.assertEqual(source, "readings_daily_agg")
        self.assertEqual(interval, "1 day")

        print("✅ Query routing logic correct")

    def test_continuous_aggregate_ddl(self):
        """Test generation of Continuous Aggregate DDL."""
        print("\nTesting Continuous Aggregate DDL...")
        manager = TimescaleManager()
        
        ddl = manager.generate_continuous_aggregate_query(
            view_name="readings_hourly",
            source_table="readings",
            time_bucket="1 hour",
            aggregates=[
                {"func": "AVG", "column": "temp", "alias": "avg_temp"},
                {"func": "MAX", "column": "temp", "alias": "max_temp"}
            ],
            group_by=["sensor_id"]
        )
        print(f"   Generated DDL: {ddl}")
        
        self.assertIn("CREATE MATERIALIZED VIEW readings_hourly", ddl)
        self.assertIn("timescaledb.continuous", ddl)
        self.assertIn("time_bucket('1 hour', time)", ddl)
        self.assertIn("AVG(temp) AS avg_temp", ddl)
        self.assertIn("GROUP BY bucket, sensor_id", ddl)
        print("✅ Continuous Aggregate DDL correct")

    def test_refresh_policy_ddl(self):
        """Test generation of Refresh Policy DDL."""
        print("\nTesting Refresh Policy DDL...")
        manager = TimescaleManager()
        
        ddl = manager.generate_refresh_policy_query(
            view_name="readings_hourly",
            start_offset="3 days",
            end_offset="1 hour",
            schedule_interval="1 hour"
        )
        
        self.assertIn("add_continuous_aggregate_policy", ddl)
        self.assertIn("'readings_hourly'", ddl)
        self.assertIn("INTERVAL '3 days'", ddl)
        print("✅ Refresh Policy DDL correct")

    def test_retention_policy_ddl(self):
        """Test generation of Retention Policy DDL."""
        print("\nTesting Retention Policy DDL...")
        manager = TimescaleManager()
        
        ddl = manager.generate_retention_policy_query(
            table_name="readings",
            drop_after="1 year"
        )
        
        self.assertIn("add_retention_policy", ddl)
        self.assertIn("'readings'", ddl)
        self.assertIn("INTERVAL '1 year'", ddl)
        print("✅ Retention Policy DDL correct")

if __name__ == "__main__":
    unittest.main()
