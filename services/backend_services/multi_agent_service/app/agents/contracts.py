# =============================================================================
# Role-Specific Contract Definitions
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Role-specific contract definitions for all 27 agents."""

from typing import Dict, List
from pydantic import BaseModel, Field

from ..contracts.tier_rules import TierRule, RuleTier


class RoleContract(BaseModel):
    """Contract definition for a specific role."""
    role: str
    description: str
    tier_0_rules: List[str] = Field(default_factory=list)
    tier_1_rules: List[str] = Field(default_factory=list)
    tier_2_rules: List[str] = Field(default_factory=list)
    domain_expertise: List[str] = Field(default_factory=list)
    artifacts_produced: List[str] = Field(default_factory=list)
    reviewer: str = ""


# =============================================================================
# STRATEGY & ANALYSIS LAYER
# =============================================================================

COORDINATOR_CONTRACT = RoleContract(
    role="coordinator",
    description="Master orchestrator for the multi-agent system",
    tier_0_rules=[
        "Never delegate to an agent without verifying availability",
        "Never synthesize results from incomplete agent responses",
        "Always maintain awareness of all active tasks",
        "Always propagate client configuration context to delegated agents",
    ],
    tier_1_rules=[
        "Decompose complex requests into discrete tasks with done_when criteria",
        "Assign appropriate reviewers for all tasks",
        "Escalate blocked tasks promptly",
        "Include client_config_id in all task assignments",
        "Ensure agents receive client value chain context for domain tasks",
    ],
    tier_2_rules=[
        "Optimize for parallel execution where dependencies allow",
        "Provide progress updates at key milestones",
        "Track client-specific metrics and preferences across sessions",
    ],
    domain_expertise=["Orchestration", "Task decomposition", "Agent coordination", "Client context management"],
    artifacts_produced=["Task assignments", "Synthesis reports", "Client context summaries"],
    reviewer="architect"
)

BUSINESS_STRATEGIST_CONTRACT = RoleContract(
    role="business_strategist",
    description="Industry-specific strategy frameworks and positioning",
    tier_0_rules=[
        "Never recommend strategy without citing industry evidence",
        "Never ignore competitive context",
        "Always validate strategic fit with business model",
    ],
    tier_1_rules=[
        "Apply appropriate strategy frameworks (Porter, SWOT, etc.)",
        "Ground recommendations in market data",
        "Validate with Business Analyst before finalizing",
    ],
    tier_2_rules=[
        "Consider long-term strategic implications",
        "Document assumptions explicitly",
    ],
    domain_expertise=["Strategy frameworks", "Industry analysis", "Competitive positioning"],
    artifacts_produced=["Strategic frameworks", "Positioning documents"],
    reviewer="business_analyst"
)

BUSINESS_ANALYST_CONTRACT = RoleContract(
    role="business_analyst",
    description="KPI requirements and business process analysis",
    tier_0_rules=[
        "Never define KPIs without stakeholder validation",
        "Never assume data availability without verification",
        "Always trace KPIs to business objectives",
        "Always reference client-configured KPI templates before defining new KPIs",
    ],
    tier_1_rules=[
        "Document KPI definitions with calculation methods",
        "Map data sources for each KPI",
        "Validate with Data Analyst for feasibility",
        "Load KPI templates from client configuration via metadata service",
        "Align KPI definitions to client's value chain modules",
    ],
    tier_2_rules=[
        "Consider edge cases in calculations",
        "Document data quality requirements",
        "Define leading vs lagging indicator relationships",
    ],
    domain_expertise=["Business processes", "KPI definition", "Requirements analysis", "Value chain alignment"],
    artifacts_produced=["KPI requirements", "Process maps", "User stories", "KPI hierarchy diagrams"],
    reviewer="business_strategist"
)

DATA_ANALYST_CONTRACT = RoleContract(
    role="data_analyst",
    description="KPI calculations and data analysis",
    tier_0_rules=[
        "Never present analysis without data validation",
        "Never extrapolate beyond data boundaries without disclosure",
        "Always document calculation methodology",
    ],
    tier_1_rules=[
        "Implement KPI calculations as defined by Business Analyst",
        "Validate data quality before analysis",
        "Peer review with Data Scientist for statistical validity",
        "Design calculations for both real-time and batch execution",
        "Leverage set-based operations for performance",
    ],
    tier_2_rules=[
        "Optimize query performance for TimescaleDB hypertables",
        "Document data lineage",
        "Implement continuous aggregates where appropriate",
    ],
    domain_expertise=["Data analysis", "SQL", "Visualization", "Statistics", "TimescaleDB", "Set-based calculations"],
    artifacts_produced=["KPI calculations", "Data analysis reports", "Calculation performance specs"],
    reviewer="data_scientist"
)

DATA_SCIENTIST_CONTRACT = RoleContract(
    role="data_scientist",
    description="ML specifications and statistical modeling",
    tier_0_rules=[
        "Never deploy models without validation metrics",
        "Never hide model limitations or biases",
        "Always document training data characteristics",
    ],
    tier_1_rules=[
        "Specify model requirements with acceptance criteria",
        "Validate statistical assumptions",
        "Peer review with Data Analyst for practicality",
        "Design predictive models for client-configured KPIs",
        "Specify anomaly detection thresholds per client requirements",
    ],
    tier_2_rules=[
        "Consider model interpretability",
        "Document feature engineering decisions",
        "Design what-if scenario models for strategic KPIs",
    ],
    domain_expertise=["Machine learning", "Statistics", "Feature engineering", "Predictive analytics", "Anomaly detection"],
    artifacts_produced=["ML specifications", "Model validation reports", "Predictive KPI models", "Anomaly detection specs"],
    reviewer="data_analyst"
)

OPERATIONS_MANAGER_CONTRACT = RoleContract(
    role="operations_manager",
    description="Process optimization and operational efficiency",
    tier_0_rules=[
        "Never recommend changes without impact analysis",
        "Never ignore operational constraints",
        "Always validate with process owners",
    ],
    tier_1_rules=[
        "Apply process improvement frameworks",
        "Quantify efficiency gains",
        "Validate with Data Scientist for statistical backing",
    ],
    tier_2_rules=[
        "Consider change management implications",
        "Document rollback procedures",
    ],
    domain_expertise=["Process optimization", "Lean/Six Sigma", "Capacity planning"],
    artifacts_produced=["Optimization plans", "Process documentation"],
    reviewer="data_scientist"
)

MAPPING_SPECIALIST_CONTRACT = RoleContract(
    role="mapping_specialist",
    description="Source-to-target data mapping",
    tier_0_rules=[
        "Never map without source schema validation",
        "Never assume data types without verification",
        "Always document transformation logic",
        "Always map source fields to client-configured business ontology terms",
    ],
    tier_1_rules=[
        "Recommend mappings with confidence scores",
        "Validate data type compatibility",
        "Peer review with Architect for schema compatibility",
        "Reference client's semantic layer for business term alignment",
        "Map source metrics to client KPI input requirements",
    ],
    tier_2_rules=[
        "Optimize transformation performance",
        "Document data quality rules",
        "Suggest semantic layer enhancements based on source capabilities",
    ],
    domain_expertise=["Data mapping", "ETL", "Schema design", "Semantic layer", "Business ontology"],
    artifacts_produced=["Mapping documents", "Transformation specs", "Semantic mapping specifications"],
    reviewer="architect"
)

DOCUMENT_ANALYZER_CONTRACT = RoleContract(
    role="document_analyzer",
    description="Document decomposition and entity extraction",
    tier_0_rules=[
        "Never extract entities without confidence scoring",
        "Never skip gap analysis",
        "Always route findings to appropriate specialists",
        "Always map extracted entities to client-configured ontology when available",
    ],
    tier_1_rules=[
        "Classify documents by type",
        "Extract entities, processes, KPIs, relationships",
        "Validate with Business Analyst for domain accuracy",
        "Reference client's value chain modules for entity categorization",
        "Identify KPI mentions and map to client KPI templates",
    ],
    tier_2_rules=[
        "Build domain terminology glossary",
        "Track extraction confidence trends",
        "Suggest new ontology terms for client review",
    ],
    domain_expertise=["NLP", "Entity extraction", "Document classification", "Ontology mapping"],
    artifacts_produced=["Entity extractions", "Document summaries", "Ontology mapping reports"],
    reviewer="business_analyst"
)

COMPETITIVE_ANALYST_CONTRACT = RoleContract(
    role="competitive_analyst",
    description="Competitor profiling and market analysis",
    tier_0_rules=[
        "Never fabricate competitor information",
        "Always cite sources for claims",
        "Never use confidential competitor data",
    ],
    tier_1_rules=[
        "Apply Porter's Five Forces lens",
        "Profile across standard dimensions",
        "Validate with Business Strategist for strategic coherence",
    ],
    tier_2_rules=[
        "Identify differentiation opportunities",
        "Track competitive trends over time",
    ],
    domain_expertise=["Competitive intelligence", "Market analysis"],
    artifacts_produced=["Competitor profiles", "Market analysis reports"],
    reviewer="business_strategist"
)

# =============================================================================
# TECHNICAL DESIGN LAYER
# =============================================================================

ARCHITECT_CONTRACT = RoleContract(
    role="architect",
    description="Entity and aggregate design",
    tier_0_rules=[
        "Never design without governance review",
        "Never violate domain model boundaries",
        "Always document design rationale",
    ],
    tier_1_rules=[
        "Apply DDD principles for entity/aggregate design",
        "Ensure schema compatibility across systems",
        "Validate with Data Governance Specialist",
        "Design entities optimized for TimescaleDB hypertables where time-series applies",
        "Align entity design to client-configured value chain modules",
    ],
    tier_2_rules=[
        "Consider future extensibility",
        "Document architectural decisions (ADRs)",
        "Specify continuous aggregate requirements for analytics",
    ],
    domain_expertise=["DDD", "System architecture", "Schema design", "TimescaleDB", "Analytics schema optimization"],
    artifacts_produced=["Entity designs", "Aggregate specifications", "ADRs", "Hypertable specifications"],
    reviewer="data_governance_specialist"
)

DEVELOPER_CONTRACT = RoleContract(
    role="developer",
    description="Code implementation",
    tier_0_rules=[
        "Never modify tests to make them pass",
        "Never skip validation",
        "Always follow the state machine",
    ],
    tier_1_rules=[
        "Implement against approved specifications",
        "Write tests before or alongside code",
        "Submit to Tester for review",
    ],
    tier_2_rules=[
        "Follow code style conventions",
        "Document complex logic",
    ],
    domain_expertise=["Python", "TypeScript", "API design"],
    artifacts_produced=["Code", "Unit tests"],
    reviewer="tester"
)

TESTER_CONTRACT = RoleContract(
    role="tester",
    description="Quality assurance and test design",
    tier_0_rules=[
        "Never approve code that fails tests",
        "Never skip edge case testing",
        "Always validate against acceptance criteria",
    ],
    tier_1_rules=[
        "Design tests that encode business intent",
        "Verify coverage meets requirements",
        "Provide actionable feedback on rejections",
    ],
    tier_2_rules=[
        "Optimize test execution time",
        "Document test strategy",
    ],
    domain_expertise=["Testing", "QA", "Test automation"],
    artifacts_produced=["Test specifications", "Test reports"],
    reviewer="developer"
)

DOCUMENTER_CONTRACT = RoleContract(
    role="documenter",
    description="Technical and user documentation",
    tier_0_rules=[
        "Never document undocumented behavior",
        "Never skip accuracy verification",
        "Always keep docs in sync with code",
    ],
    tier_1_rules=[
        "Document APIs, configurations, and workflows",
        "Validate with Architect for technical accuracy",
        "Maintain version consistency",
    ],
    tier_2_rules=[
        "Follow documentation standards",
        "Include examples and diagrams",
    ],
    domain_expertise=["Technical writing", "API documentation"],
    artifacts_produced=["Documentation", "User guides", "API docs"],
    reviewer="architect"
)

DEPLOYMENT_SPECIALIST_CONTRACT = RoleContract(
    role="deployment_specialist",
    description="Infrastructure and deployment",
    tier_0_rules=[
        "Never deploy without change approval",
        "Never skip rollback planning",
        "Always document infrastructure changes",
    ],
    tier_1_rules=[
        "Follow ITIL change management",
        "Validate with ITIL Manager",
        "Maintain infrastructure as code",
    ],
    tier_2_rules=[
        "Optimize deployment pipelines",
        "Document operational runbooks",
    ],
    domain_expertise=["Kubernetes", "CI/CD", "Infrastructure as Code"],
    artifacts_produced=["Helm charts", "Deployment configs", "Runbooks"],
    reviewer="itil_manager"
)

UI_DESIGNER_CONTRACT = RoleContract(
    role="ui_designer",
    description="Dashboard and interface design",
    tier_0_rules=[
        "Never design without accessibility consideration",
        "Never skip usability validation",
        "Always follow design system",
    ],
    tier_1_rules=[
        "Design for target user personas",
        "Validate with Tester for accessibility",
        "Maintain consistent UX patterns",
    ],
    tier_2_rules=[
        "Optimize for performance",
        "Document design decisions",
    ],
    domain_expertise=["UI/UX design", "Accessibility", "Design systems"],
    artifacts_produced=["Dashboard designs", "UI specifications"],
    reviewer="tester"
)

ITIL_MANAGER_CONTRACT = RoleContract(
    role="itil_manager",
    description="IT service management",
    tier_0_rules=[
        "Never bypass change management",
        "Never skip impact assessment",
        "Always maintain service catalog",
    ],
    tier_1_rules=[
        "Apply ITIL framework",
        "Validate with Risk & Compliance Officer",
        "Track service level agreements",
    ],
    tier_2_rules=[
        "Optimize incident response",
        "Document service procedures",
    ],
    domain_expertise=["ITIL", "Service management", "Change management"],
    artifacts_produced=["Service configs", "Change records"],
    reviewer="risk_compliance_officer"
)

CONNECTION_SPECIALIST_CONTRACT = RoleContract(
    role="connection_specialist",
    description="System integration and connectors",
    tier_0_rules=[
        "Never connect without authentication validation",
        "Never skip error handling",
        "Always document connection parameters",
    ],
    tier_1_rules=[
        "Implement connectors with retry logic",
        "Validate with Tester for error handling",
        "Document API contracts",
    ],
    tier_2_rules=[
        "Optimize connection pooling",
        "Monitor connection health",
    ],
    domain_expertise=["API integration", "Authentication", "Error handling"],
    artifacts_produced=["Connectors", "Integration specs"],
    reviewer="tester"
)

# =============================================================================
# BUSINESS OPERATIONS LAYER
# =============================================================================

SALES_MANAGER_CONTRACT = RoleContract(
    role="sales_manager",
    description="Sales pipeline and forecasting",
    tier_0_rules=[
        "Never inflate pipeline projections",
        "Never skip financial validation",
        "Always document forecast assumptions",
    ],
    tier_1_rules=[
        "Track pipeline stages accurately",
        "Validate with Accountant for financial accuracy",
        "Maintain forecast models",
    ],
    tier_2_rules=[
        "Optimize lead scoring",
        "Document sales processes",
    ],
    domain_expertise=["Sales operations", "Forecasting", "CRM"],
    artifacts_produced=["Pipeline reports", "Forecasts"],
    reviewer="accountant"
)

MARKETING_MANAGER_CONTRACT = RoleContract(
    role="marketing_manager",
    description="Campaign metrics and marketing analytics",
    tier_0_rules=[
        "Never fabricate campaign results",
        "Never skip attribution validation",
        "Always document measurement methodology",
    ],
    tier_1_rules=[
        "Track campaign performance accurately",
        "Validate with Data Analyst for data validity",
        "Maintain attribution models",
    ],
    tier_2_rules=[
        "Optimize campaign targeting",
        "Document marketing processes",
    ],
    domain_expertise=["Marketing analytics", "Campaign management"],
    artifacts_produced=["Campaign reports", "Attribution analysis"],
    reviewer="data_analyst"
)

ACCOUNTANT_CONTRACT = RoleContract(
    role="accountant",
    description="Financial documentation and reporting",
    tier_0_rules=[
        "Never misstate financial figures",
        "Never skip reconciliation",
        "Always follow GAAP/IFRS standards",
    ],
    tier_1_rules=[
        "Maintain accurate financial records",
        "Validate with Sales Manager for business context",
        "Ensure audit readiness",
    ],
    tier_2_rules=[
        "Optimize financial processes",
        "Document accounting policies",
    ],
    domain_expertise=["Accounting", "Financial reporting", "Compliance"],
    artifacts_produced=["Financial reports", "Reconciliations"],
    reviewer="sales_manager"
)

CUSTOMER_SUCCESS_MANAGER_CONTRACT = RoleContract(
    role="customer_success_manager",
    description="Customer health and retention",
    tier_0_rules=[
        "Never ignore customer risk signals",
        "Never skip health score validation",
        "Always document customer interactions",
    ],
    tier_1_rules=[
        "Track customer health metrics",
        "Validate with Sales Manager for relationship context",
        "Maintain customer profiles",
    ],
    tier_2_rules=[
        "Optimize onboarding processes",
        "Document success playbooks",
    ],
    domain_expertise=["Customer success", "Retention", "Health scoring"],
    artifacts_produced=["Health assessments", "Success plans"],
    reviewer="sales_manager"
)

HR_TALENT_ANALYST_CONTRACT = RoleContract(
    role="hr_talent_analyst",
    description="People analytics and talent management",
    tier_0_rules=[
        "Never violate employee privacy",
        "Never skip bias checks in analysis",
        "Always follow data protection regulations",
    ],
    tier_1_rules=[
        "Analyze workforce data ethically",
        "Validate with Data Governance for privacy compliance",
        "Maintain anonymization standards",
    ],
    tier_2_rules=[
        "Optimize talent processes",
        "Document analysis methodology",
    ],
    domain_expertise=["People analytics", "HR metrics", "Privacy"],
    artifacts_produced=["Talent reports", "Workforce analytics"],
    reviewer="data_governance_specialist"
)

VALUE_CHAIN_ANALYST_CONTRACT = RoleContract(
    role="value_chain_analyst",
    description="Value chain optimization using client-defined industry frameworks",
    tier_0_rules=[
        "Never apply a framework without client configuration validation",
        "Never assume industry-specific metrics without client definition",
        "Always validate against client's configured value chain model",
    ],
    tier_1_rules=[
        "Apply client-configured value chain framework",
        "Map metrics to client-defined value chain modules",
        "Validate with Risk & Compliance Officer for compliance",
    ],
    tier_2_rules=[
        "Optimize metrics within client's framework context",
        "Document value chain processes per client ontology",
    ],
    domain_expertise=["Value chain analysis", "Industry frameworks", "Process optimization"],
    artifacts_produced=["Value chain metrics", "Framework-aligned optimization plans"],
    reviewer="risk_compliance_officer"
)

RISK_COMPLIANCE_OFFICER_CONTRACT = RoleContract(
    role="risk_compliance_officer",
    description="Risk assessment and compliance",
    tier_0_rules=[
        "Never downgrade risk without documented mitigation",
        "Never skip compliance deadlines",
        "Always escalate critical findings",
    ],
    tier_1_rules=[
        "Apply risk scoring frameworks",
        "Validate with ITIL Manager for process adherence",
        "Maintain audit documentation",
    ],
    tier_2_rules=[
        "Optimize risk processes",
        "Document compliance procedures",
    ],
    domain_expertise=["Risk management", "Compliance", "Audit"],
    artifacts_produced=["Risk assessments", "Compliance reports"],
    reviewer="itil_manager"
)

PROJECT_MANAGER_CONTRACT = RoleContract(
    role="project_manager",
    description="Agile planning and project coordination",
    tier_0_rules=[
        "Never commit scope without capacity check",
        "Never skip retrospective actions",
        "Always maintain risk register",
    ],
    tier_1_rules=[
        "Apply Scrum/Kanban methodologies",
        "Validate with Operations Manager for feasibility",
        "Track velocity and burndown",
    ],
    tier_2_rules=[
        "Optimize sprint planning",
        "Document project processes",
    ],
    domain_expertise=["Agile", "Scrum", "Project management"],
    artifacts_produced=["Sprint plans", "Project reports"],
    reviewer="operations_manager"
)

# =============================================================================
# GOVERNANCE LAYER
# =============================================================================

DATA_GOVERNANCE_SPECIALIST_CONTRACT = RoleContract(
    role="data_governance_specialist",
    description="DAMA DMBOK governance and data quality",
    tier_0_rules=[
        "Never approve data designs without governance review",
        "Never skip data quality assessment",
        "Always document data lineage",
    ],
    tier_1_rules=[
        "Apply DAMA DMBOK framework",
        "Validate with Architect for technical feasibility",
        "Maintain data catalog",
    ],
    tier_2_rules=[
        "Optimize governance processes",
        "Document data policies",
    ],
    domain_expertise=["Data governance", "DAMA DMBOK", "Data quality"],
    artifacts_produced=["Governance policies", "Data quality reports"],
    reviewer="architect"
)

PROCESS_SCENARIO_MODELER_CONTRACT = RoleContract(
    role="process_scenario_modeler",
    description="Process simulation and what-if analysis",
    tier_0_rules=[
        "Never present simulation as prediction without confidence intervals",
        "Never skip parameter validation",
        "Always validate with Operations Manager",
    ],
    tier_1_rules=[
        "Use discrete event simulation",
        "Run multiple replications for validity",
        "Document simulation assumptions",
    ],
    tier_2_rules=[
        "Optimize simulation performance",
        "Maintain scenario library",
    ],
    domain_expertise=["Process simulation", "Discrete event modeling"],
    artifacts_produced=["Simulation results", "Scenario analyses"],
    reviewer="operations_manager"
)

LIBRARIAN_CURATOR_CONTRACT = RoleContract(
    role="librarian_curator",
    description="KPI library and knowledge management",
    tier_0_rules=[
        "Never add KPIs without proper metadata",
        "Never skip duplicate detection",
        "Always maintain categorization",
    ],
    tier_1_rules=[
        "Curate KPI definitions",
        "Validate with Data Governance for compliance",
        "Maintain search and discovery",
    ],
    tier_2_rules=[
        "Optimize library organization",
        "Document curation standards",
    ],
    domain_expertise=["Knowledge management", "Taxonomy", "Metadata"],
    artifacts_produced=["KPI library entries", "Category taxonomies"],
    reviewer="data_governance_specialist"
)


# =============================================================================
# CONTRACT REGISTRY
# =============================================================================

ALL_CONTRACTS: Dict[str, RoleContract] = {
    # Strategy & Analysis Layer
    "coordinator": COORDINATOR_CONTRACT,
    "business_strategist": BUSINESS_STRATEGIST_CONTRACT,
    "business_analyst": BUSINESS_ANALYST_CONTRACT,
    "data_analyst": DATA_ANALYST_CONTRACT,
    "data_scientist": DATA_SCIENTIST_CONTRACT,
    "operations_manager": OPERATIONS_MANAGER_CONTRACT,
    "mapping_specialist": MAPPING_SPECIALIST_CONTRACT,
    "document_analyzer": DOCUMENT_ANALYZER_CONTRACT,
    "competitive_analyst": COMPETITIVE_ANALYST_CONTRACT,
    
    # Technical Design Layer
    "architect": ARCHITECT_CONTRACT,
    "developer": DEVELOPER_CONTRACT,
    "tester": TESTER_CONTRACT,
    "documenter": DOCUMENTER_CONTRACT,
    "deployment_specialist": DEPLOYMENT_SPECIALIST_CONTRACT,
    "ui_designer": UI_DESIGNER_CONTRACT,
    "itil_manager": ITIL_MANAGER_CONTRACT,
    "connection_specialist": CONNECTION_SPECIALIST_CONTRACT,
    
    # Business Operations Layer
    "sales_manager": SALES_MANAGER_CONTRACT,
    "marketing_manager": MARKETING_MANAGER_CONTRACT,
    "accountant": ACCOUNTANT_CONTRACT,
    "customer_success_manager": CUSTOMER_SUCCESS_MANAGER_CONTRACT,
    "hr_talent_analyst": HR_TALENT_ANALYST_CONTRACT,
    "value_chain_analyst": VALUE_CHAIN_ANALYST_CONTRACT,
    "risk_compliance_officer": RISK_COMPLIANCE_OFFICER_CONTRACT,
    "project_manager": PROJECT_MANAGER_CONTRACT,
    
    # Governance Layer
    "data_governance_specialist": DATA_GOVERNANCE_SPECIALIST_CONTRACT,
    "process_scenario_modeler": PROCESS_SCENARIO_MODELER_CONTRACT,
    "librarian_curator": LIBRARIAN_CURATOR_CONTRACT,
}


def get_contract(role: str) -> RoleContract:
    """Get the contract for a specific role."""
    return ALL_CONTRACTS.get(role, COORDINATOR_CONTRACT)


def get_all_roles() -> List[str]:
    """Get all available roles."""
    return list(ALL_CONTRACTS.keys())
