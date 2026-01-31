# =============================================================================
# Contract Enforcer Tests
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Tests for contract enforcer and hard stop triggers."""

import pytest
from enum import Enum
from typing import List, Dict, Optional


class HardStopTrigger(str, Enum):
    """Hard stop trigger types."""
    ASSUMPTION_OVERFLOW = "assumption_count_exceeded"
    REPEATED_FIX = "same_fix_proposed_twice"
    EVIDENCE_CONTRADICTION = "evidence_contradicts_hypothesis"
    EXECUTION_DIVERGENCE = "execution_diverges_from_approval"
    TOOL_FAILURE_CASCADE = "tool_failed_3x"


class MockContractEnforcer:
    """Mock contract enforcer for testing."""
    
    def __init__(self, max_assumptions: int = 3, max_tool_failures: int = 3):
        self.max_assumptions = max_assumptions
        self.max_tool_failures = max_tool_failures
        self.assumption_count = 0
        self.assumptions: List[str] = []
        self.fix_history: List[str] = []
        self.tool_failures: Dict[str, int] = {}
        self.violations: List[str] = []
    
    def add_assumption(self, assumption: str) -> bool:
        """Add an assumption and check for overflow."""
        self.assumptions.append(assumption)
        self.assumption_count += 1
        return self.assumption_count >= self.max_assumptions
    
    def record_fix(self, fix_description: str) -> bool:
        """Record a fix and check for repetition."""
        normalized = fix_description.lower().strip()
        
        for prev in self.fix_history:
            if self._similar(normalized, prev):
                return True
        
        self.fix_history.append(normalized)
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
    
    def record_tool_failure(self, tool_name: str) -> bool:
        """Record a tool failure and check for cascade."""
        self.tool_failures[tool_name] = self.tool_failures.get(tool_name, 0) + 1
        return self.tool_failures[tool_name] >= self.max_tool_failures
    
    def check_triggers(self) -> Optional[HardStopTrigger]:
        """Check if any hard stop triggers should fire."""
        if self.assumption_count >= self.max_assumptions:
            return HardStopTrigger.ASSUMPTION_OVERFLOW
        
        for tool, count in self.tool_failures.items():
            if count >= self.max_tool_failures:
                return HardStopTrigger.TOOL_FAILURE_CASCADE
        
        return None
    
    def reset(self):
        """Reset the enforcer state."""
        self.assumption_count = 0
        self.assumptions.clear()
        self.fix_history.clear()
        self.tool_failures.clear()
        self.violations.clear()


class TestAssumptionOverflow:
    """Test assumption overflow trigger."""
    
    @pytest.mark.asyncio
    async def test_assumption_overflow_triggers(self, simulator):
        """Test that 3+ assumptions trigger overflow."""
        enforcer = MockContractEnforcer(max_assumptions=3)
        
        enforcer.add_assumption("Assumption 1")
        enforcer.add_assumption("Assumption 2")
        overflow = enforcer.add_assumption("Assumption 3")
        
        assert overflow is True
        trigger = enforcer.check_triggers()
        assert trigger == HardStopTrigger.ASSUMPTION_OVERFLOW
    
    @pytest.mark.asyncio
    async def test_assumptions_below_threshold(self, simulator):
        """Test that fewer assumptions don't trigger."""
        enforcer = MockContractEnforcer(max_assumptions=3)
        
        enforcer.add_assumption("Assumption 1")
        enforcer.add_assumption("Assumption 2")
        
        trigger = enforcer.check_triggers()
        assert trigger is None
    
    @pytest.mark.asyncio
    async def test_assumption_count_tracked(self, simulator):
        """Test that assumptions are counted correctly."""
        enforcer = MockContractEnforcer(max_assumptions=5)
        
        for i in range(4):
            enforcer.add_assumption(f"Assumption {i}")
        
        assert enforcer.assumption_count == 4
        assert len(enforcer.assumptions) == 4


class TestRepeatedFix:
    """Test repeated fix detection."""
    
    @pytest.mark.asyncio
    async def test_repeated_fix_detected(self, simulator):
        """Test that same fix proposed twice is detected."""
        enforcer = MockContractEnforcer()
        
        enforcer.record_fix("Add null check to validate()")
        repeated = enforcer.record_fix("Add null check to validate()")
        
        assert repeated is True
    
    @pytest.mark.asyncio
    async def test_similar_fix_detected(self, simulator):
        """Test that similar fixes are detected."""
        enforcer = MockContractEnforcer()
        
        enforcer.record_fix("Add null check to validate function")
        repeated = enforcer.record_fix("Add null check to validate method")
        
        assert repeated is True
    
    @pytest.mark.asyncio
    async def test_different_fixes_allowed(self, simulator):
        """Test that different fixes are not flagged."""
        enforcer = MockContractEnforcer()
        
        enforcer.record_fix("Add null check to validate()")
        repeated = enforcer.record_fix("Refactor error handling in process()")
        
        assert repeated is False
    
    @pytest.mark.asyncio
    async def test_fix_history_maintained(self, simulator):
        """Test that fix history is maintained."""
        enforcer = MockContractEnforcer()
        
        enforcer.record_fix("Fix 1")
        enforcer.record_fix("Fix 2")
        enforcer.record_fix("Fix 3")
        
        assert len(enforcer.fix_history) == 3


class TestToolFailureCascade:
    """Test tool failure cascade trigger."""
    
    @pytest.mark.asyncio
    async def test_tool_failure_cascade_triggers(self, simulator):
        """Test that 3 consecutive tool failures trigger cascade."""
        enforcer = MockContractEnforcer(max_tool_failures=3)
        
        enforcer.record_tool_failure("api_call")
        enforcer.record_tool_failure("api_call")
        cascade = enforcer.record_tool_failure("api_call")
        
        assert cascade is True
        trigger = enforcer.check_triggers()
        assert trigger == HardStopTrigger.TOOL_FAILURE_CASCADE
    
    @pytest.mark.asyncio
    async def test_different_tools_tracked_separately(self, simulator):
        """Test that different tools are tracked separately."""
        enforcer = MockContractEnforcer(max_tool_failures=3)
        
        enforcer.record_tool_failure("tool_a")
        enforcer.record_tool_failure("tool_b")
        enforcer.record_tool_failure("tool_a")
        
        assert enforcer.tool_failures["tool_a"] == 2
        assert enforcer.tool_failures["tool_b"] == 1
        assert enforcer.check_triggers() is None
    
    @pytest.mark.asyncio
    async def test_tool_failures_below_threshold(self, simulator):
        """Test that fewer failures don't trigger."""
        enforcer = MockContractEnforcer(max_tool_failures=3)
        
        enforcer.record_tool_failure("api_call")
        enforcer.record_tool_failure("api_call")
        
        trigger = enforcer.check_triggers()
        assert trigger is None


class TestEnforcerReset:
    """Test enforcer reset functionality."""
    
    @pytest.mark.asyncio
    async def test_reset_clears_state(self, simulator):
        """Test that reset clears all state."""
        enforcer = MockContractEnforcer()
        
        enforcer.add_assumption("Test assumption")
        enforcer.record_fix("Test fix")
        enforcer.record_tool_failure("test_tool")
        
        enforcer.reset()
        
        assert enforcer.assumption_count == 0
        assert len(enforcer.assumptions) == 0
        assert len(enforcer.fix_history) == 0
        assert len(enforcer.tool_failures) == 0
