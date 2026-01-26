"""
Pydantic models for Knowledge Graph MCP Server.

The Knowledge Graph stores ontology information (value chains, modules, KPIs, entities)
and their relationships in TimescaleDB, providing graph-like traversal capabilities.
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID
from enum import Enum


class EntityType(str, Enum):
    """Types of entities in the knowledge graph."""
    VALUE_CHAIN = "value_chain"
    MODULE = "module"
    KPI = "kpi"
    ENTITY = "entity"
    PROCESS = "process"
    ACTIVITY = "activity"
    ACTOR = "actor"
    DATA_SOURCE = "data_source"
    BOUNDED_CONTEXT = "bounded_context"
    RELATIONSHIP = "relationship"


class RelationType(str, Enum):
    """Types of relationships between entities."""
    BELONGS_TO = "belongs_to"
    CONTAINS = "contains"
    USES = "uses"
    FLOWS_TO = "flows_to"
    DEPENDS_ON = "depends_on"
    PRODUCES = "produces"
    CONSUMES = "consumes"
    CALCULATES = "calculates"
    REFERENCES = "references"


class KnowledgeNode(BaseModel):
    """A node in the knowledge graph."""
    id: Optional[UUID] = None
    name: str
    entity_type: EntityType
    observations: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    metadata_definition_id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class KnowledgeRelation(BaseModel):
    """A relationship between nodes in the knowledge graph."""
    id: Optional[UUID] = None
    from_node_id: UUID
    to_node_id: UUID
    from_node_name: Optional[str] = None
    to_node_name: Optional[str] = None
    relation_type: RelationType
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: Optional[datetime] = None


class KnowledgeNodeWithRelations(BaseModel):
    """A node with its incoming and outgoing relations."""
    node: KnowledgeNode
    incoming_relations: List[KnowledgeRelation] = Field(default_factory=list)
    outgoing_relations: List[KnowledgeRelation] = Field(default_factory=list)


class LineagePath(BaseModel):
    """A lineage path from source to target."""
    nodes: List[KnowledgeNode]
    relations: List[KnowledgeRelation]
    depth: int


class KGToolResponse(BaseModel):
    """Base response for Knowledge Graph MCP tools."""
    success: bool
    data: Dict[str, Any] = Field(default_factory=dict)
    error: Optional[str] = None
    execution_time_ms: float = 0.0
    correlation_id: Optional[str] = None


# Request Models

class CreateEntityRequest(BaseModel):
    """Request to create a knowledge graph entity."""
    name: str
    entity_type: EntityType
    observations: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class CreateRelationRequest(BaseModel):
    """Request to create a relationship between entities."""
    from_entity: str  # Name of source entity
    to_entity: str  # Name of target entity
    relation_type: RelationType
    metadata: Dict[str, Any] = Field(default_factory=dict)


class SearchNodesRequest(BaseModel):
    """Request to search for nodes."""
    query: str
    entity_types: Optional[List[EntityType]] = None
    limit: int = Field(default=20, le=100)


class GetEntityContextRequest(BaseModel):
    """Request to get entity context with relations."""
    name: str
    depth: int = Field(default=1, le=3)
    include_observations: bool = True


class GetLineageRequest(BaseModel):
    """Request to get lineage (dependency chain)."""
    entity_name: str
    direction: str = "upstream"  # upstream or downstream
    max_depth: int = Field(default=5, le=10)
    relation_types: Optional[List[RelationType]] = None


class OpenNodesRequest(BaseModel):
    """Request to open multiple nodes by name."""
    names: List[str]


class AddObservationsRequest(BaseModel):
    """Request to add observations to an entity."""
    entity_name: str
    observations: List[str]


class DeleteEntityRequest(BaseModel):
    """Request to delete an entity."""
    name: str
    cascade: bool = False  # Delete related relations


class DeleteRelationRequest(BaseModel):
    """Request to delete a relation."""
    from_entity: str
    to_entity: str
    relation_type: RelationType
