"""
Comprehensive Agent Workflow Handoffs Test

Tests and documents ALL workflow handoffs between agents in the multi-agent system.
This test serves as both validation and living documentation of agent collaboration patterns.

This test is maintained by the TesterAgent and should be run:
- When any agent workflow process is added or changed
- As part of CI/CD pipeline for multi-agent service
- On demand via TesterAgent's validate_workflow_handoffs tool

Workflow Categories:
1. Entity Design Workflow (Architect -> Business Analyst -> Developer -> Tester -> Documenter)
2. ML/Predictive Workflow (Data Scientist -> Architect -> Developer -> Tester -> Documenter)
3. Sales Workflow (Marketing -> Sales -> Project Manager)
4. Customer Success Workflow (Customer Success -> Sales, Data Scientist)
5. Operations Workflow (Operations -> Data Scientist, Process Engineer)
6. Governance Workflow (Architect -> Data Governance)
7. Integration Workflow (Integration Specialist -> Developer, Mapping Specialist)
8. Knowledge Curation Workflow (Librarian -> Architect, Business Analyst)
"""

import asyncio
import json
import logging
import sys
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

sys.path.insert(0, str(Path(__file__).parent.parent))

# Import from the shared registry
try:
    from services.backend_services.multi_agent_service.app.agents.workflow_handoff_registry import (
        get_handoff_registry,
        WorkflowHandoffRegistry,
        HandoffDefinition as RegistryHandoffDefinition,
        AgentType as RegistryAgentType,
        WorkflowCategory as RegistryWorkflowCategory
    )
    REGISTRY_AVAILABLE = True
except ImportError:
    REGISTRY_AVAILABLE = False

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

TEST_RESULTS_DIR = Path(__file__).parent.parent / "test_results"


# Local definitions for standalone test execution
class AgentType(Enum):
    """All agent types in the multi-agent system."""
    # Sub Agents
    ARCHITECT = "ArchitectAgent"
    BUSINESS_ANALYST = "BusinessAnalystAgent"
    DEVELOPER = "DeveloperAgent"
    TESTER = "TesterAgent"
    DOCUMENTER = "DocumenterAgent"
    DATA_ANALYST = "DataAnalystAgent"
    DATA_GOVERNANCE = "DataGovernanceSpecialistAgent"
    RELEASE_MANAGER = "ReleaseManagerAgent"
    DATA_QUALITY = "DataQualityAnalystAgent"
    INTEGRATION_SPECIALIST = "IntegrationSpecialistAgent"
    MAPPING_SPECIALIST = "MappingSpecialistAgent"
    LIBRARIAN_CURATOR = "LibrarianCuratorAgent"
    FORMULA_BUILDER = "FormulaBuilderAgent"
    
    # Business Agents
    SALES_MANAGER = "SalesManagerAgent"
    MARKETING_MANAGER = "MarketingManagerAgent"
    DATA_SCIENTIST = "DataScientistAgent"
    BUSINESS_STRATEGIST = "BusinessStrategistAgent"
    DATA_STEWARD = "DataStewardAgent"
    CUSTOMER_SUCCESS = "CustomerSuccessManagerAgent"
    OPERATIONS_MANAGER = "OperationsManagerAgent"
    PROJECT_MANAGER = "ProjectManagerAgent"
    ACCOUNTANT = "AccountantAgent"
    COMPETITIVE_ANALYST = "CompetitiveAnalystAgent"
    PROCESS_ENGINEER = "ProcessEngineerAgent"
    UI_DESIGNER = "UIDesignerAgent"
    DEPLOYMENT_SPECIALIST = "DeploymentSpecialistAgent"


class WorkflowCategory(Enum):
    """Workflow categories for organizing handoffs."""
    ENTITY_DESIGN = "Entity Design Workflow"
    ML_PREDICTIVE = "ML/Predictive Model Workflow"
    SALES_PIPELINE = "Sales Pipeline Workflow"
    CUSTOMER_SUCCESS = "Customer Success Workflow"
    OPERATIONS = "Operations Workflow"
    GOVERNANCE = "Governance Workflow"
    INTEGRATION = "Integration Workflow"
    KNOWLEDGE_CURATION = "Knowledge Curation Workflow"
    ANALYTICS = "Analytics Workflow"
    RELEASE = "Release Management Workflow"


@dataclass
class HandoffDefinition:
    """Definition of a handoff between agents."""
    name: str
    tool_name: str
    source_agent: AgentType
    target_agent: AgentType
    category: WorkflowCategory
    description: str
    required_inputs: List[str]
    expected_outputs: List[str]
    bidirectional: bool = False
    response_tool: Optional[str] = None


@dataclass
class AgentContext:
    """Simulated agent context for testing."""
    session_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    value_chain_type: Optional[str] = "supply_chain"
    industry: Optional[str] = "B2B SaaS"
    artifacts: Dict[str, Any] = field(default_factory=dict)


@dataclass
class HandoffTestResult:
    """Result from a handoff test."""
    handoff_name: str
    tool_name: str
    source_agent: str
    target_agent: str
    category: str
    success: bool
    artifact_id: Optional[str] = None
    error: Optional[str] = None
    duration_ms: float = 0.0


# =============================================================================
# COMPLETE HANDOFF REGISTRY
# =============================================================================

HANDOFF_REGISTRY: List[HandoffDefinition] = [
    # =========================================================================
    # ENTITY DESIGN WORKFLOW
    # =========================================================================
    HandoffDefinition(
        name="Architect requests entity validation",
        tool_name="request_entity_validation",
        source_agent=AgentType.ARCHITECT,
        target_agent=AgentType.BUSINESS_ANALYST,
        category=WorkflowCategory.ENTITY_DESIGN,
        description="Architect requests Business Analyst to validate entity design against industry best practices",
        required_inputs=["entity_name", "entity_type", "proposed_attributes"],
        expected_outputs=["validation_status", "recommendations"],
        bidirectional=True,
        response_tool="share_entity_validation"
    ),
    HandoffDefinition(
        name="Architect requests KPI requirements",
        tool_name="request_kpi_requirements",
        source_agent=AgentType.ARCHITECT,
        target_agent=AgentType.BUSINESS_ANALYST,
        category=WorkflowCategory.ENTITY_DESIGN,
        description="Architect requests Business Analyst to identify KPIs for designed entities",
        required_inputs=["entity_name", "business_context"],
        expected_outputs=["kpi_list", "measurement_requirements"]
    ),
    HandoffDefinition(
        name="Architect requests schema generation",
        tool_name="request_schema_generation",
        source_agent=AgentType.ARCHITECT,
        target_agent=AgentType.DEVELOPER,
        category=WorkflowCategory.ENTITY_DESIGN,
        description="Architect requests Developer to generate schemas from entity designs",
        required_inputs=["entity_definitions", "schema_type"],
        expected_outputs=["schema_artifacts"],
        bidirectional=True,
        response_tool="share_schema_artifacts"
    ),
    HandoffDefinition(
        name="Developer requests test specification",
        tool_name="request_test_specification",
        source_agent=AgentType.DEVELOPER,
        target_agent=AgentType.TESTER,
        category=WorkflowCategory.ENTITY_DESIGN,
        description="Developer requests Tester to create test specifications for generated code",
        required_inputs=["code_artifact", "test_requirements"],
        expected_outputs=["test_specification", "test_cases"]
    ),
    HandoffDefinition(
        name="Developer requests documentation",
        tool_name="request_documentation",
        source_agent=AgentType.DEVELOPER,
        target_agent=AgentType.DOCUMENTER,
        category=WorkflowCategory.ENTITY_DESIGN,
        description="Developer requests Documenter to create documentation for generated code",
        required_inputs=["code_artifact", "doc_type"],
        expected_outputs=["documentation"]
    ),
    HandoffDefinition(
        name="Tester requests test documentation",
        tool_name="request_test_documentation",
        source_agent=AgentType.TESTER,
        target_agent=AgentType.DOCUMENTER,
        category=WorkflowCategory.ENTITY_DESIGN,
        description="Tester requests Documenter to create test documentation",
        required_inputs=["test_suite", "test_cases"],
        expected_outputs=["test_documentation"]
    ),
    
    # =========================================================================
    # ML/PREDICTIVE MODEL WORKFLOW
    # =========================================================================
    HandoffDefinition(
        name="Data Scientist handoff to Architect for model design",
        tool_name="handoff_to_architect_for_model_design",
        source_agent=AgentType.DATA_SCIENTIST,
        target_agent=AgentType.ARCHITECT,
        category=WorkflowCategory.ML_PREDICTIVE,
        description="Data Scientist hands off correlation analysis to Architect for ML model architecture design",
        required_inputs=["correlation_analysis_id", "model_type", "target_variable", "features"],
        expected_outputs=["model_architecture"]
    ),
    HandoffDefinition(
        name="Data Scientist handoff to Developer for implementation",
        tool_name="handoff_to_developer_for_implementation",
        source_agent=AgentType.DATA_SCIENTIST,
        target_agent=AgentType.DEVELOPER,
        category=WorkflowCategory.ML_PREDICTIVE,
        description="Data Scientist hands off model specification to Developer for implementation",
        required_inputs=["model_specification_id", "architecture_id"],
        expected_outputs=["implementation_artifacts"]
    ),
    HandoffDefinition(
        name="Data Scientist requests architecture review",
        tool_name="request_architecture_review",
        source_agent=AgentType.DATA_SCIENTIST,
        target_agent=AgentType.ARCHITECT,
        category=WorkflowCategory.ML_PREDICTIVE,
        description="Data Scientist requests Architect to review proposed model architecture",
        required_inputs=["model_specification", "architecture_proposal"],
        expected_outputs=["review_feedback", "approval_status"]
    ),
    HandoffDefinition(
        name="Architect handoff ML architecture to Developer",
        tool_name="handoff_model_architecture_to_developer",
        source_agent=AgentType.ARCHITECT,
        target_agent=AgentType.DEVELOPER,
        category=WorkflowCategory.ML_PREDICTIVE,
        description="Architect hands off ML model architecture to Developer for implementation",
        required_inputs=["architecture_id", "model_specification_id"],
        expected_outputs=["implementation_plan"]
    ),
    HandoffDefinition(
        name="Developer handoff ML to Tester",
        tool_name="handoff_ml_to_tester",
        source_agent=AgentType.DEVELOPER,
        target_agent=AgentType.TESTER,
        category=WorkflowCategory.ML_PREDICTIVE,
        description="Developer hands off ML model implementation to Tester for testing",
        required_inputs=["model_specification_id", "implementation_id", "model_type"],
        expected_outputs=["test_plan", "test_results"]
    ),
    HandoffDefinition(
        name="Developer handoff ML to Documenter",
        tool_name="handoff_ml_to_documenter",
        source_agent=AgentType.DEVELOPER,
        target_agent=AgentType.DOCUMENTER,
        category=WorkflowCategory.ML_PREDICTIVE,
        description="Developer hands off ML model to Documenter for documentation",
        required_inputs=["model_specification_id", "model_name", "model_purpose"],
        expected_outputs=["model_documentation", "api_documentation", "user_guide"]
    ),
    
    # =========================================================================
    # ANALYTICS WORKFLOW
    # =========================================================================
    HandoffDefinition(
        name="Business Analyst requests KPI calculation design",
        tool_name="request_kpi_calculation_design",
        source_agent=AgentType.BUSINESS_ANALYST,
        target_agent=AgentType.DATA_ANALYST,
        category=WorkflowCategory.ANALYTICS,
        description="Business Analyst requests Data Analyst to design calculation logic for KPIs",
        required_inputs=["kpi_list", "calculation_requirements"],
        expected_outputs=["calculation_definitions"]
    ),
    HandoffDefinition(
        name="Business Analyst requests predictive analysis",
        tool_name="request_predictive_analysis",
        source_agent=AgentType.BUSINESS_ANALYST,
        target_agent=AgentType.DATA_SCIENTIST,
        category=WorkflowCategory.ANALYTICS,
        description="Business Analyst requests Data Scientist to analyze KPIs for predictive opportunities",
        required_inputs=["kpi_ids"],
        expected_outputs=["predictive_opportunities", "correlation_analysis"]
    ),
    HandoffDefinition(
        name="Data Steward requests statistical validation",
        tool_name="request_statistical_validation",
        source_agent=AgentType.DATA_STEWARD,
        target_agent=AgentType.DATA_SCIENTIST,
        category=WorkflowCategory.ANALYTICS,
        description="Data Steward requests Data Scientist to validate KPI correlations statistically",
        required_inputs=["kpi_pairs", "suspected_correlations"],
        expected_outputs=["statistical_validation", "p_values"]
    ),
    HandoffDefinition(
        name="Data Steward requests ML model design",
        tool_name="request_ml_model_design",
        source_agent=AgentType.DATA_STEWARD,
        target_agent=AgentType.DATA_SCIENTIST,
        category=WorkflowCategory.ANALYTICS,
        description="Data Steward collaborates with Data Scientist on predictive ML models",
        required_inputs=["target_kpi", "feature_kpis"],
        expected_outputs=["model_design", "feature_importance"]
    ),
    HandoffDefinition(
        name="Formula Builder requests Data Analyst review",
        tool_name="request_data_analyst_review",
        source_agent=AgentType.FORMULA_BUILDER,
        target_agent=AgentType.DATA_ANALYST,
        category=WorkflowCategory.ANALYTICS,
        description="Formula Builder requests Data Analyst to review calculation logic",
        required_inputs=["formula_definition", "calculation_steps"],
        expected_outputs=["review_feedback", "optimization_suggestions"]
    ),
    
    # =========================================================================
    # SALES PIPELINE WORKFLOW
    # =========================================================================
    HandoffDefinition(
        name="Sales Manager requests MQL from Marketing",
        tool_name="request_mql_from_marketing",
        source_agent=AgentType.SALES_MANAGER,
        target_agent=AgentType.MARKETING_MANAGER,
        category=WorkflowCategory.SALES_PIPELINE,
        description="Sales Manager requests Marketing Qualified Leads from Marketing",
        required_inputs=["lead_criteria", "quantity_needed"],
        expected_outputs=["mql_list"]
    ),
    HandoffDefinition(
        name="Sales Manager requests deal pricing",
        tool_name="request_deal_pricing",
        source_agent=AgentType.SALES_MANAGER,
        target_agent=AgentType.ACCOUNTANT,
        category=WorkflowCategory.SALES_PIPELINE,
        description="Sales Manager requests deal pricing from Accountant",
        required_inputs=["deal_id", "pricing_requirements"],
        expected_outputs=["pricing_proposal", "financial_terms"]
    ),
    HandoffDefinition(
        name="Sales Manager handoff to Project Manager",
        tool_name="handoff_to_project_manager",
        source_agent=AgentType.SALES_MANAGER,
        target_agent=AgentType.PROJECT_MANAGER,
        category=WorkflowCategory.SALES_PIPELINE,
        description="Sales Manager hands off won deal to Project Manager for onboarding",
        required_inputs=["deal_id", "client_info", "contract_terms"],
        expected_outputs=["onboarding_plan"]
    ),
    HandoffDefinition(
        name="Marketing Manager handoff MQL to Sales",
        tool_name="handoff_mql_to_sales",
        source_agent=AgentType.MARKETING_MANAGER,
        target_agent=AgentType.SALES_MANAGER,
        category=WorkflowCategory.SALES_PIPELINE,
        description="Marketing Manager hands off qualified leads to Sales Manager",
        required_inputs=["lead_list", "qualification_criteria"],
        expected_outputs=["acceptance_status"]
    ),
    HandoffDefinition(
        name="Marketing Manager requests campaign analytics",
        tool_name="request_campaign_analytics",
        source_agent=AgentType.MARKETING_MANAGER,
        target_agent=AgentType.DATA_SCIENTIST,
        category=WorkflowCategory.SALES_PIPELINE,
        description="Marketing Manager requests campaign performance analysis",
        required_inputs=["campaign_id"],
        expected_outputs=["performance_analysis", "recommendations"]
    ),
    HandoffDefinition(
        name="Marketing Manager requests design assets",
        tool_name="request_design_assets",
        source_agent=AgentType.MARKETING_MANAGER,
        target_agent=AgentType.UI_DESIGNER,
        category=WorkflowCategory.SALES_PIPELINE,
        description="Marketing Manager requests design assets for campaigns",
        required_inputs=["campaign_brief", "asset_requirements"],
        expected_outputs=["design_assets"]
    ),
    
    # =========================================================================
    # CUSTOMER SUCCESS WORKFLOW
    # =========================================================================
    HandoffDefinition(
        name="Customer Success requests churn prediction model",
        tool_name="request_churn_prediction_model",
        source_agent=AgentType.CUSTOMER_SUCCESS,
        target_agent=AgentType.DATA_SCIENTIST,
        category=WorkflowCategory.CUSTOMER_SUCCESS,
        description="Customer Success requests churn prediction model from Data Scientist",
        required_inputs=["customer_segment", "prediction_requirements"],
        expected_outputs=["churn_model", "risk_scores"]
    ),
    HandoffDefinition(
        name="Customer Success handoff expansion to Sales",
        tool_name="handoff_expansion_to_sales",
        source_agent=AgentType.CUSTOMER_SUCCESS,
        target_agent=AgentType.SALES_MANAGER,
        category=WorkflowCategory.CUSTOMER_SUCCESS,
        description="Customer Success hands off expansion opportunity to Sales",
        required_inputs=["customer_id", "expansion_opportunity"],
        expected_outputs=["sales_engagement_plan"]
    ),
    
    # =========================================================================
    # OPERATIONS WORKFLOW
    # =========================================================================
    HandoffDefinition(
        name="Operations Manager requests demand forecast model",
        tool_name="request_demand_forecast_model",
        source_agent=AgentType.OPERATIONS_MANAGER,
        target_agent=AgentType.DATA_SCIENTIST,
        category=WorkflowCategory.OPERATIONS,
        description="Operations Manager requests demand forecasting model",
        required_inputs=["forecast_horizon", "product_categories"],
        expected_outputs=["forecast_model", "predictions"]
    ),
    HandoffDefinition(
        name="Process Engineer requests operations review",
        tool_name="request_operations_review",
        source_agent=AgentType.PROCESS_ENGINEER,
        target_agent=AgentType.OPERATIONS_MANAGER,
        category=WorkflowCategory.OPERATIONS,
        description="Process Engineer requests Operations Manager to review simulation results",
        required_inputs=["simulation_id", "process_changes"],
        expected_outputs=["review_feedback", "approval_status"]
    ),
    
    # =========================================================================
    # GOVERNANCE WORKFLOW
    # =========================================================================
    HandoffDefinition(
        name="Architect requests governance review",
        tool_name="request_governance_review",
        source_agent=AgentType.ARCHITECT,
        target_agent=AgentType.DATA_GOVERNANCE,
        category=WorkflowCategory.GOVERNANCE,
        description="Architect requests Data Governance Specialist to review entity design for compliance",
        required_inputs=["entity_definition", "compliance_requirements"],
        expected_outputs=["compliance_status", "recommendations"]
    ),
    
    # =========================================================================
    # INTEGRATION WORKFLOW
    # =========================================================================
    HandoffDefinition(
        name="Integration Specialist requests mapping assistance",
        tool_name="request_mapping_assistance",
        source_agent=AgentType.INTEGRATION_SPECIALIST,
        target_agent=AgentType.MAPPING_SPECIALIST,
        category=WorkflowCategory.INTEGRATION,
        description="Integration Specialist requests help with field mappings",
        required_inputs=["source_schema", "target_schema"],
        expected_outputs=["field_mappings", "transformation_rules"]
    ),
    HandoffDefinition(
        name="Integration Specialist requests custom development",
        tool_name="request_custom_development",
        source_agent=AgentType.INTEGRATION_SPECIALIST,
        target_agent=AgentType.DEVELOPER,
        category=WorkflowCategory.INTEGRATION,
        description="Integration Specialist requests custom integration code",
        required_inputs=["integration_requirements", "api_specifications"],
        expected_outputs=["integration_code"]
    ),
    HandoffDefinition(
        name="Data Quality Analyst requests data profiling",
        tool_name="request_data_profiling",
        source_agent=AgentType.DATA_QUALITY,
        target_agent=AgentType.DATA_ANALYST,
        category=WorkflowCategory.INTEGRATION,
        description="Data Quality Analyst requests Data Analyst to profile source data",
        required_inputs=["data_source", "profiling_requirements"],
        expected_outputs=["data_profile", "quality_metrics"]
    ),
    
    # =========================================================================
    # KNOWLEDGE CURATION WORKFLOW
    # =========================================================================
    HandoffDefinition(
        name="Librarian Curator requests Architect review",
        tool_name="request_architect_review",
        source_agent=AgentType.LIBRARIAN_CURATOR,
        target_agent=AgentType.ARCHITECT,
        category=WorkflowCategory.KNOWLEDGE_CURATION,
        description="Librarian Curator requests Architect to review extracted entities for DDD design",
        required_inputs=["extracted_entities", "domain_context"],
        expected_outputs=["design_feedback", "entity_refinements"]
    ),
    HandoffDefinition(
        name="Librarian Curator requests Business Analyst review",
        tool_name="request_business_analyst_review",
        source_agent=AgentType.LIBRARIAN_CURATOR,
        target_agent=AgentType.BUSINESS_ANALYST,
        category=WorkflowCategory.KNOWLEDGE_CURATION,
        description="Librarian Curator requests Business Analyst to review extracted KPIs",
        required_inputs=["extracted_kpis", "business_context"],
        expected_outputs=["kpi_validation", "business_alignment"]
    ),
    HandoffDefinition(
        name="Business Strategist requests competitive analysis",
        tool_name="request_competitive_analysis",
        source_agent=AgentType.BUSINESS_STRATEGIST,
        target_agent=AgentType.COMPETITIVE_ANALYST,
        category=WorkflowCategory.KNOWLEDGE_CURATION,
        description="Business Strategist requests competitive analysis after business model elicitation",
        required_inputs=["business_model", "market_segment"],
        expected_outputs=["competitive_landscape", "peer_analysis"]
    ),
    HandoffDefinition(
        name="Competitive Analyst requests Strategist review",
        tool_name="request_strategist_review",
        source_agent=AgentType.COMPETITIVE_ANALYST,
        target_agent=AgentType.BUSINESS_STRATEGIST,
        category=WorkflowCategory.KNOWLEDGE_CURATION,
        description="Competitive Analyst requests Business Strategist to review findings",
        required_inputs=["competitive_findings", "market_analysis"],
        expected_outputs=["strategic_implications", "recommendations"]
    ),
    
    # =========================================================================
    # RELEASE MANAGEMENT WORKFLOW
    # =========================================================================
    HandoffDefinition(
        name="Developer requests deployment config",
        tool_name="request_deployment_config",
        source_agent=AgentType.DEVELOPER,
        target_agent=AgentType.DEPLOYMENT_SPECIALIST,
        category=WorkflowCategory.RELEASE,
        description="Developer requests deployment configuration from Deployment Specialist",
        required_inputs=["artifact_id", "deployment_target"],
        expected_outputs=["deployment_config", "infrastructure_requirements"]
    ),
    HandoffDefinition(
        name="Release Manager requests deployment review",
        tool_name="request_deployment_review",
        source_agent=AgentType.RELEASE_MANAGER,
        target_agent=AgentType.DEPLOYMENT_SPECIALIST,
        category=WorkflowCategory.RELEASE,
        description="Release Manager requests Deployment Specialist to review release plan",
        required_inputs=["release_plan", "deployment_schedule"],
        expected_outputs=["review_feedback", "approval_status"]
    ),
]


class AgentWorkflowHandoffTester:
    """Comprehensive tester for all agent workflow handoffs."""
    
    def __init__(self):
        self.context = AgentContext()
        self.results: List[HandoffTestResult] = []
        self.summary: Dict[str, Any] = {}
    
    async def simulate_handoff(
        self,
        handoff: HandoffDefinition
    ) -> Tuple[bool, Optional[str], Optional[Dict[str, Any]]]:
        """Simulate a handoff between agents."""
        try:
            # Create simulated handoff artifact
            artifact = {
                "id": f"{handoff.tool_name.upper()}-{str(uuid.uuid4())[:8].upper()}",
                "handoff_type": f"{handoff.source_agent.value}_to_{handoff.target_agent.value}",
                "tool_name": handoff.tool_name,
                "source_agent": handoff.source_agent.value,
                "target_agent": handoff.target_agent.value,
                "category": handoff.category.value,
                "required_inputs": {inp: f"test_{inp}" for inp in handoff.required_inputs},
                "status": f"pending_{handoff.target_agent.value.lower()}",
                "created_at": datetime.utcnow().isoformat()
            }
            
            # Store in context artifacts
            artifact_key = f"{handoff.category.name.lower()}_handoffs"
            if artifact_key not in self.context.artifacts:
                self.context.artifacts[artifact_key] = []
            self.context.artifacts[artifact_key].append(artifact)
            
            return True, artifact["id"], artifact
            
        except Exception as e:
            return False, None, {"error": str(e)}
    
    async def test_handoff(self, handoff: HandoffDefinition) -> HandoffTestResult:
        """Test a single handoff."""
        start_time = datetime.utcnow()
        
        success, artifact_id, artifact_data = await self.simulate_handoff(handoff)
        
        duration_ms = (datetime.utcnow() - start_time).total_seconds() * 1000
        
        return HandoffTestResult(
            handoff_name=handoff.name,
            tool_name=handoff.tool_name,
            source_agent=handoff.source_agent.value,
            target_agent=handoff.target_agent.value,
            category=handoff.category.value,
            success=success,
            artifact_id=artifact_id,
            error=artifact_data.get("error") if not success else None,
            duration_ms=duration_ms
        )
    
    async def run_all_tests(self) -> None:
        """Run all handoff tests."""
        logger.info("=" * 70)
        logger.info("COMPREHENSIVE AGENT WORKFLOW HANDOFFS TEST")
        logger.info("=" * 70)
        logger.info(f"Total handoffs to test: {len(HANDOFF_REGISTRY)}")
        
        # Group by category for organized output
        by_category: Dict[WorkflowCategory, List[HandoffDefinition]] = {}
        for handoff in HANDOFF_REGISTRY:
            if handoff.category not in by_category:
                by_category[handoff.category] = []
            by_category[handoff.category].append(handoff)
        
        for category, handoffs in by_category.items():
            logger.info(f"\n--- {category.value} ({len(handoffs)} handoffs) ---")
            for handoff in handoffs:
                result = await self.test_handoff(handoff)
                self.results.append(result)
                status = "PASS" if result.success else "FAIL"
                logger.info(f"  [{status}] {handoff.source_agent.value} -> {handoff.target_agent.value}: {handoff.tool_name}")
        
        self.generate_summary()
    
    def generate_summary(self) -> Dict[str, Any]:
        """Generate comprehensive test summary."""
        total = len(self.results)
        passed = sum(1 for r in self.results if r.success)
        
        # Count by category
        category_stats = {}
        for result in self.results:
            cat = result.category
            if cat not in category_stats:
                category_stats[cat] = {"total": 0, "passed": 0}
            category_stats[cat]["total"] += 1
            if result.success:
                category_stats[cat]["passed"] += 1
        
        # Count unique agent pairs
        agent_pairs = set()
        for result in self.results:
            agent_pairs.add((result.source_agent, result.target_agent))
        
        # Build agent collaboration matrix
        agents_as_source = {}
        agents_as_target = {}
        for result in self.results:
            if result.source_agent not in agents_as_source:
                agents_as_source[result.source_agent] = 0
            agents_as_source[result.source_agent] += 1
            
            if result.target_agent not in agents_as_target:
                agents_as_target[result.target_agent] = 0
            agents_as_target[result.target_agent] += 1
        
        self.summary = {
            "test_run_id": f"HANDOFF-TEST-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}",
            "timestamp": datetime.utcnow().isoformat(),
            "total_handoffs": total,
            "passed": passed,
            "failed": total - passed,
            "success_rate": (passed / total * 100) if total > 0 else 0,
            "unique_agent_pairs": len(agent_pairs),
            "workflow_categories": len(category_stats),
            "category_breakdown": category_stats,
            "agents_as_source": dict(sorted(agents_as_source.items(), key=lambda x: -x[1])),
            "agents_as_target": dict(sorted(agents_as_target.items(), key=lambda x: -x[1])),
        }
        
        return self.summary
    
    def generate_handoff_documentation(self) -> str:
        """Generate comprehensive documentation of all handoffs."""
        doc = """# Agent Workflow Handoffs Documentation

This document provides a comprehensive reference of all workflow handoffs between agents
in the AnalyticsEngine multi-agent system.

## Overview

"""
        doc += f"- **Total Handoff Types:** {len(HANDOFF_REGISTRY)}\n"
        doc += f"- **Workflow Categories:** {len(WorkflowCategory)}\n"
        doc += f"- **Agent Types:** {len(AgentType)}\n\n"
        
        doc += "## Handoff Matrix\n\n"
        doc += "| Source Agent | Target Agent | Tool Name | Category |\n"
        doc += "|-------------|--------------|-----------|----------|\n"
        for handoff in HANDOFF_REGISTRY:
            doc += f"| {handoff.source_agent.value} | {handoff.target_agent.value} | `{handoff.tool_name}` | {handoff.category.value} |\n"
        
        doc += "\n---\n\n## Handoffs by Workflow Category\n\n"
        
        # Group by category
        by_category: Dict[WorkflowCategory, List[HandoffDefinition]] = {}
        for handoff in HANDOFF_REGISTRY:
            if handoff.category not in by_category:
                by_category[handoff.category] = []
            by_category[handoff.category].append(handoff)
        
        for category, handoffs in by_category.items():
            doc += f"### {category.value}\n\n"
            for handoff in handoffs:
                doc += f"#### {handoff.name}\n\n"
                doc += f"- **Tool:** `{handoff.tool_name}`\n"
                doc += f"- **Source:** {handoff.source_agent.value}\n"
                doc += f"- **Target:** {handoff.target_agent.value}\n"
                doc += f"- **Description:** {handoff.description}\n"
                doc += f"- **Required Inputs:** {', '.join(handoff.required_inputs)}\n"
                doc += f"- **Expected Outputs:** {', '.join(handoff.expected_outputs)}\n"
                if handoff.bidirectional:
                    doc += f"- **Response Tool:** `{handoff.response_tool}`\n"
                doc += "\n"
        
        doc += "---\n\n## Agent Collaboration Summary\n\n"
        
        # Count agents as source and target
        source_counts = {}
        target_counts = {}
        for handoff in HANDOFF_REGISTRY:
            src = handoff.source_agent.value
            tgt = handoff.target_agent.value
            source_counts[src] = source_counts.get(src, 0) + 1
            target_counts[tgt] = target_counts.get(tgt, 0) + 1
        
        doc += "### Agents as Handoff Source\n\n"
        doc += "| Agent | Outgoing Handoffs |\n"
        doc += "|-------|------------------|\n"
        for agent, count in sorted(source_counts.items(), key=lambda x: -x[1]):
            doc += f"| {agent} | {count} |\n"
        
        doc += "\n### Agents as Handoff Target\n\n"
        doc += "| Agent | Incoming Handoffs |\n"
        doc += "|-------|------------------|\n"
        for agent, count in sorted(target_counts.items(), key=lambda x: -x[1]):
            doc += f"| {agent} | {count} |\n"
        
        return doc
    
    def save_results(self, output_dir: Path) -> Tuple[str, str]:
        """Save test results and documentation."""
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        
        # Test results markdown
        results_path = output_dir / f"agent_handoff_test_{timestamp}.md"
        
        results_content = f"""# Agent Workflow Handoffs Test Results

**Test Run ID:** {self.summary.get('test_run_id', 'N/A')}  
**Timestamp:** {self.summary.get('timestamp', 'N/A')}  

---

## Summary

| Metric | Value |
|--------|-------|
| Total Handoffs Tested | {self.summary['total_handoffs']} |
| Passed | {self.summary['passed']} |
| Failed | {self.summary['failed']} |
| Success Rate | {self.summary['success_rate']:.1f}% |
| Unique Agent Pairs | {self.summary['unique_agent_pairs']} |
| Workflow Categories | {self.summary['workflow_categories']} |

## Results by Category

"""
        for category, stats in self.summary['category_breakdown'].items():
            pct = (stats['passed'] / stats['total'] * 100) if stats['total'] > 0 else 0
            results_content += f"### {category}\n\n"
            results_content += f"- Passed: {stats['passed']}/{stats['total']} ({pct:.0f}%)\n\n"
        
        results_content += "## Detailed Results\n\n"
        results_content += "| Handoff | Source | Target | Category | Status |\n"
        results_content += "|---------|--------|--------|----------|--------|\n"
        
        for result in self.results:
            status = "PASS" if result.success else "FAIL"
            results_content += f"| `{result.tool_name}` | {result.source_agent} | {result.target_agent} | {result.category} | {status} |\n"
        
        with open(results_path, 'w', encoding='utf-8') as f:
            f.write(results_content)
        
        # Comprehensive documentation
        doc_path = output_dir / f"AGENT_HANDOFF_DOCUMENTATION_{timestamp}.md"
        doc_content = self.generate_handoff_documentation()
        
        with open(doc_path, 'w', encoding='utf-8') as f:
            f.write(doc_content)
        
        # JSON results
        json_path = output_dir / f"agent_handoff_test_{timestamp}.json"
        json_data = {
            "summary": self.summary,
            "handoff_registry": [
                {
                    "name": h.name,
                    "tool_name": h.tool_name,
                    "source_agent": h.source_agent.value,
                    "target_agent": h.target_agent.value,
                    "category": h.category.value,
                    "description": h.description,
                    "required_inputs": h.required_inputs,
                    "expected_outputs": h.expected_outputs,
                    "bidirectional": h.bidirectional,
                    "response_tool": h.response_tool
                }
                for h in HANDOFF_REGISTRY
            ],
            "test_results": [
                {
                    "handoff_name": r.handoff_name,
                    "tool_name": r.tool_name,
                    "source_agent": r.source_agent,
                    "target_agent": r.target_agent,
                    "category": r.category,
                    "success": r.success,
                    "artifact_id": r.artifact_id,
                    "error": r.error
                }
                for r in self.results
            ]
        }
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2)
        
        logger.info(f"Results saved to: {results_path}")
        logger.info(f"Documentation saved to: {doc_path}")
        
        return str(results_path), str(doc_path)


def get_handoff_registry_for_test() -> List[HandoffDefinition]:
    """
    Get the handoff registry - uses shared registry if available,
    otherwise falls back to local HANDOFF_REGISTRY.
    
    This allows the test to work both:
    - Standalone (using local definitions)
    - Integrated with TesterAgent (using shared registry)
    """
    if REGISTRY_AVAILABLE:
        logger.info("Using shared WorkflowHandoffRegistry")
        registry = get_handoff_registry()
        # Convert registry handoffs to local HandoffDefinition format
        handoffs = []
        for h in registry.handoffs:
            handoffs.append(HandoffDefinition(
                name=h.name,
                tool_name=h.tool_name,
                source_agent=AgentType(h.source_agent.value),
                target_agent=AgentType(h.target_agent.value),
                category=WorkflowCategory(h.category.value),
                description=h.description,
                required_inputs=h.required_inputs,
                expected_outputs=h.expected_outputs,
                bidirectional=h.bidirectional,
                response_tool=h.response_tool
            ))
        return handoffs
    else:
        logger.info("Using local HANDOFF_REGISTRY (shared registry not available)")
        return HANDOFF_REGISTRY


async def run_workflow_validation(
    category_filter: Optional[str] = None,
    save_results: bool = True
) -> Dict[str, Any]:
    """
    Run workflow validation - callable by TesterAgent or directly.
    
    Args:
        category_filter: Optional category to filter validation
        save_results: Whether to save results to files
    
    Returns:
        Validation summary dictionary
    """
    tester = AgentWorkflowHandoffTester()
    await tester.run_all_tests()
    
    if save_results:
        tester.save_results(TEST_RESULTS_DIR)
    
    return tester.summary


async def main():
    """Run comprehensive agent workflow handoffs test."""
    logger.info(f"Registry available: {REGISTRY_AVAILABLE}")
    
    tester = AgentWorkflowHandoffTester()
    await tester.run_all_tests()
    
    # Print summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Total Handoffs: {tester.summary['total_handoffs']}")
    print(f"Passed: {tester.summary['passed']}")
    print(f"Failed: {tester.summary['failed']}")
    print(f"Success Rate: {tester.summary['success_rate']:.1f}%")
    print(f"Unique Agent Pairs: {tester.summary['unique_agent_pairs']}")
    print(f"Workflow Categories: {tester.summary['workflow_categories']}")
    
    print("\n--- Category Breakdown ---")
    for category, stats in tester.summary['category_breakdown'].items():
        print(f"  {category}: {stats['passed']}/{stats['total']}")
    
    if REGISTRY_AVAILABLE:
        registry = get_handoff_registry()
        print(f"\n--- Registry Info ---")
        print(f"  Registry Hash: {registry.compute_registry_hash()}")
        print(f"  Version: {registry.VERSION}")
    
    # Save results
    tester.save_results(TEST_RESULTS_DIR)
    
    return 0 if tester.summary['failed'] == 0 else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
