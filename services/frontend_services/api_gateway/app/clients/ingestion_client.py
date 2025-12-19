
from typing import Dict, Any, List, Optional
import httpx
from app.core.logging import get_logger

logger = get_logger(__name__)

class IngestionServiceClient:
    def __init__(self, base_url: str, timeout: float = 30.0):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.AsyncClient(timeout=timeout)

    async def create_job(self, job: Dict[str, Any]) -> Dict[str, Any]:
        response = await self.client.post(f"{self.base_url}/jobs", json=job)
        response.raise_for_status()
        return response.json()

    async def run_job(self, job_id: str) -> Dict[str, Any]:
        response = await self.client.post(f"{self.base_url}/jobs/{job_id}/run")
        response.raise_for_status()
        return response.json()

    async def get_job_status(self, job_id: str) -> Dict[str, Any]:
        response = await self.client.get(f"{self.base_url}/jobs/{job_id}")
        response.raise_for_status()
        return response.json()

    async def preview_transformation(self, data: List[Dict[str, Any]], rules: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        payload = {"data": data, "rules": rules}
        response = await self.client.post(f"{self.base_url}/transform/preview", json=payload)
        response.raise_for_status()
        return response.json()

    async def close(self):
        await self.client.aclose()
