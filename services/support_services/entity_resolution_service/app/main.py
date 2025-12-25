
import logging
from typing import List, Dict, Any
from fastapi import FastAPI, BackgroundTasks, HTTPException, Depends
from contextlib import asynccontextmanager
from datetime import datetime

from .config import get_settings
from .models import EntityRecord, MatchCandidate
from .engine.matching import MatchingEngine
from .api import router as api_router

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

settings = get_settings()

# Initialize Matching Engine
matching_engine = MatchingEngine(threshold=settings.MATCHING_THRESHOLD if hasattr(settings, 'MATCHING_THRESHOLD') else 0.85)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup (LLM-only, no spaCy)
    logger.info("Entity Resolution Service Starting (LLM-only mode)...")
    yield
    # Shutdown
    logger.info("Entity Resolution Service Shutting Down...")

app = FastAPI(
    title=settings.service_name,
    version="1.0.0",
    lifespan=lifespan,
    openapi_url="/api/v1/openapi.json"
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": settings.service_name}

# Include API router with semantic extraction endpoints
app.include_router(api_router, prefix="/api/v1/entity-resolution")

@app.post("/api/v1/resolve", response_model=List[Dict[str, Any]])
async def resolve_entity(record: EntityRecord):
    """
    Real-time entity resolution: Find matches for a single record against a known set.
    For now, this is a stateless check against provided candidates or a mock DB.
    """
    # In a real implementation, 'candidates' would be fetched from the Database Service
    # based on blocking keys (e.g., same zip code, same first letter of name).
    # Here we simulate with a dummy candidate list for the scaffold.
    mock_candidates = [
        EntityRecord(
            record_id="1", 
            source_system="CRM", 
            entity_type="Customer", 
            attributes={"name": "John Smith", "email": "john@example.com"}
        ),
        EntityRecord(
            record_id="2", 
            source_system="ERP", 
            entity_type="Customer", 
            attributes={"name": "Jane Doe", "email": "jane@example.com"}
        ),
        EntityRecord(
            record_id="3", 
            source_system="Legacy", 
            entity_type="Customer", 
            attributes={"name": "J. Smith", "email": "jsmith@test.com"}
        )
    ]
    
    matches = await matching_engine.find_matches(record, mock_candidates)
    return matches

async def run_batch_job(records: List[EntityRecord]):
    """Background task for batch processing."""
    logger.info(f"Starting batch processing for {len(records)} records")
    groups = await matching_engine.process_batch(records)
    logger.info(f"Batch complete. Found {len(groups)} duplicate groups.")
    # Here we would persist 'Golden Records' to the Database Service
    # and trigger retroactive fixes via Messaging Service.

@app.post("/api/v1/batch/process")
async def trigger_batch_process(records: List[EntityRecord], background_tasks: BackgroundTasks):
    """
    Trigger a batch processing job.
    """
    background_tasks.add_task(run_batch_job, records)
    return {"message": "Batch processing started", "record_count": len(records)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.service_host, port=settings.service_port)
