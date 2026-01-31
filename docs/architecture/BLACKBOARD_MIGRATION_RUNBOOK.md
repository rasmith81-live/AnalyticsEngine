# Blackboard Migration Runbook

## Phase 16: Conversation Service Refactoring

This runbook documents the migration from Redis pub/sub peer-to-peer coordination to blackboard-based multi-agent coordination.

---

## Overview

### Before Migration
- Agents communicate via direct peer-to-peer calls (`_consult_peer`)
- Coordination happens through Redis pub/sub
- No contract enforcement
- No state machine tracking

### After Migration
- Agents communicate via blackboard tasks and artifacts
- Coordination happens through `multi_agent_service`
- Contract enforcement with state machines
- Full audit trail and observability

---

## Migration Strategy

### Gradual Rollout

The migration uses feature flags for gradual rollout:

| Flag | Description | Default |
|------|-------------|---------|
| `MULTI_AGENT_SERVICE_ENABLED` | Enable multi-agent service | `true` |
| `BLACKBOARD_ROLLOUT_PERCENT` | Percentage of sessions using blackboard | `0` |
| `CONTRACT_ENFORCEMENT_ENABLED` | Enable contract enforcement | `false` |

### Session-Level Routing

Sessions are routed based on:
1. Feature flag percentage (hash-based consistent routing)
2. Circuit breaker state (fallback to legacy if service unavailable)

```python
from app.agents.config import should_use_blackboard

# Each session gets consistent routing
use_blackboard = should_use_blackboard(session_id)
```

---

## Pre-Migration Checklist

- [ ] `multi_agent_service` deployed and healthy
- [ ] Redis connectivity verified
- [ ] Feature flags configured
- [ ] Monitoring dashboards ready
- [ ] Rollback procedure tested

---

## Migration Steps

### Step 1: Deploy multi_agent_service

```bash
# Deploy multi_agent_service
kubectl apply -f charts/multi_agent_service/

# Verify health
curl http://multi_agent_service:8000/api/v1/health/ready
```

### Step 2: Enable Feature Flags (0% Rollout)

```bash
# Set environment variables
export MULTI_AGENT_SERVICE_ENABLED=true
export BLACKBOARD_ROLLOUT_PERCENT=0
export CONTRACT_ENFORCEMENT_ENABLED=false
```

### Step 3: Gradual Rollout

Increase rollout percentage gradually:

| Day | Rollout % | Monitoring Focus |
|-----|-----------|------------------|
| 1 | 1% | Error rates, latency |
| 2 | 5% | Contract violations, degraded mode triggers |
| 3 | 10% | Peer review completions |
| 4 | 25% | Full workflow completion |
| 5 | 50% | Performance under load |
| 6 | 75% | Edge cases |
| 7 | 100% | Full migration |

### Step 4: Enable Contract Enforcement

After 100% rollout is stable:

```bash
export CONTRACT_ENFORCEMENT_ENABLED=true
```

---

## Rollback Procedure

### Immediate Rollback

```bash
# Disable blackboard routing
export BLACKBOARD_ROLLOUT_PERCENT=0

# Sessions will use legacy peer-to-peer
```

### Circuit Breaker Automatic Rollback

The circuit breaker automatically falls back to legacy mode when:
- `multi_agent_service` is unavailable
- Error rate exceeds threshold
- Latency exceeds threshold

---

## Monitoring

### Key Metrics

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| `multi_agent_blackboard_operations_total` | Blackboard operation count | N/A |
| `multi_agent_contract_violations_total` | Contract violation count | > 10/min |
| `multi_agent_hard_stops_total` | Hard stop count | > 5/min |
| `multi_agent_degraded_mode_active` | Degraded mode active | Any |

### Grafana Dashboard

Dashboard available at: `charts/multi_agent_service/dashboards/multi_agent_service.json`

---

## Troubleshooting

### Service Unavailable

**Symptom:** Sessions falling back to legacy mode

**Check:**
```bash
# Health check
curl http://multi_agent_service:8000/api/v1/health/ready

# Redis connectivity
curl http://multi_agent_service:8000/api/v1/health/detailed
```

### High Contract Violations

**Symptom:** Many Tier 1 violations

**Check:**
- Agent prompts include contract section
- State transitions follow valid paths
- Approval requests properly formed

### Degraded Mode Stuck

**Symptom:** Sessions not recovering from degraded mode

**Resolution:**
```bash
# Restart conversation service pods
kubectl rollout restart deployment/conversation-service
```

---

## Code Changes Summary

### New Files

| File | Purpose |
|------|---------|
| `agents/config.py` | Feature flags and rollout configuration |
| `agents/blackboard_mixin.py` | Blackboard coordination mixin |
| `agents/contract_adapter.py` | Contract enforcement adapter |
| `agents/multi_agent_client.py` | Multi-agent service client |
| `agents/circuit_breaker.py` | Circuit breaker for graceful degradation |

### Modified Files

| File | Changes |
|------|---------|
| `agents/orchestrator.py` | Session blackboard initialization |
| `agents/base_agent.py` | Blackboard-aware peer consultation |
| `agents/__init__.py` | New exports |
| `agents_api.py` | New blackboard access endpoints |

---

## Verification

### Functional Tests

```bash
# Run E2E tests
pytest tests/e2e/ -v --tb=short

# Run blackboard lifecycle tests
pytest tests/e2e/test_ui_conversation_flow.py -v
```

### Load Tests

```bash
# Run load test with blackboard enabled
locust -f tests/load/conversation_load.py --host http://localhost:8026
```

---

## Post-Migration

After successful migration to 100%:

1. Remove legacy peer-to-peer code (optional)
2. Update documentation
3. Archive migration feature flags
4. Update runbooks for new architecture

---

## References

- [Agent Contracts Build Plan](./AGENT_CONTRACTS_BUILD_PLAN.md)
- [Multi-Agent Service API](../api/multi_agent_service.md)
- [Tangi Vass - Turning AI Coding Agents into Senior Engineering Peers](https://medium.com/@tangivass)
