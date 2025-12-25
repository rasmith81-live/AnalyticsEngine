# Operations Guide - Analytics Engine

**Deployment, monitoring, and operational procedures**

---

## Table of Contents

1. [Overview](#overview)
2. [Deployment](#deployment)
3. [Monitoring](#monitoring)
4. [Troubleshooting](#troubleshooting)
5. [Maintenance](#maintenance)
6. [Backup and Recovery](#backup-and-recovery)
7. [Performance Tuning](#performance-tuning)
8. [Security Operations](#security-operations)

---

## Overview

This guide covers operational procedures for deploying, monitoring, and maintaining the Analytics Engine platform in development, staging, and production environments.

### Operational Responsibilities

- **Deployment**: Docker Compose / Kubernetes orchestration
- **Monitoring**: Health checks, metrics, logging
- **Maintenance**: Updates, migrations, scaling
- **Backup**: Data protection and recovery
- **Security**: Access control, secrets management
- **Performance**: Optimization and tuning

---

## Deployment

### Docker Compose Deployment

#### **Development Environment**

**Start All Services**:
```powershell
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine

# Start infrastructure
docker-compose up -d timescaledb redis azurite

# Wait for health checks (30-60 seconds)
docker-compose ps

# Start backend services
docker-compose up -d database_service messaging_service

# Start business services
docker-compose up -d business_metadata calculation_engine_service demo_config_service connector_service

# Start API gateway
docker-compose up -d api_gateway
```

**Verify Deployment**:
```powershell
# Check all services
docker-compose ps

# Check health endpoints
curl http://localhost:8000/health  # Database Service
curl http://localhost:8020/health  # Business Metadata
curl http://localhost:8090/health  # API Gateway
```

#### **Production Environment**

**Pre-Deployment Checklist**:
- [ ] Environment variables configured
- [ ] SSL certificates in place
- [ ] Database backup completed
- [ ] Migration plan reviewed
- [ ] Rollback plan prepared
- [ ] Monitoring configured

**Deployment Steps**:
```bash
# 1. Backup current state
docker-compose exec timescaledb pg_dump -U multiservice_user multiservice_db > backup_pre_deploy.sql

# 2. Pull latest images
docker-compose pull

# 3. Run migrations
docker-compose run --rm database_service alembic upgrade head

# 4. Rolling update (one service at a time)
docker-compose up -d --no-deps --build database_service
docker-compose up -d --no-deps --build messaging_service
docker-compose up -d --no-deps --build business_metadata
# ... continue for each service

# 5. Verify health
docker-compose ps
curl http://localhost:8090/health
```

### Service Startup Order

**Correct Order**:
1. **Infrastructure**: timescaledb, redis, azurite
2. **Backend Services**: database_service, messaging_service
3. **Business Services**: business_metadata, calculation_engine_service, etc.
4. **Frontend Services**: api_gateway, demo_config_ui

**Why Order Matters**:
- Services depend on infrastructure being ready
- Business services need backend services
- API Gateway routes to business services

### Environment Configuration

**Environment Files**:
```
.env                    ← Main environment file
.env.development        ← Development overrides
.env.production         ← Production overrides
```

**Key Variables**:
```bash
# Database
DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/db
POSTGRES_USER=multiservice_user
POSTGRES_PASSWORD=<strong_password>
POSTGRES_DB=multiservice_db

# Redis
REDIS_URL=redis://redis:6379

# Services
ENVIRONMENT=production
LOG_LEVEL=INFO
SERVICE_NAME=analytics_engine

# Security
SECRET_KEY=<generate_random_key>
API_KEY=<generate_api_key>

# Optional
OPENAI_API_KEY=<your_key>
AZURE_STORAGE_CONNECTION_STRING=<connection_string>
```

### Health Checks

**Service Health Endpoints**:
```
http://localhost:8000/health  # Database Service
http://localhost:8001/health  # Messaging Service
http://localhost:8020/health  # Business Metadata
http://localhost:8021/health  # Calculation Engine
http://localhost:8022/health  # Demo Config Service
http://localhost:8023/health  # Connector Service
http://localhost:8090/health  # API Gateway
```

**Health Check Script**:
```powershell
# check_health.ps1
$services = @(
    @{Name="Database"; Port=8000},
    @{Name="Messaging"; Port=8001},
    @{Name="Metadata"; Port=8020},
    @{Name="Calculation"; Port=8021},
    @{Name="Gateway"; Port=8090}
)

foreach ($service in $services) {
    try {
        $response = Invoke-RestMethod -Uri "http://localhost:$($service.Port)/health" -TimeoutSec 5
        if ($response.status -eq "healthy") {
            Write-Host "✅ $($service.Name) is healthy" -ForegroundColor Green
        } else {
            Write-Host "⚠️  $($service.Name) is unhealthy" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "❌ $($service.Name) is down" -ForegroundColor Red
    }
}
```

---

## Monitoring

### Metrics Collection

**Prometheus Metrics**:
```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'analytics_engine'
    static_configs:
      - targets:
        - 'database_service:8000'
        - 'messaging_service:8001'
        - 'business_metadata:8020'
        - 'calculation_engine:8021'
```

**Key Metrics**:
- Request rate (requests/second)
- Response time (p50, p95, p99)
- Error rate (errors/total requests)
- Database connections (active/idle)
- Redis operations (get/set/pub/sub)
- Memory usage
- CPU usage

### Logging

**Log Levels**:
```
DEBUG   - Detailed diagnostic information
INFO    - General informational messages
WARNING - Warning messages
ERROR   - Error messages
CRITICAL - Critical errors
```

**View Logs**:
```powershell
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f business_metadata

# Last 100 lines
docker-compose logs --tail=100 calculation_engine_service

# Since timestamp
docker-compose logs --since 2025-12-21T10:00:00 database_service
```

**Log Aggregation**:
```yaml
# docker-compose.yml
services:
  business_metadata:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

### Alerting

**Alert Conditions**:
- Service down (health check fails)
- High error rate (>5%)
- Slow response time (p95 > 1s)
- Database connection pool exhausted
- Disk space low (<10%)
- Memory usage high (>90%)

**Alert Channels**:
- Email notifications
- Slack/Teams webhooks
- PagerDuty integration
- SMS alerts (critical only)

---

## Troubleshooting

### Common Issues

#### **Issue: Service Won't Start**

**Symptoms**:
- Container exits immediately
- Health check fails
- Logs show errors

**Diagnosis**:
```powershell
# Check container status
docker-compose ps

# View logs
docker-compose logs business_metadata

# Check for port conflicts
netstat -ano | findstr ":8020"

# Verify environment variables
docker-compose config
```

**Solutions**:
1. Check environment variables are set
2. Verify dependencies are running (DB, Redis)
3. Check port availability
4. Review logs for specific errors
5. Rebuild container: `docker-compose build --no-cache business_metadata`

#### **Issue: Database Connection Failed**

**Symptoms**:
- Services can't connect to database
- "Connection refused" errors
- Timeout errors

**Diagnosis**:
```powershell
# Check TimescaleDB is running
docker-compose ps timescaledb

# Test connection
docker-compose exec timescaledb psql -U multiservice_user -d multiservice_db -c "SELECT 1;"

# Check connection string
echo $env:DATABASE_URL
```

**Solutions**:
1. Verify TimescaleDB is healthy
2. Check credentials match
3. Verify network connectivity
4. Check connection pool settings
5. Review firewall rules

#### **Issue: High Memory Usage**

**Symptoms**:
- Container using excessive memory
- OOM (Out of Memory) errors
- System slowdown

**Diagnosis**:
```powershell
# Check memory usage
docker stats

# Check specific container
docker stats analyticsengine-business_metadata-1
```

**Solutions**:
1. Increase container memory limit
2. Optimize queries (reduce result sets)
3. Enable query result caching
4. Review connection pool size
5. Check for memory leaks

#### **Issue: Slow Query Performance**

**Symptoms**:
- API responses slow
- Database queries timeout
- High CPU on database

**Diagnosis**:
```sql
-- Check slow queries
SELECT query, calls, total_time, mean_time
FROM pg_stat_statements
ORDER BY mean_time DESC
LIMIT 10;

-- Check active queries
SELECT pid, query, state, query_start
FROM pg_stat_activity
WHERE state != 'idle';
```

**Solutions**:
1. Add indexes on frequently queried columns
2. Use continuous aggregates for time-series
3. Enable query caching
4. Optimize query structure
5. Increase database resources

### Debugging Tools

**Docker Commands**:
```powershell
# Execute command in container
docker-compose exec business_metadata bash

# View container logs
docker-compose logs -f business_metadata

# Inspect container
docker inspect analyticsengine-business_metadata-1

# Check resource usage
docker stats
```

**Database Tools**:
```powershell
# Connect to database
docker-compose exec timescaledb psql -U multiservice_user -d multiservice_db

# List tables
\dt

# Describe table
\d connector_profiles

# View indexes
\di

# Check table sizes
SELECT pg_size_pretty(pg_total_relation_size('connector_profiles'));
```

---

## Maintenance

### Regular Maintenance Tasks

#### **Daily**
- [ ] Check service health
- [ ] Review error logs
- [ ] Monitor disk space
- [ ] Verify backups completed

#### **Weekly**
- [ ] Review performance metrics
- [ ] Check for security updates
- [ ] Analyze slow queries
- [ ] Clean up old logs

#### **Monthly**
- [ ] Update dependencies
- [ ] Review capacity planning
- [ ] Test disaster recovery
- [ ] Security audit

### Updates and Patches

**Update Process**:
```powershell
# 1. Backup current state
docker-compose exec timescaledb pg_dump -U multiservice_user multiservice_db > backup.sql

# 2. Pull latest images
docker-compose pull

# 3. Stop services
docker-compose down

# 4. Start with new images
docker-compose up -d

# 5. Run migrations
docker-compose exec database_service alembic upgrade head

# 6. Verify health
docker-compose ps
```

### Scaling

**Horizontal Scaling**:
```yaml
# docker-compose.yml
services:
  calculation_engine_service:
    deploy:
      replicas: 3  # Run 3 instances
```

**Vertical Scaling**:
```yaml
# docker-compose.yml
services:
  timescaledb:
    deploy:
      resources:
        limits:
          cpus: '4'
          memory: 8G
        reservations:
          cpus: '2'
          memory: 4G
```

---

## Backup and Recovery

### Backup Strategy

**Backup Types**:
1. **Full Backup**: Complete database dump (daily)
2. **Incremental Backup**: WAL archiving (continuous)
3. **Volume Backup**: Docker volume snapshot (weekly)
4. **Configuration Backup**: Environment files (on change)

**Backup Schedule**:
```
Daily:   Full database backup at 2 AM
Hourly:  WAL archiving
Weekly:  Volume snapshot
Monthly: Long-term archive
```

### Backup Procedures

**Full Database Backup**:
```powershell
# Create backup
$date = Get-Date -Format "yyyyMMdd_HHmmss"
docker-compose exec timescaledb pg_dump -U multiservice_user multiservice_db > "backup_$date.sql"

# Compress backup
gzip "backup_$date.sql"

# Upload to cloud storage
aws s3 cp "backup_$date.sql.gz" s3://backups/analytics-engine/
```

**Volume Backup**:
```powershell
# Stop services
docker-compose stop

# Backup volume
docker run --rm -v analyticsengine_timescaledb_data:/data -v ${PWD}:/backup alpine tar czf /backup/volume_backup.tar.gz /data

# Restart services
docker-compose start
```

### Recovery Procedures

**Restore from Backup**:
```powershell
# 1. Stop services
docker-compose down

# 2. Remove old volume
docker volume rm analyticsengine_timescaledb_data

# 3. Recreate volume
docker volume create analyticsengine_timescaledb_data

# 4. Start database
docker-compose up -d timescaledb

# 5. Wait for database to be ready
Start-Sleep -Seconds 30

# 6. Restore backup
gunzip -c backup_20251221.sql.gz | docker-compose exec -T timescaledb psql -U multiservice_user -d multiservice_db

# 7. Verify data
docker-compose exec timescaledb psql -U multiservice_user -d multiservice_db -c "\dt"

# 8. Start all services
docker-compose up -d
```

---

## Performance Tuning

### Database Optimization

**Connection Pooling**:
```python
# Increase pool size for high load
engine = create_async_engine(
    DATABASE_URL,
    pool_size=50,
    max_overflow=20
)
```

**Query Optimization**:
```sql
-- Add indexes
CREATE INDEX idx_connector_profiles_created_at ON connector_profiles(created_at);

-- Use continuous aggregates
CREATE MATERIALIZED VIEW kpi_hourly
WITH (timescaledb.continuous) AS
SELECT time_bucket('1 hour', time), AVG(value)
FROM kpi_data
GROUP BY 1;
```

### Caching Strategy

**Redis Caching**:
```python
# Cache query results
cache_key = f"kpis:{module}:{timeframe}"
cached = await redis.get(cache_key)
if cached:
    return cached

result = await execute_query(...)
await redis.setex(cache_key, 300, result)  # 5 min TTL
```

### Resource Allocation

**Docker Resource Limits**:
```yaml
services:
  timescaledb:
    deploy:
      resources:
        limits:
          cpus: '4'
          memory: 8G
```

---

## Security Operations

### Access Control

**Service-to-Service Authentication**:
- API keys for service authentication
- JWT tokens for user sessions
- Network isolation via Docker networks

**Database Access**:
- Separate users for services
- Read-only users for reporting
- Strong passwords
- Connection encryption (SSL)

### Secrets Management

**Environment Variables**:
```powershell
# Never commit secrets to git
# Use environment variables or secret management

# Development
$env:DATABASE_PASSWORD = "dev_password"

# Production - use secrets manager
# AWS Secrets Manager, Azure Key Vault, etc.
```

### Security Monitoring

**Audit Logging**:
- Log all authentication attempts
- Track API access patterns
- Monitor for suspicious activity
- Alert on security events

---

## Related Documentation

- **[Deployment History](../deployment/)** - Deployment summaries
- **[Database Guide](../database/README.md)** - Database operations
- **[Architecture Overview](../architecture/README.md)** - System architecture
- **[Troubleshooting Guide](./troubleshooting.md)** - Detailed troubleshooting

---

**Next**: [Development Guide](../development/README.md) | [Database Guide](../database/README.md)

