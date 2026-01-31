# =============================================================================
# Escalation Handling
# Based on: Tangi Vass - "Adversarial Vibe Coding" / LIZA System
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Escalation handling with two-failures rule."""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class EscalationReason(str, Enum):
    """Reasons for escalation."""
    TWO_FAILURES = "two_failures"
    BLOCKED = "blocked"
    VIOLATION = "violation"
    TIMEOUT = "timeout"
    MANUAL = "manual"


class Escalation(BaseModel):
    """An escalation record."""
    escalation_id: str
    task_id: str
    reason: EscalationReason
    failed_by: List[str] = Field(default_factory=list)
    failure_reasons: List[str] = Field(default_factory=list)
    escalated_to: str = "coordinator"
    resolved: bool = False
    resolution: Optional[str] = None
    resolved_by: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    resolved_at: Optional[datetime] = None


class TwoFailuresRule:
    """
    The Two-Failures Rule from the LIZA system.
    
    From the article:
    "If two different agents fail the same task, the task is presumed
    to be poorly defined. It is blocked and escalated to the coordinator,
    who must document why before rescoping."
    """
    
    def check(self, failed_by: List[str]) -> bool:
        """Check if the two-failures rule applies."""
        unique_agents = set(failed_by)
        return len(unique_agents) >= 2
    
    def create_escalation(
        self,
        task_id: str,
        failed_by: List[str],
        failure_reasons: List[str]
    ) -> Escalation:
        """Create an escalation due to two-failures rule."""
        return Escalation(
            escalation_id=f"ESC-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
            task_id=task_id,
            reason=EscalationReason.TWO_FAILURES,
            failed_by=failed_by,
            failure_reasons=failure_reasons,
            escalated_to="coordinator"
        )


class EscalationHandler:
    """
    Handler for task escalations.
    
    Manages the escalation workflow when tasks cannot be completed
    through normal channels.
    """
    
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.escalations: Dict[str, Escalation] = {}
        self.two_failures_rule = TwoFailuresRule()
    
    def check_and_escalate(
        self,
        task_id: str,
        failed_by: List[str],
        failure_reasons: List[str]
    ) -> Optional[Escalation]:
        """Check if escalation is needed and create if so."""
        if self.two_failures_rule.check(failed_by):
            escalation = self.two_failures_rule.create_escalation(
                task_id, failed_by, failure_reasons
            )
            self.escalations[escalation.escalation_id] = escalation
            return escalation
        return None
    
    def escalate_blocked(
        self,
        task_id: str,
        blocked_reason: str
    ) -> Escalation:
        """Escalate a blocked task."""
        escalation = Escalation(
            escalation_id=f"ESC-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
            task_id=task_id,
            reason=EscalationReason.BLOCKED,
            failure_reasons=[blocked_reason],
            escalated_to="coordinator"
        )
        self.escalations[escalation.escalation_id] = escalation
        return escalation
    
    def escalate_violation(
        self,
        task_id: str,
        violation_details: str,
        agent_role: str
    ) -> Escalation:
        """Escalate due to a contract violation."""
        escalation = Escalation(
            escalation_id=f"ESC-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
            task_id=task_id,
            reason=EscalationReason.VIOLATION,
            failed_by=[agent_role],
            failure_reasons=[violation_details],
            escalated_to="coordinator"
        )
        self.escalations[escalation.escalation_id] = escalation
        return escalation
    
    def resolve(
        self,
        escalation_id: str,
        resolution: str,
        resolved_by: str
    ) -> Escalation:
        """Resolve an escalation."""
        if escalation_id not in self.escalations:
            raise ValueError(f"Escalation {escalation_id} not found")
        
        escalation = self.escalations[escalation_id]
        escalation.resolved = True
        escalation.resolution = resolution
        escalation.resolved_by = resolved_by
        escalation.resolved_at = datetime.utcnow()
        
        return escalation
    
    def get_pending_escalations(self) -> List[Escalation]:
        """Get all pending (unresolved) escalations."""
        return [e for e in self.escalations.values() if not e.resolved]
    
    def get_escalation_for_task(self, task_id: str) -> Optional[Escalation]:
        """Get the most recent escalation for a task."""
        task_escalations = [
            e for e in self.escalations.values()
            if e.task_id == task_id
        ]
        if task_escalations:
            return sorted(task_escalations, key=lambda e: e.created_at)[-1]
        return None
    
    def get_escalation_metrics(self) -> Dict[str, Any]:
        """Get metrics about escalations."""
        total = len(self.escalations)
        resolved = sum(1 for e in self.escalations.values() if e.resolved)
        by_reason = {}
        for e in self.escalations.values():
            reason = e.reason.value
            by_reason[reason] = by_reason.get(reason, 0) + 1
        
        return {
            "total_escalations": total,
            "resolved": resolved,
            "pending": total - resolved,
            "by_reason": by_reason
        }
