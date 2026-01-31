# =============================================================================
# Blackboard Flow Integration Tests
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Integration tests for blackboard task lifecycle."""

import pytest
from typing import Dict, Any, List
from datetime import datetime
from uuid import uuid4


class MockBlackboard:
    """Mock blackboard for integration testing."""
    
    def __init__(self):
        self._tasks: Dict[str, Any] = {}
        self._artifacts: Dict[str, Any] = {}
        self._reviews: Dict[str, Any] = {}
        self._audit_log: List[Dict[str, Any]] = []
    
    async def create_task(
        self,
        session_id: str,
        title: str,
        done_when: List[str],
        creator_role: str = "coordinator"
    ) -> Dict[str, Any]:
        """Create a task on the blackboard."""
        task_id = f"task_{uuid4().hex[:8]}"
        task = {
            "id": task_id,
            "session_id": session_id,
            "title": title,
            "done_when": done_when,
            "status": "open",
            "created_by": creator_role,
            "assigned_to": None,
            "created_at": datetime.utcnow().isoformat()
        }
        self._tasks[task_id] = task
        self._log_action("task_created", task)
        return task
    
    async def claim_task(
        self,
        task_id: str,
        agent_role: str
    ) -> Dict[str, Any]:
        """Claim a task for an agent."""
        if task_id not in self._tasks:
            raise ValueError(f"Task {task_id} not found")
        
        task = self._tasks[task_id]
        if task["status"] != "open":
            raise ValueError(f"Task {task_id} is not open")
        
        task["status"] = "in_progress"
        task["assigned_to"] = agent_role
        self._log_action("task_claimed", task)
        return task
    
    async def submit_artifact(
        self,
        task_id: str,
        artifact_type: str,
        content: Dict[str, Any],
        creator_role: str
    ) -> Dict[str, Any]:
        """Submit an artifact for a task."""
        if task_id not in self._tasks:
            raise ValueError(f"Task {task_id} not found")
        
        artifact_id = f"artifact_{uuid4().hex[:8]}"
        artifact = {
            "id": artifact_id,
            "task_id": task_id,
            "artifact_type": artifact_type,
            "content": content,
            "status": "pending_review",
            "created_by": creator_role,
            "created_at": datetime.utcnow().isoformat()
        }
        self._artifacts[artifact_id] = artifact
        self._log_action("artifact_submitted", artifact)
        return artifact
    
    async def submit_review(
        self,
        artifact_id: str,
        reviewer_role: str,
        verdict: str,
        comments: str = ""
    ) -> Dict[str, Any]:
        """Submit a review for an artifact."""
        if artifact_id not in self._artifacts:
            raise ValueError(f"Artifact {artifact_id} not found")
        
        artifact = self._artifacts[artifact_id]
        
        if artifact["created_by"] == reviewer_role:
            raise ValueError("Self-review is not allowed")
        
        review_id = f"review_{uuid4().hex[:8]}"
        review = {
            "id": review_id,
            "artifact_id": artifact_id,
            "reviewer": reviewer_role,
            "verdict": verdict,
            "comments": comments,
            "created_at": datetime.utcnow().isoformat()
        }
        self._reviews[review_id] = review
        
        if verdict == "approved":
            artifact["status"] = "approved"
            task = self._tasks[artifact["task_id"]]
            task["status"] = "done"
        elif verdict == "rejected":
            artifact["status"] = "rejected"
        
        self._log_action("review_submitted", review)
        return review
    
    async def get_task(self, task_id: str) -> Dict[str, Any]:
        """Get a task by ID."""
        if task_id not in self._tasks:
            raise ValueError(f"Task {task_id} not found")
        return self._tasks[task_id]
    
    async def get_artifact(self, artifact_id: str) -> Dict[str, Any]:
        """Get an artifact by ID."""
        if artifact_id not in self._artifacts:
            raise ValueError(f"Artifact {artifact_id} not found")
        return self._artifacts[artifact_id]
    
    def _log_action(self, action: str, data: Dict[str, Any]):
        """Log an action to the audit log."""
        self._audit_log.append({
            "action": action,
            "data": data,
            "timestamp": datetime.utcnow().isoformat()
        })


@pytest.fixture
def blackboard():
    """Provide a mock blackboard for testing."""
    return MockBlackboard()


class TestBlackboardTaskFlow:
    """Test complete task lifecycle through blackboard."""
    
    @pytest.mark.asyncio
    async def test_task_creation_to_completion(self, simulated_session, blackboard):
        """Test complete task flow from creation to completion."""
        task = await blackboard.create_task(
            session_id=simulated_session.id,
            title="Implement user entity",
            done_when=["Schema created", "Tests written", "Reviewed"]
        )
        assert task["status"] == "open"
        
        claimed = await blackboard.claim_task(
            task_id=task["id"],
            agent_role="developer"
        )
        assert claimed["status"] == "in_progress"
        assert claimed["assigned_to"] == "developer"
        
        artifact = await blackboard.submit_artifact(
            task_id=task["id"],
            artifact_type="schema",
            content={"name": "User", "fields": ["id", "name", "email"]},
            creator_role="developer"
        )
        assert artifact["status"] == "pending_review"
        
        review = await blackboard.submit_review(
            artifact_id=artifact["id"],
            reviewer_role="architect",
            verdict="approved"
        )
        assert review["verdict"] == "approved"
        
        final_task = await blackboard.get_task(task["id"])
        assert final_task["status"] == "done"
    
    @pytest.mark.asyncio
    async def test_self_review_blocked(self, simulated_session, blackboard):
        """Test that self-review is blocked."""
        task = await blackboard.create_task(
            session_id=simulated_session.id,
            title="Test task",
            done_when=["Completed"]
        )
        
        await blackboard.claim_task(task["id"], "developer")
        
        artifact = await blackboard.submit_artifact(
            task_id=task["id"],
            artifact_type="code",
            content={"file": "test.py"},
            creator_role="developer"
        )
        
        with pytest.raises(ValueError, match="Self-review is not allowed"):
            await blackboard.submit_review(
                artifact_id=artifact["id"],
                reviewer_role="developer",
                verdict="approved"
            )
    
    @pytest.mark.asyncio
    async def test_rejection_keeps_task_open(self, simulated_session, blackboard):
        """Test that rejection keeps task in progress."""
        task = await blackboard.create_task(
            session_id=simulated_session.id,
            title="Test task",
            done_when=["Completed"]
        )
        
        await blackboard.claim_task(task["id"], "developer")
        
        artifact = await blackboard.submit_artifact(
            task_id=task["id"],
            artifact_type="code",
            content={"file": "test.py"},
            creator_role="developer"
        )
        
        review = await blackboard.submit_review(
            artifact_id=artifact["id"],
            reviewer_role="architect",
            verdict="rejected",
            comments="Missing error handling"
        )
        
        assert review["verdict"] == "rejected"
        
        final_artifact = await blackboard.get_artifact(artifact["id"])
        assert final_artifact["status"] == "rejected"
        
        final_task = await blackboard.get_task(task["id"])
        assert final_task["status"] == "in_progress"
    
    @pytest.mark.asyncio
    async def test_audit_log_maintained(self, simulated_session, blackboard):
        """Test that audit log captures all actions."""
        task = await blackboard.create_task(
            session_id=simulated_session.id,
            title="Test task",
            done_when=["Completed"]
        )
        
        await blackboard.claim_task(task["id"], "developer")
        
        artifact = await blackboard.submit_artifact(
            task_id=task["id"],
            artifact_type="code",
            content={},
            creator_role="developer"
        )
        
        await blackboard.submit_review(
            artifact_id=artifact["id"],
            reviewer_role="architect",
            verdict="approved"
        )
        
        assert len(blackboard._audit_log) == 4
        actions = [entry["action"] for entry in blackboard._audit_log]
        assert actions == [
            "task_created",
            "task_claimed",
            "artifact_submitted",
            "review_submitted"
        ]
