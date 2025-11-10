# Multi-Value Chain Schema Management Strategy

**Date**: November 10, 2025  
**Context**: Thousands of value chains, each with unique object models and KPIs  
**Challenge**: How to manage Alembic migrations and database schemas at scale?

---

## 🎯 The Problem

### Current Situation
```
Value Chains: SCOR, Sales Management, Customer Success, Supply Chain, Finance...
Potentially: THOUSANDS of value chains

Each Value Chain Has:
├─ Unique KPIs (10-100 per chain)
├─ Unique Object Models (5-50 per chain)
├─ Unique Table Schemas (Layer 2 tables)
└─ Unique Relationships (UML diagrams)

Problem: How do we manage database schemas for thousands of value chains?
```

### The Alembic Challenge

**Traditional Approach** (Won't Scale):
```python
# alembic/versions/001_add_scor_tables.py
def upgrade():
    op.create_table('orders', ...)
    op.create_table('shipments', ...)
    op.create_table('deliveries', ...)
    # ... 25 SCOR tables

# alembic/versions/002_add_sales_tables.py
def upgrade():
    op.create_table('leads', ...)
    op.create_table('opportunities', ...)
    # ... 30 Sales tables

# alembic/versions/003_add_customer_success_tables.py
# ... and so on for THOUSANDS of value chains
```

**Problems**:
- ❌ Thousands of migration files
- ❌ Migration conflicts
- ❌ Slow migration execution
- ❌ Hard to track what belongs to which value chain
- ❌ Can't enable/disable value chains dynamically
- ❌ Schema bloat (all tables always present)

---

## 🏗️ Recommended Architecture

### **Hybrid: Metadata-Driven + Schema-per-Value-Chain**

```
┌─────────────────────────────────────────────────────────────┐
│ Metadata Service (Central)                                  │
│ ├─ KPI Definitions (ALL value chains)                       │
│ ├─ Object Model Definitions (ALL value chains)              │
│ ├─ Table Schema Definitions (JSON)                          │
│ └─ Value Chain Registry                                     │
│                                                              │
│ Database: metadata_db                                       │
│ Schema: Single schema with metadata tables                  │
│ Alembic: ONE migration history (stable)                     │
└─────────────────────────────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                   ↓
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ SCOR Service │  │ Sales Service│  │ CustSucc Svc │
│              │  │              │  │              │
│ Calculation  │  │ Calculation  │  │ Calculation  │
│ Engine       │  │ Engine       │  │ Engine       │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       ↓                  ↓                  ↓
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ scor_data    │  │ sales_data   │  │ custsuc_data │
│ (schema)     │  │ (schema)     │  │ (schema)     │
│              │  │              │  │              │
│ Dynamic      │  │ Dynamic      │  │ Dynamic      │
│ Schema       │  │ Schema       │  │ Schema       │
│ Creation     │  │ Creation     │  │ Creation     │
└──────────────┘  └──────────────┘  └──────────────┘

Key: Each value chain gets its own database schema
     Tables created dynamically from metadata definitions
     No Alembic migrations for value chain tables
```

---

## 📊 Three-Tier Schema Strategy

### Tier 1: Metadata Schema (Static, Alembic-Managed)

**Purpose**: Store definitions, not data

**Tables** (Managed by Alembic):
```sql
-- Core metadata tables (rarely change)
CREATE TABLE industries (...);
CREATE TABLE value_chains (...);
CREATE TABLE modules (...);
CREATE TABLE object_models (...);  -- Stores table_schema as JSON
CREATE TABLE kpis (...);
CREATE TABLE benchmarks (...);
CREATE TABLE clients (...);

-- Association tables
CREATE TABLE module_objectmodel_association (...);
CREATE TABLE objectmodel_kpi_association (...);
```

**Alembic Usage**:
```python
# Only for metadata schema changes
# alembic/versions/001_initial_metadata_schema.py
def upgrade():
    op.create_table('object_models', ...)
    op.create_table('kpis', ...)
    # ... core metadata tables only
```

**Characteristics**:
- ✅ Stable schema (changes infrequently)
- ✅ Traditional Alembic migrations
- ✅ Single migration history
- ✅ Easy to manage

---

### Tier 2: Value Chain Schemas (Dynamic, Metadata-Driven)

**Purpose**: Store actual business data per value chain

**Schema Creation** (Dynamic):
```python
# NOT managed by Alembic
# Created dynamically from object_models.table_schema

# When SCOR value chain is activated:
CREATE SCHEMA scor_data;
CREATE TABLE scor_data.orders (...);      -- From object_models
CREATE TABLE scor_data.shipments (...);   -- From object_models
CREATE TABLE scor_data.deliveries (...);  -- From object_models

# When Sales value chain is activated:
CREATE SCHEMA sales_data;
CREATE TABLE sales_data.leads (...);
CREATE TABLE sales_data.opportunities (...);
CREATE TABLE sales_data.deals (...);
```

**How It Works**:
```python
# Schema Manager Service
class ValueChainSchemaManager:
    def activate_value_chain(self, value_chain_code: str):
        """
        Dynamically create schema and tables for a value chain.
        Reads table definitions from metadata.
        """
        # 1. Get value chain metadata
        value_chain = get_value_chain(value_chain_code)
        
        # 2. Create schema
        schema_name = f"{value_chain_code.lower()}_data"
        execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name}")
        
        # 3. Get all object models for this value chain
        object_models = get_object_models_for_value_chain(value_chain_code)
        
        # 4. Create tables from table_schema JSON
        for obj_model in object_models:
            table_schema = obj_model.table_schema  # JSON definition
            create_table_from_schema(schema_name, table_schema)
        
        # 5. Create TimescaleDB hypertables if needed
        for obj_model in object_models:
            if obj_model.is_hypertable:
                create_hypertable(schema_name, obj_model.table_name)
    
    def deactivate_value_chain(self, value_chain_code: str):
        """Drop schema and all tables for a value chain."""
        schema_name = f"{value_chain_code.lower()}_data"
        execute(f"DROP SCHEMA IF EXISTS {schema_name} CASCADE")
```

**Characteristics**:
- ✅ No Alembic migrations needed
- ✅ Dynamic creation/deletion
- ✅ Isolated per value chain
- ✅ Scales to thousands of value chains
- ✅ Enable/disable value chains on demand

---

### Tier 3: Shared Data Schema (Optional, Alembic-Managed)

**Purpose**: Tables shared across ALL value chains

**Tables** (Managed by Alembic):
```sql
-- Shared across all value chains
CREATE TABLE shared_data.customers (...);
CREATE TABLE shared_data.products (...);
CREATE TABLE shared_data.locations (...);
CREATE TABLE shared_data.employees (...);
```

**When to Use**:
- Customer master data (used by SCOR, Sales, Support)
- Product catalog (used by multiple value chains)
- Organization structure (shared reference data)

**Alembic Usage**:
```python
# alembic/versions/002_shared_data_tables.py
def upgrade():
    op.create_schema('shared_data')
    op.create_table('customers', ..., schema='shared_data')
    op.create_table('products', ..., schema='shared_data')
```

---

## 🔧 Implementation Details

### 1. Object Model Definition (Metadata)

```python
# definitions/object_models/order.py
ORDER = {
    "name": "ORDER",
    "display_name": "Order",
    "description": "Customer order",
    "table_name": "orders",
    
    # JSON schema definition for dynamic table creation
    "table_schema": {
        "columns": [
            {
                "name": "id",
                "type": "UUID",
                "primary_key": True,
                "default": "uuid_generate_v4()"
            },
            {
                "name": "order_number",
                "type": "VARCHAR(50)",
                "nullable": False,
                "unique": True,
                "index": True
            },
            {
                "name": "customer_id",
                "type": "UUID",
                "nullable": False,
                "foreign_key": {
                    "table": "shared_data.customers",
                    "column": "id"
                },
                "index": True
            },
            {
                "name": "order_date",
                "type": "TIMESTAMP",
                "nullable": False,
                "index": True
            },
            {
                "name": "total_amount",
                "type": "DECIMAL(15,2)",
                "nullable": False
            },
            {
                "name": "status",
                "type": "VARCHAR(20)",
                "nullable": False,
                "index": True
            },
            {
                "name": "metadata",
                "type": "JSONB",
                "default": "{}"
            },
            {
                "name": "created_at",
                "type": "TIMESTAMP",
                "default": "CURRENT_TIMESTAMP"
            },
            {
                "name": "updated_at",
                "type": "TIMESTAMP",
                "default": "CURRENT_TIMESTAMP"
            }
        ],
        "indexes": [
            {
                "name": "idx_orders_customer_date",
                "columns": ["customer_id", "order_date"]
            },
            {
                "name": "idx_orders_status_date",
                "columns": ["status", "order_date"]
            }
        ],
        "constraints": [
            {
                "type": "check",
                "name": "chk_orders_amount_positive",
                "expression": "total_amount >= 0"
            }
        ]
    },
    
    # Metadata
    "metadata_": {
        "modules": ["ASCM_SCOR", "SALES_MANAGEMENT"],
        "value_chains": ["SUPPLY_CHAIN", "SALES"],
        "is_hypertable": False,
        "partition_key": None
    }
}
```

### 2. Dynamic Table Creation Service

```python
# services/schema_manager/table_creator.py

from typing import Dict, Any
import sqlalchemy as sa
from sqlalchemy import MetaData, Table, Column
from sqlalchemy.dialects import postgresql

class DynamicTableCreator:
    """Creates database tables dynamically from JSON schema definitions."""
    
    TYPE_MAPPING = {
        "UUID": postgresql.UUID,
        "VARCHAR": sa.String,
        "TEXT": sa.Text,
        "INTEGER": sa.Integer,
        "BIGINT": sa.BigInteger,
        "DECIMAL": sa.Numeric,
        "FLOAT": sa.Float,
        "BOOLEAN": sa.Boolean,
        "TIMESTAMP": sa.DateTime,
        "DATE": sa.Date,
        "TIME": sa.Time,
        "JSONB": postgresql.JSONB,
        "ARRAY": postgresql.ARRAY
    }
    
    def create_table_from_schema(
        self, 
        schema_name: str, 
        table_schema: Dict[str, Any],
        engine
    ):
        """
        Create a table from JSON schema definition.
        
        Args:
            schema_name: Database schema name (e.g., 'scor_data')
            table_schema: JSON table schema from object model
            engine: SQLAlchemy engine
        """
        metadata = MetaData(schema=schema_name)
        
        # Parse columns
        columns = []
        for col_def in table_schema['columns']:
            column = self._create_column(col_def)
            columns.append(column)
        
        # Create table
        table = Table(
            table_schema['table_name'],
            metadata,
            *columns,
            schema=schema_name
        )
        
        # Create table in database
        table.create(engine, checkfirst=True)
        
        # Create indexes
        if 'indexes' in table_schema:
            self._create_indexes(
                engine, 
                schema_name, 
                table_schema['table_name'],
                table_schema['indexes']
            )
        
        # Create constraints
        if 'constraints' in table_schema:
            self._create_constraints(
                engine,
                schema_name,
                table_schema['table_name'],
                table_schema['constraints']
            )
        
        return table
    
    def _create_column(self, col_def: Dict[str, Any]) -> Column:
        """Create SQLAlchemy Column from JSON definition."""
        # Parse type
        col_type_str = col_def['type']
        
        # Handle parameterized types (e.g., VARCHAR(50))
        if '(' in col_type_str:
            base_type, params = col_type_str.split('(')
            params = params.rstrip(')').split(',')
            
            if base_type == 'VARCHAR':
                col_type = sa.String(int(params[0]))
            elif base_type == 'DECIMAL':
                col_type = sa.Numeric(int(params[0]), int(params[1]))
            else:
                col_type = self.TYPE_MAPPING[base_type]
        else:
            col_type = self.TYPE_MAPPING[col_type_str]
        
        # Build column
        kwargs = {
            'nullable': col_def.get('nullable', True),
            'primary_key': col_def.get('primary_key', False),
            'unique': col_def.get('unique', False),
            'index': col_def.get('index', False)
        }
        
        # Add default
        if 'default' in col_def:
            if col_def['default'] == 'uuid_generate_v4()':
                kwargs['server_default'] = sa.text('uuid_generate_v4()')
            elif col_def['default'] == 'CURRENT_TIMESTAMP':
                kwargs['server_default'] = sa.func.current_timestamp()
            else:
                kwargs['default'] = col_def['default']
        
        # Add foreign key
        if 'foreign_key' in col_def:
            fk = col_def['foreign_key']
            kwargs['foreign_key'] = f"{fk['table']}.{fk['column']}"
        
        return Column(col_def['name'], col_type, **kwargs)
    
    def _create_indexes(
        self, 
        engine, 
        schema_name: str, 
        table_name: str,
        indexes: list
    ):
        """Create indexes from JSON definition."""
        for idx_def in indexes:
            columns_str = ', '.join(idx_def['columns'])
            sql = f"""
                CREATE INDEX IF NOT EXISTS {idx_def['name']}
                ON {schema_name}.{table_name} ({columns_str})
            """
            engine.execute(sql)
    
    def _create_constraints(
        self,
        engine,
        schema_name: str,
        table_name: str,
        constraints: list
    ):
        """Create constraints from JSON definition."""
        for const_def in constraints:
            if const_def['type'] == 'check':
                sql = f"""
                    ALTER TABLE {schema_name}.{table_name}
                    ADD CONSTRAINT {const_def['name']}
                    CHECK ({const_def['expression']})
                """
                engine.execute(sql)
```

### 3. Value Chain Activation Service

```python
# services/schema_manager/value_chain_activator.py

class ValueChainActivator:
    """Manages activation/deactivation of value chain schemas."""
    
    def __init__(self, db_engine, metadata_service):
        self.engine = db_engine
        self.metadata = metadata_service
        self.table_creator = DynamicTableCreator()
    
    async def activate_value_chain(self, value_chain_code: str):
        """
        Activate a value chain by creating its schema and tables.
        
        Args:
            value_chain_code: Value chain code (e.g., 'SUPPLY_CHAIN')
        """
        # 1. Get value chain metadata
        value_chain = await self.metadata.get_value_chain(value_chain_code)
        if not value_chain:
            raise ValueError(f"Value chain {value_chain_code} not found")
        
        # 2. Create schema
        schema_name = f"{value_chain_code.lower()}_data"
        await self._create_schema(schema_name)
        
        # 3. Get all modules for this value chain
        modules = await self.metadata.get_modules_for_value_chain(value_chain_code)
        
        # 4. Get all object models for these modules
        object_models = []
        for module in modules:
            models = await self.metadata.get_object_models_for_module(module.code)
            object_models.extend(models)
        
        # 5. Create tables for each object model
        for obj_model in object_models:
            if obj_model.table_schema:
                self.table_creator.create_table_from_schema(
                    schema_name,
                    obj_model.table_schema,
                    self.engine
                )
                
                # Create hypertable if needed
                if obj_model.metadata_.get('is_hypertable'):
                    await self._create_hypertable(
                        schema_name,
                        obj_model.table_name,
                        obj_model.metadata_.get('partition_key', 'created_at')
                    )
        
        # 6. Mark value chain as active
        await self.metadata.set_value_chain_status(value_chain_code, 'active')
        
        return {
            "value_chain": value_chain_code,
            "schema": schema_name,
            "tables_created": len(object_models),
            "status": "active"
        }
    
    async def deactivate_value_chain(self, value_chain_code: str):
        """
        Deactivate a value chain by dropping its schema.
        
        WARNING: This will delete all data!
        """
        schema_name = f"{value_chain_code.lower()}_data"
        
        # Drop schema and all tables
        await self.engine.execute(
            f"DROP SCHEMA IF EXISTS {schema_name} CASCADE"
        )
        
        # Mark as inactive
        await self.metadata.set_value_chain_status(value_chain_code, 'inactive')
        
        return {
            "value_chain": value_chain_code,
            "schema": schema_name,
            "status": "inactive"
        }
    
    async def _create_schema(self, schema_name: str):
        """Create database schema."""
        await self.engine.execute(
            f"CREATE SCHEMA IF NOT EXISTS {schema_name}"
        )
    
    async def _create_hypertable(
        self,
        schema_name: str,
        table_name: str,
        time_column: str
    ):
        """Convert table to TimescaleDB hypertable."""
        await self.engine.execute(f"""
            SELECT create_hypertable(
                '{schema_name}.{table_name}',
                '{time_column}',
                if_not_exists => TRUE
            )
        """)
```

---

## 🔄 Alembic Management Strategy

### What Gets Alembic Migrations?

**YES - Use Alembic**:
1. ✅ Metadata schema tables (industries, value_chains, modules, object_models, kpis)
2. ✅ Shared data tables (customers, products, locations)
3. ✅ System tables (users, permissions, audit_logs)

**NO - Don't Use Alembic**:
1. ❌ Value chain-specific tables (orders, shipments, leads, opportunities)
2. ❌ Dynamic tables created from object model definitions
3. ❌ Tables that vary by tenant/client

### Alembic Structure

```
alembic/
├── versions/
│   ├── 001_initial_metadata_schema.py      # Core metadata tables
│   ├── 002_add_shared_data_schema.py       # Shared reference data
│   ├── 003_add_audit_tables.py             # System tables
│   ├── 004_add_client_isolation.py         # Multi-tenancy
│   └── 005_metadata_schema_update.py       # Metadata changes only
├── env.py
└── script.py.mako
```

### Migration Example

```python
# alembic/versions/001_initial_metadata_schema.py

def upgrade():
    # Core metadata tables only
    op.create_table(
        'object_models',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('code', sa.String(100), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('table_name', sa.String(100), nullable=True),
        sa.Column('table_schema', postgresql.JSONB, nullable=True),  # JSON definition
        sa.Column('metadata_', postgresql.JSONB, nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('code')
    )
    
    # Don't create value chain tables here!
    # They're created dynamically from table_schema JSON

def downgrade():
    op.drop_table('object_models')
```

---

## 📋 Schema Management Workflow

### Adding a New Value Chain

```python
# 1. Define object models (Python definitions)
# definitions/object_models/lead.py
LEAD = {
    "name": "LEAD",
    "table_name": "leads",
    "table_schema": { ... },  # JSON schema
    "metadata_": {
        "modules": ["SALES_MANAGEMENT"],
        "value_chains": ["SALES"]
    }
}

# 2. Define KPIs
# definitions/kpis/sales/lead_conversion_rate.py
LEAD_CONVERSION_RATE = KPI(
    name="Lead Conversion Rate",
    code="LEAD_CONVERSION_RATE",
    # ...
)

# 3. Define module
# definitions/modules/sales_management.py
SALES_MANAGEMENT = {
    "code": "SALES_MANAGEMENT",
    "associated_object_models": ["LEAD", "OPPORTUNITY", "DEAL"],
    "associated_kpis": ["LEAD_CONVERSION_RATE", ...]
}

# 4. Define value chain
# definitions/value_chains/sales.py
SALES = {
    "code": "SALES",
    "name": "Sales Management",
    "associated_modules": ["SALES_MANAGEMENT"]
}

# 5. Load definitions into metadata database
python scripts/load_definitions.py --value-chain SALES

# 6. Activate value chain (creates schema and tables dynamically)
POST /api/value-chains/SALES/activate

# Result:
# - Schema 'sales_data' created
# - Tables created from object model definitions
# - No Alembic migration needed!
```

### Updating an Object Model

```python
# Scenario: Add new column to 'orders' table

# 1. Update object model definition
# definitions/object_models/order.py
ORDER = {
    "table_schema": {
        "columns": [
            # ... existing columns
            {
                "name": "priority",  # NEW COLUMN
                "type": "VARCHAR(20)",
                "nullable": True,
                "default": "normal"
            }
        ]
    }
}

# 2. Run schema migration tool
python scripts/migrate_value_chain_schema.py \
    --value-chain SUPPLY_CHAIN \
    --object-model ORDER \
    --action add_column

# Behind the scenes:
# - Reads current table schema from database
# - Compares with new definition
# - Generates ALTER TABLE statement
# - Applies migration
# - Updates metadata

# Result:
# ALTER TABLE scor_data.orders ADD COLUMN priority VARCHAR(20) DEFAULT 'normal';
```

---

## 🎯 Benefits of This Approach

### 1. **Scalability** ✅
- Supports thousands of value chains
- No migration file explosion
- Dynamic schema creation

### 2. **Flexibility** ✅
- Enable/disable value chains on demand
- Add new value chains without code changes
- Update schemas without Alembic migrations

### 3. **Isolation** ✅
- Each value chain in separate schema
- No cross-contamination
- Clear ownership

### 4. **Maintainability** ✅
- Single source of truth (object model definitions)
- Metadata-driven
- Easy to understand

### 5. **Multi-Tenancy** ✅
- Can create schema per client per value chain
- `client_123_scor_data`, `client_456_scor_data`
- Complete data isolation

---

## 🚀 Implementation Roadmap

### Phase 1: Metadata Foundation (Week 1-2)
- ✅ Stabilize metadata schema
- ✅ Create Alembic migrations for metadata tables
- ✅ Ensure object_models.table_schema is comprehensive

### Phase 2: Dynamic Table Creator (Week 3-4)
- ✅ Build DynamicTableCreator service
- ✅ Support all PostgreSQL column types
- ✅ Handle indexes, constraints, foreign keys
- ✅ TimescaleDB hypertable support

### Phase 3: Value Chain Activator (Week 5-6)
- ✅ Build ValueChainActivator service
- ✅ Schema creation/deletion
- ✅ Table creation from metadata
- ✅ Activation status tracking

### Phase 4: Schema Migration Tool (Week 7-8)
- ✅ Compare current vs new schema
- ✅ Generate ALTER statements
- ✅ Safe migration execution
- ✅ Rollback support

### Phase 5: Multi-Tenancy (Week 9-10)
- ✅ Client-specific schemas
- ✅ Schema naming conventions
- ✅ Data isolation guarantees

---

## 📊 Final Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ Metadata Database (metadata_db)                             │
│ ├─ Alembic-managed (stable schema)                          │
│ ├─ Stores: KPIs, Object Models, Modules, Value Chains       │
│ └─ Single source of truth                                   │
└─────────────────────────────────────────────────────────────┘
                           │
                           │ Reads definitions
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Schema Manager Service                                      │
│ ├─ DynamicTableCreator                                      │
│ ├─ ValueChainActivator                                      │
│ └─ SchemaMigrationTool                                      │
└─────────────────────────────────────────────────────────────┘
                           │
                           │ Creates schemas dynamically
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Analytics Database (analytics_db)                           │
│                                                              │
│ ├─ scor_data (schema)           ← SCOR value chain         │
│ │  ├─ orders                                                │
│ │  ├─ shipments                                             │
│ │  └─ deliveries                                            │
│                                                              │
│ ├─ sales_data (schema)          ← Sales value chain        │
│ │  ├─ leads                                                 │
│ │  ├─ opportunities                                         │
│ │  └─ deals                                                 │
│                                                              │
│ ├─ customer_success_data        ← Customer Success         │
│ │  ├─ tickets                                               │
│ │  └─ interactions                                          │
│                                                              │
│ └─ shared_data (schema)         ← Shared reference data    │
│    ├─ customers (Alembic)                                   │
│    ├─ products (Alembic)                                    │
│    └─ locations (Alembic)                                   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎉 Summary

### Answer to Your Question

**"How do we maintain and manage the Alembic objects?"**

**Answer**: **Don't use Alembic for value chain tables!**

Instead:
1. ✅ **Alembic for Metadata** - Core metadata tables only
2. ✅ **Dynamic Creation** - Value chain tables created from JSON definitions
3. ✅ **Schema per Value Chain** - Isolated schemas (scor_data, sales_data, etc.)
4. ✅ **Metadata-Driven** - Single source of truth in object model definitions
5. ✅ **Schema Manager Service** - Handles dynamic table creation/migration

### Key Insight

**Traditional Alembic doesn't scale to thousands of value chains.**

The solution: **Metadata-driven dynamic schema management** where:
- Object models define table schemas as JSON
- Tables are created dynamically when value chains are activated
- No migration files for value chain tables
- Alembic only for stable metadata schema

This approach scales to **unlimited value chains** without migration explosion! 🚀
