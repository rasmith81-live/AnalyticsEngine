# Entity Resolution Service

## Overview

No overview provided.

## Data Models

### `SourceRecord`



**Fields:**

- `record_id`: `str`
- `source_system`: `str`
- `entity_type`: `str`
- `attributes`: `Dict[str, Any]`
- `timestamp`: `Optional[str]`

### `MatchCandidate`



**Fields:**

- `record_a_id`: `str`
- `record_b_id`: `str`
- `score`: `float`
- `match_reasons`: `List[str]`

### `GoldenRecord`



**Fields:**

- `golden_id`: `str`
- `entity_type`: `str`
- `attributes`: `Dict[str, Any]`
- `source_record_ids`: `List[str]`
- `lineage`: `List[Dict[str, Any]]`

