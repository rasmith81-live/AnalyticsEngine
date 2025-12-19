
from typing import Dict, Any, List, Optional
import httpx
from app.core.logging import get_logger

logger = get_logger(__name__)

class ConnectorServiceClient:
    def __init__(self, base_url: str, timeout: float = 30.0):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.AsyncClient(timeout=timeout)

    async def create_connection(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        response = await self.client.post(f"{self.base_url}/connections", json=profile)
        response.raise_for_status()
        return response.json()

    async def get_connection(self, connection_id: str) -> Dict[str, Any]:
        response = await self.client.get(f"{self.base_url}/connections/{connection_id}")
        response.raise_for_status()
        return response.json()

    async def test_connection(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        response = await self.client.post(f"{self.base_url}/connections/test", json=profile)
        response.raise_for_status()
        return response.json()

    async def discover_schema(self, connection_id: str) -> List[Dict[str, Any]]:
        response = await self.client.post(f"{self.base_url}/discovery/schema", params={"connection_id": connection_id})
        response.raise_for_status()
        return response.json()
        
    async def preview_data(self, connection_id: str, table_name: str, limit: int = 5) -> List[Dict[str, Any]]:
        response = await self.client.post(
            f"{self.base_url}/discovery/preview", 
            params={"connection_id": connection_id, "table_name": table_name, "limit": limit}
        )
        response.raise_for_status()
        return response.json()

    async def close(self):
        await self.client.aclose()
