
import logging
import sys
import os
from pathlib import Path
from typing import List, Dict, Any, Optional
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, BackgroundTasks, Body
from pydantic import BaseModel

# Add backend services to path
backend_services_path = Path(__file__).parent.parent.parent.parent / "backend_services"
sys.path.insert(0, str(backend_services_path))

from database_service.app.messaging_client import MessagingClient
from app.engine.matching import BatchMatcher
from app.engine.merging import MergeEngine
from app.engine.retroactive_fix import RetroactiveFixEngine

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global instances
messaging_client: Optional[MessagingClient] = None
matcher: Optional[BatchMatcher] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan."""
    global messaging_client, matcher
    
    # Initialize messaging client
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
    messaging_client = MessagingClient(
        redis_url=redis_url,
        service_name="entity_resolution_service",
        pool_size=5
    )
    await messaging_client.connect()
    logger.info("MessagingClient connected")
    
    # Initialize matcher
    matcher = BatchMatcher()
    logger.info("BatchMatcher initialized")
    
    yield
    
    # Cleanup
    if messaging_client:
        await messaging_client.disconnect()
        logger.info("MessagingClient disconnected")

app = FastAPI(
    title="Entity Resolution Service",
    version="1.0.0",
    lifespan=lifespan
)


# Request Models
class MatchRequest(BaseModel):
    source_records: List[Dict[str, Any]]
    threshold: float = 0.85

class MergeRequest(BaseModel):
    match_candidate_ids: List[str]
    strategy: str = "frequency_based" # or "recency_based", "source_priority"

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "entity_resolution_service"}

@app.post("/matching/run")
async def run_matching_job(request: MatchRequest, background_tasks: BackgroundTasks):
    """
    Trigger a batch matching job.
    """
    try:
        # Convert dicts to internal SourceRecord objects if needed
        # For now, assuming the engine handles the logic or we adapt here
        # This is a stub implementation to expose the endpoint
        job_id = "job_" + str(len(request.source_records)) # Mock ID
        
        logger.info(f"Starting matching job {job_id} for {len(request.source_records)} records")
        
        # Publish event that matching job started
        if messaging_client:
            await messaging_client.publish_event(
                event_type="entity.matching.started",
                payload={
                    "job_id": job_id,
                    "record_count": len(request.source_records),
                    "threshold": request.threshold
                },
                correlation_id=job_id
            )
        
        return {"job_id": job_id, "status": "queued", "message": "Matching job started"}
    except Exception as e:
        logger.error(f"Error starting matching job: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/merging/create-golden-record")
async def create_golden_record(request: MergeRequest):
    """
    Create a golden record from matched candidates.
    """
    golden_record_id = f"gr_{len(request.match_candidate_ids)}"
    
    # Publish event that golden record was created
    if messaging_client:
        await messaging_client.publish_event(
            event_type="entity.golden_record.created",
            payload={
                "golden_record_id": golden_record_id,
                "candidate_ids": request.match_candidate_ids,
                "strategy": request.strategy
            },
            correlation_id=golden_record_id
        )
        logger.info(f"Published entity.golden_record.created event for {golden_record_id}")
    
    return {"golden_record_id": golden_record_id, "status": "created"}

@app.post("/retroactive/fix")
async def trigger_retroactive_fix(entity_id: str):
    """
    Trigger retroactive fix for an entity.
    """
    task_id = f"fix_{entity_id}"
    
    # Publish event that retroactive fix started
    if messaging_client:
        await messaging_client.publish_event(
            event_type="entity.retroactive_fix.started",
            payload={
                "task_id": task_id,
                "entity_id": entity_id
            },
            correlation_id=task_id
        )
        logger.info(f"Published entity.retroactive_fix.started event for {entity_id}")
    
    return {"task_id": task_id, "status": "processing"}
