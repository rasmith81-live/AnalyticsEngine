
from typing import List, Dict, Any
from fastapi import APIRouter, Depends, UploadFile, File
from ...clients.metadata_ingestion_client import MetadataIngestionServiceClient
from ...api.dependencies import get_metadata_ingestion_client

router = APIRouter()

@router.get("/knowledge/industries")
async def list_industries(
    client: MetadataIngestionServiceClient = Depends(get_metadata_ingestion_client)
):
    return await client.list_industries()

@router.get("/knowledge/industries/{code}/value-chain")
async def get_industry_value_chain(
    code: str,
    client: MetadataIngestionServiceClient = Depends(get_metadata_ingestion_client)
):
    return await client.get_industry_value_chain(code)

@router.get("/knowledge/industries/{code}/kpis")
async def get_industry_kpis(
    code: str,
    client: MetadataIngestionServiceClient = Depends(get_metadata_ingestion_client)
):
    return await client.get_industry_kpis(code)

@router.post("/mapping/decompose")
async def decompose_kpi(
    payload: Dict[str, Any],
    client: MetadataIngestionServiceClient = Depends(get_metadata_ingestion_client)
):
    formula = payload.get("formula")
    return await client.decompose_kpi(formula)

@router.post("/import/upload")
async def upload_excel(
    file: UploadFile = File(...),
    client: MetadataIngestionServiceClient = Depends(get_metadata_ingestion_client)
):
    return await client.upload_excel(file)

@router.post("/import/{import_id}/enrich")
async def enrich_import(
    import_id: str,
    client: MetadataIngestionServiceClient = Depends(get_metadata_ingestion_client)
):
    """Optional AI enrichment - extracts entities using LLM."""
    return await client.enrich_import(import_id)

@router.post("/import/{import_id}/commit")
async def commit_import(
    import_id: str,
    client: MetadataIngestionServiceClient = Depends(get_metadata_ingestion_client)
):
    return await client.commit_import(import_id)
