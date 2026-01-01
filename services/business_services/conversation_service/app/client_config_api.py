"""
Client Configuration API Router.

Provides endpoints for saving and loading client configurations,
including recordings, intents, entities, and value chain models.
"""

import logging
from typing import List, Optional
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from .database import get_db_session
from .client_config_repository import ClientConfigurationRepository
from .client_config_models import (
    CreateClientConfigurationRequest,
    UpdateClientConfigurationRequest,
    SaveRecordingRequest,
    SaveIntentRequest,
    SaveEntityRequest,
    SaveValueChainModelRequest,
    SaveFullConfigurationRequest,
    ClientConfigurationResponse,
    ClientRecordingResponse,
    ClientIntentResponse,
    ClientEntityResponse,
    ClientValueChainModelResponse,
    FullClientConfigurationResponse,
    ClientConfigurationListResponse
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/client-config", tags=["Client Configuration"])


# ============================================================================
# Configuration Endpoints
# ============================================================================

@router.post("/configurations", response_model=ClientConfigurationResponse)
async def create_configuration(
    request: CreateClientConfigurationRequest,
    session: AsyncSession = Depends(get_db_session)
):
    """Create a new client configuration."""
    repo = ClientConfigurationRepository(session)
    config = await repo.create_configuration(request)
    
    return ClientConfigurationResponse(
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
        recording_count=0,
        intent_count=0,
        entity_count=0,
        model_count=0
    )


@router.get("/configurations/{config_id}", response_model=FullClientConfigurationResponse)
async def get_configuration(
    config_id: int,
    session: AsyncSession = Depends(get_db_session)
):
    """Get a client configuration with all related data."""
    repo = ClientConfigurationRepository(session)
    result = await repo.get_full_configuration(config_id)
    
    if not result:
        raise HTTPException(status_code=404, detail="Configuration not found")
    
    return result


@router.get("/configurations/by-uuid/{uuid}", response_model=FullClientConfigurationResponse)
async def get_configuration_by_uuid(
    uuid: str,
    session: AsyncSession = Depends(get_db_session)
):
    """Get a client configuration by UUID."""
    repo = ClientConfigurationRepository(session)
    config = await repo.get_configuration_by_uuid(uuid)
    
    if not config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    
    result = await repo.get_full_configuration(config.id)
    return result


@router.get("/search", response_model=ClientConfigurationListResponse)
async def search_configurations(
    client_name: Optional[str] = Query(None, description="Filter by client name (partial match)"),
    date_from: Optional[str] = Query(None, description="Filter by date from (ISO format)"),
    date_to: Optional[str] = Query(None, description="Filter by date to (ISO format)"),
    status: Optional[str] = Query(None, description="Filter by status (draft, active, archived)"),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    session: AsyncSession = Depends(get_db_session)
):
    """Search configurations by client name and/or date range."""
    repo = ClientConfigurationRepository(session)
    configs, total = await repo.search_configurations(
        client_name=client_name,
        date_from=date_from,
        date_to=date_to,
        status=status,
        page=page,
        page_size=page_size
    )
    
    items = []
    for config in configs:
        recordings = await repo.get_recordings(config.id)
        intents = await repo.get_intents(config.id)
        entities = await repo.get_entities(config.id)
        models = await repo.get_value_chain_models(config.id)
        
        items.append(ClientConfigurationResponse(
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
        ))
    
    return ClientConfigurationListResponse(
        items=items,
        total=total,
        page=page,
        page_size=page_size
    )


@router.get("/clients/{client_id}/configurations", response_model=ClientConfigurationListResponse)
async def list_client_configurations(
    client_id: str,
    status: Optional[str] = Query(None, description="Filter by status (draft, active, archived)"),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    session: AsyncSession = Depends(get_db_session)
):
    """List configurations for a client."""
    repo = ClientConfigurationRepository(session)
    configs, total = await repo.get_configurations_by_client(
        client_id=client_id,
        status=status,
        page=page,
        page_size=page_size
    )
    
    items = []
    for config in configs:
        recordings = await repo.get_recordings(config.id)
        intents = await repo.get_intents(config.id)
        entities = await repo.get_entities(config.id)
        models = await repo.get_value_chain_models(config.id)
        
        items.append(ClientConfigurationResponse(
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
        ))
    
    return ClientConfigurationListResponse(
        items=items,
        total=total,
        page=page,
        page_size=page_size
    )


@router.patch("/configurations/{config_id}", response_model=ClientConfigurationResponse)
async def update_configuration(
    config_id: int,
    request: UpdateClientConfigurationRequest,
    session: AsyncSession = Depends(get_db_session)
):
    """Update a client configuration."""
    repo = ClientConfigurationRepository(session)
    config = await repo.update_configuration(config_id, request)
    
    if not config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    
    recordings = await repo.get_recordings(config.id)
    intents = await repo.get_intents(config.id)
    entities = await repo.get_entities(config.id)
    models = await repo.get_value_chain_models(config.id)
    
    return ClientConfigurationResponse(
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
    )


@router.delete("/configurations/{config_id}")
async def delete_configuration(
    config_id: int,
    session: AsyncSession = Depends(get_db_session)
):
    """Delete a client configuration and all related data."""
    repo = ClientConfigurationRepository(session)
    deleted = await repo.delete_configuration(config_id)
    
    if not deleted:
        raise HTTPException(status_code=404, detail="Configuration not found")
    
    return {"message": "Configuration deleted successfully"}


# ============================================================================
# Recording Endpoints
# ============================================================================

@router.post("/configurations/{config_id}/recordings", response_model=ClientRecordingResponse)
async def add_recording(
    config_id: int,
    request: SaveRecordingRequest,
    session: AsyncSession = Depends(get_db_session)
):
    """Add a recording to a configuration."""
    repo = ClientConfigurationRepository(session)
    
    config = await repo.get_configuration_by_id(config_id)
    if not config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    
    recording = await repo.add_recording(config_id, request)
    return ClientRecordingResponse.model_validate(recording)


@router.get("/configurations/{config_id}/recordings", response_model=List[ClientRecordingResponse])
async def get_recordings(
    config_id: int,
    session: AsyncSession = Depends(get_db_session)
):
    """Get all recordings for a configuration."""
    repo = ClientConfigurationRepository(session)
    recordings = await repo.get_recordings(config_id)
    return [ClientRecordingResponse.model_validate(r) for r in recordings]


# ============================================================================
# Intent Endpoints
# ============================================================================

@router.post("/configurations/{config_id}/intents", response_model=ClientIntentResponse)
async def add_intent(
    config_id: int,
    request: SaveIntentRequest,
    session: AsyncSession = Depends(get_db_session)
):
    """Add an intent to a configuration."""
    repo = ClientConfigurationRepository(session)
    
    config = await repo.get_configuration_by_id(config_id)
    if not config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    
    intent = await repo.add_intent(config_id, request)
    return ClientIntentResponse.model_validate(intent)


@router.post("/configurations/{config_id}/intents/bulk", response_model=List[ClientIntentResponse])
async def add_intents_bulk(
    config_id: int,
    requests: List[SaveIntentRequest],
    session: AsyncSession = Depends(get_db_session)
):
    """Add multiple intents to a configuration."""
    repo = ClientConfigurationRepository(session)
    
    config = await repo.get_configuration_by_id(config_id)
    if not config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    
    intents = await repo.add_intents_bulk(config_id, requests)
    return [ClientIntentResponse.model_validate(i) for i in intents]


@router.get("/configurations/{config_id}/intents", response_model=List[ClientIntentResponse])
async def get_intents(
    config_id: int,
    session: AsyncSession = Depends(get_db_session)
):
    """Get all intents for a configuration."""
    repo = ClientConfigurationRepository(session)
    intents = await repo.get_intents(config_id)
    return [ClientIntentResponse.model_validate(i) for i in intents]


# ============================================================================
# Entity Endpoints
# ============================================================================

@router.post("/configurations/{config_id}/entities", response_model=ClientEntityResponse)
async def add_entity(
    config_id: int,
    request: SaveEntityRequest,
    session: AsyncSession = Depends(get_db_session)
):
    """Add an entity to a configuration."""
    repo = ClientConfigurationRepository(session)
    
    config = await repo.get_configuration_by_id(config_id)
    if not config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    
    entity = await repo.add_entity(config_id, request)
    return ClientEntityResponse.model_validate(entity)


@router.post("/configurations/{config_id}/entities/bulk", response_model=List[ClientEntityResponse])
async def add_entities_bulk(
    config_id: int,
    requests: List[SaveEntityRequest],
    session: AsyncSession = Depends(get_db_session)
):
    """Add multiple entities to a configuration."""
    repo = ClientConfigurationRepository(session)
    
    config = await repo.get_configuration_by_id(config_id)
    if not config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    
    entities = await repo.add_entities_bulk(config_id, requests)
    return [ClientEntityResponse.model_validate(e) for e in entities]


@router.get("/configurations/{config_id}/entities", response_model=List[ClientEntityResponse])
async def get_entities(
    config_id: int,
    session: AsyncSession = Depends(get_db_session)
):
    """Get all entities for a configuration."""
    repo = ClientConfigurationRepository(session)
    entities = await repo.get_entities(config_id)
    return [ClientEntityResponse.model_validate(e) for e in entities]


# ============================================================================
# Value Chain Model Endpoints
# ============================================================================

@router.post("/configurations/{config_id}/models", response_model=ClientValueChainModelResponse)
async def add_value_chain_model(
    config_id: int,
    request: SaveValueChainModelRequest,
    session: AsyncSession = Depends(get_db_session)
):
    """Add a value chain model to a configuration."""
    repo = ClientConfigurationRepository(session)
    
    config = await repo.get_configuration_by_id(config_id)
    if not config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    
    model = await repo.add_value_chain_model(config_id, request)
    return ClientValueChainModelResponse.model_validate(model)


@router.get("/configurations/{config_id}/models", response_model=List[ClientValueChainModelResponse])
async def get_value_chain_models(
    config_id: int,
    session: AsyncSession = Depends(get_db_session)
):
    """Get all value chain models for a configuration."""
    repo = ClientConfigurationRepository(session)
    models = await repo.get_value_chain_models(config_id)
    return [ClientValueChainModelResponse.model_validate(m) for m in models]


@router.get("/configurations/{config_id}/models/active", response_model=ClientValueChainModelResponse)
async def get_active_value_chain_model(
    config_id: int,
    session: AsyncSession = Depends(get_db_session)
):
    """Get the active value chain model for a configuration."""
    repo = ClientConfigurationRepository(session)
    model = await repo.get_active_value_chain_model(config_id)
    
    if not model:
        raise HTTPException(status_code=404, detail="No active model found")
    
    return ClientValueChainModelResponse.model_validate(model)


# ============================================================================
# Full Configuration Save (Convenience Endpoint)
# ============================================================================

@router.post("/save-full", response_model=FullClientConfigurationResponse)
async def save_full_configuration(
    request: SaveFullConfigurationRequest,
    session: AsyncSession = Depends(get_db_session)
):
    """
    Save a complete configuration with all components in one request.
    
    This is a convenience endpoint for saving everything from a conversation session.
    """
    repo = ClientConfigurationRepository(session)
    
    # Create configuration
    config = await repo.create_configuration(request.configuration)
    
    # Add recordings
    if request.recordings:
        for rec_req in request.recordings:
            await repo.add_recording(config.id, rec_req)
    
    # Add intents
    if request.intents:
        await repo.add_intents_bulk(config.id, request.intents)
    
    # Add entities
    if request.entities:
        await repo.add_entities_bulk(config.id, request.entities)
    
    # Add value chain model
    if request.value_chain_model:
        await repo.add_value_chain_model(config.id, request.value_chain_model)
    
    # Return full configuration
    result = await repo.get_full_configuration(config.id)
    return result
