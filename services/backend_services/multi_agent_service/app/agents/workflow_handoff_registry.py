"""
Agent Workflow Handoff Registry

Central registry of all workflow handoffs between agents in the multi-agent system.
This registry is maintained by the TesterAgent and serves as the source of truth
for workflow validation tests.

Usage:
- TesterAgent uses this to validate all agent handoffs are working
- Run validation tests when any agent workflow is added or changed
- Auto-generates documentation of agent collaboration patterns
"""

import json
import hashlib
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field, asdict


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
    added_date: str = field(default_factory=lambda: datetime.utcnow().strftime("%Y-%m-%d"))
    last_validated: Optional[str] = None
    validation_status: str = "pending"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "name": self.name,
            "tool_name": self.tool_name,
            "source_agent": self.source_agent.value,
            "target_agent": self.target_agent.value,
            "category": self.category.value,
            "description": self.description,
            "required_inputs": self.required_inputs,
            "expected_outputs": self.expected_outputs,
            "bidirectional": self.bidirectional,
            "response_tool": self.response_tool,
            "added_date": self.added_date,
            "last_validated": self.last_validated,
            "validation_status": self.validation_status
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "HandoffDefinition":
        """Create from dictionary."""
        return cls(
            name=data["name"],
            tool_name=data["tool_name"],
            source_agent=AgentType(data["source_agent"]),
            target_agent=AgentType(data["target_agent"]),
            category=WorkflowCategory(data["category"]),
            description=data["description"],
            required_inputs=data["required_inputs"],
            expected_outputs=data["expected_outputs"],
            bidirectional=data.get("bidirectional", False),
            response_tool=data.get("response_tool"),
            added_date=data.get("added_date", datetime.utcnow().strftime("%Y-%m-%d")),
            last_validated=data.get("last_validated"),
            validation_status=data.get("validation_status", "pending")
        )


class WorkflowHandoffRegistry:
    """
    Central registry for all agent workflow handoffs.
    
    This registry is the authoritative source for:
    - All defined handoffs between agents
    - Validation status of each handoff
    - Change detection for workflow modifications
    """
    
    # Registry version - increment when schema changes
    VERSION = "1.0.0"
    
    def __init__(self):
        self._handoffs: List[HandoffDefinition] = []
        self._load_default_handoffs()
    
    def _load_default_handoffs(self) -> None:
        """Load the default set of handoffs."""
        self._handoffs = [
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
    
    @property
    def handoffs(self) -> List[HandoffDefinition]:
        """Get all registered handoffs."""
        return self._handoffs
    
    def get_by_category(self, category: WorkflowCategory) -> List[HandoffDefinition]:
        """Get handoffs filtered by category."""
        return [h for h in self._handoffs if h.category == category]
    
    def get_by_source_agent(self, agent: AgentType) -> List[HandoffDefinition]:
        """Get handoffs where agent is the source."""
        return [h for h in self._handoffs if h.source_agent == agent]
    
    def get_by_target_agent(self, agent: AgentType) -> List[HandoffDefinition]:
        """Get handoffs where agent is the target."""
        return [h for h in self._handoffs if h.target_agent == agent]
    
    def get_by_tool_name(self, tool_name: str) -> Optional[HandoffDefinition]:
        """Get handoff by tool name."""
        for h in self._handoffs:
            if h.tool_name == tool_name:
                return h
        return None
    
    def add_handoff(self, handoff: HandoffDefinition) -> None:
        """Add a new handoff to the registry."""
        # Check for duplicates
        existing = self.get_by_tool_name(handoff.tool_name)
        if existing:
            raise ValueError(f"Handoff with tool_name '{handoff.tool_name}' already exists")
        self._handoffs.append(handoff)
    
    def update_validation_status(
        self, 
        tool_name: str, 
        status: str, 
        validated_at: Optional[str] = None
    ) -> bool:
        """Update validation status for a handoff."""
        handoff = self.get_by_tool_name(tool_name)
        if handoff:
            handoff.validation_status = status
            handoff.last_validated = validated_at or datetime.utcnow().isoformat()
            return True
        return False
    
    def compute_registry_hash(self) -> str:
        """Compute a hash of the registry for change detection."""
        data = json.dumps(
            [h.to_dict() for h in self._handoffs],
            sort_keys=True
        )
        return hashlib.sha256(data.encode()).hexdigest()[:16]
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get registry statistics."""
        by_category = {}
        for h in self._handoffs:
            cat = h.category.value
            by_category[cat] = by_category.get(cat, 0) + 1
        
        source_agents = {}
        target_agents = {}
        for h in self._handoffs:
            src = h.source_agent.value
            tgt = h.target_agent.value
            source_agents[src] = source_agents.get(src, 0) + 1
            target_agents[tgt] = target_agents.get(tgt, 0) + 1
        
        validation_status = {}
        for h in self._handoffs:
            vs = h.validation_status
            validation_status[vs] = validation_status.get(vs, 0) + 1
        
        return {
            "version": self.VERSION,
            "total_handoffs": len(self._handoffs),
            "categories": len(by_category),
            "by_category": by_category,
            "unique_source_agents": len(source_agents),
            "unique_target_agents": len(target_agents),
            "source_agents": source_agents,
            "target_agents": target_agents,
            "validation_status": validation_status,
            "registry_hash": self.compute_registry_hash()
        }
    
    def export_to_json(self, path: Path) -> None:
        """Export registry to JSON file."""
        data = {
            "version": self.VERSION,
            "exported_at": datetime.utcnow().isoformat(),
            "registry_hash": self.compute_registry_hash(),
            "handoffs": [h.to_dict() for h in self._handoffs]
        }
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    
    def import_from_json(self, path: Path) -> None:
        """Import registry from JSON file."""
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self._handoffs = [HandoffDefinition.from_dict(h) for h in data["handoffs"]]
    
    def generate_documentation(self) -> str:
        """Generate markdown documentation of the registry."""
        doc = f"""# Agent Workflow Handoff Registry

**Version:** {self.VERSION}  
**Total Handoffs:** {len(self._handoffs)}  
**Registry Hash:** {self.compute_registry_hash()}  
**Generated:** {datetime.utcnow().isoformat()}

---

## Handoff Matrix

| Source Agent | Target Agent | Tool Name | Category |
|-------------|--------------|-----------|----------|
"""
        for h in self._handoffs:
            doc += f"| {h.source_agent.value} | {h.target_agent.value} | `{h.tool_name}` | {h.category.value} |\n"
        
        doc += "\n---\n\n## By Workflow Category\n\n"
        
        by_category: Dict[WorkflowCategory, List[HandoffDefinition]] = {}
        for h in self._handoffs:
            if h.category not in by_category:
                by_category[h.category] = []
            by_category[h.category].append(h)
        
        for category, handoffs in by_category.items():
            doc += f"### {category.value}\n\n"
            for h in handoffs:
                doc += f"**{h.name}**\n"
                doc += f"- Tool: `{h.tool_name}`\n"
                doc += f"- {h.source_agent.value} → {h.target_agent.value}\n"
                doc += f"- Inputs: {', '.join(h.required_inputs)}\n"
                doc += f"- Outputs: {', '.join(h.expected_outputs)}\n\n"
        
        return doc


# Global singleton instance
_registry_instance: Optional[WorkflowHandoffRegistry] = None


def get_handoff_registry() -> WorkflowHandoffRegistry:
    """Get the global handoff registry instance."""
    global _registry_instance
    if _registry_instance is None:
        _registry_instance = WorkflowHandoffRegistry()
    return _registry_instance
