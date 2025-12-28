
from typing import Dict, Any, List, Optional
import httpx
from app.core.logging import get_logger

logger = get_logger(__name__)

class ConversationServiceClient:
    def __init__(self, base_url: str, timeout: float = 120.0):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.AsyncClient(timeout=timeout)

    async def create_session(self, user_id: str) -> Dict[str, Any]:
        """Create a new interview session."""
        response = await self.client.post(
            f"{self.base_url}/api/v1/sessions",
            params={"user_id": user_id}
        )
        response.raise_for_status()
        return response.json()

    async def get_session(self, session_id: str) -> Dict[str, Any]:
        """Get session details."""
        response = await self.client.get(f"{self.base_url}/api/v1/sessions/{session_id}")
        response.raise_for_status()
        return response.json()

    async def chat(self, session_id: Optional[str], user_id: str, message: str, skip_response: bool = False) -> Dict[str, Any]:
        """Send a chat message and get response with intents."""
        payload = {
            "session_id": session_id,
            "user_id": user_id,
            "message": message,
            "skip_response": skip_response
        }
        response = await self.client.post(f"{self.base_url}/api/v1/chat", json=payload)
        response.raise_for_status()
        return response.json()

    async def generate_model(self, session_id: str) -> Dict[str, Any]:
        """Generate value chain model from session."""
        response = await self.client.post(f"{self.base_url}/api/v1/sessions/{session_id}/model")
        response.raise_for_status()
        return response.json()

    async def match_intent(self, intent: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Match business intent to ontology patterns."""
        response = await self.client.post(f"{self.base_url}/api/v1/match-intent", json=intent)
        response.raise_for_status()
        return response.json()

    async def recommend_strategy(self, business_description: str, use_cases: List[str]) -> List[Dict[str, Any]]:
        """Get value chain recommendations."""
        payload = {
            "business_description": business_description,
            "use_cases": use_cases
        }
        response = await self.client.post(f"{self.base_url}/api/v1/recommend-strategy", json=payload)
        response.raise_for_status()
        return response.json()

    async def close(self):
        await self.client.aclose()
