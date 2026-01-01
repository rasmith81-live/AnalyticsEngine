"""
Pydantic models for Client Configuration API.

These models are used for API requests/responses and are separate from
the SQLAlchemy database models.
"""

from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
import uuid


# ============================================================================
# Request Models
# ============================================================================

class CreateClientConfigurationRequest(BaseModel):
    """Request to create a new client configuration."""
    client_id: str = Field(..., description="Unique client identifier")
    client_name: str = Field(..., description="Client display name")
    name: str = Field(..., description="Configuration name")
    description: Optional[str] = Field(None, description="Configuration description")
    source_session_id: Optional[str] = Field(None, description="Source conversation session ID")


class UpdateClientConfigurationRequest(BaseModel):
    """Request to update a client configuration."""
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None  # draft, active, archived
    version: Optional[str] = None


class SaveRecordingRequest(BaseModel):
    """Request to save a conversation recording."""
    session_id: str = Field(..., description="Session ID of the recording")
    transcript: str = Field(..., description="Full transcript text")
    duration_seconds: Optional[float] = Field(None, description="Recording duration")
    speaker_count: Optional[int] = Field(None, description="Number of speakers")
    recorded_at: datetime = Field(default_factory=datetime.utcnow)
    segments: Optional[List[Dict[str, Any]]] = Field(None, description="Transcript segments with timestamps")


class SaveIntentRequest(BaseModel):
    """Request to save a business intent."""
    name: str = Field(..., description="Intent name")
    description: Optional[str] = None
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    domain: str = Field(default="general")
    category: Optional[str] = None
    target_entities: Optional[List[str]] = None
    requested_metrics: Optional[List[str]] = None
    parameters: Optional[Dict[str, Any]] = None
    source_utterance: Optional[str] = None


class SaveEntityRequest(BaseModel):
    """Request to save a business entity."""
    name: str = Field(..., description="Entity name")
    entity_type: str = Field(..., description="Entity type (Process, Activity, Metric, Object)")
    description: Optional[str] = None
    properties: Optional[Dict[str, Any]] = None
    related_entities: Optional[Dict[str, Any]] = None
    extraction_confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    source_context: Optional[str] = None


class ValueChainNodeRequest(BaseModel):
    """Value chain node for model creation."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    type: str  # Process, Activity, Metric, Entity
    description: Optional[str] = None
    properties: Optional[Dict[str, Any]] = None


class ValueChainLinkRequest(BaseModel):
    """Value chain link for model creation."""
    source_id: str
    target_id: str
    type: str  # feeds, measures, consists_of


class SaveValueChainModelRequest(BaseModel):
    """Request to save a value chain model."""
    name: str = Field(..., description="Model name")
    description: Optional[str] = None
    version: str = Field(default="1.0")
    nodes: List[ValueChainNodeRequest] = Field(default_factory=list)
    links: List[ValueChainLinkRequest] = Field(default_factory=list)
    generated_from_session: Optional[str] = None
    generation_method: str = Field(default="llm")


class SaveFullConfigurationRequest(BaseModel):
    """Request to save a complete configuration with all components."""
    configuration: CreateClientConfigurationRequest
    recordings: Optional[List[SaveRecordingRequest]] = None
    intents: Optional[List[SaveIntentRequest]] = None
    entities: Optional[List[SaveEntityRequest]] = None
    value_chain_model: Optional[SaveValueChainModelRequest] = None


# ============================================================================
# Response Models
# ============================================================================

class ClientConfigurationResponse(BaseModel):
    """Response model for client configuration."""
    id: int
    uuid: str
    client_id: str
    client_name: str
    name: str
    description: Optional[str]
    version: str
    status: str
    source_session_id: Optional[str]
    created_at: datetime
    updated_at: datetime
    
    # Counts for related items
    recording_count: int = 0
    intent_count: int = 0
    entity_count: int = 0
    model_count: int = 0
    
    model_config = {"from_attributes": True}


class ClientRecordingResponse(BaseModel):
    """Response model for client recording."""
    id: int
    uuid: str
    configuration_id: int
    session_id: str
    transcript: str
    duration_seconds: Optional[float]
    speaker_count: Optional[int]
    recorded_at: datetime
    segments: Optional[List[Dict[str, Any]]]
    created_at: datetime
    updated_at: datetime
    
    model_config = {"from_attributes": True}


class ClientIntentResponse(BaseModel):
    """Response model for client intent."""
    id: int
    uuid: str
    configuration_id: int
    name: str
    description: Optional[str]
    confidence: float
    domain: str
    category: Optional[str]
    target_entities: Optional[List[str]]
    requested_metrics: Optional[List[str]]
    parameters: Optional[Dict[str, Any]]
    source_utterance: Optional[str]
    created_at: datetime
    updated_at: datetime
    
    model_config = {"from_attributes": True}


class ClientEntityResponse(BaseModel):
    """Response model for client entity."""
    id: int
    uuid: str
    configuration_id: int
    name: str
    entity_type: str
    description: Optional[str]
    properties: Optional[Dict[str, Any]]
    related_entities: Optional[Dict[str, Any]]
    extraction_confidence: float
    source_context: Optional[str]
    created_at: datetime
    updated_at: datetime
    
    model_config = {"from_attributes": True}


class ClientValueChainModelResponse(BaseModel):
    """Response model for client value chain model."""
    id: int
    uuid: str
    configuration_id: int
    name: str
    description: Optional[str]
    version: str
    nodes: List[Dict[str, Any]]
    links: List[Dict[str, Any]]
    is_active: bool
    generated_from_session: Optional[str]
    generation_method: str
    created_at: datetime
    updated_at: datetime
    
    model_config = {"from_attributes": True}


class FullClientConfigurationResponse(BaseModel):
    """Response model for complete client configuration with all components."""
    configuration: ClientConfigurationResponse
    recordings: List[ClientRecordingResponse] = []
    intents: List[ClientIntentResponse] = []
    entities: List[ClientEntityResponse] = []
    value_chain_models: List[ClientValueChainModelResponse] = []


class ClientConfigurationListResponse(BaseModel):
    """Response model for listing client configurations."""
    items: List[ClientConfigurationResponse]
    total: int
    page: int
    page_size: int
