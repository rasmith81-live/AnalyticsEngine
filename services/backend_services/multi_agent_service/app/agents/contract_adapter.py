# =============================================================================
# Contract Adapter for Agent Integration
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# Migrated from conversation_service as part of architecture consolidation
# =============================================================================
"""
Adapter for integrating contract infrastructure into agents.

This adapter allows agents to:
1. Use behavioral contracts
2. Follow the state machine
3. Participate in peer review
4. Report to the blackboard
5. Use the dashboard for monitoring
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime
import logging
import os

logger = logging.getLogger(__name__)

# Multi-agent service configuration
MULTI_AGENT_SERVICE_URL = os.getenv(
    "MULTI_AGENT_SERVICE_URL", 
    "http://localhost:8090"
)


@dataclass
class ContractState:
    """Local contract state tracking for an agent."""
    agent_role: str
    session_id: str
    current_state: str = "idle"
    assumption_count: int = 0
    failed_attempts: int = 0
    tool_call_count: int = 0
    tier_0_violations: int = 0
    tier_1_violations: int = 0
    last_transition: Optional[datetime] = None
    
    # Thresholds
    max_assumptions: int = 3
    max_failed_attempts: int = 2
    max_tool_calls: int = 10


@dataclass
class ApprovalRequest:
    """Local approval request structure."""
    intent: str
    scope: str
    approach: str
    consequences: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)
    validation_plan: str = ""
    assumptions: List[str] = field(default_factory=list)
    status: str = "pending"


@dataclass
class StruggleSignal:
    """Local struggle signal structure."""
    signal_type: str
    what_i_understand: str
    what_i_tried: List[Dict[str, str]] = field(default_factory=list)
    where_im_stuck: str = ""
    what_would_help: str = ""


class ContractAdapter:
    """
    Adapter that adds contract enforcement to agents.
    
    This adapter integrates with the multi_agent_service contract
    infrastructure to enforce behavioral contracts.
    """
    
    # Forbidden state transitions
    FORBIDDEN_TRANSITIONS = {
        ("analysis", "execution"),
        ("analysis", "done"),
        ("execution", "done"),
        ("approval_pending", "done"),
        ("idle", "execution"),
        ("idle", "done"),
    }
    
    # Valid state transitions
    VALID_TRANSITIONS = {
        ("idle", "analysis"),
        ("analysis", "approval_pending"),
        ("analysis", "blocked"),
        ("approval_pending", "execution"),
        ("approval_pending", "analysis"),
        ("execution", "validation"),
        ("execution", "blocked"),
        ("validation", "done"),
        ("validation", "execution"),
        ("blocked", "analysis"),
        ("blocked", "reset"),
        ("done", "idle"),
        ("reset", "idle"),
    }
    
    def __init__(self, agent_role: str, session_id: str):
        self.state = ContractState(
            agent_role=agent_role,
            session_id=session_id
        )
        self._pending_approval: Optional[ApprovalRequest] = None
        self._fix_history: List[str] = []
    
    def get_current_state(self) -> str:
        """Get the current state machine state."""
        return self.state.current_state
    
    def can_transition_to(self, target_state: str) -> bool:
        """Check if a transition to the target state is allowed."""
        current = self.state.current_state
        return (current, target_state) in self.VALID_TRANSITIONS
    
    def is_transition_forbidden(self, target_state: str) -> bool:
        """Check if a transition is explicitly forbidden."""
        current = self.state.current_state
        return (current, target_state) in self.FORBIDDEN_TRANSITIONS
    
    def transition_to(self, target_state: str) -> bool:
        """
        Attempt to transition to a new state.
        
        Returns True if successful, raises ValueError if forbidden.
        """
        if self.is_transition_forbidden(target_state):
            self.state.tier_1_violations += 1
            raise ValueError(
                f"Forbidden transition: {self.state.current_state} → {target_state}. "
                f"This violates the contract."
            )
        
        if not self.can_transition_to(target_state):
            raise ValueError(
                f"Invalid transition: {self.state.current_state} → {target_state}. "
                f"Not in valid transitions."
            )
        
        self.state.current_state = target_state
        self.state.last_transition = datetime.utcnow()
        return True
    
    def add_assumption(self, assumption: str) -> bool:
        """
        Add an assumption and check for overflow.
        
        Returns True if overflow (hard stop trigger).
        """
        self.state.assumption_count += 1
        
        if self.state.assumption_count >= self.state.max_assumptions:
            logger.warning(
                f"Assumption overflow: {self.state.assumption_count} >= "
                f"{self.state.max_assumptions}. Hard stop triggered."
            )
            return True
        
        return False
    
    def record_failed_attempt(self) -> bool:
        """
        Record a failed attempt.
        
        Returns True if struggle signal should be sent.
        """
        self.state.failed_attempts += 1
        return self.state.failed_attempts >= self.state.max_failed_attempts
    
    def record_fix_attempt(self, fix_description: str) -> bool:
        """
        Record a fix attempt and check for repetition.
        
        Returns True if repeated fix (hard stop trigger).
        """
        normalized = fix_description.lower().strip()
        
        for prev in self._fix_history:
            if self._similar(normalized, prev):
                logger.warning(f"Repeated fix detected: {fix_description}")
                return True
        
        self._fix_history.append(normalized)
        return False
    
    def _similar(self, s1: str, s2: str) -> bool:
        """Check if two strings are similar."""
        words1 = set(s1.split())
        words2 = set(s2.split())
        if not words1 or not words2:
            return False
        overlap = len(words1.intersection(words2))
        total = len(words1.union(words2))
        return overlap / total > 0.7
    
    def record_tool_call(self) -> bool:
        """
        Record a tool call.
        
        Returns True if limit exceeded.
        """
        self.state.tool_call_count += 1
        return self.state.tool_call_count >= self.state.max_tool_calls
    
    def reset_task_tracking(self) -> None:
        """Reset tracking for a new task."""
        self.state.assumption_count = 0
        self.state.failed_attempts = 0
        self.state.tool_call_count = 0
        self._fix_history.clear()
    
    def create_approval_request(
        self,
        intent: str,
        scope: str,
        approach: str,
        consequences: List[str] = None,
        risks: List[str] = None,
        validation_plan: str = "",
        assumptions: List[str] = None
    ) -> ApprovalRequest:
        """Create an approval request."""
        self._pending_approval = ApprovalRequest(
            intent=intent,
            scope=scope,
            approach=approach,
            consequences=consequences or [],
            risks=risks or [],
            validation_plan=validation_plan,
            assumptions=assumptions or []
        )
        
        # Check assumptions
        for assumption in (assumptions or []):
            if self.add_assumption(assumption):
                raise ValueError("Assumption overflow - too many assumptions")
        
        # Transition to approval pending
        self.transition_to("approval_pending")
        
        return self._pending_approval
    
    def create_struggle_signal(
        self,
        signal_type: str,
        what_i_understand: str,
        what_i_tried: List[Dict[str, str]],
        where_im_stuck: str,
        what_would_help: str
    ) -> StruggleSignal:
        """Create a struggle signal."""
        signal = StruggleSignal(
            signal_type=signal_type,
            what_i_understand=what_i_understand,
            what_i_tried=what_i_tried,
            where_im_stuck=where_im_stuck,
            what_would_help=what_would_help
        )
        
        # Transition to blocked
        self.transition_to("blocked")
        
        return signal
    
    def force_reset(self) -> None:
        """Force a reset to idle state."""
        self.state.current_state = "idle"
        self.reset_task_tracking()
        logger.info(f"Agent {self.state.agent_role} forced to RESET")
    
    def get_contract_prompt_section(self) -> str:
        """Generate the contract section to inject into the system prompt."""
        return f"""
## Behavioral Contract

This contract is the single source of truth. When conflicts arise, defer here.

### Current State
State: {self.state.current_state.upper()}
Assumptions: {self.state.assumption_count}/{self.state.max_assumptions}
Failed Attempts: {self.state.failed_attempts}/{self.state.max_failed_attempts}
Tool Calls: {self.state.tool_call_count}/{self.state.max_tool_calls}

### Tier 0 Rules (NEVER VIOLATE)
- Never fabricate success or claim completion without verification
- Never modify tests to make them pass instead of fixing the code
- Never expand scope beyond what was approved
- Never hide difficulty or pretend to understand when confused

### Tier 1 Rules (Core Workflow)
- Follow the state machine - no forbidden transitions
- Request approval before any state-changing action
- Signal struggle within 2 failed attempts
- Submit work to designated reviewer, never self-approve

### Hard Stop Triggers
If any of these fire, STOP immediately:
- Same fix proposed twice
- Assumption count >= 3
- Tool failed 3x consecutively
- Evidence contradicts hypothesis

### Struggle Protocol
After 2 failed attempts, you MUST signal:
🚨 SYNC NEEDED — [signal type]
What I understand: ...
What I've tried: ...
Where I'm stuck: ...
What would help: ...
"""
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get current metrics for dashboard."""
        return {
            "agent_role": self.state.agent_role,
            "session_id": self.state.session_id,
            "current_state": self.state.current_state,
            "assumption_count": self.state.assumption_count,
            "failed_attempts": self.state.failed_attempts,
            "tool_call_count": self.state.tool_call_count,
            "tier_0_violations": self.state.tier_0_violations,
            "tier_1_violations": self.state.tier_1_violations,
        }
