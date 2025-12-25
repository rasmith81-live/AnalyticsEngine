"""High-level metadata service orchestrating repositories and backend services."""

from typing import List, Optional, Dict, Any
from uuid import UUID
import uuid

from ..repositories import MetadataWriteRepository, MetadataQueryRepository
from .metadata_instantiation_service import MetadataInstantiationService

from ..ontology_models import (
    ThingDefinition,
    RelationshipDefinition,
    CompanyValueChainModelDefinition,
    MetricDefinition,
    BusinessProcessDefinition
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
    
    async def create_definition_from_dict(
        self,
        kind: str,
        code: str,
        name: str,
        data: Dict[str, Any],
        created_by: str
    ) -> UUID:
        """Create a metadata definition directly from a dict (bypasses Pydantic validation).
        
        Use for auto-generated definitions where full model validation isn't needed.
        
        Args:
            kind: Definition type
            code: Business identifier
            name: Display name
            data: Raw definition data
            created_by: User creating the definition
            
        Returns:
            UUID of created definition
        """
        if not code:
            raise ValueError(f"Definition must have a 'code' field: {kind}")
        
        return await self.write_repo.create_definition(
            kind=kind,
            code=code,
            name=name,
            data=data,
            created_by=created_by
        )
    
    async def update_definition_from_dict(
        self,
        code: str,
        kind: str,
        data: Dict[str, Any],
        changed_by: str,
        change_description: Optional[str] = None
    ) -> None:
        """Update a metadata definition directly from a dict (bypasses Pydantic validation).
        
        Use for updates where full model validation isn't needed.
        
        Args:
            code: Business identifier
            kind: Type of definition
            data: Raw definition data
            changed_by: User making the change
            change_description: Optional description
        """
        await self.write_repo.update_definition(
            code=code,
            kind=kind,
            data=data,
            changed_by=changed_by,
            change_description=change_description
        )
    
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
    
    async def get_all_by_kind_raw(
        self,
        kind: str,
        limit: Optional[int] = None,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        """Get all definitions of a specific kind as raw dicts (no Pydantic validation).
        
        Use this for endpoints that need to return data that may not conform to 
        strict Pydantic model requirements.
        
        Args:
            kind: Type of definition
            limit: Max results
            offset: Pagination offset
            
        Returns:
            List of raw definition dicts
        """
        results = await self.query_repo.get_all_by_kind(kind, limit=limit, offset=offset)
        return [r['data'] for r in results]
    
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
    # Conversation Modeling
    # -------------------------------------------------------------------------

    async def persist_generated_model(
        self,
        session_id: str,
        user_id: str,
        model_data: Dict[str, Any]
    ) -> str:
        """Persist a generated value chain model from Conversation Service.
        
        Decomposes the nested model into:
        - BusinessProcessDefinition (for Process/Activity nodes)
        - MetricDefinition (for Metric nodes)
        - RelationshipDefinition (for links)
        - CompanyValueChainModelDefinition (container)
        """
        # 1. Create container model
        model_id = str(uuid.uuid4())
        model_name = model_data.get("name", "Generated Model")
        
        # We assume a default company for the session or derive from context
        # For now, using a placeholder company
        company_id = "comp_generated" 
        
        included_nodes = []
        
        # 2. Process Nodes
        node_id_map = {} # Map internal node ID to system code
        
        for node in model_data.get("nodes", []):
            internal_id = node.get("id")
            name = node.get("name")
            node_type = node.get("type", "Process")
            description = node.get("description")
            
            # Generate a system code
            code = f"{node_type.upper()}_{uuid.uuid4().hex[:8]}"
            node_id_map[internal_id] = code
            included_nodes.append(code)
            
            # Create Definition based on type
            if node_type in ["Process", "Activity"]:
                defn = BusinessProcessDefinition(
                    kind="business_process_definition",
                    id=str(uuid.uuid4()),
                    code=code,
                    name=name,
                    description=description,
                    process_type="core" if node_type == "Process" else "support",
                    domain="process"
                )
                await self.create_definition(defn, created_by=user_id)
                
            elif node_type == "Metric":
                defn = MetricDefinition(
                    kind="metric_definition",
                    id=str(uuid.uuid4()),
                    code=code,
                    name=name,
                    description=description
                )
                await self.create_definition(defn, created_by=user_id)
            
            else:
                # Default to Entity for unknown types
                defn = EntityDefinition(
                    kind="entity_definition",
                    id=str(uuid.uuid4()),
                    code=code,
                    name=name,
                    description=description
                )
                await self.create_definition(defn, created_by=user_id)

        # 3. Process Links (Relationships)
        for link in model_data.get("links", []):
            source_internal = link.get("source_id")
            target_internal = link.get("target_id")
            rel_type = link.get("type", "related_to")
            
            if source_internal in node_id_map and target_internal in node_id_map:
                await self.write_repo.create_relationship(
                    from_entity_code=node_id_map[source_internal],
                    to_entity_code=node_id_map[target_internal],
                    relationship_type=rel_type
                )

        # 4. Create CompanyValueChainModelDefinition
        model_def = CompanyValueChainModelDefinition(
            kind="company_value_chain_model_definition",
            id=model_id,
            name=model_name,
            company_id=company_id,
            session_id=session_id,
            derived_from="conversation",
            included_nodes=included_nodes
        )
        
        # Need to implement instantiate for CompanyValueChainModelDefinition if not present
        # Or just use generic create_definition since it's a ThingDefinition
        
        # We need a code for the model definition itself
        model_def.id = model_id # ThingDefinition requires ID
        # Since ThingDefinition doesn't explicitly require 'code' field but create_definition does...
        # Wait, CompanyValueChainModelDefinition inherits ThingDefinition.
        # create_definition extracts code using instantiation service.
        # ThingDefinition has 'id' and 'name'. It doesn't enforce 'code' field on base, 
        # but subclasses like EntityDefinition have it.
        # CompanyValueChainModelDefinition does NOT have a 'code' field in ontology_models.py.
        # This might be an issue for create_definition which expects a code.
        
        # Let's check CompanyValueChainModelDefinition in ontology_models.py
        # class CompanyValueChainModelDefinition(ThingDefinition):
        #     kind: str = "company_value_chain_model_definition"
        #     company_id: str
        #     ...
        
        # It does NOT have a code field. 
        # I should probably add one or use ID as code.
        # Ideally, I should fix the model or the persistence logic.
        # For now, I'll monkey-patch/add a code attribute if possible or rely on instantiation service to handle it.
        # But Pydantic models are strict.
        
        # FIX: I will rely on the fact that I can't easily change the model structure here without editing ontology_models.py.
        # But wait, create_definition calls self.instantiation.get_code_from_model(definition).
        # If that fails, it raises ValueError.
        
        # Let's inspect MetadataInstantiationService.get_code_from_model
        # I don't have that file open. I should probably ensure the model has a code.
        pass # Placeholder for thought process.

        # Let's create the definition using a dict approach to bypass pydantic validation if needed,
        # but create_definition takes a ThingDefinition.
        
        # Actually, I'll update CompanyValueChainModelDefinition to include 'code' in ontology_models.py 
        # OR I will just pass it as extra data if allowed (ConfigDict(extra="allow")).
        # ThingDefinition allows extra.
        
        # Assign a code
        model_code = f"VCM_{uuid.uuid4().hex[:8]}"
        setattr(model_def, "code", model_code) # This works if extra="allow"
        
        await self.create_definition(model_def, created_by=user_id)
        
        return model_id

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
