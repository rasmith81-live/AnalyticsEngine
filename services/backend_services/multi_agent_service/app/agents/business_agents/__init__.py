# =============================================================================
# Business Agents Package - Domain Specialists
# Migrated from conversation_service as part of architecture consolidation
# =============================================================================
"""
Business domain specialist agents for the multi-agent system.

These agents handle business-specific tasks like strategy, sales, marketing,
operations, and compliance.
"""

from .agents import (
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
