# TimescaleDB Archival Implementation Guide

This guide provides detailed implementation instructions for setting up and configuring the event-driven TimescaleDB archival solution in the multi-microservice architecture.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Database Service Configuration](#database-service-configuration)
3. [Archival Service Configuration](#archival-service-configuration)
4. [Redis Configuration](#redis-configuration)
5. [Azure Storage Configuration](#azure-storage-configuration)
6. [Deployment Steps](#deployment-steps)
7. [Verification and Testing](#verification-and-testing)
8. [Monitoring and Maintenance](#monitoring-and-maintenance)
9. [Troubleshooting](#troubleshooting)

## Prerequisites

Before implementing the archival solution, ensure you have:

- TimescaleDB properly configured with hypertables
- Redis server running and accessible to both services
- Azure Storage account (or Azurite for local development)
- Docker and Docker Compose for containerized deployment
- Python 3.9+ with async support

## Database Service Configuration

### 1. RetentionManager Setup

The `RetentionManager` class in the Database Service is responsible for identifying chunks older than the retention period and initiating the archival process.

#### Key Configuration Parameters

In `config.py`:

```python
class DatabaseServiceSettings(BaseSettings):
    # Existing settings...
    
    # Retention and Archival Settings
    retention_period_days: int = 730  # 2 years
    retention_check_interval_hours: int = 24
    archival_batch_size: int = 10
    archival_service_url: str = "http://archival_service:8080"
    archival_service_timeout_seconds: int = 30
    
    # Redis Settings for Messaging
    redis_channel_prefix: str = "database"
    redis_pool_size: int = 10
    
    # Lakehouse Settings
    lakehouse_storage_account: str = "yourstorageaccount"
    lakehouse_container: str = "timescaledb-archive"
```

#### RetentionManager Implementation

The `RetentionManager` class should:

1. Connect to TimescaleDB
2. Identify chunks older than the retention period
3. Publish archival events via Redis
4. Handle archival confirmations
5. Drop chunks after successful archival

Key methods include:

- `start()`: Initialize and start the retention manager
- `stop()`: Gracefully stop the retention manager
- `check_retention()`: Identify chunks for archival
- `publish_archival_event()`: Create and publish archival events
- `handle_archival_confirmation()`: Process confirmation events
- `drop_chunk()`: Remove archived chunks from TimescaleDB

### 2. MessagingClient Integration

The `MessagingClient` in the Database Service handles Redis pub/sub communication:

```python
# Initialize in main.py
messaging_client = MessagingClient(
    redis_url=config.redis_url,
    service_name="database_service",
    pool_size=config.redis_pool_size
)

# Start messaging client
await messaging_client.connect()

# Subscribe to confirmations
await messaging_client.subscribe(
    topic=f"{config.redis_channel_prefix}.archival.confirmation",
    callback=retention_manager.handle_archival_confirmation
)
```

### 3. API Endpoints

Add the following endpoints to the Database Service:

```python
@app.get("/database/retention/status")
async def get_retention_status(
    retention_manager: RetentionManager = Depends(get_retention_manager)
):
    """Get the current retention status for all hypertables."""
    return await retention_manager.get_status()

@app.post("/database/retention/trigger-archival")
async def trigger_archival(
    table_name: str = Query(..., description="Name of the hypertable to archive"),
    retention_manager: RetentionManager = Depends(get_retention_manager)
):
    """Manually trigger the archival process for a specific table."""
    return await retention_manager.trigger_archival(table_name)
```

## Archival Service Configuration

### 1. LakehouseClient Setup

The `LakehouseClient` handles writing archived data to Azure Data Lake Storage:

#### Key Configuration Parameters

In `config.py`:

```python
class ArchivalServiceSettings(BaseSettings):
    # Service settings
    service_name: str = "archival_service"
    host: str = "0.0.0.0"
    port: int = 8080
    
    # Redis settings
    redis_url: str = "redis://redis:6379"
    redis_pool_size: int = 10
    
    # Azure Storage settings
    azure_storage_connection_string: str = ""
    azure_storage_account_name: str = "yourstorageaccount"
    azure_storage_container: str = "timescaledb-archive"
    
    # Concurrency settings
    max_concurrent_archival_tasks: int = 5
    
    # Database settings for data extraction
    timescaledb_url: str = "postgresql://postgres:postgres@timescaledb:5432/postgres"
```

### 2. Event Handling

Implement event handlers in the Archival Service:

```python
@app.on_event("startup")
async def startup_event():
    # Initialize messaging client
    app.state.messaging_client = MessagingClient(
        redis_url=config.redis_url,
        service_name=config.service_name,
        pool_size=config.redis_pool_size
    )
    
    # Initialize lakehouse client
    app.state.lakehouse_client = LakehouseClient(
        connection_string=config.azure_storage_connection_string,
        account_name=config.azure_storage_account_name,
        container_name=config.azure_storage_container
    )
    
    # Connect to messaging
    await app.state.messaging_client.connect()
    
    # Subscribe to archival events
    await app.state.messaging_client.subscribe(
        topic="database.archival.request",
        callback=process_archival_event
    )
```

### 3. Archival Processing

Implement the archival processing logic:

```python
async def process_archival_event(payload):
    """Process an archival event from the Database Service."""
    try:
        # Parse event
        event = ArchivalEvent(**payload)
        
        # Extract data from TimescaleDB
        data = await extract_chunk_data(event)
        
        # Generate lakehouse path
        lakehouse_path = f"{event.table_name}/{event.chunk_id}.parquet"
        
        # Write to lakehouse
        await app.state.lakehouse_client.write_parquet(
            path=lakehouse_path,
            data=data
        )
        
        # Create success confirmation
        confirmation = ArchivalConfirmation(
            event_id=event.event_id,
            chunk_id=event.chunk_id,
            table_name=event.table_name,
            status=ArchivalStatus.SUCCESS,
            lakehouse_path=lakehouse_path,
            completed_at=datetime.utcnow().isoformat()
        )
    except Exception as e:
        # Create failure confirmation
        confirmation = ArchivalConfirmation(
            event_id=event.event_id,
            chunk_id=event.chunk_id,
            table_name=event.table_name,
            status=ArchivalStatus.FAILED,
            error_message=str(e),
            completed_at=datetime.utcnow().isoformat()
        )
    
    # Publish confirmation
    await app.state.messaging_client.publish_event(
        topic="database.archival.confirmation",
        event_type="archival_confirmation",
        payload=confirmation.model_dump()
    )
```

### 4. Data Extraction

Implement efficient data extraction from TimescaleDB:

```python
async def extract_chunk_data(event: ArchivalEvent):
    """Extract data from a TimescaleDB chunk."""
    # Connect to TimescaleDB
    engine = create_async_engine(config.timescaledb_url)
    
    async with engine.connect() as conn:
        # Query to extract data from specific chunk
        query = f"""
        SELECT * FROM {event.schema_name}.{event.table_name}
        WHERE {event.time_column} >= '{event.chunk_start_time}'
        AND {event.time_column} < '{event.chunk_end_time}'
        """
        
        # Execute query and fetch results
        result = await conn.execute(text(query))
        rows = result.fetchall()
        
        # Convert to dictionary format
        columns = result.keys()
        data = [dict(zip(columns, row)) for row in rows]
        
        return {
            "metadata": {
                "table_name": event.table_name,
                "chunk_id": event.chunk_id,
                "start_time": event.chunk_start_time,
                "end_time": event.chunk_end_time,
                "schema_name": event.schema_name,
                "row_count": len(data)
            },
            "rows": data
        }
```

## Redis Configuration

Configure Redis for reliable pub/sub messaging:

```yaml
# docker-compose.yml
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

## Azure Storage Configuration

### Local Development with Azurite

For local development, use Azurite to emulate Azure Storage:

```yaml
# docker-compose.yml
azurite:
  image: mcr.microsoft.com/azure-storage/azurite
  ports:
    - "10000:10000"  # Blob service
    - "10001:10001"  # Queue service
    - "10002:10002"  # Table service
  volumes:
    - azurite-data:/data
  healthcheck:
    test: ["CMD", "nc", "-z", "localhost", "10000"]
    interval: 5s
    timeout: 3s
    retries: 5
```

### Production Configuration

For production, use a real Azure Storage account:

1. Create an Azure Storage account
2. Create a container named `timescaledb-archive`
3. Generate a connection string or use managed identity
4. Configure the connection string in both services

## Deployment Steps

### 1. Update Docker Compose

Ensure your `docker-compose.yml` includes all required services:

```yaml
version: '3.8'

services:
  database_service:
    build: ./services/backend_services/database_service
    environment:
      - REDIS_URL=redis://redis:6379
      - TIMESCALEDB_URL=postgresql://postgres:postgres@timescaledb:5432/postgres
      - RETENTION_PERIOD_DAYS=730
      - LAKEHOUSE_STORAGE_ACCOUNT=yourstorageaccount
      - LAKEHOUSE_CONTAINER=timescaledb-archive
    depends_on:
      - redis
      - timescaledb
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 10s
      timeout: 5s
      retries: 5

  archival_service:
    build: ./services/backend_services/archival_service
    environment:
      - REDIS_URL=redis://redis:6379
      - TIMESCALEDB_URL=postgresql://postgres:postgres@timescaledb:5432/postgres
      - AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://azurite:10000/devstoreaccount1;
      - AZURE_STORAGE_ACCOUNT_NAME=devstoreaccount1
      - AZURE_STORAGE_CONTAINER=timescaledb-archive
    depends_on:
      - redis
      - timescaledb
      - azurite
    ports:
      - "8080:8080"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 10s
      timeout: 5s
      retries: 5

  timescaledb:
    image: timescale/timescaledb:latest-pg14
    environment:
      - POSTGRES_PASSWORD=postgres
    ports:
      - "5432:5432"
    volumes:
      - timescaledb-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

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

  azurite:
    image: mcr.microsoft.com/azure-storage/azurite
    ports:
      - "10000:10000"
      - "10001:10001"
      - "10002:10002"
    volumes:
      - azurite-data:/data

volumes:
  timescaledb-data:
  redis-data:
  azurite-data:
```

### 2. Build and Deploy

Deploy the services using Docker Compose:

```powershell
docker-compose build
docker-compose up -d
```

### 3. Verify Deployment

Check that all services are running:

```powershell
docker-compose ps
```

## Verification and Testing

### 1. Run the Test Script

The test script simulates the archival workflow:

```powershell
python tests/test_archival_workflow.py
```

### 2. Check API Endpoints

Verify the API endpoints are working:

```powershell
# Check Database Service health
Invoke-RestMethod -Uri "http://localhost:8000/health"

# Check Archival Service health
Invoke-RestMethod -Uri "http://localhost:8080/health"

# Check retention status
Invoke-RestMethod -Uri "http://localhost:8000/database/retention/status"
```

### 3. Verify Lakehouse Storage

Check that data is being written to the lakehouse:

```powershell
# For local Azurite
$env:AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://localhost:10000/devstoreaccount1;"
az storage blob list --container-name timescaledb-archive --output table
```

## Monitoring and Maintenance

### 1. Monitor Archival Metrics

Check archival metrics regularly:

```powershell
# Get archival metrics
Invoke-RestMethod -Uri "http://localhost:8080/archival/metrics"
```

### 2. Check Retention Status

Monitor retention status to ensure chunks are being archived:

```powershell
# Get retention status
Invoke-RestMethod -Uri "http://localhost:8000/database/retention/status"
```

### 3. Set Up Alerts

Configure alerts for:

- Failed archival events
- High chunk counts awaiting archival
- Storage capacity issues
- Redis connection problems

### 4. Regular Maintenance

Perform these maintenance tasks:

- Review archival logs weekly
- Validate lakehouse storage organization monthly
- Test the recovery process quarterly
- Update service configurations as needed

## Troubleshooting

### Common Issues and Solutions

#### 1. Archival Events Not Being Processed

**Symptoms:**
- Chunks older than retention period remain in TimescaleDB
- No archival events in Redis

**Solutions:**
- Check Redis connectivity from Database Service
- Verify retention manager is running
- Check retention period configuration
- Manually trigger archival via API

#### 2. Archival Confirmations Not Received

**Symptoms:**
- Archival events are published but chunks aren't dropped
- No confirmation events in Redis

**Solutions:**
- Check Redis connectivity from Archival Service
- Verify subscription to confirmation topic
- Check for errors in Archival Service logs

#### 3. Data Extraction Failures

**Symptoms:**
- Failed archival confirmations with database errors
- Timeout errors in Archival Service logs

**Solutions:**
- Increase query timeout settings
- Reduce batch size for large chunks
- Check TimescaleDB connection from Archival Service

#### 4. Lakehouse Storage Issues

**Symptoms:**
- Failed archival confirmations with storage errors
- Permission denied errors

**Solutions:**
- Verify storage connection string
- Check container existence and permissions
- For Azurite, ensure service is running and accessible

#### 5. Performance Issues

**Symptoms:**
- Slow archival processing
- Growing backlog of chunks to archive

**Solutions:**
- Increase concurrent archival tasks
- Optimize data extraction queries
- Consider scaling Archival Service horizontally
- Adjust chunk interval in TimescaleDB for more manageable sizes
