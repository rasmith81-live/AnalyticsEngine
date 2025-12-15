# Business Metadata Service

Data-driven metadata management service for the Analytics Engine ontology.

## Overview

This service provides a scalable, data-driven approach to storing and managing metadata definitions (entities, metrics, value chains, relationships) in TimescaleDB. It provides a data-driven approach with a database-backed system capable of handling millions of metadata objects.

## Architecture

### Backend Service Integration

This service **integrates with existing backend services** rather than implementing its own infrastructure:

- **database_service**: Database management, CQRS pattern, Redis caching, migrations
- **messaging_service**: Event publishing for metadata changes
- **archival_service**: Version history and retention policies

### Components

```
business_metadata/
├── models/                  # SQLAlchemy models (TimescaleDB hypertables)
│   ├── metadata_definition.py
│   ├── metadata_relationship.py
│   └── metadata_version.py
│
├── repositories/            # CQRS repositories
│   ├── metadata_write_repository.py    # Command side
│   └── metadata_query_repository.py    # Query side
│
├── services/                # Business logic
│   ├── metadata_service.py
│   └── metadata_instantiation_service.py
│
├── api/                     # REST endpoints
│   └── metadata_api.py
│
├── migrations/              # Alembic migrations
│   └── 001_create_metadata_tables.py
│
├── config.py                # Settings (extends DatabaseServiceSettings)
├── dependencies.py          # Dependency injection
└── main.py                  # FastAPI application
```

## Features

### CQRS Pattern
- **Write Repository**: Create, update, delete with event publishing
- **Query Repository**: Optimized reads with Redis caching

### TimescaleDB Hypertables
- `metadata_definitions`: Main metadata storage
- `metadata_relationships`: Knowledge graph edges
- `metadata_versions`: Audit trail and time-travel

### Event Publishing
All metadata changes publish events via messaging_service:
- `metadata.{kind}.created`
- `metadata.{kind}.updated`
- `metadata.{kind}.deleted`
- `metadata.relationship.created`
- `metadata.relationship.deleted`

### Pydantic Model Instantiation
Seamless conversion between database JSONB and Pydantic models from `analytics_metadata_service`.

### Knowledge Graph Queries
- Relationship traversal with configurable depth
- Recursive CTE for graph exploration
- Filter by relationship types

### Version History
- Track all changes with audit trail
- Time-travel queries
- Change descriptions

## API Endpoints

### Generic Endpoints (All Definition Types)

```
POST   /api/v1/metadata/definitions              # Create definition
GET    /api/v1/metadata/definitions/{kind}/{code} # Get by code
PUT    /api/v1/metadata/definitions/{kind}/{code} # Update
DELETE /api/v1/metadata/definitions/{kind}/{code} # Soft delete
GET    /api/v1/metadata/definitions/{kind}        # List by kind
POST   /api/v1/metadata/definitions/search        # Search with filters
GET    /api/v1/metadata/definitions/{kind}/count  # Count by kind
```

### Relationships

```
GET /api/v1/metadata/definitions/{kind}/{code}/relationships  # Get relationships
GET /api/v1/metadata/definitions/{kind}/{code}/graph          # Knowledge graph
```

### Version History

```
GET /api/v1/metadata/definitions/{kind}/{code}/versions  # Version history
```

### Bulk Operations

```
POST /api/v1/metadata/definitions/bulk  # Bulk create/upsert
```

### Type-Specific Convenience Endpoints

```
GET /api/v1/metadata/entities/{code}       # Get entity
GET /api/v1/metadata/metrics/{code}        # Get metric
GET /api/v1/metadata/value-chains/{code}   # Get value chain
```

## Configuration

Extends `DatabaseServiceSettings` from database_service:

```python
# .env file
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/analytics_engine
REDIS_HOST=localhost
REDIS_PORT=6379
SERVICE_PORT=8023
DEBUG=false
LOG_LEVEL=INFO
```

## Running the Service

### Prerequisites

1. Backend services must be running:
   - database_service (PostgreSQL + TimescaleDB + Redis)
   - messaging_service (Redis pub/sub)

2. Install dependencies:
```bash
pip install fastapi uvicorn sqlalchemy asyncpg redis pydantic pydantic-settings
```

### Start Service

```bash
cd services/business_services/business_metadata
python main.py
```

Or with uvicorn:
```bash
uvicorn main:app --host 0.0.0.0 --port 8023 --reload
```

### Run Migrations

Migrations are automatically run on startup via database_service's migration_manager.

## Usage Examples

### Create Entity Definition

```python
import requests

entity = {
    "kind": "entity_definition",
    "code": "CUSTOMER",
    "name": "Customer",
    "description": "Customer entity",
    "table_schema": {...},
    "relationships": [...]
}

response = requests.post(
    "http://localhost:8023/api/v1/metadata/definitions",
    json=entity,
    params={"created_by": "user@example.com"}
)
```

### Get Entity with Relationships

```python
response = requests.get(
    "http://localhost:8023/api/v1/metadata/entities/CUSTOMER",
    params={"include_relationships": True}
)
entity = response.json()
```

### Search Definitions

```python
response = requests.post(
    "http://localhost:8023/api/v1/metadata/definitions/search",
    params={"kind": "entity_definition"},
    json={
        "code": "CUSTOMER*",
        "data": {"category": "sales"}
    }
)
results = response.json()
```

### Get Knowledge Graph

```python
response = requests.get(
    "http://localhost:8023/api/v1/metadata/entities/CUSTOMER/graph",
    params={"depth": 3, "relationship_types": ["contains", "relates to"]}
)
graph = response.json()
# Returns: {"root": "CUSTOMER", "nodes": [...], "edges": [...]}
```

## Event Subscriptions

Other services can subscribe to metadata change events:

```python
from messaging_service.app.subscription_manager import SubscriptionManager

async def handle_entity_created(message):
    print(f"Entity created: {message['code']}")

subscription_manager = SubscriptionManager(settings)
await subscription_manager.subscribe(
    topic="metadata.entity_definition.created",
    handler=handle_entity_created
)
```

## Migration from File-Driven System

To migrate existing metadata from Python files:

1. **Extract definitions** from `analytics_metadata_service/definitions/`
2. **Bulk load** via `/api/v1/metadata/definitions/bulk` endpoint
3. **Verify** counts and relationships
4. **Deprecate** file-driven approach

Example migration script:

```python
from analytics_metadata_service.definitions.entities import *
from analytics_metadata_service.definitions.kpis import *

# Collect all definitions
definitions = [
    CUSTOMER_ENTITY,
    PRODUCT_ENTITY,
    # ... all entities, metrics, value chains
]

# Bulk create
response = requests.post(
    "http://localhost:8023/api/v1/metadata/definitions/bulk",
    json=[d.model_dump() for d in definitions],
    params={"created_by": "migration_script"}
)
```

## Performance

- **Redis caching**: 1-hour TTL for read queries
- **TimescaleDB hypertables**: Optimized for time-series queries
- **CQRS pattern**: Separate read/write paths for scalability
- **Bulk operations**: Efficient upserts for seeding
- **Connection pooling**: Via database_service (20 connections default)

## Monitoring

Integrates with observability_service for:
- Request metrics
- Database query performance
- Cache hit rates
- Event publishing metrics

## Testing

```bash
# Unit tests
pytest tests/unit/

# Integration tests (requires backend services)
pytest tests/integration/

# Load tests
locust -f tests/load/locustfile.py
```

## Documentation

- API docs: http://localhost:8023/docs
- Architecture: `ARCHITECTURE_INTEGRATION.md`
- Backend integration: See `backend_services/` README files
