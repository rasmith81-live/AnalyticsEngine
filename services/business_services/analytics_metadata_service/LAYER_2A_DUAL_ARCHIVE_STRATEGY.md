# Layer 2a: Dual Archive Strategy

**Date**: November 8, 2025  
**Purpose**: Document the dual archival strategy for complete data lineage

---

## 🎯 Overview

**Layer 2a (Archive Layer)** stores TWO types of archived data:

1. **Analytics Data Archive** - Transformed data from Layer 2
2. **Source Data Archive** - Raw data from Layer 3 ⭐ **NEW**

---

## 📊 Dual Archive Structure

```
Azure Data Lake Storage Gen2
Container: timescaledb-archive

/analytics_service/
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
  └── source/                 ← Raw data from Layer 3 (NEW!)
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

---

## 🔄 Data Flow with Dual Archival

```
┌─────────────────────────────────────────────────────────────┐
│ External System (CRM, ERP, Old SCOR Service)               │
└────────────────────┬────────────────────────────────────────┘
                     │ Integration API
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ LAYER 3: source_customers (TimescaleDB)                    │
│ - Raw data as received                                      │
│ - Temporary staging (7 days)                                │
└────────┬────────────────────────────────────┬───────────────┘
         │                                    │
         │ ETL/Transform                      │ Archive Source
         │                                    │ (Immediate)
         ▼                                    ▼
┌─────────────────────────┐    ┌──────────────────────────────┐
│ LAYER 2: customers      │    │ LAYER 2a: source/customers/  │
│ - Transformed data      │    │ - Original raw data          │
│ - Active (90 days)      │    │ - Lineage preservation       │
└────────┬────────────────┘    │ - Audit trail                │
         │                     │ - Retained 7+ years          │
         │ Age out             └──────────────────────────────┘
         │ (90 days)
         ▼
┌─────────────────────────────────────────────────────────────┐
│ LAYER 2a: analytics/customers/                              │
│ - Archived transformed data                                 │
│ - Historical analytics                                      │
│ - Retained 7+ years                                         │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 Why Archive Layer 3 Source Data?

### 1. **Complete Lineage Transparency** 🔍
- Track data from original source to final analytics
- Prove data authenticity for audits
- Document transformation history

### 2. **Audit Compliance** 🔒
- SOX, GDPR, HIPAA requirements
- Immutable source records
- Regulatory reporting

### 3. **Recoverability** 🔄
- Replay transformations if bugs found
- Rebuild analytics from source
- Disaster recovery capability

### 4. **Data Quality Forensics** 🔬
- Investigate discrepancies
- Compare source vs transformed
- Root cause analysis

### 5. **Transformation Validation** ✅
- Verify ETL logic correctness
- Test new transformation rules
- A/B test different mappings

---

## 📋 Archival Policies

### Analytics Data (Layer 2 → Layer 2a)
```python
{
    "source_layer": "layer_2",
    "archive_type": "analytics",
    "table_name": "scor_metrics",
    "retention_in_layer_2": "90 days",
    "archive_after": "90 days",
    "archive_retention": "7 years",
    "archive_format": "parquet",
    "compression": "snappy",
    "partition_by": "day"
}
```

### Source Data (Layer 3 → Layer 2a) ⭐ NEW
```python
{
    "source_layer": "layer_3",
    "archive_type": "source",
    "table_name": "source_scor_metrics",
    "retention_in_layer_3": "7 days",
    "archive_after": "immediate",  # Archive as soon as processed
    "archive_retention": "7 years",
    "archive_format": "parquet",
    "compression": "snappy",
    "partition_by": "ingestion_date",
    "preserve_raw_format": true
}
```

---

## 🔍 Querying Archived Data

### Query Analytics Archive
```python
# Historical analytics data (transformed)
result = archival_service.retrieve_archived_data(
    table_name="scor_metrics",
    data_type="analytics",
    start_time="2024-01-01T00:00:00Z",
    end_time="2024-01-31T23:59:59Z",
    columns=["metric_id", "value", "timestamp", "process_id"]
)
```

### Query Source Archive (Lineage)
```python
# Original source data (raw)
result = archival_service.retrieve_archived_data(
    table_name="scor_metrics",
    data_type="source",
    start_time="2024-11-01T00:00:00Z",
    end_time="2024-11-08T23:59:59Z",
    columns=["raw_id", "raw_data", "ingested_at"]
)
```

### Compare Source vs Analytics
```python
# Lineage analysis - compare original vs transformed
source_data = archival_service.retrieve_archived_data(
    table_name="scor_metrics",
    data_type="source",
    start_time="2024-11-01",
    end_time="2024-11-01"
)

analytics_data = archival_service.retrieve_archived_data(
    table_name="scor_metrics",
    data_type="analytics",
    start_time="2024-11-01",
    end_time="2024-11-01"
)

# Validate transformation
validate_transformation(source_data, analytics_data)
```

---

## 💡 Use Cases

### 1. **Audit Investigation**
```
Auditor: "Show me the original data received on 2024-03-15"
→ Query Layer 2a source archive
→ Retrieve raw data as it was received
→ Prove data authenticity
```

### 2. **Transformation Bug Fix**
```
Developer: "We found a bug in the ETL logic from last month"
→ Query Layer 2a source archive for affected period
→ Fix transformation logic
→ Replay transformation on archived source data
→ Update Layer 2 analytics data
```

### 3. **Data Quality Investigation**
```
Analyst: "Why is this metric showing unexpected values?"
→ Query Layer 2a analytics archive (transformed data)
→ Query Layer 2a source archive (raw data)
→ Compare source vs transformed
→ Identify transformation issue or source data problem
```

### 4. **Compliance Reporting**
```
Compliance Officer: "Prove data lineage for regulatory audit"
→ Show source data in Layer 2a source archive
→ Show transformation logic in code
→ Show analytics data in Layer 2a analytics archive
→ Complete end-to-end lineage documented
```

### 5. **Disaster Recovery**
```
DBA: "Layer 2 database corrupted, need to rebuild"
→ Query Layer 2a source archive for all raw data
→ Replay all transformations
→ Rebuild Layer 2 analytics tables
→ Full recovery from source
```

---

## 📊 Storage Comparison

| Aspect | Analytics Archive | Source Archive |
|--------|------------------|----------------|
| **Source** | Layer 2 (transformed) | Layer 3 (raw) |
| **Format** | Parquet (columnar) | Parquet (preserves raw structure) |
| **Purpose** | Historical analytics | Lineage & audit |
| **Partition** | By timestamp | By ingestion_date |
| **Compression** | High (snappy) | High (snappy) |
| **Query Pattern** | Trend analysis | Forensic analysis |
| **Retention** | 7+ years | 7+ years |
| **Size** | Larger (more columns) | Smaller (raw only) |
| **Update** | Immutable | Immutable |

---

## 🔑 Key Benefits

### Cost Optimization
- ✅ Layer 3 only keeps 7 days (minimal database storage)
- ✅ Source data archived to cheap object storage
- ✅ 90% cost reduction vs keeping in TimescaleDB

### Complete Lineage
- ✅ Source data preserved forever
- ✅ Transformation history documented
- ✅ End-to-end traceability

### Compliance & Audit
- ✅ Immutable source records
- ✅ Regulatory compliance (SOX, GDPR, HIPAA)
- ✅ Audit trail from source to analytics

### Recoverability
- ✅ Replay transformations
- ✅ Disaster recovery
- ✅ Bug fixes without data loss

### Data Quality
- ✅ Root cause analysis
- ✅ Transformation validation
- ✅ Source vs analytics comparison

---

## 🚀 Implementation

### Archival Service Configuration
```python
# config.py
ARCHIVAL_POLICIES = [
    {
        "name": "analytics_data_archival",
        "source_layer": "layer_2",
        "archive_type": "analytics",
        "retention_days": 90,
        "archive_format": "parquet"
    },
    {
        "name": "source_data_archival",  # NEW!
        "source_layer": "layer_3",
        "archive_type": "source",
        "retention_days": 7,
        "archive_immediately": true,  # Archive as soon as processed
        "archive_format": "parquet",
        "preserve_raw_format": true
    }
]
```

### ETL Process with Dual Archival
```python
async def process_source_data(source_record):
    """Process source data with dual archival."""
    
    # 1. Store in Layer 3 (temporary)
    await db.execute(
        "INSERT INTO source_customers VALUES (...)"
    )
    
    # 2. Archive source data to Layer 2a (immediate)
    await archival_service.archive_source_data(
        table_name="source_customers",
        data=source_record,
        archive_type="source"
    )
    
    # 3. Transform to Layer 2 format
    transformed = transform_customer_data(source_record)
    
    # 4. Insert into Layer 2 (analytics)
    await db.execute(
        "INSERT INTO customers VALUES (...)"
    )
    
    # 5. Mark source as processed
    await db.execute(
        "UPDATE source_customers SET processed = true WHERE id = ..."
    )
    
    # Note: Layer 2 data will be archived to Layer 2a after 90 days
```

---

## 🎯 Summary

**Dual Archive Strategy provides:**

1. **Analytics Archive** (Layer 2 → Layer 2a)
   - Historical analytics data
   - Trend analysis
   - Performance metrics over time

2. **Source Archive** (Layer 3 → Layer 2a) ⭐ **NEW**
   - Original raw data
   - Complete lineage
   - Audit compliance
   - Transformation recoverability

**Result**: Enterprise-grade data platform with:
- 💰 Cost optimization
- 🔍 Complete transparency
- 🔒 Regulatory compliance
- 🔄 Full recoverability
- 📊 Historical analytics

**Both archives accessible via archival service API for complete data lifecycle management!** 🚀
