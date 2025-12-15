# Complete Data Architecture: Knowledge Graph & Multi-Layer Storage

**Date**: December 8, 2025  
**Status**: Comprehensive architecture with Knowledge Graph ontology

---

## 🏗️ Architecture Overview

The analytics platform uses a **Knowledge Graph-based metadata layer** combined with a **four-layer data storage architecture** that separates metadata, active analytics data, archived data, and source data into distinct layers with clear responsibilities.

```
┌─────────────────────────────────────────────────────────────────┐
│ Layer 0: KNOWLEDGE GRAPH (Business Metadata)                   │
│ ├─ Ontology: Entities, Metrics, Relationships, Dimensions      │
│ ├─ Business: Companies, Actors, Strategies, Use Cases          │
│ ├─ Authorization: Clients, Roles, Permissions, Security        │
│ ├─ Geography: Countries, Regions, MSAs, Industries             │
│ ├─ External: Events, News, Market Conditions                   │
│ ├─ Location: TimescaleDB (business_metadata schema)            │
│ └─ Purpose: Unified ontology for all business concepts         │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼ CQRS Scripts (table creation from ontology)
┌─────────────────────────────────────────────────────────────────┐
│ Layer 2: ANALYTICS MODEL (Active Business Data)                │
│ ├─ Customers, Orders, Products, SCOR Processes, etc.           │
│ ├─ Location: TimescaleDB (analytics_data schema)               │
│ ├─ Format: PostgreSQL tables + TimescaleDB hypertables         │
│ └─ Purpose: Active data for real-time analytics                │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼ Archival Service (aging data)
┌─────────────────────────────────────────────────────────────────┐
│ Layer 2a: ARCHIVE (Historical Data Lake)                       │
│ ├─ Archived chunks from Layer 2 tables                         │
│ ├─ Location: Azure Data Lake Storage Gen2                      │
│ ├─ Format: Parquet/Delta Lake (columnar storage)               │
│ └─ Purpose: Long-term storage, historical analytics            │
└─────────────────────────────────────────────────────────────────┘
                            ▲
                            │ ETL/Mapping
┌─────────────────────────────────────────────────────────────────┐
│ Layer 3: SOURCE MODEL (Integration/Staging)                    │
│ ├─ Raw data from external systems                              │
│ ├─ Location: TimescaleDB (integration_data schema)             │
│ ├─ Format: PostgreSQL staging tables                           │
│ └─ Purpose: Temporary staging for data transformation          │
└─────────────────────────────────────────────────────────────────┘
                            ▲
                            │ Integration Services
                    External Systems (CRM, ERP, etc.)
```

---

## 📊 Layer 0: Knowledge Graph (Business Metadata Layer)

**Purpose**: Store the **unified ontology** that describes all business concepts, relationships, and metadata

**Service**: `business_metadata` at `services/business_services/business_metadata`

**Database**: TimescaleDB schema `business_metadata`

**Architecture**: Knowledge Graph with versioned, relationship-rich metadata

### What's Stored

The Knowledge Graph ontology contains **26 primary definition classes** organized into 5 layers:

*Note: Core layer contains 6 classes, Business layer contains 8 classes*

#### **Core Ontology Layer**
- `ThingDefinition` - Base class for all definitions
- `EntityDefinition` - Business entity definitions (customers, orders, products)
- `RelationshipDefinition` - Relationships between entities
- `MetricDefinition` - KPI and metric definitions with formulas
- `ValueSetDefinition` - Enumerated value sets
- `CodeSystemDefinition` - Code system definitions

#### **Business Ontology Layer**
- `ValueChainPatternDefinition` - Value chain patterns (base class)
- `ActorDefinition` - Actors (people, roles, organizations, systems)
- `BeneficiaryDefinition` - Value chain beneficiaries
- `CompanyDefinition` - Company-level value chains (inherits from ValueChainPattern)
- `BusinessProcessDefinition` - Process-level value chains (inherits from ValueChainPattern)
- `StrategicObjectiveDefinition` - Strategic business objectives
- `BenchmarkDefinition` - Industry benchmarks with citations
- `ExternalEventDefinition` - External events/news impacting business

#### **Authorization & Access Control Layer**
- `ClientDefinition` - Multi-tenant clients/organizations
- `RoleDefinition` - Roles within client organizations
- `PermissionDefinition` - Base permission class
- `ModulePermissionDefinition` - Module-level access control
- `EntityPermissionDefinition` - Entity-level access control
- `MetricPermissionDefinition` - Metric-level access control
- `AttributePermissionDefinition` - Attribute-level access with masking
- `RowLevelSecurityDefinition` - Row-level security filters

#### **Geographic & Industry Classification Layer**
- `CountryDefinition` - Countries with ISO 3166-1 codes
- `RegionDefinition` - States, provinces, territories
- `MetropolitanAreaDefinition` - MSAs and CMAs
- `NAICSIndustryDefinition` - NAICS industry codes

#### **Analytics Strategy & Data Management Layer**
- `AnalyticsStrategyDefinition` - Company analytics strategy and maturity
- `DataSourceDefinition` - Data sources with quality tracking
- `DataProductDefinition` - Curated data assets with SLAs
- `AnalyticsUseCaseDefinition` - Business problems solved with analytics
- `DimensionDefinition` - Analytical dimensions for slicing
- `MetricCategoryDefinition` - Hierarchical metric categorization
- `DataQualityRuleDefinition` - Data quality validation rules

### Key Characteristics

- ✅ **Unified Ontology** - Single source of truth for all business concepts
- ✅ **Graph-Based** - Rich relationships between all entities
- ✅ **Versioned** - Full version history and temporal queries
- ✅ **JSONB Storage** - Flexible schema with PostgreSQL JSONB
- ✅ **Pydantic Models** - Type-safe Python models with validation
- ✅ **RESTful API** - FastAPI endpoints for CRUD operations
- ✅ **Cached** - Redis caching for performance
- ✅ **Searchable** - Full-text search and filtering

### Storage Structure

```
services/business_services/business_metadata/
├── api/
│   └── metadata_api.py          ← RESTful API endpoints
├── services/
│   ├── metadata_service.py      ← High-level orchestration
│   └── metadata_instantiation_service.py  ← Model conversion
├── repositories/
│   └── metadata_repository.py   ← Database access layer
├── models/
│   ├── metadata_definition.py   ← SQLAlchemy models
│   └── metadata_version.py      ← Version tracking
└── main.py                      ← FastAPI application

services/business_services/analytics_metadata_service/definitions/
└── ontology_models.py           ← Pydantic ontology definitions
```

### Database Schema

```sql
-- Core metadata table with JSONB storage
CREATE TABLE business_metadata.metadata_definitions (
    id UUID PRIMARY KEY,
    kind VARCHAR(100) NOT NULL,
    code VARCHAR(100),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    definition_data JSONB NOT NULL,  -- Full Pydantic model as JSON
    version INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    created_by VARCHAR(100),
    updated_by VARCHAR(100),
    metadata_ JSONB DEFAULT '{}'::jsonb
);

-- Version history table
CREATE TABLE business_metadata.metadata_versions (
    id UUID PRIMARY KEY,
    definition_id UUID REFERENCES metadata_definitions(id),
    version INTEGER NOT NULL,
    definition_data JSONB NOT NULL,
    change_description TEXT,
    changed_at TIMESTAMPTZ DEFAULT NOW(),
    changed_by VARCHAR(100)
);

-- Indexes for performance
CREATE INDEX idx_metadata_kind ON metadata_definitions(kind);
CREATE INDEX idx_metadata_code ON metadata_definitions(code);
CREATE INDEX idx_metadata_active ON metadata_definitions(is_active);
CREATE INDEX idx_metadata_data_gin ON metadata_definitions USING gin(definition_data);
```

### API Endpoints

```
# Core CRUD operations
POST   /api/v1/metadata/definitions          - Create definition
GET    /api/v1/metadata/definitions/{id}     - Get by ID
PUT    /api/v1/metadata/definitions/{id}     - Update definition
DELETE /api/v1/metadata/definitions/{id}     - Delete definition

# Search and query
GET    /api/v1/metadata/definitions          - List all (with filters)
POST   /api/v1/metadata/search               - Advanced search
GET    /api/v1/metadata/kinds                - List all kinds

# Relationships
GET    /api/v1/metadata/definitions/{id}/relationships  - Get relationships
POST   /api/v1/metadata/relationships        - Create relationship

# Versioning
GET    /api/v1/metadata/definitions/{id}/versions       - Version history
GET    /api/v1/metadata/definitions/{id}/versions/{v}   - Get specific version

# Type-specific convenience endpoints
GET    /api/v1/metadata/entities/{code}              - Get entity
GET    /api/v1/metadata/metrics/{code}               - Get metric
GET    /api/v1/metadata/companies/{code}             - Get company
GET    /api/v1/metadata/clients/{code}               - Get client
GET    /api/v1/metadata/analytics-strategies/{code}  - Get strategy
GET    /api/v1/metadata/data-sources/{code}          - Get data source
GET    /api/v1/metadata/external-events/{code}       - Get external event
# ... and 18 more type-specific endpoints
```

### Complete Traceability Chain

The Knowledge Graph enables end-to-end traceability:

```
AnalyticsStrategy (maturity, governance)
  ↓ strategic_priorities
StrategicObjectives (business goals)
  ↓ aligned_use_cases
AnalyticsUseCases (problems to solve)
  ↓ required_data_sources, required_metrics
DataProducts (curated assets)
  ↓ included_metrics, source_entities
Metrics (KPIs)
  ↓ required_objects, data_sources
Entities (data models)
  ↓ table_schema
DataSources (raw data)

PLUS External Context:
ExternalEvents → affected_metrics, affected_entities, related_companies
```

---

## 📈 Layer 2: Analytics Model Layer (Active Business Data)

**Purpose**: Store **active business data** for real-time analytics and reporting

**Database**: TimescaleDB schema `analytics_data`

**What's Stored**:
- **Customer data** - Active customer records
- **Order data** - Recent order records
- **Product data** - Current product catalog
- **SCOR Process data** - Active SCOR process instances
- **SCOR Metric data** - Recent metric measurements
- **All other business entities** - Hot/active operational data

**Key Characteristics**:
- ✅ **Active data** - Recent, frequently accessed records
- ✅ **Dynamically created** - Tables generated from Layer 0 ontology
- ✅ **CQRS pattern** - Write models + Read models
- ✅ **TimescaleDB hypertables** - For time-series data with automatic partitioning
- ✅ **Analytics-ready** - Optimized for querying and reporting
- ✅ **Hot storage** - Fast access, higher cost

**Data Retention**:
- Recent data (e.g., last 90 days for high-frequency data)
- Actively queried records
- Real-time analytics workloads

**How Tables Are Created**:
```
Layer 0 Ontology (EntityDefinition) → CQRS Scripts → Layer 2 Tables
```

**Example Tables**:
```sql
-- CQRS Write Models
analytics_data.customers
analytics_data.scor_processes
analytics_data.scor_metrics

-- CQRS Read Models (optimized for queries)
analytics_data.customers_read
analytics_data.scor_processes_read
analytics_data.scor_metrics_read
```

---

## 🗄️ Layer 2a: Archive Layer (Historical Data Lake)

**Purpose**: Store **historical data** archived from Layer 2 for long-term retention and cost optimization

**Storage**: Azure Data Lake Storage Gen2 (ADLS Gen2)

**Service**: `archival_service` at `services/backend_services/archival_service`

**What's Stored**:
- **Archived TimescaleDB chunks** - Old data moved from Layer 2
- **Historical time-series data** - Aged-out metrics and measurements
- **Compliance data** - Long-term retention for regulatory requirements
- **Historical analytics** - Data for trend analysis over years

**Key Characteristics**:
- ✅ **Cold storage** - Infrequently accessed, low cost
- ✅ **Columnar format** - Parquet or Delta Lake for efficient storage
- ✅ **Compressed** - Optimized for storage efficiency
- ✅ **Queryable** - Can be queried via archival service API
- ✅ **Immutable** - Write-once, read-many pattern
- ✅ **Partitioned** - Organized by date hierarchy (year/month/day)

### Dual Archive Strategy

**Layer 2a contains TWO types of archived data:**

1. **Analytics Data Archive** (from Layer 2)
   - Transformed business data
   - Historical analytics queries
   - Performance metrics over time
   - Trend analysis

2. **Source Data Archive** (from Layer 3)
   - Original raw data as received
   - Preserves data lineage
   - Enables transformation replay
   - Audit trail for compliance

### Storage Format

```
Container: timescaledb-archive

/analytics_data/
  ├── analytics/              ← Transformed data from Layer 2
  │   ├── customers/
  │   │   └── 2024/
  │   │       └── 11/
  │   │           └── 01/
  │   │               └── chunk_12345.parquet
  │   ├── scor_metrics/
  │   │   └── 2024/
  │   │       └── 10/
  │   │           └── 15/
  │   │               └── chunk_67890.parquet
  │   └── orders/
  │       └── 2024/...
  │
  └── source/                 ← Raw data from Layer 3
      ├── customers/
      │   └── 2024/
      │       └── 11/
      │           └── 08/
      │               ├── source_batch_001.parquet
      │               └── source_batch_002.parquet
      ├── scor_metrics/
      │   └── 2024/
      │       └── 11/
      │           └── 08/
      │               └── source_batch_003.parquet
      └── orders/
          └── 2024/...
```

### Archival Process

1. **TimescaleDB chunk aging** - Chunks older than retention policy
2. **Archival event** - Published to Redis queue
3. **Archival service** - Extracts chunk data from TimescaleDB
4. **Data transformation** - Converts to Parquet/Delta format
5. **Upload to ADLS** - Writes to Azure Data Lake Storage
6. **Confirmation** - Publishes success event
7. **Chunk deletion** - TimescaleDB chunk can be dropped (optional)

### Retrieval Process

```python
# Query historical transformed data
archival_service.retrieve_archived_data(
    table_name="scor_metrics",
    data_type="analytics",  # or "source" for raw data
    start_time="2024-01-01",
    end_time="2024-01-31",
    columns=["metric_id", "value", "timestamp"]
)

# Query original source data for lineage/audit
archival_service.retrieve_archived_data(
    table_name="scor_metrics",
    data_type="source",  # Raw source data
    start_time="2024-11-01",
    end_time="2024-11-08"
)
```

---

## 🔄 Layer 3: Source Model Layer (Integration/Staging)

**Purpose**: Store **raw data ingested from source systems** before transformation

**Database**: TimescaleDB schema `integration_data`

**What's Stored**:
- **Source customer data** - Raw data from CRM systems
- **Source order data** - Raw data from ERP systems
- **Source product data** - Raw data from product catalogs
- **Source SCOR data** - Raw data from old SCOR service
- **All other source data** - Unprocessed integration data

**Key Characteristics**:
- ✅ **Raw/staging data** - As received from source systems
- ✅ **Temporary in Layer 3** - Data transformed and moved to Layer 2
- ✅ **Archived to Layer 2a** - Raw data preserved for lineage and audit
- ✅ **Integration layer** - Handles data ingestion
- ✅ **Real-time processing** - Continuous data flow (not batch)
- ✅ **Mapping/transformation** - ETL logic to Layer 2

**Example Tables**:
```sql
-- Staging tables (temporary in TimescaleDB)
integration_data.source_customers
integration_data.source_orders
integration_data.source_scor_processes
```

**Data Flow**:
```
External System → Integration Service → Layer 3 (staging) → 
Transformation/Mapping → Layer 2 (analytics)
       ↓
Layer 2a (archive source data for lineage/audit)
```

**Layer 3 Retention Policy**:
```python
{
    "layer": "source",
    "retention_in_timescaledb": "7 days",  # Keep in Layer 3 for 1 week
    "archive_to_layer_2a": true,           # Archive raw source data
    "archive_retention": "7 years",        # Keep in archive for compliance
    "archive_format": "parquet",           # Compressed columnar format
    "partition_by": "ingestion_date"       # Partition by when data arrived
}
```

---

## 🔄 Complete Data Flow

### End-to-End Journey of a Data Record

```
1. ONTOLOGY DEFINITION (Layer 0)
   ┌──────────────────────────┐
   │ Knowledge Graph:         │
   │ EntityDefinition         │
   │ - code: "CUSTOMER"       │
   │ - table_schema: {...}    │
   │ - relationships: [...]   │
   └────────┬─────────────────┘
            │ CQRS Scripts
            ▼

2. INGESTION (External → Layer 3)
   ┌─────────────┐
   │ CRM System  │
   └──────┬──────┘
          │ API/Integration
          ▼
   ┌─────────────────────┐
   │ Layer 3: source_    │
   │ customers (staging) │
   └──────┬──────────────┘
          │
          ├─────────────────────────────────┐
          │                                 │
          │ ETL/Mapping                     │ Archive Source
          ▼                                 ▼
   ┌─────────────────────┐         ┌──────────────────────┐
   │ Layer 2: customers  │         │ Layer 2a: source/    │
   │ (active analytics)  │         │ customers/2024/12/08/│
   └──────┬──────────────┘         │ raw_data.parquet     │
                                    │ (source lineage)     │
                                    └──────────────────────┘

3. ANALYTICS (Layer 2 queries)
          │ Real-time queries
          │ KPI calculations (using MetricDefinition from Layer 0)
          │ Dashboards
          ▼
   [Active for 90 days]

4. ARCHIVAL (Layer 2 → Layer 2a)
          │ Aging policy
          ▼
   ┌─────────────────────────┐
   │ Layer 2a: analytics/    │
   │ customers/2024/12/01/   │
   │ chunk.parquet           │
   │ (transformed data)      │
   └──────┬──────────────────┘

5. HISTORICAL ANALYTICS (Layer 2a queries)
          │ Historical trends
          │ Compliance reports
          │ Long-term analysis
          │ Data lineage tracking
          ▼
   [Both source & transformed data retained for 7+ years]
```

---

## 📊 Layer Comparison Matrix

| Aspect | Layer 0 | Layer 2 | Layer 2a | Layer 3 |
|--------|---------|---------|----------|---------|
| **Purpose** | Ontology & Metadata | Active analytics | Historical archive | Staging |
| **Data Type** | Definitions & Relationships | Business records | Source + Analytics archives | Raw data |
| **Storage** | TimescaleDB | TimescaleDB | Azure Data Lake | TimescaleDB |
| **Schema** | business_metadata | analytics_data | N/A | integration_data |
| **Format** | JSONB | PostgreSQL + Hypertables | Parquet/Delta | PostgreSQL |
| **Access Pattern** | Frequent | Frequent | Occasional | Temporary |
| **Query Speed** | Fast | Fast | Moderate | Fast |
| **Data Volume** | Small (MB-GB) | Medium (GB-TB) | Large (TB-PB) | Small (GB) |
| **Retention** | Permanent (versioned) | 30-90 days | 7+ years | 7 days |
| **Archived to 2a** | No | Yes | N/A | Yes (for lineage) |
| **Cost** | Low | Medium-High | Very Low | Low |
| **CQRS** | No | Yes | No | No |
| **Compression** | No | Minimal | High | No |
| **Versioning** | Yes (full history) | No | No | No |
| **Graph-based** | Yes | No | No | No |

---

## 🎯 Complete Example: Customer Analytics

### Layer 0: Customer Ontology Definition

```python
# EntityDefinition in Knowledge Graph
CUSTOMER_ENTITY = EntityDefinition(
    kind="entity_definition",
    id="Entity:CUSTOMER",
    code="CUSTOMER",
    name="Customer",
    description="Customer entity with demographics and behavior",
    table_schema=TableSchemaDefinition(
        table_name="customers",
        columns=[
            ColumnDefinition(name="customer_id", type="UUID", primary_key=True),
            ColumnDefinition(name="name", type="String(255)"),
            ColumnDefinition(name="email", type="String(255)"),
            ColumnDefinition(name="country_code", type="String(2)"),
            ColumnDefinition(name="created_at", type="DateTime"),
            ColumnDefinition(name="lifetime_value", type="Decimal(10,2)")
        ]
    ),
    relationships=[
        RelationshipDefinition(
            kind="relationship_definition",
            from_entity="CUSTOMER",
            to_entity="ORDER",
            relationship_type="places",
            from_cardinality="1",
            to_cardinality="0..*"
        ),
        RelationshipDefinition(
            kind="relationship_definition",
            from_entity="CUSTOMER",
            to_entity="COUNTRY",
            relationship_type="located_in",
            from_cardinality="*",
            to_cardinality="1"
        )
    ]
)

# MetricDefinition in Knowledge Graph
CUSTOMER_LTV = MetricDefinition(
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
    dimensions=["country", "customer_segment", "acquisition_channel"],
    metric_category="FINANCIAL",
    data_sources=["CRM_SYSTEM", "ORDER_SYSTEM"]
)

# AnalyticsUseCaseDefinition in Knowledge Graph
CUSTOMER_SEGMENTATION = AnalyticsUseCaseDefinition(
    kind="analytics_use_case_definition",
    code="CUSTOMER_SEGMENTATION",
    name="Customer Segmentation Analysis",
    use_case_type="reporting",
    business_problem="Identify high-value customer segments for targeted marketing",
    expected_value="20% increase in marketing ROI",
    success_metrics=["CUSTOMER_LTV", "CUSTOMER_RETENTION_RATE"],
    required_data_sources=["CRM_SYSTEM"],
    required_entities=["CUSTOMER", "ORDER"],
    required_metrics=["CUSTOMER_LTV", "CUSTOMER_RETENTION_RATE"],
    business_owner="MARKETING_VP",
    technical_owner="DATA_TEAM_LEAD",
    maturity_stage="production"
)
```

### Layer 2: Active Customer Data (Last 90 Days)

```sql
-- Active customers in TimescaleDB
SELECT * FROM analytics_data.customers
WHERE created_at > NOW() - INTERVAL '90 days';

-- Example: Recent customer
customer_id: "550e8400-e29b-41d4-a716-446655440000"
name: "Acme Corporation"
email: "contact@acme.com"
country_code: "US"
created_at: 2024-12-08 10:00:00
lifetime_value: 125000.00
```

### Layer 2a: Archived Customer Data (Historical)

**Two Archive Types in Layer 2a:**

**1. Analytics Data Archive** (from Layer 2):
```
Azure Data Lake:
/timescaledb-archive/analytics_data/analytics/customers/
  /2024/
    /01/  ← January transformed data
      /15/
        chunk_12345.parquet  (transformed analytics data)
    /02/  ← February transformed data
      /20/
        chunk_12346.parquet
```

**2. Source Data Archive** (from Layer 3):
```
Azure Data Lake:
/timescaledb-archive/analytics_data/source/customers/
  /2024/
    /12/  ← December raw source data
      /08/
        source_batch_001.parquet  (original raw data from CRM)
        source_batch_002.parquet
```

### Layer 3: Source Customer Data (Staging)

```sql
-- Raw data from CRM system (temporary in Layer 3)
INSERT INTO integration_data.source_customers
VALUES (
    raw_id: "crm_12345",
    raw_data: '{"customer_name": "Acme Corp", "email": "contact@acme.com", ...}',
    ingested_at: NOW(),
    processed: false
);

-- Parallel operations:
-- 1. ETL transforms to Layer 2 format
-- 2. Archive raw data to Layer 2a for lineage
-- 3. Mark processed: true
-- 4. Delete from Layer 3 after 7 days
```

---

## 🔑 Key Relationships Between Layers

### Layer 0 → Layer 2
- **Ontology → Implementation**
- CQRS scripts read `EntityDefinition.table_schema` from Layer 0
- Generate SQLAlchemy models and Alembic migrations
- Create tables in Layer 2
- **MetricDefinition** drives KPI calculation engine

### Layer 2 ↔ Layer 2a
- **Active ↔ Archive**
- Archival service monitors TimescaleDB chunk age
- Moves old chunks from Layer 2 to Layer 2a
- Can retrieve archived data back for queries
- **Bidirectional** but asymmetric (write to 2a, read from both)

### Layer 3 → Layer 2 (and Layer 2a)
- **Source → Target (with lineage preservation)**
- ETL processes transform raw data
- Map source schema to analytics schema (defined in Layer 0)
- Load into Layer 2 tables
- **Simultaneously archive source data to Layer 2a**
- **Dual flow**: Transform to Layer 2 + Archive to Layer 2a

### Layer 0 ← → Layer 2 ← → Layer 2a
- **Schema consistency**
- Layer 0 defines ontology and schema
- Layer 2 implements schema
- Layer 2a archives data in same schema (but different format)
- Schema changes propagate through all layers

---

## 🚀 Benefits of This Architecture

### 1. **Unified Ontology** ⭐ NEW
- Single source of truth for all business concepts
- Graph-based relationships enable complex queries
- Versioned metadata with full history
- Type-safe Pydantic models with validation
- RESTful API for all metadata operations

### 2. **Complete Traceability**
- AnalyticsStrategy → StrategicObjectives → UseCases → Metrics → Entities → DataSources
- External events linked to affected metrics and entities
- Full data lineage from source to analytics
- Audit trail for compliance

### 3. **Cost Optimization**
- Hot data (Layer 2) on expensive fast storage
- Cold data (Layer 2a) on cheap object storage
- 90% cost reduction for historical data
- Source data archived immediately (no long-term Layer 3 storage costs)

### 4. **Performance**
- Layer 2 stays lean (only recent data)
- Fast queries on active data
- Historical queries still possible via Layer 2a
- Layer 3 stays small (7-day retention only)
- Redis caching for Layer 0 metadata

### 5. **Scalability**
- Layer 2a can store unlimited data
- No database size constraints
- Horizontal scaling via partitioning
- Both source and analytics data scale independently
- Knowledge Graph scales with business complexity

### 6. **Compliance & Audit**
- Long-term retention (7+ years) in Layer 2a
- **Complete data lineage** - Source data preserved
- **Audit trail** - Track transformations from source to analytics
- Regulatory compliance (SOX, GDPR, HIPAA, etc.)
- **Immutable source records** - Original data never modified
- Row-level security and data masking in Layer 0

### 7. **Data Quality & Recoverability**
- **Replay transformations** - Reprocess from archived source data
- **Root cause analysis** - Investigate data quality issues
- **Disaster recovery** - Rebuild analytics from source
- **Transformation validation** - Compare source vs transformed
- **Bug fixes** - Correct transformation logic and reprocess
- Data quality rules defined in Layer 0

### 8. **Flexibility**
- Multiple storage formats (Parquet, Delta)
- Can query across layers
- Time travel with Delta Lake
- **Dual archives** - Source and analytics data separately queryable
- Extensible ontology for new business concepts

### 9. **Business Context**
- Geographic and industry classification
- External events and market conditions
- Analytics strategy and maturity tracking
- Use case management and prioritization
- Benchmark comparisons

---

## 🎯 Current Status

### Layer 0: ✅ COMPLETE
- **26 ontology classes** defined in `ontology_models.py`
- **business_metadata service** deployed with FastAPI
- **RESTful API** with 30+ endpoints
- **Version tracking** and history
- **Redis caching** enabled
- **PostgreSQL JSONB** storage
- Ready to drive Layer 2 creation

### Layer 2: ⏳ NEXT STEP
- Need to create tables from Layer 0 ontology
- Run CQRS scripts for entity tables
- Apply Alembic migrations
- Implement CQRS read/write models

### Layer 2a: ✅ OPERATIONAL
- Archival service deployed and running
- Azure Data Lake Storage configured
- Parquet/Delta Lake support enabled
- Dual archive strategy (analytics + source)
- Ready to archive Layer 2 data

### Layer 3: 🔮 FUTURE
- Will be created when integrations are built
- Handles data ingestion from external systems
- Maps to Layer 2 analytics tables
- Immediate archival to Layer 2a for lineage

---

## 📋 Service Locations

```
services/business_services/
├── business_metadata/              ← Layer 0: Knowledge Graph
│   ├── api/metadata_api.py
│   ├── services/
│   │   ├── metadata_service.py
│   │   └── metadata_instantiation_service.py
│   ├── repositories/metadata_repository.py
│   ├── models/
│   │   ├── metadata_definition.py
│   │   └── metadata_version.py
│   └── main.py
│
└── analytics_metadata_service/
    └── definitions/
        └── ontology_models.py      ← Pydantic ontology definitions

services/backend_services/
└── archival_service/               ← Layer 2a: Archive
    ├── lakehouse_client.py
    ├── archival_processor.py
    ├── management.py
    └── tasks.py
```

---

## 🎉 Summary

**Four-layer architecture with Knowledge Graph ontology provides:**

- ✅ **Layer 0** - Knowledge Graph ontology (unified metadata, 26 classes in 5 layers)
  - Core Ontology (6 classes)
  - Business Ontology (8 classes including ValueChainPatternDefinition and ExternalEventDefinition)
  - Authorization & Access Control (8 classes)
  - Geographic & Industry Classification (4 classes)
  - Analytics Strategy & Data Management (7 classes)
- ✅ **Layer 2** - Active analytics data (hot storage, 30-90 days)
- ✅ **Layer 2a** - Archived data (cold storage, 7+ years)
  - Analytics data archive (from Layer 2)
  - Source data archive (from Layer 3) for lineage & audit
- ✅ **Layer 3** - Source/staging data (integration, 7 days)

**Complete data lifecycle with ontology-driven design**:
```
Layer 0 (Knowledge Graph Ontology)
    ↓ defines structure
External System → Layer 3 (staging) ──┬→ Layer 2 (active) → Layer 2a (analytics archive)
                  [7 days]            │  [30-90 days]       [7+ years]
                                      │
                                      └→ Layer 2a (source archive)
                                         [7+ years - lineage preservation]
```

**Key Innovations**: 
- **Knowledge Graph ontology** - Unified, versioned, graph-based metadata
- **26 ontology classes** - Complete business, authorization, geography, and strategy
- **Dual archival strategy** - Complete data lineage preservation
- **End-to-end traceability** - From strategy to data sources
- **External context** - News and events impact analysis

**This architecture enables:**
- 💰 Cost-effective storage
- 📊 Scalable analytics
- 🔒 Regulatory compliance
- 🔍 Complete data lineage
- 🔄 Transformation recoverability
- 📈 Historical trend analysis
- 🎯 Strategy-driven analytics
- 🌍 Geographic and industry segmentation
- 📰 External event impact tracking

**Enterprise-grade data platform with Knowledge Graph foundation!** 🚀
