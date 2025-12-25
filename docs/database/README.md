# Database Guide - Analytics Engine

**Complete guide to database architecture, migrations, and data management**

---

## Table of Contents

1. [Overview](#overview)
2. [Database Architecture](#database-architecture)
3. [TimescaleDB Features](#timescaledb-features)
4. [Schema Management](#schema-management)
5. [Migrations](#migrations)
6. [Data Persistence](#data-persistence)
7. [CQRS Pattern](#cqrs-pattern)
8. [Performance Optimization](#performance-optimization)
9. [Backup and Recovery](#backup-and-recovery)

---

## Overview

Analytics Engine uses **TimescaleDB**, a PostgreSQL extension optimized for time-series data, as its primary database. The system implements a **CQRS pattern** with separate read and write models for optimal performance.

### Key Features

- ✅ **TimescaleDB Hypertables**: Automatic time-based partitioning
- ✅ **Continuous Aggregates**: Pre-computed materialized views
- ✅ **Alembic Migrations**: Automated schema versioning
- ✅ **CQRS Pattern**: Optimized read/write separation
- ✅ **Docker Volumes**: Persistent data storage
- ✅ **Two-Tier Schema**: System core + dynamic layer

---

## Database Architecture

### Connection Details

**Development**:
```
Host: localhost
Port: 5432
Database: multiservice_db
User: multiservice_user
Password: multiservice_password
```

**Connection String**:
```
postgresql+asyncpg://multiservice_user:multiservice_password@localhost:5432/multiservice_db
```

### Database Structure

```
multiservice_db
├── public (schema)
│   ├── alembic_version          ← Migration tracking
│   ├── connector_profiles       ← Connection profiles (JSONB)
│   ├── client_configs           ← Client configurations (JSONB)
│   ├── service_proposals        ← Service proposals (JSONB)
│   ├── market_data              ← Market data (hypertable)
│   └── news_articles            ← News articles (hypertable)
└── analytics_data (schema)
    └── [dynamic tables]         ← User-defined tables
```

### Table Categories

#### **System Tables** (Zone 1)
Managed by Alembic migrations:
- `alembic_version` - Migration tracking
- `connector_profiles` - Data source connections
- `client_configs` - Client settings
- `service_proposals` - Generated proposals

#### **Time-Series Tables** (Hypertables)
Optimized for time-series data:
- `market_data` - Financial market data
- `news_articles` - News and sentiment data
- `telemetry_events` - System telemetry

#### **Dynamic Tables** (Zone 2)
Application-managed:
- User-defined object models
- KPI calculation results
- Custom analytics tables

---

## TimescaleDB Features

### Hypertables

**What are Hypertables?**
TimescaleDB's abstraction for time-series data that automatically partitions data into chunks based on time.

**Benefits**:
- Automatic time-based partitioning
- Efficient time-range queries
- Parallel query execution
- Automatic chunk management

**Creating a Hypertable**:
```sql
-- Create regular table
CREATE TABLE sensor_data (
    time TIMESTAMPTZ NOT NULL,
    sensor_id INTEGER,
    temperature DOUBLE PRECISION,
    humidity DOUBLE PRECISION
);

-- Convert to hypertable
SELECT create_hypertable('sensor_data', 'time');
```

**In Alembic Migration**:
```python
def upgrade():
    # Create table
    op.create_table(
        'sensor_data',
        sa.Column('time', sa.DateTime(timezone=True), nullable=False),
        sa.Column('sensor_id', sa.Integer()),
        sa.Column('temperature', sa.Float()),
        sa.Column('humidity', sa.Float())
    )
    
    # Convert to hypertable
    op.execute("SELECT create_hypertable('sensor_data', 'time');")
```

### Continuous Aggregates

**What are Continuous Aggregates?**
Automatically refreshed materialized views that pre-compute aggregations.

**Benefits**:
- Pre-computed aggregations
- Automatic refresh
- Fast query performance
- Reduced compute load

**Example**:
```sql
CREATE MATERIALIZED VIEW sensor_data_hourly
WITH (timescaledb.continuous) AS
SELECT 
    time_bucket('1 hour', time) AS bucket,
    sensor_id,
    AVG(temperature) AS avg_temp,
    MAX(temperature) AS max_temp,
    MIN(temperature) AS min_temp
FROM sensor_data
GROUP BY bucket, sensor_id;

-- Add refresh policy
SELECT add_continuous_aggregate_policy('sensor_data_hourly',
    start_offset => INTERVAL '3 hours',
    end_offset => INTERVAL '1 hour',
    schedule_interval => INTERVAL '1 hour');
```

### Compression

**Automatic Data Compression**:
```sql
-- Enable compression
ALTER TABLE sensor_data SET (
    timescaledb.compress,
    timescaledb.compress_segmentby = 'sensor_id'
);

-- Add compression policy (compress data older than 7 days)
SELECT add_compression_policy('sensor_data', INTERVAL '7 days');
```

### Retention Policies

**Automatic Data Archival**:
```sql
-- Drop chunks older than 2 years
SELECT add_retention_policy('sensor_data', INTERVAL '2 years');
```

---

## Schema Management

### Two-Tier Strategy

#### **Zone 1: System Core**
**Characteristics**:
- Static tables (Auth, Metadata, Config)
- Managed by Alembic migrations
- Strict schema enforcement
- CI/CD validation on mismatch

**Tables**:
- `alembic_version`
- `connector_profiles`
- `client_configs`
- `service_proposals`
- System configuration tables

**Management**:
```bash
# Create migration
alembic revision -m "add system table"

# Apply migration
alembic upgrade head

# Rollback
alembic downgrade -1
```

#### **Zone 2: Dynamic Layer**
**Characteristics**:
- User-defined tables
- Application-managed schema
- Self-healing via ConsistencyChecker
- Flexible schema evolution

**Tables**:
- Object model tables
- KPI result tables
- Custom analytics tables

**Management**:
- Defined in object model definitions
- Created by Business Metadata Service
- Validated by ConsistencyChecker
- No Alembic migrations needed

---

## Migrations

### Alembic Setup

**Directory Structure**:
```
alembic/
├── versions/
│   └── 20251221_062048_add_persistent_storage_tables.py
├── env.py
├── script.py.mako
└── README
```

**Configuration** (`alembic.ini`):
```ini
[alembic]
script_location = alembic
sqlalchemy.url = postgresql+asyncpg://user:pass@localhost:5432/db
```

### Creating Migrations

**Auto-generate Migration**:
```bash
# Set environment variable
export DATABASE_URL="postgresql+asyncpg://multiservice_user:multiservice_password@localhost:5432/multiservice_db"

# Auto-generate migration
alembic revision --autogenerate -m "add new table"
```

**Manual Migration**:
```bash
# Create empty migration
alembic revision -m "custom changes"
```

**Migration Template**:
```python
"""add new table

Revision ID: abc123
Revises: xyz789
Create Date: 2025-12-21 10:00:00.000000
"""
from alembic import op
import sqlalchemy as sa

revision = 'abc123'
down_revision = 'xyz789'

def upgrade():
    op.create_table(
        'my_table',
        sa.Column('id', sa.String(255), primary_key=True),
        sa.Column('data', sa.JSON(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'))
    )
    
    # Create index
    op.create_index('ix_my_table_created_at', 'my_table', ['created_at'])
    
    # Convert to hypertable (if time-series)
    op.execute("SELECT create_hypertable('my_table', 'created_at');")

def downgrade():
    op.drop_index('ix_my_table_created_at')
    op.drop_table('my_table')
```

### Running Migrations

**Check Current Version**:
```bash
alembic current
```

**View History**:
```bash
alembic history --verbose
```

**Upgrade to Latest**:
```bash
alembic upgrade head
```

**Upgrade One Version**:
```bash
alembic upgrade +1
```

**Downgrade One Version**:
```bash
alembic downgrade -1
```

**Downgrade to Specific Version**:
```bash
alembic downgrade abc123
```

**Downgrade to Base**:
```bash
alembic downgrade base
```

### Migration Best Practices

1. **Always test migrations** in development first
2. **Backup database** before production migrations
3. **Use transactions** for atomic migrations
4. **Add indexes** for frequently queried columns
5. **Document changes** in migration docstring
6. **Test rollback** (downgrade) functionality
7. **Avoid data loss** in downgrade operations

---

## Data Persistence

### Docker Volumes

**Volume Configuration** (`docker-compose.yml`):
```yaml
volumes:
  timescaledb_data:
    driver: local
```

**Volume Mount**:
```yaml
services:
  timescaledb:
    volumes:
      - timescaledb_data:/var/lib/postgresql/data
```

### How Persistence Works

1. **Container starts** → Mounts volume to `/var/lib/postgresql/data`
2. **PostgreSQL writes** → Data written to volume (on host)
3. **Container stops** → Volume remains on host
4. **Container restarts** → Mounts same volume
5. **Data available** → All tables and data intact

### Volume Management

**List Volumes**:
```bash
docker volume ls
```

**Inspect Volume**:
```bash
docker volume inspect analyticsengine_timescaledb_data
```

**Backup Volume**:
```bash
docker run --rm -v analyticsengine_timescaledb_data:/data -v $(pwd):/backup alpine tar czf /backup/db_backup.tar.gz /data
```

**Restore Volume**:
```bash
docker run --rm -v analyticsengine_timescaledb_data:/data -v $(pwd):/backup alpine tar xzf /backup/db_backup.tar.gz -C /
```

**Remove Volume** (⚠️ DANGER - deletes all data):
```bash
docker-compose down -v
```

### Data Verification

**Check Data Persists**:
```bash
# Insert test data
docker-compose exec timescaledb psql -U multiservice_user -d multiservice_db -c "INSERT INTO connector_profiles (id, profile_data) VALUES ('test-1', '{\"name\": \"test\"}'::jsonb);"

# Restart container
docker-compose restart timescaledb

# Verify data still exists
docker-compose exec timescaledb psql -U multiservice_user -d multiservice_db -c "SELECT * FROM connector_profiles WHERE id = 'test-1';"
```

---

## CQRS Pattern

### Command Side (Write)

**Characteristics**:
- Normalized data model
- Strong consistency
- Validation and business rules
- Event publishing

**Flow**:
```
Command → Validation → Write Model → Database → Event
```

**Example**:
```python
async def create_entity(command: CreateEntityCommand):
    # Validate
    validate_command(command)
    
    # Execute command
    result = await db_service.execute_command(
        command="INSERT INTO entities (id, data) VALUES (:id, :data)",
        parameters={"id": command.id, "data": command.data}
    )
    
    # Publish event
    await messaging_service.publish_event(
        topic="entity.created",
        payload={"entity_id": command.id}
    )
    
    return result
```

### Query Side (Read)

**Characteristics**:
- Denormalized data model
- Eventual consistency
- Optimized for queries
- Caching enabled

**Flow**:
```
Query → Cache Check → Read Model → Result
```

**Example**:
```python
async def get_entities(query: GetEntitiesQuery):
    # Check cache
    cache_key = f"entities:{query.filters}"
    cached = await redis.get(cache_key)
    if cached:
        return cached
    
    # Execute query
    result = await db_service.execute_query(
        query="SELECT * FROM entities WHERE status = :status",
        parameters={"status": query.status}
    )
    
    # Cache result
    await redis.setex(cache_key, 300, result)
    
    return result
```

### Read Model Updates

**Event-Driven Updates**:
```python
async def on_entity_created(event: EntityCreatedEvent):
    # Update read model
    await db_service.execute_command(
        command="INSERT INTO entity_summary (id, name, count) VALUES (:id, :name, 1) ON CONFLICT (id) DO UPDATE SET count = entity_summary.count + 1",
        parameters={"id": event.entity_id, "name": event.entity_name}
    )
```

---

## Performance Optimization

### Indexing Strategy

**Time-Series Indexes**:
```sql
-- Time-based index (automatically created for hypertables)
CREATE INDEX idx_sensor_data_time ON sensor_data (time DESC);

-- Composite index
CREATE INDEX idx_sensor_data_time_sensor ON sensor_data (time DESC, sensor_id);
```

**JSONB Indexes**:
```sql
-- GIN index for JSONB queries
CREATE INDEX idx_connector_profiles_data ON connector_profiles USING GIN (profile_data);

-- Specific JSONB path index
CREATE INDEX idx_connector_profiles_type ON connector_profiles ((profile_data->>'type'));
```

### Query Optimization

**Use Continuous Aggregates**:
```sql
-- Instead of aggregating on every query
SELECT time_bucket('1 hour', time), AVG(temperature)
FROM sensor_data
WHERE time > NOW() - INTERVAL '7 days'
GROUP BY 1;

-- Use pre-computed continuous aggregate
SELECT * FROM sensor_data_hourly
WHERE bucket > NOW() - INTERVAL '7 days';
```

**Partition Pruning**:
```sql
-- TimescaleDB automatically prunes partitions
SELECT * FROM sensor_data
WHERE time BETWEEN '2025-01-01' AND '2025-01-31';
-- Only scans January chunks
```

### Connection Pooling

**SQLAlchemy Pool Configuration**:
```python
engine = create_async_engine(
    DATABASE_URL,
    pool_size=20,          # Max connections
    max_overflow=10,       # Additional connections
    pool_timeout=30,       # Wait timeout
    pool_recycle=3600,     # Recycle connections
    pool_pre_ping=True     # Verify connections
)
```

---

## Backup and Recovery

### Backup Strategies

**Full Database Backup**:
```bash
# Backup
docker-compose exec timescaledb pg_dump -U multiservice_user multiservice_db > backup_$(date +%Y%m%d).sql

# Restore
cat backup_20251221.sql | docker-compose exec -T timescaledb psql -U multiservice_user -d multiservice_db
```

**Selective Table Backup**:
```bash
# Backup specific table
docker-compose exec timescaledb pg_dump -U multiservice_user -d multiservice_db -t connector_profiles > connector_profiles_backup.sql
```

**Compressed Backup**:
```bash
# Backup with compression
docker-compose exec timescaledb pg_dump -U multiservice_user multiservice_db | gzip > backup_$(date +%Y%m%d).sql.gz

# Restore
gunzip -c backup_20251221.sql.gz | docker-compose exec -T timescaledb psql -U multiservice_user -d multiservice_db
```

### Point-in-Time Recovery

**Enable WAL Archiving**:
```yaml
# docker-compose.yml
timescaledb:
  command: >
    postgres
    -c wal_level=replica
    -c archive_mode=on
    -c archive_command='cp %p /var/lib/postgresql/archive/%f'
```

### Disaster Recovery

**Recovery Steps**:
1. Stop all services
2. Restore database from backup
3. Run migrations to latest version
4. Verify data integrity
5. Restart services
6. Validate functionality

---

## Related Documentation

- **[Database Migration Guide](../DATABASE_MIGRATION_GUIDE.md)** - Recent migration details
- **[Archival Guide](../archival_implementation_guide.md)** - Data archival to lakehouse
- **[Operations Guide](../operations/README.md)** - Deployment and operations
- **[Architecture Overview](../architecture/README.md)** - System architecture

---

## Useful Commands Reference

```bash
# Connect to database
docker-compose exec timescaledb psql -U multiservice_user -d multiservice_db

# List tables
\dt

# Describe table
\d connector_profiles

# List indexes
\di

# View hypertables
SELECT * FROM timescaledb_information.hypertables;

# View continuous aggregates
SELECT * FROM timescaledb_information.continuous_aggregates;

# View chunks
SELECT * FROM timescaledb_information.chunks;

# Database size
SELECT pg_size_pretty(pg_database_size('multiservice_db'));

# Table size
SELECT pg_size_pretty(pg_total_relation_size('connector_profiles'));
```

---

**Next**: [Operations Guide](../operations/README.md) | [Development Guide](../development/README.md)

