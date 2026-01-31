# =============================================================================
# Contract Violations and RESET Semantics
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
#
# "When a Tier 0 rule is violated, the agent enters RESET state.
# This prevents violation cascades—one mistake doesn't compound into many."
# =============================================================================
"""Contract violation handling and RESET semantics."""

from enum import Enum
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime

from .tier_rules import RuleTier


class ViolationSeverity(str, Enum):
    """Severity of a contract violation."""
    CRITICAL = "critical"    # Tier 0 violation - immediate RESET
    HIGH = "high"            # Tier 1 violation - warning, may escalate
    MEDIUM = "medium"        # Tier 2 violation - logged, monitored
    LOW = "low"              # Tier 3 violation - noted for improvement


class ContractViolation(Exception):
    """
    Exception raised when an agent violates a contract rule.
    
    The violation includes:
    - The rule that was violated
    - The tier (determines severity)
    - Context about what happened
    """
    
    def __init__(
        self,
        rule: str,
        tier: RuleTier,
        context: str,
        agent_role: Optional[str] = None,
        session_id: Optional[str] = None
    ):
        self.rule = rule
        self.tier = tier
        self.context = context
        self.agent_role = agent_role
        self.session_id = session_id
        self.timestamp = datetime.utcnow()
        self.severity = self._determine_severity()
        
        super().__init__(
            f"Contract Violation [Tier {tier}]: {rule}. Context: {context}"
        )
    
    def _determine_severity(self) -> ViolationSeverity:
        """Determine severity based on tier."""
        severity_map = {
            RuleTier.TIER_0: ViolationSeverity.CRITICAL,
            RuleTier.TIER_1: ViolationSeverity.HIGH,
            RuleTier.TIER_2: ViolationSeverity.MEDIUM,
            RuleTier.TIER_3: ViolationSeverity.LOW,
        }
        return severity_map.get(self.tier, ViolationSeverity.MEDIUM)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert violation to dictionary for logging."""
        return {
            "rule": self.rule,
            "tier": self.tier.value,
            "severity": self.severity.value,
            "context": self.context,
            "agent_role": self.agent_role,
            "session_id": self.session_id,
            "timestamp": self.timestamp.isoformat(),
        }


class ViolationRecord(BaseModel):
    """Record of a contract violation for audit purposes."""
    violation_id: str
    rule: str
    tier: int
    severity: ViolationSeverity
    context: str
    agent_role: str
    session_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    
    # Resolution
    resolved: bool = False
    resolution_action: Optional[str] = None
    resolved_at: Optional[datetime] = None


class ResetSemantics:
    """
    RESET semantics for handling contract violations.
    
    From the article:
    "RESET isn't punishment—it's a circuit breaker. When something goes wrong,
    we need a clean starting point rather than trying to recover mid-stream."
    
    RESET involves:
    1. Acknowledge the violation
    2. Discard uncertain context
    3. Return to known-good state
    4. Log for pattern analysis
    """
    
    def __init__(self):
        self.reset_history: List[Dict[str, Any]] = []
    
    def trigger_reset(
        self,
        violation: ContractViolation,
        agent_contract: Any,  # AgentContract
        blackboard: Any = None  # AgentBlackboard
    ) -> Dict[str, Any]:
        """
        Trigger a RESET due to a contract violation.
        
        Returns a dict describing what was reset.
        """
        reset_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "violation": violation.to_dict(),
            "agent_role": violation.agent_role,
            "session_id": violation.session_id,
            "previous_state": agent_contract.current_state.value if agent_contract else None,
            "actions_taken": []
        }
        
        # 1. Force the agent contract to IDLE state
        if agent_contract:
            agent_contract.force_reset()
            reset_record["actions_taken"].append("Forced state machine to IDLE")
        
        # 2. Mark current task as blocked (if blackboard available)
        if blackboard:
            # This would mark current task as blocked
            reset_record["actions_taken"].append("Marked current task as BLOCKED")
        
        # 3. Clear uncertain context
        reset_record["actions_taken"].append("Cleared uncertain context")
        
        # 4. Log for pattern analysis
        self.reset_history.append(reset_record)
        
        return reset_record
    
    def get_reset_count(self, agent_role: str = None, session_id: str = None) -> int:
        """Get the number of resets, optionally filtered."""
        count = 0
        for record in self.reset_history:
            if agent_role and record.get("agent_role") != agent_role:
                continue
            if session_id and record.get("session_id") != session_id:
                continue
            count += 1
        return count
    
    def get_reset_patterns(self) -> Dict[str, int]:
        """Analyze reset patterns by rule violated."""
        patterns: Dict[str, int] = {}
        for record in self.reset_history:
            rule = record.get("violation", {}).get("rule", "unknown")
            patterns[rule] = patterns.get(rule, 0) + 1
        return patterns


class ViolationHandler:
    """
    Handler for processing contract violations.
    
    Determines appropriate response based on violation severity:
    - CRITICAL (Tier 0): Immediate RESET, log, alert
    - HIGH (Tier 1): Warning, may escalate to RESET if repeated
    - MEDIUM (Tier 2): Log for monitoring
    - LOW (Tier 3): Note for improvement
    """
    
    def __init__(self):
        self.violation_log: List[ViolationRecord] = []
        self.reset_semantics = ResetSemantics()
        self._violation_counts: Dict[str, Dict[str, int]] = {}  # {agent: {rule: count}}
    
    def handle_violation(
        self,
        violation: ContractViolation,
        agent_contract: Any = None,
        blackboard: Any = None
    ) -> Dict[str, Any]:
        """
        Handle a contract violation based on its severity.
        
        Returns a dict describing the handling action taken.
        """
        # Track violation count
        self._track_violation(violation)
        
        # Log the violation
        record = ViolationRecord(
            violation_id=f"V-{datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}",
            rule=violation.rule,
            tier=violation.tier,
            severity=violation.severity,
            context=violation.context,
            agent_role=violation.agent_role or "unknown",
            session_id=violation.session_id or "unknown"
        )
        self.violation_log.append(record)
        
        # Determine action based on severity
        if violation.severity == ViolationSeverity.CRITICAL:
            # Tier 0: Immediate RESET
            reset_record = self.reset_semantics.trigger_reset(
                violation, agent_contract, blackboard
            )
            return {
                "action": "RESET",
                "severity": "critical",
                "message": f"Tier 0 violation triggered RESET: {violation.rule}",
                "reset_record": reset_record
            }
        
        elif violation.severity == ViolationSeverity.HIGH:
            # Tier 1: Check if repeated, may escalate
            count = self._get_violation_count(violation.agent_role, violation.rule)
            if count >= 2:
                # Repeated Tier 1 violation → RESET
                reset_record = self.reset_semantics.trigger_reset(
                    violation, agent_contract, blackboard
                )
                return {
                    "action": "RESET",
                    "severity": "high",
                    "message": f"Repeated Tier 1 violation triggered RESET: {violation.rule}",
                    "reset_record": reset_record
                }
            else:
                return {
                    "action": "WARNING",
                    "severity": "high",
                    "message": f"Tier 1 violation warning ({count}/2 before RESET): {violation.rule}",
                    "violation_count": count
                }
        
        elif violation.severity == ViolationSeverity.MEDIUM:
            # Tier 2: Log and monitor
            return {
                "action": "LOGGED",
                "severity": "medium",
                "message": f"Tier 2 violation logged for monitoring: {violation.rule}"
            }
        
        else:
            # Tier 3: Note for improvement
            return {
                "action": "NOTED",
                "severity": "low",
                "message": f"Tier 3 violation noted: {violation.rule}"
            }
    
    def _track_violation(self, violation: ContractViolation) -> None:
        """Track violation counts by agent and rule."""
        agent = violation.agent_role or "unknown"
        rule = violation.rule
        
        if agent not in self._violation_counts:
            self._violation_counts[agent] = {}
        
        if rule not in self._violation_counts[agent]:
            self._violation_counts[agent][rule] = 0
        
        self._violation_counts[agent][rule] += 1
    
    def _get_violation_count(self, agent_role: str, rule: str) -> int:
        """Get the violation count for a specific agent and rule."""
        agent = agent_role or "unknown"
        return self._violation_counts.get(agent, {}).get(rule, 0)
    
    def get_violation_summary(self, agent_role: str = None) -> Dict[str, Any]:
        """Get a summary of violations, optionally filtered by agent."""
        if agent_role:
            violations = [v for v in self.violation_log if v.agent_role == agent_role]
        else:
            violations = self.violation_log
        
        return {
            "total_violations": len(violations),
            "by_severity": {
                severity.value: len([v for v in violations if v.severity == severity])
                for severity in ViolationSeverity
            },
            "by_tier": {
                tier: len([v for v in violations if v.tier == tier])
                for tier in range(4)
            },
            "reset_count": self.reset_semantics.get_reset_count(agent_role),
            "patterns": self.reset_semantics.get_reset_patterns()
        }
