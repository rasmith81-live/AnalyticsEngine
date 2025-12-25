
import logging
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
import os

# Add backend services to path
backend_services_path = Path(__file__).parent.parent.parent.parent / "backend_services"
sys.path.insert(0, str(backend_services_path))

from database_service.app.messaging_client import MessagingClient
from app.pipeline import PipelineOrchestrator, IngestionJob
from app.transformation_engine import TransformationEngine

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global instances
messaging_client: Optional[MessagingClient] = None
pipeline_orchestrator: Optional[PipelineOrchestrator] = None
transformation_engine = TransformationEngine()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan."""
    global messaging_client, pipeline_orchestrator
    
    # Initialize messaging client
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
    messaging_client = MessagingClient(
        redis_url=redis_url,
        service_name="ingestion_service",
        pool_size=5
    )
    await messaging_client.connect()
    logger.info("MessagingClient connected")
    
    # Initialize pipeline orchestrator with messaging client
    pipeline_orchestrator = PipelineOrchestrator(messaging_client=messaging_client)
    logger.info("PipelineOrchestrator initialized")
    
    yield
    
    # Cleanup
    if messaging_client:
        await messaging_client.disconnect()
        logger.info("MessagingClient disconnected")

app = FastAPI(
    title="Ingestion Service",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "ingestion_service"}

@app.post("/jobs")
async def create_ingestion_job(job: IngestionJob):
    """Create a new ingestion job."""
    job_id = await pipeline_orchestrator.create_job(job)
    return {"job_id": job_id, "status": "created"}

@app.post("/jobs/{job_id}/run")
async def run_ingestion_job(job_id: str, background_tasks: BackgroundTasks):
    """Trigger an ingestion job immediately."""
    # Run in background
    background_tasks.add_task(pipeline_orchestrator.run_job, job_id)
    return {"message": "Job execution started", "job_id": job_id}

@app.get("/jobs/{job_id}")
async def get_job_status(job_id: str):
    job = pipeline_orchestrator.jobs.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@app.post("/transform/preview")
async def preview_transformation(data: List[Dict[str, Any]], rules: List[Dict[str, Any]]):
    """Preview transformation rules on sample data."""
    import pandas as pd
    try:
        df = pd.DataFrame(data)
        result_df = await transformation_engine.apply_transformations(df, rules)
        return result_df.to_dict(orient="records")
    except Exception as e:
        logger.error(f"Transformation preview failed: {e}")
        raise HTTPException(status_code=400, detail=str(e))
