"""
API endpoints for Machine Learning Service.

This module provides the API endpoints for Model Registry, Training Jobs, and Inference.
"""

import logging
import uuid
import asyncio
from datetime import datetime
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status, BackgroundTasks
from pydantic import BaseModel, Field

from ..messaging_client import MessagingClient
from ..database_client import DatabaseClient
from ..dependencies import get_messaging_client, get_database_client, get_service_uptime
from ..models import (
    MLModelCreate, MLModelResponse,
    ModelVersionCreate, ModelVersionResponse,
    TrainingJobCreate, TrainingJobResponse,
    InferenceRequest, InferenceResponse, PredictionResult,
    ModelType, ModelStatus, JobStatus,
    ServiceHealth, DependencyStatus
)

# Configure logging
logger = logging.getLogger(__name__)

# Initialize router
router = APIRouter()

# --- Health Check ---

@router.get("/status", response_model=ServiceHealth)
async def get_service_status(
    messaging_client: MessagingClient = Depends(get_messaging_client),
    database_client: DatabaseClient = Depends(get_database_client)
):
    """
    Get the current status of Machine Learning Service and its dependencies.
    """
    dependencies = []
    
    # Check messaging connection
    try:
        start_time = datetime.utcnow()
        msg_health = await messaging_client.check_health()
        end_time = datetime.utcnow()
        response_time = (end_time - start_time).total_seconds() * 1000
        
        is_healthy = isinstance(msg_health, dict) and msg_health.get("status") in ["ok", "healthy", "operational"]
        
        dependencies.append(DependencyStatus(
            service_name="messaging_service",
            url=messaging_client.base_url,
            status="healthy" if is_healthy else "unhealthy",
            response_time_ms=response_time,
            last_check=end_time,
            error=None if is_healthy else str(msg_health)
        ))
    except Exception as e:
        dependencies.append(DependencyStatus(
            service_name="messaging_service",
            url="unknown",
            status="unhealthy",
            response_time_ms=0,
            last_check=datetime.utcnow(),
            error=str(e)
        ))

    # Check database connection
    try:
        start_time = datetime.utcnow()
        db_health = await database_client.check_health()
        end_time = datetime.utcnow()
        response_time = (end_time - start_time).total_seconds() * 1000
        
        is_healthy = isinstance(db_health, dict) and db_health.get("status") in ["ok", "healthy", "operational"]
        
        dependencies.append(DependencyStatus(
            service_name="database_service",
            url=database_client.base_url,
            status="healthy" if is_healthy else "unhealthy",
            response_time_ms=response_time,
            last_check=end_time,
            error=None if is_healthy else str(db_health)
        ))
    except Exception as e:
        dependencies.append(DependencyStatus(
            service_name="database_service",
            url="unknown",
            status="unhealthy",
            response_time_ms=0,
            last_check=datetime.utcnow(),
            error=str(e)
        ))

    overall_status = "healthy" if all(d.status == "healthy" for d in dependencies) else "degraded"

    return ServiceHealth(
        status=overall_status,
        timestamp=datetime.utcnow(),
        dependencies=dependencies,
        active_subscriptions=len(messaging_client.active_subscriptions),
        uptime_seconds=get_service_uptime(),
        version="1.0.0",
        error=None if overall_status == "healthy" else "Dependencies unhealthy"
    )


# --- Model Registry Endpoints ---

@router.post("/models", response_model=MLModelResponse, status_code=status.HTTP_202_ACCEPTED)
async def create_model(
    model: MLModelCreate,
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Register a new ML Model.
    Publishes a CreateModelCommand to the ecosystem.
    """
    model_id = str(uuid.uuid4())
    correlation_id = str(uuid.uuid4())
    
    try:
        # Publish command
        await messaging_client.publish_command(
            command_type="CreateModelCommand",
            payload={
                "id": model_id,
                **model.dict()
            },
            correlation_id=correlation_id
        )
        
        # Return accepted response with generated ID
        # In a real system, we might return a 202 and a location header, 
        # or wait for the event if we had synchronous consistency.
        return MLModelResponse(
            id=model_id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            latest_version=None,
            **model.dict()
        )
    except Exception as e:
        logger.error(f"Error creating model: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/models/{model_id}", response_model=MLModelResponse)
async def get_model(
    model_id: str,
    database_client: DatabaseClient = Depends(get_database_client)
):
    """
    Get model details.
    """
    try:
        model_data = await database_client.get_model(model_id)
        if not model_data:
            raise HTTPException(status_code=404, detail=f"Model {model_id} not found")
            
        return MLModelResponse(**model_data)
    except Exception as e:
        logger.error(f"Error retrieving model {model_id}: {e}")
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(status_code=500, detail=f"Failed to retrieve model: {str(e)}")


@router.post("/models/{model_id}/versions", response_model=ModelVersionResponse, status_code=status.HTTP_202_ACCEPTED)
async def create_model_version(
    model_id: str,
    version: ModelVersionCreate,
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Register a new version for a model.
    """
    if version.model_id != model_id:
        raise HTTPException(status_code=400, detail="Model ID mismatch in body and path")
        
    version_id = str(uuid.uuid4())
    correlation_id = str(uuid.uuid4())
    
    try:
        await messaging_client.publish_command(
            command_type="CreateVersionCommand",
            payload={
                "id": version_id,
                **version.dict()
            },
            correlation_id=correlation_id
        )
        
        return ModelVersionResponse(
            id=version_id,
            created_at=datetime.utcnow(),
            **version.dict()
        )
    except Exception as e:
        logger.error(f"Error creating model version: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# --- Training Job Endpoints ---

@router.post("/jobs", response_model=TrainingJobResponse, status_code=status.HTTP_202_ACCEPTED)
async def start_training_job(
    job: TrainingJobCreate,
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Launch a training job.
    """
    job_id = str(uuid.uuid4())
    correlation_id = str(uuid.uuid4())
    
    try:
        await messaging_client.publish_command(
            command_type="StartTrainingJobCommand",
            payload={
                "id": job_id,
                **job.dict()
            },
            correlation_id=correlation_id
        )
        
        return TrainingJobResponse(
            id=job_id,
            status=JobStatus.PENDING,
            progress=0,
            started_at=datetime.utcnow(),
            **job.dict()
        )
    except Exception as e:
        logger.error(f"Error starting training job: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/jobs/{job_id}", response_model=TrainingJobResponse)
async def get_job_status(
    job_id: str,
    database_client: DatabaseClient = Depends(get_database_client)
):
    """
    Get training job status.
    """
    try:
        job_data = await database_client.get_job(job_id)
        if not job_data:
            raise HTTPException(status_code=404, detail=f"Training job {job_id} not found")
            
        return TrainingJobResponse(**job_data)
    except Exception as e:
        logger.error(f"Error retrieving job {job_id}: {e}")
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(status_code=500, detail=f"Failed to retrieve training job: {str(e)}")


# --- Inference Endpoints ---

@router.post("/inference", response_model=InferenceResponse)
async def run_inference(
    request: InferenceRequest,
    # In a real scenario, this might need to call a Model Serving microservice 
    # or load the model locally. For this architecture, we'll simulate logic.
):
    """
    Run inference using a registered model.
    NOTE: This is a simulation for the demo environment.
    """
    # Simulate processing time
    await asyncio.sleep(0.1) 
    
    # Mock logic based on input
    predictions = []
    
    # Handle single dict or list of dicts
    inputs = request.features if isinstance(request.features, list) else [request.features]
    
    for feature_set in inputs:
        # Mock prediction logic (random-ish but deterministic for same input)
        # Assuming classification for demo
        seed = sum(str(v).count('a') for v in feature_set.values()) # silly hash
        score = (seed % 100) / 100.0
        
        prediction = "Positive" if score > 0.5 else "Negative"
        
        predictions.append(PredictionResult(
            prediction=prediction,
            probability=score if score > 0.5 else 1-score,
            explanation={"feature_importance_mock": 0.8}
        ))
    
    return InferenceResponse(
        model_id=request.model_id,
        version=request.version or "latest",
        results=predictions,
        inference_time_ms=100.0
    )
