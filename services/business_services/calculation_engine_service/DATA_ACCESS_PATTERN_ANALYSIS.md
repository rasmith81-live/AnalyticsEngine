# Data Access Pattern Analysis: Synchronous vs Streaming

**Date**: November 11, 2025  
**Question**: Should the Calculation Engine use streaming pub/sub for data access?

---

## 🔄 Proposed Pattern (User Suggestion)

```
1. Calculation Engine → Database Service (HTTP request)
   "Please send me order data"

2. Database Service → Messaging Service (Pub/Sub)
   Publishes data continuously at prescribed intervals

3. Calculation Engine ← Messaging Service (Subscribe)
   Receives data stream continuously

4. Calculation Engine performs calculations

5. Calculation Engine → Visualization (Send results)
```

---

## ❌ Why This Pattern is PROBLEMATIC

### **Problem 1: Request-Response Mismatch**

**User Scenario:**
```
User clicks "Calculate Perfect Order Fulfillment for January 2025"
↓
User expects result in 1-2 seconds
```

**With Streaming Pattern:**
```
1. Calculation Engine requests data (HTTP)
2. Database Service starts publishing stream
3. Calculation Engine subscribes and waits...
4. Data arrives over time (could be seconds/minutes)
5. Calculation Engine processes stream
6. Finally returns result

Total time: 5-30 seconds (UNACCEPTABLE for real-time UI)
```

**With Direct HTTP:**
```
1. Calculation Engine requests data (HTTP)
2. Database Service queries and returns data
3. Calculation Engine calculates
4. Returns result

Total time: 0.5-2 seconds (ACCEPTABLE)
```

---

### **Problem 2: Correlation Complexity**

**Streaming Pattern Issues:**
```python
# Calculation Engine receives request
async def calculate(params):
    # 1. Send HTTP request to Database Service
    request_id = str(uuid.uuid4())
    await http_client.post("/database/stream-data", {
        "request_id": request_id,
        "table": "orders",
        "filters": {...}
    })
    
    # 2. Subscribe to messaging channel
    channel = f"data.stream.{request_id}"
    await messaging_client.subscribe(channel, callback)
    
    # 3. Wait for data to arrive... HOW LONG?
    # - What if data never arrives?
    # - What if only partial data arrives?
    # - How do we know when stream is complete?
    # - What if we get data for wrong request?
    
    # 4. Need complex state management
    received_data = []
    timeout = 30  # seconds
    start_time = time.time()
    
    while not stream_complete:
        if time.time() - start_time > timeout:
            raise TimeoutError("Data stream timeout")
        await asyncio.sleep(0.1)
    
    # 5. Finally calculate
    result = calculate_kpi(received_data)
    return result
```

**This is MUCH more complex than:**
```python
async def calculate(params):
    # 1. Request data (synchronous)
    data = await database_client.query(table="orders", filters={...})
    
    # 2. Calculate
    result = calculate_kpi(data)
    
    # 3. Return
    return result
```

---

### **Problem 3: Resource Waste**

**Streaming Pattern:**
- Database Service must maintain pub/sub connection
- Messaging Service must buffer messages
- Calculation Engine must maintain subscription
- All for a **ONE-TIME** query!

**Direct HTTP:**
- Single request-response
- Connection closes immediately
- No lingering resources

---

### **Problem 4: Error Handling Nightmare**

**What if things go wrong?**

**Streaming Pattern Failure Scenarios:**
1. HTTP request succeeds, but Database Service fails to publish
2. Database Service publishes, but Calculation Engine misses messages
3. Partial data received, then stream stops
4. Wrong data arrives on channel (correlation ID mismatch)
5. Timeout - how long to wait?
6. Retry - how to restart a stream?

**Direct HTTP Failure Scenarios:**
1. Request fails → Get HTTP error code → Retry
2. That's it!

---

## ✅ When Streaming DOES Make Sense

Your pattern **IS CORRECT** for these scenarios:

### **Scenario 1: Continuous Data Ingestion**
```
IoT Sensors → Database Service → Messaging Service → Calculation Engine
                                                    ↓
                                            Real-time monitoring
                                            Continuous calculations
```

**Example:**
- Temperature sensors send data every second
- Database Service publishes to "sensor.data.stream"
- Calculation Engine subscribes
- Calculates rolling averages, alerts, etc.
- **No user waiting** - continuous background processing

### **Scenario 2: Scheduled Batch Processing**
```
Scheduler → Database Service (trigger export)
                ↓
         Messaging Service (publish data chunks)
                ↓
         Calculation Engine (subscribe)
                ↓
         Process large dataset in chunks
                ↓
         Publish results when complete
```

**Example:**
- Daily batch: Calculate all KPIs for all customers
- Database exports 1M records in chunks of 10K
- Calculation Engine processes each chunk
- Takes 30 minutes - **no user waiting**

### **Scenario 3: Event-Driven Updates**
```
Database Service detects data change
         ↓
Publishes "data.updated" event
         ↓
Calculation Engine subscribes
         ↓
Recalculates affected KPIs
         ↓
Updates cache
```

**Example:**
- New orders arrive in database
- Database Service publishes "orders.inserted" event
- Calculation Engine recalculates affected KPIs
- Updates dashboard cache
- **Proactive, not reactive**

---

## 🎯 Recommended Pattern by Use Case

### **Use Case 1: On-Demand User Request (Real-Time)**
**Pattern**: Synchronous HTTP Request-Response

```
User clicks "Calculate" 
    ↓ HTTP REST
API Gateway
    ↓ HTTP REST
Calculation Engine
    ↓ HTTP REST (synchronous query)
Database Service
    ↓ HTTP REST (response)
Calculation Engine (calculates)
    ↓ HTTP REST (response)
API Gateway
    ↓ HTTP REST
User sees result (1-2 seconds)
```

**Why:**
- User is waiting
- Need low latency
- One-time query
- Simple error handling

---

### **Use Case 2: Scheduled Batch Calculation**
**Pattern**: Asynchronous Pub/Sub

```
Scheduler
    ↓ Pub/Sub (command)
Calculation Engine (subscribes)
    ↓ HTTP REST (query large dataset)
Database Service
    ↓ HTTP REST (response with data)
Calculation Engine (calculates)
    ↓ Pub/Sub (publish results)
Messaging Service
    ↓ Pub/Sub (subscribers notified)
Cache Service, Notification Service, etc.
```

**Why:**
- No user waiting
- Large dataset
- Asynchronous processing
- Multiple subscribers for results

---

### **Use Case 3: Real-Time Data Stream Processing**
**Pattern**: Streaming Pub/Sub (Your Suggested Pattern!)

```
Data Source (IoT, API, etc.)
    ↓ Pub/Sub (continuous stream)
Database Service (stores + publishes)
    ↓ Pub/Sub (data stream)
Calculation Engine (subscribes)
    ↓ Continuous calculations
    ↓ Pub/Sub (publish results)
Real-Time Dashboard
```

**Why:**
- Continuous data flow
- Real-time monitoring
- No request-response needed
- Event-driven architecture

---

## 📊 Pattern Comparison

| Aspect | Synchronous HTTP | Streaming Pub/Sub |
|--------|-----------------|-------------------|
| **Latency** | 10-50ms | 100-500ms+ |
| **Complexity** | Low | High |
| **User Waiting** | ✅ Good | ❌ Bad |
| **Batch Processing** | ❌ Inefficient | ✅ Good |
| **Real-Time Stream** | ❌ Not suitable | ✅ Perfect |
| **Error Handling** | Simple | Complex |
| **Resource Usage** | Minimal | Higher |
| **Correlation** | Not needed | Required |
| **Timeout Handling** | Built-in | Manual |

---

## 🎯 Final Recommendation

### **For Your Analytics Engine:**

**1. On-Demand KPI Calculations (90% of use cases)**
```
✅ USE: Synchronous HTTP REST
Calculation Engine → Database Service (HTTP query)
Database Service → Calculation Engine (HTTP response)
```

**2. Result Notifications**
```
✅ USE: Asynchronous Pub/Sub
Calculation Engine → Messaging Service (publish result event)
Other Services ← Messaging Service (subscribe to events)
```

**3. Scheduled Batch Jobs**
```
✅ USE: Pub/Sub for trigger, HTTP for data
Scheduler → Messaging Service (publish batch command)
Calculation Engine ← Messaging Service (subscribe to commands)
Calculation Engine → Database Service (HTTP query for data)
Calculation Engine → Messaging Service (publish results)
```

**4. Real-Time Streaming (Future Feature)**
```
✅ USE: Streaming Pub/Sub (Your Pattern!)
Data Source → Database Service → Messaging Service → Calculation Engine
```

---

## 💡 Key Insight

**Your suggested pattern is EXCELLENT for streaming data, but NOT for request-response queries!**

Think of it this way:

**Streaming Pub/Sub** = Netflix (continuous stream, no waiting)
**Synchronous HTTP** = Google Search (instant result, user waiting)

For KPI calculations where a user clicks "Calculate" and waits for a result, you want **Google Search**, not **Netflix**!

---

## 🔧 Hybrid Approach (Best of Both Worlds)

```python
class CalculationEngine:
    
    async def calculate_on_demand(self, params):
        """User-triggered calculation - use HTTP."""
        # User is waiting - need fast response
        data = await self.database_client.query(...)  # HTTP
        result = self.calculate(data)
        return result  # HTTP response
    
    async def calculate_batch(self, job_config):
        """Scheduled batch - use pub/sub."""
        # No user waiting - can be async
        data = await self.database_client.query_large(...)  # HTTP
        results = []
        for chunk in data:
            result = self.calculate(chunk)
            results.append(result)
        
        # Publish results
        await self.messaging_client.publish_event(
            "batch.completed",
            {"results": results}
        )  # Pub/Sub
    
    async def process_stream(self):
        """Real-time stream - use pub/sub."""
        # Subscribe to data stream
        await self.messaging_client.subscribe(
            "data.stream",
            self.on_data_received
        )  # Pub/Sub
    
    async def on_data_received(self, data):
        """Handle streaming data."""
        result = self.calculate(data)
        await self.messaging_client.publish_event(
            "realtime.result",
            result
        )  # Pub/Sub
```

**This gives you:**
- ✅ Fast response for user queries (HTTP)
- ✅ Efficient batch processing (Pub/Sub)
- ✅ Real-time streaming capability (Pub/Sub)

---

## 📝 Summary

**Your Pattern:**
- ✅ Perfect for real-time streaming
- ✅ Perfect for continuous data ingestion
- ❌ NOT good for user-waiting queries
- ❌ Adds unnecessary complexity for simple requests

**Recommended Pattern:**
- ✅ HTTP for on-demand queries (user waiting)
- ✅ Pub/Sub for result notifications (event-driven)
- ✅ Pub/Sub for batch triggers (scheduled)
- ✅ Pub/Sub for streaming (continuous data)

**Use the right tool for the job!** 🎯
