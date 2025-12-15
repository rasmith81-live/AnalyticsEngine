# Business Metadata - Quick Reference

## Service Overview

The **business_metadata** service provides a Knowledge Graph-based metadata layer with 26 ontology classes organized into 5 layers. It uses a versioned, graph-based approach with JSONB storage and RESTful APIs.

## File Structure

```
business_metadata/
├── __init__.py
├── main.py                          # FastAPI application
├── config.py                        # Configuration settings
├── api/
│   ├── __init__.py
│   └── metadata_api.py              # RESTful API endpoints
├── services/
│   ├── __init__.py
│   ├── metadata_service.py          # High-level orchestration
│   └── metadata_instantiation_service.py  # Model conversion
├── repositories/
│   ├── __init__.py
│   └── metadata_repository.py       # Database access layer
├── models/
│   ├── __init__.py
│   ├── metadata_definition.py       # SQLAlchemy models
│   └── metadata_version.py          # Version tracking
└── README.md                        # Detailed documentation
```

## Ontology Layers (26 Classes)

### Core Ontology Layer (6 classes)
- `ThingDefinition` - Base class for all definitions
- `EntityDefinition` - Business entity definitions
- `RelationshipDefinition` - Entity relationships
- `MetricDefinition` - KPI and metric definitions
- `ValueSetDefinition` - Enumerated value sets
- `CodeSystemDefinition` - Code system definitions

### Business Ontology Layer (8 classes)
- `ValueChainPatternDefinition` - Value chain patterns (base class)
- `ActorDefinition` - Actors (people, roles, organizations, systems)
- `BeneficiaryDefinition` - Value chain beneficiaries
- `CompanyDefinition` - Company-level value chains (inherits from ValueChainPattern)
- `BusinessProcessDefinition` - Process-level value chains (inherits from ValueChainPattern)
- `StrategicObjectiveDefinition` - Strategic business objectives
- `BenchmarkDefinition` - Industry benchmarks with citations
- `ExternalEventDefinition` - External events/news impacting business

### Authorization & Access Control Layer (8 classes)
- `ClientDefinition` - Multi-tenant clients/organizations
- `RoleDefinition` - Roles within client organizations
- `PermissionDefinition` - Base permission class
- `ModulePermissionDefinition` - Module-level access control
- `EntityPermissionDefinition` - Entity-level access control
- `MetricPermissionDefinition` - Metric-level access control
- `AttributePermissionDefinition` - Attribute-level access with masking
- `RowLevelSecurityDefinition` - Row-level security filters

### Geographic & Industry Classification Layer (4 classes)
- `CountryDefinition` - Countries with ISO 3166-1 codes
- `RegionDefinition` - States, provinces, territories
- `MetropolitanAreaDefinition` - MSAs and CMAs
- `NAICSIndustryDefinition` - NAICS industry codes

### Analytics Strategy & Data Management Layer (7 classes)
- `AnalyticsStrategyDefinition` - Company analytics strategy and maturity
- `DataSourceDefinition` - Data sources with quality tracking
- `DataProductDefinition` - Curated data assets with SLAs
- `AnalyticsUseCaseDefinition` - Business problems solved with analytics
- `DimensionDefinition` - Analytical dimensions for slicing
- `MetricCategoryDefinition` - Hierarchical metric categorization
- `DataQualityRuleDefinition` - Data quality validation rules

## Quick Import Guide

```python
# Pydantic Ontology Models
from definitions.ontology_models import (
    # Core
    ThingDefinition,
    EntityDefinition,
    RelationshipDefinition,
    MetricDefinition,
    ValueChainPatternDefinition,
    
    # Business
    ActorDefinition,
    BeneficiaryDefinition,
    CompanyDefinition,
    BusinessProcessDefinition,
    StrategicObjectiveDefinition,
    BenchmarkDefinition,
    ExternalEventDefinition,
    
    # Authorization
    ClientDefinition,
    RoleDefinition,
    PermissionDefinition,
    RowLevelSecurityDefinition,
    
    # Geography
    CountryDefinition,
    RegionDefinition,
    MetropolitanAreaDefinition,
    NAICSIndustryDefinition,
    
    # Analytics Strategy
    AnalyticsStrategyDefinition,
    DataSourceDefinition,
    DataProductDefinition,
    AnalyticsUseCaseDefinition,
    DimensionDefinition,
    MetricCategoryDefinition,
    DataQualityRuleDefinition
)

# Service Layer
from services.metadata_service import MetadataService
from services.metadata_instantiation_service import MetadataInstantiationService

# Repository Layer
from repositories.metadata_repository import MetadataRepository

# Database Models
from models.metadata_definition import MetadataDefinition
from models.metadata_version import MetadataVersion
```

## API Endpoints

### Core CRUD Operations
```bash
# Create definition
POST /api/v1/metadata/definitions
{
  "kind": "entity_definition",
  "code": "CUSTOMER",
  "name": "Customer",
  "description": "Customer entity",
  "definition_data": {...}
}

# Get by ID
GET /api/v1/metadata/definitions/{id}

# Update definition
PUT /api/v1/metadata/definitions/{id}

# Delete definition
DELETE /api/v1/metadata/definitions/{id}

# List all (with filters)
GET /api/v1/metadata/definitions?kind=entity_definition&is_active=true

# Search
POST /api/v1/metadata/search
{
  "kind": "metric_definition",
  "filters": {"category": "financial"}
}
```

### Type-Specific Endpoints
```bash
# Entities
GET /api/v1/metadata/entities/{code}

# Metrics
GET /api/v1/metadata/metrics/{code}

# Companies
GET /api/v1/metadata/companies/{code}

# Clients
GET /api/v1/metadata/clients/{code}

# Analytics Strategies
GET /api/v1/metadata/analytics-strategies/{code}

# Data Sources
GET /api/v1/metadata/data-sources/{code}

# External Events
GET /api/v1/metadata/external-events/{code}

# Countries
GET /api/v1/metadata/countries/{code}

# Regions
GET /api/v1/metadata/regions/{code}

# Metropolitan Areas
GET /api/v1/metadata/metropolitan-areas/{code}

# NAICS Industries
GET /api/v1/metadata/naics-industries/{code}
```

### Hierarchical Queries
```bash
# Get regions for a country
GET /api/v1/metadata/countries/{country_code}/regions

# Get MSAs for a region
GET /api/v1/metadata/regions/{region_code}/metropolitan-areas

# Get benchmarks for a metric
GET /api/v1/metadata/metrics/{metric_code}/benchmarks

# Get roles for a client
GET /api/v1/metadata/clients/{client_code}/roles
```

### Versioning
```bash
# Get version history
GET /api/v1/metadata/definitions/{id}/versions

# Get specific version
GET /api/v1/metadata/definitions/{id}/versions/{version}
```

### Relationships
```bash
# Get relationships
GET /api/v1/metadata/definitions/{id}/relationships

# Create relationship
POST /api/v1/metadata/relationships
```

## Common Operations

### Create Entity Definition
```python
from definitions.ontology_models import EntityDefinition, TableSchemaDefinition, ColumnDefinition

entity = EntityDefinition(
    kind="entity_definition",
    id="Entity:CUSTOMER",
    code="CUSTOMER",
    name="Customer",
    description="Customer entity with demographics",
    table_schema=TableSchemaDefinition(
        table_name="customers",
        columns=[
            ColumnDefinition(
                name="customer_id",
                type="UUID",
                primary_key=True
            ),
            ColumnDefinition(
                name="name",
                type="String(255)",
                nullable=False
            ),
            ColumnDefinition(
                name="email",
                type="String(255)"
            )
        ]
    )
)

# Create via API
response = requests.post(
    "http://localhost:8000/api/v1/metadata/definitions",
    json=entity.model_dump()
)
```

### Create Metric Definition
```python
from definitions.ontology_models import MetricDefinition

metric = MetricDefinition(
    kind="metric_definition",
    code="CUSTOMER_LTV",
    name="Customer Lifetime Value",
    description="Total value of customer over their lifetime",
    formula="SUM(Order.total_amount) WHERE Order.customer_id = Customer.customer_id",
    required_objects=["CUSTOMER", "ORDER"],
    unit="USD",
    data_type="decimal",
    aggregation_methods=["sum", "avg", "median"],
    time_periods=["monthly", "quarterly", "yearly"],
    dimensions=["country", "customer_segment"],
    metric_category="FINANCIAL"
)

# Create via API
response = requests.post(
    "http://localhost:8000/api/v1/metadata/definitions",
    json=metric.model_dump()
)
```

### Create External Event
```python
from definitions.ontology_models import ExternalEventDefinition

event = ExternalEventDefinition(
    kind="external_event_definition",
    code="FED_RATE_HIKE_2024_12",
    name="Federal Reserve Rate Hike December 2024",
    event_type="economic",
    event_category="economy",
    event_date="2024-12-18",
    headline="Fed Raises Interest Rates by 0.25%",
    summary="Federal Reserve increases benchmark rate to combat inflation",
    source="Federal Reserve",
    source_url="https://www.federalreserve.gov",
    sentiment="negative",
    impact_level="high",
    affected_metrics=["INTEREST_EXPENSE", "BORROWING_COST"],
    related_industries=["522110", "522120"],  # Banking NAICS codes
    related_geographies=["US"],
    predicted_impact="Increased borrowing costs, reduced lending activity"
)

# Create via API
response = requests.post(
    "http://localhost:8000/api/v1/metadata/definitions",
    json=event.model_dump()
)
```

### Create Analytics Use Case
```python
from definitions.ontology_models import AnalyticsUseCaseDefinition

use_case = AnalyticsUseCaseDefinition(
    kind="analytics_use_case_definition",
    code="CUSTOMER_CHURN_PREDICTION",
    name="Customer Churn Prediction",
    use_case_type="prediction",
    business_problem="Identify customers at risk of churning",
    expected_value="15% reduction in churn rate",
    success_metrics=["CHURN_RATE", "CUSTOMER_RETENTION_RATE"],
    required_data_sources=["CRM_SYSTEM", "SUPPORT_SYSTEM"],
    required_entities=["CUSTOMER", "SUPPORT_TICKET", "ORDER"],
    required_metrics=["CUSTOMER_LTV", "SUPPORT_TICKET_COUNT"],
    business_owner="VP_CUSTOMER_SUCCESS",
    technical_owner="DATA_SCIENCE_LEAD",
    maturity_stage="production",
    implementation_priority="high"
)

# Create via API
response = requests.post(
    "http://localhost:8000/api/v1/metadata/definitions",
    json=use_case.model_dump()
)
```

## Using the Service Layer

### Python Service Usage
```python
from services.metadata_service import MetadataService
from definitions.ontology_models import EntityDefinition

# Initialize service
service = MetadataService()

# Create definition
entity = EntityDefinition(...)
created = await service.create_definition(entity)

# Get definition
entity = await service.get_definition(
    id="550e8400-e29b-41d4-a716-446655440000"
)

# Get by code
entity = await service.get_definition(
    code="CUSTOMER",
    kind="entity_definition"
)

# Update definition
updated = await service.update_definition(
    id="550e8400-e29b-41d4-a716-446655440000",
    updates={"description": "Updated description"}
)

# Search definitions
results = await service.search_definitions(
    kind="metric_definition",
    filters={"category": "financial"}
)

# Get relationships
relationships = await service.get_relationships(
    definition_id="550e8400-e29b-41d4-a716-446655440000"
)

# Get version history
versions = await service.get_version_history(
    definition_id="550e8400-e29b-41d4-a716-446655440000"
)
```

## Key Features

### All Definitions Include
- ✅ UUID primary key
- ✅ Kind (ontology class type)
- ✅ Code (stable identifier)
- ✅ Name and description
- ✅ Full definition data (JSONB)
- ✅ Version tracking
- ✅ Active status flag
- ✅ Timestamps (created_at, updated_at)
- ✅ Audit fields (created_by, updated_by)
- ✅ Metadata field (extensibility)

### Knowledge Graph Features
- ✅ **Graph-based relationships** - Rich connections between all entities
- ✅ **Versioned metadata** - Full version history and temporal queries
- ✅ **JSONB storage** - Flexible schema with PostgreSQL JSONB
- ✅ **Type-safe models** - Pydantic validation
- ✅ **RESTful API** - FastAPI endpoints
- ✅ **Redis caching** - Performance optimization
- ✅ **Full-text search** - Advanced filtering

### Traceability Chain
```
AnalyticsStrategy
  ↓ strategic_priorities
StrategicObjectives
  ↓ aligned_use_cases
AnalyticsUseCases
  ↓ required_metrics, required_data_sources
Metrics
  ↓ required_objects, data_sources
Entities
  ↓ table_schema
DataSources

PLUS External Context:
ExternalEvents → affected_metrics, affected_entities, related_companies
```

## Database Schema

```sql
-- Core metadata table
CREATE TABLE business_metadata.metadata_definitions (
    id UUID PRIMARY KEY,
    kind VARCHAR(100) NOT NULL,
    code VARCHAR(100),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    definition_data JSONB NOT NULL,
    version INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    created_by VARCHAR(100),
    updated_by VARCHAR(100),
    metadata_ JSONB DEFAULT '{}'::jsonb
);

-- Version history
CREATE TABLE business_metadata.metadata_versions (
    id UUID PRIMARY KEY,
    definition_id UUID REFERENCES metadata_definitions(id),
    version INTEGER NOT NULL,
    definition_data JSONB NOT NULL,
    change_description TEXT,
    changed_at TIMESTAMPTZ DEFAULT NOW(),
    changed_by VARCHAR(100)
);

-- Indexes
CREATE INDEX idx_metadata_kind ON metadata_definitions(kind);
CREATE INDEX idx_metadata_code ON metadata_definitions(code);
CREATE INDEX idx_metadata_active ON metadata_definitions(is_active);
CREATE INDEX idx_metadata_data_gin ON metadata_definitions USING gin(definition_data);
```

## Configuration

```python
# config.py
class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql+asyncpg://user:pass@localhost/analytics"
    
    # Redis Cache
    redis_url: str = "redis://localhost:6379/0"
    cache_ttl: int = 3600
    
    # API
    api_prefix: str = "/api/v1/metadata"
    
    # Service
    max_results: int = 1000
    enable_versioning: bool = True
    enable_caching: bool = True
```

## Common Queries

### Get All Entities
```python
entities = await service.search_definitions(
    kind="entity_definition",
    filters={"is_active": True}
)
```

### Get All Metrics by Category
```python
financial_metrics = await service.search_definitions(
    kind="metric_definition",
    filters={"category": "financial"}
)
```

### Get Analytics Strategy with Use Cases
```python
strategy = await service.get_definition(
    code="COMPANY_ANALYTICS_2024",
    kind="analytics_strategy_definition"
)

# Get linked use cases
use_cases = []
for use_case_code in strategy.primary_use_cases:
    uc = await service.get_definition(
        code=use_case_code,
        kind="analytics_use_case_definition"
    )
    use_cases.append(uc)
```

### Get External Events by Impact
```python
high_impact_events = await service.search_definitions(
    kind="external_event_definition",
    filters={"impact_level": "high"}
)
```

### Get Geographic Hierarchy
```python
# Get country
country = await service.get_definition(
    code="US",
    kind="country_definition"
)

# Get regions for country
regions = await service.search_definitions(
    kind="region_definition",
    filters={"country_code": "US"}
)

# Get MSAs for region
msas = await service.search_definitions(
    kind="metropolitan_area_definition",
    filters={"region_code": "CA"}
)
```

## Tips

- ✅ Use `code` fields for stable identifiers (never change)
- ✅ Use `is_active` for soft deletes
- ✅ Use `metadata_` for extensibility
- ✅ Always include version tracking for audit trails
- ✅ Use relationships to link definitions
- ✅ Cache frequently accessed definitions
- ✅ Use type-specific endpoints for convenience
- ✅ Leverage JSONB for flexible schema evolution
- ✅ Use hierarchical queries for geographic and organizational structures
- ✅ Link external events to affected metrics and entities for impact analysis

## Next Steps

1. **Start the Service**
   ```bash
   cd services/business_services/business_metadata
   uvicorn main:app --reload --port 8000
   ```

2. **Create Initial Ontology**
   - Define core entities
   - Define key metrics
   - Define relationships
   - Define geographic classifications

3. **Integrate with Layer 2**
   - Use CQRS scripts to generate tables from EntityDefinitions
   - Create Alembic migrations
   - Deploy to analytics_data schema

4. **Build Analytics Use Cases**
   - Define business problems
   - Link to required data sources and metrics
   - Track maturity and priority

5. **Monitor External Events**
   - Capture news and market events
   - Link to affected metrics and entities
   - Track predicted vs actual impact

## Architecture Integration

This service is **Layer 0** in the four-layer architecture:

```
Layer 0: Knowledge Graph (business_metadata) ← YOU ARE HERE
  ↓ defines structure
Layer 2: Active Analytics Data (analytics_data)
  ↓ archives to
Layer 2a: Historical Archive (Azure Data Lake)
  ↑ sources from
Layer 3: Integration/Staging (integration_data)
```

See `COMPLETE_DATA_ARCHITECTURE.md` for full architecture details.
