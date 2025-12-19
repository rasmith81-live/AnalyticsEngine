
from typing import Dict, Any, List, Optional
import httpx
from app.core.logging import get_logger

logger = get_logger(__name__)

class ConversationServiceClient:
    def __init__(self, base_url: str, timeout: float = 30.0):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.AsyncClient(timeout=timeout)

    async def process_utterance(self, session_id: str, utterance: str) -> Dict[str, Any]:
        payload = {"session_id": session_id, "utterance": utterance}
        response = await self.client.post(f"{self.base_url}/conversation/utterance", json=payload)
        response.raise_for_status()
        return response.json()

    async def get_session(self, session_id: str) -> Dict[str, Any]:
        response = await self.client.get(f"{self.base_url}/conversation/session/{session_id}")
        response.raise_for_status()
        return response.json()

    async def start_session(self, user_id: str) -> Dict[str, Any]:
        response = await self.client.post(f"{self.base_url}/conversation/session", params={"user_id": user_id})
        response.raise_for_status()
        return response.json()

    async def close(self):
        await self.client.aclose()
