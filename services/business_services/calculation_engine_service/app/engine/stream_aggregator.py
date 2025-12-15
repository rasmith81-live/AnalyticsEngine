
import logging
import json
from typing import Dict, Any, List, Optional, Union
from datetime import datetime
import redis.asyncio as redis
from pydantic import BaseModel

logger = logging.getLogger(__name__)

class TimeSeriesSample(BaseModel):
    timestamp: float  # Unix timestamp in milliseconds
    value: float
    labels: Dict[str, str]

class StreamAggregator:
    """
    In-Memory Stream Aggregator using Redis TimeSeries.
    Handles high-velocity metrics ingestion and aggregation before persistence.
    """

    def __init__(self, redis_url: str, retention_ms: int = 3600000): # Default 1 hour retention
        self.redis_url = redis_url
        self.retention_ms = retention_ms
        self.client: Optional[redis.Redis] = None

    async def connect(self):
        """Connect to Redis."""
        if not self.client:
            self.client = redis.from_url(self.redis_url, decode_responses=True)
            try:
                # Check for TimeSeries module
                await self.client.execute_command("TS.INFO", "test_key")
            except redis.ResponseError as e:
                if "unknown command" in str(e).lower():
                    logger.warning("Redis TimeSeries module not available. Fallback or limited functionality.")
                else:
                    # Key doesn't exist is expected
                    pass
            except Exception as e:
                logger.warning(f"Redis connection warning: {e}")

    async def close(self):
        """Close Redis connection."""
        if self.client:
            await self.client.close()
            self.client = None

    def _get_key(self, metric_name: str, dimensions: Dict[str, str]) -> str:
        """Generate Redis key for the time series."""
        # Sort dimensions for consistent key generation
        dim_str = ",".join(f"{k}={v}" for k, v in sorted(dimensions.items()))
        return f"ts:{metric_name}{{{dim_str}}}"

    async def add_sample(self, metric_name: str, value: float, dimensions: Dict[str, str] = None):
        """
        Add a sample to the time series.
        Creates the series if it doesn't exist.
        """
        if not self.client:
            await self.connect()
            
        dimensions = dimensions or {}
        key = self._get_key(metric_name, dimensions)
        timestamp = int(datetime.utcnow().timestamp() * 1000)

        try:
            # TS.ADD key timestamp value [RETENTION retentionTime] [LABELS label value..]
            # Use ON_DUPLICATE='LAST' (overwrite) or 'SUM' depending on semantics. Defaulting to LAST.
            
            # Prepare labels list
            labels = []
            for k, v in dimensions.items():
                labels.extend([k, v])
            labels.extend(["metric", metric_name])

            await self.client.execute_command(
                "TS.ADD", key, timestamp, value, 
                "RETENTION", self.retention_ms, 
                "LABELS", *labels,
                "ON_DUPLICATE", "LAST" 
            )
        except Exception as e:
            logger.error(f"Failed to add sample to Redis TS {key}: {e}")
            raise

    async def get_range(self, metric_name: str, start_ts: int, end_ts: int, 
                       aggregation: str = None, bucket_size_ms: int = None,
                       dimensions: Dict[str, str] = None) -> List[Dict[str, Any]]:
        """
        Query a range of data.
        """
        if not self.client:
            await self.connect()

        dimensions = dimensions or {}
        key = self._get_key(metric_name, dimensions)

        try:
            # TS.RANGE key fromTimestamp toTimestamp [AGGREGATION aggregatorType bucketDuration]
            args = ["TS.RANGE", key, start_ts, end_ts]
            if aggregation and bucket_size_ms:
                args.extend(["AGGREGATION", aggregation, bucket_size_ms])
            
            response = await self.client.execute_command(*args)
            # Response is list of [timestamp, value]
            return [{"timestamp": item[0], "value": float(item[1])} for item in response]
        except Exception as e:
            logger.error(f"Failed to get range from Redis TS {key}: {e}")
            return []

    async def get_last_value(self, metric_name: str, dimensions: Dict[str, str] = None) -> Optional[Dict[str, Any]]:
        """Get the last value."""
        if not self.client:
            await self.connect()

        dimensions = dimensions or {}
        key = self._get_key(metric_name, dimensions)

        try:
            response = await self.client.execute_command("TS.GET", key)
            if response:
                return {"timestamp": response[0], "value": float(response[1])}
            return None
        except Exception as e:
            # Key might not exist
            return None

    async def create_rule(self, source_metric: str, dest_metric: str, 
                         aggregation: str, bucket_size_ms: int,
                         dimensions: Dict[str, str] = None):
        """Create a compaction rule (Continuous Aggregate in Redis)."""
        if not self.client:
            await self.connect()
            
        dimensions = dimensions or {}
        source_key = self._get_key(source_metric, dimensions)
        dest_key = self._get_key(dest_metric, dimensions) # Usually purely aggregated, but reusing dim logic for now

        try:
            # Ensure dest key exists
            try:
                await self.client.execute_command("TS.CREATE", dest_key, "RETENTION", self.retention_ms * 24) # Keep aggs longer
            except Exception:
                pass # Exists

            await self.client.execute_command("TS.CREATERULE", source_key, dest_key, "AGGREGATION", aggregation, bucket_size_ms)
        except Exception as e:
            logger.error(f"Failed to create Redis TS rule: {e}")

