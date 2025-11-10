# Analytics Models

This package contains the hierarchical analytics model structure for the AnalyticsEngine project.

## Hierarchy Structure

The analytics models support **many-to-many relationships** with **ValueChain** as an intermediate layer:

```
Industry ←→ ValueChain ←→ Module (many-to-many)
                            ↕
                       ObjectModel (many-to-many)
                            ↕
                       Object + KPI (many-to-many)
```

**Key Features:**
- Industries can have multiple ValueChains (and vice versa)
- ValueChains can contain multiple Modules (and vice versa)
- ObjectModels can belong to multiple Modules
- Objects can belong to multiple ObjectModels
- KPIs can belong to multiple ObjectModels
- Clients can access specific ValueChains

This allows for reusable components across different contexts with better organization.

## Models Overview

### Industry
- **Purpose**: Top-level container representing a business sector or domain
- **Contains**: Multiple value chains
- **Key Fields**:
  - `name`: Industry name
  - `code`: Unique industry code
  - `description`: Industry description
  - `is_active`: Active status flag
  - `metadata_`: Additional metadata (JSON)

### ValueChain
- **Purpose**: Intermediate layer representing sequences of business activities that create value
- **Contains**: Multiple modules
- **Belongs To**: Multiple industries (many-to-many)
- **Key Fields**:
  - `name`: Value chain name
  - `code`: Unique value chain code
  - `description`: Value chain description
  - `display_order`: Order for display/sorting
  - `is_active`: Active status flag
  - `metadata_`: Additional metadata (JSON)

### Module
- **Purpose**: Functional area or component within value chains
- **Contains**: Multiple object models
- **Belongs To**: Multiple value chains (many-to-many)
- **Key Fields**:
  - `name`: Module name
  - `code`: Unique module code
  - `display_order`: Order for display/sorting
  - `is_active`: Active status flag
  - `metadata_`: Additional metadata (JSON)

### ObjectModel
- **Purpose**: Data model or entity type definition with UML class diagram
- **Contains**: Multiple objects, KPIs, and attributes
- **Key Fields**:
  - `name`: Object model name
  - `code`: Unique object model code
  - `schema_definition`: UML class diagram (entity-level only - classes and relationships)
  - `display_order`: Order for display/sorting
  - `is_active`: Active status flag
  - `metadata_`: Additional metadata (JSON)
- **Note**: Attributes and methods are defined separately via ObjectAttribute model

### ObjectAttribute
- **Purpose**: Define attributes and methods for ObjectModel classes
- **Key Fields**:
  - `name`: Attribute/method name
  - `code`: Unique attribute code
  - `object_model_id`: Foreign key to ObjectModel
  - `data_type`: Data type (string, integer, decimal, etc.)
  - `attribute_type`: Type (field, method, computed, etc.)
  - `is_required`: Whether attribute is required
  - `is_unique`: Whether attribute must be unique
  - `validation_rules`: JSON validation rules
  - `default_value`: Default value

### Object
- **Purpose**: Individual data instance within an object model
- **Key Fields**:
  - `name`: Object name
  - `code`: Unique object code
  - `object_model_id`: Foreign key to parent object model
  - `data_values`: JSON containing object data
  - `is_active`: Active status flag
  - `metadata_`: Additional metadata (JSON)

### KPI (Key Performance Indicator)
- **Purpose**: Comprehensive measurable metric with detailed definition, insights, and guidance
- **Core Fields**:
  - `name`: KPI name
  - `code`: Unique KPI code
  - `object_model_id`: Foreign key to parent object model
  - `description`: Brief KPI description
  - `is_active`: Active status flag
  
- **Definition & Context**:
  - `kpi_definition`: Clear explanation of what the KPI measures
  - `expected_business_insights`: Typical business insights from tracking this KPI
  - `measurement_approach`: Outline of the measurement process
  
- **Calculation & Measurement**:
  - `formula`: Standard formula for calculating the KPI
  - `calculation_formula`: Detailed calculation with variables
  - `unit_of_measure`: Unit of measurement
  - `target_value`: Target/goal value
  - `current_value`: Current measured value
  - `threshold_warning`: Warning threshold
  - `threshold_critical`: Critical threshold
  
- **Analysis & Insights**:
  - `trend_analysis`: How the KPI evolves over time and what trends indicate
  - `diagnostic_questions`: Questions to understand current position (JSON)
  - `actionable_steps`: Practical tips for improvement (JSON with operational/strategic/tactical)
  
- **Visualization & Reporting**:
  - `visualization_suggestions`: Recommended charts/graphs (JSON)
  - `risk_warnings`: Potential risks requiring attention (JSON)
  
- **Tools & Integration**:
  - `suggested_tracking_tools`: Tools and technologies for tracking (JSON)
  - `integration_points`: Integration with other systems (JSON)
  
- **Impact & Relationships**:
  - `change_impact`: How changes affect other KPIs
  - `source`: Source reference or external citation
  - `parent_kpi_id`: Reference to parent KPI if derived/custom
  
- **Display & Categorization**:
  - `category`: KPI category for grouping
  - `display_order`: Order for display/sorting
  - `metadata_`: Additional metadata (JSON)

## Database Models vs Pydantic Schemas

### Database Models (`db_models.py`)
- SQLAlchemy ORM models for database persistence
- Define table structure, relationships, and indexes
- Used for database operations (CRUD)
- Include TimescaleDB optimizations with indexes

### Pydantic Schemas (`schemas.py`)
- API request/response models
- Data validation and serialization
- Follow CQRS pattern (Command/Query Responsibility Segregation)
- Three schema types per model:
  - `Create`: For creating new records
  - `Update`: For updating existing records
  - `Read`: For reading/returning data

## Usage Examples

### Creating a New Industry

```python
from analytics_models import Industry, IndustryCreate

# Using Pydantic schema for API
industry_data = IndustryCreate(
    name="Financial Services",
    code="FIN_SVC",
    description="Financial services industry analytics",
    is_active=True
)

# Create database record
industry = Industry(
    name=industry_data.name,
    code=industry_data.code,
    description=industry_data.description,
    is_active=industry_data.is_active
)
```

### Creating a Module

```python
from analytics_models import Module, ModuleCreate

module_data = ModuleCreate(
    industry_id=1,
    name="Risk Management",
    code="RISK_MGMT",
    description="Risk management analytics module",
    display_order=1
)

module = Module(**module_data.model_dump())
```

### Creating an ObjectModel with Objects and KPIs

```python
from analytics_models import ObjectModel, Object, KPI

# Create object model
object_model = ObjectModel(
    module_id=1,
    name="Portfolio",
    code="PORTFOLIO",
    description="Investment portfolio model",
    schema_definition={
        "fields": ["name", "value", "risk_score"]
    }
)

# Create an object
portfolio_obj = Object(
    object_model_id=object_model.id,
    name="Tech Portfolio",
    code="TECH_PORT_001",
    data_values={
        "name": "Technology Stocks",
        "value": 1000000.00,
        "risk_score": 7.5
    }
)

# Create a comprehensive KPI
kpi = KPI(
    object_model_id=object_model.id,
    name="Portfolio Return",
    code="PORT_RETURN",
    description="Measures the return on investment for the portfolio",
    
    # Definition & Context
    kpi_definition="Portfolio Return measures the percentage gain or loss on the investment portfolio over a specific period",
    expected_business_insights="Provides insights into investment performance, risk-adjusted returns, and portfolio manager effectiveness",
    measurement_approach="Calculate by comparing current portfolio value to initial investment, adjusted for contributions and withdrawals",
    
    # Calculation
    formula="Portfolio Return = ((Current Value - Initial Value) / Initial Value) * 100",
    calculation_formula="((current_value - initial_value) / initial_value) * 100",
    unit_of_measure="percentage",
    target_value=10.0,
    current_value=8.5,
    threshold_warning=5.0,
    threshold_critical=2.0,
    
    # Analysis & Insights
    trend_analysis="Positive trends indicate successful investment strategy; compare against benchmark indices",
    diagnostic_questions={
        "questions": [
            "How does our return compare to market benchmarks?",
            "What is driving the current performance?",
            "Are we meeting our risk-adjusted return targets?"
        ]
    },
    actionable_steps={
        "operational": ["Rebalance portfolio quarterly", "Review underperforming assets"],
        "strategic": ["Adjust asset allocation based on market conditions"],
        "tactical": ["Implement stop-loss orders for risk management"]
    },
    
    # Visualization
    visualization_suggestions={
        "primary_charts": [
            {"type": "line_chart", "description": "Portfolio return over time vs benchmark"}
        ]
    },
    
    # Impact & Source
    change_impact="Changes in portfolio return directly impact investor confidence and fund inflows",
    source="Standard financial industry metric",
    
    category="Performance"
)
```

### Creating a Derived KPI

```python
# Create a derived KPI based on a parent KPI
channel_specific_kpi = KPI(
    object_model_id=object_model.id,
    name="Google Ads CAC",
    code="GOOGLE_ADS_CAC",
    description="Customer Acquisition Cost for Google Ads channel",
    
    formula="Google Ads CAC = Total Google Ads Spend / Customers from Google Ads",
    unit_of_measure="USD",
    target_value=40.0,
    current_value=38.0,
    
    # Reference to parent KPI
    parent_kpi_id=1,  # ID of the main CAC KPI
    source="Derived from parent CAC metric, customized for Google Ads channel",
    
    category="Channel-Specific Acquisition"
)
```

## CQRS Pattern

The schemas follow the CQRS (Command Query Responsibility Segregation) pattern:

### Commands (Write Operations)
```python
from analytics_models.schemas import CreateIndustryCommand
import uuid

command = CreateIndustryCommand(
    industry=IndustryCreate(
        name="Healthcare",
        code="HEALTH"
    ),
    command_id=str(uuid.uuid4())
)
```

### Queries (Read Operations)
```python
from analytics_models.schemas import GetIndustryQuery
import uuid

query = GetIndustryQuery(
    industry_id=1,
    include_modules=True,
    query_id=str(uuid.uuid4())
)
```

## Database Indexes

All models include optimized indexes for common query patterns:
- Primary keys (auto-indexed)
- Foreign keys
- Name and code fields
- Active status flags
- Display order fields
- Category fields (for KPIs)

## Relationships

The models use SQLAlchemy relationships with:
- **Cascade deletes**: Deleting a parent deletes all children
- **Lazy loading**: `selectin` for efficient querying
- **Back-populates**: Bidirectional relationships

## Integration with TimescaleDB

While these models don't use TimescaleDB hypertables directly, they are designed to work with the existing TimescaleDB infrastructure:
- All timestamp fields use timezone-aware datetime
- Indexes are optimized for time-series queries
- JSON fields allow flexible metadata storage

## Next Steps

To use these models in your application:

1. **Create Alembic migration**:
   ```bash
   alembic revision --autogenerate -m "Add analytics models"
   ```

2. **Apply migration**:
   ```bash
   alembic upgrade head
   ```

3. **Create service layer** for business logic and API endpoints

4. **Implement repositories** for data access patterns

5. **Add validation logic** for business rules
