# =============================================================================
# Adversarial Pairing
# Based on: Tangi Vass - "Adversarial Vibe Coding" / LIZA System
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Adversarial pairing for peer review."""

from typing import Dict, List, Optional
from pydantic import BaseModel


class AdversarialPair(BaseModel):
    """An adversarial creator-reviewer pair."""
    creator: str
    reviewer: str
    artifact_type: str
    review_focus: str


# Complete adversarial pairing for all 27+ agents
ADVERSARIAL_PAIRS: Dict[str, AdversarialPair] = {
    # Strategy & Analysis Layer
    "business_strategist": AdversarialPair(
        creator="business_strategist",
        reviewer="business_analyst",
        artifact_type="Strategic frameworks",
        review_focus="Industry validity"
    ),
    "business_analyst": AdversarialPair(
        creator="business_analyst",
        reviewer="business_strategist",
        artifact_type="KPI requirements",
        review_focus="Strategic alignment"
    ),
    "data_analyst": AdversarialPair(
        creator="data_analyst",
        reviewer="data_scientist",
        artifact_type="KPI calculations",
        review_focus="Statistical validity"
    ),
    "data_scientist": AdversarialPair(
        creator="data_scientist",
        reviewer="data_analyst",
        artifact_type="ML specifications",
        review_focus="Practicality"
    ),
    "operations_manager": AdversarialPair(
        creator="operations_manager",
        reviewer="data_scientist",
        artifact_type="Optimization plans",
        review_focus="Statistical backing"
    ),
    "mapping_specialist": AdversarialPair(
        creator="mapping_specialist",
        reviewer="architect",
        artifact_type="Source mappings",
        review_focus="Schema compatibility"
    ),
    "document_analyzer": AdversarialPair(
        creator="document_analyzer",
        reviewer="business_analyst",
        artifact_type="Extracted entities",
        review_focus="Domain accuracy"
    ),
    "competitive_analyst": AdversarialPair(
        creator="competitive_analyst",
        reviewer="business_strategist",
        artifact_type="Market analysis",
        review_focus="Strategic coherence"
    ),
    
    # Technical Design Layer
    "architect": AdversarialPair(
        creator="architect",
        reviewer="data_governance_specialist",
        artifact_type="Entity/aggregate designs",
        review_focus="Governance compliance"
    ),
    "developer": AdversarialPair(
        creator="developer",
        reviewer="tester",
        artifact_type="Code artifacts",
        review_focus="Quality/correctness"
    ),
    "tester": AdversarialPair(
        creator="tester",
        reviewer="developer",
        artifact_type="Test specifications",
        review_focus="Coverage adequacy"
    ),
    "documenter": AdversarialPair(
        creator="documenter",
        reviewer="architect",
        artifact_type="Documentation",
        review_focus="Technical accuracy"
    ),
    "deployment_specialist": AdversarialPair(
        creator="deployment_specialist",
        reviewer="itil_manager",
        artifact_type="Infrastructure configs",
        review_focus="Change management"
    ),
    "ui_designer": AdversarialPair(
        creator="ui_designer",
        reviewer="tester",
        artifact_type="Dashboard designs",
        review_focus="Accessibility/usability"
    ),
    "itil_manager": AdversarialPair(
        creator="itil_manager",
        reviewer="risk_compliance_officer",
        artifact_type="Service configs",
        review_focus="Risk compliance"
    ),
    "connection_specialist": AdversarialPair(
        creator="connection_specialist",
        reviewer="tester",
        artifact_type="Integration code",
        review_focus="Error handling"
    ),
    
    # Business Operations Layer
    "sales_manager": AdversarialPair(
        creator="sales_manager",
        reviewer="accountant",
        artifact_type="Pipeline data",
        review_focus="Financial accuracy"
    ),
    "marketing_manager": AdversarialPair(
        creator="marketing_manager",
        reviewer="data_analyst",
        artifact_type="Campaign metrics",
        review_focus="Data validity"
    ),
    "accountant": AdversarialPair(
        creator="accountant",
        reviewer="sales_manager",
        artifact_type="Financial docs",
        review_focus="Business context"
    ),
    "customer_success_manager": AdversarialPair(
        creator="customer_success_manager",
        reviewer="sales_manager",
        artifact_type="Health assessments",
        review_focus="Client relationship"
    ),
    "hr_talent_analyst": AdversarialPair(
        creator="hr_talent_analyst",
        reviewer="data_governance_specialist",
        artifact_type="People analytics",
        review_focus="Privacy compliance"
    ),
    "supply_chain_analyst": AdversarialPair(
        creator="supply_chain_analyst",
        reviewer="risk_compliance_officer",
        artifact_type="Supply chain metrics",
        review_focus="Risk assessment"
    ),
    "risk_compliance_officer": AdversarialPair(
        creator="risk_compliance_officer",
        reviewer="itil_manager",
        artifact_type="Compliance reports",
        review_focus="Process adherence"
    ),
    "project_manager": AdversarialPair(
        creator="project_manager",
        reviewer="operations_manager",
        artifact_type="Sprint plans",
        review_focus="Operational feasibility"
    ),
    
    # Governance Layer
    "data_governance_specialist": AdversarialPair(
        creator="data_governance_specialist",
        reviewer="architect",
        artifact_type="Governance policies",
        review_focus="Technical feasibility"
    ),
    "process_scenario_modeler": AdversarialPair(
        creator="process_scenario_modeler",
        reviewer="operations_manager",
        artifact_type="Simulation results",
        review_focus="Operational validity"
    ),
    "librarian_curator": AdversarialPair(
        creator="librarian_curator",
        reviewer="data_governance_specialist",
        artifact_type="KPI library entries",
        review_focus="Governance compliance"
    ),
    
    # Coordinator (reviewed by architect)
    "coordinator": AdversarialPair(
        creator="coordinator",
        reviewer="architect",
        artifact_type="Coordination decisions",
        review_focus="Technical soundness"
    ),
}


def get_reviewer_for_role(creator_role: str) -> str:
    """Get the designated reviewer for a creator role."""
    pair = ADVERSARIAL_PAIRS.get(creator_role)
    if pair:
        return pair.reviewer
    return "coordinator"  # Default fallback


def get_review_focus(creator_role: str) -> str:
    """Get what the reviewer should focus on."""
    pair = ADVERSARIAL_PAIRS.get(creator_role)
    if pair:
        return pair.review_focus
    return "General quality"


class AdversarialPairs:
    """Manager for adversarial pairing."""
    
    def __init__(self):
        self.pairs = ADVERSARIAL_PAIRS
    
    def get_pair(self, creator_role: str) -> Optional[AdversarialPair]:
        """Get the adversarial pair for a creator."""
        return self.pairs.get(creator_role)
    
    def get_reviewer(self, creator_role: str) -> str:
        """Get the reviewer for a creator."""
        return get_reviewer_for_role(creator_role)
    
    def can_review(self, reviewer_role: str, creator_role: str) -> bool:
        """Check if a reviewer can review a creator's work."""
        # Tier 0 rule: cannot review own work
        if reviewer_role == creator_role:
            return False
        
        # Check if this is the designated pairing
        pair = self.pairs.get(creator_role)
        if pair:
            return pair.reviewer == reviewer_role
        
        # Allow coordinator to review anyone
        if reviewer_role == "coordinator":
            return True
        
        return False
    
    def get_all_pairs(self) -> List[AdversarialPair]:
        """Get all adversarial pairs."""
        return list(self.pairs.values())
