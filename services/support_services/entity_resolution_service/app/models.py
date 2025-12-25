
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class EntityType(BaseModel):
    """Definition of an entity type (e.g., 'Customer', 'Product')."""
    name: str
    attributes: List[str]

class EntityRecord(BaseModel):
    """A single record representing an entity from a specific source."""
    record_id: str
    source_system: str
    entity_type: str
    attributes: Dict[str, Any]
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class MatchCandidate(BaseModel):
    """A potential match found by the engine."""
    record: EntityRecord
    score: float
    match_confidence: str # 'HIGH', 'MEDIUM', 'LOW'

class ResolutionResult(BaseModel):
    """Result of an entity resolution request."""
    source_record: EntityRecord
    matches: List[MatchCandidate]
    resolution_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    processing_time_ms: float

class GoldenRecord(BaseModel):
    """The consolidated 'Golden Record' for an entity."""
    entity_id: str
    entity_type: str
    attributes: Dict[str, Any]
    lineage: List[str] # List of source record IDs
    last_updated: datetime


class SemanticExtractionRequest(BaseModel):
    """Request for NLP-based semantic entity extraction from text."""
    text: str = Field(..., description="Text to extract entities from")
    name: Optional[str] = Field(None, description="KPI/item name for context")
    description: Optional[str] = Field(None, description="KPI/item description")
    formula: Optional[str] = Field(None, description="Optional formula to parse")
    source_file: Optional[str] = Field(None, description="Source file name for context")


class ExtractedEntity(BaseModel):
    """An entity extracted via NLP semantic analysis."""
    text: str = Field(..., description="Original text of the entity")
    lemma: str = Field(..., description="Lemmatized/normalized form")
    entity_type: Optional[str] = Field(None, description="Classified entity type if matched")
    confidence: float = Field(default=1.0, description="Confidence score 0-1")
    pos_tag: Optional[str] = Field(None, description="Part-of-speech tag")


class SemanticExtractionResponse(BaseModel):
    """Response from NLP-based semantic entity extraction."""
    entities: List[ExtractedEntity] = Field(default_factory=list, description="Extracted entities")
    domain: Optional[str] = Field(None, description="Inferred business domain")
    domain_confidence: float = Field(default=0.0, description="Domain inference confidence")
    module: Optional[str] = Field(None, description="Inferred module/category")
    noun_phrases: List[str] = Field(default_factory=list, description="All extracted noun phrases")
    processing_time_ms: float = Field(default=0.0, description="Processing time in milliseconds")


class ItemEvent(BaseModel):
    """Event model for item domain events."""
    event_type: str = Field(..., description="Type of event")
    item_id: str = Field(..., description="Item identifier")
    payload: Dict[str, Any] = Field(default_factory=dict, description="Event payload")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    correlation_id: Optional[str] = Field(None, description="Correlation ID for tracing")


class DataModel(BaseModel):
    """Generic data model for service requests."""
    data: Dict[str, Any] = Field(default_factory=dict)
    metadata: Optional[Dict[str, Any]] = Field(None)


class CommandModel(BaseModel):
    """Command model for service operations."""
    command: str = Field(..., description="Command name")
    payload: Dict[str, Any] = Field(default_factory=dict)
    correlation_id: Optional[str] = Field(None)


class ResponseModel(BaseModel):
    """Generic response model."""
    success: bool = Field(default=True)
    message: Optional[str] = Field(None)
    data: Optional[Dict[str, Any]] = Field(None)
    error: Optional[str] = Field(None)


class IntentExtractionRequest(BaseModel):
    """Request for LLM-based business intent extraction."""
    text: str = Field(..., description="Text to extract intent from (KPI name, description, user query)")
    context: Optional[List[str]] = Field(default_factory=list, description="Additional context strings")
    source_file: Optional[str] = Field(None, description="Source file name for context")


class BusinessIntent(BaseModel):
    """Structured business intent extracted via LLM."""
    domain: str = Field(..., description="Business domain (e.g., supply_chain, sales, sustainability)")
    domain_confidence: float = Field(default=0.8, description="Confidence score 0-1")
    target_entities: List[str] = Field(default_factory=list, description="Identified business entities")
    action: Optional[str] = Field(None, description="Intended action (monitor, optimize, predict, measure)")
    metrics: List[str] = Field(default_factory=list, description="Identified metrics/KPIs")
    time_horizon: Optional[str] = Field(None, description="Time context (real_time, historical, forecast)")
    is_new_domain: bool = Field(default=False, description="True if domain doesn't exist in BMS")


class IntentExtractionResponse(BaseModel):
    """Response from LLM-based intent extraction."""
    intent: BusinessIntent = Field(..., description="Extracted business intent")
    raw_entities: List[ExtractedEntity] = Field(default_factory=list, description="NLP-extracted entities")
    noun_phrases: List[str] = Field(default_factory=list, description="Extracted noun phrases")
    processing_time_ms: float = Field(default=0.0, description="Processing time")
