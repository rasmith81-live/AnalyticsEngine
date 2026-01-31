# =============================================================================
# Debugging Skill
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Debugging skill - narrowing search, not guess-and-check."""

from typing import Dict, List, Any
from .base_skill import Skill, SkillResult, SkillFinding


class DebuggingSkill(Skill):
    """
    Debugging Skill: Narrowing search, not guess-and-check.
    
    From the article:
    "Debugging is about narrowing the search space systematically.
    If the same fix is proposed twice, that's a hard stop.
    Escalate after one failed fix—don't spiral."
    
    Key principles:
    1. Form hypothesis first
    2. Test hypothesis with minimal change
    3. One failed fix = escalate, don't spiral
    4. Same fix twice = hard stop
    """
    
    def __init__(self):
        super().__init__(
            name="Debugging",
            principle="Narrowing search, not guess-and-check. Escalate after one failed fix."
        )
        self.fix_history: List[str] = []
    
    async def apply(
        self,
        context: Dict[str, Any],
        content: str
    ) -> SkillResult:
        """Apply debugging skill to analyze debugging approach."""
        findings: List[SkillFinding] = []
        
        # Check for guess-and-check patterns
        patterns = self._detect_patterns(content)
        
        for pattern in patterns:
            if len(findings) >= self.MAX_FINDINGS:
                break
            findings.append(pattern)
        
        score = self._calculate_score(findings)
        
        return SkillResult(
            skill_name=self.name,
            findings=findings,
            score=score,
            context={"fix_history_size": len(self.fix_history)}
        )
    
    def check_repeated_fix(self, fix_description: str) -> bool:
        """
        Check if this fix has been proposed before.
        
        Returns True if this is a repeated fix (hard stop trigger).
        """
        normalized = fix_description.lower().strip()
        
        for prev_fix in self.fix_history:
            if self._similar(normalized, prev_fix):
                return True
        
        self.fix_history.append(normalized)
        return False
    
    def _similar(self, fix1: str, fix2: str) -> bool:
        """Check if two fix descriptions are similar."""
        # Simple similarity check - could be more sophisticated
        words1 = set(fix1.split())
        words2 = set(fix2.split())
        
        if not words1 or not words2:
            return False
        
        overlap = len(words1.intersection(words2))
        total = len(words1.union(words2))
        
        return overlap / total > 0.7
    
    def _detect_patterns(self, content: str) -> List[SkillFinding]:
        """Detect debugging anti-patterns."""
        findings = []
        content_lower = content.lower()
        
        # Guess-and-check pattern
        guess_words = ["try", "maybe", "might", "perhaps", "could be"]
        guess_count = sum(1 for word in guess_words if word in content_lower)
        if guess_count >= 2:
            findings.append(self.create_finding(
                description="Guess-and-check pattern detected",
                severity="medium",
                category="debugging_approach",
                recommendation="Form a specific hypothesis before making changes",
                evidence=f"Found {guess_count} uncertainty markers"
            ))
        
        # Spiral pattern (multiple attempts mentioned)
        if "again" in content_lower or "another try" in content_lower:
            findings.append(self.create_finding(
                description="Debugging spiral detected - multiple attempts",
                severity="high",
                category="debugging_approach",
                recommendation="Stop and escalate. Don't continue spiraling.",
                evidence="Found 'again' or 'another try' patterns"
            ))
        
        # Lack of hypothesis
        hypothesis_markers = ["because", "hypothesis", "theory", "suspect", "believe"]
        if not any(marker in content_lower for marker in hypothesis_markers):
            findings.append(self.create_finding(
                description="No clear hypothesis stated",
                severity="low",
                category="debugging_approach",
                recommendation="State your hypothesis explicitly before debugging",
                evidence="No hypothesis markers found"
            ))
        
        return findings
    
    def _calculate_score(self, findings: List[SkillFinding]) -> float:
        """Calculate debugging approach score."""
        if not findings:
            return 100.0
        
        severity_weights = {"critical": 30, "high": 20, "medium": 10, "low": 5}
        penalty = sum(severity_weights.get(f.severity, 5) for f in findings)
        
        return max(0.0, 100.0 - penalty)
    
    def to_prompt_section(self) -> str:
        """Generate skill section for system prompt."""
        return f"""### {self.name} Skill

**Principle**: {self.principle}

**HARD STOP**: If the same fix is proposed twice, STOP immediately.

**Debugging Protocol**:
1. Form a specific hypothesis
2. Test with minimal change
3. If fix fails: ESCALATE (don't try again)
4. If same fix proposed twice: HARD STOP

**Anti-Patterns to Avoid**:
- Guess-and-check ("let's try...", "maybe if...")
- Spiraling (multiple attempts without hypothesis)
- Scope expansion (changing more than needed)

**Fix History Tracked**: {len(self.fix_history)} fixes recorded
"""
