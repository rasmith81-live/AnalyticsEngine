"""Pydantic models for Process Simulation Service.

These models support discrete event simulation of business processes
and what-if scenario analysis.
"""

from datetime import datetime, timedelta
from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Tuple, Union
from uuid import UUID

from pydantic import BaseModel, Field


# =============================================================================
# Enums
# =============================================================================

class StepType(str, Enum):
    """Type of process step."""
    TASK = "task"
    DECISION = "decision"
    PARALLEL_GATEWAY = "parallel_gateway"
    EVENT = "event"
    SUBPROCESS = "subprocess"
    START = "start"
    END = "end"


class DistributionType(str, Enum):
    """Statistical distribution types for duration/arrival."""
    FIXED = "fixed"
    NORMAL = "normal"
    EXPONENTIAL = "exponential"
    TRIANGULAR = "triangular"
    UNIFORM = "uniform"
    POISSON = "poisson"
    FROM_DATA = "from_data"


class SimulationStatus(str, Enum):
    """Status of a simulation run."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class ChangeType(str, Enum):
    """Type of parameter change in a scenario."""
    STEP_DURATION = "step_duration"
    RESOURCE_CAPACITY = "resource_capacity"
    DEFECT_RATE = "defect_rate"
    COST = "cost"
    ROUTING_PROBABILITY = "routing_probability"
    ARRIVAL_RATE = "arrival_rate"


class ImpactDirection(str, Enum):
    """Direction of impact on a KPI."""
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"


class RiskLevel(str, Enum):
    """Risk level assessment."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


# =============================================================================
# Duration & Distribution Models
# =============================================================================

class DurationDistribution(BaseModel):
    """Statistical distribution for step duration."""
    distribution_type: DistributionType = DistributionType.FIXED
    parameters: Dict[str, float] = Field(default_factory=dict)
    # For FIXED: {"value": 10}
    # For NORMAL: {"mean": 10, "std": 2}
    # For EXPONENTIAL: {"rate": 0.1}
    # For TRIANGULAR: {"min": 5, "mode": 10, "max": 15}
    # For UNIFORM: {"min": 5, "max": 15}


class ArrivalDistribution(BaseModel):
    """Distribution of work item arrivals."""
    distribution_type: DistributionType = DistributionType.POISSON
    parameters: Dict[str, Any] = Field(default_factory=dict)
    # For POISSON: {"rate": 5}  # arrivals per hour
    # For FROM_DATA: {"data_source": "historical_arrivals"}


# =============================================================================
# Process Definition Models
# =============================================================================

class ResourceRequirement(BaseModel):
    """Resource requirement for a process step."""
    resource_type: str
    quantity: int = 1
    skill_level: Optional[str] = None


class ProcessStep(BaseModel):
    """A single step in a process."""
    id: str
    name: str
    step_type: StepType = StepType.TASK
    description: Optional[str] = None
    
    # Timing
    duration_distribution: DurationDistribution = Field(default_factory=DurationDistribution)
    
    # Resources
    required_resources: List[str] = Field(default_factory=list)
    resource_quantity: int = 1
    
    # Cost
    fixed_cost: float = 0.0
    variable_cost_per_unit: float = 0.0
    
    # Quality
    defect_rate: float = 0.0  # Probability of defect/rework (0-1)
    
    # Capacity
    max_concurrent: Optional[int] = None
    
    # Utilization tracking
    utilization: Optional[float] = None
    wait_time: Optional[float] = None


class ProcessTransition(BaseModel):
    """Transition between process steps."""
    from_step: str
    to_step: str
    condition: Optional[str] = None  # For decision gateways
    probability: float = 1.0  # For probabilistic routing


class ProcessDefinition(BaseModel):
    """A business process that can be simulated."""
    id: Optional[UUID] = None
    code: str
    name: str
    description: Optional[str] = None
    
    # Process structure
    steps: List[ProcessStep] = Field(default_factory=list)
    transitions: List[ProcessTransition] = Field(default_factory=list)
    
    # Linkage to strategy
    value_chain_module: Optional[str] = None
    linked_kpis: List[str] = Field(default_factory=list)
    
    # Simulation parameters
    default_parameters: Dict[str, Any] = Field(default_factory=dict)
    resource_requirements: List[ResourceRequirement] = Field(default_factory=list)
    
    # Metadata
    version: int = 1
    is_active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class ProcessDefinitionCreate(BaseModel):
    """Create request for process definition."""
    code: str
    name: str
    description: Optional[str] = None
    steps: List[ProcessStep]
    transitions: List[ProcessTransition]
    value_chain_module: Optional[str] = None
    linked_kpis: List[str] = Field(default_factory=list)
    default_parameters: Dict[str, Any] = Field(default_factory=dict)
    resource_requirements: List[ResourceRequirement] = Field(default_factory=list)


# =============================================================================
# Scenario Models
# =============================================================================

class ParameterChange(BaseModel):
    """A change to apply in a scenario."""
    change_type: ChangeType
    target: str  # Step ID or resource ID
    parameter: str
    original_value: Any
    new_value: Any
    change_description: Optional[str] = None


class SimulationConfig(BaseModel):
    """Configuration for a simulation run."""
    simulation_duration_hours: float = 168  # 1 week default
    warm_up_period_hours: float = 24
    number_of_replications: int = 10
    random_seed: Optional[int] = None
    initial_wip: int = 0


class ScenarioDefinition(BaseModel):
    """A what-if scenario to simulate."""
    id: Optional[UUID] = None
    name: str
    description: Optional[str] = None
    
    # Base process
    process_id: UUID
    
    # Parameter overrides
    parameter_changes: List[ParameterChange] = Field(default_factory=list)
    
    # Simulation settings
    simulation_config: SimulationConfig = Field(default_factory=SimulationConfig)
    
    # Input assumptions
    arrival_distribution: ArrivalDistribution = Field(default_factory=ArrivalDistribution)
    
    # Flags
    is_baseline: bool = False
    
    # Metadata
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None


class ScenarioCreate(BaseModel):
    """Create request for scenario."""
    name: str
    description: Optional[str] = None
    process_id: UUID
    parameter_changes: List[ParameterChange] = Field(default_factory=list)
    simulation_config: SimulationConfig = Field(default_factory=SimulationConfig)
    arrival_distribution: ArrivalDistribution = Field(default_factory=ArrivalDistribution)
    is_baseline: bool = False


# =============================================================================
# Simulation Result Models
# =============================================================================

class BottleneckInfo(BaseModel):
    """Information about a process bottleneck."""
    step_id: str
    step_name: str
    utilization: float
    wait_time_avg: float
    wait_time_max: float
    queue_length_avg: float
    severity: RiskLevel


class KPIPrediction(BaseModel):
    """Predicted KPI value from simulation."""
    kpi_code: str
    kpi_name: Optional[str] = None
    baseline_value: float
    predicted_value: float
    change_percent: float
    confidence_interval: Tuple[float, float]
    impact_direction: ImpactDirection


class SimulationEvent(BaseModel):
    """Single event in simulation event log."""
    time: datetime
    event_type: str  # arrival, start, complete, queue, resource_acquire, resource_release
    step_id: Optional[str] = None
    entity_id: Optional[str] = None
    resource_id: Optional[str] = None
    event_data: Dict[str, Any] = Field(default_factory=dict)


class SimulationResult(BaseModel):
    """Results from a process simulation."""
    id: Optional[UUID] = None
    scenario_id: UUID
    status: SimulationStatus = SimulationStatus.PENDING
    progress: int = 0
    
    # Timing metrics
    avg_cycle_time: Optional[float] = None
    min_cycle_time: Optional[float] = None
    max_cycle_time: Optional[float] = None
    cycle_time_std: Optional[float] = None
    
    # Throughput metrics
    total_completed: Optional[int] = None
    throughput_rate: Optional[float] = None  # per hour
    
    # Resource utilization
    resource_utilization: Dict[str, float] = Field(default_factory=dict)
    
    # Cost metrics
    total_cost: Optional[float] = None
    cost_per_unit: Optional[float] = None
    
    # Quality metrics
    defect_count: Optional[int] = None
    defect_rate: Optional[float] = None
    rework_count: Optional[int] = None
    
    # Bottleneck analysis
    bottlenecks: List[BottleneckInfo] = Field(default_factory=list)
    
    # KPI predictions
    kpi_predictions: Dict[str, KPIPrediction] = Field(default_factory=dict)
    
    # Confidence intervals
    confidence_level: float = 0.95
    confidence_intervals: Dict[str, Tuple[float, float]] = Field(default_factory=dict)
    
    # Timing
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error: Optional[str] = None


# =============================================================================
# Impact Analysis Models
# =============================================================================

class KPIImpact(BaseModel):
    """Impact on a specific KPI."""
    kpi_code: str
    kpi_name: Optional[str] = None
    business_level: Literal["tactical", "operational", "functional", "business_unit", "corporate"] = "operational"
    
    current_value: float
    predicted_value: float
    change_absolute: float
    change_percent: float
    
    impact_type: ImpactDirection
    confidence: float
    
    # Cascade effects
    upstream_effects: List[str] = Field(default_factory=list)
    downstream_effects: List[str] = Field(default_factory=list)


class RiskItem(BaseModel):
    """Risk identified in impact analysis."""
    risk_type: str
    description: str
    severity: RiskLevel
    probability: float
    mitigation: Optional[str] = None


class TradeOff(BaseModel):
    """Trade-off between competing objectives."""
    improving_kpi: str
    degrading_kpi: str
    improvement_amount: float
    degradation_amount: float
    net_business_value: Optional[float] = None
    recommendation: Optional[str] = None


class Recommendation(BaseModel):
    """Recommendation from impact analysis."""
    action: str
    rationale: str
    priority: Literal["low", "medium", "high", "critical"]
    expected_impact: Optional[str] = None


class ImpactAnalysis(BaseModel):
    """Analysis of scenario impact on KPIs."""
    id: Optional[UUID] = None
    scenario_id: UUID
    simulation_result_id: Optional[UUID] = None
    
    # KPI impacts
    kpi_impacts: List[KPIImpact] = Field(default_factory=list)
    
    # Strategic alignment
    strategic_alignment_score: Optional[float] = None  # 0-100
    aligned_objectives: List[str] = Field(default_factory=list)
    conflicting_objectives: List[str] = Field(default_factory=list)
    
    # Risk assessment
    risk_level: RiskLevel = RiskLevel.LOW
    risks: List[RiskItem] = Field(default_factory=list)
    
    # Recommendations
    recommendations: List[Recommendation] = Field(default_factory=list)
    
    # Trade-offs
    trade_offs: List[TradeOff] = Field(default_factory=list)
    
    created_at: Optional[datetime] = None


# =============================================================================
# Comparison Models
# =============================================================================

class ScenarioComparison(BaseModel):
    """Comparison of multiple scenarios."""
    id: Optional[UUID] = None
    scenario_ids: List[UUID]
    comparison_kpis: List[str]
    
    # Results per scenario
    scenario_results: Dict[str, SimulationResult] = Field(default_factory=dict)
    
    # Comparison metrics
    kpi_comparison: Dict[str, Dict[str, float]] = Field(default_factory=dict)
    # Structure: {kpi_code: {scenario_id: value}}
    
    # Rankings
    rankings: Dict[str, List[str]] = Field(default_factory=dict)
    # Structure: {ranking_criteria: [scenario_ids in order]}
    
    best_scenario: Optional[str] = None
    recommendation: Optional[str] = None
    
    created_at: Optional[datetime] = None


# =============================================================================
# API Response Models
# =============================================================================

class SimulationStartResponse(BaseModel):
    """Response when starting a simulation."""
    simulation_id: UUID
    scenario_id: UUID
    status: SimulationStatus
    message: str


class SimulationStatusResponse(BaseModel):
    """Response for simulation status check."""
    simulation_id: UUID
    status: SimulationStatus
    progress: int
    estimated_completion: Optional[datetime] = None
    result: Optional[SimulationResult] = None
