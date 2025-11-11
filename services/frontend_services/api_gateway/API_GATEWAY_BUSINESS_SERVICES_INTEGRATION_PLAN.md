# API Gateway - Business Services Integration Plan

**Date**: November 11, 2025  
**Purpose**: Define how the API Gateway will integrate with business services to support the Demo/Config UI

---

## 🎯 Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│ Frontend: Demo/Config UI (React)                            │
│ Port: 3000                                                  │
└─────────────────────────────────────────────────────────────┘
                           ↓ HTTP REST
┌─────────────────────────────────────────────────────────────┐
│ API Gateway (FastAPI)                                       │
│ Port: 8090                                                  │
│ ├─ /api/v1/metadata/*    → analytics_metadata_service      │
│ ├─ /api/v1/calculations/* → calculation_engine_service     │
│ └─ /api/v1/config/*       → demo_config_service            │
└─────────────────────────────────────────────────────────────┘
                           ↓ HTTP REST
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                   ↓
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Metadata     │  │ Calculation  │  │ Config       │
│ Service      │  │ Engine       │  │ Service      │
│ Port: 8020   │  │ Port: 8021   │  │ Port: 8022   │
└──────────────┘  └──────────────┘  └──────────────┘
```

---

## 📋 Service Requirements

### **1. Analytics Metadata Service** (Port: 8020)

**Purpose**: Provides KPI definitions, object models, modules, value chains

**Endpoints Needed:**

#### **KPI Endpoints**
```
GET  /api/v1/kpis                    # List all KPIs
GET  /api/v1/kpis/{code}             # Get single KPI by code
GET  /api/v1/kpis/module/{code}      # Get KPIs by module
GET  /api/v1/kpis/value-chain/{code} # Get KPIs by value chain
GET  /api/v1/kpis/industry/{code}    # Get KPIs by industry
```

#### **Object Model Endpoints**
```
GET  /api/v1/object-models           # List all object models
GET  /api/v1/object-models/{code}    # Get single object model
GET  /api/v1/object-models/module/{code} # Get object models by module
```

#### **Module Endpoints**
```
GET  /api/v1/modules                 # List all modules
GET  /api/v1/modules/{code}          # Get single module
GET  /api/v1/modules/value-chain/{code} # Get modules by value chain
```

#### **Value Chain Endpoints**
```
GET  /api/v1/value-chains            # List all value chains
GET  /api/v1/value-chains/{code}     # Get single value chain
```

#### **Industry Endpoints**
```
GET  /api/v1/industries              # List all industries
GET  /api/v1/industries/{code}       # Get single industry
```

**Response Format:**
```json
{
  "code": "PERFECT_ORDER_FULFILLMENT",
  "name": "Perfect Order Fulfillment",
  "description": "...",
  "formula": "...",
  "required_objects": ["Order", "Shipment"],
  "metadata_": {
    "modules": ["SUPPLY_CHAIN"],
    "value_chains": ["SCOR"]
  },
  "sample_data": { ... }
}
```

---

### **2. Calculation Engine Service** (Port: 8021)

**Purpose**: Real-time KPI calculation engine (on-demand AND scheduled batch)

**Key Concept**: The calculation engine uses the SAME real-time calculation logic for both:
- **On-Demand**: User-triggered calculations (immediate response)
- **Scheduled Batch**: Automated calculations at intervals (intraday, daily, weekly, monthly)
  - Batch jobs use the same calculation engine
  - Data is refreshed at scheduled intervals
  - Results can be cached for performance

**Endpoints Needed:**

#### **On-Demand Calculation Endpoints**
```
POST /api/v1/calculate               # Calculate single KPI (real-time)
POST /api/v1/calculate/batch         # Calculate multiple KPIs (real-time)
POST /api/v1/calculate/dashboard     # Calculate dashboard KPIs (real-time)
```

#### **Scheduled Batch Endpoints**
```
POST /api/v1/batch/schedule          # Schedule batch calculation job
GET  /api/v1/batch/jobs              # List scheduled batch jobs
GET  /api/v1/batch/jobs/{id}         # Get batch job details
PUT  /api/v1/batch/jobs/{id}         # Update batch job schedule
DELETE /api/v1/batch/jobs/{id}       # Cancel batch job
GET  /api/v1/batch/results/{job_id}  # Get batch calculation results
```

**Request Format (Single):**
```json
{
  "kpi_code": "PERFECT_ORDER_FULFILLMENT",
  "time_period": {
    "start_date": "2025-01-01",
    "end_date": "2025-01-31"
  },
  "filters": {
    "customer_segment": "Enterprise",
    "region": "North America"
  },
  "aggregation": "average"
}
```

**Response Format:**
```json
{
  "kpi_code": "PERFECT_ORDER_FULFILLMENT",
  "value": 94.5,
  "unit": "%",
  "time_period": { ... },
  "calculated_at": "2025-11-11T08:00:00Z",
  "metadata": {
    "data_points": 1250,
    "confidence": 0.95
  }
}
```

**Request Format (Dashboard):**
```json
{
  "dashboard_id": "supply_chain_overview",
  "kpi_codes": ["PERFECT_ORDER_FULFILLMENT", "ON_TIME_DELIVERY", "FILL_RATE"],
  "time_period": { ... },
  "filters": { ... }
}
```

**Response Format (Dashboard):**
```json
{
  "dashboard_id": "supply_chain_overview",
  "calculated_at": "2025-11-11T08:00:00Z",
  "results": {
    "PERFECT_ORDER_FULFILLMENT": { "value": 94.5, ... },
    "ON_TIME_DELIVERY": { "value": 96.2, ... },
    "FILL_RATE": { "value": 98.1, ... }
  }
}
```

**Batch Job Request Format:**
```json
{
  "job_name": "daily_supply_chain_metrics",
  "schedule": {
    "frequency": "daily",  // intraday, daily, weekly, monthly
    "time": "06:00:00",    // UTC time
    "timezone": "America/New_York"
  },
  "kpi_codes": ["PERFECT_ORDER_FULFILLMENT", "ON_TIME_DELIVERY"],
  "filters": {
    "region": "North America"
  },
  "output": {
    "store_results": true,
    "cache_ttl": 86400,  // 24 hours
    "notify_on_completion": true
  }
}
```

**Batch Job Response:**
```json
{
  "job_id": "batch_job_12345",
  "status": "scheduled",
  "next_run": "2025-11-12T06:00:00Z",
  "last_run": "2025-11-11T06:00:00Z",
  "last_result": {
    "status": "success",
    "kpis_calculated": 2,
    "execution_time_ms": 1250
  }
}
```

**Key Difference: On-Demand vs Batch**
- **On-Demand**: Immediate calculation, fresh data query, user waits for response
- **Batch**: Scheduled calculation, data refreshed at intervals, results cached and served instantly
- **Same Engine**: Both use identical calculation logic, just different triggering mechanisms

---

### **3. Demo Config Service** (Port: 8022)

**Purpose**: Client configuration, custom KPIs, data source mapping

**Endpoints Needed:**

#### **Client Configuration**
```
GET    /api/v1/clients                # List all client configs
GET    /api/v1/clients/{id}           # Get client config
POST   /api/v1/clients                # Create client config
PUT    /api/v1/clients/{id}           # Update client config
DELETE /api/v1/clients/{id}           # Delete client config
```

#### **Custom KPI Management**
```
GET    /api/v1/clients/{id}/custom-kpis      # List custom KPIs
POST   /api/v1/clients/{id}/custom-kpis      # Create custom KPI
PUT    /api/v1/clients/{id}/custom-kpis/{code} # Update custom KPI
DELETE /api/v1/clients/{id}/custom-kpis/{code} # Delete custom KPI
```

#### **Data Source Configuration**
```
GET    /api/v1/clients/{id}/data-sources     # List data sources
POST   /api/v1/clients/{id}/data-sources     # Add data source
PUT    /api/v1/clients/{id}/data-sources/{id} # Update data source
DELETE /api/v1/clients/{id}/data-sources/{id} # Delete data source
POST   /api/v1/clients/{id}/data-sources/{id}/test # Test connection
```

#### **Service Proposal (SOW)**
```
POST   /api/v1/clients/{id}/proposal         # Generate SOW
GET    /api/v1/clients/{id}/proposal         # Get SOW
PUT    /api/v1/clients/{id}/proposal         # Update SOW
```

---

## 🔧 API Gateway Implementation

### **1. HTTP Clients** (New Files)

**File**: `app/clients/metadata_client.py`
```python
class MetadataServiceClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(timeout=30.0)
    
    async def get_kpis(self) -> List[Dict]:
        response = await self.client.get(f"{self.base_url}/api/v1/kpis")
        return response.json()
    
    async def get_kpi(self, code: str) -> Dict:
        response = await self.client.get(f"{self.base_url}/api/v1/kpis/{code}")
        return response.json()
    
    # ... more methods
```

**File**: `app/clients/calculation_client.py`
```python
class CalculationEngineClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(timeout=60.0)  # Longer timeout
    
    async def calculate_kpi(self, params: Dict) -> Dict:
        response = await self.client.post(
            f"{self.base_url}/api/v1/calculate",
            json=params
        )
        return response.json()
    
    async def calculate_dashboard(self, config: Dict) -> Dict:
        response = await self.client.post(
            f"{self.base_url}/api/v1/calculate/dashboard",
            json=config
        )
        return response.json()
```

**File**: `app/clients/config_client.py`
```python
class DemoConfigServiceClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(timeout=30.0)
    
    async def get_client_config(self, client_id: str) -> Dict:
        response = await self.client.get(
            f"{self.base_url}/api/v1/clients/{client_id}"
        )
        return response.json()
    
    # ... more methods
```

---

### **2. API Routes** (New Files)

**File**: `app/api/v1/metadata.py`
```python
from fastapi import APIRouter, Depends, HTTPException
from app.clients.metadata_client import MetadataServiceClient
from app.api.dependencies import get_metadata_client

router = APIRouter()

@router.get("/kpis")
async def get_kpis(
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    return await client.get_kpis()

@router.get("/kpis/{code}")
async def get_kpi(
    code: str,
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    return await client.get_kpi(code)

# ... more routes
```

**File**: `app/api/v1/calculations.py`
```python
from fastapi import APIRouter, Depends
from app.clients.calculation_client import CalculationEngineClient
from app.api.dependencies import get_calculation_client

router = APIRouter()

@router.post("/calculate")
async def calculate_kpi(
    params: dict,
    client: CalculationEngineClient = Depends(get_calculation_client)
):
    return await client.calculate_kpi(params)

@router.post("/calculate/dashboard")
async def calculate_dashboard(
    config: dict,
    client: CalculationEngineClient = Depends(get_calculation_client)
):
    return await client.calculate_dashboard(config)
```

**File**: `app/api/v1/config.py`
```python
from fastapi import APIRouter, Depends
from app.clients.config_client import DemoConfigServiceClient
from app.api.dependencies import get_config_client

router = APIRouter()

@router.get("/clients/{client_id}")
async def get_client_config(
    client_id: str,
    client: DemoConfigServiceClient = Depends(get_config_client)
):
    return await client.get_client_config(client_id)

# ... more routes
```

---

### **3. Dependencies** (Update Existing)

**File**: `app/api/dependencies.py`
```python
from app.clients.metadata_client import MetadataServiceClient
from app.clients.calculation_client import CalculationEngineClient
from app.clients.config_client import DemoConfigServiceClient
from app.core.config import settings

def get_metadata_client() -> MetadataServiceClient:
    service_url = settings.SERVICE_REGISTRY["metadata_service"]["url"]
    return MetadataServiceClient(service_url)

def get_calculation_client() -> CalculationEngineClient:
    service_url = settings.SERVICE_REGISTRY["calculation_engine"]["url"]
    return CalculationEngineClient(service_url)

def get_config_client() -> DemoConfigServiceClient:
    service_url = settings.SERVICE_REGISTRY["config_service"]["url"]
    return DemoConfigServiceClient(service_url)
```

---

### **4. Service Registry** (Update Config)

**File**: `app/core/config.py`
```python
SERVICE_REGISTRY: Dict[str, Dict[str, Any]] = Field(default_factory=lambda: {
    # Business Services (NEW)
    "metadata_service": {
        "url": os.getenv("METADATA_SERVICE_URL", "http://localhost:8020"),
        "timeout": 30.0,
        "health_endpoint": "/health",
    },
    "calculation_engine": {
        "url": os.getenv("CALCULATION_ENGINE_URL", "http://localhost:8021"),
        "timeout": 60.0,  # Longer timeout for calculations
        "health_endpoint": "/health",
    },
    "config_service": {
        "url": os.getenv("CONFIG_SERVICE_URL", "http://localhost:8022"),
        "timeout": 30.0,
        "health_endpoint": "/health",
    },
    
    # Backend Services (EXISTING)
    "messaging_service": { ... },
    "database_service": { ... },
    # ...
})
```

---

### **5. Router Registration** (Update)

**File**: `app/api/router.py`
```python
from fastapi import APIRouter

from .v1.metadata import router as metadata_router
from .v1.calculations import router as calculations_router
from .v1.config import router as config_router
# ... existing imports

api_router = APIRouter(prefix="/api/v1")

# Business Service Routes (NEW)
api_router.include_router(metadata_router, prefix="/metadata", tags=["metadata"])
api_router.include_router(calculations_router, prefix="/calculations", tags=["calculations"])
api_router.include_router(config_router, prefix="/config", tags=["config"])

# Existing routes
api_router.include_router(analytics_router, prefix="/analytics", tags=["analytics"])
# ...
```

---

## 🔄 Request Flow Example

### **Frontend Request: Get KPI Details**

```
1. Frontend (React)
   ↓ GET http://localhost:8090/api/v1/metadata/kpis/PERFECT_ORDER_FULFILLMENT
   
2. API Gateway (Port 8090)
   ├─ Receives request
   ├─ Applies middleware (auth, rate limit, tracing)
   ├─ Routes to metadata_router
   ↓ GET http://localhost:8020/api/v1/kpis/PERFECT_ORDER_FULFILLMENT
   
3. Metadata Service (Port 8020)
   ├─ Loads KPI definition from Python dict
   ├─ Returns JSON response
   ↓ Response
   
4. API Gateway
   ├─ Receives response
   ├─ Applies response middleware
   ↓ Response
   
5. Frontend
   └─ Displays KPI details
```

### **Frontend Request: Calculate KPI**

```
1. Frontend (React)
   ↓ POST http://localhost:8090/api/v1/calculations/calculate
   
2. API Gateway (Port 8090)
   ├─ Receives request
   ├─ Applies middleware
   ├─ Routes to calculations_router
   ↓ POST http://localhost:8021/api/v1/calculate
   
3. Calculation Engine (Port 8021)
   ├─ Routes to appropriate handler (SCOR, CRM, etc.)
   ├─ Fetches data from database
   ├─ Performs calculation
   ├─ Returns result
   ↓ Response
   
4. API Gateway
   ├─ Caches result (optional)
   ↓ Response
   
5. Frontend
   └─ Displays calculated value
```

---

## 📝 Implementation Checklist

### **Phase 1: Metadata Service Integration**
- [ ] Create `app/clients/metadata_client.py`
- [ ] Create `app/api/v1/metadata.py`
- [ ] Update `app/api/dependencies.py`
- [ ] Update `app/core/config.py` SERVICE_REGISTRY
- [ ] Update `app/api/router.py`
- [ ] Test all metadata endpoints

### **Phase 2: Calculation Engine Integration**
- [ ] Create `app/clients/calculation_client.py`
- [ ] Create `app/api/v1/calculations.py`
- [ ] Update dependencies
- [ ] Update router
- [ ] Test calculation endpoints

### **Phase 3: Config Service Integration**
- [ ] Create `app/clients/config_client.py`
- [ ] Create `app/api/v1/config.py`
- [ ] Update dependencies
- [ ] Update router
- [ ] Test config endpoints

### **Phase 4: Frontend Integration**
- [ ] Update `metadataApi.ts` to use correct gateway URLs
- [ ] Add `calculationApi.ts` for calculation requests
- [ ] Add `configApi.ts` for config management
- [ ] Test end-to-end flow

---

## 🎯 Success Criteria

1. ✅ Frontend can fetch KPI definitions via API Gateway
2. ✅ Frontend can fetch object models via API Gateway
3. ✅ Frontend can request real-time KPI calculations
4. ✅ Frontend can manage client configurations
5. ✅ All requests route through API Gateway (no direct service calls)
6. ✅ Middleware applies to all requests (auth, rate limit, tracing)
7. ✅ Service health checks work for all business services
8. ✅ Circuit breaker protects against service failures

---

## 🔐 Security & Performance

**Authentication**: JWT tokens validated at API Gateway  
**Rate Limiting**: Applied per client at gateway level  
**Caching**: Metadata responses cached for 5 minutes  
**Circuit Breaker**: Protects against cascading failures  
**Timeouts**: 30s for metadata/config, 60s for calculations  
**Tracing**: Distributed tracing across all services  

---

## 📊 Monitoring

**Metrics to Track**:
- Request count per endpoint
- Response time per service
- Error rate per service
- Cache hit rate
- Circuit breaker state

**Health Checks**:
- API Gateway: `/health`
- Each service: Registered in service registry
- Aggregate health: `/health?detailed=true`
