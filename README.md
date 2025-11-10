# MarketNovaTrader

## Overview

This project extends the base-platforn into an automated trading platform called MarketNovaTrader.

## Architecture

The project uses a microservices architecture with clear separation of concerns:

### Backend Services (Infrastructure)

#### 1. **Database Service** (`database_service`)
- **Purpose**: Centralized database operations, schema management, and TimescaleDB functionality
- **Port**: 8000
- **Features**:
  - CQRS command/query execution
  - Automated migration management
  - TimescaleDB hypertable operations
  - Schema validation and discovery
  - Real-time read model projections

#### 2. **Messaging Service** (`messaging_service`)
- **Purpose**: Centralized Redis operations, pub/sub management, and inter-service communication
- **Port**: 8001
- **Features**:
  - Event publishing and consumption
  - Redis connection management
  - Message routing and queuing
  - Subscription management
  - Dead letter queue handling

#### 3. **Archival Service** (`archival_service`)
- **Purpose**: TimescaleDB data archival to lakehouse
- **Port**: 8004
- **Features**:
  - Automated data retention policies
  - Lakehouse integration (Azure Storage)
  - Chunk compression and archival

#### 4. **Observability Service** (`observability_service`)
- **Purpose**: Centralized monitoring, metrics, and distributed tracing
- **Port**: 8080, 4317 (OTLP)
- **Features**:
  - OpenTelemetry trace collection
  - Prometheus metrics aggregation
  - Service health monitoring
  - Performance analytics

#### 5. **Calculation Engine Service** (`calculation_engine_service`)
- **Purpose**: Generic KPI calculation orchestration
- **Port**: 8021
- **Features**:
  - Value chain calculation routing
  - Parallel KPI execution
  - Result caching and aggregation
  - Dashboard calculation support

### Business Services (Domain Logic)

#### 1. **Analytics Metadata Service** (`analytics_metadata_service`)
- **Purpose**: Single source of truth for KPI, Object Model, Module, and Value Chain definitions
- **Port**: 8020
- **Features**:
  - 500+ KPI definitions via REST API
  - Object model schemas for dynamic table creation
  - Module and value chain registry
  - Industry standards integration (SCOR, etc.)

#### 2. **Systems Monitor** (`systems_monitor`)
- **Port**: 8010
- **Purpose**: System health and performance monitoring

#### 3. **Controller Service** (`controller_service`)
- **Port**: 8011
- **Purpose**: Orchestration and workflow management

#### 4. **Entity Resolution Service** (`entity_resolution_service`)
- **Port**: 8012
- **Purpose**: Entity matching and deduplication

#### 5. **Data Governance Service** (`data_governance_service`)
- **Port**: 8013
- **Purpose**: Data quality and compliance management

#### 6. **Machine Learning Service** (`machine_learning_service`)
- **Port**: 8014
- **Purpose**: ML model training and inference

### Frontend Services

#### **API Gateway** (`api_gateway`)
- **Purpose**: Unified interface for all services
- **Port**: 8090
- **Features**:
  - Request routing and aggregation
  - Rate limiting and circuit breaking
  - CORS and authentication
  - Service health checks

## Key Improvements Over Traditional Architecture

### ✅ **Eliminated Common Directory**
- All shared functionality consolidated into dedicated services
- No more scattered common utilities
- Clear service boundaries and responsibilities

### ✅ **Centralized Database Operations**
- Single point for all database interactions
- Consistent CQRS pattern enforcement
- Optimized TimescaleDB operations
- Automated migration management

### ✅ **Centralized Messaging**
- Redis operations in one place
- Event routing and management
- Subscription lifecycle management
- Message reliability and error handling

### ✅ **Real-time Processing with CQRS**
- Command/Query separation with optimized execution paths
- TimescaleDB hypertables for time-series data
- Continuous aggregates for read model optimization
- Event-driven architecture with Redis integration

## Technology Stack

- **Framework**: FastAPI
- **Database**: TimescaleDB (PostgreSQL extension)
- **Messaging**: Redis
- **ORM**: SQLAlchemy 2.0+ with asyncio
- **Migration**: Alembic with automated management
- **Data Validation**: Pydantic v2
- **Containerization**: Docker & Docker Compose

## CI/CD

This project is equipped with a GitHub Actions CI/CD workflow that automates testing, building, and pushing Docker images to Docker Hub. The workflow is triggered on every push to the `main` branch.

Key features:
- Automated tests with `pytest`.
- Parallel Docker image builds for all services.
- Dynamic image tagging based on the repository and service name.
- Configurability for different GitHub and Docker Hub accounts via repository secrets.

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Python 3.8+ (for local development)

### Running the Services

1. **Start all services**:
   ```powershell
   docker-compose up --build
   ```

2. **Verify services are running**:
   - Database Service: http://localhost:8000/health
   - Messaging Service: http://localhost:8001/health
   - Service A: http://localhost:8002/health
   - Service B: http://localhost:8003/health

3. **Run migrations**:
   ```powershell
   # Migrations run automatically on startup
   # Check logs: docker-compose logs database_service
   ```

### API Documentation

Once services are running, access interactive API documentation:

- Database Service: http://localhost:8000/docs
- Messaging Service: http://localhost:8001/docs
- Service A: http://localhost:8002/docs
- Service B: http://localhost:8003/docs

## Service Interaction Examples

### Creating an Item in Service A (CQRS Command)
```bash
curl -X POST "http://localhost:8002/items" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Sample Item",
    "description": "Created via CQRS pattern",
    "created_by": "user123"
  }'
```

### Querying Items (CQRS Query with TimescaleDB)
```bash
curl "http://localhost:8002/items?limit=10&name_filter=Sample"
```

### Real-time Analytics
```bash
curl "http://localhost:8002/analytics/items-by-hour?hours_back=24"
```

### Cross-Service Communication
```bash
curl -X POST "http://localhost:8002/collaborate-with-service-b" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello from Service A"}'
```

## Development

### Local Development Setup

1. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

2. **Set environment variables**:
   ```powershell
   $env:DATABASE_URL = "postgresql+asyncpg://user:password@localhost:5432/multiservice_db"
   $env:REDIS_URL = "redis://localhost:6379"
   ```

3. **Run individual services**:
   ```powershell
   # Database Service
   cd services/backend_services/database_service
   uvicorn app.main:app --reload --port 8000

   # Messaging Service  
   cd services/backend_services/messaging_service
   uvicorn app.main:app --reload --port 8001

   # Service A
   cd services/service_a
   uvicorn app.main:app --reload --port 8002

   # Service B
   cd services/service_b
   uvicorn app.main:app --reload --port 8003
   ```

## Testing

### Unit Tests
```powershell
pytest tests/unit/
```

### Integration Tests
```powershell
pytest tests/integration/
```

### Load Tests
```powershell
pytest tests/performance/
```

## Monitoring

### Health Checks
- All services expose `/health` endpoints
- Database connectivity validation
- Redis connectivity validation
- Service dependency checks

### Metrics
- Command/Query execution times
- Event processing rates
- Database connection pool status
- Redis operation metrics

## Architecture Benefits

### 🎯 **Single Responsibility**
- Each service has one clear purpose
- Database operations centralized
- Messaging operations centralized
- Business logic separated

### 🚀 **Scalability**
- Services can be scaled independently
- Database service handles connection pooling
- Messaging service manages Redis connections
- Horizontal scaling support

### 🔧 **Maintainability**
- Clear service boundaries
- Consistent CQRS patterns
- Centralized configuration
- Automated migrations

### 📊 **Real-time Processing**
- TimescaleDB for time-series data
- Continuous aggregates for analytics
- Event-driven updates
- Sub-second query performance

## Contributing

1. Fork the repository
2. Create a feature branch
3. Implement changes with tests
4. Submit a pull request

## License

MIT License - see LICENSE file for details.
