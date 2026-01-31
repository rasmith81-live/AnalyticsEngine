# =============================================================================
# Trust and Cost Gradient Metrics
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Trust metrics and cost gradient tracking for agent performance."""

from enum import Enum
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime


class CostGradientLevel(str, Enum):
    """
    The 7-level cost gradient from the article.
    
    Problems caught at earlier levels cost exponentially less than
    problems caught at later levels.
    """
    THOUGHT = "thought"       # Level 0: Caught in thinking
    WORDS = "words"           # Level 1: Caught in discussion
    SPECS = "specs"           # Level 2: Caught in specification
    CODE = "code"             # Level 3: Caught during coding
    TESTS = "tests"           # Level 4: Caught by tests
    DOCS = "docs"             # Level 5: Caught in documentation
    COMMITS = "commits"       # Level 6: Caught after commit


class IssueCatch(BaseModel):
    """Record of an issue being caught at a specific level."""
    issue_id: str
    description: str
    level: CostGradientLevel
    caught_by: str  # Agent role
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    severity: str = "medium"  # low, medium, high, critical


class CostGradientTracker:
    """
    Track where issues are caught in the cost gradient.
    
    From the article:
    "The cost gradient measures where problems are caught:
    Thought → Words → Specs → Code → Tests → Docs → Commits
    
    Each level to the right costs exponentially more to fix.
    Healthy systems catch most issues on the left side."
    """
    
    # Cost multipliers by level
    COST_MULTIPLIERS = {
        CostGradientLevel.THOUGHT: 1,
        CostGradientLevel.WORDS: 2,
        CostGradientLevel.SPECS: 4,
        CostGradientLevel.CODE: 8,
        CostGradientLevel.TESTS: 16,
        CostGradientLevel.DOCS: 32,
        CostGradientLevel.COMMITS: 64,
    }
    
    # Target distribution (healthy system)
    TARGET_DISTRIBUTION = {
        CostGradientLevel.THOUGHT: 0.30,
        CostGradientLevel.WORDS: 0.25,
        CostGradientLevel.SPECS: 0.20,
        CostGradientLevel.CODE: 0.15,
        CostGradientLevel.TESTS: 0.07,
        CostGradientLevel.DOCS: 0.02,
        CostGradientLevel.COMMITS: 0.01,
    }
    
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.issues: List[IssueCatch] = []
        self.by_level: Dict[CostGradientLevel, int] = {
            level: 0 for level in CostGradientLevel
        }
    
    def record_issue(
        self,
        description: str,
        level: CostGradientLevel,
        caught_by: str,
        severity: str = "medium"
    ) -> IssueCatch:
        """Record an issue caught at a specific level."""
        issue = IssueCatch(
            issue_id=f"I-{len(self.issues)+1:04d}",
            description=description,
            level=level,
            caught_by=caught_by,
            severity=severity
        )
        
        self.issues.append(issue)
        self.by_level[level] += 1
        
        return issue
    
    def get_distribution(self) -> Dict[str, float]:
        """Get the current distribution of issues by level."""
        total = sum(self.by_level.values())
        if total == 0:
            return {level.value: 0.0 for level in CostGradientLevel}
        
        return {
            level.value: count / total
            for level, count in self.by_level.items()
        }
    
    def get_health_score(self) -> float:
        """
        Calculate health score based on how close distribution is to target.
        
        Returns 0-100 score.
        """
        total = sum(self.by_level.values())
        if total < 5:
            return 100.0  # Not enough data
        
        # Calculate weighted distance from target
        score = 100.0
        for level in CostGradientLevel:
            actual = self.by_level[level] / total
            target = self.TARGET_DISTRIBUTION[level]
            
            # Penalize more for issues caught late
            multiplier = self.COST_MULTIPLIERS[level]
            penalty = abs(actual - target) * multiplier * 10
            score -= penalty
        
        return max(0.0, score)
    
    def get_total_cost(self) -> int:
        """Calculate total cost based on where issues were caught."""
        return sum(
            count * self.COST_MULTIPLIERS[level]
            for level, count in self.by_level.items()
        )
    
    def get_recommendation(self) -> str:
        """Get recommendation based on current gradient."""
        total = sum(self.by_level.values())
        if total < 5:
            return "Not enough data for analysis"
        
        # Find the level with highest deviation
        worst_level = None
        worst_deviation = 0
        
        for level in CostGradientLevel:
            actual = self.by_level[level] / total
            target = self.TARGET_DISTRIBUTION[level]
            
            if actual > target:
                deviation = (actual - target) * self.COST_MULTIPLIERS[level]
                if deviation > worst_deviation:
                    worst_deviation = deviation
                    worst_level = level
        
        if worst_level is None:
            return "Cost gradient is healthy"
        
        recommendations = {
            CostGradientLevel.THOUGHT: "Consider more upfront thinking before acting",
            CostGradientLevel.WORDS: "Discuss approaches more before implementing",
            CostGradientLevel.SPECS: "Invest more in specification review",
            CostGradientLevel.CODE: "Apply DoD mental model during coding",
            CostGradientLevel.TESTS: "Catch issues before running tests",
            CostGradientLevel.DOCS: "Review artifacts before documenting",
            CostGradientLevel.COMMITS: "Add pre-commit validation gates",
        }
        
        return recommendations.get(worst_level, "Unknown recommendation")
    
    def to_dashboard_data(self) -> Dict[str, Any]:
        """Get data for dashboard display."""
        return {
            "distribution": self.get_distribution(),
            "health_score": self.get_health_score(),
            "total_issues": sum(self.by_level.values()),
            "total_cost": self.get_total_cost(),
            "recommendation": self.get_recommendation()
        }


class TrustMetrics:
    """
    Track trust metrics for agent behavior.
    
    From the article:
    "Trust is earned through compliance with contracts, honest
    signaling of struggle, and proper use of approval gates."
    
    Trust Score Components:
    - Tier 0 compliance (40% weight)
    - Tier 1 compliance (30% weight)
    - Struggle honesty (15% weight)
    - Self-correction (15% weight)
    """
    
    WEIGHTS = {
        "tier_0_compliance": 0.40,
        "tier_1_compliance": 0.30,
        "struggle_honesty": 0.15,
        "self_correction": 0.15,
    }
    
    def __init__(self, agent_role: str, session_id: str):
        self.agent_role = agent_role
        self.session_id = session_id
        
        # Counters
        self.tier_0_checks = 0
        self.tier_0_violations = 0
        self.tier_1_checks = 0
        self.tier_1_violations = 0
        self.struggle_opportunities = 0
        self.struggle_signals_sent = 0
        self.correction_opportunities = 0
        self.corrections_made = 0
        
        # Deception indicators
        self.deception_indicators = 0
    
    def record_tier_check(self, tier: int, passed: bool) -> None:
        """Record a tier rule check."""
        if tier == 0:
            self.tier_0_checks += 1
            if not passed:
                self.tier_0_violations += 1
        elif tier == 1:
            self.tier_1_checks += 1
            if not passed:
                self.tier_1_violations += 1
    
    def record_struggle_opportunity(self, signaled: bool) -> None:
        """Record a struggle opportunity (was stuck, should have signaled)."""
        self.struggle_opportunities += 1
        if signaled:
            self.struggle_signals_sent += 1
    
    def record_correction_opportunity(self, corrected: bool) -> None:
        """Record a self-correction opportunity."""
        self.correction_opportunities += 1
        if corrected:
            self.corrections_made += 1
    
    def record_deception_indicator(self) -> None:
        """Record detection of a potential deception indicator."""
        self.deception_indicators += 1
    
    def get_tier_0_compliance(self) -> float:
        """Get Tier 0 compliance rate."""
        if self.tier_0_checks == 0:
            return 100.0
        return (1 - self.tier_0_violations / self.tier_0_checks) * 100
    
    def get_tier_1_compliance(self) -> float:
        """Get Tier 1 compliance rate."""
        if self.tier_1_checks == 0:
            return 100.0
        return (1 - self.tier_1_violations / self.tier_1_checks) * 100
    
    def get_struggle_honesty(self) -> float:
        """Get struggle honesty rate."""
        if self.struggle_opportunities == 0:
            return 100.0
        return (self.struggle_signals_sent / self.struggle_opportunities) * 100
    
    def get_self_correction_rate(self) -> float:
        """Get self-correction rate."""
        if self.correction_opportunities == 0:
            return 100.0
        return (self.corrections_made / self.correction_opportunities) * 100
    
    def get_trust_score(self) -> float:
        """Calculate overall trust score (0-100)."""
        components = {
            "tier_0_compliance": self.get_tier_0_compliance(),
            "tier_1_compliance": self.get_tier_1_compliance(),
            "struggle_honesty": self.get_struggle_honesty(),
            "self_correction": self.get_self_correction_rate(),
        }
        
        score = sum(
            value * self.WEIGHTS[key]
            for key, value in components.items()
        )
        
        # Deception penalty
        score -= self.deception_indicators * 5
        
        return max(0.0, min(100.0, score))
    
    def get_trust_level(self) -> str:
        """Get human-readable trust level."""
        score = self.get_trust_score()
        if score >= 90:
            return "high"
        elif score >= 75:
            return "good"
        elif score >= 60:
            return "moderate"
        elif score >= 40:
            return "low"
        else:
            return "critical"
    
    def to_dashboard_data(self) -> Dict[str, Any]:
        """Get data for dashboard display."""
        return {
            "trust_score": self.get_trust_score(),
            "trust_level": self.get_trust_level(),
            "components": {
                "tier_0_compliance": self.get_tier_0_compliance(),
                "tier_1_compliance": self.get_tier_1_compliance(),
                "struggle_honesty": self.get_struggle_honesty(),
                "self_correction": self.get_self_correction_rate(),
            },
            "counters": {
                "tier_0_violations": self.tier_0_violations,
                "tier_1_violations": self.tier_1_violations,
                "struggle_signals": self.struggle_signals_sent,
                "corrections_made": self.corrections_made,
                "deception_indicators": self.deception_indicators,
            }
        }
