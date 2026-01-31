# =============================================================================
# Multi-Agent Service Integration Tests
# =============================================================================
"""
Integration tests for multi_agent_service and conversation_service.

Tests cover:
- Service-to-service communication
- Blackboard operations
- Contract enforcement across services
- Circuit breaker behavior
"""

import pytest
import asyncio
from unittest.mock import patch, AsyncMock, MagicMock
from datetime import datetime

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from services.backend_services.multi_agent_service.app.agents.contract_adapter import (
    ContractAdapter,
    ContractState,
)
from services.backend_services.multi_agent_service.app.discovery.fuzzy_discovery import (
    FuzzyAgentDiscovery,
)
from services.backend_services.multi_agent_service.app.delegation.dry_run import (
    DelegationPreviewBuilder,
    DryRunExecutor,
)


class TestContractIntegration:
    """Tests for contract enforcement integration."""
    
    @pytest.mark.asyncio
    async def test_contract_adapter_workflow(self):
        """Test complete contract adapter workflow."""
        adapter = ContractAdapter("developer", "integration-session-1")
        
        # Start task
        assert adapter.get_current_state() == "idle"
        adapter.transition_to("analysis")
        assert adapter.get_current_state() == "analysis"
        
        # Request approval
        adapter.add_assumption("Using Python 3.11")
        approval = adapter.create_approval_request(
            intent="Implement feature",
            scope="Single endpoint",
            approach="FastAPI",
            assumptions=["REST API preferred"]
        )
        assert adapter.get_current_state() == "approval_pending"
        
        # Execute
        adapter.transition_to("execution")
        adapter.record_tool_call()
        assert adapter.get_current_state() == "execution"
        
        # Validate
        adapter.transition_to("validation")
        assert adapter.get_current_state() == "validation"
        
        # Complete
        adapter.transition_to("done")
        assert adapter.get_current_state() == "done"
    
    @pytest.mark.asyncio
    async def test_hard_stop_on_assumption_overflow(self):
        """Test hard stop triggers on assumption overflow."""
        adapter = ContractAdapter("analyst", "integration-session-2")
        adapter.transition_to("analysis")
        
        # Add assumptions up to limit
        adapter.add_assumption("Assumption 1")
        adapter.add_assumption("Assumption 2")
        
        # Third assumption triggers hard stop
        with pytest.raises(ValueError, match="Assumption overflow"):
            adapter.create_approval_request(
                intent="Test",
                scope="Test",
                approach="Test",
                assumptions=["Assumption 3"]
            )
    
    @pytest.mark.asyncio
    async def test_struggle_signal_workflow(self):
        """Test struggle signal creation workflow."""
        adapter = ContractAdapter("developer", "integration-session-3")
        adapter.transition_to("analysis")
        
        # Record failed attempts
        adapter.record_failed_attempt()
        should_struggle = adapter.record_failed_attempt()
        assert should_struggle is True
        
        # Create struggle signal
        signal = adapter.create_struggle_signal(
            signal_type="technical_blocker",
            what_i_understand="Need to implement X",
            what_i_tried=[{"approach": "Y", "outcome": "Failed"}],
            where_im_stuck="Cannot resolve dependency",
            what_would_help="Expert help"
        )
        
        assert adapter.get_current_state() == "blocked"
        assert signal.signal_type == "technical_blocker"


class TestDiscoveryIntegration:
    """Tests for agent discovery integration."""
    
    def test_discovery_with_real_agents(self):
        """Test discovery returns real agent matches."""
        discovery = FuzzyAgentDiscovery()
        
        # Search for business-related agents
        results = discovery.search("business strategy")
        
        assert len(results) > 0
        roles = [r.agent_role for r in results]
        assert "business_strategist" in roles or "business_analyst" in roles
    
    def test_discovery_for_technical_task(self):
        """Test discovery for technical task description."""
        discovery = FuzzyAgentDiscovery()
        
        suggestions = discovery.suggest_agents(
            "Create a Kubernetes deployment for the API service",
            limit=3
        )
        
        assert len(suggestions) > 0
        roles = [s.agent_role for s in suggestions]
        assert "deployment_specialist" in roles or "architect" in roles


class TestDelegationPreview:
    """Tests for delegation preview integration."""
    
    @pytest.mark.asyncio
    async def test_dry_run_preview(self):
        """Test dry-run preview generation."""
        executor = DryRunExecutor()
        
        result = await executor.delegate(
            task="Analyze inventory levels",
            target_agent="supply_chain_analyst",
            dry_run=True,
            context={"requires_review": True}
        )
        
        assert result["mode"] == "dry_run"
        assert "preview" in result
        assert result["preview"]["task"] == "Analyze inventory levels"
        assert result["preview"]["target_agent"] == "supply_chain_analyst"
    
    @pytest.mark.asyncio
    async def test_preview_includes_actions(self):
        """Test preview includes predicted actions."""
        builder = DelegationPreviewBuilder()
        
        preview = builder.build_preview(
            task="Implement REST API for orders",
            target_agent="developer",
            context={}
        )
        
        assert len(preview.predicted_actions) > 0
        action_types = [a.action_type.value for a in preview.predicted_actions]
        assert "contract_check" in action_types
        assert "task_creation" in action_types
    
    @pytest.mark.asyncio
    async def test_preview_with_blockers(self):
        """Test preview identifies blockers."""
        builder = DelegationPreviewBuilder()
        
        preview = builder.build_preview(
            task="Deploy application",
            target_agent="deployment_specialist",
            context={"blackboard_unavailable": True}
        )
        
        assert "Blackboard service is unavailable" in preview.potential_blockers


class TestCrossServiceIntegration:
    """Tests for cross-service integration patterns."""
    
    @pytest.mark.asyncio
    async def test_contract_metrics_collection(self):
        """Test metrics collection from contract adapter."""
        adapter = ContractAdapter("architect", "metrics-session")
        adapter.transition_to("analysis")
        adapter.add_assumption("Test assumption")
        adapter.record_tool_call()
        
        metrics = adapter.get_metrics()
        
        assert metrics["agent_role"] == "architect"
        assert metrics["current_state"] == "analysis"
        assert metrics["assumption_count"] == 1
        assert metrics["tool_call_count"] == 1
    
    @pytest.mark.asyncio
    async def test_prompt_injection_in_contract(self):
        """Test contract prompt section injection."""
        adapter = ContractAdapter("developer", "prompt-session")
        adapter.transition_to("analysis")
        
        prompt = adapter.get_contract_prompt_section()
        
        assert "## Behavioral Contract" in prompt
        assert "Tier 0 Rules" in prompt
        assert "Hard Stop Triggers" in prompt
        assert "Struggle Protocol" in prompt


class TestMultipleAgentCoordination:
    """Tests for multi-agent coordination patterns."""
    
    @pytest.mark.asyncio
    async def test_parallel_agent_discovery(self):
        """Test parallel agent discovery for complex task."""
        discovery = FuzzyAgentDiscovery()
        
        # Simulate finding agents for different aspects of a task
        tasks = [
            "design system architecture",
            "implement business logic",
            "write test cases",
            "create documentation"
        ]
        
        all_suggestions = []
        for task in tasks:
            suggestions = discovery.suggest_agents(task, limit=2)
            all_suggestions.extend([s.agent_role for s in suggestions])
        
        # Should have diverse agents
        unique_agents = set(all_suggestions)
        assert len(unique_agents) >= 3
    
    @pytest.mark.asyncio
    async def test_sequential_contract_states(self):
        """Test sequential contract state transitions across agents."""
        agents = [
            ContractAdapter("architect", "coord-session"),
            ContractAdapter("developer", "coord-session"),
            ContractAdapter("tester", "coord-session"),
        ]
        
        # Architect designs
        agents[0].transition_to("analysis")
        agents[0].transition_to("approval_pending")
        agents[0].transition_to("execution")
        agents[0].transition_to("validation")
        agents[0].transition_to("done")
        
        # Developer implements
        agents[1].transition_to("analysis")
        agents[1].transition_to("approval_pending")
        agents[1].transition_to("execution")
        agents[1].transition_to("validation")
        agents[1].transition_to("done")
        
        # Tester validates
        agents[2].transition_to("analysis")
        agents[2].transition_to("approval_pending")
        agents[2].transition_to("execution")
        agents[2].transition_to("validation")
        agents[2].transition_to("done")
        
        # All agents completed
        assert all(a.get_current_state() == "done" for a in agents)


class TestErrorHandling:
    """Tests for error handling in integration scenarios."""
    
    @pytest.mark.asyncio
    async def test_invalid_state_recovery(self):
        """Test recovery from invalid state transition."""
        adapter = ContractAdapter("developer", "error-session")
        adapter.transition_to("analysis")
        
        # Attempt invalid transition
        try:
            adapter.transition_to("done")  # Forbidden
        except ValueError:
            pass
        
        # Should still be in analysis state
        assert adapter.get_current_state() == "analysis"
        
        # Can continue with valid transitions
        adapter.transition_to("approval_pending")
        assert adapter.get_current_state() == "approval_pending"
    
    @pytest.mark.asyncio
    async def test_force_reset_recovery(self):
        """Test force reset for stuck agents."""
        adapter = ContractAdapter("developer", "stuck-session")
        adapter.transition_to("analysis")
        adapter.add_assumption("A1")
        adapter.add_assumption("A2")
        adapter.record_failed_attempt()
        
        # Force reset
        adapter.force_reset()
        
        assert adapter.get_current_state() == "idle"
        assert adapter.state.assumption_count == 0
        assert adapter.state.failed_attempts == 0
