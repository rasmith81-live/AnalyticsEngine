
from typing import Dict, List, Any, Optional
import httpx
from app.core.logging import get_logger

logger = get_logger(__name__)

class MetadataServiceClient:
    def __init__(self, base_url: str, timeout: float = 30.0):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.AsyncClient(timeout=timeout)

    async def get_kpis(self) -> List[Dict[str, Any]]:
        response = await self.client.get(f"{self.base_url}/api/v1/kpis")
        response.raise_for_status()
        return response.json()

    async def get_kpi(self, code: str) -> Dict[str, Any]:
        response = await self.client.get(f"{self.base_url}/api/v1/kpis/{code}")
        response.raise_for_status()
        return response.json()

    async def get_kpis_by_module(self, module_code: str) -> List[Dict[str, Any]]:
        response = await self.client.get(f"{self.base_url}/api/v1/kpis/module/{module_code}")
        response.raise_for_status()
        return response.json()

    async def get_kpis_by_value_chain(self, vc_code: str) -> List[Dict[str, Any]]:
        response = await self.client.get(f"{self.base_url}/api/v1/kpis/value-chain/{vc_code}")
        response.raise_for_status()
        return response.json()

    async def get_object_models(self) -> List[Dict[str, Any]]:
        response = await self.client.get(f"{self.base_url}/api/v1/object-models")
        response.raise_for_status()
        return response.json()
        
    async def get_object_model(self, code: str) -> Dict[str, Any]:
        response = await self.client.get(f"{self.base_url}/api/v1/object-models/{code}")
        response.raise_for_status()
        return response.json()

    async def get_object_models_by_module(self, module_code: str) -> List[Dict[str, Any]]:
        response = await self.client.get(f"{self.base_url}/api/v1/object-models/module/{module_code}")
        response.raise_for_status()
        return response.json()

    async def get_modules(self) -> List[Dict[str, Any]]:
        response = await self.client.get(f"{self.base_url}/api/v1/modules")
        response.raise_for_status()
        return response.json()

    async def get_module(self, code: str) -> Dict[str, Any]:
        response = await self.client.get(f"{self.base_url}/api/v1/modules/{code}")
        response.raise_for_status()
        return response.json()

    async def get_modules_by_value_chain(self, vc_code: str) -> List[Dict[str, Any]]:
        response = await self.client.get(f"{self.base_url}/api/v1/modules/value-chain/{vc_code}")
        response.raise_for_status()
        return response.json()

    async def get_value_chains(self) -> List[str]:
        response = await self.client.get(f"{self.base_url}/api/v1/value-chains")
        response.raise_for_status()
        return response.json()

    async def get_value_chain(self, code: str) -> Dict[str, Any]:
        response = await self.client.get(f"{self.base_url}/api/v1/value-chains/{code}")
        response.raise_for_status()
        return response.json()

    async def get_industries(self) -> List[str]:
        response = await self.client.get(f"{self.base_url}/api/v1/industries")
        response.raise_for_status()
        return response.json()

    async def get_industry(self, code: str) -> Dict[str, Any]:
        response = await self.client.get(f"{self.base_url}/api/v1/industries/{code}")
        response.raise_for_status()
        return response.json()

    async def get_value_chains_by_industry(self, industry_code: str) -> List[Dict[str, Any]]:
        response = await self.client.get(f"{self.base_url}/api/v1/industries/{industry_code}/value-chains")
        response.raise_for_status()
        return response.json()

    async def close(self):
        await self.client.aclose()
