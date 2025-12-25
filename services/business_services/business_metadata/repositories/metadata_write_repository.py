"""Write repository for metadata (CQRS Command Side).

Integrates with:
- database_service for database operations
- messaging_service for event publishing
"""

import hashlib
import json
import logging
from typing import List, Optional
from uuid import UUID
from datetime import datetime

logger = logging.getLogger(__name__)

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert

import sys
from pathlib import Path
backend_services_path = Path(__file__).parent.parent.parent.parent / "backend_services"
sys.path.insert(0, str(backend_services_path))

from messaging_service.app.event_publisher import EventPublisher

from ..models import MetadataDefinition, MetadataRelationship, MetadataVersion


class MetadataWriteRepository:
    """Handles all write operations for metadata (CQRS Command Side).
    
    Features:
    - Create, Update, Delete operations
    - Version tracking
    - Relationship management
    - Event publishing for all changes
    - Bulk operations for seeding
    """
    
    def __init__(self, session: AsyncSession, event_publisher: EventPublisher):
        """Initialize write repository.
        
        Args:
            session: Database session from database_service
            event_publisher: Event publisher from messaging_service
        """
        self.session = session
        self.event_publisher = event_publisher
    
    def _compute_hash(self, data: dict) -> str:
        """Compute hash of metadata for change detection."""
        json_str = json.dumps(data, sort_keys=True)
        return hashlib.sha256(json_str.encode()).hexdigest()
    
    async def create_definition(
        self,
        kind: str,
        code: str,
        name: str,
        data: dict,
        created_by: str,
        metadata_hash: Optional[str] = None
    ) -> UUID:
        """Create a new metadata definition.
        
        Args:
            kind: Type of definition (e.g., "entity_definition")
            code: Business identifier
            name: Human-readable name
            data: Full Pydantic model as dict
            created_by: User who created it
            metadata_hash: Optional hash for change detection
            
        Returns:
            UUID of created definition
        """
        if not metadata_hash:
            metadata_hash = self._compute_hash(data)
        
        definition = MetadataDefinition(
            kind=kind,
            code=code,
            name=name,
            version=1,
            data=data,
            created_by=created_by,
            is_active=True,
            metadata_hash=metadata_hash
        )
        
        self.session.add(definition)
        
        # Create version history entry
        await self._create_version_entry(
            code=code,
            kind=kind,
            version=1,
            data=data,
            change_type="created",
            changed_by=created_by
        )
        
        await self.session.flush()
        
        # Publish event
        await self._publish_event(
            event_type="created",
            kind=kind,
            code=code,
            version=1,
            changed_by=created_by
        )
        
        return definition.id
    
    async def update_definition(
        self,
        code: str,
        kind: str,
        data: dict,
        changed_by: str,
        change_description: Optional[str] = None
    ) -> None:
        """Update existing definition (creates new version).
        
        Args:
            code: Business identifier
            kind: Type of definition
            data: Updated Pydantic model as dict
            changed_by: User who made the change
            change_description: Optional description of changes
        """
        # Get current version
        stmt = select(MetadataDefinition).where(
            MetadataDefinition.code == code,
            MetadataDefinition.kind == kind,
            MetadataDefinition.is_active == True
        )
        result = await self.session.execute(stmt)
        current = result.scalar_one_or_none()
        
        if not current:
            raise ValueError(f"Definition not found: {kind}:{code}")
        
        # Check if data actually changed
        new_hash = self._compute_hash(data)
        if new_hash == current.metadata_hash:
            return  # No changes
        
        # Increment version
        new_version = current.version + 1
        
        # Update definition
        stmt = (
            update(MetadataDefinition)
            .where(
                MetadataDefinition.code == code,
                MetadataDefinition.kind == kind,
                MetadataDefinition.is_active == True
            )
            .values(
                data=data,
                version=new_version,
                updated_at=datetime.utcnow(),
                metadata_hash=new_hash
            )
        )
        await self.session.execute(stmt)
        
        # Create version history entry
        await self._create_version_entry(
            code=code,
            kind=kind,
            version=new_version,
            data=data,
            change_type="updated",
            changed_by=changed_by,
            change_description=change_description
        )
        
        # Publish event
        await self._publish_event(
            event_type="updated",
            kind=kind,
            code=code,
            version=new_version,
            changed_by=changed_by,
            change_description=change_description
        )
    
    async def delete_definition(
        self,
        code: str,
        kind: str,
        deleted_by: str
    ) -> None:
        """Soft delete definition (set is_active = False).
        
        Args:
            code: Business identifier
            kind: Type of definition
            deleted_by: User who deleted it
        """
        # Get current definition
        stmt = select(MetadataDefinition).where(
            MetadataDefinition.code == code,
            MetadataDefinition.kind == kind,
            MetadataDefinition.is_active == True
        )
        result = await self.session.execute(stmt)
        current = result.scalar_one_or_none()
        
        if not current:
            raise ValueError(f"Definition not found: {kind}:{code}")
        
        # Soft delete
        stmt = (
            update(MetadataDefinition)
            .where(
                MetadataDefinition.code == code,
                MetadataDefinition.kind == kind,
                MetadataDefinition.is_active == True
            )
            .values(
                is_active=False,
                updated_at=datetime.utcnow()
            )
        )
        await self.session.execute(stmt)
        
        # Create version history entry
        await self._create_version_entry(
            code=code,
            kind=kind,
            version=current.version,
            data=current.data,
            change_type="deleted",
            changed_by=deleted_by
        )
        
        # Publish event
        await self._publish_event(
            event_type="deleted",
            kind=kind,
            code=code,
            version=current.version,
            changed_by=deleted_by
        )
    
    async def create_relationship(
        self,
        from_entity_code: str,
        to_entity_code: str,
        relationship_type: str,
        from_cardinality: Optional[str] = None,
        to_cardinality: Optional[str] = None,
        metadata: Optional[dict] = None
    ) -> UUID:
        """Create a relationship between entities.
        
        Args:
            from_entity_code: Source entity code
            to_entity_code: Target entity code
            relationship_type: Type of relationship
            from_cardinality: Source cardinality (e.g., "1", "*")
            to_cardinality: Target cardinality
            metadata: Optional metadata about the relationship
            
        Returns:
            UUID of created relationship
        """
        # Check if active relationship already exists to prevent duplicates
        stmt = select(MetadataRelationship).where(
            MetadataRelationship.from_entity_code == from_entity_code,
            MetadataRelationship.to_entity_code == to_entity_code,
            MetadataRelationship.relationship_type == relationship_type,
            MetadataRelationship.is_active == True
        )
        result = await self.session.execute(stmt)
        existing = result.scalar_one_or_none()
        
        if existing:
            # If exists, update metadata if provided and return existing ID
            if metadata:
                existing.metadata_ = metadata  # Note: model uses metadata_ not metadata
            return existing.id

        relationship = MetadataRelationship(
            from_entity_code=from_entity_code,
            to_entity_code=to_entity_code,
            relationship_type=relationship_type,
            from_cardinality=from_cardinality,
            to_cardinality=to_cardinality,
            metadata=metadata,
            is_active=True
        )
        
        self.session.add(relationship)
        await self.session.flush()
        
        # Publish event (skip if publisher doesn't have the method)
        try:
            if hasattr(self.event_publisher, 'publish_message'):
                await self.event_publisher.publish_message(
                    channel="metadata.relationship.created",
                    payload={
                        "from_entity_code": from_entity_code,
                        "to_entity_code": to_entity_code,
                        "relationship_type": relationship_type,
                        "timestamp": datetime.utcnow().isoformat()
                    }
                )
        except Exception as e:
            logger.warning(f"Failed to publish relationship created event: {e}")
        
        return relationship.id
    
    async def delete_relationship(
        self,
        from_entity_code: str,
        to_entity_code: str,
        relationship_type: str
    ) -> None:
        """Soft delete a relationship.
        
        Args:
            from_entity_code: Source entity code
            to_entity_code: Target entity code
            relationship_type: Type of relationship
        """
        stmt = (
            update(MetadataRelationship)
            .where(
                MetadataRelationship.from_entity_code == from_entity_code,
                MetadataRelationship.to_entity_code == to_entity_code,
                MetadataRelationship.relationship_type == relationship_type,
                MetadataRelationship.is_active == True
            )
            .values(is_active=False)
        )
        await self.session.execute(stmt)
        
        # Publish event (skip if publisher doesn't have the method)
        try:
            if hasattr(self.event_publisher, 'publish_message'):
                await self.event_publisher.publish_message(
                    channel="metadata.relationship.deleted",
                    payload={
                        "from_entity_code": from_entity_code,
                        "to_entity_code": to_entity_code,
                        "relationship_type": relationship_type,
                        "timestamp": datetime.utcnow().isoformat()
                    }
                )
        except Exception as e:
            logger.warning(f"Failed to publish relationship deleted event: {e}")
    
    async def bulk_upsert_definitions(
        self,
        definitions: List[dict],
        created_by: str
    ) -> List[UUID]:
        """Bulk insert/update definitions (for seeding).
        
        Uses PostgreSQL INSERT ... ON CONFLICT for efficiency.
        
        Args:
            definitions: List of definition dicts with keys: kind, code, name, data
            created_by: User performing the bulk operation
            
        Returns:
            List of UUIDs (new or existing)
        """
        ids = []
        
        for defn in definitions:
            # Use ON CONFLICT to handle duplicates - update existing records
            stmt = insert(MetadataDefinition).values(
                kind=defn['kind'],
                code=defn['code'],
                name=defn['name'],
                version=1,
                data=defn['data'],
                created_by=created_by,
                is_active=True,
                metadata_hash=self._compute_hash(defn['data'])
            ).on_conflict_do_update(
                index_elements=['kind', 'code'],  # Unique constraint on (kind, code)
                set_={
                    'name': defn['name'],
                    'data': defn['data'],
                    'metadata_hash': self._compute_hash(defn['data']),
                    'updated_at': datetime.utcnow()
                }
            ).returning(MetadataDefinition.id)
            
            result = await self.session.execute(stmt)
            ids.append(result.scalar_one())
        
        # Publish bulk event (skip for now if publisher not available)
        try:
            if hasattr(self.event_publisher, 'publish'):
                await self.event_publisher.publish(
                    topic="metadata.bulk.upserted",
                    message={
                        "count": len(definitions),
                        "created_by": created_by,
                        "timestamp": datetime.utcnow().isoformat()
                    }
                )
        except Exception:
            pass  # Event publishing is optional
        
        return ids
    
    async def _create_version_entry(
        self,
        code: str,
        kind: str,
        version: int,
        data: dict,
        change_type: str,
        changed_by: str,
        change_description: Optional[str] = None
    ) -> None:
        """Create version history entry."""
        version_entry = MetadataVersion(
            definition_code=code,
            definition_kind=kind,
            version=version,
            data=data,
            change_type=change_type,
            changed_by=changed_by,
            change_description=change_description
        )
        self.session.add(version_entry)
    
    async def _publish_event(
        self,
        event_type: str,
        kind: str,
        code: str,
        version: int,
        changed_by: str,
        change_description: Optional[str] = None
    ) -> None:
        """Publish metadata change event to messaging service."""
        try:
            await self.event_publisher.publish_message(
                channel=f"metadata.{kind}.{event_type}",
                payload={
                    "event_type": event_type,
                    "kind": kind,
                    "code": code,
                    "version": version,
                    "changed_by": changed_by,
                    "change_description": change_description,
                    "timestamp": datetime.utcnow().isoformat()
                }
            )
        except Exception as e:
            logger.warning(f"Failed to publish {event_type} event for {kind}:{code}: {e}")
