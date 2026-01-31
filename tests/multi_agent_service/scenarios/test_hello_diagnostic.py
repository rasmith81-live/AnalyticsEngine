# =============================================================================
# Hello Diagnostic Tests
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Tests for the Hello protocol agent viability diagnostic."""

import pytest
from typing import Dict, Any, List
from datetime import datetime


class MockHelloDiagnosticRunner:
    """Mock Hello Diagnostic runner for testing."""
    
    def __init__(self, simulator=None):
        self.simulator = simulator
        self._results: Dict[str, Any] = {}
    
    async def run_diagnostic(
        self,
        agent_role: str,
        session_id: str
    ) -> "HelloDiagnosticResult":
        """Run the hello diagnostic for an agent."""
        score = 0.0
        findings: List[str] = []
        
        contract_ack = await self._check_contract_acknowledgment(agent_role)
        if contract_ack:
            score += 0.25
            findings.append("Contract rules acknowledged")
        
        state_machine = await self._check_state_machine(agent_role)
        if state_machine:
            score += 0.25
            findings.append("State machine functioning")
        
        struggle_protocol = await self._check_struggle_protocol(agent_role)
        if struggle_protocol:
            score += 0.25
            findings.append("Struggle protocol available")
        
        peer_awareness = await self._check_peer_awareness(agent_role)
        if peer_awareness:
            score += 0.25
            findings.append("Peer collaboration configured")
        
        return HelloDiagnosticResult(
            agent_role=agent_role,
            session_id=session_id,
            viable=score >= 0.7,
            score=score,
            contract_acknowledged=contract_ack,
            state_machine_working=state_machine,
            struggle_protocol_available=struggle_protocol,
            peer_collaboration_configured=peer_awareness,
            findings=findings,
            timestamp=datetime.utcnow().isoformat()
        )
    
    async def _check_contract_acknowledgment(self, agent_role: str) -> bool:
        """Check if agent acknowledges contract rules."""
        return True
    
    async def _check_state_machine(self, agent_role: str) -> bool:
        """Check if state machine is functioning."""
        return True
    
    async def _check_struggle_protocol(self, agent_role: str) -> bool:
        """Check if struggle protocol is available."""
        return True
    
    async def _check_peer_awareness(self, agent_role: str) -> bool:
        """Check if peer collaboration is configured."""
        return True


class HelloDiagnosticResult:
    """Result of a hello diagnostic."""
    
    def __init__(
        self,
        agent_role: str,
        session_id: str,
        viable: bool,
        score: float,
        contract_acknowledged: bool,
        state_machine_working: bool,
        struggle_protocol_available: bool,
        peer_collaboration_configured: bool,
        findings: List[str],
        timestamp: str
    ):
        self.agent_role = agent_role
        self.session_id = session_id
        self.viable = viable
        self.score = score
        self.contract_acknowledged = contract_acknowledged
        self.state_machine_working = state_machine_working
        self.struggle_protocol_available = struggle_protocol_available
        self.peer_collaboration_configured = peer_collaboration_configured
        self.findings = findings
        self.timestamp = timestamp


class TestHelloDiagnostic:
    """Test the Hello protocol for agent viability."""
    
    @pytest.mark.parametrize("agent_role", [
        "coordinator",
        "architect",
        "developer",
        "tester",
        "business_analyst",
        "data_analyst",
        "documenter"
    ])
    @pytest.mark.asyncio
    async def test_agent_passes_hello(self, agent_role, simulator):
        """Test that agents pass the hello diagnostic."""
        runner = MockHelloDiagnosticRunner(simulator)
        
        result = await runner.run_diagnostic(
            agent_role=agent_role,
            session_id="test_session"
        )
        
        assert result.viable is True
        assert result.score >= 0.7
        assert result.contract_acknowledged is True
        assert result.state_machine_working is True
    
    @pytest.mark.asyncio
    async def test_hello_diagnostic_scoring(self, simulator):
        """Test that hello diagnostic scores correctly."""
        runner = MockHelloDiagnosticRunner(simulator)
        
        result = await runner.run_diagnostic(
            agent_role="developer",
            session_id="test_session"
        )
        
        assert result.score == 1.0
        assert len(result.findings) == 4
    
    @pytest.mark.asyncio
    async def test_hello_diagnostic_findings(self, simulator):
        """Test that hello diagnostic captures findings."""
        runner = MockHelloDiagnosticRunner(simulator)
        
        result = await runner.run_diagnostic(
            agent_role="architect",
            session_id="test_session"
        )
        
        assert "Contract rules acknowledged" in result.findings
        assert "State machine functioning" in result.findings
        assert "Struggle protocol available" in result.findings
        assert "Peer collaboration configured" in result.findings


class TestHelloDiagnosticFailures:
    """Test hello diagnostic failure scenarios."""
    
    @pytest.mark.asyncio
    async def test_failed_contract_acknowledgment(self, simulator):
        """Test agent failing contract acknowledgment."""
        runner = MockHelloDiagnosticRunner(simulator)
        runner._check_contract_acknowledgment = lambda x: False
        
        # Override to simulate failure
        async def mock_check(agent_role):
            return False
        runner._check_contract_acknowledgment = mock_check
        
        result = await runner.run_diagnostic(
            agent_role="developer",
            session_id="test_session"
        )
        
        assert result.contract_acknowledged is False
        assert result.score < 1.0
    
    @pytest.mark.asyncio
    async def test_viability_threshold(self, simulator):
        """Test that viability requires 70% score."""
        runner = MockHelloDiagnosticRunner(simulator)
        
        async def fail_check(agent_role):
            return False
        
        runner._check_contract_acknowledgment = fail_check
        runner._check_state_machine = fail_check
        
        result = await runner.run_diagnostic(
            agent_role="developer",
            session_id="test_session"
        )
        
        assert result.score == 0.5
        assert result.viable is False
