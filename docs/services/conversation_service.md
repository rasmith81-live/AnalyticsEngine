# Conversation Service

## Overview

No overview provided.

## Data Models

### `Utterance`



**Fields:**

- `id`: `str`
- `session_id`: `str`
- `sender`: `SenderType`
- `content`: `str`
- `timestamp`: `datetime`
- `metadata`: `Optional[Dict[str, Any]]`

### `BusinessIntent`



**Fields:**

- `name`: `str`
- `confidence`: `float`
- `parameters`: `Dict[str, Any]`
- `description`: `Optional[str]`
- `domain`: `str`
- `target_entities`: `List[str]`
- `requested_metrics`: `List[str]`

### `InterviewSession`



**Fields:**

- `id`: `str`
- `user_id`: `str`
- `start_time`: `datetime`
- `last_activity`: `datetime`
- `status`: `str`
- `context`: `Dict[str, Any]`
- `intents_identified`: `List[BusinessIntent]`

### `ValueChainNode`



**Fields:**

- `id`: `str`
- `name`: `str`
- `type`: `str`
- `description`: `Optional[str]`
- `properties`: `Dict[str, Any]`

### `ValueChainLink`



**Fields:**

- `source_id`: `str`
- `target_id`: `str`
- `type`: `str`

### `CompanyValueChainModel`



**Fields:**

- `id`: `str`
- `name`: `str`
- `nodes`: `List[ValueChainNode]`
- `links`: `List[ValueChainLink]`
- `created_at`: `datetime`
- `updated_at`: `datetime`
- `version`: `str`

### `ChatRequest`



**Fields:**

- `session_id`: `Optional[str]`
- `user_id`: `str`
- `message`: `str`
- `skip_response`: `bool`

### `ChatResponse`



**Fields:**

- `session_id`: `str`
- `message`: `str`
- `intents`: `List[BusinessIntent]`

### `MapDefinitionRequest`



**Fields:**

- `definition`: `str`

### `RecommendStrategyRequest`



**Fields:**

- `business_description`: `str`
- `use_cases`: `List[str]`

