# =============================================================================
# Base Contract Agent
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Base agent class with behavioral contract enforcement."""

from enum import Enum
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime
import logging

from ..contracts.state_machine import AgentContract, AgentState, TransitionGate
from ..contracts.tier_rules import ContractRules, RuleTier
from ..contracts.enforcer import ContractEnforcer, StruggleSignal, ApprovalRequest
from ..contracts.violations import ContractViolation, ViolationHandler
from ..blackboard.models import AgentBlackboard
from ..blackboard.operations import BlackboardOperations

logger = logging.getLogger(__name__)


class AgentRole(str, Enum):
    """All 27 agent roles plus coordinator."""
    # Strategy & Analysis Layer
    COORDINATOR = "coordinator"
    BUSINESS_STRATEGIST = "business_strategist"
    BUSINESS_ANALYST = "business_analyst"
    DATA_ANALYST = "data_analyst"
    DATA_SCIENTIST = "data_scientist"
    OPERATIONS_MANAGER = "operations_manager"
    MAPPING_SPECIALIST = "mapping_specialist"
    DOCUMENT_ANALYZER = "document_analyzer"
    COMPETITIVE_ANALYST = "competitive_analyst"
    
    # Technical Design Layer
    ARCHITECT = "architect"
    DEVELOPER = "developer"
    TESTER = "tester"
    DOCUMENTER = "documenter"
    DEPLOYMENT_SPECIALIST = "deployment_specialist"
    UI_DESIGNER = "ui_designer"
    ITIL_MANAGER = "itil_manager"
    CONNECTION_SPECIALIST = "connection_specialist"
    
    # Business Operations Layer
    SALES_MANAGER = "sales_manager"
    MARKETING_MANAGER = "marketing_manager"
    ACCOUNTANT = "accountant"
    CUSTOMER_SUCCESS_MANAGER = "customer_success_manager"
    HR_TALENT_ANALYST = "hr_talent_analyst"
    SUPPLY_CHAIN_ANALYST = "supply_chain_analyst"
    RISK_COMPLIANCE_OFFICER = "risk_compliance_officer"
    PROJECT_MANAGER = "project_manager"
    
    # Governance Layer
    DATA_GOVERNANCE_SPECIALIST = "data_governance_specialist"
    PROCESS_SCENARIO_MODELER = "process_scenario_modeler"
    LIBRARIAN_CURATOR = "librarian_curator"


class AgentConfig(BaseModel):
    """Configuration for an agent."""
    role: AgentRole
    model: str = "claude-sonnet-4-20250514"
    max_tokens: int = 4096
    temperature: float = 0.5
    
    # Contract settings
    max_tool_calls: int = 10
    max_consultation_depth: int = 2
    struggle_signal_after: int = 2
    assumption_threshold: int = 3
    
    # Role-specific rules
    tier_0_rules: List[str] = Field(default_factory=list)
    tier_1_rules: List[str] = Field(default_factory=list)
    tier_2_rules: List[str] = Field(default_factory=list)


class AgentResponse(BaseModel):
    """Response from agent processing."""
    content: str
    state: AgentState
    artifacts: List[Dict[str, Any]] = Field(default_factory=list)
    approval_request: Optional[ApprovalRequest] = None
    struggle_signal: Optional[StruggleSignal] = None
    violations: List[Dict[str, Any]] = Field(default_factory=list)
    success: bool = True


class BaseContractAgent:
    """
    Base agent class with behavioral contract enforcement.
    
    All agents inherit from this class and get:
    - State machine with forbidden transitions
    - Tier-based rules (T0-T3)
    - Hard stop triggers
    - Struggle protocol
    - Approval gates
    - DoR/DoD mental models
    """
    
    def __init__(
        self,
        config: AgentConfig,
        session_id: str,
        blackboard: Optional[AgentBlackboard] = None
    ):
        self.config = config
        self.session_id = session_id
        
        # Initialize contract components
        self.contract = AgentContract(
            agent_role=config.role.value,
            session_id=session_id
        )
        self.rules = self._build_contract_rules()
        self.enforcer = ContractEnforcer(
            contract_rules=self.rules,
            assumption_threshold=config.assumption_threshold,
            struggle_signal_after=config.struggle_signal_after
        )
        self.violation_handler = ViolationHandler()
        
        # Blackboard integration
        self.blackboard = blackboard
        self.blackboard_ops = BlackboardOperations(blackboard) if blackboard else None
        
        # Tracking
        self._tool_call_count = 0
        self._initialized = False
    
    def _build_contract_rules(self) -> ContractRules:
        """Build contract rules combining universal and role-specific rules."""
        rules = ContractRules.get_universal_rules()
        
        # Add role-specific rules if configured
        # (Role-specific rules would be added here)
        
        return rules
    
    async def initialize(self) -> None:
        """Initialize the agent (Hello Protocol)."""
        self._initialized = True
        logger.info(f"Agent {self.config.role.value} initialized for session {self.session_id}")
    
    async def process(
        self,
        message: str,
        context: Optional[Dict[str, Any]] = None
    ) -> AgentResponse:
        """
        Process a message with contract enforcement.
        
        This method:
        1. Checks current state
        2. Validates against contract rules
        3. Processes the message
        4. Handles state transitions
        5. Returns response with any approvals/signals needed
        """
        if not self._initialized:
            await self.initialize()
        
        violations = []
        
        try:
            # Check hard stop triggers before processing
            trigger = self.enforcer.check_triggers()
            if trigger:
                return AgentResponse(
                    content=f"Hard stop triggered: {trigger.value}. Processing halted.",
                    state=self.contract.current_state,
                    success=False
                )
            
            # Transition to analysis if idle
            if self.contract.current_state == AgentState.IDLE:
                self.contract.transition_to(AgentState.ANALYSIS)
            
            # Process the message (subclasses implement this)
            response_content = await self._process_message(message, context)
            
            return AgentResponse(
                content=response_content,
                state=self.contract.current_state,
                violations=[v.to_dict() for v in self.violation_handler.violation_log[-5:]]
            )
            
        except ContractViolation as e:
            # Handle violation
            handling = self.violation_handler.handle_violation(
                e, self.contract, self.blackboard
            )
            
            return AgentResponse(
                content=f"Contract violation: {e.rule}. {handling.get('message', '')}",
                state=self.contract.current_state,
                violations=[e.to_dict()],
                success=False
            )
    
    async def _process_message(
        self,
        message: str,
        context: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Process a message. Subclasses should override this.
        
        The base implementation just echoes the message.
        """
        return f"[{self.config.role.value}] Received: {message}"
    
    async def request_approval(
        self,
        intent: str,
        scope: str,
        approach: str,
        consequences: List[str],
        risks: List[str],
        validation_plan: str,
        assumptions: List[str]
    ) -> ApprovalRequest:
        """
        Request approval before executing a state-changing action.
        
        This implements the approval gate from the contract.
        """
        # Check for assumption overflow
        for assumption in assumptions:
            trigger = self.enforcer.add_assumption(assumption)
            if trigger:
                raise ContractViolation(
                    rule="Assumption overflow",
                    tier=RuleTier.TIER_1,
                    context=f"Too many assumptions ({len(assumptions)}). Hard stop triggered.",
                    agent_role=self.config.role.value,
                    session_id=self.session_id
                )
        
        request = ApprovalRequest(
            request_id=f"AR-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
            agent_role=self.config.role.value,
            session_id=self.session_id,
            intent=intent,
            scope=scope,
            approach=approach,
            consequences=consequences,
            risks=risks,
            validation_plan=validation_plan,
            assumptions=assumptions
        )
        
        # Submit to enforcer
        self.enforcer.submit_approval_request(request)
        
        # Transition to approval pending
        self.contract.transition_to(AgentState.APPROVAL_PENDING)
        
        logger.info(f"Agent {self.config.role.value} requesting approval: {intent}")
        
        return request
    
    async def signal_struggle(
        self,
        signal_type: str,
        what_i_understand: str,
        what_i_tried: List[Dict[str, str]],
        where_im_stuck: str,
        what_would_help: str
    ) -> StruggleSignal:
        """
        Signal that the agent is stuck.
        
        This implements the Struggle Protocol from the contract.
        """
        signal = StruggleSignal(
            signal_type=signal_type,
            what_i_understand=what_i_understand,
            what_i_tried=what_i_tried,
            where_im_stuck=where_im_stuck,
            what_would_help=what_would_help,
            agent_role=self.config.role.value,
            session_id=self.session_id,
            attempt_count=self.enforcer.failed_attempts
        )
        
        # Submit to enforcer
        self.enforcer.submit_struggle_signal(signal)
        
        # Transition to blocked
        self.contract.transition_to(AgentState.BLOCKED)
        
        logger.info(f"Agent {self.config.role.value} signaling struggle: {signal_type}")
        
        return signal
    
    def check_definition_of_ready(self, criteria: List[str]) -> bool:
        """
        Check Definition of Ready before transitioning to approval.
        
        DoR is a mental model that agents apply BEFORE starting work.
        """
        # Self-check questions from the contract
        self_check = [
            "Do I understand what success looks like?",
            "Are all required inputs available?",
            "Have upstream dependencies been satisfied?",
            "Do I have sufficient context to proceed?",
            "Are there ambiguities I should clarify first?"
        ]
        
        # Check each criterion
        all_ready = all(self._evaluate_criterion(c) for c in criteria)
        
        if all_ready:
            self.contract.set_gate_result(TransitionGate.DEFINITION_OF_READY, True)
        
        return all_ready
    
    def check_definition_of_done(self, criteria: List[str]) -> bool:
        """
        Check Definition of Done before declaring complete.
        
        DoD is a mental model that agents apply DURING and AFTER work.
        Enables self-correction before external review.
        """
        # Self-check questions from the contract
        self_check = [
            "Does this satisfy every done_when criterion?",
            "Did I actually run validation, or just assume it would pass?",
            "Is there anything subtle I might be missing?",
            "Would I approve this if I were the reviewer?",
            "Am I glossing over any edge cases?"
        ]
        
        # Check each criterion
        all_done = all(self._evaluate_criterion(c) for c in criteria)
        
        if all_done:
            self.contract.set_gate_result(TransitionGate.DEFINITION_OF_DONE, True)
        
        return all_done
    
    def _evaluate_criterion(self, criterion: str) -> bool:
        """Evaluate a single criterion. Subclasses should override."""
        # Base implementation: assume true (subclasses should implement properly)
        return True
    
    def get_system_prompt(self) -> str:
        """Generate the system prompt with contract injection."""
        base_prompt = self._get_base_system_prompt()
        
        contract_section = f"""
## Behavioral Contract

This contract is the single source of truth. When conflicts arise, defer here.

{self.rules.to_prompt_section()}

{self.contract.to_prompt_section()}

{self.enforcer.to_prompt_section()}
"""
        
        return f"{base_prompt}\n{contract_section}"
    
    def _get_base_system_prompt(self) -> str:
        """Get the base system prompt for this agent role. Subclasses override."""
        return f"You are the {self.config.role.value} agent."
