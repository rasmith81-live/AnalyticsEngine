"""
Pydantic Schemas for Analytics Models

API request/response models following CQRS pattern for the analytics hierarchy.
"""

from datetime import datetime
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field, ConfigDict


# ============================================================================
# Industry Schemas
# ============================================================================

class IndustryBase(BaseModel):
    """Base schema for Industry."""
    name: str = Field(..., min_length=1, max_length=255, description="Industry name")
    code: str = Field(..., min_length=1, max_length=50, description="Unique industry code")
    description: Optional[str] = Field(None, description="Industry description")
    is_active: bool = Field(True, description="Whether the industry is active")
    metadata_: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class IndustryCreate(IndustryBase):
    """Schema for creating an Industry."""
    pass


class IndustryUpdate(BaseModel):
    """Schema for updating an Industry."""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = None
    is_active: Optional[bool] = None
    metadata_: Optional[Dict[str, Any]] = None


class IndustryRead(IndustryBase):
    """Schema for reading an Industry."""
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class IndustryWithValueChains(IndustryRead):
    """Schema for Industry with nested value chains."""
    value_chains: List["ValueChainRead"] = Field(default_factory=list)
    
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# ValueChain Schemas
# ============================================================================

class ValueChainBase(BaseModel):
    """Base schema for ValueChain."""
    name: str = Field(..., min_length=1, max_length=255, description="Value chain name")
    code: str = Field(..., min_length=1, max_length=50, description="Unique value chain code")
    description: Optional[str] = Field(None, description="Value chain description")
    is_active: bool = Field(True, description="Whether the value chain is active")
    display_order: int = Field(0, ge=0, description="Display order for sorting")
    metadata_: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class ValueChainCreate(ValueChainBase):
    """Schema for creating a ValueChain."""
    industry_ids: List[int] = Field(default_factory=list, description="IDs of industries to associate with")


class ValueChainUpdate(BaseModel):
    """Schema for updating a ValueChain."""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = None
    is_active: Optional[bool] = None
    display_order: Optional[int] = Field(None, ge=0)
    metadata_: Optional[Dict[str, Any]] = None


class ValueChainRead(ValueChainBase):
    """Schema for reading a ValueChain."""
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class ValueChainWithModules(ValueChainRead):
    """Schema for ValueChain with nested modules."""
    modules: List["ModuleRead"] = Field(default_factory=list)
    
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# Module Schemas
# ============================================================================

class ModuleBase(BaseModel):
    """Base schema for Module."""
    name: str = Field(..., min_length=1, max_length=255, description="Module name")
    code: str = Field(..., min_length=1, max_length=50, description="Unique module code")
    description: Optional[str] = Field(None, description="Module description")
    is_active: bool = Field(True, description="Whether the module is active")
    display_order: int = Field(0, ge=0, description="Display order for sorting")
    metadata_: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class ModuleCreate(ModuleBase):
    """Schema for creating a Module."""
    value_chain_ids: List[int] = Field(default_factory=list, description="IDs of value chains to associate with")


class ModuleUpdate(BaseModel):
    """Schema for updating a Module."""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = None
    is_active: Optional[bool] = None
    display_order: Optional[int] = Field(None, ge=0)
    metadata_: Optional[Dict[str, Any]] = None
    industry_ids: Optional[List[int]] = Field(None, description="IDs of industries to associate with")


class ModuleRead(ModuleBase):
    """Schema for reading a Module."""
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class ModuleWithObjectModels(ModuleRead):
    """Schema for Module with nested object models."""
    object_models: List["ObjectModelRead"] = Field(default_factory=list)
    
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# ObjectModel Schemas
# ============================================================================

class ObjectModelBase(BaseModel):
    """Base schema for ObjectModel."""
    name: str = Field(..., min_length=1, max_length=255, description="Object model name")
    code: str = Field(..., min_length=1, max_length=50, description="Unique object model code")
    description: Optional[str] = Field(None, description="Object model description")
    is_active: bool = Field(True, description="Whether the object model is active")
    display_order: int = Field(0, ge=0, description="Display order for sorting")
    schema_definition: Optional[Dict[str, Any]] = Field(None, description="Schema definition for objects")
    metadata_: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class ObjectModelCreate(ObjectModelBase):
    """Schema for creating an ObjectModel."""
    module_ids: List[int] = Field(default_factory=list, description="IDs of modules to associate with")


class ObjectModelUpdate(BaseModel):
    """Schema for updating an ObjectModel."""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = None
    is_active: Optional[bool] = None
    display_order: Optional[int] = Field(None, ge=0)
    schema_definition: Optional[Dict[str, Any]] = None
    metadata_: Optional[Dict[str, Any]] = None
    module_ids: Optional[List[int]] = Field(None, description="IDs of modules to associate with")


class ObjectModelRead(ObjectModelBase):
    """Schema for reading an ObjectModel."""
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class ObjectModelWithDetails(ObjectModelRead):
    """Schema for ObjectModel with nested objects and KPIs."""
    objects: List["ObjectRead"] = Field(default_factory=list)
    kpis: List["KPIRead"] = Field(default_factory=list)
    
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# ObjectAttribute Schemas
# ============================================================================

class ObjectAttributeBase(BaseModel):
    """Base schema for ObjectAttribute."""
    name: str = Field(..., min_length=1, max_length=255, description="Attribute name")
    code: str = Field(..., min_length=1, max_length=50, description="Unique attribute code")
    description: Optional[str] = Field(None, description="Attribute description")
    data_type: str = Field(..., description="Data type: string, integer, float, boolean, date, datetime, json")
    is_required: bool = Field(False, description="Whether the attribute is required")
    is_active: bool = Field(True, description="Whether the attribute is active")
    default_value: Optional[str] = Field(None, description="Default value for the attribute")
    validation_rules: Optional[Dict[str, Any]] = Field(None, description="Validation rules")
    display_order: int = Field(0, ge=0, description="Display order for sorting")
    metadata_: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class ObjectAttributeCreate(ObjectAttributeBase):
    """Schema for creating an ObjectAttribute."""
    object_model_id: int = Field(..., gt=0, description="ID of the parent object model")


class ObjectAttributeUpdate(BaseModel):
    """Schema for updating an ObjectAttribute."""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = None
    data_type: Optional[str] = None
    is_required: Optional[bool] = None
    is_active: Optional[bool] = None
    default_value: Optional[str] = None
    validation_rules: Optional[Dict[str, Any]] = None
    display_order: Optional[int] = Field(None, ge=0)
    metadata_: Optional[Dict[str, Any]] = None


class ObjectAttributeRead(ObjectAttributeBase):
    """Schema for reading an ObjectAttribute."""
    id: int
    object_model_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# Object Schemas
# ============================================================================

class ObjectBase(BaseModel):
    """Base schema for Object."""
    name: str = Field(..., min_length=1, max_length=255, description="Object name")
    code: str = Field(..., min_length=1, max_length=50, description="Unique object code")
    description: Optional[str] = Field(None, description="Object description")
    is_active: bool = Field(True, description="Whether the object is active")
    data_values: Optional[Dict[str, Any]] = Field(None, description="Object data values")
    metadata_: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class ObjectCreate(ObjectBase):
    """Schema for creating an Object."""
    object_model_ids: List[int] = Field(default_factory=list, description="IDs of object models to associate with")


class ObjectUpdate(BaseModel):
    """Schema for updating an Object."""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = None
    is_active: Optional[bool] = None
    data_values: Optional[Dict[str, Any]] = None
    metadata_: Optional[Dict[str, Any]] = None
    object_model_ids: Optional[List[int]] = Field(None, description="IDs of object models to associate with")


class ObjectRead(ObjectBase):
    """Schema for reading an Object."""
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# KPI Schemas
# ============================================================================

class KPIBase(BaseModel):
    """Base schema for KPI with comprehensive definition and tracking fields."""
    # Core Identification
    name: str = Field(..., min_length=1, max_length=255, description="KPI name")
    code: str = Field(..., min_length=1, max_length=50, description="Unique KPI code")
    description: Optional[str] = Field(None, description="KPI description")
    is_active: bool = Field(True, description="Whether the KPI is active")
    
    # KPI Definition & Context
    kpi_definition: Optional[str] = Field(None, description="Clear explanation of what the KPI measures")
    expected_business_insights: Optional[str] = Field(None, description="Typical business insights expected from tracking this KPI")
    measurement_approach: Optional[str] = Field(None, description="Outline of the approach or process followed to measure this KPI")
    
    # Calculation & Measurement
    formula: Optional[str] = Field(None, description="Standard formula used to calculate this KPI")
    calculation_formula: Optional[str] = Field(None, description="Detailed calculation formula with explicit object attribute references")
    attribute_references: Optional[Dict[str, str]] = Field(None, description="Object attribute codes referenced in the formula")
    unit_of_measure: Optional[str] = Field(None, max_length=50, description="Unit of measure")
    
    # Target Values & Thresholds
    target_value: Optional[float] = Field(None, description="Target value for the KPI")
    current_value: Optional[float] = Field(None, description="Current value of the KPI")
    threshold_warning: Optional[float] = Field(None, description="Warning threshold")
    threshold_critical: Optional[float] = Field(None, description="Critical threshold")
    
    # Analysis & Insights
    trend_analysis: Optional[str] = Field(None, description="Insights into how the KPI evolves over time and what trends indicate")
    diagnostic_questions: Optional[Dict[str, Any]] = Field(None, description="Questions to ask to understand current position and improvement opportunities")
    actionable_steps: Optional[Dict[str, Any]] = Field(None, description="Practical tips for improving the KPI (operational, strategic, tactical)")
    
    # Visualization & Reporting
    visualization_suggestions: Optional[Dict[str, Any]] = Field(None, description="Recommended charts/graphs for representing KPI trends and patterns")
    risk_warnings: Optional[Dict[str, Any]] = Field(None, description="Potential risks or warning signs requiring immediate attention")
    
    # Tools & Integration
    suggested_tracking_tools: Optional[Dict[str, Any]] = Field(None, description="Tools, technologies, and software for tracking and analyzing the KPI")
    integration_points: Optional[Dict[str, Any]] = Field(None, description="How the KPI integrates with other business systems and processes")
    
    # Impact & Relationships
    change_impact: Optional[str] = Field(None, description="How changes in this KPI impact other KPIs and expected changes")
    source: Optional[str] = Field(None, max_length=500, description="Source reference or parent KPI this was derived from")
    parent_kpi_id: Optional[int] = Field(None, gt=0, description="Reference to parent KPI if this is a derived/custom KPI")
    
    # Display and Categorization
    display_order: int = Field(0, ge=0, description="Display order for sorting")
    category: Optional[str] = Field(None, max_length=100, description="KPI category")
    
    # Metadata
    metadata_: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class KPICreate(KPIBase):
    """Schema for creating a KPI."""
    object_model_ids: List[int] = Field(default_factory=list, description="IDs of object models to associate with")


class KPIUpdate(BaseModel):
    """Schema for updating a KPI."""
    # Core Identification
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = None
    is_active: Optional[bool] = None
    
    # KPI Definition & Context
    kpi_definition: Optional[str] = None
    expected_business_insights: Optional[str] = None
    measurement_approach: Optional[str] = None
    
    # Calculation & Measurement
    formula: Optional[str] = None
    calculation_formula: Optional[str] = None
    attribute_references: Optional[Dict[str, str]] = None
    unit_of_measure: Optional[str] = Field(None, max_length=50)
    
    # Target Values & Thresholds
    target_value: Optional[float] = None
    current_value: Optional[float] = None
    threshold_warning: Optional[float] = None
    threshold_critical: Optional[float] = None
    
    # Analysis & Insights
    trend_analysis: Optional[str] = None
    diagnostic_questions: Optional[Dict[str, Any]] = None
    actionable_steps: Optional[Dict[str, Any]] = None
    
    # Visualization & Reporting
    visualization_suggestions: Optional[Dict[str, Any]] = None
    risk_warnings: Optional[Dict[str, Any]] = None
    
    # Tools & Integration
    suggested_tracking_tools: Optional[Dict[str, Any]] = None
    integration_points: Optional[Dict[str, Any]] = None
    
    # Impact & Relationships
    change_impact: Optional[str] = None
    source: Optional[str] = Field(None, max_length=500)
    parent_kpi_id: Optional[int] = Field(None, gt=0)
    
    # Display and Categorization
    display_order: Optional[int] = Field(None, ge=0)
    category: Optional[str] = Field(None, max_length=100)
    
    # Metadata
    metadata_: Optional[Dict[str, Any]] = None
    object_model_ids: Optional[List[int]] = Field(None, description="IDs of object models to associate with")


class KPIRead(KPIBase):
    """Schema for reading a KPI."""
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class KPIWithStatus(KPIRead):
    """Schema for KPI with calculated status."""
    status: str = Field(..., description="Current status (normal, warning, critical)")
    variance: Optional[float] = Field(None, description="Variance from target")
    variance_percentage: Optional[float] = Field(None, description="Variance percentage from target")
    
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# Benchmark Schemas
# ============================================================================

class BenchmarkBase(BaseModel):
    """Base schema for Benchmark with comprehensive citation and context."""
    # Core Identification
    name: str = Field(..., min_length=1, max_length=255, description="Benchmark name")
    code: str = Field(..., min_length=1, max_length=50, description="Unique benchmark code")
    description: Optional[str] = Field(None, description="Detailed description")
    is_active: bool = Field(True, description="Whether benchmark is active")
    
    # Exact Metric Information
    metric_value: Optional[float] = Field(None, description="Benchmark value (numeric)")
    metric_value_text: Optional[str] = Field(None, max_length=255, description="Text representation of value")
    metric_unit: Optional[str] = Field(None, max_length=100, description="Unit of measure (%, $, seconds, etc.)")
    statistic_type: Optional[str] = Field(None, max_length=50, description="mean, median, percentile, range, etc.")
    percentile: Optional[int] = Field(None, ge=0, le=100, description="Percentile value (0-100)")
    value_min: Optional[float] = Field(None, description="Minimum value in range")
    value_max: Optional[float] = Field(None, description="Maximum value in range")
    
    # Metric Definition & Attributes
    metric_definition: Optional[str] = Field(None, description="How the metric is defined")
    metric_normalization: Optional[str] = Field(None, description="How the metric is normalized")
    metric_filters: Optional[Dict[str, Any]] = Field(None, description="Filters applied to the metric")
    cohort_rules: Optional[Dict[str, Any]] = Field(None, description="Cohort or segment rules")
    
    # Company Size
    company_size: Optional[str] = Field(None, max_length=100, description="Company size category")
    company_size_min: Optional[int] = Field(None, ge=0, description="Minimum company size")
    company_size_max: Optional[int] = Field(None, ge=0, description="Maximum company size")
    company_size_metric: Optional[str] = Field(None, max_length=50, description="employees, revenue, etc.")
    
    # Time Period
    time_period: Optional[str] = Field(None, max_length=255, description="Time period as reported")
    time_period_start: Optional[datetime] = Field(None, description="Start date of time period")
    time_period_end: Optional[datetime] = Field(None, description="End date of time period")
    
    # Population
    population: Optional[str] = Field(None, max_length=255, description="What was measured")
    population_size: Optional[int] = Field(None, ge=0, description="Size of population measured")
    
    # Industry
    industry: Optional[str] = Field(None, max_length=255, description="Industry or sector")
    industry_tags: Optional[Dict[str, Any]] = Field(None, description="Array of industry tags")
    
    # Geography
    geography: Optional[str] = Field(None, max_length=255, description="Geographic scope")
    country: Optional[str] = Field(None, max_length=100, description="Specific country")
    region: Optional[str] = Field(None, max_length=100, description="Region")
    
    # Sample Size
    sample_size: Optional[int] = Field(None, ge=0, description="Number of observations")
    sample_description: Optional[str] = Field(None, description="Description of the sample")
    
    # Source Details & Citation
    source_publisher: Optional[str] = Field(None, max_length=255, description="Publisher or organization")
    source_author: Optional[str] = Field(None, max_length=255, description="Author(s)")
    source_title: Optional[str] = Field(None, max_length=500, description="Title of report/study")
    source_year: Optional[int] = Field(None, ge=1900, le=2100, description="Publication year")
    source_date: Optional[datetime] = Field(None, description="Exact publication date")
    source_excerpt: Optional[str] = Field(None, description="Relevant excerpt from source")
    source_url: Optional[str] = Field(None, max_length=1000, description="URL to source")
    source_download_url: Optional[str] = Field(None, max_length=1000, description="Download URL")
    source_doi: Optional[str] = Field(None, max_length=255, description="Digital Object Identifier")
    source_type: Optional[str] = Field(None, max_length=100, description="research_report, whitepaper, etc.")
    source_credibility: Optional[str] = Field(None, max_length=50, description="high, medium, low")
    
    # Methodology & Comments
    methodology_notes: Optional[str] = Field(None, description="Research methodology notes")
    caveats: Optional[str] = Field(None, description="Important caveats or limitations")
    special_coverage: Optional[str] = Field(None, description="Special coverage areas")
    comments: Optional[str] = Field(None, description="Additional comments")
    
    # Quality & Validation
    confidence_level: Optional[str] = Field(None, max_length=50, description="high, medium, low")
    data_quality_score: Optional[int] = Field(None, ge=0, le=100, description="Quality score (0-100)")
    last_verified_at: Optional[datetime] = Field(None, description="Last verification date")
    verified_by: Optional[str] = Field(None, max_length=255, description="Who verified")
    
    # Categorization & Display
    benchmark_category: Optional[str] = Field(None, max_length=100, description="Category")
    display_order: int = Field(0, ge=0, description="Display order")
    is_featured: bool = Field(False, description="Feature prominently")
    
    # Metadata
    tags: Optional[Dict[str, Any]] = Field(None, description="Tags for categorization")
    metadata_: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class BenchmarkCreate(BenchmarkBase):
    """Schema for creating a Benchmark."""
    kpi_id: int = Field(..., gt=0, description="KPI ID this benchmark applies to")


class BenchmarkUpdate(BaseModel):
    """Schema for updating a Benchmark."""
    # Core Identification
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = None
    is_active: Optional[bool] = None
    
    # Exact Metric Information
    metric_value: Optional[float] = None
    metric_value_text: Optional[str] = Field(None, max_length=255)
    metric_unit: Optional[str] = Field(None, max_length=100)
    statistic_type: Optional[str] = Field(None, max_length=50)
    percentile: Optional[int] = Field(None, ge=0, le=100)
    value_min: Optional[float] = None
    value_max: Optional[float] = None
    
    # Metric Definition & Attributes
    metric_definition: Optional[str] = None
    metric_normalization: Optional[str] = None
    metric_filters: Optional[Dict[str, Any]] = None
    cohort_rules: Optional[Dict[str, Any]] = None
    
    # Company Size
    company_size: Optional[str] = Field(None, max_length=100)
    company_size_min: Optional[int] = Field(None, ge=0)
    company_size_max: Optional[int] = Field(None, ge=0)
    company_size_metric: Optional[str] = Field(None, max_length=50)
    
    # Time Period
    time_period: Optional[str] = Field(None, max_length=255)
    time_period_start: Optional[datetime] = None
    time_period_end: Optional[datetime] = None
    
    # Population
    population: Optional[str] = Field(None, max_length=255)
    population_size: Optional[int] = Field(None, ge=0)
    
    # Industry
    industry: Optional[str] = Field(None, max_length=255)
    industry_tags: Optional[Dict[str, Any]] = None
    
    # Geography
    geography: Optional[str] = Field(None, max_length=255)
    country: Optional[str] = Field(None, max_length=100)
    region: Optional[str] = Field(None, max_length=100)
    
    # Sample Size
    sample_size: Optional[int] = Field(None, ge=0)
    sample_description: Optional[str] = None
    
    # Source Details & Citation
    source_publisher: Optional[str] = Field(None, max_length=255)
    source_author: Optional[str] = Field(None, max_length=255)
    source_title: Optional[str] = Field(None, max_length=500)
    source_year: Optional[int] = Field(None, ge=1900, le=2100)
    source_date: Optional[datetime] = None
    source_excerpt: Optional[str] = None
    source_url: Optional[str] = Field(None, max_length=1000)
    source_download_url: Optional[str] = Field(None, max_length=1000)
    source_doi: Optional[str] = Field(None, max_length=255)
    source_type: Optional[str] = Field(None, max_length=100)
    source_credibility: Optional[str] = Field(None, max_length=50)
    
    # Methodology & Comments
    methodology_notes: Optional[str] = None
    caveats: Optional[str] = None
    special_coverage: Optional[str] = None
    comments: Optional[str] = None
    
    # Quality & Validation
    confidence_level: Optional[str] = Field(None, max_length=50)
    data_quality_score: Optional[int] = Field(None, ge=0, le=100)
    last_verified_at: Optional[datetime] = None
    verified_by: Optional[str] = Field(None, max_length=255)
    
    # Categorization & Display
    benchmark_category: Optional[str] = Field(None, max_length=100)
    display_order: Optional[int] = Field(None, ge=0)
    is_featured: Optional[bool] = None
    
    # Metadata
    tags: Optional[Dict[str, Any]] = None
    metadata_: Optional[Dict[str, Any]] = None


class BenchmarkRead(BenchmarkBase):
    """Schema for reading a Benchmark."""
    id: int
    kpi_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# Hierarchy Schemas
# ============================================================================

class FullHierarchy(IndustryRead):
    """Complete hierarchy from Industry down to Objects and KPIs."""
    modules: List[ModuleWithObjectModels] = Field(default_factory=list)
    
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# Command and Query Schemas (CQRS Pattern)
# ============================================================================

class CreateIndustryCommand(BaseModel):
    """Command to create an industry."""
    industry: IndustryCreate
    command_id: str = Field(..., description="Unique command identifier")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class UpdateIndustryCommand(BaseModel):
    """Command to update an industry."""
    industry_id: int
    updates: IndustryUpdate
    command_id: str = Field(..., description="Unique command identifier")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class GetIndustryQuery(BaseModel):
    """Query to get an industry."""
    industry_id: Optional[int] = None
    code: Optional[str] = None
    include_modules: bool = False
    query_id: str = Field(..., description="Unique query identifier")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ListIndustriesQuery(BaseModel):
    """Query to list industries."""
    is_active: Optional[bool] = None
    skip: int = Field(0, ge=0)
    limit: int = Field(100, ge=1, le=1000)
    query_id: str = Field(..., description="Unique query identifier")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


# ============================================================================
# Geography Schemas
# ============================================================================

class CountryBase(BaseModel):
    """Base schema for Country."""
    name: str = Field(..., min_length=1, max_length=255, description="Country name")
    code: str = Field(..., min_length=1, max_length=10, description="Country code")
    iso_alpha2: Optional[str] = Field(None, max_length=2, description="ISO 3166-1 alpha-2 code")
    iso_alpha3: Optional[str] = Field(None, max_length=3, description="ISO 3166-1 alpha-3 code")
    iso_numeric: Optional[str] = Field(None, max_length=3, description="ISO 3166-1 numeric code")
    capital: Optional[str] = Field(None, max_length=255, description="Capital city")
    currency_code: Optional[str] = Field(None, max_length=3, description="ISO 4217 currency code")
    currency_name: Optional[str] = Field(None, max_length=100, description="Currency name")
    phone_code: Optional[str] = Field(None, max_length=20, description="International dialing code")
    is_active: bool = Field(True, description="Whether country is active")
    metadata_: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class CountryCreate(CountryBase):
    """Schema for creating a Country."""
    pass


class CountryUpdate(BaseModel):
    """Schema for updating a Country."""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    code: Optional[str] = Field(None, min_length=1, max_length=10)
    iso_alpha2: Optional[str] = Field(None, max_length=2)
    iso_alpha3: Optional[str] = Field(None, max_length=3)
    iso_numeric: Optional[str] = Field(None, max_length=3)
    capital: Optional[str] = Field(None, max_length=255)
    currency_code: Optional[str] = Field(None, max_length=3)
    currency_name: Optional[str] = Field(None, max_length=100)
    phone_code: Optional[str] = Field(None, max_length=20)
    is_active: Optional[bool] = None
    metadata_: Optional[Dict[str, Any]] = None


class CountryRead(CountryBase):
    """Schema for reading a Country."""
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class RegionBase(BaseModel):
    """Base schema for Region."""
    name: str = Field(..., min_length=1, max_length=255, description="Region name")
    code: str = Field(..., min_length=1, max_length=50, description="Region code")
    region_type: Optional[str] = Field(None, max_length=50, description="Type: state, province, etc.")
    capital: Optional[str] = Field(None, max_length=255, description="Capital city")
    abbreviation: Optional[str] = Field(None, max_length=10, description="Common abbreviation")
    is_active: bool = Field(True, description="Whether region is active")
    metadata_: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class RegionCreate(RegionBase):
    """Schema for creating a Region."""
    country_id: int = Field(..., gt=0, description="Country ID")


class RegionUpdate(BaseModel):
    """Schema for updating a Region."""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    region_type: Optional[str] = Field(None, max_length=50)
    capital: Optional[str] = Field(None, max_length=255)
    abbreviation: Optional[str] = Field(None, max_length=10)
    is_active: Optional[bool] = None
    metadata_: Optional[Dict[str, Any]] = None


class RegionRead(RegionBase):
    """Schema for reading a Region."""
    id: int
    country_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class MetropolitanStatisticalAreaBase(BaseModel):
    """Base schema for MetropolitanStatisticalArea."""
    name: str = Field(..., min_length=1, max_length=255, description="MSA name")
    code: str = Field(..., min_length=1, max_length=50, description="MSA code")
    cbsa_code: Optional[str] = Field(None, max_length=10, description="CBSA code")
    msa_type: Optional[str] = Field(None, max_length=50, description="Type: metropolitan, micropolitan")
    population: Optional[int] = Field(None, ge=0, description="Population estimate")
    population_year: Optional[int] = Field(None, ge=1900, le=2100, description="Year of estimate")
    central_city: Optional[str] = Field(None, max_length=255, description="Primary central city")
    counties: Optional[Dict[str, Any]] = Field(None, description="Array of counties")
    is_active: bool = Field(True, description="Whether MSA is active")
    metadata_: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class MetropolitanStatisticalAreaCreate(MetropolitanStatisticalAreaBase):
    """Schema for creating a MetropolitanStatisticalArea."""
    region_id: int = Field(..., gt=0, description="Region ID")


class MetropolitanStatisticalAreaUpdate(BaseModel):
    """Schema for updating a MetropolitanStatisticalArea."""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    cbsa_code: Optional[str] = Field(None, max_length=10)
    msa_type: Optional[str] = Field(None, max_length=50)
    population: Optional[int] = Field(None, ge=0)
    population_year: Optional[int] = Field(None, ge=1900, le=2100)
    central_city: Optional[str] = Field(None, max_length=255)
    counties: Optional[Dict[str, Any]] = None
    is_active: Optional[bool] = None
    metadata_: Optional[Dict[str, Any]] = None


class MetropolitanStatisticalAreaRead(MetropolitanStatisticalAreaBase):
    """Schema for reading a MetropolitanStatisticalArea."""
    id: int
    region_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# Client & Authorization Schemas
# ============================================================================

class ClientBase(BaseModel):
    """Base schema for Client."""
    name: str = Field(..., min_length=1, max_length=255, description="Client name")
    code: str = Field(..., min_length=1, max_length=50, description="Unique client code")
    description: Optional[str] = Field(None, description="Client description")
    is_active: bool = Field(True, description="Whether the client is active")
    
    # NAICS Industry Classification
    naics_code: Optional[str] = Field(None, max_length=10, description="NAICS code")
    naics_title: Optional[str] = Field(None, max_length=255, description="NAICS industry title")
    naics_sector: Optional[str] = Field(None, max_length=100, description="NAICS sector")
    naics_subsector: Optional[str] = Field(None, max_length=100, description="NAICS subsector")
    
    # Geography
    country_id: Optional[int] = Field(None, gt=0, description="Country ID")
    region_id: Optional[int] = Field(None, gt=0, description="Region ID")
    metropolitan_area_id: Optional[int] = Field(None, gt=0, description="Metropolitan Area ID")
    
    config: Optional[Dict[str, Any]] = Field(None, description="Client-specific configuration")
    contact_email: Optional[str] = Field(None, max_length=255, description="Contact email")
    contact_phone: Optional[str] = Field(None, max_length=50, description="Contact phone")
    metadata_: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class ClientCreate(ClientBase):
    """Schema for creating a Client."""
    pass


class ClientUpdate(BaseModel):
    """Schema for updating a Client."""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = None
    is_active: Optional[bool] = None
    
    # NAICS Industry Classification
    naics_code: Optional[str] = Field(None, max_length=10)
    naics_title: Optional[str] = Field(None, max_length=255)
    naics_sector: Optional[str] = Field(None, max_length=100)
    naics_subsector: Optional[str] = Field(None, max_length=100)
    
    # Geography
    country_id: Optional[int] = Field(None, gt=0)
    region_id: Optional[int] = Field(None, gt=0)
    metropolitan_area_id: Optional[int] = Field(None, gt=0)
    
    config: Optional[Dict[str, Any]] = None
    contact_email: Optional[str] = Field(None, max_length=255)
    contact_phone: Optional[str] = Field(None, max_length=50)
    metadata_: Optional[Dict[str, Any]] = None


class ClientRead(ClientBase):
    """Schema for reading a Client."""
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# ClientRole Schemas
# ============================================================================

class ClientRoleBase(BaseModel):
    """Base schema for ClientRole."""
    name: str = Field(..., min_length=1, max_length=255, description="Role name")
    code: str = Field(..., min_length=1, max_length=50, description="Unique role code")
    description: Optional[str] = Field(None, description="Role description")
    is_active: bool = Field(True, description="Whether the role is active")
    permissions: Optional[Dict[str, Any]] = Field(None, description="Role-specific permissions")
    metadata_: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")


class ClientRoleCreate(ClientRoleBase):
    """Schema for creating a ClientRole."""
    client_id: int = Field(..., gt=0, description="ID of the parent client")


class ClientRoleUpdate(BaseModel):
    """Schema for updating a ClientRole."""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = None
    is_active: Optional[bool] = None
    permissions: Optional[Dict[str, Any]] = None
    metadata_: Optional[Dict[str, Any]] = None


class ClientRoleRead(ClientRoleBase):
    """Schema for reading a ClientRole."""
    id: int
    client_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# Permission Schemas
# ============================================================================

class ClientModulePermissionBase(BaseModel):
    """Base schema for ClientModulePermission."""
    can_view: bool = Field(True, description="Can view module")
    can_create: bool = Field(False, description="Can create in module")
    can_update: bool = Field(False, description="Can update in module")
    can_delete: bool = Field(False, description="Can delete in module")
    config: Optional[Dict[str, Any]] = Field(None, description="Module-specific configuration")


class ClientModulePermissionCreate(ClientModulePermissionBase):
    """Schema for creating a ClientModulePermission."""
    client_id: int = Field(..., gt=0, description="Client ID")
    module_id: int = Field(..., gt=0, description="Module ID")


class ClientModulePermissionUpdate(BaseModel):
    """Schema for updating a ClientModulePermission."""
    can_view: Optional[bool] = None
    can_create: Optional[bool] = None
    can_update: Optional[bool] = None
    can_delete: Optional[bool] = None
    config: Optional[Dict[str, Any]] = None


class ClientModulePermissionRead(ClientModulePermissionBase):
    """Schema for reading a ClientModulePermission."""
    id: int
    client_id: int
    module_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class RoleObjectModelPermissionBase(BaseModel):
    """Base schema for RoleObjectModelPermission."""
    can_view: bool = Field(True, description="Can view object model")
    can_create: bool = Field(False, description="Can create objects")
    can_update: bool = Field(False, description="Can update objects")
    can_delete: bool = Field(False, description="Can delete objects")
    config: Optional[Dict[str, Any]] = Field(None, description="ObjectModel-specific configuration")


class RoleObjectModelPermissionCreate(RoleObjectModelPermissionBase):
    """Schema for creating a RoleObjectModelPermission."""
    role_id: int = Field(..., gt=0, description="Role ID")
    object_model_id: int = Field(..., gt=0, description="ObjectModel ID")


class RoleObjectModelPermissionUpdate(BaseModel):
    """Schema for updating a RoleObjectModelPermission."""
    can_view: Optional[bool] = None
    can_create: Optional[bool] = None
    can_update: Optional[bool] = None
    can_delete: Optional[bool] = None
    config: Optional[Dict[str, Any]] = None


class RoleObjectModelPermissionRead(RoleObjectModelPermissionBase):
    """Schema for reading a RoleObjectModelPermission."""
    id: int
    role_id: int
    object_model_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class RoleObjectPermissionBase(BaseModel):
    """Base schema for RoleObjectPermission."""
    can_view: bool = Field(True, description="Can view object")
    can_update: bool = Field(False, description="Can update object")
    can_delete: bool = Field(False, description="Can delete object")
    row_filter: Optional[Dict[str, Any]] = Field(None, description="Row-level security filter")
    config: Optional[Dict[str, Any]] = Field(None, description="Object-specific configuration")


class RoleObjectPermissionCreate(RoleObjectPermissionBase):
    """Schema for creating a RoleObjectPermission."""
    role_id: int = Field(..., gt=0, description="Role ID")
    object_id: int = Field(..., gt=0, description="Object ID")


class RoleObjectPermissionUpdate(BaseModel):
    """Schema for updating a RoleObjectPermission."""
    can_view: Optional[bool] = None
    can_update: Optional[bool] = None
    can_delete: Optional[bool] = None
    row_filter: Optional[Dict[str, Any]] = None
    config: Optional[Dict[str, Any]] = None


class RoleObjectPermissionRead(RoleObjectPermissionBase):
    """Schema for reading a RoleObjectPermission."""
    id: int
    role_id: int
    object_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class RoleKPIPermissionBase(BaseModel):
    """Base schema for RoleKPIPermission."""
    can_view: bool = Field(True, description="Can view KPI")
    can_update: bool = Field(False, description="Can update KPI")
    config: Optional[Dict[str, Any]] = Field(None, description="KPI-specific configuration")


class RoleKPIPermissionCreate(RoleKPIPermissionBase):
    """Schema for creating a RoleKPIPermission."""
    role_id: int = Field(..., gt=0, description="Role ID")
    kpi_id: int = Field(..., gt=0, description="KPI ID")


class RoleKPIPermissionUpdate(BaseModel):
    """Schema for updating a RoleKPIPermission."""
    can_view: Optional[bool] = None
    can_update: Optional[bool] = None
    config: Optional[Dict[str, Any]] = None


class RoleKPIPermissionRead(RoleKPIPermissionBase):
    """Schema for reading a RoleKPIPermission."""
    id: int
    role_id: int
    kpi_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class RoleAttributePermissionBase(BaseModel):
    """Base schema for RoleAttributePermission."""
    can_view: bool = Field(True, description="Can view attribute")
    can_update: bool = Field(False, description="Can update attribute")
    is_masked: bool = Field(False, description="Whether to mask the attribute value")
    mask_type: Optional[str] = Field(None, max_length=50, description="Masking type: partial, full, hash, encrypt")
    config: Optional[Dict[str, Any]] = Field(None, description="Attribute-specific configuration")


class RoleAttributePermissionCreate(RoleAttributePermissionBase):
    """Schema for creating a RoleAttributePermission."""
    role_id: int = Field(..., gt=0, description="Role ID")
    attribute_id: int = Field(..., gt=0, description="Attribute ID")


class RoleAttributePermissionUpdate(BaseModel):
    """Schema for updating a RoleAttributePermission."""
    can_view: Optional[bool] = None
    can_update: Optional[bool] = None
    is_masked: Optional[bool] = None
    mask_type: Optional[str] = Field(None, max_length=50)
    config: Optional[Dict[str, Any]] = None


class RoleAttributePermissionRead(RoleAttributePermissionBase):
    """Schema for reading a RoleAttributePermission."""
    id: int
    role_id: int
    attribute_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# Update forward references
IndustryWithModules.model_rebuild()
ModuleWithObjectModels.model_rebuild()
ObjectModelWithDetails.model_rebuild()
FullHierarchy.model_rebuild()
