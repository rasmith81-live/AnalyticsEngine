# Data Simulator Service

Generates realistic demo data for KPI calculations with **time acceleration**.

## Time Acceleration Model

The simulator uses a two-axis time model:

1. **Real-time interval**: How often data is generated (e.g., every 10 seconds)
2. **Simulated time interval**: What each real-time interval represents (e.g., 1 hour of business time)

### Example

With `real_interval_seconds=10` and `simulated_interval_hours=1`:

| Real Time | Simulated Time |
|-----------|----------------|
| 10 seconds | 1 hour |
| 1 minute | 6 hours |
| 10 minutes | 2.5 days |
| 1 hour | 15 days |
| 4 hours | 2 months |

This allows a demo to show realistic KPI trends (churn over months, seasonal patterns) in just minutes.

## Features

- **KPI-Aware Data Generation**: Analyzes `set_based_definition` to determine what entity data is needed
- **Scenario Presets**: Healthy, Struggling, Seasonal, Growth Spurt, Stable, Volatile
- **Entity Types**: Customers, Policies, Subscriptions, Leads, Transactions
- **Realistic Patterns**: Churn, retention, growth, conversion with configurable rates
- **Time Acceleration**: Compress months of business data into minutes of demo time

## API Endpoints

### Simulation Management

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/simulations` | POST | Create a new simulation |
| `/simulations` | GET | List all simulations |
| `/simulations/{id}` | GET | Get simulation details |
| `/simulations/{id}/start` | POST | Start a simulation |
| `/simulations/{id}/pause` | POST | Pause a simulation |
| `/simulations/{id}/resume` | POST | Resume a simulation |
| `/simulations/{id}/stop` | POST | Stop a simulation |
| `/simulations/{id}` | DELETE | Delete a simulation |

### Data Access

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/simulations/{id}/ticks` | GET | Get recent simulation ticks |
| `/simulations/{id}/entities/{name}` | GET | Get entity data at a time |
| `/simulations/{id}/state` | GET | Get full simulation state |

### Quick Start

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/simulations/quick-start` | POST | Quick start with defaults |

## Usage Examples

### Quick Start

```bash
curl -X POST http://localhost:8007/simulations/quick-start \
  -H "Content-Type: application/json" \
  -d '{
    "scenario": "healthy",
    "entity_type": "customers",
    "initial_count": 1000,
    "real_interval_seconds": 10,
    "simulated_interval_hours": 1
  }'
```

### Create KPI-Aware Simulation

```bash
curl -X POST http://localhost:8007/simulations \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Customer Churn Demo",
    "kpi_codes": ["CHURN_RATE", "RETENTION_RATE", "GROWTH_RATE"],
    "scenario": "struggling",
    "real_interval_seconds": 5,
    "simulated_interval_hours": 24,
    "auto_start": true
  }'
```

### Get Recent Ticks

```bash
curl http://localhost:8007/simulations/{simulation_id}/ticks?limit=10
```

## Scenarios

| Scenario | Churn | Growth | Description |
|----------|-------|--------|-------------|
| `healthy` | Low (1%) | High (7.5%) | Growing business |
| `struggling` | High (4%) | Low (1.5%) | Declining business |
| `seasonal` | Variable | Variable | Cyclical patterns |
| `growth_spurt` | Low (1.4%) | Very High (15%) | Rapid expansion |
| `stable` | Normal (2%) | Normal (5%) | Steady state |
| `volatile` | Random | Random | High variance |

## Running the Service

```bash
cd services/business_services/data_simulator_service
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8007 --reload
```

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    SimulationEngine                         │
│  - Orchestrates time acceleration loop                      │
│  - Manages entity generators                                │
│  - Emits ticks and events                                   │
└─────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ EntityGenerator │ │ EntityGenerator │ │ EntityGenerator │
│   (customers)   │ │   (policies)    │ │    (leads)      │
│                 │ │                 │ │                 │
│ - Churn logic   │ │ - Churn logic   │ │ - Conversion    │
│ - Growth logic  │ │ - Growth logic  │ │ - Expiration    │
│ - Attributes    │ │ - Attributes    │ │ - Attributes    │
└─────────────────┘ └─────────────────┘ └─────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      KPIAnalyzer                            │
│  - Fetches KPI set_based_definitions                        │
│  - Extracts required entities and columns                   │
│  - Infers appropriate rates                                 │
└─────────────────────────────────────────────────────────────┘
```
