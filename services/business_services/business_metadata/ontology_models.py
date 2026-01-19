"""Ontology and meta-definition models for the Analytics Metadata Service.

These Pydantic v2 models represent the knowledge-graph-oriented foundation
for entities, events, metrics, modules, value chains, and governance objects.

They are designed to:
- Mirror the conceptual ontology documented in SERVICE_INTERPLAY_ARCHITECTURE.md
- Serve as the *new* source of truth for metadata (legacy dicts will be
  migrated into these models rather than coexisting long-term)
- Drive generation of execution artifacts (Pydantic models, TimescaleDB
  schemas, APIs, etc.)
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict


# ---------------------------------------------------------------------------
# Core building blocks
# ---------------------------------------------------------------------------


class NodeDefinition(BaseModel):
    """Base ontology class for all node definitions in the knowledge graph.
    
    Note: edges (relationships) are NOT embedded here to avoid circular references.
    They are stored separately in the relationships table and fetched via
    the relationships API endpoints.
    """

    model_config = ConfigDict(extra="allow")

    id: Optional[str] = None
    kind: str
    name: str
    description: Optional[str] = None
    metadata_: Dict[str, Any] = {}


# Backward compatibility alias
ThingDefinition = NodeDefinition


class ColumnDefinition(BaseModel):
    """Column definition for relational/TimescaleDB schemas."""

    name: str
    type: str
    description: Optional[str] = None
    primary_key: bool = False
    autoincrement: bool = False
    nullable: bool = True
    unique: bool = False
    index: bool = False
    length: Optional[int] = None
    foreign_key: Optional[str] = None


class TableSchemaDefinition(BaseModel):
    table_name: str
    class_name: Optional[str] = None
    columns: List[ColumnDefinition]


# ---------------------------------------------------------------------------
# Entity / Relationship layer
# ---------------------------------------------------------------------------


class EntityDefinition(NodeDefinition):
    """Ontology representation of a business entity/object model (data/noun).
    
    Represents static data structures like Customer, Order, Product.
    """

    kind: str = "entity_definition"
    code: str
    table_schema: Optional[TableSchemaDefinition] = None
    schema_definition: Optional[str] = None  # UML / graph snippet


# ---------------------------------------------------------------------------
# Process layer
# ---------------------------------------------------------------------------


class ProcessDefinition(NodeDefinition):
    """Base ontology class for all process/workflow definitions (action/verb).
    
    Represents dynamic processes, workflows, and value flows.
    Child classes include ValueChainPatternDefinition and BusinessProcessDefinition.
    """

    kind: str = "process_definition"
    code: str
    process_type: Optional[str] = None  # "value_chain", "business_process", "workflow"
    
    # Graph pattern for process flow
    graph_pattern: Optional["GraphPatternDefinition"] = None
    
    # Associated metrics for this process
    associated_metrics: List[str] = []
    
    # Business ontology fields
    business_purpose: Optional[str] = None  # Purpose statement
    intended_value: Optional[str] = None  # Value to be produced


class EdgeDefinition(BaseModel):
    """Ontology representation of an edge (relationship) between nodes in the knowledge graph.
    
    Note: Inherits from BaseModel (not NodeDefinition) to avoid circular reference
    since NodeDefinition could have edges: List[EdgeDefinition].
    """
    model_config = ConfigDict(extra="allow")

    id: Optional[str] = None
    kind: str = "edge_definition"
    name: str = ""
    description: Optional[str] = None
    from_entity: str
    to_entity: str
    relationship_type: str
    from_cardinality: Optional[str] = None
    to_cardinality: Optional[str] = None
    metadata_: Dict[str, Any] = {}


# Backward compatibility alias
RelationshipDefinition = EdgeDefinition


# ---------------------------------------------------------------------------
# Terminology layer
# ---------------------------------------------------------------------------


class ValueSetDefinition(NodeDefinition):
    kind: str = "value_set_definition"

    codes: List[str]


class CodeSystemDefinition(NodeDefinition):
    kind: str = "code_system_definition"

    # map code -> human-readable label/description
    codes: Dict[str, str] = {}


# ---------------------------------------------------------------------------
# Metric / KPI layer
# ---------------------------------------------------------------------------


class MetricDefinition(NodeDefinition):
    """Metric/KPI definition without time or arithmetic modifiers in name.
    
    Time and arithmetic modifiers are applied at QUERY TIME via:
    - time_periods: Available time granularities
    - aggregation_methods: Available aggregation functions
    - dimensions: Available dimension filters
    
    Example: "Recurring Revenue" (NOT "Monthly Recurring Revenue")
    
    Benchmarks are stored as separate BenchmarkDefinition entities linked via relationships.
    
    Calculation Types:
    - "simple": Direct formula calculation (math_expression)
    - "set_based": Multi-step set operations (set_based_definition)
    """
    kind: str = "metric_definition"

    code: str
    category: Optional[str] = None
    modules: List[str] = []
    required_objects: List[str] = []
    formula: Optional[str] = None  # Natural language formula description
    math_expression: Optional[str] = None  # Parsed mathematical expression for calculation engine
    unit: Optional[str] = None
    data_type: str = "decimal"
    
    # Calculation type - determines which engine processes this metric
    calculation_type: str = "simple"  # "simple", "set_based"
    
    # Set-based calculation definition (for calculation_type="set_based")
    # Stores the complete SetBasedKPIDefinition as JSON
    # Structure: {
    #   "base_entity": "customers",
    #   "key_column": "customer_id",
    #   "period_parameters": ["PeriodStart", "PeriodEnd"],
    #   "steps": [...],  # List of CalculationStep definitions
    #   "final_formula": "CASE WHEN X > 0 THEN (Y/X)*100 ELSE 0 END"
    # }
    set_based_definition: Optional[Dict[str, Any]] = None
    
    # Time modifiers - applied at query time
    aggregation_methods: List[str] = []  # ["sum", "avg", "min", "max", "count", "median"]
    default_aggregation: str = "sum"
    
    # Calculation Method
    calculation_method: str = "exact"  # "exact", "approximate"
    
    # Arithmetic modifiers - applied at query time
    time_periods: List[str] = []  # ["daily", "weekly", "monthly", "quarterly", "yearly"]
    default_time_period: str = "monthly"
    
    # Dimension modifiers - applied at query time
    dimensions: List[str] = []  # dimension codes (e.g., product, customer)
    
    # Analytics classification
    metric_classification: str = "operational"  # "operational", "result", "business_value"
    analytics_type: str = "operational"  # "operational", "correlative", "predictive"
    
    # For correlative metrics
    correlated_with: List[str] = []  # Other metric codes
    correlation_strength: Optional[float] = None
    
    # For predictive metrics
    prediction_model: Optional[str] = None
    prediction_confidence: Optional[float] = None
    scenario_parameters: Dict[str, Any] = {}
    
    # Analytics strategy linkage
    metric_category: Optional[str] = None  # Links to MetricCategoryDefinition
    data_sources: List[str] = []  # Links to DataSourceDefinition
    quality_rules: List[str] = []  # Links to DataQualityRuleDefinition


# ---------------------------------------------------------------------------
# Value chain layer
# ---------------------------------------------------------------------------


class GraphNodePattern(BaseModel):
    id: str
    class_: str
    role: Optional[str] = None
    metadata_: Dict[str, Any] = {}


class GraphEdgePattern(BaseModel):
    from_: str
    to: str
    relationship_type: str
    metadata_: Dict[str, Any] = {}


class GraphPatternDefinition(BaseModel):
    nodes: List[GraphNodePattern] = []
    edges: List[GraphEdgePattern] = []


class DimensionBinding(BaseModel):
    metric: str
    dimension_name: str
    node: str


class ValueChainPatternDefinition(ProcessDefinition):
    """Value chain pattern at any granularity level.
    
    Inherits from ProcessDefinition.
    
    The 'domain' field indicates granularity:
    - "company": Top-level (entire company as a value chain)
    - "industry" or "cross_industry": High-level value chains (e.g., SUPPLY_CHAIN, SALES_MGMT)
    - "module": Mid-level patterns (e.g., CHANNEL_SALES, CUSTOMER_SUCCESS, ASCM_SCOR)
    - "process": Low-level operational patterns
    
    All are value chain patterns, just at different scales.
    """
    kind: str = "value_chain_pattern_definition"
    process_type: str = "value_chain"  # Override from ProcessDefinition

    domain: Optional[str] = None  # Granularity: "company", "industry", "module", "process"
    applicability: Dict[str, Any] = {}
    graph_pattern: GraphPatternDefinition = GraphPatternDefinition()  # Override with concrete type
    dimension_bindings: List[DimensionBinding] = []


class CompanyValueChainModelDefinition(NodeDefinition):
    """Company-specific value chain instance (derived from patterns)."""
    kind: str = "company_value_chain_model_definition"

    company_id: str
    session_id: Optional[str] = None
    derived_from: Optional[str] = None
    included_nodes: List[str] = []
    included_edges: List[str] = []
    applied_patterns: List[str] = []


# ---------------------------------------------------------------------------
# Actor layer
# ---------------------------------------------------------------------------


class ActorDefinition(NodeDefinition):
    """Actors that perform actions and participate in processes.
    
    Actors can be people, roles, organizations, or systems.
    """
    kind: str = "actor_definition"
    
    code: str
    actor_type: str  # "person", "role", "organization", "system"
    capabilities: List[str] = []  # What they can do
    responsibilities: List[str] = []  # What they're responsible for


class BeneficiaryDefinition(ActorDefinition):
    """Actors that receive value from value chains.
    
    Inherits all actor characteristics and adds beneficiary-specific fields.
    """
    kind: str = "beneficiary_definition"
    
    # Inherited from ActorDefinition:
    # - code, actor_type, capabilities, responsibilities
    
    # Beneficiary-specific fields:
    value_received: Optional[str] = None  # Type of value received
    value_measurement: Optional[str] = None  # Metric code measuring value


# ---------------------------------------------------------------------------
# Authorization / Access Control layer
# ---------------------------------------------------------------------------


class ClientDefinition(NodeDefinition):
    """Multi-tenant client/organization with access control.
    
    Represents a tenant organization with access to specific modules
    and role-based permissions. Separate from CompanyDefinition which
    represents a business entity in the knowledge graph.
    """
    kind: str = "client_definition"
    
    code: str
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    config: Dict[str, Any] = {}  # Client-specific configuration
    is_active: bool = True
    
    # Geographic classification
    country_code: Optional[str] = None  # Links to CountryDefinition
    region_code: Optional[str] = None  # Links to RegionDefinition
    metropolitan_area_code: Optional[str] = None  # Links to MetropolitanAreaDefinition
    
    # Industry classification
    naics_code: Optional[str] = None  # Links to NAICSIndustryDefinition
    naics_title: Optional[str] = None
    naics_sector: Optional[str] = None
    naics_subsector: Optional[str] = None


class RoleDefinition(ActorDefinition):
    """Role within a client organization with specific permissions.
    
    Inherits from ActorDefinition and adds RBAC-specific fields.
    Roles define what actions users can perform within a client's context.
    """
    kind: str = "role_definition"
    
    # Inherited from ActorDefinition:
    # - code, actor_type, capabilities, responsibilities
    
    # Role-specific fields:
    client_code: str  # Links to ClientDefinition
    permissions: Dict[str, Any] = {}  # Role-specific permissions
    is_admin: bool = False


class PermissionDefinition(NodeDefinition):
    """Base class for all permission types.
    
    Defines access control rules for various resource types.
    Uses relationships to link subjects (clients, roles) to resources.
    """
    kind: str = "permission_definition"
    
    code: str
    subject_code: str  # Who (client, role, user)
    subject_type: str  # "client", "role", "user"
    resource_code: str  # What (module, entity, metric, attribute)
    resource_type: str  # "module", "entity", "metric", "attribute"
    
    # CRUD permissions
    can_view: bool = False
    can_create: bool = False
    can_update: bool = False
    can_delete: bool = False
    
    # Additional config
    config: Dict[str, Any] = {}


class ModulePermissionDefinition(PermissionDefinition):
    """Module-level access control (client whitelist).
    
    Whitelist approach: only explicitly listed modules are accessible.
    """
    kind: str = "module_permission_definition"
    resource_type: str = "module"


class EntityPermissionDefinition(PermissionDefinition):
    """Entity/ObjectModel-level access control.
    
    Controls which entities a role can access and what operations
    they can perform.
    """
    kind: str = "entity_permission_definition"
    resource_type: str = "entity"


class MetricPermissionDefinition(PermissionDefinition):
    """Metric/KPI-level access control.
    
    Controls which metrics a role can view and update.
    """
    kind: str = "metric_permission_definition"
    resource_type: str = "metric"


class AttributePermissionDefinition(PermissionDefinition):
    """Attribute-level access control with data masking.
    
    Controls field-level access and supports data masking for
    sensitive attributes.
    """
    kind: str = "attribute_permission_definition"
    resource_type: str = "attribute"
    
    # Data masking fields
    is_masked: bool = False
    mask_type: Optional[str] = None  # "partial", "full", "hash", "encrypt"
    mask_pattern: Optional[str] = None  # Custom mask pattern


class RowLevelSecurityDefinition(NodeDefinition):
    """Row-level security filter for data access control.
    
    Defines attribute-based filters that restrict which rows
    a role can access within an entity.
    """
    kind: str = "row_level_security_definition"
    
    code: str
    role_code: str  # Links to RoleDefinition
    entity_code: str  # Links to EntityDefinition
    
    # Filter definition
    attribute_filters: Dict[str, Any] = {}  # {"REGION": {"eq": "US-WEST"}}
    filter_logic: str = "AND"  # "AND" or "OR"
    
    # Supported operators: eq, ne, in, not_in, gt, gte, lt, lte, contains, startswith, between


# ---------------------------------------------------------------------------
# Geographic & Industry Classification layer
# ---------------------------------------------------------------------------


class CountryDefinition(NodeDefinition):
    """Country with ISO codes and basic information.
    
    Represents a country for geographic classification and client segmentation.
    Uses official ISO 3166-1 codes for standardization.
    """
    kind: str = "country_definition"
    
    code: str  # Country code (e.g., "US")
    iso_alpha2: str  # ISO 3166-1 alpha-2 (e.g., "US")
    iso_alpha3: str  # ISO 3166-1 alpha-3 (e.g., "USA")
    iso_numeric: str  # ISO 3166-1 numeric (e.g., "840")
    capital: Optional[str] = None
    currency_code: Optional[str] = None  # ISO 4217 (e.g., "USD")
    currency_name: Optional[str] = None
    phone_code: Optional[str] = None  # e.g., "+1"


class RegionDefinition(NodeDefinition):
    """State, province, or administrative region within a country.
    
    Represents sub-national geographic divisions (states, provinces, territories).
    """
    kind: str = "region_definition"
    
    code: str  # Region code (e.g., "CA", "ON")
    country_code: str  # Links to CountryDefinition
    region_type: str  # "state", "province", "territory", "county"
    capital: Optional[str] = None
    abbreviation: Optional[str] = None


class MetropolitanAreaDefinition(NodeDefinition):
    """Metropolitan Statistical Area (MSA) or equivalent.
    
    Represents metropolitan areas as defined by census/statistical agencies.
    Includes US MSAs, Canadian CMAs, and international equivalents.
    """
    kind: str = "metropolitan_area_definition"
    
    code: str  # MSA/CBSA code
    region_code: str  # Links to RegionDefinition
    cbsa_code: Optional[str] = None  # Core Based Statistical Area code
    msa_type: str = "metropolitan"  # "metropolitan", "micropolitan"
    population: Optional[int] = None
    population_year: Optional[int] = None
    central_city: Optional[str] = None
    counties: List[str] = []  # List of counties in the MSA


class NAICSIndustryDefinition(NodeDefinition):
    """NAICS (North American Industry Classification System) industry code.
    
    Represents standardized industry classifications for business establishments.
    Supports 2-6 digit NAICS codes with hierarchical structure.
    """
    kind: str = "naics_industry_definition"
    
    code: str  # NAICS code (2-6 digits)
    title: str  # Industry title/description
    sector: str  # 2-digit sector name
    subsector: Optional[str] = None  # 3-digit subsector name
    industry_group: Optional[str] = None  # 4-digit industry group
    naics_level: int  # 2, 3, 4, 5, or 6 digit level


# ---------------------------------------------------------------------------
# Business ontology layer
# ---------------------------------------------------------------------------


class CompanyDefinition(ValueChainPatternDefinition):
    """A company is the top-level value chain.
    
    Inherits all value chain characteristics:
    - domain (set to "company")
    - applicability
    - graph_pattern (company's value chain graph)
    - associated_metrics (company-level KPIs)
    - business_purpose
    - intended_value
    """
    kind: str = "company_definition"
    
    # Company-specific fields:
    code: str  # Company identifier
    naics_code: str  # Links to NAICSIndustryDefinition
    industry_codes: List[str] = []  # Additional industry codes
    legal_structure: Optional[str] = None  # "public", "private", "nonprofit"
    
    # Geographic classification
    country_code: Optional[str] = None  # Links to CountryDefinition
    region_code: Optional[str] = None  # Links to RegionDefinition
    metropolitan_area_code: Optional[str] = None  # Links to MetropolitanAreaDefinition
    
    # Override domain to be "company"
    domain: str = "company"  # Top-level granularity


class BusinessProcessDefinition(ValueChainPatternDefinition):
    """A business process is a low-level value chain pattern.
    
    Inherits from ValueChainPatternDefinition (which inherits from ProcessDefinition).
    Adds process-specific execution details.
    """
    kind: str = "business_process_definition"
    process_type: str = "business_process"  # Override from ProcessDefinition
    
    # Process-specific execution fields:
    performed_by_actors: List[str] = []  # ActorDefinition codes
    uses_entities: List[str] = []  # EntityDefinition codes
    produces_event_types: List[str] = []  # Event entity codes
    
    # Override domain to be "process"
    domain: str = "process"  # Low-level granularity


class StrategicObjectiveDefinition(NodeDefinition):
    """Strategic objectives that achieve business purpose and produce value."""
    kind: str = "strategic_objective_definition"
    
    code: str
    objective_type: str  # "growth", "efficiency", "quality", "innovation"
    target_value: Optional[str] = None  # Target metric value
    timeframe: Optional[str] = None  # "Q1 2025", "FY2025"
    
    # Analytics strategy alignment
    aligned_use_cases: List[str] = []  # Links to AnalyticsUseCaseDefinition
    supporting_metrics: List[str] = []  # Links to MetricDefinition (KPIs)
    responsible_actors: List[str] = []  # Links to ActorDefinition


class BenchmarkDefinition(NodeDefinition):
    """Industry benchmark data point for metrics with full citation and context.
    
    Each benchmark represents a specific data point from research studies, industry
    reports, or authoritative sources that provide context for KPI performance evaluation.
    
    Linked to metrics via relationships, not embedded in metric definitions.
    """
    kind: str = "benchmark_definition"
    
    code: str
    metric_code: str  # Links to MetricDefinition via relationship
    
    # Exact Metric Information
    metric_value: Optional[float] = None
    metric_value_text: Optional[str] = None  # For ranges or non-numeric
    metric_unit: Optional[str] = None  # %, $, seconds, count
    statistic_type: str = "mean"  # mean, median, mode, percentile, range
    percentile: Optional[int] = None  # 0-100 if applicable
    value_min: Optional[float] = None
    value_max: Optional[float] = None
    
    # Metric Definition & Attributes
    metric_definition: Optional[str] = None  # How metric is defined
    metric_normalization: Optional[str] = None  # How normalized
    metric_filters: Dict[str, Any] = {}
    cohort_rules: Dict[str, Any] = {}
    
    # Context & Segmentation - Company Size
    company_size: Optional[str] = None  # SMB, Mid-Market, Enterprise
    company_size_min: Optional[int] = None
    company_size_max: Optional[int] = None
    company_size_metric: Optional[str] = None  # employees, revenue, customers
    
    # Context & Segmentation - Time Period
    time_period: Optional[str] = None  # Q1 2024, 2023 Annual
    time_period_start: Optional[str] = None  # ISO date
    time_period_end: Optional[str] = None  # ISO date
    
    # Context & Segmentation - Population
    population: Optional[str] = None  # What was measured
    population_size: Optional[int] = None
    
    # Context & Segmentation - Industry
    industry: Optional[str] = None
    industry_tags: List[str] = []
    
    # Context & Segmentation - Geography
    geography: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    
    # Context & Segmentation - Sample
    sample_size: Optional[int] = None
    sample_description: Optional[str] = None
    
    # Source Details & Citation
    source_publisher: Optional[str] = None
    source_author: Optional[str] = None
    source_title: Optional[str] = None
    source_year: Optional[int] = None
    source_date: Optional[str] = None  # ISO date
    source_excerpt: Optional[str] = None
    source_url: Optional[str] = None
    source_download_url: Optional[str] = None
    source_doi: Optional[str] = None
    source_type: Optional[str] = None  # research_report, whitepaper, academic_study, etc.
    source_credibility: str = "medium"  # high, medium, low
    
    # Methodology & Comments
    methodology_notes: Optional[str] = None
    caveats: Optional[str] = None
    special_coverage: Optional[str] = None
    comments: Optional[str] = None
    
    # Quality & Validation
    confidence_level: str = "medium"  # high, medium, low
    data_quality_score: Optional[int] = None  # 0-100
    last_verified_at: Optional[str] = None  # ISO date
    verified_by: Optional[str] = None
    
    # Categorization & Display
    benchmark_category: str = "industry_standard"  # industry_standard, best_in_class, average, poor_performance
    display_order: int = 0
    is_featured: bool = False
    tags: List[str] = []


class ExternalEventDefinition(NodeDefinition):
    """External event or news that may impact business metrics.
    
    Captures external context like news, economic events, regulatory changes,
    competitor actions, and market conditions that influence business performance.
    """
    kind: str = "external_event_definition"
    
    code: str
    event_type: str  # "news", "economic", "regulatory", "competitor", "market", "technology", "social"
    event_category: str  # "company", "industry", "economy", "government", "global"
    
    # Event details
    event_date: str  # ISO date
    headline: str
    summary: Optional[str] = None
    source: Optional[str] = None  # News outlet, agency, etc.
    source_url: Optional[str] = None
    
    # Impact assessment
    sentiment: Optional[str] = None  # "positive", "negative", "neutral"
    impact_level: Optional[str] = None  # "critical", "high", "medium", "low"
    affected_metrics: List[str] = []  # Links to MetricDefinition
    affected_entities: List[str] = []  # Links to EntityDefinition (companies, products, etc.)
    
    # Context
    related_companies: List[str] = []  # Links to CompanyDefinition
    related_industries: List[str] = []  # Links to NAICSIndustryDefinition
    related_geographies: List[str] = []  # Links to CountryDefinition or RegionDefinition
    
    # Analysis
    predicted_impact: Optional[str] = None  # Qualitative or quantitative prediction
    actual_impact: Optional[str] = None  # Measured after the fact
    tags: List[str] = []


# ---------------------------------------------------------------------------
# Analytics Strategy & Data Management layer
# ---------------------------------------------------------------------------


class AnalyticsStrategyDefinition(NodeDefinition):
    """Company's overall analytics strategy and maturity.
    
    Defines the strategic approach to analytics, maturity level,
    and alignment with business objectives.
    """
    kind: str = "analytics_strategy_definition"
    
    code: str
    company_code: str  # Links to CompanyDefinition
    
    # Strategy attributes
    analytics_maturity_level: str  # "descriptive", "diagnostic", "predictive", "prescriptive", "cognitive"
    data_culture_score: Optional[float] = None  # 0-100
    investment_level: Optional[str] = None  # "minimal", "moderate", "significant", "transformative"
    
    # Focus areas
    primary_use_cases: List[str] = []  # ["customer_analytics", "operational_efficiency", "risk_management"]
    strategic_priorities: List[str] = []  # Links to StrategicObjectiveDefinition codes
    
    # Capabilities
    current_capabilities: List[str] = []
    target_capabilities: List[str] = []
    capability_gaps: List[str] = []
    
    # Governance
    governance_model: Optional[str] = None  # "centralized", "federated", "decentralized"
    data_governance_maturity: Optional[str] = None


class DataSourceDefinition(NodeDefinition):
    """External or internal data source for analytics.
    
    Represents data sources that feed the analytics platform.
    """
    kind: str = "data_source_definition"
    
    code: str
    source_type: str  # "transactional", "operational", "external", "streaming", "batch"
    source_system: str  # "salesforce", "erp", "crm", "iot_sensors"
    
    # Technical details
    connection_type: str  # "api", "database", "file", "stream"
    refresh_frequency: Optional[str] = None  # "real-time", "hourly", "daily", "weekly"
    data_volume: Optional[str] = None  # "small", "medium", "large", "massive"
    
    # Quality
    data_quality_score: Optional[float] = None
    completeness_score: Optional[float] = None
    timeliness_score: Optional[float] = None
    
    # Governance
    data_owner: Optional[str] = None  # Links to ActorDefinition
    data_steward: Optional[str] = None  # Links to ActorDefinition
    sensitivity_level: Optional[str] = None  # "public", "internal", "confidential", "restricted"


class DataProductDefinition(NodeDefinition):
    """Packaged data asset with defined consumers and SLAs.
    
    Represents curated data products for specific use cases.
    """
    kind: str = "data_product_definition"
    
    code: str
    product_type: str  # "dataset", "dashboard", "report", "api", "model"
    
    # Ownership
    product_owner: str  # Links to ActorDefinition
    consumers: List[str] = []  # Links to ActorDefinition or RoleDefinition
    
    # Content
    source_entities: List[str] = []  # Links to EntityDefinition
    included_metrics: List[str] = []  # Links to MetricDefinition
    
    # SLA
    refresh_sla: Optional[str] = None
    availability_sla: Optional[float] = None  # 99.9%
    latency_sla: Optional[str] = None


class AnalyticsUseCaseDefinition(NodeDefinition):
    """Specific analytics use case or application.
    
    Represents a business problem being solved with analytics.
    """
    kind: str = "analytics_use_case_definition"
    
    code: str
    use_case_type: str  # "reporting", "monitoring", "prediction", "optimization", "automation"
    
    # Business context
    business_problem: str
    expected_value: Optional[str] = None
    success_metrics: List[str] = []  # Links to MetricDefinition
    
    # Implementation
    required_data_sources: List[str] = []  # Links to DataSourceDefinition
    required_entities: List[str] = []  # Links to EntityDefinition
    required_metrics: List[str] = []  # Links to MetricDefinition
    
    # Stakeholders
    business_owner: str  # Links to ActorDefinition
    technical_owner: str  # Links to ActorDefinition
    end_users: List[str] = []  # Links to RoleDefinition
    
    # Status
    maturity_stage: str  # "concept", "pilot", "production", "optimized", "retired"
    implementation_priority: Optional[str] = None  # "critical", "high", "medium", "low"


class DimensionDefinition(NodeDefinition):
    """Analytical dimension for slicing and dicing metrics.
    
    Represents dimensions like time, geography, product, customer segment.
    Already referenced in MetricDefinition.dimensions but now formalized.
    """
    kind: str = "dimension_definition"
    
    code: str
    dimension_type: str  # "time", "geography", "product", "customer", "organizational"
    
    # Hierarchy
    hierarchy_levels: List[str] = []  # ["year", "quarter", "month", "day"]
    parent_dimension: Optional[str] = None
    
    # Source
    source_entity: Optional[str] = None  # Links to EntityDefinition
    source_attribute: Optional[str] = None
    
    # Cardinality
    estimated_cardinality: Optional[int] = None  # Number of distinct values


class MetricCategoryDefinition(NodeDefinition):
    """Hierarchical categorization of metrics.
    
    Organizes metrics into logical categories for navigation and discovery.
    """
    kind: str = "metric_category_definition"
    
    code: str
    category_type: str  # "financial", "operational", "customer", "employee", "risk"
    parent_category: Optional[str] = None  # For hierarchical categories
    
    # Organization
    display_order: int = 0
    icon: Optional[str] = None
    color: Optional[str] = None


class DataQualityRuleDefinition(NodeDefinition):
    """Data quality rule for validation and monitoring.
    
    Defines rules to ensure data quality across entities and attributes.
    """
    kind: str = "data_quality_rule_definition"
    
    code: str
    rule_type: str  # "completeness", "accuracy", "consistency", "timeliness", "validity"
    
    # Scope
    target_entity: str  # Links to EntityDefinition
    target_attributes: List[str] = []
    
    # Rule logic
    rule_expression: str  # SQL or formula
    threshold: Optional[float] = None
    severity: str  # "critical", "high", "medium", "low"
    
    # Monitoring
    check_frequency: str  # "real-time", "hourly", "daily"
    alert_recipients: List[str] = []  # Links to ActorDefinition


# ---------------------------------------------------------------------------
# Governance / policy layer
# ---------------------------------------------------------------------------


class ConstraintDefinition(NodeDefinition):
    kind: str = "constraint_definition"

    target_kind: str  # e.g., entity_definition, value_chain_pattern_definition
    expression: Dict[str, Any]  # shape/validation expression


class DesignPolicyRuleDefinition(BaseModel):
    id: str
    when: Dict[str, Any]
    then: Dict[str, Any]
    and_: Optional[Dict[str, Any]] = None


class DesignPolicyDefinition(NodeDefinition):
    kind: str = "design_policy_definition"

    scope: str = "global"
    version: Optional[str] = None
    rules: List[DesignPolicyRuleDefinition] = []


# ---------------------------------------------------------------------------
# Conversation / intent layer
# ---------------------------------------------------------------------------


class InterviewSessionDefinition(NodeDefinition):
    kind: str = "interview_session_definition"

    company_id: Optional[str] = None
    industry_codes: List[str] = []
    participants: List[str] = []
    started_at: Optional[str] = None
    ended_at: Optional[str] = None


class UtteranceDefinition(NodeDefinition):
    kind: str = "utterance_definition"

    session_id: str
    speaker: str
    timestamp: Optional[str] = None
    raw_text: str
    nlp_annotations: Dict[str, Any] = {}


class BusinessIntentDefinition(NodeDefinition):
    kind: str = "business_intent_definition"

    session_id: str
    intent_type: str
    target_concepts: List[str] = []
    priority: Optional[str] = None
    confidence_score: Optional[float] = None
    source_utterances: List[str] = []


class PatternMatchDefinition(NodeDefinition):
    kind: str = "pattern_match_definition"

    session_id: str
    pattern_id: str
    matched_entities: Dict[str, str] = {}
    confidence_score: Optional[float] = None
    supporting_intents: List[str] = []


class DesignSuggestionDefinition(NodeDefinition):
    kind: str = "design_suggestion_definition"

    session_id: str
    suggested_changes: Dict[str, Any]
    status: str = "proposed"  # proposed | accepted | rejected
    rationale: Optional[str] = None


# ---------------------------------------------------------------------------
# CRM / Sales Pipeline layer (Sales Manager Agent)
# ---------------------------------------------------------------------------


class ProspectDefinition(NodeDefinition):
    """Prospect in the early sales pipeline.
    
    Represents a potential customer before qualification.
    Used by Sales Manager Agent for prospect tracking.
    """
    kind: str = "prospect_definition"
    
    code: str
    company_name: str
    contact_name: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    
    # Classification
    industry: Optional[str] = None  # Links to NAICSIndustryDefinition
    company_size: Optional[str] = None  # "startup", "smb", "mid_market", "enterprise"
    source: Optional[str] = None  # "referral", "website", "event", "cold_outreach"
    
    # Engagement
    initial_interest: Optional[str] = None
    engagement_score: int = 0  # 0-100
    last_contact_date: Optional[str] = None
    
    # Status
    status: str = "new"  # "new", "contacted", "engaged", "qualified", "disqualified"
    assigned_to: Optional[str] = None  # Links to ActorDefinition


class LeadDefinition(NodeDefinition):
    """Qualified lead in the sales pipeline.
    
    Represents a prospect that has been qualified using BANT criteria.
    Used by Sales Manager Agent for lead management.
    """
    kind: str = "lead_definition"
    
    code: str
    prospect_code: Optional[str] = None  # Links to ProspectDefinition
    
    # BANT Qualification
    budget_confirmed: bool = False
    budget_range: Optional[str] = None
    authority_confirmed: bool = False
    decision_maker: Optional[str] = None
    need_identified: bool = False
    pain_points: List[str] = []
    timeline: Optional[str] = None
    
    # Scoring
    lead_score: int = 0  # 0-100
    lead_grade: Optional[str] = None  # "A", "B", "C", "D"
    is_mql: bool = False  # Marketing Qualified Lead
    is_sql: bool = False  # Sales Qualified Lead
    
    # Status
    status: str = "new"  # "new", "working", "nurturing", "qualified", "converted", "lost"
    qualified_date: Optional[str] = None
    assigned_to: Optional[str] = None


class OpportunityDefinition(NodeDefinition):
    """Sales opportunity in the pipeline.
    
    Represents a qualified deal being pursued.
    Used by Sales Manager Agent for opportunity management.
    """
    kind: str = "opportunity_definition"
    
    code: str
    lead_code: Optional[str] = None  # Links to LeadDefinition
    
    # Deal details
    opportunity_name: str
    deal_value: float = 0.0
    currency: str = "USD"
    products_services: List[str] = []
    
    # Pipeline
    stage: str = "discovery"  # "discovery", "qualification", "proposal", "negotiation", "closing", "won", "lost"
    win_probability: int = 50  # 0-100
    expected_close_date: Optional[str] = None
    actual_close_date: Optional[str] = None
    
    # Competition
    competitors: List[str] = []
    competitive_position: Optional[str] = None  # "strong", "neutral", "weak"
    
    # Activities
    next_action: Optional[str] = None
    next_action_date: Optional[str] = None
    
    # Ownership
    owner: Optional[str] = None  # Links to ActorDefinition
    team_members: List[str] = []


class DealDefinition(NodeDefinition):
    """Closed deal (won opportunity).
    
    Represents a successfully closed sale.
    Used by Sales Manager and Accountant Agents.
    """
    kind: str = "deal_definition"
    
    code: str
    opportunity_code: str  # Links to OpportunityDefinition
    client_code: str  # Links to ClientDefinition
    
    # Contract details
    contract_value: float
    contract_term_months: int = 12
    contract_start_date: str
    contract_end_date: Optional[str] = None
    
    # Products/Services
    products_services: List[str] = []
    pricing_model: str = "fixed"  # "fixed", "subscription", "usage_based", "hybrid"
    
    # Status
    status: str = "active"  # "active", "renewed", "churned", "expired"
    renewal_date: Optional[str] = None
    
    # Revenue
    arr: Optional[float] = None  # Annual Recurring Revenue
    mrr: Optional[float] = None  # Monthly Recurring Revenue


# ---------------------------------------------------------------------------
# Project Management layer (Project Manager Agent)
# ---------------------------------------------------------------------------


class ProjectDefinition(NodeDefinition):
    """Project for client engagement.
    
    Represents a project with scope, timeline, and deliverables.
    Used by Project Manager Agent for project tracking.
    """
    kind: str = "project_definition"
    
    code: str
    client_code: str  # Links to ClientDefinition
    deal_code: Optional[str] = None  # Links to DealDefinition
    
    # Project details
    project_name: str
    project_type: str  # "implementation", "consulting", "development", "support"
    
    # Timeline
    start_date: Optional[str] = None
    target_end_date: Optional[str] = None
    actual_end_date: Optional[str] = None
    
    # Status
    status: str = "planning"  # "planning", "in_progress", "on_hold", "completed", "cancelled"
    health: str = "green"  # "green", "yellow", "red"
    
    # Budget
    budget: Optional[float] = None
    spent: float = 0.0
    
    # Team
    project_manager: Optional[str] = None  # Links to ActorDefinition
    team_members: List[str] = []
    
    # Methodology
    methodology: str = "agile"  # "agile", "waterfall", "hybrid"


class EpicDefinition(NodeDefinition):
    """Epic (large feature or initiative).
    
    Represents a large body of work that can be broken into stories.
    Used by Project Manager Agent for backlog management.
    """
    kind: str = "epic_definition"
    
    code: str
    project_code: str  # Links to ProjectDefinition
    
    # Epic details
    title: str
    business_value: Optional[str] = None
    acceptance_criteria: List[str] = []
    
    # Status
    status: str = "backlog"  # "backlog", "in_progress", "done"
    priority: str = "medium"  # "critical", "high", "medium", "low"
    
    # Sizing
    story_points: Optional[int] = None
    estimated_days: Optional[int] = None


class SprintDefinition(NodeDefinition):
    """Sprint (time-boxed iteration).
    
    Represents a sprint in agile methodology.
    Used by Project Manager Agent for sprint planning.
    """
    kind: str = "sprint_definition"
    
    code: str
    project_code: str  # Links to ProjectDefinition
    
    # Sprint details
    sprint_name: str
    sprint_number: int
    
    # Timeline
    start_date: str
    end_date: str
    
    # Capacity
    capacity_points: Optional[int] = None
    committed_points: int = 0
    completed_points: int = 0
    
    # Status
    status: str = "planning"  # "planning", "active", "completed"
    
    # Goals
    sprint_goal: Optional[str] = None


class UserStoryDefinition(NodeDefinition):
    """User story (requirement).
    
    Represents a user requirement in agile format.
    Used by Project Manager Agent for backlog management.
    """
    kind: str = "user_story_definition"
    
    code: str
    epic_code: Optional[str] = None  # Links to EpicDefinition
    sprint_code: Optional[str] = None  # Links to SprintDefinition
    
    # Story details
    title: str
    as_a: str  # User role
    i_want: str  # Desired action
    so_that: str  # Business value
    
    # Acceptance criteria
    acceptance_criteria: List[str] = []
    
    # Status
    status: str = "backlog"  # "backlog", "ready", "in_progress", "review", "done"
    priority: str = "medium"  # "critical", "high", "medium", "low"
    
    # Sizing
    story_points: Optional[int] = None
    
    # Assignment
    assignee: Optional[str] = None  # Links to ActorDefinition


# ---------------------------------------------------------------------------
# Financial Documents layer (Accountant Agent)
# ---------------------------------------------------------------------------


class ProposalDefinition(NodeDefinition):
    """Client proposal document.
    
    Represents a proposal with pricing and scope.
    Used by Accountant Agent for proposal management.
    """
    kind: str = "proposal_definition"
    
    code: str
    prospect_code: Optional[str] = None  # Links to ProspectDefinition
    opportunity_code: Optional[str] = None  # Links to OpportunityDefinition
    
    # Proposal details
    proposal_title: str
    executive_summary: Optional[str] = None
    
    # Pricing
    pricing_model: str = "fixed"  # "fixed", "time_and_materials", "retainer", "hybrid"
    total_amount: float = 0.0
    currency: str = "USD"
    
    # Scope items
    scope_items: List[Dict[str, Any]] = []  # [{description, amount, type}]
    
    # Terms
    payment_terms: Optional[str] = None
    validity_days: int = 30
    
    # Status
    status: str = "draft"  # "draft", "sent", "viewed", "accepted", "rejected", "expired"
    sent_date: Optional[str] = None
    response_date: Optional[str] = None


class StatementOfWorkDefinition(NodeDefinition):
    """Statement of Work (SOW) document.
    
    Represents a detailed SOW with deliverables and milestones.
    Used by Accountant Agent for SOW management.
    """
    kind: str = "statement_of_work_definition"
    
    code: str
    proposal_code: Optional[str] = None  # Links to ProposalDefinition
    deal_code: Optional[str] = None  # Links to DealDefinition
    project_code: Optional[str] = None  # Links to ProjectDefinition
    
    # SOW details
    sow_title: str
    objectives: List[str] = []
    
    # Deliverables
    deliverables: List[Dict[str, Any]] = []  # [{name, description, acceptance_criteria, due_date}]
    
    # Milestones
    milestones: List[Dict[str, Any]] = []  # [{name, due_date, payment_amount, deliverables}]
    
    # Resources
    resource_allocation: List[Dict[str, Any]] = []  # [{role, hours, rate}]
    
    # Terms
    total_value: float = 0.0
    payment_schedule: List[Dict[str, Any]] = []
    change_management_process: Optional[str] = None
    
    # Status
    status: str = "draft"  # "draft", "pending_approval", "approved", "active", "completed"


class InvoiceDefinition(NodeDefinition):
    """Invoice for billing.
    
    Represents an invoice for services rendered.
    Used by Accountant Agent for AR management.
    """
    kind: str = "invoice_definition"
    
    code: str
    client_code: str  # Links to ClientDefinition
    deal_code: Optional[str] = None  # Links to DealDefinition
    sow_code: Optional[str] = None  # Links to StatementOfWorkDefinition
    milestone_id: Optional[str] = None
    
    # Invoice details
    invoice_number: str
    invoice_date: str
    due_date: str
    
    # Line items
    line_items: List[Dict[str, Any]] = []  # [{description, quantity, unit_price, amount}]
    
    # Amounts
    subtotal: float = 0.0
    tax_rate: float = 0.0
    tax_amount: float = 0.0
    total_amount: float = 0.0
    
    # Status
    status: str = "draft"  # "draft", "sent", "viewed", "paid", "overdue", "cancelled"
    paid_date: Optional[str] = None
    paid_amount: float = 0.0


class PaymentDefinition(NodeDefinition):
    """Payment received.
    
    Represents a payment transaction.
    Used by Accountant Agent for payment tracking.
    """
    kind: str = "payment_definition"
    
    code: str
    invoice_code: str  # Links to InvoiceDefinition
    client_code: str  # Links to ClientDefinition
    
    # Payment details
    payment_date: str
    amount: float
    currency: str = "USD"
    
    # Method
    payment_method: str  # "wire", "ach", "credit_card", "check"
    reference_number: Optional[str] = None
    
    # Status
    status: str = "completed"  # "pending", "completed", "failed", "refunded"


# ---------------------------------------------------------------------------
# Marketing layer (Marketing Manager Agent)
# ---------------------------------------------------------------------------


class BuyerPersonaDefinition(NodeDefinition):
    """Buyer persona for targeting.
    
    Represents an ideal customer profile.
    Used by Marketing Manager Agent for targeting.
    """
    kind: str = "buyer_persona_definition"
    
    code: str
    
    # Demographics
    persona_name: str
    job_title: str
    industry: Optional[str] = None
    company_size: Optional[str] = None
    
    # Psychographics
    pain_points: List[str] = []
    goals: List[str] = []
    challenges: List[str] = []
    motivations: List[str] = []
    
    # Behavior
    preferred_channels: List[str] = []
    content_preferences: List[str] = []
    decision_criteria: List[str] = []
    
    # Journey
    awareness_triggers: List[str] = []
    evaluation_factors: List[str] = []
    objections: List[str] = []


class MarketingCampaignDefinition(NodeDefinition):
    """Marketing campaign.
    
    Represents a marketing campaign with channels and metrics.
    Used by Marketing Manager Agent for campaign management.
    """
    kind: str = "marketing_campaign_definition"
    
    code: str
    
    # Campaign details
    campaign_name: str
    campaign_type: str  # "awareness", "lead_generation", "nurturing", "conversion", "retention"
    
    # Targeting
    target_personas: List[str] = []  # Links to BuyerPersonaDefinition
    target_segments: List[str] = []
    
    # Channels
    channels: List[str] = []  # "seo", "sem", "social_media", "email", "content", "events"
    
    # Messaging
    key_message: Optional[str] = None
    call_to_action: Optional[str] = None
    
    # Timeline
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    
    # Budget
    budget: float = 0.0
    spent: float = 0.0
    
    # Metrics
    impressions: int = 0
    clicks: int = 0
    conversions: int = 0
    leads_generated: int = 0
    revenue_attributed: float = 0.0
    
    # Status
    status: str = "draft"  # "draft", "scheduled", "active", "paused", "completed"


class LeadScoringModelDefinition(NodeDefinition):
    """Lead scoring model.
    
    Defines criteria for scoring leads.
    Used by Marketing Manager Agent for lead qualification.
    """
    kind: str = "lead_scoring_model_definition"
    
    code: str
    
    # Model details
    model_name: str
    
    # Demographic scoring
    demographic_criteria: List[Dict[str, Any]] = []  # [{attribute, value, points}]
    
    # Behavioral scoring
    behavioral_criteria: List[Dict[str, Any]] = []  # [{action, points}]
    
    # Thresholds
    mql_threshold: int = 50  # Marketing Qualified Lead threshold
    sql_threshold: int = 80  # Sales Qualified Lead threshold
    
    # Status
    is_active: bool = True


class ContentCalendarDefinition(NodeDefinition):
    """Content calendar for planning.
    
    Represents a content publishing schedule.
    Used by Marketing Manager Agent for content planning.
    """
    kind: str = "content_calendar_definition"
    
    code: str
    
    # Calendar details
    calendar_name: str
    duration_weeks: int = 4
    
    # Content types
    content_types: List[str] = []  # "blog_post", "whitepaper", "video", "webinar", etc.
    themes: List[str] = []
    
    # Schedule
    publishing_frequency: Optional[str] = None
    content_items: List[Dict[str, Any]] = []  # [{title, type, publish_date, status}]


# ---------------------------------------------------------------------------
# Technical / DDD layer (Architect Agent)
# ---------------------------------------------------------------------------


class BoundedContextDefinition(NodeDefinition):
    """DDD Bounded Context.
    
    Represents a bounded context with ubiquitous language.
    Used by Architect Agent for DDD design.
    """
    kind: str = "bounded_context_definition"
    
    code: str
    
    # Context details
    subdomain_type: str  # "core", "supporting", "generic"
    
    # Ubiquitous language
    ubiquitous_language: List[Dict[str, str]] = []  # [{term, definition}]
    
    # Aggregates
    aggregates: List[str] = []  # Links to AggregateDefinition
    
    # Context relationships
    upstream_contexts: List[str] = []
    downstream_contexts: List[str] = []
    integration_pattern: Optional[str] = None  # "partnership", "shared_kernel", etc.


class AggregateDefinition(NodeDefinition):
    """DDD Aggregate.
    
    Represents an aggregate with root entity and invariants.
    Used by Architect Agent for DDD design.
    """
    kind: str = "aggregate_definition"
    
    code: str
    bounded_context_code: str  # Links to BoundedContextDefinition
    
    # Aggregate details
    root_entity: str  # Links to EntityDefinition
    
    # Components
    entities: List[str] = []  # Links to EntityDefinition
    value_objects: List[Dict[str, Any]] = []  # [{name, attributes}]
    
    # Invariants
    invariants: List[str] = []  # Business rules
    
    # Design rules
    design_rules: List[str] = [
        "External references only to the aggregate root",
        "Transactional consistency within aggregate boundary",
        "Eventual consistency between aggregates"
    ]


class DomainEventDefinition(NodeDefinition):
    """DDD Domain Event.
    
    Represents a domain event that captures something significant.
    Used by Architect Agent for event-driven design.
    """
    kind: str = "domain_event_definition"
    
    code: str
    source_aggregate: str  # Links to AggregateDefinition
    bounded_context_code: str  # Links to BoundedContextDefinition
    
    # Event details (name should be past tense)
    event_name: str  # e.g., "OrderPlaced", "PaymentReceived"
    
    # Payload
    payload_fields: List[Dict[str, str]] = []  # [{field, type}]
    
    # Subscribers
    subscribers: List[str] = []  # Bounded contexts or aggregates
    
    # Characteristics
    is_immutable: bool = True


# ---------------------------------------------------------------------------
# Testing layer (Tester Agent)
# ---------------------------------------------------------------------------


class TestSuiteDefinition(NodeDefinition):
    """Test suite for validation.
    
    Represents a collection of test cases.
    Used by Tester Agent for test management.
    """
    kind: str = "test_suite_definition"
    
    code: str
    
    # Suite details
    suite_name: str
    suite_type: str  # "unit", "integration", "e2e", "performance", "security"
    
    # Scope
    target_artifact: Optional[str] = None  # What is being tested
    target_type: Optional[str] = None  # "schema", "model", "api", "formula"
    
    # Test cases
    test_cases: List[str] = []  # Links to TestCaseDefinition
    
    # Status
    status: str = "draft"  # "draft", "ready", "running", "passed", "failed"
    last_run_date: Optional[str] = None
    pass_rate: Optional[float] = None


class TestCaseDefinition(NodeDefinition):
    """Test case for validation.
    
    Represents an individual test case.
    Used by Tester Agent for test execution.
    """
    kind: str = "test_case_definition"
    
    code: str
    suite_code: Optional[str] = None  # Links to TestSuiteDefinition
    
    # Test details
    test_name: str
    test_type: str  # "positive", "negative", "edge_case", "boundary"
    
    # Test definition
    preconditions: List[str] = []
    test_steps: List[str] = []
    expected_result: str
    
    # Test data
    test_data: Dict[str, Any] = {}
    
    # Status
    status: str = "not_run"  # "not_run", "passed", "failed", "blocked", "skipped"
    actual_result: Optional[str] = None
    error_message: Optional[str] = None
    
    # Priority
    priority: str = "medium"  # "critical", "high", "medium", "low"


# ---------------------------------------------------------------------------
# Deployment layer (Deployment Specialist Agent)
# ---------------------------------------------------------------------------


class EnvironmentDefinition(NodeDefinition):
    """Deployment environment.
    
    Represents a deployment environment (dev, staging, prod).
    Used by Deployment Specialist Agent.
    """
    kind: str = "environment_definition"
    
    code: str
    
    # Environment details
    environment_name: str
    environment_type: str  # "development", "staging", "production"
    
    # Infrastructure
    cloud_provider: Optional[str] = None  # "azure", "aws", "gcp"
    region: Optional[str] = None
    
    # Configuration
    config: Dict[str, Any] = {}
    secrets_ref: Optional[str] = None  # Reference to secrets manager
    
    # Status
    status: str = "active"  # "active", "maintenance", "deprecated"


class DeploymentConfigDefinition(NodeDefinition):
    """Deployment configuration.
    
    Represents deployment settings for an artifact.
    Used by Deployment Specialist Agent.
    """
    kind: str = "deployment_config_definition"
    
    code: str
    environment_code: str  # Links to EnvironmentDefinition
    
    # Artifact
    artifact_type: str  # "service", "database", "function", "container"
    artifact_name: str
    artifact_version: Optional[str] = None
    
    # Kubernetes/Container
    replicas: int = 1
    cpu_request: Optional[str] = None
    memory_request: Optional[str] = None
    cpu_limit: Optional[str] = None
    memory_limit: Optional[str] = None
    
    # Networking
    port: Optional[int] = None
    ingress_enabled: bool = False
    
    # Health
    health_check_path: Optional[str] = None
    readiness_probe: Optional[Dict[str, Any]] = None
    liveness_probe: Optional[Dict[str, Any]] = None
    
    # Status
    status: str = "pending"  # "pending", "deploying", "deployed", "failed"
    deployed_at: Optional[str] = None


# ---------------------------------------------------------------------------
# UI/Dashboard layer (UI Designer Agent)
# ---------------------------------------------------------------------------


class DashboardLayoutDefinition(NodeDefinition):
    """Dashboard layout design.
    
    Represents a dashboard layout with sections and widgets.
    Used by UI Designer Agent for dashboard design.
    """
    kind: str = "dashboard_layout_definition"
    
    code: str
    
    # Dashboard details
    dashboard_name: str
    dashboard_type: str  # "executive", "operational", "analytical", "tactical"
    
    # Layout
    layout_type: str = "grid"  # "grid", "freeform", "tabs"
    columns: int = 12
    
    # Sections
    sections: List[Dict[str, Any]] = []  # [{name, row, col, width, height, widgets}]
    
    # Widgets
    widgets: List[Dict[str, Any]] = []  # [{type, metric_code, chart_type, position}]
    
    # Filters
    global_filters: List[str] = []  # Dimension codes
    
    # Refresh
    refresh_frequency: str = "manual"  # "real-time", "5min", "15min", "hourly", "daily", "manual"


class StyleGuideDefinition(NodeDefinition):
    """Style guide for UI design.
    
    Represents design tokens and styling rules.
    Used by UI Designer Agent for consistent styling.
    """
    kind: str = "style_guide_definition"
    
    code: str
    
    # Colors
    primary_color: str = "#1976D2"
    secondary_color: str = "#424242"
    accent_color: str = "#FF4081"
    background_color: str = "#FFFFFF"
    surface_color: str = "#F5F5F5"
    error_color: str = "#D32F2F"
    success_color: str = "#388E3C"
    warning_color: str = "#F57C00"
    
    # Data visualization colors
    chart_colors: List[str] = []
    sequential_palette: List[str] = []
    diverging_palette: List[str] = []
    
    # Typography
    font_family: str = "Inter, sans-serif"
    heading_sizes: Dict[str, str] = {}  # {"h1": "2rem", "h2": "1.5rem", ...}
    body_size: str = "1rem"
    
    # Spacing
    spacing_unit: int = 8  # Base spacing in pixels
    border_radius: str = "4px"
    
    # Shadows
    elevation_levels: Dict[str, str] = {}


class UIComponentDefinition(NodeDefinition):
    """UI component specification.
    
    Represents a reusable UI component.
    Used by UI Designer Agent for component library.
    """
    kind: str = "ui_component_definition"
    
    code: str
    
    # Component details
    component_name: str
    component_type: str  # "chart", "card", "table", "filter", "form", "navigation"
    
    # Props
    props: List[Dict[str, Any]] = []  # [{name, type, required, default}]
    
    # Variants
    variants: List[str] = []
    
    # Styling
    css_class: Optional[str] = None
    style_overrides: Dict[str, Any] = {}
    
    # Accessibility
    aria_label: Optional[str] = None
    keyboard_navigation: bool = True


# ---------------------------------------------------------------------------
# Analytics / ML layer (Data Scientist, Operations Manager Agents)
# ---------------------------------------------------------------------------


class MLModelDefinition(NodeDefinition):
    """Machine learning model specification.
    
    Represents an ML model for predictions.
    Used by Data Scientist Agent for model management.
    """
    kind: str = "ml_model_definition"
    
    code: str
    
    # Model details
    model_name: str
    model_type: str  # "regression", "classification", "clustering", "time_series", "anomaly_detection"
    algorithm: Optional[str] = None  # "random_forest", "xgboost", "lstm", etc.
    
    # Purpose
    prediction_target: str  # What is being predicted
    business_use_case: Optional[str] = None
    
    # Features
    feature_columns: List[str] = []
    target_column: str
    
    # Performance
    accuracy: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    f1_score: Optional[float] = None
    rmse: Optional[float] = None
    mae: Optional[float] = None
    
    # Training
    training_data_source: Optional[str] = None
    training_date: Optional[str] = None
    training_samples: Optional[int] = None
    
    # Deployment
    model_version: str = "1.0.0"
    is_deployed: bool = False
    endpoint_url: Optional[str] = None
    
    # Interpretability
    interpretability_level: str = "medium"  # "high", "medium", "low"
    feature_importance: Dict[str, float] = {}


class CorrelationAnalysisDefinition(NodeDefinition):
    """Correlation analysis between metrics.
    
    Represents statistical correlation analysis.
    Used by Data Scientist and Operations Manager Agents.
    """
    kind: str = "correlation_analysis_definition"
    
    code: str
    
    # Analysis details
    analysis_name: str
    
    # Metrics being correlated
    metric_a: str  # Links to MetricDefinition
    metric_b: str  # Links to MetricDefinition
    
    # Results
    correlation_coefficient: Optional[float] = None  # -1 to 1
    correlation_type: Optional[str] = None  # "positive", "negative", "none"
    p_value: Optional[float] = None
    confidence_level: float = 0.95
    
    # Method
    method: str = "pearson"  # "pearson", "spearman", "kendall"
    
    # Time lag
    time_lag: Optional[str] = None  # e.g., "7 days", "1 month"
    is_leading_indicator: bool = False
    
    # Causality
    granger_causality_tested: bool = False
    is_causal: Optional[bool] = None
    
    # Status
    validated: bool = False
    validated_by: Optional[str] = None
    validated_date: Optional[str] = None


class OptimizationPlanDefinition(NodeDefinition):
    """Optimization plan for performance improvement.
    
    Represents a prioritized optimization plan.
    Used by Operations Manager Agent.
    """
    kind: str = "optimization_plan_definition"
    
    code: str
    
    # Plan details
    plan_name: str
    
    # Focus areas
    focus_kpis: List[str] = []  # Links to MetricDefinition
    bottlenecks_addressed: List[str] = []
    
    # Initiatives
    quick_wins: List[Dict[str, Any]] = []  # [{title, impact, effort, timeline}]
    strategic_initiatives: List[Dict[str, Any]] = []  # [{title, impact, effort, timeline}]
    
    # Expected impact
    expected_improvement: Dict[str, float] = {}  # {kpi_code: improvement_percentage}
    confidence_level: str = "medium"  # "high", "medium", "low"
    
    # Timeline
    implementation_start: Optional[str] = None
    implementation_end: Optional[str] = None
    
    # Status
    status: str = "draft"  # "draft", "approved", "in_progress", "completed"


class OperationalHealthDefinition(NodeDefinition):
    """Operational health assessment.
    
    Represents an operational health scorecard.
    Used by Operations Manager Agent.
    """
    kind: str = "operational_health_definition"
    
    code: str
    
    # Assessment details
    assessment_name: str
    assessment_date: str
    
    # Overall score
    overall_score: float = 0.0  # 0-100
    health_status: str = "unknown"  # "excellent", "good", "fair", "poor", "critical"
    
    # Category scores
    category_scores: Dict[str, float] = {}  # {category: score}
    
    # SWOT
    strengths: List[str] = []
    weaknesses: List[str] = []
    opportunities: List[str] = []
    threats: List[str] = []
    
    # Recommendations
    priority_actions: List[str] = []


# ---------------------------------------------------------------------------
# Customer Success layer (Customer Success Manager Agent)
# ---------------------------------------------------------------------------


class CustomerHealthScoreDefinition(NodeDefinition):
    """Customer health score for retention tracking.
    
    Represents a customer health assessment.
    Used by Customer Success Manager Agent.
    """
    kind: str = "customer_health_score_definition"
    
    code: str
    client_code: str  # Links to ClientDefinition
    
    # Component scores (0-100)
    overall_score: float = 50.0
    usage_score: float = 50.0
    engagement_score: float = 50.0
    support_score: float = 50.0
    payment_score: float = 50.0
    adoption_score: float = 50.0
    
    # Status
    health_status: str = "neutral"  # "healthy", "neutral", "at_risk", "critical"
    
    # Trend
    trend: Optional[str] = None  # "improving", "stable", "declining"
    previous_score: Optional[float] = None


class ChurnRiskAssessmentDefinition(NodeDefinition):
    """Churn risk assessment for a customer.
    
    Used by Customer Success Manager Agent.
    """
    kind: str = "churn_risk_assessment_definition"
    
    code: str
    client_code: str  # Links to ClientDefinition
    
    # Risk assessment
    risk_level: str = "low"  # "critical", "high", "medium", "low"
    churn_probability: float = 0.1  # 0-1
    
    # Risk factors
    risk_factors: List[str] = []
    mitigation_actions: List[str] = []
    
    # Prediction
    predicted_churn_date: Optional[str] = None
    days_until_churn: Optional[int] = None


class NPSSurveyDefinition(NodeDefinition):
    """NPS survey response.
    
    Used by Customer Success Manager Agent.
    """
    kind: str = "nps_survey_definition"
    
    code: str
    client_code: str  # Links to ClientDefinition
    
    # NPS data
    score: int  # 0-10
    category: str  # "promoter", "passive", "detractor"
    feedback: Optional[str] = None
    
    # Context
    survey_date: str
    touchpoint: Optional[str] = None  # "onboarding", "support", "renewal", etc.


# ---------------------------------------------------------------------------
# HR/Talent layer (HR Talent Analyst Agent)
# ---------------------------------------------------------------------------


class EmployeeDefinition(NodeDefinition):
    """Employee record for HR analytics.
    
    Used by HR Talent Analyst Agent.
    """
    kind: str = "employee_definition"
    
    code: str
    
    # Basic info
    department: str
    role: str
    level: Optional[str] = None  # "individual_contributor", "manager", "director", "executive"
    location: Optional[str] = None
    
    # Tenure
    hire_date: str
    tenure_months: Optional[int] = None
    
    # Status
    status: str = "active"  # "active", "on_leave", "terminated"
    termination_type: Optional[str] = None  # "voluntary", "involuntary"
    termination_date: Optional[str] = None


class EngagementSurveyDefinition(NodeDefinition):
    """Employee engagement survey results.
    
    Used by HR Talent Analyst Agent.
    """
    kind: str = "engagement_survey_definition"
    
    code: str
    
    # Survey info
    survey_name: str
    survey_date: str
    
    # Scores
    overall_score: float  # 0-100
    dimension_scores: Dict[str, float] = {}  # {dimension: score}
    
    # Participation
    response_rate: float = 0.0
    respondent_count: int = 0
    
    # eNPS
    enps_score: Optional[int] = None  # -100 to 100


class SkillsGapAnalysisDefinition(NodeDefinition):
    """Skills gap analysis for workforce planning.
    
    Used by HR Talent Analyst Agent.
    """
    kind: str = "skills_gap_analysis_definition"
    
    code: str
    department: str
    
    # Skills assessment
    required_skills: List[str] = []
    current_skills: List[str] = []
    gap_skills: List[str] = []
    
    # Recommendations
    training_recommendations: List[str] = []
    hiring_recommendations: List[str] = []
    
    # Priority
    priority: str = "medium"  # "critical", "high", "medium", "low"


# ---------------------------------------------------------------------------
# Risk & Compliance layer (Risk Compliance Officer Agent)
# ---------------------------------------------------------------------------


class RiskAssessmentDefinition(NodeDefinition):
    """Enterprise risk assessment.
    
    Used by Risk & Compliance Officer Agent.
    """
    kind: str = "risk_assessment_definition"
    
    code: str
    
    # Risk details
    risk_name: str
    risk_category: str  # "operational", "financial", "strategic", "compliance", "technology", "reputational"
    
    # Scoring (1-5 scale)
    likelihood: int = 3
    impact: int = 3
    risk_score: int = 9  # likelihood * impact
    risk_level: str = "medium"  # "critical", "high", "medium", "low"
    
    # Mitigation
    mitigation_controls: List[str] = []
    residual_risk_score: Optional[int] = None
    
    # Status
    status: str = "open"  # "open", "mitigated", "accepted", "transferred"
    owner: Optional[str] = None


class ComplianceRequirementDefinition(NodeDefinition):
    """Compliance requirement tracking.
    
    Used by Risk & Compliance Officer Agent.
    """
    kind: str = "compliance_requirement_definition"
    
    code: str
    
    # Requirement details
    regulation: str  # "SOX", "GDPR", "HIPAA", "SOC2", "PCI_DSS", etc.
    requirement_id: str
    
    # Status
    status: str = "partial"  # "compliant", "non_compliant", "partial", "not_applicable"
    
    # Evidence
    evidence: List[str] = []
    last_audit_date: Optional[str] = None
    next_audit_date: Optional[str] = None


class ControlEvaluationDefinition(NodeDefinition):
    """Internal control evaluation.
    
    Used by Risk & Compliance Officer Agent.
    """
    kind: str = "control_evaluation_definition"
    
    code: str
    
    # Control details
    control_name: str
    control_type: str  # "preventive", "detective", "corrective"
    
    # Evaluation
    effectiveness: str  # "effective", "partially_effective", "ineffective"
    test_results: Optional[str] = None
    
    # Gaps
    gaps_identified: List[str] = []
    remediation_actions: List[str] = []


# ---------------------------------------------------------------------------
# Supply Chain layer (Supply Chain Analyst Agent)
# ---------------------------------------------------------------------------


class SupplierDefinition(NodeDefinition):
    """Supplier for supply chain management.
    
    Used by Supply Chain Analyst Agent.
    """
    kind: str = "supplier_definition"
    
    code: str
    supplier_name: str
    
    # Classification
    category: str  # "raw_materials", "components", "services", "logistics"
    tier: int = 1  # 1, 2, 3 (tier 1 = direct supplier)
    
    # Location
    country: Optional[str] = None
    region: Optional[str] = None
    
    # Performance
    on_time_delivery_rate: Optional[float] = None
    quality_score: Optional[float] = None
    cost_competitiveness: Optional[float] = None
    
    # Risk
    risk_level: str = "medium"  # "high", "medium", "low"
    is_sole_source: bool = False


class InventoryItemDefinition(NodeDefinition):
    """Inventory item for supply chain tracking.
    
    Used by Supply Chain Analyst Agent.
    """
    kind: str = "inventory_item_definition"
    
    code: str
    product_code: str
    
    # Classification (ABC/XYZ)
    abc_class: str = "B"  # "A", "B", "C"
    xyz_class: str = "Y"  # "X", "Y", "Z"
    
    # Levels
    current_quantity: int = 0
    safety_stock: int = 0
    reorder_point: int = 0
    economic_order_quantity: Optional[int] = None
    
    # Metrics
    turnover_rate: Optional[float] = None
    days_of_supply: Optional[int] = None
    
    # Status
    status: str = "in_stock"  # "in_stock", "low_stock", "out_of_stock", "excess"


class SCORMetricDefinition(NodeDefinition):
    """SCOR framework metric.
    
    Used by Supply Chain Analyst Agent.
    """
    kind: str = "scor_metric_definition"
    
    code: str
    
    # SCOR classification
    scor_level: int = 1  # 1, 2, or 3
    scor_process: str  # "plan", "source", "make", "deliver", "return"
    
    # Metric details
    metric_name: str
    current_value: Optional[float] = None
    target_value: Optional[float] = None
    benchmark_value: Optional[float] = None
    
    # Performance
    performance_gap: Optional[float] = None
    trend: Optional[str] = None  # "improving", "stable", "declining"


# ---------------------------------------------------------------------------
# ITIL layer (ITIL Manager Agent)
# ---------------------------------------------------------------------------


class ITILIncidentDefinition(NodeDefinition):
    """ITIL incident record.
    
    Used by ITIL Manager Agent.
    """
    kind: str = "itil_incident_definition"
    
    code: str
    
    # Incident details
    title: str
    category: str  # "hardware", "software", "network", "security", "access", "other"
    
    # Priority matrix
    priority: str  # "critical", "high", "medium", "low"
    impact: str  # "widespread", "significant", "moderate", "minor"
    urgency: str  # "critical", "high", "medium", "low"
    
    # Service
    affected_service: Optional[str] = None
    
    # Status
    status: str = "open"  # "open", "in_progress", "pending", "resolved", "closed"
    
    # Timing
    logged_at: str
    resolved_at: Optional[str] = None
    resolution_time_minutes: Optional[int] = None


class ITILProblemDefinition(NodeDefinition):
    """ITIL problem record for root cause analysis.
    
    Used by ITIL Manager Agent.
    """
    kind: str = "itil_problem_definition"
    
    code: str
    
    # Problem details
    title: str
    category: Optional[str] = None
    
    # Related incidents
    related_incidents: List[str] = []
    
    # Root cause
    root_cause: Optional[str] = None
    workaround: Optional[str] = None
    
    # Status
    status: str = "open"  # "open", "known_error", "resolved", "closed"


class ChangeRequestDefinition(NodeDefinition):
    """ITIL change request (RFC).
    
    Used by ITIL Manager Agent.
    """
    kind: str = "change_request_definition"
    
    code: str
    
    # Change details
    title: str
    change_type: str  # "standard", "normal", "emergency"
    category: str  # "infrastructure", "application", "security", "network", "database"
    
    # Risk
    risk_level: str  # "high", "medium", "low"
    
    # Plans
    implementation_plan: Optional[str] = None
    rollback_plan: Optional[str] = None
    
    # Approval
    approval_required: bool = True
    cab_review: bool = False
    
    # Status
    status: str = "submitted"  # "submitted", "approved", "rejected", "scheduled", "implemented", "failed"
    scheduled_date: Optional[str] = None


class ServiceLevelAgreementDefinition(NodeDefinition):
    """Service Level Agreement (SLA).
    
    Used by ITIL Manager Agent.
    """
    kind: str = "service_level_agreement_definition"
    
    code: str
    service_name: str
    
    # Targets
    availability_target: float = 99.9  # Percentage
    response_time_target: Optional[str] = None
    resolution_time_target: Optional[str] = None
    
    # Support
    support_hours: str = "8x5"  # "24x7", "8x5", etc.
    escalation_path: List[str] = []
    
    # Status
    status: str = "active"  # "draft", "active", "expired"
    
    # Performance
    current_availability: Optional[float] = None
    sla_compliance_rate: Optional[float] = None


class ConfigurationItemDefinition(NodeDefinition):
    """Configuration Item (CI) for CMDB.
    
    Used by ITIL Manager Agent.
    """
    kind: str = "configuration_item_definition"
    
    code: str
    ci_name: str
    
    # Classification
    ci_type: str  # "server", "application", "database", "network_device", "storage", "service"
    
    # Status
    status: str = "active"  # "active", "inactive", "planned", "retired"
    
    # Ownership
    owner: Optional[str] = None
    
    # Relationships
    dependencies: List[str] = []  # CIs this depends on
    dependents: List[str] = []  # CIs that depend on this
    
    # Attributes
    attributes: Dict[str, Any] = {}


# ---------------------------------------------------------------------------
# Mapping layer (Mapping Specialist Agent)
# ---------------------------------------------------------------------------


class SourceSchemaDefinition(NodeDefinition):
    """Source system schema for mapping.
    
    Used by Mapping Specialist Agent.
    """
    kind: str = "source_schema_definition"
    
    code: str
    source_system: str  # "salesforce", "sap", "quickbooks", etc.
    entity_name: str
    
    # Attributes
    attributes: List[Dict[str, Any]] = []
    attribute_count: int = 0
    
    # Metadata
    primary_key: Optional[str] = None
    foreign_keys: List[str] = []


class MappingRuleDefinition(NodeDefinition):
    """Attribute mapping rule.
    
    Used by Mapping Specialist Agent.
    """
    kind: str = "mapping_rule_definition"
    
    code: str
    
    # Source and target
    source_attribute: str
    target_attribute: str
    
    # Mapping type
    mapping_type: str  # "direct", "transform", "lookup", "derived", "constant", "conditional"
    
    # Transformation
    transformation: Dict[str, Any] = {}
    null_handling: str = "pass_through"  # "pass_through", "default_value", "reject", "derive"
    
    # Status
    status: str = "active"  # "active", "inactive", "pending_review"
    confidence_score: Optional[float] = None


class TransformationDefinition(NodeDefinition):
    """Data transformation specification.
    
    Used by Mapping Specialist Agent.
    """
    kind: str = "transformation_definition"
    
    code: str
    
    # Types
    source_type: str
    target_type: str
    transformation_type: str  # "type_cast", "format", "lookup", "calculation", "aggregation", "split", "concatenate"
    
    # Parameters
    parameters: Dict[str, Any] = {}
    
    # Validation
    is_reversible: bool = False
    potential_data_loss: bool = False


# ---------------------------------------------------------------------------
# Connection layer (Connection Specialist Agent)
# ---------------------------------------------------------------------------


class ConnectionDefinition(NodeDefinition):
    """System connection configuration.
    
    Used by Connection Specialist Agent.
    """
    kind: str = "connection_definition"
    
    code: str
    connection_name: str
    
    # Systems
    source_system: str
    target_system: str = "analytics_engine"
    
    # Connection type
    connection_type: str  # "rest_api", "graphql", "webhook", "polling", "cdc", "streaming"
    auth_method: str  # "oauth2", "api_key", "jwt", "basic", "custom"
    
    # Sync pattern
    sync_pattern: str = "near_real_time"  # "real_time", "near_real_time", "scheduled", "on_demand"
    
    # Status
    status: str = "configured"  # "designed", "configured", "active", "inactive", "error"
    
    # Metrics
    last_sync_at: Optional[str] = None
    success_rate: Optional[float] = None
    avg_latency_ms: Optional[int] = None


class APIWrapperDefinition(NodeDefinition):
    """API wrapper specification.
    
    Used by Connection Specialist Agent.
    """
    kind: str = "api_wrapper_definition"
    
    code: str
    system_name: str
    api_version: str = "v1"
    
    # Endpoints
    endpoints: List[str] = []
    
    # Implementation
    language: str = "python"  # "python", "typescript", "java"
    
    # Features
    supports_pagination: bool = True
    supports_rate_limiting: bool = True
    supports_retry: bool = True


class WebhookReceiverDefinition(NodeDefinition):
    """Webhook receiver configuration.
    
    Used by Connection Specialist Agent.
    """
    kind: str = "webhook_receiver_definition"
    
    code: str
    source_system: str
    
    # Configuration
    endpoint_path: str
    event_types: List[str] = []
    verification_method: str = "hmac"  # "hmac", "token", "ip_whitelist", "none"
    
    # Status
    status: str = "configured"  # "configured", "active", "inactive"
    
    # Metrics
    events_received: int = 0
    last_event_at: Optional[str] = None


class EventHandlerDefinition(NodeDefinition):
    """Event handler for incoming data.
    
    Used by Connection Specialist Agent.
    """
    kind: str = "event_handler_definition"
    
    code: str
    
    # Event details
    event_type: str
    source_system: str
    
    # Handler
    handler_logic: str
    target_entity: str
    
    # Status
    status: str = "active"  # "active", "inactive", "error"
    
    # Metrics
    events_processed: int = 0
    error_count: int = 0


# ---------------------------------------------------------------------------
# Document Analysis layer (Document Analyzer Agent)
# ---------------------------------------------------------------------------


class AnalyzedDocumentDefinition(NodeDefinition):
    """Analyzed document record.
    
    Used by Document Analyzer Agent.
    """
    kind: str = "analyzed_document_definition"
    
    code: str
    document_name: str
    
    # Classification
    document_type: str  # "business_plan", "technical_spec", "data_dictionary", "process_map", "requirements", "report_spec", "api_doc", "org_chart", "policy", "sop", "other"
    source_system: Optional[str] = None
    
    # Analysis
    content_length: int = 0
    analysis_status: str = "pending"  # "pending", "analyzing", "analyzed", "error"
    analyzed_at: Optional[str] = None
    
    # Extraction summary
    entities_found: int = 0
    processes_found: int = 0
    kpis_found: int = 0
    relationships_found: int = 0
    terminology_terms: int = 0
    
    # Quality
    confidence_score: float = 0.0


class ExtractedEntityDefinition(NodeDefinition):
    """Entity extracted from document.
    
    Used by Document Analyzer Agent.
    """
    kind: str = "extracted_entity_definition"
    
    code: str
    entity_name: str
    
    # Source
    document_id: str
    source_location: Optional[str] = None  # Page/section reference
    
    # Entity details
    entity_type: str  # "business_object", "data_entity", "actor", "system", "concept"
    attributes: List[Dict[str, Any]] = []
    
    # Quality
    confidence_score: float = 0.0
    requires_clarification: bool = False
    clarification_notes: Optional[str] = None


class ExtractedProcessDefinition(NodeDefinition):
    """Process extracted from document.
    
    Used by Document Analyzer Agent.
    """
    kind: str = "extracted_process_definition"
    
    code: str
    process_name: str
    
    # Source
    document_id: str
    source_location: Optional[str] = None
    
    # Process details
    process_type: str  # "workflow", "procedure", "business_process", "integration"
    steps: List[Dict[str, Any]] = []
    actors: List[str] = []
    inputs: List[str] = []
    outputs: List[str] = []
    
    # Quality
    confidence_score: float = 0.0


class ExtractedTermDefinition(NodeDefinition):
    """Domain term extracted for ubiquitous language.
    
    Used by Document Analyzer Agent.
    """
    kind: str = "extracted_term_definition"
    
    code: str
    term: str
    
    # Source
    document_id: str
    
    # Term details
    definition: Optional[str] = None
    synonyms: List[str] = []
    related_terms: List[str] = []
    context: Optional[str] = None
    
    # Classification
    domain_area: Optional[str] = None  # "sales", "finance", "operations", etc.
    
    # Quality
    confidence_score: float = 0.0


class DocumentGapAnalysisDefinition(NodeDefinition):
    """Gap analysis for document.
    
    Used by Document Analyzer Agent.
    """
    kind: str = "document_gap_analysis_definition"
    
    code: str
    document_id: str
    
    # Analysis scope
    target_areas: List[str] = []  # "entities", "processes", "kpis", "relationships"
    
    # Gaps identified
    gaps: List[Dict[str, Any]] = []
    
    # Clarification needed
    clarification_questions: List[str] = []
    
    # Status
    analyzed_at: Optional[str] = None


# ---------------------------------------------------------------------------
# Communication Style layer (Master Coordinator - Adaptive Communication)
# ---------------------------------------------------------------------------


class CommunicationStyleProfile(NodeDefinition):
    """Interviewee communication style profile for adaptive responses.
    
    Used by Master Coordinator for adaptive communication.
    """
    kind: str = "communication_style_profile"
    
    code: str
    session_id: str
    
    # Detected persona
    detected_role: str = "unknown"  # "executive", "technical", "analyst", "operations", "unknown"
    role_confidence: float = 0.0
    
    # Communication characteristics
    abstraction_level: str = "balanced"  # "strategic", "tactical", "detailed", "balanced"
    vocabulary_type: str = "mixed"  # "business", "technical", "mixed"
    detail_preference: str = "moderate"  # "summary", "moderate", "comprehensive"
    
    # Speaking patterns
    uses_metrics: bool = False
    uses_frameworks: bool = False
    asks_clarifying_questions: bool = False
    prefers_examples: bool = False
    prefers_visuals: bool = False
    
    # Detected indicators
    role_indicators: List[str] = []  # Phrases/terms that indicate role
    vocabulary_samples: List[str] = []  # Sample terms used
    
    # Response formatting preference
    preferred_response_agent: Optional[str] = None  # Agent to format responses (e.g., "architect", "business_analyst")
    response_format: str = "adaptive"  # "executive_summary", "technical_detail", "balanced", "adaptive"
    
    # Detail level adjustment (allows drilling down while maintaining core style)
    base_detail_level: int = 1  # 1=summary, 2=moderate, 3=detailed, 4=comprehensive
    current_detail_level: int = 1  # Can be adjusted up/down on demand
    max_detail_level: int = 4
    detail_adjustment_history: List[Dict[str, Any]] = []  # Track drill-down requests
    
    # Analysis metadata
    utterances_analyzed: int = 0
    last_updated_at: Optional[str] = None


class StyleDetectionResult(NodeDefinition):
    """Result of analyzing an utterance for communication style.
    
    Used by Master Coordinator for style detection.
    """
    kind: str = "style_detection_result"
    
    code: str
    utterance_id: str
    
    # Detection results
    detected_indicators: List[Dict[str, Any]] = []
    
    # Role signals
    executive_signals: List[str] = []
    technical_signals: List[str] = []
    analyst_signals: List[str] = []
    
    # Abstraction signals
    strategic_terms: List[str] = []
    tactical_terms: List[str] = []
    detailed_terms: List[str] = []
    
    # Confidence
    detection_confidence: float = 0.0
    
    # Timestamp
    detected_at: Optional[str] = None


# ---------------------------------------------------------------------------
# Competitive Intelligence layer (Competitive Analyst Agent)
# ---------------------------------------------------------------------------


class CompetitorProfileDefinition(NodeDefinition):
    """Competitor company profile.
    
    Used by Competitive Analyst Agent.
    """
    kind: str = "competitor_profile_definition"
    
    code: str
    company_name: str
    
    # Identity
    website: Optional[str] = None
    founding_year: Optional[int] = None
    headquarters: Optional[str] = None
    employee_count: Optional[int] = None
    funding_stage: Optional[str] = None  # "seed", "series_a", "series_b", "public", etc.
    total_funding: Optional[str] = None
    
    # Business Model
    business_model: Optional[str] = None
    revenue_model: Optional[str] = None  # "subscription", "transactional", "freemium", etc.
    pricing_strategy: Optional[str] = None
    target_market: Optional[str] = None
    customer_segments: List[str] = []
    
    # Offerings
    products: List[str] = []
    services: List[str] = []
    key_features: List[str] = []
    
    # Competitive Position
    strengths: List[str] = []
    weaknesses: List[str] = []
    market_position: Optional[str] = None  # "leader", "challenger", "niche", "emerging"
    competitive_advantages: List[str] = []
    
    # Metadata
    profile_depth: str = "standard"  # "basic", "standard", "comprehensive"
    confidence_score: float = 0.0
    sources: List[str] = []
    profiled_at: Optional[str] = None


class CompetitiveLandscapeDefinition(NodeDefinition):
    """Competitive landscape analysis.
    
    Used by Competitive Analyst Agent.
    """
    kind: str = "competitive_landscape_definition"
    
    code: str
    industry: str
    segment: Optional[str] = None
    
    # Analysis type
    analysis_type: str = "comprehensive"  # "five_forces", "market_map", "trend_analysis", "comprehensive"
    
    # Five Forces
    threat_of_new_entrants: Optional[str] = None  # "low", "medium", "high"
    bargaining_power_suppliers: Optional[str] = None
    bargaining_power_buyers: Optional[str] = None
    threat_of_substitutes: Optional[str] = None
    competitive_rivalry: Optional[str] = None
    
    # Market Structure
    market_leaders: List[str] = []
    challengers: List[str] = []
    niche_players: List[str] = []
    emerging_players: List[str] = []
    
    # Trends
    market_trends: List[str] = []
    technology_trends: List[str] = []
    regulatory_trends: List[str] = []
    
    # Metadata
    analyzed_at: Optional[str] = None


class MarketGapAnalysisDefinition(NodeDefinition):
    """Market gap and opportunity analysis.
    
    Used by Competitive Analyst Agent.
    """
    kind: str = "market_gap_analysis_definition"
    
    code: str
    industry: str
    
    # Analysis inputs
    current_offerings: List[str] = []
    customer_pain_points: List[str] = []
    
    # Identified gaps
    identified_gaps: List[Dict[str, Any]] = []
    
    # Opportunities
    opportunities: List[Dict[str, Any]] = []
    
    # Recommendations
    differentiation_strategies: List[str] = []
    
    # Metadata
    analyzed_at: Optional[str] = None


# ---------------------------------------------------------------------------
# Process Scenario Modeler layer (Process Scenario Modeler Agent)
# ---------------------------------------------------------------------------


class DurationDistributionDefinition(BaseModel):
    """Statistical distribution for step duration."""
    distribution_type: str = "normal"  # "fixed", "normal", "exponential", "triangular", "uniform"
    parameters: Dict[str, float] = {}  # e.g., {"mean": 10, "std": 2} for normal


class ProcessStepDefinition(BaseModel):
    """A single step in a simulatable process."""
    id: str
    name: str
    step_type: str = "task"  # "task", "decision", "parallel_gateway", "event", "subprocess"
    
    # Timing
    duration_distribution: Optional[DurationDistributionDefinition] = None
    
    # Resources
    required_resources: List[str] = []
    resource_quantity: int = 1
    
    # Cost
    fixed_cost: float = 0.0
    variable_cost_per_unit: float = 0.0
    
    # Quality
    defect_rate: float = 0.0  # Probability of defect/rework
    
    # Capacity
    max_concurrent: Optional[int] = None


class ProcessTransitionDefinition(BaseModel):
    """Transition between process steps."""
    from_step: str
    to_step: str
    condition: Optional[str] = None  # For decision gateways
    probability: float = 1.0  # For probabilistic routing


class ResourceRequirementDefinition(BaseModel):
    """Resource requirement for a process."""
    resource_type: str
    quantity: int = 1
    cost_per_unit: float = 0.0
    availability_schedule: Optional[str] = None


class SimulatableProcessDefinition(NodeDefinition):
    """A business process that can be simulated.
    
    Used by Process Scenario Modeler Agent.
    """
    kind: str = "simulatable_process_definition"
    
    code: str
    
    # Process structure
    steps: List[ProcessStepDefinition] = []
    transitions: List[ProcessTransitionDefinition] = []
    
    # Linkage to strategy
    value_chain_module: Optional[str] = None  # Links to value chain module
    linked_kpis: List[str] = []  # KPIs affected by this process
    
    # Simulation parameters
    default_parameters: Dict[str, Any] = {}
    resource_requirements: List[ResourceRequirementDefinition] = []
    
    # Metadata
    version: int = 1
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class ParameterChangeDefinition(BaseModel):
    """A change to apply in a scenario."""
    change_type: str  # "step_duration", "resource_capacity", "defect_rate", "cost", "routing_probability", "arrival_rate"
    target: str  # Step ID or resource ID
    parameter: str
    original_value: Any = None
    new_value: Any = None
    change_description: Optional[str] = None


class ArrivalDistributionDefinition(BaseModel):
    """Distribution of work item arrivals."""
    distribution_type: str = "poisson"  # "constant", "poisson", "from_data"
    parameters: Dict[str, Any] = {}


class ScenarioDefinition(NodeDefinition):
    """A what-if scenario to simulate.
    
    Used by Process Scenario Modeler Agent.
    """
    kind: str = "scenario_definition"
    
    code: str
    
    # Base process
    process_id: str
    
    # Parameter overrides
    parameter_changes: List[ParameterChangeDefinition] = []
    
    # Simulation settings
    simulation_duration_hours: float = 168.0  # 1 week default
    warm_up_period_hours: float = 24.0
    number_of_replications: int = 10
    random_seed: Optional[int] = None
    
    # Input assumptions
    arrival_distribution: Optional[ArrivalDistributionDefinition] = None
    initial_wip: int = 0
    
    # Metadata
    created_at: Optional[str] = None


class BottleneckInfoDefinition(BaseModel):
    """Information about a detected bottleneck."""
    step_id: str
    step_name: str
    utilization: float
    queue_length_avg: float
    wait_time_avg: float
    severity: str = "medium"  # "low", "medium", "high", "critical"
    recommendation: Optional[str] = None


class KPIPredictionDefinition(BaseModel):
    """Predicted KPI value from simulation."""
    kpi_code: str
    baseline_value: float = 0.0
    predicted_value: float = 0.0
    change_percent: float = 0.0
    confidence_interval_lower: float = 0.0
    confidence_interval_upper: float = 0.0
    impact_direction: str = "neutral"  # "positive", "negative", "neutral"


class SimulationEventDefinition(BaseModel):
    """A single event in the simulation event log."""
    timestamp: str
    event_type: str  # "arrival", "start", "complete", "queue", "resource_acquire", "resource_release"
    step_id: Optional[str] = None
    entity_id: str
    resource_id: Optional[str] = None
    attributes: Dict[str, Any] = {}


class SimulationResultDefinition(NodeDefinition):
    """Results from a process simulation.
    
    Used by Process Scenario Modeler Agent.
    """
    kind: str = "simulation_result_definition"
    
    code: str
    scenario_id: str
    
    # Timing metrics
    avg_cycle_time: float = 0.0
    min_cycle_time: float = 0.0
    max_cycle_time: float = 0.0
    cycle_time_std: float = 0.0
    
    # Throughput metrics
    total_completed: int = 0
    throughput_rate: float = 0.0  # per hour
    
    # Resource utilization
    resource_utilization: Dict[str, float] = {}  # resource_id -> utilization %
    
    # Cost metrics
    total_cost: float = 0.0
    cost_per_unit: float = 0.0
    
    # Quality metrics
    defect_count: int = 0
    defect_rate: float = 0.0
    rework_count: int = 0
    
    # Bottleneck analysis
    bottlenecks: List[BottleneckInfoDefinition] = []
    
    # KPI predictions
    predicted_kpi_values: List[KPIPredictionDefinition] = []
    
    # Confidence intervals
    confidence_level: float = 0.95
    
    # Metadata
    simulation_started_at: Optional[str] = None
    simulation_completed_at: Optional[str] = None
    simulation_duration_ms: int = 0


class ImpactAnalysisDefinition(NodeDefinition):
    """Analysis of scenario impact on KPIs.
    
    Used by Process Scenario Modeler Agent.
    """
    kind: str = "impact_analysis_definition"
    
    code: str
    scenario_id: str
    simulation_result_id: str
    
    # KPI impacts
    kpi_impacts: List[Dict[str, Any]] = []
    
    # Strategic alignment
    strategic_alignment_score: float = 0.0  # 0-100
    aligned_objectives: List[str] = []
    conflicting_objectives: List[str] = []
    
    # Risk assessment
    risk_level: str = "medium"  # "low", "medium", "high", "critical"
    risks: List[Dict[str, Any]] = []
    
    # Recommendations
    recommendations: List[Dict[str, Any]] = []
    
    # Trade-offs
    trade_offs: List[Dict[str, Any]] = []
    
    # Metadata
    analyzed_at: Optional[str] = None


# ---------------------------------------------------------------------------
# Predictive What-If layer (Operations Manager + Data Scientist Agents)
# ---------------------------------------------------------------------------


class ConstraintDefinitionForWhatIf(BaseModel):
    """A constraint on the what-if analysis."""
    constraint_type: str  # "budget", "capacity", "regulatory", "contractual", "other"
    description: str
    limit_value: Optional[float] = None
    limit_unit: Optional[str] = None


class WhatIfQuestionDefinition(NodeDefinition):
    """A what-if question to analyze.
    
    Used by Operations Manager and Data Scientist Agents.
    """
    kind: str = "what_if_question_definition"
    
    code: str
    question_text: str  # Natural language question
    
    # Parsed components
    change_type: str = "change"  # "increase", "decrease", "add", "remove", "change"
    change_subject: str = ""  # What is being changed (e.g., "price", "capacity")
    change_magnitude: Optional[float] = None  # Numeric change amount
    change_unit: Optional[str] = None  # Unit of change (%, $, units, etc.)
    
    # Context
    business_context: Optional[str] = None
    affected_segments: List[str] = []  # Customer segments, regions, products
    time_horizon: str = "medium_term"  # "immediate", "short_term", "medium_term", "long_term"
    
    # Constraints
    constraints: List[ConstraintDefinitionForWhatIf] = []
    assumptions: List[str] = []
    
    # Affected KPIs (identified by Operations Manager)
    affected_kpis: List[str] = []
    
    # Metadata
    asked_by: Optional[str] = None
    asked_at: Optional[str] = None
    status: str = "pending"  # "pending", "analyzing", "completed", "failed"


class HistoricalEvidenceDefinition(BaseModel):
    """Historical evidence supporting a prediction."""
    event_date: str
    event_description: str
    observed_change: float
    observed_outcome: float
    relevance_score: float = 0.0


class CascadeEffectDefinition(BaseModel):
    """A cascade effect from primary impact to secondary KPIs."""
    trigger_kpi: str
    affected_kpi: str
    relationship_type: str = "direct"  # "direct", "indirect", "lagged"
    lag_periods: Optional[int] = None
    
    # Effect magnitude
    effect_multiplier: float = 1.0  # e.g., 0.5 means 50% of trigger change
    predicted_change: float = 0.0
    
    # Confidence
    confidence: float = 0.0
    evidence_strength: str = "moderate"  # "strong", "moderate", "weak"


class KPIImpactPredictionDefinition(BaseModel):
    """Predicted impact on a specific KPI."""
    kpi_code: str
    kpi_name: str
    business_level: str = "operational"  # "tactical", "operational", "functional", "business_unit", "corporate"
    
    # Current state
    current_value: float = 0.0
    current_trend: str = "stable"  # "increasing", "decreasing", "stable"
    
    # Predicted state
    predicted_value: float = 0.0
    predicted_change_absolute: float = 0.0
    predicted_change_percent: float = 0.0
    
    # Confidence interval
    confidence_level: float = 0.95
    lower_bound: float = 0.0
    upper_bound: float = 0.0
    
    # Impact classification
    impact_direction: str = "neutral"  # "positive", "negative", "neutral"
    impact_magnitude: str = "moderate"  # "minimal", "moderate", "significant", "major"
    
    # Time to impact
    time_to_impact: Optional[str] = None  # e.g., "2-4 weeks"
    impact_duration: Optional[str] = None  # e.g., "ongoing", "temporary (3 months)"
    
    # Evidence
    historical_evidence: List[HistoricalEvidenceDefinition] = []
    correlation_strength: float = 0.0


class NetImpactDefinition(BaseModel):
    """Net business impact after all effects."""
    primary_impact_value: float = 0.0
    cascade_impact_value: float = 0.0
    total_impact_value: float = 0.0
    
    # Financial summary
    revenue_impact: float = 0.0
    cost_impact: float = 0.0
    profit_impact: float = 0.0
    
    # Risk-adjusted
    risk_adjusted_value: float = 0.0
    risk_factors: List[str] = []
    
    # Recommendation
    recommendation: str = "neutral"  # "strongly_recommend", "recommend", "neutral", "caution", "not_recommended"
    recommendation_rationale: Optional[str] = None


class SensitivityPointDefinition(BaseModel):
    """A single point in sensitivity analysis."""
    variable_value: float
    predicted_outcome: float
    confidence_lower: float = 0.0
    confidence_upper: float = 0.0


class SensitivityAnalysisDefinition(BaseModel):
    """Sensitivity analysis results."""
    variable_name: str
    target_kpi: str
    sensitivity_points: List[SensitivityPointDefinition] = []
    optimal_value: Optional[float] = None
    optimal_outcome: Optional[float] = None


class OptimalValueDefinition(BaseModel):
    """Optimal value finding result."""
    variable: str
    target_kpi: str
    optimization_goal: str  # "maximize", "minimize"
    optimal_value: float
    predicted_outcome: float
    constraints_satisfied: bool = True
    constraint_violations: List[str] = []


class ModelUsedDefinition(BaseModel):
    """An ML model used in the prediction."""
    model_type: str  # e.g., "XGBoost Regression"
    model_id: str
    purpose: str  # e.g., "Predict churn rate from price change"
    accuracy_metric: str = "r2"
    accuracy_value: float = 0.0
    feature_importance: Dict[str, float] = {}


class PredictionMethodologyDefinition(BaseModel):
    """How the prediction was generated."""
    
    # Data sources
    data_period: str = ""  # e.g., "Last 24 months"
    data_points: int = 0
    
    # Models used
    models_used: List[ModelUsedDefinition] = []
    
    # Correlation analysis
    correlations_analyzed: int = 0
    significant_correlations: int = 0
    
    # Validation
    backtesting_accuracy: float = 0.0
    cross_validation_score: float = 0.0


class WhatIfPredictionDefinition(NodeDefinition):
    """Prediction results for a what-if question.
    
    Used by Operations Manager and Data Scientist Agents.
    """
    kind: str = "what_if_prediction_definition"
    
    code: str
    question_id: str
    
    # Primary predictions
    primary_impacts: List[KPIImpactPredictionDefinition] = []
    
    # Cascade effects
    cascade_effects: List[CascadeEffectDefinition] = []
    
    # Net impact
    net_impact: Optional[NetImpactDefinition] = None
    
    # Confidence
    overall_confidence: float = 0.0  # 0-1
    data_quality_score: float = 0.0  # 0-1
    model_reliability: float = 0.0  # 0-1
    
    # Sensitivity analysis
    sensitivity_analysis: Optional[SensitivityAnalysisDefinition] = None
    
    # Optimal value
    optimal_value: Optional[OptimalValueDefinition] = None
    
    # Recommendations
    recommendations: List[Dict[str, Any]] = []
    
    # Methodology
    methodology: Optional[PredictionMethodologyDefinition] = None
    
    # Metadata
    predicted_at: Optional[str] = None
    prediction_duration_ms: int = 0


__all__ = [
    # Core building blocks
    "NodeDefinition",
    "EdgeDefinition",
    "ProcessDefinition",
    "ThingDefinition",  # Backward compatibility alias
    "RelationshipDefinition",  # Backward compatibility alias
    "ColumnDefinition",
    "TableSchemaDefinition",
    "EntityDefinition",
    "ValueSetDefinition",
    "CodeSystemDefinition",
    "MetricDefinition",
    "GraphNodePattern",
    "GraphEdgePattern",
    "GraphPatternDefinition",
    "DimensionBinding",
    "ValueChainPatternDefinition",
    "CompanyValueChainModelDefinition",
    "ActorDefinition",
    "BeneficiaryDefinition",
    "ClientDefinition",
    "RoleDefinition",
    "PermissionDefinition",
    "ModulePermissionDefinition",
    "EntityPermissionDefinition",
    "MetricPermissionDefinition",
    "AttributePermissionDefinition",
    "RowLevelSecurityDefinition",
    "CountryDefinition",
    "RegionDefinition",
    "MetropolitanAreaDefinition",
    "NAICSIndustryDefinition",
    "CompanyDefinition",
    "BusinessProcessDefinition",
    "StrategicObjectiveDefinition",
    "BenchmarkDefinition",
    "AnalyticsStrategyDefinition",
    "DataSourceDefinition",
    "DataProductDefinition",
    "AnalyticsUseCaseDefinition",
    "DimensionDefinition",
    "MetricCategoryDefinition",
    "DataQualityRuleDefinition",
    "ExternalEventDefinition",
    "ConstraintDefinition",
    "DesignPolicyRuleDefinition",
    "DesignPolicyDefinition",
    "InterviewSessionDefinition",
    "UtteranceDefinition",
    "BusinessIntentDefinition",
    "PatternMatchDefinition",
    "DesignSuggestionDefinition",
    # CRM / Sales Pipeline (Sales Manager Agent)
    "ProspectDefinition",
    "LeadDefinition",
    "OpportunityDefinition",
    "DealDefinition",
    # Project Management (Project Manager Agent)
    "ProjectDefinition",
    "EpicDefinition",
    "SprintDefinition",
    "UserStoryDefinition",
    # Financial Documents (Accountant Agent)
    "ProposalDefinition",
    "StatementOfWorkDefinition",
    "InvoiceDefinition",
    "PaymentDefinition",
    # Marketing (Marketing Manager Agent)
    "BuyerPersonaDefinition",
    "MarketingCampaignDefinition",
    "LeadScoringModelDefinition",
    "ContentCalendarDefinition",
    # Technical / DDD (Architect Agent)
    "BoundedContextDefinition",
    "AggregateDefinition",
    "DomainEventDefinition",
    # Testing (Tester Agent)
    "TestSuiteDefinition",
    "TestCaseDefinition",
    # Deployment (Deployment Specialist Agent)
    "EnvironmentDefinition",
    "DeploymentConfigDefinition",
    # UI/Dashboard (UI Designer Agent)
    "DashboardLayoutDefinition",
    "StyleGuideDefinition",
    "UIComponentDefinition",
    # Analytics / ML (Data Scientist, Operations Manager Agents)
    "MLModelDefinition",
    "CorrelationAnalysisDefinition",
    "OptimizationPlanDefinition",
    "OperationalHealthDefinition",
    # Customer Success (Customer Success Manager Agent)
    "CustomerHealthScoreDefinition",
    "ChurnRiskAssessmentDefinition",
    "NPSSurveyDefinition",
    # HR/Talent (HR Talent Analyst Agent)
    "EmployeeDefinition",
    "EngagementSurveyDefinition",
    "SkillsGapAnalysisDefinition",
    # Risk & Compliance (Risk Compliance Officer Agent)
    "RiskAssessmentDefinition",
    "ComplianceRequirementDefinition",
    "ControlEvaluationDefinition",
    # Supply Chain (Supply Chain Analyst Agent)
    "SupplierDefinition",
    "InventoryItemDefinition",
    "SCORMetricDefinition",
    # ITIL (ITIL Manager Agent)
    "ITILIncidentDefinition",
    "ITILProblemDefinition",
    "ChangeRequestDefinition",
    "ServiceLevelAgreementDefinition",
    "ConfigurationItemDefinition",
    # Mapping (Mapping Specialist Agent)
    "SourceSchemaDefinition",
    "MappingRuleDefinition",
    "TransformationDefinition",
    # Connection (Connection Specialist Agent)
    "ConnectionDefinition",
    "APIWrapperDefinition",
    "WebhookReceiverDefinition",
    "EventHandlerDefinition",
    # Document Analysis (Document Analyzer Agent)
    "AnalyzedDocumentDefinition",
    "ExtractedEntityDefinition",
    "ExtractedProcessDefinition",
    "ExtractedTermDefinition",
    "DocumentGapAnalysisDefinition",
    # Communication Style (Master Coordinator - Adaptive Communication)
    "CommunicationStyleProfile",
    "StyleDetectionResult",
    # Competitive Intelligence (Competitive Analyst Agent)
    "CompetitorProfileDefinition",
    "CompetitiveLandscapeDefinition",
    "MarketGapAnalysisDefinition",
    # Process Scenario Modeler (Process Scenario Modeler Agent)
    "DurationDistributionDefinition",
    "ProcessStepDefinition",
    "ProcessTransitionDefinition",
    "ResourceRequirementDefinition",
    "SimulatableProcessDefinition",
    "ParameterChangeDefinition",
    "ArrivalDistributionDefinition",
    "ScenarioDefinition",
    "BottleneckInfoDefinition",
    "KPIPredictionDefinition",
    "SimulationEventDefinition",
    "SimulationResultDefinition",
    "ImpactAnalysisDefinition",
    # Predictive What-If (Operations Manager + Data Scientist Agents)
    "ConstraintDefinitionForWhatIf",
    "WhatIfQuestionDefinition",
    "HistoricalEvidenceDefinition",
    "CascadeEffectDefinition",
    "KPIImpactPredictionDefinition",
    "NetImpactDefinition",
    "SensitivityPointDefinition",
    "SensitivityAnalysisDefinition",
    "OptimalValueDefinition",
    "ModelUsedDefinition",
    "PredictionMethodologyDefinition",
    "WhatIfPredictionDefinition",
]
