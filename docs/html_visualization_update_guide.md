# HTML Visualization Update Guide

This document outlines the changes needed to update the HTML visualization to match the updated PlantUML diagram, specifically focusing on the messaging-based communication pattern for the observability service.

## 1. Telemetry and Metrics Flow Updates

### 4.1 Metrics Collection - Detailed
- Update the flow to show ServiceA sending metrics to Messaging Service via POST /messaging/publish
- Ensure Observability Service subscribes to telemetry.metrics via Redis
- Update the flow to show Observability Service processing metrics and publishing to database channel via Messaging Service
- Add a note indicating "Process metrics and store via messaging"
- Change Redis pub/sub channel from "telemetry.traces" to "telemetry.metrics"

### 4.2 Trace Events Collection - Detailed (New Section)
- Add a new group section for trace events collection
- Show ServiceA sending traces to Messaging Service via POST /messaging/publish
- Show Messaging Service publishing to telemetry.traces channel in Redis
- Show Observability Service subscribing to telemetry.traces channel
- Add a note indicating "Process traces and store via messaging"
- Show Observability Service publishing trace.store events to database channel via Messaging Service

### 4.3 Dependency Events Collection - Detailed (New Section)
- Add a new group section for dependency events collection
- Show ServiceA sending dependency data to Messaging Service via POST /messaging/publish
- Show Messaging Service publishing to telemetry.dependencies channel in Redis
- Show Observability Service subscribing to telemetry.dependencies channel
- Add a note indicating "Process dependency data and store via messaging"
- Show Observability Service publishing dependency.store events to database channel via Messaging Service

## 2. Health Check Flow Updates

### 5.4 Observability Health Check - Detailed (New Section)
- Add a new group section for observability health checks
- Show Gateway publishing health.check events for observability_service to Redis
- Show Observability Service subscribing to health.check channel
- Show Observability Service performing health_check()
- Update to show Observability Service using Messaging Service for Redis health check:
  - POST /messaging/publish with health.check message
  - Messaging Service performs PING to Redis
  - Messaging Service returns health status to Observability Service
- Update to show Observability Service using Messaging Service for database health check:
  - POST /messaging/publish to database channel with health.check event
  - Messaging Service publishes to database channel
- Show Observability Service publishing health.status to Redis
- Show Gateway subscribing to health.status channel

## 3. General Architecture Updates

- Update the "Architectural Patterns" section to emphasize that all inter-service communication, including observability telemetry and health checks, goes through the messaging service
- Update the "Infrastructure Components" section to clarify that Redis is not accessed directly by the observability service
- Add a note about the decoupled architecture where observability service only interacts with other services through the messaging service

## HTML Structure Pattern

When implementing these changes, follow the existing HTML structure pattern:

```html
<div class="group">
    <div class="group-title">Section Title</div>
    
    <div class="message">
        <div>Source Service</div>
        <div class="arrow">
            <span class="message-label">Message Content</span>
        </div>
        <div>Target Service</div>
    </div>
    
    <div class="note">Additional information or endpoint details</div>
    
    <!-- Additional messages and notes -->
</div>
```

## Implementation Priority

1. Add the Observability Health Check section (5.4)
2. Update the Metrics Collection section (4.1)
3. Add the Trace Events Collection section (4.2)
4. Add the Dependency Events Collection section (4.3)
5. Update the general architecture descriptions
