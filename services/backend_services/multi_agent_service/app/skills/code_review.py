# =============================================================================
# Code Review Skill
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Code review skill - risk mitigation, not gatekeeping."""

from typing import Dict, List, Any
from .base_skill import Skill, SkillResult, SkillFinding


class CodeReviewSkill(Skill):
    """
    Code Review Skill: Risk mitigation, not gatekeeping.
    
    From the article:
    "Code review is about risk mitigation. 70% of attention should go to
    security, correctness, and edge cases. Apply the 2am test:
    'Would this page me at 2am?'"
    
    Key principles:
    1. 70% attention on security/correctness
    2. 30% on style/maintainability
    3. Apply the 2am test
    4. Reviewer can't implement - separation enforced
    """
    
    # Review focus allocation
    FOCUS_ALLOCATION = {
        "security": 0.30,
        "correctness": 0.25,
        "edge_cases": 0.15,
        "style": 0.15,
        "maintainability": 0.15,
    }
    
    def __init__(self):
        super().__init__(
            name="Code Review",
            principle="Risk mitigation, not gatekeeping. Apply the 2am test."
        )
    
    async def apply(
        self,
        context: Dict[str, Any],
        content: str
    ) -> SkillResult:
        """Apply code review skill."""
        findings: List[SkillFinding] = []
        
        # Apply different review lenses
        security_findings = self._review_security(content)
        correctness_findings = self._review_correctness(content)
        edge_case_findings = self._review_edge_cases(content)
        
        # Combine findings up to limit
        all_findings = security_findings + correctness_findings + edge_case_findings
        findings = all_findings[:self.MAX_FINDINGS]
        
        # Apply the 2am test
        two_am_result = self._apply_2am_test(content)
        if two_am_result:
            findings.insert(0, two_am_result)
        
        score = self._calculate_score(findings)
        
        return SkillResult(
            skill_name=self.name,
            findings=findings,
            score=score,
            context={"focus_allocation": self.FOCUS_ALLOCATION}
        )
    
    def _review_security(self, content: str) -> List[SkillFinding]:
        """Review for security issues."""
        findings = []
        content_lower = content.lower()
        
        # Check for common security issues
        security_patterns = [
            ("password", "Hardcoded password or credential"),
            ("api_key", "Hardcoded API key"),
            ("secret", "Hardcoded secret"),
            ("eval(", "Dangerous eval() usage"),
            ("exec(", "Dangerous exec() usage"),
            ("sql", "Potential SQL injection if not parameterized"),
        ]
        
        for pattern, description in security_patterns:
            if pattern in content_lower:
                findings.append(self.create_finding(
                    description=description,
                    severity="high",
                    category="security",
                    recommendation="Review and remediate security concern",
                    evidence=f"Found pattern: {pattern}"
                ))
        
        return findings
    
    def _review_correctness(self, content: str) -> List[SkillFinding]:
        """Review for correctness issues."""
        findings = []
        content_lower = content.lower()
        
        # Check for common correctness issues
        if "todo" in content_lower or "fixme" in content_lower:
            findings.append(self.create_finding(
                description="TODO/FIXME marker indicates incomplete implementation",
                severity="medium",
                category="correctness",
                recommendation="Complete or document the TODO item",
                evidence="Found TODO/FIXME marker"
            ))
        
        if "pass" in content_lower and ("except" in content_lower or "try" in content_lower):
            findings.append(self.create_finding(
                description="Silent exception handling detected",
                severity="medium",
                category="correctness",
                recommendation="Handle exceptions explicitly or log them",
                evidence="Found pass in exception handler"
            ))
        
        return findings
    
    def _review_edge_cases(self, content: str) -> List[SkillFinding]:
        """Review for edge case handling."""
        findings = []
        content_lower = content.lower()
        
        # Check for missing null/none checks
        if ("." in content_lower and 
            "none" not in content_lower and 
            "null" not in content_lower and
            "if " not in content_lower):
            findings.append(self.create_finding(
                description="Potential missing null check",
                severity="low",
                category="edge_cases",
                recommendation="Verify null/None cases are handled",
                evidence="Method calls without apparent null checks"
            ))
        
        return findings
    
    def _apply_2am_test(self, content: str) -> SkillFinding | None:
        """
        Apply the 2am test: Would this page me at 2am?
        
        Look for patterns that could cause production issues.
        """
        content_lower = content.lower()
        
        # Patterns that might page you at 2am
        risky_patterns = [
            ("infinite", "Potential infinite loop/recursion"),
            ("while true", "Unbounded while loop"),
            ("no timeout", "Missing timeout"),
            ("retry forever", "Unbounded retry"),
        ]
        
        for pattern, description in risky_patterns:
            if pattern in content_lower:
                return self.create_finding(
                    description=f"2am Test Failed: {description}",
                    severity="high",
                    category="2am_test",
                    recommendation="This could cause production issues. Add bounds/timeouts.",
                    evidence=f"Found pattern: {pattern}"
                )
        
        return None
    
    def _calculate_score(self, findings: List[SkillFinding]) -> float:
        """Calculate review score."""
        if not findings:
            return 100.0
        
        # Weight by focus area
        severity_weights = {"critical": 25, "high": 15, "medium": 8, "low": 3}
        penalty = sum(severity_weights.get(f.severity, 5) for f in findings)
        
        return max(0.0, 100.0 - penalty)
    
    def to_prompt_section(self) -> str:
        """Generate skill section for system prompt."""
        return f"""### {self.name} Skill

**Principle**: {self.principle}

**Attention Allocation**:
- Security: 30%
- Correctness: 25%
- Edge Cases: 15%
- Style: 15%
- Maintainability: 15%

**The 2am Test**: Would this code page you at 2am?
- Look for unbounded loops
- Look for missing timeouts
- Look for silent failures
- Look for data corruption risks

**Reviewer Constraint**: Reviewer cannot implement code.
If code needs changes, reject with specific feedback.
"""
