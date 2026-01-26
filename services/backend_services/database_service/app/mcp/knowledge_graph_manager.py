"""
Knowledge Graph Manager for TimescaleDB-backed graph operations.

Provides graph-like query and traversal capabilities using TimescaleDB
as the backing store, syncing with metadata_definitions when applicable.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional, TYPE_CHECKING
from uuid import UUID, uuid4
from datetime import datetime

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from .knowledge_graph_models import (
    KnowledgeNode,
    KnowledgeRelation,
    KnowledgeNodeWithRelations,
    LineagePath,
    EntityType,
    RelationType,
)

if TYPE_CHECKING:
    from ..database_manager import DatabaseManager

logger = logging.getLogger(__name__)


class KnowledgeGraphManager:
    """
    Manages knowledge graph operations using TimescaleDB.
    
    The knowledge graph stores ontology entities and their relationships,
    enabling graph-like traversal for lineage analysis and context retrieval.
    """
    
    def __init__(self, db_manager: "DatabaseManager"):
        self.db_manager = db_manager
        self._initialized = False
    
    async def initialize(self) -> None:
        """Initialize the knowledge graph tables if they don't exist."""
        if self._initialized:
            return
        
        create_tables_sql = """
        -- Knowledge graph nodes
        CREATE TABLE IF NOT EXISTS knowledge_graph_nodes (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            name VARCHAR(255) NOT NULL,
            entity_type VARCHAR(100) NOT NULL,
            observations JSONB DEFAULT '[]'::jsonb,
            metadata JSONB DEFAULT '{}'::jsonb,
            metadata_definition_id UUID,
            created_at TIMESTAMPTZ DEFAULT NOW(),
            updated_at TIMESTAMPTZ DEFAULT NOW(),
            UNIQUE(name, entity_type)
        );

        -- Knowledge graph relations
        CREATE TABLE IF NOT EXISTS knowledge_graph_relations (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            from_node_id UUID NOT NULL REFERENCES knowledge_graph_nodes(id) ON DELETE CASCADE,
            to_node_id UUID NOT NULL REFERENCES knowledge_graph_nodes(id) ON DELETE CASCADE,
            relation_type VARCHAR(100) NOT NULL,
            metadata JSONB DEFAULT '{}'::jsonb,
            created_at TIMESTAMPTZ DEFAULT NOW(),
            UNIQUE(from_node_id, to_node_id, relation_type)
        );

        -- Indexes for efficient graph traversal
        CREATE INDEX IF NOT EXISTS idx_kg_nodes_type ON knowledge_graph_nodes(entity_type);
        CREATE INDEX IF NOT EXISTS idx_kg_nodes_name ON knowledge_graph_nodes(name);
        CREATE INDEX IF NOT EXISTS idx_kg_nodes_name_lower ON knowledge_graph_nodes(LOWER(name));
        CREATE INDEX IF NOT EXISTS idx_kg_relations_from ON knowledge_graph_relations(from_node_id);
        CREATE INDEX IF NOT EXISTS idx_kg_relations_to ON knowledge_graph_relations(to_node_id);
        CREATE INDEX IF NOT EXISTS idx_kg_relations_type ON knowledge_graph_relations(relation_type);
        CREATE INDEX IF NOT EXISTS idx_kg_nodes_observations ON knowledge_graph_nodes USING GIN (observations);
        """
        
        try:
            async with self.db_manager.get_session() as session:
                for statement in create_tables_sql.split(';'):
                    statement = statement.strip()
                    if statement:
                        await session.execute(text(statement))
                await session.commit()
            
            self._initialized = True
            logger.info("Knowledge graph tables initialized")
        except Exception as e:
            logger.error(f"Failed to initialize knowledge graph tables: {e}")
            raise
    
    async def create_node(
        self,
        name: str,
        entity_type: EntityType,
        observations: List[str] = None,
        metadata: Dict[str, Any] = None,
        metadata_definition_id: UUID = None
    ) -> KnowledgeNode:
        """Create a new node in the knowledge graph."""
        await self.initialize()
        
        node_id = uuid4()
        observations = observations or []
        metadata = metadata or {}
        
        query = """
            INSERT INTO knowledge_graph_nodes 
                (id, name, entity_type, observations, metadata, metadata_definition_id)
            VALUES 
                (:id, :name, :entity_type, :observations::jsonb, :metadata::jsonb, :metadata_def_id)
            ON CONFLICT (name, entity_type) 
            DO UPDATE SET
                observations = knowledge_graph_nodes.observations || :observations::jsonb,
                metadata = knowledge_graph_nodes.metadata || :metadata::jsonb,
                updated_at = NOW()
            RETURNING id, name, entity_type, observations, metadata, metadata_definition_id, created_at, updated_at
        """
        
        import json
        async with self.db_manager.get_session() as session:
            result = await session.execute(
                text(query),
                {
                    "id": str(node_id),
                    "name": name,
                    "entity_type": entity_type.value,
                    "observations": json.dumps(observations),
                    "metadata": json.dumps(metadata),
                    "metadata_def_id": str(metadata_definition_id) if metadata_definition_id else None
                }
            )
            await session.commit()
            row = result.fetchone()
        
        return KnowledgeNode(
            id=row.id,
            name=row.name,
            entity_type=EntityType(row.entity_type),
            observations=row.observations or [],
            metadata=row.metadata or {},
            metadata_definition_id=row.metadata_definition_id,
            created_at=row.created_at,
            updated_at=row.updated_at
        )
    
    async def create_relation(
        self,
        from_node_name: str,
        to_node_name: str,
        relation_type: RelationType,
        metadata: Dict[str, Any] = None
    ) -> KnowledgeRelation:
        """Create a relationship between two nodes."""
        await self.initialize()
        
        import json
        metadata = metadata or {}
        
        # First, get the node IDs
        query = """
            WITH from_node AS (
                SELECT id FROM knowledge_graph_nodes WHERE LOWER(name) = LOWER(:from_name) LIMIT 1
            ),
            to_node AS (
                SELECT id FROM knowledge_graph_nodes WHERE LOWER(name) = LOWER(:to_name) LIMIT 1
            )
            INSERT INTO knowledge_graph_relations 
                (id, from_node_id, to_node_id, relation_type, metadata)
            SELECT 
                gen_random_uuid(),
                from_node.id,
                to_node.id,
                :relation_type,
                :metadata::jsonb
            FROM from_node, to_node
            ON CONFLICT (from_node_id, to_node_id, relation_type) DO NOTHING
            RETURNING id, from_node_id, to_node_id, relation_type, metadata, created_at
        """
        
        async with self.db_manager.get_session() as session:
            result = await session.execute(
                text(query),
                {
                    "from_name": from_node_name,
                    "to_name": to_node_name,
                    "relation_type": relation_type.value,
                    "metadata": json.dumps(metadata)
                }
            )
            await session.commit()
            row = result.fetchone()
        
        if not row:
            raise ValueError(f"Could not create relation: nodes '{from_node_name}' or '{to_node_name}' not found")
        
        return KnowledgeRelation(
            id=row.id,
            from_node_id=row.from_node_id,
            to_node_id=row.to_node_id,
            from_node_name=from_node_name,
            to_node_name=to_node_name,
            relation_type=RelationType(row.relation_type),
            metadata=row.metadata or {},
            created_at=row.created_at
        )
    
    async def search_nodes(
        self,
        query: str,
        entity_types: List[EntityType] = None,
        limit: int = 20
    ) -> List[KnowledgeNode]:
        """Search for nodes by name or observation content."""
        await self.initialize()
        
        search_query = """
            SELECT 
                id, name, entity_type, observations, metadata, 
                metadata_definition_id, created_at, updated_at,
                GREATEST(
                    similarity(LOWER(name), LOWER(:query)),
                    CASE WHEN observations::text ILIKE '%' || :query || '%' THEN 0.5 ELSE 0 END
                ) AS relevance
            FROM knowledge_graph_nodes
            WHERE 
                (LOWER(name) LIKE '%' || LOWER(:query) || '%'
                OR observations::text ILIKE '%' || :query || '%')
        """
        
        params = {"query": query, "limit": limit}
        
        if entity_types:
            type_values = [t.value for t in entity_types]
            search_query += " AND entity_type = ANY(:entity_types)"
            params["entity_types"] = type_values
        
        search_query += " ORDER BY relevance DESC, name LIMIT :limit"
        
        async with self.db_manager.get_session() as session:
            result = await session.execute(text(search_query), params)
            rows = result.fetchall()
        
        return [
            KnowledgeNode(
                id=row.id,
                name=row.name,
                entity_type=EntityType(row.entity_type),
                observations=row.observations or [],
                metadata=row.metadata or {},
                metadata_definition_id=row.metadata_definition_id,
                created_at=row.created_at,
                updated_at=row.updated_at
            )
            for row in rows
        ]
    
    async def get_node_by_name(self, name: str) -> Optional[KnowledgeNode]:
        """Get a node by its name."""
        await self.initialize()
        
        query = """
            SELECT id, name, entity_type, observations, metadata, 
                   metadata_definition_id, created_at, updated_at
            FROM knowledge_graph_nodes
            WHERE LOWER(name) = LOWER(:name)
            LIMIT 1
        """
        
        async with self.db_manager.get_session() as session:
            result = await session.execute(text(query), {"name": name})
            row = result.fetchone()
        
        if not row:
            return None
        
        return KnowledgeNode(
            id=row.id,
            name=row.name,
            entity_type=EntityType(row.entity_type),
            observations=row.observations or [],
            metadata=row.metadata or {},
            metadata_definition_id=row.metadata_definition_id,
            created_at=row.created_at,
            updated_at=row.updated_at
        )
    
    async def get_entity_context(
        self,
        name: str,
        depth: int = 1,
        include_observations: bool = True
    ) -> Optional[KnowledgeNodeWithRelations]:
        """Get an entity with its immediate relations."""
        await self.initialize()
        
        node = await self.get_node_by_name(name)
        if not node:
            return None
        
        # Get incoming relations
        incoming_query = """
            SELECT 
                r.id, r.from_node_id, r.to_node_id, r.relation_type, r.metadata, r.created_at,
                fn.name AS from_node_name, tn.name AS to_node_name
            FROM knowledge_graph_relations r
            JOIN knowledge_graph_nodes fn ON fn.id = r.from_node_id
            JOIN knowledge_graph_nodes tn ON tn.id = r.to_node_id
            WHERE r.to_node_id = :node_id
        """
        
        # Get outgoing relations
        outgoing_query = """
            SELECT 
                r.id, r.from_node_id, r.to_node_id, r.relation_type, r.metadata, r.created_at,
                fn.name AS from_node_name, tn.name AS to_node_name
            FROM knowledge_graph_relations r
            JOIN knowledge_graph_nodes fn ON fn.id = r.from_node_id
            JOIN knowledge_graph_nodes tn ON tn.id = r.to_node_id
            WHERE r.from_node_id = :node_id
        """
        
        async with self.db_manager.get_session() as session:
            incoming_result = await session.execute(text(incoming_query), {"node_id": str(node.id)})
            incoming_rows = incoming_result.fetchall()
            
            outgoing_result = await session.execute(text(outgoing_query), {"node_id": str(node.id)})
            outgoing_rows = outgoing_result.fetchall()
        
        incoming_relations = [
            KnowledgeRelation(
                id=row.id,
                from_node_id=row.from_node_id,
                to_node_id=row.to_node_id,
                from_node_name=row.from_node_name,
                to_node_name=row.to_node_name,
                relation_type=RelationType(row.relation_type),
                metadata=row.metadata or {},
                created_at=row.created_at
            )
            for row in incoming_rows
        ]
        
        outgoing_relations = [
            KnowledgeRelation(
                id=row.id,
                from_node_id=row.from_node_id,
                to_node_id=row.to_node_id,
                from_node_name=row.from_node_name,
                to_node_name=row.to_node_name,
                relation_type=RelationType(row.relation_type),
                metadata=row.metadata or {},
                created_at=row.created_at
            )
            for row in outgoing_rows
        ]
        
        if not include_observations:
            node.observations = []
        
        return KnowledgeNodeWithRelations(
            node=node,
            incoming_relations=incoming_relations,
            outgoing_relations=outgoing_relations
        )
    
    async def get_lineage(
        self,
        entity_name: str,
        direction: str = "upstream",
        max_depth: int = 5,
        relation_types: List[RelationType] = None
    ) -> LineagePath:
        """
        Get lineage (dependency chain) for an entity.
        
        Args:
            entity_name: Starting entity name
            direction: 'upstream' (what it depends on) or 'downstream' (what depends on it)
            max_depth: Maximum traversal depth
            relation_types: Filter by relation types
        """
        await self.initialize()
        
        node = await self.get_node_by_name(entity_name)
        if not node:
            return LineagePath(nodes=[], relations=[], depth=0)
        
        # Recursive CTE for graph traversal
        if direction == "upstream":
            # Follow outgoing relations (what this entity uses/depends on)
            traverse_query = """
                WITH RECURSIVE lineage AS (
                    -- Base case: starting node
                    SELECT 
                        n.id, n.name, n.entity_type, n.observations, n.metadata,
                        n.metadata_definition_id, n.created_at, n.updated_at,
                        0 AS depth,
                        ARRAY[n.id] AS path
                    FROM knowledge_graph_nodes n
                    WHERE LOWER(n.name) = LOWER(:entity_name)
                    
                    UNION ALL
                    
                    -- Recursive case: follow outgoing relations
                    SELECT 
                        n.id, n.name, n.entity_type, n.observations, n.metadata,
                        n.metadata_definition_id, n.created_at, n.updated_at,
                        l.depth + 1,
                        l.path || n.id
                    FROM lineage l
                    JOIN knowledge_graph_relations r ON r.from_node_id = l.id
                    JOIN knowledge_graph_nodes n ON n.id = r.to_node_id
                    WHERE l.depth < :max_depth
                      AND NOT n.id = ANY(l.path)  -- Prevent cycles
                )
                SELECT DISTINCT ON (id) * FROM lineage ORDER BY id, depth
            """
        else:
            # Follow incoming relations (what depends on this entity)
            traverse_query = """
                WITH RECURSIVE lineage AS (
                    SELECT 
                        n.id, n.name, n.entity_type, n.observations, n.metadata,
                        n.metadata_definition_id, n.created_at, n.updated_at,
                        0 AS depth,
                        ARRAY[n.id] AS path
                    FROM knowledge_graph_nodes n
                    WHERE LOWER(n.name) = LOWER(:entity_name)
                    
                    UNION ALL
                    
                    SELECT 
                        n.id, n.name, n.entity_type, n.observations, n.metadata,
                        n.metadata_definition_id, n.created_at, n.updated_at,
                        l.depth + 1,
                        l.path || n.id
                    FROM lineage l
                    JOIN knowledge_graph_relations r ON r.to_node_id = l.id
                    JOIN knowledge_graph_nodes n ON n.id = r.from_node_id
                    WHERE l.depth < :max_depth
                      AND NOT n.id = ANY(l.path)
                )
                SELECT DISTINCT ON (id) * FROM lineage ORDER BY id, depth
            """
        
        async with self.db_manager.get_session() as session:
            result = await session.execute(
                text(traverse_query),
                {"entity_name": entity_name, "max_depth": max_depth}
            )
            rows = result.fetchall()
        
        nodes = [
            KnowledgeNode(
                id=row.id,
                name=row.name,
                entity_type=EntityType(row.entity_type),
                observations=row.observations or [],
                metadata=row.metadata or {},
                metadata_definition_id=row.metadata_definition_id,
                created_at=row.created_at,
                updated_at=row.updated_at
            )
            for row in rows
        ]
        
        # Get relations between lineage nodes
        if len(nodes) > 1:
            node_ids = [str(n.id) for n in nodes]
            relations_query = """
                SELECT 
                    r.id, r.from_node_id, r.to_node_id, r.relation_type, r.metadata, r.created_at,
                    fn.name AS from_node_name, tn.name AS to_node_name
                FROM knowledge_graph_relations r
                JOIN knowledge_graph_nodes fn ON fn.id = r.from_node_id
                JOIN knowledge_graph_nodes tn ON tn.id = r.to_node_id
                WHERE r.from_node_id = ANY(:node_ids::uuid[])
                  AND r.to_node_id = ANY(:node_ids::uuid[])
            """
            
            async with self.db_manager.get_session() as session:
                result = await session.execute(
                    text(relations_query),
                    {"node_ids": node_ids}
                )
                rel_rows = result.fetchall()
            
            relations = [
                KnowledgeRelation(
                    id=row.id,
                    from_node_id=row.from_node_id,
                    to_node_id=row.to_node_id,
                    from_node_name=row.from_node_name,
                    to_node_name=row.to_node_name,
                    relation_type=RelationType(row.relation_type),
                    metadata=row.metadata or {},
                    created_at=row.created_at
                )
                for row in rel_rows
            ]
        else:
            relations = []
        
        max_depth_found = max((row.depth for row in rows), default=0)
        
        return LineagePath(
            nodes=nodes,
            relations=relations,
            depth=max_depth_found
        )
    
    async def open_nodes(self, names: List[str]) -> List[KnowledgeNode]:
        """Get multiple nodes by their names."""
        await self.initialize()
        
        if not names:
            return []
        
        query = """
            SELECT id, name, entity_type, observations, metadata, 
                   metadata_definition_id, created_at, updated_at
            FROM knowledge_graph_nodes
            WHERE LOWER(name) = ANY(:names)
        """
        
        lower_names = [n.lower() for n in names]
        
        async with self.db_manager.get_session() as session:
            result = await session.execute(text(query), {"names": lower_names})
            rows = result.fetchall()
        
        return [
            KnowledgeNode(
                id=row.id,
                name=row.name,
                entity_type=EntityType(row.entity_type),
                observations=row.observations or [],
                metadata=row.metadata or {},
                metadata_definition_id=row.metadata_definition_id,
                created_at=row.created_at,
                updated_at=row.updated_at
            )
            for row in rows
        ]
    
    async def add_observations(
        self,
        entity_name: str,
        observations: List[str]
    ) -> Optional[KnowledgeNode]:
        """Add observations to an existing entity."""
        await self.initialize()
        
        import json
        
        query = """
            UPDATE knowledge_graph_nodes
            SET 
                observations = observations || :observations::jsonb,
                updated_at = NOW()
            WHERE LOWER(name) = LOWER(:name)
            RETURNING id, name, entity_type, observations, metadata, 
                      metadata_definition_id, created_at, updated_at
        """
        
        async with self.db_manager.get_session() as session:
            result = await session.execute(
                text(query),
                {"name": entity_name, "observations": json.dumps(observations)}
            )
            await session.commit()
            row = result.fetchone()
        
        if not row:
            return None
        
        return KnowledgeNode(
            id=row.id,
            name=row.name,
            entity_type=EntityType(row.entity_type),
            observations=row.observations or [],
            metadata=row.metadata or {},
            metadata_definition_id=row.metadata_definition_id,
            created_at=row.created_at,
            updated_at=row.updated_at
        )
    
    async def delete_node(self, name: str, cascade: bool = False) -> bool:
        """Delete a node from the knowledge graph."""
        await self.initialize()
        
        if cascade:
            # Delete relations first, then node
            delete_query = """
                WITH deleted_node AS (
                    SELECT id FROM knowledge_graph_nodes WHERE LOWER(name) = LOWER(:name)
                )
                DELETE FROM knowledge_graph_relations
                WHERE from_node_id IN (SELECT id FROM deleted_node)
                   OR to_node_id IN (SELECT id FROM deleted_node);
                
                DELETE FROM knowledge_graph_nodes WHERE LOWER(name) = LOWER(:name);
            """
        else:
            delete_query = """
                DELETE FROM knowledge_graph_nodes 
                WHERE LOWER(name) = LOWER(:name)
                AND NOT EXISTS (
                    SELECT 1 FROM knowledge_graph_relations 
                    WHERE from_node_id = knowledge_graph_nodes.id 
                       OR to_node_id = knowledge_graph_nodes.id
                )
            """
        
        async with self.db_manager.get_session() as session:
            result = await session.execute(text(delete_query), {"name": name})
            await session.commit()
            return result.rowcount > 0
    
    async def delete_relation(
        self,
        from_entity: str,
        to_entity: str,
        relation_type: RelationType
    ) -> bool:
        """Delete a specific relation."""
        await self.initialize()
        
        query = """
            DELETE FROM knowledge_graph_relations r
            USING knowledge_graph_nodes fn, knowledge_graph_nodes tn
            WHERE r.from_node_id = fn.id
              AND r.to_node_id = tn.id
              AND LOWER(fn.name) = LOWER(:from_name)
              AND LOWER(tn.name) = LOWER(:to_name)
              AND r.relation_type = :relation_type
        """
        
        async with self.db_manager.get_session() as session:
            result = await session.execute(
                text(query),
                {
                    "from_name": from_entity,
                    "to_name": to_entity,
                    "relation_type": relation_type.value
                }
            )
            await session.commit()
            return result.rowcount > 0
