"""High-level metadata service orchestrating repositories and backend services."""

from typing import List, Optional, Dict, Any
from uuid import UUID

from ..repositories import MetadataWriteRepository, MetadataQueryRepository
from .metadata_instantiation_service import MetadataInstantiationService

# Import ontology models
import sys
from pathlib import Path
analytics_metadata_path = Path(__file__).parent.parent.parent / "analytics_metadata_service"
sys.path.insert(0, str(analytics_metadata_path))

from definitions.ontology_models import (
    ThingDefinition,
    RelationshipDefinition,
)


class MetadataService:
    """High-level metadata operations with caching and validation.
    
    Orchestrates:
    - Write/Query repositories (CQRS)
    - Event publishing (via messaging_service)
    - Model instantiation (Pydantic)
    - Relationship management
    """
    
    def __init__(
        self,
        write_repo: MetadataWriteRepository,
        query_repo: MetadataQueryRepository,
        instantiation_service: MetadataInstantiationService
    ):
        self.write_repo = write_repo
        self.query_repo = query_repo
        self.instantiation = instantiation_service
    
    # -------------------------------------------------------------------------
    # Generic CRUD operations (work for all definition types)
    # -------------------------------------------------------------------------
    
    async def create_definition(
        self,
        definition: ThingDefinition,
        created_by: str
    ) -> UUID:
        """Create a new metadata definition.
        
        Args:
            definition: Pydantic model instance
            created_by: User creating the definition
            
        Returns:
            UUID of created definition
        """
        # Extract metadata
        kind = self.instantiation.get_kind_from_model(definition)
        code = self.instantiation.get_code_from_model(definition)
        name = self.instantiation.get_name_from_model(definition)
        data = self.instantiation.serialize(definition)
        
        if not code:
            raise ValueError(f"Definition must have a 'code' field: {kind}")
        
        # Create in database
        definition_id = await self.write_repo.create_definition(
            kind=kind,
            code=code,
            name=name,
            data=data,
            created_by=created_by
        )
        
        # Create relationships if present
        if hasattr(definition, 'relationships') and definition.relationships:
            for rel in definition.relationships:
                await self.write_repo.create_relationship(
                    from_entity_code=rel.from_entity,
                    to_entity_code=rel.to_entity,
                    relationship_type=rel.relationship_type,
                    from_cardinality=rel.from_cardinality,
                    to_cardinality=rel.to_cardinality,
                    metadata=rel.metadata_ if hasattr(rel, 'metadata_') else None
                )
        
        return definition_id
    
    async def get_definition(
        self,
        code: str,
        kind: str,
        include_relationships: bool = True,
        version: Optional[int] = None,
        use_cache: bool = True
    ) -> Optional[ThingDefinition]:
        """Get definition by code.
        
        Args:
            code: Business identifier
            kind: Type of definition
            include_relationships: Whether to load relationships
            version: Specific version (None = latest)
            use_cache: Whether to use Redis cache
            
        Returns:
            Pydantic model instance or None
        """
        # Query database
        result = await self.query_repo.get_by_code(code, kind, version, use_cache)
        if not result:
            return None
        
        # Instantiate model
        definition = self.instantiation.instantiate(kind, result['data'])
        
        # Load relationships if requested
        if include_relationships and hasattr(definition, 'relationships'):
            relationships = await self.query_repo.get_relationships(code)
            definition.relationships = [
                self._dict_to_relationship(r) for r in relationships
            ]
        
        return definition
    
    async def update_definition(
        self,
        code: str,
        kind: str,
        definition: ThingDefinition,
        changed_by: str,
        change_description: Optional[str] = None
    ) -> None:
        """Update definition (creates new version).
        
        Args:
            code: Business identifier
            kind: Type of definition
            definition: Updated Pydantic model
            changed_by: User making the change
            change_description: Optional description
        """
        data = self.instantiation.serialize(definition)
        
        # Update definition
        await self.write_repo.update_definition(
            code=code,
            kind=kind,
            data=data,
            changed_by=changed_by,
            change_description=change_description
        )
        
        # Sync relationships (delete old, create new)
        if hasattr(definition, 'relationships') and definition.relationships:
            # Get existing relationships
            existing = await self.query_repo.get_relationships(code, direction="outbound")
            
            # Delete relationships not in new definition
            new_rel_keys = {
                (r.from_entity, r.to_entity, r.relationship_type)
                for r in definition.relationships
            }
            
            for existing_rel in existing:
                key = (
                    existing_rel['from_entity_code'],
                    existing_rel['to_entity_code'],
                    existing_rel['relationship_type']
                )
                if key not in new_rel_keys:
                    await self.write_repo.delete_relationship(*key)
            
            # Create new relationships
            existing_keys = {
                (r['from_entity_code'], r['to_entity_code'], r['relationship_type'])
                for r in existing
            }
            
            for rel in definition.relationships:
                key = (rel.from_entity, rel.to_entity, rel.relationship_type)
                if key not in existing_keys:
                    await self.write_repo.create_relationship(
                        from_entity_code=rel.from_entity,
                        to_entity_code=rel.to_entity,
                        relationship_type=rel.relationship_type,
                        from_cardinality=rel.from_cardinality,
                        to_cardinality=rel.to_cardinality,
                        metadata=rel.metadata_ if hasattr(rel, 'metadata_') else None
                    )
    
    async def delete_definition(
        self,
        code: str,
        kind: str,
        deleted_by: str
    ) -> None:
        """Soft delete definition.
        
        Args:
            code: Business identifier
            kind: Type of definition
            deleted_by: User deleting it
        """
        await self.write_repo.delete_definition(code, kind, deleted_by)
    
    async def search_definitions(
        self,
        kind: str,
        filters: Optional[Dict[str, Any]] = None,
        limit: int = 100,
        offset: int = 0
    ) -> List[ThingDefinition]:
        """Search definitions with filters.
        
        Args:
            kind: Type of definition
            filters: Optional filter criteria
            limit: Max results
            offset: Pagination offset
            
        Returns:
            List of Pydantic model instances
        """
        search_filters = {'kind': kind}
        if filters:
            search_filters.update(filters)
        
        results = await self.query_repo.search(search_filters, limit, offset)
        
        return [
            self.instantiation.instantiate(kind, r['data'])
            for r in results
        ]
    
    async def get_all_by_kind(
        self,
        kind: str,
        limit: Optional[int] = None,
        offset: int = 0
    ) -> List[ThingDefinition]:
        """Get all definitions of a specific kind.
        
        Args:
            kind: Type of definition
            limit: Max results
            offset: Pagination offset
            
        Returns:
            List of Pydantic model instances
        """
        results = await self.query_repo.get_all_by_kind(kind, limit=limit, offset=offset)
        
        return [
            self.instantiation.instantiate(kind, r['data'])
            for r in results
        ]
    
    async def get_knowledge_graph(
        self,
        entity_code: str,
        depth: int = 2,
        relationship_types: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Get knowledge graph around an entity.
        
        Args:
            entity_code: Starting entity code
            depth: Max traversal depth
            relationship_types: Filter by specific types
            
        Returns:
            Dict with nodes and edges
        """
        return await self.query_repo.get_relationship_graph(
            entity_code,
            depth=depth,
            relationship_types=relationship_types
        )
    
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
            limit: Max versions
            
        Returns:
            List of version dicts
        """
        return await self.query_repo.get_version_history(code, kind, limit)
    
    async def count_by_kind(self, kind: str) -> int:
        """Count definitions of a specific kind.
        
        Args:
            kind: Type of definition
            
        Returns:
            Count
        """
        return await self.query_repo.count_by_kind(kind)
    
    # -------------------------------------------------------------------------
    # Bulk operations
    # -------------------------------------------------------------------------
    
    async def bulk_create_definitions(
        self,
        definitions: List[ThingDefinition],
        created_by: str
    ) -> List[UUID]:
        """Bulk create definitions (for seeding).
        
        Args:
            definitions: List of Pydantic models
            created_by: User creating them
            
        Returns:
            List of UUIDs
        """
        definition_dicts = []
        
        for defn in definitions:
            kind = self.instantiation.get_kind_from_model(defn)
            code = self.instantiation.get_code_from_model(defn)
            name = self.instantiation.get_name_from_model(defn)
            data = self.instantiation.serialize(defn)
            
            if not code:
                raise ValueError(f"Definition must have a 'code' field: {kind}")
            
            definition_dicts.append({
                'kind': kind,
                'code': code,
                'name': name,
                'data': data
            })
        
        return await self.write_repo.bulk_upsert_definitions(definition_dicts, created_by)
    
    # -------------------------------------------------------------------------
    # Helper methods
    # -------------------------------------------------------------------------
    
    def _dict_to_relationship(self, rel_dict: Dict[str, Any]) -> RelationshipDefinition:
        """Convert relationship dict to Pydantic model."""
        return RelationshipDefinition(
            kind="relationship_definition",
            id=rel_dict['id'],
            name=f"{rel_dict['from_entity_code']} {rel_dict['relationship_type']} {rel_dict['to_entity_code']}",
            from_entity=rel_dict['from_entity_code'],
            to_entity=rel_dict['to_entity_code'],
            relationship_type=rel_dict['relationship_type'],
            from_cardinality=rel_dict.get('from_cardinality'),
            to_cardinality=rel_dict.get('to_cardinality'),
            metadata_=rel_dict.get('metadata', {})
        )
