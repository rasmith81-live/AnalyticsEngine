
import logging
from typing import List, Dict, Any
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel

from app.pipeline import pipeline_orchestrator, IngestionJob
from app.transformation_engine import TransformationEngine

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Ingestion Service", version="1.0.0")

transformation_engine = TransformationEngine()

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
