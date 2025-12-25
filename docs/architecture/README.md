# Analytics Engine - Architecture Overview

**System architecture, design patterns, and technical decisions**

---

## Table of Contents

1. [System Overview](#system-overview)
2. [Architecture Principles](#architecture-principles)
3. [Microservices Architecture](#microservices-architecture)
4. [Data Architecture](#data-architecture)
5. [Event-Driven Architecture](#event-driven-architecture)
6. [Security Architecture](#security-architecture)
7. [Technology Stack](#technology-stack)
8. [Design Patterns](#design-patterns)

---

## System Overview

Analytics Engine is a **real-time, streaming-first analytics platform** built on a microservices architecture. The system provides on-demand KPI calculations with configurable refresh periods across multiple business value chains.

### Key Characteristics

- **Real-Time Processing**: Sub-second query performance with TimescaleDB continuous aggregates
- **Event-Driven**: Asynchronous communication via Redis pub/sub
- **CQRS Pattern**: Separate read and write models for optimal performance
- **Microservices**: Independently deployable services with clear boundaries
- **Cloud-Native**: Containerized with Docker, orchestrated with Docker Compose/Kubernetes

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         Frontend Layer                          │
│  ┌──────────────┐                        ┌──────────────┐      │
│  │ Demo Config  │                        │  API Gateway │      │
│  │     UI       │◄───────────────────────┤   (8090)     │      │
│  │   (3000)     │                        └──────────────┘      │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                       Business Services                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   Business   │  │ Calculation  │  │  Demo Config │         │
│  │   Metadata   │  │    Engine    │  │   Service    │         │
│  │   (8020)     │  │   (8021)     │  │   (8022)     │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │  Connector   │  │  Ingestion   │  │ Conversation │         │
│  │   Service    │  │   Service    │  │   Service    │         │
│  │   (8023)     │  │   (8024)     │  │   (8026)     │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                      Backend Services                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   Database   │  │  Messaging   │  │  Archival    │         │
│  │   Service    │  │   Service    │  │   Service    │         │
│  │   (8000)     │  │   (8001)     │  │   (8005)     │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                    Infrastructure Layer                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ TimescaleDB  │  │    Redis     │  │   Azurite    │         │
│  │   (5432)     │  │   (6379)     │  │  (10000-2)   │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
└─────────────────────────────────────────────────────────────────┘
```

---

## Architecture Principles

### 1. **Single Responsibility**
Each service has one clear purpose and bounded context:
- **Database Service**: All database operations
- **Messaging Service**: All Redis operations
- **Business Metadata**: KPI and object model definitions
- **Calculation Engine**: KPI calculation orchestration

### 2. **Separation of Concerns**
Clear boundaries between layers:
- **Frontend**: User interface and presentation
- **Business Services**: Domain logic and business rules
- **Backend Services**: Infrastructure and cross-cutting concerns
- **Infrastructure**: Data storage and messaging

### 3. **CQRS (Command Query Responsibility Segregation)**
Separate read and write operations:
- **Commands**: Write operations with validation and business logic
- **Queries**: Optimized read operations with caching
- **Read Models**: Denormalized views for fast queries
- **Write Models**: Normalized for data integrity

### 4. **Event-Driven Communication**
Asynchronous, loosely-coupled services:
- **Events**: Domain events published to Redis
- **Pub/Sub**: Services subscribe to relevant events
- **Event Sourcing**: Audit trail of all changes
- **Eventual Consistency**: Accept temporary inconsistency for scalability

### 5. **API-First Design**
Well-defined contracts between services:
- **REST APIs**: Synchronous request/response
- **Event APIs**: Asynchronous messaging
- **OpenAPI/Swagger**: Auto-generated documentation
- **Versioning**: Backward-compatible changes

### 6. **Cloud-Native**
Built for cloud deployment:
- **Containerization**: Docker for consistency
- **Orchestration**: Docker Compose / Kubernetes
- **Scalability**: Horizontal scaling of services
- **Resilience**: Health checks, retries, circuit breakers

---

## Microservices Architecture

### Service Classification

#### **Backend Services** (Infrastructure)
Provide infrastructure capabilities to other services:

| Service | Port | Responsibility |
|---------|------|----------------|
| Database Service | 8000 | Database operations, CQRS, migrations |
| Messaging Service | 8001 | Redis operations, pub/sub, messaging |
| Archival Service | 8005 | Data archival to lakehouse |
| Observability Service | 8080 | Monitoring, metrics, tracing |

#### **Business Services** (Domain Logic)
Implement business capabilities:

| Service | Port | Responsibility |
|---------|------|----------------|
| Business Metadata | 8020 | KPI definitions, object models |
| Calculation Engine | 8021 | KPI calculation orchestration |
| Demo Config Service | 8022 | Configuration and proposals |
| Connector Service | 8023 | Data source connectors |
| Ingestion Service | 8024 | Data ingestion and transformation |
| Metadata Ingestion | 8025 | Excel/CSV bulk import |
| Conversation Service | 8026 | Chatbot and NLP |

#### **Support Services** (Optional Capabilities)
Provide specialized functionality:

| Service | Port | Responsibility |
|---------|------|----------------|
| Systems Monitor | 8010 | System health monitoring |
| Entity Resolution | 8012 | Entity matching and deduplication |
| Data Governance | 8013 | Data quality and compliance |
| Machine Learning | 8014 | ML model training and inference |

#### **Frontend Services**
User interfaces and API gateway:

| Service | Port | Responsibility |
|---------|------|----------------|
| API Gateway | 8090 | Unified API interface |
| Demo Config UI | 3000 | React frontend application |

### Communication Patterns

```
Frontend → API Gateway → Business Services (HTTP REST)
Backend Services ↔ Backend Services (Redis pub/sub)
Backend Services → Business Services (HTTP REST via Gateway)
Support Services → Any (HTTP REST or messaging)
```

### Service Dependencies

```
Business Metadata
  ├─→ Database Service (HTTP)
  └─→ Messaging Service (HTTP)

Calculation Engine
  ├─→ Business Metadata (HTTP)
  ├─→ Database Service (HTTP)
  └─→ Messaging Service (HTTP)

Connector Service
  ├─→ Database Service (HTTP)
  └─→ Messaging Service (HTTP)

All Services
  ├─→ TimescaleDB (via Database Service)
  └─→ Redis (via Messaging Service)
```

---

## Data Architecture

### Database Strategy

#### **TimescaleDB** (Primary Database)
PostgreSQL extension optimized for time-series data:

**Features**:
- **Hypertables**: Automatic time-based partitioning
- **Continuous Aggregates**: Pre-computed materialized views
- **Compression**: Automatic data compression
- **Retention Policies**: Automated data lifecycle

**Use Cases**:
- Time-series metrics and KPIs
- Event logs and audit trails
- Real-time analytics
- Historical data analysis

#### **Redis** (Cache and Messaging)
In-memory data store:

**Features**:
- **Caching**: Query result caching
- **Pub/Sub**: Event messaging
- **Streams**: Event sourcing
- **TTL**: Automatic expiration

**Use Cases**:
- Query result caching
- Session storage
- Real-time messaging
- Rate limiting

### CQRS Pattern Implementation

#### **Write Side (Commands)**
```
Command → Validation → Business Logic → Write Model → Database
                                              ↓
                                         Event Published
```

**Characteristics**:
- Normalized data model
- Strong consistency
- Validation and business rules
- Event publishing

#### **Read Side (Queries)**
```
Query → Cache Check → Read Model → Optimized Query → Result
```

**Characteristics**:
- Denormalized data model
- Eventual consistency
- Optimized for queries
- Caching enabled

### Data Flow

```
1. Client Request
   ↓
2. API Gateway (routing)
   ↓
3. Business Service (validation)
   ↓
4. Database Service (CQRS)
   ├─→ Command Path: Write to TimescaleDB
   │   └─→ Publish event to Redis
   └─→ Query Path: Read from cache or TimescaleDB
   ↓
5. Response to Client
```

### Schema Management

#### **Two-Tier Strategy**

**Zone 1 (System Core)**:
- Static tables (Auth, Metadata)
- Managed by Alembic migrations
- Strict schema enforcement
- CI/CD validation

**Zone 2 (Dynamic Layer)**:
- User-defined tables
- Application-managed schema
- Self-healing via ConsistencyChecker
- Flexible schema evolution

---

## Event-Driven Architecture

### Event Types

#### **Domain Events**
Business-significant occurrences:
- `entity.created`
- `entity.updated`
- `entity.deleted`
- `calculation.completed`
- `ingestion.completed`

#### **Integration Events**
Cross-service communication:
- `data.ingested`
- `schema.changed`
- `archival.requested`
- `archival.completed`

#### **System Events**
Infrastructure events:
- `service.started`
- `service.stopped`
- `health.degraded`
- `migration.completed`

### Event Flow

```
1. Service A: Perform operation
   ↓
2. Service A: Publish event to Redis
   ↓
3. Redis: Broadcast to subscribers
   ↓
4. Service B, C, D: Receive event
   ↓
5. Services: Process event asynchronously
   ↓
6. Services: Update read models
```

### Event Schema

```json
{
  "event_id": "uuid",
  "event_type": "entity.created",
  "timestamp": "2025-12-21T12:00:00Z",
  "source_service": "business_metadata",
  "correlation_id": "uuid",
  "payload": {
    "entity_id": "123",
    "entity_type": "kpi",
    "data": {...}
  }
}
```

---

## Security Architecture

### Authentication

#### **Development**
- Mock Identity Provider (OIDC-compatible)
- No Azure dependencies
- Mirrors production auth flows

#### **Production**
- Azure AD SSO (OIDC/OAuth2)
- JWT tokens
- Role-based access control (RBAC)

### Authorization

#### **Row-Level Security (RLS)**
- Dynamic SQL WHERE clauses
- User/role-based filtering
- Implemented in Database Service

#### **API Security**
- API Gateway authentication
- Service-to-service authentication
- Rate limiting
- CORS configuration

### Data Security

#### **Encryption**
- TLS/SSL for all HTTP traffic
- Database encryption at rest
- Secrets management (environment variables)

#### **Sensitive Data**
- Credentials stored in database (JSONB encrypted)
- No hardcoded secrets
- Environment-based configuration

---

## Technology Stack

### Core Technologies

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Framework** | FastAPI | High-performance async web framework |
| **Database** | TimescaleDB | Time-series PostgreSQL extension |
| **Cache/Messaging** | Redis | In-memory data store and pub/sub |
| **ORM** | SQLAlchemy 2.0+ | Database abstraction with async support |
| **Migration** | Alembic | Database schema versioning |
| **Validation** | Pydantic v2 | Data validation and serialization |
| **Containerization** | Docker | Application containerization |
| **Orchestration** | Docker Compose | Multi-container orchestration |
| **Frontend** | React + Vite | Modern web application |
| **API Docs** | OpenAPI/Swagger | Auto-generated API documentation |

### Supporting Technologies

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Observability** | OpenTelemetry | Distributed tracing |
| **Metrics** | Prometheus | Metrics collection |
| **Storage** | Azure Blob Storage | Data lake storage |
| **Testing** | Pytest | Unit and integration testing |
| **Linting** | Ruff | Python linting |
| **Type Checking** | MyPy | Static type checking |

---

## Design Patterns

### 1. **CQRS (Command Query Responsibility Segregation)**
Separate read and write operations for optimal performance.

### 2. **Event Sourcing**
Store state changes as a sequence of events.

### 3. **Repository Pattern**
Abstract data access logic from business logic.

### 4. **Factory Pattern**
Create objects without specifying exact classes.

### 5. **Strategy Pattern**
Define family of algorithms, encapsulate each one.

### 6. **Observer Pattern**
Event-driven communication between services.

### 7. **Circuit Breaker**
Prevent cascading failures in distributed systems.

### 8. **Retry Pattern**
Automatic retry with exponential backoff.

---

## Architecture Benefits

### ✅ **Scalability**
- Services scale independently
- Horizontal scaling support
- Database connection pooling
- Redis-based caching

### ✅ **Maintainability**
- Clear service boundaries
- Consistent patterns
- Centralized configuration
- Automated migrations

### ✅ **Performance**
- TimescaleDB for time-series
- Continuous aggregates
- Redis caching
- Sub-second queries

### ✅ **Reliability**
- Health checks
- Circuit breakers
- Retry mechanisms
- Event-driven resilience

### ✅ **Flexibility**
- Microservices independence
- Technology diversity
- Easy feature addition
- Gradual migration

---

## Related Documentation

- **[Microservices Architecture](./microservices.md)** - Detailed service design
- **[Data Architecture](./data-architecture.md)** - Database and CQRS patterns
- **[Event-Driven Architecture](./event-driven.md)** - Messaging and events
- **[Security Architecture](./security.md)** - Authentication and authorization
- **[CQRS Pattern](./cqrs-pattern.md)** - Command/Query separation

---

**Next**: [Data Architecture](./data-architecture.md) | [Development Guide](../development/README.md)

