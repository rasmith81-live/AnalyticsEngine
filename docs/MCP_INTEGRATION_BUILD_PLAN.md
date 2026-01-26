# MCP Integration Build Plan

## Executive Summary

This document outlines the implementation plan for integrating Model Context Protocol (MCP) servers into the AnalyticsEngine multi-agent system. The integration adds three MCP servers:

1. **PostgreSQL MCP** - Database introspection and query capabilities for TimescaleDB
2. **Knowledge Graph MCP** - Ontology, value chain, and relationship management
3. **Web Search MCP** - External competitive intelligence and research

---

## Architecture Analysis

### Current State

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CURRENT ARCHITECTURE                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Conversation Service (business_services)                                   │
│  └── AgentOrchestrator                                                      │
│      └── StrategyCoordinator + 26 Sub-Agents                               │
│          └── tools.py (HTTP calls to services)                             │
│                                                                              │
│  Database Service (backend_services)                                        │
│  ├── HTTP API (/database/query, /database/command)                         │
│  ├── QueryRequestHandler (pub/sub: database.query, database.command)       │
│  └── Multiple consumers (telemetry, commands, simulation, KPI results)     │
│                                                                              │
│  Messaging Service (backend_services)                                       │
│  ├── EventPublisher (Redis pub/sub)                                        │
│  └── SubscriptionManager                                                   │
│                                                                              │
│  Communication Patterns:                                                    │
│  • HTTP API calls for synchronous operations                               │
│  • Redis pub/sub for async events and request-reply                        │
│  • RequestReplyServer pattern for database access via messaging            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Key Findings

| Component | Pattern | Notes |
|-----------|---------|-------|
| Agent Tools (`tools.py`) | Direct HTTP calls | `httpx.AsyncClient` to services |
| Database Service | Dual: HTTP + Pub/Sub | `QueryRequestHandler` for pub/sub |
| Messaging Service | Central hub | All events routed through Redis |
| Service-to-Service | Pub/Sub preferred | Event-driven architecture |

---

## Design Decision: Hybrid MCP Integration

### Recommendation: **Direct MCP for Reads, Messaging for Writes**

Based on architecture analysis, we recommend a **hybrid approach**:

| Operation Type | Pattern | Rationale |
|----------------|---------|-----------|
| **Schema introspection** | Direct MCP | Low latency, read-only |
| **Knowledge graph queries** | Direct MCP | Fast traversal needed |
| **Web search** | Direct MCP | External service, no internal routing |
| **Artifact persistence** | Via Messaging | Audit trail, event-driven |
| **Knowledge graph updates** | Via Messaging | Consistency, sync to TimescaleDB |

### Why Not Messaging-Only?

1. **Latency**: Agents need instant responses for schema lookups
2. **Simplicity**: MCP protocol is request-response, not pub/sub
3. **Existing Pattern**: `tools.py` already uses direct HTTP calls

### Why Not Direct-Only?

1. **Audit Trail**: Write operations should be logged via messaging
2. **Event-Driven**: Other services may need to react to changes
3. **Consistency**: Knowledge Graph syncs with TimescaleDB metadata tables

---

## Target Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         TARGET ARCHITECTURE                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  CONVERSATION SERVICE (business_services)                                   │
│  ┌────────────────────────────────────────────────────────────────────────┐│
│  │                        AgentOrchestrator                                ││
│  │                              │                                          ││
│  │         ┌────────────────────┼────────────────────┐                    ││
│  │         ▼                    ▼                    ▼                    ││
│  │  ┌─────────────┐      ┌───────────┐      ┌──────────────┐             ││
│  │  │ Coordinator │      │ Architect │      │ CompetitiveA │             ││
│  │  └──────┬──────┘      └─────┬─────┘      └──────┬───────┘             ││
│  └─────────┼───────────────────┼───────────────────┼────────────────────-┘│
│            │                   │                   │                       │
│  ┌─────────▼───────────────────▼───────────────────▼────────────────────┐ │
│  │                      MCPClientManager                                 │ │
│  │                                                                       │ │
│  │  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐          │ │
│  │  │ PostgresMCP    │  │ KnowledgeGraph │  │ WebSearchMCP   │          │ │
│  │  │ Client         │  │ MCP Client     │  │ Client         │          │ │
│  │  │                │  │                │  │                │          │ │
│  │  │ • list_schemas │  │ • search_nodes │  │ • search_web   │          │ │
│  │  │ • list_tables  │  │ • get_context  │  │ • search_news  │          │ │
│  │  │ • describe_tbl │  │ • get_lineage  │  │ • get_page     │          │ │
│  │  │ • query_sample │  │                │  │                │          │ │
│  │  └───────┬────────┘  └───────┬────────┘  └───────┬────────┘          │ │
│  └──────────┼───────────────────┼───────────────────┼────────────────────┘ │
│             │                   │                   │                      │
└─────────────┼───────────────────┼───────────────────┼──────────────────────┘
              │                   │                   │
              ▼                   ▼                   ▼
┌─────────────────────┐ ┌─────────────────────┐ ┌─────────────────────┐
│  DATABASE SERVICE   │ │  DATABASE SERVICE   │ │  EXTERNAL           │
│  (backend_services) │ │  (backend_services) │ │                     │
│                     │ │                     │ │  Brave Search API   │
│  PostgreSQL MCP     │ │  Knowledge Graph    │ │  OR                 │
│  Server Module      │ │  MCP Server Module  │ │  Exa API            │
│                     │ │                     │ │                     │
│  TimescaleDB        │ │  TimescaleDB        │ │                     │
│  (read-only)        │ │  (metadata tables)  │ │                     │
└─────────────────────┘ └──────────┬──────────┘ └─────────────────────┘
                                   │
                                   │ WRITES via Messaging
                                   ▼
                       ┌─────────────────────┐
                       │  MESSAGING SERVICE  │
                       │  (backend_services) │
                       │                     │
                       │  Redis Pub/Sub      │
                       │  • knowledge.update │
                       │  • knowledge.sync   │
                       └─────────────────────┘
```

---

## Implementation Plan

### Phase 1: PostgreSQL MCP Server (database_service)

**Location**: `services/backend_services/database_service/app/mcp/`

#### Files to Create

| File | Purpose |
|------|---------|
| `__init__.py` | Module init |
| `postgres_mcp_server.py` | MCP server implementation |
| `postgres_mcp_tools.py` | Tool definitions |
| `postgres_mcp_models.py` | Pydantic models |

#### Tools to Implement

| Tool | Description | Agent Users |
|------|-------------|-------------|
| `list_schemas` | List all DB schemas | Architect |
| `list_tables` | List tables in schema | Architect, Developer |
| `describe_table` | Get columns, types, constraints | Developer, DataAnalyst |
| `list_hypertables` | List TimescaleDB hypertables | DataAnalyst |
| `list_continuous_aggregates` | List caggs | DataAnalyst |
| `query_sample` | SELECT LIMIT 10 (read-only) | DataAnalyst, Tester |
| `explain_query` | EXPLAIN ANALYZE | DataAnalyst |
| `get_table_stats` | Row count, size, compression | Architect |

#### Integration Points

```python
# database_service/app/main.py additions
from .mcp.postgres_mcp_server import PostgresMCPServer

# In lifespan():
postgres_mcp = PostgresMCPServer(database_manager=database_manager)
await postgres_mcp.start()

# New endpoint for MCP protocol
app.mount("/mcp", postgres_mcp.app)
```

#### Estimated Points: **3 pts**

---

### Phase 2: Knowledge Graph MCP Server (database_service)

**Location**: `services/backend_services/database_service/app/mcp/`

#### Design Decision: TimescaleDB-Backed (Not Separate Graph DB)

Per your architecture preference, the Knowledge Graph will use **TimescaleDB** as its backend, storing data in the existing metadata tables with graph-like query capabilities.

#### Database Schema (New Tables)

```sql
-- Knowledge graph nodes (extends metadata_definitions)
CREATE TABLE IF NOT EXISTS knowledge_graph_nodes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    entity_type VARCHAR(100) NOT NULL,  -- value_chain, module, kpi, entity, etc.
    observations JSONB DEFAULT '[]',     -- List of observations
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    
    -- Link to existing metadata if applicable
    metadata_definition_id UUID REFERENCES metadata_definitions(id),
    
    UNIQUE(name, entity_type)
);

-- Knowledge graph relations (extends metadata_relationships)
CREATE TABLE IF NOT EXISTS knowledge_graph_relations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    from_node_id UUID NOT NULL REFERENCES knowledge_graph_nodes(id),
    to_node_id UUID NOT NULL REFERENCES knowledge_graph_nodes(id),
    relation_type VARCHAR(100) NOT NULL,  -- belongs_to, uses, contains, flows_to
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    
    UNIQUE(from_node_id, to_node_id, relation_type)
);

-- Indexes for graph traversal
CREATE INDEX idx_kg_nodes_type ON knowledge_graph_nodes(entity_type);
CREATE INDEX idx_kg_nodes_name ON knowledge_graph_nodes(name);
CREATE INDEX idx_kg_relations_from ON knowledge_graph_relations(from_node_id);
CREATE INDEX idx_kg_relations_to ON knowledge_graph_relations(to_node_id);
CREATE INDEX idx_kg_relations_type ON knowledge_graph_relations(relation_type);
```

#### Files to Create

| File | Purpose |
|------|---------|
| `knowledge_graph_mcp_server.py` | MCP server implementation |
| `knowledge_graph_mcp_tools.py` | Tool definitions |
| `knowledge_graph_models.py` | Pydantic models |
| `knowledge_graph_manager.py` | Graph query logic |

#### Tools to Implement

| Tool | Description | Agent Users |
|------|-------------|-------------|
| `create_entity` | Add node to graph | BusinessStrategist |
| `create_relation` | Link two nodes | BusinessAnalyst |
| `search_nodes` | Find by name/type/content | Coordinator, All |
| `get_entity_context` | Get node + relations | All |
| `get_lineage` | Trace KPI → entities | Architect, DataAnalyst |
| `open_nodes` | Get multiple nodes by name | Coordinator |
| `add_observations` | Add facts to node | All |

#### Messaging Integration (Writes)

```python
# Knowledge graph updates publish events for sync
class KnowledgeGraphMCPServer:
    async def create_entity(self, params):
        # 1. Insert to knowledge_graph_nodes
        node = await self._insert_node(params)
        
        # 2. Publish event for downstream sync
        await self.messaging_client.publish(
            channel="knowledge.entity_created",
            payload={
                "node_id": str(node.id),
                "name": node.name,
                "entity_type": node.entity_type
            }
        )
        
        return node
```

#### Sync with Existing Metadata Tables

```python
# Consumer in database_service to sync knowledge graph with metadata_definitions
class KnowledgeGraphSyncConsumer:
    """Syncs knowledge_graph_nodes with metadata_definitions on changes."""
    
    async def handle_metadata_created(self, event):
        """When metadata_definition created, create corresponding KG node."""
        await self.kg_manager.upsert_node(
            name=event["code"],
            entity_type=event["kind"],
            metadata_definition_id=event["id"]
        )
```

#### Estimated Points: **5 pts**

---

### Phase 3: Web Search MCP Client (conversation_service)

**Location**: `services/business_services/conversation_service/app/mcp/`

This is a **client** that connects to external search APIs, not a server we host.

#### Files to Create

| File | Purpose |
|------|---------|
| `web_search_mcp_client.py` | Client wrapper |
| `web_search_models.py` | Response models |

#### Provider Options

| Provider | Strengths | API Cost |
|----------|-----------|----------|
| **Brave Search** | General web search, privacy-focused | Free tier available |
| **Exa** | Semantic search, better for research | Pay per query |
| **Tavily** | AI-optimized, structured results | Pay per query |

#### Tools to Implement

| Tool | Description | Agent Users |
|------|-------------|-------------|
| `search_web` | General web search | CompetitiveAnalyst |
| `search_news` | Recent news articles | MarketingManager |
| `search_companies` | Company profiles | CompetitiveAnalyst |
| `get_page_content` | Extract page text | DocumentAnalyzer |

#### Estimated Points: **2 pts**

---

### Phase 4: MCPClientManager (conversation_service)

**Location**: `services/business_services/conversation_service/app/mcp/`

Centralized manager for all MCP connections in the agent system.

#### Files to Create

| File | Purpose |
|------|---------|
| `__init__.py` | Module init |
| `mcp_client_manager.py` | Central manager |
| `mcp_config.py` | Configuration |

#### Implementation

```python
class MCPClientManager:
    """Manages MCP client connections for the agent system."""
    
    def __init__(self, config: MCPConfig):
        self.config = config
        self.clients: Dict[str, BaseMCPClient] = {}
        
    async def initialize(self):
        # PostgreSQL MCP (internal service)
        if self.config.postgres_mcp_enabled:
            self.clients["postgres"] = PostgresMCPClient(
                base_url=self.config.database_service_url + "/mcp",
                read_only=True
            )
            await self.clients["postgres"].connect()
        
        # Knowledge Graph MCP (internal service)
        if self.config.knowledge_mcp_enabled:
            self.clients["knowledge"] = KnowledgeGraphMCPClient(
                base_url=self.config.database_service_url + "/mcp/knowledge"
            )
            await self.clients["knowledge"].connect()
        
        # Web Search MCP (external)
        if self.config.web_search_enabled:
            self.clients["web_search"] = WebSearchMCPClient(
                provider=self.config.web_search_provider,
                api_key=self.config.web_search_api_key
            )
    
    def get_tools_for_agent(self, agent_role: AgentRole) -> List[ToolDefinition]:
        """Get MCP tools available to a specific agent role."""
        tools = []
        
        # PostgreSQL MCP tools
        if agent_role in [AgentRole.ARCHITECT, AgentRole.DEVELOPER, 
                          AgentRole.DATA_ANALYST, AgentRole.TESTER]:
            if "postgres" in self.clients:
                tools.extend(self.clients["postgres"].get_tools())
        
        # Knowledge Graph MCP tools
        if agent_role in [AgentRole.COORDINATOR, AgentRole.BUSINESS_STRATEGIST,
                          AgentRole.BUSINESS_ANALYST, AgentRole.ARCHITECT]:
            if "knowledge" in self.clients:
                tools.extend(self.clients["knowledge"].get_tools())
        
        # Web Search MCP tools
        if agent_role in [AgentRole.COMPETITIVE_ANALYST, AgentRole.MARKETING_MANAGER,
                          AgentRole.BUSINESS_STRATEGIST]:
            if "web_search" in self.clients:
                tools.extend(self.clients["web_search"].get_tools())
        
        return tools
```

#### Estimated Points: **2 pts**

---

### Phase 5: Agent Integration

Modify base agent and orchestrator to use MCP tools.

#### Files to Modify

| File | Changes |
|------|---------|
| `base_agent.py` | Accept MCPClientManager, merge MCP tools |
| `orchestrator.py` | Initialize MCPClientManager, pass to agents |
| `coordinator.py` | Use knowledge graph for context |

#### Integration Pattern

```python
# orchestrator.py
class AgentOrchestrator:
    async def initialize(self):
        # ... existing init ...
        
        # Initialize MCP client manager
        mcp_config = MCPConfig.from_env()
        self._mcp_manager = MCPClientManager(mcp_config)
        await self._mcp_manager.initialize()
        
        # Pass MCP manager to agents
        self._sub_agents = {
            "architect": ArchitectAgent(
                api_key=api_key,
                mcp_manager=self._mcp_manager
            ),
            # ... other agents ...
        }
```

```python
# base_agent.py
class BaseAgent:
    def __init__(self, config, api_key, mcp_manager=None):
        # ... existing ...
        self.mcp_manager = mcp_manager
        self._mcp_tools = []
    
    async def initialize(self):
        # ... existing ...
        
        # Load MCP tools for this agent
        if self.mcp_manager:
            self._mcp_tools = self.mcp_manager.get_tools_for_agent(
                self.config.role
            )
            for tool in self._mcp_tools:
                self.register_tool(tool.name, tool.execute)
```

#### Estimated Points: **2 pts**

---

## Summary: Total Effort

| Phase | Component | Points |
|-------|-----------|--------|
| 1 | PostgreSQL MCP Server | 3 |
| 2 | Knowledge Graph MCP Server | 5 |
| 3 | Web Search MCP Client | 2 |
| 4 | MCPClientManager | 2 |
| 5 | Agent Integration | 2 |
| **Total** | | **14 pts** |

---

## File Structure (Final)

```
services/
├── backend_services/
│   └── database_service/
│       └── app/
│           ├── mcp/                          # NEW
│           │   ├── __init__.py
│           │   ├── postgres_mcp_server.py
│           │   ├── postgres_mcp_tools.py
│           │   ├── postgres_mcp_models.py
│           │   ├── knowledge_graph_mcp_server.py
│           │   ├── knowledge_graph_mcp_tools.py
│           │   ├── knowledge_graph_models.py
│           │   └── knowledge_graph_manager.py
│           └── main.py                       # MODIFIED
│
└── business_services/
    └── conversation_service/
        └── app/
            ├── mcp/                          # NEW
            │   ├── __init__.py
            │   ├── mcp_client_manager.py
            │   ├── mcp_config.py
            │   ├── postgres_mcp_client.py
            │   ├── knowledge_graph_mcp_client.py
            │   └── web_search_mcp_client.py
            └── agents/
                ├── base_agent.py             # MODIFIED
                ├── orchestrator.py           # MODIFIED
                └── coordinator.py            # MODIFIED
```

---

## Configuration

```yaml
# config/mcp_servers.yaml
mcp:
  postgres:
    enabled: true
    # Uses database_service internal connection
    read_only: true
    allowed_schemas:
      - public
      - analytics_data
    max_sample_rows: 10
  
  knowledge_graph:
    enabled: true
    # Uses database_service internal connection
    sync_with_metadata: true
    publish_events: true
    event_channels:
      entity_created: "knowledge.entity_created"
      relation_created: "knowledge.relation_created"
      observation_added: "knowledge.observation_added"
  
  web_search:
    enabled: true
    provider: "brave"  # brave, exa, tavily
    api_key: "${WEB_SEARCH_API_KEY}"
    rate_limit_per_minute: 10
    cache_ttl_seconds: 3600

# Agent role to MCP tool mapping
agent_mcp_access:
  architect:
    - postgres.list_schemas
    - postgres.list_tables
    - postgres.describe_table
    - postgres.get_table_stats
    - knowledge.search_nodes
    - knowledge.get_lineage
  
  developer:
    - postgres.list_tables
    - postgres.describe_table
    - postgres.list_hypertables
    - knowledge.get_entity_context
  
  data_analyst:
    - postgres.query_sample
    - postgres.explain_query
    - postgres.list_continuous_aggregates
    - knowledge.get_lineage
  
  competitive_analyst:
    - web_search.search_web
    - web_search.search_companies
    - web_search.search_news
    - knowledge.search_nodes
  
  business_strategist:
    - knowledge.create_entity
    - knowledge.create_relation
    - knowledge.search_nodes
    - web_search.search_web
  
  coordinator:
    - knowledge.search_nodes
    - knowledge.get_entity_context
    - knowledge.open_nodes
```

---

## Migration Strategy

### Phase 1: Non-Breaking Addition
1. Add MCP servers as **optional** modules
2. Existing `tools.py` continues to work
3. Agents get MCP tools **in addition to** existing tools

### Phase 2: Gradual Adoption
1. Test MCP tools with specific agents
2. Validate performance and reliability
3. Migrate high-value use cases first

### Phase 3: Full Integration
1. Deprecate overlapping tools in `tools.py`
2. MCP becomes primary integration method
3. Remove deprecated tools

---

## Testing Strategy

### Unit Tests
- Each MCP tool individually
- Tool parameter validation
- Error handling

### Integration Tests
- MCP server ↔ database_service
- MCPClientManager ↔ agents
- Knowledge graph ↔ metadata sync

### End-to-End Tests
- Agent uses MCP tool in conversation
- Full design session with MCP-enabled agents
- Knowledge graph persistence across sessions

---

## Next Steps

1. **Approve this plan** - Confirm design decisions
2. **Phase 1**: Implement PostgreSQL MCP Server
3. **Phase 2**: Implement Knowledge Graph MCP Server
4. **Phase 3**: Add Web Search MCP Client
5. **Phase 4**: Build MCPClientManager
6. **Phase 5**: Integrate with agents

---

## Appendix: Architecture Compliance Checklist

| Requirement | Compliant | Notes |
|-------------|-----------|-------|
| Microservices architecture | ✅ | MCP servers part of existing services |
| CQRS pattern | ✅ | Reads via MCP, writes via messaging |
| TimescaleDB for storage | ✅ | Knowledge graph uses metadata tables |
| Redis for messaging | ✅ | Write events published to Redis |
| Real-time processing | ✅ | Direct MCP calls for low latency |
| Event-driven | ✅ | Knowledge updates trigger events |
| Pydantic v2 models | ✅ | All MCP models use Pydantic v2 |
| OpenTelemetry tracing | ✅ | MCP calls include trace context |
