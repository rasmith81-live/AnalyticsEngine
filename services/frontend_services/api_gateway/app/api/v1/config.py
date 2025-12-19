
from typing import List, Dict, Any
from fastapi import APIRouter, Depends
from ...clients.config_client import DemoConfigServiceClient
from ...api.dependencies import get_config_client

router = APIRouter()

@router.get("/clients")
async def get_client_configs(
    client: DemoConfigServiceClient = Depends(get_config_client)
):
    return await client.get_client_configs()

@router.get("/clients/{client_id}")
async def get_client_config(
    client_id: str,
    client: DemoConfigServiceClient = Depends(get_config_client)
):
    return await client.get_client_config(client_id)

@router.post("/clients")
async def create_client_config(
    config: Dict[str, Any],
    client: DemoConfigServiceClient = Depends(get_config_client)
):
    return await client.create_client_config(config)

@router.put("/clients/{client_id}")
async def update_client_config(
    client_id: str,
    config: Dict[str, Any],
    client: DemoConfigServiceClient = Depends(get_config_client)
):
    return await client.update_client_config(client_id, config)

@router.get("/clients/{client_id}/custom-kpis")
async def get_custom_kpis(
    client_id: str,
    client: DemoConfigServiceClient = Depends(get_config_client)
):
    return await client.get_custom_kpis(client_id)

@router.post("/clients/{client_id}/custom-kpis")
async def create_custom_kpi(
    client_id: str,
    kpi: Dict[str, Any],
    client: DemoConfigServiceClient = Depends(get_config_client)
):
    return await client.create_custom_kpi(client_id, kpi)

@router.post("/clients/{client_id}/proposal")
async def generate_proposal(
    client_id: str,
    options: Dict[str, Any],
    client: DemoConfigServiceClient = Depends(get_config_client)
):
    return await client.generate_proposal(client_id, options)

@router.get("/clients/{client_id}/proposal")
async def get_proposal(
    client_id: str,
    client: DemoConfigServiceClient = Depends(get_config_client)
):
    return await client.get_proposal(client_id)

@router.put("/clients/{client_id}/proposal")
async def update_proposal(
    client_id: str,
    proposal: Dict[str, Any],
    client: DemoConfigServiceClient = Depends(get_config_client)
):
    return await client.update_proposal(client_id, proposal)
