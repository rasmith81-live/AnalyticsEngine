# =============================================================================
# Multi-Agent Service Test Fixtures
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Shared test fixtures for multi_agent_service tests."""

import pytest
import asyncio
from typing import Dict, Any, List
from datetime import datetime
from uuid import uuid4

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'services', 'backend_services', 'multi_agent_service'))


@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for async tests."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def session_id() -> str:
    """Generate a unique session ID for tests."""
    return f"test_session_{uuid4().hex[:8]}"


@pytest.fixture
def agent_roles() -> List[str]:
    """List of agent roles for testing."""
    return [
        "coordinator",
        "architect", 
        "developer",
        "tester",
        "business_analyst",
        "data_analyst",
        "documenter"
    ]


class MockSimulator:
    """
    Mock simulator service for test data generation.
    
    Per project rules, all tests use the simulator service.
    This mock provides the same interface for unit tests.
    """
    
    def __init__(self):
        self._sessions: Dict[str, Any] = {}
        self._tasks: Dict[str, Any] = {}
        self._artifacts: Dict[str, Any] = {}
    
    async def initialize(self):
        """Initialize the simulator."""
        pass
    
    async def cleanup(self):
        """Cleanup simulator resources."""
        self._sessions.clear()
        self._tasks.clear()
        self._artifacts.clear()
    
    async def create_session(
        self,
        session_type: str = "multi_agent",
        agents: List[str] = None
    ) -> "MockSession":
        """Create a simulated agent session."""
        session_id = f"sim_session_{uuid4().hex[:8]}"
        session = MockSession(
            id=session_id,
            session_type=session_type,
            agents=agents or ["coordinator", "architect", "developer", "tester"],
            created_at=datetime.utcnow()
        )
        self._sessions[session_id] = session
        return session
    
    async def create_task(
        self,
        session_id: str,
        title: str,
        done_when: List[str]
    ) -> "MockTask":
        """Create a simulated blackboard task."""
        task_id = f"sim_task_{uuid4().hex[:8]}"
        task = MockTask(
            id=task_id,
            session_id=session_id,
            title=title,
            done_when=done_when,
            status="open",
            created_at=datetime.utcnow()
        )
        self._tasks[task_id] = task
        return task
    
    async def create_artifact(
        self,
        task_id: str,
        artifact_type: str,
        content: Dict[str, Any]
    ) -> "MockArtifact":
        """Create a simulated artifact."""
        artifact_id = f"sim_artifact_{uuid4().hex[:8]}"
        artifact = MockArtifact(
            id=artifact_id,
            task_id=task_id,
            artifact_type=artifact_type,
            content=content,
            status="pending_review",
            created_at=datetime.utcnow()
        )
        self._artifacts[artifact_id] = artifact
        return artifact


class MockSession:
    """Mock session for testing."""
    
    def __init__(
        self,
        id: str,
        session_type: str,
        agents: List[str],
        created_at: datetime
    ):
        self.id = id
        self.session_type = session_type
        self.agents = agents
        self.created_at = created_at
        self.status = "active"


class MockTask:
    """Mock task for testing."""
    
    def __init__(
        self,
        id: str,
        session_id: str,
        title: str,
        done_when: List[str],
        status: str,
        created_at: datetime
    ):
        self.id = id
        self.session_id = session_id
        self.title = title
        self.done_when = done_when
        self.status = status
        self.created_at = created_at
        self.assigned_to = None


class MockArtifact:
    """Mock artifact for testing."""
    
    def __init__(
        self,
        id: str,
        task_id: str,
        artifact_type: str,
        content: Dict[str, Any],
        status: str,
        created_at: datetime
    ):
        self.id = id
        self.task_id = task_id
        self.artifact_type = artifact_type
        self.content = content
        self.status = status
        self.created_at = created_at


@pytest.fixture
async def simulator():
    """Provide simulator service for test data."""
    sim = MockSimulator()
    await sim.initialize()
    yield sim
    await sim.cleanup()


@pytest.fixture
async def simulated_session(simulator):
    """Create a simulated agent session."""
    return await simulator.create_session(
        session_type="multi_agent",
        agents=["coordinator", "architect", "developer", "tester"]
    )


@pytest.fixture
async def simulated_task(simulator, simulated_session):
    """Create a simulated blackboard task."""
    return await simulator.create_task(
        session_id=simulated_session.id,
        title="Design entity schema",
        done_when=["Schema validated", "Tests pass", "Peer reviewed"]
    )


@pytest.fixture
def mock_contract_config() -> Dict[str, Any]:
    """Mock contract configuration for testing."""
    return {
        "max_assumptions": 3,
        "max_failed_attempts": 2,
        "max_tool_calls": 10,
        "tier_0_rules": [
            "Never fabricate success",
            "Never modify tests to pass",
            "Never expand scope without approval"
        ],
        "tier_1_rules": [
            "Follow state machine transitions",
            "Request approval before execution",
            "Signal struggle within 2 attempts"
        ]
    }
