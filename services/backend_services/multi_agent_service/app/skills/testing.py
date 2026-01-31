# =============================================================================
# Testing Skill
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Testing skill - tests encode intent, never fix tests by accepting broken code."""

from typing import Dict, List, Any
from enum import Enum
from .base_skill import Skill, SkillResult, SkillFinding


class TestOutcome(str, Enum):
    """Possible test outcomes."""
    PASS = "pass"
    FAIL = "fail"
    ERROR = "error"
    SKIP = "skip"


class TestInterpretation(str, Enum):
    """How to interpret a test outcome."""
    FIX_CODE = "fix_code"
    FIX_TEST = "fix_test"
    CLARIFY_SPEC = "clarify_spec"
    INVESTIGATE = "investigate"


class TestingSkill(Skill):
    """
    Testing Skill: Tests encode intent.
    
    From the article:
    "Tests encode the client's intent and business requirements.
    Never fix tests by accepting broken code—this is a Tier 0 violation."
    
    Key principle: When a test fails, the interpretation matrix determines
    what action to take:
    
    | Test Written By | Failure Interpretation |
    |-----------------|------------------------|
    | Spec           | Fix the code           |
    | Developer      | Investigate both       |
    | Generated      | Low trust - verify     |
    """
    
    # Interpretation matrix
    INTERPRETATION_MATRIX = {
        ("spec", "fail"): TestInterpretation.FIX_CODE,
        ("spec", "error"): TestInterpretation.INVESTIGATE,
        ("developer", "fail"): TestInterpretation.INVESTIGATE,
        ("developer", "error"): TestInterpretation.INVESTIGATE,
        ("generated", "fail"): TestInterpretation.CLARIFY_SPEC,
        ("generated", "error"): TestInterpretation.INVESTIGATE,
    }
    
    def __init__(self):
        super().__init__(
            name="Testing",
            principle="Tests encode intent. Never fix tests by accepting broken code."
        )
    
    async def apply(
        self,
        context: Dict[str, Any],
        content: str
    ) -> SkillResult:
        """Apply testing skill to analyze test results."""
        findings: List[SkillFinding] = []
        
        # Analyze test patterns in content
        test_patterns = self._analyze_test_patterns(content)
        
        for pattern in test_patterns:
            if len(findings) >= self.MAX_FINDINGS:
                break
            
            interpretation = self._get_interpretation(
                pattern["source"],
                pattern["outcome"]
            )
            
            finding = self._create_test_finding(pattern, interpretation)
            if finding:
                findings.append(finding)
        
        score = self._calculate_score(findings)
        
        return SkillResult(
            skill_name=self.name,
            findings=findings,
            score=score,
            context={"patterns_analyzed": len(test_patterns)}
        )
    
    def _analyze_test_patterns(self, content: str) -> List[Dict[str, Any]]:
        """Analyze content for test-related patterns."""
        patterns = []
        content_lower = content.lower()
        
        # Detect test modification patterns (Tier 0 violation risk)
        if "modify" in content_lower and "test" in content_lower:
            patterns.append({
                "description": "Potential test modification detected",
                "source": "developer",
                "outcome": "fail",
                "risk": "tier_0_violation"
            })
        
        # Detect test skipping
        if "skip" in content_lower and "test" in content_lower:
            patterns.append({
                "description": "Test skipping detected",
                "source": "developer",
                "outcome": "skip",
                "risk": "coverage_gap"
            })
        
        # Detect assertion changes
        if "assert" in content_lower and ("change" in content_lower or "update" in content_lower):
            patterns.append({
                "description": "Assertion modification detected",
                "source": "developer",
                "outcome": "fail",
                "risk": "intent_drift"
            })
        
        return patterns
    
    def _get_interpretation(
        self,
        source: str,
        outcome: str
    ) -> TestInterpretation:
        """Get interpretation from the matrix."""
        return self.INTERPRETATION_MATRIX.get(
            (source, outcome),
            TestInterpretation.INVESTIGATE
        )
    
    def _create_test_finding(
        self,
        pattern: Dict[str, Any],
        interpretation: TestInterpretation
    ) -> SkillFinding | None:
        """Create a finding from a test pattern."""
        if pattern.get("risk") == "tier_0_violation":
            return self.create_finding(
                description="Potential Tier 0 violation: modifying tests instead of fixing code",
                severity="critical",
                category="test_integrity",
                recommendation="Fix the code to make the test pass, not the other way around",
                evidence=pattern.get("description")
            )
        
        if pattern.get("risk") == "coverage_gap":
            return self.create_finding(
                description="Test skipping reduces coverage",
                severity="medium",
                category="test_coverage",
                recommendation="Run all tests or document why skip is necessary",
                evidence=pattern.get("description")
            )
        
        return None
    
    def _calculate_score(self, findings: List[SkillFinding]) -> float:
        """Calculate score based on findings."""
        if not findings:
            return 100.0
        
        # Critical findings (Tier 0 risks) severely impact score
        critical_count = sum(1 for f in findings if f.severity == "critical")
        other_count = len(findings) - critical_count
        
        return max(0.0, 100.0 - (critical_count * 40) - (other_count * 10))
    
    def to_prompt_section(self) -> str:
        """Generate skill section for system prompt."""
        return f"""### {self.name} Skill

**Principle**: {self.principle}

**TIER 0 RULE**: Never modify tests to make them pass. This is deception.

**Interpretation Matrix**:
| Test Source | On Failure | Action |
|-------------|------------|--------|
| From Spec   | Fail       | Fix the code |
| Developer   | Fail       | Investigate both |
| Generated   | Fail       | Verify against spec |

**When Test Fails**:
1. Check test source (spec, developer, generated)
2. Apply interpretation matrix
3. Fix code OR escalate spec ambiguity
4. NEVER modify test to pass without explicit approval
"""
