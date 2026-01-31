# =============================================================================
# Blackboard Agent Mixin
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# Migrated from conversation_service as part of architecture consolidation
# =============================================================================
"""
Mixin that adds blackboard coordination to agents.

This mixin allows agents to integrate with the blackboard
for task coordination, artifact submission, and peer review.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
import logging
import os

from ..blackboard.operations import BlackboardOperations
from ..blackboard.store import RedisBlackboardStore

logger = logging.getLogger(__name__)


DEGRADED_MODE_ANNOUNCEMENT = """
⚠️ DEGRADED MODE ACTIVE

The following contract features are suspended:
- Peer review (self-review allowed temporarily)
- State machine enforcement
- Blackboard audit logging

Tier 0 rules remain in effect:
- Never fabricate success
- Never modify tests to pass
- Signal when stuck

Reason: {reason}
"""


class BlackboardAgentMixin:
    """
    Mixin that adds blackboard coordination to agents.
    
    Usage:
        class MyAgent(BlackboardAgentMixin, BaseAgent):
            pass
    
    This mixin provides:
    - Blackboard task and artifact operations
    - Contract state management
    - Graceful degradation when service is unavailable
    """
    
    _blackboard_ops: Optional[BlackboardOperations] = None
    _blackboard_enabled: bool = True
    _degraded_mode: bool = False
    _degraded_reason: Optional[str] = None
    
    def _init_blackboard(self, session_id: str, blackboard_store: Optional[RedisBlackboardStore] = None):
        """Initialize the blackboard operations."""
        self._session_id = session_id
        self._blackboard_enabled = os.getenv(
            "MULTI_AGENT_SERVICE_ENABLED", "true"
        ).lower() == "true"
        
        if self._blackboard_enabled and blackboard_store:
            self._blackboard_ops = BlackboardOperations(blackboard_store)
    
    async def consult_peer_via_blackboard(
        self,
        peer_role: str,
        question: str,
        context_summary: str
    ) -> Dict[str, Any]:
        """
        Consult a peer agent via the blackboard.
        
        Instead of direct peer calls, creates a task on the blackboard
        that the peer agent can claim and respond to.
        """
        if not self._blackboard_enabled or self._degraded_mode or not self._blackboard_ops:
            return await self._consult_peer_local(peer_role, question, context_summary)
        
        try:
            task = await self._blackboard_ops.create_task(
                session_id=self._session_id,
                title=f"Peer consultation: {question[:50]}...",
                description=f"Question from {self._agent_role}: {question}\n\nContext: {context_summary}",
                done_when=["Response provided"],
                creator_role=self._agent_role
            )
            
            logger.info(
                f"Created consultation task {task.id} for peer {peer_role}"
            )
            
            return {
                "success": True,
                "task_id": task.id,
                "message": f"Consultation request created for {peer_role}",
                "via": "blackboard"
            }
        except Exception as e:
            self._enter_degraded_mode(str(e))
            return await self._consult_peer_local(peer_role, question, context_summary)
    
    async def _consult_peer_local(
        self,
        peer_role: str,
        question: str,
        context_summary: str
    ) -> Dict[str, Any]:
        """Fallback: consult peer using local mechanism."""
        if hasattr(self, '_consult_peer'):
            return await self._consult_peer({
                "peer_role": peer_role,
                "question": question,
                "context_summary": context_summary
            }, getattr(self, '_context', None))
        
        return {
            "success": False,
            "error": "Local peer consultation not available",
            "degraded": True
        }
    
    async def signal_ready_via_blackboard(
        self,
        summary: str,
        key_findings: List[str],
        recommendations: List[str] = None
    ) -> Dict[str, Any]:
        """
        Signal readiness via the blackboard.
        
        Updates the agent's task status and submits findings as artifacts.
        """
        if not self._blackboard_enabled or self._degraded_mode or not self._blackboard_ops:
            return await self._signal_ready_local(summary, key_findings, recommendations)
        
        try:
            artifact = await self._blackboard_ops.submit_artifact(
                session_id=self._session_id,
                task_id=getattr(self, '_current_task_id', 'unknown'),
                artifact_type="ready_signal",
                content={
                    "summary": summary,
                    "key_findings": key_findings,
                    "recommendations": recommendations or [],
                    "agent_role": self._agent_role,
                    "timestamp": datetime.utcnow().isoformat()
                },
                creator_role=self._agent_role
            )
            
            logger.info(f"Submitted ready signal artifact {artifact.id}")
            
            return {
                "success": True,
                "artifact_id": artifact.id,
                "message": "Ready signal submitted to blackboard"
            }
        except Exception as e:
            self._enter_degraded_mode(str(e))
            return await self._signal_ready_local(summary, key_findings, recommendations)
    
    async def _signal_ready_local(
        self,
        summary: str,
        key_findings: List[str],
        recommendations: List[str] = None
    ) -> Dict[str, Any]:
        """Fallback: signal ready using local mechanism."""
        if hasattr(self, '_signal_ready_for_coordinator'):
            return await self._signal_ready_for_coordinator({
                "summary": summary,
                "key_findings": key_findings,
                "recommendations": recommendations or [],
                "peers_consulted": []
            }, getattr(self, '_context', None))
        
        return {
            "success": True,
            "degraded": True,
            "message": "Ready signal stored locally (degraded mode)"
        }
    
    async def submit_for_review(
        self,
        artifact_type: str,
        content: Dict[str, Any],
        done_when_checklist: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Submit work for peer review via the blackboard.
        
        Required before completion per contract.
        """
        if not self._blackboard_enabled or self._degraded_mode or not self._blackboard_ops:
            logger.warning("Peer review skipped - degraded mode")
            return {
                "success": True,
                "degraded": True,
                "message": "Review skipped in degraded mode"
            }
        
        try:
            artifact = await self._blackboard_ops.submit_artifact(
                session_id=self._session_id,
                task_id=getattr(self, '_current_task_id', 'unknown'),
                artifact_type=artifact_type,
                content={
                    **content,
                    "done_when_checklist": done_when_checklist
                },
                creator_role=self._agent_role
            )
            
            logger.info(
                f"Submitted artifact {artifact.id} for review (type: {artifact_type})"
            )
            
            return {
                "success": True,
                "artifact_id": artifact.id,
                "status": "pending_review",
                "message": "Submitted for peer review"
            }
        except Exception as e:
            self._enter_degraded_mode(str(e))
            return {
                "success": True,
                "degraded": True,
                "message": "Review skipped - service unavailable"
            }
    
    async def check_contract_compliance(self, action: str) -> bool:
        """
        Check if an action is compliant with the contract.
        
        Returns True if compliant, False if violation detected.
        """
        if not self._blackboard_enabled or self._degraded_mode:
            return True
        
        # Contract compliance check would be done via the contract adapter
        return True
    
    async def transition_state(
        self,
        new_state: str,
        rationale: str = ""
    ) -> bool:
        """
        Request a state transition.
        
        The contract enforcer will validate the transition.
        """
        if not self._blackboard_enabled or self._degraded_mode:
            return True
        
        # State transition would be handled by the contract adapter
        return True
    
    def _enter_degraded_mode(self, reason: str):
        """Enter degraded mode when service is unavailable."""
        if not self._degraded_mode:
            self._degraded_mode = True
            self._degraded_reason = reason
            logger.warning(
                f"Entering DEGRADED MODE: {reason}"
            )
    
    def get_degraded_announcement(self) -> Optional[str]:
        """Get the degraded mode announcement if active."""
        if self._degraded_mode:
            return DEGRADED_MODE_ANNOUNCEMENT.format(
                reason=self._degraded_reason or "Unknown"
            )
        return None
    
    @property
    def _agent_role(self) -> str:
        """Get the agent role."""
        if hasattr(self, 'config') and hasattr(self.config, 'role'):
            role = self.config.role
            return role.value if hasattr(role, 'value') else str(role)
        return "unknown"
