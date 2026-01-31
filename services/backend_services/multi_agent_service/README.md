# Multi-Agent Service

## Attribution

This service is based on the groundbreaking work of **Tangi Vass** on behavioral contracts for AI coding agents.

| Source | Link |
|--------|------|
| "Turning AI Coding Agents into Senior Engineering Peers" | [Medium Article](https://medium.com/@tangi.vass/turning-ai-coding-agents-into-senior-engineering-peers-c3d178621c9e) |
| "Adversarial Vibe Coding Without the Vibes" | [Medium Article](https://medium.com/@tangi.vass/i-tried-to-kill-vibe-coding-i-built-adversarial-vibe-coding-without-the-vibes-bc4a63872440) |
| LIZA: Peer-Supervised Multi-Agent System | [GitHub](https://github.com/liza-mas/liza) |

## Overview

The Multi-Agent Service provides the agent contract infrastructure for the AnalyticsEngine. It implements behavioral constraints, coordination mechanisms, and monitoring for 27+ specialized AI agents.

## Key Features

- **Behavioral Contracts**: Tier-based rules (T0-T3) that constrain agent behavior
- **State Machine**: Explicit states with forbidden transitions
- **Blackboard Architecture**: Shared state for agent coordination (replaces pub/sub)
- **Peer Review**: Adversarial pairing ensures no agent reviews their own work
- **Skills**: Domain-specific contract applications (Testing, Debugging, Systemic Thinking)
- **Self-Monitoring**: Token budget warnings, drift detection, degraded mode announcements
- **Performance Dashboard**: Metrics for trust, cost gradient, and agent effectiveness

## Architecture

```
multi_agent_service/
├── app/
│   ├── agents/           # Agent definitions with contracts
│   ├── blackboard/       # Shared state coordination
│   ├── contracts/        # State machine, tier rules, enforcer
│   ├── dashboard/        # Performance dashboard
│   ├── monitoring/       # Self-monitoring components
│   ├── peer_review/      # Adversarial pairing
│   ├── protocols/        # Hello, Struggle, Magic Phrases
│   ├── skills/           # Domain-specific skills
│   └── api/              # REST API endpoints
```

## Quick Start

### Prerequisites

- Python 3.11+
- Redis (for blackboard persistence)
- PostgreSQL (for audit log)

### Installation

```bash
cd services/backend_services/multi_agent_service
pip install -r requirements.txt
```

### Running

```bash
# Development
uvicorn app.main:app --reload --port 8090

# Production
uvicorn app.main:app --host 0.0.0.0 --port 8090
```

### Docker

```bash
docker build -t multi-agent-service .
docker run -p 8090:8090 multi-agent-service
```

## API Endpoints

### Health
- `GET /health` - Service health check
- `GET /ready` - Readiness check
- `GET /live` - Liveness check

### Agents
- `POST /agents/invoke` - Invoke an agent
- `GET /agents/list` - List all agent roles
- `GET /agents/{role}/contract` - Get agent contract
- `POST /agents/{role}/reset` - Reset agent state

### Blackboard
- `GET /blackboard/{session_id}` - Get blackboard state
- `POST /blackboard/{session_id}/tasks` - Create task
- `POST /blackboard/{session_id}/tasks/{id}/claim` - Claim task
- `POST /blackboard/{session_id}/struggle-signals` - Submit struggle signal
- `GET /blackboard/{session_id}/audit-log` - Get audit log

### Dashboard
- `GET /dashboard/{session_id}/summary` - Get dashboard summary
- `POST /dashboard/{session_id}/hello-diagnostic` - Run hello diagnostic
- `GET /dashboard/{session_id}/token-budget` - Token budget status
- `GET /dashboard/{session_id}/drift` - Drift detection status
- `GET /dashboard/{session_id}/degraded-mode` - Degraded mode status

## Contract Tier System

| Tier | Description | Enforcement |
|------|-------------|-------------|
| **T0** | Safety/Deception Prevention | Never violated - immediate RESET |
| **T1** | Core Workflow | Approval gates, state machine |
| **T2** | Quality Standards | Can be suspended under pressure |
| **T3** | Nice-to-Have | First to be suspended |

## The 27 Agent Roles

### Strategy & Analysis Layer
- Coordinator, Business Strategist, Business Analyst, Data Analyst
- Data Scientist, Operations Manager, Mapping Specialist
- Document Analyzer, Competitive Analyst

### Technical Design Layer
- Architect, Developer, Tester, Documenter
- Deployment Specialist, UI Designer, ITIL Manager, Connection Specialist

### Business Operations Layer
- Sales Manager, Marketing Manager, Accountant
- Customer Success Manager, HR/Talent Analyst, Supply Chain Analyst
- Risk & Compliance Officer, Project Manager

### Governance Layer
- Data Governance Specialist, Process Scenario Modeler, Librarian Curator

## License

Please refer to the [LIZA repository](https://github.com/liza-mas/liza) for licensing terms regarding the behavioral contract concepts.
