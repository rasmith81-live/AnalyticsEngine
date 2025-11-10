"""
Database Models for Analytics Hierarchy

SQLAlchemy models representing the hierarchical structure with many-to-many relationships:
- Modules can belong to multiple Industries
- ObjectModels can belong to multiple Modules
- Objects can belong to multiple ObjectModels
- KPIs can belong to multiple ObjectModels
"""

from datetime import datetime
from typing import List, Optional

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Text,
    Float,
    Boolean,
    ForeignKey,
    Index,
    JSON,
    Table,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    """Base class for all SQLAlchemy models."""
    pass


class TimestampMixin:
    """Mixin for created_at and updated_at columns."""
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )


# ============================================================================
# Association Tables for Many-to-Many Relationships
# ============================================================================

industry_valuechain_association = Table(
    "industry_valuechain_association",
    Base.metadata,
    Column("industry_id", Integer, ForeignKey("industries.id", ondelete="CASCADE"), primary_key=True),
    Column("value_chain_id", Integer, ForeignKey("value_chains.id", ondelete="CASCADE"), primary_key=True),
    Column("created_at", DateTime(timezone=True), default=datetime.utcnow, nullable=False),
    Index("ix_industry_valuechain_industry_id", "industry_id"),
    Index("ix_industry_valuechain_value_chain_id", "value_chain_id"),
)

valuechain_module_association = Table(
    "valuechain_module_association",
    Base.metadata,
    Column("value_chain_id", Integer, ForeignKey("value_chains.id", ondelete="CASCADE"), primary_key=True),
    Column("module_id", Integer, ForeignKey("modules.id", ondelete="CASCADE"), primary_key=True),
    Column("created_at", DateTime(timezone=True), default=datetime.utcnow, nullable=False),
    Index("ix_valuechain_module_value_chain_id", "value_chain_id"),
    Index("ix_valuechain_module_module_id", "module_id"),
)

module_objectmodel_association = Table(
    "module_objectmodel_association",
    Base.metadata,
    Column("module_id", Integer, ForeignKey("modules.id", ondelete="CASCADE"), primary_key=True),
    Column("object_model_id", Integer, ForeignKey("object_models.id", ondelete="CASCADE"), primary_key=True),
    Column("created_at", DateTime(timezone=True), default=datetime.utcnow, nullable=False),
    Index("ix_module_objectmodel_module_id", "module_id"),
    Index("ix_module_objectmodel_object_model_id", "object_model_id"),
)

# objectmodel_object_association removed - ObjectModel now serves as both model and instance

objectmodel_kpi_association = Table(
    "objectmodel_kpi_association",
    Base.metadata,
    Column("object_model_id", Integer, ForeignKey("object_models.id", ondelete="CASCADE"), primary_key=True),
    Column("kpi_id", Integer, ForeignKey("kpis.id", ondelete="CASCADE"), primary_key=True),
    Column("created_at", DateTime(timezone=True), default=datetime.utcnow, nullable=False),
    Index("ix_objectmodel_kpi_object_model_id", "object_model_id"),
    Index("ix_objectmodel_kpi_kpi_id", "kpi_id"),
)

module_kpi_association = Table(
    "module_kpi_association",
    Base.metadata,
    Column("module_id", Integer, ForeignKey("modules.id", ondelete="CASCADE"), primary_key=True),
    Column("kpi_id", Integer, ForeignKey("kpis.id", ondelete="CASCADE"), primary_key=True),
    Column("created_at", DateTime(timezone=True), default=datetime.utcnow, nullable=False),
    Index("ix_module_kpi_module_id", "module_id"),
    Index("ix_module_kpi_kpi_id", "kpi_id"),
)

client_valuechain_association = Table(
    "client_valuechain_association",
    Base.metadata,
    Column("client_id", Integer, ForeignKey("clients.id", ondelete="CASCADE"), primary_key=True),
    Column("value_chain_id", Integer, ForeignKey("value_chains.id", ondelete="CASCADE"), primary_key=True),
    Column("created_at", DateTime(timezone=True), default=datetime.utcnow, nullable=False),
    Index("ix_client_valuechain_client_id", "client_id"),
    Index("ix_client_valuechain_value_chain_id", "value_chain_id"),
)


class Industry(Base, TimestampMixin):
    """
    Industry Model - Top-level container for value chains.
    
    An Industry represents a business sector or domain that can contain
    multiple value chains for organizing analytics. Value chains can be shared
    across multiple industries.
    """
    __tablename__ = "industries"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    metadata_: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # Many-to-Many Relationships
    value_chains: Mapped[List["ValueChain"]] = relationship(
        "ValueChain",
        secondary=industry_valuechain_association,
        back_populates="industries",
        lazy="selectin"
    )
    
    __table_args__ = (
        Index("ix_industries_name", "name"),
        Index("ix_industries_code", "code"),
        Index("ix_industries_is_active", "is_active"),
    )
    
    def __repr__(self) -> str:
        return f"<Industry(id={self.id}, name='{self.name}', code='{self.code}')>"


class ValueChain(Base, TimestampMixin):
    """
    ValueChain Model - Intermediate layer between Industry and Module.
    
    A ValueChain represents a sequence of business activities that create value.
    Value chains can be shared across multiple industries and contain multiple
    modules. This provides an additional organizational layer for analytics.
    """
    __tablename__ = "value_chains"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    code: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    metadata_: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # Many-to-Many Relationships
    industries: Mapped[List["Industry"]] = relationship(
        "Industry",
        secondary=industry_valuechain_association,
        back_populates="value_chains",
        lazy="selectin"
    )
    modules: Mapped[List["Module"]] = relationship(
        "Module",
        secondary=valuechain_module_association,
        back_populates="value_chains",
        lazy="selectin"
    )
    clients: Mapped[List["Client"]] = relationship(
        "Client",
        secondary=client_valuechain_association,
        back_populates="value_chains",
        lazy="selectin"
    )
    
    __table_args__ = (
        Index("ix_value_chains_name", "name"),
        Index("ix_value_chains_code", "code"),
        Index("ix_value_chains_is_active", "is_active"),
        Index("ix_value_chains_display_order", "display_order"),
    )
    
    def __repr__(self) -> str:
        return f"<ValueChain(id={self.id}, name='{self.name}', code='{self.code}')>"


class Module(Base, TimestampMixin):
    """
    Module Model - Container for object models.
    
    A Module represents a functional area or component that can be shared
    across multiple value chains and contains multiple object models.
    Object models can also be shared across multiple modules.
    """
    __tablename__ = "modules"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    code: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    metadata_: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # Many-to-Many Relationships
    value_chains: Mapped[List["ValueChain"]] = relationship(
        "ValueChain",
        secondary=valuechain_module_association,
        back_populates="modules",
        lazy="selectin"
    )
    object_models: Mapped[List["ObjectModel"]] = relationship(
        "ObjectModel",
        secondary=module_objectmodel_association,
        back_populates="modules",
        lazy="selectin"
    )
    kpis: Mapped[List["KPI"]] = relationship(
        "KPI",
        secondary=module_kpi_association,
        back_populates="modules",
        lazy="selectin"
    )
    
    __table_args__ = (
        Index("ix_modules_name", "name"),
        Index("ix_modules_code", "code"),
        Index("ix_modules_is_active", "is_active"),
        Index("ix_modules_display_order", "display_order"),
    )
    
    def __repr__(self) -> str:
        return f"<Module(id={self.id}, name='{self.name}', code='{self.code}')>"


class ObjectModel(Base, TimestampMixin):
    """
    ObjectModel - Unified object model and instance definition.
    
    Serves as both the object model definition (schema) and can represent instances.
    Combines the structure definition with actual data values for maximum flexibility.
    
    The schema_definition field stores a UML class diagram at the ENTITY LEVEL ONLY,
    defining classes and their relationships. Attributes and methods are defined
    separately through the ObjectAttribute model for flexibility and reusability.
    
    The data_values field stores actual attribute values for this object instance,
    using the ObjectAttribute codes as keys.
    
    Example schema_definition structure:
    {
        "classes": [
            {
                "name": "Customer",
                "stereotype": "entity",
                "description": "Customer entity representing a buyer"
            },
            {
                "name": "Order",
                "stereotype": "entity",
                "description": "Order placed by a customer"
            }
        ],
        "relationships": [
            {
                "type": "association",
                "from": "Customer",
                "to": "Order",
                "fromMultiplicity": "1",
                "toMultiplicity": "*",
                "fromNavigable": true,
                "toNavigable": true,
                "label": "places"
            }
        ]
    }
    
    Note: Attributes and methods for each class are defined separately using the
    ObjectAttribute model, which provides more flexibility for dynamic schemas.
    """
    __tablename__ = "object_models"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    code: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    
    # Schema Definition (UML)
    schema_definition: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="UML class diagram definition with classes, attributes, methods, and relationships"
    )
    
    # Instance Data (from former Object model)
    data_values: Mapped[Optional[dict]] = mapped_column(
        JSON, 
        nullable=True,
        comment="Attribute values stored as key-value pairs matching ObjectAttribute codes"
    )
    
    metadata_: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # One-to-Many Relationship for Attributes
    attributes: Mapped[List["ObjectAttribute"]] = relationship(
        "ObjectAttribute",
        back_populates="object_model",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    # Many-to-Many Relationships
    modules: Mapped[List["Module"]] = relationship(
        "Module",
        secondary=module_objectmodel_association,
        back_populates="object_models",
        lazy="selectin"
    )
    kpis: Mapped[List["KPI"]] = relationship(
        "KPI",
        secondary=objectmodel_kpi_association,
        back_populates="object_models",
        lazy="selectin"
    )
    
    __table_args__ = (
        Index("ix_object_models_name", "name"),
        Index("ix_object_models_code", "code"),
        Index("ix_object_models_is_active", "is_active"),
        Index("ix_object_models_display_order", "display_order"),
    )
    
    def __repr__(self) -> str:
        return f"<ObjectModel(id={self.id}, name='{self.name}', code='{self.code}')>"


class ObjectAttribute(Base, TimestampMixin):
    """
    ObjectAttribute - Defines an attribute/field for an ObjectModel.
    
    Represents a specific attribute (like a database table column) that objects
    of this model will have. Used to define the schema/structure of objects.
    """
    __tablename__ = "object_attributes"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    object_model_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("object_models.id", ondelete="CASCADE"),
        nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    code: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    data_type: Mapped[str] = mapped_column(
        String(50), 
        nullable=False,
        comment="Data type: string, integer, float, boolean, date, datetime, json"
    )
    is_required: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    default_value: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    validation_rules: Mapped[Optional[dict]] = mapped_column(
        JSON, 
        nullable=True,
        comment="Validation rules: min, max, pattern, enum, etc."
    )
    display_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    metadata_: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # Relationships
    object_model: Mapped["ObjectModel"] = relationship(
        "ObjectModel",
        back_populates="attributes"
    )
    
    __table_args__ = (
        Index("ix_object_attributes_object_model_id", "object_model_id"),
        Index("ix_object_attributes_name", "name"),
        Index("ix_object_attributes_code", "code"),
        Index("ix_object_attributes_is_active", "is_active"),
        Index("ix_object_attributes_display_order", "display_order"),
    )
    
    def __repr__(self) -> str:
        return f"<ObjectAttribute(id={self.id}, name='{self.name}', data_type='{self.data_type}')>"


# Object class removed - ObjectModel now serves as both model definition and instance


class KPI(Base, TimestampMixin):
    """
    KPI - Key Performance Indicator.
    
    Represents a comprehensive measurable metric that can be associated with
    multiple object models and modules. Includes detailed definition, measurement 
    approach, insights, and actionable guidance. Supports derivation from parent KPIs.
    
    Many-to-Many Relationships:
    - KPIs can belong to multiple ObjectModels
    - KPIs can belong to multiple Modules
    """
    __tablename__ = "kpis"
    
    # Core Identification
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    code: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    # KPI Definition & Context
    kpi_definition: Mapped[Optional[str]] = mapped_column(
        Text, 
        nullable=True,
        comment="Clear explanation of what the KPI measures"
    )
    expected_business_insights: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        comment="Typical business insights expected from tracking this KPI"
    )
    measurement_approach: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        comment="Outline of the approach or process followed to measure this KPI"
    )
    
    # Calculation & Measurement
    formula: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        comment="Standard formula used to calculate this KPI"
    )
    calculation_formula: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        comment="Detailed calculation formula with explicit object attribute references"
    )
    attribute_references: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Object attribute codes referenced in the formula, e.g., {'revenue': 'REVENUE', 'cost': 'COST'}"
    )
    unit_of_measure: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    
    # Target Values & Thresholds
    target_value: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    current_value: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    threshold_warning: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    threshold_critical: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    
    # Analysis & Insights
    trend_analysis: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        comment="Insights into how the KPI evolves over time and what trends indicate"
    )
    diagnostic_questions: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Questions to ask to understand current position and improvement opportunities"
    )
    actionable_steps: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Practical tips for improving the KPI (operational, strategic, tactical)"
    )
    
    # Visualization & Reporting
    visualization_suggestions: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Recommended charts/graphs for representing KPI trends and patterns"
    )
    risk_warnings: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Potential risks or warning signs requiring immediate attention"
    )
    
    # Tools & Integration
    suggested_tracking_tools: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Tools, technologies, and software for tracking and analyzing the KPI"
    )
    integration_points: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="How the KPI integrates with other business systems and processes"
    )
    
    # Impact & Relationships
    change_impact: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        comment="How changes in this KPI impact other KPIs and expected changes"
    )
    source: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True,
        comment="Source reference or parent KPI this was derived from"
    )
    parent_kpi_id: Mapped[Optional[int]] = mapped_column(
        Integer,
        ForeignKey("kpis.id", ondelete="SET NULL"),
        nullable=True,
        comment="Reference to parent KPI if this is a derived/custom KPI"
    )
    
    # Display and Categorization
    display_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    category: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    
    # Metadata
    metadata_: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # Many-to-Many Relationships
    object_models: Mapped[List["ObjectModel"]] = relationship(
        "ObjectModel",
        secondary=objectmodel_kpi_association,
        back_populates="kpis",
        lazy="selectin"
    )
    modules: Mapped[List["Module"]] = relationship(
        "Module",
        secondary=module_kpi_association,
        back_populates="kpis",
        lazy="selectin"
    )
    
    # Self-referential relationship for derived KPIs
    parent_kpi: Mapped[Optional["KPI"]] = relationship(
        "KPI",
        remote_side=[id],
        backref="derived_kpis",
        foreign_keys=[parent_kpi_id]
    )
    
    __table_args__ = (
        Index("ix_kpis_name", "name"),
        Index("ix_kpis_code", "code"),
        Index("ix_kpis_is_active", "is_active"),
        Index("ix_kpis_category", "category"),
        Index("ix_kpis_display_order", "display_order"),
        Index("ix_kpis_parent_kpi_id", "parent_kpi_id"),
        Index("ix_kpis_source", "source"),
    )
    
    # Relationship to benchmarks
    benchmarks: Mapped[List["Benchmark"]] = relationship(
        "Benchmark",
        back_populates="kpi",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    def __repr__(self) -> str:
        return f"<KPI(id={self.id}, name='{self.name}', code='{self.code}')>"


class Benchmark(Base, TimestampMixin):
    """
    Benchmark - Industry benchmark data point for KPIs.
    
    Stores comprehensive benchmark data with full citation and structured context.
    Each benchmark represents a specific data point from a research study, industry report,
    or authoritative source that provides context for KPI performance evaluation.
    """
    __tablename__ = "benchmarks"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    kpi_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("kpis.id", ondelete="CASCADE"),
        nullable=False,
        comment="Reference to the KPI this benchmark applies to"
    )
    
    # Core Identification
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="Benchmark name or title"
    )
    code: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        comment="Unique benchmark code"
    )
    description: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        comment="Detailed description of the benchmark"
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    # ========================================================================
    # Exact Metric Information
    # ========================================================================
    
    metric_value: Mapped[Optional[float]] = mapped_column(
        nullable=True,
        comment="The benchmark value (numeric)"
    )
    metric_value_text: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
        comment="Text representation of value (for non-numeric or ranges)"
    )
    metric_unit: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
        comment="Unit of measure (e.g., %, $, seconds, count)"
    )
    statistic_type: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
        comment="Type of statistic: mean, median, mode, percentile, range, etc."
    )
    percentile: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
        comment="Percentile value if statistic_type is percentile (e.g., 50, 75, 90)"
    )
    
    # Value ranges for benchmarks that provide ranges
    value_min: Mapped[Optional[float]] = mapped_column(
        nullable=True,
        comment="Minimum value in range"
    )
    value_max: Mapped[Optional[float]] = mapped_column(
        nullable=True,
        comment="Maximum value in range"
    )
    
    # ========================================================================
    # Metric Definition & Attributes
    # ========================================================================
    
    metric_definition: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        comment="How the metric is defined and calculated"
    )
    metric_normalization: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        comment="How the metric is normalized (e.g., per user, per session, per dollar)"
    )
    metric_filters: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Filters applied to the metric (e.g., device type, traffic source)"
    )
    cohort_rules: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Cohort or segment rules applied"
    )
    
    # ========================================================================
    # Context & Segmentation
    # ========================================================================
    
    # Company Size
    company_size: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
        comment="Company size (e.g., SMB, Mid-Market, Enterprise, 1-50 employees)"
    )
    company_size_min: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
        comment="Minimum company size (employee count or revenue)"
    )
    company_size_max: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
        comment="Maximum company size (employee count or revenue)"
    )
    company_size_metric: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
        comment="Size metric: employees, revenue, customers, etc."
    )
    
    # Time Period
    time_period: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
        comment="Time period as reported (e.g., Q1 2024, 2023 Annual, Jan-Mar 2024)"
    )
    time_period_start: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        comment="Start date of time period"
    )
    time_period_end: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        comment="End date of time period"
    )
    
    # Population
    population: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
        comment="What was measured (e.g., landing pages, sessions, users, companies)"
    )
    population_size: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
        comment="Size of the population measured"
    )
    
    # Industry
    industry: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
        comment="Industry or sector (e.g., SaaS, E-commerce, Healthcare, Cross-industry)"
    )
    industry_tags: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Array of industry tags for multi-industry benchmarks"
    )
    
    # Geography
    geography: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
        comment="Geographic scope (e.g., United States, Global, EMEA, North America)"
    )
    country: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
        comment="Specific country if applicable"
    )
    region: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
        comment="Region (e.g., North America, Europe, Asia-Pacific)"
    )
    
    # Sample Size
    sample_size: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
        comment="Number of data points, companies, or observations in the study"
    )
    sample_description: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        comment="Description of the sample (e.g., Fortune 500 companies, B2B SaaS startups)"
    )
    
    # ========================================================================
    # Source Details & Citation
    # ========================================================================
    
    # Publisher/Author
    source_publisher: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
        comment="Publisher or organization (e.g., Gartner, McKinsey, HubSpot)"
    )
    source_author: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
        comment="Author(s) of the study or report"
    )
    source_title: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True,
        comment="Title of the report, study, or publication"
    )
    
    # Year & Date
    source_year: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
        comment="Year the source was published"
    )
    source_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        comment="Exact publication date if available"
    )
    
    # Source Excerpt
    source_excerpt: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        comment="Relevant excerpt or quote from the source for context"
    )
    
    # URLs & Downloads
    source_url: Mapped[Optional[str]] = mapped_column(
        String(1000),
        nullable=True,
        comment="URL to the source (web page, article, etc.)"
    )
    source_download_url: Mapped[Optional[str]] = mapped_column(
        String(1000),
        nullable=True,
        comment="URL to download whitepaper, PDF, or full report"
    )
    source_doi: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
        comment="Digital Object Identifier (DOI) for academic sources"
    )
    
    # Source Type & Credibility
    source_type: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
        comment="Type: research_report, whitepaper, academic_study, industry_survey, etc."
    )
    source_credibility: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
        comment="Credibility rating: high, medium, low"
    )
    
    # ========================================================================
    # Additional Comments & Methodology
    # ========================================================================
    
    methodology_notes: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        comment="Notes on research methodology, data collection, and analysis approach"
    )
    caveats: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        comment="Important caveats, limitations, or considerations"
    )
    special_coverage: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        comment="Special coverage areas or unique aspects of this benchmark"
    )
    comments: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        comment="Additional comments or notes"
    )
    
    # ========================================================================
    # Benchmark Quality & Validation
    # ========================================================================
    
    confidence_level: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
        comment="Confidence level: high, medium, low"
    )
    data_quality_score: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
        comment="Data quality score (0-100)"
    )
    last_verified_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        comment="When this benchmark was last verified or reviewed"
    )
    verified_by: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
        comment="Who verified or reviewed this benchmark"
    )
    
    # ========================================================================
    # Categorization & Display
    # ========================================================================
    
    benchmark_category: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
        comment="Category: industry_standard, best_in_class, average, poor_performance"
    )
    display_order: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
        comment="Display order for sorting"
    )
    is_featured: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
        comment="Whether to feature this benchmark prominently"
    )
    
    # ========================================================================
    # Additional Metadata
    # ========================================================================
    
    tags: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Array of tags for categorization and search"
    )
    metadata_: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Additional metadata and custom fields"
    )
    
    # Relationships
    kpi: Mapped["KPI"] = relationship(
        "KPI",
        back_populates="benchmarks"
    )
    
    __table_args__ = (
        Index("ix_benchmarks_kpi_id", "kpi_id"),
        Index("ix_benchmarks_name", "name"),
        Index("ix_benchmarks_code", "code"),
        Index("ix_benchmarks_is_active", "is_active"),
        Index("ix_benchmarks_industry", "industry"),
        Index("ix_benchmarks_geography", "geography"),
        Index("ix_benchmarks_company_size", "company_size"),
        Index("ix_benchmarks_source_publisher", "source_publisher"),
        Index("ix_benchmarks_source_year", "source_year"),
        Index("ix_benchmarks_benchmark_category", "benchmark_category"),
        Index("ix_benchmarks_display_order", "display_order"),
        Index("ix_benchmarks_is_featured", "is_featured"),
    )
    
    def __repr__(self) -> str:
        return f"<Benchmark(id={self.id}, name='{self.name}', kpi_id={self.kpi_id})>"


# ============================================================================
# Geography Models
# ============================================================================

class Country(Base, TimestampMixin):
    """
    Country - Geographic country entity.
    
    Represents a country with ISO codes and regional information.
    """
    __tablename__ = "countries"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        comment="Country name"
    )
    code: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        unique=True,
        comment="Country code (e.g., US, CA, GB)"
    )
    iso_alpha2: Mapped[Optional[str]] = mapped_column(
        String(2),
        nullable=True,
        comment="ISO 3166-1 alpha-2 code"
    )
    iso_alpha3: Mapped[Optional[str]] = mapped_column(
        String(3),
        nullable=True,
        comment="ISO 3166-1 alpha-3 code"
    )
    iso_numeric: Mapped[Optional[str]] = mapped_column(
        String(3),
        nullable=True,
        comment="ISO 3166-1 numeric code"
    )
    
    # Additional Information
    capital: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    currency_code: Mapped[Optional[str]] = mapped_column(
        String(3),
        nullable=True,
        comment="ISO 4217 currency code"
    )
    currency_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    phone_code: Mapped[Optional[str]] = mapped_column(
        String(20),
        nullable=True,
        comment="International dialing code"
    )
    
    # Status
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    # Metadata
    metadata_: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # Relationships
    regions: Mapped[List["Region"]] = relationship(
        "Region",
        back_populates="country",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    clients: Mapped[List["Client"]] = relationship(
        "Client",
        back_populates="country",
        lazy="selectin"
    )
    
    __table_args__ = (
        Index("ix_countries_name", "name"),
        Index("ix_countries_code", "code"),
        Index("ix_countries_iso_alpha2", "iso_alpha2"),
        Index("ix_countries_iso_alpha3", "iso_alpha3"),
        Index("ix_countries_is_active", "is_active"),
    )
    
    def __repr__(self) -> str:
        return f"<Country(id={self.id}, name='{self.name}', code='{self.code}')>"


class Region(Base, TimestampMixin):
    """
    Region - Geographic region within a country.
    
    Represents a state, province, or administrative region within a country.
    """
    __tablename__ = "regions"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    country_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("countries.id", ondelete="CASCADE"),
        nullable=False
    )
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="Region name (e.g., California, Ontario, England)"
    )
    code: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        comment="Region code (e.g., CA, ON, ENG)"
    )
    region_type: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
        comment="Type: state, province, territory, county, etc."
    )
    
    # Additional Information
    capital: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    abbreviation: Mapped[Optional[str]] = mapped_column(
        String(10),
        nullable=True,
        comment="Common abbreviation"
    )
    
    # Status
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    # Metadata
    metadata_: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # Relationships
    country: Mapped["Country"] = relationship(
        "Country",
        back_populates="regions"
    )
    metropolitan_areas: Mapped[List["MetropolitanStatisticalArea"]] = relationship(
        "MetropolitanStatisticalArea",
        back_populates="region",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    clients: Mapped[List["Client"]] = relationship(
        "Client",
        back_populates="region",
        lazy="selectin"
    )
    
    __table_args__ = (
        Index("ix_regions_country_id", "country_id"),
        Index("ix_regions_name", "name"),
        Index("ix_regions_code", "code"),
        Index("ix_regions_region_type", "region_type"),
        Index("ix_regions_is_active", "is_active"),
        Index("ix_regions_country_code", "country_id", "code", unique=True),
    )
    
    def __repr__(self) -> str:
        return f"<Region(id={self.id}, name='{self.name}', code='{self.code}')>"


class MetropolitanStatisticalArea(Base, TimestampMixin):
    """
    MetropolitanStatisticalArea - Metropolitan Statistical Area (MSA).
    
    Represents a metropolitan statistical area as defined by the U.S. Office of
    Management and Budget or equivalent international designations.
    """
    __tablename__ = "metropolitan_statistical_areas"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    region_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("regions.id", ondelete="CASCADE"),
        nullable=False
    )
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="MSA name (e.g., New York-Newark-Jersey City, NY-NJ-PA)"
    )
    code: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        comment="MSA code or CBSA code"
    )
    
    # MSA Details
    cbsa_code: Mapped[Optional[str]] = mapped_column(
        String(10),
        nullable=True,
        comment="Core Based Statistical Area (CBSA) code"
    )
    msa_type: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
        comment="Type: metropolitan, micropolitan"
    )
    population: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
        comment="Population estimate"
    )
    population_year: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
        comment="Year of population estimate"
    )
    
    # Geographic Details
    central_city: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
        comment="Primary central city"
    )
    counties: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Array of counties in the MSA"
    )
    
    # Status
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    # Metadata
    metadata_: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # Relationships
    region: Mapped["Region"] = relationship(
        "Region",
        back_populates="metropolitan_areas"
    )
    clients: Mapped[List["Client"]] = relationship(
        "Client",
        back_populates="metropolitan_area",
        lazy="selectin"
    )
    
    __table_args__ = (
        Index("ix_msa_region_id", "region_id"),
        Index("ix_msa_name", "name"),
        Index("ix_msa_code", "code"),
        Index("ix_msa_cbsa_code", "cbsa_code"),
        Index("ix_msa_msa_type", "msa_type"),
        Index("ix_msa_is_active", "is_active"),
    )
    
    def __repr__(self) -> str:
        return f"<MetropolitanStatisticalArea(id={self.id}, name='{self.name}', code='{self.code}')>"


# ============================================================================
# Client & Authorization Models
# ============================================================================

class Client(Base, TimestampMixin):
    """
    Client - Administrative entity for access control.
    
    Represents a client organization or tenant with specific access permissions
    to modules, object models, objects, KPIs, and attributes. Implements
    multi-tenancy and role-based access control.
    """
    __tablename__ = "clients"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    # NAICS Industry Classification
    naics_code: Mapped[Optional[str]] = mapped_column(
        String(10),
        nullable=True,
        comment="North American Industry Classification System (NAICS) code"
    )
    naics_title: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True,
        comment="NAICS industry title/description"
    )
    naics_sector: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
        comment="NAICS sector (2-digit level)"
    )
    naics_subsector: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
        comment="NAICS subsector (3-digit level)"
    )
    
    # Geography - Foreign Keys
    country_id: Mapped[Optional[int]] = mapped_column(
        Integer,
        ForeignKey("countries.id", ondelete="SET NULL"),
        nullable=True,
        comment="Country where client is located"
    )
    region_id: Mapped[Optional[int]] = mapped_column(
        Integer,
        ForeignKey("regions.id", ondelete="SET NULL"),
        nullable=True,
        comment="Region/state/province where client is located"
    )
    metropolitan_area_id: Mapped[Optional[int]] = mapped_column(
        Integer,
        ForeignKey("metropolitan_statistical_areas.id", ondelete="SET NULL"),
        nullable=True,
        comment="Metropolitan Statistical Area where client is located"
    )
    
    # Client Configuration
    config: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Client-specific configuration settings"
    )
    
    # Contact Information
    contact_email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    contact_phone: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    
    # Metadata
    metadata_: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # Relationships
    # Geography
    country: Mapped[Optional["Country"]] = relationship(
        "Country",
        back_populates="clients"
    )
    region: Mapped[Optional["Region"]] = relationship(
        "Region",
        back_populates="clients"
    )
    metropolitan_area: Mapped[Optional["MetropolitanStatisticalArea"]] = relationship(
        "MetropolitanStatisticalArea",
        back_populates="clients"
    )
    
    # Value Chains Access
    value_chains: Mapped[List["ValueChain"]] = relationship(
        "ValueChain",
        secondary=client_valuechain_association,
        back_populates="clients",
        lazy="selectin"
    )
    
    # Authorization
    roles: Mapped[List["ClientRole"]] = relationship(
        "ClientRole",
        back_populates="client",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    module_permissions: Mapped[List["ClientModulePermission"]] = relationship(
        "ClientModulePermission",
        back_populates="client",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    __table_args__ = (
        Index("ix_clients_name", "name"),
        Index("ix_clients_code", "code"),
        Index("ix_clients_is_active", "is_active"),
        Index("ix_clients_naics_code", "naics_code"),
        Index("ix_clients_naics_sector", "naics_sector"),
        Index("ix_clients_country_id", "country_id"),
        Index("ix_clients_region_id", "region_id"),
        Index("ix_clients_metropolitan_area_id", "metropolitan_area_id"),
    )
    
    def __repr__(self) -> str:
        return f"<Client(id={self.id}, name='{self.name}', code='{self.code}')>"


class ClientRole(Base, TimestampMixin):
    """
    ClientRole - Role definition for client users.
    
    Defines roles within a client organization with specific permissions
    to access object models, objects, KPIs, and attributes. Supports
    fine-grained access control and row-level security.
    """
    __tablename__ = "client_roles"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    client_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("clients.id", ondelete="CASCADE"),
        nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    code: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    # Role Configuration
    permissions: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Role-specific permissions configuration"
    )
    
    # Metadata
    metadata_: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    
    # Relationships
    client: Mapped["Client"] = relationship(
        "Client",
        back_populates="roles"
    )
    object_model_permissions: Mapped[List["RoleObjectModelPermission"]] = relationship(
        "RoleObjectModelPermission",
        back_populates="role",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    object_permissions: Mapped[List["RoleObjectPermission"]] = relationship(
        "RoleObjectPermission",
        back_populates="role",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    kpi_permissions: Mapped[List["RoleKPIPermission"]] = relationship(
        "RoleKPIPermission",
        back_populates="role",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    attribute_permissions: Mapped[List["RoleAttributePermission"]] = relationship(
        "RoleAttributePermission",
        back_populates="role",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    __table_args__ = (
        Index("ix_client_roles_client_id", "client_id"),
        Index("ix_client_roles_name", "name"),
        Index("ix_client_roles_code", "code"),
        Index("ix_client_roles_is_active", "is_active"),
    )
    
    def __repr__(self) -> str:
        return f"<ClientRole(id={self.id}, name='{self.name}', client_id={self.client_id})>"


class ClientModulePermission(Base, TimestampMixin):
    """
    ClientModulePermission - Module access control for clients.
    
    Defines which modules a client can access. Only explicitly listed
    modules are available to the client.
    """
    __tablename__ = "client_module_permissions"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    client_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("clients.id", ondelete="CASCADE"),
        nullable=False
    )
    module_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("modules.id", ondelete="CASCADE"),
        nullable=False
    )
    
    # Permission Flags
    can_view: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    can_create: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    can_update: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    can_delete: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    # Additional Configuration
    config: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Module-specific permission configuration"
    )
    
    # Relationships
    client: Mapped["Client"] = relationship(
        "Client",
        back_populates="module_permissions"
    )
    module: Mapped["Module"] = relationship("Module")
    
    __table_args__ = (
        Index("ix_client_module_permissions_client_id", "client_id"),
        Index("ix_client_module_permissions_module_id", "module_id"),
        Index("ix_client_module_permissions_client_module", "client_id", "module_id", unique=True),
    )
    
    def __repr__(self) -> str:
        return f"<ClientModulePermission(client_id={self.client_id}, module_id={self.module_id})>"


class RoleObjectModelPermission(Base, TimestampMixin):
    """
    RoleObjectModelPermission - ObjectModel access control for roles.
    
    Defines which object models a role can access within the client's
    available modules.
    """
    __tablename__ = "role_objectmodel_permissions"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    role_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("client_roles.id", ondelete="CASCADE"),
        nullable=False
    )
    object_model_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("object_models.id", ondelete="CASCADE"),
        nullable=False
    )
    
    # Permission Flags
    can_view: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    can_create: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    can_update: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    can_delete: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    # Additional Configuration
    config: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="ObjectModel-specific permission configuration"
    )
    
    # Relationships
    role: Mapped["ClientRole"] = relationship(
        "ClientRole",
        back_populates="object_model_permissions"
    )
    object_model: Mapped["ObjectModel"] = relationship("ObjectModel")
    
    __table_args__ = (
        Index("ix_role_objectmodel_permissions_role_id", "role_id"),
        Index("ix_role_objectmodel_permissions_object_model_id", "object_model_id"),
        Index("ix_role_objectmodel_permissions_role_model", "role_id", "object_model_id", unique=True),
    )
    
    def __repr__(self) -> str:
        return f"<RoleObjectModelPermission(role_id={self.role_id}, object_model_id={self.object_model_id})>"


class RoleObjectPermission(Base, TimestampMixin):
    """
    RoleObjectPermission - Object-level access control for roles.
    
    Defines which specific objects a role can access, including row-level
    security filters for data access control.
    """
    __tablename__ = "role_object_permissions"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    role_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("client_roles.id", ondelete="CASCADE"),
        nullable=False
    )
    object_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("objects.id", ondelete="CASCADE"),
        nullable=False
    )
    
    # Permission Flags
    can_view: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    can_update: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    can_delete: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    # Row-Level Security
    row_filter: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Row-level security filter: attribute conditions for data access"
    )
    
    # Additional Configuration
    config: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Object-specific permission configuration"
    )
    
    # Relationships
    role: Mapped["ClientRole"] = relationship(
        "ClientRole",
        back_populates="object_permissions"
    )
    object: Mapped["Object"] = relationship("Object")
    
    __table_args__ = (
        Index("ix_role_object_permissions_role_id", "role_id"),
        Index("ix_role_object_permissions_object_id", "object_id"),
        Index("ix_role_object_permissions_role_object", "role_id", "object_id", unique=True),
    )
    
    def __repr__(self) -> str:
        return f"<RoleObjectPermission(role_id={self.role_id}, object_id={self.object_id})>"


class RoleKPIPermission(Base, TimestampMixin):
    """
    RoleKPIPermission - KPI access control for roles.
    
    Defines which KPIs a role can view and analyze.
    """
    __tablename__ = "role_kpi_permissions"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    role_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("client_roles.id", ondelete="CASCADE"),
        nullable=False
    )
    kpi_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("kpis.id", ondelete="CASCADE"),
        nullable=False
    )
    
    # Permission Flags
    can_view: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    can_update: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    # Additional Configuration
    config: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="KPI-specific permission configuration"
    )
    
    # Relationships
    role: Mapped["ClientRole"] = relationship(
        "ClientRole",
        back_populates="kpi_permissions"
    )
    kpi: Mapped["KPI"] = relationship("KPI")
    
    __table_args__ = (
        Index("ix_role_kpi_permissions_role_id", "role_id"),
        Index("ix_role_kpi_permissions_kpi_id", "kpi_id"),
        Index("ix_role_kpi_permissions_role_kpi", "role_id", "kpi_id", unique=True),
    )
    
    def __repr__(self) -> str:
        return f"<RoleKPIPermission(role_id={self.role_id}, kpi_id={self.kpi_id})>"


class RoleAttributePermission(Base, TimestampMixin):
    """
    RoleAttributePermission - Attribute-level access control for roles.
    
    Defines which object attributes a role can view. Enables field-level
    security for sensitive data.
    """
    __tablename__ = "role_attribute_permissions"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    role_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("client_roles.id", ondelete="CASCADE"),
        nullable=False
    )
    attribute_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("object_attributes.id", ondelete="CASCADE"),
        nullable=False
    )
    
    # Permission Flags
    can_view: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    can_update: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    # Data Masking
    is_masked: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
        comment="Whether to mask/redact the attribute value"
    )
    mask_type: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
        comment="Masking type: partial, full, hash, encrypt"
    )
    
    # Additional Configuration
    config: Mapped[Optional[dict]] = mapped_column(
        JSON,
        nullable=True,
        comment="Attribute-specific permission configuration"
    )
    
    # Relationships
    role: Mapped["ClientRole"] = relationship(
        "ClientRole",
        back_populates="attribute_permissions"
    )
    attribute: Mapped["ObjectAttribute"] = relationship("ObjectAttribute")
    
    __table_args__ = (
        Index("ix_role_attribute_permissions_role_id", "role_id"),
        Index("ix_role_attribute_permissions_attribute_id", "attribute_id"),
        Index("ix_role_attribute_permissions_role_attr", "role_id", "attribute_id", unique=True),
    )
    
    def __repr__(self) -> str:
        return f"<RoleAttributePermission(role_id={self.role_id}, attribute_id={self.attribute_id})>"
