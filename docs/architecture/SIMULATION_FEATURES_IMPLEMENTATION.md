# Simulation Features Implementation Plan

**Status:** In Development  
**Date:** February 1, 2026

This document tracks the implementation of two key simulation capabilities:
1. **Predictive What-If Scenarios** - Strategic objective correlation and ML-based outcome prediction
2. **Process Scenario Modeler** - Discrete event simulation

---

## Primary Goal: Strategic Objective Correlation

**The key goal of the ML capabilities is to identify correlations between KPIs (or KPI groupings) and strategic objectives, so that business users can understand what events are directly contributing to strategic objective outcomes, success, or failure. They understand the levers that are driving the business forward.**

This is the **primary responsibility of the Data Scientist Agent**.

---

## Implementation Status

### Phase 1: Foundation (Completed)

| Component | Status | Location |
|-----------|--------|----------|
| KPI Correlation Fields | ✅ Complete | `MetricDefinition.correlated_with` |
| Relationship Storage | ✅ Complete | `MetadataRelationship` table |
| ML Service Scaffold | ✅ Complete | `machine_learning_service/` |
| Data Scientist Agent | ✅ Complete | `business_agents/agents.py` |
| **Strategic Objective Tools** | ✅ Complete | Data Scientist Agent (6 new tools) |
| UI Pages (Mock) | ✅ Complete | `PredictiveWhatIfPage.tsx`, `ProcessScenarioModelerPage.tsx` |
| Database Migration | ✅ Complete | `alembic/versions/20260201_113600_add_simulation_features_tables.py` |
| Process Simulation Service | ✅ Complete | `services/business_services/process_simulation_service/` |
| ProcessScenarioModelerAgent | ✅ Complete | `business_agents/agents.py` (registered in orchestrator) |
| Docker Compose Entry | ✅ Complete | Port 8027 |

### Phase 2: Predictive What-If (Week 1-2)

| Task | Status | Details |
|------|--------|---------|
| KPI Dependency Graph API | 🔄 In Progress | Add relationship types: `leads_to`, `affects`, `derived_from` |
| ML Model Types | ⏳ Pending | Price elasticity, churn prediction, revenue forecaster |
| Training Pipeline | ⏳ Pending | Connect to historical KPI data |
| Data Scientist Tools | ⏳ Pending | Wire to real ML Service |
| UI Integration | ⏳ Pending | Replace mock data with API calls |

### Phase 3: Process Simulation (Week 3-4)

| Task | Status | Details |
|------|--------|---------|
| Process Simulation Service | ⏳ Pending | New microservice |
| DES Engine | ⏳ Pending | SimPy-based simulator |
| ProcessScenarioModelerAgent | ⏳ Pending | New agent |
| Process Definition Tables | ⏳ Pending | Database schema |
| UI Integration | ⏳ Pending | Connect to simulation API |

---

## Architecture

### Predictive What-If Data Flow

```
┌─────────────────────┐
│  User Question      │
│  "What if +10%?"    │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐     ┌─────────────────────┐
│  Conversation       │────▶│  Data Scientist     │
│  Service            │     │  Agent              │
└─────────────────────┘     └─────────┬───────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          │                           │                           │
          ▼                           ▼                           ▼
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│  Business Metadata  │     │  Machine Learning   │     │  Database Service   │
│  (KPI Dependencies) │     │  Service            │     │  (Historical Data)  │
└─────────────────────┘     │  (/inference)       │     └─────────────────────┘
                            └─────────────────────┘
```

### Process Simulation Data Flow

```
┌─────────────────────┐
│  Process Definition │
│  (BPMN-style)       │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐     ┌─────────────────────┐
│  Scenario           │────▶│  Process Simulation │
│  Parameters         │     │  Service            │
└─────────────────────┘     │  (DES Engine)       │
                            └─────────┬───────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          │                           │                           │
          ▼                           ▼                           ▼
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│  Event Log          │     │  KPI Predictions    │     │  Bottleneck         │
│  (TimescaleDB)      │     │                     │     │  Analysis           │
└─────────────────────┘     └─────────────────────┘     └─────────────────────┘
```

---

## KPI Dependency Relationship Types

Add these relationship types to `metadata_relationships`:

| Type | Description | Example |
|------|-------------|---------|
| `kpi_leads_to` | Leading indicator relationship | Customer Satisfaction → Revenue |
| `kpi_affects` | Causal impact | Price → Volume → Revenue |
| `kpi_derived_from` | Calculation dependency | Profit = Revenue - Cost |
| `kpi_correlated_with` | Statistical correlation | Churn ↔ NPS |

---

## ML Models Required

### 1. Price Elasticity Model
- **Type:** Regression
- **Input:** Price change %, historical price-volume data
- **Output:** Predicted volume change, revenue impact
- **Algorithm:** Polynomial regression or XGBoost

### 2. Churn Predictor
- **Type:** Classification
- **Input:** Customer attributes, engagement metrics
- **Output:** Churn probability, segment risk
- **Algorithm:** Logistic regression, Random Forest

### 3. Revenue Forecaster
- **Type:** Time Series
- **Input:** Historical revenue, seasonality
- **Output:** Point forecast + confidence interval
- **Algorithm:** Prophet or ARIMA

### 4. KPI Cascade Model
- **Type:** Causal inference
- **Input:** KPI dependency graph, historical correlations
- **Output:** Multi-KPI impact predictions
- **Algorithm:** Structural equation modeling / VAR

---

## Database Schema Additions

### KPI Correlation History (TimescaleDB)

```sql
CREATE TABLE kpi_correlations (
    time TIMESTAMPTZ NOT NULL,
    kpi_a_code VARCHAR(100) NOT NULL,
    kpi_b_code VARCHAR(100) NOT NULL,
    correlation_coefficient DECIMAL(5,4),
    correlation_method VARCHAR(50),  -- pearson, spearman
    lag_periods INTEGER DEFAULT 0,
    p_value DECIMAL(10,8),
    sample_size INTEGER,
    CONSTRAINT pk_kpi_correlations PRIMARY KEY (time, kpi_a_code, kpi_b_code)
);
SELECT create_hypertable('kpi_correlations', 'time');
```

### Process Definitions

```sql
CREATE TABLE process_definitions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code VARCHAR(100) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    value_chain_module VARCHAR(100),
    definition JSONB NOT NULL,
    linked_kpis JSONB DEFAULT '[]',
    version INTEGER DEFAULT 1,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE process_scenarios (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    process_id UUID REFERENCES process_definitions(id),
    parameter_changes JSONB NOT NULL,
    simulation_config JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE simulation_runs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    scenario_id UUID REFERENCES process_scenarios(id),
    status VARCHAR(50) NOT NULL,
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    results JSONB,
    error TEXT
);
```

---

## API Endpoints

### Predictive What-If API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `POST /api/v1/what-if/analyze` | POST | Submit what-if question |
| `GET /api/v1/what-if/{id}` | GET | Get prediction results |
| `POST /api/v1/what-if/sensitivity` | POST | Run sensitivity analysis |
| `POST /api/v1/what-if/optimize` | POST | Find optimal value |
| `GET /api/v1/kpi-dependencies/{code}` | GET | Get KPI dependency graph |

### Process Simulation API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `GET/POST /api/v1/processes` | GET/POST | CRUD process definitions |
| `GET/POST /api/v1/scenarios` | GET/POST | CRUD scenarios |
| `POST /api/v1/simulations` | POST | Start simulation |
| `GET /api/v1/simulations/{id}` | GET | Get results |
| `POST /api/v1/simulations/compare` | POST | Compare scenarios |

---

## Next Steps

1. **Add KPI dependency relationship types** to Business Metadata
2. **Implement correlation calculation** in Calculation Engine
3. **Add ML training endpoints** to Machine Learning Service
4. **Wire Data Scientist Agent** tools to real services
5. **Create Process Simulation Service** scaffold
6. **Implement DES engine** with SimPy
7. **Connect UI pages** to real APIs

---

## Related Documents

- [FEATURE_SPEC_PREDICTIVE_WHAT_IF.md](./FEATURE_SPEC_PREDICTIVE_WHAT_IF.md)
- [FEATURE_SPEC_PROCESS_SCENARIO_MODELER.md](./FEATURE_SPEC_PROCESS_SCENARIO_MODELER.md)
- [FEATURE_ARCHITECTURE.md](./FEATURE_ARCHITECTURE.md)
