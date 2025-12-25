# Getting Started with Analytics Engine

**Complete setup and onboarding guide**

---

## Overview

Analytics Engine is a real-time, microservices-based analytics platform that provides on-demand KPI calculations across multiple value chains (Supply Chain, CRM, Sales, Financial). This guide will help you get the platform running on your local machine.

---

## Prerequisites

### Required Software
- **Docker Desktop** 4.0+ (with Docker Compose)
- **Node.js** 18+ and npm
- **Python** 3.11+ (for local development)
- **PowerShell** (Windows) or Bash (Linux/Mac)
- **Git** for version control

### System Requirements
- **RAM**: 8GB minimum, 16GB recommended
- **Disk Space**: 10GB free space
- **CPU**: 4 cores minimum
- **OS**: Windows 10/11, macOS 10.15+, or Linux

### Optional Tools
- **VS Code** or **PyCharm** for development
- **Postman** or **Insomnia** for API testing
- **pgAdmin** or **DBeaver** for database management

---

## Quick Start (5 Minutes)

**Want to get running immediately?** Follow these minimal steps:

1. **Start services**: `docker-compose up -d business_metadata calculation_engine_service api_gateway`
2. **Verify health**: `curl http://localhost:8090/health`
3. **View API docs**: http://localhost:8090/docs

For complete setup with database, migrations, and all services, continue with the detailed installation steps below.

---

## Installation Steps

### 1. Clone the Repository

```powershell
cd C:\Users\Arthu\CascadeProjects
git clone https://github.com/your-org/AnalyticsEngine.git
cd AnalyticsEngine
```

### 2. Environment Configuration

Create environment files:

```powershell
# Copy example environment file
cp .env.example .env

# Edit .env with your settings
notepad .env
```

**Key environment variables**:
```bash
# Database
DATABASE_URL=postgresql+asyncpg://multiservice_user:multiservice_password@timescaledb:5432/multiservice_db
POSTGRES_USER=multiservice_user
POSTGRES_PASSWORD=multiservice_password
POSTGRES_DB=multiservice_db

# Redis
REDIS_URL=redis://redis:6379

# Services
SERVICE_NAME=analytics_engine
ENVIRONMENT=development
LOG_LEVEL=INFO

# Optional: OpenAI for conversation service
OPENAI_API_KEY=your_key_here
```

### 3. Start Core Infrastructure

Start TimescaleDB and Redis first:

```powershell
docker-compose up -d timescaledb redis
```

**Wait for health checks** (30-60 seconds):
```powershell
docker-compose ps
```

Expected output:
```
NAME                          STATUS
analyticsengine-timescaledb-1 Up (healthy)
analyticsengine-redis-1       Up (healthy)
```

### 4. Run Database Migrations

```powershell
# Set environment variable
$env:DATABASE_URL="postgresql+asyncpg://multiservice_user:multiservice_password@localhost:5432/multiservice_db"

# Run migrations
python -m alembic upgrade head
```

**Verify tables created**:
```powershell
docker-compose exec timescaledb psql -U multiservice_user -d multiservice_db -c "\dt"
```

### 5. Start Backend Services

```powershell
# Start all backend services
docker-compose up -d database_service messaging_service business_metadata calculation_engine_service demo_config_service connector_service

# Check service health
docker-compose ps
```

### 6. Verify Backend Services

Test each service health endpoint:

```powershell
# Database Service
curl http://localhost:8000/health

# Messaging Service
curl http://localhost:8001/health

# Business Metadata
curl http://localhost:8020/health

# Calculation Engine
curl http://localhost:8021/health

# Demo Config Service
curl http://localhost:8022/health

# Connector Service
curl http://localhost:8023/health
```

All should return: `{"status": "healthy"}`

### 7. Start API Gateway

```powershell
docker-compose up -d api_gateway

# Verify gateway
curl http://localhost:8090/health
```

### 8. Setup Frontend

```powershell
cd services/frontend_services/demo_config_ui

# Install dependencies
npm install

# Create frontend .env
@"
VITE_API_BASE_URL=http://localhost:8090
VITE_ENABLE_DEMO=true
VITE_ENABLE_CUSTOM_KPIS=true
"@ | Out-File -FilePath .env -Encoding utf8

# Start development server
npm run dev
```

Frontend will be available at: **http://localhost:3000**

---

## Verification

### 1. Check All Services

```powershell
docker-compose ps
```

Expected services running:
- ✅ timescaledb (port 5432)
- ✅ redis (ports 6379, 8001)
- ✅ database_service (port 8000)
- ✅ messaging_service (port 8001)
- ✅ business_metadata (port 8020)
- ✅ calculation_engine_service (port 8021)
- ✅ demo_config_service (port 8022)
- ✅ connector_service (port 8023)
- ✅ api_gateway (port 8090)

### 2. Test API Endpoints

**Get KPI Statistics**:
```powershell
curl http://localhost:8090/api/v1/metadata/stats
```

**Get All KPIs**:
```powershell
curl http://localhost:8090/api/v1/metadata/kpis | ConvertFrom-Json | Select-Object -First 5
```

**Get Value Chains**:
```powershell
curl http://localhost:8090/api/v1/metadata/value-chains
```

### 3. Access API Documentation

Open in browser:
- **API Gateway (Unified)**: http://localhost:8090/docs
- **Business Metadata**: http://localhost:8020/docs
- **Calculation Engine**: http://localhost:8021/docs
- **Demo Config Service**: http://localhost:8022/docs
- **Connector Service**: http://localhost:8023/docs
- **Database Service**: http://localhost:8000/docs
- **Messaging Service**: http://localhost:8001/docs

### 4. Test Frontend

1. Open http://localhost:3000
2. Verify UI loads without errors
3. Check browser console for errors
4. Test navigation between pages

---

## Common Issues and Solutions

### Issue: Docker services won't start

**Solution**:
```powershell
# Check Docker Desktop is running
docker version

# Check for port conflicts
netstat -ano | findstr "8000 8001 8020 8021 8022 8023 8090 3000 5432 6379"

# Restart Docker Desktop
# Then try again
docker-compose up -d
```

### Issue: Database connection failed

**Solution**:
```powershell
# Check TimescaleDB is healthy
docker-compose ps timescaledb

# Check logs
docker-compose logs timescaledb

# Verify credentials in .env match docker-compose.yml
```

### Issue: Redis connection failed

**Solution**:
```powershell
# Check Redis is healthy
docker-compose ps redis

# Test Redis connection
docker-compose exec redis redis-cli ping
# Should return: PONG

# Check logs
docker-compose logs redis
```

### Issue: Frontend won't start

**Solution**:
```powershell
cd services/frontend_services/demo_config_ui

# Clear cache and reinstall
Remove-Item -Recurse -Force node_modules
Remove-Item package-lock.json
npm install

# Check .env file exists
cat .env

# Start dev server
npm run dev
```

### Issue: Port already in use

**Solution**:
```powershell
# Find process using port (e.g., 8000)
netstat -ano | findstr ":8000"

# Kill process (replace PID with actual process ID)
taskkill /PID <PID> /F

# Or change port in docker-compose.yml
```

### Issue: Migration failed

**Solution**:
```powershell
# Check database is accessible
docker-compose exec timescaledb psql -U multiservice_user -d multiservice_db -c "SELECT version();"

# Check migration status
$env:DATABASE_URL="postgresql+asyncpg://multiservice_user:multiservice_password@localhost:5432/multiservice_db"
python -m alembic current

# Reset and retry
python -m alembic downgrade base
python -m alembic upgrade head
```

---

## Next Steps

### For Developers

1. **[Development Setup](../development/setup.md)** - Configure your IDE and tools
2. **[Architecture Overview](../architecture/README.md)** - Understand the system design
3. **[Coding Standards](../development/coding-standards.md)** - Follow best practices
4. **[Testing Guide](../development/testing.md)** - Write and run tests

### For DevOps

1. **[Deployment Guide](../operations/deployment.md)** - Deploy to production
2. **[Monitoring Guide](../operations/monitoring.md)** - Set up observability
3. **[Backup and Recovery](../operations/backup-recovery.md)** - Data protection

### For Business Users

1. **[Business Plan](../../BUSINESS_PLAN.md)** - Understand the business model
2. **[Features](../../features.md)** - Explore available features
3. **[API Gateway](../services/api_gateway.md)** - Learn about the API

---

## Useful Commands

### Docker Commands

```powershell
# View all running containers
docker-compose ps

# View logs for a service
docker-compose logs -f business_metadata

# Restart a service
docker-compose restart calculation_engine_service

# Stop all services
docker-compose down

# Start all services
docker-compose up -d

# Rebuild a service
docker-compose build --no-cache demo_config_service

# Remove all containers and volumes (CAUTION: deletes data)
docker-compose down -v
```

### Database Commands

```powershell
# Connect to database
docker-compose exec timescaledb psql -U multiservice_user -d multiservice_db

# List tables
docker-compose exec timescaledb psql -U multiservice_user -d multiservice_db -c "\dt"

# Run SQL query
docker-compose exec timescaledb psql -U multiservice_user -d multiservice_db -c "SELECT COUNT(*) FROM connector_profiles;"

# Backup database
docker-compose exec timescaledb pg_dump -U multiservice_user multiservice_db > backup.sql

# Restore database
cat backup.sql | docker-compose exec -T timescaledb psql -U multiservice_user -d multiservice_db
```

### Migration Commands

```powershell
# Check current migration
python -m alembic current

# View migration history
python -m alembic history

# Upgrade to latest
python -m alembic upgrade head

# Downgrade one revision
python -m alembic downgrade -1

# Create new migration
python -m alembic revision -m "description"
```

---

## Configuration Reference

### Service Ports

| Service | Port | Protocol | Purpose |
|---------|------|----------|---------|
| TimescaleDB | 5432 | TCP | PostgreSQL database |
| Redis | 6379 | TCP | Redis cache/messaging |
| RedisInsight | 8001 | HTTP | Redis web UI |
| Database Service | 8000 | HTTP | Database API |
| Messaging Service | 8001 | HTTP | Messaging API |
| Business Metadata | 8020 | HTTP | Metadata API |
| Calculation Engine | 8021 | HTTP | Calculation API |
| Demo Config Service | 8022 | HTTP | Config API |
| Connector Service | 8023 | HTTP | Connector API |
| Ingestion Service | 8024 | HTTP | Ingestion API |
| Metadata Ingestion | 8025 | HTTP | Bulk import API |
| Conversation Service | 8026 | HTTP | Chatbot API |
| API Gateway | 8090 | HTTP | Unified API |
| Frontend UI | 3000 | HTTP | React app |

### Docker Volumes

| Volume | Purpose | Data Stored |
|--------|---------|-------------|
| timescaledb_data | Database persistence | All database tables and data |
| redis_data | Redis persistence | Cache and message queues |
| azurite_data | Storage emulator | Blob/queue/table storage |
| prometheus_data | Metrics storage | Prometheus metrics |

---

## Success Checklist

- [ ] Docker Desktop installed and running
- [ ] Repository cloned
- [ ] Environment files created (.env)
- [ ] TimescaleDB running and healthy
- [ ] Redis running and healthy
- [ ] Database migrations completed
- [ ] All backend services running
- [ ] API Gateway running
- [ ] All health checks passing
- [ ] API documentation accessible
- [ ] Frontend dependencies installed
- [ ] Frontend dev server running
- [ ] Can access http://localhost:3000
- [ ] Can make API calls successfully

---

## Support

- **Documentation**: [docs/INDEX.md](../INDEX.md)
- **Troubleshooting**: [operations/troubleshooting.md](../operations/troubleshooting.md)
- **Issues**: [GitHub Issues](https://github.com/your-org/analytics-engine/issues)
- **Email**: support@your-company.com

---

**You're ready to start developing!** 🚀

**Next**: [Architecture Overview](../architecture/README.md) | [Development Guide](../development/README.md)

