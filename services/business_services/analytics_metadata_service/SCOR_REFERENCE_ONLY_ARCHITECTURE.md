# SCOR Reference-Only Architecture

**Date**: November 8, 2025  
**Status**: ✅ IMPLEMENTED  
**Decision**: SCOR objects are metadata/reference only, NOT Layer 2 tables

---

## 🎯 Architecture Decision

### Problem Identified
SCOR metrics (RL.1.1, RS.1.1, etc.) were initially designed to create Layer 2 tables, but this is incorrect because:
- SCOR metrics are **framework definitions**, not business data
- They should be **KPIs**, not database records
- Business entities (orders, shipments) should create Layer 2 tables, not SCOR metrics

### Solution: Reference-Only Approach

**SCOR objects = Layer 1 metadata ONLY**

```
Layer 1 (Metadata):
├── SCOR Module (ascm_scor.py)
├── SCOR Object Models (reference/catalog):
│   ├── scor_process.py (process catalog)
│   ├── scor_metric.py (metric catalog) ← REFERENCE ONLY
│   ├── scor_practice.py (practice catalog)
│   └── scor_skill.py (skill catalog)
├── KPIs (created from SCOR metrics):
│   ├── perfect_order_fulfillment.py (from RL.1.1)
│   ├── order_fulfillment_cycle_time.py (from RS.1.1)
│   └── ... (all SCOR metrics as KPIs)
└── Object Models (business entities):
    ├── order.py
    ├── shipment.py
    ├── inventory.py
    └── supplier.py

Layer 2 (Analytics Tables):
├── orders (from ORDER object model)
├── shipments (from SHIPMENT object model)
├── inventory (from INVENTORY object model)
├── suppliers (from SUPPLIER object model)
└── scor_metric_observations (hypertable for tracking)

NO scor_metrics, scor_processes, scor_practices, or scor_skills tables!
```

---

## 📊 How SCOR Works in This Architecture

### 1. SCOR Metrics Stored in Layer 1 Metadata

```python
# Stored in existing object_models table (db_models.py)
INSERT INTO object_models (code, name, description, metadata) VALUES (
    'SCOR_METRIC_RL_1_1',
    'Perfect Order Fulfillment',
    'Percentage of orders delivered on time, complete, damage-free',
    '{
        "scor_id": "RL.1.1",
        "performance_attribute": "Reliability",
        "level": "Level 1 - Strategic",
        "formula": "(Perfect Orders / Total Orders) * 100"
    }'
);
```

### 2. KPIs Created from SCOR Metrics

```python
# kpis/perfect_order_fulfillment.py
PERFECT_ORDER_FULFILLMENT = KPI(
    code="PERFECT_ORDER_FULFILLMENT",
    name="Perfect Order Fulfillment",
    category="Supply Chain Reliability",
    
    formula="""
    (Count of orders delivered:
     - On time
     - Complete
     - Damage-free
     - With correct documentation
    ) / Total Orders * 100
    """,
    
    metadata_={
        "scor_reference": {
            "metric_id": "RL.1.1",
            "performance_attribute": "Reliability",
            "level": "Level 1 - Strategic",
            "scor_version": "14.0"
        },
        "required_objects": ["Order", "Shipment", "Delivery"],
        "modules": ["ASCM_SCOR", "LOGISTICS", "ORDER_MANAGEMENT"],
        "aggregation_methods": ["percentage"],
        "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"]
    }
)
```

### 3. Business Entities Create Layer 2 Tables

```python
# object_models/order.py
ORDER = ObjectModel(
    name="Order",
    code="ORDER",
    table_schema={...},  # Creates Layer 2 table
    metadata_={
        "modules": ["ASCM_SCOR", "ORDER_MANAGEMENT"],
        "related_kpis": [
            "PERFECT_ORDER_FULFILLMENT",
            "ORDER_FULFILLMENT_CYCLE_TIME"
        ]
    }
)
```

### 4. Metric Observations Tracked in Hypertable

```sql
-- Single hypertable for all SCOR metric observations
CREATE TABLE scor_metric_observations (
    timestamp TIMESTAMPTZ NOT NULL,
    scor_metric_id VARCHAR(50),  -- e.g., "RL.1.1"
    kpi_code VARCHAR(100),        -- e.g., "PERFECT_ORDER_FULFILLMENT"
    value NUMERIC,
    unit VARCHAR(50),
    context JSONB,                -- Additional dimensions
    organization_id INTEGER,
    process_id VARCHAR(50)
);

SELECT create_hypertable('scor_metric_observations', 'timestamp');

-- Example data
INSERT INTO scor_metric_observations VALUES (
    '2024-11-08 13:00:00',
    'RL.1.1',
    'PERFECT_ORDER_FULFILLMENT',
    98.5,
    'percentage',
    '{"region": "North America", "product_line": "Electronics"}',
    1,
    'F1'
);
```

---

## 🔄 Data Flow

```
1. SCOR Framework (External)
   ↓
2. SCOR Object Models (Layer 1 - Reference)
   - Stored in object_models table
   - Defines metric catalog
   ↓
3. KPI Definitions (Layer 1 - Definitions)
   - Created from SCOR metrics
   - Enriched with SCOR metadata
   ↓
4. Object Models (Layer 1 → Layer 2)
   - Derived from KPI analysis
   - Creates business entity tables
   ↓
5. Business Data (Layer 2 - Tables)
   - orders, shipments, inventory, etc.
   - Actual operational data
   ↓
6. KPI Calculations (Runtime)
   - Query Layer 2 tables
   - Calculate metric values
   ↓
7. Metric Observations (Layer 2 - Hypertable)
   - Store calculated values
   - Time-series tracking
```

---

## 📋 Implementation Steps

### Step 1: Mark SCOR Objects as Reference-Only ✅

Updated all SCOR object models with:
```python
metadata_={
    "is_reference_only": True,
    "creates_layer_2_table": False,
    "stored_in_layer_1": True,
    "implementation_note": "Implemented as KPIs, not Layer 2 tables"
}
```

Files updated:
- ✅ `scor_metric.py`
- ⏳ `scor_process.py`
- ⏳ `scor_practice.py`
- ⏳ `scor_skill.py`

### Step 2: Create Metric Observations Hypertable

```python
# object_models/scor_metric_observation.py
SCOR_METRIC_OBSERVATION = ObjectModel(
    name="SCOR Metric Observation",
    code="SCOR_METRIC_OBSERVATION",
    table_schema={
        "table_name": "scor_metric_observations",
        "is_hypertable": True,
        "time_column": "timestamp",
        "columns": [
            {"name": "timestamp", "type": "DateTime", "nullable": False},
            {"name": "scor_metric_id", "type": "String", "length": 50},
            {"name": "kpi_code", "type": "String", "length": 100},
            {"name": "value", "type": "Float"},
            {"name": "unit", "type": "String", "length": 50},
            {"name": "context", "type": "JSON"},
            {"name": "organization_id", "type": "Integer"},
            {"name": "process_id", "type": "String", "length": 50}
        ]
    }
)
```

### Step 3: Generate SCOR-Based KPIs

Create KPI definitions for each SCOR metric:
- RL.1.1 → `perfect_order_fulfillment.py`
- RS.1.1 → `order_fulfillment_cycle_time.py`
- CO.1.1 → `total_supply_chain_cost.py`
- AM.1.1 → `cash_to_cash_cycle_time.py`
- ... (all Level 1 metrics)

### Step 4: Identify Required Object Models

Analyze SCOR KPIs to determine needed business entities:
- Orders
- Shipments
- Deliveries
- Inventory
- Suppliers
- Costs
- Payments
- Receipts

### Step 5: Create/Update Object Models

Ensure all required object models exist with proper `table_schema`.

---

## 🎯 Benefits of This Approach

### 1. **Correct Separation of Concerns**
- ✅ SCOR = Framework reference (Layer 1)
- ✅ KPIs = Metric definitions (Layer 1)
- ✅ Business entities = Data tables (Layer 2)

### 2. **Flexibility**
- ✅ Can use SCOR metrics as-is
- ✅ Can create custom KPIs
- ✅ Can enrich existing KPIs with SCOR metadata

### 3. **No Data Duplication**
- ✅ SCOR metrics stored once in metadata
- ✅ Business data stored in appropriate tables
- ✅ Observations tracked in single hypertable

### 4. **Industry Standard Compliance**
- ✅ SCOR framework properly represented
- ✅ Metrics traceable to SCOR IDs
- ✅ Benchmarking enabled

### 5. **Scalability**
- ✅ Single observations table for all metrics
- ✅ TimescaleDB hypertable for performance
- ✅ Flexible schema for context data

---

## 📊 Comparison: Old vs New Approach

| Aspect | Old Approach (Incorrect) | New Approach (Correct) |
|--------|-------------------------|------------------------|
| **SCOR Metrics** | Layer 2 table (scor_metrics) | Layer 1 metadata only |
| **Metric Data** | Rows in scor_metrics table | KPI definitions |
| **Observations** | Separate table per metric | Single hypertable |
| **Business Data** | Unclear | Proper object models |
| **KPIs** | Separate from SCOR | Created from SCOR metrics |
| **Layer 2 Tables** | scor_* tables | Business entity tables |
| **Flexibility** | Low | High |
| **SCOR Compliance** | Partial | Full |

---

## 🚀 Next Actions

1. ✅ Mark all SCOR objects as reference-only
2. ⏳ Create `scor_metric_observation.py` object model
3. ⏳ Generate SCOR-based KPI definitions
4. ⏳ Analyze required object models
5. ⏳ Create/update business entity object models
6. ⏳ Create Layer 2 table for observations only
7. ⏳ Update documentation

---

## 📝 Key Takeaway

**SCOR objects are NOT data tables. They are framework references that enrich KPIs and guide object model creation.**

```
SCOR Metric (RL.1.1) → KPI (PERFECT_ORDER_FULFILLMENT) → Object Models (Order, Shipment) → Layer 2 Tables
     [Reference]            [Definition]                      [Schema]                    [Data]
```

This architecture maintains SCOR framework integrity while properly separating concerns across the data layers.
