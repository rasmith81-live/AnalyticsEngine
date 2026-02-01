# Multi-Agent Testing Guide

This guide provides a comprehensive testing strategy for the multi-agent system, including unit tests, integration tests, E2E tests, and the mock interview test plan.

## Table of Contents

1. [Test Pyramid](#test-pyramid)
2. [Unit Tests](#unit-tests)
3. [Integration Tests](#integration-tests)
4. [End-to-End Tests](#end-to-end-tests)
5. [Performance Tests](#performance-tests)
6. [Mock Interview Test Plan](#mock-interview-test-plan)
7. [Test Execution](#test-execution)
8. [CI/CD Integration](#cicd-integration)

---

## Test Pyramid

```
                ┌─────────────────┐
                │   E2E Tests     │  ← 10% (UI + Full Stack)
                │   (Playwright)  │
                ├─────────────────┤
                │  Integration    │  ← 30% (Service Boundaries)
                │     Tests       │
                ├─────────────────┤
                │   Unit Tests    │  ← 60% (Component Logic)
                │                 │
                └─────────────────┘
```

---

## Unit Tests

### Contract Infrastructure Tests

**Location:** `tests/unit/multi_agent_service/contracts/`

| Test File | Component | Coverage |
|-----------|-----------|----------|
| `test_contract_adapter.py` | ContractAdapter | State transitions, violations, thresholds |
| `test_state_machine.py` | AgentContract | Valid/forbidden transitions |
| `test_tier_rules.py` | ContractRules | Rule evaluation, tier classification |
| `test_violations.py` | ViolationHandler | Violation detection, logging |
| `test_enforcer.py` | ContractEnforcer | Hard stops, struggle signals |

**Key Test Cases:**

```python
def test_forbidden_transition_raises_error():
    """Verify forbidden transitions raise ValueError."""
    adapter = ContractAdapter("architect", "session-1")
    adapter.transition_to("analysis")
    with pytest.raises(ValueError, match="Forbidden transition"):
        adapter.transition_to("done")  # analysis → done is forbidden

def test_assumption_overflow_triggers_hard_stop():
    """Verify 3 assumptions trigger hard stop."""
    adapter = ContractAdapter("developer", "session-1")
    adapter.add_assumption("User wants REST API")
    adapter.add_assumption("Using Python 3.11")
    result = adapter.add_assumption("Database is PostgreSQL")
    assert result is True  # Hard stop triggered
```

### Agent Tests

**Location:** `tests/unit/multi_agent_service/agents/`

| Test File | Component | Coverage |
|-----------|-----------|----------|
| `test_base_agent.py` | ContractAgent | Tool invocation, state management |
| `test_coordinator.py` | StrategyCoordinator | Delegation, synthesis |
| `test_orchestrator.py` | AgentOrchestrator | Session lifecycle, parallel execution |
| `test_sub_agents.py` | Technical agents | Role-specific behavior |
| `test_business_agents.py` | Business agents | Domain expertise |

### Blackboard Tests

**Location:** `tests/unit/multi_agent_service/blackboard/`

| Test File | Component | Coverage |
|-----------|-----------|----------|
| `test_store.py` | RedisBlackboardStore | CRUD operations, TTL |
| `test_operations.py` | BlackboardOperations | Task/artifact lifecycle |
| `test_models.py` | Task, Artifact models | Validation, serialization |
| `test_audit.py` | AuditLog | Event logging |

### State Machine Coverage

```python
@pytest.mark.parametrize("from_state,to_state,expected", [
    ("idle", "analysis", True),
    ("analysis", "approval_pending", True),
    ("analysis", "done", False),  # Forbidden
    ("idle", "execution", False),  # Forbidden
    ("execution", "validation", True),
    ("validation", "done", True),
])
def test_state_transitions(from_state, to_state, expected):
    """Verify all state transitions are correctly enforced."""
    adapter = ContractAdapter("test", "session")
    adapter.state.current_state = from_state
    
    if expected:
        assert adapter.transition_to(to_state)
    else:
        with pytest.raises(ValueError):
            adapter.transition_to(to_state)
```

---

## Integration Tests

### Service-to-Service Tests

**Location:** `tests/integration/`

| Test File | Services | Coverage |
|-----------|----------|----------|
| `test_conversation_to_multi_agent.py` | conversation → multi_agent | Client calls, circuit breaker |
| `test_multi_agent_blackboard.py` | multi_agent + Redis | Blackboard persistence |
| `test_agent_orchestration.py` | Orchestrator + Agents | Parallel execution |
| `test_contract_enforcement.py` | Contracts + Agents | Contract flow |

**Example:**

```python
@pytest.mark.integration
async def test_conversation_creates_session_via_multi_agent():
    """Verify conversation_service can create session via multi_agent_service."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{MULTI_AGENT_URL}/agents/sessions",
            json={"user_id": "test-user", "context": {}}
        )
        assert response.status_code == 201
        session = response.json()
        assert "id" in session
```

### API Contract Tests

**Location:** `tests/integration/api/`

| Test File | Endpoint | Coverage |
|-----------|----------|----------|
| `test_blackboard_api.py` | `/blackboard/*` | Task, artifact CRUD |
| `test_registry_api.py` | `/api/v1/registry/*` | Agent registration |
| `test_template_api.py` | `/api/v1/templates/*` | Scaffolding, fragments |
| `test_health_api.py` | `/health/*` | Readiness, liveness |

---

## End-to-End Tests

### UI + Full Stack Tests

**Location:** `tests/e2e/`

| Test File | Scenario | Tools |
|-----------|----------|-------|
| `test_ui_conversation_flow.py` | Full interview session | Playwright |
| `test_ui_contract_violation.py` | Violation handling | Playwright |
| `test_ui_degraded_mode.py` | Graceful degradation | Playwright |
| `test_ui_struggle_signal.py` | Struggle notification | Playwright |
| `test_blackboard_lifecycle.py` | Task/artifact flow | pytest + httpx |

### E2E Test Fixtures

```python
@pytest.fixture
async def multi_agent_service():
    """Start multi_agent_service for testing."""
    process = await start_service("multi_agent_service", port=8090)
    await wait_for_health(f"http://localhost:8090/health/ready")
    yield "http://localhost:8090"
    await stop_service(process)

@pytest.fixture
async def browser(playwright):
    """Playwright browser for UI tests."""
    browser = await playwright.chromium.launch(headless=True)
    yield browser
    await browser.close()
```

---

## Performance Tests

### Load Tests

**Location:** `tests/performance/`

| Test | Target | SLA |
|------|--------|-----|
| Concurrent sessions | 100 sessions | < 500ms p95 |
| Task throughput | 1000 tasks/min | < 100ms p95 |
| Agent delegation | 50 concurrent | < 1s p95 |

### Stress Tests

| Test | Scenario | Expected |
|------|----------|----------|
| Redis unavailable | Blackboard down | Graceful degradation |
| Agent timeout | LLM slow | Circuit breaker activation |
| Memory pressure | Large sessions | OOM prevention |

---

## Mock Interview Test Plan

### Overview

Validates all agents by simulating a CEO interview designed to activate each agent based on their specialized capabilities.

### Agents Under Test

| Agent | Role | Trigger Topics |
|-------|------|----------------|
| `coordinator` | Master orchestrator | Session management, delegation |
| `architect` | System design | Architecture, integration, scale |
| `business_analyst` | Industry analysis | Business model, processes |
| `data_analyst` | KPI calculations | Set-based metrics, aggregations |
| `developer` | Code generation | Schemas, integrations |
| `tester` | Quality assurance | Testing strategy, validation |
| `documenter` | Documentation | Compliance docs, guides |
| `deployment_specialist` | Infrastructure | Azure, deployment |
| `project_manager` | Planning | Timeline, phases, resources |
| `sales_manager` | Sales metrics | Pipeline, forecasting |
| `accountant` | Financial metrics | Revenue, cash flow |
| `data_governance_specialist` | Compliance | GDPR, SOC2, data quality |
| `data_scientist` | ML/Analytics | Predictive models, ML |
| `marketing_manager` | Marketing metrics | ROI, attribution |
| `ui_designer` | User experience | Dashboards, UX |
| `business_strategist` | Strategy | Positioning, competitive |
| `operations_manager` | Operations | ITIL, monitoring |
| `librarian_curator` | Ontology | KPI catalog, definitions |
| `competitive_analyst` | Competition | Web research, benchmarks |

### Interview Script

| Turn | CEO Topic | Target Agents |
|------|-----------|---------------|
| 1 | Business Introduction | coordinator, business_analyst, architect |
| 2 | KPI Requirements | librarian_curator, data_analyst, business_strategist |
| 3 | Technical Architecture | architect, developer, deployment_specialist, data_governance |
| 4 | Competitive Intelligence | competitive_analyst, librarian_curator, business_strategist |
| 5 | Departmental Analytics | sales_manager, marketing_manager, accountant, data_scientist |
| 6 | UI and Compliance | ui_designer, tester, documenter, data_governance |
| 7 | Operations and Planning | operations_manager, project_manager, deployment_specialist |

### Running the Interview Test

**Prerequisites:** Set `ANTHROPIC_API_KEY` in environment.

```powershell
# Start test
Invoke-RestMethod -Uri "http://localhost:8026/api/v1/tests/run" `
  -Method POST -ContentType "application/json" `
  -Body '{"test_type": "mock_interview"}'

# Check status
Invoke-RestMethod -Uri "http://localhost:8026/api/v1/tests/{test_id}/status"

# Get results
Invoke-RestMethod -Uri "http://localhost:8026/api/v1/tests/{test_id}/results"

# Get markdown report
Invoke-RestMethod -Uri "http://localhost:8026/api/v1/tests/{test_id}/markdown"
```

### Success Criteria

- [ ] All 19 agents activated at least once
- [ ] 100% coverage of target agents per turn
- [ ] No critical errors during execution
- [ ] Average response time < 5000ms per turn
- [ ] MCP tools invoked for Knowledge Graph, PostgreSQL, Web Search

---

## Test Execution

### Run All Tests

```powershell
# Unit tests
pytest tests/unit -v --cov=services --cov-report=html

# Integration tests (requires Redis)
pytest tests/integration -v -m integration

# E2E tests (requires full stack)
pytest tests/e2e -v -m e2e

# Full test suite
pytest tests/ -v --cov=services --cov-report=html
```

### Run Specific Categories

```powershell
# Contract tests only
pytest tests/unit -v -k "contract"

# Agent tests only
pytest tests/unit -v -k "agent"

# Blackboard tests only
pytest tests/unit -v -k "blackboard"
```

---

## CI/CD Integration

### Test Stages

```yaml
stages:
  - name: Unit Tests
    command: pytest tests/unit -v --cov=services
    timeout: 10m
    
  - name: Integration Tests
    command: pytest tests/integration -v -m integration
    timeout: 15m
    services: [redis, postgres]
      
  - name: E2E Tests
    command: pytest tests/e2e -v -m e2e
    timeout: 20m
    services: [multi_agent_service, conversation_service, redis, postgres]
```

### Coverage Requirements

| Component | Minimum Coverage |
|-----------|------------------|
| contracts/ | 90% |
| agents/ | 80% |
| blackboard/ | 85% |
| api/ | 75% |

---

## Test Data & Fixtures

### Simulator Service Integration

All tests use the `simulator_service` for generating test data:

```python
from services.backend_services.integration_service.simulator import (
    SimulatorClient,
    generate_interview_session,
)

@pytest.fixture
def simulator():
    return SimulatorClient()

@pytest.fixture
def sample_session(simulator):
    return simulator.generate_interview_session(
        industry="retail",
        complexity="medium"
    )
```

### Mock LLM Responses

```python
@pytest.fixture
def mock_llm():
    with patch("anthropic.Anthropic") as mock:
        mock.return_value.messages.create.return_value = MockResponse(
            content="Mocked LLM response for testing"
        )
        yield mock
```

---

## Test Results

Results stored in `test_results/`:

```
test_results/
├── unit_tests_YYYYMMDD_HHMMSS.json
├── integration_tests_YYYYMMDD_HHMMSS.json
├── e2e_tests_YYYYMMDD_HHMMSS.json
└── coverage/
    └── index.html
```

---

## Known Limitations

1. **LLM API Costs**: Unit tests mock LLM calls to avoid API costs
2. **Redis Required**: Integration tests require Redis instance
3. **Playwright Setup**: E2E tests require Playwright browsers installed
4. **Simulator Dependency**: Tests rely on simulator service for data generation
