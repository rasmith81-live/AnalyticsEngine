
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
