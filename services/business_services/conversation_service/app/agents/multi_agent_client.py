# =============================================================================
# Multi-Agent Service Client
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""
Client for consuming the multi_agent_service from conversation_service.

This client provides:
1. Blackboard operations (task create, claim, artifact submit, review)
2. Contract state management
3. Circuit breaker for graceful degradation
4. Fallback to local execution when service unavailable
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
from pydantic import BaseModel, Field
import httpx
import logging
import os

from .circuit_breaker import CircuitBreaker, ServiceUnavailable

logger = logging.getLogger(__name__)


class TaskCreate(BaseModel):
    """Request to create a task."""
    title: str
    description: str = ""
    done_when: List[str]


class TaskResponse(BaseModel):
    """Response from task operations."""
    id: str
    session_id: str
    title: str
    status: str
    assigned_to: Optional[str] = None
    done_when: List[str] = Field(default_factory=list)
    created_at: str


class ArtifactSubmit(BaseModel):
    """Request to submit an artifact."""
    artifact_type: str
    content: Dict[str, Any]
    task_id: Optional[str] = None


class ArtifactResponse(BaseModel):
    """Response from artifact operations."""
    id: str
    task_id: str
    artifact_type: str
    status: str
    created_by: str
    created_at: str


class ReviewSubmit(BaseModel):
    """Request to submit a review."""
    verdict: str  # "approved" or "rejected"
    comments: str = ""


class ReviewResponse(BaseModel):
    """Response from review operations."""
    id: str
    artifact_id: str
    reviewer: str
    verdict: str
    comments: str
    created_at: str


class AgentStateResponse(BaseModel):
    """Response for agent state."""
    agent_role: str
    session_id: str
    current_state: str
    assumption_count: int = 0
    failed_attempts: int = 0
    tool_call_count: int = 0


class MultiAgentServiceClient:
    """
    Client for blackboard operations via multi_agent_service.
    
    Provides circuit breaker pattern for graceful degradation
    when the service is unavailable.
    """
    
    def __init__(
        self,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
        fallback_enabled: bool = True
    ):
        self.base_url = base_url or os.getenv(
            "MULTI_AGENT_SERVICE_URL",
            "http://multi_agent_service:8000"
        )
        self.timeout = timeout
        self.fallback_enabled = fallback_enabled
        self._circuit_breaker = CircuitBreaker(
            failure_threshold=3,
            recovery_timeout=60
        )
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
    
    async def _request(
        self,
        method: str,
        path: str,
        **kwargs
    ) -> Dict[str, Any]:
        """Make a request with circuit breaker protection."""
        if self._circuit_breaker.is_open:
            raise ServiceUnavailable("Circuit breaker open")
        
        try:
            client = await self._get_client()
            response = await getattr(client, method)(path, **kwargs)
            response.raise_for_status()
            self._circuit_breaker.record_success()
            return response.json()
        except httpx.HTTPError as e:
            self._circuit_breaker.record_failure()
            logger.error(f"multi_agent_service request failed: {e}")
            raise ServiceUnavailable(str(e))
    
    async def create_task(
        self,
        session_id: str,
        title: str,
        description: str,
        done_when: List[str],
        creator_role: str = "coordinator"
    ) -> TaskResponse:
        """Create a task on the blackboard."""
        data = await self._request(
            "post",
            f"/blackboard/{session_id}/tasks",
            params={"creator_role": creator_role},
            json={
                "title": title,
                "description": description,
                "done_when": done_when
            }
        )
        return TaskResponse(**data)
    
    async def claim_task(
        self,
        session_id: str,
        task_id: str,
        agent_role: str
    ) -> TaskResponse:
        """Claim a task for an agent."""
        data = await self._request(
            "post",
            f"/blackboard/{session_id}/tasks/{task_id}/claim",
            json={"agent_role": agent_role}
        )
        return TaskResponse(**data)
    
    async def submit_artifact(
        self,
        session_id: str,
        task_id: str,
        artifact_type: str,
        content: Dict[str, Any],
        creator_role: str
    ) -> ArtifactResponse:
        """Submit an artifact for a task."""
        data = await self._request(
            "post",
            f"/blackboard/{session_id}/artifacts",
            json={
                "task_id": task_id,
                "artifact_type": artifact_type,
                "content": content,
                "creator_role": creator_role
            }
        )
        return ArtifactResponse(**data)
    
    async def get_review_queue(
        self,
        session_id: str,
        reviewer_role: str
    ) -> List[ArtifactResponse]:
        """Get artifacts pending review for a reviewer."""
        data = await self._request(
            "get",
            f"/blackboard/{session_id}/review-queue",
            params={"reviewer_role": reviewer_role}
        )
        return [ArtifactResponse(**item) for item in data.get("items", [])]
    
    async def submit_review(
        self,
        session_id: str,
        artifact_id: str,
        reviewer_role: str,
        verdict: str,
        comments: str = ""
    ) -> ReviewResponse:
        """Submit a review for an artifact."""
        data = await self._request(
            "post",
            f"/blackboard/{session_id}/artifacts/{artifact_id}/review",
            json={
                "reviewer_role": reviewer_role,
                "verdict": verdict,
                "comments": comments
            }
        )
        return ReviewResponse(**data)
    
    async def get_agent_state(
        self,
        session_id: str,
        agent_role: str
    ) -> AgentStateResponse:
        """Get the current state of an agent."""
        data = await self._request(
            "get",
            f"/agents/{agent_role}/state",
            params={"session_id": session_id}
        )
        return AgentStateResponse(**data)
    
    async def transition_state(
        self,
        session_id: str,
        agent_role: str,
        new_state: str,
        rationale: str = ""
    ) -> bool:
        """Request a state transition for an agent."""
        data = await self._request(
            "post",
            f"/agents/{agent_role}/transition",
            params={"session_id": session_id},
            json={
                "to_state": new_state,
                "rationale": rationale
            }
        )
        return data.get("success", False)
    
    async def signal_struggle(
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
        data = await self._request(
            "post",
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
        return data
    
    async def get_session_artifacts(
        self,
        session_id: str
    ) -> List[Dict[str, Any]]:
        """Get all artifacts for a session."""
        data = await self._request(
            "get",
            f"/blackboard/{session_id}/artifacts"
        )
        return data.get("artifacts", []) if isinstance(data, dict) else data
    
    async def get_session_tasks(
        self,
        session_id: str
    ) -> List[Dict[str, Any]]:
        """Get all tasks for a session."""
        data = await self._request(
            "get",
            f"/blackboard/{session_id}/tasks"
        )
        return data.get("tasks", []) if isinstance(data, dict) else data
    
    async def get_contract_status(
        self,
        session_id: str
    ) -> Dict[str, Any]:
        """Get contract compliance status for all agents in a session."""
        try:
            data = await self._request(
                "get",
                f"/agents/contract-status",
                params={"session_id": session_id}
            )
            return data
        except ServiceUnavailable:
            return {
                "agents": [],
                "degraded_mode": True,
                "degraded_reason": "multi_agent_service unavailable"
            }
    
    async def get_session_reviews(
        self,
        session_id: str
    ) -> List[Dict[str, Any]]:
        """Get all reviews for a session."""
        data = await self._request(
            "get",
            f"/blackboard/{session_id}/reviews"
        )
        return data.get("reviews", []) if isinstance(data, dict) else data
    
    async def health_check(self) -> bool:
        """Check if the service is healthy."""
        try:
            await self._request("get", "/health")
            return True
        except ServiceUnavailable:
            return False
    
    def is_available(self) -> bool:
        """Check if the service is available (circuit breaker closed)."""
        return not self._circuit_breaker.is_open
    
    # =========================================================================
    # Session Management Methods (for agents_api.py)
    # =========================================================================
    
    async def create_session(
        self,
        user_id: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Create a new design session."""
        try:
            data = await self._request(
                "post",
                "/api/v1/agents/sessions",
                json={
                    "user_id": user_id,
                    "context": context or {}
                }
            )
            return data
        except ServiceUnavailable:
            # Return a local session placeholder
            import uuid
            return {
                "id": str(uuid.uuid4()),
                "user_id": user_id,
                "status": "active",
                "degraded": True
            }
    
    async def get_session(
        self,
        session_id: str
    ) -> Optional[Dict[str, Any]]:
        """Get session details."""
        try:
            data = await self._request(
                "get",
                f"/api/v1/agents/sessions/{session_id}"
            )
            return data
        except ServiceUnavailable:
            return None
    
    async def send_message(
        self,
        session_id: str,
        message: str
    ) -> Dict[str, Any]:
        """Send a message to a session."""
        try:
            data = await self._request(
                "post",
                f"/api/v1/agents/sessions/{session_id}/message",
                json={"message": message}
            )
            return data
        except ServiceUnavailable:
            return {
                "content": "Service temporarily unavailable. Please try again.",
                "agent_role": "system",
                "success": False,
                "error": "multi_agent_service unavailable"
            }
    
    async def run_parallel_analysis(
        self,
        session_id: str,
        analysis_type: str = "comprehensive"
    ) -> Dict[str, Any]:
        """Run parallel analysis with multiple agents."""
        try:
            data = await self._request(
                "post",
                f"/api/v1/agents/sessions/{session_id}/analyze",
                json={"analysis_type": analysis_type}
            )
            return data
        except ServiceUnavailable:
            return {"error": "multi_agent_service unavailable"}
    
    async def finalize_session(
        self,
        session_id: str
    ) -> Dict[str, Any]:
        """Finalize a design session."""
        try:
            data = await self._request(
                "post",
                f"/api/v1/agents/sessions/{session_id}/finalize"
            )
            return data
        except ServiceUnavailable:
            return {
                "success": False,
                "error": "multi_agent_service unavailable"
            }
    
    async def cancel_session(
        self,
        session_id: str
    ) -> Dict[str, Any]:
        """Cancel a design session."""
        try:
            data = await self._request(
                "delete",
                f"/api/v1/agents/sessions/{session_id}"
            )
            return data
        except ServiceUnavailable:
            return {"success": False, "error": "multi_agent_service unavailable"}
    
    async def list_sessions(
        self,
        user_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """List all sessions, optionally filtered by user."""
        try:
            params = {}
            if user_id:
                params["user_id"] = user_id
            data = await self._request(
                "get",
                "/api/v1/agents/sessions",
                params=params
            )
            return data.get("sessions", []) if isinstance(data, dict) else data
        except ServiceUnavailable:
            return []
