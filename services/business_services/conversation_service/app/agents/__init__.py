"""
Multi-Agent Framework for Analytics Engine

This module provides a multi-agent architecture using Claude models:
- Strategy Coordinator (Claude Opus 4.5): Master orchestrator
- Specialized Sub-Agents (Claude Sonnet 4): Domain experts

The agents collaborate to design comprehensive business value chain models
through client interviews conducted via the Conversation Service.
"""

from .base_agent import BaseAgent, AgentConfig, AgentResponse, AgentMessage
from .coordinator import StrategyCoordinator
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
    DocumentAnalyzerAgent
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
    ProcessScenarioModelerAgent
)
from .orchestrator import AgentOrchestrator
from .tools import (
    DesignValueChainTool,
    DefineEntityTool,
    IdentifyKPIsTool,
    GenerateSchemaTool,
    ValidateSchemaTool,
    GenerateDocsTool
)

__all__ = [
    # Base classes
    "BaseAgent",
    "AgentConfig",
    "AgentResponse",
    "AgentMessage",
    
    # Coordinator
    "StrategyCoordinator",
    
    # Sub-agents
    "ArchitectAgent",
    "BusinessAnalystAgent",
    "DataAnalystAgent",
    "DeveloperAgent",
    "TesterAgent",
    "DocumenterAgent",
    "DeploymentSpecialistAgent",
    "ProjectManagerAgent",
    
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
    
    # Technical agents
    "ITILManagerAgent",
    
    # Analytics/Integration specialists
    "MappingSpecialistAgent",
    "ConnectionSpecialistAgent",
    
    # Document analysis
    "DocumentAnalyzerAgent",
    
    # Orchestrator
    "AgentOrchestrator",
    
    # Tools
    "DesignValueChainTool",
    "DefineEntityTool",
    "IdentifyKPIsTool",
    "GenerateSchemaTool",
    "ValidateSchemaTool",
    "GenerateDocsTool",
]
