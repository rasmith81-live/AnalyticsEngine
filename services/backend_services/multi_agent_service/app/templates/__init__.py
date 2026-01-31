# =============================================================================
# Agent Templates Package
# Phase 19: Prompt Library Integration
# Reference: https://www.shawnewallace.com/2025-11-19-building-a-personal-prompt-library/
# =============================================================================
"""
Agent templates package for prompt library management.

Provides:
- PromptLibrary: Centralized prompt template management
- AgentScaffolder: Create new agents from templates
- PromptFragments: Reusable prompt components
"""

from .prompt_library import PromptLibrary, PromptTemplate, PromptScenario
from .agent_scaffolder import AgentScaffolder, AgentTemplateConfig
from .prompt_fragments import PromptFragments, FragmentComposer

__all__ = [
    "PromptLibrary",
    "PromptTemplate",
    "PromptScenario",
    "AgentScaffolder",
    "AgentTemplateConfig",
    "PromptFragments",
    "FragmentComposer",
]
