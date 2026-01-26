"""
Knowledge Graph MCP Tools for ontology and relationship management.

These tools provide access to the knowledge graph for AI agents,
enabling them to store and query value chains, KPIs, entities, and relationships.
"""

from __future__ import annotations

import logging
import time
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, TYPE_CHECKING

from .knowledge_graph_models import (
    KGToolResponse,
    EntityType,
    RelationType,
    CreateEntityRequest,
    CreateRelationRequest,
    SearchNodesRequest,
    GetEntityContextRequest,
    GetLineageRequest,
    OpenNodesRequest,
    AddObservationsRequest,
)
from .knowledge_graph_manager import KnowledgeGraphManager

if TYPE_CHECKING:
    from ..database_manager import DatabaseManager

logger = logging.getLogger(__name__)


class BaseKGTool(ABC):
    """Base class for Knowledge Graph MCP tools."""
    
    name: str
    description: str
    
    def __init__(self, kg_manager: KnowledgeGraphManager):
        self.kg_manager = kg_manager
    
    @abstractmethod
    async def execute(self, params: Dict[str, Any]) -> KGToolResponse:
        """Execute the tool with given parameters."""
        pass
    
    def get_schema(self) -> Dict[str, Any]:
        """Get the tool's parameter schema for Claude."""
        return {
            "name": self.name,
            "description": self.description,
            "input_schema": self._get_input_schema()
        }
    
    @abstractmethod
    def _get_input_schema(self) -> Dict[str, Any]:
        """Get the input schema for this tool."""
        pass


class CreateEntityTool(BaseKGTool):
    """Create an entity in the knowledge graph."""
    
    name = "create_entity"
    description = "Create a new entity in the knowledge graph (value chain, module, KPI, entity, etc.)"
    
    def _get_input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Unique name for the entity"
                },
                "entity_type": {
                    "type": "string",
                    "enum": [e.value for e in EntityType],
                    "description": "Type of entity"
                },
                "observations": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of observations/facts about the entity"
                },
                "metadata": {
                    "type": "object",
                    "description": "Additional metadata for the entity"
                }
            },
            "required": ["name", "entity_type"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> KGToolResponse:
        start_time = time.time()
        try:
            request = CreateEntityRequest(**params)
            
            node = await self.kg_manager.create_node(
                name=request.name,
                entity_type=request.entity_type,
                observations=request.observations,
                metadata=request.metadata
            )
            
            return KGToolResponse(
                success=True,
                data={"entity": node.model_dump(mode="json")},
                execution_time_ms=(time.time() - start_time) * 1000
            )
            
        except Exception as e:
            logger.error(f"CreateEntityTool failed: {e}")
            return KGToolResponse(
                success=False,
                error=str(e),
                execution_time_ms=(time.time() - start_time) * 1000
            )


class CreateRelationTool(BaseKGTool):
    """Create a relationship between entities."""
    
    name = "create_relation"
    description = "Create a relationship between two entities in the knowledge graph"
    
    def _get_input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "from_entity": {
                    "type": "string",
                    "description": "Name of the source entity"
                },
                "to_entity": {
                    "type": "string",
                    "description": "Name of the target entity"
                },
                "relation_type": {
                    "type": "string",
                    "enum": [r.value for r in RelationType],
                    "description": "Type of relationship"
                },
                "metadata": {
                    "type": "object",
                    "description": "Additional metadata for the relationship"
                }
            },
            "required": ["from_entity", "to_entity", "relation_type"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> KGToolResponse:
        start_time = time.time()
        try:
            request = CreateRelationRequest(**params)
            
            relation = await self.kg_manager.create_relation(
                from_node_name=request.from_entity,
                to_node_name=request.to_entity,
                relation_type=request.relation_type,
                metadata=request.metadata
            )
            
            return KGToolResponse(
                success=True,
                data={"relation": relation.model_dump(mode="json")},
                execution_time_ms=(time.time() - start_time) * 1000
            )
            
        except Exception as e:
            logger.error(f"CreateRelationTool failed: {e}")
            return KGToolResponse(
                success=False,
                error=str(e),
                execution_time_ms=(time.time() - start_time) * 1000
            )


class SearchNodesTool(BaseKGTool):
    """Search for nodes in the knowledge graph."""
    
    name = "search_nodes"
    description = "Search for entities in the knowledge graph by name or observation content"
    
    def _get_input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query (matches name or observations)"
                },
                "entity_types": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "enum": [e.value for e in EntityType]
                    },
                    "description": "Filter by entity types"
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum results to return",
                    "default": 20,
                    "maximum": 100
                }
            },
            "required": ["query"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> KGToolResponse:
        start_time = time.time()
        try:
            request = SearchNodesRequest(**params)
            
            entity_types = None
            if request.entity_types:
                entity_types = [EntityType(t) for t in request.entity_types]
            
            nodes = await self.kg_manager.search_nodes(
                query=request.query,
                entity_types=entity_types,
                limit=request.limit
            )
            
            return KGToolResponse(
                success=True,
                data={
                    "nodes": [n.model_dump(mode="json") for n in nodes],
                    "count": len(nodes)
                },
                execution_time_ms=(time.time() - start_time) * 1000
            )
            
        except Exception as e:
            logger.error(f"SearchNodesTool failed: {e}")
            return KGToolResponse(
                success=False,
                error=str(e),
                execution_time_ms=(time.time() - start_time) * 1000
            )


class GetEntityContextTool(BaseKGTool):
    """Get entity with its relationships."""
    
    name = "get_entity_context"
    description = "Get an entity and its immediate relationships (what it connects to and from)"
    
    def _get_input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Name of the entity"
                },
                "depth": {
                    "type": "integer",
                    "description": "Depth of relationship traversal",
                    "default": 1,
                    "maximum": 3
                },
                "include_observations": {
                    "type": "boolean",
                    "description": "Include observation details",
                    "default": True
                }
            },
            "required": ["name"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> KGToolResponse:
        start_time = time.time()
        try:
            request = GetEntityContextRequest(**params)
            
            context = await self.kg_manager.get_entity_context(
                name=request.name,
                depth=request.depth,
                include_observations=request.include_observations
            )
            
            if not context:
                return KGToolResponse(
                    success=False,
                    error=f"Entity '{request.name}' not found",
                    execution_time_ms=(time.time() - start_time) * 1000
                )
            
            return KGToolResponse(
                success=True,
                data={
                    "entity": context.node.model_dump(mode="json"),
                    "incoming_relations": [r.model_dump(mode="json") for r in context.incoming_relations],
                    "outgoing_relations": [r.model_dump(mode="json") for r in context.outgoing_relations]
                },
                execution_time_ms=(time.time() - start_time) * 1000
            )
            
        except Exception as e:
            logger.error(f"GetEntityContextTool failed: {e}")
            return KGToolResponse(
                success=False,
                error=str(e),
                execution_time_ms=(time.time() - start_time) * 1000
            )


class GetLineageTool(BaseKGTool):
    """Get lineage (dependency chain) for an entity."""
    
    name = "get_lineage"
    description = "Trace the dependency chain for an entity (upstream: what it depends on, downstream: what depends on it)"
    
    def _get_input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "entity_name": {
                    "type": "string",
                    "description": "Name of the entity to trace lineage for"
                },
                "direction": {
                    "type": "string",
                    "enum": ["upstream", "downstream"],
                    "description": "Direction of lineage traversal",
                    "default": "upstream"
                },
                "max_depth": {
                    "type": "integer",
                    "description": "Maximum traversal depth",
                    "default": 5,
                    "maximum": 10
                },
                "relation_types": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "enum": [r.value for r in RelationType]
                    },
                    "description": "Filter by relation types"
                }
            },
            "required": ["entity_name"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> KGToolResponse:
        start_time = time.time()
        try:
            request = GetLineageRequest(**params)
            
            relation_types = None
            if request.relation_types:
                relation_types = [RelationType(r) for r in request.relation_types]
            
            lineage = await self.kg_manager.get_lineage(
                entity_name=request.entity_name,
                direction=request.direction,
                max_depth=request.max_depth,
                relation_types=relation_types
            )
            
            return KGToolResponse(
                success=True,
                data={
                    "nodes": [n.model_dump(mode="json") for n in lineage.nodes],
                    "relations": [r.model_dump(mode="json") for r in lineage.relations],
                    "depth": lineage.depth,
                    "node_count": len(lineage.nodes)
                },
                execution_time_ms=(time.time() - start_time) * 1000
            )
            
        except Exception as e:
            logger.error(f"GetLineageTool failed: {e}")
            return KGToolResponse(
                success=False,
                error=str(e),
                execution_time_ms=(time.time() - start_time) * 1000
            )


class OpenNodesTool(BaseKGTool):
    """Open multiple nodes by name."""
    
    name = "open_nodes"
    description = "Retrieve multiple entities by their names"
    
    def _get_input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "names": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of entity names to retrieve"
                }
            },
            "required": ["names"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> KGToolResponse:
        start_time = time.time()
        try:
            request = OpenNodesRequest(**params)
            
            nodes = await self.kg_manager.open_nodes(request.names)
            
            return KGToolResponse(
                success=True,
                data={
                    "nodes": [n.model_dump(mode="json") for n in nodes],
                    "found": len(nodes),
                    "requested": len(request.names)
                },
                execution_time_ms=(time.time() - start_time) * 1000
            )
            
        except Exception as e:
            logger.error(f"OpenNodesTool failed: {e}")
            return KGToolResponse(
                success=False,
                error=str(e),
                execution_time_ms=(time.time() - start_time) * 1000
            )


class AddObservationsTool(BaseKGTool):
    """Add observations to an entity."""
    
    name = "add_observations"
    description = "Add new observations (facts) to an existing entity"
    
    def _get_input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "entity_name": {
                    "type": "string",
                    "description": "Name of the entity to add observations to"
                },
                "observations": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of observations to add"
                }
            },
            "required": ["entity_name", "observations"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> KGToolResponse:
        start_time = time.time()
        try:
            request = AddObservationsRequest(**params)
            
            node = await self.kg_manager.add_observations(
                entity_name=request.entity_name,
                observations=request.observations
            )
            
            if not node:
                return KGToolResponse(
                    success=False,
                    error=f"Entity '{request.entity_name}' not found",
                    execution_time_ms=(time.time() - start_time) * 1000
                )
            
            return KGToolResponse(
                success=True,
                data={
                    "entity": node.model_dump(mode="json"),
                    "observations_added": len(request.observations)
                },
                execution_time_ms=(time.time() - start_time) * 1000
            )
            
        except Exception as e:
            logger.error(f"AddObservationsTool failed: {e}")
            return KGToolResponse(
                success=False,
                error=str(e),
                execution_time_ms=(time.time() - start_time) * 1000
            )


# Tool registry
ALL_KNOWLEDGE_GRAPH_TOOLS = [
    CreateEntityTool,
    CreateRelationTool,
    SearchNodesTool,
    GetEntityContextTool,
    GetLineageTool,
    OpenNodesTool,
    AddObservationsTool,
]
