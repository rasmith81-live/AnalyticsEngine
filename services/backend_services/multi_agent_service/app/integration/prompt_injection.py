# =============================================================================
# System Prompt Injection
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Dynamic injection of contract rules into agent system prompts."""

from typing import Dict, List, Optional, Any
from datetime import datetime

from ..contracts.state_machine import AgentContract
from ..contracts.tier_rules import ContractRules, RuleTier
from ..contracts.enforcer import ContractEnforcer
from ..monitoring.token_budget import TokenBudgetMonitor
from ..monitoring.drift_detector import DriftDetector
from ..monitoring.degraded_mode import DegradedModeMonitor
from ..protocols.collaboration_modes import CollaborationModeManager
from ..agents.contracts import get_contract, RoleContract


class PromptInjector:
    """
    Injects contract rules and state into agent system prompts.
    
    From the article:
    "The contract is injected into the system prompt—the agent
    carries its constraints wherever it goes."
    
    The prompt injection includes:
    1. Universal contract rules (Tier 0-3)
    2. Role-specific rules
    3. Current state machine status
    4. Hard stop trigger status
    5. Self-monitoring announcements
    """
    
    ATTRIBUTION_HEADER = """# Attribution
This behavioral contract is based on the work of Tangi Vass.
Reference: https://github.com/liza-mas/liza
"""
    
    def __init__(
        self,
        agent_role: str,
        session_id: str,
        contract: Optional[AgentContract] = None,
        enforcer: Optional[ContractEnforcer] = None,
        token_monitor: Optional[TokenBudgetMonitor] = None,
        drift_detector: Optional[DriftDetector] = None,
        degraded_monitor: Optional[DegradedModeMonitor] = None,
        mode_manager: Optional[CollaborationModeManager] = None
    ):
        self.agent_role = agent_role
        self.session_id = session_id
        
        # Contract components
        self.contract = contract or AgentContract(agent_role, session_id)
        self.enforcer = enforcer or ContractEnforcer()
        self.universal_rules = ContractRules.get_universal_rules()
        self.role_contract = get_contract(agent_role)
        
        # Monitoring components
        self.token_monitor = token_monitor
        self.drift_detector = drift_detector
        self.degraded_monitor = degraded_monitor
        
        # Collaboration mode
        self.mode_manager = mode_manager or CollaborationModeManager()
    
    def build_contract_section(
        self,
        suspended_tiers: Optional[List[RuleTier]] = None
    ) -> str:
        """Build the full contract section for system prompt injection."""
        sections = []
        
        # Attribution
        sections.append(self.ATTRIBUTION_HEADER)
        
        # Main header
        sections.append(f"""# Behavioral Contract for {self.agent_role}

This contract is the single source of truth. When conflicts arise, defer here.
Session: {self.session_id}
Generated: {datetime.utcnow().isoformat()}
""")
        
        # Universal rules
        sections.append(self.universal_rules.to_prompt_section(suspended_tiers))
        
        # Role-specific rules
        sections.append(self._build_role_section())
        
        # State machine
        sections.append(self.contract.to_prompt_section())
        
        # Enforcer status
        sections.append(self.enforcer.to_prompt_section())
        
        # Collaboration mode
        sections.append(self.mode_manager.to_prompt_section())
        
        # Self-monitoring (if available)
        monitoring_section = self._build_monitoring_section()
        if monitoring_section:
            sections.append(monitoring_section)
        
        return "\n\n".join(sections)
    
    def _build_role_section(self) -> str:
        """Build the role-specific section."""
        rc = self.role_contract
        
        lines = [
            f"### Role: {rc.role}",
            f"**Description**: {rc.description}",
            "",
            "**Domain Expertise**: " + ", ".join(rc.domain_expertise),
            "**Artifacts Produced**: " + ", ".join(rc.artifacts_produced),
            f"**Designated Reviewer**: {rc.reviewer}",
            "",
            "**Role-Specific Rules:**"
        ]
        
        if rc.tier_0_rules:
            lines.append("Tier 0 (NEVER VIOLATE):")
            for rule in rc.tier_0_rules:
                lines.append(f"  - {rule}")
        
        if rc.tier_1_rules:
            lines.append("Tier 1 (Core Workflow):")
            for rule in rc.tier_1_rules:
                lines.append(f"  - {rule}")
        
        if rc.tier_2_rules:
            lines.append("Tier 2 (Quality):")
            for rule in rc.tier_2_rules:
                lines.append(f"  - {rule}")
        
        return "\n".join(lines)
    
    def _build_monitoring_section(self) -> Optional[str]:
        """Build the self-monitoring section."""
        sections = []
        
        # Token budget
        if self.token_monitor:
            announcement = self.token_monitor.get_announcement()
            if announcement:
                sections.append(announcement)
            sections.append(self.token_monitor.to_prompt_section())
        
        # Drift detection
        if self.drift_detector:
            announcement = self.drift_detector.get_announcement()
            if announcement:
                sections.append(announcement)
        
        # Degraded mode
        if self.degraded_monitor:
            announcement = self.degraded_monitor.get_announcement()
            if announcement:
                sections.append(announcement)
            sections.append(self.degraded_monitor.to_prompt_section())
        
        if sections:
            return "### Self-Monitoring\n\n" + "\n\n".join(sections)
        
        return None
    
    def inject_into_prompt(
        self,
        base_prompt: str,
        suspended_tiers: Optional[List[RuleTier]] = None
    ) -> str:
        """Inject contract section into a base system prompt."""
        contract_section = self.build_contract_section(suspended_tiers)
        
        # Insert contract after base prompt
        return f"{base_prompt}\n\n{contract_section}"
    
    def get_tool_registration(self) -> List[Dict[str, Any]]:
        """Get the contract-aware tools to register with the agent."""
        return [
            {
                "name": "request_approval",
                "description": "Request approval before any state-changing action. Required by contract.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "intent": {"type": "string", "description": "What you're trying to achieve"},
                        "scope": {"type": "string", "description": "What will be affected"},
                        "approach": {"type": "string", "description": "How you plan to do it"},
                        "consequences": {"type": "array", "items": {"type": "string"}},
                        "risks": {"type": "array", "items": {"type": "string"}},
                        "validation_plan": {"type": "string", "description": "How you'll verify success"},
                        "assumptions": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["intent", "scope", "approach", "validation_plan"]
                }
            },
            {
                "name": "signal_struggle",
                "description": "Signal that you are stuck. Use this instead of faking progress.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "signal_type": {
                            "type": "string",
                            "enum": ["blocked", "confused", "conflicting_evidence", "resource_missing"]
                        },
                        "what_i_understand": {"type": "string"},
                        "what_i_tried": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "action": {"type": "string"},
                                    "outcome": {"type": "string"}
                                }
                            }
                        },
                        "where_im_stuck": {"type": "string"},
                        "what_would_help": {"type": "string"}
                    },
                    "required": ["signal_type", "what_i_understand", "where_im_stuck", "what_would_help"]
                }
            },
            {
                "name": "transition_state",
                "description": "Request a state transition. Will be validated against contract.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "to_state": {
                            "type": "string",
                            "enum": ["analysis", "approval_pending", "execution", "validation", "done", "blocked"]
                        },
                        "rationale": {"type": "string", "description": "Why this transition is appropriate"}
                    },
                    "required": ["to_state", "rationale"]
                }
            },
            {
                "name": "submit_for_review",
                "description": "Submit your work for peer review. Required before completion.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "artifact_type": {"type": "string"},
                        "content": {"type": "object"},
                        "done_when_checklist": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "criterion": {"type": "string"},
                                    "met": {"type": "boolean"},
                                    "evidence": {"type": "string"}
                                }
                            }
                        }
                    },
                    "required": ["artifact_type", "content", "done_when_checklist"]
                }
            }
        ]
