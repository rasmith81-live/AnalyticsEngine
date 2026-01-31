# =============================================================================
# Agent Module for Multi-Agent Service
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# Consolidated from conversation_service as part of architecture migration
# =============================================================================
"""
Agents module providing contract-enabled agents.

This module contains:
- Base agent classes with contract enforcement
- Strategy coordinator and orchestrator
- Technical specialist agents (12 agents)
- Business domain agents (14 agents)
- Contract adapter and blackboard mixin
"""

from .base_agent import AgentRole, ContractAgent
from .contracts import ROLE_CONTRACTS
from .contract_adapter import ContractAdapter, ContractState, ApprovalRequest, StruggleSignal
from .blackboard_mixin import BlackboardAgentMixin
from .coordinator import StrategyCoordinator
from .orchestrator import AgentOrchestrator, DesignSession, OrchestratorConfig

from .sub_agents import (
    ArchitectAgent,
    BusinessAnalystAgent,
    DataAnalystAgent,
    DeveloperAgent,
    TesterAgent,
    DocumenterAgent,
    DeploymentSpecialistAgent,
    ProjectManagerAgent,
    ITILManagerAgent,
    MappingSpecialistAgent,
    ConnectionSpecialistAgent,
    DocumentAnalyzerAgent,
    LibrarianCuratorAgent,
)

from .business_agents import (
    SalesManagerAgent,
    AccountantAgent,
    DataGovernanceSpecialistAgent,
    DataScientistAgent,
    MarketingManagerAgent,
    UIDesignerAgent,
    BusinessStrategistAgent,
    OperationsManagerAgent,
    CustomerSuccessManagerAgent,
    HRTalentAnalystAgent,
    RiskComplianceOfficerAgent,
    SupplyChainAnalystAgent,
    CompetitiveAnalystAgent,
    ProcessScenarioModelerAgent,
)

__all__ = [
    # Core
    "AgentRole",
    "ContractAgent",
    "ROLE_CONTRACTS",
    
    # Contract infrastructure
    "ContractAdapter",
    "ContractState",
    "ApprovalRequest",
    "StruggleSignal",
    "BlackboardAgentMixin",
    
    # Orchestration
    "StrategyCoordinator",
    "AgentOrchestrator",
    "DesignSession",
    "OrchestratorConfig",
    
    # Technical specialists
    "ArchitectAgent",
    "BusinessAnalystAgent",
    "DataAnalystAgent",
    "DeveloperAgent",
    "TesterAgent",
    "DocumenterAgent",
    "DeploymentSpecialistAgent",
    "ProjectManagerAgent",
    "ITILManagerAgent",
    "MappingSpecialistAgent",
    "ConnectionSpecialistAgent",
    "DocumentAnalyzerAgent",
    "LibrarianCuratorAgent",
    
    # Business agents
    "SalesManagerAgent",
    "AccountantAgent",
    "DataGovernanceSpecialistAgent",
    "DataScientistAgent",
    "MarketingManagerAgent",
    "UIDesignerAgent",
    "BusinessStrategistAgent",
    "OperationsManagerAgent",
    "CustomerSuccessManagerAgent",
    "HRTalentAnalystAgent",
    "RiskComplianceOfficerAgent",
    "SupplyChainAnalystAgent",
    "CompetitiveAnalystAgent",
    "ProcessScenarioModelerAgent",
]
