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
import httpx

import os

from .agents.redis_agent_client import RedisAgentClient, get_redis_agent_client
from .agents.config import get_agent_settings

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/agents", tags=["Multi-Agent Design"])

# Multi-Agent Service URL for proxying requests (use env var from docker-compose)
MULTI_AGENT_SERVICE_URL = os.getenv("MULTI_AGENT_SERVICE_URL", "http://multi_agent_service:8000")


# =============================================================================
# Request/Response Models
# =============================================================================

class AgentInfo(BaseModel):
    """Information about an available agent."""
    role: str
    description: str
    layer: str
    capabilities: List[str] = Field(default_factory=list)


class AgentListResponse(BaseModel):
    """Response containing list of available agents."""
    agents: List[AgentInfo]
    total: int


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

def get_multi_agent_client() -> RedisAgentClient:
    """Dependency to get the Redis-based multi-agent client."""
    return get_redis_agent_client()


# =============================================================================
# REST Endpoints
# =============================================================================

@router.get("", response_model=AgentListResponse)
async def list_agents():
    """
    List all available agents in the multi-agent system.
    
    Returns the 27 specialized agents organized by layer:
    - Strategy Layer (8 agents)
    - Technical Layer (8 agents)
    - Business Layer (8 agents)
    - Governance Layer (3 agents)
    """
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{MULTI_AGENT_SERVICE_URL}/agents/list")
            
            if response.status_code == 200:
                data = response.json()
                # Transform response to AgentListResponse format
                agents = []
                if isinstance(data, list):
                    for agent in data:
                        agents.append(AgentInfo(
                            role=agent.get("role", agent.get("name", "unknown")),
                            description=agent.get("description", ""),
                            layer=agent.get("layer", "unknown"),
                            capabilities=agent.get("capabilities", [])
                        ))
                elif isinstance(data, dict) and "agents" in data:
                    for agent in data["agents"]:
                        agents.append(AgentInfo(
                            role=agent.get("role", agent.get("name", "unknown")),
                            description=agent.get("description", ""),
                            layer=agent.get("layer", "unknown"),
                            capabilities=agent.get("capabilities", [])
                        ))
                
                return AgentListResponse(agents=agents, total=len(agents))
            else:
                logger.warning(f"Multi-agent service returned {response.status_code}")
                raise HTTPException(status_code=response.status_code, detail="Failed to fetch agents")
    except httpx.RequestError as e:
        logger.error(f"Failed to connect to multi-agent service: {e}")
        raise HTTPException(status_code=503, detail="Multi-agent service unavailable")
    except Exception as e:
        logger.error(f"Failed to list agents: {e}")
        raise HTTPException(status_code=500, detail=str(e))


class MCPServerInfo(BaseModel):
    """Information about an MCP server."""
    name: str
    description: str
    status: str
    tools_count: int


class MCPServersResponse(BaseModel):
    """Response containing list of MCP servers."""
    servers: List[MCPServerInfo]
    total: int


@router.get("/mcp/servers", response_model=MCPServersResponse)
async def list_mcp_servers():
    """
    List all configured MCP servers.
    
    Returns the 3 MCP servers:
    - PostgreSQL MCP Server (database introspection)
    - Knowledge Graph MCP Server (ontology management)
    - Exa Web Search (external research)
    """
    from .mcp import MCPClientManager, MCPConfig
    
    try:
        config = MCPConfig.from_env()
        manager = MCPClientManager(config)
        await manager.initialize()
        
        servers = []
        
        # PostgreSQL MCP
        if config.postgres_mcp_enabled:
            pg_client = manager.get_client("postgres")
            servers.append(MCPServerInfo(
                name="postgres",
                description="PostgreSQL MCP Server - database introspection and schema analysis",
                status="connected" if pg_client else "disabled",
                tools_count=len([t for t in manager.list_all_tools() if t.startswith("postgres_")])
            ))
        
        # Knowledge Graph MCP
        if config.knowledge_mcp_enabled:
            kg_client = manager.get_client("knowledge")
            servers.append(MCPServerInfo(
                name="knowledge_graph",
                description="Knowledge Graph MCP Server - ontology management and entity relations",
                status="connected" if kg_client else "disabled",
                tools_count=len([t for t in manager.list_all_tools() if t.startswith("knowledge_")])
            ))
        
        # Exa Web Search
        if config.web_search_enabled:
            ws_client = manager.get_client("web_search")
            servers.append(MCPServerInfo(
                name="web_search",
                description="Exa Web Search - external research and company information",
                status="connected" if ws_client else "disabled",
                tools_count=len([t for t in manager.list_all_tools() if t.startswith("web_search_")])
            ))
        
        await manager.close()
        
        return MCPServersResponse(servers=servers, total=len(servers))
    except Exception as e:
        logger.error(f"Failed to list MCP servers: {e}")
        # Return configured servers even if initialization fails
        return MCPServersResponse(
            servers=[
                MCPServerInfo(name="postgres", description="PostgreSQL MCP Server", status="configured", tools_count=0),
                MCPServerInfo(name="knowledge_graph", description="Knowledge Graph MCP Server", status="configured", tools_count=0),
                MCPServerInfo(name="web_search", description="Exa Web Search", status="configured", tools_count=0),
            ],
            total=3
        )


@router.post("/design-session", response_model=CreateSessionResponse)
async def create_design_session(
    request: CreateSessionRequest,
    client: RedisAgentClient = Depends(get_multi_agent_client)
):
    """
    Create a new multi-agent design session.
    
    This starts a new session where the Strategy Coordinator (Claude Opus 4.5)
    will lead an interview to design a business value chain model.
    """
    try:
        session = await client.create_session(
            user_id=request.user_id,
            context={
                "business_description": request.business_description,
                "industry": request.industry
            }
        )
        
        # Generate initial greeting
        initial_message = "Hello! I'm your Strategy Coordinator. I'll be helping you design a comprehensive business value chain model."
        
        if request.business_description:
            initial_message += f"\n\nI see you've described your business as: {request.business_description[:200]}..."
            initial_message += "\n\nLet me analyze this and ask some clarifying questions."
        else:
            initial_message += "\n\nTo get started, could you tell me about your business? What industry are you in, and what are your main products or services?"
        
        return CreateSessionResponse(
            session_id=session.get("id", session.get("session_id", "unknown")),
            user_id=request.user_id,
            status=session.get("status", "active"),
            message=initial_message
        )
        
    except Exception as e:
        logger.error(f"Failed to create design session: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sessions/{session_id}", response_model=Dict[str, Any])
async def get_session(
    session_id: str,
    client: RedisAgentClient = Depends(get_multi_agent_client)
):
    """Get details of a design session."""
    try:
        session = await client.get_session(session_id)
        if not session:
            raise HTTPException(status_code=404, detail=f"Session {session_id} not found")
        return session
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get session: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/sessions/{session_id}/message", response_model=SendMessageResponse)
async def send_message(
    session_id: str,
    request: SendMessageRequest,
    client: RedisAgentClient = Depends(get_multi_agent_client)
):
    """
    Send a message to a design session.
    
    The Strategy Coordinator will process the message, potentially
    delegating to sub-agents, and return a response.
    """
    try:
        response = await client.send_message(session_id, request.message)
        
        return SendMessageResponse(
            session_id=session_id,
            agent_role=response.get("agent_role", "coordinator"),
            content=response.get("content", ""),
            artifacts=response.get("artifacts", {}),
            success=response.get("success", True),
            error=response.get("error")
        )
        
    except Exception as e:
        logger.error(f"Failed to process message: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/sessions/{session_id}/analyze", response_model=ParallelAnalysisResponse)
async def run_parallel_analysis(
    session_id: str,
    request: ParallelAnalysisRequest,
    client: RedisAgentClient = Depends(get_multi_agent_client)
):
    """
    Run parallel analysis with multiple sub-agents.
    
    This triggers the Architect, Business Analyst, and Developer agents
    to work in parallel on the current session context.
    """
    try:
        results = await client.run_parallel_analysis(
            session_id, 
            request.analysis_type
        )
        
        return ParallelAnalysisResponse(
            session_id=session_id,
            results=results
        )
        
    except Exception as e:
        logger.error(f"Failed to run parallel analysis: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sessions/{session_id}/artifacts", response_model=SessionArtifactsResponse)
async def get_session_artifacts_endpoint(
    session_id: str,
    client: RedisAgentClient = Depends(get_multi_agent_client)
):
    """Get all artifacts generated in a session."""
    try:
        result = await client.get_session_artifacts(session_id)
        
        if isinstance(result, dict) and "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        
        return SessionArtifactsResponse(
            session_id=session_id,
            artifacts=result if isinstance(result, dict) else {},
            entities=result.get("entities", []) if isinstance(result, dict) else [],
            kpis=result.get("kpis", []) if isinstance(result, dict) else []
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get artifacts: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/sessions/{session_id}/finalize", response_model=FinalizeSessionResponse)
async def finalize_session(
    session_id: str,
    client: RedisAgentClient = Depends(get_multi_agent_client)
):
    """
    Finalize a design session.
    
    This runs validation, generates documentation, and prepares
    all artifacts for persistence to the Business Metadata Service.
    """
    try:
        result = await client.finalize_session(session_id)
        
        if not result.get("success"):
            raise HTTPException(status_code=500, detail=result.get("error", "Finalization failed"))
        
        return FinalizeSessionResponse(
            success=result.get("success", True),
            session_id=session_id,
            status=result.get("status", "finalized"),
            value_chain=result.get("value_chain", {}),
            artifacts=result.get("artifacts", {}),
            validation=result.get("validation", {})
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to finalize session: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/sessions/{session_id}")
async def cancel_session(
    session_id: str,
    client: RedisAgentClient = Depends(get_multi_agent_client)
):
    """Cancel a design session."""
    try:
        result = await client.cancel_session(session_id)
        return {"success": True, "session_id": session_id, "status": "cancelled"}
    except Exception as e:
        logger.error(f"Failed to cancel session: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sessions", response_model=SessionListResponse)
async def list_sessions(
    user_id: Optional[str] = None,
    client: RedisAgentClient = Depends(get_multi_agent_client)
):
    """List all design sessions, optionally filtered by user."""
    try:
        sessions = await client.list_sessions(user_id)
        return SessionListResponse(sessions=sessions if isinstance(sessions, list) else [])
    except Exception as e:
        logger.error(f"Failed to list sessions: {e}")
        return SessionListResponse(sessions=[])


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
        # Get client
        client = MultiAgentServiceClient()
        
        # Send connection confirmation
        await websocket.send_json({
            "type": "connected",
            "session_id": session_id,
            "status": "active"
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
                # Stream response from coordinator via client
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
                
                # Send message via client (non-streaming for now)
                try:
                    response = await client.send_message(session_id, content)
                    
                    await websocket.send_json({
                        "type": "chunk",
                        "content": response.get("content", "")
                    })
                    
                    # Send completion
                    await websocket.send_json({
                        "type": "complete",
                        "content": response.get("content", "")
                    })
                except Exception as e:
                    await websocket.send_json({
                        "type": "error",
                        "message": str(e)
                    })
                
            elif message_type == "analyze":
                # Run parallel analysis
                analysis_type = message_data.get("analysis_type", "comprehensive")
                
                await websocket.send_json({
                    "type": "analyzing",
                    "message": f"Running {analysis_type} analysis with multiple agents..."
                })
                
                try:
                    results = await client.run_parallel_analysis(
                        session_id, 
                        analysis_type
                    )
                    
                    await websocket.send_json({
                        "type": "analysis_complete",
                        "results": results
                    })
                except Exception as e:
                    await websocket.send_json({
                        "type": "error",
                        "message": str(e)
                    })
                
            elif message_type == "finalize":
                # Finalize session
                await websocket.send_json({
                    "type": "finalizing",
                    "message": "Finalizing design session..."
                })
                
                try:
                    result = await client.finalize_session(session_id)
                    
                    await websocket.send_json({
                        "type": "finalized",
                        "result": result
                    })
                except Exception as e:
                    await websocket.send_json({
                        "type": "error",
                        "message": str(e)
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


# =============================================================================
# Phase 16: Blackboard Access Endpoints
# =============================================================================

class BlackboardTaskResponse(BaseModel):
    """Response containing blackboard tasks."""
    session_id: str
    tasks: List[Dict[str, Any]]
    total: int


class BlackboardArtifactResponse(BaseModel):
    """Response containing blackboard artifacts."""
    session_id: str
    artifacts: List[Dict[str, Any]]
    total: int


class ContractStatusResponse(BaseModel):
    """Response containing contract status for agents."""
    session_id: str
    agents: List[Dict[str, Any]]
    degraded_mode: bool
    degraded_reason: Optional[str] = None


class AgentStateResponse(BaseModel):
    """Response containing agent state machine status."""
    session_id: str
    agent_role: str
    current_state: str
    assumption_count: int
    failed_attempts: int
    last_transition: Optional[str] = None
    contract_violations: int


@router.get("/{session_id}/blackboard/tasks", response_model=BlackboardTaskResponse)
async def get_session_tasks(
    session_id: str,
    client: RedisAgentClient = Depends(get_multi_agent_client)
):
    """
    Get all tasks on the blackboard for a session.
    
    Returns tasks with their status, assignee, and completion criteria.
    """
    from .agents.config import get_agent_settings, should_use_blackboard
    
    settings = get_agent_settings()
    
    if not should_use_blackboard(session_id):
        return BlackboardTaskResponse(
            session_id=session_id,
            tasks=[],
            total=0
        )
    
    try:
        tasks = await client.get_session_tasks(session_id)
        
        return BlackboardTaskResponse(
            session_id=session_id,
            tasks=[t.model_dump() if hasattr(t, 'model_dump') else t for t in tasks],
            total=len(tasks)
        )
    except Exception as e:
        logger.warning(f"Failed to fetch blackboard tasks: {e}")
        return BlackboardTaskResponse(
            session_id=session_id,
            tasks=[],
            total=0
        )


@router.get("/{session_id}/blackboard/artifacts", response_model=BlackboardArtifactResponse)
async def get_blackboard_artifacts(
    session_id: str,
    client: RedisAgentClient = Depends(get_multi_agent_client)
):
    """
    Get all artifacts submitted for a session.
    
    Returns artifacts with their type, creator, and review status.
    """
    from .agents.config import should_use_blackboard
    
    if not should_use_blackboard(session_id):
        return BlackboardArtifactResponse(session_id=session_id, artifacts=[], total=0)
    
    try:
        artifacts = await client.get_session_artifacts(session_id)
        
        return BlackboardArtifactResponse(
            session_id=session_id,
            artifacts=[a.model_dump() if hasattr(a, 'model_dump') else a for a in artifacts],
            total=len(artifacts)
        )
    except Exception as e:
        logger.warning(f"Failed to fetch blackboard artifacts: {e}")
        return BlackboardArtifactResponse(session_id=session_id, artifacts=[], total=0)


@router.get("/{session_id}/contract-status", response_model=ContractStatusResponse)
async def get_contract_status(
    session_id: str,
    client: RedisAgentClient = Depends(get_multi_agent_client)
):
    """
    Get contract compliance status for all agents in session.
    
    Returns current state, violation count, and degraded mode status.
    """
    from .agents.config import get_agent_settings, should_use_blackboard
    
    settings = get_agent_settings()
    
    if not should_use_blackboard(session_id):
        return ContractStatusResponse(
            session_id=session_id,
            agents=[],
            degraded_mode=not settings.MULTI_AGENT_SERVICE_ENABLED,
            degraded_reason="Blackboard not enabled for this session"
        )
    
    try:
        status = await client.get_contract_status(session_id)
        
        return ContractStatusResponse(
            session_id=session_id,
            agents=status.get("agents", []),
            degraded_mode=status.get("degraded_mode", False),
            degraded_reason=status.get("degraded_reason")
        )
    except Exception as e:
        logger.warning(f"Failed to fetch contract status: {e}")
        return ContractStatusResponse(
            session_id=session_id,
            agents=[],
            degraded_mode=True,
            degraded_reason=f"multi_agent_service unavailable: {str(e)}"
        )


@router.get("/{session_id}/agent/{agent_role}/state", response_model=AgentStateResponse)
async def get_agent_state(
    session_id: str,
    agent_role: str,
    client: RedisAgentClient = Depends(get_multi_agent_client)
):
    """
    Get current state machine state for an agent.
    
    Returns the agent's current state, transition history, and metrics.
    """
    from .agents.config import should_use_blackboard
    
    if not should_use_blackboard(session_id):
        return AgentStateResponse(
            session_id=session_id,
            agent_role=agent_role,
            current_state="unknown",
            assumption_count=0,
            failed_attempts=0,
            contract_violations=0
        )
    
    try:
        state = await client.get_agent_state(session_id, agent_role)
        
        return AgentStateResponse(
            session_id=session_id,
            agent_role=agent_role,
            current_state=state.get("current_state", "idle"),
            assumption_count=state.get("assumption_count", 0),
            failed_attempts=state.get("failed_attempts", 0),
            last_transition=state.get("last_transition"),
            contract_violations=state.get("contract_violations", 0)
        )
    except Exception as e:
        logger.warning(f"Failed to fetch agent state: {e}")
        return AgentStateResponse(
            session_id=session_id,
            agent_role=agent_role,
            current_state="unknown",
            assumption_count=0,
            failed_attempts=0,
            contract_violations=0
        )
