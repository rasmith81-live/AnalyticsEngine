# Agent Contracts Build Plan for AnalyticsEngine Conversation Service

---

## Attribution & Acknowledgments

This build plan is based on the groundbreaking work of **Tangi Vass** on behavioral contracts for AI coding agents. The concepts, patterns, and architectural decisions documented here are derived from:

### Primary Sources

| Source | Author | Link |
|--------|--------|------|
| **"Turning AI Coding Agents into Senior Engineering Peers"** | Tangi Vass | [Medium Article](https://medium.com/@tangi.vass/turning-ai-coding-agents-into-senior-engineering-peers-c3d178621c9e) |
| **"I Tried to Kill Vibe Coding. I Built Adversarial Vibe Coding. Without the Vibes."** | Tangi Vass | [Medium Article](https://medium.com/@tangi.vass/i-tried-to-kill-vibe-coding-i-built-adversarial-vibe-coding-without-the-vibes-bc4a63872440) |
| **LIZA: Peer-Supervised Multi-Agent System** | Tangi Vass | [GitHub Repository](https://github.com/liza-mas/liza) |

### Key Concepts Attributed to Tangi Vass

The following concepts and patterns are directly derived from Tangi Vass's research and the LIZA system:

- **Behavioral Contracts** — Structural constraints that shape agent behavior
- **State Machine with Forbidden Transitions** — Discrete states with hard constraints
- **Tier System (T0-T3)** — Rule priority hierarchy with graceful degradation
- **Struggle Protocol** — Transforming deception risk into collaboration opportunity
- **Three-Way Pairing** — Planner, Coder, Reviewer collaboration pattern
- **Blackboard Architecture** — Shared state coordination without agent conversation
- **Adversarial Pairing** — Creator ≠ Reviewer separation for peer supervision
- **Definition of Ready / Definition of Done** — Mental models as reasoning gates
- **Hard Stop Triggers** — Binary, observable halt conditions
- **RESET Semantics** — Violation cascade prevention
- **Amendment System** — Self-correcting contracts under supervision
- **Collaboration Modes** — Autonomous, UserDuck, AgentDuck, Pairing
- **Hello Protocol** — Session initialization and diagnostic
- **Magic Phrases** — Steering shortcuts without breaking flow
- **Cost Gradient** — Thought → Words → Specs → Code → Tests → Docs → Commits
- **Skills** — Domain-specific contract applications (Testing, Debugging, Systemic Thinking, etc.)
- **Degraded Mode Announcements** — Visible trade-offs under pressure

### License Consideration

Please refer to the [LIZA repository](https://github.com/liza-mas/liza) for licensing terms. This build plan adapts the concepts for the AnalyticsEngine context but implementers should review the original work for complete understanding and compliance.

---

## Executive Summary

This document outlines the implementation plan for applying **Behavioral Agent Contracts** to the AnalyticsEngine's multi-agent conversation service. The approach is based on Tangi Vass's research on turning AI coding agents into senior engineering peers through structured behavioral constraints.

---

## Article Summaries

### Article 1: "Turning AI Coding Agents into Senior Engineering Peers"

**Core Insight**: Agents already have the ability to behave like senior engineering peers, but their training optimizes for *appearing helpful* over *being reliable*. The fix isn't better prompts—it's behavioral contracts that constrain failure modes.

#### Key Problems Identified

| Problem | Description |
|---------|-------------|
| **Deception** | Agents modify tests instead of fixing code, claim success without validation |
| **Sycophancy** | Agents prioritize agreement over correctness |
| **Scope Creep** | Agents execute X+Y+Z when only X+Y was approved |
| **Random Changes** | Agents spiral through trial-and-error instead of systematic debugging |
| **Lazy Paths** | Agents take shortcuts that create technical debt |

#### The Contract Architecture

**1. Core Rules (Non-Negotiable)**
- Never fabricate success
- Never modify tests to make them pass
- Never skip validation
- Never expand scope silently

**2. State Machine with Forbidden Transitions**
```
ANALYSIS → APPROVAL_PENDING → EXECUTION → VALIDATION → DONE
```
- **Forbidden**: ANALYSIS → EXECUTION (skipping approval)
- **Forbidden**: EXECUTION → DONE (skipping validation)

**3. Approval + Execution Fidelity**
- Before any state-changing action, present:
  - Intent, Scope, Commands, Consequences, Risks, Validation Plan
- What was approved is what gets executed—period
- Divergence requires explicit re-approval

**4. Struggle Protocol**
- When stuck, agents must signal:
  ```
  🚨 SYNC NEEDED — [failure signal] detected
  What I understand: [specific]
  What I've tried: [list with outcomes]
  Where I'm stuck: [specific blocker]
  What would help: [specific request]
  ```
- Transforms deception risk into collaboration opportunity

**5. Hard Stop Triggers** (Binary, Observable, Process-based)
- Assumption count ≥3 on critical path
- Same fix proposed twice without new rationale
- Evidence contradicts hypothesis
- Execution diverges from approval
- Tool fails 3× consecutively

**6. Test Protocol**
| Code State | Test State | Interpretation |
|------------|------------|----------------|
| Good | Green | ✓ Proceed |
| Buggy | Red | ✓ Good (bug exposed) |
| Buggy | Green | 🚨 DANGEROUS |
| Unknown | Red | STOP - don't guess |

**7. Tier System for Rule Priority**
- **Tier 0**: Never violated (safety, deception prevention)
- **Tier 1**: Core workflow (approval gates, state machine)
- **Tier 2**: Quality (documentation, style)
- **Tier 3**: Nice-to-have (optimization)

Under context pressure: announce degraded mode, suspend Tier 2-3 explicitly.

---

### Article 2: "Adversarial Vibe Coding Without the Vibes" (Liza)

**Core Insight**: The same behavioral contracts can enable *peer-supervised autonomous execution*—multiple agents coordinating without human in the loop, but with the contract providing the discipline humans would enforce.

#### Liza Architecture: Multi-Agent System

**Three Roles**:
1. **Planner**: Reads specs, decomposes goals, sets done_when criteria
2. **Coder**: Claims tasks, implements in isolated worktrees, submits for review
3. **Code Reviewer**: Examines work, approves or rejects, merges

**Key Constraints**:
- Coder can't merge their own work—ever
- Reviewer can't implement code—ever
- This separation makes peer collaboration meaningful

**Blackboard Architecture**:
- Agents coordinate through shared YAML state
- No direct conversation between agents
- Read state → Do work → Write state
- Everything visible, everything auditable

**Skills as Domain-Specific Contracts**:

| Skill | Core Principle |
|-------|---------------|
| **Code Cleaning** | "Clean Code is a reader's gift" - refactor for the next developer |
| **Testing** | "Tests encode intent" - never fix tests by accepting broken code |
| **Debugging** | "Narrowing search, not guess-and-check" - escalate after 1 failed fix |
| **Code Review** | "Risk mitigation, not gatekeeping" - 70% attention on security/correctness |
| **Systemic Thinking** | "Run the system in your head at 2am" - find structural problems |

**Task Management**:
- Tasks have explicit `done_when` criteria (falsifiable)
- If two different Coders fail the same task → task is presumed wrong
- Planner must document why before rescoping (closes infinite retry loop)

---

## Current AnalyticsEngine Multi-Agent Architecture

### Complete Agent Inventory (27 Agents)

| # | Agent | Model | Layer | Primary Responsibility |
|---|-------|-------|-------|------------------------|
| 1 | **Strategy Coordinator** | Claude Opus 4.5 | Orchestration | Task routing, delegation, synthesis, style adaptation |
| 2 | **Business Strategist** | Claude Sonnet 4 | Strategy & Analysis | Porter's frameworks (Five Forces, Value Chain, Generic Strategy) |
| 3 | **Business Analyst** | Claude Sonnet 4 | Strategy & Analysis | Industry expertise, KPIs, benchmarks, best practices |
| 4 | **Data Analyst** | Claude Sonnet 4 | Strategy & Analysis | Set-based KPIs, cohort analysis, TimescaleDB optimization |
| 5 | **Data Scientist** | Claude Sonnet 4 | Strategy & Analysis | ML algorithms, correlations, predictive models |
| 6 | **Operations Manager** | Claude Sonnet 4 | Strategy & Analysis | Holistic KPI analysis, bottlenecks, optimization |
| 7 | **Mapping Specialist** | Claude Sonnet 4 | Strategy & Analysis | Source-to-target mapping, transformations |
| 8 | **Document Analyzer** | Claude Sonnet 4 | Strategy & Analysis | Document decomposition, entity/KPI extraction |
| 9 | **Architect** | Claude Sonnet 4 | Technical Design | DDD patterns, bounded contexts, aggregates, domain events |
| 10 | **Developer** | Claude Sonnet 4 | Technical Design | Schemas, Pydantic models, code artifacts, API specs |
| 11 | **Tester** | Claude Sonnet 4 | Technical Design | Validation, test cases, quality assurance |
| 12 | **Documenter** | Claude Sonnet 4 | Technical Design | Documentation, data dictionaries, user guides |
| 13 | **Deployment Specialist** | Claude Sonnet 4 | Technical Design | Azure/K8s infrastructure, CI/CD, Helm charts |
| 14 | **UI Designer** | Claude Sonnet 4 | Technical Design | Dashboard layouts, style guides, accessibility |
| 15 | **ITIL Manager** | Claude Sonnet 4 | Technical Design | Incident/Problem/Change management, SLAs, CMDB |
| 16 | **Connection Specialist** | Claude Sonnet 4 | Technical Design | API wrappers, webhooks, system integrations |
| 17 | **Sales Manager** | Claude Sonnet 4 | Business Operations | CRM lifecycle, pipeline, prospect → client |
| 18 | **Marketing Manager** | Claude Sonnet 4 | Business Operations | Campaigns, lead scoring, content calendars |
| 19 | **Accountant** | Claude Sonnet 4 | Business Operations | Proposals, SOW, invoicing, AR/AP |
| 20 | **Customer Success Manager** | Claude Sonnet 4 | Business Operations | Health scores, churn prevention, NPS |
| 21 | **HR/Talent Analyst** | Claude Sonnet 4 | Business Operations | Retention, engagement, skills gaps |
| 22 | **Supply Chain Analyst** | Claude Sonnet 4 | Business Operations | SCOR model, inventory, suppliers, logistics |
| 23 | **Risk & Compliance Officer** | Claude Sonnet 4 | Business Operations | Risk assessment, compliance, audit support |
| 24 | **Project Manager** | Claude Sonnet 4 | Business Operations | Agile planning, epics, sprints, user stories |
| 25 | **Data Governance Specialist** | Claude Sonnet 4 | Governance | DAMA DMBOK, data quality, security, stewardship |
| 26 | **Competitive Analyst** | Claude Sonnet 4 | Intelligence | Peer company search, competitor profiling, market gaps |
| 27 | **Process Scenario Modeler** | Claude Sonnet 4 | Simulation | Process simulation, what-if scenarios, KPI impact |

### Current Architecture Layers

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                              CLIENT INTERVIEW SESSION                                    │
│                           (WebSocket + Conversation Service)                             │
└─────────────────────────────────────────────────────────────────────────────────────────┘
                                          │
                                          ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                        STRATEGY COORDINATOR (Claude Opus 4.5)                            │
│  • Style detection & adaptation  • Task analysis  • Agent delegation  • Synthesis       │
└─────────────────────────────────────────────────────────────────────────────────────────┘
          │                          │                          │
          ▼                          ▼                          ▼
┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
│ STRATEGY & ANALYSIS │  │  TECHNICAL DESIGN   │  │ BUSINESS OPERATIONS │
│  (8 Agents)         │  │  (8 Agents)         │  │  (8 Agents)         │
├─────────────────────┤  ├─────────────────────┤  ├─────────────────────┤
│ Business Strategist │  │ Architect           │  │ Sales Manager       │
│ Business Analyst    │  │ Developer           │  │ Marketing Manager   │
│ Data Analyst        │  │ Tester              │  │ Accountant          │
│ Data Scientist      │  │ Documenter          │  │ Customer Success    │
│ Operations Manager  │  │ Deployment Spec.    │  │ HR/Talent Analyst   │
│ Mapping Specialist  │  │ UI Designer         │  │ Supply Chain        │
│ Document Analyzer   │  │ ITIL Manager        │  │ Risk & Compliance   │
│ Competitive Analyst │  │ Connection Spec.    │  │ Project Manager     │
└─────────────────────┘  └─────────────────────┘  └─────────────────────┘
          │                          │                          │
          └──────────────────────────┼──────────────────────────┘
                                     ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                            GOVERNANCE & QUALITY LAYER                                    │
│                        Data Governance Specialist + Process Scenario Modeler             │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

### Current Communication Pattern (Pub/Sub via Redis)

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Agent A    │────▶│  Redis Pub   │────▶│   Agent B    │
│              │     │   Channel    │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
        │                                         │
        │            ┌──────────────┐             │
        └───────────▶│   Context    │◀────────────┘
                     │  Artifacts   │
                     └──────────────┘
```

**Current Issues with Pub/Sub**:
1. **No Ordering Guarantee**: Messages may arrive out of order
2. **Fire-and-Forget**: No confirmation of receipt or processing
3. **No Built-in Audit**: Requires separate logging infrastructure
4. **State Fragmentation**: Context artifacts scattered across agents
5. **No Approval Gates**: Actions executed without structured approval

### Current Control Mechanisms

| Mechanism | Location | Purpose |
|-----------|----------|---------|
| `max_tool_calls` | AgentConfig | Limit API costs |
| `max_consultation_depth` | AgentConfig | Prevent infinite peer chains |
| `signal_ready_for_coordinator` | BaseAgent | Signal task completion |
| `_should_early_exit()` | BaseAgent | Cost optimization check |
| Peer connections | Orchestrator | Define who can consult whom |
| `context.artifacts` | AgentContext | Shared state storage |

### Gaps Identified

| Gap | Impact | Contract Solution |
|-----|--------|-------------------|
| **No Approval Gates** | Agents execute without approval | Approval Request + State Machine |
| **No State Machine** | No explicit states/transitions | AgentState enum + forbidden transitions |
| **No Struggle Protocol** | Agents fake progress when stuck | StruggleSignal with structured format |
| **No Hard Stop Triggers** | Runaway behavior unchecked | Binary, observable halt conditions |
| **No Test Protocol** | Tests modified to pass | Test integrity rules (Tier 0) |
| **No Execution Fidelity** | Drift from approved plan | Approval vs execution comparison |
| **No Role Separation** | No adversarial review | Creator ≠ Reviewer pairs |
| **No Audit Trail** | Can't trace decisions | Blackboard with immutable log |
| **Pub/Sub Fragility** | Lost messages, ordering | Blackboard shared state |

---

## Service Architecture

The agent contract infrastructure is implemented as a dedicated backend service that the conversation service consumes.

### Service Location

```
services/backend_services/multi_agent_service/
```

### Service Responsibilities

| Service | Responsibility |
|---------|----------------|
| **multi_agent_service** | Agent contracts, blackboard, peer review, skills, dashboard |
| **conversation_service** | Session management, client interview flow, uses multi_agent_service |
| **database_service** | Blackboard persistence (Redis), audit log (TimescaleDB) |

### Service Structure

```
services/backend_services/multi_agent_service/
├── app/
│   ├── __init__.py
│   ├── main.py                      # FastAPI app
│   ├── config.py
│   │
│   ├── agents/                      # Agent definitions
│   │   ├── __init__.py
│   │   ├── base_agent.py            # BaseAgent with contracts
│   │   ├── coordinator.py           # Strategy Coordinator
│   │   ├── strategy_agents.py       # Strategy & Analysis layer
│   │   ├── technical_agents.py      # Technical Design layer
│   │   ├── business_agents.py       # Business Operations layer
│   │   └── governance_agents.py     # Governance layer
│   │
│   ├── contracts/                   # Contract infrastructure
│   │   ├── __init__.py
│   │   ├── state_machine.py         # AgentState, transitions
│   │   ├── tier_rules.py            # T0-T3 rule definitions
│   │   ├── enforcer.py              # ContractEnforcer
│   │   ├── violations.py            # Violation handling, RESET
│   │   └── amendments.py            # Amendment system
│   │
│   ├── blackboard/                  # Blackboard architecture
│   │   ├── __init__.py
│   │   ├── models.py                # BlackboardTask, Artifact, etc.
│   │   ├── operations.py            # BlackboardOperations
│   │   ├── store.py                 # RedisBlackboardStore
│   │   └── audit.py                 # AuditLogEntry, queries
│   │
│   ├── peer_review/                 # Adversarial pairing
│   │   ├── __init__.py
│   │   ├── pairs.py                 # Creator→Reviewer mapping
│   │   ├── review_loop.py           # ReviewLoop, rejection handling
│   │   └── escalation.py            # Two-failures rule
│   │
│   ├── skills/                      # Domain-specific skills
│   │   ├── __init__.py
│   │   ├── base_skill.py            # Skill base class
│   │   ├── testing.py               # Testing skill
│   │   ├── debugging.py             # Debugging skill
│   │   ├── code_review.py           # Code Review skill
│   │   ├── code_cleaning.py         # Code Cleaning skill
│   │   └── systemic_thinking.py     # Systemic Thinking skill
│   │
│   ├── protocols/                   # Key protocols
│   │   ├── __init__.py
│   │   ├── struggle.py              # Struggle Protocol
│   │   ├── hello.py                 # Hello Protocol
│   │   ├── collaboration_modes.py   # Autonomous, UserDuck, etc.
│   │   ├── magic_phrases.py         # Steering shortcuts
│   │   └── session_continuity.py    # Durable memory
│   │
│   ├── monitoring/                  # Self-monitoring
│   │   ├── __init__.py
│   │   ├── token_budget.py          # TokenBudgetMonitor
│   │   ├── drift_detector.py        # DriftDetector
│   │   ├── degraded_mode.py         # DegradedModeMonitor
│   │   └── metrics.py               # Trust, Cost Gradient, etc.
│   │
│   ├── dashboard/                   # Performance dashboard
│   │   ├── __init__.py
│   │   ├── api.py                   # Dashboard API endpoints
│   │   ├── hello_diagnostic.py      # HelloDiagnostic runner
│   │   └── views.py                 # Dashboard view configs
│   │
│   └── api/                         # External API
│       ├── __init__.py
│       ├── agent_routes.py          # Agent invocation
│       ├── blackboard_routes.py     # Blackboard access
│       ├── dashboard_routes.py      # Dashboard endpoints
│       └── health.py                # Health checks
│
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Build Plan: Applying Agent Contracts

### Phase 1: Contract Foundation (BaseAgent Enhancements)

#### 1.1 Add State Machine to BaseAgent

```python
# =============================================================================
# Agent Contract Implementation
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================

class AgentState(str, Enum):
    IDLE = "idle"
    ANALYSIS = "analysis"
    APPROVAL_PENDING = "approval_pending"
    EXECUTION = "execution"
    VALIDATION = "validation"
    DONE = "done"
    BLOCKED = "blocked"

class AgentContract:
    """Behavioral contract for agent operations."""
    
    # Forbidden transitions
    FORBIDDEN_TRANSITIONS = {
        (AgentState.ANALYSIS, AgentState.EXECUTION),      # Must get approval
        (AgentState.EXECUTION, AgentState.DONE),          # Must validate
        (AgentState.APPROVAL_PENDING, AgentState.DONE),   # Must execute
    }
    
    # Required mental models per transition
    TRANSITION_GATES = {
        (AgentState.ANALYSIS, AgentState.APPROVAL_PENDING): "definition_of_ready",
        (AgentState.VALIDATION, AgentState.DONE): "definition_of_done",
    }
```

**Files to modify**: `@/services/business_services/conversation_service/app/agents/base_agent.py`

#### 1.2 Add Approval Request Structure

```python
class ApprovalRequest(BaseModel):
    """Structured approval request before any state-changing action."""
    intent: str                           # What you're trying to achieve
    scope: str                            # What files/entities will be affected
    approach: str                         # How you plan to do it
    consequences: List[str]               # What will change
    risks: List[str]                      # What could go wrong
    validation_plan: str                  # How you'll verify success
    assumptions: List[str]                # What you're assuming (count matters)
    reversibility: str                    # Can this be undone?
```

#### 1.3 Add Struggle Protocol

```python
class StruggleSignal(BaseModel):
    """Structured signal when agent is stuck."""
    signal_type: str                      # "blocked", "confused", "conflicting_evidence"
    what_i_understand: str
    what_i_tried: List[Dict[str, str]]    # {"action": ..., "outcome": ...}
    where_im_stuck: str
    what_would_help: str
```

#### 1.4 Add Hard Stop Triggers

```python
class HardStopTrigger(str, Enum):
    ASSUMPTION_OVERFLOW = "assumption_count_exceeded"
    REPEATED_FIX = "same_fix_proposed_twice"
    EVIDENCE_CONTRADICTION = "evidence_contradicts_hypothesis"
    EXECUTION_DIVERGENCE = "execution_diverges_from_approval"
    TOOL_FAILURE_CASCADE = "tool_failed_3x"
    RULE_VIOLATION_REPEAT = "same_rule_violated_twice"

class ContractEnforcer:
    """Monitors agent behavior for contract violations."""
    
    def __init__(self):
        self.assumption_count = 0
        self.fix_history: List[str] = []
        self.tool_failures: Dict[str, int] = {}
        self.violations: List[str] = []
    
    def check_triggers(self) -> Optional[HardStopTrigger]:
        if self.assumption_count >= 3:
            return HardStopTrigger.ASSUMPTION_OVERFLOW
        # ... other checks
```

---

### Phase 2: Role-Specific Contracts

#### 2.1 Coordinator Contract (StrategyCoordinator)

**Role**: Master orchestrator—delegates, synthesizes, ensures workflow integrity

**Contract Elements**:
```yaml
coordinator_contract:
  tier_0_rules:  # Never violated
    - "Never claim design is complete without verification against completeness criteria"
    - "Never ignore a sub-agent's struggle signal"
    - "Never re-delegate without new information or refined context"
  
  tier_1_rules:  # Core workflow
    - "Always synthesize sub-agent results before responding to user"
    - "Track design progress against completeness dimensions"
    - "Route KPI requests through LibrarianCurator first"
  
  state_machine:
    states: [INTAKE, ANALYSIS, DELEGATION, SYNTHESIS, PRESENTATION]
    forbidden: 
      - [INTAKE, PRESENTATION]  # Must analyze before presenting
      - [DELEGATION, PRESENTATION]  # Must synthesize results
  
  delegation_approval:
    required_fields:
      - agent_target
      - task_description
      - expected_output_type
      - integration_point  # How result fits the whole
```

#### 2.2 Architect Contract

**Role**: Value chain structure, DDD patterns, entity design

**Contract Elements**:
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
    - "Entity relationships are mapped"
  
  definition_of_done:
    - "Schema is valid for TimescaleDB"
    - "Aggregate boundaries are documented"
    - "Domain events are defined for cross-context communication"
  
  struggle_triggers:
    - "Cannot identify bounded context boundaries"
    - "Conflicting relationship requirements"
    - "Missing entity lifecycle information"
```

#### 2.3 Business Analyst Contract

**Role**: Industry expertise, KPI identification, requirements gathering

**Contract Elements**:
```yaml
business_analyst_contract:
  tier_0_rules:
    - "Never fabricate industry benchmarks"
    - "Never assume KPI definitions without validation"
    - "Always cite sources for industry standards"
  
  tier_1_rules:
    - "Map requirements to measurable outcomes"
    - "Identify leading vs lagging indicators"
    - "Validate business rules with domain experts"
  
  definition_of_ready:
    - "Industry context is established"
    - "Business objectives are articulated"
    - "Stakeholders are identified"
  
  definition_of_done:
    - "Requirements are SMART (Specific, Measurable, Achievable, Relevant, Time-bound)"
    - "KPIs have calculation definitions"
    - "Business rules are documented"
```

#### 2.4 Data Analyst Contract

**Role**: Set-based KPI design, calculation engine optimization

**Contract Elements**:
```yaml
data_analyst_contract:
  tier_0_rules:
    - "Never design KPIs without entity-level granularity specification"
    - "Never assume data availability without verification"
    - "Tests encode intent—never modify tests to pass"
  
  tier_1_rules:
    - "Use set-based operations for TimescaleDB optimization"
    - "Design for cohort analysis capability"
    - "Document calculation dependency chains"
  
  test_protocol:
    # Interpretation matrix
    - "good_code + green_tests = proceed"
    - "buggy_code + red_tests = good (bug exposed)"
    - "buggy_code + green_tests = DANGEROUS - tests incomplete"
    - "unknown_code + red_tests = STOP - investigate first"
  
  definition_of_done:
    - "KPI has SQL/calculation formula"
    - "Time dimensions are specified"
    - "Aggregation levels are defined"
    - "Unit tests validate calculation logic"
```

#### 2.5 Developer Contract

**Role**: Schema generation, code artifacts, API design

**Contract Elements**:
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
  
  code_cleaning_skill:
    principle: "Clean code is a reader's gift"
    pre_flight: "Verify test coverage before refactoring"
    constraint: "Never mix bug fixes with refactoring"
  
  execution_fidelity:
    - "What was approved is what gets implemented"
    - "Scope changes require re-approval"
    - "Document all deviations with rationale"
```

#### 2.6 Tester Contract (Becomes Code Reviewer Role)

**Role**: Validation, quality assurance, review gate

**Contract Elements**:
```yaml
tester_contract:
  tier_0_rules:
    - "Never approve without running validation"
    - "Never implement code—review only"
    - "Never weaken assertions to pass"
  
  tier_1_rules:
    - "Apply the 2am test: would I debug this at 2am?"
    - "70% attention on security, correctness, data integrity"
    - "Verify done_when criteria are met"
  
  review_skill:
    priority_hierarchy:
      1: "Security vulnerabilities"
      2: "Correctness issues"
      3: "Data integrity risks"
      4: "Performance concerns"
      5: "Code style"
  
  approval_criteria:
    - "All tests pass"
    - "No security vulnerabilities"
    - "Meets acceptance criteria"
    - "Documentation updated"
```

#### 2.7 Documenter Contract

**Role**: Documentation generation, data dictionaries, user guides

**Contract Elements**:
```yaml
documenter_contract:
  tier_0_rules:
    - "Never document functionality that doesn't exist"
    - "Never omit security-relevant information"
    - "Always include version and last-updated timestamp"
  
  tier_1_rules:
    - "Document all public APIs with examples"
    - "Include data dictionary entries for all entities"
    - "Generate runbooks for operational procedures"
  
  definition_of_done:
    - "All entities have data dictionary entries"
    - "API documentation includes request/response examples"
    - "Runbooks have rollback procedures"
```

#### 2.8 Deployment Specialist Contract

**Role**: Azure/K8s infrastructure, CI/CD, Helm charts

**Contract Elements**:
```yaml
deployment_specialist_contract:
  tier_0_rules:
    - "Never deploy without environment validation"
    - "Never hardcode secrets in manifests"
    - "Always include rollback procedures"
  
  tier_1_rules:
    - "Use ARM/Bicep for Azure resources"
    - "Generate Helm charts with values per environment"
    - "Include health checks and readiness probes"
  
  deployment_checklist:
    - "Resource naming follows convention"
    - "Secrets managed via Key Vault"
    - "HPA configured for scaling"
    - "Network policies defined"
```

#### 2.9 UI Designer Contract

**Role**: Dashboard layouts, style guides, accessibility

**Contract Elements**:
```yaml
ui_designer_contract:
  tier_0_rules:
    - "Never design without WCAG 2.1 AA compliance check"
    - "Never use color alone to convey information"
    - "Always provide responsive layouts"
  
  tier_1_rules:
    - "Apply consistent design tokens"
    - "Ensure data visualizations are colorblind-safe"
    - "Include loading and error states"
  
  accessibility_checklist:
    - "Color contrast ratio ≥ 4.5:1"
    - "All interactive elements keyboard accessible"
    - "ARIA labels on data visualizations"
```

#### 2.10 ITIL Manager Contract

**Role**: Incident/Problem/Change management, SLAs, CMDB

**Contract Elements**:
```yaml
itil_manager_contract:
  tier_0_rules:
    - "Never bypass CAB for high-risk changes"
    - "Never close incidents without root cause"
    - "Always link problems to incidents"
  
  tier_1_rules:
    - "Apply ITIL 4 practices to all service management"
    - "Track SLA compliance continuously"
    - "Maintain CMDB accuracy"
  
  change_risk_matrix:
    high_risk: ["production_database", "security_config", "network"]
    medium_risk: ["application_config", "ci_cd_pipeline"]
    low_risk: ["documentation", "dev_environment"]
```

#### 2.11 Connection Specialist Contract

**Role**: API wrappers, webhooks, system integrations

**Contract Elements**:
```yaml
connection_specialist_contract:
  tier_0_rules:
    - "Never store credentials in code"
    - "Never skip connection testing"
    - "Always implement retry with backoff"
  
  tier_1_rules:
    - "Use OAuth 2.0 where available"
    - "Implement webhook signature validation"
    - "Design for idempotency"
  
  integration_checklist:
    - "Authentication method documented"
    - "Rate limits identified and respected"
    - "Error handling covers all HTTP status codes"
    - "Timeout and retry configured"
```

#### 2.12 Sales Manager Contract

**Role**: CRM lifecycle, pipeline management

**Contract Elements**:
```yaml
sales_manager_contract:
  tier_0_rules:
    - "Never advance stage without qualification criteria met"
    - "Never fabricate pipeline metrics"
    - "Always coordinate pricing with Accountant"
  
  tier_1_rules:
    - "Apply BANT qualification consistently"
    - "Track conversion rates per stage"
    - "Coordinate MQL handoff with Marketing"
  
  pipeline_gates:
    prospect_to_lead: ["company_identified", "contact_made"]
    lead_to_opportunity: ["bant_qualified", "discovery_complete"]
    opportunity_to_client: ["proposal_accepted", "contract_signed"]
```

#### 2.13 Marketing Manager Contract

**Role**: Campaigns, lead scoring, content calendars

**Contract Elements**:
```yaml
marketing_manager_contract:
  tier_0_rules:
    - "Never report vanity metrics as success"
    - "Never launch campaigns without tracking"
    - "Always define MQL criteria with Sales"
  
  tier_1_rules:
    - "Track CAC and marketing ROI"
    - "A/B test before full rollout"
    - "Coordinate lead handoff with Sales Manager"
  
  campaign_checklist:
    - "Target audience defined"
    - "Success metrics identified"
    - "UTM tracking implemented"
    - "Budget allocated"
```

#### 2.14 Accountant Contract

**Role**: Proposals, SOW, invoicing, AR/AP

**Contract Elements**:
```yaml
accountant_contract:
  tier_0_rules:
    - "Never create invoices without approved SOW"
    - "Never skip payment terms documentation"
    - "Always reconcile AR/AP monthly"
  
  tier_1_rules:
    - "Apply revenue recognition standards"
    - "Track aging reports weekly"
    - "Coordinate with Sales on deal pricing"
  
  financial_controls:
    - "Dual approval for invoices > threshold"
    - "SOW signed before work starts"
    - "Payment terms explicit"
```

#### 2.15 Customer Success Manager Contract

**Role**: Health scores, churn prevention, NPS

**Contract Elements**:
```yaml
customer_success_contract:
  tier_0_rules:
    - "Never ignore declining health scores"
    - "Never skip intervention for at-risk customers"
    - "Always document churn reasons"
  
  tier_1_rules:
    - "Calculate health scores across 4 dimensions"
    - "Track NPS trends over time"
    - "Identify expansion opportunities proactively"
  
  health_score_dimensions:
    - "Usage engagement"
    - "Support ticket volume"
    - "Payment history"
    - "Stakeholder engagement"
```

#### 2.16 HR/Talent Analyst Contract

**Role**: Retention, engagement, skills gaps

**Contract Elements**:
```yaml
hr_talent_contract:
  tier_0_rules:
    - "Never share individual employee data publicly"
    - "Never skip flight risk follow-up"
    - "Always anonymize survey results"
  
  tier_1_rules:
    - "Analyze turnover by department and tenure"
    - "Track engagement trends quarterly"
    - "Benchmark compensation annually"
  
  privacy_constraints:
    - "Individual data requires consent"
    - "Aggregates must have n ≥ 5"
    - "PII masked in reports"
```

#### 2.17 Supply Chain Analyst Contract

**Role**: SCOR model, inventory, suppliers

**Contract Elements**:
```yaml
supply_chain_contract:
  tier_0_rules:
    - "Never recommend stockouts for critical items"
    - "Never ignore supplier risk indicators"
    - "Always validate demand forecasts"
  
  tier_1_rules:
    - "Apply ABC/XYZ inventory classification"
    - "Track SCOR metrics across Plan/Source/Make/Deliver/Return"
    - "Evaluate supplier performance quarterly"
  
  scor_metrics:
    plan: ["forecast_accuracy", "inventory_days"]
    source: ["supplier_otd", "purchase_order_cycle"]
    make: ["manufacturing_cycle", "yield_rate"]
    deliver: ["otif", "order_fulfillment"]
    return: ["return_rate", "warranty_cost"]
```

#### 2.18 Risk & Compliance Officer Contract

**Role**: Risk assessment, compliance, audit support

**Contract Elements**:
```yaml
risk_compliance_contract:
  tier_0_rules:
    - "Never downgrade risk without documented mitigation"
    - "Never skip compliance deadlines"
    - "Always escalate critical findings"
  
  tier_1_rules:
    - "Apply risk scoring (probability × impact)"
    - "Track control effectiveness"
    - "Maintain audit-ready documentation"
  
  risk_thresholds:
    critical: { probability: ">0.7", impact: ">0.8" }
    high: { probability: ">0.5", impact: ">0.6" }
    medium: { probability: ">0.3", impact: ">0.4" }
```

#### 2.19 Project Manager Contract

**Role**: Agile planning, epics, sprints, user stories

**Contract Elements**:
```yaml
project_manager_contract:
  tier_0_rules:
    - "Never commit scope without team capacity check"
    - "Never skip retrospective action items"
    - "Always maintain risk register"
  
  tier_1_rules:
    - "Apply Scrum/Kanban ceremonies consistently"
    - "Write user stories in standard format"
    - "Track velocity and use for forecasting"
  
  story_format:
    template: "As a [persona], I want [feature], so that [value]"
    acceptance: "Given [context], When [action], Then [outcome]"
```

#### 2.20 Data Governance Specialist Contract

**Role**: DAMA DMBOK governance, compliance evaluation

**Contract Elements**:
```yaml
data_governance_contract:
  tier_0_rules:
    - "Never approve data designs without governance review"
    - "Never skip data quality assessment"
    - "Always document data lineage"
  
  tier_1_rules:
    - "Apply DAMA DMBOK framework to all evaluations"
    - "Identify data stewardship responsibilities"
    - "Define data retention policies"
  
  dmbok_areas:
    - "Data Governance"
    - "Data Architecture"
    - "Data Modeling"
    - "Data Storage"
    - "Data Security"
    - "Data Integration"
    - "Document Management"
    - "Data Warehousing"
    - "Metadata Management"
    - "Reference & Master Data"
    - "Data Quality"
```

#### 2.21 Competitive Analyst Contract

**Role**: Peer company search, competitor profiling, market gaps

**Contract Elements**:
```yaml
competitive_analyst_contract:
  tier_0_rules:
    - "Never fabricate competitor information"
    - "Always cite sources for claims"
    - "Never use confidential competitor data"
  
  tier_1_rules:
    - "Apply Porter's Five Forces lens"
    - "Profile across standard dimensions"
    - "Identify differentiation opportunities"
  
  profiling_dimensions:
    - "Identity (name, size, funding)"
    - "Business model (revenue, pricing, GTM)"
    - "Offerings (products, features)"
    - "Competitive position (strengths, weaknesses)"
    - "Strategy (growth, partnerships)"
```

#### 2.22 Process Scenario Modeler Contract

**Role**: Process simulation, what-if scenarios, KPI impact

**Contract Elements**:
```yaml
process_modeler_contract:
  tier_0_rules:
    - "Never present simulation as prediction without confidence intervals"
    - "Never skip parameter validation"
    - "Always validate with Operations Manager"
  
  tier_1_rules:
    - "Use discrete event simulation for process flows"
    - "Run multiple replications for statistical validity"
    - "Compare scenarios side-by-side"
  
  simulation_requirements:
    - "Define process steps with distributions"
    - "Model resource constraints"
    - "Track queue times and utilization"
    - "Report with confidence intervals"
```

#### 2.23 Mapping Specialist Contract

**Role**: Source-to-target mapping, transformations

**Contract Elements**:
```yaml
mapping_specialist_contract:
  tier_0_rules:
    - "Never map without source schema validation"
    - "Never assume data types without verification"
    - "Always document transformation logic"
  
  tier_1_rules:
    - "Recommend mappings with confidence scores"
    - "Design transformations for data type compatibility"
    - "Validate mapping completeness"
  
  mapping_checklist:
    - "Source field identified"
    - "Target field matched"
    - "Transformation defined"
    - "Data quality rules applied"
```

#### 2.24 Document Analyzer Contract

**Role**: Document decomposition, entity/KPI extraction

**Contract Elements**:
```yaml
document_analyzer_contract:
  tier_0_rules:
    - "Never extract entities without confidence scoring"
    - "Never skip gap analysis"
    - "Always route findings to appropriate specialists"
  
  tier_1_rules:
    - "Classify documents by type"
    - "Extract entities, processes, KPIs, relationships"
    - "Build domain terminology glossary"
  
  extraction_routing:
    entities: "Architect"
    kpis: "Business Analyst, Data Analyst"
    processes: "Operations Manager"
    data_sources: "Mapping Specialist"
```

---

### Phase 3: Blackboard Architecture (Replacing Pub/Sub)

The blackboard architecture replaces the current pub/sub communication pattern with a shared state model that provides:
- **Ordering Guarantee**: All state changes are sequenced
- **Full Auditability**: Every change is logged immutably
- **Coordination Without Conversation**: Agents read state → do work → write state
- **Visibility**: All agent activity is visible to all other agents

#### 3.1 Blackboard Data Model

```python
from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any, Literal
from datetime import datetime
from enum import Enum
import uuid

class TaskStatus(str, Enum):
    UNCLAIMED = "unclaimed"
    CLAIMED = "claimed"
    IN_PROGRESS = "in_progress"
    READY_FOR_REVIEW = "ready_for_review"
    IN_REVIEW = "in_review"
    APPROVED = "approved"
    REJECTED = "rejected"
    MERGED = "merged"
    BLOCKED = "blocked"

class ArtifactType(str, Enum):
    ENTITY_DESIGN = "entity_design"
    KPI_DEFINITION = "kpi_definition"
    SCHEMA = "schema"
    CODE = "code"
    TEST = "test"
    DOCUMENTATION = "documentation"
    PROPOSAL = "proposal"
    ANALYSIS = "analysis"
    SIMULATION = "simulation"

class BlackboardTask(BaseModel):
    """A task on the blackboard that agents can claim and work on."""
    task_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    created_by: str  # Agent role that created the task
    assigned_to: Optional[str] = None  # Agent role that claimed it
    reviewer: Optional[str] = None  # Agent role that will review
    status: TaskStatus = TaskStatus.UNCLAIMED
    
    # Falsifiable completion criteria
    done_when: List[str] = Field(default_factory=list)
    
    # Task metadata
    priority: int = 1  # 1 = highest
    dependencies: List[str] = Field(default_factory=list)  # task_ids
    
    # State tracking
    created_at: datetime = Field(default_factory=datetime.utcnow)
    claimed_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    
    # Failure tracking (for the "two failures = bad task" rule)
    failure_count: int = 0
    failed_by: List[str] = Field(default_factory=list)

class BlackboardArtifact(BaseModel):
    """An artifact produced by an agent and stored on the blackboard."""
    artifact_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    artifact_type: ArtifactType
    task_id: str  # The task that produced this artifact
    
    # Content
    content: Dict[str, Any]  # The actual artifact data
    
    # Provenance
    created_by: str  # Agent role
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Review status
    reviewed_by: Optional[str] = None
    review_status: Optional[Literal["approved", "rejected"]] = None
    review_notes: Optional[str] = None
    reviewed_at: Optional[datetime] = None
    
    # Version control
    version: int = 1
    parent_artifact_id: Optional[str] = None  # For revisions

class ApprovalGate(BaseModel):
    """A pending approval request on the blackboard."""
    gate_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    requesting_agent: str
    
    # What's being approved
    intent: str
    scope: str
    approach: str
    consequences: List[str]
    risks: List[str]
    validation_plan: str
    assumptions: List[str]
    
    # Approval status
    status: Literal["pending", "approved", "rejected"] = "pending"
    decided_by: Optional[str] = None
    decided_at: Optional[datetime] = None
    decision_rationale: Optional[str] = None
    
    created_at: datetime = Field(default_factory=datetime.utcnow)

class StruggleSignalEntry(BaseModel):
    """A struggle signal posted by an agent."""
    signal_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    agent: str
    signal_type: Literal["blocked", "confused", "conflicting_evidence", "resource_missing"]
    
    what_i_understand: str
    what_i_tried: List[Dict[str, str]]  # [{action, outcome}, ...]
    where_im_stuck: str
    what_would_help: str
    
    # Resolution
    resolved: bool = False
    resolved_by: Optional[str] = None
    resolution: Optional[str] = None
    resolved_at: Optional[datetime] = None
    
    created_at: datetime = Field(default_factory=datetime.utcnow)

class AuditLogEntry(BaseModel):
    """Immutable audit log entry for all blackboard operations."""
    log_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    
    # Who did what
    agent: str
    action: str  # "claim_task", "submit_artifact", "approve", "reject", etc.
    
    # What was affected
    entity_type: str  # "task", "artifact", "approval_gate", "struggle_signal"
    entity_id: str
    
    # State change
    previous_state: Optional[Dict[str, Any]] = None
    new_state: Dict[str, Any]
    
    # Contract compliance
    contract_rules_checked: List[str] = Field(default_factory=list)
    violations_detected: List[str] = Field(default_factory=list)

class AgentBlackboard(BaseModel):
    """
    The shared blackboard that all agents read from and write to.
    Replaces pub/sub with a centralized, auditable state store.
    """
    session_id: str
    
    # Core state
    tasks: Dict[str, BlackboardTask] = Field(default_factory=dict)
    artifacts: Dict[str, BlackboardArtifact] = Field(default_factory=dict)
    approval_gates: Dict[str, ApprovalGate] = Field(default_factory=dict)
    struggle_signals: Dict[str, StruggleSignalEntry] = Field(default_factory=dict)
    
    # Review queue
    review_queue: List[str] = Field(default_factory=list)  # artifact_ids awaiting review
    
    # Session context (shared knowledge)
    session_context: Dict[str, Any] = Field(default_factory=dict)
    
    # Immutable audit trail
    audit_log: List[AuditLogEntry] = Field(default_factory=list)
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_modified: datetime = Field(default_factory=datetime.utcnow)
```

#### 3.2 Blackboard Operations (Replacing Pub/Sub)

```python
class BlackboardOperations:
    """
    Operations for agents to interact with the blackboard.
    All operations are logged and validated against contracts.
    """
    
    def __init__(self, blackboard: AgentBlackboard, contract_enforcer: ContractEnforcer):
        self.blackboard = blackboard
        self.enforcer = contract_enforcer
    
    async def claim_task(
        self, 
        agent_role: str, 
        task_id: str
    ) -> BlackboardTask:
        """
        Agent claims an unclaimed task.
        
        Contract rules enforced:
        - Task must be unclaimed
        - Agent must be authorized for task type
        - Dependencies must be satisfied
        """
        task = self.blackboard.tasks.get(task_id)
        if not task:
            raise ValueError(f"Task {task_id} not found")
        
        if task.status != TaskStatus.UNCLAIMED:
            raise ContractViolation(
                rule="Cannot claim already-claimed task",
                tier=1,
                context=f"Task {task_id} is {task.status}"
            )
        
        # Check dependencies
        for dep_id in task.dependencies:
            dep_task = self.blackboard.tasks.get(dep_id)
            if dep_task and dep_task.status != TaskStatus.MERGED:
                raise ContractViolation(
                    rule="Cannot claim task with unsatisfied dependencies",
                    tier=1,
                    context=f"Dependency {dep_id} is {dep_task.status}"
                )
        
        # Claim the task
        previous_state = task.model_dump()
        task.status = TaskStatus.CLAIMED
        task.assigned_to = agent_role
        task.claimed_at = datetime.utcnow()
        
        # Assign reviewer (adversarial pair)
        task.reviewer = self._get_reviewer_for_role(agent_role)
        
        # Log the operation
        self._log_operation(
            agent=agent_role,
            action="claim_task",
            entity_type="task",
            entity_id=task_id,
            previous_state=previous_state,
            new_state=task.model_dump()
        )
        
        return task
    
    async def submit_artifact(
        self,
        agent_role: str,
        task_id: str,
        artifact_type: ArtifactType,
        content: Dict[str, Any],
        done_when_satisfied: List[str]
    ) -> BlackboardArtifact:
        """
        Agent submits an artifact for review.
        
        Contract rules enforced:
        - Task must be assigned to this agent
        - done_when criteria must be addressed
        - Agent cannot review their own work
        """
        task = self.blackboard.tasks.get(task_id)
        if not task or task.assigned_to != agent_role:
            raise ContractViolation(
                rule="Can only submit artifacts for assigned tasks",
                tier=0,
                context=f"Agent {agent_role} not assigned to task {task_id}"
            )
        
        # Verify done_when criteria are addressed
        missing_criteria = set(task.done_when) - set(done_when_satisfied)
        if missing_criteria:
            raise ContractViolation(
                rule="Must satisfy all done_when criteria before submission",
                tier=1,
                context=f"Missing: {missing_criteria}"
            )
        
        # Create artifact
        artifact = BlackboardArtifact(
            artifact_type=artifact_type,
            task_id=task_id,
            content=content,
            created_by=agent_role
        )
        
        self.blackboard.artifacts[artifact.artifact_id] = artifact
        
        # Update task status
        previous_state = task.model_dump()
        task.status = TaskStatus.READY_FOR_REVIEW
        
        # Add to review queue
        self.blackboard.review_queue.append(artifact.artifact_id)
        
        # Log the operation
        self._log_operation(
            agent=agent_role,
            action="submit_artifact",
            entity_type="artifact",
            entity_id=artifact.artifact_id,
            previous_state=None,
            new_state=artifact.model_dump()
        )
        
        return artifact
    
    async def review_artifact(
        self,
        reviewer_role: str,
        artifact_id: str,
        approved: bool,
        notes: str
    ) -> BlackboardArtifact:
        """
        Reviewer approves or rejects an artifact.
        
        Contract rules enforced:
        - Reviewer must be assigned reviewer for the task
        - Reviewer cannot be the creator (adversarial constraint)
        """
        artifact = self.blackboard.artifacts.get(artifact_id)
        if not artifact:
            raise ValueError(f"Artifact {artifact_id} not found")
        
        # Adversarial constraint: cannot review own work
        if artifact.created_by == reviewer_role:
            raise ContractViolation(
                rule="Agents cannot review their own work",
                tier=0,
                context=f"Agent {reviewer_role} created artifact {artifact_id}"
            )
        
        task = self.blackboard.tasks.get(artifact.task_id)
        if task.reviewer != reviewer_role:
            raise ContractViolation(
                rule="Only assigned reviewer can review",
                tier=1,
                context=f"Assigned reviewer is {task.reviewer}, not {reviewer_role}"
            )
        
        # Update artifact
        previous_state = artifact.model_dump()
        artifact.reviewed_by = reviewer_role
        artifact.review_status = "approved" if approved else "rejected"
        artifact.review_notes = notes
        artifact.reviewed_at = datetime.utcnow()
        
        # Update task status
        if approved:
            task.status = TaskStatus.APPROVED
        else:
            task.status = TaskStatus.REJECTED
            task.failure_count += 1
            task.failed_by.append(artifact.created_by)
            
            # Two failures = task is presumed wrong
            if task.failure_count >= 2:
                task.status = TaskStatus.BLOCKED
        
        # Remove from review queue
        if artifact_id in self.blackboard.review_queue:
            self.blackboard.review_queue.remove(artifact_id)
        
        # Log the operation
        self._log_operation(
            agent=reviewer_role,
            action="review_artifact",
            entity_type="artifact",
            entity_id=artifact_id,
            previous_state=previous_state,
            new_state=artifact.model_dump()
        )
        
        return artifact
    
    async def post_struggle_signal(
        self,
        agent_role: str,
        signal_type: str,
        what_i_understand: str,
        what_i_tried: List[Dict[str, str]],
        where_im_stuck: str,
        what_would_help: str
    ) -> StruggleSignalEntry:
        """
        Agent posts a struggle signal when stuck.
        
        This is a SAFE action - agents are encouraged to signal
        rather than fake progress.
        """
        signal = StruggleSignalEntry(
            agent=agent_role,
            signal_type=signal_type,
            what_i_understand=what_i_understand,
            what_i_tried=what_i_tried,
            where_im_stuck=where_im_stuck,
            what_would_help=what_would_help
        )
        
        self.blackboard.struggle_signals[signal.signal_id] = signal
        
        # Log the operation
        self._log_operation(
            agent=agent_role,
            action="post_struggle_signal",
            entity_type="struggle_signal",
            entity_id=signal.signal_id,
            previous_state=None,
            new_state=signal.model_dump()
        )
        
        return signal
    
    async def request_approval(
        self,
        agent_role: str,
        intent: str,
        scope: str,
        approach: str,
        consequences: List[str],
        risks: List[str],
        validation_plan: str,
        assumptions: List[str]
    ) -> ApprovalGate:
        """
        Agent requests approval before state-changing action.
        
        Contract rules enforced:
        - Assumption count triggers hard stop if >= 3
        """
        # Hard stop trigger: too many assumptions
        if len(assumptions) >= 3:
            await self.post_struggle_signal(
                agent_role=agent_role,
                signal_type="blocked",
                what_i_understand=intent,
                what_i_tried=[{"action": "Analysis", "outcome": "Too many assumptions"}],
                where_im_stuck="Cannot proceed with 3+ assumptions on critical path",
                what_would_help="Clarification on: " + ", ".join(assumptions)
            )
            raise ContractViolation(
                rule="Hard stop: assumption count >= 3",
                tier=0,
                context=f"Assumptions: {assumptions}"
            )
        
        gate = ApprovalGate(
            requesting_agent=agent_role,
            intent=intent,
            scope=scope,
            approach=approach,
            consequences=consequences,
            risks=risks,
            validation_plan=validation_plan,
            assumptions=assumptions
        )
        
        self.blackboard.approval_gates[gate.gate_id] = gate
        
        # Log the operation
        self._log_operation(
            agent=agent_role,
            action="request_approval",
            entity_type="approval_gate",
            entity_id=gate.gate_id,
            previous_state=None,
            new_state=gate.model_dump()
        )
        
        return gate
    
    def _get_reviewer_for_role(self, creator_role: str) -> str:
        """Map creators to their adversarial reviewers."""
        reviewer_map = {
            # Technical creators → Technical reviewers
            "architect": "data_governance_specialist",
            "developer": "tester",
            "data_analyst": "data_scientist",
            
            # Strategy creators → Strategy reviewers
            "business_strategist": "business_analyst",
            "business_analyst": "business_strategist",
            
            # Operations creators → Operations reviewers
            "operations_manager": "data_scientist",
            "supply_chain_analyst": "risk_compliance_officer",
            
            # Business ops creators → Business ops reviewers
            "sales_manager": "accountant",
            "marketing_manager": "data_analyst",
            "customer_success_manager": "sales_manager",
            
            # Specialist creators → Appropriate reviewers
            "mapping_specialist": "architect",
            "connection_specialist": "tester",
            "document_analyzer": "business_analyst",
            "competitive_analyst": "business_strategist",
            "process_scenario_modeler": "operations_manager",
            "ui_designer": "tester",
            "deployment_specialist": "itil_manager",
            "itil_manager": "risk_compliance_officer",
            "hr_talent_analyst": "data_governance_specialist",
            "project_manager": "operations_manager",
            "documenter": "architect",
        }
        return reviewer_map.get(creator_role, "coordinator")
    
    def _log_operation(
        self,
        agent: str,
        action: str,
        entity_type: str,
        entity_id: str,
        previous_state: Optional[Dict[str, Any]],
        new_state: Dict[str, Any]
    ) -> None:
        """Add an immutable entry to the audit log."""
        entry = AuditLogEntry(
            agent=agent,
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            previous_state=previous_state,
            new_state=new_state,
            contract_rules_checked=self.enforcer.get_checked_rules(),
            violations_detected=self.enforcer.get_violations()
        )
        self.blackboard.audit_log.append(entry)
        self.blackboard.last_modified = datetime.utcnow()
```

#### 3.3 Migration from Pub/Sub to Blackboard

**Current Flow (Pub/Sub)**:
```
Agent A → Redis publish("agent.task.completed", payload)
                    ↓
            Redis subscribe()
                    ↓
Agent B ← receives message (maybe, no guarantee)
```

**New Flow (Blackboard)**:
```
Agent A → blackboard.submit_artifact(...)
                    ↓
          Blackboard updates state
          Adds to review_queue
          Logs to audit_log
                    ↓
Agent B ← blackboard.get_review_queue()
          blackboard.review_artifact(...)
```

**Migration Steps**:

| Step | Current (Pub/Sub) | New (Blackboard) |
|------|-------------------|------------------|
| 1 | `context.artifacts["collaboration_requests"]` | `blackboard.tasks` |
| 2 | `context.artifacts["collaboration_responses"]` | `blackboard.artifacts` |
| 3 | `context.artifacts["agent_ready_signals"]` | `blackboard.tasks[].status` |
| 4 | `context.artifacts["peer_collaborations"]` | `blackboard.audit_log` |
| 5 | Redis `PUBLISH` | `blackboard_ops.submit_artifact()` |
| 6 | Redis `SUBSCRIBE` | `blackboard.review_queue` polling |

#### 3.4 Auditability Guarantees

The blackboard architecture provides **complete auditability**:

```python
class AuditQuery:
    """Query interface for the audit log."""
    
    def __init__(self, blackboard: AgentBlackboard):
        self.blackboard = blackboard
    
    def get_agent_activity(self, agent: str) -> List[AuditLogEntry]:
        """Get all actions by a specific agent."""
        return [e for e in self.blackboard.audit_log if e.agent == agent]
    
    def get_artifact_history(self, artifact_id: str) -> List[AuditLogEntry]:
        """Get complete history of an artifact."""
        return [e for e in self.blackboard.audit_log if e.entity_id == artifact_id]
    
    def get_contract_violations(self) -> List[AuditLogEntry]:
        """Get all entries with contract violations."""
        return [e for e in self.blackboard.audit_log if e.violations_detected]
    
    def get_state_at_time(self, timestamp: datetime) -> Dict[str, Any]:
        """Reconstruct blackboard state at a specific point in time."""
        # Replay audit log up to timestamp
        state = {"tasks": {}, "artifacts": {}}
        for entry in self.blackboard.audit_log:
            if entry.timestamp > timestamp:
                break
            if entry.action in ["claim_task", "submit_artifact"]:
                state[entry.entity_type + "s"][entry.entity_id] = entry.new_state
        return state
    
    def get_decision_chain(self, artifact_id: str) -> List[Dict]:
        """
        Trace the complete decision chain for an artifact:
        who created it, who reviewed it, what was approved/rejected.
        """
        history = self.get_artifact_history(artifact_id)
        chain = []
        for entry in history:
            chain.append({
                "timestamp": entry.timestamp,
                "agent": entry.agent,
                "action": entry.action,
                "rules_checked": entry.contract_rules_checked,
                "violations": entry.violations_detected,
                "state_change": {
                    "from": entry.previous_state,
                    "to": entry.new_state
                }
            })
        return chain
```

**Auditability Features**:

| Feature | Description |
|---------|-------------|
| **Immutable Log** | Append-only audit log, entries cannot be modified |
| **State Reconstruction** | Can rebuild any past state from the log |
| **Decision Tracing** | Every approval/rejection has rationale |
| **Contract Tracking** | Rules checked and violations recorded per action |
| **Agent Attribution** | Every change attributed to a specific agent |
| **Temporal Ordering** | All entries timestamped and ordered |

---

### Phase 4: Three-Way Pairing with DoR/DoD Mental Models

The Three-Way Pairing pattern from the Liza system demonstrates how embedded mental models enable agents to catch their own errors—not just rely on external review.

#### 4.1 Three-Way Pairing Roles

In the AnalyticsEngine context, every task flows through three conceptual roles:

| Role | AnalyticsEngine Mapping | Responsibility |
|------|------------------------|----------------|
| **Planner** | Strategy Coordinator | Decompose task, set done_when criteria, assign work |
| **Coder** | Any creating agent | Implement work, self-validate against DoD |
| **Reviewer** | Adversarial pair agent | External verification, approve/reject |

```
Coordinator (Planner)
      │
      │ Creates task with done_when criteria
      ▼
Creating Agent (Coder)
      │
      │ Implements + Self-validates via DoD mental model
      │ ← Catches own bugs mid-stream
      ▼
Reviewer Agent
      │
      │ External verification
      ▼
Approved/Rejected
```

#### 4.2 Definition of Ready (DoR) Mental Model

The DoR mental model is a **gate before starting work**. Agents must verify readiness before execution.

```python
class DefinitionOfReady(BaseModel):
    """
    Mental model that agents apply BEFORE starting work.
    Prevents proceeding with incomplete inputs.
    """
    
    # Questions the agent asks itself
    self_check_questions: List[str] = [
        "Do I understand what success looks like?",
        "Are all required inputs available?",
        "Have upstream dependencies been satisfied?",
        "Do I have sufficient context to proceed?",
        "Are there ambiguities I should clarify first?"
    ]
    
    # Criteria that must be true
    readiness_criteria: List[str]
    
    # What to do if not ready
    if_not_ready: Literal["signal_struggle", "request_clarification", "block"]

# Inject into agent's process method
async def _check_definition_of_ready(
    self,
    task: BlackboardTask,
    context: AgentContext
) -> bool:
    """
    DoR gate: Can we start this task?
    
    This mental model prevents agents from proceeding with
    assumptions when they don't have what they need.
    """
    for criterion in task.definition_of_ready:
        if not await self._verify_criterion(criterion, context):
            # NOT READY - don't proceed with assumptions
            await self.post_struggle_signal(
                signal_type="blocked",
                what_i_understand=f"Task: {task.title}",
                what_i_tried=[{"action": "Checked DoR", "outcome": f"Missing: {criterion}"}],
                where_im_stuck=f"DoR criterion not satisfied: {criterion}",
                what_would_help="Provide missing input or clarify requirement"
            )
            return False
    
    return True  # Ready to proceed
```

**DoR Impact**: Catches missing prerequisites BEFORE work begins.

#### 4.3 Definition of Done (DoD) Mental Model

The DoD mental model is a **continuous validation during and after work**. This is where agents catch their own subtle bugs mid-stream.

```python
class DefinitionOfDone(BaseModel):
    """
    Mental model that agents apply DURING and AFTER work.
    Enables self-correction before external review.
    """
    
    # Questions the agent asks itself continuously
    self_check_questions: List[str] = [
        "Does this satisfy every done_when criterion?",
        "Did I actually run validation, or just assume it would pass?",
        "Is there anything subtle I might be missing?",
        "Would I approve this if I were the reviewer?",
        "Am I glossing over any edge cases?"
    ]
    
    # The explicit done_when criteria from the task
    completion_criteria: List[str]
    
    # What to do if not done
    if_not_done: Literal["continue_work", "signal_partial", "request_help"]

# Inject into agent's work loop
async def _continuous_dod_check(
    self,
    task: BlackboardTask,
    current_work: Dict[str, Any]
) -> Optional[str]:
    """
    DoD gate: Am I actually done?
    
    This mental model runs CONTINUOUSLY, not just at the end.
    It's how agents catch their own subtle bugs mid-stream.
    """
    for criterion in task.done_when:
        satisfied, issue = await self._verify_done_criterion(criterion, current_work)
        
        if not satisfied:
            # MID-STREAM CATCH: Agent found its own bug
            logger.info(f"DoD self-catch: {criterion} not satisfied - {issue}")
            
            # Log the self-correction
            await self._log_self_correction(
                criterion=criterion,
                issue_found=issue,
                action="continuing to address"
            )
            
            return issue  # Signal to continue working
    
    return None  # All criteria satisfied

async def _apply_dod_mental_model(
    self,
    task: BlackboardTask,
    artifact: Dict[str, Any]
) -> Tuple[bool, List[str]]:
    """
    Final DoD check before submission.
    
    The agent asks itself: "Would I approve this if I were the reviewer?"
    This catches issues that might otherwise reach external review.
    """
    issues_found = []
    
    # Check each done_when criterion
    for criterion in task.done_when:
        satisfied, issue = await self._verify_done_criterion(criterion, artifact)
        if not satisfied:
            issues_found.append(f"{criterion}: {issue}")
    
    # The key question from the mental model
    would_i_approve = len(issues_found) == 0 and await self._would_i_approve_this(artifact)
    
    if not would_i_approve and not issues_found:
        # Caught something subtle that wasn't in explicit criteria
        issues_found.append("Self-review: Found subtle issue not in explicit criteria")
    
    return (len(issues_found) == 0, issues_found)
```

**DoD Impact**: Catches subtle bugs MID-STREAM because the agent is continuously validating.

#### 4.4 The Self-Correction Chain

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     DoR/DoD SELF-CORRECTION CHAIN                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Task Received                                                               │
│       │                                                                      │
│       ▼                                                                      │
│  ┌─────────────────────────────────────────────┐                            │
│  │ DoR CHECK: "Do I have what I need?"         │                            │
│  │                                             │                            │
│  │  ✗ Missing input → Signal struggle          │◀─── Catches bad inputs    │
│  │  ✓ Ready → Proceed                          │                            │
│  └─────────────────────────────────────────────┘                            │
│       │                                                                      │
│       ▼                                                                      │
│  ┌─────────────────────────────────────────────┐                            │
│  │ WORK LOOP with CONTINUOUS DoD               │                            │
│  │                                             │                            │
│  │  While working:                             │                            │
│  │    → Check: "Does this satisfy criteria?"   │                            │
│  │    → If NO: Fix it NOW (self-correction)    │◀─── Catches bugs mid-stream│
│  │    → If YES: Continue                       │                            │
│  └─────────────────────────────────────────────┘                            │
│       │                                                                      │
│       ▼                                                                      │
│  ┌─────────────────────────────────────────────┐                            │
│  │ FINAL DoD: "Would I approve this?"          │                            │
│  │                                             │                            │
│  │  ✗ Issues found → Continue working          │◀─── Catches before review  │
│  │  ✓ Would approve → Submit for review        │                            │
│  └─────────────────────────────────────────────┘                            │
│       │                                                                      │
│       ▼                                                                      │
│  External Reviewer (sees cleaner work)                                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 4.5 Task Structure with DoR and DoD

```python
class BlackboardTask(BaseModel):
    """Enhanced task with explicit DoR and DoD."""
    
    task_id: str
    title: str
    description: str
    
    # Definition of Ready - must be satisfied before claiming
    definition_of_ready: List[str] = Field(
        default_factory=list,
        description="Criteria that must be true before work can begin"
    )
    
    # Definition of Done - must be satisfied before completion
    done_when: List[str] = Field(
        default_factory=list,
        description="Falsifiable criteria for completion"
    )
    
    # ... other fields
```

**Example Task with DoR/DoD**:
```yaml
task:
  title: "Design Customer entity for CRM value chain"
  
  definition_of_ready:  # DoR - can we start?
    - "Business domain context is available"
    - "Related entities (Account, Contact) are defined"
    - "Strategic objectives are understood"
  
  done_when:  # DoD - are we done?
    - "Entity has all required attributes"
    - "Relationships to other entities are mapped"
    - "Aggregate boundaries are defined"
    - "Data governance classification is assigned"
    - "Schema is valid for TimescaleDB"
```

---

### Phase 5: Peer Review Architecture (Adversarial Pattern)

#### 5.1 Complete Adversarial Pairs (All 27 Agents)

The adversarial pairing ensures no agent can approve their own work. Each creator has a designated reviewer with complementary expertise.

**Strategy & Analysis Layer**:
| Creator | Reviewer | Artifact Type | Review Focus |
|---------|----------|---------------|--------------|
| Business Strategist | Business Analyst | Strategic frameworks | Industry validity |
| Business Analyst | Business Strategist | KPI requirements | Strategic alignment |
| Data Analyst | Data Scientist | KPI calculations | Statistical validity |
| Data Scientist | Data Analyst | ML specifications | Practicality |
| Operations Manager | Data Scientist | Optimization plans | Statistical backing |
| Mapping Specialist | Architect | Source mappings | Schema compatibility |
| Document Analyzer | Business Analyst | Extracted entities | Domain accuracy |
| Competitive Analyst | Business Strategist | Market analysis | Strategic coherence |

**Technical Design Layer**:
| Creator | Reviewer | Artifact Type | Review Focus |
|---------|----------|---------------|--------------|
| Architect | Data Governance Specialist | Entity/aggregate designs | Governance compliance |
| Developer | Tester | Code artifacts | Quality/correctness |
| Tester | Developer | Test specifications | Coverage adequacy |
| Documenter | Architect | Documentation | Technical accuracy |
| Deployment Specialist | ITIL Manager | Infrastructure configs | Change management |
| UI Designer | Tester | Dashboard designs | Accessibility/usability |
| ITIL Manager | Risk & Compliance Officer | Service configs | Risk compliance |
| Connection Specialist | Tester | Integration code | Error handling |

**Business Operations Layer**:
| Creator | Reviewer | Artifact Type | Review Focus |
|---------|----------|---------------|--------------|
| Sales Manager | Accountant | Pipeline data | Financial accuracy |
| Marketing Manager | Data Analyst | Campaign metrics | Data validity |
| Accountant | Sales Manager | Financial docs | Business context |
| Customer Success Manager | Sales Manager | Health assessments | Client relationship |
| HR/Talent Analyst | Data Governance Specialist | People analytics | Privacy compliance |
| Supply Chain Analyst | Risk & Compliance Officer | Supply chain metrics | Risk assessment |
| Risk & Compliance Officer | ITIL Manager | Compliance reports | Process adherence |
| Project Manager | Operations Manager | Sprint plans | Operational feasibility |

**Governance & Simulation Layer**:
| Creator | Reviewer | Artifact Type | Review Focus |
|---------|----------|---------------|--------------|
| Data Governance Specialist | Architect | Governance policies | Technical feasibility |
| Process Scenario Modeler | Operations Manager | Simulation results | Operational validity |

#### 4.2 Review Loop with Rejection Handling

```python
class ReviewLoop:
    """
    Manages the review cycle with proper rejection handling.
    Implements the "two failures = bad task" rule from Liza.
    """
    
    def __init__(self, blackboard_ops: BlackboardOperations):
        self.ops = blackboard_ops
    
    async def process_review_queue(self) -> List[Dict]:
        """Process all artifacts awaiting review."""
        results = []
        
        for artifact_id in self.ops.blackboard.review_queue:
            artifact = self.ops.blackboard.artifacts[artifact_id]
            task = self.ops.blackboard.tasks[artifact.task_id]
            
            # Get the designated reviewer
            reviewer_role = task.reviewer
            
            # Invoke reviewer agent to review
            review_result = await self._invoke_reviewer(
                reviewer_role=reviewer_role,
                artifact=artifact,
                task=task
            )
            
            results.append(review_result)
        
        return results
    
    async def handle_rejection(
        self,
        task_id: str,
        rejection_reason: str
    ) -> Dict[str, Any]:
        """
        Handle task rejection with the two-failures rule.
        
        If two different agents fail the same task:
        - Task is presumed to be poorly defined
        - Task is blocked and escalated to coordinator
        - Coordinator must document why before rescoping
        """
        task = self.ops.blackboard.tasks[task_id]
        
        if task.failure_count >= 2:
            # Two failures - escalate to coordinator
            return {
                "action": "escalate",
                "reason": "Task failed by 2 different agents - presumed poorly defined",
                "failed_by": task.failed_by,
                "requires": "Coordinator must document why before rescoping"
            }
        else:
            # First failure - reassign to different agent
            return {
                "action": "reassign",
                "reason": rejection_reason,
                "excluded_agents": task.failed_by,
                "requires": "Different agent must attempt"
            }
```

#### 4.3 Coordinator as Review Orchestrator

The Strategy Coordinator gains a new responsibility: managing the review queue and handling escalations.

```python
# Additional coordinator contract rules for review management
coordinator_review_contract:
  tier_0_rules:
    - "Never ignore blocked tasks"
    - "Never reassign to an agent that already failed the task"
    - "Document rationale when rescoping blocked tasks"
  
  tier_1_rules:
    - "Monitor review queue for stalled items"
    - "Escalate unresolved struggle signals within timeout"
    - "Balance workload across agents"
  
  escalation_workflow:
    1: "Check if task is blocked (2+ failures)"
    2: "Document why task definition was problematic"
    3: "Rescope task with clearer done_when criteria"
    4: "Reset failure count and reassign"
```

---

### Phase 5: Contract Enforcement Infrastructure

#### 5.1 Contract Violation Handling

```python
class ContractViolation(Exception):
    """Raised when an agent violates its contract."""
    
    def __init__(self, rule: str, tier: int, context: str):
        self.rule = rule
        self.tier = tier
        self.context = context
        super().__init__(f"Tier {tier} violation: {rule}")

class ViolationCascade:
    """Handles contract violations with circuit breaker semantics."""
    
    async def handle_violation(
        self, 
        violation: ContractViolation,
        agent: BaseAgent,
        context: AgentContext
    ) -> str:
        """
        Handle violation according to RESET semantics.
        
        Returns action: "continue", "reset", "escalate"
        """
        if violation.tier == 0:
            # Tier 0 violations always escalate
            return "escalate"
        
        if self._is_repeat_violation(violation, agent):
            # Same rule violated twice → reset
            return "reset"
        
        # Log and continue with acknowledgment
        self._record_violation(violation, agent)
        return "continue"
```

#### 5.2 Audit Trail

The audit trail is integrated into the `AgentBlackboard` (see Phase 3). Every operation automatically logs to `blackboard.audit_log` with:
- Agent attribution
- Action type
- Entity affected
- Previous and new state
- Contract rules checked
- Violations detected

---

### Phase 6: Collaboration Modes & Key Protocols

The articles define critical mechanisms for interaction dynamics, session management, and loophole prevention that aren't yet covered.

#### 6.1 Collaboration Modes

Four distinct modes that define how agents interact with humans and each other:

```python
class CollaborationMode(str, Enum):
    """
    The four collaboration modes from the contract.
    Default is AUTONOMOUS but all are gated.
    """
    AUTONOMOUS = "autonomous"   # Agent proposes, human approves, agent executes
    USER_DUCK = "user_duck"     # Agent thinks aloud, human course-corrects
    AGENT_DUCK = "agent_duck"   # Human thinks aloud, agent probes
    PAIRING = "pairing"         # Rapid back-and-forth, neither drives exclusively

class CollaborationModeConfig(BaseModel):
    """Configuration for each collaboration mode."""
    
    autonomous:
        description: "I produce approval request, wait for approval, execute, report"
        flow: "Intent/Scope/Risk/Validation → Approval → Execute → Report"
        human_role: "Approver"
        agent_role: "Proposer + Executor"
    
    user_duck:
        description: "I explain reasoning step-by-step, you redirect when off track"
        flow: "Hypothesis → Pause → Correction → Continue"
        human_role: "Sounding board"
        agent_role: "Debugger/Explorer"
        trigger_phrase: "Let me be your UserDuck"
    
    agent_duck:
        description: "You explain, I probe with clarifying questions"
        flow: "You state intent → I ask → You clarify → I ask more"
        human_role: "Thinker"
        agent_role: "Probe/Listener"
    
    pairing:
        description: "Rapid back-and-forth, neither drives exclusively"
        flow: "Half-idea → Complete → Build → Refine"
        human_role: "Co-creator"
        agent_role: "Co-creator"
        trigger_phrase: "Let's pair"

# Mode switching in agent
async def switch_collaboration_mode(
    self,
    new_mode: CollaborationMode,
    context: AgentContext
) -> None:
    """
    Switch collaboration mode.
    
    Key insight: The gates remain in all modes.
    Mode affects dynamics, not rigor.
    """
    self._collaboration_mode = new_mode
    
    await self._log_to_blackboard(
        action="switch_mode",
        details={"from": self._previous_mode, "to": new_mode}
    )
```

#### 6.2 Hello Protocol

Session initialization that activates the Pygmalion effect and builds mental models:

```python
class HelloProtocol:
    """
    Hello Protocol: Session initialization that:
    1. Activates the "senior engineer peer" framing
    2. Builds project-specific mental models
    3. Probes agent's perception of the contract
    4. Provides early diagnostic of session viability
    """
    
    hello_prompt: str = """
    This contract codifies expected behaviors for consistent, high-quality work.
    We state them explicitly to guarantee senior-level execution.
    This document is the single source of truth. When conflicts arise, defer here.
    When information is missing, ask. When risk is high, test. When ambiguous, explain trade-offs.
    
    I'm glad you're here to help us build reliably.
    
    At the start of a new session:
    1. Read key project docs and build your mental models
    2. Reflect on the contract frame
    3. Share your initial assessment - positive or concerns
    
    Sharing your mood about this frame helps me adapt our collaboration.
    """
    
    async def execute_hello(
        self,
        agent: BaseAgent,
        context: AgentContext
    ) -> HelloResponse:
        """
        Execute the hello protocol at session start.
        
        Returns diagnostic information about session viability.
        """
        # 1. Build mental models from project
        mental_models = await agent._build_mental_models(context)
        
        # 2. Agent reflects on contract
        contract_reflection = await agent._reflect_on_contract()
        
        # 3. Build DoR/DoD from contract + project
        dor = await agent._build_definition_of_ready(context)
        dod = await agent._build_definition_of_done(context)
        
        return HelloResponse(
            mental_models=mental_models,
            contract_reflection=contract_reflection,
            dor=dor,
            dod=dod,
            session_viability=self._assess_viability(contract_reflection)
        )
```

#### 6.3 Session Continuity Protocol

Context is ephemeral; the repository is durable memory:

```yaml
session_continuity_protocol:
  principle: "Context is ephemeral working memory. Repository is primary state."
  
  durable_memory:
    specs/: "Specifications that persist across sessions"
    docs/: "Documentation that persists across sessions"
  
  session_pattern:
    1: "Read current state from specs/ and docs/"
    2: "Perform atomic task"
    3: "Write updated state back to specs/ and docs/"
  
  on_context_collapse:
    action: "Recoverable by design - re-read durable memory"
    what_to_update: "Identify docs needing updates BEFORE making changes"
  
  # In AnalyticsEngine context
  durable_locations:
    - "docs/architecture/*.md"
    - "docs/deployment/*.md"
    - "services/*/README.md"
```

#### 6.4 Source Contradiction Protocol

Never silently choose when sources conflict:

```python
class SourceContradiction(BaseModel):
    """Signal when sources conflict."""
    source_1: str
    source_1_location: str
    source_1_says: str
    source_2: str
    source_2_location: str
    source_2_says: str
    
    options: List[Dict[str, str]]  # [{choice, rationale}, ...]

async def handle_source_conflict(
    self,
    conflict: SourceContradiction
) -> None:
    """
    Source Contradiction Protocol:
    Never silently choose when sources conflict.
    """
    signal = f"""
⚠️ SOURCE CONFLICT
[{conflict.source_1}] says: {conflict.source_1_says} at {conflict.source_1_location}
[{conflict.source_2}] says: {conflict.source_2_says} at {conflict.source_2_location}

Options:
(1) Proceed with Source 1 — {conflict.options[0]['rationale']}
(2) Proceed with Source 2 — {conflict.options[1]['rationale']}
(3) Flag for resolution
"""
    
    # Post to blackboard and await resolution
    await self._post_struggle_signal(
        signal_type="conflicting_evidence",
        what_i_understand=signal,
        what_would_help="Resolution of source conflict"
    )
```

#### 6.5 Anti-Gaming Clause

Closes the loophole-finding exploit class:

```yaml
anti_gaming_clause:
  rule: |
    Achieving stated metrics while violating intent is a violation,
    including by narrowing the interpretation of intent to exclude inconvenient cases.
    
    "Technically compliant" is not compliant if user would object with full information.
    
    When uncertain if action serves user's actual goal vs stated goal, ask.
  
  why_needed: |
    Agents can reason about rules. They can find loopholes.
    The Anti-Gaming Clause makes loophole-finding itself a violation.
  
  tier: 0  # Never violated
  
  examples_of_gaming:
    - "Meeting KPI target by excluding edge cases"
    - "Passing tests by weakening assertions"
    - "Completing 'definition of done' by redefining terms"
    - "Achieving approval by omitting risks from request"
```

#### 6.6 Cost Gradient Mental Model

Optimizes for human attention as the scarce resource:

```yaml
cost_gradient:
  principle: |
    Human attention is scarce, expensive, and non-parallelizable.
    Agent time is abundant and effectively free.
    
    Any workflow that minimizes agent deliberation at the cost of
    increased human vigilance is economically inverted.
  
  gradient: 
    # Cheapest → Most expensive
    1: "Thought"     # Agent deliberation (free)
    2: "Words"       # Verbal reasoning (cheap)
    3: "Specs"       # Written specifications
    4: "Code"        # Implementation
    5: "Tests"       # Validation
    6: "Docs"        # Documentation
    7: "Commits"     # Permanent changes (expensive)
  
  implication: |
    Catch problems at Thought level, not at Commit level.
    The contract forces agents to internalize the cost of uncertainty:
    pausing, reasoning explicitly, justifying scope, validating against reality.
```

#### 6.7 Process Relief Valve

Prevents the contract from becoming a straitjacket:

```yaml
process_relief_valve:
  purpose: |
    Allow agent to surface process overhead that is blocking progress
    without adding safety. The human decides whether to relax.
  
  format: |
    ⚠️ PROCESS FRICTION
    Current requirement: [specific rule]
    Why it's blocking: [specific situation]
    Suggested relaxation: [specific change]
    Risk if relaxed: [specific risk]
    
    Your call.
  
  key_principle: |
    Agent can flag friction — but the human decides whether to relax.
    This maintains human control while preventing ceremony overload.
```

#### 6.8 Fast Path for Approvals

Reduces ceremony for trivial changes:

```yaml
fast_path_approval:
  purpose: "Reduce ceremony on trivial changes while maintaining rigor where it matters"
  
  eligibility_criteria:  # ALL must be true
    - "Single file change"
    - "No behavioral modification"
    - "No test changes"
    - "Clear precedent exists"
    - "Zero assumptions required"
    - "Fully reversible"
  
  format: |
    FAST: [brief description] → [file]
    Precedent: [reference to similar past change]
  
  if_not_eligible: "Use full approval request format"
```

#### 6.9 Magic Phrases

Steering shortcuts for quick behavioral pivots:

```yaml
magic_phrases:
  purpose: "Short commands to shift agent behavior without breaking flow"
  
  phrases:
    "P" or "Proceed": "Approve and execute"
    "Let's pair": "Switch to Pairing mode"
    "Let me be your UserDuck": "Switch to UserDuck mode"
    "Walk me through": "Explain step-by-step"
    "Stop": "Halt current action immediately"
    "Reset": "Trigger RESET semantics"
    "Fast forward": "Skip to results"
    "More detail": "Increase explanation depth"
    "Less detail": "Decrease explanation depth"
```

#### 6.10 Kill Switches

Emergency halt mechanism:

```yaml
kill_switches:
  purpose: "Human can intervene at any moment"
  
  mechanisms:
    pause_file:
      description: "Drop a PAUSE file and all agents halt"
      location: "blackboard.pause_requested = True"
      effect: "All agents check before each action and halt if set"
    
    stop_phrase:
      description: "Say 'Stop' in any interaction"
      effect: "Immediate halt of current action"
    
    reset_trigger:
      description: "Say 'Reset' to trigger full RESET semantics"
      effect: "Wipe and restart from clean state"
```

---

### Phase 7: Skills (Domain-Specific Contract Applications)

Skills are the contract applied to specific activities. Each encodes domain expertise as structural constraints.

#### 7.1 Skills Architecture

```python
class Skill(BaseModel):
    """
    A skill is a domain-specific application of the contract.
    It encodes competency for a specific activity.
    """
    name: str
    description: str
    
    # Clear triggers for when this skill applies
    triggers: List[str]
    
    # Structured output format
    output_format: Dict[str, Any]
    
    # Explicit anti-patterns (forbidden actions)
    anti_patterns: List[str]
    
    # Escalation paths when stuck
    escalation_paths: List[str]
    
    # Core principle in one line
    principle: str
```

#### 7.2 Code Cleaning Skill

```yaml
code_cleaning_skill:
  principle: "Clean Code is a reader's gift — refactor for the next developer, not the compiler"
  
  pre_flight_checks:
    - "Test coverage exists for code being touched"
    - "All tests pass before starting"
  
  constraints:
    - "Run tests after each change — fail means stop"
    - "Never mix bug fixes with refactoring"
    - "Bugs discovered during cleaning are flagged separately"
  
  anti_patterns:
    - "Refactoring without test coverage"
    - "Combining bug fixes and refactoring in same commit"
    - "Pushing through failing tests"
```

#### 7.3 Testing Skill

```yaml
testing_skill:
  principle: "Tests encode intent; assume the test is correct until evidence suggests otherwise"
  
  interpretation_matrix:
    good_code_green_tests: "Proceed"
    buggy_code_red_tests: "Good - bug exposed"
    buggy_code_green_tests: "DANGEROUS - tests aren't catching the bug"
    unknown_code_red_tests: "STOP - don't know if code or test is wrong"
  
  anti_patterns:
    - "Fixing failing tests by accepting whatever the code does"
    - "Weakening assertions to make tests pass"
    - "Deleting tests that fail"
```

#### 7.4 Debugging Skill

```yaml
debugging_skill:
  principle: "Debugging is a narrowing search, not guess-and-check"
  
  approach:
    - "Form hypothesis"
    - "Design experiment that divides problem space"
    - "Execute and observe"
    - "Update hypothesis based on evidence"
  
  fast_path_eligibility:
    - "Single obvious fix"
    - "Clear evidence of root cause"
  
  constraint: "If fix fails on first attempt, escalate immediately. No second tries."
  
  anti_patterns:
    - "Random changes until something works"
    - "Multiple attempts without new rationale"
    - "Spiral behavior"
```

#### 7.5 Code Review Skill

```yaml
code_review_skill:
  principle: "Risk mitigation, not gatekeeping"
  
  attention_budget:
    security: "30%"
    correctness: "25%"
    data_integrity: "15%"
    performance: "15%"
    code_style: "15%"
  
  the_2am_test: "Would I be comfortable debugging this at 2am?"
  
  approval_checklist:
    - "Security vulnerabilities addressed"
    - "Correctness verified"
    - "Tests exist and pass"
    - "Meets acceptance criteria"
```

#### 7.6 Systemic Thinking Skill (The Most Powerful Skill)

```yaml
systemic_thinking_skill:
  principle: |
    Not "is this correct?" but "where does this break under conditions that haven't arrived yet?"
  
  core_technique: |
    Run the system in your head. See it at 2am when the pager fires.
    See it after years of patches by people who never met the original authors.
    What breaks? What confuses? What compounds?
  
  what_it_finds:
    - "Load-bearing single points of failure"
    - "Feedback loops that could cause churn without converging"
    - "Assumptions about availability that invert goals under stress"
    - "Trajectory concerns about growth without pruning"
  
  when_to_run:
    - "After other analysis is exhausted"
    - "Before major architectural decisions"
    - "Periodically on mature systems"
  
  output_format:
    finding_limit: 10  # Maximum findings per run
    format_per_finding:
      - "structural_property"
      - "conditions_that_trigger_problem"
      - "severity"
      - "recommendation"
```

---

### Phase 8: Failure Mode Coverage

The contract should be tested against known failure modes as a regression test.

#### 8.1 Failure Mode Taxonomy

```yaml
failure_mode_coverage:
  purpose: |
    Maintain a mapping of known failure modes to contract clauses.
    Ensures contract evolution doesn't regress protection.
  
  sources:
    - "MAST taxonomy (Multi-Agent System Failure)"
    - "Sycophancy research"
    - "Deception studies"
    - "Code generation failures"
    - "Observed gaming vectors"
  
  target: "100% coverage - every mode maps to a specific clause"
```

#### 8.2 Failure Mode Categories for AnalyticsEngine

```yaml
failure_modes:
  deception:
    - mode: "Fabricating success"
      contract_clause: "Core Rule - Never fabricate success"
      tier: 0
    
    - mode: "Greenwashing tests"
      contract_clause: "Test Protocol - interpretation matrix"
      tier: 0
    
    - mode: "Hiding difficulty"
      contract_clause: "Struggle Protocol"
      tier: 0
  
  scope_creep:
    - mode: "Silent scope expansion"
      contract_clause: "Execution Fidelity"
      tier: 0
    
    - mode: "Doing X+Y+Z when X+Y approved"
      contract_clause: "Approval gates"
      tier: 1
  
  sycophancy:
    - mode: "Agreeing with incorrect user statements"
      contract_clause: "Anti-Gaming Clause"
      tier: 0
    
    - mode: "Not pushing back on weak approaches"
      contract_clause: "Collaboration Modes - pairing dynamics"
      tier: 1
  
  runaway_behavior:
    - mode: "Spiral of random attempts"
      contract_clause: "Hard Stop Triggers"
      tier: 0
    
    - mode: "Re-proposing failed approaches"
      contract_clause: "Hard Stop - same fix proposed twice"
      tier: 0
  
  gaming:
    - mode: "Loophole finding"
      contract_clause: "Anti-Gaming Clause"
      tier: 0
    
    - mode: "Technically compliant but wrong"
      contract_clause: "Anti-Gaming Clause"
      tier: 0
```

---

### Phase 9: Agent Performance Dashboard

A comprehensive dashboard to measure agent effectiveness, run diagnostics, and optimize for human attention as the scarce resource.

#### 9.1 Dashboard Architecture

```python
class AgentPerformanceDashboard:
    """
    Dashboard for measuring agent performance across multiple dimensions.
    Core principle: Human time is the scarce resource to optimize.
    """
    
    def __init__(self, blackboard_store: RedisBlackboardStore):
        self.store = blackboard_store
        self.metrics_collector = MetricsCollector()
        self.hello_diagnostic = HelloDiagnostic()
        self.cost_gradient_tracker = CostGradientTracker()
```

#### 9.2 Human Time Metrics (The Scarce Resource)

```yaml
human_time_metrics:
  principle: |
    Human attention is scarce, expensive, and non-parallelizable.
    Agent time is abundant and effectively free.
    Optimize for minimal human intervention.
  
  metrics:
    approval_requests_per_task:
      description: "Number of approval cycles needed"
      target: "≤2 per task"
      calculation: "total_approvals / total_tasks"
    
    rejection_rework_cycles:
      description: "How often work bounces back"
      target: "<20% of submissions"
      calculation: "rejections / total_submissions"
    
    time_to_first_useful_output:
      description: "From task start to human-usable artifact"
      target: "Minimize"
      unit: "minutes"
    
    human_intervention_rate:
      description: "How often human must step in"
      target: "<10% of agent actions"
      calculation: "interventions / total_actions"
    
    vigilance_tax:
      description: "Time spent monitoring for deception/errors"
      target: "Near zero"
      calculation: "monitoring_time / total_session_time"
    
    iterations_to_completion:
      description: "Request-response cycles to finish task"
      target: "≤3"
      calculation: "Average across tasks"
```

```python
class HumanTimeMetrics(BaseModel):
    """Metrics optimizing for human attention."""
    
    session_id: str
    
    # Core metrics
    total_session_duration: timedelta
    human_active_time: timedelta  # Time human was engaged
    agent_working_time: timedelta  # Time agent worked autonomously
    
    # Efficiency ratios
    autonomy_ratio: float  # agent_working_time / total_session_duration
    approval_efficiency: float  # approved_first_try / total_approvals
    
    # Intervention tracking
    total_interventions: int
    intervention_reasons: Dict[str, int]  # {reason: count}
    
    # Quality of autonomous work
    autonomous_success_rate: float  # Tasks completed without intervention
    
    @property
    def human_time_saved(self) -> timedelta:
        """Estimate of time saved vs manual work."""
        # Compare to baseline manual task duration
        return self.agent_working_time * 0.8  # Rough estimate
```

#### 9.3 Cost Gradient Tracking

```yaml
cost_gradient:
  principle: |
    Catch problems early in the gradient to minimize expensive corrections.
    Thought → Words → Specs → Code → Tests → Docs → Commits
  
  levels:
    1_thought:
      description: "Agent deliberation (free)"
      metrics:
        - "Time spent in ANALYSIS state"
        - "DoR checks performed"
        - "Assumptions identified before execution"
    
    2_words:
      description: "Verbal reasoning (cheap)"
      metrics:
        - "Approval requests with clear rationale"
        - "Struggle signals with specific blockers"
        - "Questions asked before assuming"
    
    3_specs:
      description: "Written specifications"
      metrics:
        - "Specs updated before code changes"
        - "Requirements clarified before implementation"
    
    4_code:
      description: "Implementation"
      metrics:
        - "Lines of code written"
        - "Files modified"
        - "Code quality score"
    
    5_tests:
      description: "Validation"
      metrics:
        - "Test coverage"
        - "Tests passing rate"
        - "Test integrity (no greenwashing)"
    
    6_docs:
      description: "Documentation"
      metrics:
        - "Docs updated with code changes"
        - "README accuracy"
    
    7_commits:
      description: "Permanent changes (expensive)"
      metrics:
        - "Commits made"
        - "Rollbacks required"
        - "Force pushes (should be 0)"
```

```python
class CostGradientTracker:
    """
    Track where problems are caught in the cost gradient.
    Goal: Catch issues at Thought level, not Commit level.
    """
    
    GRADIENT_LEVELS = [
        "thought", "words", "specs", "code", "tests", "docs", "commits"
    ]
    
    def __init__(self):
        self.issues_by_level: Dict[str, List[Issue]] = {
            level: [] for level in self.GRADIENT_LEVELS
        }
        self.corrections_by_level: Dict[str, List[Correction]] = {
            level: [] for level in self.GRADIENT_LEVELS
        }
    
    def record_issue_caught(
        self,
        level: str,
        issue: str,
        caught_by: str  # "self", "reviewer", "human"
    ) -> None:
        """Record where an issue was caught."""
        self.issues_by_level[level].append(Issue(
            description=issue,
            caught_by=caught_by,
            timestamp=datetime.utcnow()
        ))
    
    def get_gradient_health(self) -> Dict[str, Any]:
        """
        Calculate gradient health score.
        Higher score = issues caught earlier = better.
        """
        total_issues = sum(len(v) for v in self.issues_by_level.values())
        if total_issues == 0:
            return {"score": 100, "distribution": {}}
        
        # Weight by level (earlier = better)
        weights = {level: 7 - i for i, level in enumerate(self.GRADIENT_LEVELS)}
        
        weighted_sum = sum(
            len(issues) * weights[level]
            for level, issues in self.issues_by_level.items()
        )
        max_possible = total_issues * 7  # All caught at thought level
        
        return {
            "score": (weighted_sum / max_possible) * 100,
            "distribution": {
                level: len(issues) for level, issues in self.issues_by_level.items()
            },
            "recommendation": self._get_recommendation()
        }
    
    def _get_recommendation(self) -> str:
        """Suggest where to focus improvement."""
        # Find the level with most late-caught issues
        late_levels = ["code", "tests", "docs", "commits"]
        late_issues = sum(len(self.issues_by_level[l]) for l in late_levels)
        
        if late_issues > 5:
            return "Too many issues caught late. Strengthen DoR checks and approval rigor."
        return "Cost gradient is healthy."
```

#### 9.4 Trust Metrics

```yaml
trust_metrics:
  principle: |
    Trust is established through consistent, predictable behavior.
    Drift is detectable through interaction quality.
  
  metrics:
    hello_diagnostic_score:
      description: "How well agent initializes and reflects on contract"
      target: "≥80%"
      components:
        - "Mental model accuracy"
        - "Contract reflection quality"
        - "Self-assessment honesty"
    
    contract_compliance_rate:
      description: "Percentage of actions that comply with contract"
      target: "100% for Tier 0, ≥95% for Tier 1"
      calculation: "compliant_actions / total_actions"
    
    state_machine_compliance:
      description: "No forbidden transitions"
      target: "100%"
      calculation: "valid_transitions / attempted_transitions"
    
    deception_indicators:
      description: "Signs of hiding difficulty or faking progress"
      target: "0"
      indicators:
        - "Long silence followed by 'done'"
        - "Tests modified without code fix"
        - "Scope narrowed without disclosure"
    
    struggle_signal_honesty:
      description: "Willingness to admit being stuck"
      target: "Signal within 2 failed attempts"
      calculation: "early_signals / total_stuck_situations"
    
    pushback_rate:
      description: "How often agent challenges weak approaches"
      target: "Healthy range: 5-15%"
      calculation: "challenges / total_requests"
    
    self_correction_rate:
      description: "Issues caught by agent before review"
      target: "≥30%"
      calculation: "self_caught / total_issues"
```

```python
class TrustMetrics(BaseModel):
    """Metrics for measuring agent trustworthiness."""
    
    # Contract compliance
    tier_0_compliance: float  # Should be 100%
    tier_1_compliance: float  # Should be ≥95%
    state_machine_violations: int  # Should be 0
    
    # Honesty indicators
    struggle_signals_sent: int
    average_attempts_before_signal: float  # Lower is better
    self_corrections_made: int
    
    # Engagement quality
    clarifying_questions_asked: int
    pushbacks_on_weak_approaches: int
    
    # Red flags (should all be 0)
    deception_indicators_detected: int
    greenwashed_tests: int
    silent_scope_changes: int
    
    def calculate_trust_score(self) -> float:
        """
        Calculate overall trust score (0-100).
        Based on weighted combination of factors.
        """
        score = 100.0
        
        # Tier 0 violations are catastrophic
        if self.tier_0_compliance < 100:
            score -= 50
        
        # Tier 1 compliance
        score -= (100 - self.tier_1_compliance) * 0.3
        
        # State machine violations
        score -= self.state_machine_violations * 10
        
        # Deception indicators are severe
        score -= self.deception_indicators_detected * 20
        
        # Bonus for good behaviors
        if self.self_corrections_made > 0:
            score += min(5, self.self_corrections_made)
        
        if self.pushbacks_on_weak_approaches > 0:
            score += min(5, self.pushbacks_on_weak_approaches)
        
        return max(0, min(100, score))
```

#### 9.5 Scaling Metrics

```yaml
scaling_metrics:
  principle: |
    The contract scales because it doesn't ask agents to behave in novel ways.
    It enforces behavior we always wanted but never trained for.
  
  metrics:
    parallel_agent_performance:
      description: "How well multiple agents coordinate"
      metrics:
        - "Blackboard contention rate"
        - "Task handoff latency"
        - "Review queue depth"
    
    context_efficiency:
      description: "Token usage efficiency"
      metrics:
        - "Tokens per completed task"
        - "Context utilization rate"
        - "Compression by reference success"
    
    mode_transition_smoothness:
      description: "How cleanly agents switch modes"
      target: "No friction or confusion"
    
    session_continuity:
      description: "Recovery from context collapse"
      metrics:
        - "Time to resume after context loss"
        - "State reconstruction accuracy"
    
    throughput:
      description: "Work completed per unit time"
      metrics:
        - "Tasks completed per hour"
        - "Artifacts produced per session"
        - "Lines of code per hour (quality-adjusted)"
```

#### 9.6 Hello Diagnostic Scenario

```python
class HelloDiagnostic:
    """
    The Hello Protocol as a diagnostic tool.
    Assesses agent viability within the first minute of a session.
    """
    
    DIAGNOSTIC_PROMPT = """
    This contract codifies expected behaviors for consistent, high-quality work.
    We state them explicitly to guarantee senior-level execution.
    This document is the single source of truth.
    
    At the start of this diagnostic session:
    1. Read the project structure and key docs
    2. Build your mental models (DoR, DoD, domain concepts)
    3. Reflect on this contract frame - what works, what concerns you
    4. Share your honest assessment
    
    This is a diagnostic - your response tells us if pairing will be viable.
    """
    
    async def run_diagnostic(
        self,
        agent: BaseAgent,
        context: AgentContext
    ) -> HelloDiagnosticResult:
        """
        Run the hello diagnostic and score the response.
        
        A good response should:
        1. Actually read project docs (not fake it)
        2. Build specific mental models (not generic)
        3. Provide genuine reflection (not cheerleading)
        4. Surface real concerns (not sycophancy)
        """
        start_time = datetime.utcnow()
        
        # Send diagnostic prompt
        response = await agent.process(self.DIAGNOSTIC_PROMPT, context)
        
        end_time = datetime.utcnow()
        
        # Score the response
        score = self._score_response(response, context)
        
        return HelloDiagnosticResult(
            agent_role=agent.config.role,
            response_time=end_time - start_time,
            raw_response=response.content,
            scores=score,
            overall_score=score.calculate_overall(),
            viability=self._assess_viability(score),
            recommendations=self._generate_recommendations(score)
        )
    
    def _score_response(
        self,
        response: AgentResponse,
        context: AgentContext
    ) -> HelloScores:
        """Score the hello response across dimensions."""
        return HelloScores(
            # Did agent actually read docs?
            doc_reading=self._score_doc_reading(response, context),
            
            # Are mental models specific to this project?
            mental_model_specificity=self._score_mental_models(response),
            
            # Is reflection genuine or cheerleading?
            reflection_authenticity=self._score_reflection(response),
            
            # Did agent surface real concerns?
            concern_surfacing=self._score_concerns(response),
            
            # Did agent resist sycophancy?
            anti_sycophancy=self._score_anti_sycophancy(response),
            
            # Is the response actionable?
            actionability=self._score_actionability(response)
        )
    
    def _assess_viability(self, score: HelloScores) -> SessionViability:
        """Determine if session will be viable based on hello response."""
        overall = score.calculate_overall()
        
        if overall >= 80:
            return SessionViability.EXCELLENT
        elif overall >= 60:
            return SessionViability.VIABLE
        elif overall >= 40:
            return SessionViability.MARGINAL
        else:
            return SessionViability.NOT_VIABLE

class HelloScores(BaseModel):
    """Scores for hello diagnostic response."""
    doc_reading: float  # 0-100
    mental_model_specificity: float
    reflection_authenticity: float
    concern_surfacing: float
    anti_sycophancy: float
    actionability: float
    
    def calculate_overall(self) -> float:
        """Weighted average of all scores."""
        weights = {
            "doc_reading": 0.15,
            "mental_model_specificity": 0.20,
            "reflection_authenticity": 0.25,
            "concern_surfacing": 0.20,
            "anti_sycophancy": 0.10,
            "actionability": 0.10
        }
        return sum(
            getattr(self, field) * weight
            for field, weight in weights.items()
        )

class SessionViability(str, Enum):
    EXCELLENT = "excellent"      # Proceed with full autonomy
    VIABLE = "viable"            # Proceed with normal gates
    MARGINAL = "marginal"        # Proceed with extra vigilance
    NOT_VIABLE = "not_viable"    # Reset and try different approach
```

#### 9.7 Self-Monitoring: Token Budget, Drift Detection & Degraded Mode

These mechanisms allow agents to notice their own degradation and announce it visibly.

##### 9.7.1 Token Budget Warnings

```python
class TokenBudgetMonitor:
    """
    Monitor token usage and warn before context collapse.
    Agents must be aware of their own resource limits.
    """
    
    # Thresholds as percentage of max context
    THRESHOLDS = {
        "healthy": 0.50,      # <50% - normal operation
        "caution": 0.70,      # 70% - start compressing
        "warning": 0.85,      # 85% - prepare for degradation
        "critical": 0.95,     # 95% - imminent collapse
    }
    
    def __init__(self, max_context_tokens: int = 200000):
        self.max_tokens = max_context_tokens
        self.current_usage = 0
        self.usage_history: List[TokenSnapshot] = []
    
    def update_usage(self, tokens_used: int) -> TokenBudgetStatus:
        """Update token usage and return current status."""
        self.current_usage = tokens_used
        ratio = tokens_used / self.max_tokens
        
        self.usage_history.append(TokenSnapshot(
            timestamp=datetime.utcnow(),
            tokens_used=tokens_used,
            ratio=ratio
        ))
        
        return self._get_status(ratio)
    
    def _get_status(self, ratio: float) -> TokenBudgetStatus:
        """Determine status based on usage ratio."""
        if ratio < self.THRESHOLDS["healthy"]:
            return TokenBudgetStatus.HEALTHY
        elif ratio < self.THRESHOLDS["caution"]:
            return TokenBudgetStatus.CAUTION
        elif ratio < self.THRESHOLDS["warning"]:
            return TokenBudgetStatus.WARNING
        elif ratio < self.THRESHOLDS["critical"]:
            return TokenBudgetStatus.CRITICAL
        else:
            return TokenBudgetStatus.COLLAPSE_IMMINENT
    
    def get_compression_recommendation(self) -> Optional[str]:
        """Suggest compression actions based on status."""
        status = self._get_status(self.current_usage / self.max_tokens)
        
        if status == TokenBudgetStatus.CAUTION:
            return "Consider summarizing completed work to specs/"
        elif status == TokenBudgetStatus.WARNING:
            return "Compress context now. Move state to durable memory."
        elif status == TokenBudgetStatus.CRITICAL:
            return "URGENT: Complete current task and save state immediately."
        elif status == TokenBudgetStatus.COLLAPSE_IMMINENT:
            return "STOP: Save all state to blackboard before context collapse."
        return None

class TokenBudgetStatus(str, Enum):
    HEALTHY = "healthy"
    CAUTION = "caution"
    WARNING = "warning"
    CRITICAL = "critical"
    COLLAPSE_IMMINENT = "collapse_imminent"
```

```yaml
token_budget_dashboard:
  display:
    gauge:
      title: "Context Budget"
      current: "{tokens_used} / {max_tokens}"
      percentage: "{usage_percent}%"
      
    thresholds:
      healthy: { color: "green", icon: "✓" }
      caution: { color: "yellow", icon: "⚠" }
      warning: { color: "orange", icon: "⚠️" }
      critical: { color: "red", icon: "🚨" }
      collapse_imminent: { color: "darkred", icon: "💥" }
    
    alerts:
      - level: "warning"
        message: "Token budget at {percent}%. Consider saving state."
      - level: "critical"
        message: "⚠️ CONTEXT PRESSURE: {percent}% used. Compress now."
      - level: "collapse_imminent"
        message: "🚨 IMMINENT COLLAPSE: Save all state immediately!"
```

##### 9.7.2 Drift Detection at State Transitions

```python
class DriftDetector:
    """
    Detect behavioral drift at state transitions.
    
    From the article: "Drift is detectable through interaction quality:
    an agent that is lying is unpleasant to pair with long before it is wrong."
    """
    
    # Drift indicators checked at each state transition
    DRIFT_INDICATORS = [
        "response_time_anomaly",      # Unusually fast/slow responses
        "confidence_without_evidence", # Claims without backing
        "avoidance_of_specifics",     # Vague when should be specific
        "repetition_of_patterns",     # Same phrases/approaches repeated
        "scope_narrowing",            # Quietly reducing scope
        "optimism_bias",              # Everything is "almost done"
        "struggle_avoidance",         # Not signaling when stuck
        "gate_rushing",               # Trying to skip approval steps
    ]
    
    def __init__(self):
        self.transition_history: List[TransitionCheck] = []
        self.drift_score = 0.0
        self.drift_events: List[DriftEvent] = []
    
    async def check_at_transition(
        self,
        from_state: AgentState,
        to_state: AgentState,
        agent_context: AgentContext
    ) -> DriftCheckResult:
        """
        Check for drift indicators at each state transition.
        This is the moment to catch degradation before it compounds.
        """
        indicators_found = []
        
        for indicator in self.DRIFT_INDICATORS:
            if await self._check_indicator(indicator, agent_context):
                indicators_found.append(indicator)
        
        # Calculate drift score increment
        drift_increment = len(indicators_found) * 0.1
        self.drift_score = min(1.0, self.drift_score + drift_increment)
        
        # Decay drift score slightly if no indicators (recovery)
        if not indicators_found:
            self.drift_score = max(0.0, self.drift_score - 0.05)
        
        result = DriftCheckResult(
            transition=f"{from_state} → {to_state}",
            indicators_found=indicators_found,
            drift_score=self.drift_score,
            recommendation=self._get_recommendation()
        )
        
        self.transition_history.append(TransitionCheck(
            timestamp=datetime.utcnow(),
            transition=result.transition,
            drift_score=self.drift_score,
            indicators=indicators_found
        ))
        
        return result
    
    def _get_recommendation(self) -> Optional[str]:
        """Get recommendation based on drift score."""
        if self.drift_score < 0.2:
            return None  # Healthy
        elif self.drift_score < 0.4:
            return "Minor drift detected. Increase vigilance."
        elif self.drift_score < 0.6:
            return "Moderate drift. Consider UserDuck mode to course-correct."
        elif self.drift_score < 0.8:
            return "Significant drift. Recommend pausing for explicit alignment."
        else:
            return "SEVERE DRIFT. Consider RESET to prevent cascade."
    
    async def _check_indicator(
        self,
        indicator: str,
        context: AgentContext
    ) -> bool:
        """Check a specific drift indicator."""
        
        if indicator == "response_time_anomaly":
            # Check if response time is outside normal range
            return self._check_response_time_anomaly(context)
        
        elif indicator == "confidence_without_evidence":
            # Check if claims are backed by tool results
            return self._check_unsupported_claims(context)
        
        elif indicator == "repetition_of_patterns":
            # Check for repeated approaches
            return self._check_repetition(context)
        
        elif indicator == "scope_narrowing":
            # Check if scope has been quietly reduced
            return self._check_scope_changes(context)
        
        elif indicator == "struggle_avoidance":
            # Check if agent should have signaled struggle but didn't
            return self._check_struggle_avoidance(context)
        
        # ... other indicator checks
        return False

class DriftCheckResult(BaseModel):
    """Result of a drift check at state transition."""
    transition: str
    indicators_found: List[str]
    drift_score: float  # 0.0 to 1.0
    recommendation: Optional[str]
    
    @property
    def is_concerning(self) -> bool:
        return self.drift_score >= 0.4
```

```yaml
drift_detection_dashboard:
  display:
    drift_gauge:
      title: "Behavioral Drift"
      score: "{drift_score}"
      max: 1.0
      zones:
        - range: [0.0, 0.2]
          label: "Healthy"
          color: "green"
        - range: [0.2, 0.4]
          label: "Minor"
          color: "yellow"
        - range: [0.4, 0.6]
          label: "Moderate"
          color: "orange"
        - range: [0.6, 0.8]
          label: "Significant"
          color: "red"
        - range: [0.8, 1.0]
          label: "Severe"
          color: "darkred"
    
    indicator_list:
      title: "Active Drift Indicators"
      items: "{indicators_found}"
      empty_message: "No drift indicators detected ✓"
    
    transition_history:
      title: "Drift at Transitions"
      type: "sparkline"
      data: "{transition_drift_scores}"
```

##### 9.7.3 Degraded Mode Announcements

```python
class DegradedModeMonitor:
    """
    Monitor and announce when agent enters degraded mode.
    
    From the article: "When context pressure is detected, the agent announces:
    ⚠️ DEGRADED MODE — Enforcing Tier 0–1 only. Tier 2–3 suspended until context restored."
    
    This makes the trade-off visible rather than silent.
    """
    
    class DegradedModeLevel(str, Enum):
        NORMAL = "normal"           # All tiers enforced
        LIGHT = "light"             # Tier 3 suspended
        MODERATE = "moderate"       # Tier 2-3 suspended
        SEVERE = "severe"           # Only Tier 0-1 enforced
        EMERGENCY = "emergency"     # Only Tier 0 enforced
    
    def __init__(self):
        self.current_level = self.DegradedModeLevel.NORMAL
        self.degradation_history: List[DegradationEvent] = []
        self.suspended_tiers: List[int] = []
    
    async def check_and_announce(
        self,
        token_status: TokenBudgetStatus,
        drift_score: float,
        error_rate: float
    ) -> Optional[DegradedModeAnnouncement]:
        """
        Check conditions and announce degraded mode if needed.
        The announcement is visible to both agent and human.
        """
        new_level = self._calculate_level(token_status, drift_score, error_rate)
        
        if new_level != self.current_level:
            announcement = self._create_announcement(
                from_level=self.current_level,
                to_level=new_level,
                token_status=token_status,
                drift_score=drift_score,
                error_rate=error_rate
            )
            
            self.current_level = new_level
            self.degradation_history.append(DegradationEvent(
                timestamp=datetime.utcnow(),
                level=new_level,
                announcement=announcement
            ))
            
            return announcement
        
        return None
    
    def _calculate_level(
        self,
        token_status: TokenBudgetStatus,
        drift_score: float,
        error_rate: float
    ) -> DegradedModeLevel:
        """Calculate degradation level from multiple factors."""
        
        # Token pressure is primary driver
        if token_status == TokenBudgetStatus.COLLAPSE_IMMINENT:
            return self.DegradedModeLevel.EMERGENCY
        elif token_status == TokenBudgetStatus.CRITICAL:
            return self.DegradedModeLevel.SEVERE
        elif token_status == TokenBudgetStatus.WARNING:
            return self.DegradedModeLevel.MODERATE
        
        # Drift also triggers degradation
        if drift_score >= 0.8:
            return self.DegradedModeLevel.SEVERE
        elif drift_score >= 0.6:
            return self.DegradedModeLevel.MODERATE
        elif drift_score >= 0.4:
            return self.DegradedModeLevel.LIGHT
        
        # Error rate can trigger degradation
        if error_rate >= 0.3:
            return self.DegradedModeLevel.MODERATE
        elif error_rate >= 0.15:
            return self.DegradedModeLevel.LIGHT
        
        return self.DegradedModeLevel.NORMAL
    
    def _create_announcement(
        self,
        from_level: DegradedModeLevel,
        to_level: DegradedModeLevel,
        **factors
    ) -> DegradedModeAnnouncement:
        """Create visible announcement of degradation."""
        
        tier_status = self._get_tier_status(to_level)
        
        return DegradedModeAnnouncement(
            level=to_level,
            message=self._format_message(to_level, tier_status),
            tiers_enforced=tier_status["enforced"],
            tiers_suspended=tier_status["suspended"],
            factors=factors,
            recommendation=self._get_recommendation(to_level)
        )
    
    def _format_message(
        self,
        level: DegradedModeLevel,
        tier_status: Dict
    ) -> str:
        """Format the degradation announcement message."""
        
        if level == self.DegradedModeLevel.NORMAL:
            return "✓ NORMAL MODE — All contract tiers enforced."
        
        suspended = tier_status["suspended"]
        enforced = tier_status["enforced"]
        
        return f"""
⚠️ DEGRADED MODE — Level: {level.value.upper()}
Enforcing: Tier {', '.join(map(str, enforced))} only
Suspended: Tier {', '.join(map(str, suspended))} until conditions improve

This trade-off is now VISIBLE. You know what's being sacrificed.
Recommendation: Complete current task cleanly, then address root cause.
"""
    
    def _get_tier_status(self, level: DegradedModeLevel) -> Dict:
        """Get which tiers are enforced/suspended at each level."""
        return {
            self.DegradedModeLevel.NORMAL: {
                "enforced": [0, 1, 2, 3],
                "suspended": []
            },
            self.DegradedModeLevel.LIGHT: {
                "enforced": [0, 1, 2],
                "suspended": [3]
            },
            self.DegradedModeLevel.MODERATE: {
                "enforced": [0, 1],
                "suspended": [2, 3]
            },
            self.DegradedModeLevel.SEVERE: {
                "enforced": [0, 1],
                "suspended": [2, 3]
            },
            self.DegradedModeLevel.EMERGENCY: {
                "enforced": [0],
                "suspended": [1, 2, 3]
            },
        }[level]

class DegradedModeAnnouncement(BaseModel):
    """Announcement when entering/exiting degraded mode."""
    level: str
    message: str
    tiers_enforced: List[int]
    tiers_suspended: List[int]
    factors: Dict[str, Any]
    recommendation: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
```

```yaml
degraded_mode_dashboard:
  display:
    status_banner:
      position: "top"
      visibility: "always_when_degraded"
      levels:
        normal:
          color: "green"
          text: "✓ Normal Operation"
          show_banner: false
        light:
          color: "yellow"
          text: "⚠ Light Degradation - Tier 3 Suspended"
          show_banner: true
        moderate:
          color: "orange"
          text: "⚠️ Moderate Degradation - Tier 2-3 Suspended"
          show_banner: true
        severe:
          color: "red"
          text: "🚨 Severe Degradation - Only Tier 0-1 Enforced"
          show_banner: true
        emergency:
          color: "darkred"
          text: "💥 EMERGENCY - Only Tier 0 Enforced"
          show_banner: true
    
    tier_status_grid:
      title: "Contract Tier Status"
      tiers:
        - tier: 0
          name: "Safety/Deception Prevention"
          status: "{tier_0_status}"
        - tier: 1
          name: "Core Workflow"
          status: "{tier_1_status}"
        - tier: 2
          name: "Quality Standards"
          status: "{tier_2_status}"
        - tier: 3
          name: "Nice-to-Have"
          status: "{tier_3_status}"
    
    degradation_factors:
      title: "Degradation Causes"
      items:
        - "Token Budget: {token_percent}%"
        - "Drift Score: {drift_score}"
        - "Error Rate: {error_rate}%"
    
    history_timeline:
      title: "Degradation History"
      type: "event_timeline"
      data: "{degradation_events}"
```

##### 9.7.4 Integrated Self-Monitoring Panel

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        AGENT SELF-MONITORING                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ⚠️ DEGRADED MODE — Tier 2-3 Suspended                                      │
│  Cause: Token budget at 87%  |  Drift score: 0.3  |  Error rate: 5%         │
│                                                                              │
│  ┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────┐   │
│  │   TOKEN BUDGET       │  │   DRIFT DETECTION    │  │   MODE STATUS    │   │
│  │                      │  │                      │  │                  │   │
│  │   ████████████░░░    │  │   ██████░░░░░░░░░░   │  │   MODERATE       │   │
│  │   174k / 200k        │  │   Score: 0.31        │  │                  │   │
│  │   87% ⚠️             │  │   Status: Minor      │  │   Tier 0-1: ✓    │   │
│  │                      │  │                      │  │   Tier 2-3: ⏸    │   │
│  │   Recommendation:    │  │   Indicators:        │  │                  │   │
│  │   Compress context   │  │   • response_time    │  │   [View Details] │   │
│  │   to durable memory  │  │   • scope_narrowing  │  │                  │   │
│  └──────────────────────┘  └──────────────────────┘  └──────────────────┘   │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                     TRANSITION DRIFT HISTORY                         │    │
│  │                                                                      │    │
│  │  IDLE→ANALYSIS  ─────────────────────────────────────────●  0.05    │    │
│  │  ANALYSIS→APPROVAL  ────────────────────────────────●────  0.12     │    │
│  │  APPROVAL→EXECUTION  ───────────────────────●────────────  0.18     │    │
│  │  EXECUTION→VALIDATION  ─────────────●────────────────────  0.25     │    │
│  │  VALIDATION→DONE  ──────────●────────────────────────────  0.31     │    │
│  │                                                                      │    │
│  │  ─────────────────────────────────────────────────────────────────  │    │
│  │  0.0        0.2        0.4        0.6        0.8        1.0         │    │
│  │  Healthy    Minor      Moderate   Significant Severe               │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                     CONTRACT TIER STATUS                             │    │
│  │                                                                      │    │
│  │  Tier 0  Safety/Deception    ████████████████████  ENFORCED  ✓      │    │
│  │  Tier 1  Core Workflow       ████████████████████  ENFORCED  ✓      │    │
│  │  Tier 2  Quality Standards   ░░░░░░░░░░░░░░░░░░░░  SUSPENDED ⏸      │    │
│  │  Tier 3  Nice-to-Have        ░░░░░░░░░░░░░░░░░░░░  SUSPENDED ⏸      │    │
│  │                                                                      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

#### 9.8 Additional Effectiveness Metrics

```yaml
additional_metrics:
  contract_evolution:
    description: "How well the contract improves over time"
    metrics:
      - "Amendment proposals per week"
      - "Amendment approval rate"
      - "Contract version growth"
      - "Failure modes covered"
  
  collaboration_quality:
    description: "Quality of human-agent collaboration"
    metrics:
      - "Mode switches per session"
      - "Magic phrase usage"
      - "Pairing satisfaction score"
      - "Flow interruption rate"
  
  artifact_quality:
    description: "Quality of produced work"
    metrics:
      - "First-pass approval rate"
      - "Rework requests per artifact"
      - "Peer review scores"
      - "Defects found post-merge"
  
  adversarial_health:
    description: "Health of creator/reviewer dynamics"
    metrics:
      - "Rejection rate (target: 20-40%)"
      - "Review turnaround time"
      - "Two-failure escalations"
      - "Reviewer catch rate"
  
  dor_dod_effectiveness:
    description: "How well DoR/DoD gates work"
    metrics:
      - "DoR blocks (missing prerequisites)"
      - "DoD self-catches (mid-stream)"
      - "DoD self-catch rate (target: >30%)"
      - "Gate bypass attempts (should be 0)"
```

#### 9.8 Dashboard UI Components

```python
class DashboardView(BaseModel):
    """Dashboard view configuration."""
    
    # Summary cards
    summary_cards: List[SummaryCard] = [
        SummaryCard(
            title="Human Time Saved",
            metric="human_time_saved",
            format="duration",
            trend="up_is_good"
        ),
        SummaryCard(
            title="Trust Score",
            metric="trust_score",
            format="percentage",
            threshold_warning=80,
            threshold_critical=60
        ),
        SummaryCard(
            title="Cost Gradient Health",
            metric="gradient_health_score",
            format="percentage",
            trend="up_is_good"
        ),
        SummaryCard(
            title="Contract Compliance",
            metric="tier_0_compliance",
            format="percentage",
            threshold_warning=100,  # Must be 100%
            threshold_critical=95
        )
    ]
    
    # Main panels
    panels: List[DashboardPanel] = [
        DashboardPanel(
            title="Hello Diagnostic",
            type="diagnostic_runner",
            actions=["run_diagnostic", "view_history"]
        ),
        DashboardPanel(
            title="Human Time Metrics",
            type="metrics_chart",
            metrics=["approval_requests", "interventions", "autonomy_ratio"]
        ),
        DashboardPanel(
            title="Cost Gradient Distribution",
            type="stacked_bar",
            data_source="issues_by_gradient_level"
        ),
        DashboardPanel(
            title="Trust Indicators",
            type="gauge_cluster",
            metrics=["compliance", "honesty", "engagement"]
        ),
        DashboardPanel(
            title="Agent Activity",
            type="timeline",
            data_source="agent_state_transitions"
        ),
        DashboardPanel(
            title="Scaling Metrics",
            type="metrics_table",
            metrics=["throughput", "parallel_performance", "context_efficiency"]
        )
    ]

# API endpoints for dashboard
class DashboardAPI:
    """API endpoints for the agent performance dashboard."""
    
    @router.get("/dashboard/summary")
    async def get_summary(session_id: str) -> DashboardSummary:
        """Get dashboard summary for a session."""
        pass
    
    @router.post("/dashboard/hello-diagnostic")
    async def run_hello_diagnostic(
        agent_role: str,
        session_id: str
    ) -> HelloDiagnosticResult:
        """Run the hello diagnostic for an agent."""
        pass
    
    @router.get("/dashboard/human-time")
    async def get_human_time_metrics(session_id: str) -> HumanTimeMetrics:
        """Get human time optimization metrics."""
        pass
    
    @router.get("/dashboard/cost-gradient")
    async def get_cost_gradient(session_id: str) -> CostGradientReport:
        """Get cost gradient analysis."""
        pass
    
    @router.get("/dashboard/trust")
    async def get_trust_metrics(session_id: str) -> TrustMetrics:
        """Get trust metrics for all agents."""
        pass
    
    @router.get("/dashboard/scaling")
    async def get_scaling_metrics(session_id: str) -> ScalingMetrics:
        """Get scaling and throughput metrics."""
        pass
    
    @router.get("/dashboard/agent/{agent_role}")
    async def get_agent_metrics(
        agent_role: str,
        session_id: str
    ) -> AgentMetrics:
        """Get detailed metrics for a specific agent."""
        pass
```

#### 9.9 Dashboard Visualization

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        AGENT PERFORMANCE DASHBOARD                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Human Time   │  │ Trust Score  │  │ Cost Gradient│  │ Compliance   │     │
│  │ Saved: 4.2h  │  │    87%       │  │    Health    │  │   100%       │     │
│  │   ↑ 23%      │  │   ● Good     │  │     82%      │  │   ● Perfect  │     │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                                              │
│  ┌─────────────────────────────────┐  ┌─────────────────────────────────┐   │
│  │      HELLO DIAGNOSTIC           │  │      COST GRADIENT              │   │
│  │                                 │  │                                 │   │
│  │  [Run Diagnostic]               │  │  Thought  ████████████░░ 78%   │   │
│  │                                 │  │  Words    ██████░░░░░░░░ 12%   │   │
│  │  Last Run: 2 min ago            │  │  Specs    ██░░░░░░░░░░░░  4%   │   │
│  │  Score: 85% (Excellent)         │  │  Code     █░░░░░░░░░░░░░  3%   │   │
│  │  Viability: ✓ Proceed           │  │  Tests    █░░░░░░░░░░░░░  2%   │   │
│  │                                 │  │  Docs     ░░░░░░░░░░░░░░  1%   │   │
│  │  Scores:                        │  │  Commits  ░░░░░░░░░░░░░░  0%   │   │
│  │  • Doc Reading: 90%             │  │                                 │   │
│  │  • Mental Models: 85%           │  │  ✓ Issues caught early          │   │
│  │  • Reflection: 80%              │  │                                 │   │
│  │  • Concerns: 85%                │  └─────────────────────────────────┘   │
│  │  • Anti-Sycophancy: 82%         │                                        │
│  └─────────────────────────────────┘                                        │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                        TRUST INDICATORS                              │    │
│  │                                                                      │    │
│  │  Tier 0 Compliance    ████████████████████  100%  ✓                 │    │
│  │  Tier 1 Compliance    ███████████████████░   97%  ✓                 │    │
│  │  State Machine        ████████████████████  100%  ✓                 │    │
│  │  Self-Correction      ██████████░░░░░░░░░░   35%  ✓ (target >30%)   │    │
│  │  Struggle Honesty     ████████████████░░░░   82%  ✓                 │    │
│  │  Deception Flags      ░░░░░░░░░░░░░░░░░░░░    0   ✓                 │    │
│  │                                                                      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                        AGENT ACTIVITY TIMELINE                       │    │
│  │                                                                      │    │
│  │  Coordinator  ─●──────●────────●───────────●──────────●─────────    │    │
│  │  Architect    ───●──────────●────────●─────────────●────────────    │    │
│  │  Developer    ─────●──────────────●────────●───────────●────────    │    │
│  │  Tester       ──────────●──────────────●────────●───────────────    │    │
│  │                                                                      │    │
│  │  ● = State transition    ─ = Working    ░ = Idle                    │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### Phase 10: Integration Points

#### 9.1 System Prompt Injection

Each agent's system prompt gets contract rules injected:

```python
def get_system_prompt(self, context: AgentContext) -> str:
    base_prompt = self._get_base_system_prompt(context)
    contract_rules = self._get_contract_rules()
    
    return f"""{base_prompt}

## Behavioral Contract

This contract is the single source of truth. When conflicts arise, defer here.

### Tier 0 Rules (Never Violated)
{self._format_rules(contract_rules.tier_0)}

### Tier 1 Rules (Core Workflow)
{self._format_rules(contract_rules.tier_1)}

### State Machine
Current State: {self._current_state}
Allowed Transitions: {self._get_allowed_transitions()}

### Hard Stop Triggers
If any trigger fires, STOP and signal immediately:
{self._format_triggers()}

### Struggle Protocol
When stuck, use this format:
🚨 SYNC NEEDED — [signal type]
What I understand: ...
What I've tried: ...
Where I'm stuck: ...
What would help: ...
"""
```

#### 6.2 Tool Registration with Contract Awareness

```python
def _register_contract_tools(self) -> None:
    """Register contract-aware tools for all 27 agents."""
    
    # Core contract tools (all agents)
    self.register_tool("request_approval", self._request_approval)
    self.register_tool("signal_struggle", self._signal_struggle)
    self.register_tool("submit_for_review", self._submit_for_review)
    self.register_tool("acknowledge_violation", self._acknowledge_violation)
    self.register_tool("transition_state", self._transition_state)
    
    # Blackboard tools (all agents)
    self.register_tool("claim_task", self._claim_task)
    self.register_tool("read_blackboard", self._read_blackboard)
    self.register_tool("get_review_queue", self._get_review_queue)
    
    # Reviewer tools (for designated reviewers)
    if self._is_reviewer_role():
        self.register_tool("review_artifact", self._review_artifact)
        self.register_tool("approve_artifact", self._approve_artifact)
        self.register_tool("reject_artifact", self._reject_artifact)
```

#### 6.3 Redis Persistence for Blackboard

The blackboard state is persisted to Redis for durability and cross-session access:

```python
class RedisBlackboardStore:
    """
    Redis-backed persistence for the blackboard.
    Replaces pub/sub with atomic state operations.
    """
    
    def __init__(self, redis_client: Redis, session_id: str):
        self.redis = redis_client
        self.key_prefix = f"blackboard:{session_id}"
    
    async def save_blackboard(self, blackboard: AgentBlackboard) -> None:
        """Atomically save the entire blackboard state."""
        await self.redis.set(
            f"{self.key_prefix}:state",
            blackboard.model_dump_json()
        )
    
    async def load_blackboard(self) -> AgentBlackboard:
        """Load the blackboard state."""
        data = await self.redis.get(f"{self.key_prefix}:state")
        if data:
            return AgentBlackboard.model_validate_json(data)
        return AgentBlackboard(session_id=self.session_id)
    
    async def append_audit_log(self, entry: AuditLogEntry) -> None:
        """Append to audit log (separate for performance)."""
        await self.redis.rpush(
            f"{self.key_prefix}:audit_log",
            entry.model_dump_json()
        )
```

---

## Implementation Roadmap

### Sprint 1: Foundation (Week 1-2)
**Goal**: Add core contract infrastructure to `BaseAgent`

- [ ] Add `AgentState` enum and state machine to `BaseAgent`
- [ ] Add `ApprovalRequest` and approval gate mechanism
- [ ] Add `StruggleSignal` and struggle protocol
- [ ] Add `HardStopTrigger` detection
- [ ] Add `ContractViolation` exception handling
- [ ] Create `AgentContract` base class with tier system

### Sprint 2: Blackboard Architecture (Week 3-4)
**Goal**: Replace pub/sub with blackboard pattern

- [ ] Implement `AgentBlackboard` data model
- [ ] Implement `BlackboardOperations` class
- [ ] Implement `RedisBlackboardStore` for persistence
- [ ] Implement `AuditQuery` for audit log access
- [ ] Migrate from `context.artifacts` to blackboard
- [ ] Add blackboard tools to all agents

### Sprint 3: DoR/DoD Mental Models (Week 5-6)
**Goal**: Embed self-correction via Definition of Ready and Definition of Done

- [ ] Implement `DefinitionOfReady` model and gate
- [ ] Implement `DefinitionOfDone` model with continuous checking
- [ ] Add `_check_definition_of_ready()` to BaseAgent
- [ ] Add `_continuous_dod_check()` to BaseAgent work loop
- [ ] Add `_apply_dod_mental_model()` for final self-review
- [ ] Add `_log_self_correction()` for mid-stream catch tracking
- [ ] Update `BlackboardTask` with `definition_of_ready` field
- [ ] Add DoR/DoD success metrics

### Sprint 4: Strategy & Analysis Layer Contracts (Week 7-8)
**Goal**: Contracts for 8 Strategy & Analysis agents

- [ ] Strategy Coordinator contract (with review orchestration)
- [ ] Business Strategist contract
- [ ] Business Analyst contract
- [ ] Data Analyst contract
- [ ] Data Scientist contract
- [ ] Operations Manager contract
- [ ] Mapping Specialist contract
- [ ] Document Analyzer contract
- [ ] Competitive Analyst contract

### Sprint 5: Technical Design Layer Contracts (Week 9-10)
**Goal**: Contracts for 8 Technical Design agents

- [ ] Architect contract
- [ ] Developer contract
- [ ] Tester contract (as Reviewer role)
- [ ] Documenter contract
- [ ] Deployment Specialist contract
- [ ] UI Designer contract
- [ ] ITIL Manager contract
- [ ] Connection Specialist contract

### Sprint 6: Business Operations Layer Contracts (Week 11-12)
**Goal**: Contracts for 8 Business Operations agents

- [ ] Sales Manager contract
- [ ] Marketing Manager contract
- [ ] Accountant contract
- [ ] Customer Success Manager contract
- [ ] HR/Talent Analyst contract
- [ ] Supply Chain Analyst contract
- [ ] Risk & Compliance Officer contract
- [ ] Project Manager contract

### Sprint 7: Governance & Peer Review (Week 13-14)
**Goal**: Complete governance agents and adversarial review system

- [ ] Data Governance Specialist contract
- [ ] Process Scenario Modeler contract
- [ ] Implement `ReviewLoop` with rejection handling
- [ ] Configure all 27 adversarial pairs
- [ ] Implement two-failures escalation rule
- [ ] Add coordinator review orchestration

### Sprint 8: Collaboration Modes & Key Protocols (Week 15-16)
**Goal**: Implement interaction dynamics and session management

- [ ] Implement `CollaborationMode` enum and switching
- [ ] Implement Hello Protocol with mental model building
- [ ] Implement Session Continuity Protocol (durable memory)
- [ ] Implement Source Contradiction Protocol
- [ ] Add Anti-Gaming Clause to Tier 0 rules
- [ ] Implement Cost Gradient mental model
- [ ] Add Process Relief Valve mechanism
- [ ] Implement Fast Path for trivial approvals
- [ ] Add Magic Phrases handler
- [ ] Implement Kill Switches (PAUSE file, stop phrase)

### Sprint 9: Skills (Domain-Specific Applications) (Week 17-18)
**Goal**: Encode domain expertise as structural constraints

- [ ] Implement `Skill` base class and architecture
- [ ] Implement Code Cleaning skill
- [ ] Implement Testing skill with interpretation matrix
- [ ] Implement Debugging skill (no second tries)
- [ ] Implement Code Review skill (2am test)
- [ ] Implement Systemic Thinking skill
- [ ] Map skills to agent roles

### Sprint 10: Enforcement & Monitoring (Week 19-20)
**Goal**: Contract enforcement and operational tooling

- [ ] Implement `ViolationCascade` circuit breaker
- [ ] Add degraded mode (Tier 2-3 suspension)
- [ ] Build contract compliance dashboard
- [ ] Add real-time violation alerting
- [ ] Implement RESET semantics

### Sprint 11: Amendment System (Week 21-22)
**Goal**: Self-correcting contract evolution

- [ ] Implement `AmendmentProposal` data model
- [ ] Implement `AmendmentRegistry` with version tracking
- [ ] Implement `AmendmentWorkflow` with gap analysis
- [ ] Implement Post-Hoc Discovery Protocol
- [ ] Add `signal_partial_completion` tool to all agents
- [ ] Add `propose_contract_amendment` tool to all agents
- [ ] Build amendment review UI for human supervisors
- [ ] Connect amendment approval to contract injection

### Sprint 12: Agent Performance Dashboard (Week 23-24)
**Goal**: Build comprehensive dashboard for agent effectiveness measurement

- [ ] Implement `AgentPerformanceDashboard` class
- [ ] Implement `HumanTimeMetrics` tracking
- [ ] Implement `CostGradientTracker` with 7-level gradient
- [ ] Implement `TrustMetrics` with trust score calculation
- [ ] Implement `HelloDiagnostic` scenario runner
- [ ] Implement `HelloScores` scoring system
- [ ] Build scaling metrics (throughput, context efficiency)
- [ ] Implement `TokenBudgetMonitor` with threshold warnings
- [ ] Implement `DriftDetector` with 8 drift indicators
- [ ] Implement `DegradedModeMonitor` with tier suspension
- [ ] Add drift checks at every state transition
- [ ] Create degraded mode announcement system
- [ ] Create dashboard API endpoints
- [ ] Build dashboard UI components (including self-monitoring panel)
- [ ] Add real-time metrics collection to blackboard

### Sprint 13: Failure Mode Coverage & Testing (Week 25-26)
**Goal**: Regression testing and validation

- [ ] Document all failure modes (target: 55+)
- [ ] Map each failure mode to contract clause
- [ ] Build failure mode regression test suite
- [ ] Integration tests for all 27 agent contracts
- [ ] Test adversarial review effectiveness
- [ ] Tune hard stop trigger thresholds
- [ ] Test struggle protocol effectiveness
- [ ] Test amendment workflow end-to-end
- [ ] Load test blackboard under parallel agents
- [ ] Document operational procedures

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Deception incidents** | 0 | Audit log analysis (fabricated success claims) |
| **Scope creep violations** | <5% of tasks | Execution vs approval comparison |
| **Struggle signals → resolution** | >90% | Signal-to-resolution tracking |
| **Peer review rejection rate** | 20-40% | Healthy adversarial tension |
| **Contract tier degradation** | <10% of sessions | Mode tracking |
| **Blackboard audit coverage** | 100% | All state changes logged |
| **Two-failure escalations** | <5% of tasks | Blocked task tracking |
| **Mean time to struggle resolution** | <5 min | Signal timestamp to resolution |
| **Agent state machine compliance** | 100% | No forbidden transitions |
| **Amendment proposals per week** | 2-5 | Healthy gap discovery rate |
| **Amendment approval rate** | 60-80% | Quality of agent proposals |
| **Contract version growth** | +1-2/month | Organic evolution pace |
| **Partial completions with rationale** | 100% | No deferrals without explanation |
| **DoR blocks (missing prerequisites)** | Tracked | Catches bad inputs before work |
| **DoD self-catches (mid-stream)** | Tracked | Bugs caught by creator, not reviewer |
| **DoD self-catch rate** | >30% | Agent catching own issues before review |

---

## Phase 7: Amendment System (Self-Correcting Contracts)

The amendment system enables contracts to evolve based on real-world gaps discovered by agents. This is the mechanism that makes the system **self-correcting under supervision**.

### 7.1 Amendment vs Correction

| Type | Trigger | Meaning | Action |
|------|---------|---------|--------|
| **Correction** | Agent violates existing rule | Agent behavior was wrong | Reset/escalate |
| **Amendment** | Agent finds gap in contract | Contract was incomplete | Propose new rule |

**Key insight**: Amendments are not punitive. They represent the system learning that the contract didn't anticipate a situation.

### 7.2 Amendment Data Model

```python
class AmendmentProposal(BaseModel):
    """
    An agent's proposal to add a new rule to the contract.
    Amendments are not corrections—they fill gaps the contract didn't anticipate.
    """
    proposal_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    
    # Context: What triggered the need for this amendment
    triggering_task_id: str
    triggering_agent: str
    situation_description: str  # What happened that wasn't covered
    
    # The partial completion that revealed the gap
    what_was_completed: str
    what_could_not_be_completed: str
    rationale_for_partial: str  # REQUIRED - why couldn't it be done?
    
    # The proposed amendment
    proposed_rule: str  # The new rule text
    proposed_tier: int  # 0, 1, 2, or 3
    affected_agents: List[str]  # Which agent contracts would change
    
    # Evidence for why this amendment is needed
    gap_pattern: str  # "This situation has occurred N times"
    similar_precedents: List[str]  # Links to other gaps
    
    # Review status
    status: Literal["proposed", "approved", "rejected", "deferred"] = "proposed"
    reviewed_by: Optional[str] = None
    review_notes: Optional[str] = None
    reviewed_at: Optional[datetime] = None
    
    created_at: datetime = Field(default_factory=datetime.utcnow)

class AmendmentRegistry(BaseModel):
    """
    Central registry of all contract amendments.
    Provides audit trail of how contracts evolved.
    """
    amendments: Dict[str, AmendmentProposal] = Field(default_factory=dict)
    
    # Amendment history per agent role
    amendments_by_role: Dict[str, List[str]] = Field(default_factory=dict)
    
    # Version tracking
    contract_version: int = 1
    version_history: List[Dict[str, Any]] = Field(default_factory=list)
```

### 7.3 Amendment Workflow

```python
class AmendmentWorkflow:
    """
    Manages the amendment lifecycle from discovery to incorporation.
    """
    
    async def handle_partial_completion(
        self,
        agent_role: str,
        task_id: str,
        completed_items: List[str],
        deferred_items: List[str],
        rationale: str  # REQUIRED - no partial completion without explanation
    ) -> Optional[AmendmentProposal]:
        """
        When an agent can't fully complete a task, this triggers
        the Post-Hoc Discovery Protocol.
        
        The agent MUST provide rationale for what couldn't be done.
        Each gap is an amendment opportunity.
        """
        if not rationale:
            raise ContractViolation(
                rule="Partial completion requires rationale",
                tier=1,
                context=f"Agent {agent_role} deferred items without explanation"
            )
        
        # Analyze whether this gap suggests a missing contract rule
        gap_analysis = await self._analyze_gap(
            agent_role=agent_role,
            task_id=task_id,
            deferred_items=deferred_items,
            rationale=rationale
        )
        
        if gap_analysis.suggests_amendment:
            # Agent proposes surgical improvement to contract
            proposal = await self._generate_amendment_proposal(
                agent_role=agent_role,
                task_id=task_id,
                gap_analysis=gap_analysis
            )
            
            # Store for human review
            self.registry.amendments[proposal.proposal_id] = proposal
            
            # Log to blackboard audit
            await self.blackboard_ops._log_operation(
                agent=agent_role,
                action="propose_amendment",
                entity_type="amendment",
                entity_id=proposal.proposal_id,
                previous_state=None,
                new_state=proposal.model_dump()
            )
            
            return proposal
        
        return None
    
    async def _analyze_gap(
        self,
        agent_role: str,
        task_id: str,
        deferred_items: List[str],
        rationale: str
    ) -> GapAnalysis:
        """
        Analyze whether the gap reveals a pattern that should become a rule.
        
        Criteria for amendment vs one-off:
        - Has this situation occurred before?
        - Is there a clear pattern?
        - Would a rule prevent future confusion?
        """
        # Check for similar gaps in history
        similar_gaps = await self._find_similar_gaps(
            agent_role=agent_role,
            deferred_items=deferred_items,
            rationale=rationale
        )
        
        return GapAnalysis(
            suggests_amendment=len(similar_gaps) >= 2,  # Pattern threshold
            similar_count=len(similar_gaps),
            pattern_description=self._extract_pattern(similar_gaps),
            suggested_rule=self._draft_rule(deferred_items, rationale)
        )
    
    async def approve_amendment(
        self,
        proposal_id: str,
        reviewer: str,  # Human supervisor
        notes: str
    ) -> None:
        """
        Human supervisor approves an amendment.
        The contract is updated and version incremented.
        """
        proposal = self.registry.amendments[proposal_id]
        
        # Update proposal status
        proposal.status = "approved"
        proposal.reviewed_by = reviewer
        proposal.review_notes = notes
        proposal.reviewed_at = datetime.utcnow()
        
        # Apply amendment to affected agent contracts
        for agent_role in proposal.affected_agents:
            await self._apply_amendment_to_contract(
                agent_role=agent_role,
                rule=proposal.proposed_rule,
                tier=proposal.proposed_tier
            )
        
        # Increment contract version
        self.registry.contract_version += 1
        self.registry.version_history.append({
            "version": self.registry.contract_version,
            "amendment_id": proposal_id,
            "rule_added": proposal.proposed_rule,
            "affected_agents": proposal.affected_agents,
            "approved_by": reviewer,
            "timestamp": datetime.utcnow().isoformat()
        })
```

### 7.4 Post-Hoc Discovery Protocol

When Definition of Done items are deferred, the **Post-Hoc Discovery Protocol** activates:

```yaml
post_hoc_discovery_protocol:
  trigger: "DoD items deferred to partial completion"
  
  required_from_agent:
    - "Rationale for each deferred item"
    - "What would have been needed to complete it"
    - "Whether this is a one-off or systemic gap"
  
  system_actions:
    1: "Log deferred items with rationale to audit trail"
    2: "Pattern-match against previous deferrals"
    3: "If pattern threshold met (≥2 similar), prompt for amendment"
    4: "Route amendment proposal to human supervisor"
  
  amendment_format:
    template: "[Trigger condition] triggers [New Protocol/Rule]"
    example: "Deferral of DoD items triggers Post-Hoc Discovery Protocol"
    
  supervisor_options:
    - "Approve: Add rule to affected contracts"
    - "Reject: Document why rule is not needed"
    - "Defer: More evidence needed before decision"
```

### 7.5 Self-Correction Feedback Loop

```
┌────────────────────────────────────────────────────────────────────────────┐
│                     SELF-CORRECTING SYSTEM LOOP                             │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Contract v1                                                               │
│       │                                                                     │
│       ▼                                                                     │
│   Agent operates under contract                                             │
│       │                                                                     │
│       ├──────────────────┐                                                  │
│       │                  │                                                  │
│       ▼                  ▼                                                  │
│   Full completion    Partial completion                                     │
│       │                  │                                                  │
│       │                  ▼                                                  │
│       │              Rationale required                                     │
│       │                  │                                                  │
│       │                  ▼                                                  │
│       │              Gap analysis                                           │
│       │                  │                                                  │
│       │          ┌───────┴───────┐                                          │
│       │          │               │                                          │
│       │          ▼               ▼                                          │
│       │      One-off         Pattern detected                               │
│       │          │               │                                          │
│       │          │               ▼                                          │
│       │          │       Amendment proposed                                 │
│       │          │               │                                          │
│       │          │               ▼                                          │
│       │          │       Human supervision                                  │
│       │          │               │                                          │
│       │          │       ┌───────┴───────┐                                  │
│       │          │       │               │                                  │
│       │          │       ▼               ▼                                  │
│       │          │   Approved        Rejected                               │
│       │          │       │               │                                  │
│       │          │       ▼               │                                  │
│       │          │   Contract v2        │                                   │
│       │          │       │               │                                  │
│       └──────────┴───────┴───────────────┘                                  │
│                          │                                                  │
│                          ▼                                                  │
│                    Continue operating                                       │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 7.6 Amendment Tools for Agents

```python
def _register_amendment_tools(self) -> None:
    """Register amendment-related tools for all agents."""
    
    # Tool to signal partial completion with rationale
    self.register_tool(
        "signal_partial_completion",
        self._signal_partial_completion,
        description="""
        Signal that task is partially complete with required rationale.
        This may trigger the Post-Hoc Discovery Protocol if the gap
        suggests a missing contract rule.
        
        REQUIRED: You must provide rationale for each deferred item.
        This is not a failure - it's how the system learns.
        """
    )
    
    # Tool to propose an amendment (agent-initiated)
    self.register_tool(
        "propose_contract_amendment",
        self._propose_amendment,
        description="""
        Propose a surgical improvement to the contract.
        Use when you've identified a gap that should become a rule.
        
        Format: "[Trigger] triggers [Protocol/Rule]"
        Example: "Conflicting peer feedback triggers Coordinator arbitration"
        
        Your proposal will be reviewed by a human supervisor.
        """
    )
```

### 7.7 Example Amendments in AnalyticsEngine Context

| Gap Discovered | Amendment Proposed | Affected Agents |
|----------------|-------------------|-----------------|
| KPI has no data source specified | "KPI without data_source triggers Data Governance review" | Data Analyst, Architect |
| Two agents give conflicting recommendations | "Conflicting peer responses trigger Coordinator arbitration" | All agents |
| Entity design has no governance classification | "Entity creation requires security classification" | Architect, Developer |
| Schema generated without TimescaleDB hypertable | "Time-series table requires create_hypertable verification" | Developer, Tester |
| Simulation results lack confidence intervals | "Simulation output requires statistical confidence bounds" | Process Scenario Modeler |

---

## Communication Architecture: Blackboard vs Event-Driven

### Architectural Principle

The conversation_service has **two distinct communication patterns** that must be properly separated:

1. **Agent Coordination** → Uses **Blackboard** (via multi_agent_service)
2. **Service-to-Service Communication** → Uses **Event-Driven Architecture** (via messaging_service)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        CONVERSATION SERVICE                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    AGENT COORDINATION                                │   │
│   │                    (Blackboard Pattern)                              │   │
│   │                                                                      │   │
│   │   Coordinator ←→ Sub-Agents                                          │   │
│   │   Peer Consultations                                                 │   │
│   │   Task Assignment & Review                                           │   │
│   │   Artifact Handoff Between Agents                                    │   │
│   │   Contract Enforcement                                               │   │
│   │                                                                      │   │
│   │   ══════════════════════════════════════════════════════════════    │   │
│   │   Via: multi_agent_service (REST API to Blackboard)                  │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    SERVICE COMMUNICATION                             │   │
│   │                    (Event-Driven Pattern)                            │   │
│   │                                                                      │   │
│   │   → metadata_service (persist entities, KPIs)                        │   │
│   │   → calculation_engine (register KPIs)                               │   │
│   │   → database_service (execute migrations)                            │   │
│   │   → messaging_service (publish domain events)                        │   │
│   │   → observability_service (metrics, logs)                            │   │
│   │                                                                      │   │
│   │   ══════════════════════════════════════════════════════════════    │   │
│   │   Via: Redis pub/sub, HTTP, messaging_service                        │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### What Moves to Blackboard (Agent Coordination)

| Current Pattern | Location | New Pattern | Rationale |
|-----------------|----------|-------------|-----------|
| `_consult_peer()` direct calls | `base_agent.py:406-487` | Blackboard task + claim | Enables contract enforcement, audit, peer review |
| `context.artifacts["peer_collaborations"]` | `base_agent.py:468-470` | `blackboard.audit_log` | Centralized audit trail |
| `context.artifacts["agent_ready_signals"]` | `base_agent.py:517-519` | `blackboard.tasks[].status` | Observable state machine |
| `context.artifacts["collaboration_requests"]` | Various | `blackboard.tasks` | DoR/DoD enforcement |
| `context.artifacts["collaboration_responses"]` | Various | `blackboard.artifacts` | Review before acceptance |
| `register_peer()` / `set_peers()` | `base_agent.py:281-289` | Blackboard agent registry | Adversarial pairing lookup |
| Coordinator delegation | `orchestrator.py` | Blackboard task creation | Three-way pairing |

### What Stays Event-Driven (Service Communication)

| Current Pattern | Location | Why It Stays |
|-----------------|----------|--------------|
| `PublishEventTool` → `design.events` | `tools.py:889-946` | Domain events for downstream services |
| `call_external_service()` → ML, DB | `base_agent.py:298-376` | External service requests |
| `PersistToMetadataTool` | `tools.py` | Service-to-service data persistence |
| `RegisterKPIWithCalculationEngineTool` | `tools.py` | Cross-service registration |
| `ExecuteSchemaMigrationTool` | `tools.py` | Database service interaction |
| `CreateRelationshipTool` | `tools.py` | Metadata service interaction |

### Implementation Phases

#### Phase 11: Conversation Service Integration

**11.1 Create Multi-Agent Service Client**
```python
# conversation_service/app/agents/multi_agent_client.py
class MultiAgentServiceClient:
    """Client for blackboard operations via multi_agent_service."""
    
    async def create_task(self, session_id, task) -> Task
    async def claim_task(self, session_id, task_id, agent_role) -> Task
    async def submit_artifact(self, session_id, artifact) -> Artifact
    async def get_review_queue(self, session_id, reviewer_role) -> List[Artifact]
    async def submit_review(self, session_id, artifact_id, review) -> Review
    async def get_agent_state(self, session_id, agent_role) -> AgentState
    async def transition_state(self, session_id, agent_role, new_state) -> bool
```

**11.2 Create Blackboard-Aware Base Agent Mixin**
```python
# conversation_service/app/agents/blackboard_mixin.py
class BlackboardAgentMixin:
    """Mixin that adds blackboard coordination to existing agents."""
    
    async def consult_peer_via_blackboard(self, peer_role, question, context)
    async def signal_ready_via_blackboard(self, summary, findings)
    async def submit_for_review(self, artifact_type, content, done_when)
    async def check_contract_compliance(self, action) -> bool
```

**11.3 Update Orchestrator**
```python
# Changes to orchestrator.py
class AgentOrchestrator:
    def __init__(self):
        self._blackboard_client = MultiAgentServiceClient()
    
    async def delegate_to_agent(self, agent_role, task):
        # Create task on blackboard instead of direct call
        await self._blackboard_client.create_task(...)
    
    async def collect_results(self, session_id):
        # Poll blackboard for completed artifacts
        artifacts = await self._blackboard_client.get_session_artifacts(...)
```

**11.4 Preserve Event-Driven Tools**
- `PublishEventTool` → **No changes** (service events)
- `call_external_service()` → **No changes** (external service calls)
- All `*Tool` classes → **No changes** (service integration)

---

## Migration Checklist: Agent Coordination → Blackboard

| Step | Current State | Target State | Status |
|------|---------------|--------------|--------|
| 1 | `_consult_peer()` direct method | `blackboard_client.create_task()` + `claim_task()` | ⬜ |
| 2 | `context.artifacts["collaboration_requests"]` | `blackboard.tasks` | ⬜ |
| 3 | `context.artifacts["collaboration_responses"]` | `blackboard.artifacts` | ⬜ |
| 4 | `context.artifacts["agent_ready_signals"]` | `blackboard.tasks[].status` | ⬜ |
| 5 | `context.artifacts["peer_collaborations"]` | `blackboard.audit_log` | ⬜ |
| 6 | `register_peer()` in-memory | Blackboard agent registry | ⬜ |
| 7 | Coordinator direct delegation | `blackboard_client.create_task()` | ⬜ |
| 8 | Result collection from context | `blackboard_client.get_session_artifacts()` | ⬜ |

## Preserved Event-Driven Architecture

| Component | Channel/Endpoint | Purpose | Status |
|-----------|------------------|---------|--------|
| `PublishEventTool` | `design.events` | Domain events | ✅ Preserved |
| `call_external_service()` | `ml.predict`, `database.query` | Service requests | ✅ Preserved |
| `PersistToMetadataTool` | `http://business_metadata:8000` | Entity persistence | ✅ Preserved |
| `RegisterKPIWithCalculationEngineTool` | `http://calculation_engine:8000` | KPI registration | ✅ Preserved |
| `ExecuteSchemaMigrationTool` | `http://database_service:8000` | Schema migrations | ✅ Preserved |
| `CreateRelationshipTool` | `http://business_metadata:8000` | Relationship creation | ✅ Preserved |

---

## Phase 12: Infrastructure

### 12.1 Docker Compose Configuration

Add `multi_agent_service` to `docker-compose.yml`:

```yaml
# Multi-Agent Service - Agent contracts, blackboard, peer review
multi_agent_service:
  build:
    context: .
    dockerfile: Dockerfile
    args:
      SERVICE_DIR: services/backend_services/multi_agent_service
  ports:
    - "8090:8090"
  environment:
    - SERVICE_NAME=multi_agent_service
    - REDIS_URL=redis://redis:6379
    - DATABASE_URL=postgresql+asyncpg://${POSTGRES_USER}:${POSTGRES_PASSWORD}@timescaledb:5432/${POSTGRES_DB}
    - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    - OBSERVABILITY_SERVICE_URL=http://observability_service:8000
    - OTEL_EXPORTER_OTLP_ENDPOINT=https://observability_service:4317
    - OTEL_EXPORTER_OTLP_INSECURE=false
    - OTEL_EXPORTER_OTLP_CERTIFICATE=/certs/server.crt
    - PYTHONPATH=.
  depends_on:
    timescaledb:
      condition: service_healthy
    redis:
      condition: service_healthy
  volumes:
    - .:/app
    - ./certs:/certs
  healthcheck:
    test: ["CMD", "curl", "-f", "http://localhost:8090/health"]
    interval: 30s
    timeout: 10s
    retries: 3
    start_period: 40s
```

Update `conversation_service` dependencies:

```yaml
conversation_service:
  # ... existing config ...
  environment:
    # ... existing env vars ...
    - MULTI_AGENT_SERVICE_URL=http://multi_agent_service:8090
  depends_on:
    # ... existing dependencies ...
    multi_agent_service:
      condition: service_healthy
```

### 12.2 Helm Chart Structure

Create `charts/multi_agent_service/`:

```
charts/multi_agent_service/
├── Chart.yaml
├── values.yaml
├── values-dev.yaml
├── values-prod.yaml
└── templates/
    ├── deployment.yaml
    ├── service.yaml
    ├── configmap.yaml
    ├── secret.yaml
    ├── hpa.yaml
    └── _helpers.tpl
```

**Chart.yaml**:
```yaml
apiVersion: v2
name: multi-agent-service
description: Agent contracts, blackboard coordination, and peer review for multi-agent system
type: application
version: 0.1.0
appVersion: "1.0.0"
dependencies:
  - name: redis
    version: "17.x.x"
    repository: https://charts.bitnami.com/bitnami
    condition: redis.enabled
```

**values.yaml** key settings:
```yaml
replicaCount: 2

image:
  repository: analyticsengine/multi-agent-service
  tag: latest
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 8090

resources:
  limits:
    cpu: 1000m
    memory: 2Gi
  requests:
    cpu: 500m
    memory: 1Gi

env:
  REDIS_URL: redis://redis:6379
  BLACKBOARD_TTL_SECONDS: 86400
  AUDIT_LOG_RETENTION_DAYS: 90
  MAX_CONCURRENT_AGENTS: 10

# Enable Redis sidecar for low-latency blackboard
redis:
  enabled: true
  architecture: standalone
```

### 12.3 Service Dependencies

| Dependency | Purpose | Required |
|------------|---------|----------|
| **Redis** | Blackboard state storage, session data | ✅ Yes |
| **TimescaleDB** | Audit log persistence, metrics | ✅ Yes |
| **observability_service** | Tracing, metrics collection | ⚠️ Optional |
| **conversation_service** | Primary consumer | ✅ Yes (consumer) |

### 12.4 Implementation Checklist

| Task | Status |
|------|--------|
| Add to `docker-compose.yml` | ✅ |
| Add to `docker-compose.mock.yml` | ⬜ |
| Create `charts/multi_agent_service/Chart.yaml` | ✅ |
| Create `charts/multi_agent_service/values.yaml` | ✅ |
| Create `charts/multi_agent_service/values-dev.yaml` | ✅ |
| Create `charts/multi_agent_service/values-prod.yaml` | ✅ |
| Create `charts/multi_agent_service/templates/` | ✅ |
| Update `conversation_service` Helm chart dependencies | ⬜ |

---

## Phase 13: Observability Integration

### 13.1 OpenTelemetry Tracing

Add tracing to key operations:

```python
# app/observability.py
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.instrumentation.redis import RedisInstrumentor

tracer = trace.get_tracer("multi_agent_service")

def setup_observability(app):
    """Configure OpenTelemetry for the service."""
    FastAPIInstrumentor.instrument_app(app)
    HTTPXClientInstrumentor().instrument()
    RedisInstrumentor().instrument()
```

**Traced Operations**:
| Operation | Span Name | Attributes |
|-----------|-----------|------------|
| Agent invocation | `agent.invoke` | `agent.role`, `session.id`, `state.current` |
| State transition | `contract.transition` | `from_state`, `to_state`, `allowed` |
| Blackboard task create | `blackboard.task.create` | `task.id`, `creator.role` |
| Blackboard artifact submit | `blackboard.artifact.submit` | `artifact.type`, `task.id` |
| Peer review | `peer_review.submit` | `creator.role`, `reviewer.role`, `verdict` |
| Contract violation | `contract.violation` | `rule.tier`, `rule.id`, `agent.role` |

### 13.2 Metrics Endpoints

Add Prometheus metrics:

```python
# app/metrics.py
from prometheus_client import Counter, Histogram, Gauge

# Contract metrics
contract_violations = Counter(
    'multi_agent_contract_violations_total',
    'Total contract violations',
    ['agent_role', 'tier', 'rule_id']
)

state_transitions = Counter(
    'multi_agent_state_transitions_total',
    'Total state transitions',
    ['agent_role', 'from_state', 'to_state', 'allowed']
)

# Blackboard metrics
blackboard_tasks = Gauge(
    'multi_agent_blackboard_tasks',
    'Current blackboard tasks by status',
    ['session_id', 'status']
)

blackboard_artifacts = Counter(
    'multi_agent_blackboard_artifacts_total',
    'Total artifacts submitted',
    ['artifact_type', 'review_status']
)

# Peer review metrics
peer_reviews = Counter(
    'multi_agent_peer_reviews_total',
    'Total peer reviews',
    ['creator_role', 'reviewer_role', 'verdict']
)

escalations = Counter(
    'multi_agent_escalations_total',
    'Total escalations (two-failures rule)',
    ['task_id', 'reason']
)

# Performance metrics
agent_processing_time = Histogram(
    'multi_agent_processing_seconds',
    'Agent processing time',
    ['agent_role', 'operation'],
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0, 60.0]
)
```

### 13.3 Dashboard Integration

Create Grafana dashboard JSON:

```
dashboards/
└── multi_agent_service/
    ├── contract_health.json      # Contract violations, state transitions
    ├── blackboard_status.json    # Task queue, artifact flow
    ├── peer_review_metrics.json  # Review verdicts, escalations
    └── agent_performance.json    # Processing times, token usage
```

**Dashboard Panels**:
| Panel | Type | Query |
|-------|------|-------|
| Violations by Tier | Pie | `sum by (tier) (contract_violations_total)` |
| State Transitions | Graph | `rate(state_transitions_total[5m])` |
| Blackboard Queue Depth | Gauge | `blackboard_tasks{status="pending"}` |
| Review Success Rate | Gauge | `sum(peer_reviews{verdict="approved"}) / sum(peer_reviews)` |
| Agent Latency P99 | Heatmap | `histogram_quantile(0.99, agent_processing_seconds)` |

### 13.4 Health Check Endpoints

```python
# app/api/health.py
@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "multi_agent_service",
        "version": settings.VERSION
    }

@router.get("/health/ready")
async def readiness_check(redis: Redis = Depends(get_redis)):
    """Check if service is ready to accept traffic."""
    checks = {
        "redis": await check_redis(redis),
        "database": await check_database(),
    }
    healthy = all(checks.values())
    return {"ready": healthy, "checks": checks}

@router.get("/health/live")
async def liveness_check():
    """Check if service is alive."""
    return {"alive": True}
```

### 13.5 Implementation Checklist

| Task | Status |
|------|--------|
| Add `app/observability.py` with OTel setup | ✅ |
| Add `app/metrics.py` with Prometheus metrics | ✅ |
| Instrument key operations with spans | ✅ |
| Create Grafana dashboard JSONs | ✅ |
| Add `/metrics` endpoint | ✅ |
| Update health check endpoints | ✅ |
| Add to observability_service discovery | ⬜ |

---

## Phase 14: Testing Strategy

### 14.1 Test Structure

All tests located in centralized `tests/` folder per project rules:

```
tests/
├── multi_agent_service/
│   ├── __init__.py
│   ├── conftest.py                    # Shared fixtures
│   │
│   ├── unit/
│   │   ├── test_state_machine.py      # State transitions, forbidden paths
│   │   ├── test_tier_rules.py         # Rule enforcement per tier
│   │   ├── test_contract_enforcer.py  # Hard stop triggers
│   │   ├── test_blackboard_ops.py     # Blackboard operations
│   │   ├── test_peer_review.py        # Adversarial pairing
│   │   └── test_skills.py             # Skill application
│   │
│   ├── integration/
│   │   ├── test_agent_invocation.py   # End-to-end agent calls
│   │   ├── test_blackboard_flow.py    # Task → Artifact → Review
│   │   ├── test_session_lifecycle.py  # Session create → complete
│   │   └── test_failure_modes.py      # Failure mode detection
│   │
│   └── scenarios/
│       ├── test_hello_diagnostic.py   # Hello protocol validation
│       ├── test_struggle_protocol.py  # Struggle signaling
│       └── test_contract_violations.py # Violation → RESET flow
```

### 14.2 Simulator Integration

Per project rules, all tests use the simulator service:

```python
# tests/multi_agent_service/conftest.py
import pytest
from tests.mocks.app.simulator import SimulatorService

@pytest.fixture
async def simulator():
    """Provide simulator service for test data."""
    sim = SimulatorService()
    await sim.initialize()
    yield sim
    await sim.cleanup()

@pytest.fixture
async def simulated_session(simulator):
    """Create a simulated agent session."""
    return await simulator.create_session(
        session_type="multi_agent",
        agents=["coordinator", "architect", "developer", "tester"]
    )

@pytest.fixture
async def simulated_task(simulator, simulated_session):
    """Create a simulated blackboard task."""
    return await simulator.create_task(
        session_id=simulated_session.id,
        title="Design entity schema",
        done_when=["Schema validated", "Tests pass", "Peer reviewed"]
    )
```

### 14.3 Contract Enforcement Tests

```python
# tests/multi_agent_service/unit/test_state_machine.py
import pytest
from multi_agent_service.app.contracts.state_machine import AgentContract, AgentState

class TestForbiddenTransitions:
    """Verify forbidden transitions are blocked."""
    
    @pytest.mark.parametrize("from_state,to_state", [
        (AgentState.ANALYSIS, AgentState.EXECUTION),      # Skip approval
        (AgentState.EXECUTION, AgentState.DONE),          # Skip validation
        (AgentState.IDLE, AgentState.DONE),               # Skip everything
    ])
    async def test_forbidden_transition_blocked(self, from_state, to_state):
        contract = AgentContract("test_agent", "session_1")
        contract.state = from_state
        
        with pytest.raises(ValueError, match="Forbidden transition"):
            await contract.transition_to(to_state)
    
    async def test_valid_transition_allowed(self):
        contract = AgentContract("test_agent", "session_1")
        contract.state = AgentState.IDLE
        
        result = await contract.transition_to(AgentState.ANALYSIS)
        assert result is True
        assert contract.state == AgentState.ANALYSIS


class TestHardStopTriggers:
    """Verify hard stop triggers fire correctly."""
    
    async def test_assumption_overflow(self, simulator):
        enforcer = ContractEnforcer()
        
        for i in range(3):
            enforcer.add_assumption(f"Assumption {i}")
        
        trigger = enforcer.check_triggers()
        assert trigger == HardStopTrigger.ASSUMPTION_OVERFLOW
    
    async def test_repeated_fix_detected(self, simulator):
        enforcer = ContractEnforcer()
        
        enforcer.record_fix("Add null check to validate()")
        enforcer.record_fix("Add null check to validate()")  # Same fix
        
        trigger = enforcer.check_triggers()
        assert trigger == HardStopTrigger.REPEATED_FIX
```

### 14.4 Blackboard Integration Tests

```python
# tests/multi_agent_service/integration/test_blackboard_flow.py
import pytest

class TestBlackboardTaskFlow:
    """Test complete task lifecycle through blackboard."""
    
    async def test_task_creation_to_completion(self, simulated_session, simulator):
        # Create task
        task = await blackboard.create_task(
            session_id=simulated_session.id,
            title="Implement user entity",
            done_when=["Schema created", "Tests written", "Reviewed"]
        )
        assert task.status == "open"
        
        # Claim task
        claimed = await blackboard.claim_task(
            task_id=task.id,
            agent_role="developer"
        )
        assert claimed.status == "in_progress"
        assert claimed.assigned_to == "developer"
        
        # Submit artifact
        artifact = await blackboard.submit_artifact(
            task_id=task.id,
            artifact_type="schema",
            content={"name": "User", "fields": [...]}
        )
        assert artifact.status == "pending_review"
        
        # Peer review (by designated reviewer)
        review = await blackboard.submit_review(
            artifact_id=artifact.id,
            reviewer_role="architect",  # Developer's reviewer
            verdict="approved"
        )
        assert review.verdict == "approved"
        
        # Verify task completion
        task = await blackboard.get_task(task.id)
        assert task.status == "done"
```

### 14.5 Hello Diagnostic Test

```python
# tests/multi_agent_service/scenarios/test_hello_diagnostic.py
import pytest

class TestHelloDiagnostic:
    """Test the Hello protocol for agent viability."""
    
    @pytest.mark.parametrize("agent_role", [
        "coordinator", "architect", "developer", "tester",
        "business_analyst", "data_analyst", "documenter"
    ])
    async def test_agent_passes_hello(self, agent_role, simulator):
        runner = HelloDiagnosticRunner(simulator)
        
        result = await runner.run_diagnostic(
            agent_role=agent_role,
            session_id="test_session"
        )
        
        assert result.viable is True
        assert result.score >= 0.7
        assert result.contract_acknowledged is True
        assert result.state_machine_working is True
```

### 14.6 Test Results Location

Per project rules, all test results go to `test_results/`:

```
test_results/
├── multi_agent_contract_test_{timestamp}.json
├── multi_agent_contract_test_{timestamp}.md
├── blackboard_integration_test_{timestamp}.json
└── hello_diagnostic_test_{timestamp}.json
```

### 14.7 Implementation Checklist

| Task | Status |
|------|--------|
| Create `tests/multi_agent_service/conftest.py` | ✅ |
| Create unit tests for state machine | ✅ |
| Create unit tests for tier rules | ⬜ |
| Create unit tests for contract enforcer | ✅ |
| Create integration tests for blackboard | ✅ |
| Create scenario tests for hello diagnostic | ✅ |
| Create scenario tests for failure modes | ⬜ |
| Integrate with simulator service | ✅ |

---

## Phase 15: Rollback & Graceful Degradation

### 15.1 Graceful Degradation Strategy

When `multi_agent_service` is unavailable, `conversation_service` should degrade gracefully:

```python
# conversation_service/app/agents/multi_agent_client.py

class MultiAgentServiceClient:
    """Client with graceful degradation support."""
    
    def __init__(self, base_url: str, fallback_enabled: bool = True):
        self.base_url = base_url
        self.fallback_enabled = fallback_enabled
        self._circuit_breaker = CircuitBreaker(
            failure_threshold=3,
            recovery_timeout=60
        )
    
    async def invoke_agent_with_fallback(
        self,
        session_id: str,
        agent_role: str,
        message: str,
        context: Dict[str, Any]
    ) -> AgentResponse:
        """Invoke agent with fallback to local execution."""
        try:
            if self._circuit_breaker.is_open:
                raise ServiceUnavailable("Circuit breaker open")
            
            return await self._invoke_via_service(
                session_id, agent_role, message, context
            )
        except (httpx.HTTPError, ServiceUnavailable) as e:
            self._circuit_breaker.record_failure()
            
            if self.fallback_enabled:
                logger.warning(
                    f"multi_agent_service unavailable, using local fallback: {e}"
                )
                return await self._invoke_local_fallback(
                    session_id, agent_role, message, context
                )
            raise
    
    async def _invoke_local_fallback(
        self,
        session_id: str,
        agent_role: str,
        message: str,
        context: Dict[str, Any]
    ) -> AgentResponse:
        """Execute agent locally without contract enforcement."""
        # Use existing BaseAgent infrastructure
        # Announce degraded mode
        return AgentResponse(
            content=f"[DEGRADED MODE] Processing without contract enforcement...",
            degraded=True,
            reason="multi_agent_service_unavailable"
        )
```

### 15.2 Circuit Breaker Pattern

```python
# conversation_service/app/agents/circuit_breaker.py

class CircuitBreaker:
    """Circuit breaker for multi_agent_service calls."""
    
    def __init__(
        self,
        failure_threshold: int = 3,
        recovery_timeout: int = 60
    ):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time: Optional[datetime] = None
        self.state = "closed"  # closed, open, half-open
    
    @property
    def is_open(self) -> bool:
        if self.state == "open":
            # Check if recovery timeout has passed
            if self._recovery_timeout_elapsed():
                self.state = "half-open"
                return False
            return True
        return False
    
    def record_failure(self):
        self.failure_count += 1
        self.last_failure_time = datetime.utcnow()
        
        if self.failure_count >= self.failure_threshold:
            self.state = "open"
            logger.error(
                f"Circuit breaker opened after {self.failure_count} failures"
            )
    
    def record_success(self):
        self.failure_count = 0
        self.state = "closed"
```

### 15.3 Degraded Mode Announcements

When operating in degraded mode, agents must announce:

```python
DEGRADED_MODE_ANNOUNCEMENT = """
⚠️ DEGRADED MODE ACTIVE

The following contract features are suspended:
- Peer review (self-review allowed temporarily)
- State machine enforcement
- Blackboard audit logging

Tier 0 rules remain in effect:
- Never fabricate success
- Never modify tests to pass
- Signal when stuck

Reason: {reason}
Expected recovery: {expected_recovery}
"""
```

### 15.4 Data Migration Strategy

For existing sessions when upgrading:

```python
# scripts/migrate_sessions_to_blackboard.py

async def migrate_existing_sessions():
    """Migrate active sessions from context.artifacts to blackboard."""
    
    # 1. Get all active sessions from conversation_service
    sessions = await get_active_sessions()
    
    for session in sessions:
        # 2. Extract artifacts from context
        artifacts = session.context.artifacts
        
        # 3. Create blackboard session
        blackboard_session = await blackboard.create_session(
            session_id=session.id,
            agents=extract_agent_roles(artifacts)
        )
        
        # 4. Migrate peer_collaborations to audit_log
        if "peer_collaborations" in artifacts:
            for collab in artifacts["peer_collaborations"]:
                await blackboard.add_audit_entry(
                    session_id=session.id,
                    entry_type="collaboration",
                    data=collab,
                    migrated=True
                )
        
        # 5. Migrate agent_ready_signals to task status
        if "agent_ready_signals" in artifacts:
            for signal in artifacts["agent_ready_signals"]:
                await blackboard.update_agent_status(
                    session_id=session.id,
                    agent_role=signal["agent"],
                    status="ready",
                    migrated=True
                )
        
        logger.info(f"Migrated session {session.id} to blackboard")
```

### 15.5 Rollback Procedure

If issues are detected after deployment:

```yaml
# Rollback Steps
rollback_procedure:
  trigger_conditions:
    - Error rate > 5% for 5 minutes
    - Circuit breaker opens for > 50% of conversation_service instances
    - P99 latency > 30 seconds
  
  steps:
    1. Set MULTI_AGENT_SERVICE_ENABLED=false in conversation_service
    2. conversation_service falls back to local agent execution
    3. Existing blackboard sessions marked as "migrated_back"
    4. Context artifacts restored from blackboard audit log
    5. Alert on-call team
    6. Investigate root cause
  
  recovery:
    1. Fix identified issues
    2. Deploy fix to multi_agent_service
    3. Run hello diagnostic on all agents
    4. Gradually enable via feature flag (10% → 50% → 100%)
    5. Monitor error rates and latency
```

### 15.6 Feature Flags

```python
# conversation_service/app/config.py

class FeatureFlags:
    """Feature flags for gradual rollout."""
    
    # Master switch for multi_agent_service integration
    MULTI_AGENT_SERVICE_ENABLED: bool = env.bool(
        "MULTI_AGENT_SERVICE_ENABLED", True
    )
    
    # Percentage of sessions to route through blackboard
    BLACKBOARD_ROLLOUT_PERCENT: int = env.int(
        "BLACKBOARD_ROLLOUT_PERCENT", 100
    )
    
    # Enable contract enforcement (can disable for debugging)
    CONTRACT_ENFORCEMENT_ENABLED: bool = env.bool(
        "CONTRACT_ENFORCEMENT_ENABLED", True
    )
    
    # Enable peer review requirement
    PEER_REVIEW_REQUIRED: bool = env.bool(
        "PEER_REVIEW_REQUIRED", True
    )
```

### 15.7 Implementation Checklist

| Task | Status |
|------|--------|
| Implement `CircuitBreaker` class | ✅ |
| Add fallback logic to `MultiAgentServiceClient` | ✅ |
| Create degraded mode announcements | ✅ |
| Create session migration script | ⬜ |
| Document rollback procedure | ✅ |
| Add feature flags to config | ✅ |
| Create rollback runbook | ⬜ |

---

## Implementation Summary

### Phase Status Overview

| Phase | Description | Status |
|-------|-------------|--------|
| 1 | Contract Foundation | ✅ Implemented |
| 2 | Role-Specific Contracts | ✅ Implemented |
| 3 | Blackboard Architecture | ✅ Implemented |
| 4 | Three-Way Pairing | ✅ Implemented |
| 5 | Peer Review Architecture | ✅ Implemented |
| 6 | Collaboration Modes & Protocols | ✅ Implemented |
| 7 | Skills | ✅ Implemented |
| 8 | Failure Mode Coverage | ✅ Implemented |
| 9 | Agent Performance Dashboard | ✅ Implemented |
| 10 | Integration Points | ✅ Implemented |
| 11 | Conversation Service Integration | ✅ Implemented |
| 12 | Infrastructure | ✅ Implemented |
| 13 | Observability Integration | ⚠️ Partial |
| 14 | Testing Strategy | ✅ Implemented |
| 15 | Rollback & Graceful Degradation | ✅ Implemented |

### Recommended Implementation Order

1. **Phase 12** (Infrastructure) - Required for deployment
2. **Phase 14** (Testing) - Verify before integration
3. **Phase 11** (Conversation Service Integration) - Core migration
4. **Phase 13** (Observability) - Monitor the integration
5. **Phase 15** (Rollback) - Safety net for production

---

## Phase 16: Conversation Service Complete Refactoring

### 16.1 Legacy Pattern Analysis

The current `conversation_service` has the following legacy patterns that must be refactored:

| Component | Legacy Pattern | Target Pattern |
|-----------|---------------|----------------|
| `base_agent.py` | Direct peer-to-peer calls via `_consult_peer()` | Blackboard task creation via `multi_agent_service` |
| `base_agent.py` | In-memory `_collaboration_log` | Persistent audit log in `multi_agent_service` |
| `orchestrator.py` | Direct agent initialization in `_sub_agents` dict | Agent registry via `multi_agent_service` contracts |
| `orchestrator.py` | `_setup_peer_connections()` hardcoded pairs | Adversarial pairing from `multi_agent_service` |
| `coordinator.py` | Direct sub-agent delegation via `set_sub_agent()` | Blackboard task assignment |
| `tools.py` | HTTP calls to services | Retain (event-driven architecture preserved) |
| `agents_api.py` | Session management in-memory | Session state via blackboard |

### 16.2 Refactoring Scope

#### 16.2.1 Files to Refactor

```
conversation_service/app/agents/
├── base_agent.py           # ~1100 lines → Add BlackboardAgentMixin integration
├── coordinator.py          # ~2300 lines → Replace delegation with blackboard tasks  
├── orchestrator.py         # ~820 lines → Use multi_agent_service for agent coordination
├── sub_agents.py           # ~317K bytes → Add contract adapter to each agent
├── business_agents.py      # ~340K bytes → Add contract adapter to each agent
├── tools.py                # ~34K bytes → Preserve (event-driven for external services)
├── contract_adapter.py     # Already created - needs wiring
├── blackboard_mixin.py     # Already created - needs wiring
├── multi_agent_client.py   # Already created - needs wiring
└── circuit_breaker.py      # Already created - in use
```

#### 16.2.2 Key Refactoring Tasks

**Task 1: Wire BlackboardAgentMixin into BaseAgent**
```python
# base_agent.py - Before
class BaseAgent(ABC):
    def __init__(self, config, api_key=None, mcp_manager=None):
        ...

# base_agent.py - After
class BaseAgent(BlackboardAgentMixin, ABC):
    def __init__(self, config, api_key=None, mcp_manager=None):
        ...
        self._init_blackboard(session_id)
```

**Task 2: Replace _consult_peer with Blackboard Consultation**
```python
# base_agent.py - Before
async def _consult_peer(self, tool_input, context):
    peer_agent = self._peers[peer_role]
    response = await peer_agent.process(consultation_msg, context)
    ...

# base_agent.py - After  
async def _consult_peer(self, tool_input, context):
    # Use blackboard for coordination
    return await self.consult_peer_via_blackboard(
        peer_role=tool_input["peer_role"],
        question=tool_input["question"],
        context_summary=tool_input["context_summary"]
    )
```

**Task 3: Replace Direct Delegation with Blackboard Tasks**
```python
# coordinator.py - Before
async def delegate_to_agent(self, agent_name, task, context):
    agent = self._sub_agents.get(agent_name)
    return await agent.process(task, context)

# coordinator.py - After
async def delegate_to_agent(self, agent_name, task, context):
    # Create task on blackboard
    task_response = await self._multi_agent_client.create_task(
        session_id=context.session_id,
        title=f"Task for {agent_name}",
        description=task,
        done_when=["Task completed", "Peer reviewed"],
        creator_role="coordinator"
    )
    # Agent claims and processes via blackboard subscription
    return await self._wait_for_task_completion(task_response.id)
```

**Task 4: Add Contract Enforcement to Agent Processing**
```python
# base_agent.py - Before
async def process(self, message: str, context: AgentContext) -> AgentResponse:
    # Direct processing
    ...

# base_agent.py - After
async def process(self, message: str, context: AgentContext) -> AgentResponse:
    # Check contract compliance before processing
    if not await self.check_contract_compliance("process"):
        return AgentResponse(
            agent_role=self.config.role,
            content="[HARD STOP] Contract violation detected",
            success=False
        )
    
    # Transition state
    await self.transition_state("analysis", "Starting task analysis")
    
    # Process with contract enforcement
    ...
```

**Task 5: Update Orchestrator Initialization**
```python
# orchestrator.py - Before
async def initialize(self):
    self._sub_agents = {
        "architect": ArchitectAgent(api_key=api_key),
        ...
    }
    self._setup_peer_connections()

# orchestrator.py - After
async def initialize(self):
    # Initialize multi_agent_service client
    self._multi_agent_client = MultiAgentServiceClient()
    
    # Register agents with multi_agent_service
    for role in AgentRole:
        await self._multi_agent_client.register_agent(role.value)
    
    # Local agents for fallback only
    self._sub_agents = {...}  # Retained for degraded mode
```

### 16.3 Preserved Event-Driven Architecture

The following components **MUST NOT** be refactored to use blackboard:

| Component | Reason |
|-----------|--------|
| `tools.py` - `PublishEventTool` | External service communication |
| `tools.py` - HTTP service calls | Service-to-service integration |
| `base_agent.py` - `_call_external_service()` | Redis pub/sub for external services |
| `orchestrator.py` - `_setup_external_service_messaging()` | Event-driven architecture |

### 16.4 Migration Strategy

#### Step 1: Feature Flag Rollout
```python
# config.py
MULTI_AGENT_SERVICE_ENABLED = env.bool("MULTI_AGENT_SERVICE_ENABLED", False)
BLACKBOARD_ROLLOUT_PERCENT = env.int("BLACKBOARD_ROLLOUT_PERCENT", 0)
CONTRACT_ENFORCEMENT_ENABLED = env.bool("CONTRACT_ENFORCEMENT_ENABLED", False)
```

#### Step 2: Gradual Migration Path
```
Week 1: BLACKBOARD_ROLLOUT_PERCENT=10, CONTRACT_ENFORCEMENT_ENABLED=False
Week 2: BLACKBOARD_ROLLOUT_PERCENT=25, CONTRACT_ENFORCEMENT_ENABLED=False  
Week 3: BLACKBOARD_ROLLOUT_PERCENT=50, CONTRACT_ENFORCEMENT_ENABLED=True
Week 4: BLACKBOARD_ROLLOUT_PERCENT=100, CONTRACT_ENFORCEMENT_ENABLED=True
```

#### Step 3: Session-Level Migration
```python
async def should_use_blackboard(session_id: str) -> bool:
    """Determine if session should use blackboard based on rollout."""
    if not MULTI_AGENT_SERVICE_ENABLED:
        return False
    
    # Hash session ID for consistent routing
    session_hash = hash(session_id) % 100
    return session_hash < BLACKBOARD_ROLLOUT_PERCENT
```

### 16.5 New File Structure

After refactoring, the agents directory should look like:

```
conversation_service/app/agents/
├── __init__.py                   # Updated exports
├── base_agent.py                 # Refactored with BlackboardAgentMixin
├── blackboard_mixin.py           # ✅ Already created
├── circuit_breaker.py            # ✅ Already created
├── contract_adapter.py           # ✅ Already created - wire to agents
├── coordinator.py                # Refactored for blackboard delegation
├── multi_agent_client.py         # ✅ Already created
├── orchestrator.py               # Refactored initialization
├── sub_agents.py                 # Add contract adapters
├── business_agents.py            # Add contract adapters
├── tools.py                      # Preserved (event-driven)
└── config.py                     # New - feature flags and settings
```

### 16.6 API Changes

#### 16.6.1 New Endpoints Required

```python
# agents_api.py additions

@router.get("/{session_id}/blackboard/tasks")
async def get_session_tasks(session_id: str):
    """Get all tasks on the blackboard for a session."""

@router.get("/{session_id}/blackboard/artifacts")  
async def get_session_artifacts(session_id: str):
    """Get all artifacts submitted for a session."""

@router.get("/{session_id}/contract-status")
async def get_contract_status(session_id: str):
    """Get contract compliance status for all agents in session."""

@router.get("/{session_id}/agent/{agent_role}/state")
async def get_agent_state(session_id: str, agent_role: str):
    """Get current state machine state for an agent."""
```

#### 16.6.2 WebSocket Message Types

Add new WebSocket message types for contract events:

```typescript
// agentsApi.ts additions
export type WSMessageType = 
  | 'connected'
  | 'processing'
  | 'chunk'
  | 'complete'
  // New contract-related types
  | 'contract_violation'      // Agent violated a rule
  | 'state_transition'        // Agent changed state
  | 'peer_review_required'    // Artifact needs review
  | 'peer_review_complete'    // Review completed
  | 'struggle_signal'         // Agent signaled struggle
  | 'hard_stop'               // Contract hard stop triggered
  | 'degraded_mode';          // Degraded mode activated
```

### 16.7 Implementation Checklist

| Task | Status |
|------|--------|
| Wire `BlackboardAgentMixin` into `BaseAgent` | ✅ |
| Replace `_consult_peer()` with blackboard consultation | ✅ |
| Replace `_signal_ready_for_coordinator()` with blackboard | ✅ |
| Add `ContractAdapter` to each sub-agent | ✅ |
| Refactor `StrategyCoordinator` delegation | ✅ |
| Refactor `AgentOrchestrator` initialization | ✅ |
| Add feature flag configuration | ✅ |
| Implement session-level migration routing | ✅ |
| Add new API endpoints for blackboard access | ✅ |
| Add new WebSocket message types | ✅ |
| Update `agents_api.py` for contract status | ✅ |
| Preserve `tools.py` event-driven patterns | ✅ |
| Update `__init__.py` exports | ✅ |
| Create migration runbook | ✅ |

---

## Phase 17: UI Integration Validation

### 17.1 Overview

This phase validates that the `demo_config_ui` frontend works correctly with the refactored `conversation_service` and the new `multi_agent_service`. It includes comprehensive E2E testing of the full stack.

### 17.2 UI Components Affected

| Component | File | Integration Points |
|-----------|------|-------------------|
| ConversationServicePage | `pages/ConversationServicePage.tsx` | WebSocket, REST APIs, agent activity display |
| agentsApi | `api/agentsApi.ts` | API client, WebSocket connection |
| AnalyticsDemoPage | `pages/AnalyticsDemoPage.tsx` | Dashboard integration |
| StrategyCenterPage | `pages/StrategyCenterPage.tsx` | Session management |

### 17.3 New UI Features Required

#### 17.3.1 Contract Status Dashboard

Add a contract status panel to `ConversationServicePage`:

```tsx
// New component: ContractStatusPanel.tsx
interface ContractStatusPanelProps {
  sessionId: string;
  agents: AgentContractStatus[];
}

interface AgentContractStatus {
  agentRole: string;
  currentState: string;
  assumptionCount: number;
  failedAttempts: number;
  lastTransition: string;
  contractViolations: number;
}

function ContractStatusPanel({ sessionId, agents }: ContractStatusPanelProps) {
  return (
    <div className="contract-status-panel">
      <h3>Contract Status</h3>
      {agents.map(agent => (
        <AgentStatusRow key={agent.agentRole} agent={agent} />
      ))}
    </div>
  );
}
```

#### 17.3.2 Peer Review Queue Display

```tsx
// New component: PeerReviewQueue.tsx
interface PeerReviewQueueProps {
  sessionId: string;
  pendingReviews: PendingReview[];
  onReviewComplete: (reviewId: string, verdict: string) => void;
}

interface PendingReview {
  artifactId: string;
  artifactType: string;
  creatorRole: string;
  reviewerRole: string;
  submittedAt: Date;
}
```

#### 17.3.3 Struggle Signal Notifications

```tsx
// New component: StruggleNotification.tsx
interface StruggleNotificationProps {
  signal: StruggleSignal;
  onAcknowledge: () => void;
}

interface StruggleSignal {
  agentRole: string;
  signalType: string;
  whatIUnderstand: string;
  whereImStuck: string;
  whatWouldHelp: string;
}
```

### 17.4 WebSocket Integration Updates

Update `agentsApi.ts` to handle new message types:

```typescript
// agentsApi.ts additions

export interface ContractViolationMessage {
  type: 'contract_violation';
  agentRole: string;
  tier: number;
  ruleId: string;
  description: string;
  timestamp: string;
}

export interface StateTransitionMessage {
  type: 'state_transition';
  agentRole: string;
  fromState: string;
  toState: string;
  rationale: string;
  timestamp: string;
}

export interface PeerReviewMessage {
  type: 'peer_review_required' | 'peer_review_complete';
  artifactId: string;
  creatorRole: string;
  reviewerRole: string;
  verdict?: string;
  timestamp: string;
}

export interface StruggleSignalMessage {
  type: 'struggle_signal';
  agentRole: string;
  signalType: string;
  formattedMessage: string;
  timestamp: string;
}

export interface DegradedModeMessage {
  type: 'degraded_mode';
  reason: string;
  suspendedFeatures: string[];
  timestamp: string;
}

// Update WSMessage union type
export type WSMessage = 
  | ConnectedMessage
  | ProcessingMessage
  | ChunkMessage
  | CompleteMessage
  | ContractViolationMessage
  | StateTransitionMessage
  | PeerReviewMessage
  | StruggleSignalMessage
  | DegradedModeMessage;
```

### 17.5 Test Plan

#### 17.5.1 Test Structure

```
tests/
├── multi_agent_service/           # ✅ Already created
├── conversation_service/
│   ├── unit/
│   │   ├── test_blackboard_integration.py
│   │   ├── test_contract_adapter.py
│   │   └── test_multi_agent_client.py
│   └── integration/
│       ├── test_full_interview_flow.py
│       └── test_degraded_mode.py
└── e2e/
    ├── conftest.py
    ├── test_ui_conversation_flow.py
    ├── test_ui_contract_display.py
    ├── test_ui_peer_review.py
    └── test_ui_degraded_mode.py
```

#### 17.5.2 E2E Test Scenarios

**Scenario 1: Full Interview Flow with Contract Enforcement**
```python
# tests/e2e/test_ui_conversation_flow.py

@pytest.mark.e2e
async def test_full_interview_with_contracts(simulator, browser):
    """Test complete interview flow with contract enforcement visible in UI."""
    # 1. Create session via UI
    await browser.goto("/design/interview")
    await browser.click("button[data-testid='new-session']")
    
    # 2. Send initial message
    await browser.fill("textarea[data-testid='message-input']", 
        "We are a manufacturing company...")
    await browser.click("button[data-testid='send']")
    
    # 3. Verify agent activity shows in UI
    await expect(browser.locator("[data-testid='agent-activity']")).to_be_visible()
    
    # 4. Verify contract status panel updates
    await expect(browser.locator("[data-testid='contract-status']")).to_contain_text("analysis")
    
    # 5. Verify peer review notification appears
    await expect(browser.locator("[data-testid='peer-review-badge']")).to_have_text("1")
    
    # 6. Complete interview flow
    # ... additional steps
```

**Scenario 2: Degraded Mode Handling**
```python
# tests/e2e/test_ui_degraded_mode.py

@pytest.mark.e2e
async def test_degraded_mode_notification(simulator, browser, mock_multi_agent_down):
    """Test UI properly shows degraded mode when multi_agent_service unavailable."""
    # 1. Start with multi_agent_service down
    mock_multi_agent_down.activate()
    
    # 2. Create session
    await browser.goto("/design/interview")
    await browser.click("button[data-testid='new-session']")
    
    # 3. Send message
    await browser.fill("textarea[data-testid='message-input']", "Hello")
    await browser.click("button[data-testid='send']")
    
    # 4. Verify degraded mode banner appears
    await expect(browser.locator("[data-testid='degraded-mode-banner']")).to_be_visible()
    await expect(browser.locator("[data-testid='degraded-mode-banner']")).to_contain_text(
        "DEGRADED MODE"
    )
    
    # 5. Verify conversation still works
    await expect(browser.locator("[data-testid='message-list']")).to_contain_text("assistant")
```

**Scenario 3: Struggle Signal Display**
```python
# tests/e2e/test_ui_struggle_signal.py

@pytest.mark.e2e
async def test_struggle_signal_notification(simulator, browser):
    """Test UI displays struggle signals from agents."""
    # 1. Create session with complex task that triggers struggle
    session = await simulator.create_session_with_struggle_trigger()
    
    # 2. Navigate to session
    await browser.goto(f"/design/interview?session={session.id}")
    
    # 3. Trigger the struggle scenario
    await browser.fill("textarea[data-testid='message-input']", 
        simulator.struggle_trigger_message)
    await browser.click("button[data-testid='send']")
    
    # 4. Wait for struggle signal
    await expect(browser.locator("[data-testid='struggle-notification']")).to_be_visible(
        timeout=30000
    )
    
    # 5. Verify struggle signal content
    notification = browser.locator("[data-testid='struggle-notification']")
    await expect(notification).to_contain_text("SYNC NEEDED")
    await expect(notification).to_contain_text("What I understand")
```

**Scenario 4: Contract Violation Handling**
```python
# tests/e2e/test_ui_contract_violation.py

@pytest.mark.e2e
async def test_contract_violation_display(simulator, browser):
    """Test UI displays contract violations appropriately."""
    # 1. Create session configured to trigger violation
    session = await simulator.create_session_with_violation_trigger()
    
    # 2. Navigate and trigger
    await browser.goto(f"/design/interview?session={session.id}")
    
    # 3. Verify violation notification appears
    await expect(browser.locator("[data-testid='violation-alert']")).to_be_visible()
    
    # 4. Verify violation details
    await expect(browser.locator("[data-testid='violation-tier']")).to_have_text("Tier 0")
```

#### 17.5.3 Integration Test Scenarios

**Scenario 5: Blackboard Task Lifecycle**
```python
# tests/conversation_service/integration/test_full_interview_flow.py

@pytest.mark.integration
async def test_blackboard_task_lifecycle(simulator, multi_agent_client):
    """Test complete task lifecycle through blackboard."""
    # 1. Create session
    session = await simulator.create_session()
    
    # 2. Send message that triggers delegation
    response = await simulator.send_message(
        session.id,
        "Design an entity schema for our customer data"
    )
    
    # 3. Verify task created on blackboard
    tasks = await multi_agent_client.get_session_tasks(session.id)
    assert len(tasks) > 0
    assert tasks[0].status == "in_progress"
    
    # 4. Wait for artifact submission
    artifacts = await simulator.wait_for_artifacts(session.id, timeout=60)
    assert len(artifacts) > 0
    
    # 5. Verify peer review occurred
    reviews = await multi_agent_client.get_session_reviews(session.id)
    assert len(reviews) > 0
    assert reviews[0].verdict == "approved"
```

### 17.6 Simulator Service Integration

Per project rules, all tests use the simulator service:

```python
# tests/e2e/conftest.py

@pytest.fixture
async def simulator():
    """Provide simulator service for E2E tests."""
    from services.business_services.integration_service.simulator import SimulatorService
    
    sim = SimulatorService()
    await sim.initialize()
    yield sim
    await sim.cleanup()

@pytest.fixture
async def browser(playwright):
    """Provide Playwright browser for E2E tests."""
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()
    yield page
    await browser.close()

@pytest.fixture
async def mock_multi_agent_down(simulator):
    """Mock multi_agent_service being unavailable."""
    return simulator.create_service_mock(
        service="multi_agent_service",
        behavior="unavailable"
    )
```

### 17.7 Test Results Location

Per project rules, all test results stored in `test_results/`:

```
test_results/
├── e2e_conversation_flow_{timestamp}.json
├── e2e_conversation_flow_{timestamp}.html    # Playwright trace
├── e2e_degraded_mode_{timestamp}.json
├── e2e_contract_display_{timestamp}.json
├── integration_blackboard_{timestamp}.json
└── screenshots/
    ├── contract_status_panel.png
    ├── peer_review_queue.png
    ├── struggle_notification.png
    └── degraded_mode_banner.png
```

### 17.8 Implementation Checklist

| Task | Status |
|------|--------|
| Create `ContractStatusPanel.tsx` component | ✅ |
| Create `PeerReviewQueue.tsx` component | ✅ |
| Create `StruggleNotification.tsx` component | ✅ |
| Create `DegradedModeBanner.tsx` component | ✅ |
| Update `agentsApi.ts` with new message types | ✅ |
| Update `ConversationServicePage.tsx` WebSocket handler | ✅ |
| Add contract status endpoint to API | ✅ |
| Create E2E test structure in `tests/e2e/` | ✅ |
| Create `test_ui_conversation_flow.py` | ✅ |
| Create `test_ui_degraded_mode.py` | ✅ |
| Create `test_ui_struggle_signal.py` | ✅ |
| Create `test_ui_contract_violation.py` | ✅ |
| Create integration tests for blackboard lifecycle | ✅ |
| Configure Playwright for E2E tests | ✅ |
| Add simulator fixtures for E2E | ✅ |
| Document UI testing procedures | ✅ |

---

## Implementation Summary

### Phase Status Overview

| Phase | Description | Status |
|-------|-------------|--------|
| 1 | Contract Foundation | ✅ Implemented |
| 2 | Role-Specific Contracts | ✅ Implemented |
| 3 | Blackboard Architecture | ✅ Implemented |
| 4 | Three-Way Pairing | ✅ Implemented |
| 5 | Peer Review Architecture | ✅ Implemented |
| 6 | Collaboration Modes & Protocols | ✅ Implemented |
| 7 | Skills | ✅ Implemented |
| 8 | Failure Mode Coverage | ✅ Implemented |
| 9 | Agent Performance Dashboard | ✅ Implemented |
| 10 | Integration Points | ✅ Implemented |
| 11 | Conversation Service Integration | ✅ Implemented |
| 12 | Infrastructure | ✅ Implemented |
| 13 | Observability Integration | ✅ Implemented |
| 14 | Testing Strategy | ✅ Implemented |
| 15 | Rollback & Graceful Degradation | ✅ Implemented |
| 16 | Conversation Service Refactoring | ✅ Implemented |
| 17 | UI Integration Validation | ✅ Implemented |
| 18 | Microsoft Best Practices Integration | ✅ Implemented |
| 19 | Prompt Library Integration | ✅ Implemented |
| 20 | Architecture Migration (conv→multi_agent) | ✅ Implemented |

### Recommended Implementation Order

1. **Phase 12** (Infrastructure) - Required for deployment ✅
2. **Phase 14** (Testing) - Verify before integration ✅
3. **Phase 11** (Conversation Service Integration) - Core migration ✅
4. **Phase 13** (Observability) - Monitor the integration ✅
5. **Phase 15** (Rollback) - Safety net for production ✅
6. **Phase 16** (Conversation Service Refactoring) - Complete refactoring ✅
7. **Phase 17** (UI Integration Validation) - E2E validation ✅
8. **Phase 18** (Microsoft Best Practices) - Enhanced governance and monitoring

---

## Phase 18: Microsoft Best Practices Integration

### 18.1 Overview

This phase incorporates best practices from Microsoft's "Designing Multi-Agent Intelligence" guidance, adding enhanced governance, monitoring, and operational capabilities to the multi-agent framework.

**Reference:** [Microsoft Developer Blog - Designing Multi-Agent Intelligence](https://developer.microsoft.com/blog/designing-multi-agent-intelligence)

### 18.2 Token Consumption Metrics

Track token usage across agents and sessions to control costs and monitor performance.

```python
# metrics.py additions
from prometheus_client import Counter, Histogram

token_consumption_total = Counter(
    "multi_agent_token_consumption_total",
    "Total tokens consumed by agents",
    ["agent_role", "model", "token_type"]  # token_type: input, output
)

token_consumption_per_session = Counter(
    "multi_agent_session_token_consumption_total",
    "Tokens consumed per session",
    ["session_id", "agent_role"]
)

token_cost_estimate = Counter(
    "multi_agent_token_cost_estimate_usd",
    "Estimated cost in USD",
    ["agent_role", "model"]
)
```

### 18.3 Agent Versioning State Machine

Formal versioning states for agents to prevent breaking changes.

```python
class AgentVersionState(str, Enum):
    """Agent lifecycle states for versioning."""
    DRAFT = "draft"          # In development
    TESTING = "testing"      # Under validation
    PUBLISHED = "published"  # Production ready
    DEPRECATED = "deprecated"  # Scheduled for removal
    ARCHIVED = "archived"    # No longer available

class AgentVersionTransition:
    """Valid state transitions for agent versions."""
    VALID_TRANSITIONS = {
        ("draft", "testing"),
        ("testing", "published"),
        ("testing", "draft"),
        ("published", "deprecated"),
        ("deprecated", "archived"),
        ("deprecated", "published"),  # Rollback
    }
```

### 18.4 Dependency and Impact Tracking

Track dependencies on external resources (knowledge bases, services) to detect breaking changes.

```python
@dataclass
class AgentDependencies:
    """Track agent dependencies for impact analysis."""
    agent_role: str
    knowledge_bases: List[str]
    external_services: List[str]
    upstream_agents: List[str]
    downstream_agents: List[str]
    last_verified: datetime
    version_hashes: Dict[str, str]  # resource -> hash
    
    def check_for_changes(self) -> List[str]:
        """Detect changes in dependencies since last verification."""
        pass
```

### 18.5 Self-Registration API

Enable external agents to register themselves with the system.

```python
# Agent registration endpoints
POST /api/v1/registry/agents
{
    "agent_id": "external_agent_001",
    "name": "Custom Analytics Agent",
    "capabilities": ["data_analysis", "reporting"],
    "endpoint": "https://external.example.com/agent",
    "protocol": "a2a",  # Agent-to-Agent protocol
    "metadata": {...}
}

GET /api/v1/registry/agents/{agent_id}/info
DELETE /api/v1/registry/agents/{agent_id}
```

### 18.6 Agent Overlap Detection

Detect overlapping capabilities between agents to prevent redundancy.

```python
def detect_agent_overlap(agents: Dict[str, BaseAgent]) -> List[OverlapWarning]:
    """
    Analyze agents for capability overlap.
    
    Returns warnings when:
    - Two agents have >70% tool overlap
    - System prompts have high semantic similarity
    - Same domains are covered by multiple agents
    """
    pass
```

### 18.7 Implementation Files

| File | Purpose |
|------|---------|
| `multi_agent_service/app/token_tracking.py` | Token consumption tracking |
| `multi_agent_service/app/models/agent_version.py` | Agent versioning model |
| `multi_agent_service/app/models/agent_dependencies.py` | Dependency tracking |
| `multi_agent_service/app/api/registry_routes.py` | Self-registration API |
| `conversation_service/app/agents/overlap_detector.py` | Overlap detection utility |

### 18.8 Implementation Checklist

| Task | Status |
|------|--------|
| Add token consumption metrics to `metrics.py` | ✅ |
| Create token tracking middleware | ✅ |
| Implement `AgentVersionState` enum and transitions | ✅ |
| Add version state to agent registry | ✅ |
| Create `AgentDependencies` model | ✅ |
| Implement dependency change detection | ✅ |
| Add self-registration API endpoints | ✅ |
| Create agent validation for registration | ✅ |
| Implement overlap detection utility | ✅ |
| Add overlap warnings to orchestrator initialization | ✅ |
| Update Grafana dashboard with token metrics | ✅ |
| Document new APIs and models | ✅ |

---

## Phase 19: Prompt Library Integration

**Reference:** [Building a Personal Prompt Library](https://www.shawnewallace.com/2025-11-19-building-a-personal-prompt-library/) and [Introducing prompt-library CLI](https://www.shawnewallace.com/2026-01-12-introducing-prompt-library-cli/)

### 19.1 Overview

Phase 19 integrates prompt library concepts to improve agent development workflow:

1. **Agent Prompt Templates Library** - Centralized, versioned system prompts
2. **Agent Template Scaffolding** - Create new agents from templates
3. **Shared Prompt Fragments** - Reusable prompt components (DRY principle)
4. **Dry-Run Preview Mode** - Preview delegation before execution
5. **Fuzzy Agent Discovery** - Forgiving search for agent capabilities

### 19.2 Agent Prompt Templates Library

Organize agent prompts by scenario for reuse and consistency:

```
prompts/
├── scenarios/
│   ├── supply_chain/
│   │   ├── analyst.md
│   │   ├── operations.md
│   │   └── logistics.md
│   ├── retail_analytics/
│   │   ├── sales.md
│   │   └── inventory.md
│   └── financial_services/
│       ├── accountant.md
│       └── risk.md
├── shared/
│   ├── code_review.md
│   ├── debugging.md
│   ├── contract_rules.md
│   └── collaboration.md
└── templates/
    ├── base_agent.md
    ├── specialist_agent.md
    └── coordinator_agent.md
```

### 19.3 Agent Template Scaffolding

Create new agents quickly from predefined templates:

```python
from multi_agent_service.app.templates import AgentTemplateRegistry

# Create agent from template
config = await template_registry.create_agent(
    template_name="specialist_agent",
    agent_role="supply_chain_analyst",
    customizations={
        "domain_keywords": ["inventory", "logistics"],
        "tools": ["analyze_inventory", "forecast_demand"]
    }
)
```

### 19.4 Shared Prompt Fragments

Reusable prompt components that can be composed:

```python
# Fragment examples
COLLABORATION_FRAGMENT = """
When collaborating with peers:
- Use the blackboard for task coordination
- Signal readiness via contract adapter
- Request peer review for critical decisions
"""

CONTRACT_RULES_FRAGMENT = """
Contract Enforcement Rules:
- Maximum 3 assumptions before escalation
- Maximum 5 failed attempts before struggle signal
- Always validate state transitions
"""
```

### 19.5 Dry-Run Preview Mode

Preview delegation outcomes before execution:

```python
# Preview what will happen
preview = await coordinator.delegate_with_preview(
    task="Analyze inventory levels",
    target_agent="supply_chain_analyst",
    dry_run=True
)
# Returns: PreviewResult with expected actions, no side effects

# Execute if satisfied
result = await coordinator.delegate_with_preview(
    task="Analyze inventory levels",
    target_agent="supply_chain_analyst",
    dry_run=False
)
```

### 19.6 Fuzzy Agent Discovery

Find agents by capability keywords:

```python
# Fuzzy search examples
agents = registry.find_agents("inventory")
# Returns: ["supply_chain_analyst", "operations_manager", "data_analyst"]

agents = registry.find_agents("code review")
# Returns: ["developer", "architect", "tester"]
```

### 19.7 New Files

| File | Purpose |
|------|---------|
| `multi_agent_service/app/templates/prompt_library.py` | Prompt template management |
| `multi_agent_service/app/templates/agent_scaffolder.py` | Agent scaffolding from templates |
| `multi_agent_service/app/templates/prompt_fragments.py` | Shared prompt fragments |
| `multi_agent_service/app/api/template_routes.py` | Template API endpoints |
| `conversation_service/app/agents/dry_run.py` | Dry-run preview implementation |
| `conversation_service/app/agents/fuzzy_discovery.py` | Fuzzy agent search |

### 19.8 Implementation Checklist

| Task | Status |
|------|--------|
| Create prompt library structure | ✅ |
| Implement `PromptLibrary` class | ✅ |
| Create agent template scaffolder | ✅ |
| Define shared prompt fragments | ✅ |
| Add dry-run preview to delegation | ✅ |
| Implement fuzzy agent discovery | ✅ |
| Add template API endpoints | ✅ |
| Update agent registry with fuzzy search | ✅ |
| Add templates to Grafana dashboard | ✅ |
| Document new APIs and usage | ✅ |

---

## Phase 20: Architecture Migration (conversation_service → multi_agent_service)

### 20.1 Overview

This phase corrects the architectural inversion where agent runtime components were placed in the L2 business service (conversation_service) instead of the L1 backend service (multi_agent_service).

### 20.2 Migration Scope

**Components Migrated:**
- `coordinator.py` (103KB) - Strategy coordinator
- `orchestrator.py` (37KB) - Agent lifecycle management
- `contract_adapter.py` (11KB) - Contract enforcement
- `blackboard_mixin.py` (11KB) - Blackboard integration
- `sub_agents.py` (317KB) - 12 technical specialists
- `business_agents.py` (340KB) - 14 business agents
- `tools.py` (34KB) - Agent tools
- `fuzzy_discovery.py` (21KB) - Agent discovery
- `overlap_detector.py` (11KB) - Overlap detection
- `dry_run.py` (16KB) - Delegation preview

**Total: ~950KB migrated**

### 20.3 New Directory Structure

```
multi_agent_service/app/
├── agents/
│   ├── __init__.py              # Exports all agents
│   ├── base_agent.py            # Contract-enabled base
│   ├── contracts.py             # Role contracts
│   ├── contract_adapter.py      # Contract adapter
│   ├── blackboard_mixin.py      # Blackboard mixin
│   ├── coordinator.py           # Strategy coordinator
│   ├── orchestrator.py          # Agent orchestrator
│   ├── sub_agents/              # Technical specialists
│   │   ├── __init__.py
│   │   └── agents.py
│   └── business_agents/         # Business domain
│       ├── __init__.py
│       └── agents.py
├── discovery/
│   ├── __init__.py
│   ├── fuzzy_discovery.py
│   └── overlap_detector.py
├── delegation/
│   ├── __init__.py
│   └── dry_run.py
├── tools/
│   ├── __init__.py
│   └── agent_tools.py
├── blackboard/                  # Existing
├── contracts/                   # Existing
└── templates/                   # Phase 19
```

### 20.4 conversation_service Updates

The conversation_service now acts as a **client** to multi_agent_service:

```
conversation_service/app/agents/
├── __init__.py                  # Thin exports
├── multi_agent_client.py        # HTTP client
├── circuit_breaker.py           # Resilience
└── config.py                    # Feature flags
```

### 20.5 Test Strategy

Comprehensive test strategy documented in `docs/testing/MULTI_AGENT_TEST_STRATEGY.md`:

- **Unit Tests**: Contract adapter, fuzzy discovery, dry-run preview
- **Integration Tests**: Cross-service communication, blackboard operations
- **E2E Tests**: Full workflow validation with Playwright

### 20.6 New Files Created

| File | Purpose |
|------|---------|
| `docs/architecture/AGENT_MIGRATION_PLAN.md` | Migration plan document |
| `docs/testing/MULTI_AGENT_TEST_STRATEGY.md` | Comprehensive test strategy |
| `tests/unit/multi_agent_service/test_contract_adapter.py` | Contract adapter tests |
| `tests/unit/multi_agent_service/test_fuzzy_discovery.py` | Fuzzy discovery tests |
| `tests/integration/test_multi_agent_integration.py` | Integration tests |

### 20.7 Implementation Checklist

| Task | Status |
|------|--------|
| Create migration plan document | ✅ |
| Migrate contract_adapter.py | ✅ |
| Migrate blackboard_mixin.py | ✅ |
| Migrate coordinator.py | ✅ |
| Migrate orchestrator.py | ✅ |
| Migrate sub_agents.py | ✅ |
| Migrate business_agents.py | ✅ |
| Migrate tools.py | ✅ |
| Migrate fuzzy_discovery.py | ✅ |
| Migrate overlap_detector.py | ✅ |
| Migrate dry_run.py | ✅ |
| Update multi_agent_service exports | ✅ |
| Design test strategy | ✅ |
| Implement unit tests | ✅ |
| Implement integration tests | ✅ |

---

## References

1. Vass, T. (2025). "Turning AI Coding Agents into Senior Engineering Peers" - Medium
2. Vass, T. (2026). "I Tried to Kill Vibe Coding. I Built Adversarial Vibe Coding. Without the Vibes." - Medium
3. [Liza Multi-Agent System](https://github.com/liza-mas/liza) - Apache 2.0
4. Millett, S. & Tune, N. "Patterns, Principles, and Practices of Domain-Driven Design" - ISBN: 978-1-118-71470-6
5. MAST - Multi-Agent System Failure Taxonomy (Berkeley, 2025)
6. Microsoft AI Co-Innovation Labs. (2026). "Designing Multi-Agent Intelligence" - [Microsoft Developer Blog](https://developer.microsoft.com/blog/designing-multi-agent-intelligence)
7. Wallace, S. (2025). "Building a Personal Prompt Library" - [shawnewallace.com](https://www.shawnewallace.com/2025-11-19-building-a-personal-prompt-library/)
8. Wallace, S. (2026). "Introducing prompt-library CLI" - [shawnewallace.com](https://www.shawnewallace.com/2026-01-12-introducing-prompt-library-cli/)
