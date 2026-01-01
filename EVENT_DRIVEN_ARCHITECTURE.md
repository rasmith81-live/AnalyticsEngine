# Event-Driven Architecture

This document describes the event-driven architecture patterns used throughout the AnalyticsEngine platform.

## Overview

The platform follows a **fully event-driven architecture** where:
- **Backend services communicate exclusively via Redis pub/sub messaging**
- **Only the API Gateway uses HTTP for external client communication**
- **Request/reply patterns over pub/sub replace synchronous HTTP calls between services**

## Communication Patterns

### 1. Fire-and-Forget Events (Pub/Sub)

Used for events that don't require a response.

```
┌─────────────┐     publish      ┌─────────────┐     subscribe     ┌─────────────┐
│  Publisher  │ ───────────────► │    Redis    │ ◄─────────────── │  Subscriber │
│   Service   │                  │   Pub/Sub   │                   │   Service   │
└─────────────┘                  └─────────────┘                   └─────────────┘
```

**Channels:**
| Channel | Publisher | Subscribers | Purpose |
|---------|-----------|-------------|---------|
| `simulation.entity.created` | Data Simulator | Database Service, Calculation Engine | Entity creation events |
| `simulation.entity.updated` | Data Simulator | Database Service, Calculation Engine | Entity update events |
| `simulation.entity.deactivated` | Data Simulator | Database Service | Entity deactivation events |
| `simulation.tick` | Data Simulator | Monitoring | Simulation tick events |
| `kpi.calculated` | Calculation Engine | Database Service | Calculated KPI results |
| `kpi.calculated.{kpi_code}` | Calculation Engine | Dashboards | KPI-specific results |
| `archive.kpi_results` | Database Service | Archival Service | KPI results for archival |
| `archival.events` | Database Service | Archival Service | Data archival requests |
| `stream.subscribe` | Calculation Engine | Database Service | Stream subscription requests |
| `stream.unsubscribe` | Calculation Engine | Database Service | Stream unsubscription requests |
| `stream.heartbeat` | Calculation Engine | Database Service | Keep subscriptions alive |

### 2. Request/Reply Pattern (Pub/Sub)

Used for operations that require a response (replaces HTTP calls).

```
┌─────────────┐                  ┌─────────────┐                   ┌─────────────┐
│  Requester  │ ──── request ──► │    Redis    │ ◄── subscribe ─── │  Responder  │
│   Service   │                  │   Pub/Sub   │                   │   Service   │
│             │ ◄─── reply ───── │             │ ──── publish ───► │             │
└─────────────┘                  └─────────────┘                   └─────────────┘
```

**Request Channels:**
| Channel | Responder | Purpose |
|---------|-----------|---------|
| `database.query` | Database Service | Execute read queries |
| `database.command` | Database Service | Execute write commands |
| `metadata.lookup` | Metadata Service | Fetch KPI/entity definitions |

**Request Message Format:**
```json
{
  "correlation_id": "uuid",
  "reply_to": "reply.{service}.{instance}",
  "request_type": "execute_query",
  "source": "calculation_engine",
  "timestamp": "2024-01-01T00:00:00Z",
  "payload": { ... }
}
```

**Response Message Format:**
```json
{
  "correlation_id": "uuid",
  "source": "database_service",
  "timestamp": "2024-01-01T00:00:00Z",
  "payload": { ... }
}
```

Or on error:
```json
{
  "correlation_id": "uuid",
  "source": "database_service",
  "timestamp": "2024-01-01T00:00:00Z",
  "error": "Error message"
}
```

## Service Communication Map

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              FRONTEND SERVICES                                   │
│  ┌─────────────┐                                                                │
│  │  Demo UI    │ ──── HTTP ────┐                                                │
│  └─────────────┘               │                                                │
│                                ▼                                                │
│                         ┌─────────────┐                                         │
│                         │ API Gateway │ ◄──── HTTP (only external interface)    │
│                         └──────┬──────┘                                         │
└────────────────────────────────┼────────────────────────────────────────────────┘
                                 │ HTTP (to business services)
┌────────────────────────────────┼────────────────────────────────────────────────┐
│                         BUSINESS SERVICES                                        │
│                                ▼                                                │
│  ┌─────────────┐    ┌─────────────────┐    ┌──────────────────┐                │
│  │    Data     │    │   Calculation   │    │    Metadata      │                │
│  │  Simulator  │    │     Engine      │    │   Ingestion      │                │
│  └──────┬──────┘    └────────┬────────┘    └────────┬─────────┘                │
│         │                    │                      │                           │
└─────────┼────────────────────┼──────────────────────┼───────────────────────────┘
          │                    │                      │
          │ pub/sub            │ pub/sub              │ pub/sub
          ▼                    ▼                      ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           MESSAGING SERVICE (Redis)                              │
│                                                                                  │
│   Channels: simulation.*, kpi.*, database.*, metadata.*, archive.*, stream.*    │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
          │                    │                      │
          │ pub/sub            │ pub/sub              │ pub/sub
          ▼                    ▼                      ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           BACKEND SERVICES                                       │
│                                                                                  │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐      │
│  │  Database   │    │  Archival   │    │ Observability│    │  Messaging  │      │
│  │   Service   │    │   Service   │    │   Service   │    │   Service   │      │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘      │
│         │                  │                                                    │
│         ▼                  ▼                                                    │
│  ┌─────────────┐    ┌─────────────┐                                            │
│  │ TimescaleDB │    │  Lakehouse  │                                            │
│  └─────────────┘    └─────────────┘                                            │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## Implementation Components

### Request/Reply Infrastructure

**Location:** `services/backend_services/database_service/app/request_reply.py`

- `RequestReplyClient` - Client for making request/reply calls
- `RequestReplyServer` - Server for handling request/reply calls

### Pub/Sub Clients

| Service | Client | Location |
|---------|--------|----------|
| Calculation Engine | `DatabaseClientPubSub` | `calculation_engine_service/app/clients/database_client_pubsub.py` |
| Calculation Engine | `MetadataClientPubSub` | `calculation_engine_service/app/clients/metadata_client_pubsub.py` |
| Data Simulator | `MetadataClientPubSub` | `data_simulator_service/app/metadata_client_pubsub.py` |
| Data Simulator | `SimulatorMessagingClient` | `data_simulator_service/app/messaging_client.py` |

### Request Handlers

| Service | Handler | Location | Channels |
|---------|---------|----------|----------|
| Database Service | `QueryRequestHandler` | `database_service/app/query_request_handler.py` | `database.query`, `database.command` |
| Metadata Service | `MetadataRequestHandler` | `metadata_ingestion_service/app/metadata_request_handler.py` | `metadata.lookup` |

### Event Consumers

| Service | Consumer | Location | Channels |
|---------|----------|----------|----------|
| Database Service | `SimulationDataConsumer` | `database_service/app/simulation_data_consumer.py` | `simulation.entity.*` |
| Database Service | `KPIResultConsumer` | `database_service/app/kpi_result_consumer.py` | `kpi.calculated` |
| Archival Service | `handle_kpi_result_archival` | `archival_service/app/main.py` | `archive.kpi_results` |
| Calculation Engine | `StreamProcessor` | `calculation_engine_service/app/stream_processor.py` | `simulation.entity.created` |

## Data Flow Examples

### Example 1: Simulation Data Flow

```
1. Data Simulator generates entity
2. Publishes to: simulation.entity.created
3. Database Service receives, persists to TimescaleDB
4. Calculation Engine receives, calculates KPIs
5. Calculation Engine publishes to: kpi.calculated
6. Database Service receives, persists KPI result
7. Database Service forwards to: archive.kpi_results
8. Archival Service receives, stores in Lakehouse
```

### Example 2: KPI Calculation Request

```
1. Calculation Engine needs to execute SQL query
2. Sends request to: database.query (with reply_to channel)
3. Database Service receives request
4. Executes query against TimescaleDB
5. Publishes response to: reply.calculation_engine.{instance}
6. Calculation Engine receives response, continues processing
```

### Example 3: Metadata Lookup

```
1. Data Simulator needs KPI definition
2. Sends request to: metadata.lookup (with reply_to channel)
3. Metadata Service receives request
4. Fetches definition from storage
5. Publishes response to: reply.data_simulator.{instance}
6. Data Simulator receives definition, continues simulation
```

## Configuration

All services use the `REDIS_URL` environment variable for pub/sub connectivity:

```bash
REDIS_URL=redis://localhost:6379
```

## Benefits

1. **Loose Coupling** - Services don't need to know each other's locations
2. **Scalability** - Multiple instances can subscribe to the same channels
3. **Resilience** - Services can restart without breaking connections
4. **Observability** - All messages flow through Redis, enabling monitoring
5. **Flexibility** - Easy to add new consumers without modifying publishers
