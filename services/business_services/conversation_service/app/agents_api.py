"""
Multi-Agent API Endpoints

REST and WebSocket endpoints for the multi-agent design system.
Integrates with the Conversation Service to provide AI-powered
business value chain design capabilities.
"""

from __future__ import annotations

import asyncio
import json
import logging
from datetime import datetime
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, HTTPException, WebSocket, WebSocketDisconnect, Depends
from pydantic import BaseModel, Field

from .agents.orchestrator import (
    AgentOrchestrator,
    OrchestratorConfig,
    DesignSession,
    get_orchestrator
)
from .agents.base_agent import AgentResponse

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/agents", tags=["Multi-Agent Design"])


# =============================================================================
# Request/Response Models
# =============================================================================

class CreateSessionRequest(BaseModel):
    """Request to create a new design session."""
    user_id: str
    business_description: Optional[str] = None
    industry: Optional[str] = None


class CreateSessionResponse(BaseModel):
    """Response from creating a design session."""
    session_id: str
    user_id: str
    status: str
    message: str


class SendMessageRequest(BaseModel):
    """Request to send a message to a design session."""
    message: str


class SendMessageResponse(BaseModel):
    """Response from sending a message."""
    session_id: str
    agent_role: str
    content: str
    artifacts: Dict[str, Any] = Field(default_factory=dict)
    success: bool
    error: Optional[str] = None


class ParallelAnalysisRequest(BaseModel):
    """Request for parallel analysis."""
    analysis_type: str = "comprehensive"  # comprehensive, validation


class ParallelAnalysisResponse(BaseModel):
    """Response from parallel analysis."""
    session_id: str
    results: Dict[str, Any]


class FinalizeSessionResponse(BaseModel):
    """Response from finalizing a session."""
    success: bool
    session_id: str
    status: str
    value_chain: Dict[str, Any]
    artifacts: Dict[str, Any]
    validation: Dict[str, Any]


class SessionArtifactsResponse(BaseModel):
    """Response containing session artifacts."""
    session_id: str
    artifacts: Dict[str, Any]
    entities: List[str]
    kpis: List[str]


class SessionListResponse(BaseModel):
    """Response containing list of sessions."""
    sessions: List[Dict[str, Any]]


# =============================================================================
# Dependency Injection
# =============================================================================

async def get_agent_orchestrator() -> AgentOrchestrator:
    """Dependency to get the agent orchestrator."""
    config = OrchestratorConfig()
    return await get_orchestrator(config)


# =============================================================================
# REST Endpoints
# =============================================================================

@router.post("/design-session", response_model=CreateSessionResponse)
async def create_design_session(
    request: CreateSessionRequest,
    orchestrator: AgentOrchestrator = Depends(get_agent_orchestrator)
):
    """
    Create a new multi-agent design session.
    
    This starts a new session where the Strategy Coordinator (Claude Opus 4.5)
    will lead an interview to design a business value chain model.
    """
    try:
        session = await orchestrator.create_session(
            user_id=request.user_id,
            business_description=request.business_description,
            industry=request.industry
        )
        
        # Generate initial greeting
        initial_message = "Hello! I'm your Strategy Coordinator. I'll be helping you design a comprehensive business value chain model."
        
        if request.business_description:
            initial_message += f"\n\nI see you've described your business as: {request.business_description[:200]}..."
            initial_message += "\n\nLet me analyze this and ask some clarifying questions."
        else:
            initial_message += "\n\nTo get started, could you tell me about your business? What industry are you in, and what are your main products or services?"
        
        return CreateSessionResponse(
            session_id=session.id,
            user_id=session.user_id,
            status=session.status,
            message=initial_message
        )
        
    except Exception as e:
        logger.error(f"Failed to create design session: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sessions/{session_id}", response_model=Dict[str, Any])
async def get_session(
    session_id: str,
    orchestrator: AgentOrchestrator = Depends(get_agent_orchestrator)
):
    """Get details of a design session."""
    session = orchestrator.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail=f"Session {session_id} not found")
    
    return {
        "session_id": session.id,
        "user_id": session.user_id,
        "status": session.status,
        "created_at": session.created_at.isoformat(),
        "updated_at": session.updated_at.isoformat(),
        "message_count": session.message_count,
        "artifacts_generated": session.artifacts_generated,
        "context": {
            "industry": session.context.industry,
            "value_chain_type": session.context.value_chain_type,
            "identified_entities": session.context.identified_entities,
            "identified_kpis": session.context.identified_kpis
        }
    }


@router.post("/sessions/{session_id}/message", response_model=SendMessageResponse)
async def send_message(
    session_id: str,
    request: SendMessageRequest,
    orchestrator: AgentOrchestrator = Depends(get_agent_orchestrator)
):
    """
    Send a message to a design session.
    
    The Strategy Coordinator will process the message, potentially
    delegating to sub-agents, and return a response.
    """
    session = orchestrator.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail=f"Session {session_id} not found")
    
    try:
        response = await orchestrator.process_message(session_id, request.message)
        
        return SendMessageResponse(
            session_id=session_id,
            agent_role=response.agent_role.value if hasattr(response.agent_role, 'value') else str(response.agent_role),
            content=response.content,
            artifacts=response.artifacts,
            success=response.success,
            error=response.error
        )
        
    except Exception as e:
        logger.error(f"Failed to process message: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/sessions/{session_id}/analyze", response_model=ParallelAnalysisResponse)
async def run_parallel_analysis(
    session_id: str,
    request: ParallelAnalysisRequest,
    orchestrator: AgentOrchestrator = Depends(get_agent_orchestrator)
):
    """
    Run parallel analysis with multiple sub-agents.
    
    This triggers the Architect, Business Analyst, and Developer agents
    to work in parallel on the current session context.
    """
    session = orchestrator.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail=f"Session {session_id} not found")
    
    try:
        results = await orchestrator.run_parallel_analysis(
            session_id, 
            request.analysis_type
        )
        
        # Convert AgentResponse objects to dicts
        serialized_results = {}
        for agent_name, response in results.items():
            if isinstance(response, AgentResponse):
                serialized_results[agent_name] = {
                    "agent_role": str(response.agent_role),
                    "content": response.content,
                    "artifacts": response.artifacts,
                    "success": response.success,
                    "error": response.error
                }
            else:
                serialized_results[agent_name] = response
        
        return ParallelAnalysisResponse(
            session_id=session_id,
            results=serialized_results
        )
        
    except Exception as e:
        logger.error(f"Failed to run parallel analysis: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sessions/{session_id}/artifacts", response_model=SessionArtifactsResponse)
async def get_session_artifacts(
    session_id: str,
    orchestrator: AgentOrchestrator = Depends(get_agent_orchestrator)
):
    """Get all artifacts generated in a session."""
    try:
        result = await orchestrator.get_session_artifacts(session_id)
        
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        
        return SessionArtifactsResponse(
            session_id=result["session_id"],
            artifacts=result["artifacts"],
            entities=result["entities"],
            kpis=result["kpis"]
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get artifacts: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/sessions/{session_id}/finalize", response_model=FinalizeSessionResponse)
async def finalize_session(
    session_id: str,
    orchestrator: AgentOrchestrator = Depends(get_agent_orchestrator)
):
    """
    Finalize a design session.
    
    This runs validation, generates documentation, and prepares
    all artifacts for persistence to the Business Metadata Service.
    """
    session = orchestrator.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail=f"Session {session_id} not found")
    
    try:
        result = await orchestrator.finalize_session(session_id)
        
        if not result.get("success"):
            raise HTTPException(status_code=500, detail=result.get("error", "Finalization failed"))
        
        return FinalizeSessionResponse(
            success=result["success"],
            session_id=result["session_id"],
            status=result["status"],
            value_chain=result["value_chain"],
            artifacts=result["artifacts"],
            validation=result["validation"]
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to finalize session: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/sessions/{session_id}")
async def cancel_session(
    session_id: str,
    orchestrator: AgentOrchestrator = Depends(get_agent_orchestrator)
):
    """Cancel a design session."""
    success = await orchestrator.cancel_session(session_id)
    
    if not success:
        raise HTTPException(status_code=404, detail=f"Session {session_id} not found")
    
    return {"success": True, "session_id": session_id, "status": "cancelled"}


@router.get("/sessions", response_model=SessionListResponse)
async def list_sessions(
    user_id: Optional[str] = None,
    orchestrator: AgentOrchestrator = Depends(get_agent_orchestrator)
):
    """List all design sessions, optionally filtered by user."""
    sessions = orchestrator.list_sessions(user_id)
    
    return SessionListResponse(
        sessions=[
            {
                "session_id": s.id,
                "user_id": s.user_id,
                "status": s.status,
                "created_at": s.created_at.isoformat(),
                "message_count": s.message_count
            }
            for s in sessions
        ]
    )


# =============================================================================
# WebSocket Helpers
# =============================================================================

async def _send_agent_activities_from_artifacts(
    websocket: WebSocket, 
    session_id: str, 
    artifacts: Dict[str, Any]
) -> None:
    """Extract and send agent activities from session artifacts."""
    timestamp = datetime.utcnow().isoformat()
    
    # Check for delegations
    if "delegations" in artifacts:
        for i, delegation in enumerate(artifacts["delegations"]):
            await websocket.send_json({
                "type": "agent_activity",
                "activity": {
                    "id": f"act_del_{session_id}_{i}",
                    "type": "delegation",
                    "source": "coordinator",
                    "target": delegation.get("agent") or delegation.get("target", "unknown"),
                    "details": delegation.get("task"),
                    "timestamp": timestamp
                }
            })
    
    # Check for peer consultations
    if "peer_consultations" in artifacts:
        for i, consultation in enumerate(artifacts["peer_consultations"]):
            await websocket.send_json({
                "type": "agent_activity",
                "activity": {
                    "id": f"act_peer_{session_id}_{i}",
                    "type": "peer_consultation",
                    "source": consultation.get("from", "unknown"),
                    "target": consultation.get("to", "unknown"),
                    "details": consultation.get("question"),
                    "timestamp": timestamp
                }
            })
    
    # Check for tool calls
    if "tool_calls" in artifacts:
        for i, tool in enumerate(artifacts["tool_calls"]):
            activity_type = "mcp_tool" if tool.get("is_mcp") else "tool_call"
            await websocket.send_json({
                "type": "agent_activity",
                "activity": {
                    "id": f"act_tool_{session_id}_{i}",
                    "type": activity_type,
                    "source": tool.get("agent", "unknown"),
                    "tool": tool.get("name"),
                    "details": tool.get("result"),
                    "timestamp": timestamp
                }
            })
    
    # Check for agents consulted (from synthesis)
    if "agents_consulted" in artifacts:
        for i, agent in enumerate(artifacts["agents_consulted"]):
            await websocket.send_json({
                "type": "agent_activity",
                "activity": {
                    "id": f"act_consult_{session_id}_{i}",
                    "type": "delegation",
                    "source": "coordinator",
                    "target": agent,
                    "timestamp": timestamp
                }
            })
    
    # Check for synthesis indicator
    if "synthesis" in artifacts or "key_insights" in artifacts:
        await websocket.send_json({
            "type": "agent_activity",
            "activity": {
                "id": f"act_synth_{session_id}",
                "type": "synthesis",
                "source": "coordinator",
                "details": "Synthesizing agent results",
                "timestamp": timestamp
            }
        })


# =============================================================================
# WebSocket Endpoint
# =============================================================================

@router.websocket("/ws/{session_id}")
async def websocket_design_session(
    websocket: WebSocket,
    session_id: str
):
    """
    WebSocket endpoint for real-time design sessions.
    
    Provides streaming responses from the Strategy Coordinator
    and real-time updates during parallel agent processing.
    """
    await websocket.accept()
    
    try:
        # Get orchestrator
        orchestrator = await get_orchestrator()
        
        # Verify session exists
        session = orchestrator.get_session(session_id)
        if not session:
            await websocket.send_json({
                "type": "error",
                "message": f"Session {session_id} not found"
            })
            await websocket.close()
            return
        
        # Send connection confirmation
        await websocket.send_json({
            "type": "connected",
            "session_id": session_id,
            "status": session.status
        })
        
        while True:
            # Receive message
            data = await websocket.receive_text()
            
            try:
                message_data = json.loads(data)
                message_type = message_data.get("type", "message")
                content = message_data.get("content", data)
            except json.JSONDecodeError:
                message_type = "message"
                content = data
            
            if message_type == "message":
                from .agents.base_agent import StreamEvent, StreamEventType
                
                # Stream response from coordinator
                await websocket.send_json({
                    "type": "processing",
                    "message": "Processing your message..."
                })
                
                # Send initial activity for user message
                await websocket.send_json({
                    "type": "agent_activity",
                    "activity": {
                        "id": f"act_{session_id}_{datetime.utcnow().timestamp()}",
                        "type": "delegation",
                        "source": "user",
                        "target": "coordinator",
                        "timestamp": datetime.utcnow().isoformat()
                    }
                })
                
                full_response = []
                activity_counter = 0
                async for event in orchestrator.stream_message(session_id, content):
                    if isinstance(event, StreamEvent):
                        if event.event_type == StreamEventType.TEXT:
                            # Text chunk - send as before
                            if event.content:
                                full_response.append(event.content)
                                await websocket.send_json({
                                    "type": "chunk",
                                    "content": event.content
                                })
                        elif event.event_type == StreamEventType.DELEGATION:
                            # Real-time delegation activity
                            activity_counter += 1
                            await websocket.send_json({
                                "type": "agent_activity",
                                "activity": {
                                    "id": f"act_del_{session_id}_{activity_counter}",
                                    "type": "delegation",
                                    "source": event.source or "coordinator",
                                    "target": event.target or "unknown",
                                    "details": event.details,
                                    "timestamp": event.timestamp.isoformat()
                                }
                            })
                        elif event.event_type == StreamEventType.PEER_CONSULTATION:
                            # Real-time peer consultation
                            activity_counter += 1
                            await websocket.send_json({
                                "type": "agent_activity",
                                "activity": {
                                    "id": f"act_peer_{session_id}_{activity_counter}",
                                    "type": "peer_consultation",
                                    "source": event.source or "unknown",
                                    "target": event.target or "unknown",
                                    "details": event.details,
                                    "timestamp": event.timestamp.isoformat()
                                }
                            })
                        elif event.event_type == StreamEventType.TOOL_CALL:
                            # Real-time tool call activity
                            activity_counter += 1
                            await websocket.send_json({
                                "type": "agent_activity",
                                "activity": {
                                    "id": f"act_tool_{session_id}_{activity_counter}",
                                    "type": "tool_call",
                                    "source": event.source or "unknown",
                                    "tool_name": event.tool_name,
                                    "details": event.details,
                                    "timestamp": event.timestamp.isoformat()
                                }
                            })
                    else:
                        # Legacy string handling (fallback)
                        full_response.append(str(event))
                        await websocket.send_json({
                            "type": "chunk",
                            "content": str(event)
                        })
                
                # Fetch artifacts after processing for design progress
                try:
                    artifacts_result = await orchestrator.get_session_artifacts(session_id)
                    if "artifacts" in artifacts_result:
                        artifacts = artifacts_result["artifacts"]
                        
                        # Send design progress if available
                        if "design_progress" in artifacts:
                            await websocket.send_json({
                                "type": "design_progress",
                                "progress": artifacts["design_progress"]
                            })
                except Exception as e:
                    logger.debug(f"Could not fetch artifacts for design progress: {e}")
                
                # Send completion
                await websocket.send_json({
                    "type": "complete",
                    "content": "".join(full_response)
                })
                
            elif message_type == "analyze":
                # Run parallel analysis
                analysis_type = message_data.get("analysis_type", "comprehensive")
                
                await websocket.send_json({
                    "type": "analyzing",
                    "message": f"Running {analysis_type} analysis with multiple agents..."
                })
                
                results = await orchestrator.run_parallel_analysis(
                    session_id, 
                    analysis_type
                )
                
                # Send results
                serialized = {}
                for agent, response in results.items():
                    if isinstance(response, AgentResponse):
                        serialized[agent] = {
                            "content": response.content,
                            "artifacts": response.artifacts,
                            "success": response.success
                        }
                    else:
                        serialized[agent] = response
                
                await websocket.send_json({
                    "type": "analysis_complete",
                    "results": serialized
                })
                
            elif message_type == "finalize":
                # Finalize session
                await websocket.send_json({
                    "type": "finalizing",
                    "message": "Finalizing design session..."
                })
                
                result = await orchestrator.finalize_session(session_id)
                
                await websocket.send_json({
                    "type": "finalized",
                    "result": result
                })
                
            elif message_type == "ping":
                await websocket.send_json({"type": "pong"})
                
    except WebSocketDisconnect:
        logger.info(f"WebSocket disconnected for session {session_id}")
    except Exception as e:
        logger.error(f"WebSocket error for session {session_id}: {e}")
        try:
            await websocket.send_json({
                "type": "error",
                "message": str(e)
            })
        except Exception:
            pass
        await websocket.close()
