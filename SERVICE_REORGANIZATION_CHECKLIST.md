# Service Reorganization Checklist

**Date**: November 10, 2025  
**Changes**: Rename and move analytics services

---

## Changes Made

### 1. Renamed: analytics_models → analytics_metadata_service
```
FROM: services/business_services/analytics_models/
TO:   services/business_services/analytics_metadata_service/
```

### 2. Moved: calculation_engine → calculation_engine_service
```
FROM: services/business_services/calculation_engine/
TO:   services/backend_services/calculation_engine_service/
```

---

## Post-Move Updates Required

### ✅ Step 1: Run Reorganization Script

```powershell
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine
.\scripts\reorganize_services.ps1
```

### ✅ Step 2: Update docker-compose.yml

Add/update these services:

```yaml
# Add analytics_metadata_service
analytics_metadata_service:
  build:
    context: .
    dockerfile: Dockerfile
    args:
      SERVICE_DIR: services/business_services/analytics_metadata_service
  ports:
    - "8020:8000"
  environment:
    - SERVICE_NAME=analytics_metadata_service
    - DATABASE_SERVICE_URL=http://database_service:8000
    - MESSAGING_SERVICE_URL=http://messaging_service:8000
    - OBSERVABILITY_SERVICE_URL=http://observability_service:8000
    - ENABLE_DISTRIBUTED_TRACING=true
    - OTLP_ENDPOINT=https://observability_service:4317
    - PYTHONPATH=.
  depends_on:
    database_service:
      condition: service_healthy
    messaging_service:
      condition: service_healthy
  volumes:
    - .:/app
    - ./certs:/certs
  healthcheck:
    test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
    interval: 30s
    timeout: 10s
    retries: 3
    start_period: 40s

# Add calculation_engine_service
calculation_engine_service:
  build:
    context: .
    dockerfile: Dockerfile
    args:
      SERVICE_DIR: services/backend_services/calculation_engine_service
  ports:
    - "8021:8000"
  environment:
    - SERVICE_NAME=calculation_engine_service
    - DATABASE_SERVICE_URL=http://database_service:8000
    - MESSAGING_SERVICE_URL=http://messaging_service:8000
    - METADATA_SERVICE_URL=http://analytics_metadata_service:8000
    - OBSERVABILITY_SERVICE_URL=http://observability_service:8000
    - ENABLE_DISTRIBUTED_TRACING=true
    - OTLP_ENDPOINT=https://observability_service:4317
    - CACHE_ENABLED=true
    - CACHE_TTL=3600
    - PYTHONPATH=.
  depends_on:
    database_service:
      condition: service_healthy
    messaging_service:
      condition: service_healthy
    analytics_metadata_service:
      condition: service_healthy
  volumes:
    - .:/app
    - ./certs:/certs
  healthcheck:
    test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
    interval: 30s
    timeout: 10s
    retries: 3
    start_period: 40s
```

### ✅ Step 3: Update API Gateway Configuration

Update `services/frontend_services/api_gateway/` to include new services:

```python
# In api_gateway config or environment
ANALYTICS_METADATA_SERVICE_URL=http://analytics_metadata_service:8000
CALCULATION_ENGINE_SERVICE_URL=http://calculation_engine_service:8000
```

### ✅ Step 4: Update Import Statements

Search for any imports referencing old paths:

```powershell
# Search for old references
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine
Get-ChildItem -Recurse -Include *.py | Select-String "analytics_models" | Select-Object Path, LineNumber, Line
Get-ChildItem -Recurse -Include *.py | Select-String "calculation_engine" | Select-Object Path, LineNumber, Line
```

**Common patterns to update**:
```python
# OLD
from services.business_services.analytics_models import ...
from services.business_services.calculation_engine import ...

# NEW
from services.business_services.analytics_metadata_service import ...
from services.backend_services.calculation_engine_service import ...
```

### ✅ Step 5: Update README.md

Update main README to reflect new service structure:

```markdown
## Architecture

### Backend Services (Infrastructure)
1. database_service (Port 8000)
2. messaging_service (Port 8001)
3. archival_service (Port 8004)
4. observability_service (Port 8080)
5. **calculation_engine_service (Port 8021)** ← NEW

### Business Services (Domain Logic)
1. **analytics_metadata_service (Port 8020)** ← RENAMED
2. systems_monitor (Port 8010)
3. controller_service (Port 8011)
4. entity_resolution_service (Port 8012)
5. ... (other business services)
```

### ✅ Step 6: Update Documentation References

Files to update:
- `README.md` - Main project README
- `ANALYTICS_MICROSERVICES_ARCHITECTURE.md`
- `ANALYTICS_MODELS_MIGRATION_PLAN.md`
- `CALCULATION_ENGINE_ARCHITECTURE.md`
- Any other docs referencing old paths

### ✅ Step 7: Update .env Files

Check and update any .env files with service URLs:

```bash
# In various .env files
ANALYTICS_METADATA_SERVICE_URL=http://analytics_metadata_service:8000
CALCULATION_ENGINE_SERVICE_URL=http://calculation_engine_service:8000
```

### ✅ Step 8: Test Services

```powershell
# Build and start services
docker-compose build analytics_metadata_service
docker-compose build calculation_engine_service

# Start services
docker-compose up -d analytics_metadata_service
docker-compose up -d calculation_engine_service

# Check health
curl http://localhost:8020/health  # Metadata service
curl http://localhost:8021/health  # Calculation engine

# Check logs
docker-compose logs analytics_metadata_service
docker-compose logs calculation_engine_service
```

---

## Verification Checklist

- [ ] Run reorganization script successfully
- [ ] Update docker-compose.yml with new service definitions
- [ ] Update API Gateway configuration
- [ ] Search and update any import statements
- [ ] Update README.md
- [ ] Update documentation files
- [ ] Update .env files
- [ ] Build Docker images successfully
- [ ] Start services successfully
- [ ] Health checks pass
- [ ] API endpoints respond correctly
- [ ] No errors in logs

---

## New Service Structure

```
services/
├── backend_services/
│   ├── database_service/
│   ├── messaging_service/
│   ├── archival_service/
│   ├── observability_service/
│   └── calculation_engine_service/     ← MOVED HERE
│
├── business_services/
│   ├── analytics_metadata_service/     ← RENAMED
│   ├── systems_monitor/
│   ├── controller_service/
│   ├── entity_resolution_service/
│   ├── data_governance_service/
│   ├── machine_learning_service/
│   └── ... (other business services)
│
├── frontend_services/
│   └── api_gateway/
│
└── support_services/
    └── ... (support services)
```

---

## Rationale for Changes

### analytics_models → analytics_metadata_service
- **Why**: More descriptive name
- **What it does**: Serves metadata definitions via REST API
- **Location**: business_services (domain-specific metadata)

### calculation_engine → calculation_engine_service
- **Why**: Consistent naming with other services
- **Location**: backend_services (infrastructure for calculations)
- **What it does**: Generic calculation orchestration (not domain-specific)

### Why calculation_engine_service is Backend
- It's infrastructure/framework code (like database_service, messaging_service)
- Provides generic calculation capabilities
- Not tied to specific business domain
- Reusable across all value chains

---

## Quick Reference

### Old Paths
```
services/business_services/analytics_models/
services/business_services/calculation_engine/
```

### New Paths
```
services/business_services/analytics_metadata_service/
services/backend_services/calculation_engine_service/
```

### Ports
- analytics_metadata_service: 8020
- calculation_engine_service: 8021

### Service URLs
- http://analytics_metadata_service:8000
- http://calculation_engine_service:8000

---

## Rollback (If Needed)

If something goes wrong:

```powershell
# Rename back
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\services\business_services
Rename-Item analytics_metadata_service analytics_models

# Move back
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\services\backend_services
Move-Item calculation_engine_service ..\business_services\calculation_engine
```

---

## Notes

- Git will track these as renames/moves (preserves history)
- Docker volumes are mounted, so paths in containers update automatically
- No data loss - just organizational changes
- Services remain functionally identical
