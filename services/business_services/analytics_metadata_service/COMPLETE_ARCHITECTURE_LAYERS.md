# Complete Data Architecture: Layers 1, 2, 2a, and 3

**Date**: November 8, 2025  
**Status**: Comprehensive architecture documentation including archival layer

---

## 🏗️ Four-Layer Architecture Overview

The analytics platform uses a **four-layer data architecture** that separates metadata, active analytics data, archived data, and source data into distinct layers with clear responsibilities.

```
┌─────────────────────────────────────────────────────────────────┐
│ Layer 1: METADATA (Definitions)                                │
│ ├─ Modules, Object Models, KPIs, Benchmarks                    │
│ ├─ Location: TimescaleDB (analytics_service schema)            │
│ └─ Purpose: Define structure and relationships                  │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼ CQRS Scripts (table creation)
┌─────────────────────────────────────────────────────────────────┐
│ Layer 2: ANALYTICS MODEL (Active Business Data)                │
│ ├─ Customers, Orders, Products, SCOR Processes, etc.           │
│ ├─ Location: TimescaleDB (analytics_service schema)            │
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
│ ├─ Location: TimescaleDB (analytics_service schema)            │
│ ├─ Format: PostgreSQL staging tables                           │
│ └─ Purpose: Temporary staging for data transformation          │
└─────────────────────────────────────────────────────────────────┘
                            ▲
                            │ Integration Services
                    External Systems (CRM, ERP, etc.)
```

---

## 📊 Layer 1: Metadata Layer (Definition Layer)

**Purpose**: Store the **definitions and schemas** that describe the data structure

**Database**: TimescaleDB schema `analytics_service` (metadata tables)

**What's Stored**:
- **Industries** - Industry classifications
- **Value Chains** - Business value chain definitions
- **Modules** - Analytics module definitions (e.g., ASCM_SCOR, CUSTOMER_RETENTION)
- **Object Models** - Generic container for ALL object type definitions
- **Object Attributes** - Generic attributes for any object
- **KPIs** - KPI definitions and formulas
- **Benchmarks** - Industry benchmark data
- **Clients** - Client configurations
- **Association Tables** - Many-to-many relationships

**Key Characteristics**:
- ✅ **Metadata only** - No actual business data
- ✅ **Definitions** - Describes what CAN exist
- ✅ **Schema definitions** - JSON `table_schema` for each object model
- ✅ **Relationships** - UML diagrams showing how objects relate
- ✅ **Already exists** - These tables are in `db_models.py`

**Storage Location**:
```
services/business_services/analytics_models/
├── db_models.py              ← Layer 1 SQLAlchemy models
├── definitions/
│   ├── modules/              ← Module definitions
│   ├── object_models/        ← Object model definitions (with table_schema)
│   ├── kpis/                 ← KPI definitions
│   └── benchmarks/           ← Benchmark definitions
```

---

## 📈 Layer 2: Analytics Model Layer (Active Business Data)

**Purpose**: Store **active business data** for real-time analytics and reporting

**Database**: TimescaleDB schema `analytics_service` (analytics tables)

**What's Stored**:
- **Customer data** - Active customer records
- **Order data** - Recent order records
- **Product data** - Current product catalog
- **SCOR Process data** - Active SCOR process instances
- **SCOR Metric data** - Recent metric measurements
- **All other business entities** - Hot/active operational data

**Key Characteristics**:
- ✅ **Active data** - Recent, frequently accessed records
- ✅ **Dynamically created** - Tables generated from Layer 1 definitions
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
Layer 1 Definition → CQRS Scripts → Layer 2 Tables
```

**Example Tables**:
```sql
-- CQRS Write Models
analytics_service.customers
analytics_service.scor_processes
analytics_service.scor_metrics

-- CQRS Read Models (optimized for queries)
analytics_service.customers_read
analytics_service.scor_processes_read
analytics_service.scor_metrics_read
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

**Storage Format**:
```
Container: timescaledb-archive
Format: Parquet (default) or Delta Lake
Structure:
  /analytics_service/
    /customers/
      /2024/
        /01/
          /15/
            chunk_12345.parquet
            chunk_12346.parquet
    /scor_metrics/
      /2024/
        /11/
          /01/
            chunk_78901.parquet
```

**Archival Process**:
1. **TimescaleDB chunk aging** - Chunks older than retention policy
2. **Archival event** - Published to Redis queue
3. **Archival service** - Extracts chunk data from TimescaleDB
4. **Data transformation** - Converts to Parquet/Delta format
5. **Upload to ADLS** - Writes to Azure Data Lake Storage
6. **Confirmation** - Publishes success event
7. **Chunk deletion** - TimescaleDB chunk can be dropped (optional)

**Retrieval Process**:
```python
# Via archival service API
GET /api/v1/retrieve
{
  "table_name": "scor_metrics",
  "start_time": "2024-01-01T00:00:00Z",
  "end_time": "2024-01-31T23:59:59Z",
  "columns": ["metric_id", "value", "timestamp"]
}

# Returns: Parquet file or DataFrame
```

**Configuration** (from `config.py`):
```python
# Azure Data Lake Storage
storage_account: str = "devstoreaccount1"
container_name: str = "timescaledb-archive"
default_format: str = "parquet"  # or "delta"

# Archival settings
max_concurrent_archival_tasks: int = 5
chunk_batch_size: int = 10
auto_archival_enabled: bool = True
```

**Benefits**:
- 💰 **Cost savings** - 90% cheaper than hot storage
- 📊 **Historical analytics** - Access to years of data
- 🔒 **Compliance** - Long-term retention (7+ years)
- 🚀 **Performance** - Keeps Layer 2 lean and fast
- 📈 **Scalability** - Unlimited storage capacity

---

## 🔄 Layer 3: Source Model Layer (Integration/Staging)

**Purpose**: Store **raw data ingested from source systems** before transformation

**Database**: TimescaleDB schema `analytics_service` (source tables)

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
analytics_service.source_customers
analytics_service.source_orders
analytics_service.source_scor_processes
```

**Data Flow**:
```
External System → Integration Service → Layer 3 (staging) → 
Transformation/Mapping → Layer 2 (analytics)
       ↓
Layer 2a (archive source data for lineage/audit)
```

**Archival of Layer 3 Data**:
- ✅ **Complete lineage transparency** - Track data from source to analytics
- ✅ **Audit compliance** - Preserve original source data for audits
- ✅ **Recoverability** - Replay transformations if needed
- ✅ **Data quality forensics** - Investigate transformation issues
- ✅ **Regulatory compliance** - Maintain source data for SOX, GDPR, etc.

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
1. INGESTION (External → Layer 3)
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
   │ (active analytics)  │         │ customers/2024/11/08/│
   └──────┬──────────────┘         │ raw_data.parquet     │
                                    │ (source lineage)     │
                                    └──────────────────────┘

2. ANALYTICS (Layer 2 queries)
          │ Real-time queries
          │ KPI calculations
          │ Dashboards
          ▼
   [Active for 90 days]

3. ARCHIVAL (Layer 2 → Layer 2a)
          │ Aging policy
          ▼
   ┌─────────────────────────┐
   │ Layer 2a: analytics/    │
   │ customers/2024/11/01/   │
   │ chunk.parquet           │
   │ (transformed data)      │
   └──────┬──────────────────┘

4. HISTORICAL ANALYTICS (Layer 2a queries)
          │ Historical trends
          │ Compliance reports
          │ Long-term analysis
          │ Data lineage tracking
          ▼
   [Both source & transformed data retained for 7+ years]
```

### Dual Archive Strategy

**Layer 2a now contains TWO types of archived data:**

1. **Source Data Archive** (from Layer 3)
   - Original raw data as received
   - Preserves data lineage
   - Enables transformation replay
   - Audit trail for compliance

2. **Analytics Data Archive** (from Layer 2)
   - Transformed business data
   - Historical analytics queries
   - Performance metrics over time
   - Trend analysis

---

## 📊 Layer Comparison Matrix

| Aspect | Layer 1 | Layer 2 | Layer 2a | Layer 3 |
|--------|---------|---------|----------|---------|
| **Purpose** | Definitions | Active analytics | Historical archive | Staging |
| **Data Type** | Metadata | Business records | Source + Analytics archives | Raw data |
| **Storage** | TimescaleDB | TimescaleDB | Azure Data Lake | TimescaleDB |
| **Format** | PostgreSQL | PostgreSQL + Hypertables | Parquet/Delta | PostgreSQL |
| **Access Pattern** | Rare | Frequent | Occasional | Temporary |
| **Query Speed** | Fast | Fast | Moderate | Fast |
| **Data Volume** | Small (KB-MB) | Medium (GB-TB) | Large (TB-PB) | Small (GB) |
| **Retention** | Permanent | 30-90 days | 7+ years | 7 days |
| **Archived to 2a** | No | Yes | N/A | Yes (for lineage) |
| **Cost** | Low | Medium-High | Very Low | Low |
| **CQRS** | No | Yes | No | No |
| **Compression** | No | Minimal | High | No |
| **Partitioning** | No | Time-based | Date hierarchy | No |

---

## 🎯 SCOR Example Across All Layers

### Layer 1: SCOR Definitions
```python
# Module definition
ASCM_SCOR = Module(code="ASCM_SCOR", ...)

# Object model with table_schema
SCOR_METRIC = ObjectModel(
    code="SCOR_METRIC",
    table_schema={
        "table_name": "scor_metrics",
        "columns": [...]
    }
)
```

### Layer 2: Active SCOR Metrics (Last 90 Days)
```sql
-- Active metrics in TimescaleDB
SELECT * FROM analytics_service.scor_metrics
WHERE timestamp > NOW() - INTERVAL '90 days';

-- Example: Recent supply chain performance
metric_id: "SCOR.P1.1.CYCLE_TIME"
value: 2.5
timestamp: 2024-11-08 13:00:00
```

### Layer 2a: Archived SCOR Data (Historical)

**Two Archive Types in Layer 2a:**

**1. Analytics Data Archive** (from Layer 2):
```
Azure Data Lake:
/timescaledb-archive/analytics_service/analytics/scor_metrics/
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
/timescaledb-archive/analytics_service/source/scor_metrics/
  /2024/
    /11/  ← November raw source data
      /08/
        source_batch_001.parquet  (original raw data from old SCOR service)
        source_batch_002.parquet
```

**Retrieval**:
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

### Layer 3: Source SCOR Data (Staging)
```sql
-- Raw data from old SCOR service (temporary in Layer 3)
INSERT INTO analytics_service.source_scor_metrics
VALUES (
    raw_id: "old_scor_12345",
    raw_data: '{"metric": "cycle_time", "val": 2.5, ...}',
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

### Layer 1 → Layer 2
- **Definition → Implementation**
- CQRS scripts read `table_schema` from Layer 1
- Generate SQLAlchemy models and Alembic migrations
- Create tables in Layer 2

### Layer 2 ↔ Layer 2a
- **Active ↔ Archive**
- Archival service monitors TimescaleDB chunk age
- Moves old chunks from Layer 2 to Layer 2a
- Can retrieve archived data back for queries
- **Bidirectional** but asymmetric (write to 2a, read from both)

### Layer 3 → Layer 2 (and Layer 2a)
- **Source → Target (with lineage preservation)**
- ETL processes transform raw data
- Map source schema to analytics schema
- Load into Layer 2 tables
- **Simultaneously archive source data to Layer 2a**
- **Dual flow**: Transform to Layer 2 + Archive to Layer 2a

### Layer 1 ← → Layer 2 ← → Layer 2a
- **Schema consistency**
- Layer 1 defines schema
- Layer 2 implements schema
- Layer 2a archives data in same schema (but different format)
- Schema changes propagate through all layers

---

## 📋 Archival Service Details

**Location**: `services/backend_services/archival_service`

**Key Components**:
1. **`lakehouse_client.py`** - Azure Data Lake Storage client
2. **`archival_processor.py`** - Chunk extraction and archival logic
3. **`management.py`** - Archival policy management
4. **`tasks.py`** - Background archival tasks
5. **`config.py`** - Configuration settings

**Supported Formats**:
- ✅ **Parquet** - Columnar, compressed, fast queries (default)
- ✅ **Delta Lake** - ACID transactions, time travel, versioning
- ✅ **JSON** - Human-readable, debugging

**API Endpoints**:
```
POST /api/v1/archive        - Trigger manual archival
GET  /api/v1/retrieve       - Retrieve archived data
GET  /api/v1/status         - Check archival status
GET  /api/v1/policies       - List archival policies
POST /api/v1/policies       - Create archival policy
```

**Archival Policies**:
```python
{
    "table_name": "scor_metrics",
    "retention_days": 90,        # Keep in Layer 2 for 90 days
    "archive_format": "parquet",
    "compression": "snappy",
    "partition_by": "day"
}
```

---

## 🎯 Current Status

### Layer 1: ✅ COMPLETE
- All 88 object models restructured with `table_schema`
- SCOR module and object models defined
- Ready for Layer 2 creation

### Layer 2: ⏳ NEXT STEP
- Need to create tables from Layer 1 definitions
- Run CQRS scripts for SCOR tables
- Apply Alembic migrations

### Layer 2a: ✅ OPERATIONAL
- Archival service deployed and running
- Azure Data Lake Storage configured
- Parquet/Delta Lake support enabled
- Ready to archive Layer 2 data

### Layer 3: 🔮 FUTURE
- Will be created when integrations are built
- Handles data ingestion from external systems
- Maps to Layer 2 analytics tables

---

## 🚀 Benefits of This Architecture

### 1. **Cost Optimization**
- Hot data (Layer 2) on expensive fast storage
- Cold data (Layer 2a) on cheap object storage
- 90% cost reduction for historical data
- Source data archived immediately (no long-term Layer 3 storage costs)

### 2. **Performance**
- Layer 2 stays lean (only recent data)
- Fast queries on active data
- Historical queries still possible via Layer 2a
- Layer 3 stays small (7-day retention only)

### 3. **Scalability**
- Layer 2a can store unlimited data
- No database size constraints
- Horizontal scaling via partitioning
- Both source and analytics data scale independently

### 4. **Compliance & Audit**
- Long-term retention (7+ years) in Layer 2a
- **Complete data lineage** - Source data preserved
- **Audit trail** - Track transformations from source to analytics
- Regulatory compliance (SOX, GDPR, HIPAA, etc.)
- **Immutable source records** - Original data never modified

### 5. **Data Quality & Recoverability**
- **Replay transformations** - Reprocess from archived source data
- **Root cause analysis** - Investigate data quality issues
- **Disaster recovery** - Rebuild analytics from source
- **Transformation validation** - Compare source vs transformed
- **Bug fixes** - Correct transformation logic and reprocess

### 6. **Flexibility**
- Multiple storage formats (Parquet, Delta)
- Can query across layers
- Time travel with Delta Lake
- **Dual archives** - Source and analytics data separately queryable

### 7. **Separation of Concerns**
- Layer 1: What can exist (definitions)
- Layer 2: What does exist (active data)
- Layer 2a: What did exist (historical data) + What was received (source lineage)
- Layer 3: What's coming in (staging - temporary)

### 8. **Complete Lineage Transparency** ⭐ NEW
- **End-to-end traceability** - From external system to analytics
- **Source preservation** - Original data format retained
- **Transformation history** - Track how data evolved
- **Compliance reporting** - Prove data authenticity
- **Forensic analysis** - Investigate discrepancies at any point in pipeline

---

## 🎉 Summary

**Four-layer architecture provides:**
- ✅ **Layer 1** - Metadata and definitions
- ✅ **Layer 2** - Active analytics data (hot storage, 30-90 days)
- ✅ **Layer 2a** - Archived data (cold storage, 7+ years)
  - Analytics data archive (from Layer 2)
  - Source data archive (from Layer 3) ⭐ **For lineage & audit**
- ✅ **Layer 3** - Source/staging data (integration, 7 days)

**Complete data lifecycle with lineage preservation**:
```
External System → Layer 3 (staging) ──┬→ Layer 2 (active) → Layer 2a (analytics archive)
                  [7 days]            │  [30-90 days]       [7+ years]
                                      │
                                      └→ Layer 2a (source archive)
                                         [7+ years - lineage preservation]
```

**Key Innovation**: 
- **Dual archival strategy** ensures complete data lineage
- **Source data preserved** for audit, compliance, and recoverability
- **Analytics data archived** for historical analysis
- **Both accessible** via archival service API

**This architecture enables:**
- 💰 Cost-effective storage
- 📊 Scalable analytics
- 🔒 Regulatory compliance
- 🔍 Complete data lineage
- 🔄 Transformation recoverability
- 📈 Historical trend analysis

**Enterprise-grade data platform with full transparency and auditability!** 🚀
