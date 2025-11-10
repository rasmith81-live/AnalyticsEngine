# Analytics Metadata Service

**Single source of truth for all analytics metadata**

This service exposes KPI, Object Model, Module, and Value Chain definitions via REST API.

---

## Overview

The Analytics Metadata Service wraps the existing `definitions/` directory structure with a FastAPI REST API, making all analytics metadata accessible to other services (especially the Calculation Engine).

### What It Serves

- **KPIs** (500+) - Complete KPI definitions with formulas, benchmarks, required objects
- **Object Models** - Table schemas, UML relationships, metadata
- **Modules** - Groupings of KPIs and object models
- **Value Chains** - SCOR, CRM, Sales, Financial, etc.
- **Industries** - Industry-specific definitions
- **Benchmarks** - Performance benchmarks
- **Attributes** - Attribute definitions

---

## Architecture

```
analytics_metadata_service/
├── app/
│   ├── main.py                 ← FastAPI application
│   ├── config.py               ← Service configuration
│   ├── loader.py               ← Definition loader
│   ├── api/                    ← REST API endpoints
│   │   ├── kpis.py
│   │   ├── object_models.py
│   │   ├── modules.py
│   │   └── value_chains.py
│   └── definitions/            ← Original definitions (unchanged)
│       ├── kpis/
│       ├── object_models/
│       ├── modules/
│       └── value_chains/
└── .env
```

---

## API Endpoints

### KPIs

```bash
GET /kpis                           # List all KPIs
GET /kpis?module=ASCM_SCOR          # Filter by module
GET /kpis?value_chain=SUPPLY_CHAIN  # Filter by value chain
GET /kpis/{kpi_code}                # Get specific KPI
GET /kpis/{kpi_code}/formula        # Get KPI formula
GET /kpis/{kpi_code}/benchmarks     # Get KPI benchmarks
GET /kpis/{kpi_code}/required-objects  # Get required object models
```

### Object Models

```bash
GET /object-models                  # List all object models
GET /object-models/{model_code}     # Get specific object model
GET /object-models/{model_code}/schema  # Get table schema (for dynamic creation)
GET /object-models/{model_code}/relationships  # Get UML relationships
GET /object-models/{model_code}/modules  # Get modules using this model
```

### Modules

```bash
GET /modules                        # List all modules
GET /modules/{module_code}          # Get specific module
GET /modules/{module_code}/kpis     # Get all KPIs in module
GET /modules/{module_code}/object-models  # Get all object models in module
```

### Value Chains

```bash
GET /value-chains                   # List all value chains
GET /value-chains/{vc_code}         # Get specific value chain
GET /value-chains/{vc_code}/modules  # Get all modules in value chain
GET /value-chains/{vc_code}/kpis    # Get all KPIs in value chain
GET /value-chains/{vc_code}/object-models  # Get all object models
```

### System

```bash
GET /                               # Service info
GET /health                         # Health check
GET /stats                          # Definition statistics
GET /docs                           # Interactive API documentation
```

---

## Running the Service

### Local Development

```powershell
# Install dependencies
pip install fastapi uvicorn pydantic pydantic-settings

# Run service
cd services/business_services/analytics_models
uvicorn app.main:app --reload --port 8020
```

### Docker

```yaml
# Add to docker-compose.yml
analytics_metadata_service:
  build:
    context: .
    dockerfile: Dockerfile
    args:
      SERVICE_DIR: services/business_services/analytics_models
  ports:
    - "8020:8000"
  environment:
    - SERVICE_NAME=analytics_metadata_service
    - DATABASE_SERVICE_URL=http://database_service:8000
    - MESSAGING_SERVICE_URL=http://messaging_service:8000
  depends_on:
    - database_service
    - messaging_service
```

---

## Usage Examples

### Get KPI Definition

```bash
curl http://localhost:8020/kpis/PERFECT_ORDER_FULFILLMENT
```

Response:
```json
{
  "code": "PERFECT_ORDER_FULFILLMENT",
  "name": "Perfect Order Fulfillment",
  "formula": "(Total perfect orders / Total orders) × 100%",
  "unit": "Percentage",
  "required_objects": ["ORDER", "DELIVERY", "SHIPMENT"],
  "metadata_": {
    "modules": ["ASCM_SCOR"],
    "value_chains": ["SUPPLY_CHAIN"]
  }
}
```

### Get Object Model Schema

```bash
curl http://localhost:8020/object-models/ORDER/schema
```

Response:
```json
{
  "model_code": "ORDER",
  "table_name": "orders",
  "table_schema": {
    "columns": [
      {"name": "id", "type": "UUID", "primary_key": true},
      {"name": "order_number", "type": "VARCHAR(50)", "unique": true},
      {"name": "customer_id", "type": "UUID", "foreign_key": {...}},
      {"name": "order_date", "type": "TIMESTAMP"},
      {"name": "total_amount", "type": "DECIMAL(15,2)"}
    ],
    "indexes": [...],
    "constraints": [...]
  }
}
```

### Get Value Chain KPIs

```bash
curl http://localhost:8020/value-chains/SUPPLY_CHAIN/kpis
```

---

## Integration with Calculation Engine

The Calculation Engine uses this service to fetch KPI definitions:

```python
# In calculation handler
async def get_kpi_definition(self, kpi_code: str):
    response = await http_client.get(
        f"{self.metadata_service_url}/kpis/{kpi_code}"
    )
    return response.json()

# Use definition for calculation
kpi_def = await self.get_kpi_definition("PERFECT_ORDER_FULFILLMENT")
formula = kpi_def["formula"]
required_objects = kpi_def["required_objects"]
```

---

## Key Features

### ✅ No Data Migration

- All existing definitions stay in place
- No changes to file structure
- No rewriting needed

### ✅ Fast Loading

- Definitions loaded once on startup
- Cached in memory
- Sub-millisecond response times

### ✅ Flexible Querying

- Filter KPIs by module, value chain, industry
- Get related definitions (KPIs for a module, etc.)
- Pagination support

### ✅ Schema for Dynamic Tables

- Object models include `table_schema` JSON
- Used by Schema Manager to create tables dynamically
- No Alembic migrations needed for value chain tables

---

## What Changed

### Added ✅

- `app/main.py` - FastAPI service
- `app/config.py` - Configuration
- `app/loader.py` - Definition loader
- `app/api/` - REST API endpoints
- `.env` - Environment configuration

### Unchanged ❌

- `definitions/` - All definitions stay the same
- `db_models.py` - SQLAlchemy models unchanged
- `schemas.py` - Pydantic schemas unchanged
- `utils.py` - Helper functions unchanged

---

## Next Steps

1. ✅ Service created and ready
2. Add to `docker-compose.yml`
3. Test endpoints
4. Update Calculation Engine to use this service
5. Update Schema Manager to use this service

---

## API Documentation

Once running, visit:
- **Interactive Docs**: http://localhost:8020/docs
- **ReDoc**: http://localhost:8020/redoc
- **OpenAPI JSON**: http://localhost:8020/openapi.json

---

## Summary

This service wraps your existing analytics definitions with a REST API, making them accessible to:
- **Calculation Engine** - For KPI formulas and metadata
- **Schema Manager** - For dynamic table creation
- **API Gateway** - For dashboard queries
- **Any other service** - Single source of truth

**Zero migration needed!** Just add the wrapper and go. 🚀
