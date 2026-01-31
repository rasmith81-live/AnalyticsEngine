# =============================================================================
# Blackboard Architecture
# Based on: Tangi Vass - "Adversarial Vibe Coding" / LIZA System
# Reference: https://github.com/liza-mas/liza
#
# "Agents coordinate through a blackboard—a shared YAML file defining current
# state. No conversation between agents. Read state, do work, write state.
# Everything visible, everything auditable."
# =============================================================================
"""Blackboard architecture for agent coordination."""

from .models import (
    TaskStatus,
    ArtifactType,
    BlackboardTask,
    BlackboardArtifact,
    ApprovalGate,
    StruggleSignalEntry,
    AuditLogEntry,
    AgentBlackboard,
)
from .operations import BlackboardOperations
from .store import RedisBlackboardStore
from .audit import AuditLogger

__all__ = [
    "TaskStatus",
    "ArtifactType",
    "BlackboardTask",
    "BlackboardArtifact",
    "ApprovalGate",
    "StruggleSignalEntry",
    "AuditLogEntry",
    "AgentBlackboard",
    "BlackboardOperations",
    "RedisBlackboardStore",
    "AuditLogger",
]
