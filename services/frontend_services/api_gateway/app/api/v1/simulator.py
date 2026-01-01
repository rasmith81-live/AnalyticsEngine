"""API Gateway routes for the Data Simulator Service."""

from fastapi import APIRouter, HTTPException, Query
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

from ...clients.simulator_client import simulator_client


router = APIRouter()


class CreateSimulationRequest(BaseModel):
    """Request to create a new simulation."""
    name: Optional[str] = None
    kpi_codes: List[str] = Field(..., min_length=1)
    scenario: str = "healthy"
    real_interval_seconds: float = Field(default=10.0, ge=1.0)
    simulated_interval_hours: float = Field(default=1.0, ge=0.01)
    auto_start: bool = True


# ============================================================================
# KPI Endpoints
# ============================================================================

@router.get("/kpis")
async def list_kpis():
    """List all available KPIs for simulation."""
    try:
        return await simulator_client.list_kpis()
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Simulator service error: {str(e)}")


@router.get("/kpis/{kpi_code}")
async def get_kpi(kpi_code: str):
    """Get details of a specific KPI."""
    try:
        return await simulator_client.get_kpi(kpi_code)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Simulator service error: {str(e)}")


@router.get("/kpis/{kpi_code}/entities")
async def get_kpi_entities(kpi_code: str):
    """Get entities required for a specific KPI."""
    try:
        return await simulator_client.get_kpi_entities(kpi_code)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Simulator service error: {str(e)}")


# ============================================================================
# Simulation Endpoints
# ============================================================================

@router.get("/simulations")
async def list_simulations():
    """List all simulations."""
    try:
        return await simulator_client.list_simulations()
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Simulator service error: {str(e)}")


@router.post("/simulations")
async def create_simulation(request: CreateSimulationRequest):
    """Create a new simulation."""
    try:
        config = {
            "name": request.name or f"Simulation - {', '.join(request.kpi_codes)}",
            "kpi_codes": request.kpi_codes,
            "scenario": request.scenario,
            "real_interval_seconds": request.real_interval_seconds,
            "simulated_interval_hours": request.simulated_interval_hours,
            "auto_start": request.auto_start,
        }
        return await simulator_client.create_simulation(config)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Simulator service error: {str(e)}")


@router.get("/simulations/{simulation_id}")
async def get_simulation(simulation_id: str):
    """Get a specific simulation."""
    try:
        return await simulator_client.get_simulation(simulation_id)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Simulator service error: {str(e)}")


@router.post("/simulations/{simulation_id}/start")
async def start_simulation(simulation_id: str):
    """Start a simulation."""
    try:
        return await simulator_client.start_simulation(simulation_id)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Simulator service error: {str(e)}")


@router.post("/simulations/{simulation_id}/pause")
async def pause_simulation(simulation_id: str):
    """Pause a simulation."""
    try:
        return await simulator_client.pause_simulation(simulation_id)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Simulator service error: {str(e)}")


@router.post("/simulations/{simulation_id}/resume")
async def resume_simulation(simulation_id: str):
    """Resume a simulation."""
    try:
        return await simulator_client.resume_simulation(simulation_id)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Simulator service error: {str(e)}")


@router.post("/simulations/{simulation_id}/stop")
async def stop_simulation(simulation_id: str):
    """Stop a simulation."""
    try:
        return await simulator_client.stop_simulation(simulation_id)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Simulator service error: {str(e)}")


@router.delete("/simulations/{simulation_id}")
async def delete_simulation(simulation_id: str):
    """Delete a simulation."""
    try:
        await simulator_client.delete_simulation(simulation_id)
        return {"status": "deleted", "simulation_id": simulation_id}
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Simulator service error: {str(e)}")


@router.get("/simulations/{simulation_id}/ticks")
async def get_simulation_ticks(
    simulation_id: str,
    limit: int = Query(default=100, ge=1, le=1000),
    offset: int = Query(default=0, ge=0)
):
    """Get simulation ticks."""
    try:
        return await simulator_client.get_simulation_ticks(simulation_id, limit, offset)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Simulator service error: {str(e)}")


@router.get("/simulations/{simulation_id}/data/{entity_type}")
async def get_simulation_data(
    simulation_id: str,
    entity_type: str,
    limit: int = Query(default=100, ge=1, le=10000)
):
    """Get simulation entity data."""
    try:
        return await simulator_client.get_simulation_data(simulation_id, entity_type, limit)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Simulator service error: {str(e)}")
