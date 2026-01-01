"""Pydantic models for the Data Simulator Service."""

from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Literal
from enum import Enum
from pydantic import BaseModel, Field, ConfigDict


class TimeAccelerationConfig(BaseModel):
    """Configuration for time acceleration in simulation.
    
    Defines the relationship between real-time intervals and simulated time.
    
    Example:
        real_interval_seconds=10, simulated_interval_hours=1
        means every 10 seconds of real time = 1 hour of simulated business time
    """
    model_config = ConfigDict(extra="forbid")
    
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
    
    @property
    def acceleration_factor(self) -> float:
        """Calculate the time acceleration factor."""
        real_hours = self.real_interval_seconds / 3600
        return self.simulated_interval_hours / real_hours
    
    @property
    def simulated_interval_timedelta(self) -> timedelta:
        """Get the simulated interval as a timedelta."""
        return timedelta(hours=self.simulated_interval_hours)


class SimulationScenario(str, Enum):
    """Pre-defined simulation scenarios with different business patterns."""
    HEALTHY = "healthy"           # Low churn, steady growth
    STRUGGLING = "struggling"     # High churn, negative growth
    SEASONAL = "seasonal"         # Cyclical patterns
    GROWTH_SPURT = "growth_spurt" # Rapid acquisition
    STABLE = "stable"             # Minimal change
    VOLATILE = "volatile"         # Random fluctuations


class EntityConfig(BaseModel):
    """Configuration for an entity type to simulate."""
    model_config = ConfigDict(extra="allow")
    
    entity_name: str = Field(description="Name of the entity (e.g., 'customers')")
    table_name: str = Field(description="Database table name")
    key_column: str = Field(default="id", description="Primary key column")
    
    initial_count: int = Field(default=1000, ge=0, description="Starting entity count")
    
    base_churn_rate: float = Field(
        default=0.02,
        ge=0.0,
        le=1.0,
        description="Base monthly churn rate (0.02 = 2%)"
    )
    base_growth_rate: float = Field(
        default=0.05,
        ge=0.0,
        le=1.0,
        description="Base monthly growth rate (0.05 = 5%)"
    )
    base_conversion_rate: float = Field(
        default=0.15,
        ge=0.0,
        le=1.0,
        description="Base conversion rate for funnel entities"
    )
    
    attributes: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional attributes to generate for each entity"
    )


class SimulationConfig(BaseModel):
    """Full configuration for a simulation run."""
    model_config = ConfigDict(extra="allow")
    
    simulation_id: str = Field(description="Unique identifier for this simulation")
    name: str = Field(description="Human-readable name")
    description: Optional[str] = None
    
    time_config: TimeAccelerationConfig = Field(
        default_factory=TimeAccelerationConfig,
        description="Time acceleration settings"
    )
    
    scenario: SimulationScenario = Field(
        default=SimulationScenario.HEALTHY,
        description="Pre-defined scenario to use"
    )
    
    entities: List[EntityConfig] = Field(
        default_factory=list,
        description="Entity types to simulate"
    )
    
    kpi_codes: List[str] = Field(
        default_factory=list,
        description="KPI codes to generate data for"
    )
    
    start_simulated_time: datetime = Field(
        default_factory=lambda: datetime.utcnow() - timedelta(days=365),
        description="Starting point in simulated time"
    )
    
    random_seed: Optional[int] = Field(
        default=None,
        description="Random seed for reproducibility"
    )


class SimulationState(BaseModel):
    """Current state of a running simulation."""
    model_config = ConfigDict(extra="allow")
    
    simulation_id: str
    config: SimulationConfig
    
    status: Literal["pending", "running", "paused", "stopped", "completed"] = "pending"
    
    current_simulated_time: datetime
    ticks_completed: int = 0
    
    entity_counts: Dict[str, int] = Field(
        default_factory=dict,
        description="Current count of each entity type"
    )
    
    started_at: Optional[datetime] = None
    last_tick_at: Optional[datetime] = None
    
    error_message: Optional[str] = None


class EntityEvent(BaseModel):
    """An event that occurred to an entity (creation, update, deletion)."""
    model_config = ConfigDict(extra="forbid")
    
    event_type: Literal["create", "update", "deactivate", "convert"]
    entity_name: str
    entity_id: str
    
    simulated_time: datetime
    real_time: datetime = Field(default_factory=datetime.utcnow)
    
    attributes: Dict[str, Any] = Field(default_factory=dict)


class SimulationTick(BaseModel):
    """Result of a single simulation tick."""
    model_config = ConfigDict(extra="forbid")
    
    tick_number: int
    simulated_time: datetime
    real_time: datetime
    
    events: List[EntityEvent] = Field(default_factory=list)
    
    entity_counts: Dict[str, int] = Field(default_factory=dict)
    
    metrics: Dict[str, float] = Field(
        default_factory=dict,
        description="Computed KPI values at this tick"
    )
