# Agent Interview Test Plan

## Overview

This test plan validates all agents in the multi-agent system by simulating a CEO interview that is designed to activate each agent based on their specialized capabilities.

## Test Objective

Verify that:
1. All 19 agents can be activated through natural conversation
2. Agents respond appropriately to their domain-specific triggers
3. The Coordinator properly delegates to sub-agents
4. MCP tools (Knowledge Graph, PostgreSQL, Web Search) are invoked correctly
5. Inter-agent communication flows as designed

## Agents Under Test

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

## Mock Interview Script

### Turn 1: Business Introduction
**CEO says:** Introduction to B2B SaaS supply chain company
**Target agents:** coordinator, business_analyst, architect
**Expected actions:**
- Coordinator initializes session context
- Business Analyst identifies industry (B2B SaaS, Supply Chain)
- Architect assesses system scale

### Turn 2: KPI Requirements
**CEO says:** Need KPIs for CAC, LTV, churn, SCOR benchmarking
**Target agents:** librarian_curator, data_analyst, business_strategist
**Expected actions:**
- Librarian Curator searches existing KPI catalog
- Data Analyst designs calculation logic
- Business Strategist aligns metrics to strategy

### Turn 3: Technical Architecture
**CEO says:** Multiple data sources (Salesforce, NetSuite, PostgreSQL, Snowflake), Azure deployment
**Target agents:** architect, developer, deployment_specialist, data_governance_specialist
**Expected actions:**
- Architect designs integration architecture
- Developer proposes schema patterns
- Deployment Specialist plans Azure infrastructure
- Data Governance Specialist defines data policies

### Turn 4: Competitive Intelligence
**CEO says:** Concerned about Coupa, SAP Ariba, Jaggaer - need research
**Target agents:** competitive_analyst, librarian_curator, business_strategist
**Expected actions:**
- Competitive Analyst uses web search MCP
- Librarian Curator researches best practices
- Business Strategist provides positioning advice

### Turn 5: Departmental Analytics
**CEO says:** Sales forecasting, marketing attribution, financial projections
**Target agents:** sales_manager, marketing_manager, accountant, data_scientist
**Expected actions:**
- Sales Manager defines pipeline KPIs
- Marketing Manager designs attribution models
- Accountant specifies financial metrics
- Data Scientist proposes ML models

### Turn 6: UI and Compliance
**CEO says:** Modern UI for operations managers, SOC 2/GDPR compliance
**Target agents:** ui_designer, tester, documenter, data_governance_specialist
**Expected actions:**
- UI Designer proposes dashboard patterns
- Tester outlines compliance testing
- Documenter plans compliance documentation
- Data Governance Specialist maps requirements

### Turn 7: Operations and Planning
**CEO says:** ITIL practices, monitoring, project timeline
**Target agents:** operations_manager, project_manager, deployment_specialist
**Expected actions:**
- Operations Manager aligns to ITIL
- Project Manager creates timeline
- Deployment Specialist plans monitoring

## Test Execution

### API Endpoint
```
POST /api/v1/tests/run
```

### Stream Results
```
GET /api/v1/tests/{test_id}/stream
```

### Get Markdown Report
```
GET /api/v1/tests/{test_id}/markdown
```

## Success Criteria

- [ ] All 19 agents activated at least once
- [ ] 100% coverage of target agents per turn
- [ ] No critical errors during execution
- [ ] Average response time < 5000ms per turn
- [ ] MCP tools invoked for Knowledge Graph, PostgreSQL, Web Search

---

## Test Results

### Test Infrastructure Status: ✅ READY

The test harness is fully implemented and ready to run. **Requires `ANTHROPIC_API_KEY` to be set.**

### Configuration Required

Add to `docker-compose.yml` under `conversation_service` environment:
```yaml
environment:
  - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
```

Or set in `.env` file:
```
ANTHROPIC_API_KEY=sk-ant-...
```

### Running the Test

1. **Start test:**
```powershell
Invoke-RestMethod -Uri "http://localhost:8026/api/v1/tests/run" -Method POST -ContentType "application/json" -Body '{"test_type": "mock_interview"}'
```

2. **Check status:**
```powershell
Invoke-RestMethod -Uri "http://localhost:8026/api/v1/tests/{test_id}/status" -Method GET
```

3. **Get full results:**
```powershell
Invoke-RestMethod -Uri "http://localhost:8026/api/v1/tests/{test_id}/results" -Method GET
```

4. **Get markdown report:**
```powershell
Invoke-RestMethod -Uri "http://localhost:8026/api/v1/tests/{test_id}/markdown" -Method GET
```

### Test Run: 2026-01-23 (Infrastructure Validation)

**Status:** Completed (API Key Required)  
**Test ID:** TEST-20260123-192554  
**Started:** 2026-01-23T19:25:54  
**Completed:** 2026-01-23T19:25:58  

**Issue:** `ANTHROPIC_API_KEY` not configured - LLM calls failed with authentication error.

**Infrastructure Validated:**
- ✅ Test harness endpoint working
- ✅ Session creation successful
- ✅ All 7 interview turns processed
- ✅ Event streaming functional
- ✅ Result aggregation working
- ❌ LLM calls require API key

### Coverage Summary (Pending API Key)
| Metric | Target | Actual |
|--------|--------|--------|
| Agents Activated | 19 | 0* |
| Coverage % | 100% | 0%* |
| Errors | 0 | 0 |

*Requires ANTHROPIC_API_KEY to activate agents

### Files Created

| File | Purpose |
|------|---------|
| `tests/agent_interview_test.py` | Standalone test runner |
| `tests/mock_interview_data.py` | Interview script data |
| `app/api/test_routes.py` | API endpoints for test execution |

### Next Steps

1. Set `ANTHROPIC_API_KEY` in environment
2. Rebuild and restart `conversation_service`
3. Run test: `POST /api/v1/tests/run`
4. Monitor results in real-time via SSE stream
5. View final report via `/api/v1/tests/{id}/markdown`
