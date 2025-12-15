# Entity Resolution Service

## Overview

No overview provided.

## Data Models

### `EntityType`

Definition of an entity type (e.g., 'Customer', 'Product').

**Fields:**

- `name`: `str`
- `attributes`: `List[str]`

### `EntityRecord`

A single record representing an entity from a specific source.

**Fields:**

- `record_id`: `str`
- `source_system`: `str`
- `entity_type`: `str`
- `attributes`: `Dict[str, Any]`
- `timestamp`: `datetime`

### `MatchCandidate`

A potential match found by the engine.

**Fields:**

- `record`: `EntityRecord`
- `score`: `float`
- `match_confidence`: `str`

### `ResolutionResult`

Result of an entity resolution request.

**Fields:**

- `source_record`: `EntityRecord`
- `matches`: `List[MatchCandidate]`
- `resolution_id`: `str`
- `processing_time_ms`: `float`

### `GoldenRecord`

The consolidated 'Golden Record' for an entity.

**Fields:**

- `entity_id`: `str`
- `entity_type`: `str`
- `attributes`: `Dict[str, Any]`
- `lineage`: `List[str]`
- `last_updated`: `datetime`

