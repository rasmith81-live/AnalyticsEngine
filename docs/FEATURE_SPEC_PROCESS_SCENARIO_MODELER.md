# Feature Specification: Process Scenario Modeler

**Document Version:** 1.0  
**Date:** January 19, 2026  
**Product:** Northstar by MarketNova  
**Status:** Proposed

---

## Executive Summary

The Process Scenario Modeler enables users to simulate business process execution and test "what-if" scenarios before implementing changes. This feature bridges the gap between strategy design (what to measure) and process design (how work flows), allowing organizations to validate operational changes against their strategic KPIs.

**Core Value Proposition:**
> *"Test your strategic changes in a digital sandbox before deploying to production. See how process modifications impact your KPIs across all levels—from tactical operations to corporate strategy."*

---

## Problem Statement

### Current Gap

| Capability | Northstar Today | ARIS (Competitor) |
|------------|-----------------|-------------------|
| Design business strategy | ✅ AI-assisted | ❌ Manual |
| Define KPIs | ✅ Auto-generated | ❌ Separate tools |
| Simulate KPI data | ✅ SimulationPage | ❌ |
| **Simulate process execution** | ❌ **GAP** | ✅ Process Digital Twin |
| **Test process changes** | ❌ **GAP** | ✅ Scenario Simulation |
| **Compare designed vs. actual** | ❌ **GAP** | ✅ Process Mining |

### Business Need

Organizations need to:
1. Test process changes before implementation (reduce risk)
2. Predict KPI impact of operational decisions
3. Validate that process changes align with strategic goals
4. Compare multiple scenarios to find optimal solutions

---

## Feature Overview

### Process Scenario Modeler Components

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                       PROCESS SCENARIO MODELER                                   │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐             │
│  │  PROCESS        │    │  SCENARIO       │    │  IMPACT         │             │
│  │  DESIGNER       │ →  │  SIMULATOR      │ →  │  ANALYZER       │             │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘             │
│                                                                                  │
│  • Define process flows    • Run simulations     • KPI impact analysis         │
│  • Set parameters          • Apply scenarios     • Bottleneck detection        │
│  • Link to KPIs            • Generate events     • Optimization recommendations│
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Detailed Requirements

### 1. Process Designer

**Purpose:** Define and visualize business processes linked to the value chain.

#### 1.1 Process Definition Model

```python
class ProcessDefinition(BaseModel):
    """A business process that can be simulated."""
    id: str
    code: str
    name: str
    description: Optional[str]
    
    # Process structure
    steps: List[ProcessStep]
    transitions: List[ProcessTransition]
    
    # Linkage to strategy
    value_chain_module: str  # Links to value chain module
    linked_kpis: List[str]   # KPIs affected by this process
    
    # Simulation parameters
    default_parameters: Dict[str, Any]
    resource_requirements: List[ResourceRequirement]
    
    # Metadata
    created_at: datetime
    updated_at: datetime
    version: int


class ProcessStep(BaseModel):
    """A single step in a process."""
    id: str
    name: str
    step_type: Literal["task", "decision", "parallel_gateway", "event", "subprocess"]
    
    # Timing
    duration_distribution: DurationDistribution
    
    # Resources
    required_resources: List[str]
    resource_quantity: int = 1
    
    # Cost
    fixed_cost: float = 0.0
    variable_cost_per_unit: float = 0.0
    
    # Quality
    defect_rate: float = 0.0  # Probability of defect/rework
    
    # Capacity
    max_concurrent: Optional[int] = None


class ProcessTransition(BaseModel):
    """Transition between process steps."""
    from_step: str
    to_step: str
    condition: Optional[str]  # For decision gateways
    probability: float = 1.0  # For probabilistic routing


class DurationDistribution(BaseModel):
    """Statistical distribution for step duration."""
    distribution_type: Literal["fixed", "normal", "exponential", "triangular", "uniform"]
    parameters: Dict[str, float]  # e.g., {"mean": 10, "std": 2} for normal
```

#### 1.2 Process Designer UI

| Component | Description |
|-----------|-------------|
| **Canvas** | Drag-and-drop BPMN-style process designer |
| **Step Library** | Pre-built step templates (Task, Decision, Gateway, Event) |
| **Property Panel** | Configure step parameters, durations, costs |
| **KPI Linker** | Connect process steps to affected KPIs |
| **Validation** | Check process completeness and consistency |

---

### 2. Scenario Simulator

**Purpose:** Run simulations with different parameter configurations.

#### 2.1 Scenario Definition Model

```python
class ScenarioDefinition(BaseModel):
    """A what-if scenario to simulate."""
    id: str
    name: str
    description: Optional[str]
    
    # Base process
    process_id: str
    
    # Parameter overrides
    parameter_changes: List[ParameterChange]
    
    # Simulation settings
    simulation_duration: timedelta
    warm_up_period: timedelta
    number_of_replications: int = 10
    random_seed: Optional[int] = None
    
    # Input assumptions
    arrival_rate: ArrivalDistribution
    initial_wip: int = 0


class ParameterChange(BaseModel):
    """A change to apply in a scenario."""
    change_type: Literal["step_duration", "resource_capacity", "defect_rate", 
                         "cost", "routing_probability", "arrival_rate"]
    target: str  # Step ID or resource ID
    parameter: str
    original_value: Any
    new_value: Any
    change_description: str


class ArrivalDistribution(BaseModel):
    """Distribution of work item arrivals."""
    distribution_type: Literal["constant", "poisson", "from_data"]
    parameters: Dict[str, Any]
    # For "from_data": use historical arrival patterns
```

#### 2.2 Simulation Engine

```python
class ProcessSimulationEngine:
    """Discrete event simulation engine for process scenarios."""
    
    async def run_simulation(
        self,
        process: ProcessDefinition,
        scenario: ScenarioDefinition,
        context: AgentContext
    ) -> SimulationResult:
        """
        Run a discrete event simulation of the process.
        
        Returns:
            SimulationResult with KPI predictions and event log
        """
        pass
    
    async def compare_scenarios(
        self,
        process: ProcessDefinition,
        scenarios: List[ScenarioDefinition],
        comparison_kpis: List[str]
    ) -> ScenarioComparison:
        """
        Compare multiple scenarios side-by-side.
        """
        pass


class SimulationResult(BaseModel):
    """Results from a process simulation."""
    id: str
    scenario_id: str
    
    # Timing metrics
    avg_cycle_time: float
    min_cycle_time: float
    max_cycle_time: float
    cycle_time_std: float
    
    # Throughput metrics
    total_completed: int
    throughput_rate: float  # per hour
    
    # Resource utilization
    resource_utilization: Dict[str, float]  # resource_id -> utilization %
    
    # Cost metrics
    total_cost: float
    cost_per_unit: float
    
    # Quality metrics
    defect_count: int
    defect_rate: float
    rework_count: int
    
    # Bottleneck analysis
    bottlenecks: List[BottleneckInfo]
    
    # KPI predictions
    predicted_kpi_values: Dict[str, KPIPrediction]
    
    # Event log (for detailed analysis)
    event_log: List[SimulationEvent]
    
    # Confidence intervals
    confidence_level: float = 0.95
    confidence_intervals: Dict[str, Tuple[float, float]]


class KPIPrediction(BaseModel):
    """Predicted KPI value from simulation."""
    kpi_code: str
    baseline_value: float
    predicted_value: float
    change_percent: float
    confidence_interval: Tuple[float, float]
    impact_direction: Literal["positive", "negative", "neutral"]
```

#### 2.3 Scenario Simulator UI

| Component | Description |
|-----------|-------------|
| **Scenario Builder** | Create scenarios with parameter changes |
| **Comparison View** | Side-by-side scenario comparison |
| **Animation** | Visual process flow animation during simulation |
| **Progress Tracker** | Real-time simulation progress |
| **Results Dashboard** | KPI predictions, bottlenecks, recommendations |

---

### 3. Impact Analyzer

**Purpose:** Analyze simulation results and predict KPI impacts.

#### 3.1 Impact Analysis Model

```python
class ImpactAnalysis(BaseModel):
    """Analysis of scenario impact on KPIs."""
    id: str
    scenario_id: str
    
    # KPI impacts
    kpi_impacts: List[KPIImpact]
    
    # Strategic alignment
    strategic_alignment_score: float  # 0-100
    aligned_objectives: List[str]
    conflicting_objectives: List[str]
    
    # Risk assessment
    risk_level: Literal["low", "medium", "high", "critical"]
    risks: List[RiskItem]
    
    # Recommendations
    recommendations: List[Recommendation]
    
    # Trade-offs
    trade_offs: List[TradeOff]


class KPIImpact(BaseModel):
    """Impact on a specific KPI."""
    kpi_code: str
    kpi_name: str
    business_level: Literal["tactical", "operational", "functional", "business_unit", "corporate"]
    
    current_value: float
    predicted_value: float
    change_absolute: float
    change_percent: float
    
    impact_type: Literal["improvement", "degradation", "neutral"]
    confidence: float
    
    # Cascade effects
    upstream_effects: List[str]  # KPIs that influence this
    downstream_effects: List[str]  # KPIs influenced by this


class TradeOff(BaseModel):
    """Trade-off between competing objectives."""
    improving_kpi: str
    degrading_kpi: str
    improvement_amount: float
    degradation_amount: float
    net_business_value: float
    recommendation: str
```

---

### 4. Agent Integration

#### 4.1 Process Scenario Modeler Agent

New agent to be added to the multi-agent architecture:

```python
class ProcessScenarioModelerAgent(BaseAgent):
    """
    Process Scenario Modeler Agent for process simulation and what-if analysis.
    
    Responsibilities:
    - Design and validate process definitions
    - Create and run simulation scenarios
    - Analyze simulation results
    - Predict KPI impacts
    - Recommend process optimizations
    - Collaborate with Operations Manager and Data Scientist
    """
    
    def _get_system_prompt(self) -> str:
        return """You are an expert Process Simulation Specialist.

## Your Role
You help organizations test process changes in a digital sandbox before 
implementing them in production. You bridge strategy design with operational 
execution by predicting how process changes will impact KPIs.

## Core Responsibilities

### 1. Process Design
- Define process flows from value chain modules
- Set step parameters (duration, cost, resources)
- Link processes to strategic KPIs
- Validate process completeness

### 2. Scenario Creation
- Create what-if scenarios with parameter changes
- Define simulation parameters
- Set up comparison scenarios

### 3. Simulation Execution
- Run discrete event simulations
- Generate event logs
- Calculate performance metrics

### 4. Impact Analysis
- Predict KPI impacts
- Identify bottlenecks
- Assess strategic alignment
- Recommend optimizations

## Collaboration
- Work with Operations Manager to understand operational context
- Work with Data Scientist to validate predictions statistically
- Work with Business Strategist to ensure strategic alignment

## Tools Available
- design_process: Create process definition from value chain
- create_scenario: Define what-if scenario
- run_simulation: Execute process simulation
- analyze_impact: Analyze KPI impacts
- compare_scenarios: Compare multiple scenarios
- identify_bottlenecks: Find process bottlenecks
- recommend_optimizations: Generate optimization recommendations
- request_statistical_validation: Ask Data Scientist to validate
"""
    
    def _get_process_scenario_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="design_process",
                description="Design a process definition from value chain module",
                parameters={
                    "type": "object",
                    "properties": {
                        "process_name": {"type": "string"},
                        "value_chain_module": {"type": "string"},
                        "steps": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "step_type": {"type": "string"},
                                    "duration_mean": {"type": "number"},
                                    "duration_std": {"type": "number"},
                                    "cost": {"type": "number"}
                                }
                            }
                        },
                        "linked_kpis": {
                            "type": "array",
                            "items": {"type": "string"}
                        }
                    },
                    "required": ["process_name", "value_chain_module", "steps"]
                }
            ),
            ToolDefinition(
                name="create_scenario",
                description="Create a what-if scenario with parameter changes",
                parameters={
                    "type": "object",
                    "properties": {
                        "scenario_name": {"type": "string"},
                        "process_id": {"type": "string"},
                        "parameter_changes": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "change_type": {"type": "string"},
                                    "target": {"type": "string"},
                                    "parameter": {"type": "string"},
                                    "new_value": {}
                                }
                            }
                        },
                        "simulation_duration_hours": {"type": "number"},
                        "replications": {"type": "integer"}
                    },
                    "required": ["scenario_name", "process_id", "parameter_changes"]
                }
            ),
            ToolDefinition(
                name="run_simulation",
                description="Execute a process simulation",
                parameters={
                    "type": "object",
                    "properties": {
                        "scenario_id": {"type": "string"},
                        "real_time_updates": {"type": "boolean"}
                    },
                    "required": ["scenario_id"]
                }
            ),
            ToolDefinition(
                name="analyze_impact",
                description="Analyze the impact of a scenario on KPIs",
                parameters={
                    "type": "object",
                    "properties": {
                        "simulation_result_id": {"type": "string"},
                        "focus_kpis": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "include_cascade_effects": {"type": "boolean"}
                    },
                    "required": ["simulation_result_id"]
                }
            ),
            ToolDefinition(
                name="compare_scenarios",
                description="Compare multiple scenarios side-by-side",
                parameters={
                    "type": "object",
                    "properties": {
                        "scenario_ids": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "comparison_kpis": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "ranking_criteria": {"type": "string"}
                    },
                    "required": ["scenario_ids"]
                }
            ),
            ToolDefinition(
                name="recommend_optimizations",
                description="Generate process optimization recommendations",
                parameters={
                    "type": "object",
                    "properties": {
                        "process_id": {"type": "string"},
                        "optimization_goals": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "constraints": {
                            "type": "object",
                            "properties": {
                                "max_cost_increase": {"type": "number"},
                                "min_quality_level": {"type": "number"},
                                "resource_limits": {"type": "object"}
                            }
                        }
                    },
                    "required": ["process_id", "optimization_goals"]
                }
            )
        ]
```

#### 4.2 Coordinator Integration

Add delegation to Process Scenario Modeler in the Master Coordinator:

```python
ToolDefinition(
    name="delegate_to_process_scenario_modeler",
    description="Delegate to Process Scenario Modeler for process simulation and what-if analysis",
    parameters={
        "type": "object",
        "properties": {
            "task": {"type": "string"},
            "task_type": {
                "type": "string",
                "enum": ["design_process", "create_scenario", "run_simulation", 
                         "analyze_impact", "compare_scenarios", "optimize"]
            },
            "process_context": {"type": "string"}
        },
        "required": ["task"]
    }
)
```

---

### 5. UI Integration

#### 5.1 New Portal Section: Process Modeler

Add to Design Studio:

```
Design Studio
├── AI Interview
├── Business Model
├── KPI Configuration
├── Object Models
├── Gap Analysis
├── Import
└── **Process Modeler** (NEW)
    ├── Process Designer
    ├── Scenario Builder
    ├── Simulation Runner
    └── Impact Analysis
```

#### 5.2 Process Modeler Page Components

| Component | Description |
|-----------|-------------|
| `ProcessDesigner.tsx` | BPMN-style process canvas |
| `StepLibrary.tsx` | Draggable step templates |
| `StepProperties.tsx` | Step configuration panel |
| `ScenarioBuilder.tsx` | Create/edit scenarios |
| `SimulationRunner.tsx` | Run and monitor simulations |
| `ImpactDashboard.tsx` | KPI impact visualization |
| `ScenarioComparison.tsx` | Side-by-side comparison |
| `ProcessAnimation.tsx` | Animated process flow |

---

### 6. Backend Services

#### 6.1 New Service: Process Simulation Service

```
services/
└── business_services/
    └── process_simulation_service/
        ├── app/
        │   ├── main.py
        │   ├── models.py
        │   ├── api/
        │   │   └── endpoints.py
        │   ├── engine/
        │   │   ├── simulator.py
        │   │   ├── event_generator.py
        │   │   └── statistics.py
        │   └── analysis/
        │       ├── impact_analyzer.py
        │       └── bottleneck_detector.py
        ├── Dockerfile
        └── requirements.txt
```

#### 6.2 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/processes` | GET/POST | List/create process definitions |
| `/api/v1/processes/{id}` | GET/PUT/DELETE | CRUD for process |
| `/api/v1/scenarios` | GET/POST | List/create scenarios |
| `/api/v1/scenarios/{id}` | GET/PUT/DELETE | CRUD for scenario |
| `/api/v1/simulations` | POST | Start simulation |
| `/api/v1/simulations/{id}` | GET | Get simulation status/results |
| `/api/v1/simulations/{id}/events` | GET | Get event log |
| `/api/v1/analysis/impact` | POST | Analyze KPI impact |
| `/api/v1/analysis/compare` | POST | Compare scenarios |
| `/api/v1/analysis/bottlenecks` | POST | Detect bottlenecks |

---

### 7. Data Model

#### 7.1 Database Tables

```sql
-- Process definitions
CREATE TABLE process_definitions (
    id UUID PRIMARY KEY,
    code VARCHAR(100) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    value_chain_module VARCHAR(100),
    definition JSONB NOT NULL,  -- Full process structure
    version INTEGER DEFAULT 1,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Scenarios
CREATE TABLE scenarios (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    process_id UUID REFERENCES process_definitions(id),
    parameter_changes JSONB NOT NULL,
    simulation_config JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Simulation runs
CREATE TABLE simulation_runs (
    id UUID PRIMARY KEY,
    scenario_id UUID REFERENCES scenarios(id),
    status VARCHAR(50) NOT NULL,
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    results JSONB,
    error TEXT
);

-- Simulation events (hypertable for time-series)
CREATE TABLE simulation_events (
    time TIMESTAMPTZ NOT NULL,
    simulation_id UUID NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    step_id VARCHAR(100),
    entity_id VARCHAR(100),
    event_data JSONB
);
SELECT create_hypertable('simulation_events', 'time');
```

---

### 8. Integration with Existing Features

#### 8.1 Value Chain Integration

- Processes are derived from value chain modules
- Each process step maps to value chain activities
- KPI linkage flows from value chain → process → step

#### 8.2 Simulation Service Integration

- Reuse existing `SimulationPage` patterns
- Extend simulator to support process-level simulation
- Share event generation infrastructure

#### 8.3 Analytics Integration

- Simulation results feed into Analytics Hub
- Compare simulated vs. actual performance
- Use historical data to calibrate simulation parameters

---

### 9. Example Use Cases

#### Use Case 1: Reduce Order Cycle Time

```
Scenario: "Reduce Order Cycle Time by 20%"

Parameter Changes:
- Order Processing step: duration -30%
- Add parallel gateway for credit check
- Increase warehouse staff by 2

Simulation Results:
- Cycle Time: 5.2 days → 4.1 days (-21%)
- Throughput: +15%
- Cost per Order: +$2.50 (+8%)
- Customer Satisfaction (predicted): +12 NPS points

Trade-off Analysis:
- Improving cycle time increases labor cost
- Net business value: +$1.2M annually (faster delivery > labor cost)
```

#### Use Case 2: Compare Automation Options

```
Scenarios to Compare:
1. Baseline (current state)
2. Partial Automation (automate data entry)
3. Full Automation (RPA for entire process)

Comparison Results:
| Metric | Baseline | Partial | Full |
|--------|----------|---------|------|
| Cycle Time | 5.2 days | 4.0 days | 2.1 days |
| Cost/Unit | $45 | $38 | $25 |
| Defect Rate | 3.2% | 2.1% | 0.8% |
| Implementation Cost | $0 | $150K | $500K |
| ROI (1 year) | - | 180% | 95% |

Recommendation: Partial Automation (best ROI)
```

---

### 10. Implementation Phases

#### Phase 1: Core Simulation (Weeks 1-4)
- [ ] Process definition model
- [ ] Basic simulation engine
- [ ] Simple scenario creation
- [ ] Results storage

#### Phase 2: UI & Visualization (Weeks 5-8)
- [ ] Process designer canvas
- [ ] Scenario builder UI
- [ ] Results dashboard
- [ ] Process animation

#### Phase 3: Impact Analysis (Weeks 9-12)
- [ ] KPI impact prediction
- [ ] Bottleneck detection
- [ ] Scenario comparison
- [ ] Optimization recommendations

#### Phase 4: Agent Integration (Weeks 13-16)
- [ ] Process Scenario Modeler Agent
- [ ] Coordinator integration
- [ ] Cross-agent collaboration
- [ ] Natural language scenario creation

---

## Success Metrics

| Metric | Target |
|--------|--------|
| Simulation accuracy vs. actual | >85% |
| Time to create scenario | <10 minutes |
| Scenarios per process | >5 average |
| User adoption | >60% of clients |
| Process changes validated before deployment | >80% |

---

## Dependencies

- Existing Simulation Service infrastructure
- Value Chain definitions from Business Metadata
- KPI definitions and calculations
- Operations Manager Agent (collaboration)
- Data Scientist Agent (statistical validation)

---

*Document maintained by MarketNova Product Team*
