# Machine Learning Service

## Overview

Machine Learning Service - Manages ML Models, Training Jobs, and Inference.

This service:
- Uses Database Service for metadata persistence (via messaging/CQRS pattern)
- Uses Messaging Service for event publishing (Training Jobs)
- Exposes API for Model Registry and Inference

## Data Models

### `EventCallback`

Event callback model for messaging.

**Fields:**

- `event_type`: `str`
- `payload`: `Dict[str, Any]`
- `timestamp`: `Optional[datetime]`

### `MLModelBase`

Base model for ML Model definition.

**Fields:**

- `name`: `str`
- `description`: `Optional[str]`
- `type`: `ModelType`
- `metadata`: `Dict[str, Any]`

### `ModelVersionBase`

Base model for a specific version of a model.

**Fields:**

- `version`: `str`
- `status`: `ModelStatus`
- `hyperparameters`: `Dict[str, Any]`
- `metrics`: `Dict[str, float]`
- `artifact_url`: `Optional[str]`

### `TrainingJobBase`

Base model for a training job.

**Fields:**

- `model_id`: `str`
- `dataset_id`: `str`
- `hyperparameters`: `Dict[str, Any]`

### `InferenceRequest`

Request for model inference.

**Fields:**

- `model_id`: `str`
- `version`: `Optional[str]`
- `features`: `Union[List[Dict[str, Any]], Dict[str, Any]]`

### `PredictionResult`

Single prediction result.

**Fields:**

- `prediction`: `Any`
- `probability`: `Optional[float]`
- `explanation`: `Optional[Dict[str, float]]`

### `InferenceResponse`

Response from inference endpoint.

**Fields:**

- `model_id`: `str`
- `version`: `str`
- `results`: `List[PredictionResult]`
- `inference_time_ms`: `float`

### `DependencyStatus`

Dependency status model.

**Fields:**

- `service_name`: `str`
- `url`: `str`
- `status`: `str`
- `response_time_ms`: `float`
- `last_check`: `datetime`
- `error`: `Optional[str]`

### `ServiceHealth`

Service health status model.

**Fields:**

- `status`: `str`
- `timestamp`: `datetime`
- `dependencies`: `List[DependencyStatus]`
- `active_subscriptions`: `int`
- `uptime_seconds`: `float`
- `version`: `str`
- `error`: `Optional[str]`

### `ErrorResponse`

Error response model.

**Fields:**

- `error`: `str`
- `error_code`: `Optional[str]`
- `timestamp`: `datetime`
- `request_id`: `Optional[str]`
- `details`: `Optional[Dict[str, Any]]`

### `ValidationError`

Validation error model.

**Fields:**

- `field`: `str`
- `message`: `str`
- `value`: `Any`

