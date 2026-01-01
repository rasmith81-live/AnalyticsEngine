"""
Client Configuration Repository - Database operations for client configurations.

Uses async SQLAlchemy for database operations following CQRS patterns.
"""

import logging
from datetime import datetime
from typing import List, Optional, Dict, Any

from sqlalchemy import select, func, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from .db_models import (
    ClientConfiguration,
    ClientRecording,
    ClientIntent,
    ClientEntity,
    ClientValueChainModel
)
from .client_config_models import (
    CreateClientConfigurationRequest,
    UpdateClientConfigurationRequest,
    SaveRecordingRequest,
    SaveIntentRequest,
    SaveEntityRequest,
    SaveValueChainModelRequest,
    ClientConfigurationResponse,
    ClientRecordingResponse,
    ClientIntentResponse,
    ClientEntityResponse,
    ClientValueChainModelResponse,
    FullClientConfigurationResponse
)

logger = logging.getLogger(__name__)


class ClientConfigurationRepository:
    """Repository for client configuration database operations."""
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    # ========================================================================
    # Configuration CRUD
    # ========================================================================
    
    async def create_configuration(
        self,
        request: CreateClientConfigurationRequest
    ) -> ClientConfiguration:
        """Create a new client configuration."""
        config = ClientConfiguration(
            client_id=request.client_id,
            client_name=request.client_name,
            name=request.name,
            description=request.description,
            source_session_id=request.source_session_id
        )
        self.session.add(config)
        await self.session.flush()
        await self.session.refresh(config)
        return config
    
    async def get_configuration_by_id(self, config_id: int) -> Optional[ClientConfiguration]:
        """Get configuration by ID."""
        result = await self.session.execute(
            select(ClientConfiguration).where(ClientConfiguration.id == config_id)
        )
        return result.scalar_one_or_none()
    
    async def get_configuration_by_uuid(self, uuid: str) -> Optional[ClientConfiguration]:
        """Get configuration by UUID."""
        result = await self.session.execute(
            select(ClientConfiguration).where(ClientConfiguration.uuid == uuid)
        )
        return result.scalar_one_or_none()
    
    async def get_configurations_by_client(
        self,
        client_id: str,
        status: Optional[str] = None,
        page: int = 1,
        page_size: int = 20
    ) -> tuple[List[ClientConfiguration], int]:
        """Get configurations for a client with pagination."""
        query = select(ClientConfiguration).where(
            ClientConfiguration.client_id == client_id
        )
        
        if status:
            query = query.where(ClientConfiguration.status == status)
        
        # Get total count
        count_query = select(func.count()).select_from(query.subquery())
        total = (await self.session.execute(count_query)).scalar() or 0
        
        # Get paginated results
        query = query.order_by(ClientConfiguration.updated_at.desc())
        query = query.offset((page - 1) * page_size).limit(page_size)
        
        result = await self.session.execute(query)
        configs = list(result.scalars().all())
        
        return configs, total
    
    async def search_configurations(
        self,
        client_name: Optional[str] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        status: Optional[str] = None,
        page: int = 1,
        page_size: int = 20
    ) -> tuple[List[ClientConfiguration], int]:
        """Search configurations by client name and/or date range."""
        from datetime import datetime
        
        query = select(ClientConfiguration)
        
        # Filter by client name (case-insensitive partial match)
        if client_name:
            query = query.where(
                ClientConfiguration.client_name.ilike(f"%{client_name}%")
            )
        
        # Filter by date range
        if date_from:
            try:
                from_date = datetime.fromisoformat(date_from.replace('Z', '+00:00'))
                query = query.where(ClientConfiguration.created_at >= from_date)
            except ValueError:
                pass
        
        if date_to:
            try:
                to_date = datetime.fromisoformat(date_to.replace('Z', '+00:00'))
                query = query.where(ClientConfiguration.created_at <= to_date)
            except ValueError:
                pass
        
        # Filter by status
        if status:
            query = query.where(ClientConfiguration.status == status)
        
        # Get total count
        count_query = select(func.count()).select_from(query.subquery())
        total = (await self.session.execute(count_query)).scalar() or 0
        
        # Get paginated results
        query = query.order_by(ClientConfiguration.created_at.desc())
        query = query.offset((page - 1) * page_size).limit(page_size)
        
        result = await self.session.execute(query)
        configs = list(result.scalars().all())
        
        return configs, total
    
    async def update_configuration(
        self,
        config_id: int,
        request: UpdateClientConfigurationRequest
    ) -> Optional[ClientConfiguration]:
        """Update a configuration."""
        config = await self.get_configuration_by_id(config_id)
        if not config:
            return None
        
        if request.name is not None:
            config.name = request.name
        if request.description is not None:
            config.description = request.description
        if request.status is not None:
            config.status = request.status
        if request.version is not None:
            config.version = request.version
        
        config.updated_at = datetime.utcnow()
        await self.session.flush()
        await self.session.refresh(config)
        return config
    
    async def delete_configuration(self, config_id: int) -> bool:
        """Delete a configuration and all related data."""
        config = await self.get_configuration_by_id(config_id)
        if not config:
            return False
        
        await self.session.delete(config)
        await self.session.flush()
        return True
    
    # ========================================================================
    # Recording CRUD
    # ========================================================================
    
    async def add_recording(
        self,
        config_id: int,
        request: SaveRecordingRequest
    ) -> ClientRecording:
        """Add a recording to a configuration."""
        recording = ClientRecording(
            configuration_id=config_id,
            session_id=request.session_id,
            transcript=request.transcript,
            duration_seconds=request.duration_seconds,
            speaker_count=request.speaker_count,
            recorded_at=request.recorded_at,
            segments=request.segments
        )
        self.session.add(recording)
        await self.session.flush()
        await self.session.refresh(recording)
        return recording
    
    async def get_recordings(self, config_id: int) -> List[ClientRecording]:
        """Get all recordings for a configuration."""
        result = await self.session.execute(
            select(ClientRecording)
            .where(ClientRecording.configuration_id == config_id)
            .order_by(ClientRecording.recorded_at.desc())
        )
        return list(result.scalars().all())
    
    async def delete_recording(self, recording_id: int) -> bool:
        """Delete a recording."""
        result = await self.session.execute(
            delete(ClientRecording).where(ClientRecording.id == recording_id)
        )
        await self.session.flush()
        return result.rowcount > 0
    
    # ========================================================================
    # Intent CRUD
    # ========================================================================
    
    async def add_intent(
        self,
        config_id: int,
        request: SaveIntentRequest
    ) -> ClientIntent:
        """Add an intent to a configuration."""
        intent = ClientIntent(
            configuration_id=config_id,
            name=request.name,
            description=request.description,
            confidence=request.confidence,
            domain=request.domain,
            category=request.category,
            target_entities=request.target_entities,
            requested_metrics=request.requested_metrics,
            parameters=request.parameters,
            source_utterance=request.source_utterance
        )
        self.session.add(intent)
        await self.session.flush()
        await self.session.refresh(intent)
        return intent
    
    async def add_intents_bulk(
        self,
        config_id: int,
        requests: List[SaveIntentRequest]
    ) -> List[ClientIntent]:
        """Add multiple intents to a configuration."""
        intents = []
        for req in requests:
            intent = ClientIntent(
                configuration_id=config_id,
                name=req.name,
                description=req.description,
                confidence=req.confidence,
                domain=req.domain,
                category=req.category,
                target_entities=req.target_entities,
                requested_metrics=req.requested_metrics,
                parameters=req.parameters,
                source_utterance=req.source_utterance
            )
            self.session.add(intent)
            intents.append(intent)
        
        await self.session.flush()
        for intent in intents:
            await self.session.refresh(intent)
        return intents
    
    async def get_intents(self, config_id: int) -> List[ClientIntent]:
        """Get all intents for a configuration."""
        result = await self.session.execute(
            select(ClientIntent)
            .where(ClientIntent.configuration_id == config_id)
            .order_by(ClientIntent.created_at.desc())
        )
        return list(result.scalars().all())
    
    async def delete_intent(self, intent_id: int) -> bool:
        """Delete an intent."""
        result = await self.session.execute(
            delete(ClientIntent).where(ClientIntent.id == intent_id)
        )
        await self.session.flush()
        return result.rowcount > 0
    
    # ========================================================================
    # Entity CRUD
    # ========================================================================
    
    async def add_entity(
        self,
        config_id: int,
        request: SaveEntityRequest
    ) -> ClientEntity:
        """Add an entity to a configuration."""
        entity = ClientEntity(
            configuration_id=config_id,
            name=request.name,
            entity_type=request.entity_type,
            description=request.description,
            properties=request.properties,
            related_entities=request.related_entities,
            extraction_confidence=request.extraction_confidence,
            source_context=request.source_context
        )
        self.session.add(entity)
        await self.session.flush()
        await self.session.refresh(entity)
        return entity
    
    async def add_entities_bulk(
        self,
        config_id: int,
        requests: List[SaveEntityRequest]
    ) -> List[ClientEntity]:
        """Add multiple entities to a configuration."""
        entities = []
        for req in requests:
            entity = ClientEntity(
                configuration_id=config_id,
                name=req.name,
                entity_type=req.entity_type,
                description=req.description,
                properties=req.properties,
                related_entities=req.related_entities,
                extraction_confidence=req.extraction_confidence,
                source_context=req.source_context
            )
            self.session.add(entity)
            entities.append(entity)
        
        await self.session.flush()
        for entity in entities:
            await self.session.refresh(entity)
        return entities
    
    async def get_entities(self, config_id: int) -> List[ClientEntity]:
        """Get all entities for a configuration."""
        result = await self.session.execute(
            select(ClientEntity)
            .where(ClientEntity.configuration_id == config_id)
            .order_by(ClientEntity.name)
        )
        return list(result.scalars().all())
    
    async def delete_entity(self, entity_id: int) -> bool:
        """Delete an entity."""
        result = await self.session.execute(
            delete(ClientEntity).where(ClientEntity.id == entity_id)
        )
        await self.session.flush()
        return result.rowcount > 0
    
    # ========================================================================
    # Value Chain Model CRUD
    # ========================================================================
    
    async def add_value_chain_model(
        self,
        config_id: int,
        request: SaveValueChainModelRequest
    ) -> ClientValueChainModel:
        """Add a value chain model to a configuration."""
        model = ClientValueChainModel(
            configuration_id=config_id,
            name=request.name,
            description=request.description,
            version=request.version,
            nodes=[node.model_dump() for node in request.nodes],
            links=[link.model_dump() for link in request.links],
            generated_from_session=request.generated_from_session,
            generation_method=request.generation_method
        )
        self.session.add(model)
        await self.session.flush()
        await self.session.refresh(model)
        return model
    
    async def get_value_chain_models(self, config_id: int) -> List[ClientValueChainModel]:
        """Get all value chain models for a configuration."""
        result = await self.session.execute(
            select(ClientValueChainModel)
            .where(ClientValueChainModel.configuration_id == config_id)
            .order_by(ClientValueChainModel.created_at.desc())
        )
        return list(result.scalars().all())
    
    async def get_active_value_chain_model(self, config_id: int) -> Optional[ClientValueChainModel]:
        """Get the active value chain model for a configuration."""
        result = await self.session.execute(
            select(ClientValueChainModel)
            .where(ClientValueChainModel.configuration_id == config_id)
            .where(ClientValueChainModel.is_active == True)
            .order_by(ClientValueChainModel.created_at.desc())
            .limit(1)
        )
        return result.scalar_one_or_none()
    
    async def delete_value_chain_model(self, model_id: int) -> bool:
        """Delete a value chain model."""
        result = await self.session.execute(
            delete(ClientValueChainModel).where(ClientValueChainModel.id == model_id)
        )
        await self.session.flush()
        return result.rowcount > 0
    
    # ========================================================================
    # Full Configuration Operations
    # ========================================================================
    
    async def get_full_configuration(self, config_id: int) -> Optional[FullClientConfigurationResponse]:
        """Get a configuration with all related data."""
        config = await self.get_configuration_by_id(config_id)
        if not config:
            return None
        
        recordings = await self.get_recordings(config_id)
        intents = await self.get_intents(config_id)
        entities = await self.get_entities(config_id)
        models = await self.get_value_chain_models(config_id)
        
        return FullClientConfigurationResponse(
            configuration=ClientConfigurationResponse(
                id=config.id,
                uuid=config.uuid,
                client_id=config.client_id,
                client_name=config.client_name,
                name=config.name,
                description=config.description,
                version=config.version,
                status=config.status,
                source_session_id=config.source_session_id,
                created_at=config.created_at,
                updated_at=config.updated_at,
                recording_count=len(recordings),
                intent_count=len(intents),
                entity_count=len(entities),
                model_count=len(models)
            ),
            recordings=[ClientRecordingResponse.model_validate(r) for r in recordings],
            intents=[ClientIntentResponse.model_validate(i) for i in intents],
            entities=[ClientEntityResponse.model_validate(e) for e in entities],
            value_chain_models=[ClientValueChainModelResponse.model_validate(m) for m in models]
        )
