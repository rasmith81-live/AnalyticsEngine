# =============================================================================
# Systemic Thinking Skill
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Systemic thinking skill - find structural problems that aren't bugs yet."""

from typing import Dict, List, Any
from .base_skill import Skill, SkillResult, SkillFinding


class SystemicThinkingSkill(Skill):
    """
    The Most Powerful Skill: Systemic Thinking.
    
    From the article:
    "Not 'is this correct?' but 'where does this break under conditions
    that haven't arrived yet?'
    
    Run the system in your head. See it at 2am when the pager fires.
    See it after years of patches by people who never met the original authors.
    What breaks? What confuses? What compounds?"
    """
    
    MAX_FINDINGS = 10
    
    SIMULATION_PROMPTS = [
        "What happens at 2am when the pager fires?",
        "What happens after 3 years of patches by engineers who never met the original team?",
        "What happens when load is 10x current peak?",
        "What if a key dependency is unavailable for 5 minutes?",
        "What are the single points of failure?",
        "What feedback loops exist that might not converge?",
        "What assumptions about human availability exist?",
        "What grows without bound? What never gets pruned?",
        "What confuses new team members?",
        "What will be the first thing to break under stress?",
    ]
    
    FINDING_CATEGORIES = [
        "single_point_of_failure",
        "feedback_loop",
        "availability_assumption",
        "growth_trajectory",
        "complexity_accumulation",
        "hidden_coupling",
        "edge_case",
        "recovery_gap",
    ]
    
    def __init__(self):
        super().__init__(
            name="Systemic Thinking",
            principle="Not 'is this correct?' but 'where does this break under conditions that haven't arrived yet?'"
        )
    
    async def apply(
        self,
        context: Dict[str, Any],
        content: str
    ) -> SkillResult:
        """
        Apply systemic thinking to find structural problems.
        
        This is NOT correctness checking. This finds problems that
        aren't bugs yet but will be under conditions that don't exist yet.
        """
        findings: List[SkillFinding] = []
        
        # Run through simulation prompts
        for prompt in self.SIMULATION_PROMPTS:
            finding = await self._simulate_scenario(prompt, content, context)
            if finding:
                findings.append(finding)
            
            if len(findings) >= self.MAX_FINDINGS:
                break
        
        # Calculate score based on findings
        score = self._calculate_score(findings)
        
        return SkillResult(
            skill_name=self.name,
            findings=findings,
            score=score,
            context={"prompts_used": len(self.SIMULATION_PROMPTS)}
        )
    
    async def _simulate_scenario(
        self,
        prompt: str,
        content: str,
        context: Dict[str, Any]
    ) -> SkillFinding | None:
        """
        Simulate a scenario and identify structural problems.
        
        In production, this would invoke an LLM with the prompt.
        For now, we provide a framework for the analysis.
        """
        # This is a placeholder - in production, you'd invoke an LLM
        # with structured prompts to analyze the content
        
        # Example patterns to detect
        patterns = self._detect_patterns(content)
        
        if not patterns:
            return None
        
        # Return the most significant finding
        pattern = patterns[0]
        return self.create_finding(
            description=pattern["description"],
            severity=pattern["severity"],
            category=pattern["category"],
            recommendation=pattern["recommendation"],
            evidence=pattern.get("evidence")
        )
    
    def _detect_patterns(self, content: str) -> List[Dict[str, Any]]:
        """Detect structural patterns that could become problems."""
        patterns = []
        content_lower = content.lower()
        
        # Single point of failure patterns
        if "single" in content_lower and ("point" in content_lower or "instance" in content_lower):
            patterns.append({
                "description": "Potential single point of failure detected",
                "severity": "high",
                "category": "single_point_of_failure",
                "recommendation": "Add redundancy or failover mechanism",
                "evidence": "Content mentions single point/instance"
            })
        
        # Unbounded growth patterns
        if any(word in content_lower for word in ["cache", "log", "history", "queue"]):
            if not any(word in content_lower for word in ["limit", "prune", "expire", "ttl"]):
                patterns.append({
                    "description": "Potential unbounded growth - data structure without cleanup",
                    "severity": "medium",
                    "category": "growth_trajectory",
                    "recommendation": "Add TTL, pruning, or size limits",
                    "evidence": "Found cache/log/queue without limit/prune/expire"
                })
        
        # Synchronous blocking patterns
        if "sync" in content_lower or "blocking" in content_lower:
            patterns.append({
                "description": "Synchronous blocking operation may cause issues under load",
                "severity": "medium",
                "category": "feedback_loop",
                "recommendation": "Consider async alternatives or timeouts",
                "evidence": "Found sync/blocking patterns"
            })
        
        return patterns
    
    def _calculate_score(self, findings: List[SkillFinding]) -> float:
        """Calculate health score based on findings."""
        if not findings:
            return 100.0
        
        severity_weights = {
            "critical": 25,
            "high": 15,
            "medium": 8,
            "low": 3
        }
        
        penalty = sum(
            severity_weights.get(f.severity, 5)
            for f in findings
        )
        
        return max(0.0, 100.0 - penalty)
    
    def to_prompt_section(self) -> str:
        """Generate skill section for system prompt."""
        return f"""### {self.name} Skill

**Principle**: {self.principle}

**Core Technique**: Run the system in your head. See it at 2am when the pager fires.
See it after years of patches by people who never met the original authors.
What breaks? What confuses? What compounds?

**What It Finds**:
- Load-bearing single points of failure
- Feedback loops that could cause churn without converging
- Assumptions about availability that invert goals under stress
- Trajectory concerns about growth without pruning

**When To Run**:
- After other analysis is exhausted
- Before major architectural decisions
- Periodically on mature systems

**Output Limit**: {self.MAX_FINDINGS} findings maximum
"""
