
from typing import List, Dict, Any
from fastapi import APIRouter, Depends
from ...clients.connector_client import ConnectorServiceClient
from ...api.dependencies import get_connector_client

router = APIRouter()

@router.post("/connections")
async def create_connection(
    profile: Dict[str, Any],
    client: ConnectorServiceClient = Depends(get_connector_client)
):
    return await client.create_connection(profile)

@router.get("/connections/{connection_id}")
async def get_connection(
    connection_id: str,
    client: ConnectorServiceClient = Depends(get_connector_client)
):
    return await client.get_connection(connection_id)

@router.post("/connections/test")
async def test_connection(
    profile: Dict[str, Any],
    client: ConnectorServiceClient = Depends(get_connector_client)
):
    return await client.test_connection(profile)

@router.post("/discovery/schema")
async def discover_schema(
    connection_id: str,
    client: ConnectorServiceClient = Depends(get_connector_client)
):
    return await client.discover_schema(connection_id)

@router.post("/discovery/preview")
async def preview_data(
    connection_id: str,
    table_name: str,
    limit: int = 5,
    client: ConnectorServiceClient = Depends(get_connector_client)
):
    return await client.preview_data(connection_id, table_name, limit)
