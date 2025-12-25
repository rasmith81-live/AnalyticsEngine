# Database Migration Guide - Persistent Storage Tables

## Overview

This guide walks you through running the database migration to add the three missing tables required for persistent storage in the Connector Service and Demo Config Service.

**Migration**: `20251221_062048_add_persistent_storage_tables.py`  
**Status**: Ready to run  
**Impact**: Resolves critical runtime failures in Connector and Demo Config services

---

## Tables Being Created

### 1. `connector_profiles`
**Purpose**: Store connection profiles for external data sources

**Structure**:
```sql
CREATE TABLE connector_profiles (
    id VARCHAR(255) PRIMARY KEY,
    profile_data JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX ix_connector_profiles_created_at ON connector_profiles(created_at);
```

**JSONB Schema**:
```json
{
  "name": "string",
  "type": "sql|api|excel",
  "connection_string": "string (encrypted)",
  "credentials": {
    "username": "string",
    "password": "string"
  },
  "schema_info": {
    "tables": [...],
    "columns": {...}
  },
  "test_status": "success|failed",
  "last_tested": "timestamp"
}
```

---

### 2. `client_configs`
**Purpose**: Store client-specific configurations

**Structure**:
```sql
CREATE TABLE client_configs (
    client_id VARCHAR(255) PRIMARY KEY,
    config_data JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX ix_client_configs_created_at ON client_configs(created_at);
```

**JSONB Schema**:
```json
{
  "client_name": "string",
  "license_type": "basic|professional|enterprise",
  "modules": ["string"],
  "preferences": {...},
  "custom_kpis": [...],
  "data_sources": [...]
}
```

---

### 3. `service_proposals`
**Purpose**: Store generated service proposals and SOWs

**Structure**:
```sql
CREATE TABLE service_proposals (
    proposal_id VARCHAR(255) PRIMARY KEY,
    proposal_data JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX ix_service_proposals_created_at ON service_proposals(created_at);
```

**JSONB Schema**:
```json
{
  "client_id": "string",
  "proposal_type": "implementation|consulting",
  "pricing": {
    "total": number,
    "breakdown": {...}
  },
  "timeline": {
    "start_date": "date",
    "end_date": "date",
    "phases": [...]
  },
  "resources": {
    "consultants": [...],
    "hours": number
  },
  "status": "draft|sent|accepted|rejected"
}
```

---

## Running the Migration

### Option 1: Using Docker Compose (Recommended)

#### Step 1: Ensure services are running
```bash
docker-compose up -d timescaledb database_service
```

#### Step 2: Check current migration status
```bash
docker-compose exec database_service alembic current
```

#### Step 3: Run the migration
```bash
docker-compose exec database_service alembic upgrade head
```

**Expected Output**:
```
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 20251221_062048, add persistent storage tables
```

#### Step 4: Verify tables created
```bash
docker-compose exec timescaledb psql -U postgres -d analytics_engine -c "\dt"
```

**Expected Output**:
```
                  List of relations
 Schema |        Name         | Type  |  Owner   
--------+---------------------+-------+----------
 public | connector_profiles  | table | postgres
 public | client_configs      | table | postgres
 public | service_proposals   | table | postgres
```

---

### Option 2: Using PowerShell Script

```powershell
# Navigate to project root
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine

# Run migration (dry run first to preview)
.\scripts\run_migration.ps1 -Action upgrade -DryRun

# Run actual migration
.\scripts\run_migration.ps1 -Action upgrade

# Check status
.\scripts\run_migration.ps1 -Action current
```

---

### Option 3: Direct Alembic Command (Local)

**Prerequisites**: 
- Python environment with alembic installed
- Database connection configured in `alembic.ini`

```bash
# From project root
alembic upgrade head
```

---

## Verification

### Quick Verification
```bash
docker-compose exec database_service python -c "
from sqlalchemy import create_engine, inspect
import os

engine = create_engine(os.environ['DATABASE_URL'].replace('+asyncpg', ''))
inspector = inspect(engine)
tables = inspector.get_table_names()

print('Tables found:')
for table in ['connector_profiles', 'client_configs', 'service_proposals']:
    if table in tables:
        print(f'  ✅ {table}')
    else:
        print(f'  ❌ {table} MISSING')
"
```

### Detailed Verification
```bash
# Run verification SQL script
docker-compose exec timescaledb psql -U postgres -d analytics_engine -f /app/scripts/verify_tables.sql
```

**This script will**:
- List all three tables
- Show table structures
- Display indexes
- Show table and column comments
- Test insert/select operations (rolled back)
- Display row counts

---

## Testing the Tables

### Test Connector Service

```bash
# Create a test connection profile
curl -X POST http://localhost:8023/connector/profiles \
  -H "Content-Type: application/json" \
  -d '{
    "id": "test-sql-connection",
    "name": "Test SQL Server",
    "type": "sql",
    "connection_string": "Server=localhost;Database=test;",
    "credentials": {
      "username": "testuser",
      "password": "testpass"
    }
  }'

# Retrieve the profile
curl http://localhost:8023/connector/profiles/test-sql-connection

# List all profiles
curl http://localhost:8023/connector/profiles
```

### Test Demo Config Service

```bash
# Create a test client config
curl -X POST http://localhost:8022/demo/clients \
  -H "Content-Type: application/json" \
  -d '{
    "client_id": "test-client-001",
    "client_name": "Test Corporation",
    "license_type": "professional",
    "modules": ["SCOR", "CRM"]
  }'

# Retrieve the config
curl http://localhost:8022/demo/clients/test-client-001

# Create a test proposal
curl -X POST http://localhost:8022/demo/proposals \
  -H "Content-Type: application/json" \
  -d '{
    "proposal_id": "prop-001",
    "client_id": "test-client-001",
    "proposal_type": "implementation",
    "status": "draft"
  }'
```

---

## Rollback (If Needed)

### Rollback to Previous State

```bash
# Check current revision
docker-compose exec database_service alembic current

# Rollback one revision
docker-compose exec database_service alembic downgrade -1

# Or rollback to base (removes all tables)
docker-compose exec database_service alembic downgrade base
```

**⚠️ WARNING**: Rollback will **delete all data** in these tables!

---

## Troubleshooting

### Issue: "relation already exists"

**Cause**: Tables were manually created or migration already ran

**Solution**:
```bash
# Mark migration as complete without running it
docker-compose exec database_service alembic stamp head
```

### Issue: "database connection failed"

**Cause**: TimescaleDB not running or connection string incorrect

**Solution**:
```bash
# Check TimescaleDB is running
docker-compose ps timescaledb

# Check database service logs
docker-compose logs database_service

# Verify connection string
docker-compose exec database_service env | grep DATABASE_URL
```

### Issue: "permission denied"

**Cause**: Database user doesn't have CREATE TABLE permissions

**Solution**:
```bash
# Grant permissions (run as postgres user)
docker-compose exec timescaledb psql -U postgres -d analytics_engine -c "
GRANT CREATE ON SCHEMA public TO your_user;
"
```

### Issue: Migration stuck or hanging

**Cause**: Database lock or long-running transaction

**Solution**:
```bash
# Check for locks
docker-compose exec timescaledb psql -U postgres -d analytics_engine -c "
SELECT pid, usename, state, query 
FROM pg_stat_activity 
WHERE state != 'idle';
"

# Kill blocking process if needed (use with caution)
# docker-compose exec timescaledb psql -U postgres -c "SELECT pg_terminate_backend(PID);"
```

---

## Post-Migration Checklist

- [ ] Migration completed successfully
- [ ] All three tables exist in database
- [ ] Indexes created on `created_at` columns
- [ ] Table and column comments present
- [ ] Connector Service can store/retrieve profiles
- [ ] Demo Config Service can store/retrieve configs
- [ ] Demo Config Service can store/retrieve proposals
- [ ] Data persists after container restart
- [ ] No errors in service logs

---

## Data Persistence Verification

### Test Container Restart

```bash
# Create test data
curl -X POST http://localhost:8023/connector/profiles \
  -H "Content-Type: application/json" \
  -d '{"id": "persist-test", "name": "Persistence Test", "type": "sql"}'

# Restart containers
docker-compose restart connector_service database_service

# Wait for services to be healthy
docker-compose ps

# Verify data still exists
curl http://localhost:8023/connector/profiles/persist-test
```

**Expected**: Data should still be present after restart

---

## Performance Considerations

### Index Usage

The migration creates indexes on `created_at` columns for efficient time-based queries:

```sql
-- Fast query with index
SELECT * FROM connector_profiles 
WHERE created_at > NOW() - INTERVAL '7 days'
ORDER BY created_at DESC;

-- Fast query with index
SELECT * FROM client_configs 
WHERE created_at BETWEEN '2025-01-01' AND '2025-12-31';
```

### JSONB Performance

JSONB columns support efficient querying:

```sql
-- Query by JSONB field (uses GIN index if created)
SELECT * FROM connector_profiles 
WHERE profile_data->>'type' = 'sql';

-- Extract specific fields
SELECT 
    id,
    profile_data->>'name' AS name,
    profile_data->>'type' AS type,
    created_at
FROM connector_profiles;
```

**Optional**: Create GIN index for JSONB queries:
```sql
CREATE INDEX idx_connector_profiles_data ON connector_profiles USING GIN (profile_data);
CREATE INDEX idx_client_configs_data ON client_configs USING GIN (config_data);
CREATE INDEX idx_service_proposals_data ON service_proposals USING GIN (proposal_data);
```

---

## Next Steps

After successful migration:

1. **Update KNOWN_LIMITATIONS_REMEDIATION_PLAN.md**: Mark Phase 1.1 as complete
2. **Update KNOWN_LIMITATIONS_VALIDATION_REPORT.md**: Update status to reflect tables now exist
3. **Test services**: Run integration tests for Connector and Demo Config services
4. **Monitor logs**: Watch for any database-related errors
5. **Performance testing**: Verify query performance meets requirements (<100ms)

---

## Related Documentation

- **Migration File**: `alembic/versions/20251221_062048_add_persistent_storage_tables.py`
- **Validation Report**: `KNOWN_LIMITATIONS_VALIDATION_REPORT.md`
- **Remediation Plan**: `KNOWN_LIMITATIONS_REMEDIATION_PLAN.md`
- **Changelog**: `CHANGELOG.md`
- **Connector Service**: `services/business_services/connector_service/app/database_client.py`
- **Demo Config Service**: `services/business_services/demo_config_service/app/database_client.py`

---

**Migration Created**: 2025-12-21  
**Status**: Ready to Execute  
**Impact**: Resolves Critical Issue #1 from Validation Report

