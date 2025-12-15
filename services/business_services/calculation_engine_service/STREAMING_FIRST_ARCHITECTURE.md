# Streaming-First Analytics Architecture

**Date**: November 11, 2025  
**Key Insight**: 80% of analytics requests are streaming, 20% are one-time queries

---

## 🎯 Use Case Distribution

```
80% - Streaming Analytics (Real-time dashboards, continuous monitoring)
20% - One-Time Queries (Ad-hoc analysis, reports)
```

**This changes EVERYTHING!** Your suggested pattern is the PRIMARY pattern, not the exception.

---

## 🏗️ Dual-Mode Architecture

### **Mode 1: Streaming Analytics (80% of requests) - PRIMARY**

**Pattern**: Pub/Sub Streaming (Your Suggested Pattern!)

```
┌─────────────────────────────────────────────────────────────┐
│ Data Sources (IoT, APIs, Databases, Event Streams)         │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Database Service                                            │
│ ├─ Ingests data continuously                                │
│ ├─ Stores in TimescaleDB                                    │
│ └─ Publishes to Messaging Service                           │
└─────────────────────────────────────────────────────────────┘
                           ↓ Pub/Sub (continuous stream)
┌─────────────────────────────────────────────────────────────┐
│ Messaging Service (Redis Pub/Sub)                          │
│ ├─ Channel: "data.stream.{domain}"                         │
│ ├─ Channel: "data.stream.supply_chain"                     │
│ ├─ Channel: "data.stream.finance"                          │
│ └─ Channel: "data.stream.marketing"                        │
└─────────────────────────────────────────────────────────────┘
                           ↓ Subscribe
┌─────────────────────────────────────────────────────────────┐
│ Calculation Engine Service                                  │
│ ├─ Subscribes to data streams                              │
│ ├─ Receives data continuously                              │
│ ├─ Calculates KPIs in real-time                            │
│ └─ Publishes results                                        │
└─────────────────────────────────────────────────────────────┘
                           ↓ Pub/Sub (results stream)
┌─────────────────────────────────────────────────────────────┐
│ Messaging Service                                           │
│ ├─ Channel: "analytics.results.{kpi_code}"                 │
│ └─ Channel: "analytics.results.dashboard.{id}"             │
└─────────────────────────────────────────────────────────────┘
                           ↓ Subscribe
┌─────────────────────────────────────────────────────────────┐
│ Frontend / Real-Time Dashboards                            │
│ ├─ WebSocket connection to API Gateway                     │
│ ├─ Subscribes to result streams                            │
│ └─ Updates UI in real-time                                 │
└─────────────────────────────────────────────────────────────┘
```

**Characteristics:**
- ✅ Continuous data flow
- ✅ Real-time updates
- ✅ No request-response needed
- ✅ Multiple dashboards can subscribe
- ✅ Low latency for streaming data
- ✅ Scalable (add more subscribers)

---

### **Mode 2: One-Time Queries (20% of requests) - SECONDARY**

**Pattern**: Synchronous HTTP Request-Response

```
┌─────────────────────────────────────────────────────────────┐
│ User / Frontend                                             │
│ "Calculate Perfect Order Fulfillment for January 2025"     │
└─────────────────────────────────────────────────────────────┘
                           ↓ HTTP REST
┌─────────────────────────────────────────────────────────────┐
│ API Gateway                                                 │
└─────────────────────────────────────────────────────────────┘
                           ↓ HTTP REST
┌─────────────────────────────────────────────────────────────┐
│ Calculation Engine Service                                  │
│ ├─ Receives one-time calculation request                   │
│ ├─ Queries Database Service (HTTP)                         │
│ ├─ Performs calculation                                     │
│ └─ Returns result                                           │
└─────────────────────────────────────────────────────────────┘
                           ↓ HTTP REST
┌─────────────────────────────────────────────────────────────┐
│ Database Service                                            │
│ ├─ Executes query                                           │
│ └─ Returns result set                                       │
└─────────────────────────────────────────────────────────────┘
                           ↓ HTTP REST (response)
┌─────────────────────────────────────────────────────────────┐
│ User sees result (1-2 seconds)                              │
└─────────────────────────────────────────────────────────────┘
```

**Characteristics:**
- ✅ Fast response for user
- ✅ Simple request-response
- ✅ Good for ad-hoc queries
- ✅ Historical data analysis
- ✅ One-time reports

---

## 🔄 Streaming Analytics Implementation

### **1. Database Service - Data Publisher**

```python
# services/backend_services/database_service/app/stream_publisher.py

class DataStreamPublisher:
    """Publishes data changes to messaging service for streaming analytics."""
    
    def __init__(self, messaging_client: MessagingClient):
        self.messaging_client = messaging_client
        self.active_streams = {}
    
    async def start_stream(self, domain: str, config: StreamConfig):
        """
        Start publishing data stream for a domain.
        
        Args:
            domain: Domain name (e.g., supply_chain, sales)
            config: Stream configuration (tables, frequency, filters)
        """
        channel = f"data.stream.{domain}"
        
        # Start background task to publish data
        task = asyncio.create_task(
            self._publish_stream(channel, config)
        )
        
        self.active_streams[domain] = task
        logger.info(f"Started data stream for {domain} on channel {channel}")
    
    async def _publish_stream(self, channel: str, config: StreamConfig):
        """Continuously publish data to channel."""
        while True:
            try:
                # Query new/updated data
                data = await self._query_stream_data(config)
                
                if data:
                    # Publish to messaging service
                    await self.messaging_client.publish_message(
                        channel=channel,
                        payload={
                            "timestamp": datetime.utcnow().isoformat(),
                            "data": data,
                            "metadata": {
                                "table": config.table,
                                "record_count": len(data)
                            }
                        }
                    )
                    
                    logger.debug(f"Published {len(data)} records to {channel}")
                
                # Wait for next interval
                await asyncio.sleep(config.interval_seconds)
                
            except Exception as e:
                logger.error(f"Error publishing stream: {e}")
                await asyncio.sleep(5)  # Backoff on error
    
    async def _query_stream_data(self, config: StreamConfig):
        """Query data for streaming."""
        # Get data since last publish
        query = f"""
            SELECT * FROM {config.schema}.{config.table}
            WHERE updated_at > %(last_timestamp)s
            ORDER BY updated_at ASC
            LIMIT %(batch_size)s
        """
        
        result = await self.execute_query(query, {
            "last_timestamp": config.last_timestamp,
            "batch_size": config.batch_size
        })
        
        # Update last timestamp
        if result:
            config.last_timestamp = result[-1]["updated_at"]
        
        return result


class StreamConfig:
    """Configuration for data stream."""
    schema: str
    table: str
    interval_seconds: int = 5  # Publish every 5 seconds
    batch_size: int = 1000
    last_timestamp: datetime = None
    filters: Dict[str, Any] = {}
```

---

### **2. Calculation Engine - Stream Processor**

```python
# services/business_services/calculation_engine_service/app/stream_processor.py

class StreamProcessor:
    """Processes data streams and calculates KPIs in real-time."""
    
    def __init__(
        self,
        messaging_client: MessagingClient,
        metadata_client: MetadataClient
    ):
        self.messaging_client = messaging_client
        self.metadata_client = metadata_client
        self.active_processors = {}
        self.kpi_cache = {}
    
    async def start_processing(self, domain: str, kpi_codes: List[str]):
        """
        Start processing data stream for KPIs.
        
        Args:
            domain: Domain to subscribe to (e.g., supply_chain, finance)
            kpi_codes: List of KPI codes to calculate
        """
        channel = f"data.stream.{domain}"
        
        # Subscribe to data stream
        subscription_id = await self.messaging_client.create_subscription(
            channel_pattern=channel,
            callback_url=None,  # Use direct callback
            auto_ack=True
        )
        
        # Register message handler
        await self.messaging_client.subscribe(
            channel=channel,
            handler=lambda msg: self._process_stream_data(msg, kpi_codes)
        )
        
        self.active_processors[domain] = subscription_id
        logger.info(f"Started stream processing for {domain}, KPIs: {kpi_codes}")
    
    async def _process_stream_data(
        self,
        message: Dict[str, Any],
        kpi_codes: List[str]
    ):
        """Process incoming stream data and calculate KPIs."""
        try:
            data = message["data"]
            timestamp = message["timestamp"]
            
            logger.debug(f"Processing {len(data)} records from stream")
            
            # Calculate each KPI
            for kpi_code in kpi_codes:
                try:
                    result = await self._calculate_streaming_kpi(
                        kpi_code=kpi_code,
                        data=data,
                        timestamp=timestamp
                    )
                    
                    # Publish result
                    await self._publish_result(kpi_code, result)
                    
                except Exception as e:
                    logger.error(f"Error calculating {kpi_code}: {e}")
            
        except Exception as e:
            logger.error(f"Error processing stream data: {e}")
    
    async def _calculate_streaming_kpi(
        self,
        kpi_code: str,
        data: List[Dict[str, Any]],
        timestamp: str
    ) -> Dict[str, Any]:
        """Calculate KPI from streaming data."""
        # Get KPI definition (cached)
        if kpi_code not in self.kpi_cache:
            self.kpi_cache[kpi_code] = await self.metadata_client.get_kpi(kpi_code)
        
        kpi_def = self.kpi_cache[kpi_code]
        
        # Get appropriate handler
        handler = self._get_handler(kpi_def)
        
        # Calculate using streaming data
        result = await handler.calculate_streaming(
            kpi_code=kpi_code,
            data=data,
            timestamp=timestamp
        )
        
        return result
    
    async def _publish_result(self, kpi_code: str, result: Dict[str, Any]):
        """Publish calculation result to messaging service."""
        # Publish to KPI-specific channel
        await self.messaging_client.publish_event(
            event_type="analytics.result",
            event_data={
                "kpi_code": kpi_code,
                "value": result["value"],
                "unit": result["unit"],
                "timestamp": result["timestamp"],
                "metadata": result.get("metadata", {})
            }
        )
        
        # Also publish to result channel for subscribers
        result_channel = f"analytics.results.{kpi_code}"
        await self.messaging_client.publish_message(
            channel=result_channel,
            payload=result
        )
```

---

### **3. API Gateway - WebSocket Bridge**

```python
# services/frontend_services/api_gateway/app/websocket_handler.py

@app.websocket("/ws/analytics/{kpi_code}")
async def websocket_analytics(websocket: WebSocket, kpi_code: str):
    """
    WebSocket endpoint for real-time analytics streaming.
    
    Frontend connects and receives continuous KPI updates.
    """
    await websocket.accept()
    
    try:
        # Subscribe to KPI result channel
        result_channel = f"analytics.results.{kpi_code}"
        message_queue = asyncio.Queue()
        
        async def message_handler(channel: str, message: Any):
            await message_queue.put(message)
        
        # Subscribe to messaging service
        await pubsub_service.subscribe(result_channel, message_handler)
        
        # Send initial connection message
        await websocket.send_json({
            "type": "connected",
            "kpi_code": kpi_code,
            "channel": result_channel,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        # Stream results to frontend
        while True:
            # Get message from queue
            message = await message_queue.get()
            
            # Send to frontend
            await websocket.send_json({
                "type": "kpi_update",
                "kpi_code": kpi_code,
                "data": message,
                "timestamp": datetime.utcnow().isoformat()
            })
            
    except WebSocketDisconnect:
        logger.info(f"WebSocket disconnected for {kpi_code}")
        await pubsub_service.unsubscribe(result_channel, message_handler)
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        await websocket.close()
```

---

### **4. Frontend - Real-Time Dashboard**

```typescript
// services/frontend_services/demo_config_ui/src/hooks/useStreamingKPI.ts

export function useStreamingKPI(kpiCode: string) {
  const [value, setValue] = useState<number | null>(null);
  const [timestamp, setTimestamp] = useState<string | null>(null);
  const [isConnected, setIsConnected] = useState(false);
  const wsRef = useRef<WebSocket | null>(null);

  useEffect(() => {
    // Connect to WebSocket
    const ws = new WebSocket(
      `ws://localhost:8090/ws/analytics/${kpiCode}`
    );

    ws.onopen = () => {
      console.log(`Connected to streaming KPI: ${kpiCode}`);
      setIsConnected(true);
    };

    ws.onmessage = (event) => {
      const message = JSON.parse(event.data);
      
      if (message.type === 'kpi_update') {
        setValue(message.data.value);
        setTimestamp(message.data.timestamp);
      }
    };

    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
      setIsConnected(false);
    };

    ws.onclose = () => {
      console.log('WebSocket closed');
      setIsConnected(false);
    };

    wsRef.current = ws;

    // Cleanup
    return () => {
      ws.close();
    };
  }, [kpiCode]);

  return { value, timestamp, isConnected };
}

// Usage in component
function RealTimeDashboard() {
  const pof = useStreamingKPI('PERFECT_ORDER_FULFILLMENT');
  const otd = useStreamingKPI('ON_TIME_DELIVERY');
  const fillRate = useStreamingKPI('FILL_RATE');

  return (
    <div>
      <KPICard
        title="Perfect Order Fulfillment"
        value={pof.value}
        timestamp={pof.timestamp}
        isLive={pof.isConnected}
      />
      <KPICard
        title="On-Time Delivery"
        value={otd.value}
        timestamp={otd.timestamp}
        isLive={otd.isConnected}
      />
      <KPICard
        title="Fill Rate"
        value={fillRate.value}
        timestamp={fillRate.timestamp}
        isLive={fillRate.isConnected}
      />
    </div>
  );
}
```

---

## 📊 Architecture Summary

### **Streaming Analytics (80%) - PRIMARY**

```
Data Sources → Database Service → Messaging Service → Calculation Engine
                                                            ↓
                                                    Messaging Service
                                                            ↓
                                        API Gateway (WebSocket) → Frontend
```

**Characteristics:**
- Continuous data flow
- Real-time updates (seconds)
- Multiple subscribers
- Event-driven
- Scalable

---

### **One-Time Queries (20%) - SECONDARY**

```
Frontend → API Gateway → Calculation Engine → Database Service
                              ↓
                         Direct HTTP
                              ↓
                          Frontend
```

**Characteristics:**
- Request-response
- Fast (1-2 seconds)
- Ad-hoc queries
- Historical analysis
- Simple

---

## 🎯 Implementation Priority

### **Phase 1: Streaming Infrastructure (HIGH PRIORITY)**
1. ✅ Implement Database Service stream publisher
2. ✅ Implement Calculation Engine stream processor
3. ✅ Implement API Gateway WebSocket bridge
4. ✅ Implement Frontend streaming hooks
5. ✅ Test with real-time dashboard

### **Phase 2: One-Time Query Support (MEDIUM PRIORITY)**
1. ✅ Implement HTTP query endpoints
2. ✅ Implement synchronous calculation path
3. ✅ Test with ad-hoc queries

### **Phase 3: Optimization (LOW PRIORITY)**
1. Add caching for streaming results
2. Add backpressure handling
3. Add stream replay capability
4. Add historical data queries

---

## 💡 Key Insights

**Your Architecture is CORRECT for your use case!**

Since **80% of your analytics are streaming**, the pub/sub pattern should be your **PRIMARY** architecture, with HTTP queries as a **SECONDARY** fallback for one-time needs.

**This is a streaming-first analytics platform!** 🚀

The dual-mode approach gives you:
- ✅ Real-time streaming for continuous monitoring (80%)
- ✅ Fast queries for ad-hoc analysis (20%)
- ✅ Best of both worlds!
