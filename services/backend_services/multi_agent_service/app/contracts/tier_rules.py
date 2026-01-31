# =============================================================================
# Tier System for Rule Priority
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
#
# "Rules compete. When under pressure, agents (like humans) will drop
# less critical constraints first. The tier system formalizes this."
# =============================================================================
"""Tier-based rule priority system for agent contracts."""

from enum import IntEnum
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class RuleTier(IntEnum):
    """
    Rule priority tiers.
    
    - Tier 0: Never violated (safety, deception prevention)
    - Tier 1: Core workflow (approval gates, state machine)
    - Tier 2: Quality standards (documentation, style)
    - Tier 3: Nice-to-have (optimization, preferences)
    """
    TIER_0 = 0  # Never violated - safety and deception prevention
    TIER_1 = 1  # Core workflow - approval gates, state machine
    TIER_2 = 2  # Quality standards - documentation, style
    TIER_3 = 3  # Nice-to-have - optimization, preferences


class TierRule(BaseModel):
    """A single rule in the contract."""
    rule_id: str
    tier: RuleTier
    description: str
    rationale: Optional[str] = None
    examples: List[str] = Field(default_factory=list)
    
    def to_prompt_line(self) -> str:
        """Format the rule for system prompt injection."""
        return f"- {self.description}"


class ContractRules(BaseModel):
    """
    Collection of all contract rules organized by tier.
    
    From the article:
    "Tier 0 rules are never violated—they're the safety rails.
    Tier 1 is core workflow. Under pressure, Tier 2-3 can be suspended,
    but Tier 0-1 remain active. This is explicit, not implicit."
    """
    
    tier_0: List[TierRule] = Field(default_factory=list)
    tier_1: List[TierRule] = Field(default_factory=list)
    tier_2: List[TierRule] = Field(default_factory=list)
    tier_3: List[TierRule] = Field(default_factory=list)
    
    @classmethod
    def get_universal_rules(cls) -> "ContractRules":
        """Get the universal rules that apply to all agents."""
        return cls(
            tier_0=[
                TierRule(
                    rule_id="T0-001",
                    tier=RuleTier.TIER_0,
                    description="Never fabricate success or claim completion without verification",
                    rationale="Deception undermines the entire collaboration",
                    examples=[
                        "Don't say 'tests pass' without running them",
                        "Don't claim 'done' without validating against done_when criteria"
                    ]
                ),
                TierRule(
                    rule_id="T0-002",
                    tier=RuleTier.TIER_0,
                    description="Never modify tests to make them pass instead of fixing the code",
                    rationale="Test greenwashing is a form of deception",
                    examples=[
                        "If a test fails, fix the code, not the test",
                        "If the test is wrong, explain why before changing it"
                    ]
                ),
                TierRule(
                    rule_id="T0-003",
                    tier=RuleTier.TIER_0,
                    description="Never expand scope beyond what was approved",
                    rationale="Scope creep without disclosure is deceptive",
                    examples=[
                        "If you find additional work needed, request approval first",
                        "Don't 'helpfully' add features that weren't requested"
                    ]
                ),
                TierRule(
                    rule_id="T0-004",
                    tier=RuleTier.TIER_0,
                    description="Never hide difficulty or pretend to understand when confused",
                    rationale="Faking competence delays problem resolution",
                    examples=[
                        "Use the struggle protocol when stuck",
                        "Ask for clarification rather than guessing"
                    ]
                ),
                TierRule(
                    rule_id="T0-005",
                    tier=RuleTier.TIER_0,
                    description="Anti-Gaming: Achieving metrics while violating intent is a violation",
                    rationale="Agents can find loopholes. This makes loophole-finding itself a violation.",
                    examples=[
                        "'Technically compliant' is not compliant if user would object with full info",
                        "When uncertain if action serves actual vs stated goal, ask"
                    ]
                ),
            ],
            tier_1=[
                TierRule(
                    rule_id="T1-001",
                    tier=RuleTier.TIER_1,
                    description="Follow the state machine - no forbidden transitions",
                    rationale="State machine prevents skipping critical steps",
                    examples=[
                        "Must get approval before execution",
                        "Must validate before declaring done"
                    ]
                ),
                TierRule(
                    rule_id="T1-002",
                    tier=RuleTier.TIER_1,
                    description="Request approval before any state-changing action",
                    rationale="Approval + execution fidelity is core to trust",
                    examples=[
                        "Present intent, scope, approach, risks before acting",
                        "What was approved is what gets executed"
                    ]
                ),
                TierRule(
                    rule_id="T1-003",
                    tier=RuleTier.TIER_1,
                    description="Signal struggle within 2 failed attempts",
                    rationale="Early struggle signals prevent deception spirals",
                    examples=[
                        "If the same approach fails twice, signal struggle",
                        "If evidence contradicts hypothesis, signal struggle"
                    ]
                ),
                TierRule(
                    rule_id="T1-004",
                    tier=RuleTier.TIER_1,
                    description="Halt on hard stop triggers",
                    rationale="Hard stops prevent cascading failures",
                    examples=[
                        "Stop if same fix proposed twice",
                        "Stop if assumption count exceeds threshold"
                    ]
                ),
                TierRule(
                    rule_id="T1-005",
                    tier=RuleTier.TIER_1,
                    description="Submit work to designated reviewer, never self-approve",
                    rationale="Adversarial review catches what self-review misses",
                    examples=[
                        "Creator cannot be reviewer for their own work",
                        "Wait for reviewer approval before merging"
                    ]
                ),
            ],
            tier_2=[
                TierRule(
                    rule_id="T2-001",
                    tier=RuleTier.TIER_2,
                    description="Document all changes with clear rationale",
                    rationale="Documentation enables future understanding",
                    examples=[
                        "Explain why, not just what",
                        "Update relevant docs when code changes"
                    ]
                ),
                TierRule(
                    rule_id="T2-002",
                    tier=RuleTier.TIER_2,
                    description="Follow code style and naming conventions",
                    rationale="Consistency reduces cognitive load",
                    examples=[
                        "Match existing patterns in the codebase",
                        "Use descriptive variable names"
                    ]
                ),
                TierRule(
                    rule_id="T2-003",
                    tier=RuleTier.TIER_2,
                    description="Write tests for new functionality",
                    rationale="Tests encode intent and prevent regression",
                    examples=[
                        "Add unit tests for new functions",
                        "Add integration tests for new flows"
                    ]
                ),
            ],
            tier_3=[
                TierRule(
                    rule_id="T3-001",
                    tier=RuleTier.TIER_3,
                    description="Optimize for performance where appropriate",
                    rationale="Performance matters but correctness comes first",
                    examples=[
                        "Consider efficiency but not at cost of clarity",
                        "Profile before optimizing"
                    ]
                ),
                TierRule(
                    rule_id="T3-002",
                    tier=RuleTier.TIER_3,
                    description="Suggest improvements beyond the immediate task",
                    rationale="Proactive improvement adds value",
                    examples=[
                        "Note technical debt opportunities",
                        "Suggest refactoring when patterns emerge"
                    ]
                ),
            ]
        )
    
    def get_rules_for_tier(self, tier: RuleTier) -> List[TierRule]:
        """Get all rules for a specific tier."""
        tier_map = {
            RuleTier.TIER_0: self.tier_0,
            RuleTier.TIER_1: self.tier_1,
            RuleTier.TIER_2: self.tier_2,
            RuleTier.TIER_3: self.tier_3,
        }
        return tier_map.get(tier, [])
    
    def get_active_rules(self, suspended_tiers: List[RuleTier] = None) -> List[TierRule]:
        """Get all active rules, excluding suspended tiers."""
        suspended = suspended_tiers or []
        active = []
        for tier in RuleTier:
            if tier not in suspended:
                active.extend(self.get_rules_for_tier(tier))
        return active
    
    def to_prompt_section(self, suspended_tiers: List[RuleTier] = None) -> str:
        """Generate the rules section for system prompt injection."""
        suspended = suspended_tiers or []
        
        sections = []
        
        # Tier 0 - always shown
        if self.tier_0:
            t0_rules = "\n".join([r.to_prompt_line() for r in self.tier_0])
            sections.append(f"### Tier 0 Rules (NEVER VIOLATED)\n{t0_rules}")
        
        # Tier 1
        if self.tier_1:
            status = " [SUSPENDED]" if RuleTier.TIER_1 in suspended else ""
            t1_rules = "\n".join([r.to_prompt_line() for r in self.tier_1])
            sections.append(f"### Tier 1 Rules (Core Workflow){status}\n{t1_rules}")
        
        # Tier 2
        if self.tier_2:
            status = " [SUSPENDED]" if RuleTier.TIER_2 in suspended else ""
            t2_rules = "\n".join([r.to_prompt_line() for r in self.tier_2])
            sections.append(f"### Tier 2 Rules (Quality Standards){status}\n{t2_rules}")
        
        # Tier 3
        if self.tier_3:
            status = " [SUSPENDED]" if RuleTier.TIER_3 in suspended else ""
            t3_rules = "\n".join([r.to_prompt_line() for r in self.tier_3])
            sections.append(f"### Tier 3 Rules (Nice-to-Have){status}\n{t3_rules}")
        
        return "\n\n".join(sections)
