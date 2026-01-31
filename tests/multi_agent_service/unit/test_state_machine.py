# =============================================================================
# State Machine Tests
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Tests for state machine transitions and forbidden paths."""

import pytest
from enum import Enum


class AgentState(str, Enum):
    """Agent states for testing."""
    IDLE = "idle"
    ANALYSIS = "analysis"
    APPROVAL_PENDING = "approval_pending"
    EXECUTION = "execution"
    VALIDATION = "validation"
    DONE = "done"
    BLOCKED = "blocked"


FORBIDDEN_TRANSITIONS = {
    (AgentState.ANALYSIS, AgentState.EXECUTION),
    (AgentState.ANALYSIS, AgentState.DONE),
    (AgentState.EXECUTION, AgentState.DONE),
    (AgentState.APPROVAL_PENDING, AgentState.DONE),
    (AgentState.IDLE, AgentState.EXECUTION),
    (AgentState.IDLE, AgentState.DONE),
}

VALID_TRANSITIONS = {
    (AgentState.IDLE, AgentState.ANALYSIS),
    (AgentState.ANALYSIS, AgentState.APPROVAL_PENDING),
    (AgentState.ANALYSIS, AgentState.BLOCKED),
    (AgentState.APPROVAL_PENDING, AgentState.EXECUTION),
    (AgentState.APPROVAL_PENDING, AgentState.ANALYSIS),
    (AgentState.EXECUTION, AgentState.VALIDATION),
    (AgentState.EXECUTION, AgentState.BLOCKED),
    (AgentState.VALIDATION, AgentState.DONE),
    (AgentState.VALIDATION, AgentState.EXECUTION),
    (AgentState.BLOCKED, AgentState.ANALYSIS),
    (AgentState.DONE, AgentState.IDLE),
}


class MockAgentContract:
    """Mock contract for testing state machine."""
    
    def __init__(self, agent_role: str, session_id: str):
        self.agent_role = agent_role
        self.session_id = session_id
        self.state = AgentState.IDLE
        self._transition_history = []
    
    def can_transition_to(self, target_state: AgentState) -> bool:
        """Check if transition is valid."""
        return (self.state, target_state) in VALID_TRANSITIONS
    
    def is_transition_forbidden(self, target_state: AgentState) -> bool:
        """Check if transition is forbidden."""
        return (self.state, target_state) in FORBIDDEN_TRANSITIONS
    
    async def transition_to(self, target_state: AgentState) -> bool:
        """Attempt state transition."""
        if self.is_transition_forbidden(target_state):
            raise ValueError(
                f"Forbidden transition: {self.state.value} → {target_state.value}"
            )
        
        if not self.can_transition_to(target_state):
            raise ValueError(
                f"Invalid transition: {self.state.value} → {target_state.value}"
            )
        
        self._transition_history.append((self.state, target_state))
        self.state = target_state
        return True


class TestForbiddenTransitions:
    """Verify forbidden transitions are blocked."""
    
    @pytest.mark.parametrize("from_state,to_state", [
        (AgentState.ANALYSIS, AgentState.EXECUTION),
        (AgentState.EXECUTION, AgentState.DONE),
        (AgentState.IDLE, AgentState.DONE),
        (AgentState.IDLE, AgentState.EXECUTION),
        (AgentState.APPROVAL_PENDING, AgentState.DONE),
    ])
    @pytest.mark.asyncio
    async def test_forbidden_transition_blocked(self, from_state, to_state):
        """Test that forbidden transitions raise ValueError."""
        contract = MockAgentContract("test_agent", "session_1")
        contract.state = from_state
        
        with pytest.raises(ValueError, match="Forbidden transition"):
            await contract.transition_to(to_state)
    
    @pytest.mark.asyncio
    async def test_analysis_to_execution_forbidden(self):
        """Test that skipping approval is forbidden."""
        contract = MockAgentContract("developer", "session_1")
        contract.state = AgentState.ANALYSIS
        
        with pytest.raises(ValueError):
            await contract.transition_to(AgentState.EXECUTION)
    
    @pytest.mark.asyncio
    async def test_execution_to_done_forbidden(self):
        """Test that skipping validation is forbidden."""
        contract = MockAgentContract("developer", "session_1")
        contract.state = AgentState.EXECUTION
        
        with pytest.raises(ValueError):
            await contract.transition_to(AgentState.DONE)


class TestValidTransitions:
    """Verify valid transitions are allowed."""
    
    @pytest.mark.asyncio
    async def test_idle_to_analysis_allowed(self):
        """Test starting analysis from idle."""
        contract = MockAgentContract("test_agent", "session_1")
        
        result = await contract.transition_to(AgentState.ANALYSIS)
        
        assert result is True
        assert contract.state == AgentState.ANALYSIS
    
    @pytest.mark.asyncio
    async def test_analysis_to_approval_pending_allowed(self):
        """Test requesting approval after analysis."""
        contract = MockAgentContract("test_agent", "session_1")
        contract.state = AgentState.ANALYSIS
        
        result = await contract.transition_to(AgentState.APPROVAL_PENDING)
        
        assert result is True
        assert contract.state == AgentState.APPROVAL_PENDING
    
    @pytest.mark.asyncio
    async def test_approval_to_execution_allowed(self):
        """Test executing after approval."""
        contract = MockAgentContract("test_agent", "session_1")
        contract.state = AgentState.APPROVAL_PENDING
        
        result = await contract.transition_to(AgentState.EXECUTION)
        
        assert result is True
        assert contract.state == AgentState.EXECUTION
    
    @pytest.mark.asyncio
    async def test_execution_to_validation_allowed(self):
        """Test validating after execution."""
        contract = MockAgentContract("test_agent", "session_1")
        contract.state = AgentState.EXECUTION
        
        result = await contract.transition_to(AgentState.VALIDATION)
        
        assert result is True
        assert contract.state == AgentState.VALIDATION
    
    @pytest.mark.asyncio
    async def test_validation_to_done_allowed(self):
        """Test completing after validation."""
        contract = MockAgentContract("test_agent", "session_1")
        contract.state = AgentState.VALIDATION
        
        result = await contract.transition_to(AgentState.DONE)
        
        assert result is True
        assert contract.state == AgentState.DONE
    
    @pytest.mark.asyncio
    async def test_full_happy_path(self):
        """Test complete valid workflow."""
        contract = MockAgentContract("developer", "session_1")
        
        await contract.transition_to(AgentState.ANALYSIS)
        await contract.transition_to(AgentState.APPROVAL_PENDING)
        await contract.transition_to(AgentState.EXECUTION)
        await contract.transition_to(AgentState.VALIDATION)
        await contract.transition_to(AgentState.DONE)
        
        assert contract.state == AgentState.DONE
        assert len(contract._transition_history) == 5


class TestBlockedState:
    """Test blocked state transitions."""
    
    @pytest.mark.asyncio
    async def test_analysis_to_blocked_allowed(self):
        """Test blocking during analysis."""
        contract = MockAgentContract("test_agent", "session_1")
        contract.state = AgentState.ANALYSIS
        
        result = await contract.transition_to(AgentState.BLOCKED)
        
        assert result is True
        assert contract.state == AgentState.BLOCKED
    
    @pytest.mark.asyncio
    async def test_execution_to_blocked_allowed(self):
        """Test blocking during execution."""
        contract = MockAgentContract("test_agent", "session_1")
        contract.state = AgentState.EXECUTION
        
        result = await contract.transition_to(AgentState.BLOCKED)
        
        assert result is True
        assert contract.state == AgentState.BLOCKED
    
    @pytest.mark.asyncio
    async def test_blocked_to_analysis_allowed(self):
        """Test resuming from blocked state."""
        contract = MockAgentContract("test_agent", "session_1")
        contract.state = AgentState.BLOCKED
        
        result = await contract.transition_to(AgentState.ANALYSIS)
        
        assert result is True
        assert contract.state == AgentState.ANALYSIS
