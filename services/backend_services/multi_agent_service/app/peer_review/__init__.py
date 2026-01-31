# =============================================================================
# Peer Review Architecture
# Based on: Tangi Vass - "Adversarial Vibe Coding" / LIZA System
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Peer review with adversarial pairing."""

from .pairs import AdversarialPairs, get_reviewer_for_role
from .review_loop import ReviewLoop, ReviewResult
from .escalation import EscalationHandler, TwoFailuresRule

__all__ = [
    "AdversarialPairs",
    "get_reviewer_for_role",
    "ReviewLoop",
    "ReviewResult",
    "EscalationHandler",
    "TwoFailuresRule",
]
