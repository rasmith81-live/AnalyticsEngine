# Process Simulation Service

## Overview

Process Simulation Service - Main Application.

Discrete event simulation for business process scenarios and what-if analysis.

## Data Models

### `DurationDistribution`

Statistical distribution for step duration.

**Fields:**

- `distribution_type`: `DistributionType`
- `parameters`: `Dict[str, float]`

### `ArrivalDistribution`

Distribution of work item arrivals.

**Fields:**

- `distribution_type`: `DistributionType`
- `parameters`: `Dict[str, Any]`

### `ResourceRequirement`

Resource requirement for a process step.

**Fields:**

- `resource_type`: `str`
- `quantity`: `int`
- `skill_level`: `Optional[str]`

### `ProcessStep`

A single step in a process.

**Fields:**

- `id`: `str`
- `name`: `str`
- `step_type`: `StepType`
- `description`: `Optional[str]`
- `duration_distribution`: `DurationDistribution`
- `required_resources`: `List[str]`
- `resource_quantity`: `int`
- `fixed_cost`: `float`
- `variable_cost_per_unit`: `float`
- `defect_rate`: `float`
- `max_concurrent`: `Optional[int]`
- `utilization`: `Optional[float]`
- `wait_time`: `Optional[float]`

### `ProcessTransition`

Transition between process steps.

**Fields:**

- `from_step`: `str`
- `to_step`: `str`
- `condition`: `Optional[str]`
- `probability`: `float`

### `ProcessDefinition`

A business process that can be simulated.

**Fields:**

- `id`: `Optional[UUID]`
- `code`: `str`
- `name`: `str`
- `description`: `Optional[str]`
- `steps`: `List[ProcessStep]`
- `transitions`: `List[ProcessTransition]`
- `value_chain_module`: `Optional[str]`
- `linked_kpis`: `List[str]`
- `default_parameters`: `Dict[str, Any]`
- `resource_requirements`: `List[ResourceRequirement]`
- `version`: `int`
- `is_active`: `bool`
- `created_at`: `Optional[datetime]`
- `updated_at`: `Optional[datetime]`

### `ProcessDefinitionCreate`

Create request for process definition.

**Fields:**

- `code`: `str`
- `name`: `str`
- `description`: `Optional[str]`
- `steps`: `List[ProcessStep]`
- `transitions`: `List[ProcessTransition]`
- `value_chain_module`: `Optional[str]`
- `linked_kpis`: `List[str]`
- `default_parameters`: `Dict[str, Any]`
- `resource_requirements`: `List[ResourceRequirement]`

### `ParameterChange`

A change to apply in a scenario.

**Fields:**

- `change_type`: `ChangeType`
- `target`: `str`
- `parameter`: `str`
- `original_value`: `Any`
- `new_value`: `Any`
- `change_description`: `Optional[str]`

### `SimulationConfig`

Configuration for a simulation run.

**Fields:**

- `simulation_duration_hours`: `float`
- `warm_up_period_hours`: `float`
- `number_of_replications`: `int`
- `random_seed`: `Optional[int]`
- `initial_wip`: `int`

### `ScenarioDefinition`

A what-if scenario to simulate.

**Fields:**

- `id`: `Optional[UUID]`
- `name`: `str`
- `description`: `Optional[str]`
- `process_id`: `UUID`
- `parameter_changes`: `List[ParameterChange]`
- `simulation_config`: `SimulationConfig`
- `arrival_distribution`: `ArrivalDistribution`
- `is_baseline`: `bool`
- `created_by`: `Optional[str]`
- `created_at`: `Optional[datetime]`

### `ScenarioCreate`

Create request for scenario.

**Fields:**

- `name`: `str`
- `description`: `Optional[str]`
- `process_id`: `UUID`
- `parameter_changes`: `List[ParameterChange]`
- `simulation_config`: `SimulationConfig`
- `arrival_distribution`: `ArrivalDistribution`
- `is_baseline`: `bool`

### `BottleneckInfo`

Information about a process bottleneck.

**Fields:**

- `step_id`: `str`
- `step_name`: `str`
- `utilization`: `float`
- `wait_time_avg`: `float`
- `wait_time_max`: `float`
- `queue_length_avg`: `float`
- `severity`: `RiskLevel`

### `KPIPrediction`

Predicted KPI value from simulation.

**Fields:**

- `kpi_code`: `str`
- `kpi_name`: `Optional[str]`
- `baseline_value`: `float`
- `predicted_value`: `float`
- `change_percent`: `float`
- `confidence_interval`: `Tuple[float, float]`
- `impact_direction`: `ImpactDirection`

### `SimulationEvent`

Single event in simulation event log.

**Fields:**

- `time`: `datetime`
- `event_type`: `str`
- `step_id`: `Optional[str]`
- `entity_id`: `Optional[str]`
- `resource_id`: `Optional[str]`
- `event_data`: `Dict[str, Any]`

### `SimulationResult`

Results from a process simulation.

**Fields:**

- `id`: `Optional[UUID]`
- `scenario_id`: `UUID`
- `status`: `SimulationStatus`
- `progress`: `int`
- `avg_cycle_time`: `Optional[float]`
- `min_cycle_time`: `Optional[float]`
- `max_cycle_time`: `Optional[float]`
- `cycle_time_std`: `Optional[float]`
- `total_completed`: `Optional[int]`
- `throughput_rate`: `Optional[float]`
- `resource_utilization`: `Dict[str, float]`
- `total_cost`: `Optional[float]`
- `cost_per_unit`: `Optional[float]`
- `defect_count`: `Optional[int]`
- `defect_rate`: `Optional[float]`
- `rework_count`: `Optional[int]`
- `bottlenecks`: `List[BottleneckInfo]`
- `kpi_predictions`: `Dict[str, KPIPrediction]`
- `confidence_level`: `float`
- `confidence_intervals`: `Dict[str, Tuple[float, float]]`
- `started_at`: `Optional[datetime]`
- `completed_at`: `Optional[datetime]`
- `error`: `Optional[str]`

### `KPIImpact`

Impact on a specific KPI.

**Fields:**

- `kpi_code`: `str`
- `kpi_name`: `Optional[str]`
- `business_level`: `Literal['tactical', 'operational', 'functional', 'business_unit', 'corporate']`
- `current_value`: `float`
- `predicted_value`: `float`
- `change_absolute`: `float`
- `change_percent`: `float`
- `impact_type`: `ImpactDirection`
- `confidence`: `float`
- `upstream_effects`: `List[str]`
- `downstream_effects`: `List[str]`

### `RiskItem`

Risk identified in impact analysis.

**Fields:**

- `risk_type`: `str`
- `description`: `str`
- `severity`: `RiskLevel`
- `probability`: `float`
- `mitigation`: `Optional[str]`

### `TradeOff`

Trade-off between competing objectives.

**Fields:**

- `improving_kpi`: `str`
- `degrading_kpi`: `str`
- `improvement_amount`: `float`
- `degradation_amount`: `float`
- `net_business_value`: `Optional[float]`
- `recommendation`: `Optional[str]`

### `Recommendation`

Recommendation from impact analysis.

**Fields:**

- `action`: `str`
- `rationale`: `str`
- `priority`: `Literal['low', 'medium', 'high', 'critical']`
- `expected_impact`: `Optional[str]`

### `ImpactAnalysis`

Analysis of scenario impact on KPIs.

**Fields:**

- `id`: `Optional[UUID]`
- `scenario_id`: `UUID`
- `simulation_result_id`: `Optional[UUID]`
- `kpi_impacts`: `List[KPIImpact]`
- `strategic_alignment_score`: `Optional[float]`
- `aligned_objectives`: `List[str]`
- `conflicting_objectives`: `List[str]`
- `risk_level`: `RiskLevel`
- `risks`: `List[RiskItem]`
- `recommendations`: `List[Recommendation]`
- `trade_offs`: `List[TradeOff]`
- `created_at`: `Optional[datetime]`

### `ScenarioComparison`

Comparison of multiple scenarios.

**Fields:**

- `id`: `Optional[UUID]`
- `scenario_ids`: `List[UUID]`
- `comparison_kpis`: `List[str]`
- `scenario_results`: `Dict[str, SimulationResult]`
- `kpi_comparison`: `Dict[str, Dict[str, float]]`
- `rankings`: `Dict[str, List[str]]`
- `best_scenario`: `Optional[str]`
- `recommendation`: `Optional[str]`
- `created_at`: `Optional[datetime]`

### `SimulationStartResponse`

Response when starting a simulation.

**Fields:**

- `simulation_id`: `UUID`
- `scenario_id`: `UUID`
- `status`: `SimulationStatus`
- `message`: `str`

### `SimulationStatusResponse`

Response for simulation status check.

**Fields:**

- `simulation_id`: `UUID`
- `status`: `SimulationStatus`
- `progress`: `int`
- `estimated_completion`: `Optional[datetime]`
- `result`: `Optional[SimulationResult]`

