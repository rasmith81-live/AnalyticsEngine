# Agent Architecture Migration Plan

## Overview

This document outlines the migration of agent components from `conversation_service` (L2 business service) to `multi_agent_service` (L1 backend service) to correct the architectural inversion.

## Current State

### conversation_service/app/agents/ (≈950KB)
- Contains all 27 agents + coordinator + orchestrator
- Contains contract adapter, blackboard mixin
- Contains Phase 18-19 components (fuzzy_discovery, dry_run, overlap_detector)
- Acts as both the agent runtime AND the conversation interface

### multi_agent_service/app/agents/ (≈40KB)
- Contains abstract base agent with contracts
- Contains role-specific contract definitions
- Exposes only REST API endpoints

## Target State

### multi_agent_service (L1 Backend) - THE AGENT RUNTIME
```
multi_agent_service/app/
├── agents/
│   ├── __init__.py
│   ├── base_agent.py          ← Unified base (merge both versions)
│   ├── coordinator.py         ← Strategy coordinator
│   ├── orchestrator.py        ← Agent lifecycle management
│   ├── sub_agents/            ← Technical specialists (12 agents)
│   │   ├── __init__.py
│   │   ├── architect.py
│   │   ├── developer.py
│   │   ├── tester.py
│   │   ├── documenter.py
│   │   ├── deployment_specialist.py
│   │   ├── project_manager.py
│   │   ├── data_analyst.py
│   │   ├── itil_manager.py
│   │   ├── mapping_specialist.py
│   │   ├── connection_specialist.py
│   │   ├── document_analyzer.py
│   │   └── librarian_curator.py
│   └── business_agents/       ← Business domain agents (14 agents)
│       ├── __init__.py
│       ├── business_strategist.py
│       ├── business_analyst.py
│       ├── sales_manager.py
│       ├── marketing_manager.py
│       ├── accountant.py
│       ├── operations_manager.py
│       ├── data_scientist.py
│       ├── data_governance.py
│       ├── ui_designer.py
│       ├── customer_success.py
│       ├── hr_talent.py
│       ├── supply_chain.py
│       ├── risk_compliance.py
│       ├── competitive_analyst.py
│       └── process_modeler.py
├── discovery/                  ← Agent discovery (Phase 19)
│   ├── __init__.py
│   ├── fuzzy_discovery.py
│   └── overlap_detector.py
├── delegation/                 ← Delegation utilities (Phase 19)
│   ├── __init__.py
│   └── dry_run.py
├── tools/                      ← Agent tools
│   ├── __init__.py
│   └── agent_tools.py
├── blackboard/                 ← Already exists
├── contracts/                  ← Already exists
├── templates/                  ← Already exists (Phase 19)
└── api/
    ├── agent_routes.py
    ├── orchestrator_routes.py  ← NEW: WebSocket for agent sessions
    └── ...
```

### conversation_service (L2 Business) - A CLIENT
```
conversation_service/app/
├── agents/
│   ├── __init__.py             ← Thin exports
│   ├── multi_agent_client.py   ← HTTP/WebSocket client
│   ├── circuit_breaker.py      ← Resilience
│   └── config.py               ← Feature flags
├── engine/                     ← Keep existing
├── models/                     ← Keep existing
└── ...
```

---

## Migration Phases

### Phase 1: Migrate Core Agent Components
**Files to migrate:**
- `contract_adapter.py` → `multi_agent_service/app/agents/contract_adapter.py`
- `blackboard_mixin.py` → `multi_agent_service/app/agents/blackboard_mixin.py`

**Merge:**
- `base_agent.py` (conversation_service) + `base_agent.py` (multi_agent_service)

### Phase 2: Migrate Orchestrator and Coordinator
**Files to migrate:**
- `coordinator.py` → `multi_agent_service/app/agents/coordinator.py`
- `orchestrator.py` → `multi_agent_service/app/agents/orchestrator.py`

### Phase 3: Migrate Specialist Agents
**Files to split and migrate:**
- `sub_agents.py` (317KB) → Split into 12 separate files in `sub_agents/`
- `business_agents.py` (340KB) → Split into 14 separate files in `business_agents/`

### Phase 4: Migrate Phase 18-19 Components
**Files to migrate:**
- `fuzzy_discovery.py` → `multi_agent_service/app/discovery/fuzzy_discovery.py`
- `overlap_detector.py` → `multi_agent_service/app/discovery/overlap_detector.py`
- `dry_run.py` → `multi_agent_service/app/delegation/dry_run.py`

### Phase 5: Migrate Tools
**Files to migrate:**
- `tools.py` → `multi_agent_service/app/tools/agent_tools.py`

### Phase 6: Update conversation_service
- Remove migrated files
- Update imports to use multi_agent_service client
- Add WebSocket client for real-time agent interaction

### Phase 7: Add Orchestrator API
- Add WebSocket endpoint for agent sessions in multi_agent_service
- Expose orchestrator functionality via REST/WebSocket

---

## Execution Order

1. ✅ Create directory structure in multi_agent_service
2. ✅ Migrate contract_adapter.py and blackboard_mixin.py
3. ✅ Merge base_agent.py versions
4. ✅ Migrate coordinator.py and orchestrator.py
5. ✅ Split and migrate sub_agents.py
6. ✅ Split and migrate business_agents.py
7. ✅ Migrate tools.py
8. ✅ Migrate fuzzy_discovery.py and overlap_detector.py
9. ✅ Migrate dry_run.py
10. ⬜ Add orchestrator WebSocket API (future enhancement)
11. ✅ Update conversation_service imports
12. ✅ Remove migrated files from conversation_service
13. ✅ Update build plan documentation
14. ✅ Create integration tests
15. ✅ Add session API endpoints to multi_agent_service

---

## Risk Mitigation

1. **Import Errors**: Update all relative imports to absolute
2. **Circular Dependencies**: Use TYPE_CHECKING guards
3. **Missing Dependencies**: Verify all imports exist in target location
4. **API Changes**: Maintain backward compatibility during transition

---

## Testing Strategy (Post-Migration)

See: `docs/testing/MULTI_AGENT_TEST_STRATEGY.md`
