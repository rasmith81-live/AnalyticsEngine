# Analytics Models Migration Plan

**Date**: November 10, 2025  
**Objective**: Transform monolithic `analytics_models` into microservices architecture with Calculation Engine

---

## Current State Analysis

### What Exists in `analytics_models/`

```
analytics_models/
├── db_models.py                    ← SQLAlchemy models (metadata schema)
├── schemas.py                      ← Pydantic schemas
├── utils.py                        ← Helper functions
├── definitions/
│   ├── kpis/                       ← 500+ KPI definitions
│   ├── object_models/              ← Object model definitions
│   ├── modules/                    ← Module definitions
│   ├── value_chains/               ← Value chain definitions
│   ├── industries/                 ← Industry definitions
│   ├── benchmarks/                 ← Benchmark data
│   └── attributes/                 ← Attribute definitions
└── [documentation files]
```

**Key Assets**:
- ✅ **500+ KPI definitions** - Complete metadata
- ✅ **Object models** - Table schemas, relationships, UML
- ✅ **Module definitions** - Groupings of KPIs
- ✅ **Value chain definitions** - SCOR, CRM, Sales, etc.
- ✅ **SQLAlchemy models** - Database schema for metadata

---

## Migration Strategy

### Phase 1: Extract Metadata Service ✅ KEEP AS-IS

**What**: `analytics_models/` becomes the **Metadata Service**

**Why**: This is already your single source of truth for:
- KPI definitions
- Object model definitions
- Module definitions
- Value chain definitions
- Industry standards

**Action**: **RENAME** (don't migrate)

```bash
# Rename directory
analytics_models/ → analytics_metadata_service/
```

**New Structure**:
```
analytics_metadata_service/
├── app/
│   ├── main.py                     ← NEW: FastAPI service
│   ├── config.py                   ← NEW: Service configuration
│   ├── api/                        ← NEW: REST API endpoints
│   │   ├── kpis.py                 ← GET /kpis, GET /kpis/{code}
│   │   ├── object_models.py        ← GET /object-models
│   │   ├── modules.py              ← GET /modules
│   │   └── value_chains.py         ← GET /value-chains
│   ├── db_models.py                ← KEEP: SQLAlchemy models
│   ├── schemas.py                  ← KEEP: Pydantic schemas
│   ├── utils.py                    ← KEEP: Helper functions
│   └── definitions/                ← KEEP: All definitions
│       ├── kpis/
│       ├── object_models/
│       ├── modules/
│       └── value_chains/
└── README.md
```

**What to Add**:
1. FastAPI service wrapper (`main.py`)
2. REST API endpoints to serve definitions
3. Configuration for service URLs
4. Health check endpoint

**What NOT to Change**:
- ❌ Don't touch KPI definitions
- ❌ Don't touch object models
- ❌ Don't touch db_models.py
- ❌ Don't touch definitions structure

---

## Phase 2: Create Calculation Engine Service ✅ ALREADY DONE

**Status**: ✅ Complete (created in previous step)

**Location**: `services/business_services/calculation_engine/`

**Components**:
- ✅ `base_handler.py` - Abstract base class
- ✅ `orchestrator.py` - Request routing
- ✅ `handlers/scor_handler.py` - SCOR calculations
- ✅ `main.py` - FastAPI service

---

## Phase 3: Implement Value Chain Handlers

### 3A: SCOR Handler (Already Started)

**File**: `calculation_engine/app/handlers/scor_handler.py`

**What to Add**:
1. **Connect to Metadata Service**
   ```python
   async def get_kpi_definition(self, kpi_code: str):
       # Call analytics_metadata_service
       response = await http_client.get(
           f"{self.metadata_service_url}/kpis/{kpi_code}"
       )
       return response.json()
   ```

2. **Implement Each SCOR KPI Calculator**
   - Map KPI codes from `definitions/kpis/` to calculation methods
   - Use object models from metadata service
   - Query `scor_data` schema via database_service

3. **SCOR KPIs to Implement** (from SCOR 14.0):
   ```python
   # Level 1 - Strategic
   - Perfect Order Fulfillment (RL.1.1)
   - Order Fulfillment Cycle Time (RS.1.1)
   - Upside Supply Chain Flexibility (AG.1.1)
   - Downside Supply Chain Adaptability (AG.1.2)
   - Total Supply Chain Cost (CO.1.1)
   - Cash-to-Cash Cycle Time (AM.1.1)
   
   # Level 2 - Diagnostic (50+ metrics)
   # Level 3 - Operational (100+ metrics)
   ```

### 3B: CRM Handler (To Create)

**File**: `calculation_engine/app/handlers/crm_handler.py`

```python
class CRMCalculationHandler(BaseCalculationHandler):
    def __init__(self, ...):
        super().__init__(
            value_chain_code="CRM",
            ...
        )
        
        self.kpi_calculators = {
            "CUSTOMER_RETENTION_RATE": self._calculate_retention,
            "CUSTOMER_LIFETIME_VALUE": self._calculate_clv,
            "CUSTOMER_CHURN_RATE": self._calculate_churn,
            "NET_PROMOTER_SCORE": self._calculate_nps,
            # ... more CRM KPIs
        }
```

**CRM KPIs to Implement** (from `definitions/kpis/`):
- Customer Retention Rate
- Customer Lifetime Value (CLV)
- Customer Churn Rate
- Net Promoter Score (NPS)
- Customer Acquisition Cost (CAC)
- Customer Satisfaction Score (CSAT)
- etc.

### 3C: Sales Handler (To Create)

**File**: `calculation_engine/app/handlers/sales_handler.py`

```python
class SalesCalculationHandler(BaseCalculationHandler):
    def __init__(self, ...):
        super().__init__(
            value_chain_code="SALES",
            ...
        )
        
        self.kpi_calculators = {
            "SALES_PIPELINE_VALUE": self._calculate_pipeline,
            "WIN_RATE": self._calculate_win_rate,
            "AVERAGE_DEAL_SIZE": self._calculate_deal_size,
            "SALES_CYCLE_LENGTH": self._calculate_cycle_length,
            # ... more Sales KPIs
        }
```

**Sales KPIs to Implement** (from `definitions/kpis/`):
- Sales Pipeline Value
- Win Rate
- Average Deal Size
- Sales Cycle Length
- Lead Conversion Rate
- Sales Velocity
- etc.

---

## Phase 4: Schema Management

### Dynamic Schema Creation

**What**: Create schemas dynamically from object model definitions

**File**: `services/business_services/schema_manager_service/`

```python
class ValueChainSchemaManager:
    async def activate_value_chain(self, value_chain_code: str):
        # 1. Get object models from metadata service
        object_models = await self.get_object_models(value_chain_code)
        
        # 2. Create schema
        schema_name = f"{value_chain_code.lower()}_data"
        await self.create_schema(schema_name)
        
        # 3. Create tables from table_schema JSON
        for obj_model in object_models:
            await self.create_table_from_schema(
                schema_name,
                obj_model["table_schema"]
            )
```

**Object Models to Migrate**:
- Read from `analytics_metadata_service/definitions/object_models/`
- Each has `table_schema` JSON with column definitions
- Create tables dynamically in value chain schemas

---

## Migration Checklist

### ✅ Phase 1: Metadata Service

- [ ] Rename `analytics_models/` to `analytics_metadata_service/`
- [ ] Create `app/main.py` with FastAPI service
- [ ] Create `app/config.py` with service settings
- [ ] Create API endpoints:
  - [ ] `GET /kpis` - List all KPIs
  - [ ] `GET /kpis/{code}` - Get KPI definition
  - [ ] `GET /object-models` - List object models
  - [ ] `GET /object-models/{code}` - Get object model
  - [ ] `GET /modules` - List modules
  - [ ] `GET /modules/{code}` - Get module
  - [ ] `GET /value-chains` - List value chains
  - [ ] `GET /value-chains/{code}` - Get value chain
- [ ] Add to `docker-compose.yml` (port 8020)
- [ ] Test endpoints

### ✅ Phase 2: Calculation Engine (DONE)

- [x] Create base handler
- [x] Create orchestrator
- [x] Create SCOR handler skeleton
- [x] Create main service

### 🔄 Phase 3: Implement Handlers

#### SCOR Handler
- [ ] Connect to metadata service
- [ ] Implement Level 1 KPIs (6 metrics)
- [ ] Implement Level 2 KPIs (50+ metrics)
- [ ] Implement Level 3 KPIs (100+ metrics)
- [ ] Add caching logic
- [ ] Add error handling
- [ ] Write tests

#### CRM Handler
- [ ] Create handler class
- [ ] Map CRM KPIs to calculators
- [ ] Implement each calculator
- [ ] Add caching logic
- [ ] Write tests

#### Sales Handler
- [ ] Create handler class
- [ ] Map Sales KPIs to calculators
- [ ] Implement each calculator
- [ ] Add caching logic
- [ ] Write tests

### 📋 Phase 4: Schema Management

- [ ] Create schema_manager_service
- [ ] Implement dynamic table creation
- [ ] Implement value chain activation
- [ ] Create migration tool for schema updates
- [ ] Test with SCOR value chain
- [ ] Test with CRM value chain
- [ ] Test with Sales value chain

### 🔗 Phase 5: Integration

- [ ] Update API Gateway routes
- [ ] Add calculation engine endpoints
- [ ] Test end-to-end flow
- [ ] Performance testing
- [ ] Load testing

---

## Key Decisions

### ✅ Keep Definitions In Place

**Decision**: Don't migrate KPI/object model definitions

**Rationale**:
- Already well-organized
- Single source of truth
- Used by Excel processor
- Used by validation scripts

**Action**: Wrap with REST API, don't restructure

### ✅ Separate Calculation from Metadata

**Decision**: Calculation logic goes in handlers, not metadata service

**Rationale**:
- Metadata service = definitions only
- Calculation engine = runtime computation
- Clear separation of concerns

### ✅ Dynamic Schema Creation

**Decision**: Don't use Alembic for value chain tables

**Rationale**:
- Scales to thousands of value chains
- No migration file explosion
- Activate/deactivate on demand

---

## File Mapping

### Before (Monolithic)
```
analytics_models/
├── db_models.py                    ← Metadata schema
├── definitions/
│   ├── kpis/                       ← KPI definitions
│   └── object_models/              ← Object models
└── [no calculation logic]
```

### After (Microservices)
```
analytics_metadata_service/         ← Renamed from analytics_models
├── app/
│   ├── main.py                     ← NEW: REST API
│   ├── db_models.py                ← SAME: Metadata schema
│   └── definitions/                ← SAME: All definitions
│       ├── kpis/
│       └── object_models/

calculation_engine/                 ← NEW: Calculation orchestration
├── app/
│   ├── main.py
│   ├── base_handler.py
│   ├── orchestrator.py
│   └── handlers/
│       ├── scor_handler.py         ← NEW: SCOR calculations
│       ├── crm_handler.py          ← NEW: CRM calculations
│       └── sales_handler.py        ← NEW: Sales calculations

schema_manager_service/             ← NEW: Dynamic schema creation
└── app/
    ├── main.py
    ├── value_chain_activator.py
    └── dynamic_table_creator.py
```

---

## Summary

### What to Do with `analytics_models/`

1. **Rename** to `analytics_metadata_service/`
2. **Add** FastAPI REST API wrapper
3. **Keep** all definitions as-is
4. **Don't** add calculation logic here

### What's New

1. **Calculation Engine** - Generic orchestration layer
2. **Value Chain Handlers** - Domain-specific calculations
3. **Schema Manager** - Dynamic table creation

### What Stays the Same

- ✅ KPI definitions
- ✅ Object model definitions
- ✅ Module definitions
- ✅ Value chain definitions
- ✅ SQLAlchemy models (metadata schema)

### What Changes

- ❌ No more monolithic calculation
- ✅ Microservices per value chain
- ✅ REST API for metadata
- ✅ Dynamic schema creation

---

## Next Steps

1. **Immediate**: Rename `analytics_models/` → `analytics_metadata_service/`
2. **Week 1**: Create REST API wrapper for metadata service
3. **Week 2**: Implement SCOR handler with real calculations
4. **Week 3**: Implement CRM handler
5. **Week 4**: Implement Sales handler
6. **Week 5**: Create schema manager service
7. **Week 6**: Integration testing

**The good news**: Your existing work is preserved! We're wrapping it with microservices, not replacing it. 🎉
