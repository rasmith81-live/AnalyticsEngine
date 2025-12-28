
from typing import Dict, Any, List, Optional
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from ...clients.conversation_client import ConversationServiceClient
from ...api.dependencies import get_conversation_client

router = APIRouter()

class ChatRequest(BaseModel):
    session_id: Optional[str] = None
    user_id: str
    message: str
    skip_response: bool = False

class BusinessIntent(BaseModel):
    name: str
    confidence: float
    parameters: Dict[str, Any] = {}
    description: Optional[str] = None
    domain: str = "general"
    target_entities: List[str] = []
    requested_metrics: List[str] = []

class RecommendStrategyRequest(BaseModel):
    business_description: str
    use_cases: List[str]

@router.post("/sessions")
async def create_session(
    user_id: str,
    client: ConversationServiceClient = Depends(get_conversation_client)
):
    """Create a new interview session."""
    return await client.create_session(user_id)

@router.get("/sessions/{session_id}")
async def get_session(
    session_id: str,
    client: ConversationServiceClient = Depends(get_conversation_client)
):
    """Get session details."""
    return await client.get_session(session_id)

@router.post("/sessions/{session_id}/model")
async def generate_model(
    session_id: str,
    client: ConversationServiceClient = Depends(get_conversation_client)
):
    """Generate value chain model from session conversation."""
    return await client.generate_model(session_id)

@router.post("/chat")
async def chat(
    request: ChatRequest,
    client: ConversationServiceClient = Depends(get_conversation_client)
):
    """Send a chat message and get response with extracted intents."""
    return await client.chat(request.session_id, request.user_id, request.message, request.skip_response)

@router.post("/match-intent")
async def match_intent(
    intent: BusinessIntent,
    client: ConversationServiceClient = Depends(get_conversation_client)
):
    """Match business intent to ontology patterns."""
    return await client.match_intent(intent.model_dump())

@router.post("/recommend-strategy")
async def recommend_strategy(
    request: RecommendStrategyRequest,
    client: ConversationServiceClient = Depends(get_conversation_client)
):
    """Get value chain recommendations based on business description."""
    return await client.recommend_strategy(request.business_description, request.use_cases)
