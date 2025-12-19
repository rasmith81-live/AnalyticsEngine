
from typing import Dict, Any, List, Optional
import httpx
from app.core.logging import get_logger

logger = get_logger(__name__)

class DemoConfigServiceClient:
    def __init__(self, base_url: str, timeout: float = 30.0):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.AsyncClient(timeout=timeout)

    async def get_client_configs(self) -> List[Dict[str, Any]]:
        response = await self.client.get(f"{self.base_url}/api/v1/clients")
        response.raise_for_status()
        return response.json()

    async def get_client_config(self, client_id: str) -> Dict[str, Any]:
        response = await self.client.get(f"{self.base_url}/api/v1/clients/{client_id}")
        response.raise_for_status()
        return response.json()

    async def create_client_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        response = await self.client.post(f"{self.base_url}/api/v1/clients", json=config)
        response.raise_for_status()
        return response.json()

    async def update_client_config(self, client_id: str, config: Dict[str, Any]) -> Dict[str, Any]:
        response = await self.client.put(f"{self.base_url}/api/v1/clients/{client_id}", json=config)
        response.raise_for_status()
        return response.json()

    async def get_custom_kpis(self, client_id: str) -> List[Dict[str, Any]]:
        response = await self.client.get(f"{self.base_url}/api/v1/clients/{client_id}/custom-kpis")
        response.raise_for_status()
        return response.json()

    async def create_custom_kpi(self, client_id: str, kpi: Dict[str, Any]) -> Dict[str, Any]:
        response = await self.client.post(f"{self.base_url}/api/v1/clients/{client_id}/custom-kpis", json=kpi)
        response.raise_for_status()
        return response.json()

    async def generate_proposal(self, client_id: str, options: Dict[str, Any]) -> Dict[str, Any]:
        response = await self.client.post(f"{self.base_url}/api/v1/clients/{client_id}/proposal", json=options)
        response.raise_for_status()
        return response.json()

    async def get_proposal(self, client_id: str) -> Dict[str, Any]:
        response = await self.client.get(f"{self.base_url}/api/v1/clients/{client_id}/proposal")
        response.raise_for_status()
        return response.json()

    async def update_proposal(self, client_id: str, proposal: Dict[str, Any]) -> Dict[str, Any]:
        response = await self.client.put(f"{self.base_url}/api/v1/clients/{client_id}/proposal", json=proposal)
        response.raise_for_status()
        return response.json()

    async def close(self):
        await self.client.aclose()
