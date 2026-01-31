# =============================================================================
# Contract Adapter Unit Tests
# =============================================================================
"""
Unit tests for the ContractAdapter class.

Tests cover:
- State transitions (valid and forbidden)
- Assumption overflow detection
- Failed attempt tracking
- Repeated fix detection
- Approval requests and struggle signals
"""

import pytest
from datetime import datetime

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from services.backend_services.multi_agent_service.app.agents.contract_adapter import (
    ContractAdapter,
    ContractState,
    ApprovalRequest,
    StruggleSignal,
)


class TestContractAdapterStateTransitions:
    """Tests for state machine transitions."""
    
    def test_initial_state_is_idle(self):
        """Verify new adapters start in idle state."""
        adapter = ContractAdapter("architect", "session-1")
        assert adapter.get_current_state() == "idle"
    
    def test_valid_transition_idle_to_analysis(self):
        """Verify valid transition from idle to analysis."""
        adapter = ContractAdapter("architect", "session-1")
        result = adapter.transition_to("analysis")
        assert result is True
        assert adapter.get_current_state() == "analysis"
    
    def test_valid_transition_analysis_to_approval_pending(self):
        """Verify valid transition from analysis to approval_pending."""
        adapter = ContractAdapter("developer", "session-1")
        adapter.transition_to("analysis")
        result = adapter.transition_to("approval_pending")
        assert result is True
        assert adapter.get_current_state() == "approval_pending"
    
    def test_valid_transition_approval_to_execution(self):
        """Verify valid transition from approval_pending to execution."""
        adapter = ContractAdapter("developer", "session-1")
        adapter.transition_to("analysis")
        adapter.transition_to("approval_pending")
        result = adapter.transition_to("execution")
        assert result is True
        assert adapter.get_current_state() == "execution"
    
    def test_valid_transition_execution_to_validation(self):
        """Verify valid transition from execution to validation."""
        adapter = ContractAdapter("tester", "session-1")
        adapter.transition_to("analysis")
        adapter.transition_to("approval_pending")
        adapter.transition_to("execution")
        result = adapter.transition_to("validation")
        assert result is True
        assert adapter.get_current_state() == "validation"
    
    def test_valid_transition_validation_to_done(self):
        """Verify valid transition from validation to done."""
        adapter = ContractAdapter("tester", "session-1")
        adapter.transition_to("analysis")
        adapter.transition_to("approval_pending")
        adapter.transition_to("execution")
        adapter.transition_to("validation")
        result = adapter.transition_to("done")
        assert result is True
        assert adapter.get_current_state() == "done"
    
    def test_forbidden_transition_analysis_to_done(self):
        """Verify forbidden transition from analysis to done raises error."""
        adapter = ContractAdapter("architect", "session-1")
        adapter.transition_to("analysis")
        
        with pytest.raises(ValueError, match="Forbidden transition"):
            adapter.transition_to("done")
    
    def test_forbidden_transition_idle_to_execution(self):
        """Verify forbidden transition from idle to execution raises error."""
        adapter = ContractAdapter("developer", "session-1")
        
        with pytest.raises(ValueError, match="Forbidden transition"):
            adapter.transition_to("execution")
    
    def test_forbidden_transition_idle_to_done(self):
        """Verify forbidden transition from idle to done raises error."""
        adapter = ContractAdapter("developer", "session-1")
        
        with pytest.raises(ValueError, match="Forbidden transition"):
            adapter.transition_to("done")
    
    def test_forbidden_transition_execution_to_done(self):
        """Verify forbidden transition from execution to done raises error."""
        adapter = ContractAdapter("developer", "session-1")
        adapter.transition_to("analysis")
        adapter.transition_to("approval_pending")
        adapter.transition_to("execution")
        
        with pytest.raises(ValueError, match="Forbidden transition"):
            adapter.transition_to("done")
    
    def test_invalid_transition_raises_error(self):
        """Verify invalid (not in valid set) transition raises error."""
        adapter = ContractAdapter("architect", "session-1")
        adapter.transition_to("analysis")
        
        with pytest.raises(ValueError, match="Invalid transition"):
            adapter.transition_to("idle")  # analysis → idle not valid
    
    def test_transition_updates_last_transition_time(self):
        """Verify transition updates last_transition timestamp."""
        adapter = ContractAdapter("architect", "session-1")
        assert adapter.state.last_transition is None
        
        adapter.transition_to("analysis")
        assert adapter.state.last_transition is not None
        assert isinstance(adapter.state.last_transition, datetime)


class TestContractAdapterAssumptions:
    """Tests for assumption tracking."""
    
    def test_add_assumption_increments_count(self):
        """Verify adding assumption increments count."""
        adapter = ContractAdapter("analyst", "session-1")
        assert adapter.state.assumption_count == 0
        
        adapter.add_assumption("User wants REST API")
        assert adapter.state.assumption_count == 1
    
    def test_add_assumption_returns_false_under_limit(self):
        """Verify add_assumption returns False when under limit."""
        adapter = ContractAdapter("analyst", "session-1")
        result = adapter.add_assumption("Assumption 1")
        assert result is False
        
        result = adapter.add_assumption("Assumption 2")
        assert result is False
    
    def test_add_assumption_returns_true_at_limit(self):
        """Verify add_assumption returns True at max (hard stop)."""
        adapter = ContractAdapter("analyst", "session-1")
        adapter.add_assumption("Assumption 1")
        adapter.add_assumption("Assumption 2")
        
        result = adapter.add_assumption("Assumption 3")
        assert result is True  # Hard stop triggered
    
    def test_custom_max_assumptions(self):
        """Verify custom max_assumptions is respected."""
        adapter = ContractAdapter("analyst", "session-1")
        adapter.state.max_assumptions = 5
        
        for i in range(4):
            result = adapter.add_assumption(f"Assumption {i+1}")
            assert result is False
        
        result = adapter.add_assumption("Assumption 5")
        assert result is True


class TestContractAdapterFailedAttempts:
    """Tests for failed attempt tracking."""
    
    def test_record_failed_attempt_increments_count(self):
        """Verify recording failed attempt increments count."""
        adapter = ContractAdapter("developer", "session-1")
        assert adapter.state.failed_attempts == 0
        
        adapter.record_failed_attempt()
        assert adapter.state.failed_attempts == 1
    
    def test_record_failed_attempt_returns_false_under_limit(self):
        """Verify returns False when under struggle threshold."""
        adapter = ContractAdapter("developer", "session-1")
        result = adapter.record_failed_attempt()
        assert result is False
    
    def test_record_failed_attempt_returns_true_at_limit(self):
        """Verify returns True at max (struggle signal needed)."""
        adapter = ContractAdapter("developer", "session-1")
        adapter.record_failed_attempt()
        
        result = adapter.record_failed_attempt()
        assert result is True  # Struggle signal needed


class TestContractAdapterRepeatedFixes:
    """Tests for repeated fix detection."""
    
    def test_first_fix_returns_false(self):
        """Verify first fix attempt is not flagged."""
        adapter = ContractAdapter("developer", "session-1")
        result = adapter.record_fix_attempt("Add null check for input")
        assert result is False
    
    def test_different_fix_returns_false(self):
        """Verify different fix is not flagged."""
        adapter = ContractAdapter("developer", "session-1")
        adapter.record_fix_attempt("Add null check for input")
        result = adapter.record_fix_attempt("Add validation for output")
        assert result is False
    
    def test_similar_fix_returns_true(self):
        """Verify similar fix triggers hard stop."""
        adapter = ContractAdapter("developer", "session-1")
        adapter.record_fix_attempt("Add null check for user input")
        result = adapter.record_fix_attempt("Add null validation for user input")
        assert result is True  # Similar fix detected
    
    def test_exact_same_fix_returns_true(self):
        """Verify exact same fix triggers hard stop."""
        adapter = ContractAdapter("developer", "session-1")
        adapter.record_fix_attempt("Add null check")
        result = adapter.record_fix_attempt("add null check")  # Case insensitive
        assert result is True


class TestContractAdapterToolCalls:
    """Tests for tool call tracking."""
    
    def test_record_tool_call_increments_count(self):
        """Verify recording tool call increments count."""
        adapter = ContractAdapter("analyst", "session-1")
        assert adapter.state.tool_call_count == 0
        
        adapter.record_tool_call()
        assert adapter.state.tool_call_count == 1
    
    def test_record_tool_call_returns_false_under_limit(self):
        """Verify returns False when under limit."""
        adapter = ContractAdapter("analyst", "session-1")
        for _ in range(9):
            result = adapter.record_tool_call()
            assert result is False
    
    def test_record_tool_call_returns_true_at_limit(self):
        """Verify returns True at max tool calls."""
        adapter = ContractAdapter("analyst", "session-1")
        for _ in range(9):
            adapter.record_tool_call()
        
        result = adapter.record_tool_call()
        assert result is True


class TestContractAdapterReset:
    """Tests for task tracking reset."""
    
    def test_reset_clears_all_tracking(self):
        """Verify reset clears all task tracking."""
        adapter = ContractAdapter("developer", "session-1")
        
        adapter.add_assumption("Test assumption")
        adapter.record_failed_attempt()
        adapter.record_tool_call()
        adapter.record_fix_attempt("Test fix")
        
        adapter.reset_task_tracking()
        
        assert adapter.state.assumption_count == 0
        assert adapter.state.failed_attempts == 0
        assert adapter.state.tool_call_count == 0
    
    def test_force_reset_returns_to_idle(self):
        """Verify force_reset returns to idle state."""
        adapter = ContractAdapter("developer", "session-1")
        adapter.transition_to("analysis")
        adapter.transition_to("approval_pending")
        adapter.add_assumption("Test")
        
        adapter.force_reset()
        
        assert adapter.get_current_state() == "idle"
        assert adapter.state.assumption_count == 0


class TestContractAdapterApprovalRequest:
    """Tests for approval request creation."""
    
    def test_create_approval_request(self):
        """Verify approval request creation."""
        adapter = ContractAdapter("developer", "session-1")
        adapter.transition_to("analysis")
        
        request = adapter.create_approval_request(
            intent="Implement REST API",
            scope="Create 5 endpoints",
            approach="Use FastAPI",
            consequences=["Changes API surface"],
            risks=["Breaking changes"],
            validation_plan="Run integration tests",
            assumptions=["User wants REST"]
        )
        
        assert request.intent == "Implement REST API"
        assert adapter.get_current_state() == "approval_pending"
    
    def test_create_approval_request_checks_assumptions(self):
        """Verify approval request checks assumption overflow."""
        adapter = ContractAdapter("developer", "session-1")
        adapter.transition_to("analysis")
        adapter.add_assumption("Assumption 1")
        adapter.add_assumption("Assumption 2")
        
        with pytest.raises(ValueError, match="Assumption overflow"):
            adapter.create_approval_request(
                intent="Test",
                scope="Test",
                approach="Test",
                assumptions=["Assumption 3"]
            )


class TestContractAdapterStruggleSignal:
    """Tests for struggle signal creation."""
    
    def test_create_struggle_signal(self):
        """Verify struggle signal creation."""
        adapter = ContractAdapter("developer", "session-1")
        adapter.transition_to("analysis")
        
        signal = adapter.create_struggle_signal(
            signal_type="technical_blocker",
            what_i_understand="Need to implement X",
            what_i_tried=[{"approach": "Used Y", "outcome": "Failed"}],
            where_im_stuck="Cannot resolve dependency",
            what_would_help="Expert consultation"
        )
        
        assert signal.signal_type == "technical_blocker"
        assert adapter.get_current_state() == "blocked"


class TestContractAdapterMetrics:
    """Tests for metrics reporting."""
    
    def test_get_metrics(self):
        """Verify metrics reporting."""
        adapter = ContractAdapter("analyst", "session-123")
        adapter.transition_to("analysis")
        adapter.add_assumption("Test")
        adapter.record_failed_attempt()
        adapter.record_tool_call()
        
        metrics = adapter.get_metrics()
        
        assert metrics["agent_role"] == "analyst"
        assert metrics["session_id"] == "session-123"
        assert metrics["current_state"] == "analysis"
        assert metrics["assumption_count"] == 1
        assert metrics["failed_attempts"] == 1
        assert metrics["tool_call_count"] == 1


class TestContractAdapterPromptSection:
    """Tests for prompt section generation."""
    
    def test_get_contract_prompt_section(self):
        """Verify contract prompt section generation."""
        adapter = ContractAdapter("developer", "session-1")
        adapter.transition_to("analysis")
        adapter.add_assumption("Test assumption")
        
        prompt = adapter.get_contract_prompt_section()
        
        assert "## Behavioral Contract" in prompt
        assert "State: ANALYSIS" in prompt
        assert "Assumptions: 1/3" in prompt
        assert "Tier 0 Rules" in prompt
        assert "Hard Stop Triggers" in prompt
