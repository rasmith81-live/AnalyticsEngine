# Data Governance Service

## Overview

No overview provided.

## Data Models

### `DataQualityRule`

Definition of a data quality rule.

**Fields:**

- `id`: `str`
- `name`: `str`
- `description`: `Optional[str]`
- `rule_type`: `RuleType`
- `target_entity`: `str`
- `target_attribute`: `Optional[str]`
- `parameters`: `Dict[str, Any]`
- `severity`: `RuleSeverity`
- `is_active`: `bool`
- `created_at`: `datetime`
- `updated_at`: `datetime`

### `ValidationResult`

Result of a rule execution against a dataset or record.

**Fields:**

- `id`: `str`
- `rule_id`: `str`
- `entity_id`: `Optional[str]`
- `is_valid`: `bool`
- `error_message`: `Optional[str]`
- `timestamp`: `datetime`
- `metadata`: `Dict[str, Any]`

### `LineageNode`

A node in the data lineage graph.

**Fields:**

- `id`: `str`
- `name`: `str`
- `type`: `NodeType`
- `properties`: `Dict[str, Any]`

### `LineageEdge`

A directed edge representing data flow.

**Fields:**

- `source_id`: `str`
- `target_id`: `str`
- `type`: `str`
- `transformation_logic`: `Optional[str]`

### `LineageGraph`

Complete lineage graph structure.

**Fields:**

- `nodes`: `List[LineageNode]`
- `edges`: `List[LineageEdge]`

### `DependencyStatus`



**Fields:**

- `service_name`: `str`
- `url`: `str`
- `status`: `str`
- `response_time_ms`: `float`
- `last_check`: `datetime`
- `error`: `Optional[str]`

### `ServiceHealth`



**Fields:**

- `status`: `str`
- `timestamp`: `datetime`
- `dependencies`: `List[DependencyStatus]`
- `uptime_seconds`: `float`
- `version`: `str`
- `error`: `Optional[str]`

