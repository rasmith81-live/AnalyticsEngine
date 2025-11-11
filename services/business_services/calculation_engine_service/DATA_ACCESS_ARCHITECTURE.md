# Calculation Engine Data Access Architecture

**Date**: November 11, 2025  
**Decision**: How should the Calculation Engine access data for KPI calculations?

---

## 🎯 The Question

When the Calculation Engine needs to query data for KPI calculations, should it:

**Option A**: Call the Database Service directly via HTTP REST?  
**Option B**: Use the Messaging Service (Redis pub/sub) for data requests?

---

## 📊 Current Implementation Status

The `BaseCalculationHandler` has **BOTH** patterns available but **NOT YET IMPLEMENTED**:

```python
class BaseCalculationHandler(ABC):
    def __init__(
        self,
        database_service_url: str,      # Option A: Direct HTTP
        messaging_service_url: str,     # Option B: Pub/Sub
        metadata_service_url: str,
        ...
    ):
        self.database_service_url = database_service_url
        self.messaging_service_url = messaging_service_url
        ...
    
    async def query_data(self, table_name, filters, columns):
        """Query data from value chain schema."""
        # Implementation calls database_service_url
        # THIS IS CURRENTLY A STUB - NOT IMPLEMENTED
        pass
    
    async def publish_result(self, result):
        """Publish calculation result to messaging service."""
        # Implementation calls messaging_service_url  
        # THIS IS CURRENTLY A STUB - NOT IMPLEMENTED
        pass
```

**Current SCOR Handler Implementation:**
- Uses `_execute_query()` method (also a stub)
- Writes SQL queries directly
- Assumes direct database access

---

## 🏗️ Architectural Decision

### **RECOMMENDED: Option A - Direct HTTP to Database Service**

**Rationale:**

1. **Business Service Classification**
   - Calculation Engine is a **Business Service**
   - Database Service is a **Backend Service**
   - Per architecture rules: Backend Services → Business Services = HTTP REST

2. **Synchronous Nature**
   - KPI calculations are **request-response** operations
   - User expects immediate result
   - HTTP REST is natural fit for synchronous queries

3. **Performance**
   - Direct HTTP call: ~10-50ms latency
   - Pub/Sub round-trip: ~50-200ms latency (publish request + wait for response)
   - Real-time calculations need low latency

4. **Simplicity**
   - HTTP REST is simpler for query operations
   - No need for correlation IDs, response channels, timeouts
   - Standard request-response pattern

5. **Error Handling**
   - HTTP status codes (200, 404, 500) are clear
   - Pub/Sub requires custom error handling protocol
   - Easier to implement retries and circuit breakers

---

## 🔄 When to Use Messaging Service

The Calculation Engine **SHOULD** use the Messaging Service for:

### **1. Publishing Results (Event-Driven)**
```python
async def publish_result(self, result: CalculationResult):
    """Publish calculation result to messaging service."""
    # Publish to channel: "events.calculation.completed"
    await messaging_client.publish_event(
        event_type="calculation.completed",
        event_data={
            "kpi_code": result.kpi_code,
            "value": result.value,
            "timestamp": result.timestamp
        }
    )
```

**Use Cases:**
- Notify other services of calculation completion
- Trigger downstream workflows
- Update caches
- Send alerts/notifications
- Audit logging

### **2. Batch Calculation Jobs**
```python
# Scheduler publishes to: "commands.calculation.batch"
await messaging_client.publish_command(
    command_type="calculate_batch",
    payload={
        "job_id": "daily_metrics_001",
        "kpi_codes": ["POF", "OTD", "FILL_RATE"],
        "schedule": "daily"
    }
)

# Calculation Engine subscribes to batch commands
# Processes asynchronously
# Publishes results when complete
```

**Use Cases:**
- Scheduled batch calculations
- Long-running calculations
- Background processing
- Decoupled workflows

---

## 📐 Recommended Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ API Gateway                                                 │
│ POST /api/v1/calculations/calculate                        │
└─────────────────────────────────────────────────────────────┘
                           ↓ HTTP REST (synchronous)
┌─────────────────────────────────────────────────────────────┐
│ Calculation Engine Service                                  │
│ ├─ Receives calculation request                            │
│ ├─ Validates parameters                                     │
│ ├─ Fetches KPI definition (HTTP → Metadata Service)        │
│ └─ Queries data (HTTP → Database Service) ⭐               │
└─────────────────────────────────────────────────────────────┘
                           ↓ HTTP REST (synchronous)
┌─────────────────────────────────────────────────────────────┐
│ Database Service                                            │
│ ├─ Receives query request                                  │
│ ├─ Executes SQL against TimescaleDB                        │
│ └─ Returns result set                                       │
└─────────────────────────────────────────────────────────────┘
                           ↓ HTTP REST (response)
┌─────────────────────────────────────────────────────────────┐
│ Calculation Engine Service                                  │
│ ├─ Receives data                                            │
│ ├─ Applies calculation formula                             │
│ ├─ Publishes result event (Pub/Sub → Messaging) ⭐         │
│ └─ Returns result to API Gateway                           │
└─────────────────────────────────────────────────────────────┘
                           ↓ HTTP REST (response)
┌─────────────────────────────────────────────────────────────┐
│ API Gateway → Frontend                                      │
└─────────────────────────────────────────────────────────────┘
```

**Key Points:**
- ⭐ **Data Query**: HTTP REST (synchronous, low latency)
- ⭐ **Result Publishing**: Pub/Sub (asynchronous, event-driven)

---

## 🔧 Implementation Plan

### **Phase 1: Implement HTTP Data Access**

**1. Create Database Service HTTP Client**
```python
# app/clients/database_client.py
class DatabaseServiceClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(timeout=30.0)
    
    async def query(
        self,
        schema: str,
        table: str,
        filters: Dict[str, Any],
        columns: List[str] = None
    ) -> List[Dict[str, Any]]:
        """Execute query via Database Service."""
        response = await self.client.post(
            f"{self.base_url}/query",
            json={
                "schema": schema,
                "table": table,
                "filters": filters,
                "columns": columns
            }
        )
        return response.json()
```

**2. Implement BaseCalculationHandler.query_data()**
```python
async def query_data(
    self,
    table_name: str,
    filters: Dict[str, Any],
    columns: List[str] = None
) -> List[Dict[str, Any]]:
    """Query data from value chain schema via Database Service."""
    db_client = DatabaseServiceClient(self.database_service_url)
    
    return await db_client.query(
        schema=self.schema_name,  # e.g., "scor_data"
        table=table_name,
        filters=filters,
        columns=columns
    )
```

**3. Update SCOR Handler to Use query_data()**
```python
async def _calculate_perfect_order(self, params: CalculationParams):
    # Replace direct SQL with query_data() call
    orders = await self.query_data(
        table_name="orders",
        filters={
            "order_date": {
                "gte": params.start_date,
                "lte": params.end_date
            }
        }
    )
    # ... rest of calculation
```

### **Phase 2: Implement Result Publishing**

**1. Create Messaging Service Client**
```python
# app/clients/messaging_client.py
class MessagingServiceClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(timeout=30.0)
    
    async def publish_event(
        self,
        event_type: str,
        event_data: Dict[str, Any]
    ):
        """Publish event to messaging service."""
        await self.client.post(
            f"{self.base_url}/messaging/events/publish",
            json={
                "event_type": event_type,
                "source_service": "calculation_engine",
                "event_data": event_data
            }
        )
```

**2. Implement BaseCalculationHandler.publish_result()**
```python
async def publish_result(self, result: CalculationResult):
    """Publish calculation result as event."""
    msg_client = MessagingServiceClient(self.messaging_service_url)
    
    await msg_client.publish_event(
        event_type="calculation.completed",
        event_data={
            "kpi_code": result.kpi_code,
            "value": result.value,
            "unit": result.unit,
            "timestamp": result.timestamp.isoformat(),
            "calculation_time_ms": result.calculation_time_ms
        }
    )
```

**3. Call publish_result() After Calculation**
```python
async def calculate(self, params: CalculationParams) -> CalculationResult:
    # ... perform calculation
    result = CalculationResult(...)
    
    # Publish result event (fire-and-forget)
    try:
        await self.publish_result(result)
    except Exception as e:
        logger.warning(f"Failed to publish result: {e}")
        # Don't fail the calculation if publishing fails
    
    return result
```

---

## 📊 Communication Pattern Summary

| Operation | Protocol | Reason |
|-----------|----------|--------|
| **Fetch KPI Definition** | HTTP REST | Synchronous, metadata lookup |
| **Query Data** | HTTP REST ⭐ | Synchronous, low latency, request-response |
| **Return Result** | HTTP REST | Synchronous, user waiting |
| **Publish Result Event** | Pub/Sub ⭐ | Asynchronous, notify other services |
| **Batch Job Trigger** | Pub/Sub | Asynchronous, scheduled processing |

---

## 🎯 Benefits of This Approach

1. **Low Latency**: Direct HTTP for data queries (10-50ms)
2. **Simple**: Standard request-response for synchronous operations
3. **Event-Driven**: Pub/Sub for asynchronous notifications
4. **Scalable**: Can add caching, connection pooling
5. **Reliable**: HTTP retries, circuit breakers, timeouts
6. **Observable**: Easy to trace HTTP calls
7. **Flexible**: Can switch to pub/sub later if needed

---

## 🚫 Why NOT Pub/Sub for Data Queries?

**Pub/Sub is designed for:**
- ✅ Asynchronous messaging
- ✅ Event notifications
- ✅ Decoupled workflows
- ✅ Fire-and-forget operations

**Pub/Sub is NOT ideal for:**
- ❌ Synchronous request-response
- ❌ Low-latency queries
- ❌ User-waiting operations
- ❌ Complex query results

**Technical Issues with Pub/Sub for Queries:**
1. Need correlation IDs to match responses
2. Need timeout handling (what if no response?)
3. Need response channels (where to listen?)
4. Higher latency (publish + subscribe + process)
5. More complex error handling
6. Harder to debug

---

## 📝 Decision Summary

**✅ USE HTTP REST FOR:**
- Data queries (Calculation Engine → Database Service)
- Metadata lookups (Calculation Engine → Metadata Service)
- Synchronous API calls

**✅ USE PUB/SUB FOR:**
- Result notifications (Calculation Engine → Other Services)
- Batch job triggers (Scheduler → Calculation Engine)
- Event-driven workflows

**This gives us the best of both worlds: Low-latency synchronous queries + Event-driven asynchronous notifications!** 🎉
