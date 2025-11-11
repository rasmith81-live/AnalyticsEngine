# Business Services Interplay Architecture

**Date**: November 11, 2025  
**Purpose**: Clarify the distinct roles and interactions between the three core business services

---

## 🎯 Three Service Roles

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Analytics Metadata Service (Port 8020)                  │
│    "What can be measured?"                                  │
│    ├─ KPI Definitions (formulas, descriptions)             │
│    ├─ Object Models (schema, relationships)                │
│    ├─ Modules & Value Chains                               │
│    └─ Sample Data (for visualization previews)             │
└─────────────────────────────────────────────────────────────┘
                           ↓ Provides definitions to
┌─────────────────────────────────────────────────────────────┐
│ 2. Calculation Engine Service (Port 8021)                  │
│    "What are the actual values?"                            │
│    ├─ Real-time KPI Calculations                           │
│    ├─ Scheduled Batch Calculations                         │
│    ├─ Fetches data from databases                          │
│    └─ Returns calculated values                            │
└─────────────────────────────────────────────────────────────┘
                           ↓ Results used by
┌─────────────────────────────────────────────────────────────┐
│ 3. Demo/Config Service (Port 8022)                         │
│    "What does this client want?"                            │
│    ├─ Client Configuration (selected KPIs)                 │
│    ├─ Custom KPI Definitions                               │
│    ├─ Data Source Mappings                                 │
│    └─ Service Proposals (SOW)                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Detailed Service Breakdown

### **1. Analytics Metadata Service** 
**Role**: "The Library" - Catalog of what exists

**Responsibilities:**
- ✅ Store KPI definitions (formula, description, required objects)
- ✅ Store object model schemas (tables, relationships)
- ✅ Store module and value chain metadata
- ✅ Provide sample data for UI previews
- ✅ Serve as single source of truth for "what can be measured"

**Does NOT:**
- ❌ Calculate actual KPI values
- ❌ Store client configurations
- ❌ Connect to client data sources
- ❌ Perform any real-time calculations

**Example Response:**
```json
{
  "code": "PERFECT_ORDER_FULFILLMENT",
  "name": "Perfect Order Fulfillment",
  "formula": "(Perfect Orders / Total Orders) * 100",
  "description": "Percentage of orders delivered...",
  "required_objects": ["Order", "Shipment", "Invoice"],
  "sample_data": {
    "current": { "value": 94.5, "unit": "%" },
    "time_series": [...]
  }
}
```

---

### **2. Calculation Engine Service**
**Role**: "The Calculator" - Computes actual values

**Responsibilities:**
- ✅ Execute KPI calculations using real client data
- ✅ Query databases for raw data
- ✅ Apply formulas from metadata service
- ✅ Handle both on-demand and scheduled batch calculations
- ✅ Cache results for performance
- ✅ Return actual calculated values

**Does NOT:**
- ❌ Define what KPIs exist (gets from metadata service)
- ❌ Store client preferences
- ❌ Manage data source connections
- ❌ Generate service proposals

**How it Uses Metadata Service:**
```python
# 1. Calculation Engine receives request
request = {
  "kpi_code": "PERFECT_ORDER_FULFILLMENT",
  "time_period": {...},
  "filters": {...}
}

# 2. Fetches KPI definition from Metadata Service
kpi_def = metadata_service.get_kpi("PERFECT_ORDER_FULFILLMENT")
# Returns: formula, required_objects, calculation_logic

# 3. Queries database for required data
orders = database.query("SELECT * FROM orders WHERE ...")
shipments = database.query("SELECT * FROM shipments WHERE ...")

# 4. Applies formula
perfect_orders = count(orders.where(on_time AND complete AND accurate))
total_orders = count(orders)
result = (perfect_orders / total_orders) * 100

# 5. Returns calculated value
return {
  "kpi_code": "PERFECT_ORDER_FULFILLMENT",
  "value": 94.5,
  "unit": "%",
  "calculated_at": "2025-11-11T08:00:00Z"
}
```

**Example Response:**
```json
{
  "kpi_code": "PERFECT_ORDER_FULFILLMENT",
  "value": 94.5,
  "unit": "%",
  "time_period": {
    "start_date": "2025-01-01",
    "end_date": "2025-01-31"
  },
  "calculated_at": "2025-11-11T08:00:00Z",
  "metadata": {
    "data_points": 1250,
    "confidence": 0.95
  }
}
```

---

### **3. Demo/Config Service**
**Role**: "The Customizer" - Client-specific configurations

**Responsibilities:**
- ✅ Store which KPIs each client has selected
- ✅ Store custom KPI definitions (client-specific variations)
- ✅ Manage data source connections (client's database, APIs)
- ✅ Map client data fields to object models
- ✅ Generate service proposals (SOW)
- ✅ Track client license and deployment info

**Does NOT:**
- ❌ Define standard KPIs (uses metadata service)
- ❌ Calculate KPI values (uses calculation engine)
- ❌ Store object model schemas

**How it Uses Other Services:**

**Uses Metadata Service:**
```python
# Client selects KPIs from catalog
available_kpis = metadata_service.get_kpis()
# Client picks: ["PERFECT_ORDER_FULFILLMENT", "ON_TIME_DELIVERY"]

# Store client selection
client_config = {
  "client_id": "acme_corp",
  "selected_kpis": ["PERFECT_ORDER_FULFILLMENT", "ON_TIME_DELIVERY"],
  "custom_kpis": [],
  "data_sources": [...]
}
```

**Uses Calculation Engine:**
```python
# When client views dashboard, config service orchestrates
client_config = config_service.get_client("acme_corp")

# For each selected KPI, request calculation
for kpi_code in client_config.selected_kpis:
    result = calculation_engine.calculate({
        "kpi_code": kpi_code,
        "client_id": "acme_corp",  # Uses client's data
        "time_period": {...}
    })
    dashboard_results[kpi_code] = result
```

**Example Client Config:**
```json
{
  "client_id": "acme_corp",
  "client_name": "ACME Corporation",
  "selected_kpis": [
    "PERFECT_ORDER_FULFILLMENT",
    "ON_TIME_DELIVERY",
    "FILL_RATE"
  ],
  "custom_kpis": [
    {
      "code": "ACME_CUSTOM_METRIC",
      "name": "ACME Custom Delivery Score",
      "source_kpi": "ON_TIME_DELIVERY",
      "formula": "modified formula...",
      "created_by": "john@acme.com"
    }
  ],
  "data_sources": [
    {
      "name": "ACME ERP",
      "type": "api",
      "connector": "sap_hana",
      "config": {
        "host": "erp.acme.com",
        "database": "production"
      },
      "field_mappings": {
        "Order.order_id": "SAP_ORDER_NUM",
        "Order.customer_id": "CUSTOMER_CODE"
      }
    }
  ],
  "license_key": "ACME-2025-ENTERPRISE",
  "license_expiration": "2026-12-31"
}
```

---

## 🔄 Complete User Flow Example

### **Scenario: User Views KPI Dashboard**

```
1. USER: Opens dashboard in Demo/Config UI
   ↓

2. FRONTEND: Requests client configuration
   GET /api/v1/config/clients/acme_corp
   ↓

3. API GATEWAY → Config Service
   Returns: {
     "selected_kpis": ["PERFECT_ORDER_FULFILLMENT", "ON_TIME_DELIVERY"],
     "data_sources": [...]
   }
   ↓

4. FRONTEND: For each KPI, requests definition + calculation
   
   4a. GET /api/v1/metadata/kpis/PERFECT_ORDER_FULFILLMENT
       API GATEWAY → Metadata Service
       Returns: {
         "formula": "...",
         "description": "...",
         "unit": "%"
       }
   
   4b. POST /api/v1/calculations/calculate
       Body: {
         "kpi_code": "PERFECT_ORDER_FULFILLMENT",
         "client_id": "acme_corp",
         "time_period": {...}
       }
       API GATEWAY → Calculation Engine
       ├─ Fetches KPI definition from Metadata Service
       ├─ Queries ACME's database using Config Service mappings
       ├─ Applies formula
       └─ Returns: { "value": 94.5, "unit": "%" }
   ↓

5. FRONTEND: Displays dashboard
   ┌─────────────────────────────────────┐
   │ Perfect Order Fulfillment           │
   │ 94.5%                               │
   │ ↑ 2.3% from last month              │
   └─────────────────────────────────────┘
```

---

## 🎨 Demo/Config UI Workflow

### **Phase 1: Browse & Select (Uses Metadata Service)**
```
User browses KPI catalog
  ↓ GET /api/v1/metadata/kpis
Metadata Service returns all available KPIs
  ↓
User sees KPI cards with:
  - Name, description, formula
  - Sample visualization (from sample_data)
  - Required objects
  ↓
User adds KPIs to cart
  ↓ Local state (not saved yet)
```

### **Phase 2: Configure (Uses Config Service)**
```
User clicks "Save Configuration"
  ↓ POST /api/v1/config/clients
Config Service stores:
  - Selected KPIs
  - Client info
  - Data source connections
  ↓
Returns client_id for future use
```

### **Phase 3: View Results (Uses All Three)**
```
User opens dashboard
  ↓ GET /api/v1/config/clients/{id}
Config Service returns selected KPIs
  ↓
For each KPI:
  ├─ GET /api/v1/metadata/kpis/{code}
  │  (Get definition for display)
  │
  └─ POST /api/v1/calculations/calculate
     (Get actual calculated value)
  ↓
Display combined results
```

---

## 🔑 Key Distinctions

| Aspect | Metadata Service | Calculation Engine | Config Service |
|--------|-----------------|-------------------|----------------|
| **Data Type** | Definitions | Values | Preferences |
| **Scope** | Universal | Per-client | Per-client |
| **Changes** | Rarely | Constantly | Occasionally |
| **Example** | "What is POF?" | "POF = 94.5%" | "ACME wants POF" |
| **Caching** | Long (hours) | Short (minutes) | Medium (hours) |
| **Source** | Python dicts | Database queries | Client input |

---

## 🎯 Why Three Services?

### **Separation of Concerns**

1. **Metadata Service**: Domain knowledge (what KPIs exist)
   - Shared across all clients
   - Rarely changes
   - Can be heavily cached

2. **Calculation Engine**: Computational logic (how to calculate)
   - Client-specific data
   - Changes frequently
   - Resource-intensive

3. **Config Service**: Client customization (who wants what)
   - Client-specific preferences
   - Changes occasionally
   - Lightweight

### **Benefits**

✅ **Independent Scaling**: Scale calculation engine separately from metadata  
✅ **Clear Ownership**: Each service has single responsibility  
✅ **Reusability**: Metadata service serves all clients  
✅ **Flexibility**: Clients can customize without affecting others  
✅ **Performance**: Cache strategies optimized per service type  

---

## 📝 Summary

**Metadata Service** = "The Menu" (what's available)  
**Calculation Engine** = "The Kitchen" (prepares your order)  
**Config Service** = "Your Order" (what you selected)  

All three work together to deliver a complete analytics experience! 🎉
