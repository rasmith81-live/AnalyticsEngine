
from typing import Dict, Any, List, Optional
import httpx
from app.core.logging import get_logger

logger = get_logger(__name__)

class MetadataIngestionServiceClient:
    def __init__(self, base_url: str, timeout: float = 60.0):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.AsyncClient(timeout=timeout)

    async def list_industries(self) -> List[Dict[str, Any]]:
        response = await self.client.get(f"{self.base_url}/knowledge/industries")
        response.raise_for_status()
        return response.json()

    async def get_industry_value_chain(self, code: str) -> Dict[str, Any]:
        response = await self.client.get(f"{self.base_url}/knowledge/industries/{code}/value-chain")
        response.raise_for_status()
        return response.json()

    async def get_industry_kpis(self, code: str) -> Dict[str, Any]:
        response = await self.client.get(f"{self.base_url}/knowledge/industries/{code}/kpis")
        response.raise_for_status()
        return response.json()

    async def decompose_kpi(self, formula: str) -> Dict[str, Any]:
        response = await self.client.post(f"{self.base_url}/mapping/decompose", json={"formula": formula})
        response.raise_for_status()
        return response.json()

    async def close(self):
        await self.client.aclose()
