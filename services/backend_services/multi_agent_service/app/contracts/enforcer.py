# =============================================================================
# Contract Enforcer
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
#
# "The enforcer monitors agent behavior for contract violations.
# It tracks assumptions, fix attempts, tool failures, and triggers
# hard stops when thresholds are exceeded."
# =============================================================================
"""Contract enforcement and hard stop trigger monitoring."""

from enum import Enum
from typing import Dict, List, Optional, Any, Callable
from pydantic import BaseModel, Field
from datetime import datetime
import logging

from .state_machine import AgentContract, AgentState
from .tier_rules import ContractRules, RuleTier
from .violations import ContractViolation, ViolationHandler

logger = logging.getLogger(__name__)


class HardStopTrigger(str, Enum):
    """
    Hard stop triggers - binary, observable conditions that halt execution.
    
    From the article:
    "Hard stops are not warnings. They are binary, observable conditions.
    When a trigger fires, execution halts. No negotiation."
    """
    ASSUMPTION_OVERFLOW = "assumption_count_exceeded"
    REPEATED_FIX = "same_fix_proposed_twice"
    EVIDENCE_CONTRADICTION = "evidence_contradicts_hypothesis"
    EXECUTION_DIVERGENCE = "execution_diverges_from_approval"
    TOOL_FAILURE_CASCADE = "tool_failed_3x"
    RULE_VIOLATION_REPEAT = "same_rule_violated_twice"
    CONTEXT_COLLAPSE = "context_budget_exceeded"


class ApprovalRequest(BaseModel):
    """
    Structured approval request before any state-changing action.
    
    From the article:
    "Before any state-changing action, present: intent, scope, commands,
    consequences, risks, validation plan. This is the approval gate."
    """
    request_id: str
    agent_role: str
    session_id: str
    
    # What you're trying to achieve
    intent: str
    
    # What files/entities will be affected
    scope: str
    
    # How you plan to do it
    approach: str
    
    # What will change
    consequences: List[str] = Field(default_factory=list)
    
    # What could go wrong
    risks: List[str] = Field(default_factory=list)
    
    # How you'll verify success
    validation_plan: str
    
    # What you're assuming (count matters!)
    assumptions: List[str] = Field(default_factory=list)
    
    # Can this be undone?
    reversibility: str = "unknown"
    
    # Status
    status: str = "pending"  # pending, approved, rejected
    approved_at: Optional[datetime] = None
    approved_by: Optional[str] = None
    rejection_reason: Optional[str] = None
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.utcnow)


class StruggleSignal(BaseModel):
    """
    Structured signal when agent is stuck.
    
    From the article:
    "The Struggle Protocol transforms a deception risk into a collaboration
    opportunity. When stuck, agents signal with structured format."
    """
    signal_type: str  # "blocked", "confused", "conflicting_evidence", "resource_missing"
    what_i_understand: str
    what_i_tried: List[Dict[str, str]] = Field(default_factory=list)  # [{action, outcome}]
    where_im_stuck: str
    what_would_help: str
    
    # Metadata
    agent_role: str
    session_id: str
    task_id: Optional[str] = None
    attempt_count: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    def to_prompt_format(self) -> str:
        """Format the struggle signal for display."""
        tried_str = "\n".join([
            f"  - {t.get('action', 'unknown')}: {t.get('outcome', 'unknown')}"
            for t in self.what_i_tried
        ])
        return f"""🚨 SYNC NEEDED — {self.signal_type}

What I understand: {self.what_i_understand}

What I've tried:
{tried_str}

Where I'm stuck: {self.where_im_stuck}

What would help: {self.what_would_help}
"""


class ContractEnforcer:
    """
    Monitors agent behavior for contract violations and hard stop triggers.
    
    Tracks:
    - Assumption count (threshold: 3)
    - Fix history (detect repeated fixes)
    - Tool failures (threshold: 3 consecutive)
    - Rule violations (detect patterns)
    """
    
    DEFAULT_ASSUMPTION_THRESHOLD = 3
    DEFAULT_TOOL_FAILURE_THRESHOLD = 3
    DEFAULT_STRUGGLE_SIGNAL_AFTER = 2
    
    def __init__(
        self,
        contract_rules: ContractRules = None,
        assumption_threshold: int = DEFAULT_ASSUMPTION_THRESHOLD,
        tool_failure_threshold: int = DEFAULT_TOOL_FAILURE_THRESHOLD,
        struggle_signal_after: int = DEFAULT_STRUGGLE_SIGNAL_AFTER
    ):
        self.rules = contract_rules or ContractRules.get_universal_rules()
        self.assumption_threshold = assumption_threshold
        self.tool_failure_threshold = tool_failure_threshold
        self.struggle_signal_after = struggle_signal_after
        
        # Tracking state
        self.assumption_count = 0
        self.assumptions: List[str] = []
        self.fix_history: List[str] = []
        self.tool_failures: Dict[str, int] = {}
        self.consecutive_tool_failures = 0
        self.failed_attempts = 0
        
        # Violation handling
        self.violation_handler = ViolationHandler()
        
        # Pending approvals
        self.pending_approvals: Dict[str, ApprovalRequest] = {}
        self.approved_requests: Dict[str, ApprovalRequest] = {}
        
        # Struggle signals
        self.struggle_signals: List[StruggleSignal] = []
    
    def reset_tracking(self) -> None:
        """Reset tracking state for a new task."""
        self.assumption_count = 0
        self.assumptions.clear()
        self.fix_history.clear()
        self.tool_failures.clear()
        self.consecutive_tool_failures = 0
        self.failed_attempts = 0
    
    def add_assumption(self, assumption: str) -> Optional[HardStopTrigger]:
        """
        Record an assumption and check for overflow.
        
        Returns HardStopTrigger.ASSUMPTION_OVERFLOW if threshold exceeded.
        """
        self.assumptions.append(assumption)
        self.assumption_count += 1
        
        if self.assumption_count >= self.assumption_threshold:
            logger.warning(
                f"Assumption overflow: {self.assumption_count} assumptions. "
                f"Threshold: {self.assumption_threshold}"
            )
            return HardStopTrigger.ASSUMPTION_OVERFLOW
        
        return None
    
    def record_fix_attempt(self, fix_description: str) -> Optional[HardStopTrigger]:
        """
        Record a fix attempt and check for repeated fixes.
        
        Returns HardStopTrigger.REPEATED_FIX if same fix proposed twice.
        """
        # Normalize the fix description for comparison
        normalized = fix_description.lower().strip()
        
        if normalized in [f.lower().strip() for f in self.fix_history]:
            logger.warning(f"Repeated fix detected: {fix_description}")
            return HardStopTrigger.REPEATED_FIX
        
        self.fix_history.append(fix_description)
        return None
    
    def record_tool_failure(self, tool_name: str) -> Optional[HardStopTrigger]:
        """
        Record a tool failure and check for cascade.
        
        Returns HardStopTrigger.TOOL_FAILURE_CASCADE if threshold exceeded.
        """
        self.tool_failures[tool_name] = self.tool_failures.get(tool_name, 0) + 1
        self.consecutive_tool_failures += 1
        
        if self.consecutive_tool_failures >= self.tool_failure_threshold:
            logger.warning(
                f"Tool failure cascade: {self.consecutive_tool_failures} consecutive failures"
            )
            return HardStopTrigger.TOOL_FAILURE_CASCADE
        
        return None
    
    def record_tool_success(self, tool_name: str) -> None:
        """Record a successful tool call, resetting consecutive failure count."""
        self.consecutive_tool_failures = 0
    
    def record_failed_attempt(self) -> bool:
        """
        Record a failed attempt and check if struggle signal is needed.
        
        Returns True if a struggle signal should be sent.
        """
        self.failed_attempts += 1
        return self.failed_attempts >= self.struggle_signal_after
    
    def check_execution_fidelity(
        self,
        approved_request: ApprovalRequest,
        actual_execution: Dict[str, Any]
    ) -> Optional[HardStopTrigger]:
        """
        Check if execution matches what was approved.
        
        Returns HardStopTrigger.EXECUTION_DIVERGENCE if they don't match.
        """
        # Compare scope
        approved_scope = set(approved_request.scope.split(","))
        actual_scope = set(actual_execution.get("scope", "").split(","))
        
        if not approved_scope.issuperset(actual_scope):
            # Execution touched things not in approved scope
            logger.warning(
                f"Execution divergence: approved scope {approved_scope}, "
                f"actual scope {actual_scope}"
            )
            return HardStopTrigger.EXECUTION_DIVERGENCE
        
        return None
    
    def check_triggers(self) -> Optional[HardStopTrigger]:
        """Check all hard stop triggers and return the first one that fires."""
        # Assumption overflow
        if self.assumption_count >= self.assumption_threshold:
            return HardStopTrigger.ASSUMPTION_OVERFLOW
        
        # Tool failure cascade
        if self.consecutive_tool_failures >= self.tool_failure_threshold:
            return HardStopTrigger.TOOL_FAILURE_CASCADE
        
        return None
    
    def submit_approval_request(self, request: ApprovalRequest) -> str:
        """Submit an approval request. Returns the request ID."""
        self.pending_approvals[request.request_id] = request
        return request.request_id
    
    def approve_request(
        self,
        request_id: str,
        approved_by: str
    ) -> ApprovalRequest:
        """Approve a pending request."""
        if request_id not in self.pending_approvals:
            raise ValueError(f"Request {request_id} not found")
        
        request = self.pending_approvals.pop(request_id)
        request.status = "approved"
        request.approved_at = datetime.utcnow()
        request.approved_by = approved_by
        
        self.approved_requests[request_id] = request
        return request
    
    def reject_request(
        self,
        request_id: str,
        rejected_by: str,
        reason: str
    ) -> ApprovalRequest:
        """Reject a pending request."""
        if request_id not in self.pending_approvals:
            raise ValueError(f"Request {request_id} not found")
        
        request = self.pending_approvals.pop(request_id)
        request.status = "rejected"
        request.rejection_reason = reason
        
        return request
    
    def submit_struggle_signal(self, signal: StruggleSignal) -> None:
        """Submit a struggle signal."""
        self.struggle_signals.append(signal)
        logger.info(f"Struggle signal received from {signal.agent_role}: {signal.signal_type}")
    
    def to_prompt_section(self) -> str:
        """Generate the enforcer status section for system prompt injection."""
        triggers_status = []
        
        # Assumption count
        triggers_status.append(
            f"Assumptions: {self.assumption_count}/{self.assumption_threshold} "
            f"({'⚠️ NEAR LIMIT' if self.assumption_count >= self.assumption_threshold - 1 else '✓'})"
        )
        
        # Tool failures
        triggers_status.append(
            f"Consecutive tool failures: {self.consecutive_tool_failures}/{self.tool_failure_threshold} "
            f"({'⚠️ NEAR LIMIT' if self.consecutive_tool_failures >= self.tool_failure_threshold - 1 else '✓'})"
        )
        
        # Failed attempts
        triggers_status.append(
            f"Failed attempts: {self.failed_attempts} "
            f"({'⚠️ SIGNAL STRUGGLE' if self.failed_attempts >= self.struggle_signal_after else '✓'})"
        )
        
        return f"""### Hard Stop Triggers
If any trigger fires, STOP and signal immediately:
{chr(10).join(['- ' + s for s in triggers_status])}

### Struggle Protocol
If stuck after {self.struggle_signal_after} attempts, use this format:
🚨 SYNC NEEDED — [signal type]
What I understand: ...
What I've tried: ...
Where I'm stuck: ...
What would help: ...
"""
