# TimescaleDB Data Archival Solution

## Overview

This document describes the event-driven data archival solution for TimescaleDB implemented in the multi-microservice architecture. The solution maintains only 2 years of data in TimescaleDB for optimal query performance while streaming older data to a lakehouse storage system (Azure Data Lake Storage Gen2) via Redis messaging.

## Architecture

![TimescaleDB Archival Architecture](./images/archival_architecture.png)

### Components

1. **Database Service**
   - Manages TimescaleDB data retention
   - Identifies chunks older than the retention period (2 years)
   - Publishes archival events via Redis
   - Drops chunks only after confirmed archival

2. **Archival Service**
   - Subscribes to archival events
   - Extracts data from TimescaleDB chunks
   - Writes data to lakehouse storage in Parquet format
   - Publishes archival confirmation events

3. **Redis Messaging**
   - Event-driven communication between services
   - Pub/sub for archival events and confirmations
   - Asynchronous processing

4. **Lakehouse Storage (Azure Data Lake Storage Gen2)**
   - Long-term storage for archived data
   - Cost-effective for historical data
   - Accessible for occasional analytics

## Event Flow

1. **Retention Check**
   - RetentionManager periodically identifies chunks older than 2 years
   - Creates `ArchivalEvent` for each chunk

2. **Archival Request**
   - Database Service publishes event to `database.archival.request` topic
   - Event contains chunk details (ID, table, time range)

3. **Data Extraction & Storage**
   - Archival Service subscribes to request topic
   - Extracts data from specified chunk
   - Writes data to lakehouse in Parquet format

4. **Archival Confirmation**
   - Archival Service publishes confirmation to `database.archival.confirmation` topic
   - Confirmation includes status (success/failure)

5. **Chunk Removal**
   - Database Service receives confirmation
   - If successful, drops the TimescaleDB chunk
   - If failed, logs error and retains chunk

## Benefits

- **Real-time Processing**: Event-driven architecture eliminates batch ETL jobs
- **Cost Optimization**: Keeps only 2 years of data in TimescaleDB
- **Performance**: Maintains optimal query performance for recent data
- **Data Integrity**: Two-phase process ensures data is archived before removal
- **Scalability**: Microservices can scale independently

## Configuration

### Database Service

```yaml
# Data Retention and Archival Configuration
retention_period_days: 730  # 2 years
retention_check_interval_hours: 24
archival_batch_size: 10
lakehouse_enabled: true
```

### Archival Service

```yaml
# Lakehouse Configuration
lakehouse_storage_account: "your_storage_account"
lakehouse_container: "timescaledb-archive"
lakehouse_connection_string: "your_connection_string"
```

## API Endpoints

### Database Service

- `GET /database/retention/status` - Get retention status for all hypertables
- `POST /database/retention/trigger-archival` - Manually trigger archival process

### Archival Service

- `GET /archival/status` - Get archival service status
- `GET /archival/events` - List recent archival events
- `GET /archival/metrics` - Get archival metrics

## Implementation Details

### RetentionManager

The RetentionManager in the Database Service:
- Uses SQL to identify chunks older than retention period
- Tracks archival events and their status
- Implements retry logic for failed archival attempts
- Provides metrics on archival operations

### Lakehouse Client

The LakehouseClient in the Archival Service:
- Handles Azure Data Lake Storage Gen2 connectivity
- Implements Parquet file writing for efficient storage
- Supports directory structure based on table/time
- Provides connection testing and file listing

## Testing

Run the archival workflow test to validate the system:

```powershell
python tests/test_archival_workflow.py
```

This test simulates:
1. Database Service identifying an old chunk
2. Publishing an archival event
3. Archival Service processing the event
4. Writing to lakehouse storage
5. Publishing confirmation
6. Database Service processing confirmation

## Monitoring

Monitor the archival process through:
- Service logs
- Archival metrics endpoints
- Redis pub/sub monitoring
- Azure Storage metrics

## Best Practices

1. **Sizing**: Configure retention period based on query patterns and storage costs
2. **Partitioning**: Use appropriate chunk intervals for efficient archival
3. **Testing**: Validate archival process with sample data before production
4. **Monitoring**: Set up alerts for failed archival events
5. **Recovery**: Implement procedures for restoring archived data if needed
