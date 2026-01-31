# =============================================================================
# State Machine with Forbidden Transitions
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
#
# "LLMs are bad at temporal discipline. They skip steps, jump ahead, declare
# victory prematurely. The state machine gives them anchors—they know where
# they are, what's required to move forward, and what's forbidden."
# =============================================================================
"""State machine implementation for agent behavioral contracts."""

from enum import Enum
from typing import Dict, List, Optional, Set, Tuple
from pydantic import BaseModel, Field
from datetime import datetime


class AgentState(str, Enum):
    """
    Discrete states an agent can be in.
    
    State transitions are explicit and some are forbidden.
    This prevents agents from skipping steps or declaring victory prematurely.
    """
    IDLE = "idle"
    ANALYSIS = "analysis"
    APPROVAL_PENDING = "approval_pending"
    EXECUTION = "execution"
    VALIDATION = "validation"
    DONE = "done"
    BLOCKED = "blocked"
    RESET = "reset"


class ForbiddenTransition(Exception):
    """Raised when an agent attempts a forbidden state transition."""
    
    def __init__(self, from_state: AgentState, to_state: AgentState, reason: str):
        self.from_state = from_state
        self.to_state = to_state
        self.reason = reason
        super().__init__(f"Forbidden transition: {from_state} → {to_state}. {reason}")


class TransitionGate(str, Enum):
    """Mental model gates that must pass before a transition is allowed."""
    DEFINITION_OF_READY = "definition_of_ready"
    DEFINITION_OF_DONE = "definition_of_done"
    APPROVAL_RECEIVED = "approval_received"
    VALIDATION_PASSED = "validation_passed"


class StateTransition(BaseModel):
    """Record of a state transition."""
    from_state: AgentState
    to_state: AgentState
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    gate_checked: Optional[TransitionGate] = None
    gate_passed: bool = True
    agent_role: str
    session_id: str


class AgentContract:
    """
    Behavioral contract enforcing state machine transitions.
    
    From the article:
    - ANALYSIS → EXECUTION is forbidden (must get approval)
    - EXECUTION → DONE is forbidden (must validate)
    - APPROVAL_PENDING → DONE is forbidden (must execute)
    """
    
    # Forbidden transitions - these are structural impossibilities, not warnings
    FORBIDDEN_TRANSITIONS: Set[Tuple[AgentState, AgentState]] = {
        (AgentState.ANALYSIS, AgentState.EXECUTION),      # Must get approval first
        (AgentState.ANALYSIS, AgentState.DONE),           # Can't skip to done
        (AgentState.EXECUTION, AgentState.DONE),          # Must validate first
        (AgentState.APPROVAL_PENDING, AgentState.DONE),   # Must execute first
        (AgentState.IDLE, AgentState.EXECUTION),          # Must analyze first
        (AgentState.IDLE, AgentState.DONE),               # Can't skip everything
    }
    
    # Gates required at specific transitions
    TRANSITION_GATES: Dict[Tuple[AgentState, AgentState], TransitionGate] = {
        (AgentState.ANALYSIS, AgentState.APPROVAL_PENDING): TransitionGate.DEFINITION_OF_READY,
        (AgentState.APPROVAL_PENDING, AgentState.EXECUTION): TransitionGate.APPROVAL_RECEIVED,
        (AgentState.EXECUTION, AgentState.VALIDATION): TransitionGate.DEFINITION_OF_DONE,
        (AgentState.VALIDATION, AgentState.DONE): TransitionGate.VALIDATION_PASSED,
    }
    
    # Valid transitions (explicit allowlist)
    VALID_TRANSITIONS: Set[Tuple[AgentState, AgentState]] = {
        (AgentState.IDLE, AgentState.ANALYSIS),
        (AgentState.ANALYSIS, AgentState.APPROVAL_PENDING),
        (AgentState.ANALYSIS, AgentState.BLOCKED),
        (AgentState.APPROVAL_PENDING, AgentState.EXECUTION),
        (AgentState.APPROVAL_PENDING, AgentState.ANALYSIS),  # Rejection → re-analyze
        (AgentState.EXECUTION, AgentState.VALIDATION),
        (AgentState.EXECUTION, AgentState.BLOCKED),
        (AgentState.VALIDATION, AgentState.DONE),
        (AgentState.VALIDATION, AgentState.EXECUTION),       # Failed validation → fix
        (AgentState.BLOCKED, AgentState.ANALYSIS),           # Unblocked → re-analyze
        (AgentState.BLOCKED, AgentState.RESET),              # Give up → reset
        (AgentState.DONE, AgentState.IDLE),                  # Ready for next task
        # Reset can go back to idle from any state
        (AgentState.RESET, AgentState.IDLE),
    }
    
    def __init__(self, agent_role: str, session_id: str):
        self.agent_role = agent_role
        self.session_id = session_id
        self._current_state = AgentState.IDLE
        self._transition_history: List[StateTransition] = []
        self._gate_results: Dict[TransitionGate, bool] = {}
    
    @property
    def current_state(self) -> AgentState:
        """Get the current state."""
        return self._current_state
    
    @property
    def transition_history(self) -> List[StateTransition]:
        """Get the transition history."""
        return self._transition_history.copy()
    
    def get_allowed_transitions(self) -> List[AgentState]:
        """Get the list of states we can transition to from the current state."""
        allowed = []
        for from_state, to_state in self.VALID_TRANSITIONS:
            if from_state == self._current_state:
                allowed.append(to_state)
        return allowed
    
    def is_transition_allowed(self, to_state: AgentState) -> bool:
        """Check if a transition to the given state is allowed."""
        return (self._current_state, to_state) in self.VALID_TRANSITIONS
    
    def is_transition_forbidden(self, to_state: AgentState) -> bool:
        """Check if a transition to the given state is forbidden."""
        return (self._current_state, to_state) in self.FORBIDDEN_TRANSITIONS
    
    def get_required_gate(self, to_state: AgentState) -> Optional[TransitionGate]:
        """Get the gate required for a transition, if any."""
        return self.TRANSITION_GATES.get((self._current_state, to_state))
    
    def set_gate_result(self, gate: TransitionGate, passed: bool) -> None:
        """Record the result of a gate check."""
        self._gate_results[gate] = passed
    
    def check_gate(self, gate: TransitionGate) -> bool:
        """Check if a gate has passed."""
        return self._gate_results.get(gate, False)
    
    def transition_to(self, to_state: AgentState) -> StateTransition:
        """
        Attempt to transition to a new state.
        
        Raises:
            ForbiddenTransition: If the transition is forbidden
            ValueError: If the transition is not in the valid set
        """
        # Check for forbidden transitions first
        if self.is_transition_forbidden(to_state):
            raise ForbiddenTransition(
                from_state=self._current_state,
                to_state=to_state,
                reason=self._get_forbidden_reason(to_state)
            )
        
        # Check if transition is valid
        if not self.is_transition_allowed(to_state):
            raise ValueError(
                f"Invalid transition: {self._current_state} → {to_state}. "
                f"Allowed: {self.get_allowed_transitions()}"
            )
        
        # Check gate if required
        required_gate = self.get_required_gate(to_state)
        gate_passed = True
        if required_gate:
            gate_passed = self.check_gate(required_gate)
            if not gate_passed:
                raise ValueError(
                    f"Gate not passed: {required_gate.value}. "
                    f"Cannot transition from {self._current_state} to {to_state}."
                )
        
        # Record the transition
        transition = StateTransition(
            from_state=self._current_state,
            to_state=to_state,
            agent_role=self.agent_role,
            session_id=self.session_id,
            gate_checked=required_gate,
            gate_passed=gate_passed
        )
        self._transition_history.append(transition)
        
        # Update state
        self._current_state = to_state
        
        # Clear gate results after successful transition
        self._gate_results.clear()
        
        return transition
    
    def force_reset(self) -> StateTransition:
        """Force a reset to IDLE state. Used after violations."""
        transition = StateTransition(
            from_state=self._current_state,
            to_state=AgentState.RESET,
            agent_role=self.agent_role,
            session_id=self.session_id
        )
        self._transition_history.append(transition)
        self._current_state = AgentState.RESET
        self._gate_results.clear()
        
        # Then transition to IDLE
        return self.transition_to(AgentState.IDLE)
    
    def _get_forbidden_reason(self, to_state: AgentState) -> str:
        """Get the reason why a transition is forbidden."""
        reasons = {
            (AgentState.ANALYSIS, AgentState.EXECUTION): 
                "Must get approval before execution. Submit approval request first.",
            (AgentState.ANALYSIS, AgentState.DONE):
                "Cannot skip from analysis to done. Must go through approval → execution → validation.",
            (AgentState.EXECUTION, AgentState.DONE):
                "Must validate before declaring done. Run validation first.",
            (AgentState.APPROVAL_PENDING, AgentState.DONE):
                "Cannot skip from approval to done. Must execute and validate first.",
            (AgentState.IDLE, AgentState.EXECUTION):
                "Cannot execute without analysis. Analyze the task first.",
            (AgentState.IDLE, AgentState.DONE):
                "Cannot declare done without doing any work.",
        }
        return reasons.get(
            (self._current_state, to_state),
            "Transition not allowed by contract."
        )
    
    def to_prompt_section(self) -> str:
        """Generate the state machine section for system prompt injection."""
        allowed = ", ".join([s.value for s in self.get_allowed_transitions()])
        return f"""### State Machine
Current State: {self._current_state.value}
Allowed Transitions: [{allowed}]

FORBIDDEN (will trigger violation):
- Cannot skip approval (ANALYSIS → EXECUTION)
- Cannot skip validation (EXECUTION → DONE)
- Cannot skip execution (APPROVAL_PENDING → DONE)
"""
