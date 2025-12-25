"""Query repository for metadata (CQRS Query Side).

Integrates with:
- database_service for database operations
- Redis caching from database_service
"""

import json
from typing import List, Optional, Dict, Any
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, or_, text, func

from ..models import MetadataDefinition, MetadataRelationship, MetadataVersion


class MetadataQueryRepository:
    """Handles all read operations for metadata (CQRS Query Side).
    
    Features:
    - Optimized read queries
    - Redis caching (via database_service)
    - Graph traversal
    - Version history
    - Full-text search
    """
    
    def __init__(self, db_manager_or_session, redis_client=None):
        """Initialize query repository.
        
        Args:
            db_manager_or_session: DatabaseManager instance or AsyncSession
            redis_client: Redis client from database_service (optional)
        """
        # Support both DatabaseManager and AsyncSession for backwards compatibility
        if hasattr(db_manager_or_session, 'execute_query'):
            # It's a DatabaseManager
            self.db_manager = db_manager_or_session
            self.session = None
            self.redis = redis_client or getattr(db_manager_or_session, 'redis_client', None)
        else:
            # It's an AsyncSession
            self.session = db_manager_or_session
            self.db_manager = None
            self.redis = redis_client
        
        self.cache_ttl = 3600  # 1 hour
    
    async def get_by_id(self, id: UUID) -> Optional[Dict[str, Any]]:
        """Get definition by UUID.
        
        Args:
            id: UUID of definition
            
        Returns:
            Dict with definition data or None
        """
        stmt = select(MetadataDefinition).where(
            MetadataDefinition.id == id,
            MetadataDefinition.is_active == True
        )
        result = await self.session.execute(stmt)
        definition = result.scalar_one_or_none()
        
        if not definition:
            return None
        
        return self._to_dict(definition)
    
    async def get_by_code(
        self,
        code: str,
        kind: str,
        version: Optional[int] = None,
        use_cache: bool = True
    ) -> Optional[Dict[str, Any]]:
        """Get definition by code (business key).
        
        Args:
            code: Business identifier
            kind: Type of definition
            version: Specific version (None = latest)
            use_cache: Whether to use Redis cache
            
        Returns:
            Dict with definition data or None
        """
        # Check cache first
        if use_cache and self.redis:
            cache_key = f"metadata:{kind}:{code}:v{version or 'latest'}"
            cached = await self.redis.get(cache_key)
            if cached:
                return json.loads(cached)
        
        # Query database
        stmt = select(MetadataDefinition).where(
            MetadataDefinition.code == code,
            MetadataDefinition.kind == kind,
            MetadataDefinition.is_active == True
        )
        
        if version is not None:
            stmt = stmt.where(MetadataDefinition.version == version)
        else:
            # Get latest version
            stmt = stmt.order_by(MetadataDefinition.version.desc()).limit(1)
        
        result = await self.session.execute(stmt)
        definition = result.scalar_one_or_none()
        
        if not definition:
            return None
        
        result_dict = self._to_dict(definition)
        
        # Cache result
        if use_cache and self.redis:
            cache_key = f"metadata:{kind}:{code}:v{version or 'latest'}"
            await self.redis.setex(
                cache_key,
                self.cache_ttl,
                json.dumps(result_dict)
            )
        
        return result_dict
    
    async def get_all_by_kind(
        self,
        kind: str,
        active_only: bool = True,
        limit: Optional[int] = None,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        """Get all definitions of a specific kind.
        
        Args:
            kind: Type of definition
            active_only: Filter to active definitions only
            limit: Max number of results
            offset: Pagination offset
            
        Returns:
            List of definition dicts
        """
        # Use subquery to get latest version of each code
        subq = (
            select(
                MetadataDefinition.code,
                func.max(MetadataDefinition.version).label('max_version')
            )
            .where(MetadataDefinition.kind == kind)
            .group_by(MetadataDefinition.code)
        )
        
        if active_only:
            subq = subq.where(MetadataDefinition.is_active == True)
        
        subq = subq.subquery()
        
        # Join to get full records
        stmt = (
            select(MetadataDefinition)
            .join(
                subq,
                and_(
                    MetadataDefinition.code == subq.c.code,
                    MetadataDefinition.version == subq.c.max_version
                )
            )
            .where(MetadataDefinition.kind == kind)
        )
        
        if active_only:
            stmt = stmt.where(MetadataDefinition.is_active == True)
        
        if limit:
            stmt = stmt.limit(limit)
        if offset:
            stmt = stmt.offset(offset)
        
        result = await self.session.execute(stmt)
        definitions = result.scalars().all()
        
        return [self._to_dict(d) for d in definitions]
    
    async def search(
        self,
        filters: Dict[str, Any],
        limit: int = 100,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        """Search definitions with flexible filters.
        
        Supports:
        - kind: exact match
        - code: exact or LIKE
        - name: LIKE search
        - data: JSONB queries
        
        Args:
            filters: Dict of filter criteria
            limit: Max results
            offset: Pagination offset
            
        Returns:
            List of matching definitions
        """
        # Use subquery for latest versions
        subq = (
            select(
                MetadataDefinition.code,
                MetadataDefinition.kind,
                func.max(MetadataDefinition.version).label('max_version')
            )
            .where(MetadataDefinition.is_active == True)
            .group_by(MetadataDefinition.code, MetadataDefinition.kind)
            .subquery()
        )
        
        stmt = (
            select(MetadataDefinition)
            .join(
                subq,
                and_(
                    MetadataDefinition.code == subq.c.code,
                    MetadataDefinition.kind == subq.c.kind,
                    MetadataDefinition.version == subq.c.max_version
                )
            )
            .where(MetadataDefinition.is_active == True)
        )
        
        # Apply filters
        if 'kind' in filters:
            stmt = stmt.where(MetadataDefinition.kind == filters['kind'])
        
        if 'code' in filters:
            if filters['code'].endswith('*'):
                # Wildcard search
                pattern = filters['code'].replace('*', '%')
                stmt = stmt.where(MetadataDefinition.code.like(pattern))
            else:
                stmt = stmt.where(MetadataDefinition.code == filters['code'])
        
        if 'name' in filters:
            stmt = stmt.where(MetadataDefinition.name.ilike(f"%{filters['name']}%"))
        
        # JSONB queries
        if 'data' in filters:
            for key, value in filters['data'].items():
                stmt = stmt.where(
                    MetadataDefinition.data[key].astext == str(value)
                )
        
        stmt = stmt.limit(limit).offset(offset)
        
        result = await self.session.execute(stmt)
        definitions = result.scalars().all()
        
        return [self._to_dict(d) for d in definitions]
    
    async def get_all_relationships(
        self,
        relationship_types: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """Get all relationships in the system.
        
        Args:
            relationship_types: Filter by specific types
            
        Returns:
            List of all relationship dicts
        """
        conditions = [MetadataRelationship.is_active == True]
        
        if relationship_types:
            conditions.append(MetadataRelationship.relationship_type.in_(relationship_types))
        
        stmt = select(MetadataRelationship).where(and_(*conditions))
        
        result = await self.session.execute(stmt)
        relationships = result.scalars().all()
        
        return [self._relationship_to_dict(r) for r in relationships]

    async def get_relationships(
        self,
        entity_code: str,
        direction: str = "both",  # "outbound", "inbound", "both"
        relationship_types: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """Get relationships for an entity.
        
        Args:
            entity_code: Entity code
            direction: "outbound", "inbound", or "both"
            relationship_types: Filter by specific types
            
        Returns:
            List of relationship dicts
        """
        conditions = [MetadataRelationship.is_active == True]
        
        if direction == "outbound":
            conditions.append(MetadataRelationship.from_entity_code == entity_code)
        elif direction == "inbound":
            conditions.append(MetadataRelationship.to_entity_code == entity_code)
        else:  # both
            conditions.append(
                or_(
                    MetadataRelationship.from_entity_code == entity_code,
                    MetadataRelationship.to_entity_code == entity_code
                )
            )
        
        if relationship_types:
            conditions.append(MetadataRelationship.relationship_type.in_(relationship_types))
        
        stmt = select(MetadataRelationship).where(and_(*conditions))
        
        result = await self.session.execute(stmt)
        relationships = result.scalars().all()
        
        return [self._relationship_to_dict(r) for r in relationships]
    
    async def check_relationship_exists(
        self,
        from_code: str,
        to_code: str,
        rel_type: str
    ) -> bool:
        """Check if a specific relationship exists.
        
        Args:
            from_code: Source entity code
            to_code: Target entity code
            rel_type: Relationship type
            
        Returns:
            True if exists and active
        """
        stmt = select(MetadataRelationship).where(
            MetadataRelationship.from_entity_code == from_code,
            MetadataRelationship.to_entity_code == to_code,
            MetadataRelationship.relationship_type == rel_type,
            MetadataRelationship.is_active == True
        )
        result = await self.session.execute(stmt)
        return result.first() is not None

    async def get_relationship_graph(
        self,
        entity_code: str,
        depth: int = 1,
        relationship_types: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Get relationship graph using recursive CTE.
        
        Performs BFS traversal up to specified depth.
        
        Args:
            entity_code: Starting entity code
            depth: Max traversal depth
            relationship_types: Filter by specific types
            
        Returns:
            Dict with nodes and edges
        """
        # Build recursive CTE query
        type_filter = ""
        if relationship_types:
            types_str = "', '".join(relationship_types)
            type_filter = f"AND relationship_type IN ('{types_str}')"
        
        query = text(f"""
            WITH RECURSIVE graph_traversal AS (
                -- Base case: direct relationships
                SELECT 
                    from_entity_code,
                    to_entity_code,
                    relationship_type,
                    from_cardinality,
                    to_cardinality,
                    metadata,
                    1 as depth
                FROM metadata_relationships
                WHERE (from_entity_code = :entity_code OR to_entity_code = :entity_code)
                  AND is_active = true
                  {type_filter}
                
                UNION ALL
                
                -- Recursive case: follow relationships
                SELECT 
                    r.from_entity_code,
                    r.to_entity_code,
                    r.relationship_type,
                    r.from_cardinality,
                    r.to_cardinality,
                    r.metadata,
                    gt.depth + 1
                FROM metadata_relationships r
                INNER JOIN graph_traversal gt 
                    ON (r.from_entity_code = gt.to_entity_code OR r.to_entity_code = gt.from_entity_code)
                WHERE gt.depth < :max_depth
                  AND r.is_active = true
                  {type_filter}
            )
            SELECT DISTINCT * FROM graph_traversal;
        """)
        
        result = await self.session.execute(
            query,
            {"entity_code": entity_code, "max_depth": depth}
        )
        
        edges = []
        nodes = set()
        
        for row in result:
            edges.append({
                "from": row.from_entity_code,
                "to": row.to_entity_code,
                "type": row.relationship_type,
                "from_cardinality": row.from_cardinality,
                "to_cardinality": row.to_cardinality,
                "metadata": row.metadata,
                "depth": row.depth
            })
            nodes.add(row.from_entity_code)
            nodes.add(row.to_entity_code)
        
        return {
            "root": entity_code,
            "nodes": list(nodes),
            "edges": edges,
            "depth": depth
        }
    
    async def get_version_history(
        self,
        code: str,
        kind: str,
        limit: int = 50
    ) -> List[Dict[str, Any]]:
        """Get version history for a definition.
        
        Args:
            code: Business identifier
            kind: Type of definition
            limit: Max versions to return
            
        Returns:
            List of version dicts (newest first)
        """
        stmt = select(MetadataVersion).where(
            MetadataVersion.definition_code == code,
            MetadataVersion.definition_kind == kind
        ).order_by(MetadataVersion.version.desc()).limit(limit)
        
        result = await self.session.execute(stmt)
        versions = result.scalars().all()
        
        return [self._version_to_dict(v) for v in versions]
    
    async def count_by_kind(self, kind: str, active_only: bool = True) -> int:
        """Count definitions of a specific kind.
        
        Args:
            kind: Type of definition
            active_only: Count only active definitions
            
        Returns:
            Count of definitions
        """
        # Count distinct codes (latest versions only)
        stmt = select(func.count(func.distinct(MetadataDefinition.code))).where(
            MetadataDefinition.kind == kind
        )
        
        if active_only:
            stmt = stmt.where(MetadataDefinition.is_active == True)
        
        result = await self.session.execute(stmt)
        return result.scalar_one()
    
    async def get_entity_by_code(self, entity_code: str):
        """Get entity definition by code.
        
        Args:
            entity_code: Entity code to retrieve
            
        Returns:
            EntityDefinition object or None
        """
        if self.db_manager:
            # Use DatabaseManager for direct query
            query = """
                SELECT * FROM metadata_definitions 
                WHERE code = :code AND kind = 'entity_definition' AND is_active = true
                ORDER BY version DESC LIMIT 1
            """
            result = await self.db_manager.execute_query(query, {"code": entity_code})
            if result and len(result) > 0:
                return self._row_to_entity(result[0])
            return None
        else:
            # Use session for SQLAlchemy query
            return await self.get_by_code(entity_code, "entity_definition")
    
    async def get_entities_by_module(self, module_code: str):
        """Get all entities for a module.
        
        Args:
            module_code: Module code to filter by
            
        Returns:
            List of EntityDefinition objects
        """
        if self.db_manager:
            # Use DatabaseManager for direct query
            query = """
                SELECT * FROM metadata_definitions 
                WHERE kind = 'entity_definition' 
                AND is_active = true
                AND data->>'module_code' = :module_code
                ORDER BY code
            """
            result = await self.db_manager.execute_query(query, {"module_code": module_code})
            return [self._row_to_entity(row) for row in result]
        else:
            # Use session for SQLAlchemy query
            stmt = select(MetadataDefinition).where(
                MetadataDefinition.kind == "entity_definition",
                MetadataDefinition.is_active == True,
                MetadataDefinition.data['module_code'].astext == module_code
            ).order_by(MetadataDefinition.code)
            
            result = await self.session.execute(stmt)
            definitions = result.scalars().all()
            return [self._row_to_entity(self._to_dict(d)) for d in definitions]
    
    async def get_all_entities(self):
        """Get all entity definitions.
        
        Returns:
            List of EntityDefinition objects
        """
        if self.db_manager:
            # Use DatabaseManager for direct query
            query = """
                SELECT * FROM metadata_definitions 
                WHERE kind = 'entity_definition' AND is_active = true
                ORDER BY code
            """
            result = await self.db_manager.execute_query(query)
            return [self._row_to_entity(row) for row in result]
        else:
            # Use session for SQLAlchemy query
            return await self.get_all_by_kind("entity_definition")
    
    def _row_to_entity(self, row):
        """Convert database row to EntityDefinition object.
        
        Args:
            row: Database row (dict or object)
            
        Returns:
            EntityDefinition object
        """
        from ..ontology_models import EntityDefinition, TableSchemaDefinition, ColumnDefinition
        
        # Handle both dict and object rows
        if isinstance(row, dict):
            data = row.get('data', {})
            code = row.get('code')
            name = row.get('name')
            description = row.get('description')
        else:
            data = row.data if hasattr(row, 'data') else {}
            code = row.code if hasattr(row, 'code') else None
            name = row.name if hasattr(row, 'name') else None
            description = row.description if hasattr(row, 'description') else None
        
        # Extract table_schema if present
        table_schema = None
        if 'table_schema' in data:
            schema_data = data['table_schema']
            columns = [
                ColumnDefinition(**col) for col in schema_data.get('columns', [])
            ]
            table_schema = TableSchemaDefinition(
                table_name=schema_data.get('table_name'),
                class_name=schema_data.get('class_name'),
                columns=columns
            )
        
        return EntityDefinition(
            id=str(row.get('id') if isinstance(row, dict) else row.id),
            code=code,
            name=name,
            description=description,
            table_schema=table_schema,
            module_code=data.get('module_code'),
            metadata_=data.get('metadata_', {})
        )
    
    def _to_dict(self, definition: MetadataDefinition) -> Dict[str, Any]:
        """Convert MetadataDefinition to dict.
        
        Args:
            definition: MetadataDefinition instance
            
        Returns:
            Dict representation
        """
        return {
            "id": str(definition.id),
            "code": definition.code,
            "kind": definition.kind,
            "name": definition.name,
            "description": definition.data.get("description") if definition.data else None,
            "data": definition.data,
            "version": definition.version,
            "is_active": definition.is_active,
            "created_at": definition.created_at.isoformat() if definition.created_at else None,
            "updated_at": definition.updated_at.isoformat() if definition.updated_at else None,
            "created_by": definition.created_by,
            "updated_by": getattr(definition, 'updated_by', None)
        }
    
    def _relationship_to_dict(self, relationship: MetadataRelationship) -> Dict[str, Any]:
        """Convert relationship model to dict."""
        return {
            "id": str(relationship.id),
            "from_entity_code": relationship.from_entity_code,
            "to_entity_code": relationship.to_entity_code,
            "relationship_type": relationship.relationship_type,
            "from_cardinality": relationship.from_cardinality,
            "to_cardinality": relationship.to_cardinality,
            "metadata_": relationship.metadata_,
            "created_at": relationship.created_at.isoformat() if relationship.created_at else None,
            "is_active": relationship.is_active
        }
    
    def _version_to_dict(self, version: MetadataVersion) -> Dict[str, Any]:
        """Convert version model to dict."""
        return {
            "id": str(version.id),
            "definition_code": version.definition_code,
            "definition_kind": version.definition_kind,
            "version": version.version,
            "data": version.data,
            "change_type": version.change_type,
            "changed_by": version.changed_by,
            "changed_at": version.changed_at.isoformat(),
            "change_description": version.change_description
        }
