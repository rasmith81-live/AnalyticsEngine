"""
Demo/Config Service

Handles client configuration, custom KPI creation, and service proposal generation.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
import uuid
from datetime import datetime
from typing import List

from .config import get_settings
from .models import (
    ClientConfigCreate, ClientConfigUpdate, ClientConfigResponse,
    CustomKPICreate, CustomKPIResponse,
    RequiredObjectsAnalysisRequest, RequiredObjectsAnalysisResponse,
    ServiceProposalCreate, ServiceProposalResponse,
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
    
    logger.info(f"Updated client config: {client_id}")
    
    return existing


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
    
    This would call the metadata service to get KPI definitions
    and aggregate all required objects.
    """
    # TODO: Call metadata service to get KPI definitions
    # For now, return mock data
    
    required_objects = set()
    
    # Mock: Each KPI requires 2-3 objects
    for kpi_code in request.kpi_codes:
        # In real implementation, fetch from metadata service
        required_objects.add("ORDER")
        required_objects.add("CUSTOMER")
        if "FULFILLMENT" in kpi_code:
            required_objects.add("SHIPMENT")
            required_objects.add("DELIVERY")
    
    return RequiredObjectsAnalysisResponse(
        kpi_codes=request.kpi_codes,
        required_objects=list(required_objects),
        object_details={},
        total_objects=len(required_objects),
        uml_diagram=None
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


# ============================================================================
# Demo Data Endpoints
# ============================================================================

@app.post("/api/demo/generate")
async def generate_demo_data(request: DemoDataRequest):
    """Generate demo data for selected KPIs."""
    # TODO: Generate realistic demo data
    
    return {
        "status": "generated",
        "kpi_codes": request.kpi_codes,
        "data_points": request.data_points,
        "message": "Demo data generation not yet implemented"
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
