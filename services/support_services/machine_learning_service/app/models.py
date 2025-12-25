"""
Pydantic models for Machine Learning Service.
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field, validator


class ModelType(str, Enum):
    """Type of ML model."""
    CLASSIFICATION = "classification"
    REGRESSION = "regression"
    CLUSTERING = "clustering"
    TIME_SERIES = "time_series"
    NLP = "nlp"


class ModelStatus(str, Enum):
    """Status of a model version."""
    STAGING = "staging"
    PRODUCTION = "production"
    ARCHIVED = "archived"
    DEPRECATED = "deprecated"


class JobStatus(str, Enum):
    """Status of a training job."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


# Event Models

class EventCallback(BaseModel):
    """Event callback model for messaging."""
    event_type: str
    payload: Dict[str, Any]
    timestamp: Optional[datetime] = None


# Domain Models

class MLModelBase(BaseModel):
    """Base model for ML Model definition."""
    name: str = Field(..., description="Model name", min_length=1, max_length=255)
    description: Optional[str] = Field(None, description="Model description")
    type: ModelType = Field(..., description="Type of problem this model solves")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")


class MLModelCreate(MLModelBase):
    """Model creation payload."""
    pass


class MLModelResponse(MLModelBase):
    """Model response."""
    id: str = Field(..., description="Model UUID")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    latest_version: Optional[str] = Field(None, description="Latest version number")


class ModelVersionBase(BaseModel):
    """Base model for a specific version of a model."""
    version: str = Field(..., description="Version string (e.g. 1.0.0)")
    status: ModelStatus = Field(default=ModelStatus.STAGING, description="Deployment status")
    hyperparameters: Dict[str, Any] = Field(default_factory=dict, description="Training hyperparameters")
    metrics: Dict[str, float] = Field(default_factory=dict, description="Performance metrics (accuracy, etc)")
    artifact_url: Optional[str] = Field(None, description="URL/Path to the serialized model artifact")


class ModelVersionCreate(ModelVersionBase):
    """Payload to register a new version."""
    model_id: str = Field(..., description="Parent Model ID")


class ModelVersionResponse(ModelVersionBase):
    """Model version response."""
    id: str = Field(..., description="Version UUID")
    model_id: str = Field(..., description="Parent Model ID")
    created_at: datetime = Field(..., description="Creation timestamp")


class TrainingJobBase(BaseModel):
    """Base model for a training job."""
    model_id: str = Field(..., description="ID of the model to train")
    dataset_id: str = Field(..., description="ID of the training dataset")
    hyperparameters: Dict[str, Any] = Field(default_factory=dict, description="Overrides for default hyperparameters")


class TrainingJobCreate(TrainingJobBase):
    """Payload to launch a training job."""
    pass


class TrainingJobResponse(TrainingJobBase):
    """Training job response."""
    id: str = Field(..., description="Job UUID")
    status: JobStatus = Field(..., description="Current status")
    progress: int = Field(default=0, ge=0, le=100, description="Progress percentage")
    started_at: datetime = Field(..., description="Start timestamp")
    finished_at: Optional[datetime] = Field(None, description="Completion timestamp")
    error: Optional[str] = Field(None, description="Error message if failed")
    resulting_version_id: Optional[str] = Field(None, description="ID of the created model version if successful")


# Inference Models

class InferenceRequest(BaseModel):
    """Request for model inference."""
    model_id: str = Field(..., description="Model ID to predict with")
    version: Optional[str] = Field(None, description="Specific version to use (default: production)")
    features: Union[List[Dict[str, Any]], Dict[str, Any]] = Field(..., description="Input features (single dict or list of dicts)")


class PredictionResult(BaseModel):
    """Single prediction result."""
    prediction: Any = Field(..., description="The predicted value/class")
    probability: Optional[float] = Field(None, description="Confidence score/probability")
    explanation: Optional[Dict[str, float]] = Field(None, description="Feature attribution/explanation")


class InferenceResponse(BaseModel):
    """Response from inference endpoint."""
    model_id: str = Field(..., description="Model ID used")
    version: str = Field(..., description="Model version used")
    results: List[PredictionResult] = Field(..., description="List of predictions")
    inference_time_ms: float = Field(..., description="Time taken to compute predictions")


# Health and Status Models (kept from template)

class DependencyStatus(BaseModel):
    """Dependency status model."""
    service_name: str = Field(..., description="Dependency service name")
    url: str = Field(..., description="Service URL")
    status: str = Field(..., description="Connection status")
    response_time_ms: float = Field(..., description="Response time in milliseconds")
    last_check: datetime = Field(..., description="Last health check timestamp")
    error: Optional[str] = Field(None, description="Error message if unhealthy")


class ServiceHealth(BaseModel):
    """Service health status model."""
    status: str = Field(..., description="Service status")
    timestamp: datetime = Field(..., description="Health check timestamp")
    dependencies: List[DependencyStatus] = Field(..., description="List of dependency statuses")
    active_subscriptions: int = Field(..., description="Number of active event subscriptions")
    uptime_seconds: float = Field(..., description="Service uptime in seconds")
    version: str = Field(..., description="Service version")
    error: Optional[str] = Field(None, description="Error message if unhealthy")


# Error Models (kept from template)

class ErrorResponse(BaseModel):
    """Error response model."""
    error: str = Field(..., description="Error message")
    error_code: Optional[str] = Field(None, description="Error code")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Error timestamp")
    request_id: Optional[str] = Field(None, description="Request ID for tracking")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional error details")


class ValidationError(BaseModel):
    """Validation error model."""
    field: str = Field(..., description="Field with validation error")
    message: str = Field(..., description="Validation error message")
    value: Any = Field(None, description="Invalid value")


class ValidationErrorResponse(ErrorResponse):
    """Validation error response model."""
    validation_errors: List[ValidationError] = Field(..., description="List of validation errors")
