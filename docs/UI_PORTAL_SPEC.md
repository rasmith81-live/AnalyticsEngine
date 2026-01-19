# Northstar Client Portal - UI Specification

**Document Version:** 1.0  
**Date:** January 19, 2026  
**Product:** Northstar by MarketNova

---

## Executive Summary

This document defines the UI/UX specification for the Northstar Client Portal—the central hub where clients design, maintain, and analyze their business strategy with AI-powered guidance.

**Core Philosophy:**
> *"Northstar is the platform that closes the loop between strategy and execution—your strategy isn't just a document, it's connected to your actual business systems and provides immediate feedback on how well you're executing."*

---

## The Northstar Workflow

The portal UI is organized around the complete client lifecycle:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              NORTHSTAR CLIENT WORKFLOW                                           │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐       │
│  │   PHASE 1   │   │   PHASE 2   │   │   PHASE 3   │   │   PHASE 4   │   │   PHASE 5   │       │
│  │   DESIGN    │ → │  SIMULATE   │ → │   DEPLOY    │ → │   ANALYZE   │ → │   EVOLVE    │       │
│  └─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘       │
│                                                                                                  │
│  • Initial interview    • Generate test data   • Sign contract      • Real-time KPIs    • Refine models    │
│  • Design business model• Present analytics    • Deploy to env      • Correlations      • Update strategy  │
│  • Identify gaps        • Validate design      • Connect systems    • AI insights       • Build documents  │
│  • Create proposal      • Resolve gaps         • Map attributes     • Recommendations   • Collaborative    │
│                                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Detailed Workflow Steps

| Step | Phase | Description | Portal Section |
|------|-------|-------------|----------------|
| 1 | Design | Initial AI interview with executives | Design Studio → Conversation |
| 2 | Design | Design business model (value chain, KPIs) | Design Studio → Business Model |
| 3 | Simulate | Present analytics using generated/simulated data | Analytics Hub → Simulation |
| 4 | Simulate | Identify design gaps and resolve | Design Studio → Gap Analysis |
| 5 | Deploy | Put together implementation plan and estimate | Proposal Center |
| 6 | Deploy | Sign application user license contract | Proposal Center → Contract |
| 7 | Deploy | Receive funds | (External) |
| 8 | Deploy | Deploy system to user environment | Deployment → System Setup |
| 9 | Deploy | Connect to corporate systems (ERP, CRM, etc.) | Deployment → Data Sources |
| 10 | Deploy | Map system attributes to analytic objects | Deployment → Mapping |
| 11 | Analyze | Present real-time calculation analytics | Analytics Hub → Live Dashboards |
| 12 | Analyze | Identify correlations and insights | Insights Feed |
| 13 | Analyze | Provide strategy and operational recommendations | Insights Feed → Recommendations |
| 14 | Evolve | Refine models based on feedback | Design Studio → Refinement |
| 15 | Evolve | Build strategy documents | Strategy Documents |
| 16 | Evolve | Open any section, modify, update direction | All Sections (Collaborative) |

---

## Portal Structure

### Main Navigation

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  🌟 NORTHSTAR                                          [Client Name] [Profile] │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  ┌──────────────────┐                                                           │
│  │ 📊 STRATEGY      │  ← Home dashboard, health score, alerts                   │
│  │    CENTER        │                                                           │
│  ├──────────────────┤                                                           │
│  │ 🎨 DESIGN        │  ← Business model design, AI interviews                   │
│  │    STUDIO        │                                                           │
│  ├──────────────────┤                                                           │
│  │ 📈 ANALYTICS     │  ← Real-time dashboards, simulation                       │
│  │    HUB           │                                                           │
│  ├──────────────────┤                                                           │
│  │ 💡 INSIGHTS      │  ← AI recommendations, correlations                       │
│  │    FEED          │                                                           │
│  ├──────────────────┤                                                           │
│  │ 📄 STRATEGY      │  ← Generated documents, presentations                     │
│  │    DOCUMENTS     │                                                           │
│  ├──────────────────┤                                                           │
│  │ 🚀 DEPLOYMENT    │  ← System connections, mapping                            │
│  │    CENTER        │                                                           │
│  ├──────────────────┤                                                           │
│  │ 📋 PROPOSAL      │  ← Estimates, contracts, SOW                              │
│  │    CENTER        │                                                           │
│  └──────────────────┘                                                           │
│                                                                                  │
│  ┌──────────────────┐                                                           │
│  │ 💬 AI STRATEGIST │  ← Always-available chat with 26 agents                   │
│  └──────────────────┘                                                           │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Current Frontend Component Mapping

### Existing Pages → New Portal Sections

| Current Page | Current Route | New Portal Section | Workflow Phase |
|--------------|---------------|-------------------|----------------|
| `ConversationServicePage.tsx` | `/conversation-service` | **Design Studio** → AI Interview | Phase 1: Design |
| `OntologyManagerPage.tsx` | `/ontology-studio` | **Design Studio** → Business Model | Phase 1: Design |
| `ConfigPage.tsx` | `/config` | **Design Studio** → KPI Configuration | Phase 1: Design |
| `ObjectModelsBrowser.tsx` | `/object-models` | **Design Studio** → Object Models | Phase 1: Design |
| `SimulationPage.tsx` | `/simulation` | **Analytics Hub** → Simulation | Phase 2: Simulate |
| `AnalyticsDemoPage.tsx` | `/analytics-demo` | **Analytics Hub** → Live Dashboards | Phase 2/4: Simulate/Analyze |
| `ServiceProposal.tsx` | `/proposal` | **Proposal Center** | Phase 3: Deploy |
| `DataSourceConfig.tsx` | `/data-sources` | **Deployment Center** → Data Sources | Phase 3: Deploy |
| `MappingPage.tsx` | `/mapping` | **Deployment Center** → Mapping | Phase 3: Deploy |
| `GovernancePage.tsx` | `/governance` | **Deployment Center** → Governance | Phase 3: Deploy |
| `AdminPage.tsx` | `/admin` | **Deployment Center** → Admin | Phase 3: Deploy |
| `MLDashboardPage.tsx` | `/ml-registry` | **Analytics Hub** → ML Models | Phase 4: Analyze |
| `SystemMonitorPage.tsx` | `/system-monitor` | **Deployment Center** → System Monitor | All Phases |
| `ExcelImportPage.tsx` | `/excel-import` | **Design Studio** → Import | Phase 1: Design |
| `DemoPage.tsx` | `/demo` | **Strategy Center** (Home) | All Phases |

### Components → Portal Features

| Current Component | New Portal Feature | Section |
|-------------------|-------------------|---------|
| `OntologyGraph.tsx` | Business Model Visualization | Design Studio |
| `OntologyTreeView.tsx` | Hierarchical Model Browser | Design Studio |
| `KPITreeSelector.tsx` | KPI Selection & Configuration | Design Studio |
| `KPICard.tsx` | KPI Dashboard Cards | Analytics Hub |
| `KPISampleVisualization.tsx` | KPI Charts & Trends | Analytics Hub |
| `ValueChainNode.tsx` | Value Chain Diagram | Design Studio |
| `ObjectModelDiagram.tsx` | Domain Model Viewer | Design Studio |
| `LineageGraph.tsx` | Data Lineage View | Analytics Hub |
| `ResourceScheduler.tsx` | Implementation Timeline | Proposal Center |
| `ProjectGanttChart.tsx` | Project Plan | Proposal Center |

---

## New Portal Sections (Detailed)

### 1. Strategy Center (Home Dashboard)

**Purpose:** Executive command center showing real-time health of business strategy.

**Components:**
| Component | Description | Data Source |
|-----------|-------------|-------------|
| Strategy Health Score | 0-100 score based on KPI performance | Calculation Engine |
| Active Alerts | AI-detected anomalies, risks, opportunities | ML Service |
| Quick Insights | Top 3 AI recommendations | Insights Feed |
| Workflow Progress | Current phase indicator | Session State |
| System Status | Connected systems health | System Monitor |
| Recent Activity | Timeline of changes | Audit Log |

**New Development Required:**
- [ ] Strategy Health Score widget
- [ ] Alert notification system
- [ ] Workflow progress indicator
- [ ] Activity timeline component

---

### 2. Design Studio

**Purpose:** Where business strategy is designed through AI conversation.

**Sub-sections:**
| Sub-section | Current Component | Enhancement Needed |
|-------------|-------------------|-------------------|
| AI Interview | `ConversationServicePage.tsx` | Rename, integrate with workflow |
| Business Model | `OntologyManagerPage.tsx` | Add value chain canvas view |
| KPI Configuration | `ConfigPage.tsx` | Integrate with business model |
| Object Models | `ObjectModelsBrowser.tsx` | Link to KPIs |
| Gap Analysis | NEW | Identify missing KPIs, data sources |
| Import | `ExcelImportPage.tsx` | Streamline for business users |

**New Development Required:**
- [ ] Gap Analysis view (compare designed model vs. available data)
- [ ] Business Model Canvas view (visual, interactive)
- [ ] Porter's Five Forces visualization
- [ ] Value Chain interactive diagram
- [ ] Competitive Landscape view

---

### 3. Analytics Hub

**Purpose:** Real-time dashboards connected to corporate systems.

**Sub-sections:**
| Sub-section | Current Component | Enhancement Needed |
|-------------|-------------------|-------------------|
| Simulation | `SimulationPage.tsx` | Rename to "Design Validation" |
| Live Dashboards | `AnalyticsDemoPage.tsx` | Multi-level selector (tactical→strategic) |
| Trend Analysis | NEW | Historical performance, forecasts |
| ML Models | `MLDashboardPage.tsx` | Integrate predictions into dashboards |
| Data Lineage | `LineageGraph.tsx` | Expand to full data flow |
| **Process Scenario Modeler** | NEW | Process simulation, what-if scenarios |
| **Predictive What-If** | NEW | Strategic change impact prediction |

**New Development Required:**
- [ ] Level selector (Tactical → Operational → Functional → BU → Corporate)
- [ ] Drill-down capability (click metric → see underlying data)
- [ ] Trend analysis with forecasting
- [ ] Threshold/alert configuration UI
- [ ] Real-time data freshness indicators
- [ ] Process Scenario Modeler UI (see Section 3.1)
- [ ] Predictive What-If UI (see Section 3.2)

---

### 3.1 Process Scenario Modeler

**Purpose:** Digital twin for process simulation—test process changes before implementing them.

**Layout:**
```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  PROCESS SCENARIO MODELER                                    [New Process ▼]   │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  ┌─────────────────────────────────────────┐  ┌──────────────────────────────┐ │
│  │         PROCESS DESIGNER                │  │      SCENARIO PANEL          │ │
│  │  ┌─────────────────────────────────┐   │  │                              │ │
│  │  │                                 │   │  │  📋 Scenarios                │ │
│  │  │   [Start] ──► [Step 1] ──►     │   │  │  ├─ Baseline (current)       │ │
│  │  │                    │            │   │  │  ├─ +20% Capacity ✓          │ │
│  │  │                    ▼            │   │  │  └─ Automation Option        │ │
│  │  │              [Decision]         │   │  │                              │ │
│  │  │               /     \           │   │  │  [+ New Scenario]            │ │
│  │  │              ▼       ▼          │   │  │                              │ │
│  │  │         [Step 2A] [Step 2B]     │   │  ├──────────────────────────────┤ │
│  │  │              \       /          │   │  │  PARAMETER CHANGES           │ │
│  │  │               ▼     ▼           │   │  │                              │ │
│  │  │              [End]              │   │  │  Step: Order Processing      │ │
│  │  │                                 │   │  │  Duration: 10min → 8min      │ │
│  │  └─────────────────────────────────┘   │  │  Resources: 2 → 3            │ │
│  │                                         │  │  Defect Rate: 2% → 1%       │ │
│  │  [Add Step] [Add Decision] [Connect]   │  │                              │ │
│  └─────────────────────────────────────────┘  └──────────────────────────────┘ │
│                                                                                  │
│  ┌──────────────────────────────────────────────────────────────────────────┐  │
│  │                        SIMULATION RESULTS                                 │  │
│  ├──────────────────────────────────────────────────────────────────────────┤  │
│  │                                                                           │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │  │
│  │  │ Cycle Time  │  │ Throughput  │  │ Utilization │  │    Cost     │     │  │
│  │  │   -15%  ▼   │  │   +22%  ▲   │  │    78%      │  │   -8%   ▼   │     │  │
│  │  │  4.2 → 3.6h │  │  45 → 55/hr │  │  ████████░░ │  │ $12 → $11   │     │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘     │  │
│  │                                                                           │  │
│  │  BOTTLENECK ANALYSIS                    KPI IMPACT PREDICTION            │  │
│  │  ┌────────────────────────────┐        ┌────────────────────────────┐   │  │
│  │  │ Step          │ Util │ Wait│        │ KPI              │ Impact  │   │  │
│  │  │───────────────┼──────┼─────│        │──────────────────┼─────────│   │  │
│  │  │ Order Process │ 95%  │ 12m │ ⚠️     │ Order Cycle Time │ -15%    │   │  │
│  │  │ Quality Check │ 72%  │ 3m  │        │ Customer Sat.    │ +8%     │   │  │
│  │  │ Shipping      │ 45%  │ 1m  │        │ Operating Cost   │ -8%     │   │  │
│  │  └────────────────────────────┘        └────────────────────────────┘   │  │
│  │                                                                           │  │
│  │  [Run Simulation]  [Compare Scenarios]  [Export Results]                 │  │
│  └──────────────────────────────────────────────────────────────────────────┘  │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

**Components:**

| Component | Description | Priority |
|-----------|-------------|----------|
| Process Designer Canvas | BPMN-style drag-and-drop process builder | High |
| Step Properties Panel | Configure duration, cost, resources, defect rate | High |
| Scenario Manager | Create, compare, and manage what-if scenarios | High |
| Parameter Change Editor | Define changes for each scenario | High |
| Simulation Runner | Execute simulation with progress indicator | High |
| Results Dashboard | Cycle time, throughput, utilization, cost metrics | High |
| Bottleneck Heatmap | Visual identification of constraints | Medium |
| KPI Impact Cards | Predicted impact on linked KPIs | High |
| Scenario Comparison Chart | Side-by-side bar/radar charts | Medium |
| Resource Utilization Timeline | Gantt-style resource view | Medium |

**New Development Required:**
- [ ] `ProcessDesignerCanvas.tsx` - BPMN-style process flow editor
- [ ] `ProcessStepNode.tsx` - Draggable step component
- [ ] `ProcessTransitionEdge.tsx` - Connection lines with conditions
- [ ] `StepPropertiesPanel.tsx` - Step configuration sidebar
- [ ] `ScenarioManager.tsx` - Scenario list and creation
- [ ] `ParameterChangeEditor.tsx` - Before/after parameter editing
- [ ] `SimulationRunner.tsx` - Run button with progress
- [ ] `SimulationResultsDashboard.tsx` - Metrics cards and charts
- [ ] `BottleneckHeatmap.tsx` - Utilization visualization
- [ ] `ScenarioComparisonChart.tsx` - Multi-scenario comparison
- [ ] `KPIImpactCards.tsx` - Predicted KPI changes

**API Endpoints Required:**
```typescript
POST /api/v1/process-simulation/processes          // Create process
GET  /api/v1/process-simulation/processes/:id      // Get process
POST /api/v1/process-simulation/scenarios          // Create scenario
POST /api/v1/process-simulation/simulate           // Run simulation
GET  /api/v1/process-simulation/results/:id        // Get results
POST /api/v1/process-simulation/compare            // Compare scenarios
```

---

### 3.2 Predictive What-If Analysis

**Purpose:** Ask strategic "what-if" questions and get AI-powered predictions with confidence intervals.

**Layout:**
```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  PREDICTIVE WHAT-IF ANALYSIS                                                    │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  ┌──────────────────────────────────────────────────────────────────────────┐  │
│  │  💬 ASK A WHAT-IF QUESTION                                                │  │
│  │  ┌────────────────────────────────────────────────────────────────────┐  │  │
│  │  │ "What if we increase prices by 10%?"                            🎤 │  │  │
│  │  └────────────────────────────────────────────────────────────────────┘  │  │
│  │                                                                           │  │
│  │  Quick Questions:                                                         │  │
│  │  [Price +10%] [Capacity +20%] [New Product] [Market Expansion] [Custom]  │  │
│  └──────────────────────────────────────────────────────────────────────────┘  │
│                                                                                  │
│  ┌──────────────────────────────────────────────────────────────────────────┐  │
│  │  📊 PREDICTION RESULTS                              Confidence: 87% ████░ │  │
│  ├──────────────────────────────────────────────────────────────────────────┤  │
│  │                                                                           │  │
│  │  PRIMARY IMPACTS                                                          │  │
│  │  ┌─────────────────────────────────────────────────────────────────────┐ │  │
│  │  │                                                                      │ │  │
│  │  │   Revenue        Churn Rate      Profit Margin    Market Share     │ │  │
│  │  │   ┌────┐         ┌────┐          ┌────┐           ┌────┐           │ │  │
│  │  │   │+8% │ ▲       │+3% │ ▲        │+12%│ ▲         │-2% │ ▼         │ │  │
│  │  │   │    │         │    │          │    │           │    │           │ │  │
│  │  │   │████│         │████│          │████│           │████│           │ │  │
│  │  │   └────┘         └────┘          └────┘           └────┘           │ │  │
│  │  │   ±2.1%          ±0.8%           ±3.2%            ±1.1%            │ │  │
│  │  │                                                                      │ │  │
│  │  └─────────────────────────────────────────────────────────────────────┘ │  │
│  │                                                                           │  │
│  │  CASCADE EFFECTS                                                          │  │
│  │  ┌─────────────────────────────────────────────────────────────────────┐ │  │
│  │  │  Price ──► Revenue (+8%) ──► Profit (+12%)                          │ │  │
│  │  │    │                                                                 │ │  │
│  │  │    └──► Churn (+3%) ──► Customer LTV (-5%) ──► Long-term Rev (-2%) │ │  │
│  │  │                                                                      │ │  │
│  │  │    └──► Market Share (-2%) ──► Competitive Position (Caution)      │ │  │
│  │  └─────────────────────────────────────────────────────────────────────┘ │  │
│  │                                                                           │  │
│  │  NET IMPACT SUMMARY                                                       │  │
│  │  ┌─────────────────────────────────────────────────────────────────────┐ │  │
│  │  │  💰 Revenue Impact: +$2.4M/year    📈 Profit Impact: +$1.8M/year   │ │  │
│  │  │  ⚠️  Risk Factors: Churn increase, competitive response             │ │  │
│  │  │  ✅ Recommendation: PROCEED WITH CAUTION - Monitor churn closely    │ │  │
│  │  └─────────────────────────────────────────────────────────────────────┘ │  │
│  │                                                                           │  │
│  └──────────────────────────────────────────────────────────────────────────┘  │
│                                                                                  │
│  ┌────────────────────────────────┐  ┌────────────────────────────────────┐   │
│  │  SENSITIVITY ANALYSIS          │  │  OPTIMAL VALUE FINDER              │   │
│  │  ┌──────────────────────────┐ │  │                                     │   │
│  │  │     Revenue vs Price     │ │  │  Optimize: Revenue                  │   │
│  │  │  ▲                       │ │  │  Variable: Price Change             │   │
│  │  │  │      ╭────╮           │ │  │  Constraint: Churn < 5%             │   │
│  │  │  │    ╭─╯    ╰─╮         │ │  │                                     │   │
│  │  │  │  ╭─╯        ╰─╮       │ │  │  ┌─────────────────────────────┐   │   │
│  │  │  │╭─╯            ╰─╮     │ │  │  │ Optimal Price: +7.2%        │   │   │
│  │  │  ├─────────────────►     │ │  │  │ Predicted Revenue: +$2.8M   │   │   │
│  │  │    -10%  0%  +10% +20%   │ │  │  │ Churn stays at: 4.8%        │   │   │
│  │  └──────────────────────────┘ │  │  └─────────────────────────────┘   │   │
│  │  [Adjust Range]               │  │  [Find Optimal] [Add Constraint]   │   │
│  └────────────────────────────────┘  └────────────────────────────────────┘   │
│                                                                                  │
│  ┌──────────────────────────────────────────────────────────────────────────┐  │
│  │  METHODOLOGY & EVIDENCE                                                   │  │
│  │  Models Used: Price Elasticity (R²=0.89), Churn Predictor (AUC=0.92)     │  │
│  │  Data Period: Last 24 months (1,248 data points)                          │  │
│  │  Historical Evidence: Q3 2024 price increase showed similar pattern       │  │
│  │  [View Full Methodology] [Export Report]                                  │  │
│  └──────────────────────────────────────────────────────────────────────────┘  │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

**Components:**

| Component | Description | Priority |
|-----------|-------------|----------|
| What-If Question Input | Natural language input with voice support | High |
| Quick Question Chips | Pre-defined common scenarios | Medium |
| Primary Impact Cards | KPI predictions with confidence intervals | High |
| Cascade Flow Diagram | Visual flow of cause-effect relationships | High |
| Net Impact Summary | Financial summary with recommendation | High |
| Sensitivity Chart | Interactive curve showing variable sensitivity | Medium |
| Optimal Value Finder | Optimization with constraints | Medium |
| Methodology Panel | Transparency on models and data used | Medium |
| Historical Evidence | Past events supporting predictions | Low |

**New Development Required:**
- [ ] `WhatIfQuestionInput.tsx` - Natural language input with parsing
- [ ] `QuickQuestionChips.tsx` - Pre-defined scenario buttons
- [ ] `PrimaryImpactCards.tsx` - KPI impact with confidence bars
- [ ] `CascadeFlowDiagram.tsx` - D3/React Flow cascade visualization
- [ ] `NetImpactSummary.tsx` - Financial summary card
- [ ] `SensitivityChart.tsx` - Interactive sensitivity curve
- [ ] `OptimalValueFinder.tsx` - Optimization panel with constraints
- [ ] `MethodologyPanel.tsx` - Model transparency section
- [ ] `HistoricalEvidenceList.tsx` - Supporting past events
- [ ] `ConfidenceIndicator.tsx` - Visual confidence level

**API Endpoints Required:**
```typescript
POST /api/v1/what-if/questions                     // Submit question
GET  /api/v1/what-if/questions/:id                 // Get parsed question
POST /api/v1/what-if/predict                       // Get predictions
POST /api/v1/what-if/cascade                       // Analyze cascade effects
POST /api/v1/what-if/sensitivity                   // Run sensitivity analysis
POST /api/v1/what-if/optimize                      // Find optimal value
GET  /api/v1/what-if/predictions/:id               // Get full prediction
```

**Agent Collaboration Flow (UI Perspective):**
```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        WHAT-IF ANALYSIS FLOW                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  User Input ──► Operations Manager ──► Data Scientist ──► Results           │
│                       │                      │                               │
│                       ▼                      ▼                               │
│              Parse question          Apply ML models                         │
│              Map dependencies        Calculate confidence                    │
│              Identify KPIs           Analyze cascades                        │
│                                      Find optimal values                     │
│                                                                              │
│  UI Updates:                                                                 │
│  1. Show "Analyzing..." with agent avatars                                  │
│  2. Stream partial results as available                                     │
│  3. Display final prediction with methodology                               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 4. Insights Feed

**Purpose:** Continuous stream of AI-discovered opportunities and recommendations.

**Components:**
| Component | Description | Priority |
|-----------|-------------|----------|
| Insight Cards | AI-generated insights with impact score | High |
| Recommendation Actions | Accept, Dismiss, Explore Further | High |
| Category Filters | Growth, Risk, Efficiency, Competitive, Anomaly | Medium |
| Agent Attribution | Which AI agent discovered this | Medium |
| Insight History | Archive with actions taken | Medium |

**New Development Required:**
- [ ] Insight card component
- [ ] Recommendation action workflow
- [ ] Insight categorization system
- [ ] Historical insight browser
- [ ] Insight → Action tracking

---

### 5. Strategy Documents

**Purpose:** Auto-generated strategy presentations and documents.

**Document Types:**
| Document | Description | Generation Trigger |
|----------|-------------|-------------------|
| Executive Summary | 1-page strategy overview | On demand |
| Board Deck | Quarterly strategy presentation | Scheduled |
| KPI Report | Performance metrics summary | Scheduled/On demand |
| Competitive Analysis | Market positioning report | On demand |
| Implementation Plan | Technical deployment guide | After proposal |

**New Development Required:**
- [ ] Document generation service
- [ ] Template management
- [ ] PDF/PowerPoint export
- [ ] Version control for documents
- [ ] Collaborative editing

---

### 6. Deployment Center

**Purpose:** System connections, data mapping, and governance.

**Sub-sections:**
| Sub-section | Current Component | Enhancement Needed |
|-------------|-------------------|-------------------|
| Data Sources | `DataSourceConfig.tsx` | Add connection wizard |
| Mapping | `MappingPage.tsx` | Visual mapping interface |
| Governance | `GovernancePage.tsx` | Policy management |
| Admin | `AdminPage.tsx` | User/role management |
| System Monitor | `SystemMonitorPage.tsx` | Real-time health |

**New Development Required:**
- [ ] Connection wizard (step-by-step)
- [ ] Visual attribute mapping (drag-and-drop)
- [ ] Data quality indicators
- [ ] Connection health monitoring

---

### 7. Proposal Center

**Purpose:** Implementation estimates, contracts, and SOW management.

**Sub-sections:**
| Sub-section | Current Component | Enhancement Needed |
|-------------|-------------------|-------------------|
| Estimate Builder | `ServiceProposal.tsx` | Integrate with designed model |
| Resource Plan | `ResourceScheduler.tsx` | Timeline view |
| Project Plan | `ProjectGanttChart.tsx` | Milestones |
| Contract | NEW | License agreement, e-signature |
| Payment | NEW | Invoice tracking |

**New Development Required:**
- [ ] Contract generation and e-signature
- [ ] Payment/invoice tracking
- [ ] SOW document generation
- [ ] Approval workflow

---

### 8. AI Strategist (Persistent Chat)

**Purpose:** Always-available AI advisor accessible from any section.

**Features:**
| Feature | Description |
|---------|-------------|
| Context Awareness | Knows current view, selected items |
| Agent Selector | Choose specific agent (Strategist, Analyst, Architect) |
| Action Suggestions | AI proposes next steps |
| Voice Input | Optional speech-to-text |
| History | Conversation archive |

**Current Component:** `ConversationServicePage.tsx` (to be refactored as floating panel)

**New Development Required:**
- [ ] Floating chat panel component
- [ ] Context injection from current view
- [ ] Agent selector dropdown
- [ ] Voice input integration
- [ ] Conversation history sidebar

---

## Proposed New Route Structure

```typescript
const routes = [
  // Strategy Center (Home)
  { path: '/', element: <StrategyCenter /> },
  
  // Design Studio
  { path: '/design', element: <DesignStudioLayout /> },
  { path: '/design/interview', element: <AIInterviewPage /> },
  { path: '/design/business-model', element: <BusinessModelPage /> },
  { path: '/design/kpis', element: <KPIConfigPage /> },
  { path: '/design/objects', element: <ObjectModelsPage /> },
  { path: '/design/gaps', element: <GapAnalysisPage /> },
  { path: '/design/import', element: <ImportPage /> },
  
  // Analytics Hub
  { path: '/analytics', element: <AnalyticsHubLayout /> },
  { path: '/analytics/simulation', element: <SimulationPage /> },
  { path: '/analytics/dashboards', element: <DashboardsPage /> },
  { path: '/analytics/trends', element: <TrendAnalysisPage /> },
  { path: '/analytics/ml', element: <MLModelsPage /> },
  { path: '/analytics/process-modeler', element: <ProcessScenarioModelerPage /> },
  { path: '/analytics/what-if', element: <PredictiveWhatIfPage /> },
  
  // Insights Feed
  { path: '/insights', element: <InsightsFeedPage /> },
  
  // Strategy Documents
  { path: '/documents', element: <DocumentsPage /> },
  { path: '/documents/:docId', element: <DocumentViewerPage /> },
  
  // Deployment Center
  { path: '/deployment', element: <DeploymentLayout /> },
  { path: '/deployment/sources', element: <DataSourcesPage /> },
  { path: '/deployment/mapping', element: <MappingPage /> },
  { path: '/deployment/governance', element: <GovernancePage /> },
  { path: '/deployment/admin', element: <AdminPage /> },
  { path: '/deployment/monitor', element: <SystemMonitorPage /> },
  
  // Proposal Center
  { path: '/proposal', element: <ProposalLayout /> },
  { path: '/proposal/estimate', element: <EstimatePage /> },
  { path: '/proposal/contract', element: <ContractPage /> },
  { path: '/proposal/project', element: <ProjectPlanPage /> },
];
```

---

## User Personas & Views

| Persona | Primary Sections | Key Actions |
|---------|-----------------|-------------|
| **CEO/Executive** | Strategy Center, Insights Feed | Review health, approve recommendations |
| **Strategy Lead** | Design Studio, Strategy Documents | Design model, create presentations |
| **Business Analyst** | Analytics Hub, Insights Feed | Deep-dive metrics, explore correlations |
| **IT/Data Engineer** | Deployment Center | Connect systems, map data |
| **Operations Manager** | Analytics Hub (Tactical level) | Monitor operational KPIs |
| **Board Member** | Strategy Documents | Review quarterly deck |

---

## Visual Design Principles

1. **Clean & Executive-Ready** - Suitable for board presentations
2. **Real-Time Indicators** - Pulse animations, live data badges
3. **AI Presence** - Subtle indicators when AI is analyzing
4. **Dark/Light Mode** - Professional appearance for any setting
5. **Mobile-Responsive** - Key insights accessible on mobile
6. **Workflow Awareness** - Always show current phase, next steps

---

## Implementation Priority

### Phase 1: Core Restructure (Weeks 1-4)
- [ ] New navigation structure
- [ ] Strategy Center home page
- [ ] Rename/reorganize existing pages
- [ ] Floating AI chat panel

### Phase 2: Design Studio & Analytics Enhancements (Weeks 5-8)
- [ ] Business Model Canvas view
- [ ] Gap Analysis page
- [ ] Porter's visualizations
- [ ] Competitive Landscape view
- [ ] **Process Scenario Modeler** - Process Designer Canvas
- [ ] **Process Scenario Modeler** - Scenario Manager
- [ ] **Predictive What-If** - Question Input & Quick Chips

### Phase 3: Simulation & Prediction Features (Weeks 9-12)
- [ ] **Process Scenario Modeler** - Simulation Runner & Results Dashboard
- [ ] **Process Scenario Modeler** - Bottleneck Heatmap & KPI Impact Cards
- [ ] **Predictive What-If** - Primary Impact Cards & Cascade Flow Diagram
- [ ] **Predictive What-If** - Net Impact Summary
- [ ] Insights Feed page
- [ ] Insight card components

### Phase 4: Advanced Analytics & Documents (Weeks 13-16)
- [ ] **Process Scenario Modeler** - Scenario Comparison Charts
- [ ] **Predictive What-If** - Sensitivity Chart & Optimal Value Finder
- [ ] **Predictive What-If** - Methodology Panel
- [ ] Document generation
- [ ] Strategy document templates

### Phase 5: Deployment & Proposal (Weeks 17-20)
- [ ] Connection wizard
- [ ] Visual mapping interface
- [ ] Contract/e-signature
- [ ] Payment tracking

---

## Technical Considerations

### State Management
- Workflow phase state (global)
- Current client context
- AI conversation history
- Real-time data subscriptions

### Real-Time Updates
- WebSocket connections for live KPIs
- Server-Sent Events for insights
- Polling for system status

### Performance
- Lazy loading for heavy components (graphs, charts)
- Virtual scrolling for large data sets
- Caching for frequently accessed data

---

*Document maintained by MarketNova Product Team*
