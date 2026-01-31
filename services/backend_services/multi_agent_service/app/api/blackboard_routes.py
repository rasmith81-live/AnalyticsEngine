# =============================================================================
# Blackboard API Routes
# Based on: Tangi Vass - "Adversarial Vibe Coding" / LIZA System
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""API routes for blackboard operations."""

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any
from datetime import datetime

from ..blackboard.models import (
    BlackboardTask,
    BlackboardArtifact,
    ApprovalGate,
    StruggleSignalEntry,
    TaskStatus,
    ArtifactType,
)
from ..blackboard.operations import BlackboardOperations

router = APIRouter()


class CreateTaskRequest(BaseModel):
    """Request to create a new task."""
    title: str
    description: str
    done_when: List[str] = Field(default_factory=list)
    priority: int = 1
    dependencies: List[str] = Field(default_factory=list)
    tags: List[str] = Field(default_factory=list)


class ClaimTaskRequest(BaseModel):
    """Request to claim a task."""
    agent_role: str


class SubmitArtifactRequest(BaseModel):
    """Request to submit an artifact."""
    agent_role: str
    artifact_type: str
    content: Dict[str, Any]


class ReviewArtifactRequest(BaseModel):
    """Request to review an artifact."""
    reviewer_role: str
    approved: bool
    notes: str


class StruggleSignalRequest(BaseModel):
    """Request to submit a struggle signal."""
    agent_role: str
    signal_type: str
    what_i_understand: str
    what_i_tried: List[Dict[str, str]] = Field(default_factory=list)
    where_im_stuck: str
    what_would_help: str


@router.get("/{session_id}")
async def get_blackboard(
    request: Request,
    session_id: str
) -> Dict[str, Any]:
    """Get the full blackboard state for a session."""
    store = request.app.state.blackboard_store
    blackboard = await store.load_blackboard(session_id)
    
    if not blackboard:
        raise HTTPException(status_code=404, detail=f"Session {session_id} not found")
    
    return blackboard.model_dump(mode="json")


@router.post("/{session_id}/tasks")
async def create_task(
    request: Request,
    session_id: str,
    task_request: CreateTaskRequest,
    creator_role: str = "coordinator"
) -> Dict[str, Any]:
    """Create a new task on the blackboard."""
    store = request.app.state.blackboard_store
    blackboard = await store.get_or_create_blackboard(session_id)
    
    ops = BlackboardOperations(blackboard)
    task = BlackboardTask(
        title=task_request.title,
        description=task_request.description,
        done_when=task_request.done_when,
        priority=task_request.priority,
        dependencies=task_request.dependencies,
        tags=task_request.tags,
        created_by=creator_role
    )
    
    await ops.create_task(creator_role, task)
    await store.save_blackboard(blackboard)
    
    return task.model_dump(mode="json")


@router.get("/{session_id}/tasks")
async def list_tasks(
    request: Request,
    session_id: str,
    status: Optional[str] = None,
    agent_role: Optional[str] = None
) -> List[Dict[str, Any]]:
    """List tasks on the blackboard."""
    store = request.app.state.blackboard_store
    blackboard = await store.load_blackboard(session_id)
    
    if not blackboard:
        raise HTTPException(status_code=404, detail=f"Session {session_id} not found")
    
    tasks = list(blackboard.tasks.values())
    
    if status:
        tasks = [t for t in tasks if t.status.value == status]
    if agent_role:
        tasks = [t for t in tasks if t.assigned_to == agent_role]
    
    return [t.model_dump(mode="json") for t in tasks]


@router.post("/{session_id}/tasks/{task_id}/claim")
async def claim_task(
    request: Request,
    session_id: str,
    task_id: str,
    claim_request: ClaimTaskRequest
) -> Dict[str, Any]:
    """Claim a task for an agent."""
    store = request.app.state.blackboard_store
    blackboard = await store.load_blackboard(session_id)
    
    if not blackboard:
        raise HTTPException(status_code=404, detail=f"Session {session_id} not found")
    
    ops = BlackboardOperations(blackboard)
    
    try:
        task = await ops.claim_task(claim_request.agent_role, task_id)
        await store.save_blackboard(blackboard)
        return task.model_dump(mode="json")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/{session_id}/tasks/{task_id}/artifacts")
async def submit_artifact(
    request: Request,
    session_id: str,
    task_id: str,
    artifact_request: SubmitArtifactRequest
) -> Dict[str, Any]:
    """Submit an artifact for a task."""
    store = request.app.state.blackboard_store
    blackboard = await store.load_blackboard(session_id)
    
    if not blackboard:
        raise HTTPException(status_code=404, detail=f"Session {session_id} not found")
    
    ops = BlackboardOperations(blackboard)
    
    artifact = BlackboardArtifact(
        artifact_type=ArtifactType(artifact_request.artifact_type),
        task_id=task_id,
        content=artifact_request.content,
        created_by=artifact_request.agent_role
    )
    
    try:
        result = await ops.submit_artifact(artifact_request.agent_role, artifact)
        await store.save_blackboard(blackboard)
        return result.model_dump(mode="json")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{session_id}/review-queue")
async def get_review_queue(
    request: Request,
    session_id: str,
    reviewer_role: Optional[str] = None
) -> List[Dict[str, Any]]:
    """Get artifacts awaiting review."""
    store = request.app.state.blackboard_store
    blackboard = await store.load_blackboard(session_id)
    
    if not blackboard:
        raise HTTPException(status_code=404, detail=f"Session {session_id} not found")
    
    if reviewer_role:
        artifacts = blackboard.get_review_queue_for_reviewer(reviewer_role)
    else:
        artifacts = [
            blackboard.artifacts[aid] 
            for aid in blackboard.review_queue 
            if aid in blackboard.artifacts
        ]
    
    return [a.model_dump(mode="json") for a in artifacts]


@router.post("/{session_id}/artifacts/{artifact_id}/review")
async def review_artifact(
    request: Request,
    session_id: str,
    artifact_id: str,
    review_request: ReviewArtifactRequest
) -> Dict[str, Any]:
    """Review an artifact (approve or reject)."""
    store = request.app.state.blackboard_store
    blackboard = await store.load_blackboard(session_id)
    
    if not blackboard:
        raise HTTPException(status_code=404, detail=f"Session {session_id} not found")
    
    ops = BlackboardOperations(blackboard)
    
    try:
        artifact = await ops.review_artifact(
            review_request.reviewer_role,
            artifact_id,
            review_request.approved,
            review_request.notes
        )
        await store.save_blackboard(blackboard)
        return artifact.model_dump(mode="json")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/{session_id}/struggle-signals")
async def submit_struggle_signal(
    request: Request,
    session_id: str,
    signal_request: StruggleSignalRequest
) -> Dict[str, Any]:
    """Submit a struggle signal."""
    store = request.app.state.blackboard_store
    blackboard = await store.get_or_create_blackboard(session_id)
    
    ops = BlackboardOperations(blackboard)
    
    signal = StruggleSignalEntry(
        agent=signal_request.agent_role,
        signal_type=signal_request.signal_type,
        what_i_understand=signal_request.what_i_understand,
        what_i_tried=signal_request.what_i_tried,
        where_im_stuck=signal_request.where_im_stuck,
        what_would_help=signal_request.what_would_help
    )
    
    result = await ops.signal_struggle(signal_request.agent_role, signal)
    await store.save_blackboard(blackboard)
    
    return result.model_dump(mode="json")


@router.get("/{session_id}/struggle-signals")
async def get_struggle_signals(
    request: Request,
    session_id: str,
    unresolved_only: bool = True
) -> List[Dict[str, Any]]:
    """Get struggle signals for a session."""
    store = request.app.state.blackboard_store
    blackboard = await store.load_blackboard(session_id)
    
    if not blackboard:
        raise HTTPException(status_code=404, detail=f"Session {session_id} not found")
    
    if unresolved_only:
        signals = blackboard.get_unresolved_struggle_signals()
    else:
        signals = list(blackboard.struggle_signals.values())
    
    return [s.model_dump(mode="json") for s in signals]


@router.get("/{session_id}/audit-log")
async def get_audit_log(
    request: Request,
    session_id: str,
    limit: int = 100
) -> List[Dict[str, Any]]:
    """Get the audit log for a session."""
    store = request.app.state.blackboard_store
    return await store.get_audit_log(session_id, limit)
