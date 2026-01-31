# =============================================================================
# Key Protocols
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Key protocols for agent collaboration."""

from .collaboration_modes import CollaborationMode, CollaborationModeManager
from .hello import HelloProtocol
from .struggle import StruggleProtocol
from .magic_phrases import MagicPhraseHandler

__all__ = [
    "CollaborationMode",
    "CollaborationModeManager",
    "HelloProtocol",
    "StruggleProtocol",
    "MagicPhraseHandler",
]
