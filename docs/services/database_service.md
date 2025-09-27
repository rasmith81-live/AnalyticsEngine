# Database Service

## Overview

Database Service - Centralized database operations for TimescaleDB with CQRS support.

This service consolidates all database functionality:
- Database connection management
- Automated migration execution
- TimescaleDB hypertable operations
- CQRS pattern enforcement
- Schema validation and discovery

## Data Models

### `QueryRequest`

Request model for database queries.

**Fields:**

- `query`: `str`
- `parameters`: `Optional[Dict[str, Any]]`
- `service_name`: `str`
- `timeout`: `Optional[int]`
- `use_cache`: `bool`

### `CommandRequest`

Request model for database commands.

**Fields:**

- `command`: `str`
- `parameters`: `Optional[Dict[str, Any]]`
- `service_name`: `str`
- `transaction_id`: `Optional[str]`
- `timeout`: `Optional[int]`

### `MigrationRequest`

Request model for migration execution.

**Fields:**

- `service_name`: `str`
- `target_revision`: `Optional[str]`
- `auto_rollback`: `bool`
- `validation_level`: `str`
- `run_in_background`: `bool`

### `HypertableRequest`

Request model for TimescaleDB hypertable creation.

**Fields:**

- `table_name`: `str`
- `time_column`: `str`
- `chunk_interval`: `Optional[str]`
- `compression_enabled`: `bool`
- `retention_period`: `Optional[str]`

### `ModelRegistrationRequest`

Request model for model registration.

**Fields:**

- `service_name`: `str`
- `models`: `List[Dict[str, Any]]`
- `auto_create_tables`: `bool`

### `QueryResponse`

Response model for database queries.

**Fields:**

- `success`: `bool`
- `data`: `Optional[Dict[str, Any]]`
- `execution_time`: `float`
- `row_count`: `int`
- `cache_hit`: `bool`
- `error_message`: `Optional[str]`

### `CommandResponse`

Response model for database commands.

**Fields:**

- `success`: `bool`
- `transaction_id`: `Optional[str]`
- `affected_rows`: `int`
- `execution_time`: `float`
- `error_message`: `Optional[str]`

### `ValidationIssue`

Validation issue model.

**Fields:**

- `severity`: `str`
- `category`: `str`
- `description`: `str`
- `location`: `str`
- `suggestion`: `Optional[str]`
- `timestamp`: `datetime`

### `MigrationResponse`

Response model for migration execution.

**Fields:**

- `success`: `bool`
- `service_name`: `str`
- `phases_completed`: `List[str]`
- `hypertables_created`: `List[str]`
- `validation_issues`: `List[Dict[str, Any]]`
- `error_message`: `Optional[str]`
- `rollback_performed`: `bool`
- `execution_time`: `Optional[float]`
- `message`: `Optional[str]`

### `HypertableResponse`

Response model for hypertable operations.

**Fields:**

- `success`: `bool`
- `table_name`: `str`
- `hypertable_created`: `bool`
- `chunk_interval`: `Optional[str]`
- `compression_policy`: `Optional[Dict[str, Any]]`
- `retention_policy`: `Optional[Dict[str, Any]]`
- `error_message`: `Optional[str]`

### `ModelInfo`

Model information.

**Fields:**

- `name`: `str`
- `table_name`: `str`
- `fields`: `Dict[str, str]`
- `relationships`: `List[str]`
- `is_hypertable`: `bool`
- `time_column`: `Optional[str]`
- `source_file`: `str`

### `ModelDiscoveryResponse`

Response model for model discovery.

**Fields:**

- `service_name`: `str`
- `models`: `List[ModelInfo]`
- `discovery_time`: `datetime`

### `HealthResponse`

Health check response model.

**Fields:**

- `status`: `str`
- `database_connected`: `bool`
- `timescaledb_available`: `bool`
- `connection_pool_status`: `Dict[str, Any]`
- `active_connections`: `int`
- `timestamp`: `datetime`

### `DatabaseConnection`

Database connection configuration.

**Fields:**

- `service_name`: `str`
- `database_url`: `str`
- `pool_size`: `int`
- `max_overflow`: `int`
- `pool_timeout`: `int`
- `pool_recycle`: `int`

### `TransactionContext`

Transaction context for command execution.

**Fields:**

- `transaction_id`: `str`
- `service_name`: `str`
- `started_at`: `datetime`
- `commands_executed`: `int`
- `is_active`: `bool`

### `CommandBase`

Base class for CQRS commands.

**Fields:**

- `command_id`: `str`
- `service_name`: `str`
- `timestamp`: `datetime`
- `correlation_id`: `Optional[str]`

### `QueryBase`

Base class for CQRS queries.

**Fields:**

- `query_id`: `str`
- `service_name`: `str`
- `timestamp`: `datetime`
- `correlation_id`: `Optional[str]`

### `ReadModelBase`

Base class for CQRS read models.

**Fields:**

- `id`: `int`
- `uuid`: `str`
- `created_at`: `datetime`
- `updated_at`: `datetime`
- `version`: `int`

### `RetentionPolicy`

TimescaleDB retention policy.

**Fields:**

- `enabled`: `bool`
- `retention_period_days`: `int`

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

### `HypertableInfo`

TimescaleDB hypertable information.

**Fields:**

- `table_name`: `str`
- `time_column`: `str`
- `chunk_interval`: `str`
- `compression_enabled`: `bool`
- `retention_period`: `Optional[str]`
- `created_at`: `datetime`
- `last_chunk_created`: `Optional[datetime]`

### `ChunkInfo`

TimescaleDB chunk information.

**Fields:**

- `chunk_name`: `str`
- `table_name`: `str`
- `range_start`: `datetime`
- `range_end`: `datetime`
- `compressed`: `bool`
- `size_bytes`: `int`

### `ContinuousAggregateInfo`

TimescaleDB continuous aggregate information.

**Fields:**

- `view_name`: `str`
- `source_table`: `str`
- `refresh_policy`: `Optional[Dict[str, Any]]`
- `materialized`: `bool`
- `created_at`: `datetime`

### `MigrationInfo`

Migration information.

**Fields:**

- `revision`: `str`
- `service_name`: `str`
- `description`: `str`
- `applied_at`: `Optional[datetime]`
- `is_current`: `bool`

### `SchemaValidationResult`

Schema validation result.

**Fields:**

- `is_valid`: `bool`
- `issues`: `List[ValidationIssue]`
- `validated_at`: `datetime`
- `validation_level`: `str`

### `PerformanceStats`

Database performance statistics.

**Fields:**

- `total_queries`: `int`
- `total_commands`: `int`
- `avg_query_time`: `float`
- `avg_command_time`: `float`
- `cache_hit_rate`: `float`
- `active_connections`: `int`
- `total_connections`: `int`
- `timestamp`: `datetime`

### `ConnectionPoolStatus`

Connection pool status.

**Fields:**

- `size`: `int`
- `checked_in`: `int`
- `checked_out`: `int`
- `overflow`: `int`
- `invalid`: `int`
- `total_created`: `int`

