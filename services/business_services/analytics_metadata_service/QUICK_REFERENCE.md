# Analytics Models - Quick Reference

## File Structure

```
analytics_models/
├── __init__.py           # Package exports
├── db_models.py          # SQLAlchemy database models
├── schemas.py            # Pydantic API schemas
├── utils.py              # Helper functions
├── examples.py           # Usage examples
├── README.md             # Detailed documentation
└── QUICK_REFERENCE.md    # This file
```

## Hierarchy Overview

```
Industry (e.g., "Financial Services")
  └── ValueChain (e.g., "Risk Management")
       └── Module (e.g., "Credit Assessment")
            └── ObjectModel (e.g., "Credit Risk Assessment")
                 ├── ObjectAttribute (e.g., "credit_score")
                 ├── Object (e.g., "Borrower ABC123")
                 └── KPI (e.g., "Default Rate")
```

## Quick Import Guide

```python
# Database Models
from analytics_models import (
    Industry,
    ValueChain,
    Module,
    ObjectModel,
    ObjectAttribute,
    Object,
    KPI,
    Benchmark
)

# Pydantic Schemas
from analytics_models import (
    IndustryCreate, IndustryUpdate, IndustryRead,
    ValueChainCreate, ValueChainUpdate, ValueChainRead,
    ModuleCreate, ModuleUpdate, ModuleRead,
    ObjectModelCreate, ObjectModelUpdate, ObjectModelRead,
    ObjectAttributeCreate, ObjectAttributeUpdate, ObjectAttributeRead,
    ObjectCreate, ObjectUpdate, ObjectRead,
    KPICreate, KPIUpdate, KPIRead,
    BenchmarkCreate, BenchmarkUpdate, BenchmarkRead
)

# Utilities
from analytics_models.utils import (
    calculate_kpi_status,
    calculate_kpi_variance,
    build_hierarchy_dict,
    get_kpi_summary
)
```

## Common Operations

### Create Industry
```python
industry = Industry(
    name="Financial Services",
    code="FIN_SVC",
    description="Financial services analytics",
    is_active=True
)
```

### Create ValueChain
```python
value_chain = ValueChain(
    name="Risk Management",
    code="RISK_MGMT",
    description="Risk assessment and management",
    display_order=1
)
# Associate with industry
industry.value_chains.append(value_chain)
```

### Create Module
```python
module = Module(
    name="Credit Assessment",
    code="CREDIT_ASSESS",
    display_order=1
)
# Associate with value chain
value_chain.modules.append(module)
```

### Create ObjectModel (Entity-Level UML)
```python
object_model = ObjectModel(
    name="Credit Risk",
    code="CREDIT_RISK",
    schema_definition={
        "classes": [
            {
                "name": "Borrower",
                "stereotype": "entity",
                "description": "Borrower entity"
            }
        ],
        "relationships": []
    }
)
# Associate with module
module.object_models.append(object_model)
```

### Create ObjectAttribute
```python
attribute = ObjectAttribute(
    object_model_id=object_model.id,
    name="creditScore",
    code="CREDIT_SCORE",
    data_type="integer",
    is_required=True,
    attribute_type="field"
)
```

### Create Object
```python
obj = Object(
    object_model_id=1,
    name="Borrower 001",
    code="BORR_001",
    data_values={
        "borrower_id": "001",
        "credit_score": 720
    }
)
```

### Create KPI
```python
kpi = KPI(
    object_model_id=1,
    name="Default Rate",
    code="DEFAULT_RATE",
    unit_of_measure="percentage",
    target_value=2.0,
    current_value=1.5,
    threshold_warning=3.0,
    threshold_critical=5.0
)
```

## Key Features

### All Models Include
- ✅ Auto-incrementing ID
- ✅ Timestamps (created_at, updated_at)
- ✅ Active status flag (is_active)
- ✅ Metadata field (JSON)
- ✅ Database indexes for performance

### Industry
- Unique name and code
- Contains multiple value chains (many-to-many)

### ValueChain
- Belongs to multiple industries (many-to-many)
- Contains multiple modules (many-to-many)
- Has display_order for sorting

### Module
- Belongs to multiple value chains (many-to-many)
- Contains multiple object models (many-to-many)
- Has display_order for sorting

### ObjectModel
- Belongs to multiple modules (many-to-many)
- Contains multiple objects, KPIs, and attributes
- Has schema_definition for UML (entity-level only)
- Has display_order for sorting

### ObjectAttribute
- Belongs to one object model
- Defines attributes and methods for entities
- Has data_type and validation_rules

### Object
- Belongs to one object model
- Has data_values (JSON) for flexible data storage

### KPI
- Belongs to one object model
- Has calculation_formula
- Has target and current values
- Has warning and critical thresholds
- Has category for grouping
- Has display_order for sorting

## Utility Functions

### Calculate KPI Status
```python
status = calculate_kpi_status(
    current_value=1.5,
    target_value=2.0,
    threshold_warning=3.0,
    threshold_critical=5.0
)
# Returns: "normal", "warning", "critical", or "unknown"
```

### Calculate KPI Variance
```python
variance = calculate_kpi_variance(
    current_value=1.5,
    target_value=2.0
)
# Returns: {"variance": -0.5, "variance_percentage": -25.0}
```

### Get KPI Summary
```python
summary = get_kpi_summary(kpis)
# Returns: {
#     "total": 10,
#     "active": 8,
#     "inactive": 2,
#     "status_counts": {"normal": 5, "warning": 2, "critical": 1, "unknown": 0},
#     "categories": {"Financial": 3, "Operational": 5}
# }
```

## Database Relationships

```python
# Access related objects (many-to-many)
industry.value_chains         # List of value chains
value_chain.industries        # List of industries
value_chain.modules           # List of modules
module.value_chains           # List of value chains
module.object_models          # List of object models
object_model.modules          # List of modules
object_model.attributes       # List of attributes
object_model.objects          # List of objects
object_model.kpis            # List of KPIs
obj.object_models            # List of object models
kpi.object_models            # List of object models
```

## CQRS Pattern

### Commands (Write)
```python
from analytics_models.schemas import CreateIndustryCommand

command = CreateIndustryCommand(
    industry=IndustryCreate(name="Tech", code="TECH"),
    command_id=str(uuid.uuid4())
)
```

### Queries (Read)
```python
from analytics_models.schemas import GetIndustryQuery

query = GetIndustryQuery(
    industry_id=1,
    include_modules=True,
    query_id=str(uuid.uuid4())
)
```

## Next Steps

1. **Create Alembic Migration**
   ```bash
   alembic revision --autogenerate -m "Add analytics models"
   alembic upgrade head
   ```

2. **Create Service Layer**
   - Implement business logic
   - Add validation rules
   - Create API endpoints

3. **Create Repository Layer**
   - Implement data access patterns
   - Add caching
   - Optimize queries

4. **Add Tests**
   - Unit tests for models
   - Integration tests for relationships
   - API endpoint tests

## Common Queries

### Get Industry with Full Hierarchy
```python
# Using SQLAlchemy with selectin loading
industry = session.query(Industry)\
    .options(selectinload(Industry.modules)
        .selectinload(Module.object_models)
        .selectinload(ObjectModel.objects))\
    .options(selectinload(Industry.modules)
        .selectinload(Module.object_models)
        .selectinload(ObjectModel.kpis))\
    .filter(Industry.id == 1)\
    .first()
```

### Get Active KPIs by Category
```python
kpis = session.query(KPI)\
    .filter(KPI.is_active == True)\
    .filter(KPI.category == "Financial")\
    .order_by(KPI.display_order)\
    .all()
```

### Get Critical KPIs
```python
critical_kpis = session.query(KPI)\
    .filter(KPI.current_value <= KPI.threshold_critical)\
    .all()
```

## Tips

- Use `display_order` to control sorting in UI
- Use `is_active` for soft deletes
- Use `metadata_` for extensibility
- Use `code` fields for stable identifiers
- Use JSON fields for flexible data storage
- Always include relationships in queries when needed
- Use CQRS pattern for clear separation of concerns
