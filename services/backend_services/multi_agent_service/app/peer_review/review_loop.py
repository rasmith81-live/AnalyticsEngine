# =============================================================================
# Review Loop
# Based on: Tangi Vass - "Adversarial Vibe Coding" / LIZA System
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Review loop with rejection handling."""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

from .pairs import get_reviewer_for_role, get_review_focus


class ReviewDecision(str, Enum):
    """Review decision options."""
    APPROVED = "approved"
    REJECTED = "rejected"
    NEEDS_REVISION = "needs_revision"


class ReviewResult(BaseModel):
    """Result of a review."""
    artifact_id: str
    task_id: str
    creator_role: str
    reviewer_role: str
    decision: ReviewDecision
    feedback: str
    review_focus: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    revision_count: int = 0


class ReviewLoop:
    """
    Manages the review cycle with proper rejection handling.
    
    From the article:
    "The Coder can't merge their own work—ever. The Reviewer can't
    implement code—ever. This separation makes peer collaboration
    meaningful."
    
    Key rules:
    1. Creator cannot review their own work (Tier 0)
    2. Only designated reviewer can review
    3. Two failures = task is poorly defined → escalate
    """
    
    MAX_REVISIONS = 3
    
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.reviews: Dict[str, List[ReviewResult]] = {}  # artifact_id -> reviews
        self.pending_reviews: List[str] = []  # artifact_ids awaiting review
    
    def submit_for_review(
        self,
        artifact_id: str,
        task_id: str,
        creator_role: str
    ) -> str:
        """Submit an artifact for review."""
        self.pending_reviews.append(artifact_id)
        
        # Initialize review history for this artifact
        if artifact_id not in self.reviews:
            self.reviews[artifact_id] = []
        
        return get_reviewer_for_role(creator_role)
    
    def process_review(
        self,
        artifact_id: str,
        task_id: str,
        creator_role: str,
        reviewer_role: str,
        decision: ReviewDecision,
        feedback: str
    ) -> ReviewResult:
        """Process a review decision."""
        # Validate reviewer
        expected_reviewer = get_reviewer_for_role(creator_role)
        if reviewer_role != expected_reviewer and reviewer_role != "coordinator":
            raise ValueError(
                f"Reviewer {reviewer_role} is not authorized. "
                f"Expected {expected_reviewer}."
            )
        
        # Check for self-review (Tier 0 violation)
        if reviewer_role == creator_role:
            raise ValueError("Cannot review own work (Tier 0 violation)")
        
        # Get revision count
        revision_count = len(self.reviews.get(artifact_id, []))
        
        result = ReviewResult(
            artifact_id=artifact_id,
            task_id=task_id,
            creator_role=creator_role,
            reviewer_role=reviewer_role,
            decision=decision,
            feedback=feedback,
            review_focus=get_review_focus(creator_role),
            revision_count=revision_count
        )
        
        # Store the review
        if artifact_id not in self.reviews:
            self.reviews[artifact_id] = []
        self.reviews[artifact_id].append(result)
        
        # Remove from pending if decided
        if artifact_id in self.pending_reviews:
            self.pending_reviews.remove(artifact_id)
        
        return result
    
    def get_review_history(self, artifact_id: str) -> List[ReviewResult]:
        """Get review history for an artifact."""
        return self.reviews.get(artifact_id, [])
    
    def get_rejection_count(self, artifact_id: str) -> int:
        """Get how many times an artifact has been rejected."""
        reviews = self.reviews.get(artifact_id, [])
        return sum(1 for r in reviews if r.decision == ReviewDecision.REJECTED)
    
    def should_escalate(self, task_id: str, failed_by: List[str]) -> bool:
        """
        Check if a task should be escalated.
        
        Two-failures rule: If two different agents fail the same task,
        the task is presumed to be poorly defined.
        """
        unique_failures = set(failed_by)
        return len(unique_failures) >= 2
    
    def get_pending_reviews(self) -> List[str]:
        """Get artifact IDs awaiting review."""
        return self.pending_reviews.copy()
    
    def get_review_metrics(self) -> Dict[str, Any]:
        """Get metrics about the review process."""
        total_reviews = sum(len(reviews) for reviews in self.reviews.values())
        approvals = sum(
            1 for reviews in self.reviews.values()
            for r in reviews if r.decision == ReviewDecision.APPROVED
        )
        rejections = sum(
            1 for reviews in self.reviews.values()
            for r in reviews if r.decision == ReviewDecision.REJECTED
        )
        
        return {
            "total_reviews": total_reviews,
            "approvals": approvals,
            "rejections": rejections,
            "pending": len(self.pending_reviews),
            "rejection_rate": rejections / total_reviews if total_reviews > 0 else 0,
            "first_pass_approval_rate": approvals / len(self.reviews) if self.reviews else 0
        }
