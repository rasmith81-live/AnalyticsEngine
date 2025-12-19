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


class ThingDefinition(BaseModel):
    """Base ontology class for all definitions."""

    model_config = ConfigDict(extra="allow")

    kind: str
    id: str
    name: str
    description: Optional[str] = None
    metadata_: Dict[str, Any] = {}
    relationships: List["RelationshipDefinition"] = []  # Outbound relationships


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


class EntityDefinition(ThingDefinition):
    """Ontology representation of a business entity/object model."""

    kind: str = "entity_definition"
    code: str
    table_schema: Optional[TableSchemaDefinition] = None
    schema_definition: Optional[str] = None  # UML / graph snippet


class RelationshipDefinition(ThingDefinition):
    """Ontology representation of a relationship between entities."""

    kind: str = "relationship_definition"
    from_entity: str
    to_entity: str
    relationship_type: str
    from_cardinality: Optional[str] = None
    to_cardinality: Optional[str] = None


# ---------------------------------------------------------------------------
# Terminology layer
# ---------------------------------------------------------------------------


class ValueSetDefinition(ThingDefinition):
    kind: str = "value_set_definition"

    codes: List[str]


class CodeSystemDefinition(ThingDefinition):
    kind: str = "code_system_definition"

    # map code -> human-readable label/description
    codes: Dict[str, str] = {}


# ---------------------------------------------------------------------------
# Metric / KPI layer
# ---------------------------------------------------------------------------


class MetricDefinition(ThingDefinition):
    """Metric/KPI definition without time or arithmetic modifiers in name.
    
    Time and arithmetic modifiers are applied at QUERY TIME via:
    - time_periods: Available time granularities
    - aggregation_methods: Available aggregation functions
    - dimensions: Available dimension filters
    
    Example: "Recurring Revenue" (NOT "Monthly Recurring Revenue")
    
    Benchmarks are stored as separate BenchmarkDefinition entities linked via relationships.
    """
    kind: str = "metric_definition"

    code: str
    category: Optional[str] = None
    modules: List[str] = []
    required_objects: List[str] = []
    formula: Optional[str] = None  # Uses Entity.attribute syntax
    unit: Optional[str] = None
    data_type: str = "decimal"
    
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


class ValueChainPatternDefinition(ThingDefinition):
    """Value chain pattern at any granularity level.
    
    The 'domain' field indicates granularity:
    - "company": Top-level (entire company as a value chain)
    - "industry" or "cross_industry": High-level value chains (e.g., SUPPLY_CHAIN, SALES_MGMT)
    - "module": Mid-level patterns (e.g., CHANNEL_SALES, CUSTOMER_SUCCESS, ASCM_SCOR)
    - "process": Low-level operational patterns
    
    All are value chain patterns, just at different scales.
    """
    kind: str = "value_chain_pattern_definition"

    domain: Optional[str] = None  # Granularity: "company", "industry", "module", "process"
    applicability: Dict[str, Any] = {}
    graph_pattern: GraphPatternDefinition = GraphPatternDefinition()
    associated_metrics: List[str] = []
    dimension_bindings: List[DimensionBinding] = []
    
    # Business ontology fields
    business_purpose: Optional[str] = None  # Purpose statement
    intended_value: Optional[str] = None  # Value to be produced


class CompanyValueChainModelDefinition(ThingDefinition):
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


class ActorDefinition(ThingDefinition):
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


class ClientDefinition(ThingDefinition):
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


class PermissionDefinition(ThingDefinition):
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


class RowLevelSecurityDefinition(ThingDefinition):
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


class CountryDefinition(ThingDefinition):
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


class RegionDefinition(ThingDefinition):
    """State, province, or administrative region within a country.
    
    Represents sub-national geographic divisions (states, provinces, territories).
    """
    kind: str = "region_definition"
    
    code: str  # Region code (e.g., "CA", "ON")
    country_code: str  # Links to CountryDefinition
    region_type: str  # "state", "province", "territory", "county"
    capital: Optional[str] = None
    abbreviation: Optional[str] = None


class MetropolitanAreaDefinition(ThingDefinition):
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


class NAICSIndustryDefinition(ThingDefinition):
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
    
    Inherits all value chain characteristics and adds process-specific fields.
    """
    kind: str = "business_process_definition"
    
    # Process-specific fields:
    code: str
    process_type: str  # "core", "support", "management"
    performed_by_actors: List[str] = []  # ActorDefinition codes
    uses_entities: List[str] = []  # EntityDefinition codes
    produces_event_types: List[str] = []  # Event entity codes
    
    # Override domain to be "process"
    domain: str = "process"  # Low-level granularity


class StrategicObjectiveDefinition(ThingDefinition):
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


class BenchmarkDefinition(ThingDefinition):
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


class ExternalEventDefinition(ThingDefinition):
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


class AnalyticsStrategyDefinition(ThingDefinition):
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


class DataSourceDefinition(ThingDefinition):
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


class DataProductDefinition(ThingDefinition):
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


class AnalyticsUseCaseDefinition(ThingDefinition):
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


class DimensionDefinition(ThingDefinition):
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


class MetricCategoryDefinition(ThingDefinition):
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


class DataQualityRuleDefinition(ThingDefinition):
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


class ConstraintDefinition(ThingDefinition):
    kind: str = "constraint_definition"

    target_kind: str  # e.g., entity_definition, value_chain_pattern_definition
    expression: Dict[str, Any]  # shape/validation expression


class DesignPolicyRuleDefinition(BaseModel):
    id: str
    when: Dict[str, Any]
    then: Dict[str, Any]
    and_: Optional[Dict[str, Any]] = None


class DesignPolicyDefinition(ThingDefinition):
    kind: str = "design_policy_definition"

    scope: str = "global"
    version: Optional[str] = None
    rules: List[DesignPolicyRuleDefinition] = []


# ---------------------------------------------------------------------------
# Conversation / intent layer
# ---------------------------------------------------------------------------


class InterviewSessionDefinition(ThingDefinition):
    kind: str = "interview_session_definition"

    company_id: Optional[str] = None
    industry_codes: List[str] = []
    participants: List[str] = []
    started_at: Optional[str] = None
    ended_at: Optional[str] = None


class UtteranceDefinition(ThingDefinition):
    kind: str = "utterance_definition"

    session_id: str
    speaker: str
    timestamp: Optional[str] = None
    raw_text: str
    nlp_annotations: Dict[str, Any] = {}


class BusinessIntentDefinition(ThingDefinition):
    kind: str = "business_intent_definition"

    session_id: str
    intent_type: str
    target_concepts: List[str] = []
    priority: Optional[str] = None
    confidence_score: Optional[float] = None
    source_utterances: List[str] = []


class PatternMatchDefinition(ThingDefinition):
    kind: str = "pattern_match_definition"

    session_id: str
    pattern_id: str
    matched_entities: Dict[str, str] = {}
    confidence_score: Optional[float] = None
    supporting_intents: List[str] = []


class DesignSuggestionDefinition(ThingDefinition):
    kind: str = "design_suggestion_definition"

    session_id: str
    suggested_changes: Dict[str, Any]
    status: str = "proposed"  # proposed | accepted | rejected
    rationale: Optional[str] = None


__all__ = [
    "ThingDefinition",
    "ColumnDefinition",
    "TableSchemaDefinition",
    "EntityDefinition",
    "RelationshipDefinition",
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
]
