# UI Testing Procedures

## Phase 17: UI Integration Validation

This document describes the testing procedures for validating the UI integration with the conversation service and multi-agent service.

---

## Overview

The UI testing validates:
1. **Contract Status Display** - Agent states, violations, assumptions
2. **Peer Review Queue** - Pending and completed reviews
3. **Struggle Notifications** - Agent struggle signals
4. **Degraded Mode Banner** - Service unavailability handling
5. **WebSocket Events** - Real-time contract event updates

---

## Prerequisites

### Environment Setup

```bash
# Start services
docker-compose up -d

# Verify services are running
curl http://localhost:8026/health  # conversation_service
curl http://localhost:8090/api/v1/health/ready  # multi_agent_service

# Install Playwright
npm install -D @playwright/test
npx playwright install
```

### Test Data

Tests use the simulator service for consistent test data:

```python
from services.business_services.integration_service.simulator import SimulatorService

simulator = SimulatorService()
await simulator.initialize()
```

---

## Test Categories

### 1. Contract Status Panel Tests

**Location:** `tests/e2e/test_ui_contract_violation.py`

**Test Cases:**
| Test | Description | Expected Result |
|------|-------------|-----------------|
| `test_contract_status_panel_visibility` | Panel appears in UI | Panel shows agent states |
| `test_violation_tier_display` | Tier 0/1/2 badges | Correct color coding |
| `test_agent_state_machine_display` | State indicators | Valid state names |
| `test_violation_count_display` | Per-agent counts | Numeric values |
| `test_assumption_count_display` | Assumption tracking | Warning at 2+, hard stop at 3 |

**Manual Verification:**
1. Open http://localhost:5173/design/interview
2. Trigger a complex task that causes agent work
3. Verify contract status panel shows agent states
4. Check for appropriate color coding

### 2. Peer Review Queue Tests

**Location:** `tests/e2e/test_ui_conversation_flow.py`

**Test Cases:**
| Test | Description | Expected Result |
|------|-------------|-----------------|
| `test_artifacts_display` | Artifacts in UI | Panel shows artifacts |
| `test_parallel_analysis_ui` | Analysis results | Results displayed |

**Manual Verification:**
1. Create a session with complex design task
2. Wait for artifacts to be generated
3. Verify peer review queue shows pending reviews
4. Check completed reviews display correctly

### 3. Struggle Signal Tests

**Location:** `tests/e2e/test_ui_struggle_signal.py`

**Test Cases:**
| Test | Description | Expected Result |
|------|-------------|-----------------|
| `test_struggle_signal_notification` | Signal appears | Notification visible |
| `test_struggle_signal_types` | Different types | Correct icons/colors |
| `test_struggle_signal_acknowledge` | User interaction | Acknowledge button works |
| `test_struggle_signal_content_display` | Full content | All fields shown |

**Triggering Struggle Signals:**
```python
# Use simulator to trigger struggle
session = await simulator.create_session_with_struggle_trigger()
await simulator.send_message(session.id, simulator.struggle_trigger_message)
```

### 4. Degraded Mode Tests

**Location:** `tests/e2e/test_ui_degraded_mode.py`

**Test Cases:**
| Test | Description | Expected Result |
|------|-------------|-----------------|
| `test_degraded_mode_notification` | Banner appears | Yellow warning banner |
| `test_degraded_mode_banner_details` | Feature lists | Suspended/active features |
| `test_degraded_mode_dismissible` | User can dismiss | Banner hides |
| `test_recovery_from_degraded_mode` | Service recovery | Banner disappears |

**Simulating Degraded Mode:**
```bash
# Stop multi_agent_service
docker-compose stop multi_agent_service

# Verify UI shows degraded mode
# Restart service
docker-compose start multi_agent_service
```

---

## Running Tests

### All E2E Tests

```bash
# Run all E2E tests
pytest tests/e2e/ -v --tb=short

# Run with specific marker
pytest tests/e2e/ -v -m e2e

# Run specific test file
pytest tests/e2e/test_ui_conversation_flow.py -v
```

### With Tracing

```bash
# Run with Playwright tracing
pytest tests/e2e/ -v --tracing=on

# View trace
npx playwright show-trace test_results/e2e_trace_*.zip
```

### Headful Mode

```bash
# Run with visible browser
pytest tests/e2e/ -v --headed
```

---

## Test Results

### Output Location

All test results are saved to `test_results/`:

```
test_results/
├── screenshots/
│   ├── test_name_YYYYMMDD_HHMMSS.png
│   └── ...
├── e2e_trace_YYYYMMDD_HHMMSS.zip
├── test_report.html
└── ...
```

### Screenshot on Failure

Screenshots are automatically captured on test failure:

```python
@pytest.fixture(autouse=True)
async def save_test_results(request, browser, test_result_path):
    yield
    if request.node.rep_call.failed:
        await browser.screenshot(path=screenshot_path)
```

---

## Common Issues

### Service Not Available

**Symptom:** Tests fail with connection errors

**Solution:**
```bash
# Check services
docker-compose ps

# Restart if needed
docker-compose restart conversation_service multi_agent_service
```

### WebSocket Connection Failed

**Symptom:** Real-time updates not working

**Solution:**
- Check browser console for WebSocket errors
- Verify CORS configuration
- Check network tab for WS connection

### Flaky Tests

**Symptom:** Tests pass/fail inconsistently

**Solution:**
- Increase timeouts for slow operations
- Add explicit waits for async operations
- Use simulator for consistent test data

---

## CI/CD Integration

### GitHub Actions

```yaml
name: E2E Tests

on: [push, pull_request]

jobs:
  e2e:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Start services
        run: docker-compose up -d
        
      - name: Wait for services
        run: |
          sleep 30
          curl --retry 10 --retry-delay 5 http://localhost:8026/health
          
      - name: Run E2E tests
        run: pytest tests/e2e/ -v --tb=short
        
      - name: Upload results
        uses: actions/upload-artifact@v3
        with:
          name: test-results
          path: test_results/
```

---

## Component Reference

### React Components

| Component | Location | Purpose |
|-----------|----------|---------|
| `ContractStatusPanel` | `src/components/agents/ContractStatusPanel.tsx` | Agent state display |
| `PeerReviewQueue` | `src/components/agents/PeerReviewQueue.tsx` | Review queue |
| `StruggleNotification` | `src/components/agents/StruggleNotification.tsx` | Struggle signals |
| `DegradedModeBanner` | `src/components/agents/DegradedModeBanner.tsx` | Degraded mode |

### API Types

| Type | Location | Purpose |
|------|----------|---------|
| `ContractViolationMessage` | `src/api/agentsApi.ts` | Violation events |
| `StruggleSignalMessage` | `src/api/agentsApi.ts` | Struggle events |
| `DegradedModeMessage` | `src/api/agentsApi.ts` | Degraded mode events |

---

## References

- [Agent Contracts Build Plan](../architecture/AGENT_CONTRACTS_BUILD_PLAN.md)
- [Blackboard Migration Runbook](../architecture/BLACKBOARD_MIGRATION_RUNBOOK.md)
- [Playwright Documentation](https://playwright.dev/docs/intro)
