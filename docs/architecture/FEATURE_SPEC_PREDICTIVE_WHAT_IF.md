# Feature Specification: Predictive What-If Scenarios

**Document Version:** 1.0  
**Date:** January 19, 2026  
**Product:** Northstar by MarketNova  
**Status:** In Development

---

## Executive Summary

Predictive What-If Scenarios enable users to **understand what drives their strategic outcomes** by identifying correlations between KPIs (or KPI groupings) and strategic objectives. Users can see which events, metrics, and business activities directly contribute to strategic objective success or failure, helping them understand the **levers that drive the business forward**.

This feature leverages the **Data Scientist Agent** as the primary analytical engine to:
- Correlate KPIs with strategic objectives to identify business drivers
- Quantify the contribution of individual KPIs to strategic success/failure
- Identify leading indicators that predict strategic objective achievement
- Predict outcomes of strategic changes with confidence intervals

**Core Value Proposition:**
> *"Understand what drives your strategic success. Northstar identifies the KPIs and business activities that directly impact your strategic objectives, so you know exactly which levers to pull to move the business forward."*

---

## Problem Statement

### Current Gap

| Capability | Northstar Today | Needed |
|------------|-----------------|--------|
| Historical KPI analysis | ✅ Analytics Hub | - |
| KPI-to-KPI correlation analysis | ✅ Data Scientist Agent | - |
| ML model recommendations | ✅ Data Scientist Agent | - |
| **KPI-to-Strategic Objective correlation** | ✅ Data Scientist Agent | ✅ |
| **Identify business drivers (levers)** | ✅ Data Scientist Agent | ✅ |
| **Quantify KPI contribution to objectives** | ✅ Data Scientist Agent | ✅ |
| **Leading indicator identification** | ✅ Data Scientist Agent | ✅ |
| **Predict outcome of strategic changes** | 🔄 In Progress | ✅ |
| **Multi-KPI cascade predictions** | 🔄 In Progress | ✅ |

### Business Need

**Primary Goal:** Executives need to understand **what drives their strategic outcomes** so they can focus efforts on the activities that matter most.

Specific needs:
1. **Identify business drivers** - Which KPIs directly contribute to strategic objective success/failure?
2. **Rank driver importance** - Which drivers have the biggest impact on strategic outcomes?
3. **Find leading indicators** - Which KPIs predict strategic success before it happens?
4. **Understand KPI groupings** - How do groups of KPIs collectively impact objectives?
5. **Predict strategic outcomes** - What is the likelihood of achieving strategic objectives?
6. **Simulate changes** - What happens to strategic objectives if we change key KPIs?

---

## Feature Overview

### Predictive What-If Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│              STRATEGIC OBJECTIVE CORRELATION & PREDICTIVE WHAT-IF               │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  STRATEGIC OBJECTIVE                                                             │
│  "Increase Market Share by 15%"                                                  │
│         │                                                                        │
│         ▼                                                                        │
│  ┌─────────────────────────────────────────────────────────────────────────┐    │
│  │                    DATA SCIENTIST AGENT (PRIMARY)                        │    │
│  │                                                                          │    │
│  │  STRATEGIC DRIVER ANALYSIS:                                              │    │
│  │  • analyze_strategic_objective_drivers: Find KPIs driving objectives     │    │
│  │  • calculate_driver_importance: Rank drivers by impact                   │    │
│  │  • identify_leading_indicators: Find predictive KPIs                     │    │
│  │  • analyze_kpi_groupings: Synergies & conflicts between drivers          │    │
│  │  • map_kpi_to_objectives: Trace KPIs to strategic hierarchy              │    │
│  │  • predict_objective_achievement: Forecast success probability           │    │
│  │                                                                          │    │
│  └─────────────────────────────────────────────────────────────────────────┘    │
│         │                                                                        │
│         ▼                                                                        │
│  ┌─────────────────────────────────────────────────────────────────────────┐    │
│  │                      BUSINESS DRIVER INSIGHTS                            │    │
│  │                                                                          │    │
│  │  TOP DRIVERS OF "Increase Market Share":                                 │    │
│  │  1. Customer Acquisition Rate    (35% contribution, leading indicator)   │    │
│  │  2. Brand Awareness Score        (25% contribution, 2-month lead)        │    │
│  │  3. Product Quality Rating       (20% contribution, direct driver)       │    │
│  │  4. Sales Rep Productivity       (12% contribution, operational lever)   │    │
│  │  5. Marketing Spend ROI          (8% contribution, synergy with #1)      │    │
│  │                                                                          │    │
│  │  ACHIEVEMENT PROBABILITY: 72% [95% CI: 65%-79%]                          │    │
│  │  RISK FACTORS: Customer Acquisition trending below target                │    │
│  │  RECOMMENDATION: Increase focus on top 3 drivers                         │    │
│  └─────────────────────────────────────────────────────────────────────────┘    │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Detailed Requirements

### 1. What-If Question Types

#### 1.1 Supported Question Categories

| Category | Example Questions |
|----------|-------------------|
| **Pricing** | "What if we raise prices by 10%?" |
| **Volume** | "What if sales volume increases by 25%?" |
| **Capacity** | "What if we add a second production shift?" |
| **Market** | "What if we expand to the European market?" |
| **Product** | "What if we launch a premium product tier?" |
| **Cost** | "What if raw material costs increase by 15%?" |
| **Staffing** | "What if we hire 10 more sales reps?" |
| **Customer** | "What if we improve NPS by 20 points?" |
| **Process** | "What if we reduce lead time by 30%?" |
| **External** | "What if a competitor enters our market?" |

#### 1.2 What-If Question Model

```python
class WhatIfQuestion(BaseModel):
    """A what-if question to analyze."""
    id: str
    question_text: str  # Natural language question
    
    # Parsed components
    change_type: Literal["increase", "decrease", "add", "remove", "change"]
    change_subject: str  # What is being changed (e.g., "price", "capacity")
    change_magnitude: Optional[float]  # Numeric change amount
    change_unit: Optional[str]  # Unit of change (%, $, units, etc.)
    
    # Context
    business_context: str
    affected_segments: List[str]  # Customer segments, regions, products
    time_horizon: Literal["immediate", "short_term", "medium_term", "long_term"]
    
    # Constraints
    constraints: List[Constraint]
    assumptions: List[str]
    
    # Metadata
    asked_by: str
    asked_at: datetime


class Constraint(BaseModel):
    """A constraint on the what-if analysis."""
    constraint_type: Literal["budget", "capacity", "regulatory", "contractual", "other"]
    description: str
    limit_value: Optional[float]
    limit_unit: Optional[str]
```

---

### 2. Prediction Engine

#### 2.1 Prediction Model

```python
class WhatIfPrediction(BaseModel):
    """Prediction results for a what-if question."""
    id: str
    question_id: str
    
    # Primary predictions
    primary_impacts: List[KPIImpactPrediction]
    
    # Cascade effects
    cascade_effects: List[CascadeEffect]
    
    # Net impact
    net_business_impact: NetImpact
    
    # Confidence
    overall_confidence: float  # 0-1
    data_quality_score: float  # 0-1
    model_reliability: float  # 0-1
    
    # Sensitivity analysis
    sensitivity_analysis: SensitivityAnalysis
    
    # Recommendations
    recommendations: List[Recommendation]
    optimal_value: Optional[OptimalValue]
    
    # Methodology
    methodology: PredictionMethodology
    
    # Metadata
    predicted_at: datetime
    prediction_duration_ms: int


class KPIImpactPrediction(BaseModel):
    """Predicted impact on a specific KPI."""
    kpi_code: str
    kpi_name: str
    business_level: Literal["tactical", "operational", "functional", "business_unit", "corporate"]
    
    # Current state
    current_value: float
    current_trend: Literal["increasing", "decreasing", "stable"]
    
    # Predicted state
    predicted_value: float
    predicted_change_absolute: float
    predicted_change_percent: float
    
    # Confidence interval
    confidence_level: float  # e.g., 0.95 for 95%
    lower_bound: float
    upper_bound: float
    
    # Impact classification
    impact_direction: Literal["positive", "negative", "neutral"]
    impact_magnitude: Literal["minimal", "moderate", "significant", "major"]
    
    # Time to impact
    time_to_impact: str  # e.g., "2-4 weeks"
    impact_duration: str  # e.g., "ongoing", "temporary (3 months)"
    
    # Evidence
    historical_evidence: List[HistoricalEvidence]
    correlation_strength: float


class CascadeEffect(BaseModel):
    """A cascade effect from primary impact to secondary KPIs."""
    trigger_kpi: str
    affected_kpi: str
    relationship_type: Literal["direct", "indirect", "lagged"]
    lag_periods: Optional[int]
    
    # Effect magnitude
    effect_multiplier: float  # e.g., 0.5 means 50% of trigger change
    predicted_change: float
    
    # Confidence
    confidence: float
    evidence_strength: Literal["strong", "moderate", "weak"]


class NetImpact(BaseModel):
    """Net business impact after all effects."""
    primary_impact_value: float
    cascade_impact_value: float
    total_impact_value: float
    
    # Financial summary
    revenue_impact: float
    cost_impact: float
    profit_impact: float
    
    # Risk-adjusted
    risk_adjusted_value: float
    risk_factors: List[str]
    
    # Recommendation
    recommendation: Literal["strongly_recommend", "recommend", "neutral", "caution", "not_recommended"]
    recommendation_rationale: str
```

#### 2.2 Prediction Methodology

```python
class PredictionMethodology(BaseModel):
    """How the prediction was generated."""
    
    # Data sources
    data_sources: List[DataSource]
    data_period: str  # e.g., "Last 24 months"
    data_points: int
    
    # Models used
    models_used: List[ModelUsed]
    
    # Correlation analysis
    correlations_analyzed: int
    significant_correlations: int
    
    # Validation
    backtesting_accuracy: float
    cross_validation_score: float


class ModelUsed(BaseModel):
    """An ML model used in the prediction."""
    model_type: str  # e.g., "XGBoost Regression"
    model_id: str
    purpose: str  # e.g., "Predict churn rate from price change"
    accuracy_metric: str
    accuracy_value: float
    feature_importance: Dict[str, float]
```

---

### 3. Agent Collaboration

#### 3.1 Operations Manager Agent Enhancements

Add new tools to the Operations Manager Agent:

```python
# New tools for Operations Manager Agent

ToolDefinition(
    name="initiate_what_if_analysis",
    description="Initiate a what-if analysis for a strategic question",
    parameters={
        "type": "object",
        "properties": {
            "question": {"type": "string", "description": "The what-if question"},
            "change_type": {
                "type": "string",
                "enum": ["increase", "decrease", "add", "remove", "change"]
            },
            "change_subject": {"type": "string"},
            "change_magnitude": {"type": "number"},
            "change_unit": {"type": "string"},
            "affected_kpis": {
                "type": "array",
                "items": {"type": "string"}
            },
            "business_context": {"type": "string"},
            "time_horizon": {
                "type": "string",
                "enum": ["immediate", "short_term", "medium_term", "long_term"]
            }
        },
        "required": ["question", "change_subject"]
    }
),

ToolDefinition(
    name="map_operational_dependencies",
    description="Map operational dependencies for a what-if scenario",
    parameters={
        "type": "object",
        "properties": {
            "primary_kpi": {"type": "string"},
            "dependency_depth": {"type": "integer", "default": 3},
            "include_external_factors": {"type": "boolean", "default": True}
        },
        "required": ["primary_kpi"]
    }
),

ToolDefinition(
    name="request_predictive_analysis",
    description="Request Data Scientist to perform predictive analysis",
    parameters={
        "type": "object",
        "properties": {
            "what_if_question_id": {"type": "string"},
            "kpis_to_predict": {
                "type": "array",
                "items": {"type": "string"}
            },
            "prediction_horizon": {"type": "string"},
            "confidence_level": {"type": "number", "default": 0.95},
            "include_sensitivity": {"type": "boolean", "default": True}
        },
        "required": ["what_if_question_id", "kpis_to_predict"]
    }
)
```

#### 3.2 Data Scientist Agent Enhancements

Add new tools to the Data Scientist Agent:

```python
# New tools for Data Scientist Agent

ToolDefinition(
    name="predict_kpi_impact",
    description="Predict the impact of a change on KPIs using ML models",
    parameters={
        "type": "object",
        "properties": {
            "what_if_question_id": {"type": "string"},
            "target_kpis": {
                "type": "array",
                "items": {"type": "string"}
            },
            "change_variable": {"type": "string"},
            "change_value": {"type": "number"},
            "prediction_method": {
                "type": "string",
                "enum": ["regression", "time_series", "causal_inference", "ensemble"]
            },
            "confidence_level": {"type": "number"}
        },
        "required": ["what_if_question_id", "target_kpis", "change_variable", "change_value"]
    }
),

ToolDefinition(
    name="analyze_cascade_effects",
    description="Analyze how changes cascade through KPI dependencies",
    parameters={
        "type": "object",
        "properties": {
            "primary_impact": {
                "type": "object",
                "properties": {
                    "kpi": {"type": "string"},
                    "change_percent": {"type": "number"}
                }
            },
            "cascade_depth": {"type": "integer", "default": 3},
            "include_feedback_loops": {"type": "boolean", "default": True}
        },
        "required": ["primary_impact"]
    }
),

ToolDefinition(
    name="run_sensitivity_analysis",
    description="Run sensitivity analysis on prediction parameters",
    parameters={
        "type": "object",
        "properties": {
            "prediction_id": {"type": "string"},
            "variable_to_vary": {"type": "string"},
            "variation_range": {
                "type": "object",
                "properties": {
                    "min": {"type": "number"},
                    "max": {"type": "number"},
                    "steps": {"type": "integer"}
                }
            }
        },
        "required": ["prediction_id", "variable_to_vary", "variation_range"]
    }
),

ToolDefinition(
    name="find_optimal_value",
    description="Find the optimal value for a variable to maximize/minimize a KPI",
    parameters={
        "type": "object",
        "properties": {
            "variable": {"type": "string"},
            "target_kpi": {"type": "string"},
            "optimization_goal": {
                "type": "string",
                "enum": ["maximize", "minimize"]
            },
            "constraints": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "kpi": {"type": "string"},
                        "operator": {"type": "string"},
                        "value": {"type": "number"}
                    }
                }
            },
            "search_range": {
                "type": "object",
                "properties": {
                    "min": {"type": "number"},
                    "max": {"type": "number"}
                }
            }
        },
        "required": ["variable", "target_kpi", "optimization_goal"]
    }
),

ToolDefinition(
    name="validate_prediction_accuracy",
    description="Validate prediction accuracy using backtesting",
    parameters={
        "type": "object",
        "properties": {
            "model_id": {"type": "string"},
            "validation_period": {"type": "string"},
            "validation_method": {
                "type": "string",
                "enum": ["holdout", "cross_validation", "time_series_split", "walk_forward"]
            }
        },
        "required": ["model_id", "validation_period"]
    }
)
```

#### 3.3 Collaboration Flow

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    WHAT-IF PREDICTION COLLABORATION FLOW                         │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  1. USER asks: "What if we raise prices by 10%?"                                │
│         │                                                                        │
│         ▼                                                                        │
│  2. MASTER COORDINATOR routes to OPERATIONS MANAGER                             │
│         │                                                                        │
│         ▼                                                                        │
│  3. OPERATIONS MANAGER:                                                          │
│     • Parses the question (change_type: increase, subject: price, magnitude: 10%)│
│     • Identifies affected KPIs: [Revenue, Churn Rate, CLV, Market Share]        │
│     • Maps operational dependencies                                              │
│     • Calls: request_predictive_analysis()                                       │
│         │                                                                        │
│         ▼                                                                        │
│  4. DATA SCIENTIST:                                                              │
│     • Retrieves historical data (price changes vs. KPI changes)                 │
│     • Analyzes correlations (price → revenue: +0.85, price → churn: +0.42)      │
│     • Applies ML models (XGBoost for revenue, Logistic for churn)               │
│     • Calculates predictions with confidence intervals                           │
│     • Analyzes cascade effects (churn → CLV → revenue)                          │
│     • Runs sensitivity analysis (optimal price increase: 7%)                     │
│     • Returns: WhatIfPrediction                                                  │
│         │                                                                        │
│         ▼                                                                        │
│  5. OPERATIONS MANAGER:                                                          │
│     • Interprets results in business context                                     │
│     • Adds operational recommendations                                           │
│     • Returns final prediction to user                                           │
│         │                                                                        │
│         ▼                                                                        │
│  6. USER receives:                                                               │
│     • Revenue: +$2.1M (+8.5%) [95% CI: +$1.8M to +$2.4M]                         │
│     • Churn Rate: +1.2% [95% CI: +0.8% to +1.6%]                                 │
│     • Net Impact: +$1.5M after churn adjustment                                  │
│     • Recommendation: Consider 7% increase (optimal point)                       │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

### 4. Prediction Models

#### 4.1 Pre-Built Prediction Models

| Model | Purpose | Input | Output |
|-------|---------|-------|--------|
| **Price Elasticity** | Predict demand change from price change | Price change % | Volume change %, Revenue change |
| **Churn Predictor** | Predict churn from various factors | Price, NPS, Usage | Churn probability |
| **Revenue Forecaster** | Predict revenue from multiple inputs | Volume, Price, Mix | Revenue |
| **Cost Estimator** | Predict cost from operational changes | Volume, Capacity, Staffing | Total Cost |
| **Capacity Planner** | Predict throughput from capacity changes | Resources, Shifts | Throughput, Lead Time |
| **Market Share** | Predict market share from competitive actions | Price, Marketing, Product | Market Share % |

#### 4.2 Model Training Pipeline

```python
class PredictionModelTrainer:
    """Trains prediction models from historical data."""
    
    async def train_price_elasticity_model(
        self,
        historical_data: pd.DataFrame,
        target_kpi: str,
        segments: List[str]
    ) -> TrainedModel:
        """
        Train a price elasticity model.
        
        Uses historical price changes and corresponding KPI changes
        to learn the elasticity relationship.
        """
        pass
    
    async def train_cascade_model(
        self,
        kpi_time_series: Dict[str, pd.Series],
        lag_periods: List[int]
    ) -> CascadeModel:
        """
        Train a model to predict cascade effects between KPIs.
        
        Uses Granger causality and VAR models to learn
        how changes in one KPI affect others over time.
        """
        pass
    
    async def train_scenario_model(
        self,
        scenario_type: str,
        historical_scenarios: List[HistoricalScenario]
    ) -> ScenarioModel:
        """
        Train a model from historical similar scenarios.
        
        Learns from past strategic decisions and their outcomes.
        """
        pass
```

---

### 5. UI Integration

#### 5.1 What-If Interface

Add to Insights Feed or as standalone section:

```
Insights Feed
├── AI Recommendations
├── Anomaly Alerts
├── Correlation Discoveries
└── **What-If Scenarios** (NEW)
    ├── Ask a Question
    ├── Saved Scenarios
    ├── Comparison View
    └── Prediction History
```

#### 5.2 What-If UI Components

| Component | Description |
|-----------|-------------|
| `WhatIfQuestionInput.tsx` | Natural language question input with suggestions |
| `QuestionParser.tsx` | Shows parsed question components |
| `PredictionProgress.tsx` | Real-time prediction progress |
| `ImpactVisualization.tsx` | Waterfall chart of KPI impacts |
| `CascadeGraph.tsx` | Visual graph of cascade effects |
| `ConfidenceDisplay.tsx` | Confidence intervals visualization |
| `SensitivityChart.tsx` | Sensitivity analysis chart |
| `OptimalValueFinder.tsx` | Interactive optimal value slider |
| `ScenarioComparison.tsx` | Compare multiple what-if scenarios |
| `PredictionHistory.tsx` | History of past predictions |

#### 5.3 Example UI Flow

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  🔮 WHAT-IF SCENARIOS                                                            │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  ┌─────────────────────────────────────────────────────────────────────────┐    │
│  │  Ask a what-if question...                                               │    │
│  │  ┌─────────────────────────────────────────────────────────────────────┐ │    │
│  │  │ What if we raise prices by 10%?                              [Ask] │ │    │
│  │  └─────────────────────────────────────────────────────────────────────┘ │    │
│  │                                                                          │    │
│  │  Suggestions:                                                            │    │
│  │  • What if we expand to Europe?                                          │    │
│  │  • What if we add a premium tier?                                        │    │
│  │  • What if we reduce lead time by 20%?                                   │    │
│  └─────────────────────────────────────────────────────────────────────────┘    │
│                                                                                  │
│  ┌─────────────────────────────────────────────────────────────────────────┐    │
│  │  PREDICTION RESULTS                                     Confidence: 87%  │    │
│  │  ─────────────────────────────────────────────────────────────────────── │    │
│  │                                                                          │    │
│  │  PRIMARY IMPACTS                                                         │    │
│  │  ┌─────────────────────────────────────────────────────────────────────┐ │    │
│  │  │  Revenue        ████████████████████░░░░  +$2.1M (+8.5%)            │ │    │
│  │  │                 [+$1.8M ─────────────────────────── +$2.4M]         │ │    │
│  │  │                                                                     │ │    │
│  │  │  Churn Rate     ██████░░░░░░░░░░░░░░░░░░  +1.2%                     │ │    │
│  │  │                 [+0.8% ─────────────────────────── +1.6%]           │ │    │
│  │  │                                                                     │ │    │
│  │  │  Customer LTV   ████████████░░░░░░░░░░░░  -$45 (-3.2%)              │ │    │
│  │  │                 [-$52 ─────────────────────────── -$38]             │ │    │
│  │  └─────────────────────────────────────────────────────────────────────┘ │    │
│  │                                                                          │    │
│  │  CASCADE EFFECTS                                                         │    │
│  │  ┌─────────────────────────────────────────────────────────────────────┐ │    │
│  │  │  Price ↑10% ──► Churn ↑1.2% ──► CLV ↓3.2% ──► Revenue ↓$0.6M       │ │    │
│  │  │                                                                     │ │    │
│  │  │  Net Revenue Impact: +$2.1M - $0.6M = +$1.5M                        │ │    │
│  │  └─────────────────────────────────────────────────────────────────────┘ │    │
│  │                                                                          │    │
│  │  OPTIMAL VALUE FINDER                                                    │    │
│  │  ┌─────────────────────────────────────────────────────────────────────┐ │    │
│  │  │  Price Increase:  0% ────────●──────────── 15%                      │ │    │
│  │  │                              7%                                      │ │    │
│  │  │                                                                     │ │    │
│  │  │  At 7% increase: Revenue +$1.8M, Churn +0.7%, Net +$1.6M (optimal)  │ │    │
│  │  └─────────────────────────────────────────────────────────────────────┘ │    │
│  │                                                                          │    │
│  │  RECOMMENDATION                                                          │    │
│  │  ┌─────────────────────────────────────────────────────────────────────┐ │    │
│  │  │  ✅ RECOMMEND: Proceed with 7% price increase                       │ │    │
│  │  │                                                                     │ │    │
│  │  │  Rationale: 7% increase maximizes net revenue while keeping churn   │ │    │
│  │  │  below the 1% threshold. Expected annual impact: +$1.6M.            │ │    │
│  │  │                                                                     │ │    │
│  │  │  [Save Scenario]  [Compare with Others]  [Create Action Plan]       │ │    │
│  │  └─────────────────────────────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────────────────────────────┘    │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

### 6. Backend Services

#### 6.1 Prediction Service

```
services/
└── business_services/
    └── prediction_service/
        ├── app/
        │   ├── main.py
        │   ├── models.py
        │   ├── api/
        │   │   └── endpoints.py
        │   ├── engine/
        │   │   ├── predictor.py
        │   │   ├── cascade_analyzer.py
        │   │   ├── sensitivity_analyzer.py
        │   │   └── optimizer.py
        │   ├── models/
        │   │   ├── price_elasticity.py
        │   │   ├── churn_predictor.py
        │   │   ├── revenue_forecaster.py
        │   │   └── cascade_model.py
        │   └── training/
        │       ├── trainer.py
        │       └── validator.py
        ├── Dockerfile
        └── requirements.txt
```

#### 6.2 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/what-if` | POST | Submit a what-if question |
| `/api/v1/what-if/{id}` | GET | Get prediction results |
| `/api/v1/what-if/{id}/cascade` | GET | Get cascade effects |
| `/api/v1/what-if/{id}/sensitivity` | GET | Get sensitivity analysis |
| `/api/v1/what-if/{id}/optimal` | GET | Get optimal value |
| `/api/v1/what-if/compare` | POST | Compare multiple scenarios |
| `/api/v1/models` | GET | List available prediction models |
| `/api/v1/models/{id}/accuracy` | GET | Get model accuracy metrics |
| `/api/v1/models/train` | POST | Trigger model training |

---

### 7. Data Requirements

#### 7.1 Historical Data Needed

| Data Type | Purpose | Minimum History |
|-----------|---------|-----------------|
| **KPI Time Series** | Correlation analysis, trend detection | 12 months |
| **Price History** | Price elasticity models | 24 months |
| **Customer Events** | Churn prediction | 12 months |
| **Operational Metrics** | Capacity/throughput models | 6 months |
| **Market Data** | Competitive analysis | 12 months |

#### 7.2 Data Quality Requirements

| Requirement | Threshold |
|-------------|-----------|
| Data completeness | >95% |
| Data freshness | <24 hours |
| Outlier handling | Documented |
| Seasonality adjustment | Applied |

---

### 8. Example Use Cases

#### Use Case 1: Price Increase Analysis

```
Question: "What if we raise prices by 10%?"

Operations Manager Analysis:
- Affected KPIs: Revenue, Churn Rate, CLV, Market Share
- Business Context: B2B SaaS, annual contracts
- Time Horizon: Medium-term (6-12 months)

Data Scientist Analysis:
- Historical correlation: Price ↑1% → Revenue ↑0.85%, Churn ↑0.12%
- Model: XGBoost regression (R² = 0.89)
- Confidence: 87%

Predictions:
| KPI | Current | Predicted | Change | 95% CI |
|-----|---------|-----------|--------|--------|
| Revenue | $24.5M | $26.6M | +8.5% | [+7.2%, +9.8%] |
| Churn Rate | 8.2% | 9.4% | +1.2% | [+0.8%, +1.6%] |
| CLV | $1,420 | $1,375 | -3.2% | [-4.1%, -2.3%] |

Cascade Effects:
- Churn ↑1.2% → Lost customers → Revenue ↓$0.6M
- Net Revenue: +$2.1M - $0.6M = +$1.5M

Optimal Value:
- 7% increase maximizes net revenue (+$1.6M)
- Above 12%, churn impact exceeds revenue gain

Recommendation: Proceed with 7% increase
```

#### Use Case 2: Capacity Expansion

```
Question: "What if we add a second production shift?"

Operations Manager Analysis:
- Affected KPIs: Throughput, Lead Time, Labor Cost, Quality
- Business Context: Manufacturing, current capacity at 85%
- Time Horizon: Immediate (1-3 months)

Data Scientist Analysis:
- Historical data: Previous shift additions
- Model: Capacity planning regression
- Confidence: 92%

Predictions:
| KPI | Current | Predicted | Change |
|-----|---------|-----------|--------|
| Throughput | 1,000/day | 1,850/day | +85% |
| Lead Time | 5 days | 2.8 days | -44% |
| Labor Cost | $2.1M/mo | $3.8M/mo | +81% |
| Defect Rate | 1.2% | 1.8% | +50% |

Trade-off Analysis:
- Revenue from increased throughput: +$4.2M/mo
- Additional labor cost: +$1.7M/mo
- Quality cost (defects): +$0.3M/mo
- Net benefit: +$2.2M/mo

Recommendation: Proceed, but invest in quality training
```

---

### 9. Implementation Phases

#### Phase 1: Core Prediction (Weeks 1-4)
- [ ] What-if question parsing
- [ ] Basic prediction models (price elasticity, churn)
- [ ] Single KPI predictions
- [ ] Confidence intervals

#### Phase 2: Cascade Analysis (Weeks 5-8)
- [ ] KPI dependency mapping
- [ ] Cascade effect prediction
- [ ] Multi-KPI predictions
- [ ] Net impact calculation

#### Phase 3: Optimization (Weeks 9-12)
- [ ] Sensitivity analysis
- [ ] Optimal value finder
- [ ] Constraint handling
- [ ] Scenario comparison

#### Phase 4: Agent Integration (Weeks 13-16)
- [ ] Operations Manager enhancements
- [ ] Data Scientist enhancements
- [ ] Collaboration flow
- [ ] Natural language interface

---

### 10. Success Metrics

| Metric | Target |
|--------|--------|
| Prediction accuracy (backtested) | >80% |
| User satisfaction with predictions | >4.0/5.0 |
| Time to get prediction | <30 seconds |
| Predictions per user per month | >5 |
| Predictions that led to action | >40% |

---

### 11. Dependencies

- Historical KPI data (12+ months)
- Data Scientist Agent (existing)
- Operations Manager Agent (existing)
- ML Service (existing)
- Analytics Hub (for historical data)

---

*Document maintained by MarketNova Product Team*
