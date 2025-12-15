
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
