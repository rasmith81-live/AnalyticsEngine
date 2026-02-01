# Multi-Agent Service Architecture

This document provides comprehensive documentation for the Analytics Engine multi-agent system, including service architecture, agent definitions, behavioral contracts, and the blackboard coordination pattern.

## Table of Contents

1. [Overview](#overview)
2. [Service Architecture](#service-architecture)
3. [Agent Inventory](#agent-inventory)
4. [Behavioral Contracts](#behavioral-contracts)
5. [Blackboard Architecture](#blackboard-architecture)
6. [Peer Review System](#peer-review-system)
7. [Protocols](#protocols)
8. [Prompt Library](#prompt-library)
9. [Domain Skills](#domain-skills)
10. [MCP Integration](#mcp-integration)
11. [Adaptive Communication](#adaptive-communication)
12. [Admin Management](#admin-management)
13. [API Reference](#api-reference)
14. [Configuration](#configuration)

---

## Overview

The multi-agent system is a collaborative AI architecture for business value chain design, leveraging Anthropic's Claude models to create specialized agents that work together through a blackboard coordination pattern with behavioral contracts.

### Key Characteristics

- **27 Specialized Agents**: Domain experts across strategy, technical, and business operations
- **Contract-Enforced Behavior**: State machines with forbidden transitions and tiered rules
- **Blackboard Coordination**: Shared state model replacing pub/sub for auditability
- **Adversarial Peer Review**: Creator ≠ Reviewer separation for quality assurance
- **Struggle Protocol**: Transforms deception risk into collaboration opportunity

### Attribution

This architecture is based on **Tangi Vass's** research on behavioral contracts for AI coding agents:
- [Turning AI Coding Agents into Senior Engineering Peers](https://medium.com/@tangi.vass/turning-ai-coding-agents-into-senior-engineering-peers-c3d178621c9e)
- [LIZA: Peer-Supervised Multi-Agent System](https://github.com/liza-mas/liza)

---

## Service Architecture

### Service Location

```
services/backend_services/multi_agent_service/
```

### Service Responsibilities

| Service | Responsibility |
|---------|----------------|
| **multi_agent_service** | Agent contracts, blackboard, peer review, skills, dashboard |
| **conversation_service** | Session management, client interview flow, consumes multi_agent_service |
| **database_service** | Blackboard persistence (Redis), audit log (TimescaleDB) |

### Directory Structure

```
multi_agent_service/
├── app/
│   ├── main.py                      # FastAPI application
│   ├── config.py                    # Service configuration
│   │
│   ├── agents/                      # Agent definitions
│   │   ├── base_agent.py            # BaseAgent with contracts
│   │   ├── coordinator.py           # Strategy Coordinator
│   │   ├── sub_agents/              # Technical specialists (12)
│   │   └── business_agents/         # Business domain agents (14)
│   │
│   ├── contracts/                   # Contract infrastructure
│   │   ├── state_machine.py         # AgentState, transitions
│   │   ├── tier_rules.py            # T0-T3 rule definitions
│   │   ├── enforcer.py              # ContractEnforcer
│   │   └── violations.py            # Violation handling, RESET
│   │
│   ├── blackboard/                  # Blackboard architecture
│   │   ├── models.py                # Task, Artifact models
│   │   ├── operations.py            # BlackboardOperations
│   │   ├── store.py                 # RedisBlackboardStore
│   │   └── audit.py                 # AuditLogEntry
│   │
│   ├── peer_review/                 # Adversarial pairing
│   │   ├── pairs.py                 # Creator→Reviewer mapping
│   │   └── review_loop.py           # ReviewLoop, escalation
│   │
│   ├── protocols/                   # Key protocols
│   │   ├── struggle.py              # Struggle Protocol
│   │   ├── hello.py                 # Hello Protocol
│   │   └── collaboration_modes.py   # Autonomous, UserDuck, etc.
│   │
│   ├── monitoring/                  # Self-monitoring
│   │   ├── token_budget.py          # TokenBudgetMonitor
│   │   ├── drift_detector.py        # DriftDetector
│   │   └── metrics.py               # Trust, Cost Gradient
│   │
│   └── api/                         # External API
│       ├── agent_routes.py          # Agent invocation
│       ├── blackboard_routes.py     # Blackboard access
│       └── dashboard_routes.py      # Dashboard endpoints
│
├── requirements.txt
└── Dockerfile
```

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          CLIENT INTERVIEW SESSION                            │
│                       (WebSocket + Conversation Service)                     │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    STRATEGY COORDINATOR (Claude Opus 4.5)                    │
│  • Style detection & adaptation  • Task analysis  • Agent delegation        │
└─────────────────────────────────────────────────────────────────────────────┘
        │                          │                          │
        ▼                          ▼                          ▼
┌───────────────────┐  ┌───────────────────┐  ┌───────────────────┐
│ STRATEGY/ANALYSIS │  │  TECHNICAL DESIGN │  │ BUSINESS OPERATIONS│
│  (8 Agents)       │  │  (8 Agents)       │  │  (8 Agents)        │
├───────────────────┤  ├───────────────────┤  ├───────────────────┤
│ Business Strat.   │  │ Architect         │  │ Sales Manager      │
│ Business Analyst  │  │ Developer         │  │ Marketing Manager  │
│ Data Analyst      │  │ Tester            │  │ Accountant         │
│ Data Scientist    │  │ Documenter        │  │ Customer Success   │
│ Operations Mgr    │  │ Deployment Spec.  │  │ HR/Talent Analyst  │
│ Mapping Spec.     │  │ UI Designer       │  │ Supply Chain       │
│ Document Analyzer │  │ ITIL Manager      │  │ Risk & Compliance  │
│ Competitive Anal. │  │ Connection Spec.  │  │ Project Manager    │
└───────────────────┘  └───────────────────┘  └───────────────────┘
        │                          │                          │
        └──────────────────────────┼──────────────────────────┘
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                        GOVERNANCE & QUALITY LAYER                            │
│              Data Governance Specialist + Process Scenario Modeler           │
└─────────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              BLACKBOARD                                      │
│  Tasks │ Artifacts │ Approval Gates │ Struggle Signals │ Audit Log          │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Agent Inventory

### Complete Agent Table (27 Agents)

| # | Agent | Model | Layer | Primary Responsibility |
|---|-------|-------|-------|------------------------|
| 1 | **Strategy Coordinator** | Claude Opus 4.5 | Orchestration | Task routing, delegation, synthesis, style adaptation |
| 2 | **Business Strategist** | Claude Sonnet 4 | Strategy | Porter's frameworks (Five Forces, Value Chain) |
| 3 | **Business Analyst** | Claude Sonnet 4 | Strategy | Industry expertise, KPIs, benchmarks |
| 4 | **Data Analyst** | Claude Sonnet 4 | Strategy | Set-based KPIs, cohort analysis, TimescaleDB |
| 5 | **Data Scientist** | Claude Sonnet 4 | Strategy | ML algorithms, correlations, predictive models |
| 6 | **Operations Manager** | Claude Sonnet 4 | Strategy | Holistic KPI analysis, bottlenecks |
| 7 | **Mapping Specialist** | Claude Sonnet 4 | Strategy | Source-to-target mapping, transformations |
| 8 | **Document Analyzer** | Claude Sonnet 4 | Strategy | Document decomposition, entity/KPI extraction |
| 9 | **Competitive Analyst** | Claude Sonnet 4 | Strategy | Peer company search, competitor profiling |
| 10 | **Architect** | Claude Sonnet 4 | Technical | DDD patterns, bounded contexts, aggregates |
| 11 | **Developer** | Claude Sonnet 4 | Technical | Schemas, Pydantic models, code artifacts |
| 12 | **Tester** | Claude Sonnet 4 | Technical | Validation, test cases, quality assurance |
| 13 | **Documenter** | Claude Sonnet 4 | Technical | Documentation, data dictionaries |
| 14 | **Deployment Specialist** | Claude Sonnet 4 | Technical | Azure/K8s infrastructure, CI/CD, Helm |
| 15 | **UI Designer** | Claude Sonnet 4 | Technical | Dashboard layouts, style guides, accessibility |
| 16 | **ITIL Manager** | Claude Sonnet 4 | Technical | Incident/Problem/Change management, SLAs |
| 17 | **Connection Specialist** | Claude Sonnet 4 | Technical | API wrappers, webhooks, integrations |
| 18 | **Sales Manager** | Claude Sonnet 4 | Business | CRM lifecycle, pipeline, forecasting |
| 19 | **Marketing Manager** | Claude Sonnet 4 | Business | Campaigns, lead scoring, attribution |
| 20 | **Accountant** | Claude Sonnet 4 | Business | Proposals, SOW, invoicing, AR/AP |
| 21 | **Customer Success** | Claude Sonnet 4 | Business | Health scores, churn prevention, NPS |
| 22 | **HR/Talent Analyst** | Claude Sonnet 4 | Business | Retention, engagement, skills gaps |
| 23 | **Supply Chain Analyst** | Claude Sonnet 4 | Business | SCOR model, inventory, logistics |
| 24 | **Risk & Compliance** | Claude Sonnet 4 | Business | Risk assessment, audit support |
| 25 | **Project Manager** | Claude Sonnet 4 | Business | Agile planning, epics, sprints |
| 26 | **Data Governance** | Claude Sonnet 4 | Governance | DAMA DMBOK, data quality, stewardship |
| 27 | **Process Modeler** | Claude Sonnet 4 | Simulation | What-if scenarios, KPI impact prediction |

### Key Agent Definitions

#### Strategy Coordinator (Master Orchestrator)

**Model**: `claude-opus-4-20250514`

**Responsibilities**:
- Style detection and adaptive communication
- Task analysis and decomposition
- Agent selection and delegation
- Result synthesis into cohesive outputs

**Tools**:
- `delegate_to_*`: Delegation to all 26 specialized sub-agents
- `synthesize_results`: Combine results from multiple agents
- `detect_communication_style`: Analyze interviewee style
- `format_response_for_style`: Adapt output formatting

**Interview Questions**:
1. "Describe your business, business model, and key strategic priorities"
2. "What pain points are you trying to address through analytics?"
3. "How will you measure success?"
4. "What decisions would you make with this information?"

#### Architect

**Model**: `claude-sonnet-4-20250514`

**DDD Patterns Applied**:
- Bounded Contexts with ubiquitous language
- Aggregates with consistency boundaries
- Domain Events for cross-context communication
- Context Mapping (Customer-Supplier, ACL, etc.)

**Tools**:
- `design_value_chain`: Create value chain structure
- `define_bounded_context`: Define DDD bounded context
- `design_aggregate`: Design aggregate with invariants
- `define_domain_event`: Define domain event with subscribers

---

## Behavioral Contracts

### Contract Architecture

Behavioral contracts constrain agent failure modes through structural constraints rather than prompting.

#### State Machine

```python
class AgentState(str, Enum):
    IDLE = "idle"
    ANALYSIS = "analysis"
    APPROVAL_PENDING = "approval_pending"
    EXECUTION = "execution"
    VALIDATION = "validation"
    DONE = "done"
    BLOCKED = "blocked"

# Forbidden Transitions
FORBIDDEN_TRANSITIONS = {
    (ANALYSIS, EXECUTION),       # Must get approval first
    (EXECUTION, DONE),           # Must validate first
    (APPROVAL_PENDING, DONE),    # Must execute first
}
```

#### Tier System for Rule Priority

| Tier | Description | Violation Response |
|------|-------------|-------------------|
| **Tier 0** | Never violated (safety, deception prevention) | Hard stop |
| **Tier 1** | Core workflow (approval gates, state machine) | Block + escalate |
| **Tier 2** | Quality (documentation, style) | Warning |
| **Tier 3** | Nice-to-have (optimization) | Log only |

Under context pressure: announce degraded mode, suspend Tier 2-3 explicitly.

#### Core Rules (Tier 0)

- Never fabricate success
- Never modify tests to make them pass
- Never skip validation
- Never expand scope silently

### Role-Specific Contracts

#### Architect Contract

```yaml
architect_contract:
  tier_0_rules:
    - "Never design entities without explicit bounded context"
    - "Never create aggregates without identifying the root"
    - "Never propose schemas without consistency boundary analysis"
  
  tier_1_rules:
    - "Apply DDD tactical patterns to all entity designs"
    - "Document relationship cardinalities explicitly"
    - "Validate designs against SOLID principles"
  
  definition_of_ready:
    - "Business domain is understood"
    - "Bounded contexts are identified"
  
  definition_of_done:
    - "Schema is valid for TimescaleDB"
    - "Aggregate boundaries are documented"
    - "Domain events are defined"
```

#### Developer Contract

```yaml
developer_contract:
  tier_0_rules:
    - "Never generate code without schema validation"
    - "Never modify tests to make them pass"
    - "Never skip type annotations"
  
  tier_1_rules:
    - "Use Pydantic v2 for all data models"
    - "Follow CQRS pattern for data operations"
    - "Generate SQLAlchemy models with proper relationships"
  
  execution_fidelity:
    - "What was approved is what gets implemented"
    - "Scope changes require re-approval"
```

#### Tester Contract (Code Reviewer)

```yaml
tester_contract:
  tier_0_rules:
    - "Never approve without running validation"
    - "Never implement code—review only"
    - "Never weaken assertions to pass"
  
  review_priority:
    1: "Security vulnerabilities"
    2: "Correctness issues"
    3: "Data integrity risks"
    4: "Performance concerns"
    5: "Code style"
  
  test_protocol:
    - "good_code + green_tests = proceed"
    - "buggy_code + red_tests = good (bug exposed)"
    - "buggy_code + green_tests = DANGEROUS"
    - "unknown_code + red_tests = STOP"
```

### Hard Stop Triggers

Binary, observable conditions that halt agent execution:

| Trigger | Description |
|---------|-------------|
| `ASSUMPTION_OVERFLOW` | ≥3 assumptions on critical path |
| `REPEATED_FIX` | Same fix proposed twice without new rationale |
| `EVIDENCE_CONTRADICTION` | Evidence contradicts hypothesis |
| `EXECUTION_DIVERGENCE` | Execution diverges from approval |
| `TOOL_FAILURE_CASCADE` | Tool fails 3× consecutively |

---

## Blackboard Architecture

The blackboard replaces pub/sub communication with a shared state model providing ordering guarantees, full auditability, and coordination without conversation.

### Data Model

```python
class BlackboardTask(BaseModel):
    task_id: str
    title: str
    description: str
    created_by: str          # Agent role that created
    assigned_to: str | None  # Agent role that claimed
    reviewer: str | None     # Agent role for review
    status: TaskStatus
    done_when: list[str]     # Falsifiable criteria
    priority: int
    dependencies: list[str]  # task_ids
    failure_count: int       # Two failures = bad task

class BlackboardArtifact(BaseModel):
    artifact_id: str
    artifact_type: ArtifactType
    task_id: str
    content: dict
    created_by: str
    review_status: str | None
    review_notes: str | None
    version: int

class AgentBlackboard(BaseModel):
    session_id: str
    tasks: dict[str, BlackboardTask]
    artifacts: dict[str, BlackboardArtifact]
    approval_gates: dict[str, ApprovalGate]
    struggle_signals: dict[str, StruggleSignalEntry]
    review_queue: list[str]
    audit_log: list[AuditLogEntry]
```

### Task Statuses

```
UNCLAIMED → CLAIMED → IN_PROGRESS → READY_FOR_REVIEW → IN_REVIEW
                                                           ↓
                                              APPROVED → MERGED
                                                   or
                                              REJECTED → (back to IN_PROGRESS)
```

### Artifact Types

- `ENTITY_DESIGN` - DDD entity definitions
- `KPI_DEFINITION` - KPI calculation specs
- `SCHEMA` - Database schemas
- `CODE` - Code artifacts
- `TEST` - Test cases
- `DOCUMENTATION` - Docs and guides
- `ANALYSIS` - Analysis results
- `SIMULATION` - What-if scenarios

---

## Peer Review System

### Adversarial Pairing

Creator ≠ Reviewer separation ensures meaningful peer supervision:

| Creator | Reviewer |
|---------|----------|
| Architect | Data Governance |
| Developer | Tester |
| Data Analyst | Business Analyst |
| Business Strategist | Operations Manager |

### Review Loop

1. Creator submits artifact to blackboard
2. Artifact enters review queue
3. Assigned reviewer claims review
4. Reviewer approves or rejects with notes
5. If rejected: Creator revises, resubmits
6. **Two-failures rule**: If two different agents fail same task → task is presumed wrong, escalate to Coordinator

---

## Protocols

### Struggle Protocol

When an agent is stuck, it must signal rather than fake progress:

```python
class StruggleSignal(BaseModel):
    signal_type: str  # "blocked", "confused", "conflicting_evidence"
    what_i_understand: str
    what_i_tried: list[dict]  # [{action, outcome}, ...]
    where_im_stuck: str
    what_would_help: str
```

**Output Format**:
```
🚨 SYNC NEEDED — [signal_type] detected
What I understand: [specific]
What I've tried: [list with outcomes]
Where I'm stuck: [specific blocker]
What would help: [specific request]
```

### Approval Request Structure

Before any state-changing action:

```python
class ApprovalRequest(BaseModel):
    intent: str           # What you're trying to achieve
    scope: str            # What files/entities affected
    approach: str         # How you plan to do it
    consequences: list    # What will change
    risks: list           # What could go wrong
    validation_plan: str  # How you'll verify success
    assumptions: list     # What you're assuming (count matters)
    reversibility: str    # Can this be undone?
```

### Hello Protocol

Session initialization diagnostic that establishes:
- Current context understanding
- Available tools and capabilities
- Contract rules in effect
- Collaboration mode (Autonomous, UserDuck, AgentDuck, Pairing)

---

## Prompt Library

A centralized, versioned system for managing agent prompts organized by scenario.

### Directory Structure

```
prompts/
├── scenarios/           # Domain-specific collections
│   ├── supply_chain/
│   ├── retail_analytics/
│   └── financial_services/
├── shared/              # Cross-scenario reusable prompts
│   ├── code_review.md
│   ├── debugging.md
│   └── contract_rules.md
└── templates/           # Base templates for scaffolding
    ├── base_agent.md
    ├── specialist_agent.md
    └── coordinator_agent.md
```

### Key Capabilities

**Agent Template Scaffolding**

```python
config = await template_registry.create_agent(
    template_name="specialist_agent",
    agent_role="supply_chain_analyst",
    customizations={
        "domain_keywords": ["inventory", "logistics"],
        "tools": ["analyze_inventory", "forecast_demand"]
    }
)
```

**Shared Prompt Fragments (DRY Principle)**

| Fragment | Purpose |
|----------|--------|
| Collaboration Rules | Blackboard coordination rules |
| Contract Rules | Enforcement thresholds and tier definitions |
| Code Review Standards | Quality criteria for reviews |
| Struggle Protocol | How to signal when stuck |

**Dry-Run Preview Mode**

```python
preview = await coordinator.delegate_with_preview(
    task="Analyze inventory levels",
    target_agent="supply_chain_analyst",
    dry_run=True  # No side effects, preview only
)
```

**Fuzzy Agent Discovery**

```python
agents = registry.find_agents("inventory")
# Returns: ["supply_chain_analyst", "operations_manager", "data_analyst"]
```

---

## Domain Skills

Specialized knowledge modules that encode best practices for specific task types.

### Available Skills

| Skill | Core Principle | Key Rules |
|-------|---------------|----------|
| **Testing** | "Tests encode intent" | Never fix tests by accepting broken code |
| **Debugging** | "Narrowing search, not guess-and-check" | Escalate after 1 failed fix |
| **Code Review** | "Risk mitigation, not gatekeeping" | 70% attention on security/correctness |
| **Code Cleaning** | "Clean code is a reader's gift" | Refactor for the next developer |
| **Systemic Thinking** | "Run the system in your head" | Find structural problems |

### Benefits

| Benefit | Description |
|---------|-------------|
| **Expertise Injection** | Domain knowledge without training |
| **Quality Consistency** | Same standards across all agents |
| **Best Practices** | Industry-proven approaches built in |

---

## MCP Integration

The multi-agent system integrates with Model Context Protocol (MCP) servers to provide agents with direct access to databases, knowledge graphs, and external search capabilities.

### MCP Servers

| Server | Location | Purpose |
|--------|----------|---------|
| **PostgreSQL MCP** | database_service | Schema introspection, table metadata, sample queries |
| **Knowledge Graph MCP** | database_service | Ontology traversal, entity context, lineage queries |
| **Web Search MCP** | External (Brave/Exa) | Competitive intelligence, news, company profiles |

### Integration Pattern

**Hybrid approach**: Direct MCP for reads, messaging for writes.

| Operation | Pattern | Rationale |
|-----------|---------|-----------|
| Schema introspection | Direct MCP | Low latency, read-only |
| Knowledge graph queries | Direct MCP | Fast traversal needed |
| Web search | Direct MCP | External service |
| Artifact persistence | Via Messaging | Audit trail, event-driven |
| Knowledge graph updates | Via Messaging | Consistency, sync to TimescaleDB |

### Agent Tool Access

| Agent | MCP Tools Available |
|-------|---------------------|
| Architect | `list_schemas`, `list_tables`, `describe_table`, `get_lineage` |
| Developer | `list_tables`, `describe_table`, `list_hypertables` |
| Data Analyst | `query_sample`, `explain_query`, `list_continuous_aggregates` |
| Competitive Analyst | `search_web`, `search_companies`, `search_news` |
| Business Strategist | `create_entity`, `create_relation`, `search_nodes` |
| Coordinator | `search_nodes`, `get_entity_context`, `open_nodes` |

### MCPClientManager

Centralized manager in `conversation_service/app/mcp/` handles:
- Client connections to internal and external MCP servers
- Tool registration per agent role
- Connection pooling and health checks

---

## Adaptive Communication

The Strategy Coordinator detects and adapts to the user's communication style.

### Style Detection

| Style | Indicators | Response Format |
|-------|------------|----------------|
| **Executive** | vision, growth, ROI, stakeholders | Executive summary, key takeaways |
| **Technical** | API, database, schema, architecture | Technical detail, specifications |
| **Analyst** | metrics, KPI, dashboard, trend | Balanced with data focus |

### Dynamic Detail Levels

| Level | Name | Description |
|-------|------|-------------|
| 1 | Summary | Executive overview, key takeaways only |
| 2 | Moderate | Key details, main points with context |
| 3 | Detailed | Comprehensive coverage, supporting details |
| 4 | Comprehensive | Full technical depth, all specifications |

**Key Principle:** When a CEO asks to "dig deeper", the system increases detail level but maintains executive vocabulary. The core style is preserved; only the depth changes.

---

## Admin Management

### Session Management

```
POST /api/v1/agents/sessions
  - Create new multi-agent design session
  - Returns session_id

POST /api/v1/agents/sessions/{session_id}/message
  - Send message to active session
  - Triggers coordinator and sub-agent processing

GET /api/v1/agents/sessions/{session_id}/artifacts
  - Retrieve generated artifacts

POST /api/v1/agents/sessions/{session_id}/finalize
  - Finalize and persist to Business Metadata Service

WebSocket /ws/agents/{session_id}
  - Real-time streaming of agent responses
```

### Blackboard Access

```
GET /api/v1/blackboard/{session_id}
  - Get current blackboard state

POST /api/v1/blackboard/{session_id}/tasks
  - Create task on blackboard

POST /api/v1/blackboard/{session_id}/tasks/{task_id}/claim
  - Claim task for execution

POST /api/v1/blackboard/{session_id}/artifacts
  - Submit artifact for review

POST /api/v1/blackboard/{session_id}/artifacts/{artifact_id}/review
  - Submit review decision
```

### Dashboard

```
GET /api/v1/dashboard/summary
  - Agent performance metrics

GET /api/v1/dashboard/hello-diagnostic
  - Run Hello Protocol diagnostic
```

### Service Integration

| Artifact Type | Target Service | API Endpoint |
|---------------|----------------|--------------|
| Entities | Business Metadata | `POST /api/v1/metadata/entities` |
| KPIs | Business Metadata | `POST /api/v1/metadata/metrics` |
| Value Chains | Business Metadata | `POST /api/v1/metadata/value-chains` |
| Relationships | Business Metadata | `POST /api/v1/metadata/relationships` |
| KPI Registration | Calculation Engine | `POST /api/v1/kpis/register` |
| Schema Migration | Database Service | `POST /api/v1/migrations/execute` |

---

## Admin Management

### Agent Profile Management

```
Admin Section
├── Agent Profiles      # View/edit all 27 agent contracts
├── New Agent           # Create new agents via pipeline
├── Contract Rules      # Browse all tiered rules
└── System Settings     # Feature flags and configuration
```

### Protected Core Agents

Five agents are protected from UI modification:

| Agent | Why Protected |
|-------|---------------|
| **Business Analyst** | Generates specs from documents |
| **Architect** | Reviews designs, assesses changes |
| **Developer** | Generates and modifies code |
| **Tester** | Validates before deployment |
| **Documenter** | Updates documentation |

These form the agent-driven code modification pipeline.

### Agent Creation Pipeline

```
Step 1: Basic Info (name, role, category, reviewer)
        ↓
Step 2: Contract Rules (Tier 0/1/2, expertise, artifacts)
        ↓
Step 3: Architect Assessment
        ├── Gap analysis
        ├── Overlap detection
        └── Recommendation (Approve/Caution/Reject)
        ↓
Step 4: Pipeline Execution
        ├── Business Analyst (if documents uploaded)
        ├── Architect (design review)
        ├── Developer (code generation)
        └── Tester (validation)
```

---

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
    developer:
      model: "claude-sonnet-4-20250514"
      max_tokens: 4096
      temperature: 0.2
    tester:
      model: "claude-sonnet-4-20250514"
      max_tokens: 4096
      temperature: 0.2

  execution:
    parallel_agents: true
    max_parallel: 3
    timeout_seconds: 120
    retry_attempts: 2

  blackboard:
    store: redis
    ttl_hours: 24
    audit_retention_days: 90

  contracts:
    enforcement_enabled: true
    degraded_mode_threshold: 0.8
```

---

## Dependencies

```
claude-agent-sdk>=1.0.0
anthropic>=0.40.0
anyio>=4.0.0
redis>=5.0.0
httpx>=0.27.0
pydantic>=2.0.0
```

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| **AI Engine** | Anthropic Claude (Opus + Sonnet) |
| **Backend** | Python, FastAPI, Pydantic v2 |
| **State Storage** | Redis (Blackboard) |
| **Audit Log** | TimescaleDB |
| **Messaging** | Redis Streams + Pub/Sub |

---

## Summary

The Multi-Agent Service transforms AI agents from unpredictable assistants into reliable enterprise partners through:

1. **Contract-Enforced Behavior** — Structural constraints that prevent deception and ensure auditability
2. **Blackboard Architecture** — Shared state coordination without hallucination-prone direct conversation
3. **Peer Review** — Adversarial pairing that catches defects before they reach production
4. **Prompt Library** — Centralized, versioned prompts for consistency and rapid agent creation
5. **Adaptive Communication** — Style detection that matches executive, technical, or analyst preferences
6. **Domain Skills** — Best practices encoded for testing, debugging, code review, and more
7. **Admin Management** — Self-service agent creation with Architect assessment and protected core agents

---

## Related Documentation

- [Agent Testing Guide](../testing/AGENT_TESTING_GUIDE.md) - Test strategy and procedures
- [Event-Driven Architecture](./EVENT_DRIVEN_ARCHITECTURE.md) - Messaging patterns
