# =============================================================================
# Multi-Agent Service Client
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Client for consuming the multi-agent service from other services."""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
import httpx
import logging

logger = logging.getLogger(__name__)


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


class MultiAgentClient:
    """
    Client for the multi-agent service.
    
    Used by conversation_service and other services to interact
    with the agent contract infrastructure.
    """
    
    def __init__(
        self,
        base_url: str = "http://localhost:8090",
        timeout: float = 120.0
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._client: Optional[httpx.AsyncClient] = None
    
    async def __aenter__(self):
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=self.timeout
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._client:
            await self._client.aclose()
    
    async def _get_client(self) -> httpx.AsyncClient:
        """Get or create the HTTP client."""
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.base_url,
                timeout=self.timeout
            )
        return self._client
    
    async def invoke_agent(
        self,
        session_id: str,
        agent_role: str,
        message: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentInvokeResponse:
        """Invoke an agent with a message."""
        client = await self._get_client()
        
        request = AgentInvokeRequest(
            session_id=session_id,
            agent_role=agent_role,
            message=message,
            context=context
        )
        
        response = await client.post(
            "/agents/invoke",
            json=request.model_dump()
        )
        response.raise_for_status()
        
        return AgentInvokeResponse.model_validate(response.json())
    
    async def get_blackboard(self, session_id: str) -> Dict[str, Any]:
        """Get the blackboard state for a session."""
        client = await self._get_client()
        
        response = await client.get(f"/blackboard/{session_id}")
        response.raise_for_status()
        
        return response.json()
    
    async def create_task(
        self,
        session_id: str,
        title: str,
        description: str,
        done_when: List[str],
        creator_role: str = "coordinator"
    ) -> Dict[str, Any]:
        """Create a task on the blackboard."""
        client = await self._get_client()
        
        response = await client.post(
            f"/blackboard/{session_id}/tasks",
            params={"creator_role": creator_role},
            json={
                "title": title,
                "description": description,
                "done_when": done_when
            }
        )
        response.raise_for_status()
        
        return response.json()
    
    async def claim_task(
        self,
        session_id: str,
        task_id: str,
        agent_role: str
    ) -> Dict[str, Any]:
        """Claim a task for an agent."""
        client = await self._get_client()
        
        response = await client.post(
            f"/blackboard/{session_id}/tasks/{task_id}/claim",
            json={"agent_role": agent_role}
        )
        response.raise_for_status()
        
        return response.json()
    
    async def submit_struggle_signal(
        self,
        session_id: str,
        agent_role: str,
        signal_type: str,
        what_i_understand: str,
        what_i_tried: List[Dict[str, str]],
        where_im_stuck: str,
        what_would_help: str
    ) -> Dict[str, Any]:
        """Submit a struggle signal."""
        client = await self._get_client()
        
        response = await client.post(
            f"/blackboard/{session_id}/struggle-signals",
            json={
                "agent_role": agent_role,
                "signal_type": signal_type,
                "what_i_understand": what_i_understand,
                "what_i_tried": what_i_tried,
                "where_im_stuck": where_im_stuck,
                "what_would_help": what_would_help
            }
        )
        response.raise_for_status()
        
        return response.json()
    
    async def get_dashboard_summary(self, session_id: str) -> Dict[str, Any]:
        """Get the dashboard summary for a session."""
        client = await self._get_client()
        
        response = await client.get(f"/dashboard/{session_id}/summary")
        response.raise_for_status()
        
        return response.json()
    
    async def run_hello_diagnostic(
        self,
        session_id: str,
        agent_role: str
    ) -> Dict[str, Any]:
        """Run the hello diagnostic for an agent."""
        client = await self._get_client()
        
        response = await client.post(
            f"/dashboard/{session_id}/hello-diagnostic",
            json={"agent_role": agent_role}
        )
        response.raise_for_status()
        
        return response.json()
    
    async def get_agent_contract(self, agent_role: str) -> Dict[str, Any]:
        """Get the contract for a specific agent role."""
        client = await self._get_client()
        
        response = await client.get(f"/agents/{agent_role}/contract")
        response.raise_for_status()
        
        return response.json()
    
    async def reset_agent(
        self,
        session_id: str,
        agent_role: str
    ) -> Dict[str, Any]:
        """Reset an agent to IDLE state."""
        client = await self._get_client()
        
        response = await client.post(
            f"/agents/{agent_role}/reset",
            params={"session_id": session_id}
        )
        response.raise_for_status()
        
        return response.json()
    
    async def health_check(self) -> Dict[str, Any]:
        """Check service health."""
        client = await self._get_client()
        
        response = await client.get("/health")
        response.raise_for_status()
        
        return response.json()
