
from typing import List, Dict, Any
from fastapi import APIRouter, Depends
from ...clients.metadata_client import MetadataServiceClient
from ...api.dependencies import get_metadata_client

router = APIRouter()

@router.get("/kpis")
async def get_kpis(
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    return await client.get_kpis()

@router.get("/kpis/{code}")
async def get_kpi(
    code: str,
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    return await client.get_kpi(code)

@router.get("/kpis/module/{code}")
async def get_kpis_by_module(
    code: str,
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    return await client.get_kpis_by_module(code)

@router.get("/kpis/value-chain/{code}")
async def get_kpis_by_value_chain(
    code: str,
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    return await client.get_kpis_by_value_chain(code)

@router.get("/object-models")
async def get_object_models(
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    return await client.get_object_models()

@router.get("/object-models/{code}")
async def get_object_model(
    code: str,
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    return await client.get_object_model(code)

@router.get("/object-models/module/{code}")
async def get_object_models_by_module(
    code: str,
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    return await client.get_object_models_by_module(code)

@router.get("/modules")
async def get_modules(
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    return await client.get_modules()

@router.get("/modules/{code}")
async def get_module(
    code: str,
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    return await client.get_module(code)

@router.get("/modules/value-chain/{code}")
async def get_modules_by_value_chain(
    code: str,
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    return await client.get_modules_by_value_chain(code)

@router.get("/value-chains")
async def get_value_chains(
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    return await client.get_value_chains()

@router.get("/value-chains/{code}")
async def get_value_chain(
    code: str,
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    return await client.get_value_chain(code)

@router.get("/industries")
async def get_industries(
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    return await client.get_industries()

@router.get("/industries/{code}")
async def get_industry(
    code: str,
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    return await client.get_industry(code)

@router.get("/industries/{code}/value-chains")
async def get_value_chains_by_industry(
    code: str,
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    return await client.get_value_chains_by_industry(code)

@router.get("/definitions/{kind}")
async def get_definitions_by_kind(
    kind: str,
    limit: int = 100,
    offset: int = 0,
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    """Proxy to business_metadata definitions endpoint."""
    return await client.get_definitions(kind, limit, offset)

@router.get("/relationships")
async def get_all_relationships(
    relationship_type: str = None,
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    """Get all relationships, optionally filtered by type."""
    return await client.get_all_relationships(relationship_type)

@router.get("/relationships/{entity_code}")
async def get_entity_relationships(
    entity_code: str,
    direction: str = "both",
    relationship_type: str = None,
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    """Get relationships for a specific entity."""
    return await client.get_entity_relationships(entity_code, direction, relationship_type)

@router.put("/definitions/{kind}/{code}")
async def update_definition(
    kind: str,
    code: str,
    definition: Dict[str, Any],
    changed_by: str = "admin",
    change_description: str = None,
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    """Proxy PUT to business_metadata definitions endpoint."""
    return await client.update_definition(kind, code, definition, changed_by, change_description)

@router.delete("/definitions/{kind}/{code}")
async def delete_definition(
    kind: str,
    code: str,
    deleted_by: str = "admin",
    client: MetadataServiceClient = Depends(get_metadata_client)
):
    """Proxy DELETE to business_metadata definitions endpoint."""
    return await client.delete_definition(kind, code, deleted_by)
