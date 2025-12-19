# Quick Start Guide - Analytics Engine

**Get up and running in 5 minutes!**

---

## Prerequisites

- Docker Desktop installed and running
- Node.js 18+ and npm installed
- PowerShell (Windows)

---

## Step 1: Start Backend Services

```powershell
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine

# Build and start core services
docker-compose build business_metadata calculation_engine_service demo_config_service api_gateway

docker-compose up -d business_metadata calculation_engine_service demo_config_service api_gateway
```

**Wait 30-60 seconds for services to start**

---

## Step 2: Verify Backend Services

```powershell
# Check health of all services
curl http://localhost:8020/health  # Metadata Service
curl http://localhost:8021/health  # Calculation Engine
curl http://localhost:8022/health  # Demo/Config Service
curl http://localhost:8090/health  # API Gateway
```

**Expected**: All should return `{"status": "healthy"}`

---

## Step 3: View API Documentation

Open in browser:
- **API Gateway (Unified)**: http://localhost:8090/docs
- **Metadata Service**: http://localhost:8020/docs
- **Calculation Engine**: http://localhost:8021/docs
- **Demo/Config Service**: http://localhost:8022/docs

---

## Step 4: Setup Frontend

```powershell
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\services\frontend_services\demo_config_ui

# Install dependencies (first time only)
npm install

# Create .env file
@"
VITE_API_BASE_URL=http://localhost:8090
VITE_ENABLE_DEMO=true
VITE_ENABLE_CUSTOM_KPIS=true
"@ | Out-File -FilePath .env -Encoding utf8
```

---

## Step 5: Start Frontend

```powershell
# Still in demo_config_ui directory
npm run dev
```

**Frontend will open at**: http://localhost:3000

---

## Quick Test

### Test via API Gateway

```powershell
# Get KPI statistics
curl http://localhost:8090/api/v1/metadata/stats

# Get all KPIs
curl http://localhost:8090/api/v1/metadata/kpis
```

---

## Service Ports

| Service | Port | URL |
|---------|------|-----|
| Business Metadata | 8020 | http://localhost:8020 |
| Calculation Engine | 8021 | http://localhost:8021 |
| Demo/Config Service | 8022 | http://localhost:8022 |
| Frontend UI | 3000 | http://localhost:3000 |
| API Gateway | 8090 | http://localhost:8090 |

---

## Troubleshooting

### Services won't start

```powershell
# Check Docker logs
docker-compose logs business_metadata
docker-compose logs calculation_engine_service
docker-compose logs demo_config_service
docker-compose logs api_gateway

# Restart services
docker-compose restart business_metadata
```

### Frontend won't start

```powershell
# Clear npm cache and reinstall
cd services/frontend_services/demo_config_ui
rm -r node_modules
rm package-lock.json
npm install
npm run dev
```

### Port conflicts

If ports are already in use, edit `docker-compose.yml` to change port mappings:
```yaml
ports:
  - "8020:8000"  # Change 8020 to another port
```

---

## Stop Everything

```powershell
# Stop frontend (Ctrl+C in terminal)

# Stop backend services
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine
docker-compose down
```

---

## Next Steps

1. **Explore API Documentation**
   - Visit http://localhost:8020/docs
   - Try out API endpoints

2. **Build UI Components**
   - Layout component
   - MetricTree component
   - UML diagram viewer

3. **Test Integration**
   - Frontend calling backend APIs
   - Create client configurations
   - Generate service proposals

---

## Common Commands

```powershell
# View logs
docker-compose logs -f analytics_metadata_service

# Restart a service
docker-compose restart demo_config_service

# Rebuild a service
docker-compose build --no-cache demo_config_service

# Check running containers
docker-compose ps

# Stop all services
docker-compose down

# Start all services
docker-compose up -d
```

---

## Success Checklist

- [ ] Docker services running
- [ ] All health checks passing
- [ ] API docs accessible
- [ ] Frontend npm install successful
- [ ] Frontend dev server running
- [ ] Can access http://localhost:3000

---

## Help

If you encounter issues:
1. Check Docker Desktop is running
2. Check logs: `docker-compose logs [service_name]`
3. Verify ports are not in use
4. Ensure .env files are created
5. Try rebuilding: `docker-compose build --no-cache`

---

**You're ready to go!** 🚀

Start building UI components and connecting everything together!
