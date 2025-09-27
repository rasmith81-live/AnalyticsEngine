# Archival Service

## Overview

Archival Service - Main Application

This service subscribes to archival events from the Database Service via Redis,
processes data archival requests, and stores data in a lakehouse format.

## Data Models

### `ArchivalEvent`

Event model for data archival requests.

**Fields:**

- `event_id`: `str`
- `table_name`: `str`
- `chunks`: `List[Dict[str, Any]]`
- `status`: `ArchivalStatus`
- `created_at`: `datetime`
- `error_message`: `Optional[str]`

### `ArchivalConfirmation`

Confirmation model for completed archival operations.

**Fields:**

- `event_id`: `str`
- `status`: `ArchivalStatus`
- `completed_at`: `datetime`
- `lakehouse_path`: `Optional[str]`
- `error_message`: `Optional[str]`

### `ChunkInfo`

TimescaleDB chunk information.

**Fields:**

- `chunk_name`: `str`
- `chunk_id`: `int`
- `range_start`: `Optional[datetime]`
- `range_end`: `Optional[datetime]`

### `ArchivalMetrics`

Metrics for archival operations.

**Fields:**

- `total_events`: `int`
- `completed_events`: `int`
- `failed_events`: `int`
- `processing_events`: `int`
- `average_processing_time_seconds`: `float`
- `total_chunks_archived`: `int`
- `total_bytes_archived`: `int`
- `timestamp`: `datetime`

### `HealthResponse`

Health check response model.

**Fields:**

- `status`: `str`
- `messaging_connected`: `bool`
- `lakehouse_connected`: `bool`
- `active_archival_events`: `int`
- `timestamp`: `datetime`
- `monitoring_health`: `Optional[Dict[str, Any]]`
- `management_health`: `Optional[Dict[str, Any]]`

### `ArchivalQuery`

Query model for archived data.

**Fields:**

- `table_name`: `str`
- `time_range_start`: `Optional[datetime]`
- `time_range_end`: `Optional[datetime]`
- `filters`: `Optional[Dict[str, Any]]`
- `limit`: `int`

### `ArchivalQueryResult`

Result model for archived data queries.

**Fields:**

- `query`: `ArchivalQuery`
- `data_paths`: `List[str]`
- `record_count`: `int`
- `execution_time_seconds`: `float`
- `timestamp`: `datetime`

