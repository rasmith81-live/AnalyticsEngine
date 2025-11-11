# Real-Time Dashboard Architecture

**Date**: November 11, 2025  
**Use Case**: Interactive dashboards with configurable refresh periods (minute, hour, daily)

---

## 🎯 User Scenario

```
User opens dashboard at 8:00 AM
  ↓
Selects KPIs to monitor
  ↓
Sets refresh period (e.g., "every minute")
  ↓
Dashboard stays open all day
  ↓
KPIs update automatically based on period
  ↓
User switches between visualizations
  ↓
Each visualization subscribes to its own data stream
  ↓
User leaves at 5:00 PM (9 hours of continuous updates)
```

---

## 🏗️ Hybrid Architecture: Best of Both Worlds

### **Pattern: Initial HTTP Load + Continuous WebSocket Updates**

```
┌─────────────────────────────────────────────────────────────┐
│ Step 1: User Opens Dashboard                                │
│ Frontend → API Gateway (HTTP GET /kpi/{code})              │
│ Returns: Current value immediately (1-2 seconds)            │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 2: Subscribe to Updates                                │
│ Frontend → API Gateway (WebSocket /ws/kpi/{code}?period=X) │
│ Establishes persistent connection                           │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Step 3: Continuous Updates                                  │
│ Database Service → Messaging → API Gateway → Frontend      │
│ Updates pushed every minute/hour/day                        │
└─────────────────────────────────────────────────────────────┘
```

**Benefits:**
- ✅ Fast initial load (HTTP)
- ✅ Continuous updates (WebSocket)
- ✅ User-configurable refresh period
- ✅ Efficient (only publish when subscribers exist)
- ✅ Scalable (multiple users, multiple KPIs)

---

## 📊 TimescaleDB Continuous Aggregates

**Perfect for period-based updates!**

```sql
-- Minute-level aggregates (auto-refreshed every minute)
CREATE MATERIALIZED VIEW kpi_values_minute
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('1 minute', timestamp) AS bucket,
    kpi_code,
    AVG(value) as avg_value,
    COUNT(*) as data_points
FROM kpi_raw_data
GROUP BY bucket, kpi_code;

-- Hourly aggregates
CREATE MATERIALIZED VIEW kpi_values_hour
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('1 hour', timestamp) AS bucket,
    kpi_code,
    AVG(value) as avg_value
FROM kpi_raw_data
GROUP BY bucket, kpi_code;

-- Daily aggregates
CREATE MATERIALIZED VIEW kpi_values_day
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('1 day', timestamp) AS bucket,
    kpi_code,
    AVG(value) as avg_value
FROM kpi_raw_data
GROUP BY bucket, kpi_code;
```

---

## 🔧 Implementation Summary

### **Database Service:**
- Monitors TimescaleDB continuous aggregates
- Publishes to messaging service when new period data available
- Only publishes if there are active subscribers (efficient!)

### **API Gateway:**
- HTTP endpoint for initial load (fast)
- WebSocket endpoint for continuous updates
- Manages subscriber count per KPI/period

### **Frontend:**
- Fetches initial value via HTTP
- Connects WebSocket for updates
- User selects refresh period (minute/hour/day)
- Automatically reconnects on disconnect

---

## 🎯 User Experience

**Scenario: User monitors Perfect Order Fulfillment all day**

```
8:00 AM - Opens dashboard
  ↓ HTTP GET (instant)
  Shows: 94.5%
  ↓ WebSocket connect (period=minute)
  
8:01 AM - Update received
  Shows: 94.6% ↑ 0.1%
  
8:02 AM - Update received
  Shows: 94.7% ↑ 0.1%
  
... continues all day ...

5:00 PM - Closes browser
  ↓ WebSocket disconnect
  Database Service stops publishing (no subscribers)
```

**User switches to hourly view:**
```
  ↓ Disconnect from minute channel
  ↓ Connect to hour channel
  Updates now come every hour instead of every minute
```

---

## 💡 Key Advantages

1. **Fast Initial Load**: HTTP gives instant feedback
2. **Efficient Updates**: Only publish when subscribers exist
3. **Flexible Periods**: User chooses minute/hour/day
4. **Scalable**: TimescaleDB continuous aggregates handle computation
5. **Always Current**: Dashboard updates automatically
6. **Resource Efficient**: Stops publishing when no one watching

---

## 📝 Summary

**Your use case requires BOTH patterns:**

- **HTTP REST**: Initial page load (fast, 1-2 seconds)
- **WebSocket + Pub/Sub**: Continuous updates (configurable period)

**This is the perfect hybrid architecture for real-time dashboards!** 🚀
