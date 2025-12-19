
from typing import List, Dict, Any
from fastapi import APIRouter, Depends
from ...clients.ingestion_client import IngestionServiceClient
from ...api.dependencies import get_ingestion_client

router = APIRouter()

@router.post("/jobs")
async def create_job(
    job: Dict[str, Any],
    client: IngestionServiceClient = Depends(get_ingestion_client)
):
    return await client.create_job(job)

@router.post("/jobs/{job_id}/run")
async def run_job(
    job_id: str,
    client: IngestionServiceClient = Depends(get_ingestion_client)
):
    return await client.run_job(job_id)

@router.get("/jobs/{job_id}")
async def get_job_status(
    job_id: str,
    client: IngestionServiceClient = Depends(get_ingestion_client)
):
    return await client.get_job_status(job_id)

@router.post("/transform/preview")
async def preview_transformation(
    payload: Dict[str, Any],
    client: IngestionServiceClient = Depends(get_ingestion_client)
):
    data = payload.get("data", [])
    rules = payload.get("rules", [])
    return await client.preview_transformation(data, rules)
