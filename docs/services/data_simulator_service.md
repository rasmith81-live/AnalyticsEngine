# Data Simulator Service

## Overview

Data Simulator Service - FastAPI Application.

Generates realistic demo data for KPI calculations with time acceleration.

Time Acceleration Model:
- real_interval_seconds: How often data is generated (e.g., 10 seconds)
- simulated_interval_hours: What each interval represents (e.g., 1 hour)

Example: 10 seconds real = 1 hour simulated
- 1 minute real = 6 hours simulated
- 10 minutes real = 2.5 days simulated
- 1 hour real = 15 days simulated

## Data Models

### `TimeAccelerationConfig`

Configuration for time acceleration in simulation.

Defines the relationship between real-time intervals and simulated time.

Example:
    real_interval_seconds=10, simulated_interval_hours=1
    means every 10 seconds of real time = 1 hour of simulated business time

**Fields:**

- `real_interval_seconds`: `float`
- `simulated_interval_hours`: `float`

### `EntityConfig`

Configuration for an entity type to simulate.

**Fields:**

- `entity_name`: `str`
- `table_name`: `str`
- `key_column`: `str`
- `initial_count`: `int`
- `base_churn_rate`: `float`
- `base_growth_rate`: `float`
- `base_conversion_rate`: `float`
- `attributes`: `Dict[str, Any]`

### `SimulationConfig`

Full configuration for a simulation run.

**Fields:**

- `simulation_id`: `str`
- `name`: `str`
- `description`: `Optional[str]`
- `time_config`: `TimeAccelerationConfig`
- `scenario`: `SimulationScenario`
- `entities`: `List[EntityConfig]`
- `kpi_codes`: `List[str]`
- `start_simulated_time`: `datetime`
- `random_seed`: `Optional[int]`

### `SimulationState`

Current state of a running simulation.

**Fields:**

- `simulation_id`: `str`
- `config`: `SimulationConfig`
- `status`: `Literal['pending', 'running', 'paused', 'stopped', 'completed']`
- `current_simulated_time`: `datetime`
- `ticks_completed`: `int`
- `entity_counts`: `Dict[str, int]`
- `started_at`: `Optional[datetime]`
- `last_tick_at`: `Optional[datetime]`
- `error_message`: `Optional[str]`

### `EntityEvent`

An event that occurred to an entity (creation, update, deletion).

**Fields:**

- `event_type`: `Literal['create', 'update', 'deactivate', 'convert']`
- `entity_name`: `str`
- `entity_id`: `str`
- `simulated_time`: `datetime`
- `real_time`: `datetime`
- `attributes`: `Dict[str, Any]`

### `SimulationTick`

Result of a single simulation tick.

**Fields:**

- `tick_number`: `int`
- `simulated_time`: `datetime`
- `real_time`: `datetime`
- `events`: `List[EntityEvent]`
- `entity_counts`: `Dict[str, int]`
- `metrics`: `Dict[str, float]`

