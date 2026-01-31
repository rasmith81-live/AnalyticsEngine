# =============================================================================
# Discovery Package - Agent Discovery and Detection
# Phase 18-19: Migrated from conversation_service
# =============================================================================
"""
Agent discovery and detection utilities.

Provides:
- Fuzzy agent discovery by capability
- Agent overlap detection
"""

from .fuzzy_discovery import (
    FuzzyAgentDiscovery,
    AgentCapability,
    SearchResult,
    get_fuzzy_discovery,
)
from .overlap_detector import (
    AgentOverlapDetector,
    OverlapWarning,
    detect_agent_overlap,
)

__all__ = [
    "FuzzyAgentDiscovery",
    "AgentCapability",
    "SearchResult",
    "get_fuzzy_discovery",
    "AgentOverlapDetector",
    "OverlapWarning",
    "detect_agent_overlap",
]
