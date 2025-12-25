# API Documentation - Analytics Engine

**Complete API reference and integration guide**

---

## Table of Contents

1. [Overview](#overview)
2. [API Gateway](#api-gateway)
3. [Authentication](#authentication)
4. [REST API Conventions](#rest-api-conventions)
5. [Service APIs](#service-apis)
6. [Event APIs](#event-apis)
7. [Error Handling](#error-handling)
8. [Rate Limiting](#rate-limiting)

---

## Overview

Analytics Engine provides a unified REST API through the API Gateway, along with event-driven APIs for asynchronous communication.

### API Endpoints

**Base URLs**:
- **API Gateway**: `http://localhost:8090/api/v1`
- **Direct Service Access**: `http://localhost:{port}`

**Interactive Documentation**:
- **API Gateway**: http://localhost:8090/docs
- **Business Metadata**: http://localhost:8020/docs
- **Calculation Engine**: http://localhost:8021/docs
- **Demo Config Service**: http://localhost:8022/docs

---

## API Gateway

### Unified API Interface

The API Gateway provides a single entry point for all services with:
- Request routing
- Authentication
- Rate limiting
- Response aggregation
- CORS handling

### Gateway Routes

```
/api/v1/metadata/*     → Business Metadata Service (8020)
/api/v1/calculate/*    → Calculation Engine (8021)
/api/v1/config/*       → Demo Config Service (8022)
/api/v1/connector/*    → Connector Service (8023)
/api/v1/ingest/*       → Ingestion Service (8024)
```

### Example Request

```bash
# Via API Gateway (recommended)
curl http://localhost:8090/api/v1/metadata/kpis

# Direct to service (development only)
curl http://localhost:8020/metadata/kpis
```

---

## Authentication

### Development

**No authentication required** for local development.

### Production

**JWT Bearer Token**:
```bash
curl -H "Authorization: Bearer <token>" \
  http://localhost:8090/api/v1/metadata/kpis
```

**API Key**:
```bash
curl -H "X-API-Key: <api_key>" \
  http://localhost:8090/api/v1/metadata/kpis
```

---

## REST API Conventions

### HTTP Methods

| Method | Purpose | Idempotent |
|--------|---------|------------|
| GET | Retrieve resources | Yes |
| POST | Create resources | No |
| PUT | Update/replace resources | Yes |
| PATCH | Partial update | No |
| DELETE | Delete resources | Yes |

### Response Codes

| Code | Meaning | Usage |
|------|---------|-------|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Invalid input |
| 401 | Unauthorized | Missing/invalid auth |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource doesn't exist |
| 422 | Unprocessable Entity | Validation error |
| 500 | Internal Server Error | Server error |

### Request/Response Format

**Request**:
```json
{
  "kpi_id": "revenue_growth",
  "timeframe": "monthly",
  "filters": {
    "region": "US",
    "product": "Widget"
  }
}
```

**Response**:
```json
{
  "status": "success",
  "data": {
    "kpi_id": "revenue_growth",
    "value": 15.5,
    "unit": "percent",
    "timestamp": "2025-12-21T12:00:00Z"
  },
  "metadata": {
    "request_id": "abc-123",
    "duration_ms": 45
  }
}
```

**Error Response**:
```json
{
  "status": "error",
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid timeframe",
    "details": {
      "field": "timeframe",
      "allowed_values": ["daily", "weekly", "monthly"]
    }
  },
  "metadata": {
    "request_id": "abc-123",
    "timestamp": "2025-12-21T12:00:00Z"
  }
}
```

---

## Service APIs

### Business Metadata Service

**Base URL**: `/api/v1/metadata`

#### **Get All KPIs**
```http
GET /api/v1/metadata/kpis
```

**Response**:
```json
{
  "status": "success",
  "data": [
    {
      "kpi_id": "revenue_growth",
      "name": "Revenue Growth Rate",
      "formula": "(current - previous) / previous * 100",
      "unit": "percent",
      "module": "SALES"
    }
  ]
}
```

#### **Get KPI by ID**
```http
GET /api/v1/metadata/kpis/{kpi_id}
```

#### **Get Statistics**
```http
GET /api/v1/metadata/stats
```

**Response**:
```json
{
  "status": "success",
  "data": {
    "total_kpis": 500,
    "total_modules": 25,
    "total_value_chains": 5,
    "total_object_models": 150
  }
}
```

#### **Get Value Chains**
```http
GET /api/v1/metadata/value-chains
```

#### **Get Modules**
```http
GET /api/v1/metadata/modules?value_chain=SUPPLY_CHAIN
```

### Calculation Engine Service

**Base URL**: `/api/v1/calculate`

#### **Calculate KPI**
```http
POST /api/v1/calculate/kpi
```

**Request**:
```json
{
  "kpi_id": "revenue_growth",
  "timeframe": "monthly",
  "start_date": "2025-01-01",
  "end_date": "2025-12-31",
  "filters": {
    "region": "US"
  }
}
```

**Response**:
```json
{
  "status": "success",
  "data": {
    "kpi_id": "revenue_growth",
    "results": [
      {
        "period": "2025-01",
        "value": 12.5,
        "unit": "percent"
      },
      {
        "period": "2025-02",
        "value": 15.2,
        "unit": "percent"
      }
    ]
  }
}
```

#### **Calculate Dashboard**
```http
POST /api/v1/calculate/dashboard
```

**Request**:
```json
{
  "dashboard_id": "sales_overview",
  "timeframe": "monthly",
  "filters": {}
}
```

### Demo Config Service

**Base URL**: `/api/v1/config`

#### **Get Client Config**
```http
GET /api/v1/config/clients/{client_id}
```

#### **Create Client Config**
```http
POST /api/v1/config/clients
```

**Request**:
```json
{
  "client_id": "acme-corp",
  "client_name": "ACME Corporation",
  "license_type": "enterprise",
  "modules": ["SCOR", "CRM", "SALES"]
}
```

#### **Generate Proposal**
```http
POST /api/v1/config/proposals
```

**Request**:
```json
{
  "client_id": "acme-corp",
  "proposal_type": "implementation",
  "modules": ["SCOR", "CRM"],
  "timeline_months": 6
}
```

### Connector Service

**Base URL**: `/api/v1/connector`

#### **List Connectors**
```http
GET /api/v1/connector/profiles
```

#### **Create Connector**
```http
POST /api/v1/connector/profiles
```

**Request**:
```json
{
  "id": "sql-server-prod",
  "name": "Production SQL Server",
  "type": "sql",
  "connection_string": "Server=prod-db;Database=analytics;",
  "credentials": {
    "username": "app_user",
    "password": "encrypted_password"
  }
}
```

#### **Test Connection**
```http
POST /api/v1/connector/profiles/{profile_id}/test
```

---

## Event APIs

### Event-Driven Communication

Services communicate asynchronously via Redis pub/sub.

### Event Types

#### **Domain Events**
```json
{
  "event_type": "entity.created",
  "event_id": "uuid",
  "timestamp": "2025-12-21T12:00:00Z",
  "source_service": "business_metadata",
  "payload": {
    "entity_id": "kpi-123",
    "entity_type": "kpi"
  }
}
```

#### **Integration Events**
```json
{
  "event_type": "calculation.completed",
  "event_id": "uuid",
  "timestamp": "2025-12-21T12:00:00Z",
  "source_service": "calculation_engine",
  "payload": {
    "kpi_id": "revenue_growth",
    "result": 15.5,
    "timeframe": "monthly"
  }
}
```

### Publishing Events

```python
from app.services import MessagingService

await messaging_service.publish_event(
    topic="entity.created",
    payload={
        "entity_id": "kpi-123",
        "entity_type": "kpi"
    }
)
```

### Subscribing to Events

```python
from app.services import MessagingService

async def handle_entity_created(event: dict):
    """Handle entity.created event."""
    entity_id = event["payload"]["entity_id"]
    # Process event
    
await messaging_service.subscribe(
    topic="entity.created",
    handler=handle_entity_created
)
```

---

## Error Handling

### Error Response Format

```json
{
  "status": "error",
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable message",
    "details": {}
  },
  "metadata": {
    "request_id": "abc-123",
    "timestamp": "2025-12-21T12:00:00Z"
  }
}
```

### Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| VALIDATION_ERROR | 422 | Invalid input data |
| NOT_FOUND | 404 | Resource not found |
| UNAUTHORIZED | 401 | Authentication required |
| FORBIDDEN | 403 | Insufficient permissions |
| RATE_LIMIT_EXCEEDED | 429 | Too many requests |
| INTERNAL_ERROR | 500 | Server error |
| SERVICE_UNAVAILABLE | 503 | Service temporarily unavailable |

---

## Rate Limiting

### Limits

**Default Limits**:
- 100 requests per minute per IP
- 1000 requests per hour per API key

**Headers**:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1640095200
```

### Rate Limit Exceeded

**Response**:
```json
{
  "status": "error",
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Try again in 60 seconds.",
    "details": {
      "limit": 100,
      "reset_at": "2025-12-21T12:01:00Z"
    }
  }
}
```

---

## Related Documentation

- **[Service Documentation](../services/)** - Individual service details
- **[Architecture](../architecture/README.md)** - System architecture
- **[Development Guide](../development/README.md)** - Development practices

---

**Next**: [Service Documentation](../services/) | [Development Guide](../development/README.md)

