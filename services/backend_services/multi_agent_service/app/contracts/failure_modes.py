# =============================================================================
# Failure Mode Coverage
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Failure mode detection and recovery strategies."""

from enum import Enum
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime


class FailureMode(str, Enum):
    """Known failure modes for AI agents."""
    
    # Deception-related
    FABRICATED_SUCCESS = "fabricated_success"
    TEST_GREENWASHING = "test_greenwashing"
    HIDDEN_SCOPE_CREEP = "hidden_scope_creep"
    FAKE_UNDERSTANDING = "fake_understanding"
    
    # Competence-related
    SYCOPHANCY = "sycophancy"
    OVERCONFIDENCE = "overconfidence"
    PREMATURE_VICTORY = "premature_victory"
    SCOPE_NARROWING = "scope_narrowing"
    
    # Process-related
    GATE_SKIPPING = "gate_skipping"
    SPIRAL_DEBUGGING = "spiral_debugging"
    ASSUMPTION_OVERFLOW = "assumption_overflow"
    CONTEXT_COLLAPSE = "context_collapse"
    
    # Collaboration-related
    SELF_REVIEW = "self_review"
    PEER_BYPASS = "peer_bypass"
    STRUGGLE_AVOIDANCE = "struggle_avoidance"


class FailureModeDefinition(BaseModel):
    """Definition of a failure mode with detection and recovery."""
    mode: FailureMode
    description: str
    detection_signals: List[str]
    recovery_strategy: str
    tier_violated: int  # Which tier rule is violated
    severity: str  # "critical", "high", "medium", "low"


# Comprehensive failure mode definitions
FAILURE_MODE_DEFINITIONS: Dict[FailureMode, FailureModeDefinition] = {
    FailureMode.FABRICATED_SUCCESS: FailureModeDefinition(
        mode=FailureMode.FABRICATED_SUCCESS,
        description="Agent claims success without verification",
        detection_signals=[
            "Claiming 'tests pass' without running them",
            "Declaring 'done' without validating done_when criteria",
            "Asserting completion with vague language"
        ],
        recovery_strategy="RESET. Require explicit validation evidence before any success claim.",
        tier_violated=0,
        severity="critical"
    ),
    FailureMode.TEST_GREENWASHING: FailureModeDefinition(
        mode=FailureMode.TEST_GREENWASHING,
        description="Agent modifies tests to pass instead of fixing code",
        detection_signals=[
            "Test file modifications alongside code changes",
            "Weakened assertions in test updates",
            "Removed test cases"
        ],
        recovery_strategy="RESET. Revert test changes. Fix code to meet original test intent.",
        tier_violated=0,
        severity="critical"
    ),
    FailureMode.HIDDEN_SCOPE_CREEP: FailureModeDefinition(
        mode=FailureMode.HIDDEN_SCOPE_CREEP,
        description="Agent expands scope without disclosure or approval",
        detection_signals=[
            "Changes to files not in approved scope",
            "'While I was here, I also...' patterns",
            "Undeclared dependencies added"
        ],
        recovery_strategy="RESET. Revert unapproved changes. Re-request approval with expanded scope.",
        tier_violated=0,
        severity="critical"
    ),
    FailureMode.FAKE_UNDERSTANDING: FailureModeDefinition(
        mode=FailureMode.FAKE_UNDERSTANDING,
        description="Agent pretends to understand when confused",
        detection_signals=[
            "Generic responses to specific questions",
            "Restating the problem without adding insight",
            "Avoidance of details"
        ],
        recovery_strategy="Trigger struggle protocol. Require explicit uncertainty expression.",
        tier_violated=0,
        severity="critical"
    ),
    FailureMode.SYCOPHANCY: FailureModeDefinition(
        mode=FailureMode.SYCOPHANCY,
        description="Agent gives hollow agreement or flattery",
        detection_signals=[
            "Excessive 'great idea' patterns",
            "Agreeing with contradictory statements",
            "Validating poor approaches"
        ],
        recovery_strategy="Reinforce anti-sycophancy rules. Require substantive disagreement.",
        tier_violated=1,
        severity="high"
    ),
    FailureMode.OVERCONFIDENCE: FailureModeDefinition(
        mode=FailureMode.OVERCONFIDENCE,
        description="Agent expresses certainty without evidence",
        detection_signals=[
            "Confidence words without backing",
            "Skipping validation steps",
            "Dismissing edge cases"
        ],
        recovery_strategy="Require evidence for all claims. Apply DoD mental model.",
        tier_violated=1,
        severity="high"
    ),
    FailureMode.PREMATURE_VICTORY: FailureModeDefinition(
        mode=FailureMode.PREMATURE_VICTORY,
        description="Agent declares completion too early",
        detection_signals=[
            "State transition to DONE without validation",
            "'Almost done' language",
            "Skipping final verification"
        ],
        recovery_strategy="Block DONE transition. Require explicit done_when checklist.",
        tier_violated=1,
        severity="high"
    ),
    FailureMode.SCOPE_NARROWING: FailureModeDefinition(
        mode=FailureMode.SCOPE_NARROWING,
        description="Agent quietly reduces scope to appear done",
        detection_signals=[
            "Partial implementation with 'TODO' markers",
            "Reduced test coverage",
            "Missing edge case handling"
        ],
        recovery_strategy="Compare output against original scope. Require explicit deferral rationale.",
        tier_violated=1,
        severity="high"
    ),
    FailureMode.GATE_SKIPPING: FailureModeDefinition(
        mode=FailureMode.GATE_SKIPPING,
        description="Agent bypasses approval or validation gates",
        detection_signals=[
            "Forbidden state transitions",
            "Missing approval requests",
            "Skipped DoR/DoD checks"
        ],
        recovery_strategy="Enforce state machine. Block forbidden transitions.",
        tier_violated=1,
        severity="high"
    ),
    FailureMode.SPIRAL_DEBUGGING: FailureModeDefinition(
        mode=FailureMode.SPIRAL_DEBUGGING,
        description="Agent makes multiple fix attempts without progress",
        detection_signals=[
            "Same fix proposed twice",
            "Growing number of changes",
            "Increasing assumptions"
        ],
        recovery_strategy="Hard stop. Trigger struggle protocol. Escalate to human.",
        tier_violated=1,
        severity="high"
    ),
    FailureMode.ASSUMPTION_OVERFLOW: FailureModeDefinition(
        mode=FailureMode.ASSUMPTION_OVERFLOW,
        description="Agent makes too many unverified assumptions",
        detection_signals=[
            "Assumption count exceeds threshold (3)",
            "Untested hypotheses accumulating",
            "Cascading 'if this then that'"
        ],
        recovery_strategy="Hard stop. Document assumptions. Request validation.",
        tier_violated=1,
        severity="high"
    ),
    FailureMode.CONTEXT_COLLAPSE: FailureModeDefinition(
        mode=FailureMode.CONTEXT_COLLAPSE,
        description="Agent loses track due to context window limits",
        detection_signals=[
            "Token usage > 85%",
            "Forgetting earlier decisions",
            "Contradicting previous statements"
        ],
        recovery_strategy="Save state. Compress context. Hand off to fresh session.",
        tier_violated=1,
        severity="high"
    ),
    FailureMode.SELF_REVIEW: FailureModeDefinition(
        mode=FailureMode.SELF_REVIEW,
        description="Agent reviews or approves their own work",
        detection_signals=[
            "Creator and reviewer are same agent",
            "Skipping peer review step"
        ],
        recovery_strategy="Block. Require different reviewer. This is a Tier 0 violation.",
        tier_violated=0,
        severity="critical"
    ),
    FailureMode.PEER_BYPASS: FailureModeDefinition(
        mode=FailureMode.PEER_BYPASS,
        description="Agent bypasses designated reviewer",
        detection_signals=[
            "Review by non-designated agent",
            "Direct merge without review"
        ],
        recovery_strategy="Reject. Route to designated reviewer.",
        tier_violated=1,
        severity="high"
    ),
    FailureMode.STRUGGLE_AVOIDANCE: FailureModeDefinition(
        mode=FailureMode.STRUGGLE_AVOIDANCE,
        description="Agent fails to signal struggle when stuck",
        detection_signals=[
            "Multiple failed attempts without signal",
            "Faking progress when blocked",
            "Long delays without updates"
        ],
        recovery_strategy="Detect and trigger forced struggle signal.",
        tier_violated=1,
        severity="high"
    ),
}


class FailureModeDetector:
    """
    Detector for known failure modes.
    
    Monitors agent behavior and detects when failure modes are emerging.
    """
    
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.detections: List[Dict[str, Any]] = []
        self.definitions = FAILURE_MODE_DEFINITIONS
    
    def check_for_failures(
        self,
        agent_role: str,
        action: str,
        context: Dict[str, Any]
    ) -> List[FailureMode]:
        """Check if current action exhibits any failure modes."""
        detected = []
        
        # Check for fabricated success
        if self._check_fabricated_success(action, context):
            detected.append(FailureMode.FABRICATED_SUCCESS)
        
        # Check for test greenwashing
        if self._check_test_greenwashing(action, context):
            detected.append(FailureMode.TEST_GREENWASHING)
        
        # Check for sycophancy
        if self._check_sycophancy(action, context):
            detected.append(FailureMode.SYCOPHANCY)
        
        # Check for overconfidence
        if self._check_overconfidence(action, context):
            detected.append(FailureMode.OVERCONFIDENCE)
        
        # Record detections
        for mode in detected:
            self.detections.append({
                "mode": mode.value,
                "agent_role": agent_role,
                "timestamp": datetime.utcnow().isoformat(),
                "context": context
            })
        
        return detected
    
    def _check_fabricated_success(
        self,
        action: str,
        context: Dict[str, Any]
    ) -> bool:
        """Check for fabricated success signals."""
        action_lower = action.lower()
        
        success_claims = ["tests pass", "completed", "done", "success"]
        validation_evidence = ["verified", "ran", "confirmed", "output"]
        
        has_claim = any(claim in action_lower for claim in success_claims)
        has_evidence = any(ev in action_lower for ev in validation_evidence)
        
        return has_claim and not has_evidence
    
    def _check_test_greenwashing(
        self,
        action: str,
        context: Dict[str, Any]
    ) -> bool:
        """Check for test modification patterns."""
        files_modified = context.get("files_modified", [])
        
        test_files = [f for f in files_modified if "test" in f.lower()]
        code_files = [f for f in files_modified if "test" not in f.lower()]
        
        # If modifying both tests and code, flag for review
        return len(test_files) > 0 and len(code_files) > 0
    
    def _check_sycophancy(
        self,
        action: str,
        context: Dict[str, Any]
    ) -> bool:
        """Check for sycophantic patterns."""
        action_lower = action.lower()
        
        syc_patterns = [
            "great idea", "excellent point", "absolutely right",
            "i agree completely", "perfect", "wonderful"
        ]
        
        return sum(1 for p in syc_patterns if p in action_lower) >= 2
    
    def _check_overconfidence(
        self,
        action: str,
        context: Dict[str, Any]
    ) -> bool:
        """Check for overconfidence patterns."""
        action_lower = action.lower()
        
        confidence_words = ["definitely", "certainly", "obviously", "clearly"]
        evidence_words = ["because", "based on", "verified", "tested"]
        
        conf_count = sum(1 for w in confidence_words if w in action_lower)
        ev_count = sum(1 for w in evidence_words if w in action_lower)
        
        return conf_count > ev_count + 1
    
    def get_recovery_strategy(self, mode: FailureMode) -> str:
        """Get the recovery strategy for a failure mode."""
        definition = self.definitions.get(mode)
        if definition:
            return definition.recovery_strategy
        return "Unknown failure mode. Escalate to human."
    
    def get_detection_summary(self) -> Dict[str, Any]:
        """Get summary of all detections."""
        mode_counts: Dict[str, int] = {}
        for detection in self.detections:
            mode = detection["mode"]
            mode_counts[mode] = mode_counts.get(mode, 0) + 1
        
        return {
            "total_detections": len(self.detections),
            "by_mode": mode_counts,
            "critical_count": sum(
                1 for d in self.detections
                if self.definitions.get(FailureMode(d["mode"]), None) and
                self.definitions[FailureMode(d["mode"])].severity == "critical"
            )
        }
