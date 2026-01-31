# =============================================================================
# Blackboard Data Models
# Based on: Tangi Vass - "Adversarial Vibe Coding" / LIZA System
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Data models for the blackboard architecture."""

from enum import Enum
from typing import Dict, List, Optional, Any, Literal
from pydantic import BaseModel, Field
from datetime import datetime
import uuid


class TaskStatus(str, Enum):
    """Status of a task on the blackboard."""
    UNCLAIMED = "unclaimed"
    CLAIMED = "claimed"
    IN_PROGRESS = "in_progress"
    READY_FOR_REVIEW = "ready_for_review"
    IN_REVIEW = "in_review"
    APPROVED = "approved"
    REJECTED = "rejected"
    MERGED = "merged"
    BLOCKED = "blocked"


class ArtifactType(str, Enum):
    """Type of artifact produced by an agent."""
    ENTITY_DESIGN = "entity_design"
    KPI_DEFINITION = "kpi_definition"
    SCHEMA = "schema"
    CODE = "code"
    TEST = "test"
    DOCUMENTATION = "documentation"
    PROPOSAL = "proposal"
    ANALYSIS = "analysis"
    SIMULATION = "simulation"
    MAPPING = "mapping"
    STRATEGY = "strategy"
    COMPLIANCE = "compliance"


class BlackboardTask(BaseModel):
    """
    A task on the blackboard that agents can claim and work on.
    
    Key features:
    - Falsifiable done_when criteria
    - Assigned reviewer for adversarial pairing
    - Failure tracking for two-failures rule
    """
    task_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    created_by: str  # Agent role that created the task
    assigned_to: Optional[str] = None  # Agent role that claimed it
    reviewer: Optional[str] = None  # Agent role that will review
    status: TaskStatus = TaskStatus.UNCLAIMED
    
    # Falsifiable completion criteria
    done_when: List[str] = Field(default_factory=list)
    
    # Task metadata
    priority: int = 1  # 1 = highest
    dependencies: List[str] = Field(default_factory=list)  # task_ids
    tags: List[str] = Field(default_factory=list)
    
    # State tracking
    created_at: datetime = Field(default_factory=datetime.utcnow)
    claimed_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    
    # Failure tracking (for the "two failures = bad task" rule)
    failure_count: int = 0
    failed_by: List[str] = Field(default_factory=list)
    failure_reasons: List[str] = Field(default_factory=list)


class BlackboardArtifact(BaseModel):
    """
    An artifact produced by an agent and stored on the blackboard.
    
    Key features:
    - Full provenance tracking
    - Review status with adversarial review
    - Version control for revisions
    """
    artifact_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    artifact_type: ArtifactType
    task_id: str  # The task that produced this artifact
    
    # Content
    content: Dict[str, Any]  # The actual artifact data
    
    # Provenance
    created_by: str  # Agent role
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Review status
    reviewed_by: Optional[str] = None
    review_status: Optional[Literal["pending", "approved", "rejected"]] = "pending"
    review_notes: Optional[str] = None
    reviewed_at: Optional[datetime] = None
    
    # Version control
    version: int = 1
    parent_artifact_id: Optional[str] = None  # For revisions


class ApprovalGate(BaseModel):
    """
    A pending approval request on the blackboard.
    
    Before any state-changing action, agents must submit an approval request.
    """
    gate_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    requesting_agent: str
    task_id: Optional[str] = None
    
    # What's being approved
    intent: str
    scope: str
    approach: str
    consequences: List[str] = Field(default_factory=list)
    risks: List[str] = Field(default_factory=list)
    validation_plan: str
    assumptions: List[str] = Field(default_factory=list)
    
    # Approval status
    status: Literal["pending", "approved", "rejected"] = "pending"
    decided_by: Optional[str] = None
    decided_at: Optional[datetime] = None
    decision_rationale: Optional[str] = None
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class StruggleSignalEntry(BaseModel):
    """
    A struggle signal posted by an agent.
    
    The struggle protocol transforms deception risk into collaboration opportunity.
    """
    signal_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    agent: str
    task_id: Optional[str] = None
    signal_type: Literal["blocked", "confused", "conflicting_evidence", "resource_missing"]
    
    what_i_understand: str
    what_i_tried: List[Dict[str, str]] = Field(default_factory=list)
    where_im_stuck: str
    what_would_help: str
    
    # Resolution
    resolved: bool = False
    resolved_by: Optional[str] = None
    resolution: Optional[str] = None
    resolved_at: Optional[datetime] = None
    
    created_at: datetime = Field(default_factory=datetime.utcnow)


class AuditLogEntry(BaseModel):
    """
    Immutable audit log entry for all blackboard operations.
    
    Everything visible, everything auditable.
    """
    log_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    
    # Who did what
    agent: str
    action: str  # "claim_task", "submit_artifact", "approve", "reject", etc.
    
    # What was affected
    entity_type: str  # "task", "artifact", "approval_gate", "struggle_signal"
    entity_id: str
    
    # State change
    previous_state: Optional[Dict[str, Any]] = None
    new_state: Dict[str, Any]
    
    # Contract compliance
    contract_rules_checked: List[str] = Field(default_factory=list)
    violations_detected: List[str] = Field(default_factory=list)
    
    # Session tracking
    session_id: str


class AgentBlackboard(BaseModel):
    """
    The shared blackboard that all agents read from and write to.
    
    Replaces pub/sub with a centralized, auditable state store.
    """
    session_id: str
    
    # Core state
    tasks: Dict[str, BlackboardTask] = Field(default_factory=dict)
    artifacts: Dict[str, BlackboardArtifact] = Field(default_factory=dict)
    approval_gates: Dict[str, ApprovalGate] = Field(default_factory=dict)
    struggle_signals: Dict[str, StruggleSignalEntry] = Field(default_factory=dict)
    
    # Review queue
    review_queue: List[str] = Field(default_factory=list)  # artifact_ids awaiting review
    
    # Session context (shared knowledge)
    session_context: Dict[str, Any] = Field(default_factory=dict)
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_modified: datetime = Field(default_factory=datetime.utcnow)
    
    def get_unclaimed_tasks(self) -> List[BlackboardTask]:
        """Get all unclaimed tasks."""
        return [t for t in self.tasks.values() if t.status == TaskStatus.UNCLAIMED]
    
    def get_tasks_for_agent(self, agent_role: str) -> List[BlackboardTask]:
        """Get all tasks assigned to an agent."""
        return [t for t in self.tasks.values() if t.assigned_to == agent_role]
    
    def get_review_queue_for_reviewer(self, reviewer_role: str) -> List[BlackboardArtifact]:
        """Get artifacts awaiting review by a specific reviewer."""
        artifacts = []
        for artifact_id in self.review_queue:
            artifact = self.artifacts.get(artifact_id)
            if artifact:
                task = self.tasks.get(artifact.task_id)
                if task and task.reviewer == reviewer_role:
                    artifacts.append(artifact)
        return artifacts
    
    def get_unresolved_struggle_signals(self) -> List[StruggleSignalEntry]:
        """Get all unresolved struggle signals."""
        return [s for s in self.struggle_signals.values() if not s.resolved]
