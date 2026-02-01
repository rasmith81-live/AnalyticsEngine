# =============================================================================
# Agent API Routes
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""API routes for agent invocation and management."""

from fastapi import APIRouter, HTTPException, Request, Depends
from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any
from datetime import datetime

router = APIRouter()


class AgentInvokeRequest(BaseModel):
    """Request to invoke an agent."""
    session_id: str
    agent_role: str
    message: str
    context: Optional[Dict[str, Any]] = None


class AgentInvokeResponse(BaseModel):
    """Response from agent invocation."""
    session_id: str
    agent_role: str
    response: str
    state: str
    artifacts: List[Dict[str, Any]] = Field(default_factory=list)
    struggle_signal: Optional[Dict[str, Any]] = None
    approval_request: Optional[Dict[str, Any]] = None
    timestamp: str


class AgentListResponse(BaseModel):
    """List of available agents."""
    agents: List[Dict[str, str]]


@router.post("/invoke", response_model=AgentInvokeResponse)
async def invoke_agent(
    request: Request,
    invoke_request: AgentInvokeRequest
) -> AgentInvokeResponse:
    """
    Invoke an agent with a message.
    
    The agent will process the message according to its contract,
    potentially transitioning through states, requesting approval,
    or signaling struggle.
    """
    # Get or create blackboard for session
    store = request.app.state.blackboard_store
    blackboard = await store.get_or_create_blackboard(invoke_request.session_id)
    
    # TODO: Implement actual agent invocation
    # For now, return a placeholder response
    return AgentInvokeResponse(
        session_id=invoke_request.session_id,
        agent_role=invoke_request.agent_role,
        response=f"Agent {invoke_request.agent_role} received message. Implementation pending.",
        state="idle",
        artifacts=[],
        struggle_signal=None,
        approval_request=None,
        timestamp=datetime.utcnow().isoformat()
    )


@router.get("/list", response_model=AgentListResponse)
async def list_agents() -> AgentListResponse:
    """List all available agent roles."""
    agents = [
        # Strategy & Analysis Layer
        {"role": "coordinator", "layer": "strategy", "description": "Master orchestrator"},
        {"role": "business_strategist", "layer": "strategy", "description": "Strategy frameworks"},
        {"role": "business_analyst", "layer": "strategy", "description": "KPI requirements"},
        {"role": "data_analyst", "layer": "strategy", "description": "KPI calculations"},
        {"role": "data_scientist", "layer": "strategy", "description": "ML specifications"},
        {"role": "operations_manager", "layer": "strategy", "description": "Optimization plans"},
        {"role": "mapping_specialist", "layer": "strategy", "description": "Source mappings"},
        {"role": "document_analyzer", "layer": "strategy", "description": "Entity extraction"},
        {"role": "competitive_analyst", "layer": "strategy", "description": "Market analysis"},
        
        # Technical Design Layer
        {"role": "architect", "layer": "technical", "description": "Entity/aggregate design"},
        {"role": "developer", "layer": "technical", "description": "Code implementation"},
        {"role": "tester", "layer": "technical", "description": "Quality assurance"},
        {"role": "documenter", "layer": "technical", "description": "Documentation"},
        {"role": "deployment_specialist", "layer": "technical", "description": "Infrastructure"},
        {"role": "ui_designer", "layer": "technical", "description": "Dashboard design"},
        {"role": "itil_manager", "layer": "technical", "description": "Service management"},
        {"role": "connection_specialist", "layer": "technical", "description": "Integration"},
        
        # Business Operations Layer
        {"role": "sales_manager", "layer": "business_ops", "description": "Pipeline management"},
        {"role": "marketing_manager", "layer": "business_ops", "description": "Campaign metrics"},
        {"role": "accountant", "layer": "business_ops", "description": "Financial docs"},
        {"role": "customer_success_manager", "layer": "business_ops", "description": "Health assessment"},
        {"role": "hr_talent_analyst", "layer": "business_ops", "description": "People analytics"},
        {"role": "supply_chain_analyst", "layer": "business_ops", "description": "Supply chain"},
        {"role": "risk_compliance_officer", "layer": "business_ops", "description": "Risk/compliance"},
        {"role": "project_manager", "layer": "business_ops", "description": "Agile planning"},
        
        # Governance Layer
        {"role": "data_governance_specialist", "layer": "governance", "description": "DAMA DMBOK"},
        {"role": "process_scenario_modeler", "layer": "governance", "description": "Simulation"},
        {"role": "librarian_curator", "layer": "governance", "description": "KPI library"},
    ]
    return AgentListResponse(agents=agents)


@router.get("/{agent_role}/contract")
async def get_agent_contract(agent_role: str) -> Dict[str, Any]:
    """Get the contract for a specific agent role."""
    # TODO: Return the actual contract for the agent
    return {
        "agent_role": agent_role,
        "tier_0_rules": [
            "Never fabricate success",
            "Never modify tests to pass",
            "Never expand scope without approval"
        ],
        "tier_1_rules": [
            "Follow state machine transitions",
            "Request approval before execution",
            "Signal struggle after 2 failed attempts"
        ],
        "state_machine": {
            "current_state": "idle",
            "allowed_transitions": ["analysis"]
        }
    }


@router.post("/{agent_role}/reset")
async def reset_agent(
    request: Request,
    agent_role: str,
    session_id: str
) -> Dict[str, str]:
    """Reset an agent to IDLE state (RESET semantics)."""
    # TODO: Implement agent reset
    return {
        "status": "reset",
        "agent_role": agent_role,
        "session_id": session_id,
        "new_state": "idle"
    }


class StateTransitionRequest(BaseModel):
    """Request to transition agent state."""
    to_state: str
    rationale: str = ""


class StateTransitionResponse(BaseModel):
    """Response from state transition."""
    success: bool
    agent_role: str
    session_id: str
    from_state: str
    to_state: str
    message: str


# Forbidden transitions based on state machine rules
FORBIDDEN_TRANSITIONS = {
    ("analysis", "execution"),      # Must get approval first
    ("analysis", "done"),           # Can't skip to done
    ("execution", "done"),          # Must validate first
    ("approval_pending", "done"),   # Must execute first
    ("idle", "execution"),          # Must analyze first
    ("idle", "done"),               # Can't skip to done
}


@router.post("/{agent_role}/transition", response_model=StateTransitionResponse)
async def transition_agent_state(
    request: Request,
    agent_role: str,
    session_id: str,
    transition_request: StateTransitionRequest
) -> StateTransitionResponse:
    """
    Transition an agent to a new state.
    
    Validates against forbidden transitions defined in the state machine.
    """
    store = request.app.state.blackboard_store
    blackboard = await store.get_or_create_blackboard(session_id)
    
    # Get current state (default to idle)
    current_state = blackboard.agent_states.get(agent_role, "idle")
    to_state = transition_request.to_state.lower()
    
    # Check for forbidden transition
    if (current_state, to_state) in FORBIDDEN_TRANSITIONS:
        return StateTransitionResponse(
            success=False,
            agent_role=agent_role,
            session_id=session_id,
            from_state=current_state,
            to_state=to_state,
            message=f"Forbidden transition: {current_state} → {to_state}. This transition violates state machine rules."
        )
    
    # Update state
    blackboard.agent_states[agent_role] = to_state
    await store.save_blackboard(blackboard)
    
    return StateTransitionResponse(
        success=True,
        agent_role=agent_role,
        session_id=session_id,
        from_state=current_state,
        to_state=to_state,
        message=f"State transitioned successfully. Rationale: {transition_request.rationale or 'None provided'}"
    )


@router.get("/{agent_role}/state")
async def get_agent_state(
    request: Request,
    agent_role: str,
    session_id: str
) -> Dict[str, Any]:
    """Get current state of an agent in a session."""
    store = request.app.state.blackboard_store
    blackboard = await store.load_blackboard(session_id)
    
    if not blackboard:
        return {
            "agent_role": agent_role,
            "session_id": session_id,
            "current_state": "idle",
            "assumption_count": 0,
            "failed_attempts": 0,
            "contract_violations": 0
        }
    
    return {
        "agent_role": agent_role,
        "session_id": session_id,
        "current_state": blackboard.agent_states.get(agent_role, "idle"),
        "assumption_count": 0,
        "failed_attempts": 0,
        "contract_violations": 0
    }


@router.get("/contract-status")
async def get_contract_status(
    request: Request,
    session_id: str
) -> Dict[str, Any]:
    """Get contract compliance status for all agents in a session."""
    store = request.app.state.blackboard_store
    blackboard = await store.load_blackboard(session_id)
    
    if not blackboard:
        return {
            "session_id": session_id,
            "agents": [],
            "degraded_mode": False,
            "degraded_reason": None
        }
    
    agents = []
    for agent_role, state in blackboard.agent_states.items():
        agents.append({
            "agent_role": agent_role,
            "current_state": state,
            "contract_violations": 0,
            "tier_0_compliant": True,
            "tier_1_compliant": True
        })
    
    return {
        "session_id": session_id,
        "agents": agents,
        "degraded_mode": False,
        "degraded_reason": None
    }
