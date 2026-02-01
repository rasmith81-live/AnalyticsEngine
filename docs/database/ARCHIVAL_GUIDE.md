# TimescaleDB Archival Guide

This guide provides a complete reference for the event-driven TimescaleDB archival solution, including architecture overview, implementation details, and operational procedures.

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Event Flow](#event-flow)
4. [Prerequisites](#prerequisites)
5. [Database Service Configuration](#database-service-configuration)
6. [Archival Service Configuration](#archival-service-configuration)
7. [Redis Configuration](#redis-configuration)
8. [Azure Storage Configuration](#azure-storage-configuration)
9. [Deployment](#deployment)
10. [API Reference](#api-reference)
11. [Testing](#testing)
12. [Monitoring](#monitoring)
13. [Troubleshooting](#troubleshooting)

---

## Overview

The archival solution maintains only **2 years of data** in TimescaleDB for optimal query performance while streaming older data to a lakehouse storage system (Azure Data Lake Storage Gen2) via Redis messaging.

### Benefits

- **Real-time Processing**: Event-driven architecture eliminates batch ETL jobs
- **Cost Optimization**: Keeps only recent data in TimescaleDB
- **Performance**: Maintains optimal query performance for recent data
- **Data Integrity**: Two-phase process ensures data is archived before removal
- **Scalability**: Microservices can scale independently

---

## Architecture

### Components

| Component | Responsibility |
|-----------|----------------|
| **Database Service** | Manages retention, identifies old chunks, publishes archival events, drops chunks after confirmation |
| **Archival Service** | Subscribes to events, extracts data, writes to lakehouse, publishes confirmations |
| **Redis Messaging** | Event-driven pub/sub communication between services |
| **Lakehouse (ADLS Gen2)** | Long-term Parquet storage for archived data |

### Component Flow

```
┌─────────────────┐     archival.request     ┌─────────────────┐
│ Database Service│ ─────────────────────────▶│ Archival Service│
│                 │                           │                 │
│ RetentionManager│     archival.confirmation │ LakehouseClient │
│                 │ ◀─────────────────────────│                 │
└────────┬────────┘                           └────────┬────────┘
         │                                             │
         ▼                                             ▼
┌─────────────────┐                           ┌─────────────────┐
│   TimescaleDB   │                           │  Azure Storage  │
│   (2yr data)    │                           │  (Parquet files)│
└─────────────────┘                           └─────────────────┘
```

---

## Event Flow

1. **Retention Check**: RetentionManager identifies chunks older than 2 years
2. **Archival Request**: Database Service publishes to `database.archival.request`
3. **Data Extraction**: Archival Service extracts data from TimescaleDB chunk
4. **Lakehouse Write**: Data written to Azure Storage in Parquet format
5. **Confirmation**: Archival Service publishes to `database.archival.confirmation`
6. **Chunk Removal**: Database Service drops the chunk after success confirmation

---

## Prerequisites

- TimescaleDB configured with hypertables
- Redis server accessible to both services
- Azure Storage account (or Azurite for local dev)
- Docker and Docker Compose
- Python 3.9+ with async support

---

## Database Service Configuration

### Settings

```python
class DatabaseServiceSettings(BaseSettings):
    # Retention and Archival Settings
    retention_period_days: int = 730  # 2 years
    retention_check_interval_hours: int = 24
    archival_batch_size: int = 10
    archival_service_url: str = "http://archival_service:8080"
    archival_service_timeout_seconds: int = 30
    
    # Redis Settings
    redis_channel_prefix: str = "database"
    redis_pool_size: int = 10
    
    # Lakehouse Settings
    lakehouse_storage_account: str = "yourstorageaccount"
    lakehouse_container: str = "timescaledb-archive"
```

### RetentionManager

The `RetentionManager` class handles:

- `start()`: Initialize and start the retention manager
- `stop()`: Gracefully stop the retention manager
- `check_retention()`: Identify chunks for archival
- `publish_archival_event()`: Create and publish archival events
- `handle_archival_confirmation()`: Process confirmation events
- `drop_chunk()`: Remove archived chunks from TimescaleDB

### MessagingClient Integration

```python
# Initialize messaging
messaging_client = MessagingClient(
    redis_url=config.redis_url,
    service_name="database_service",
    pool_size=config.redis_pool_size
)

await messaging_client.connect()

# Subscribe to confirmations
await messaging_client.subscribe(
    topic=f"{config.redis_channel_prefix}.archival.confirmation",
    callback=retention_manager.handle_archival_confirmation
)
```

---

## Archival Service Configuration

### Settings

```python
class ArchivalServiceSettings(BaseSettings):
    service_name: str = "archival_service"
    host: str = "0.0.0.0"
    port: int = 8080
    
    # Redis
    redis_url: str = "redis://redis:6379"
    redis_pool_size: int = 10
    
    # Azure Storage
    azure_storage_connection_string: str = ""
    azure_storage_account_name: str = "yourstorageaccount"
    azure_storage_container: str = "timescaledb-archive"
    
    # Concurrency
    max_concurrent_archival_tasks: int = 5
    
    # Database for extraction
    timescaledb_url: str = "postgresql://postgres:postgres@timescaledb:5432/postgres"
```

### Event Handler

```python
async def process_archival_event(payload):
    """Process an archival event from the Database Service."""
    try:
        event = ArchivalEvent(**payload)
        data = await extract_chunk_data(event)
        lakehouse_path = f"{event.table_name}/{event.chunk_id}.parquet"
        
        await app.state.lakehouse_client.write_parquet(
            path=lakehouse_path, data=data
        )
        
        confirmation = ArchivalConfirmation(
            event_id=event.event_id,
            chunk_id=event.chunk_id,
            status=ArchivalStatus.SUCCESS,
            lakehouse_path=lakehouse_path
        )
    except Exception as e:
        confirmation = ArchivalConfirmation(
            event_id=event.event_id,
            chunk_id=event.chunk_id,
            status=ArchivalStatus.FAILED,
            error_message=str(e)
        )
    
    await app.state.messaging_client.publish_event(
        topic="database.archival.confirmation",
        event_type="archival_confirmation",
        payload=confirmation.model_dump()
    )
```

---

## Redis Configuration

```yaml
redis:
  image: redis:7
  ports:
    - "6379:6379"
  volumes:
    - redis-data:/data
  command: redis-server --appendonly yes
  healthcheck:
    test: ["CMD", "redis-cli", "ping"]
    interval: 5s
    timeout: 3s
    retries: 5
```

---

## Azure Storage Configuration

### Local Development (Azurite)

```yaml
azurite:
  image: mcr.microsoft.com/azure-storage/azurite
  ports:
    - "10000:10000"  # Blob
    - "10001:10001"  # Queue
    - "10002:10002"  # Table
  volumes:
    - azurite-data:/data
```

### Production

1. Create Azure Storage account
2. Create container `timescaledb-archive`
3. Generate connection string or use managed identity
4. Configure in both services

---

## Deployment

### Docker Compose Services

```yaml
database_service:
  build: ./services/backend_services/database_service
  environment:
    - REDIS_URL=redis://redis:6379
    - RETENTION_PERIOD_DAYS=730
    - LAKEHOUSE_STORAGE_ACCOUNT=yourstorageaccount
  depends_on:
    - redis
    - timescaledb

archival_service:
  build: ./services/backend_services/archival_service
  environment:
    - REDIS_URL=redis://redis:6379
    - AZURE_STORAGE_CONNECTION_STRING=...
  depends_on:
    - redis
    - timescaledb
    - azurite
```

### Deploy

```powershell
docker-compose build
docker-compose up -d
docker-compose ps  # Verify all running
```

---

## API Reference

### Database Service

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/database/retention/status` | GET | Retention status for all hypertables |
| `/database/retention/trigger-archival` | POST | Manually trigger archival |

### Archival Service

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/archival/status` | GET | Archival service status |
| `/archival/events` | GET | Recent archival events |
| `/archival/metrics` | GET | Archival metrics |

---

## Testing

### Run Archival Workflow Test

```powershell
python tests/test_archival_workflow.py
```

### Verify Endpoints

```powershell
# Health checks
Invoke-RestMethod -Uri "http://localhost:8000/health"
Invoke-RestMethod -Uri "http://localhost:8080/health"

# Retention status
Invoke-RestMethod -Uri "http://localhost:8000/database/retention/status"
```

### Verify Lakehouse Storage

```powershell
az storage blob list --container-name timescaledb-archive --output table
```

---

## Monitoring

### Key Metrics

- Archival event count and status
- Chunk counts awaiting archival
- Storage capacity usage
- Redis connection health

### Alerts to Configure

- Failed archival events
- High chunk backlog
- Storage capacity issues
- Redis connection problems

### Maintenance Schedule

| Task | Frequency |
|------|-----------|
| Review archival logs | Weekly |
| Validate lakehouse organization | Monthly |
| Test recovery process | Quarterly |
| Update configurations | As needed |

---

## Troubleshooting

### Archival Events Not Being Processed

**Symptoms**: Chunks older than retention period remain in TimescaleDB

**Solutions**:
- Check Redis connectivity from Database Service
- Verify retention manager is running
- Check retention period configuration
- Manually trigger archival via API

### Confirmations Not Received

**Symptoms**: Events published but chunks not dropped

**Solutions**:
- Check Redis connectivity from Archival Service
- Verify subscription to confirmation topic
- Check Archival Service logs for errors

### Data Extraction Failures

**Symptoms**: Failed confirmations with database errors

**Solutions**:
- Increase query timeout settings
- Reduce batch size for large chunks
- Check TimescaleDB connection

### Lakehouse Storage Issues

**Symptoms**: Failed confirmations with storage errors

**Solutions**:
- Verify storage connection string
- Check container existence and permissions
- For Azurite, ensure service is running

### Performance Issues

**Symptoms**: Slow archival, growing backlog

**Solutions**:
- Increase concurrent archival tasks
- Optimize data extraction queries
- Scale Archival Service horizontally
- Adjust TimescaleDB chunk intervals
