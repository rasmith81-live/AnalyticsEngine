from typing import List, Dict, Any, Tuple, Optional
from datetime import datetime, timedelta
import asyncio
import logging
from .timescale_manager import TimescaleManager
from .stream_aggregator import StreamAggregator

logger = logging.getLogger(__name__)

class UnifiedQueryManager:
    """
    Merges real-time data from Redis TimeSeries with historical data from TimescaleDB.
    Provides a unified view of metrics across time.
    """
    
    def __init__(self, timescale_manager: TimescaleManager, stream_aggregator: StreamAggregator):
        self.timescale_manager = timescale_manager
        self.stream_aggregator = stream_aggregator
        # Threshold to switch between Real-time and Historical
        # Data newer than this is fetched from Redis
        self.realtime_window = timedelta(hours=1)

    async def get_unified_data(
        self, 
        metric_name: str, 
        entity_id: str,
        start_date: datetime, 
        end_date: datetime, 
        interval: str,
        aggregation: str = "AVG"
    ) -> List[Dict[str, Any]]:
        """
        Get unified metric data merging real-time and historical sources.
        
        Args:
            metric_name: KPI/Metric code
            entity_id: Entity ID
            start_date: Start of query range
            end_date: End of query range
            interval: Time bucket interval (e.g. '1h', '1d')
            aggregation: Aggregation function (AVG, SUM, MAX, MIN, COUNT)
            
        Returns:
            List of data points sorted by time
        """
        now = datetime.utcnow()
        cutoff_time = now - self.realtime_window
        
        tasks = []
        
        # 1. Determine ranges
        historical_end = min(end_date, cutoff_time)
        realtime_start = max(start_date, cutoff_time)
        
        # 2. Fetch Historical Data (if range overlaps)
        if start_date < cutoff_time:
            tasks.append(self._fetch_historical(
                metric_name, entity_id, start_date, historical_end, interval, aggregation
            ))
        else:
            tasks.append(asyncio.sleep(0, result=[])) # No historical needed

        # 3. Fetch Real-time Data (if range overlaps)
        if end_date > cutoff_time:
            tasks.append(self._fetch_realtime(
                metric_name, entity_id, realtime_start, end_date, interval, aggregation
            ))
        else:
            tasks.append(asyncio.sleep(0, result=[])) # No realtime needed
            
        # 4. Execute in parallel
        results = await asyncio.gather(*tasks)
        historical_data, realtime_data = results
        
        # 5. Merge and Sort
        # Prefer real-time data if timestamps overlap (though we tried to separate them)
        combined = historical_data + realtime_data
        combined.sort(key=lambda x: x['timestamp'])
        
        return combined

    async def _fetch_historical(
        self, 
        metric_name: str, 
        entity_id: str,
        start: datetime, 
        end: datetime, 
        interval: str,
        aggregation: str
    ) -> List[Dict[str, Any]]:
        """
        Fetch from TimescaleDB (Mock implementation assuming direct DB access or Service call).
        In a real scenario, this would generate SQL using TimescaleManager and execute it.
        """
        # Get optimal source (Raw vs Aggregate)
        table_source, time_bucket = self.timescale_manager.get_optimal_query_source(
            metric_name, (start, end), interval
        )
        
        # NOTE: In a microservice, we might call the Database Service here.
        # For this component's logic, we return a structure mimicking DB rows.
        # This is a placeholder for the actual DB call.
        return [] 

    async def _fetch_realtime(
        self, 
        metric_name: str, 
        entity_id: str,
        start: datetime, 
        end: datetime, 
        interval: str,
        aggregation: str
    ) -> List[Dict[str, Any]]:
        """
        Fetch from Redis StreamAggregator.
        """
        # Convert interval to ms for Redis
        bucket_ms = self._parse_interval_to_ms(interval)
        
        start_ts = int(start.timestamp() * 1000)
        end_ts = int(end.timestamp() * 1000)
        
        data = await self.stream_aggregator.get_range(
            metric_name=metric_name,
            start_ts=start_ts,
            end_ts=end_ts,
            aggregation=aggregation.lower(),
            bucket_size_ms=bucket_ms,
            dimensions={"entity_id": entity_id}
        )
        
        # Convert timestamps back to ISO/datetime if needed, or keep as consistent format
        # Here we return compatible dicts
        return data

    def _parse_interval_to_ms(self, interval: str) -> int:
        """Helper to parse '1h', '1m' to milliseconds."""
        unit = interval[-1].lower()
        val = int(interval[:-1])
        if unit == 's': return val * 1000
        if unit == 'm': return val * 60 * 1000
        if unit == 'h': return val * 3600 * 1000
        if unit == 'd': return val * 86400 * 1000
        return 0
