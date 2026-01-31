# =============================================================================
# Integration Points
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Integration points for connecting multi_agent_service to other services."""

from .client import MultiAgentClient
from .prompt_injection import PromptInjector

__all__ = [
    "MultiAgentClient",
    "PromptInjector",
]
