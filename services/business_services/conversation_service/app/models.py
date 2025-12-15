
from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class SenderType(str, Enum):
    USER = "user"
    BOT = "bot"
    SYSTEM = "system"

class Utterance(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    session_id: str
    sender: SenderType
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    metadata: Optional[Dict[str, Any]] = None

class BusinessIntent(BaseModel):
    name: str
    confidence: float
    parameters: Dict[str, Any] = {}
    description: Optional[str] = None

class InterviewSession(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str
    start_time: datetime = Field(default_factory=datetime.utcnow)
    last_activity: datetime = Field(default_factory=datetime.utcnow)
    status: str = "active"
    context: Dict[str, Any] = {}
    intents_identified: List[BusinessIntent] = []

class ValueChainNode(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    type: str  # e.g., "Process", "Activity", "Metric"
    description: Optional[str] = None
    properties: Dict[str, Any] = {}

class ValueChainLink(BaseModel):
    source_id: str
    target_id: str
    type: str  # e.g., "feeds", "measures", "consists_of"

class CompanyValueChainModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    nodes: List[ValueChainNode] = []
    links: List[ValueChainLink] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    version: str = "1.0"

class ChatRequest(BaseModel):
    session_id: Optional[str] = None
    user_id: str
    message: str

class ChatResponse(BaseModel):
    session_id: str
    message: str
    intents: List[BusinessIntent] = []
