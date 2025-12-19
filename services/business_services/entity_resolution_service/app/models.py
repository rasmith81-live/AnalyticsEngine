
from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class SourceRecord(BaseModel):
    record_id: str
    source_system: str
    entity_type: str
    attributes: Dict[str, Any]
    timestamp: Optional[str] = None

class MatchCandidate(BaseModel):
    record_a_id: str
    record_b_id: str
    score: float
    match_reasons: List[str]

class GoldenRecord(BaseModel):
    golden_id: str
    entity_type: str
    attributes: Dict[str, Any]
    source_record_ids: List[str]
    lineage: List[Dict[str, Any]]
