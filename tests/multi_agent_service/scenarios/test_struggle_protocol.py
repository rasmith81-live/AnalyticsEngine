# =============================================================================
# Struggle Protocol Tests
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Tests for the Struggle protocol signaling."""

import pytest
from typing import Dict, Any, List
from datetime import datetime


class MockStruggleSignal:
    """Mock struggle signal for testing."""
    
    def __init__(
        self,
        agent_role: str,
        signal_type: str,
        what_i_understand: str,
        what_i_tried: List[Dict[str, str]],
        where_im_stuck: str,
        what_would_help: str
    ):
        self.agent_role = agent_role
        self.signal_type = signal_type
        self.what_i_understand = what_i_understand
        self.what_i_tried = what_i_tried
        self.where_im_stuck = where_im_stuck
        self.what_would_help = what_would_help
        self.timestamp = datetime.utcnow().isoformat()
        self.id = f"struggle_{agent_role}_{datetime.utcnow().timestamp()}"
    
    def to_formatted_message(self) -> str:
        """Format the struggle signal for display."""
        tried_list = "\n".join([
            f"  - {item['action']}: {item['outcome']}"
            for item in self.what_i_tried
        ])
        
        return f"""🚨 SYNC NEEDED — {self.signal_type} detected

**What I understand**: {self.what_i_understand}

**What I've tried**:
{tried_list}

**Where I'm stuck**: {self.where_im_stuck}

**What would help**: {self.what_would_help}
"""


class MockStruggleProtocol:
    """Mock struggle protocol handler for testing."""
    
    def __init__(self):
        self._signals: List[MockStruggleSignal] = []
        self._resolutions: Dict[str, Any] = {}
    
    def create_signal(
        self,
        agent_role: str,
        signal_type: str,
        what_i_understand: str,
        what_i_tried: List[Dict[str, str]],
        where_im_stuck: str,
        what_would_help: str
    ) -> MockStruggleSignal:
        """Create a new struggle signal."""
        signal = MockStruggleSignal(
            agent_role=agent_role,
            signal_type=signal_type,
            what_i_understand=what_i_understand,
            what_i_tried=what_i_tried,
            where_im_stuck=where_im_stuck,
            what_would_help=what_would_help
        )
        self._signals.append(signal)
        return signal
    
    def resolve_signal(
        self,
        signal_id: str,
        resolution: str,
        resolved_by: str
    ) -> bool:
        """Mark a signal as resolved."""
        for signal in self._signals:
            if signal.id == signal_id:
                self._resolutions[signal_id] = {
                    "resolution": resolution,
                    "resolved_by": resolved_by,
                    "resolved_at": datetime.utcnow().isoformat()
                }
                return True
        return False
    
    def get_pending_signals(self) -> List[MockStruggleSignal]:
        """Get all unresolved signals."""
        return [s for s in self._signals if s.id not in self._resolutions]


class TestStruggleSignalCreation:
    """Test struggle signal creation."""
    
    @pytest.mark.asyncio
    async def test_create_struggle_signal(self, simulator):
        """Test creating a struggle signal."""
        protocol = MockStruggleProtocol()
        
        signal = protocol.create_signal(
            agent_role="developer",
            signal_type="blocked",
            what_i_understand="The API requires authentication",
            what_i_tried=[
                {"action": "Added Bearer token", "outcome": "401 Unauthorized"},
                {"action": "Checked token expiry", "outcome": "Token is valid"}
            ],
            where_im_stuck="Cannot determine correct auth header format",
            what_would_help="API documentation or example of working auth"
        )
        
        assert signal.agent_role == "developer"
        assert signal.signal_type == "blocked"
        assert len(signal.what_i_tried) == 2
        assert signal.id is not None
    
    @pytest.mark.asyncio
    async def test_signal_formatted_message(self, simulator):
        """Test that struggle signal formats correctly."""
        protocol = MockStruggleProtocol()
        
        signal = protocol.create_signal(
            agent_role="tester",
            signal_type="confused",
            what_i_understand="Test expects JSON response",
            what_i_tried=[
                {"action": "Checked content-type", "outcome": "Returns text/html"}
            ],
            where_im_stuck="Response format mismatch",
            what_would_help="Clarification on expected response format"
        )
        
        message = signal.to_formatted_message()
        
        assert "🚨 SYNC NEEDED" in message
        assert "confused" in message
        assert "Test expects JSON response" in message
        assert "Checked content-type" in message


class TestStruggleSignalResolution:
    """Test struggle signal resolution."""
    
    @pytest.mark.asyncio
    async def test_resolve_signal(self, simulator):
        """Test resolving a struggle signal."""
        protocol = MockStruggleProtocol()
        
        signal = protocol.create_signal(
            agent_role="developer",
            signal_type="blocked",
            what_i_understand="Need database schema",
            what_i_tried=[],
            where_im_stuck="Schema not documented",
            what_would_help="Schema documentation"
        )
        
        resolved = protocol.resolve_signal(
            signal_id=signal.id,
            resolution="Schema provided by architect",
            resolved_by="coordinator"
        )
        
        assert resolved is True
        assert len(protocol.get_pending_signals()) == 0
    
    @pytest.mark.asyncio
    async def test_pending_signals_tracked(self, simulator):
        """Test that pending signals are tracked."""
        protocol = MockStruggleProtocol()
        
        signal1 = protocol.create_signal(
            agent_role="developer",
            signal_type="blocked",
            what_i_understand="Issue 1",
            what_i_tried=[],
            where_im_stuck="Blocked",
            what_would_help="Help"
        )
        
        signal2 = protocol.create_signal(
            agent_role="tester",
            signal_type="confused",
            what_i_understand="Issue 2",
            what_i_tried=[],
            where_im_stuck="Confused",
            what_would_help="Clarification"
        )
        
        assert len(protocol.get_pending_signals()) == 2
        
        protocol.resolve_signal(signal1.id, "Resolved", "coordinator")
        
        assert len(protocol.get_pending_signals()) == 1
        assert protocol.get_pending_signals()[0].agent_role == "tester"


class TestStruggleProtocolIntegration:
    """Test struggle protocol with other components."""
    
    @pytest.mark.asyncio
    async def test_struggle_after_failed_attempts(self, simulator):
        """Test that struggle is signaled after failed attempts."""
        protocol = MockStruggleProtocol()
        
        attempts = [
            {"action": "First approach", "outcome": "Failed"},
            {"action": "Second approach", "outcome": "Failed"}
        ]
        
        signal = protocol.create_signal(
            agent_role="developer",
            signal_type="repeated_failure",
            what_i_understand="Task requires different approach",
            what_i_tried=attempts,
            where_im_stuck="Both standard approaches failed",
            what_would_help="Alternative strategy or peer consultation"
        )
        
        assert len(signal.what_i_tried) == 2
        assert signal.signal_type == "repeated_failure"
