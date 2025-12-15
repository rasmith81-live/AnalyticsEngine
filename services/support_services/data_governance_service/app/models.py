"""
Pydantic models for Data Governance Service.
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
import uuid

from pydantic import BaseModel, Field

# --- Data Quality Models ---

class RuleSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"

class RuleType(str, Enum):
    UNIQUENESS = "uniqueness"
    NON_NULL = "non_null"
    FORMAT = "format"
    RANGE = "range"
    CUSTOM = "custom"

class DataQualityRule(BaseModel):
    """Definition of a data quality rule."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str = Field(..., description="Human-readable name of the rule")
    description: Optional[str] = None
    rule_type: RuleType
    target_entity: str = Field(..., description="The entity (table/object) this rule applies to")
    target_attribute: Optional[str] = Field(None, description="The specific attribute (column) this rule applies to")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="Rule-specific parameters (e.g., min/max values)")
    severity: RuleSeverity = RuleSeverity.WARNING
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class ValidationResult(BaseModel):
    """Result of a rule execution against a dataset or record."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    rule_id: str
    entity_id: Optional[str] = Field(None, description="ID of the specific record checked, if applicable")
    is_valid: bool
    error_message: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    metadata: Dict[str, Any] = {}

# --- Lineage Models ---

class NodeType(str, Enum):
    SOURCE = "source"         # e.g., Database Table, API
    TRANSFORMATION = "transformation" # e.g., ETL Job, Calculation
    METRIC = "metric"         # e.g., KPI Definition
    DASHBOARD = "dashboard"   # e.g., UI View

class LineageNode(BaseModel):
    """A node in the data lineage graph."""
    id: str
    name: str
    type: NodeType
    properties: Dict[str, Any] = {}

class LineageEdge(BaseModel):
    """A directed edge representing data flow."""
    source_id: str
    target_id: str
    type: str = "flows_to"
    transformation_logic: Optional[str] = None

class LineageGraph(BaseModel):
    """Complete lineage graph structure."""
    nodes: List[LineageNode]
    edges: List[LineageEdge]

# --- System Models ---

class DependencyStatus(BaseModel):
    service_name: str
    url: str
    status: str
    response_time_ms: float
    last_check: datetime
    error: Optional[str] = None

class ServiceHealth(BaseModel):
    status: str
    timestamp: datetime
    dependencies: List[DependencyStatus]
    uptime_seconds: float
    version: str
    error: Optional[str] = None

