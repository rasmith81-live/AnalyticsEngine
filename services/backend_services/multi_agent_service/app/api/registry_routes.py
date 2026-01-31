# =============================================================================
# Agent Registry API Routes
# Phase 18: Microsoft Best Practices Integration
# Reference: https://developer.microsoft.com/blog/designing-multi-agent-intelligence
# =============================================================================
"""
Self-registration API for external agents.

Enables external agents to register themselves with the multi-agent system,
supporting dynamic discovery and integration.
"""

from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any
from datetime import datetime
import logging

from ..models.agent_version import (
    AgentVersionState,
    AgentVersion,
    get_agent_registry
)
from ..models.agent_dependencies import get_dependency_registry
from ..metrics import record_agent_registration

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/registry", tags=["registry"])


# =============================================================================
# Request/Response Models
# =============================================================================

class AgentRegistrationRequest(BaseModel):
    """Request to register an agent."""
    agent_id: str = Field(..., description="Unique identifier for the agent")
    name: str = Field(..., description="Human-readable name")
    capabilities: List[str] = Field(default_factory=list, description="List of capabilities")
    endpoint: Optional[str] = Field(None, description="Agent endpoint URL for remote agents")
    protocol: str = Field("internal", description="Communication protocol: internal, a2a, http")
    version: str = Field("1.0.0", description="Agent version")
    metadata: Dict[str, Any] = Field(default_factory=dict)
    
    # Dependency declarations
    knowledge_bases: List[str] = Field(default_factory=list)
    external_services: List[str] = Field(default_factory=list)
    upstream_agents: List[str] = Field(default_factory=list)


class AgentRegistrationResponse(BaseModel):
    """Response after registering an agent."""
    success: bool
    agent_id: str
    version: str
    state: str
    registered_at: str
    message: str


class AgentInfoResponse(BaseModel):
    """Response containing agent information."""
    agent_id: str
    name: str
    capabilities: List[str]
    endpoint: Optional[str]
    protocol: str
    version: str
    state: str
    metadata: Dict[str, Any]
    registered_at: str
    updated_at: str


class AgentListResponse(BaseModel):
    """Response containing list of agents."""
    agents: List[AgentInfoResponse]
    total: int


class VersionTransitionRequest(BaseModel):
    """Request to transition agent version state."""
    target_state: str = Field(..., description="Target state: testing, published, deprecated, archived")
    reason: str = Field("", description="Reason for transition")


# =============================================================================
# In-memory storage (replace with Redis/DB in production)
# =============================================================================

_registered_agents: Dict[str, Dict[str, Any]] = {}


# =============================================================================
# API Endpoints
# =============================================================================

@router.post("/agents", response_model=AgentRegistrationResponse)
async def register_agent(request: AgentRegistrationRequest):
    """
    Register a new agent with the system.
    
    Supports both self-registration (agent calls this) and
    registry-initiated registration (admin calls this).
    """
    try:
        agent_id = request.agent_id
        
        # Check if already registered
        if agent_id in _registered_agents:
            record_agent_registration("self", "duplicate")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Agent {agent_id} is already registered"
            )
        
        # Register with version registry
        registry = get_agent_registry()
        agent_version = registry.register_version(
            agent_role=agent_id,
            version=request.version,
            changelog=f"Initial registration: {request.name}",
            metadata={
                "name": request.name,
                "capabilities": request.capabilities,
                "endpoint": request.endpoint,
                "protocol": request.protocol,
            }
        )
        
        # Register dependencies
        dep_registry = get_dependency_registry()
        deps = dep_registry.register(agent_id)
        
        for kb in request.knowledge_bases:
            deps.add_dependency(kb, "knowledge_base")
        for svc in request.external_services:
            deps.add_dependency(svc, "external_service")
        for agent in request.upstream_agents:
            deps.add_dependency(agent, "upstream_agent")
        
        # Store agent info
        now = datetime.utcnow()
        _registered_agents[agent_id] = {
            "agent_id": agent_id,
            "name": request.name,
            "capabilities": request.capabilities,
            "endpoint": request.endpoint,
            "protocol": request.protocol,
            "version": request.version,
            "state": agent_version.state.value,
            "metadata": request.metadata,
            "registered_at": now.isoformat(),
            "updated_at": now.isoformat(),
        }
        
        record_agent_registration("self", "success")
        logger.info(f"Registered agent: {agent_id} (v{request.version})")
        
        return AgentRegistrationResponse(
            success=True,
            agent_id=agent_id,
            version=request.version,
            state=agent_version.state.value,
            registered_at=now.isoformat(),
            message=f"Agent {request.name} registered successfully"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        record_agent_registration("self", "error")
        logger.error(f"Failed to register agent: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.get("/agents", response_model=AgentListResponse)
async def list_agents(
    state: Optional[str] = None,
    capability: Optional[str] = None
):
    """
    List all registered agents.
    
    Optionally filter by state or capability.
    """
    agents = list(_registered_agents.values())
    
    # Filter by state
    if state:
        agents = [a for a in agents if a.get("state") == state]
    
    # Filter by capability
    if capability:
        agents = [
            a for a in agents 
            if capability in a.get("capabilities", [])
        ]
    
    return AgentListResponse(
        agents=[AgentInfoResponse(**a) for a in agents],
        total=len(agents)
    )


@router.get("/agents/{agent_id}", response_model=AgentInfoResponse)
async def get_agent_info(agent_id: str):
    """Get information about a specific agent."""
    if agent_id not in _registered_agents:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Agent {agent_id} not found"
        )
    
    return AgentInfoResponse(**_registered_agents[agent_id])


@router.delete("/agents/{agent_id}")
async def deregister_agent(agent_id: str):
    """Remove an agent from the registry."""
    if agent_id not in _registered_agents:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Agent {agent_id} not found"
        )
    
    del _registered_agents[agent_id]
    logger.info(f"Deregistered agent: {agent_id}")
    
    return {"success": True, "message": f"Agent {agent_id} deregistered"}


@router.post("/agents/{agent_id}/transition")
async def transition_agent_version(
    agent_id: str,
    request: VersionTransitionRequest
):
    """
    Transition an agent's version state.
    
    Valid transitions:
    - draft → testing
    - testing → published
    - testing → draft (failed)
    - published → deprecated
    - deprecated → archived
    - deprecated → published (rollback)
    """
    if agent_id not in _registered_agents:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Agent {agent_id} not found"
        )
    
    try:
        target_state = AgentVersionState(request.target_state)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid state: {request.target_state}. "
                   f"Valid states: {[s.value for s in AgentVersionState]}"
        )
    
    registry = get_agent_registry()
    agent_info = _registered_agents[agent_id]
    version = agent_info["version"]
    
    agent_version = registry.get_version(agent_id, version)
    if not agent_version:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Version {version} not found for agent {agent_id}"
        )
    
    try:
        agent_version.transition_to(target_state)
        _registered_agents[agent_id]["state"] = target_state.value
        _registered_agents[agent_id]["updated_at"] = datetime.utcnow().isoformat()
        
        return {
            "success": True,
            "agent_id": agent_id,
            "version": version,
            "previous_state": agent_info["state"],
            "new_state": target_state.value,
            "message": f"Transitioned to {target_state.value}"
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/agents/{agent_id}/dependencies")
async def get_agent_dependencies(agent_id: str):
    """Get dependency information for an agent."""
    dep_registry = get_dependency_registry()
    deps = dep_registry.get(agent_id)
    
    if not deps:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No dependencies registered for agent {agent_id}"
        )
    
    return deps.get_impact_report()


@router.post("/agents/{agent_id}/dependencies/check")
async def check_agent_dependencies(
    agent_id: str,
    current_states: Dict[str, Any]
):
    """
    Check an agent's dependencies for changes.
    
    Provide current states of resources to detect changes.
    """
    dep_registry = get_dependency_registry()
    deps = dep_registry.get(agent_id)
    
    if not deps:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No dependencies registered for agent {agent_id}"
        )
    
    changes = deps.check_all_dependencies(current_states)
    
    return {
        "agent_id": agent_id,
        "changes_detected": len(changes),
        "changes": [c.to_dict() for c in changes],
        "last_verified": deps.last_verified.isoformat() if deps.last_verified else None
    }


@router.get("/agents/search/fuzzy")
async def fuzzy_search_agents(
    query: str,
    limit: int = 5
):
    """
    Phase 19: Fuzzy search for agents by capability keywords.
    
    Supports partial matches, typos, and multi-word queries.
    """
    try:
        from difflib import SequenceMatcher
        
        query_lower = query.lower()
        query_terms = query_lower.split()
        
        results = []
        
        for agent_id, agent_info in _registered_agents.items():
            score = 0.0
            matched_terms = []
            
            role = agent_info.get("role", "").lower()
            capabilities = [c.lower() for c in agent_info.get("capabilities", [])]
            tools = [t.lower() for t in agent_info.get("tools", [])]
            
            all_terms = [role] + capabilities + tools
            
            for q_term in query_terms:
                for term in all_terms:
                    if q_term == term:
                        score += 1.0
                        matched_terms.append(term)
                    elif q_term in term:
                        score += 0.7
                        matched_terms.append(term)
                    elif term in q_term:
                        score += 0.5
                        matched_terms.append(term)
                    else:
                        similarity = SequenceMatcher(None, q_term, term).ratio()
                        if similarity >= 0.6:
                            score += similarity * 0.5
                            matched_terms.append(term)
            
            if score > 0:
                results.append({
                    "agent_id": agent_id,
                    "role": agent_info.get("role"),
                    "score": round(score / max(len(query_terms), 1), 3),
                    "matched_terms": list(set(matched_terms))[:5],
                    "capabilities": agent_info.get("capabilities", [])[:3]
                })
        
        results.sort(key=lambda x: x["score"], reverse=True)
        
        return {
            "query": query,
            "results": results[:limit],
            "total_matches": len(results)
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Search error: {str(e)}"
        )
