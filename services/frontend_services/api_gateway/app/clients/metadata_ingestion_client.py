
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

    async def upload_excel(self, file) -> Dict[str, Any]:
        # Read file content to avoid stream exhaustion issues
        content = await file.read()
        await file.seek(0)  # Reset for potential re-reads
        
        files = {"file": (file.filename, content, file.content_type)}
        response = await self.client.post(f"{self.base_url}/import/upload", files=files)
        response.raise_for_status()
        return response.json()

    async def enrich_import(self, import_id: str) -> Dict[str, Any]:
        """Call AI enrichment endpoint with extended timeout."""
        response = await self.client.post(
            f"{self.base_url}/import/{import_id}/enrich",
            timeout=300.0  # 5 minutes for LLM processing
        )
        response.raise_for_status()
        return response.json()

    async def commit_import(self, import_id: str, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        logger.info(f"commit_import called with body: {body is not None}, keys: {list(body.keys()) if body else 'None'}")
        response = await self.client.post(
            f"{self.base_url}/import/{import_id}/commit",
            json=body
        )
        response.raise_for_status()
        return response.json()

    async def close(self):
        await self.client.aclose()
