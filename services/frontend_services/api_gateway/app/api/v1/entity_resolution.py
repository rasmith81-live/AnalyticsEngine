
from typing import List, Dict, Any
from fastapi import APIRouter, Depends
from ...clients.entity_resolution_client import EntityResolutionServiceClient
from ...api.dependencies import get_entity_resolution_client

router = APIRouter()

@router.post("/matching/run")
async def run_matching_job(
    payload: Dict[str, Any],
    client: EntityResolutionServiceClient = Depends(get_entity_resolution_client)
):
    source_records = payload.get("source_records", [])
    threshold = payload.get("threshold", 0.85)
    return await client.run_matching_job(source_records, threshold)

@router.post("/merging/create-golden-record")
async def create_golden_record(
    payload: Dict[str, Any],
    client: EntityResolutionServiceClient = Depends(get_entity_resolution_client)
):
    match_candidate_ids = payload.get("match_candidate_ids", [])
    strategy = payload.get("strategy", "frequency_based")
    return await client.create_golden_record(match_candidate_ids, strategy)

@router.post("/retroactive/fix")
async def trigger_retroactive_fix(
    entity_id: str,
    client: EntityResolutionServiceClient = Depends(get_entity_resolution_client)
):
    return await client.trigger_retroactive_fix(entity_id)
