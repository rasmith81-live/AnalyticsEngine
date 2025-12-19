
from typing import Dict, Any
from fastapi import APIRouter, Depends
from ...clients.conversation_client import ConversationServiceClient
from ...api.dependencies import get_conversation_client

router = APIRouter()

@router.post("/utterance")
async def process_utterance(
    payload: Dict[str, Any],
    client: ConversationServiceClient = Depends(get_conversation_client)
):
    session_id = payload.get("session_id")
    utterance = payload.get("utterance")
    return await client.process_utterance(session_id, utterance)

@router.get("/session/{session_id}")
async def get_session(
    session_id: str,
    client: ConversationServiceClient = Depends(get_conversation_client)
):
    return await client.get_session(session_id)

@router.post("/session")
async def start_session(
    user_id: str,
    client: ConversationServiceClient = Depends(get_conversation_client)
):
    return await client.start_session(user_id)
