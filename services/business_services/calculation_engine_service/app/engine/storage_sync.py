import asyncio
import logging
from typing import Dict, List, Optional
from datetime import datetime
import httpx
from .stream_aggregator import StreamAggregator

logger = logging.getLogger(__name__)

class StorageSyncManager:
    """
    Manages write-behind synchronization of Redis TimeSeries data to TimescaleDB via Database Service.
    """
    
    def __init__(
        self, 
        stream_aggregator: StreamAggregator, 
        database_service_url: str,
        sync_interval_seconds: int = 60
    ):
        self.aggregator = stream_aggregator
        self.database_service_url = database_service_url
        self.sync_interval = sync_interval_seconds
        self._running = False
        self._task: Optional[asyncio.Task] = None
        self._http_client: Optional[httpx.AsyncClient] = None
        
        # Track last synced timestamp for each metric stream
        # key: metric_key (kpi:entity), value: timestamp_ms
        self._sync_checkpoints: Dict[str, int] = {} 

    async def start(self):
        """Start the sync loop."""
        self._running = True
        self._http_client = httpx.AsyncClient()
        self._task = asyncio.create_task(self._sync_loop())
        logger.info("StorageSyncManager started")

    async def stop(self):
        """Stop the sync loop."""
        self._running = False
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
        if self._http_client:
            await self._http_client.aclose()
        logger.info("StorageSyncManager stopped")

    async def register_stream(self, metric_name: str, entity_id: str):
        """Register a stream to be tracked for syncing."""
        key = f"{metric_name}:{entity_id}"
        if key not in self._sync_checkpoints:
            # Start syncing from now
            self._sync_checkpoints[key] = int(datetime.utcnow().timestamp() * 1000)

    async def _sync_loop(self):
        """Periodic sync loop."""
        while self._running:
            try:
                await asyncio.sleep(self.sync_interval)
                await self.sync_all()
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in sync loop: {e}")

    async def sync_all(self):
        """Sync all registered streams."""
        for key, last_synced in list(self._sync_checkpoints.items()):
            try:
                metric_name, entity_id = key.split(":")
                await self._sync_stream(metric_name, entity_id, last_synced)
            except Exception as e:
                logger.error(f"Failed to sync stream {key}: {e}")

    async def _sync_stream(self, metric_name: str, entity_id: str, last_synced: int):
        """Sync a single stream."""
        now_ms = int(datetime.utcnow().timestamp() * 1000)
        
        # Fetch data from Redis since last sync
        # We add 1ms to start to avoid duplication if exclusive, 
        # but TS.RANGE includes start/end. 
        # Best practice: use (last_synced + 1)
        
        data = await self.aggregator.get_range(
            metric_name=metric_name,
            start_ts=last_synced + 1,
            end_ts=now_ms,
            dimensions={"entity_id": entity_id}
        )
        
        if not data:
            return

        # Prepare payload for Database Service
        # Assuming batch ingestion endpoint
        payload = {
            "metric_name": metric_name,
            "entity_id": entity_id,
            "data_points": data # List of {timestamp, value}
        }
        
        # Send to Database Service
        # In a real app, this might be better via Messaging/Event Bus to decouple
        # But for 'sync', a direct write or published event is fine. 
        # Using a hypothetical endpoint here.
        response = await self._http_client.post(
            f"{self.database_service_url}/telemetry/ingest-batch",
            json=payload
        )
        response.raise_for_status()
        
        # Update checkpoint
        # Use the timestamp of the last item synced
        last_item_ts = int(data[-1]['timestamp'])
        self._sync_checkpoints[f"{metric_name}:{entity_id}"] = last_item_ts
        
        logger.debug(f"Synced {len(data)} points for {metric_name}:{entity_id}")
