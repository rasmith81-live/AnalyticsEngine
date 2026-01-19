
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any, Optional
import json
import logging
import asyncio
from datetime import datetime

# Import standardized clients
import sys
from pathlib import Path

# Add backend services to path
backend_services_path = Path(__file__).parent.parent.parent.parent / "backend_services"
sys.path.insert(0, str(backend_services_path))

from database_service.app.messaging_client import MessagingClient

from contextlib import asynccontextmanager
from typing import Optional

from .config import settings
from .models import (
    ChatRequest, ChatResponse, Utterance, BusinessIntent, 
    InterviewSession, CompanyValueChainModel, ValueChainNode, ValueChainLink,
    SenderType, RecommendStrategyRequest
)
from .llm_client import llm_client, get_llm_client
from .engine.pattern_matcher import PatternMatcher, DesignSuggester
from .engine.strategic_recommender import StrategicRecommender, StrategyScore
from .database import init_db, close_db
from .client_config_api import router as client_config_router
from .agents_api import router as agents_router

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("conversation_service")

# Global instances
messaging_client: Optional[MessagingClient] = None
pattern_matcher = PatternMatcher()
design_suggester = DesignSuggester()
strategic_recommender = StrategicRecommender()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan."""
    global messaging_client
    
    # Initialize database
    try:
        await init_db()
        logger.info("Database initialized")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        # Continue without database - in-memory mode still works
    
    # Initialize messaging client
    try:
        messaging_client = MessagingClient(
            redis_url=settings.REDIS_URL,
            service_name="conversation_service"
        )
        await messaging_client.connect()
        logger.info("MessagingClient connected")
    except Exception as e:
        logger.error(f"Failed to initialize MessagingClient: {e}")
        raise RuntimeError("MessagingClient initialization failed - cannot start service") from e
    
    yield
    
    # Cleanup
    if messaging_client:
        await messaging_client.disconnect()
        logger.info("MessagingClient disconnected")
    
    await close_db()
    logger.info("Database connections closed")

app = FastAPI(
    title=settings.APP_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include client configuration API router
app.include_router(client_config_router, prefix=settings.API_V1_STR)

# Include multi-agent design API router
app.include_router(agents_router, prefix=settings.API_V1_STR)

# In-memory session stores
active_sessions: Dict[str, List[Dict[str, str]]] = {} # Stores chat history for LLM context
sessions_store: Dict[str, InterviewSession] = {} # Stores structured session metadata

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "conversation-service"}

@app.post(f"{settings.API_V1_STR}/sessions", response_model=InterviewSession)
async def create_session(user_id: str):
    """Create a new interview session."""
    session = InterviewSession(user_id=user_id)
    sessions_store[session.id] = session
    active_sessions[session.id] = [] # Initialize chat context
    
    logger.info(f"Created new session {session.id} for user {user_id}")
    return session

@app.get(f"{settings.API_V1_STR}/sessions/{{session_id}}", response_model=InterviewSession)
async def get_session(session_id: str):
    """Get interview session details."""
    if session_id not in sessions_store:
        raise HTTPException(status_code=404, detail="Session not found")
    return sessions_store[session_id]

@app.post(f"{settings.API_V1_STR}/sessions/{{session_id}}/model", response_model=CompanyValueChainModel)
async def generate_value_chain_model(session_id: str):
    """Generate and persist a Company Value Chain Model from the session context."""
    if session_id not in sessions_store:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session = sessions_store[session_id]
    context = active_sessions.get(session_id, [])
    
    if not context:
        raise HTTPException(status_code=400, detail="Session has no context to generate model from")

    try:
        # Use LLM to generate model structure from conversation history
        model = await llm_client.generate_value_chain(context)
        model.name = f"Value Chain - {session_id}"
        
        # In a real scenario, we would persist this to the Business Metadata Service
        # For now, we'll log it and return it
        logger.info(f"Generated value chain model for session {session_id}: {model}")
        
        # Publish event
        await messaging_client.publish_event(
            topic="business_metadata.events.value_chain_generated",
            event_type="value_chain_model_generated",
            payload={
                "session_id": session_id,
                "model": model.model_dump(),
                "user_id": session.user_id
            }
        )
        
        return model
    except Exception as e:
        logger.error(f"Failed to generate value chain model: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate model: {str(e)}")

@app.post(f"{settings.API_V1_STR}/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Process a chat message from the user.
    1. Update session context
    2. Extract Business Intents using LLM
    3. Generate Response
    4. Publish 'conversation.message_received' event
    """
    session_id = request.session_id
    
    # Auto-create session if not provided or doesn't exist (backward compatibility/ease of use)
    if not session_id or session_id not in sessions_store:
        # If user_id is provided, try to find active session or create new
        if not session_id:
             session_id = f"session_{request.user_id}" # Simple deterministic ID for demo
        
        if session_id not in sessions_store:
             session = InterviewSession(id=session_id, user_id=request.user_id)
             sessions_store[session_id] = session
             active_sessions[session_id] = []
    
    # Update context
    session_context = active_sessions[session_id]
    session = sessions_store[session_id]
    
    # Extract Intents
    try:
        intents = await llm_client.extract_intents(request.message, session_context)
        logger.info(f"Extracted intents for session {session_id}: {intents}")
        
        # Update session metadata with new intents
        session.intents_identified.extend(intents)
        session.last_activity = datetime.utcnow()
        
    except Exception as e:
        logger.error(f"Error extracting intents: {e}")
        intents = []

    # Generate Response (skip if requested for faster intent-only extraction)
    if request.skip_response:
        response_text = ""
    else:
        try:
            response_text = await llm_client.generate_response(request.message, session_context, intents)
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            response_text = "I encountered an error processing your request."

    # Update context with this turn
    session_context.append({"role": "user", "content": request.message})
    session_context.append({"role": "assistant", "content": response_text})
    
    # Publish Event
    await messaging_client.publish_event(
        topic="conversation.events",
        event_type="message_received",
        payload={
            "session_id": session_id,
            "user_id": request.user_id,
            "message": request.message,
            "intents": [intent.model_dump() for intent in intents],
            "response": response_text
        }
    )
    
    # Keep context manageable
    if len(session_context) > 20:
        active_sessions[session_id] = session_context[-20:]

    return ChatResponse(
        session_id=session_id,
        message=response_text,
        intents=intents
    )

@app.post(f"{settings.API_V1_STR}/match-intent")
async def match_intent(intent: BusinessIntent) -> List[Dict[str, Any]]:
    """Match a business intent to ontology patterns."""
    return pattern_matcher.match_intent(intent)

@app.post(f"{settings.API_V1_STR}/suggestions/{{pattern_id}}/apply")
async def apply_suggestion(pattern_id: str):
    """Apply a design suggestion based on a pattern."""
    suggestion = design_suggester.suggest_design(pattern_id)
    if not suggestion:
        raise HTTPException(status_code=404, detail="Pattern not found or no suggestion available")
    return suggestion

@app.post(f"{settings.API_V1_STR}/recommend-strategy", response_model=List[StrategyScore])
async def recommend_strategy(request: RecommendStrategyRequest):
    """Recommend value chains based on business description."""
    return await strategic_recommender.recommend_value_chains(request.business_description, request.use_cases)

# WebSocket Endpoint for Real-time Chat (Legacy - uses simple LLM client)
@app.websocket("/ws/chat/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    """
    Legacy WebSocket endpoint for simple chat.
    For multi-agent design sessions, use /ws/agents/{session_id} instead.
    """
    await websocket.accept()
    session_id = f"session_{user_id}"
    
    if session_id not in active_sessions:
        active_sessions[session_id] = []
        
    try:
        while True:
            data = await websocket.receive_text()
            # Process strictly as text for now, can expand to JSON
            
            # Context
            session_context = active_sessions[session_id]
            
            # Async processing using Claude (or fallback to OpenAI)
            client = get_llm_client()
            intents = await client.extract_intents(data, session_context)
            response_text = await client.generate_response(data, session_context, intents)
            
            # Update Context
            session_context.append({"role": "user", "content": data})
            session_context.append({"role": "assistant", "content": response_text})
            
            # Send back
            response_data = {
                "message": response_text,
                "intents": [intent.model_dump() for intent in intents],
                "provider": client.provider
            }
            await websocket.send_text(json.dumps(response_data))
            
    except WebSocketDisconnect:
        logger.info(f"User {user_id} disconnected")
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        await websocket.close()


# WebSocket Endpoint for Multi-Agent Design Sessions
@app.websocket("/ws/agents/{session_id}")
async def websocket_agents_endpoint(websocket: WebSocket, session_id: str):
    """
    WebSocket endpoint for multi-agent design sessions.
    Uses Claude Opus 4.5 coordinator with specialized Sonnet 4 sub-agents.
    """
    from .agents.orchestrator import get_orchestrator
    
    await websocket.accept()
    
    try:
        orchestrator = await get_orchestrator()
        
        # Check if session exists, create if not
        session = orchestrator._sessions.get(session_id)
        if not session:
            await websocket.send_text(json.dumps({
                "type": "error",
                "message": f"Session {session_id} not found. Create via POST /api/v1/agents/design-session first."
            }))
            await websocket.close()
            return
        
        await websocket.send_text(json.dumps({
            "type": "connected",
            "session_id": session_id,
            "message": "Connected to multi-agent design session"
        }))
        
        while True:
            data = await websocket.receive_text()
            
            try:
                message_data = json.loads(data)
                message = message_data.get("message", data)
            except json.JSONDecodeError:
                message = data
            
            # Stream response from multi-agent system
            await websocket.send_text(json.dumps({
                "type": "processing",
                "message": "Processing with multi-agent system..."
            }))
            
            full_response = []
            async for chunk in orchestrator.stream_message(session_id, message):
                full_response.append(chunk)
                await websocket.send_text(json.dumps({
                    "type": "chunk",
                    "content": chunk
                }))
            
            # Send completion with artifacts
            session = orchestrator._sessions.get(session_id)
            await websocket.send_text(json.dumps({
                "type": "complete",
                "content": "".join(full_response),
                "artifacts": list(session.context.artifacts.keys()) if session else [],
                "entities": session.context.identified_entities if session else [],
                "kpis": session.context.identified_kpis if session else []
            }))
            
    except WebSocketDisconnect:
        logger.info(f"Multi-agent session {session_id} disconnected")
    except Exception as e:
        logger.error(f"Multi-agent WebSocket error: {e}")
        try:
            await websocket.send_text(json.dumps({
                "type": "error",
                "message": str(e)
            }))
        except Exception:
            pass
        await websocket.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
