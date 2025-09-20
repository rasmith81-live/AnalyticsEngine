# Microservices Architecture UML Sequence Diagrams

This directory contains UML sequence diagrams in Lucidchart format that illustrate the interactions between services in the microservices architecture.

## Available Diagrams

### 1. Service Interactions Sequence Diagram
**File:** `service_interactions_sequence_diagram.lucidchart`

This diagram shows the basic endpoint interactions between:
- Client Application
- Messaging Service
- Observability Service
- Prometheus Pushgateway
- Database Service

It illustrates:
- Message request flow
- Periodic metrics export
- OpenTelemetry tracing
- Health check interactions

### 2. Detailed Service Architecture Diagram
**File:** `detailed_service_architecture_diagram.lucidchart`

This comprehensive diagram shows the complete architecture with:
- CQRS pattern implementation (Command/Query separation)
- Write path (Command) flow
- Read path (Query) flow
- TimescaleDB integration with hypertables
- Telemetry and metrics flow

### 3. TimescaleDB Migration Sequence Diagram
**File:** `timescaledb_migration_sequence_diagram.lucidchart`

This specialized diagram illustrates the automated database migration process with:
- Container startup integration with migration triggers
- Schema evolution framework with pre/post validation
- Alembic integration with TimescaleDB hypertable creation
- CQRS pattern integration with write/read model synchronization
- Monitoring and performance tracking during migrations

## How to Open These Diagrams

1. Import these files into [Lucidchart](https://www.lucidchart.com)
2. Go to File > Import > Lucidchart (.lucidchart)
3. Select the file and import

## Architecture Overview

The architecture follows these key principles:

1. **Microservices Architecture**
   - Services are independently deployable
   - Each service has a single responsibility
   - Services communicate via well-defined APIs

2. **CQRS Pattern**
   - Command (Write) and Query (Read) responsibilities are separated
   - Write models optimize for data consistency and integrity
   - Read models optimize for query performance and denormalization

3. **TimescaleDB Integration**
   - Specialized PostgreSQL for time-series data
   - Automatic time partitioning via hypertables
   - Efficient time-based queries and aggregations

4. **Real-time Telemetry**
   - OpenTelemetry for distributed tracing
   - Prometheus-compatible metrics
   - Centralized observability service

5. **Messaging and Event Flow**
   - Redis for caching and messaging
   - Event-driven architecture for service communication

## Key Service Interactions

### Messaging Service
- Receives client requests through API Gateway
- Processes commands through Command Handler
- Updates write models in TimescaleDB
- Publishes events for read model updates
- Exports telemetry to Observability Service
- Pushes metrics to Prometheus Pushgateway

### Observability Service
- Collects traces via OTLP gRPC endpoint
- Exposes metrics at /metrics endpoint for Prometheus scraping
- Provides health check endpoints
- Centralizes monitoring and alerting

### Database Service with TimescaleDB
- Manages both write and read models
- Implements hypertables for time-series data
- Handles automatic time partitioning
- Provides efficient time-based queries and aggregations

## Deployment Considerations

The diagrams reflect the logical architecture. In deployment:
- Services run as Docker containers
- TimescaleDB runs as a specialized PostgreSQL instance
- Redis provides caching and messaging infrastructure
- Prometheus Pushgateway collects metrics from services
