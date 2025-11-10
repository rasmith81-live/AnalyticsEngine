# Product Architecture Plan

**Date**: November 10, 2025

## Three Applications

### 1. Demo/Config App (Multi-tenant SaaS)
- Metric selection tree (Industry → Value Chain → Use Case → KPI)
- UML diagram viewer (D3.js)
- Custom KPI creator with RBAC
- Required objects analyzer
- Data source configuration
- SOW generator

### 2. Client App (Single-tenant, compiled)
- D3.js dashboards
- Selected KPIs only
- License key validation
- Health telemetry
- Deployed on client Azure

### 3. Monitoring App (Multi-tenant SaaS)
- Health monitoring all clients
- Alert management
- Remote access
- License tracking
- Email notifications

## Key Recommendations

### ✅ Keep Metadata Service Centralized
- Single source of truth
- Clients fetch selected KPIs on startup
- Easy global updates

### ✅ Hybrid Deployment
- Demo/Config: Multi-tenant SaaS
- Client Apps: Single-tenant per client
- Monitoring: Multi-tenant SaaS

### ✅ Compilation Strategy
- PyInstaller for Python backend
- React production build
- Docker packaging for Azure

### ✅ License Management
- Registry key + API validation
- Expiration enforcement
- 3-month renewal reminders

### ✅ Health Telemetry
- Heartbeat every 60 seconds
- Performance metrics
- Error reporting

## New Services Needed

1. **demo_config_service** - Client configuration and SOW
2. **connector_service** - Data source connections
3. **ingestion_service** - Batch/real-time data loading
4. **mapping_service** - Drag-and-drop mapping UI
5. **client_app_service** - Compiled client application
6. **monitoring_service** - Centralized health monitoring
7. **license_service** - License validation and tracking

## Implementation Phases

**Phase 1** (Weeks 1-4): Core services ✅
**Phase 2** (Weeks 5-8): Demo/Config App
**Phase 3** (Weeks 9-12): Integration Services
**Phase 4** (Weeks 13-16): Client App
**Phase 5** (Weeks 17-20): Monitoring App
**Phase 6** (Weeks 21-24): Deployment Automation

## Your Architecture is Perfect!

Current microservices architecture aligns perfectly with this model:
- ✅ Metadata Service - Single source of truth
- ✅ Calculation Engine - Real-time KPI processing
- ✅ Backend Services - Infrastructure ready
- ✅ Microservices pattern - Scalable and maintainable

**Next**: Build demo/config service and UI
