# =============================================================================
# Skills (Domain-Specific Contract Applications)
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Skills encode domain expertise as structural constraints."""

from .base_skill import Skill, SkillResult
from .systemic_thinking import SystemicThinkingSkill
from .testing import TestingSkill
from .debugging import DebuggingSkill
from .code_review import CodeReviewSkill

__all__ = [
    "Skill",
    "SkillResult",
    "SystemicThinkingSkill",
    "TestingSkill",
    "DebuggingSkill",
    "CodeReviewSkill",
]
