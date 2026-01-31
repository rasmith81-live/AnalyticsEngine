# =============================================================================
# Amendment System for Self-Correcting Contracts
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
#
# "Each gap discovered is an amendment opportunity. The agent can propose
# surgical improvements to the contract. The system becomes self-correcting
# under supervision."
# =============================================================================
"""Amendment system for contract evolution under human supervision."""

from enum import Enum
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime
import uuid

from .tier_rules import RuleTier, TierRule


class AmendmentStatus(str, Enum):
    """Status of an amendment proposal."""
    PROPOSED = "proposed"
    UNDER_REVIEW = "under_review"
    APPROVED = "approved"
    REJECTED = "rejected"
    IMPLEMENTED = "implemented"


class AmendmentType(str, Enum):
    """Type of amendment being proposed."""
    NEW_RULE = "new_rule"
    MODIFY_RULE = "modify_rule"
    DELETE_RULE = "delete_rule"
    NEW_TRIGGER = "new_trigger"
    MODIFY_THRESHOLD = "modify_threshold"
    NEW_GATE = "new_gate"


class AmendmentProposal(BaseModel):
    """
    A proposed amendment to the contract.
    
    From the article:
    "An amendment requires rationale for partial completion—not a correction
    to agent behavior. Each gap discovered is an amendment opportunity."
    """
    proposal_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    
    # Who proposed it
    proposed_by_agent: str
    session_id: str
    
    # What kind of amendment
    amendment_type: AmendmentType
    
    # The gap that triggered this proposal
    gap_description: str
    
    # What the amendment would add/change
    proposed_change: Dict[str, Any]
    
    # Why this amendment is needed
    rationale: str
    
    # Example of when this would have helped
    example_scenario: Optional[str] = None
    
    # Status tracking
    status: AmendmentStatus = AmendmentStatus.PROPOSED
    
    # Review tracking
    reviewed_by: Optional[str] = None
    review_notes: Optional[str] = None
    reviewed_at: Optional[datetime] = None
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.utcnow)
    implemented_at: Optional[datetime] = None
    
    # Version tracking
    contract_version_before: Optional[str] = None
    contract_version_after: Optional[str] = None


class PostHocDiscoveryProtocol(BaseModel):
    """
    Protocol for discovering gaps that require amendments.
    
    Triggers when:
    - Agent defers DoD items with rationale
    - Agent signals partial completion
    - Agent identifies missing contract coverage
    """
    deferred_items: List[Dict[str, str]] = Field(default_factory=list)
    partial_completions: List[Dict[str, str]] = Field(default_factory=list)
    identified_gaps: List[str] = Field(default_factory=list)
    
    def record_deferral(
        self,
        item: str,
        rationale: str,
        agent_role: str
    ) -> Optional[AmendmentProposal]:
        """
        Record a DoD item deferral.
        
        Returns an amendment proposal if the deferral suggests a gap.
        """
        self.deferred_items.append({
            "item": item,
            "rationale": rationale,
            "agent_role": agent_role,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        # Check if this suggests an amendment
        if "not in contract" in rationale.lower() or "missing rule" in rationale.lower():
            return AmendmentProposal(
                proposed_by_agent=agent_role,
                session_id="discovery",
                amendment_type=AmendmentType.NEW_RULE,
                gap_description=f"Deferred item suggests missing rule: {item}",
                proposed_change={"suggested_rule": item},
                rationale=rationale,
                example_scenario=f"Agent deferred '{item}' because: {rationale}"
            )
        
        return None
    
    def record_partial_completion(
        self,
        completed: List[str],
        remaining: List[str],
        rationale: str,
        agent_role: str
    ) -> Optional[AmendmentProposal]:
        """
        Record a partial completion signal.
        
        Returns an amendment proposal if partial completion suggests a gap.
        """
        self.partial_completions.append({
            "completed": completed,
            "remaining": remaining,
            "rationale": rationale,
            "agent_role": agent_role,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        # Analyze if this suggests missing infrastructure
        if "no mechanism" in rationale.lower() or "contract doesn't cover" in rationale.lower():
            return AmendmentProposal(
                proposed_by_agent=agent_role,
                session_id="discovery",
                amendment_type=AmendmentType.NEW_RULE,
                gap_description=f"Partial completion due to missing mechanism",
                proposed_change={"remaining_items": remaining},
                rationale=rationale
            )
        
        return None


class AmendmentRegistry:
    """
    Registry of all amendments with version tracking.
    
    The contract evolves through amendments, each reviewed and
    approved by a human supervisor.
    """
    
    def __init__(self):
        self.proposals: Dict[str, AmendmentProposal] = {}
        self.approved_amendments: List[AmendmentProposal] = []
        self.contract_version = "1.0.0"
        self.version_history: List[Dict[str, Any]] = []
        self.discovery_protocol = PostHocDiscoveryProtocol()
    
    def submit_proposal(self, proposal: AmendmentProposal) -> str:
        """Submit a new amendment proposal. Returns the proposal ID."""
        proposal.contract_version_before = self.contract_version
        self.proposals[proposal.proposal_id] = proposal
        return proposal.proposal_id
    
    def review_proposal(
        self,
        proposal_id: str,
        approved: bool,
        reviewer: str,
        notes: str
    ) -> AmendmentProposal:
        """
        Review an amendment proposal.
        
        Only human supervisors can approve amendments.
        """
        if proposal_id not in self.proposals:
            raise ValueError(f"Proposal {proposal_id} not found")
        
        proposal = self.proposals[proposal_id]
        proposal.status = AmendmentStatus.APPROVED if approved else AmendmentStatus.REJECTED
        proposal.reviewed_by = reviewer
        proposal.review_notes = notes
        proposal.reviewed_at = datetime.utcnow()
        
        if approved:
            self.approved_amendments.append(proposal)
        
        return proposal
    
    def implement_amendment(
        self,
        proposal_id: str,
        contract_rules: Any  # ContractRules
    ) -> str:
        """
        Implement an approved amendment into the contract.
        
        Returns the new contract version.
        """
        if proposal_id not in self.proposals:
            raise ValueError(f"Proposal {proposal_id} not found")
        
        proposal = self.proposals[proposal_id]
        
        if proposal.status != AmendmentStatus.APPROVED:
            raise ValueError(f"Proposal {proposal_id} is not approved")
        
        # Increment version
        old_version = self.contract_version
        major, minor, patch = map(int, old_version.split("."))
        
        if proposal.amendment_type in [AmendmentType.NEW_RULE, AmendmentType.NEW_TRIGGER]:
            minor += 1
            patch = 0
        else:
            patch += 1
        
        new_version = f"{major}.{minor}.{patch}"
        
        # Record version history
        self.version_history.append({
            "from_version": old_version,
            "to_version": new_version,
            "amendment_id": proposal_id,
            "amendment_type": proposal.amendment_type.value,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        # Update contract (implementation depends on amendment type)
        self._apply_amendment(proposal, contract_rules)
        
        # Update proposal status
        proposal.status = AmendmentStatus.IMPLEMENTED
        proposal.contract_version_after = new_version
        proposal.implemented_at = datetime.utcnow()
        
        self.contract_version = new_version
        return new_version
    
    def _apply_amendment(
        self,
        proposal: AmendmentProposal,
        contract_rules: Any
    ) -> None:
        """Apply the amendment to the contract rules."""
        if proposal.amendment_type == AmendmentType.NEW_RULE:
            # Add a new rule
            change = proposal.proposed_change
            tier = change.get("tier", RuleTier.TIER_2)
            new_rule = TierRule(
                rule_id=f"A-{proposal.proposal_id[:8]}",
                tier=tier,
                description=change.get("description", change.get("suggested_rule", "")),
                rationale=proposal.rationale
            )
            
            # Add to appropriate tier
            tier_list = contract_rules.get_rules_for_tier(tier)
            tier_list.append(new_rule)
    
    def get_pending_proposals(self) -> List[AmendmentProposal]:
        """Get all proposals pending review."""
        return [
            p for p in self.proposals.values()
            if p.status == AmendmentStatus.PROPOSED
        ]
    
    def get_amendment_statistics(self) -> Dict[str, Any]:
        """Get statistics about amendments."""
        return {
            "total_proposals": len(self.proposals),
            "approved": len([p for p in self.proposals.values() if p.status == AmendmentStatus.APPROVED]),
            "rejected": len([p for p in self.proposals.values() if p.status == AmendmentStatus.REJECTED]),
            "implemented": len([p for p in self.proposals.values() if p.status == AmendmentStatus.IMPLEMENTED]),
            "pending": len(self.get_pending_proposals()),
            "current_version": self.contract_version,
            "version_count": len(self.version_history)
        }
