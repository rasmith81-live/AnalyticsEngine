"""Data Simulator Service - FastAPI Application.

Generates realistic demo data for KPI calculations with time acceleration.

Time Acceleration Model:
- real_interval_seconds: How often data is generated (e.g., 10 seconds)
- simulated_interval_hours: What each interval represents (e.g., 1 hour)

Example: 10 seconds real = 1 hour simulated
- 1 minute real = 6 hours simulated
- 10 minutes real = 2.5 days simulated
- 1 hour real = 15 days simulated
"""

import asyncio
from contextlib import asynccontextmanager
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional
import logging
import os

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from .models import (
    EntityConfig,
    SimulationConfig,
    SimulationScenario,
    SimulationState,
    SimulationTick,
    TimeAccelerationConfig,
)
from .simulation_engine import SimulationEngine, create_simulation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Service configuration
METADATA_SERVICE_URL = os.getenv("METADATA_SERVICE_URL", "http://localhost:8001")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

# Global simulation registry
simulations: Dict[str, SimulationEngine] = {}

# Recent ticks buffer for each simulation (for streaming/polling)
tick_buffers: Dict[str, List[SimulationTick]] = {}
MAX_BUFFER_SIZE = 100


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler."""
    logger.info("Data Simulator Service starting...")
    yield
    logger.info("Data Simulator Service shutting down...")
    # Stop all running simulations
    for sim_id, engine in simulations.items():
        if engine.state.status == "running":
            engine.stop()


app = FastAPI(
    title="Data Simulator Service",
    description="Generates realistic demo data for KPI calculations with time acceleration",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CreateSimulationRequest(BaseModel):
    """Request to create a new simulation."""
    name: str = Field(description="Human-readable name for the simulation")
    
    kpi_codes: List[str] = Field(
        default_factory=list,
        description="KPI codes to generate data for (will analyze set_based_definitions)"
    )
    
    entities: List[EntityConfig] = Field(
        default_factory=list,
        description="Explicit entity configurations"
    )
    
    scenario: SimulationScenario = Field(
        default=SimulationScenario.HEALTHY,
        description="Pre-defined scenario affecting churn/growth rates"
    )
    
    real_interval_seconds: float = Field(
        default=10.0,
        ge=1.0,
        description="How often to generate data in real seconds"
    )
    
    simulated_interval_hours: float = Field(
        default=1.0,
        ge=0.01,
        description="What time period each real interval represents in simulated hours"
    )
    
    start_simulated_time: Optional[datetime] = Field(
        default=None,
        description="Starting point in simulated time (defaults to 1 year ago)"
    )
    
    random_seed: Optional[int] = Field(
        default=None,
        description="Random seed for reproducibility"
    )
    
    auto_start: bool = Field(
        default=False,
        description="Automatically start the simulation after creation"
    )


class SimulationResponse(BaseModel):
    """Response containing simulation details."""
    simulation_id: str
    name: str
    status: str
    scenario: str
    time_acceleration: Dict[str, Any]
    entity_counts: Dict[str, int]
    ticks_completed: int
    current_simulated_time: Optional[datetime]
    started_at: Optional[datetime]


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "data_simulator_service",
        "active_simulations": len([s for s in simulations.values() if s.state.status == "running"]),
    }


@app.post("/simulations", response_model=SimulationResponse)
async def create_simulation_endpoint(
    request: CreateSimulationRequest,
    background_tasks: BackgroundTasks,
):
    """
    Create a new simulation.
    
    The simulation will analyze the specified KPIs to determine what entity data
    needs to be generated, then create realistic data with the specified time
    acceleration.
    
    Time Acceleration Example:
    - real_interval_seconds=10, simulated_interval_hours=1
    - Every 10 seconds of real time = 1 hour of simulated business time
    - 1 minute real = 6 hours simulated
    - 10 minutes real = 2.5 days simulated
    """
    # Create simulation engine
    engine = create_simulation(
        name=request.name,
        kpi_codes=request.kpi_codes,
        entities=request.entities,
        scenario=request.scenario,
        real_interval_seconds=request.real_interval_seconds,
        simulated_interval_hours=request.simulated_interval_hours,
        start_simulated_time=request.start_simulated_time,
        random_seed=request.random_seed,
        metadata_service_url=METADATA_SERVICE_URL,
        redis_url=REDIS_URL,
    )
    
    # Initialize the simulation
    await engine.initialize()
    
    # Register tick callback to buffer ticks
    sim_id = engine.config.simulation_id
    tick_buffers[sim_id] = []
    
    def buffer_tick(tick: SimulationTick):
        buffer = tick_buffers.get(sim_id, [])
        buffer.append(tick)
        if len(buffer) > MAX_BUFFER_SIZE:
            buffer.pop(0)
        tick_buffers[sim_id] = buffer
    
    engine.on_tick(buffer_tick)
    
    # Store in registry
    simulations[sim_id] = engine
    
    # Auto-start if requested
    if request.auto_start:
        background_tasks.add_task(engine.start)
    
    return _build_simulation_response(engine)


@app.get("/simulations", response_model=List[SimulationResponse])
async def list_simulations():
    """List all simulations."""
    return [_build_simulation_response(engine) for engine in simulations.values()]


@app.get("/simulations/{simulation_id}", response_model=SimulationResponse)
async def get_simulation(simulation_id: str):
    """Get details of a specific simulation."""
    if simulation_id not in simulations:
        raise HTTPException(status_code=404, detail="Simulation not found")
    
    return _build_simulation_response(simulations[simulation_id])


@app.post("/simulations/{simulation_id}/start")
async def start_simulation(simulation_id: str, background_tasks: BackgroundTasks):
    """Start a simulation."""
    if simulation_id not in simulations:
        raise HTTPException(status_code=404, detail="Simulation not found")
    
    engine = simulations[simulation_id]
    
    if engine.state.status == "running":
        raise HTTPException(status_code=400, detail="Simulation already running")
    
    background_tasks.add_task(engine.start)
    
    return {"status": "starting", "simulation_id": simulation_id}


@app.post("/simulations/{simulation_id}/pause")
async def pause_simulation(simulation_id: str):
    """Pause a running simulation."""
    if simulation_id not in simulations:
        raise HTTPException(status_code=404, detail="Simulation not found")
    
    engine = simulations[simulation_id]
    
    if engine.state.status != "running":
        raise HTTPException(status_code=400, detail="Simulation not running")
    
    engine.pause()
    
    return {"status": "paused", "simulation_id": simulation_id}


@app.post("/simulations/{simulation_id}/resume")
async def resume_simulation(simulation_id: str):
    """Resume a paused simulation."""
    if simulation_id not in simulations:
        raise HTTPException(status_code=404, detail="Simulation not found")
    
    engine = simulations[simulation_id]
    
    if engine.state.status != "paused":
        raise HTTPException(status_code=400, detail="Simulation not paused")
    
    engine.resume()
    
    return {"status": "running", "simulation_id": simulation_id}


@app.post("/simulations/{simulation_id}/stop")
async def stop_simulation(simulation_id: str):
    """Stop a simulation."""
    if simulation_id not in simulations:
        raise HTTPException(status_code=404, detail="Simulation not found")
    
    engine = simulations[simulation_id]
    await engine.stop()
    
    return {"status": "stopped", "simulation_id": simulation_id}


@app.delete("/simulations/{simulation_id}")
async def delete_simulation(simulation_id: str):
    """Delete a simulation."""
    if simulation_id not in simulations:
        raise HTTPException(status_code=404, detail="Simulation not found")
    
    engine = simulations[simulation_id]
    
    if engine.state.status == "running":
        await engine.stop()
    
    del simulations[simulation_id]
    if simulation_id in tick_buffers:
        del tick_buffers[simulation_id]
    
    return {"status": "deleted", "simulation_id": simulation_id}


@app.get("/simulations/{simulation_id}/ticks")
async def get_recent_ticks(
    simulation_id: str,
    limit: int = 10,
):
    """Get recent simulation ticks."""
    if simulation_id not in simulations:
        raise HTTPException(status_code=404, detail="Simulation not found")
    
    buffer = tick_buffers.get(simulation_id, [])
    recent = buffer[-limit:] if limit < len(buffer) else buffer
    
    return {
        "simulation_id": simulation_id,
        "ticks": [tick.model_dump() for tick in recent],
        "total_buffered": len(buffer),
    }


@app.get("/simulations/{simulation_id}/entities/{entity_name}")
async def get_entity_data(
    simulation_id: str,
    entity_name: str,
    at_time: Optional[datetime] = None,
):
    """Get entity data at a specific simulated time."""
    if simulation_id not in simulations:
        raise HTTPException(status_code=404, detail="Simulation not found")
    
    engine = simulations[simulation_id]
    
    if entity_name not in engine.generators:
        raise HTTPException(status_code=404, detail=f"Entity not found: {entity_name}")
    
    query_time = at_time or engine.state.current_simulated_time
    entities = engine.get_entities_at_time(entity_name, query_time)
    
    return {
        "entity_name": entity_name,
        "simulated_time": query_time.isoformat(),
        "count": len(entities),
        "entities": entities[:100],  # Limit response size
    }


@app.get("/simulations/{simulation_id}/state")
async def get_simulation_state(simulation_id: str):
    """Get full simulation state."""
    if simulation_id not in simulations:
        raise HTTPException(status_code=404, detail="Simulation not found")
    
    engine = simulations[simulation_id]
    return engine.get_state().model_dump()


class QuickStartRequest(BaseModel):
    """Quick start request for common demo scenarios."""
    scenario: SimulationScenario = SimulationScenario.HEALTHY
    entity_type: str = Field(
        default="customers",
        description="Primary entity type to simulate"
    )
    initial_count: int = Field(default=1000, ge=10, le=100000)
    real_interval_seconds: float = Field(default=10.0, ge=1.0)
    simulated_interval_hours: float = Field(default=1.0, ge=0.01)


class KPIInfo(BaseModel):
    """KPI information for UI display."""
    code: str
    name: str
    calculation_type: str
    required_objects: List[str]
    formula: Optional[str] = None
    category: Optional[str] = None


@app.post("/simulations/quick-start", response_model=SimulationResponse)
async def quick_start_simulation(
    request: QuickStartRequest,
    background_tasks: BackgroundTasks,
):
    """
    Quick start a simulation with sensible defaults.
    
    Creates a simulation with a single entity type and starts it immediately.
    """
    entity_config = EntityConfig(
        entity_name=request.entity_type,
        table_name=request.entity_type,
        key_column=f"{request.entity_type.rstrip('s')}_id",
        initial_count=request.initial_count,
    )
    
    engine = create_simulation(
        name=f"Quick Start - {request.entity_type} ({request.scenario.value})",
        entities=[entity_config],
        scenario=request.scenario,
        real_interval_seconds=request.real_interval_seconds,
        simulated_interval_hours=request.simulated_interval_hours,
    )
    
    await engine.initialize()
    
    sim_id = engine.config.simulation_id
    tick_buffers[sim_id] = []
    
    def buffer_tick(tick: SimulationTick):
        buffer = tick_buffers.get(sim_id, [])
        buffer.append(tick)
        if len(buffer) > MAX_BUFFER_SIZE:
            buffer.pop(0)
        tick_buffers[sim_id] = buffer
    
    engine.on_tick(buffer_tick)
    simulations[sim_id] = engine
    
    # Auto-start
    background_tasks.add_task(engine.start)
    
    return _build_simulation_response(engine)


def _build_simulation_response(engine: SimulationEngine) -> SimulationResponse:
    """Build a SimulationResponse from an engine."""
    state = engine.get_state()
    config = engine.config
    
    return SimulationResponse(
        simulation_id=config.simulation_id,
        name=config.name,
        status=state.status,
        scenario=config.scenario.value,
        time_acceleration={
            "real_interval_seconds": config.time_config.real_interval_seconds,
            "simulated_interval_hours": config.time_config.simulated_interval_hours,
            "acceleration_factor": config.time_config.acceleration_factor,
        },
        entity_counts=state.entity_counts,
        ticks_completed=state.ticks_completed,
        current_simulated_time=state.current_simulated_time,
        started_at=state.started_at,
    )


# ============================================================================
# KPI Discovery Endpoints
# ============================================================================

METADATA_SERVICE_URL = os.getenv("METADATA_SERVICE_URL", "http://localhost:8001")


@app.get("/kpis", response_model=List[KPIInfo])
async def list_available_kpis():
    """
    List all available KPIs from the metadata service.
    
    Returns KPIs with their calculation_type and required_objects so the UI
    can display what entities will be simulated for each KPI.
    """
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                f"{METADATA_SERVICE_URL}/api/v1/metadata/definitions",
                params={"kind": "metric_definition"}
            )
            if response.status_code == 200:
                definitions = response.json()
                kpis = []
                for defn in definitions:
                    kpis.append(KPIInfo(
                        code=defn.get("code", ""),
                        name=defn.get("name", ""),
                        calculation_type=defn.get("calculation_type", "simple"),
                        required_objects=defn.get("required_objects", []),
                        formula=defn.get("formula"),
                        category=defn.get("category"),
                    ))
                return kpis
    except Exception as e:
        logger.warning(f"Failed to fetch KPIs from metadata service: {e}")
    
    return []


@app.get("/kpis/{kpi_code}", response_model=KPIInfo)
async def get_kpi_info(kpi_code: str):
    """Get detailed information about a specific KPI."""
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                f"{METADATA_SERVICE_URL}/api/v1/metadata/definitions/metric_definition/{kpi_code}"
            )
            if response.status_code == 200:
                defn = response.json()
                return KPIInfo(
                    code=defn.get("code", ""),
                    name=defn.get("name", ""),
                    calculation_type=defn.get("calculation_type", "simple"),
                    required_objects=defn.get("required_objects", []),
                    formula=defn.get("formula"),
                    category=defn.get("category"),
                )
    except Exception as e:
        logger.warning(f"Failed to fetch KPI {kpi_code}: {e}")
    
    raise HTTPException(status_code=404, detail=f"KPI not found: {kpi_code}")


@app.get("/kpis/{kpi_code}/entities")
async def get_kpi_entities(kpi_code: str):
    """
    Get the entities required for a specific KPI.
    
    Returns entity definitions with their table schemas so the simulator
    knows what data to generate.
    """
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10.0) as client:
            # Get KPI definition
            kpi_response = await client.get(
                f"{METADATA_SERVICE_URL}/api/v1/metadata/definitions/metric_definition/{kpi_code}"
            )
            if kpi_response.status_code != 200:
                raise HTTPException(status_code=404, detail=f"KPI not found: {kpi_code}")
            
            kpi_def = kpi_response.json()
            required_objects = kpi_def.get("required_objects", [])
            
            # Fetch each entity definition
            entities = []
            for entity_code in required_objects:
                entity_response = await client.get(
                    f"{METADATA_SERVICE_URL}/api/v1/metadata/definitions/entity_definition/{entity_code}"
                )
                if entity_response.status_code == 200:
                    entities.append(entity_response.json())
            
            return {
                "kpi_code": kpi_code,
                "kpi_name": kpi_def.get("name"),
                "calculation_type": kpi_def.get("calculation_type", "simple"),
                "entities": entities,
            }
    except HTTPException:
        raise
    except Exception as e:
        logger.warning(f"Failed to fetch entities for KPI {kpi_code}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8007)
