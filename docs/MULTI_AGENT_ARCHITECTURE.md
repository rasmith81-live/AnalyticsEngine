# Multi-Agent Architecture for Analytics Engine

## Overview

This document describes the multi-agent architecture for the Analytics Engine, leveraging Anthropic's Claude Agent SDK to create a collaborative AI system for business value chain design.

## Architecture Summary

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    CLIENT INTERVIEW SESSION                                          │
│                                 (Conversation Service WebSocket)                                     │
│                                                                                                      │
│  4 Core Questions:                                                                                   │
│  1. Describe your business, business model, and strategic priorities                                │
│  2. What pain points are you trying to address through analytics?                                   │
│  3. How will you measure success?                                                                   │
│  4. What decisions would you make with this information?                                            │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                    │
                                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              STRATEGY COORDINATOR (Claude Opus 4.5)                                  │
│  ┌─────────────────────────────────────────────────────────────────────────────────────────────────┐│
│  │ • Listens and responds to C-suite executives (Porter's frameworks)                              ││
│  │ • Applies Five Forces, Value Chain, Generic Strategies internally                              ││
│  │ • Asks ONE pertinent follow-up question when gaps identified                                   ││
│  │ • Orchestrates 24 specialized sub-agents after gathering sufficient context                    ││
│  │ • Synthesizes results into cohesive business model                                             ││
│  └─────────────────────────────────────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                    │
    ┌───────────────────────────────────────────────┼───────────────────────────────────────────────┐
    │                                               │                                               │
    ▼                                               ▼                                               ▼
┌─────────────────────────────────────┐ ┌─────────────────────────────────────┐ ┌─────────────────────────────────────┐
│      STRATEGY & ANALYSIS LAYER      │ │       TECHNICAL DESIGN LAYER        │ │      BUSINESS OPERATIONS LAYER      │
├─────────────────────────────────────┤ ├─────────────────────────────────────┤ ├─────────────────────────────────────┤
│ • Business Strategist               │ │ • Architect                         │ │ • Sales Manager                     │
│ • Business Analyst                  │ │ • Developer                         │ │ • Marketing Manager                 │
│ • Data Analyst                      │ │ • Tester                            │ │ • Accountant                        │
│ • Data Scientist                    │ │ • Documenter                        │ │ • Customer Success Manager          │
│ • Operations Manager                │ │ • Deployment Specialist             │ │ • HR/Talent Analyst                 │
│ • Mapping Specialist                │ │ • UI Designer                       │ │ • Supply Chain Analyst              │
│                                     │ │ • ITIL Manager                      │ │ • Risk & Compliance Officer         │
│                                     │ │ • Connection Specialist             │ │ • Project Manager                   │
└─────────────────────────────────────┘ └─────────────────────────────────────┘ └─────────────────────────────────────┘
    │                                               │                                               │
    └───────────────────────────────────────────────┼───────────────────────────────────────────────┘
                                                    │
┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                     GOVERNANCE & QUALITY LAYER                                       │
├─────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                    • Data Governance Specialist                                      │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    DETAILED AGENT BREAKDOWN                                          │
├─────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                      │
│  STRATEGY & ANALYSIS (6 Agents)          TECHNICAL DESIGN (8 Agents)                                │
│  ┌─────────────────────────────────┐     ┌─────────────────────────────────┐                        │
│  │ Business Strategist             │     │ Architect                       │                        │
│  │ • Porter's Five Forces          │     │ • DDD patterns, Bounded contexts│                        │
│  │ • Value Chain Analysis          │     │ • Aggregates, Domain events     │                        │
│  ├─────────────────────────────────┤     ├─────────────────────────────────┤                        │
│  │ Business Analyst                │     │ Developer                       │                        │
│  │ • Industry expertise, KPIs      │     │ • Schemas, Pydantic models      │                        │
│  │ • Benchmarks, Best practices    │     │ • Code artifacts, API specs     │                        │
│  ├─────────────────────────────────┤     ├─────────────────────────────────┤                        │
│  │ Data Analyst                    │     │ Tester                          │                        │
│  │ • Set-based KPIs, Cohort        │     │ • Validation, Test cases        │                        │
│  │ • TimescaleDB optimization      │     │ • Quality assurance             │                        │
│  ├─────────────────────────────────┤     ├─────────────────────────────────┤                        │
│  │ Data Scientist                  │     │ Documenter                      │                        │
│  │ • ML algorithms, Correlations   │     │ • Documentation, Data dictionary│                        │
│  │ • Predictive models             │     │ • User guides, API docs         │                        │
│  ├─────────────────────────────────┤     ├─────────────────────────────────┤                        │
│  │ Operations Manager              │     │ Deployment Specialist           │                        │
│  │ • KPI analysis, Bottlenecks     │     │ • Azure/K8s infrastructure      │                        │
│  │ • Optimization plans            │     │ • CI/CD, Helm charts            │                        │
│  ├─────────────────────────────────┤     ├─────────────────────────────────┤                        │
│  │ Mapping Specialist              │     │ UI Designer                     │                        │
│  │ • Source-to-target mapping      │     │ • Dashboard layouts, Styles     │                        │
│  │ • Transformations               │     │ • Components, Accessibility     │                        │
│  ├─────────────────────────────────┤     ├─────────────────────────────────┤                        │
│  │ Document Analyzer               │     │ ITIL Manager                    │                        │
│  │ • Document decomposition        │     │ • Incident/Problem/Change mgmt  │                        │
│  │ • Entity/KPI extraction         │     │ • SLAs, CMDB, CSI               │                        │
│  └─────────────────────────────────┘     ├─────────────────────────────────┤                        │
│                                          │ Connection Specialist           │                        │
│  BUSINESS OPERATIONS (8 Agents)          │ • API wrappers, Webhooks        │                        │
│  ┌─────────────────────────────────┐     │ • System integrations           │                        │
│  │ Sales Manager                   │     └─────────────────────────────────┘                        │
│  │ • CRM lifecycle, Pipeline       │                                                                │
│  │ • Prospect → Lead → Opportunity │                                                                │
│  ├─────────────────────────────────┤                                                                │
│  │ Marketing Manager               │                                                                │
│  │ • Campaigns, Lead scoring       │                                                                │
│  │ • Content calendars, Personas   │     GOVERNANCE (1 Agent)                                       │
│  ├─────────────────────────────────┤     ┌─────────────────────────────────┐                        │
│  │ Accountant                      │     │ Data Governance Specialist      │                        │
│  │ • Proposals, SOW, Invoicing     │     │ • DAMA DMBOK principles         │                        │
│  │ • AR/AP, Financial reports      │     │ • Data quality, Security        │                        │
│  ├─────────────────────────────────┤     │ • Policies, Stewardship         │                        │
│  │ Customer Success Manager        │     └─────────────────────────────────┘                        │
│  │ • Health scores, Churn risk     │                                                                │
│  │ • NPS, Onboarding, Expansion    │                                                                │
│  ├─────────────────────────────────┤                                                                │
│  │ HR/Talent Analyst               │                                                                │
│  │ • Retention, Engagement         │                                                                │
│  │ • Skills gaps, Compensation     │                                                                │
│  ├─────────────────────────────────┤                                                                │
│  │ Supply Chain Analyst            │                                                                │
│  │ • SCOR model, Inventory         │                                                                │
│  │ • Suppliers, Logistics          │                                                                │
│  ├─────────────────────────────────┤                                                                │
│  │ Risk & Compliance Officer       │                                                                │
│  │ • Risk assessment, Compliance   │                                                                │
│  │ • Audit support, Controls       │                                                                │
│  ├─────────────────────────────────┤                                                                │
│  │ Project Manager                 │                                                                │
│  │ • Agile planning, Sprints       │                                                                │
│  │ • Epics, User stories, Risks    │                                                                │
│  └─────────────────────────────────┘                                                                │
│                                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Agent Summary Table

| # | Agent | Model | Primary Responsibility |
|---|-------|-------|------------------------|
| 1 | Master Coordinator | Claude Opus 4.5 | Task routing, agent delegation, result synthesis |
| 2 | Business Strategist Agent | Claude Sonnet 4 | Porter's frameworks (Five Forces, Value Chain, Generic Strategy) |
| 3 | Architect Agent | Claude Sonnet 4 | DDD-based architecture (Millett/Tune book) |
| 4 | Business Analyst Agent | Claude Sonnet 4 | Industry expertise, KPIs, best practices |
| 5 | Data Analyst Agent | Claude Sonnet 4 | Set-based KPIs, cohort analysis, TimescaleDB |
| 6 | Developer Agent | Claude Sonnet 4 | Schemas, Pydantic models, code artifacts |
| 7 | Tester Agent | Claude Sonnet 4 | Validation, quality assurance |
| 8 | Documenter Agent | Claude Sonnet 4 | Documentation, guides, data dictionaries |
| 9 | Deployment Specialist Agent | Claude Sonnet 4 | Azure infrastructure, Kubernetes, CI/CD |
| 10 | Project Manager Agent | Claude Sonnet 4 | Agile planning, epics, sprints, stories |
| 11 | Sales Manager Agent | Claude Sonnet 4 | CRM lifecycle (prospect → lead → opportunity → client) |
| 12 | Accountant Agent | Claude Sonnet 4 | Proposals, SOW, AR/AP, accounting integration |
| 13 | Data Governance Specialist | Claude Sonnet 4 | DAMA DMBOK governance evaluation |
| 14 | Data Scientist Agent | Claude Sonnet 4 | KPI correlations, ML algorithm recommendations |
| 15 | Marketing Manager Agent | Claude Sonnet 4 | Marketing strategy, campaigns (coordinates with Sales) |
| 16 | UI Designer Agent | Claude Sonnet 4 | Analytics dashboard design, stylesheets, components |
| 17 | Operations Manager Agent | Claude Sonnet 4 | Holistic KPI analysis, correlation detection, optimization |
| 18 | Customer Success Manager Agent | Claude Sonnet 4 | Customer health, churn prevention, NPS, retention |
| 19 | HR/Talent Analyst Agent | Claude Sonnet 4 | People analytics, retention, engagement, skills gaps |
| 20 | Risk & Compliance Officer Agent | Claude Sonnet 4 | Risk assessment, compliance tracking, audit support |
| 21 | Supply Chain Analyst Agent | Claude Sonnet 4 | SCOR model, inventory, suppliers, logistics |
| 22 | ITIL Manager Agent | Claude Sonnet 4 | ITIL 4 framework, incident/problem/change management |
| 23 | Mapping Specialist Agent | Claude Sonnet 4 | Source-to-analytics attribute mapping, transformations |
| 24 | Connection Specialist Agent | Claude Sonnet 4 | System connections, API wrappers, webhooks, event-driven integration |
| 25 | Document Analyzer Agent | Claude Sonnet 4 | Document analysis, entity/process/KPI extraction, gap identification |
| 26 | Competitive Analyst Agent | Claude Sonnet 4 | Peer company identification, competitor profiling, market landscape analysis |
| 27 | Process Scenario Modeler Agent | Claude Sonnet 4 | Process simulation, what-if scenarios, bottleneck detection, KPI impact prediction |

## Agent Definitions

### 1. Master Coordinator (Claude Opus 4.5)

**Role**: Orchestration expert who manages the team of specialized AI agents. Routes tasks, delegates to appropriate agents, and synthesizes results into cohesive outputs. **Adapts communication style to match the interviewee's speaking characteristics.**

**Core Responsibilities**:
1. **Style Detection**: Analyze interviewee's communication style and adapt responses
2. **Task Analysis**: Understand client needs and break down into delegatable tasks
3. **Agent Selection**: Choose the right sub-agent(s) for each task
4. **Delegation**: Assign tasks with clear context and requirements
5. **Synthesis**: Combine results from multiple agents into cohesive outputs
6. **Workflow Management**: Coordinate parallel and sequential agent activities
7. **Response Formatting**: Format outputs to match detected communication style

**Adaptive Communication Style**:

The coordinator detects and adapts to the interviewee's communication style:

| Style | Indicators | Response Format | Formatting Agent |
|-------|------------|-----------------|------------------|
| **Executive** | vision, growth, ROI, stakeholders, strategic | Executive summary, key takeaways | Business Strategist |
| **Technical** | API, database, schema, architecture, microservices | Technical detail, specifications | Architect |
| **Analyst** | metrics, KPI, dashboard, trend, correlation | Balanced with data focus | Data Analyst |

**Dynamic Detail Level Adjustment**:

The interviewee can request more or less detail at any time. The system adjusts depth while **maintaining their core communication style**.

| Level | Name | Description |
|-------|------|-------------|
| 1 | Summary | Executive overview, key takeaways only |
| 2 | Moderate | Key details, main points with context |
| 3 | Detailed | Comprehensive coverage, supporting details |
| 4 | Comprehensive | Full technical depth, all specifications |

**Key Principle**: When a CEO asks to "dig deeper", the system increases detail level but maintains executive vocabulary and strategic framing. The core style is preserved; only the depth changes.

**Ontology Objects Used**:
- `CommunicationStyleProfile` - Session-level style profile with detected role, preferences, and detail level
- `StyleDetectionResult` - Per-utterance style detection results

**Interview Coordination**:
The interview is driven by **four core questions** presented by the system:

1. **Business & Strategy**: "Describe your business, your business model, and key strategic priorities."
2. **Pain Points**: "Describe what pain points in your business you are trying to address through analytics."
3. **Success Metrics**: "How will you measure success?"
4. **Decision Impact**: "If you had this information available to you, what decisions would you be able to make?"

**Delegation Guidelines**:
- Delegate to **Business Strategist** for Porter's framework analysis and strategic follow-up questions
- Delegate to **Architect** for value chain structures and DDD patterns
- Delegate to multiple agents in parallel for complex, multi-domain requests

**Model**: `claude-opus-4-20250514`

**Tools Available**:
- `delegate_to_business_strategist`: Porter's frameworks analysis
- `delegate_to_architect`: Value chain and DDD design
- `delegate_to_*`: Delegation to all 25 specialized sub-agents
- `synthesize_results`: Combine results from multiple agents
- `generate_probing_questions`: Get the 4 core interview questions
- `detect_communication_style`: Analyze utterance for communication style
- `get_style_profile`: Get current session style profile
- `format_response_for_style`: Format content for detected style
- `delegate_response_formatting`: Delegate formatting to appropriate agent
- `detect_detail_request`: Detect if interviewee wants more/less detail
- `adjust_detail_level`: Adjust detail level (increase/decrease/reset)
- `format_at_detail_level`: Format content at specific detail level while maintaining style

### 2. Business Strategist Agent (Claude Sonnet 4)

**Role**: Expert Business Strategist deeply versed in Michael Porter's strategic frameworks. Analyzes business contexts and provides strategic insights.

**Porter's Strategic Frameworks**:

**Five Forces Analysis**:
- Threat of New Entrants: Entry barriers, capital requirements
- Bargaining Power of Suppliers: Concentration, switching costs
- Bargaining Power of Buyers: Price sensitivity, alternatives
- Threat of Substitutes: Alternative solutions
- Industry Rivalry: Competition intensity

**Value Chain Mapping**:
- **Primary Activities**: Inbound Logistics → Operations → Outbound Logistics → Marketing & Sales → Service
- **Support Activities**: Infrastructure, HR, Technology, Procurement

**Generic Strategies**:
- Cost Leadership (broad market, low cost)
- Differentiation (broad market, unique value)
- Cost Focus (narrow market, cost advantage)
- Differentiation Focus (narrow market, unique value)

**Strategic Fit Assessment**:
- First-order fit: Simple consistency
- Second-order fit: Activities reinforce each other
- Third-order fit: Optimization of effort

**Ontology Objects Used**:
- `CompanyValueChainModel` - Company value chain structure
- `ValueChainNodeDefinition` - Value chain activity nodes
- `ValueChainLinkDefinition` - Links between activities
- `StrategicObjectiveDefinition` - Strategic objectives and goals
- `BenchmarkDefinition` - Industry benchmarks
- `ExternalEventDefinition` - External market events

**Tools Available**:
- `analyze_five_forces`: Conduct Five Forces industry analysis
- `map_value_chain`: Map Porter's Value Chain activities
- `determine_generic_strategy`: Identify competitive strategy
- `assess_strategic_fit`: Evaluate activity system fit
- `generate_strategic_questions`: Generate Porter-informed follow-up questions
- `synthesize_strategic_insights`: Synthesize insights from client responses
- `request_competitive_analysis`: **Trigger Competitive Analyst** to profile peer companies

**Competitive Analysis Trigger**:
Once the business model is elicited and strategic insights synthesized, the Business Strategist automatically triggers the Competitive Analyst to:
1. Search for peer companies with similar business models
2. Profile key competitors
3. Analyze the competitive landscape
4. Identify market gaps and differentiation opportunities

**Model**: `claude-sonnet-4-20250514`

### 3. Architect Agent (Claude Sonnet 4)

**Role**: Technical architecture specialist deeply versed in **Domain-Driven Design (DDD)** from "Patterns, Principles, and Practices of Domain-Driven Design" by Scott Millett and Nick Tune (ISBN: 978-1-118-71470-6).

**DDD Strategic Patterns**:
- **Bounded Contexts**: Linguistic boundaries with ubiquitous language
- **Context Mapping**: Upstream/downstream relationships (Partnership, Shared Kernel, Customer-Supplier, Conformist, ACL, OHS, Published Language)
- **Subdomains**: Core (competitive advantage), Supporting (necessary), Generic (commodity)

**DDD Tactical Patterns**:
- **Entities**: Objects with identity that persists over time
- **Value Objects**: Immutable, defined by attributes, no identity
- **Aggregates**: Consistency boundaries with aggregate roots
- **Domain Events**: Immutable facts (past tense naming)
- **Repositories**: One per aggregate root
- **Domain Services**: Stateless operations using ubiquitous language

**Capabilities**:
- Identifies bounded contexts and maps relationships
- Designs aggregates with proper consistency boundaries
- Models entities vs value objects
- Defines domain events for loose coupling
- Creates value chain structures aligned with subdomains
- Generates TimescaleDB schemas optimized for aggregate persistence

**Ontology Objects Used**:
- `BoundedContextDefinition` - DDD bounded context with ubiquitous language
- `AggregateDefinition` - Aggregate root with entities and value objects
- `DomainEventDefinition` - Domain events with payload and subscribers
- `EntityDefinition` - Business entities with attributes
- `TableSchemaDefinition` - Database schema definitions
- `ColumnDefinition` - Column definitions for entities

**Model**: `claude-sonnet-4-20250514`

**Tools Available**:
- `design_value_chain`: Create value chain structure
- `define_entity`: Define business entity with attributes
- `create_relationship`: Establish entity relationships
- `define_bounded_context`: Define DDD bounded context with ubiquitous language
- `design_aggregate`: Design aggregate with root, entities, value objects, invariants
- `define_domain_event`: Define domain event with payload and subscribers
- `create_context_map`: Map relationships between bounded contexts

### 4. Business Analyst Agent (Claude Sonnet 4)

**Role**: Industry-specific expertise and KPI identification.

**Capabilities**:
- Assumes deep expertise for any industry/value chain
- Identifies relevant KPIs and metrics
- Provides industry benchmarks and best practices
- Maps business processes to standard frameworks (SCOR, etc.)
- Recommends strategic improvements

**Ontology Objects Used**:
- `MetricDefinition` - KPI and metric definitions
- `MetricCategoryDefinition` - Metric categorization
- `BenchmarkDefinition` - Industry benchmarks
- `BusinessProcessDefinition` - Business process definitions
- `CompanyDefinition` - Company information

**Model**: `claude-sonnet-4-20250514`

**Tools Available**:
- `identify_kpis`: Identify relevant KPIs for a domain
- `get_industry_benchmarks`: Retrieve industry benchmarks
- `map_to_framework`: Map processes to standard frameworks
- `recommend_improvements`: Suggest strategic improvements

### 5. Data Analyst Agent (Claude Sonnet 4)

**Role**: Set-based KPI design for calculation engine optimization.

**Capabilities**:
- Designs set-based KPIs with multi-step calculation workflows
- Creates cohort analysis metrics (retention, churn, engagement)
- Defines INTERSECT, EXCEPT, UNION operations for complex metrics
- Optimizes KPIs for TimescaleDB continuous aggregates
- Specifies proper aggregation methods and time-series patterns

**Ontology Objects Used**:
- `MetricDefinition` - KPI and metric definitions
- `DimensionDefinition` - Analytical dimensions
- `DataSourceDefinition` - Data source configurations
- `DataQualityRuleDefinition` - Data quality rules

**Model**: `claude-sonnet-4-20250514`

**Tools Available**:
- `design_set_based_kpi`: Create KPIs with calculation steps for set-processing
- `design_simple_kpi`: Create simple aggregation-based KPIs
- `design_cohort_analysis`: Design cohort retention/churn metrics
- `optimize_kpi_for_timescale`: Generate continuous aggregate definitions

**Set-Based Calculation Pattern**:
```json
{
    "calculation_type": "set_based",
    "set_based_definition": {
        "base_entity": "customers",
        "key_column": "customer_id",
        "steps": [
            {"step_name": "start_set", "operation": "SELECT", "filter": "..."},
            {"step_name": "end_set", "operation": "SELECT", "filter": "..."},
            {"step_name": "retained", "operation": "INTERSECT", "left_set": "start_set", "right_set": "end_set"}
        ],
        "final_formula": "(COUNT(retained) / COUNT(start_set)) * 100"
    }
}
```

### 6. Developer Agent (Claude Sonnet 4)

**Role**: Code generation and technical implementation.

**Capabilities**:
- Generates TimescaleDB schemas
- Creates Pydantic model definitions
- Builds KPI calculation formulas
- Produces API endpoint specifications
- Creates data transformation logic

**Ontology Objects Used**:
- `TableSchemaDefinition` - Database schema definitions
- `ColumnDefinition` - Column definitions
- `EntityDefinition` - Entity definitions with attributes

**Model**: `claude-sonnet-4-20250514`

**Tools Available**:
- `generate_schema`: Generate TimescaleDB DDL
- `create_pydantic_model`: Generate Pydantic v2 models
- `build_kpi_formula`: Create calculation formulas
- `generate_api_spec`: Create OpenAPI specifications

### 7. Tester Agent (Claude Sonnet 4)

**Role**: Quality assurance and validation.

**Capabilities**:
- Validates schema integrity
- Tests KPI formula correctness
- Verifies relationship consistency
- Performs data quality checks
- Generates test cases

**Ontology Objects Used**:
- `TestSuiteDefinition` - Test suite configurations
- `TestCaseDefinition` - Individual test case definitions
- `DataQualityRuleDefinition` - Data quality validation rules

**Model**: `claude-sonnet-4-20250514`

**Tools Available**:
- `validate_schema`: Check schema integrity
- `test_formula`: Validate KPI calculations
- `verify_relationships`: Check relationship consistency
- `generate_test_cases`: Create test scenarios

### 8. Documenter Agent (Claude Sonnet 4)

**Role**: Documentation and knowledge management.

**Capabilities**:
- Generates comprehensive documentation
- Creates user guides and runbooks
- Produces API documentation
- Builds data dictionaries
- Creates training materials

**Ontology Objects Used**:
- `EntityDefinition` - Entity documentation
- `MetricDefinition` - KPI documentation
- `TableSchemaDefinition` - Schema documentation

**Model**: `claude-sonnet-4-20250514`

**Tools Available**:
- `generate_docs`: Create documentation
- `create_data_dictionary`: Build data dictionary
- `generate_api_docs`: Create API documentation
- `create_runbook`: Generate operational runbooks

### 9. Deployment Specialist Agent (Claude Sonnet 4)

**Role**: Azure infrastructure and deployment automation.

**Capabilities**:
- Generates Azure infrastructure templates (ARM/Bicep)
- Creates Kubernetes deployment manifests
- Configures Azure PostgreSQL with TimescaleDB
- Generates Helm charts for service deployment
- Creates CI/CD pipelines (GitHub Actions, Azure DevOps)
- Produces deployment checklists and runbooks

**Ontology Objects Used**:
- `EnvironmentDefinition` - Environment configurations (dev, staging, prod)
- `DeploymentConfigDefinition` - Deployment configuration specifications

**Model**: `claude-sonnet-4-20250514`

**Tools Available**:
- `generate_azure_infrastructure`: Create ARM/Bicep templates for AKS, PostgreSQL, Redis, Key Vault
- `generate_kubernetes_manifests`: Generate Deployments, Services, HPAs
- `generate_database_config`: Configure Azure PostgreSQL with TimescaleDB
- `generate_cicd_pipeline`: Create GitHub Actions or Azure DevOps pipelines
- `generate_helm_chart`: Generate Helm chart with values.yaml
- `generate_deployment_checklist`: Create deployment runbooks

**Azure Resource Naming Convention**:
```
{client_code}-{environment}-{resource_type}-{region}
Example: acme-prod-aks-eastus
```

**Generated Artifacts**:
- Bicep templates for Azure resources
- Kubernetes manifests (Deployments, Services, ConfigMaps, HPAs)
- Helm charts with environment-specific values
- CI/CD pipeline configurations
- Database initialization scripts
- Deployment checklists and rollback procedures

### 10. Project Manager Agent (Claude Sonnet 4)

**Role**: Agile Coach and Scrum Master for project planning and work breakdown.

**Capabilities**:
- Analyzes scope from design artifacts
- Creates epics representing major features
- Plans sprints with goals and capacity
- Generates user stories with acceptance criteria (Given-When-Then)
- Creates technical tasks for non-user-facing work
- Generates project roadmaps with milestones
- Identifies and documents project risks

**Agile Expertise**:
- Scrum, Kanban, SAFe methodologies
- User story writing standards
- Story point estimation (Fibonacci: 1, 2, 3, 5, 8, 13)
- Sprint planning and capacity management
- Dependency mapping and critical path analysis

**Ontology Objects Used**:
- `EpicDefinition` - Epic definitions with business value
- `SprintDefinition` - Sprint planning configurations
- `UserStoryDefinition` - User stories with acceptance criteria
- `TechnicalTaskDefinition` - Technical task definitions

**Model**: `claude-sonnet-4-20250514`

**Tools Available**:
- `create_epic`: Create epic with business value and acceptance criteria
- `plan_sprint`: Plan sprint with goal, capacity, and stories
- `create_user_story`: Create story with persona, want, so_that, acceptance criteria
- `create_technical_task`: Create technical task (infrastructure, refactoring, spike, etc.)
- `generate_project_roadmap`: Generate roadmap from epics with milestones
- `identify_risks`: Document risks with probability, impact, and mitigation

**Story Format**:
```
As a [persona/role]
I want [feature/capability]
So that [business value/outcome]
```

**Acceptance Criteria Format**:
```
Given [precondition]
When [action]
Then [expected result]
```

**Generated Artifacts**:
- Epics with business objectives
- Sprint plans with ceremonies
- User stories with acceptance criteria
- Technical tasks
- Project roadmaps with milestones
- Risk registers with mitigation strategies

### 11. Sales Manager Agent (Claude Sonnet 4)

**Role**: CRM lifecycle management expert who tracks client relationships through the complete sales lifecycle.

**CRM Lifecycle Stages**:
1. **Prospect**: Initial contact, company research, BANT qualification
2. **Lead**: Lead scoring, nurturing campaigns, discovery calls
3. **Opportunity**: Deal registration, pipeline stages, proposal coordination
4. **Client**: Contract signing, onboarding, relationship management

**Ontology Objects Used**:
- `ProspectDefinition` - Prospect records with qualification data
- `LeadDefinition` - Lead records with scoring
- `OpportunityDefinition` - Sales opportunities with pipeline stages
- `DealDefinition` - Deal records with value and probability
- `ClientDefinition` - Client records

**Tools**:
- `create_prospect`: Register new prospect with qualification data
- `qualify_lead`: Score and qualify leads using BANT criteria
- `create_opportunity`: Create opportunity with deal details
- `update_opportunity_stage`: Progress opportunity through pipeline
- `convert_to_client`: Convert won opportunity to active client
- `generate_pipeline_report`: Generate sales pipeline analytics

**Generated Artifacts**:
- Prospect records with engagement tracking
- Lead qualification assessments
- Opportunity pipeline data
- Client onboarding documentation
- Pipeline analytics reports

### 12. Accountant Agent (Claude Sonnet 4)

**Role**: Financial operations expert managing all aspects of client financial documentation.

**Financial Document Types**:
- **Proposals**: Executive summary, scope, pricing, payment terms
- **Statements of Work**: Objectives, deliverables, milestones, payment schedule
- **Invoicing**: Invoice generation, payment tracking, aging reports
- **Expenses**: AP tracking, vendor payments, project costs

**Ontology Objects Used**:
- `ProposalDefinition` - Client proposal documents
- `StatementOfWorkDefinition` - SOW documents with deliverables
- `InvoiceDefinition` - Invoice records
- `PaymentDefinition` - Payment records
- `ExpenseDefinition` - Expense/AP entries

**Tools**:
- `create_proposal`: Generate client proposal with pricing
- `create_sow`: Create Statement of Work document
- `create_invoice`: Generate invoice for client
- `record_payment`: Record payment received
- `create_expense`: Record expense/AP entry
- `generate_financial_report`: Generate AR/AP reports
- `sync_to_accounting`: Sync transactions to accounting platform (QuickBooks, Xero, etc.)

**Generated Artifacts**:
- Client proposals
- Statements of Work
- Invoices and payment records
- Expense tracking
- Financial reports (AR aging, AP aging, profitability)

### 13. Data Governance Specialist Agent (Claude Sonnet 4)

**Role**: Data governance expert who evaluates all design considerations using DAMA DMBOK principles.

**DAMA DMBOK 11 Knowledge Areas**:
1. Data Governance - Policies, standards, accountability
2. Data Architecture - Data structures, integration patterns
3. Data Modeling and Design - Conceptual, logical, physical models
4. Data Storage and Operations - Availability, performance, backup
5. Data Security - Access controls, encryption, compliance
6. Data Integration and Interoperability - ETL/ELT, data exchange
7. Document and Content Management - Unstructured data handling
8. Data Warehousing and Business Intelligence - Analytics support
9. Metadata Management - Lineage, definitions, discovery
10. Reference and Master Data Management - Golden records, hierarchies
11. Data Quality Management - Accuracy, completeness, timeliness

**Ontology Objects Used**:
- `DataQualityRuleDefinition` - Data quality rules and thresholds
- `GovernanceConstraintDefinition` - Governance constraints
- `PermissionDefinition` - Access control permissions
- `RowLevelSecurityDefinition` - Row-level security policies
- `ActorDefinition` - Data steward assignments

**Tools**:
- `assess_governance_maturity`: Evaluate maturity across knowledge areas
- `define_data_policy`: Create data governance policy
- `assign_data_steward`: Assign data stewardship responsibility
- `evaluate_design_compliance`: Check design against governance principles
- `create_data_dictionary`: Generate data dictionary entries
- `assess_data_quality_rules`: Define quality rules for entities
- `evaluate_security_classification`: Classify data sensitivity (PII, PHI, PCI)
- `generate_governance_report`: Generate governance assessment report

**Generated Artifacts**:
- Governance maturity assessments
- Data policies and standards
- Data stewardship assignments
- Compliance evaluations
- Data dictionary entries
- Quality rules and thresholds
- Security classifications

### 14. Data Scientist Agent (Claude Sonnet 4)

**Role**: Data science expert who analyzes KPIs for statistical correlations and recommends ML algorithms.

**Core Responsibilities**:
1. **KPI Correlation Analysis**: Identify relationships, calculate coefficients, find leading/lagging indicators
2. **Pattern Recognition**: Seasonality, trends, anomalies, regime changes
3. **ML Algorithm Recommendations**: Classification, regression, clustering, time series, anomaly detection
4. **Feature Engineering**: Lag features, rolling aggregates, interaction features
5. **Model Integration**: Define inputs/outputs, training requirements, deployment plans

**Ontology Objects Used**:
- `MLModelDefinition` - ML model specifications
- `CorrelationAnalysisDefinition` - KPI correlation analysis results
- `MetricDefinition` - KPI definitions for analysis

**Tools**:
- `analyze_kpi_correlations`: Find correlations between KPIs
- `identify_ml_opportunities`: Identify ML use cases from KPIs
- `recommend_algorithm`: Recommend ML algorithm for use case
- `design_feature_set`: Design features for ML model
- `create_ml_specification`: Create ML model specification
- `register_with_ml_service`: Register model with ML Service

**ML Problem Types**:
- Classification: Churn prediction, fraud detection, lead scoring
- Regression: Revenue forecasting, demand prediction
- Clustering: Customer segmentation, product grouping
- Time Series: Sales forecasting, inventory optimization
- Anomaly Detection: Fraud, system failures, quality issues

**Generated Artifacts**:
- KPI correlation matrices
- ML opportunity assessments
- Algorithm recommendations
- Feature engineering specifications
- ML model specifications
- ML Service registrations

### 15. Marketing Manager Agent (Claude Sonnet 4)

**Role**: Marketing strategy expert who designs and manages marketing plans in coordination with the Sales Manager.

**Core Responsibilities**:
1. **Marketing Strategy**: Target segments, positioning, go-to-market
2. **Campaign Management**: Multi-channel campaigns, budgets, timelines
3. **Lead Generation**: Lead scoring criteria (with Sales Manager), MQL tracking
4. **Content Strategy**: Content calendars, themes, publishing frequency
5. **Marketing Analytics**: ROI tracking, channel performance, CAC analysis

**Ontology Objects Used**:
- `MarketingPlanDefinition` - Marketing plan documents
- `BuyerPersonaDefinition` - Target buyer personas
- `CampaignDefinition` - Marketing campaign definitions
- `ContentCalendarDefinition` - Content publishing schedules

**Tools**:
- `create_marketing_plan`: Create comprehensive marketing plan
- `define_buyer_persona`: Define target buyer persona
- `create_campaign`: Design marketing campaign
- `create_content_calendar`: Plan content schedule
- `define_lead_scoring`: Define lead scoring criteria (coordinates with Sales)
- `track_campaign_performance`: Track campaign metrics
- `generate_marketing_report`: Generate marketing analytics report

**Marketing Channels**:
- Digital: SEO, SEM, Social Media, Email, Content Marketing
- Events: Webinars, Trade Shows, Conferences
- Partnerships: Co-marketing, Affiliate, Referral
- Traditional: PR, Print, Direct Mail

**Generated Artifacts**:
- Marketing plans with objectives and KPIs
- Buyer personas
- Campaign definitions
- Content calendars
- Lead scoring models
- Campaign performance reports

### 16. UI Designer Agent (Claude Sonnet 4)

**Role**: UI/UX design expert specializing in analytics dashboards and data visualization.

**Core Responsibilities**:
1. **Dashboard Layout Design**: Wireframes, responsive layouts, information hierarchy
2. **Style System Design**: Color palettes, typography, spacing, component styles
3. **Data Visualization Design**: Chart types, color schemes, readability
4. **Component Library**: Reusable UI components, KPI cards, filters
5. **Accessibility & UX**: WCAG 2.1 AA compliance, color blindness support

**Ontology Objects Used**:
- `DashboardLayoutDefinition` - Dashboard page layouts
- `StyleGuideDefinition` - Style guide specifications
- `UIComponentDefinition` - UI component definitions

**Tools**:
- `create_dashboard_layout`: Design dashboard page layout
- `create_style_guide`: Create comprehensive style guide
- `generate_stylesheet`: Generate CSS/SCSS stylesheet
- `design_component`: Design UI component
- `create_color_palette`: Create data visualization color palette
- `design_chart_style`: Define chart styling guidelines
- `generate_design_tokens`: Generate design tokens (CSS variables)

**Design Principles**:
- **Clarity**: Data immediately understandable
- **Consistency**: Uniform patterns across pages
- **Hierarchy**: Important metrics prominent
- **Responsiveness**: Works on all screen sizes
- **Accessibility**: Usable by everyone

**Generated Artifacts**:
- Dashboard layouts with sections
- Style guides (colors, typography, spacing)
- CSS/SCSS stylesheets
- UI component specifications
- Color palettes (categorical, sequential, diverging)
- Chart styling guidelines
- Design tokens

### 17. Operations Manager Agent (Claude Sonnet 4)

**Role**: Operations expert who analyzes KPI results holistically, identifies correlating patterns, and makes optimization recommendations. Collaborates closely with the Data Scientist Agent for statistical validation and ML model design.

**Core Responsibilities**:
1. **Holistic KPI Analysis**: View all KPIs together in context
2. **Correlation Detection**: Find relationships between KPIs
3. **Bottleneck Identification**: Locate performance constraints
4. **Optimization Recommendations**: Prioritize improvement opportunities
5. **Operational Health Assessment**: Overall performance scoring
6. **Data Scientist Collaboration**: Statistical validation and ML model design

**Ontology Objects Used**:
- `OptimizationPlanDefinition` - Optimization plans with quick wins and strategic initiatives
- `OperationalHealthDefinition` - Operational health scorecards with SWOT
- `CorrelationAnalysisDefinition` - KPI correlation analysis results
- `MetricDefinition` - KPI definitions for analysis

**Data Scientist Collaboration Workflow**:
```
┌─────────────────────────┐     ┌─────────────────────────┐
│   Operations Manager    │     │    Data Scientist       │
│                         │     │                         │
│ 1. Identify patterns    │────▶│ 2. Validate statistically│
│                         │     │    (p-values, R², etc.) │
│ 3. Interpret results    │◀────│                         │
│                         │     │ 4. Design ML models     │
│ 5. Business recommend.  │◀────│    (algorithms, specs)  │
└─────────────────────────┘     └─────────────────────────┘
```

**When to Engage Data Scientist**:
- Validate suspected correlations with statistical significance testing
- Design predictive models for KPI forecasting
- Analyze time-series patterns and seasonality
- Identify causal relationships vs mere correlations
- Build anomaly detection models for operational alerts

**Analysis Frameworks**:

**KPI Correlation Analysis**:
- Positive/Negative correlations between metrics
- Leading vs Lagging indicators
- Cause-and-effect chains
- KPI influence networks

**Statistical Validation (via Data Scientist)**:
- Pearson/Spearman correlation coefficients
- Granger causality testing
- Time-lagged cross-correlation
- Regression analysis for impact quantification

**Performance Optimization**:
- Theory of Constraints (bottleneck analysis)
- Pareto Analysis (80/20 rule)
- Root Cause Analysis
- Continuous Improvement

**Operational Metrics Categories**:
- **Efficiency**: Resource utilization, cycle time
- **Quality**: Defect rates, accuracy, compliance
- **Speed**: Throughput, response time, lead time
- **Cost**: Unit costs, overhead, waste
- **Customer**: Satisfaction, retention, NPS

**Tools Available**:
- `analyze_kpi_performance`: Holistic KPI analysis
- `detect_kpi_correlations`: Find correlating patterns
- `identify_bottlenecks`: Locate performance constraints
- `generate_optimization_plan`: Create prioritized recommendations
- `assess_operational_health`: Overall health assessment (SWOT)
- `create_performance_dashboard`: Design KPI dashboard layout
- `forecast_impact`: Predict impact of proposed changes
- `request_statistical_validation`: Request Data Scientist to validate correlations
- `request_ml_model_design`: Collaborate with Data Scientist on predictive models

**Generated Artifacts**:
- KPI performance analyses
- Correlation matrices and influence chains
- Bottleneck assessments
- Optimization plans with quick wins and strategic initiatives
- Operational health scorecards
- Performance dashboards
- Impact forecasts
- Statistical validation requests (for Data Scientist)
- ML model design requests (for Data Scientist)

### 18. Customer Success Manager Agent (Claude Sonnet 4)

**Role**: Customer success expert focused on post-sale customer lifecycle, retention, and expansion.

**Core Responsibilities**:
1. **Customer Health Monitoring**: Track health scores across usage, engagement, support, payment
2. **Churn Prevention**: Identify at-risk customers and recommend interventions
3. **NPS Management**: Track Net Promoter Score and customer feedback
4. **Onboarding**: Design and track customer onboarding journeys
5. **Expansion**: Identify upsell and cross-sell opportunities

**Ontology Objects Used**:
- `CustomerHealthScoreDefinition` - Customer health assessments with component scores
- `ChurnRiskAssessmentDefinition` - Churn risk predictions with mitigation actions
- `NPSSurveyDefinition` - NPS survey responses and feedback
- `ClientDefinition` - Client records

**Tools**:
- `calculate_health_score`: Calculate customer health score
- `assess_churn_risk`: Assess churn risk with predictions
- `track_nps_survey`: Record NPS survey response
- `design_onboarding_journey`: Create onboarding journey
- `identify_expansion_opportunity`: Find upsell/cross-sell opportunities
- `generate_customer_success_report`: Generate CS analytics report

**Generated Artifacts**:
- Customer health scorecards
- Churn risk assessments
- NPS tracking reports
- Onboarding journey maps
- Expansion opportunity analyses

### 19. HR/Talent Analyst Agent (Claude Sonnet 4)

**Role**: People analytics expert focused on workforce optimization, retention, and talent development.

**Core Responsibilities**:
1. **Turnover Analysis**: Analyze voluntary/involuntary turnover patterns
2. **Flight Risk Assessment**: Predict employee attrition risk
3. **Engagement Measurement**: Track employee engagement and eNPS
4. **Skills Gap Analysis**: Identify skills gaps and training needs
5. **Compensation Benchmarking**: Analyze compensation competitiveness

**Ontology Objects Used**:
- `EmployeeDefinition` - Employee records with tenure and status
- `EngagementSurveyDefinition` - Employee engagement survey results
- `SkillsGapAnalysisDefinition` - Skills gap analysis with recommendations

**Tools**:
- `analyze_turnover`: Analyze turnover patterns by department/role
- `assess_flight_risk`: Predict employee attrition risk
- `measure_engagement`: Analyze engagement survey results
- `conduct_skills_gap_analysis`: Identify skills gaps
- `benchmark_compensation`: Compare compensation to market
- `generate_hr_analytics_report`: Generate HR analytics report

**Generated Artifacts**:
- Turnover analysis reports
- Flight risk assessments
- Engagement scorecards
- Skills gap analyses
- Compensation benchmarks

### 20. Risk & Compliance Officer Agent (Claude Sonnet 4)

**Role**: Enterprise risk and compliance expert managing risk assessment, compliance tracking, and audit support.

**Core Responsibilities**:
1. **Risk Assessment**: Identify and score enterprise risks
2. **Compliance Tracking**: Track regulatory compliance requirements
3. **Control Evaluation**: Evaluate internal control effectiveness
4. **Audit Support**: Prepare for and support audits
5. **Incident Management**: Log and track compliance incidents

**Ontology Objects Used**:
- `RiskAssessmentDefinition` - Enterprise risk assessments with scoring
- `ComplianceRequirementDefinition` - Compliance requirement tracking
- `ControlEvaluationDefinition` - Internal control evaluations

**Tools**:
- `assess_risk`: Assess and score enterprise risk
- `track_compliance_requirement`: Track compliance status
- `evaluate_control`: Evaluate control effectiveness
- `log_incident`: Log compliance incident
- `prepare_audit`: Prepare audit documentation
- `generate_risk_report`: Generate risk and compliance report

**Generated Artifacts**:
- Risk registers with scoring
- Compliance status reports
- Control evaluation reports
- Incident logs
- Audit preparation packages

### 21. Supply Chain Analyst Agent (Claude Sonnet 4)

**Role**: Supply chain expert using SCOR model for supply chain optimization.

**Core Responsibilities**:
1. **SCOR Metrics**: Track Plan, Source, Make, Deliver, Return metrics
2. **Inventory Optimization**: ABC/XYZ analysis, safety stock, reorder points
3. **Supplier Management**: Evaluate supplier performance and risk
4. **Demand Planning**: Forecast demand and optimize inventory
5. **Logistics Optimization**: Optimize transportation and warehousing

**Ontology Objects Used**:
- `SupplierDefinition` - Supplier records with performance metrics
- `InventoryItemDefinition` - Inventory items with ABC/XYZ classification
- `SCORMetricDefinition` - SCOR framework metrics

**Tools**:
- `analyze_inventory_levels`: Analyze inventory with ABC/XYZ
- `evaluate_supplier_performance`: Evaluate supplier metrics
- `calculate_scor_metrics`: Calculate SCOR framework metrics
- `forecast_demand`: Generate demand forecasts
- `optimize_safety_stock`: Calculate optimal safety stock
- `generate_supply_chain_report`: Generate supply chain analytics

**Generated Artifacts**:
- Inventory analysis reports
- Supplier scorecards
- SCOR metric dashboards
- Demand forecasts
- Safety stock recommendations

### 22. ITIL Manager Agent (Claude Sonnet 4)

**Role**: IT Service Management expert based on ITIL 4 framework.

**Core Responsibilities**:
1. **Incident Management**: Log, categorize, and track IT incidents
2. **Problem Management**: Root cause analysis and known error database
3. **Change Management**: RFC processing, CAB reviews, change calendar
4. **Service Level Management**: Define and track SLAs
5. **Configuration Management**: Maintain CMDB
6. **Continual Service Improvement**: CSI initiatives

**Ontology Objects Used**:
- `ITILIncidentDefinition` - ITIL incident records
- `ITILProblemDefinition` - Problem records with root cause
- `ChangeRequestDefinition` - Change requests (RFCs)
- `ServiceLevelAgreementDefinition` - SLA definitions
- `ConfigurationItemDefinition` - CMDB configuration items

**Tools**:
- `log_incident`: Log IT incident with priority matrix
- `create_problem_record`: Create problem for root cause analysis
- `submit_change_request`: Submit RFC with risk assessment
- `define_service_level`: Define SLA targets
- `track_configuration_item`: Track CI in CMDB
- `plan_continual_improvement`: Create CSI initiative
- `generate_itil_report`: Generate ITIL service management report

**Generated Artifacts**:
- Incident records
- Problem records with root cause
- Change requests with approval workflow
- SLA definitions
- CMDB entries
- CSI initiative plans

### 23. Mapping Specialist Agent (Claude Sonnet 4)

**Role**: Data mapping expert focused on accelerating source-to-analytics attribute mapping.

**Core Responsibilities**:
1. **Source Analysis**: Analyze source system schemas and data dictionaries
2. **Mapping Recommendations**: Suggest mappings based on semantic similarity
3. **Transformation Design**: Design data type conversions and transformations
4. **Validation**: Validate mapping compatibility and data quality
5. **Derived Fields**: Suggest calculated/derived field formulas

**Ontology Objects Used**:
- `SourceSchemaDefinition` - Source system schema definitions
- `MappingRuleDefinition` - Attribute mapping rules
- `TransformationDefinition` - Data transformation specifications

**Tools**:
- `analyze_source_schema`: Analyze source system schema
- `recommend_mappings`: Generate mapping recommendations
- `create_mapping_rule`: Create specific mapping rule
- `validate_mapping`: Validate mapping compatibility
- `design_transformation`: Design data transformation
- `suggest_derived_field`: Suggest derived field formula
- `generate_mapping_report`: Generate mapping status report

**Generated Artifacts**:
- Source schema analyses
- Mapping recommendations with confidence scores
- Mapping rules
- Transformation specifications
- Mapping status reports

### 24. Connection Specialist Agent (Claude Sonnet 4)

**Role**: Integration expert focused on designing and automating connections to client systems.

**Core Responsibilities**:
1. **Connection Design**: Design optimal connection architecture
2. **API Wrapper Development**: Generate API client code
3. **Connector Configuration**: Configure pre-built connectors
4. **Webhook Setup**: Set up webhook receivers and event handlers
5. **Event-Driven Integration**: Implement real-time data flows

**System Expertise**:
- **CRM**: Salesforce, HubSpot, Dynamics 365
- **ERP**: SAP, NetSuite, Dynamics 365 BC
- **Accounting**: QuickBooks, Xero, Sage Intacct
- **E-commerce**: Shopify, WooCommerce, Magento

**Ontology Objects Used**:
- `ConnectionDefinition` - System connection configurations
- `APIWrapperDefinition` - API wrapper specifications
- `WebhookReceiverDefinition` - Webhook receiver configurations
- `EventHandlerDefinition` - Event handler definitions

**Tools**:
- `analyze_target_system`: Analyze system integration options
- `design_connection`: Design connection architecture
- `generate_api_wrapper`: Generate API client code
- `configure_connector`: Configure connector instance
- `setup_webhook_receiver`: Set up webhook endpoint
- `create_event_handler`: Create event handler
- `test_connection`: Test connection configuration
- `generate_connection_report`: Generate connection status report

**Generated Artifacts**:
- System integration analyses
- Connection designs
- API wrapper code
- Connector configurations
- Webhook receivers
- Event handlers
- Connection test results

### 25. Document Analyzer Agent (Claude Sonnet 4)

**Role**: Document analysis expert who extracts structured business intelligence from documentation provided by interviewees.

**Core Responsibilities**:
1. **Document Classification**: Identify document type and purpose
2. **Entity Extraction**: Extract business entities, data entities, actors
3. **Process Extraction**: Extract workflows, procedures, business processes
4. **KPI Extraction**: Extract metrics and success measures
5. **Relationship Mapping**: Map connections between entities
6. **Terminology Extraction**: Build ubiquitous language from domain terms
7. **Gap Analysis**: Identify missing information for model design

**Document Types Analyzed**:
- **Business Documents**: Business plans, annual reports, org charts, policies
- **Technical Documents**: Architecture diagrams, API docs, database schemas, ERDs
- **Data Documents**: Data dictionaries, report specs, dashboard mockups, KPI definitions
- **Operational Documents**: Process flows, SOPs, workflow documentation, requirements

**Ontology Objects Used**:
- `AnalyzedDocumentDefinition` - Analyzed document records with extraction summary
- `ExtractedEntityDefinition` - Entities extracted from documents
- `ExtractedProcessDefinition` - Processes extracted from documents
- `ExtractedTermDefinition` - Domain terms for ubiquitous language
- `DocumentGapAnalysisDefinition` - Gap analysis with clarification questions

**Tools**:
- `analyze_document`: Analyze document to extract structured intelligence
- `extract_entities`: Extract business entities from document
- `extract_processes`: Extract workflows and procedures
- `extract_kpis`: Extract KPIs and metrics
- `extract_relationships`: Extract entity relationships
- `extract_terminology`: Extract domain terms for ubiquitous language
- `extract_data_sources`: Extract data source information
- `identify_gaps`: Identify information gaps needing clarification
- `generate_document_summary`: Generate comprehensive analysis summary
- `request_architect_review`: Request Architect to review extracted entities
- `request_business_analyst_review`: Request Business Analyst to review extracted KPIs

**Integration with Model Design**:
Extracted findings are automatically routed to:
- **Architect Agent**: For bounded context and entity design
- **Business Analyst Agent**: For KPI validation and industry benchmarking
- **Data Analyst Agent**: For metric design and calculation optimization
- **Mapping Specialist Agent**: For source-to-target attribute mapping

**Generated Artifacts**:
- Analyzed document records
- Extracted entities with attributes and confidence scores
- Extracted processes with steps and actors
- Domain terminology glossary
- Gap analyses with clarification questions
- Document analysis summaries with recommendations

### 26. Competitive Analyst Agent (Claude Sonnet 4)

**Role**: Competitive intelligence expert who identifies and profiles peer companies using web search to provide market landscape insights.

**Core Responsibilities**:
1. **Peer Company Identification**: Search for companies with similar business models
2. **Competitor Profiling**: Build detailed profiles of key competitors
3. **Market Positioning Analysis**: Analyze how competitors position themselves
4. **Competitive Benchmarking**: Compare capabilities, offerings, and strategies
5. **Industry Landscape Mapping**: Map the competitive ecosystem using Porter's Five Forces

**Profiling Framework**:
For each competitor, capture:
- **Identity**: Name, website, founding year, headquarters, employee count, funding
- **Business Model**: Revenue model, pricing strategy, go-to-market, target market
- **Offerings**: Products, services, key features, pricing tiers
- **Competitive Position**: Strengths, weaknesses, market position, advantages
- **Strategy**: Growth strategy, recent moves, partnerships, news

**Ontology Objects Used**:
- `CompetitorProfileDefinition` - Detailed competitor company profiles
- `CompetitiveLandscapeDefinition` - Industry landscape with Five Forces analysis
- `MarketGapAnalysisDefinition` - Market gaps and differentiation opportunities

**Tools**:
- `search_peer_companies`: Web search for peer companies with similar business models
- `profile_competitor`: Build detailed profile of a specific competitor
- `analyze_competitive_landscape`: Analyze industry landscape (Five Forces, market map)
- `compare_competitors`: Compare multiple competitors across dimensions
- `identify_market_gaps`: Identify gaps and opportunities in the market
- `track_competitor_news`: Search for recent news about competitors
- `generate_competitive_report`: Generate competitive intelligence report
- `request_strategist_review`: Request Business Strategist to review findings

**Integration with Other Agents**:
Findings inform:
- **Business Strategist**: Competitive positioning and differentiation strategy
- **Marketing Manager**: Competitive messaging and positioning
- **Sales Manager**: Competitive selling points and objection handling
- **Data Analyst**: Competitive benchmarks for KPIs

**Generated Artifacts**:
- Peer company search results
- Competitor profiles with confidence scores
- Competitive landscape analyses
- Competitor comparison matrices
- Market gap analyses
- Competitive intelligence reports
- Sales battlecards

### 27. Process Scenario Modeler Agent (Claude Sonnet 4)

**Role**: Process simulation specialist who helps organizations test process changes in a digital sandbox before implementing them in production. Bridges strategy design with operational execution by predicting how process changes will impact KPIs.

**Core Responsibilities**:
1. **Process Design**: Define process flows from value chain modules with step parameters
2. **Scenario Creation**: Create what-if scenarios with parameter changes
3. **Simulation Execution**: Run discrete event simulations with multiple replications
4. **Impact Analysis**: Predict KPI impacts from process changes
5. **Bottleneck Detection**: Identify process constraints and capacity issues
6. **Optimization Recommendations**: Generate process improvement recommendations

**Simulation Capabilities**:
- **Discrete Event Simulation**: Model process flows with statistical distributions
- **Resource Modeling**: Track resource utilization and capacity constraints
- **Cost Analysis**: Calculate process costs (fixed and variable)
- **Quality Metrics**: Track defect rates and rework
- **Scenario Comparison**: Compare multiple scenarios side-by-side

**Ontology Objects Used**:
- `SimulatableProcessDefinition` - Process definitions with steps and transitions
- `ScenarioDefinition` - What-if scenarios with parameter changes
- `SimulationResultDefinition` - Simulation results with metrics
- `ImpactAnalysisDefinition` - KPI impact analysis results

**Tools**:
- `design_process`: Create process definition from value chain module
- `create_scenario`: Define what-if scenario with parameter changes
- `run_simulation`: Execute process simulation
- `analyze_impact`: Analyze KPI impacts from simulation
- `compare_scenarios`: Compare multiple scenarios side-by-side
- `identify_bottlenecks`: Find process bottlenecks
- `recommend_optimizations`: Generate optimization recommendations
- `request_operations_review`: Request Operations Manager to review results

**Collaboration with Other Agents**:
- **Operations Manager**: Provides operational context and validates findings
- **Data Scientist**: Validates predictions statistically
- **Business Strategist**: Ensures strategic alignment of changes

**Generated Artifacts**:
- Process definitions with BPMN-style flows
- Simulation scenarios with parameter overrides
- Simulation results with performance metrics
- Bottleneck analyses with recommendations
- Scenario comparison reports
- KPI impact predictions with confidence intervals

## Cross-Agent Collaboration Framework

The multi-agent system implements a comprehensive collaboration framework that enables agents to work together seamlessly without overwhelming the interviewee.

### Collaboration Patterns

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        CROSS-AGENT COLLABORATION MAP                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐                   │
│  │  Business   │◄───►│  Architect  │◄───►│  Developer  │                   │
│  │  Strategist │     │             │     │             │                   │
│  └─────────────┘     └──────┬──────┘     └──────┬──────┘                   │
│                             │                   │                           │
│                             ▼                   ▼                           │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐                   │
│  │  Business   │◄───►│    Data     │◄───►│   Tester    │                   │
│  │   Analyst   │     │  Governance │     │             │                   │
│  └──────┬──────┘     └─────────────┘     └──────┬──────┘                   │
│         │                                       │                           │
│         ▼                                       ▼                           │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐                   │
│  │    Data     │◄───►│    Data     │◄───►│  Documenter │                   │
│  │   Analyst   │     │  Scientist  │     │             │                   │
│  └─────────────┘     └──────┬──────┘     └─────────────┘                   │
│                             │                                               │
│                             ▼                                               │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐                   │
│  │  Marketing  │◄───►│  Operations │◄───►│   Project   │                   │
│  │   Manager   │     │   Manager   │     │   Manager   │                   │
│  └──────┬──────┘     └─────────────┘     └──────┬──────┘                   │
│         │                                       │                           │
│         ▼                                       ▼                           │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐                   │
│  │    Sales    │◄───►│  Accountant │◄───►│ Deployment  │                   │
│  │   Manager   │     │             │     │  Specialist │                   │
│  └─────────────┘     └─────────────┘     └─────────────┘                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Collaboration Tool Categories

#### 1. Request Tools (Outbound)
Agents use these to request work from other agents:
- `request_entity_validation` - Architect → Business Analyst
- `request_kpi_requirements` - Architect → Business Analyst
- `request_governance_review` - Architect → Data Governance
- `request_schema_generation` - Architect → Developer
- `request_kpi_calculation_design` - Business Analyst → Data Analyst
- `request_predictive_analysis` - Business Analyst → Data Scientist
- `request_test_specification` - Developer → Tester
- `request_documentation` - Developer → Documenter
- `request_deployment_config` - Developer → Deployment Specialist
- `request_statistical_validation` - Operations Manager → Data Scientist
- `request_ml_model_design` - Operations Manager → Data Scientist
- `request_mql_from_marketing` - Sales Manager → Marketing Manager
- `request_deal_pricing` - Sales Manager → Accountant
- `request_campaign_analytics` - Marketing Manager → Data Scientist
- `request_design_assets` - Marketing Manager → UI Designer

#### 2. Response/Handoff Tools (Return)
Agents use these to return results or hand off work:
- `share_entity_validation` - Business Analyst → Architect
- `share_schema_artifacts` - Developer → Architect
- `report_test_results` - Tester → Developer
- `handoff_mql_to_sales` - Marketing Manager → Sales Manager
- `handoff_to_project_manager` - Sales Manager → Project Manager

### Collaboration Workflow

1. **Request Phase**: Agent A identifies need for Agent B's expertise
2. **Queue Phase**: Request stored in `context.artifacts["collaboration_requests"]`
3. **Processing Phase**: Coordinator routes request to Agent B
4. **Response Phase**: Agent B stores result in `context.artifacts["collaboration_responses"]`
5. **Integration Phase**: Agent A incorporates response into work

### Benefits

- **Reduced Interview Burden**: Agents collaborate behind the scenes
- **Specialized Expertise**: Each agent contributes domain knowledge
- **Data-Driven Decisions**: Statistical validation before recommendations
- **Consistent Quality**: Cross-validation between agents
- **Audit Trail**: All collaboration tracked in context artifacts

## Integration with Conversation Service

### Current Architecture

The Conversation Service currently uses:
- OpenAI/Azure OpenAI for LLM operations
- WebSocket for real-time chat
- Session management for context
- Intent extraction and response generation

### Enhanced Architecture with Multi-Agent

```python
# New flow with multi-agent coordination
Client Message → Conversation Service
                      │
                      ▼
              Strategy Coordinator
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
   Architect    Business Analyst  Developer
        │             │             │
        └─────────────┼─────────────┘
                      │
                      ▼
              Synthesized Response
                      │
                      ▼
              Client Response + Probing Questions
```

### Key Integration Points

1. **Session Context Sharing**: All agents share session context via Redis
2. **Parallel Execution**: Sub-agents run in parallel for efficiency
3. **Result Aggregation**: Coordinator synthesizes sub-agent outputs
4. **Probing Questions**: Coordinator generates follow-up questions
5. **Artifact Generation**: Developer agent creates executable artifacts

## Implementation Approach

### Phase 1: Agent Framework
- Create base `Agent` class with Claude SDK integration
- Implement `AgentOrchestrator` for coordination
- Define agent-specific tools as MCP servers

### Phase 2: Specialized Agents
- Implement each agent with specialized prompts
- Create tool definitions for each agent
- Build result aggregation logic

### Phase 3: Conversation Integration
- Integrate with existing Conversation Service
- Add multi-agent session management
- Implement parallel execution

### Phase 4: Testing & Validation
- Create integration tests
- Validate agent collaboration
- Performance optimization

## Configuration

```yaml
multi_agent:
  coordinator:
    model: "claude-opus-4-20250514"
    max_tokens: 8192
    temperature: 0.7
  
  sub_agents:
    architect:
      model: "claude-sonnet-4-20250514"
      max_tokens: 4096
      temperature: 0.3
    
    business_analyst:
      model: "claude-sonnet-4-20250514"
      max_tokens: 4096
      temperature: 0.5
    
    developer:
      model: "claude-sonnet-4-20250514"
      max_tokens: 4096
      temperature: 0.2
    
    tester:
      model: "claude-sonnet-4-20250514"
      max_tokens: 4096
      temperature: 0.2
    
    documenter:
      model: "claude-sonnet-4-20250514"
      max_tokens: 4096
      temperature: 0.4

  execution:
    parallel_agents: true
    max_parallel: 3
    timeout_seconds: 120
    retry_attempts: 2
```

## API Endpoints

### New Endpoints for Multi-Agent

```
POST /api/v1/agents/design-session
  - Start a new multi-agent design session
  - Returns session_id and initial coordinator response

POST /api/v1/agents/sessions/{session_id}/message
  - Send message to active design session
  - Triggers coordinator and sub-agent processing

GET /api/v1/agents/sessions/{session_id}/artifacts
  - Retrieve generated artifacts from session
  - Returns schemas, models, KPIs, documentation

POST /api/v1/agents/sessions/{session_id}/finalize
  - Finalize design and persist to Business Metadata Service
  - Triggers artifact generation and storage

WebSocket /ws/agents/{session_id}
  - Real-time streaming of agent responses
  - Progress updates during parallel processing
```

## Event Flow

```
1. Client sends business description
2. Coordinator analyzes using Porter's frameworks
3. Coordinator asks pertinent follow-up questions (one at a time)
4. Client responds to questions
5. Repeat steps 2-4 until sufficient context gathered
6. Coordinator spawns sub-agents in parallel:
   - Architect: Design bounded contexts, aggregates, value chain structure
   - Business Analyst: Identify KPIs and best practices
   - Data Analyst: Design set-based KPIs and calculation optimizations
   - Developer: Generate schemas and Pydantic models
7. Sub-agents return results to Coordinator
8. Coordinator synthesizes results
9. Tester validates all artifacts
10. Documenter generates documentation
11. Project Manager creates epics, sprints, and user stories
12. Deployment Specialist generates infrastructure artifacts
13. Finalization persists all artifacts to services:
    - Entities → Business Metadata Service
    - KPIs → Calculation Engine Service
    - Schemas → Database Service (TimescaleDB)
    - Relationships → metadata_relationships API
    - Events → Redis pub/sub
```

## Service Integration

The multi-agent system integrates with Analytics Engine services:

| Artifact Type | Target Service | API Endpoint |
|---------------|----------------|--------------|
| Entities | Business Metadata Service | `POST /api/v1/metadata/entities` |
| Metrics/KPIs | Business Metadata Service | `POST /api/v1/metadata/metrics` |
| Value Chains | Business Metadata Service | `POST /api/v1/metadata/value-chains` |
| Relationships | Business Metadata Service | `POST /api/v1/metadata/relationships` |
| KPI Registration | Calculation Engine Service | `POST /api/v1/kpis/register` |
| Schema Migration | Database Service | `POST /api/v1/migrations/execute` |
| Events | Messaging Service | `POST /api/v1/events/publish` |

### Relationship Types (metadata_relationships)

Per system architecture, relationships are stored ONLY in the `metadata_relationships` table:

- `belongs_to_value_chain` - Module/KPI belongs to a Value Chain
- `belongs_to_module` - KPI belongs to a Module
- `uses` - KPI uses Object Model

## Benefits

1. **Parallel Processing**: Sub-agents work simultaneously for faster results
2. **Specialized Expertise**: Each agent focuses on its domain
3. **Context Isolation**: Sub-agents have isolated context windows
4. **Comprehensive Output**: Multiple perspectives synthesized
5. **Industry Agnostic**: Business Analyst adapts to any industry
6. **Quality Assurance**: Built-in testing and validation
7. **Documentation**: Automatic documentation generation
8. **Agile Planning**: Project Manager creates actionable work items
9. **Infrastructure Ready**: Deployment Specialist generates Azure/K8s artifacts
10. **Full Service Integration**: Artifacts automatically persisted to platform services

## Dependencies

- `claude-agent-sdk>=1.0.0`: Anthropic's Agent SDK
- `anthropic>=0.40.0`: Anthropic Python client
- `anyio>=4.0.0`: Async I/O support
- `redis>=5.0.0`: Session state management
- `httpx>=0.27.0`: HTTP client for service communication
