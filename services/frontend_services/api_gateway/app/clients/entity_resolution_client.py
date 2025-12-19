
from typing import Dict, Any, List, Optional
import httpx
from app.core.logging import get_logger

logger = get_logger(__name__)

class EntityResolutionServiceClient:
    def __init__(self, base_url: str, timeout: float = 60.0):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.AsyncClient(timeout=timeout)

    async def run_matching_job(self, source_records: List[Dict[str, Any]], threshold: float = 0.85) -> Dict[str, Any]:
        payload = {"source_records": source_records, "threshold": threshold}
        response = await self.client.post(f"{self.base_url}/matching/run", json=payload)
        response.raise_for_status()
        return response.json()

    async def create_golden_record(self, match_candidate_ids: List[str], strategy: str = "frequency_based") -> Dict[str, Any]:
        payload = {"match_candidate_ids": match_candidate_ids, "strategy": strategy}
        response = await self.client.post(f"{self.base_url}/merging/create-golden-record", json=payload)
        response.raise_for_status()
        return response.json()

    async def trigger_retroactive_fix(self, entity_id: str) -> Dict[str, Any]:
        response = await self.client.post(f"{self.base_url}/retroactive/fix", params={"entity_id": entity_id})
        response.raise_for_status()
        return response.json()

    async def close(self):
        await self.client.aclose()
