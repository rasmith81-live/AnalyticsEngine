
import unittest
import asyncio
from datetime import datetime, timedelta
from unittest.mock import MagicMock, AsyncMock, patch
import sys
import os

# Add service dir to path
service_dir = os.path.dirname(os.path.abspath(__file__))
if service_dir not in sys.path:
    sys.path.insert(0, service_dir)

from app.engine.stream_aggregator import StreamAggregator
from app.engine.timescale_manager import TimescaleManager
from app.engine.unified_query_manager import UnifiedQueryManager
from app.engine.storage_sync import StorageSyncManager

class TestStreamIntegration(unittest.TestCase):
    
    def setUp(self):
        # Mocks
        self.mock_redis = MagicMock()
        self.mock_redis.execute_command = AsyncMock()
        
        self.aggregator = StreamAggregator(redis_url="redis://localhost")
        self.aggregator.client = self.mock_redis
        
        self.timescale_manager = TimescaleManager()
        self.timescale_manager.get_optimal_query_source = MagicMock(return_value=("readings_hourly", "1 hour"))

    def test_unified_query_manager(self):
        """Test UnifiedQueryManager merges real-time and historical data."""
        print("\nTesting UnifiedQueryManager...")
        
        # Setup
        unified_manager = UnifiedQueryManager(self.timescale_manager, self.aggregator)
        
        # Mock historical data (usually from DB)
        # We patch _fetch_historical since it's a placeholder in the implementation
        unified_manager._fetch_historical = AsyncMock(return_value=[
            {"timestamp": 1000, "value": 10},
            {"timestamp": 2000, "value": 20}
        ])
        
        # Mock real-time data (from Redis)
        self.aggregator.get_range = AsyncMock(return_value=[
            {"timestamp": 3000, "value": 30},
            {"timestamp": 4000, "value": 40}
        ])
        
        # Execute
        now = datetime.utcnow()
        start = now - timedelta(hours=2)
        end = now
        
        result = asyncio.run(unified_manager.get_unified_data(
            "kpi_1", "ent_1", start, end, "1h"
        ))
        
        # Verify
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0]['value'], 10)
        self.assertEqual(result[3]['value'], 40)
        print("✅ Merged Real-time and Historical data correctly")

    def test_storage_sync_manager(self):
        """Test StorageSyncManager write-behind logic."""
        print("\nTesting StorageSyncManager (Write-Behind)...")
        
        # Setup
        sync_manager = StorageSyncManager(
            self.aggregator, 
            "http://db-service", 
            sync_interval_seconds=1
        )
        sync_manager._http_client = AsyncMock()
        sync_manager._http_client.post.return_value = MagicMock(status_code=200)
        
        # Mock Redis data return for sync
        self.aggregator.get_range = AsyncMock(return_value=[
            {"timestamp": 5000, "value": 50}
        ])
        
        # Register stream
        asyncio.run(sync_manager.register_stream("kpi_1", "ent_1"))
        
        # Manually trigger sync (instead of waiting for loop)
        asyncio.run(sync_manager.sync_all())
        
        # Verify
        # Should have called get_range on aggregator
        self.aggregator.get_range.assert_called_once()
        
        # Should have posted to DB service
        sync_manager._http_client.post.assert_called_once()
        call_args = sync_manager._http_client.post.call_args
        self.assertIn("/telemetry/ingest-batch", call_args[0][0])
        self.assertEqual(call_args[1]['json']['metric_name'], "kpi_1")
        
        print("✅ Write-Behind Sync triggered correctly")

    def test_cqrs_pattern(self):
        """Verify components exist to support CQRS."""
        print("\nVerifying CQRS Components...")
        
        from app.stream_processor import StreamProcessor
        processor = StreamProcessor(MagicMock(), "url", "url", "url")
        
        # Check for Write Side (StreamAggregator + Sync)
        self.assertIsInstance(processor.aggregator, StreamAggregator)
        self.assertIsInstance(processor.sync_manager, StorageSyncManager)
        
        # Check for Read Side (UnifiedQueryManager exists in module)
        self.assertIsNotNone(UnifiedQueryManager)
        
        print("✅ CQRS Components (StreamProcessor, Aggregator, SyncManager, UnifiedQueryManager) present")

if __name__ == "__main__":
    unittest.main()
