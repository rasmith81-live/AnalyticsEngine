
from typing import Dict, List, Any, Optional
import httpx
from app.core.logging import get_logger

logger = get_logger(__name__)

class MetadataServiceClient:
    def __init__(self, base_url: str, timeout: float = 60.0):
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

    async def get_definitions(self, kind: str, limit: int = 100, offset: int = 0) -> List[Dict[str, Any]]:
        response = await self.client.get(
            f"{self.base_url}/api/v1/metadata/definitions/{kind}",
            params={"limit": limit, "offset": offset}
        )
        response.raise_for_status()
        return response.json()

    async def delete_definition(self, kind: str, code: str, deleted_by: str = "admin") -> None:
        response = await self.client.delete(
            f"{self.base_url}/api/v1/metadata/definitions/{kind}/{code}",
            params={"deleted_by": deleted_by}
        )
        response.raise_for_status()
        return {"status": "deleted", "code": code}

    async def update_definition(
        self, 
        kind: str, 
        code: str, 
        definition: Dict[str, Any],
        changed_by: str = "admin",
        change_description: Optional[str] = None
    ) -> None:
        """Update a definition."""
        params = {"changed_by": changed_by}
        if change_description:
            params["change_description"] = change_description
        
        response = await self.client.put(
            f"{self.base_url}/api/v1/metadata/definitions/{kind}/{code}",
            json=definition,
            params=params
        )
        response.raise_for_status()
        return {"status": "updated", "code": code}

    async def get_all_relationships(self, relationship_type: str = None) -> List[Dict[str, Any]]:
        """Get all relationships, optionally filtered by type."""
        # Query all entities and get their relationships
        # This is a simplified approach - in production you'd have a bulk endpoint
        params = {}
        if relationship_type:
            params["relationship_types"] = [relationship_type]
        
        # Get relationships for a known entity to test, or use a bulk endpoint
        response = await self.client.get(
            f"{self.base_url}/api/v1/metadata/relationships",
            params=params
        )
        response.raise_for_status()
        return response.json()

    async def get_entity_relationships(
        self, 
        entity_code: str, 
        direction: str = "both",
        relationship_type: str = None
    ) -> List[Dict[str, Any]]:
        """Get relationships for a specific entity."""
        params = {"direction": direction}
        if relationship_type:
            params["relationship_types"] = [relationship_type]
        
        response = await self.client.get(
            f"{self.base_url}/api/v1/metadata/definitions/metric_definition/{entity_code}/relationships",
            params=params
        )
        response.raise_for_status()
        return response.json()

    async def close(self):
        await self.client.aclose()
