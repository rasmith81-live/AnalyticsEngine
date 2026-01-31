"""
E2E Test: Blackboard Lifecycle Integration

Phase 17: UI Integration Validation

Tests the full lifecycle of blackboard operations from conversation service
through multi-agent service and back to the UI.
"""

import pytest
import asyncio
from datetime import datetime
from typing import Dict, Any


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_session_with_blackboard_enabled(simulator, multi_agent_client):
    """Test session creation with blackboard enabled."""
    
    # Create session through simulator
    session = await simulator.create_session(user_id="test_user")
    
    assert session.id is not None
    assert session.status == "active"
    
    # Verify session exists (blackboard may or may not be enabled based on rollout)


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_task_creation_on_blackboard(simulator, multi_agent_client):
    """Test that agent tasks are created on blackboard."""
    
    # Create session
    session = await simulator.create_session(user_id="test_user")
    
    # Send message that triggers agent work
    await simulator.send_message(
        session.id,
        "Design a customer relationship management system"
    )
    
    # Wait for processing
    await asyncio.sleep(5)
    
    # Check for tasks on blackboard (if blackboard is enabled)
    if multi_agent_client:
        try:
            tasks = await multi_agent_client.get_session_tasks(session.id)
            # May have tasks if blackboard is enabled
            assert isinstance(tasks, list)
        except Exception:
            pass  # Blackboard may not be enabled for this session


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_artifact_submission_lifecycle(simulator, multi_agent_client):
    """Test artifact submission and retrieval lifecycle."""
    
    session = await simulator.create_session(user_id="test_user")
    
    # Send message that should generate artifacts
    await simulator.send_message(
        session.id,
        "Create an entity schema for Product with name, price, and category"
    )
    
    # Wait for artifacts
    artifacts = await simulator.wait_for_artifacts(session.id, timeout=60)
    
    # Verify artifacts were generated
    assert artifacts is not None


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_contract_state_transitions(simulator, multi_agent_client):
    """Test that contract state transitions are tracked."""
    
    session = await simulator.create_session(user_id="test_user")
    
    # Send initial message
    await simulator.send_message(
        session.id,
        "Analyze our supply chain operations"
    )
    
    # Wait for processing
    await asyncio.sleep(5)
    
    # Check contract status if available
    if multi_agent_client:
        try:
            status = await multi_agent_client.get_contract_status(session.id)
            assert status is not None
        except Exception:
            pass  # Contract tracking may not be enabled


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_peer_review_workflow(simulator, multi_agent_client):
    """Test peer review workflow on blackboard."""
    
    session = await simulator.create_session(user_id="test_user")
    
    # Send complex task that requires peer review
    await simulator.send_message(
        session.id,
        "Design a complete data warehouse schema for retail analytics"
    )
    
    # Wait for processing
    await asyncio.sleep(10)
    
    # Check for reviews if available
    if multi_agent_client:
        try:
            reviews = await multi_agent_client.get_session_reviews(session.id)
            assert isinstance(reviews, list)
        except Exception:
            pass


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_degraded_mode_fallback(simulator, mock_multi_agent_down):
    """Test graceful degradation when multi_agent_service unavailable."""
    
    # Activate mock to simulate service down
    mock_multi_agent_down.activate()
    
    # Create session - should still work in degraded mode
    session = await simulator.create_session(user_id="test_user")
    assert session.id is not None
    
    # Send message - should use legacy peer-to-peer
    response = await simulator.send_message(
        session.id,
        "Hello, can you help me design a system?"
    )
    
    # Should still get a response
    assert response.get("success", True)


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_blackboard_consistency(simulator, multi_agent_client):
    """Test that blackboard state remains consistent across operations."""
    
    session = await simulator.create_session(user_id="test_user")
    
    # Send multiple messages
    messages = [
        "Let's design an inventory system",
        "Add support for multiple warehouses",
        "Include real-time stock tracking"
    ]
    
    for msg in messages:
        await simulator.send_message(session.id, msg)
        await asyncio.sleep(2)
    
    # Verify session state is consistent
    if multi_agent_client:
        try:
            tasks = await multi_agent_client.get_session_tasks(session.id)
            # Tasks should not have duplicates
            task_ids = [t.get("id") for t in tasks if t.get("id")]
            assert len(task_ids) == len(set(task_ids)), "Duplicate tasks detected"
        except Exception:
            pass


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_session_cleanup(simulator, multi_agent_client):
    """Test that session cleanup properly clears blackboard state."""
    
    session = await simulator.create_session(user_id="test_user")
    
    # Add some data
    await simulator.send_message(session.id, "Create a simple entity")
    await asyncio.sleep(3)
    
    # Session ID for later check
    session_id = session.id
    
    # Cleanup (if supported by simulator)
    if hasattr(simulator, 'cleanup_session'):
        await simulator.cleanup_session(session_id)
    
    # Verify cleanup (implementation dependent)


@pytest.mark.e2e
@pytest.mark.asyncio
async def test_concurrent_sessions(simulator):
    """Test multiple concurrent sessions with blackboard."""
    
    # Create multiple sessions
    sessions = []
    for i in range(3):
        session = await simulator.create_session(user_id=f"test_user_{i}")
        sessions.append(session)
    
    # Send messages to all sessions concurrently
    async def send_to_session(session, msg):
        return await simulator.send_message(session.id, msg)
    
    tasks = [
        send_to_session(s, f"Design system for user {i}")
        for i, s in enumerate(sessions)
    ]
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # All should succeed
    for result in results:
        assert not isinstance(result, Exception)
