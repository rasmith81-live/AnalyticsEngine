# Feature Architecture

Comprehensive overview of all Analytics Engine services, their features, and responsibilities across backend, business, and frontend layers.

## Table of Contents

1. [Service Overview](#service-overview)
2. [Backend Services](#backend-services)
3. [Business Services](#business-services)
4. [Frontend Services](#frontend-services)
5. [Support Services](#support-services)
6. [Service Communication](#service-communication)
7. [Feature Specifications](#feature-specifications)

---

## Service Overview

### Architecture Layers

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           FRONTEND SERVICES                                  │
│  ┌──────────────────────────────┐  ┌──────────────────────────────┐        │
│  │     API Gateway (8090)       │  │    Demo Config UI (3000)     │        │
│  │  • Routing & Proxy           │  │  • React SPA                 │        │
│  │  • JWT Auth                  │  │  • KPI Configuration         │        │
│  │  • Rate Limiting             │  │  • Data Mapping              │        │
│  │  • WebSocket Support         │  │  • Admin Console             │        │
│  └──────────────────────────────┘  └──────────────────────────────┘        │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
┌─────────────────────────────────────────────────────────────────────────────┐
│                           BUSINESS SERVICES                                  │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐                │
│  │ Business       │  │ Calculation    │  │ Conversation   │                │
│  │ Metadata(8020) │  │ Engine (8021)  │  │ Service (8026) │                │
│  ├────────────────┤  ├────────────────┤  ├────────────────┤                │
│  │ • Ontology     │  │ • KPI Calc     │  │ • Multi-Agent  │                │
│  │ • KPI Defs     │  │ • TimescaleDB  │  │ • AI Design    │                │
│  │ • Value Chains │  │ • Caching      │  │ • WebSocket    │                │
│  └────────────────┘  └────────────────┘  └────────────────┘                │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐                │
│  │ Demo Config    │  │ Connector      │  │ Ingestion      │                │
│  │ Service (8022) │  │ Service (8023) │  │ Service (8024) │                │
│  ├────────────────┤  ├────────────────┤  ├────────────────┤                │
│  │ • Proposals    │  │ • Connections  │  │ • ETL Pipeline │                │
│  │ • Simulation   │  │ • Schema Disc. │  │ • Scheduling   │                │
│  │ • Licensing    │  │ • Adapters     │  │ • Transform    │                │
│  └────────────────┘  └────────────────┘  └────────────────┘                │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐                │
│  │ Metadata       │  │ Entity         │  │ Data Simulator │                │
│  │ Ingestion(8025)│  │ Resolution     │  │ Service        │                │
│  ├────────────────┤  ├────────────────┤  ├────────────────┤                │
│  │ • Excel Import │  │ • MDM          │  │ • Synthetic    │                │
│  │ • NLP Mapping  │  │ • Golden Rec.  │  │ • Scenarios    │                │
│  │ • Ontology Sync│  │ • Deduplication│  │ • Time Series  │                │
│  └────────────────┘  └────────────────┘  └────────────────┘                │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
┌─────────────────────────────────────────────────────────────────────────────┐
│                           BACKEND SERVICES                                   │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐                │
│  │ Database       │  │ Messaging      │  │ Multi-Agent    │                │
│  │ Service (8000) │  │ Service (8001) │  │ Service        │                │
│  ├────────────────┤  ├────────────────┤  ├────────────────┤                │
│  │ • CQRS         │  │ • Redis Pub/Sub│  │ • Blackboard   │                │
│  │ • Migrations   │  │ • Event Bus    │  │ • Contracts    │                │
│  │ • TimescaleDB  │  │ • Commands     │  │ • Peer Review  │                │
│  └────────────────┘  └────────────────┘  └────────────────┘                │
│  ┌────────────────┐  ┌────────────────┐                                    │
│  │ Archival       │  │ Observability  │                                    │
│  │ Service (8005) │  │ Service (8080) │                                    │
│  ├────────────────┤  ├────────────────┤                                    │
│  │ • Lakehouse    │  │ • Telemetry    │                                    │
│  │ • Parquet      │  │ • OTLP/Traces  │                                    │
│  │ • Retention    │  │ • Alerting     │                                    │
│  └────────────────┘  └────────────────┘                                    │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
┌─────────────────────────────────────────────────────────────────────────────┐
│                           INFRASTRUCTURE                                     │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐                │
│  │ TimescaleDB    │  │ Redis          │  │ Azurite        │                │
│  │ (5432)         │  │ (6379)         │  │ (10000-2)      │                │
│  └────────────────┘  └────────────────┘  └────────────────┘                │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Service Port Summary

| Layer | Service | Port | Bounded Context |
|-------|---------|------|-----------------|
| **Frontend** | API Gateway | 8090 | Ingress & Cross-Cutting |
| **Frontend** | Demo Config UI | 3000 | User Interface |
| **Business** | Business Metadata | 8020 | Platform Ontology |
| **Business** | Calculation Engine | 8021 | KPI Orchestration |
| **Business** | Demo Config Service | 8022 | Simulation & Proposals |
| **Business** | Connector Service | 8023 | Data Connectivity |
| **Business** | Ingestion Service | 8024 | Data Movement |
| **Business** | Metadata Ingestion | 8025 | Knowledge Acquisition |
| **Business** | Conversation Service | 8026 | AI-Driven Design |
| **Business** | Process Simulation | 8027 | DES & What-If Analysis |
| **Backend** | Database Service | 8000 | Database Operations |
| **Backend** | Messaging Service | 8001 | Event Propagation |
| **Backend** | Archival Service | 8005 | Data Archival |
| **Backend** | Multi-Agent Service | - | Agent Infrastructure |
| **Backend** | Observability Service | 8080 | Telemetry & Monitoring |

---

## Backend Services

### Database Service (8000)

**Bounded Context:** Database Operations & Management

| Feature | Description | Status |
|---------|-------------|--------|
| **CQRS Implementation** | Separate read/write operations with QueryRequest/CommandRequest | ✅ |
| **Migration Management** | Automated Alembic execution, TimescaleDB setup | ✅ |
| **Schema Drift Detection** | Two-tier governance (System Core + Dynamic Layer) | ✅ |
| **Retention Management** | Data lifecycle policies, chunk archival triggers | ✅ |
| **Event Consumers** | Telemetry, News, Market event handlers | ✅ |
| **Stream Publisher** | Period-based Continuous Aggregate monitoring | ✅ |
| **Ad-Hoc Query Engine** | Dynamic QueryBuilder with secure SQL generation | ✅ |
| **MCP Server** | PostgreSQL MCP for schema introspection | ✅ |
| **Knowledge Graph MCP** | Ontology traversal, lineage queries | ✅ |

### Messaging Service (8001)

**Bounded Context:** Async Messaging & Event Propagation

| Feature | Description | Status |
|---------|-------------|--------|
| **Redis Pub/Sub** | Core event bus with connection pooling | ✅ |
| **Event Publishing** | Bulk pipeline, gzip compression, correlation IDs | ✅ |
| **Subscription Management** | Webhooks, retry logic, Dead Letter Queue | ✅ |
| **Command Support** | Explicit command routing with channel conventions | ✅ |

### Archival Service (8005)

**Bounded Context:** Data Archival & Lakehouse Storage

| Feature | Description | Status |
|---------|-------------|--------|
| **Archival Event Processing** | Redis subscriber, state management, confirmations | ✅ |
| **Lakehouse Integration** | Azure Data Lake Gen2, Parquet serialization | ✅ |
| **Distributed Tracing** | OpenTelemetry, Prometheus metrics | ✅ |

### Multi-Agent Service

**Bounded Context:** Agent Infrastructure & Coordination

| Feature | Description | Status |
|---------|-------------|--------|
| **Blackboard Architecture** | Shared state coordination, audit log | ✅ |
| **Contract Enforcement** | State machines, tier rules, hard stops | ✅ |
| **Peer Review** | Adversarial pairing, two-failures rule | ✅ |
| **Agent Skills** | Testing, debugging, code review modules | ✅ |

### Observability Service (8080)

**Bounded Context:** Telemetry & Monitoring

| Feature | Description | Status |
|---------|-------------|--------|
| **Telemetry Ingestion** | Traces, metrics, logs normalization | ✅ |
| **OTLP Server** | gRPC for OpenTelemetry protocol | ✅ |
| **Metrics & Analysis** | Prometheus registry, aggregation | ✅ |
| **Alerting System** | Threshold evaluation, Slack/Email notifications | ✅ |
| **Code Traceability** | Class/method usage logging | ✅ |

---

## Business Services

### Business Metadata Service (8020)

**Bounded Context:** Platform Ontology & Definitions

| Feature | Description | Status |
|---------|-------------|--------|
| **Ontology Management** | Entity, Relationship, Metric definitions | ✅ |
| **Access Control** | RBAC, Row-Level Security | ✅ |
| **Analytics Strategy** | Use cases, data sources | ✅ |
| **Artifact Generation** | Pydantic models, TimescaleDB DDL | ✅ |
| **Conversation Modeling** | Interview sessions, utterances | ✅ |

### Calculation Engine Service (8021)

**Bounded Context:** KPI Calculation & Orchestration

| Feature | Description | Status |
|---------|-------------|--------|
| **Calculation Orchestration** | Request routing, parallel batch execution | ✅ |
| **Dynamic Calculation** | Formula library, SQL generator, push-down policy | ✅ |
| **TimescaleDB Integration** | Continuous aggregates, query routing | ✅ |
| **Stream Aggregator** | Redis TimeSeries for sub-second metrics | ✅ |
| **Result Caching** | Domain-specific TTL, invalidation | ✅ |
| **Approximate Analytics** | HyperLogLog, t-digest for fast estimates | ✅ |
| **High-Concurrency** | Request coalescing, hierarchical queries | ✅ |

### Conversation Service (8026)

**Bounded Context:** AI-Driven Design & Modeling

| Feature | Description | Status |
|---------|-------------|--------|
| **Multi-Agent System** | 27 specialized Claude agents | ✅ |
| **LLM Pipeline** | Prompt engineering, intent extraction | ✅ |
| **Pattern Matching** | Vector search, relevance scoring | ✅ |
| **Design Suggestions** | Graph changes, interactive apply/reject | ✅ |
| **Session Management** | WebSocket, context window management | ✅ |
| **Adaptive Communication** | Style detection, detail level adjustment | ✅ |
| **Cross-Agent Collaboration** | Request/response via artifacts | ✅ |

### Demo Config Service (8022)

**Bounded Context:** Simulation, Proposals & Configuration

| Feature | Description | Status |
|---------|-------------|--------|
| **Proposal Generation** | Pricing calculator, questionnaire, PDF/Word | ✅ |
| **License Management** | Key generation, validation, renewal | ✅ |
| **Resource Scheduling** | Gantt charts, critical path | ✅ |
| **Demo Data Orchestration** | Scenario manager, snapshot persistence | ✅ |
| **Client Configuration** | Settings, cascade changes | ✅ |
| **Custom KPIs** | User-defined metrics | ✅ |

### Connector Service (8023)

**Bounded Context:** Data Connectivity & Adapters

| Feature | Description | Status |
|---------|-------------|--------|
| **Connection Management** | Profiles, secure credentials, KeyVault | ✅ |
| **Schema Discovery** | SQL/REST/GraphQL adapters, normalization | ✅ |

### Ingestion Service (8024)

**Bounded Context:** Data Movement & Scheduling

| Feature | Description | Status |
|---------|-------------|--------|
| **Ingestion Pipeline** | Batch/cron scheduler, data extractor | ✅ |
| **Data Standardization** | Entity mapping, quality validation | ✅ |
| **Transformation Logic** | SQL expressions, Python sandbox | ✅ |

### Metadata Ingestion Service (8025)

**Bounded Context:** Knowledge Acquisition & Semantic Understanding

| Feature | Description | Status |
|---------|-------------|--------|
| **Industry Knowledge Base** | NAIC codes, content packs | ✅ |
| **Semantic Mapping** | Entity extraction, value chain inference | ✅ |
| **Formula Decomposition** | Entity.attribute parsing | ✅ |
| **Time-Agnostic Normalization** | Period placeholder replacement | ✅ |
| **LLM Fallback** | Domain inference when spaCy unavailable | ✅ |

### Entity Resolution Service

**Bounded Context:** Master Data Management

| Feature | Description | Status |
|---------|-------------|--------|
| **Matching Engine** | Batch fuzzy matching, blocking strategy | ✅ |
| **Golden Record Management** | Merge logic, retroactive KPI recalculation | ✅ |

### Data Simulator Service

**Bounded Context:** Synthetic Data Generation

| Feature | Description | Status |
|---------|-------------|--------|
| **Time Series Generation** | Trend, seasonality, noise | ✅ |
| **Scenario Generators** | Health retention, churn spike, etc. | ✅ |
| **Entity Snapshots** | Start/End/New population tracking | ✅ |

---

## Frontend Services

### API Gateway (8090)

**Bounded Context:** Ingress & Cross-Cutting Concerns

| Feature | Description | Status |
|---------|-------------|--------|
| **Routing Infrastructure** | FastAPI proxy, versioned routes | ✅ |
| **Service Clients** | Timeout/retry logic per service | ✅ |
| **Security** | JWT auth, rate limiting, circuit breaker | ✅ |
| **TLS Termination** | SSL/TLS, HSTS headers | ✅ |
| **WebSocket Support** | Client connections, Redis broadcast | ✅ |

### Demo Config UI (3000)

**Bounded Context:** User Interaction & Visualization

| Page | Description | Status |
|------|-------------|--------|
| **KPI Configuration** | Metric tree, shopping cart, preview | ✅ |
| **KPI Details** | Formula, objects, benchmarks tabs | ✅ |
| **Object Model Browser** | Module grouping, UML diagrams | ✅ |
| **Required Objects** | Dependency graph, cross-linking | ✅ |
| **Demo Dashboard** | Service health, real-time widgets | ✅ |
| **Visual Data Mapper** | Drag-and-drop source→target | ✅ |
| **Service Proposal** | Pricing, scheduler, Gantt chart | ✅ |
| **Data Source Config** | Connections, schema discovery | ✅ |
| **Admin Console** | License, health, retention, alerts | ✅ |
| **Governance Console** | Data quality, lineage graph, RBAC | ✅ |
| **Excel Import** | Upload, validation, bulk commit | ✅ |
| **Ontology Studio** | Entity editor, relationship builder | ✅ |
| **Simulation Controller** | Scenario selector, job monitor | ✅ |
| **ML Dashboard** | Model registry, training launcher | ✅ |

---

## Support Services

### Azure AD SSO Service

**Bounded Context:** Enterprise Identity

| Feature | Description | Status |
|---------|-------------|--------|
| **OAuth2/OIDC** | Azure AD authorization, token exchange | ✅ |
| **Directory Sync** | Microsoft Graph user/group sync | ✅ |
| **Role Mapping** | AD groups → application roles | ✅ |
| **Multi-Tenant** | Multiple client AD tenants | ✅ |

### Data Governance Service

**Bounded Context:** Data Quality & Compliance

| Feature | Description | Status |
|---------|-------------|--------|
| **Data Quality Rules** | Uniqueness, non-null, format validation | ✅ |
| **Lineage Tracking** | Graph model, upstream/downstream queries | ✅ |

### Machine Learning Service

**Bounded Context:** Predictive Analytics

| Feature | Description | Status |
|---------|-------------|--------|
| **Model Management** | Registry, versioning, inference API | ✅ |
| **Training Pipeline** | Job queue, dataset integration | ✅ |

### Systems Monitor

**Bounded Context:** Infrastructure Health

| Feature | Description | Status |
|---------|-------------|--------|
| **Resource Monitoring** | CPU, memory, disk metrics | ✅ |
| **Alerting** | Rule-based notifications | ✅ |

---

## Service Communication

### Communication Patterns

| Pattern | Usage | Services |
|---------|-------|----------|
| **HTTP REST** | Synchronous request/response | API Gateway → All services |
| **Redis Pub/Sub** | Async events, fire-and-forget | All services via Messaging |
| **Redis Request-Reply** | Async with response | Database queries |
| **WebSocket** | Real-time streaming | Conversation, Dashboard |
| **MCP Protocol** | Agent tool access | Conversation → Database |

### Event Channels

| Channel | Publisher | Subscribers |
|---------|-----------|-------------|
| `ingestion.completed` | Ingestion Service | Calculation Engine |
| `kpi.calculated` | Calculation Engine | Database, Dashboard |
| `archival.events` | Database Service | Archival Service |
| `archival.confirmations` | Archival Service | Database Service |
| `knowledge.*` | Knowledge Graph MCP | Database Service |
| `metadata.*` | Business Metadata | Multiple |

---

## Feature Specifications

Detailed feature specifications for complex capabilities:

| Feature | Document | Status | Description |
|---------|----------|--------|-------------|
| **Predictive What-If** | [FEATURE_SPEC_PREDICTIVE_WHAT_IF.md](./FEATURE_SPEC_PREDICTIVE_WHAT_IF.md) | 🔄 In Development | AI-powered outcome prediction |
| **Process Scenario Modeler** | [FEATURE_SPEC_PROCESS_SCENARIO_MODELER.md](./FEATURE_SPEC_PROCESS_SCENARIO_MODELER.md) | 🔄 In Development | Process simulation and KPI impact |
| **Implementation Plan** | [SIMULATION_FEATURES_IMPLEMENTATION.md](./SIMULATION_FEATURES_IMPLEMENTATION.md) | 📋 Active | Technical implementation tracking |

---

## Related Documentation

- [Multi-Agent Service Architecture](./MULTI_AGENT_SERVICE_ARCHITECTURE.md) - AI agent system details
- [Event-Driven Architecture](./EVENT_DRIVEN_ARCHITECTURE.md) - Messaging patterns
- [Architecture Overview](./README.md) - Design principles and patterns
- [Features Breakdown](../features.md) - Detailed feature point estimates
