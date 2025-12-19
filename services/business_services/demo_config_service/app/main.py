"""
Demo/Config Service

Handles client configuration, custom KPI creation, and service proposal generation.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Any
import httpx
import random

import math

from .config import get_settings
from .models import (
    ClientConfigCreate, ClientConfigUpdate, ClientConfigResponse,
    CustomKPICreate, CustomKPIResponse,
    RequiredObjectsAnalysisRequest, RequiredObjectsAnalysisResponse,
    ServiceProposalCreate, ServiceProposalResponse, ServiceProposalUpdate,
    DataSourceCreate, DataSourceResponse,
    DemoDataRequest,
    IntegrationMethod, ProposalStatus
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# In-memory storage (replace with database in production)
client_configs = {}
custom_kpis = {}
service_proposals = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan."""
    settings = get_settings()
    
    logger.info(f"Starting {settings.service_name} v{settings.version}")
    logger.info(f"Environment: {settings.environment}")
    
    yield
    
    logger.info("Shutting down Demo/Config Service")


# Create FastAPI app
app = FastAPI(
    title="Demo/Config Service",
    description="Client configuration and service proposal generation",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
settings = get_settings()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================================
# Root Endpoints
# ============================================================================

@app.get("/")
async def root():
    """Root endpoint with service information."""
    settings = get_settings()
    
    return {
        "service": settings.service_name,
        "version": settings.version,
        "environment": settings.environment,
        "status": "healthy",
        "endpoints": {
            "configs": "/api/configs",
            "custom_kpis": "/api/configs/{client_id}/custom-kpis",
            "analysis": "/api/analysis/required-objects",
            "proposals": "/api/proposals",
            "demo": "/api/demo",
            "docs": "/docs",
            "health": "/health"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    settings = get_settings()
    
    return {
        "status": "healthy",
        "service": settings.service_name,
        "version": settings.version,
        "configs_count": len(client_configs),
        "custom_kpis_count": len(custom_kpis),
        "proposals_count": len(service_proposals)
    }


# ============================================================================
# Client Configuration Endpoints
# ============================================================================

@app.get("/api/configs", response_model=List[ClientConfigResponse])
async def list_client_configs():
    """List all client configurations."""
    return list(client_configs.values())


@app.get("/api/configs/{client_id}", response_model=ClientConfigResponse)
async def get_client_config(client_id: str):
    """Get client configuration by ID."""
    if client_id not in client_configs:
        raise HTTPException(status_code=404, detail=f"Client config not found: {client_id}")
    
    return client_configs[client_id]


@app.post("/api/configs", response_model=ClientConfigResponse)
async def create_client_config(config: ClientConfigCreate):
    """Create new client configuration."""
    client_id = str(uuid.uuid4())
    config_id = str(uuid.uuid4())
    
    now = datetime.utcnow()
    
    client_config = ClientConfigResponse(
        id=config_id,
        client_id=client_id,
        client_name=config.client_name,
        selected_kpis=config.selected_kpis,
        custom_kpis=[],
        data_sources=config.data_sources,
        deployment_config=config.deployment_config,
        license_key=None,
        license_expiration=None,
        created_at=now,
        updated_at=now
    )
    
    client_configs[client_id] = client_config
    
    logger.info(f"Created client config: {client_id} - {config.client_name}")
    
    return client_config


@app.put("/api/configs/{client_id}", response_model=ClientConfigResponse)
async def update_client_config(client_id: str, config: ClientConfigUpdate):
    """Update client configuration."""
    if client_id not in client_configs:
        raise HTTPException(status_code=404, detail=f"Client config not found: {client_id}")
    
    existing = client_configs[client_id]
    
    # Update fields
    if config.client_name is not None:
        existing.client_name = config.client_name
    if config.selected_kpis is not None:
        existing.selected_kpis = config.selected_kpis
    if config.data_sources is not None:
        existing.data_sources = config.data_sources
    if config.deployment_config is not None:
        existing.deployment_config = config.deployment_config
    
    existing.updated_at = datetime.utcnow()
    
    # Cascade changes (publish event)
    changes = config.model_dump(exclude_unset=True)
    if changes:
        await _publish_config_change(client_id, changes)
    
    logger.info(f"Updated client config: {client_id}")
    
    return existing


async def _publish_config_change(client_id: str, changes: Dict[str, Any]):
    """Publish configuration change event to messaging service."""
    settings = get_settings()
    
    event = {
        "event_type": "client_config_updated",
        "client_id": client_id,
        "changes": changes,
        "timestamp": datetime.utcnow().isoformat()
    }
    
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            # Fire and forget pattern for demo purposes, or await response
            await client.post(
                f"{settings.messaging_service_url}/publish",
                json={
                    "channel": "config.updates",
                    "message": event
                }
            )
            logger.info(f"Published config update event for client {client_id}")
    except Exception as e:
        logger.error(f"Failed to publish config update event: {e}")


@app.delete("/api/configs/{client_id}")
async def delete_client_config(client_id: str):
    """Delete client configuration."""
    if client_id not in client_configs:
        raise HTTPException(status_code=404, detail=f"Client config not found: {client_id}")
    
    del client_configs[client_id]
    
    # Also delete associated custom KPIs
    client_custom_kpis = [k for k, v in custom_kpis.items() if v.client_id == client_id]
    for kpi_id in client_custom_kpis:
        del custom_kpis[kpi_id]
    
    logger.info(f"Deleted client config: {client_id}")
    
    return {"status": "deleted", "client_id": client_id}


# ============================================================================
# Custom KPI Endpoints
# ============================================================================

@app.get("/api/configs/{client_id}/custom-kpis", response_model=List[CustomKPIResponse])
async def list_custom_kpis(client_id: str):
    """List custom KPIs for a client."""
    if client_id not in client_configs:
        raise HTTPException(status_code=404, detail=f"Client config not found: {client_id}")
    
    client_kpis = [kpi for kpi in custom_kpis.values() if kpi.client_id == client_id]
    
    return client_kpis


@app.post("/api/configs/{client_id}/custom-kpis", response_model=CustomKPIResponse)
async def create_custom_kpi(client_id: str, kpi: CustomKPICreate):
    """Create custom KPI for a client."""
    if client_id not in client_configs:
        raise HTTPException(status_code=404, detail=f"Client config not found: {client_id}")
    
    kpi_id = str(uuid.uuid4())
    
    custom_kpi = CustomKPIResponse(
        id=kpi_id,
        client_id=client_id,
        kpi_code=kpi.kpi_code,
        source_kpi_code=kpi.source_kpi_code,
        name=kpi.name,
        formula=kpi.formula,
        unit=kpi.unit,
        description=kpi.description,
        calculation_logic=kpi.calculation_logic,
        required_objects=kpi.required_objects,
        metadata_=kpi.metadata_,
        created_by=kpi.created_by,
        created_at=datetime.utcnow()
    )
    
    custom_kpis[kpi_id] = custom_kpi
    
    logger.info(f"Created custom KPI: {kpi.kpi_code} for client {client_id}")
    
    return custom_kpi


# ============================================================================
# Analysis Endpoints
# ============================================================================

@app.post("/api/analysis/required-objects", response_model=RequiredObjectsAnalysisResponse)
async def analyze_required_objects(request: RequiredObjectsAnalysisRequest):
    """
    Analyze required object models for selected KPIs.
    
    Calls the metadata service to get KPI definitions and aggregates all required objects.
    """
    settings = get_settings()
    required_objects = set()
    object_details = {}
    
    # Call metadata service for each KPI
    async with httpx.AsyncClient(timeout=30.0) as client:
        for kpi_code in request.kpi_codes:
            try:
                # Fetch KPI definition from metadata service
                response = await client.get(
                    f"{settings.metadata_service_url}/kpis/{kpi_code}"
                )
                
                if response.status_code == 200:
                    kpi_data = response.json()
                    kpi_required_objects = kpi_data.get("required_objects", [])
                    
                    # Add to set
                    for obj in kpi_required_objects:
                        required_objects.add(obj)
                        
                        # Fetch object model details if not already fetched
                        if obj not in object_details:
                            try:
                                obj_response = await client.get(
                                    f"{settings.metadata_service_url}/object-models/{obj}"
                                )
                                if obj_response.status_code == 200:
                                    object_details[obj] = obj_response.json()
                            except Exception as e:
                                logger.warning(f"Could not fetch object model {obj}: {e}")
                                
            except Exception as e:
                logger.error(f"Error fetching KPI {kpi_code}: {e}")
                # Continue with other KPIs
    
    return RequiredObjectsAnalysisResponse(
        kpi_codes=request.kpi_codes,
        required_objects=list(required_objects),
        object_details=object_details,
        total_objects=len(required_objects),
        uml_diagram=None  # Could generate UML from object_details if needed
    )


# ============================================================================
# Service Proposal Endpoints
# ============================================================================

@app.post("/api/proposals", response_model=ServiceProposalResponse)
async def create_service_proposal(proposal: ServiceProposalCreate):
    """Generate service proposal based on selected KPIs."""
    settings = get_settings()
    
    # Analyze required objects
    analysis = await analyze_required_objects(
        RequiredObjectsAnalysisRequest(kpi_codes=proposal.kpi_codes)
    )
    
    # Calculate estimates
    num_objects = len(analysis.required_objects)
    
    if proposal.integration_method == IntegrationMethod.BATCH:
        hours_per_object = settings.batch_integration_hours_per_object
    else:
        hours_per_object = settings.realtime_integration_hours_per_object
    
    estimated_hours = num_objects * hours_per_object
    estimated_cost = estimated_hours * settings.default_hourly_rate
    timeline_weeks = max(4, estimated_hours // 40)  # Minimum 4 weeks
    
    proposal_id = str(uuid.uuid4())
    
    service_proposal = ServiceProposalResponse(
        id=proposal_id,
        client_id=proposal.client_id,
        required_objects=analysis.required_objects,
        integration_method=proposal.integration_method,
        estimated_hours=estimated_hours,
        estimated_cost=estimated_cost,
        timeline_weeks=timeline_weeks,
        status=ProposalStatus.DRAFT,
        breakdown={
            "kpi_count": len(proposal.kpi_codes),
            "object_count": num_objects,
            "hours_per_object": hours_per_object,
            "hourly_rate": settings.default_hourly_rate,
            "phases": [
                {"name": "Discovery & Planning", "weeks": 1},
                {"name": "Integration Development", "weeks": timeline_weeks - 3},
                {"name": "Testing & UAT", "weeks": 1},
                {"name": "Deployment", "weeks": 1}
            ]
        },
        created_at=datetime.utcnow()
    )
    
    service_proposals[proposal_id] = service_proposal
    
    logger.info(f"Created service proposal: {proposal_id} for client {proposal.client_id}")
    
    return service_proposal


@app.get("/api/proposals/{proposal_id}", response_model=ServiceProposalResponse)
async def get_service_proposal(proposal_id: str):
    """Get service proposal by ID."""
    if proposal_id not in service_proposals:
        raise HTTPException(status_code=404, detail=f"Proposal not found: {proposal_id}")
    
    return service_proposals[proposal_id]


@app.put("/api/proposals/{proposal_id}", response_model=ServiceProposalResponse)
async def update_service_proposal(proposal_id: str, update: ServiceProposalUpdate):
    """Update service proposal."""
    if proposal_id not in service_proposals:
        raise HTTPException(status_code=404, detail=f"Proposal not found: {proposal_id}")
    
    proposal = service_proposals[proposal_id]
    
    if update.status:
        proposal.status = update.status
    if update.custom_notes is not None:
        # Note: custom_notes isn't in the response model yet, might need to add it or ignore for now if not needed in UI
        pass 
    if update.integration_method:
        proposal.integration_method = update.integration_method
        # Recalculate estimates if method changes
        settings = get_settings()
        num_objects = len(proposal.required_objects)
        
        if proposal.integration_method == IntegrationMethod.BATCH:
            hours_per_object = settings.batch_integration_hours_per_object
        else:
            hours_per_object = settings.realtime_integration_hours_per_object
        
        proposal.estimated_hours = num_objects * hours_per_object
        proposal.estimated_cost = proposal.estimated_hours * settings.default_hourly_rate
        proposal.timeline_weeks = max(4, proposal.estimated_hours // 40)
        
        proposal.breakdown["hours_per_object"] = hours_per_object
        proposal.breakdown["phases"][1]["weeks"] = proposal.timeline_weeks - 3

    service_proposals[proposal_id] = proposal
    logger.info(f"Updated service proposal: {proposal_id}")
    
    return proposal


# ============================================================================
# Demo Data Endpoints
# ============================================================================

@app.post("/api/demo/generate")
async def generate_demo_data(request: DemoDataRequest):
    """
    Generate realistic demo data for selected KPIs.
    
    Creates time-series data with realistic trends and variations.
    """
    settings = get_settings()
    generated_data = {}
    
    # Fetch KPI definitions to get units and typical ranges
    async with httpx.AsyncClient(timeout=30.0) as client:
        for kpi_code in request.kpi_codes:
            try:
                # Get KPI definition
                response = await client.get(
                    f"{settings.metadata_service_url}/kpis/{kpi_code}"
                )
                
                if response.status_code == 200:
                    kpi_data = response.json()
                    
                    # Generate time series data
                    time_series = _generate_time_series(
                        kpi_code=kpi_code,
                        kpi_data=kpi_data,
                        data_points=request.data_points
                    )
                    
                    generated_data[kpi_code] = {
                        "kpi_name": kpi_data.get("name", kpi_code),
                        "unit": kpi_data.get("unit", ""),
                        "time_series": time_series,
                        "statistics": _calculate_statistics(time_series)
                    }
                else:
                    logger.warning(f"Could not fetch KPI {kpi_code}")
                    
            except Exception as e:
                logger.error(f"Error generating data for {kpi_code}: {e}")
    
    return {
        "status": "generated",
        "kpi_codes": request.kpi_codes,
        "data_points": request.data_points,
        "generated_at": datetime.utcnow().isoformat(),
        "data": generated_data
    }


def _generate_time_series(kpi_code: str, kpi_data: Dict[str, Any], data_points: int) -> List[Dict[str, Any]]:
    """Generate realistic time series data for a KPI."""
    unit = kpi_data.get("unit", "")
    
    # Determine base value and range based on unit
    if "%" in unit or "Percentage" in unit:
        base_value = random.uniform(70, 95)
        variation = 5
    elif "$" in unit or "USD" in unit:
        base_value = random.uniform(100000, 1000000)
        variation = base_value * 0.1
    elif "days" in unit.lower():
        base_value = random.uniform(20, 60)
        variation = 10
    else:
        base_value = random.uniform(50, 100)
        variation = 15
    
    # Generate data points with trend and seasonality
    time_series = []
    start_date = datetime.utcnow() - timedelta(days=data_points)
    
    trend = random.uniform(-0.1, 0.1)  # Slight upward or downward trend
    
    for i in range(data_points):
        date = start_date + timedelta(days=i)
        
        # Add trend
        trend_value = base_value + (trend * i)
        
        # Add seasonality (weekly pattern)
        seasonal = variation * 0.3 * math.sin(2 * 3.14159 * i / 7)
        
        # Add random noise
        noise = random.uniform(-variation * 0.2, variation * 0.2)
        
        value = max(0, trend_value + seasonal + noise)
        
        # Round based on unit
        if "%" in unit:
            value = round(min(100, value), 2)
        elif "$" in unit:
            value = round(value, 2)
        else:
            value = round(value, 2)
        
        time_series.append({
            "date": date.strftime("%Y-%m-%d"),
            "value": value
        })
    
    return time_series


def _calculate_statistics(time_series: List[Dict[str, Any]]) -> Dict[str, float]:
    """Calculate statistics from time series data."""
    values = [point["value"] for point in time_series]
    
    if not values:
        return {}
    
    return {
        "average": round(sum(values) / len(values), 2),
        "min": round(min(values), 2),
        "max": round(max(values), 2),
        "latest": round(values[-1], 2),
        "change": round(values[-1] - values[0], 2) if len(values) > 1 else 0,
        "change_percent": round(((values[-1] - values[0]) / values[0] * 100), 2) if len(values) > 1 and values[0] != 0 else 0
    }


if __name__ == "__main__":
    import uvicorn
    settings = get_settings()
    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port,
        log_level=settings.log_level.lower()
    )
