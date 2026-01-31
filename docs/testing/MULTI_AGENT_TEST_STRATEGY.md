# Multi-Agent Service Test Strategy

## Overview

This document outlines the comprehensive test strategy for the multi-agent service architecture after the migration from conversation_service.

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

## 1. Unit Tests

### 1.1 Contract Infrastructure Tests

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

def test_repeated_fix_triggers_hard_stop():
    """Verify repeated fix detection."""
    adapter = ContractAdapter("tester", "session-1")
    adapter.record_fix_attempt("Add null check for user input")
    result = adapter.record_fix_attempt("Add null validation for user input")
    assert result is True  # Similar fix detected
```

### 1.2 Agent Tests

**Location:** `tests/unit/multi_agent_service/agents/`

| Test File | Component | Coverage |
|-----------|-----------|----------|
| `test_base_agent.py` | ContractAgent | Tool invocation, state management |
| `test_coordinator.py` | StrategyCoordinator | Delegation, synthesis |
| `test_orchestrator.py` | AgentOrchestrator | Session lifecycle, parallel execution |
| `test_sub_agents.py` | Technical agents | Role-specific behavior |
| `test_business_agents.py` | Business agents | Domain expertise |

### 1.3 Blackboard Tests

**Location:** `tests/unit/multi_agent_service/blackboard/`

| Test File | Component | Coverage |
|-----------|-----------|----------|
| `test_store.py` | RedisBlackboardStore | CRUD operations, TTL |
| `test_operations.py` | BlackboardOperations | Task/artifact lifecycle |
| `test_models.py` | Task, Artifact models | Validation, serialization |
| `test_audit.py` | AuditLog | Event logging |

### 1.4 Discovery & Delegation Tests

**Location:** `tests/unit/multi_agent_service/discovery/`

| Test File | Component | Coverage |
|-----------|-----------|----------|
| `test_fuzzy_discovery.py` | FuzzyAgentDiscovery | Search accuracy, ranking |
| `test_overlap_detector.py` | AgentOverlapDetector | Overlap detection |
| `test_dry_run.py` | DryRunExecutor | Preview generation |

---

## 2. Integration Tests

### 2.1 Service-to-Service Tests

**Location:** `tests/integration/`

| Test File | Services | Coverage |
|-----------|----------|----------|
| `test_conversation_to_multi_agent.py` | conversation → multi_agent | Client calls, circuit breaker |
| `test_multi_agent_blackboard.py` | multi_agent + Redis | Blackboard persistence |
| `test_agent_orchestration.py` | Orchestrator + Agents | Parallel execution |
| `test_contract_enforcement.py` | Contracts + Agents | Contract flow |

**Key Test Cases:**
```python
@pytest.mark.integration
async def test_conversation_creates_session_via_multi_agent():
    """Verify conversation_service can create session via multi_agent_service."""
    async with httpx.AsyncClient() as client:
        # Create session
        response = await client.post(
            f"{MULTI_AGENT_URL}/agents/sessions",
            json={"user_id": "test-user", "context": {}}
        )
        assert response.status_code == 201
        session = response.json()
        assert "id" in session
        
        # Verify session exists
        get_response = await client.get(
            f"{MULTI_AGENT_URL}/agents/sessions/{session['id']}"
        )
        assert get_response.status_code == 200

@pytest.mark.integration
async def test_circuit_breaker_activates_on_service_failure():
    """Verify circuit breaker enters degraded mode on failures."""
    client = MultiAgentServiceClient()
    
    # Simulate service unavailable
    with patch.object(client, '_make_request', side_effect=ServiceUnavailable):
        result = await client.create_task(...)
        assert result.get("degraded") is True
```

### 2.2 API Contract Tests

**Location:** `tests/integration/api/`

| Test File | Endpoint | Coverage |
|-----------|----------|----------|
| `test_blackboard_api.py` | `/blackboard/*` | Task, artifact CRUD |
| `test_registry_api.py` | `/api/v1/registry/*` | Agent registration |
| `test_template_api.py` | `/api/v1/templates/*` | Scaffolding, fragments |
| `test_health_api.py` | `/health/*` | Readiness, liveness |

---

## 3. End-to-End Tests

### 3.1 UI + Full Stack Tests

**Location:** `tests/e2e/`

| Test File | Scenario | Tools |
|-----------|----------|-------|
| `test_ui_conversation_flow.py` | Full interview session | Playwright |
| `test_ui_contract_violation.py` | Violation handling | Playwright |
| `test_ui_degraded_mode.py` | Graceful degradation | Playwright |
| `test_ui_struggle_signal.py` | Struggle notification | Playwright |
| `test_blackboard_lifecycle.py` | Task/artifact flow | pytest + httpx |

### 3.2 E2E Test Fixtures

```python
# tests/e2e/conftest.py

@pytest.fixture
async def multi_agent_service():
    """Start multi_agent_service for testing."""
    process = await start_service("multi_agent_service", port=8090)
    await wait_for_health(f"http://localhost:8090/health/ready")
    yield "http://localhost:8090"
    await stop_service(process)

@pytest.fixture
async def conversation_service(multi_agent_service):
    """Start conversation_service connected to multi_agent."""
    process = await start_service(
        "conversation_service", 
        port=8092,
        env={"MULTI_AGENT_SERVICE_URL": multi_agent_service}
    )
    await wait_for_health(f"http://localhost:8092/health")
    yield "http://localhost:8092"
    await stop_service(process)

@pytest.fixture
async def browser(playwright):
    """Playwright browser for UI tests."""
    browser = await playwright.chromium.launch(headless=True)
    yield browser
    await browser.close()
```

---

## 4. Performance Tests

### 4.1 Load Tests

**Location:** `tests/performance/`

| Test | Target | SLA |
|------|--------|-----|
| Concurrent sessions | 100 sessions | < 500ms p95 |
| Task throughput | 1000 tasks/min | < 100ms p95 |
| Agent delegation | 50 concurrent | < 1s p95 |

### 4.2 Stress Tests

| Test | Scenario | Expected |
|------|----------|----------|
| Redis unavailable | Blackboard down | Graceful degradation |
| Agent timeout | LLM slow | Circuit breaker activation |
| Memory pressure | Large sessions | OOM prevention |

---

## 5. Contract Verification Tests

### 5.1 State Machine Coverage

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

### 5.2 Tier Rule Verification

```python
@pytest.mark.parametrize("role,tier,violation,expected_action", [
    ("architect", 0, "fabricated_success", "hard_stop"),
    ("developer", 0, "modified_tests", "hard_stop"),
    ("tester", 1, "skipped_review", "warning"),
    ("analyst", 2, "verbose_response", "log"),
])
def test_tier_violations(role, tier, violation, expected_action):
    """Verify tier rules are correctly enforced."""
    enforcer = ContractEnforcer(role)
    result = enforcer.check_violation(tier, violation)
    assert result.action == expected_action
```

---

## 6. Test Data & Fixtures

### 6.1 Simulator Service Integration

All tests use the `simulator_service` for generating test data:

```python
from services.backend_services.integration_service.simulator import (
    SimulatorClient,
    generate_interview_session,
    generate_value_chain_data,
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

### 6.2 Mock LLM Responses

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

## 7. CI/CD Integration

### 7.1 Test Stages

```yaml
# .github/workflows/test.yml
stages:
  - name: Unit Tests
    command: pytest tests/unit -v --cov=services
    timeout: 10m
    
  - name: Integration Tests
    command: pytest tests/integration -v -m integration
    timeout: 15m
    services:
      - redis
      - postgres
      
  - name: E2E Tests
    command: pytest tests/e2e -v -m e2e
    timeout: 20m
    services:
      - multi_agent_service
      - conversation_service
      - redis
      - postgres
```

### 7.2 Coverage Requirements

| Component | Minimum Coverage |
|-----------|------------------|
| contracts/ | 90% |
| agents/ | 80% |
| blackboard/ | 85% |
| api/ | 75% |

---

## 8. Test Execution

### 8.1 Run All Tests

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

### 8.2 Run Specific Test Categories

```powershell
# Contract tests only
pytest tests/unit -v -k "contract"

# Agent tests only
pytest tests/unit -v -k "agent"

# Blackboard tests only
pytest tests/unit -v -k "blackboard"
```

---

## 9. Test Results

Test results are stored in `test_results/` with the following format:

```
test_results/
├── unit_tests_YYYYMMDD_HHMMSS.json
├── integration_tests_YYYYMMDD_HHMMSS.json
├── e2e_tests_YYYYMMDD_HHMMSS.json
└── coverage/
    └── index.html
```

---

## 10. Known Test Limitations

1. **LLM API Costs**: Unit tests mock LLM calls to avoid API costs
2. **Redis Required**: Integration tests require Redis instance
3. **Playwright Setup**: E2E tests require Playwright browsers installed
4. **Simulator Dependency**: Tests rely on simulator service for data generation

---

## References

- [Pytest Documentation](https://docs.pytest.org/)
- [Playwright Python](https://playwright.dev/python/)
- [Contract Testing with Pact](https://pact.io/)
