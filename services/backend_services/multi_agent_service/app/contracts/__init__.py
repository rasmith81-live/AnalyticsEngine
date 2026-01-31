# =============================================================================
# Contract Infrastructure
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Contract infrastructure for behavioral constraints on agents."""

from .state_machine import AgentState, AgentContract, ForbiddenTransition
from .tier_rules import TierRule, RuleTier, ContractRules
from .enforcer import ContractEnforcer
from .violations import ContractViolation, ViolationHandler, ResetSemantics

__all__ = [
    "AgentState",
    "AgentContract",
    "ForbiddenTransition",
    "TierRule",
    "RuleTier",
    "ContractRules",
    "ContractEnforcer",
    "ContractViolation",
    "ViolationHandler",
    "ResetSemantics",
]
