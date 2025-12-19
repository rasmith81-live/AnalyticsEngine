
from typing import Dict, Any, List, Optional
import httpx
from app.core.logging import get_logger

logger = get_logger(__name__)

class CalculationEngineClient:
    def __init__(self, base_url: str, timeout: float = 60.0):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.AsyncClient(timeout=timeout)

    async def calculate_kpi(self, params: Dict[str, Any]) -> Dict[str, Any]:
        response = await self.client.post(f"{self.base_url}/api/v1/calculate", json=params)
        response.raise_for_status()
        return response.json()

    async def calculate_batch(self, params: Dict[str, Any]) -> Dict[str, Any]:
        response = await self.client.post(f"{self.base_url}/api/v1/calculate/batch", json=params)
        response.raise_for_status()
        return response.json()

    async def calculate_dashboard(self, config: Dict[str, Any]) -> Dict[str, Any]:
        response = await self.client.post(f"{self.base_url}/api/v1/calculate/dashboard", json=config)
        response.raise_for_status()
        return response.json()
        
    async def schedule_batch_job(self, job_config: Dict[str, Any]) -> Dict[str, Any]:
        response = await self.client.post(f"{self.base_url}/api/v1/batch/schedule", json=job_config)
        response.raise_for_status()
        return response.json()

    async def close(self):
        await self.client.aclose()
