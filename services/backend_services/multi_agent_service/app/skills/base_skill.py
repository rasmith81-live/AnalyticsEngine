# =============================================================================
# Base Skill Class
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Base class for skills - domain-specific contract applications."""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime


class SkillFinding(BaseModel):
    """A finding from applying a skill."""
    finding_id: str
    description: str
    severity: str  # "critical", "high", "medium", "low"
    category: str
    recommendation: str
    evidence: Optional[str] = None


class SkillResult(BaseModel):
    """Result of applying a skill."""
    skill_name: str
    findings: List[SkillFinding] = Field(default_factory=list)
    score: float = 100.0  # 0-100
    applied_at: datetime = Field(default_factory=datetime.utcnow)
    context: Dict[str, Any] = Field(default_factory=dict)


class Skill(ABC):
    """
    Base class for skills.
    
    From the article:
    "Skills are domain-specific applications of the contract.
    They encode expert knowledge as structural constraints."
    
    Each skill:
    1. Has a specific principle it applies
    2. Produces findings up to a limit
    3. Provides actionable recommendations
    """
    
    MAX_FINDINGS = 10
    
    def __init__(self, name: str, principle: str):
        self.name = name
        self.principle = principle
    
    @abstractmethod
    async def apply(
        self,
        context: Dict[str, Any],
        content: str
    ) -> SkillResult:
        """Apply the skill and return results."""
        pass
    
    def create_finding(
        self,
        description: str,
        severity: str,
        category: str,
        recommendation: str,
        evidence: Optional[str] = None
    ) -> SkillFinding:
        """Create a finding."""
        return SkillFinding(
            finding_id=f"F-{datetime.utcnow().strftime('%H%M%S%f')[:10]}",
            description=description,
            severity=severity,
            category=category,
            recommendation=recommendation,
            evidence=evidence
        )
    
    def to_prompt_section(self) -> str:
        """Generate skill section for system prompt."""
        return f"""### {self.name} Skill
Principle: {self.principle}
Max Findings: {self.MAX_FINDINGS}
"""
