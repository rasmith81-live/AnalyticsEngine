"""API endpoints for Process Simulation Service.

Provides REST API for process definitions, scenarios, and simulations.
"""

import logging
from datetime import datetime
from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Query, status
from pydantic import BaseModel

from ..config import get_settings
from ..engine.simulator import ProcessSimulationEngine
from ..models import (
    ImpactAnalysis,
    ProcessDefinition,
    ProcessDefinitionCreate,
    ScenarioComparison,
    ScenarioCreate,
    ScenarioDefinition,
    SimulationConfig,
    SimulationResult,
    SimulationStartResponse,
    SimulationStatus,
    SimulationStatusResponse,
)

logger = logging.getLogger(__name__)
router = APIRouter()

# In-memory storage (would be replaced with database in production)
_processes: Dict[UUID, ProcessDefinition] = {}
_scenarios: Dict[UUID, ScenarioDefinition] = {}
_simulations: Dict[UUID, SimulationResult] = {}
_simulation_engine = ProcessSimulationEngine()


# =============================================================================
# Health Check
# =============================================================================

class ServiceHealth(BaseModel):
    status: str
    timestamp: datetime
    version: str
    simulation_count: int


@router.get("/status", response_model=ServiceHealth)
async def get_service_status():
    """Get service health status."""
    settings = get_settings()
    return ServiceHealth(
        status="healthy",
        timestamp=datetime.utcnow(),
        version=settings.service_version,
        simulation_count=len(_simulations)
    )


# =============================================================================
# Process Definition Endpoints
# =============================================================================

@router.get("/processes", response_model=List[ProcessDefinition])
async def list_processes(
    value_chain_module: Optional[str] = None,
    is_active: bool = True
):
    """List all process definitions."""
    processes = list(_processes.values())
    
    if value_chain_module:
        processes = [p for p in processes if p.value_chain_module == value_chain_module]
    
    if is_active:
        processes = [p for p in processes if p.is_active]
    
    return processes


@router.post("/processes", response_model=ProcessDefinition, status_code=status.HTTP_201_CREATED)
async def create_process(process: ProcessDefinitionCreate):
    """Create a new process definition."""
    process_id = uuid4()
    
    new_process = ProcessDefinition(
        id=process_id,
        code=process.code,
        name=process.name,
        description=process.description,
        steps=process.steps,
        transitions=process.transitions,
        value_chain_module=process.value_chain_module,
        linked_kpis=process.linked_kpis,
        default_parameters=process.default_parameters,
        resource_requirements=process.resource_requirements,
        version=1,
        is_active=True,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    
    _processes[process_id] = new_process
    logger.info(f"Created process definition: {process.code}")
    
    return new_process


@router.get("/processes/{process_id}", response_model=ProcessDefinition)
async def get_process(process_id: UUID):
    """Get a process definition by ID."""
    if process_id not in _processes:
        raise HTTPException(status_code=404, detail=f"Process {process_id} not found")
    return _processes[process_id]


@router.put("/processes/{process_id}", response_model=ProcessDefinition)
async def update_process(process_id: UUID, process: ProcessDefinitionCreate):
    """Update a process definition."""
    if process_id not in _processes:
        raise HTTPException(status_code=404, detail=f"Process {process_id} not found")
    
    existing = _processes[process_id]
    
    updated = ProcessDefinition(
        id=process_id,
        code=process.code,
        name=process.name,
        description=process.description,
        steps=process.steps,
        transitions=process.transitions,
        value_chain_module=process.value_chain_module,
        linked_kpis=process.linked_kpis,
        default_parameters=process.default_parameters,
        resource_requirements=process.resource_requirements,
        version=existing.version + 1,
        is_active=True,
        created_at=existing.created_at,
        updated_at=datetime.utcnow()
    )
    
    _processes[process_id] = updated
    return updated


@router.delete("/processes/{process_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_process(process_id: UUID):
    """Soft delete a process definition."""
    if process_id not in _processes:
        raise HTTPException(status_code=404, detail=f"Process {process_id} not found")
    
    _processes[process_id].is_active = False
    logger.info(f"Soft deleted process: {process_id}")


# =============================================================================
# Scenario Endpoints
# =============================================================================

@router.get("/scenarios", response_model=List[ScenarioDefinition])
async def list_scenarios(
    process_id: Optional[UUID] = None
):
    """List all scenarios, optionally filtered by process."""
    scenarios = list(_scenarios.values())
    
    if process_id:
        scenarios = [s for s in scenarios if s.process_id == process_id]
    
    return scenarios


@router.post("/scenarios", response_model=ScenarioDefinition, status_code=status.HTTP_201_CREATED)
async def create_scenario(scenario: ScenarioCreate):
    """Create a new scenario."""
    if scenario.process_id not in _processes:
        raise HTTPException(status_code=404, detail=f"Process {scenario.process_id} not found")
    
    scenario_id = uuid4()
    
    new_scenario = ScenarioDefinition(
        id=scenario_id,
        name=scenario.name,
        description=scenario.description,
        process_id=scenario.process_id,
        parameter_changes=scenario.parameter_changes,
        simulation_config=scenario.simulation_config,
        arrival_distribution=scenario.arrival_distribution,
        is_baseline=scenario.is_baseline,
        created_at=datetime.utcnow()
    )
    
    _scenarios[scenario_id] = new_scenario
    logger.info(f"Created scenario: {scenario.name}")
    
    return new_scenario


@router.get("/scenarios/{scenario_id}", response_model=ScenarioDefinition)
async def get_scenario(scenario_id: UUID):
    """Get a scenario by ID."""
    if scenario_id not in _scenarios:
        raise HTTPException(status_code=404, detail=f"Scenario {scenario_id} not found")
    return _scenarios[scenario_id]


@router.delete("/scenarios/{scenario_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_scenario(scenario_id: UUID):
    """Delete a scenario."""
    if scenario_id not in _scenarios:
        raise HTTPException(status_code=404, detail=f"Scenario {scenario_id} not found")
    
    del _scenarios[scenario_id]
    logger.info(f"Deleted scenario: {scenario_id}")


# =============================================================================
# Simulation Endpoints
# =============================================================================

async def _run_simulation_background(
    simulation_id: UUID,
    process: ProcessDefinition,
    scenario: ScenarioDefinition
):
    """Background task to run simulation."""
    try:
        _simulations[simulation_id].status = SimulationStatus.RUNNING
        _simulations[simulation_id].started_at = datetime.utcnow()
        
        result = await _simulation_engine.run_simulation(
            process=process,
            scenario=scenario,
            simulation_id=simulation_id
        )
        
        _simulations[simulation_id] = result
        logger.info(f"Simulation {simulation_id} completed")
        
    except Exception as e:
        logger.error(f"Simulation {simulation_id} failed: {e}")
        _simulations[simulation_id].status = SimulationStatus.FAILED
        _simulations[simulation_id].error = str(e)
        _simulations[simulation_id].completed_at = datetime.utcnow()


@router.post("/simulations", response_model=SimulationStartResponse, status_code=status.HTTP_202_ACCEPTED)
async def start_simulation(
    scenario_id: UUID,
    background_tasks: BackgroundTasks,
    real_time_updates: bool = False
):
    """Start a simulation run."""
    if scenario_id not in _scenarios:
        raise HTTPException(status_code=404, detail=f"Scenario {scenario_id} not found")
    
    scenario = _scenarios[scenario_id]
    
    if scenario.process_id not in _processes:
        raise HTTPException(status_code=404, detail=f"Process {scenario.process_id} not found")
    
    process = _processes[scenario.process_id]
    simulation_id = uuid4()
    
    # Initialize simulation result
    _simulations[simulation_id] = SimulationResult(
        id=simulation_id,
        scenario_id=scenario_id,
        status=SimulationStatus.PENDING,
        progress=0
    )
    
    # Start background simulation
    background_tasks.add_task(
        _run_simulation_background,
        simulation_id,
        process,
        scenario
    )
    
    logger.info(f"Started simulation {simulation_id} for scenario {scenario_id}")
    
    return SimulationStartResponse(
        simulation_id=simulation_id,
        scenario_id=scenario_id,
        status=SimulationStatus.PENDING,
        message="Simulation started"
    )


@router.get("/simulations/{simulation_id}", response_model=SimulationStatusResponse)
async def get_simulation_status(simulation_id: UUID):
    """Get simulation status and results."""
    if simulation_id not in _simulations:
        raise HTTPException(status_code=404, detail=f"Simulation {simulation_id} not found")
    
    sim = _simulations[simulation_id]
    
    return SimulationStatusResponse(
        simulation_id=simulation_id,
        status=sim.status,
        progress=sim.progress,
        result=sim if sim.status == SimulationStatus.COMPLETED else None
    )


@router.get("/simulations/{simulation_id}/results", response_model=SimulationResult)
async def get_simulation_results(simulation_id: UUID):
    """Get full simulation results."""
    if simulation_id not in _simulations:
        raise HTTPException(status_code=404, detail=f"Simulation {simulation_id} not found")
    
    sim = _simulations[simulation_id]
    
    if sim.status != SimulationStatus.COMPLETED:
        raise HTTPException(
            status_code=400,
            detail=f"Simulation not completed. Status: {sim.status}"
        )
    
    return sim


# =============================================================================
# Comparison & Analysis Endpoints
# =============================================================================

class CompareRequest(BaseModel):
    scenario_ids: List[UUID]
    comparison_kpis: List[str] = []


@router.post("/simulations/compare", response_model=Dict[str, Any])
async def compare_scenarios(request: CompareRequest):
    """Compare multiple scenarios."""
    scenarios = []
    process = None
    
    for scenario_id in request.scenario_ids:
        if scenario_id not in _scenarios:
            raise HTTPException(status_code=404, detail=f"Scenario {scenario_id} not found")
        
        scenario = _scenarios[scenario_id]
        scenarios.append(scenario)
        
        # Ensure all scenarios use the same process
        if process is None:
            if scenario.process_id not in _processes:
                raise HTTPException(status_code=404, detail=f"Process {scenario.process_id} not found")
            process = _processes[scenario.process_id]
        elif scenario.process_id != process.id:
            raise HTTPException(
                status_code=400,
                detail="All scenarios must use the same process for comparison"
            )
    
    # Run comparison
    comparison_kpis = request.comparison_kpis or process.linked_kpis
    results = await _simulation_engine.compare_scenarios(
        process=process,
        scenarios=scenarios,
        comparison_kpis=comparison_kpis
    )
    
    return results


class ImpactAnalysisRequest(BaseModel):
    simulation_result_id: UUID
    focus_kpis: List[str] = []
    include_cascade_effects: bool = True


@router.post("/analysis/impact", response_model=ImpactAnalysis)
async def analyze_impact(request: ImpactAnalysisRequest):
    """Analyze the impact of a simulation on KPIs."""
    if request.simulation_result_id not in _simulations:
        raise HTTPException(
            status_code=404,
            detail=f"Simulation {request.simulation_result_id} not found"
        )
    
    sim = _simulations[request.simulation_result_id]
    
    if sim.status != SimulationStatus.COMPLETED:
        raise HTTPException(
            status_code=400,
            detail="Simulation must be completed before impact analysis"
        )
    
    # Build impact analysis from simulation results
    kpi_impacts = []
    for kpi_code, prediction in sim.kpi_predictions.items():
        if not request.focus_kpis or kpi_code in request.focus_kpis:
            from ..models import KPIImpact
            kpi_impacts.append(KPIImpact(
                kpi_code=prediction.kpi_code,
                kpi_name=prediction.kpi_name,
                current_value=prediction.baseline_value,
                predicted_value=prediction.predicted_value,
                change_absolute=prediction.predicted_value - prediction.baseline_value,
                change_percent=prediction.change_percent,
                impact_type=prediction.impact_direction,
                confidence=0.87,  # Would come from actual analysis
                upstream_effects=[],
                downstream_effects=[]
            ))
    
    return ImpactAnalysis(
        id=uuid4(),
        scenario_id=sim.scenario_id,
        simulation_result_id=sim.id,
        kpi_impacts=kpi_impacts,
        strategic_alignment_score=75.0,
        created_at=datetime.utcnow()
    )


class BottleneckRequest(BaseModel):
    simulation_result_id: UUID
    threshold: float = 80.0


@router.post("/analysis/bottlenecks")
async def detect_bottlenecks(request: BottleneckRequest):
    """Detect bottlenecks from simulation results."""
    if request.simulation_result_id not in _simulations:
        raise HTTPException(
            status_code=404,
            detail=f"Simulation {request.simulation_result_id} not found"
        )
    
    sim = _simulations[request.simulation_result_id]
    
    # Filter bottlenecks above threshold
    critical_bottlenecks = [
        b for b in sim.bottlenecks
        if b.utilization >= request.threshold
    ]
    
    return {
        "simulation_id": sim.id,
        "threshold": request.threshold,
        "bottlenecks": critical_bottlenecks,
        "total_bottlenecks": len(critical_bottlenecks)
    }
