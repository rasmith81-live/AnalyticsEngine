# Analytics Engine Features Breakdown

This document provides a detailed breakdown of the features for the Analytics Engine backend services, including 1-2 point estimates for build and test functionality.

**Point Estimates:**
*   **1 Point**: Small task, clear scope, minimal dependencies (approx. 2-4 hours).
*   **2 Points**: Medium task, some logic complexity or integration (approx. 4-8 hours).

## Definition of Done & Testing Standards
**CRITICAL REQUIREMENT:** All features listed in this document, regardless of point estimate, require a corresponding automated test script (Unit, Integration, or E2E) to be considered complete.
*   **Unit Tests:** Validate isolated logic (e.g., Formula Parser, SQL Generation).
*   **Integration Tests:** Validate service interaction (e.g., Metadata Service -> Database Service).
*   **End-to-End Tests:** Validate full scenarios (e.g., Execution Lifecycles).
*   **Test Location:** All tests must be located in the centralized `tests/` directory or service-specific `tests/` folders.

## Backend Services

### 1. Archival Service
**Bounded Context:** Data Archival & Lakehouse Storage

#### Feature: Archival Event Processing [COMPLETED]
**Description:** Manages the lifecycle of data archival operations.
*   **[1 pt]** Implement `ArchivalEvent` Pydantic model with validation for `event_id`, `table_name`, `chunks`, etc.
*   **[2 pts]** Implement Redis subscriber for `archival.events` topic with error handling and reconnection logic.
*   **[1 pt]** Implement in-memory state management for tracking event status (PENDING -> PROCESSING -> COMPLETED/FAILED).
*   **[2 pts]** Implement data extraction logic to query TimescaleDB for specific time range chunks.
*   **[1 pt]** Implement `ArchivalConfirmation` event publishing to `archival.confirmations` topic.
*   **[1 pt]** Write unit tests for event parsing, status transitions, and validation logic.
*   **[2 pts]** Create integration test verifying the flow: Receive Event -> Update State -> Publish Confirmation.

#### Feature: Lakehouse Integration [COMPLETED]
**Description:** Interfaces with Azure Data Lake Storage Gen2.
*   **[1 pt]** Setup `LakehouseClient` with Azure SDK and configuration handling.
*   **[2 pts]** Implement `write_data` method for Parquet serialization and upload to ADLS.
*   **[1 pt]** Implement directory structure generation logic (e.g., `{table}/{year}/{month}/{day}`).
*   **[1 pt]** Implement connection health check for ADLS.
*   **[2 pts]** Create integration tests for writing and verifying file existence in ADLS (using a mock or dev container).

#### Feature: Distributed Tracing & Observability [COMPLETED]
**Description:** End-to-end tracing and metrics.
*   **[1 pt]** Configure OpenTelemetry instrumentation for FastAPI and Redis client.
*   **[1 pt]** Implement middleware to extract and propagate correlation IDs from headers/messages.
*   **[1 pt]** Define and expose Prometheus metrics for archival operations (success, fail, duration).
*   **[1 pt]** Implement `/health` endpoint checking Redis and ADLS connectivity.

---

### 2. Database Service
**Bounded Context:** Database Operations & Management

#### Feature: CQRS Implementation [COMPLETED]
**Description:** Separation of Read and Write operations.
*   **[1 pt]** Define `QueryRequest` and `CommandRequest` Pydantic models.
*   **[2 pts]** Implement `execute_query` handler with read-only database connection.
*   **[2 pts]** Implement `execute_command` handler with write connection and transaction management.
*   **[2 pts]** Implement Redis caching layer for `execute_query` results.
*   **[1 pt]** Write unit tests for query/command routing and validation.

#### Feature: Migration Management [COMPLETED]
**Description:** Automated schema evolution and TimescaleDB setup.
*   **[1 pt]** Setup `AutomatedMigrationManager` class structure and configuration.
*   **[2 pts]** Implement `_validate_timescaledb` to ensure extension presence and permissions.
*   **[2 pts]** Implement programmatic Alembic execution (upgrade/downgrade) via API.
*   **[1 pt]** Implement dynamic `DATABASE_URL` handling with Async/Sync driver switching (`asyncpg` -> `psycopg2`).
*   **[1 pt]** Implement Offline Migration mode support.
*   **[2 pts]** Implement logic to detect and convert tables to Hypertables post-migration.
*   **[2 pts]** Create integration test running a full migration cycle on a test DB.

#### Feature: Schema Drift Detection [COMPLETED]
**Description:** Monitoring alignment between code and database using a Two-Tier Schema Management strategy.
*   **[2 pts]** Implement **Zone 1 (System Core)** governance: Use Alembic to strictly manage static tables (Auth, Metadata) in the `public` schema, failing CI/CD builds on mismatch.
*   **[2 pts]** Implement **Zone 2 (Dynamic Layer)** governance: Isolate user-defined tables/hypertables into a separate schema (e.g., `analytics_data`) ignored by Alembic.
*   **[2 pts]** Implement `ConsistencyChecker` background job (Self-Healing) to reconcile `EntityDefinitions` against actual `analytics_data` tables and issue repair `ALTER` commands.

#### Feature: Retention Management [COMPLETED]
**Description:** Data lifecycle policies.
*   **[1 pt]** Define `RetentionPolicy` model and configuration loader.
*   **[2 pts]** Implement `RetentionManager` background task to scan for expired chunks.
*   **[1 pt]** Implement logic to publish `ArchivalEvent` for identified chunks.
*   **[2 pts]** Implement `drop_chunks` logic triggered *only* by successful `ArchivalConfirmation`.
*   **[2 pts]** Create integration test simulating time passage and verifying event publication + chunk drop.

#### Feature: Retention API [COMPLETED]
**Description:** Monitoring and manual control of retention.
*   **[1 pt]** Implement `GET /database/retention/status` to view hypertable chunk status.
*   **[1 pt]** Implement `POST /database/retention/trigger-archival` for manual override.

#### Feature: Event Consumers [COMPLETED]
**Description:** Write-side handling for data streams.
*   **[1 pt]** Implement base `EventConsumer` class with Redis subscription logic.
*   **[2 pts]** Implement specific consumers (Telemetry, News, Market) mapping events to DB models.
*   **[1 pt]** Write unit tests for event-to-model mapping logic.

#### Feature: Stream Publisher [COMPLETED]
**Description:** Real-time data broadcasting.
*   **[2 pts]** Implement `PeriodBasedPublisher` to monitor Continuous Aggregates (1m/1h/1d).
*   **[2 pts]** Implement Redis publishing logic for KPI updates.
*   **[1 pt]** Implement subscriber tracking management.

#### Feature: Ad-Hoc Query Engine [COMPLETED]
**Description:** Dynamic data retrieval.
*   **[2 pts]** Implement `QueryBuilder` to translate API parameters (filters, ranges) into secure SQL.
*   **[1 pt]** Implement `QueryCache` for storing heavy aggregation results.

#### Feature: Secure Artifact Storage [COMPLETED]
**Description:** Encrypted storage for sensitive configuration and features.
*   **[2 pts]** Implement `SecureStorage` table/schema with encryption-at-rest (using PGcrypto or application-level encryption).
*   **[2 pts]** Implement Admin-only API endpoints for reading and writing secure artifacts.
*   **[1 pt]** Implement key management logic for rotating encryption keys.

---

### 3. Messaging Service
**Bounded Context:** Async Messaging & Event Propagation

#### Feature: Redis Pub/Sub Infrastructure [COMPLETED]
**Description:** Core event bus implementation.
*   **[1 pt]** Setup Redis connection pool management and configuration.
*   **[2 pts]** Implement `EventPublisher` class with connection retry and error handling.
*   **[1 pt]** Implement health check for Redis connectivity.

#### Feature: Event Publishing [COMPLETED]
**Description:** Reliable message publication.
*   **[1 pt]** Implement `publish_message` method with support for metadata and correlation IDs.
*   **[2 pts]** Implement `publish_bulk` pipeline for high-throughput scenarios.
*   **[1 pt]** Implement gzip compression logic for payloads > 1KB.
*   **[1 pt]** Write unit tests for payload serialization and compression.

#### Feature: Subscription Management [COMPLETED]
**Description:** Managing service subscriptions and webhooks.
*   **[1 pt]** Define `SubscriptionRequest` model and storage (in-memory or Redis).
*   **[2 pts]** Implement `SubscriptionManager` to handle `subscribe` and `unsubscribe` requests.
*   **[2 pts]** Implement message listener loop that matches patterns and triggers webhooks.
*   **[2 pts]** Implement retry logic and Dead Letter Queue (DLQ) for failed webhook deliveries.
*   **[2 pts]** Create integration test: Publish message -> Verify Webhook received.

#### Feature: Command Support [COMPLETED]
**Description:** Explicit command routing.
*   **[1 pt]** Implement `publish_command` endpoint distinct from events.
*   **[1 pt]** Implement command-specific channel naming convention (`commands.{type}`).

---

### 4. Observability Service
**Bounded Context:** Telemetry & Monitoring

#### Feature: Telemetry Ingestion [COMPLETED]
**Description:** Ingesting traces, metrics, and logs.
*   **[1 pt]** Define domain models for `TraceData`, `MetricData`, `LogData`.
*   **[2 pts]** Implement `ingest_telemetry` endpoint validating and normalizing input.
*   **[2 pts]** Implement logic to forward normalized data to Database Service (via Messaging).
*   **[1 pt]** Write unit tests for telemetry data validation.

#### Feature: OTLP Server [COMPLETED]
**Description:** gRPC server for OpenTelemetry.
*   **[2 pts]** Implement gRPC server stub for OTLP TraceService.
*   **[2 pts]** Implement gRPC server stub for OTLP MetricsService.
*   **[2 pts]** Implement mapping logic from OTLP Protobuf format to internal domain models.
*   **[2 pts]** Create integration test sending OTLP data via a client and verifying ingestion.

#### Feature: Metrics & Analysis [COMPLETED]
**Description:** Aggregated platform metrics.
*   **[1 pt]** Implement internal Prometheus registry for aggregated metrics.
*   **[2 pts]** Implement logic to aggregate metrics from received `MetricData` events.
*   **[1 pt]** Expose `/metrics` endpoint for Prometheus scraping.

#### Feature: Health & Status Tracking [COMPLETED]
**Description:** Real-time service health monitoring.
*   **[1 pt]** Implement in-memory registry for service health status.
*   **[2 pts]** Implement logic to update health status based on `HealthData` events.
*   **[1 pt]** Expose `/system/health` endpoint summarizing platform status.

#### Feature: Alerting & Notification System [COMPLETED]
**Description:** Active monitoring and incident response.
*   **[2 pts]** Implement metric threshold evaluation logic.
*   **[2 pts]** Implement integration with Slack and Email providers for notifications.
*   **[1 pt]** Define `AlertRule` configuration model.

#### Feature: Code traceability [COMPLETED]
**Description:** Provide logging of all classes and methods usage.
*   **[2 pts]** Implement logging of all classes and methods usage as they are called
*   **[1 pt]**  Identify files in the application that have not been utilized in a given period.

---

## Business Services

### 1. Business Metadata Service
**Bounded Context:** Platform Ontology & Definitions

#### Feature: Ontology Management [COMPLETED]
**Description:** Managing the core definitions of the platform.
*   **[1 pt]** Define Pydantic models for `EntityDefinition`, `RelationshipDefinition`, and `MetricDefinition`.
*   **[1 pt]** Define Pydantic models for `ValueChainPatternDefinition` and `ActorDefinition`.
*   **[2 pts]** Implement CRUD API endpoints for managing these definitions.
*   **[2 pts]** Implement validation logic to ensure referential integrity (e.g., Metric references valid Entity).

#### Feature: Access Control & Governance [COMPLETED]
**Description:** Managing permissions and data quality rules.
*   **[1 pt]** Define models for `ClientDefinition`, `RoleDefinition`, and `PermissionDefinition`.
*   **[2 pts]** Implement `RowLevelSecurityDefinition` logic to generating dynamic SQL filters.
*   **[2 pts]** Implement API for defining and retrieving `DataQualityRuleDefinition`s.

#### Feature: Analytics Strategy [COMPLETED]
**Description:** Managing analytics use cases and strategies.
*   **[1 pt]** Define models for `AnalyticsStrategyDefinition`, `AnalyticsUseCaseDefinition`, and `DataSourceDefinition`.
*   **[2 pts]** Implement API to link Use Cases to required Entities and Metrics.

#### Feature: Execution Artifact Generation [COMPLETED]
**Description:** Generating code and schemas from ontology.
*   **[2 pts]** Implement logic to generate Pydantic v2 models from `EntityDefinition`s.
*   **[2 pts]** Implement logic to generate TimescaleDB DDL/schemas from `EntityDefinition`s.
*   **[1 pt]** Create CLI tool or API endpoint to trigger artifact generation.

#### Feature: Conversation Modeling [COMPLETED]
**Description:** Supporting chatbot-driven value chain design.
*   **[1 pt]** Define models for `InterviewSession`, `Utterance`, and `BusinessIntent`.
*   **[2 pts]** Implement API for managing interview sessions and capturing utterances (Moved to Conversation Service).
*   **[2 pts]** Implement logic to persist `CompanyValueChainModel` derived from conversations (Implemented `ConversationEventConsumer` and `persist_generated_model`).
*   **[2 pts]** Implement event consumer to persist generated models from Conversation Service.

---

### 2. Calculation Engine Service
**Bounded Context:** KPI Calculation & Orchestration

#### Feature: Calculation Orchestration [COMPLETED]
**Description:** Routing calculation requests to appropriate handlers.
*   **[2 pts]** Implement `CalculationOrchestrator` to route requests based on value chain/domain.
*   **[2 pts]** Implement generic `calculate_batch` logic for parallel execution.
*   **[1 pt]** Write unit tests for orchestrator routing logic.

#### Feature: Dynamic Calculation Engine [COMPLETED]
**Description:** Metadata-driven execution of KPI formulas using a fixed library.
*   **[2 pts]** Implement `FormulaLibrary` with a fixed set of supported SQL-native functions (e.g., SUM, AVG, LAST).
*   **[2 pts]** Implement `SQLGenerator` to compile standardized KPI definitions into optimized SQL queries against the schema.
*   **[2 pts]** Enforce **Push-Down Only** policy: All aggregations must occur in the database; Application layer receives only summary results.

#### Feature: TimescaleDB Native Integration [COMPLETED]
**Description:** Primary engine for time-series calculations.
*   **[2 pts]** Implement logic to automatically generate Continuous Aggregate Views for standard KPIs (SUM/AVG/COUNT).
*   **[2 pts]** Implement `QueryRouter` to select between Raw Hypertables, Real-time Aggregates, or Materialized Views based on time granularity.
*   **[1 pt]** Implement Refresh Policy management for Continuous Aggregates.

#### Feature: In-Memory Stream Aggregator [COMPLETED]
**Description:** Sub-second real-time analytics using Redis TimeSeries.
*   **[2 pts]** Implement `StreamAggregator` using Redis TimeSeries for immediate sub-second metric updates before persistence.
*   **[2 pts]** Implement write-through or write-behind pattern to sync Redis TimeSeries data to TimescaleDB for long-term storage.
*   **[1 pt]** Implement query logic to merge real-time Redis data with historical TimescaleDB data for "Current" views.

#### Feature: Result Caching [COMPLETED]
**Description:** Performance optimization for heavy calculations.
*   **[1 pt]** Implement Redis caching decorator/middleware for calculation results.
*   **[1 pt]** Implement domain-specific TTL strategies (e.g., SupplyChain=1hr, Finance=5min).
*   **[1 pt]** Implement cache invalidation logic based on data update events.

#### Feature: Approximate Analytics [COMPLETED]
**Description:** Using probabilistic data structures for sub-second distinct counts and percentiles.
*   **[2 pts]** Implement `HyperLogLog` integration for `COUNT(DISTINCT)` metrics (e.g., Unique Members).
*   **[2 pts]** Implement `t-digest` integration for fast percentile calculations (e.g., 95th percentile Claim Cost).
*   **[1 pt]** Implement toggle in Metadata to switch between "Exact" (slower) and "Approximate" (fast) modes.

#### Feature: High-Concurrency Optimization [COMPLETED]
**Description:** Managing load under heavy user traffic.
*   **[2 pts]** Implement **Request Coalescing** (Single-flight) to merge duplicate simultaneous calculation requests.
*   **[2 pts]** Implement **Hierarchical Query Logic** to prefer summing intermediate aggregates (Daily Views) over scanning raw data for long ranges.

---

### 3. Demo Config Service
**Bounded Context:** Simulation, Proposals & Configuration

#### Feature: Service Proposal Generation [COMPLETED]
**Description:** Automating SOW and proposal creation.
*   **[2 pts]** Implement `PricingCalculator` for licensing, SOW, and infrastructure logic.
*   **[2 pts]** Implement `QuestionnaireEngine` to manage the 8-step wizard flow and validation.
*   **[2 pts]** Implement `ProposalGenerator` to render PDF/Word documents from templates.

#### Feature: License Management [COMPLETED]
**Description:** Managing client licenses and expiration.
*   **[1 pt]** Implement `LicenseKeyGenerator` with cryptographic signing and feature flags.
*   **[2 pts]** Implement `LicenseValidator` API to check expiration, active modules, and renewal status.
*   **[1 pt]** Implement background job to send renewal email notifications (3-month warning).

#### Feature: Resource Scheduling [COMPLETED]
**Description:** Project timeline and resource management.
*   **[2 pts]** Implement `Scheduler` algorithm to assign resources to implementation tasks.
*   **[2 pts]** Implement `TimelineGenerator` to produce Gantt chart data and critical path analysis.
*   **[1 pt]** Define `ResourceAvailability` models.

#### Feature: Demo Data Orchestration [COMPLETED]
**Description:** Managing synthetic data generation scenarios.
*   **[2 pts]** Implement `ScenarioManager` to coordinate data generation across multiple KPIs.
*   **[2 pts]** Integration with Database Service to persist generated snapshots.

#### Feature: Client Configuration [COMPLETED]
**Description:** Managing client-specific settings.
*   **[1 pt]** Define `ClientConfig` models.
*   **[2 pts]** Implement API for creating and updating client configurations.
*   **[1 pt]** Implement logic to cascade config changes (e.g., active KPIs) to other services.

#### Feature: Custom KPIs [COMPLETED]
**Description:** User-defined metrics.
*   **[2 pts]** Implement API for creating `CustomKPI` definitions based on existing ones.
*   **[1 pt]** Implement validation to ensure custom formulas are parseable.

#### Feature: Demo Data Generation [COMPLETED]
**Description:** Generating realistic synthetic data for demonstrations.
*   **[2 pts]** Implement `_generate_time_series` with trend and seasonality logic.
*   **[2 pts]** Implement **Scenario Generators** (e.g., "Health Retention") to create consistent Entity Snapshots (Start/End/New) over time.
*   **[2 pts]** Implement API to trigger data generation for specific KPIs, Scenarios, and time ranges.
*   **[2 pts]** Implement logic to persist generated data via Database Service.

### 4. Conversation Service
**Bounded Context:** Chatbot-Driven Design & Modeling

#### Feature: LLM & NLP Pipeline [COMPLETED]
**Description:** Core intelligence for processing natural language.
*   **[1 pt]** Implement `LLMClient` abstraction for interfacing with providers (OpenAI/Azure).
*   **[2 pts]** Implement prompt engineering framework for "Business Intent Extraction".
*   **[2 pts]** Implement logic to parse LLM responses into structured `Utterance` and `BusinessIntent` objects.
*   **[1 pt]** Write unit tests for prompt templates and response parsing.

#### Feature: Pattern Matching Engine [COMPLETED]
**Description:** Mapping business intent to ontology patterns.
*   **[2 pts]** Implement vector search or heuristic logic to match `BusinessIntent` to `ValueChainPattern`s.
*   **[2 pts]** Implement scoring algorithm to rank relevance of matched patterns.
*   **[2 pts]** Implement API endpoint `POST /match-intent` returning ranked patterns.

#### Feature: Design Suggestion Engine [COMPLETED]
**Description:** Proposing changes to the value chain graph.
*   **[2 pts]** Implement logic to generate `DesignSuggestion`s (Add Node, Add KPI) based on matched patterns.
*   **[1 pt]** Define `DesignSuggestion` and `GraphChange` models.
*   **[2 pts]** Implement interactive API for applying or rejecting suggestions (`POST /suggestions/{id}/apply`).

#### Feature: Session Management [COMPLETED]
**Description:** Managing stateful design interviews.
*   **[2 pts]** Implement WebSocket or stateful REST endpoints for real-time conversation.
*   **[1 pt]** Implement context window management (keeping relevant history for LLM).

#### Feature: Strategic Recommendation [COMPLETED]
**Description:** Mapping business context to value chains using NLP-based semantic search via Entity Resolution Service.
*   **[2 pts]** Implement `StrategicRecommender` with semantic search using Entity Resolution Service for value chain matching.
    - Extract semantic entities from business descriptions and use cases via NLP
    - Index value chain definitions with extracted domain entities and noun phrases
    - Calculate Jaccard similarity on entity/phrase overlap (not keyword matching)
    - Return matched entities and phrases as evidence for recommendations
*   **[2 pts]** Implement strategy alignment scoring using semantic similarity of strategy concepts.
    - Compare industry domain entities against strategy concept sets
    - Return matched concepts as rationale for alignment scores
*   **[1 pt]** Expose API endpoint for Conversation Service to request mappings.

#### Feature: Multi-Agent Design System [COMPLETED]
**Description:** AI-powered collaborative design using Claude multi-agent architecture.
*   **[2 pts]** Implement `StrategyCoordinator` (Claude Opus 4.5) as strategic advisor for C-suite interviews.
    - Listens and responds to executives (does NOT drive conversation)
    - Interview driven by 4 core questions: Business/Strategy, Pain Points, Success Metrics, Decision Impact
    - Applies Porter's frameworks internally to analyze client responses
    - Asks ONE pertinent follow-up question when gaps identified (Porter-based)
    - Follow-up categories: competitive pressure, supplier/customer dynamics, operations, strategy positioning
    - Orchestrates sub-agents after gathering sufficient context
*   **[2 pts]** Implement `ArchitectAgent` (Claude Sonnet 4) for DDD-based technical architecture.
    - Deeply versed in "Patterns, Principles, and Practices of Domain-Driven Design" (Millett/Tune)
    - Identifies bounded contexts with ubiquitous language
    - Designs aggregates with consistency boundaries and invariants
    - Models entities vs value objects, defines domain events
    - Creates context maps with integration patterns (ACL, OHS, Published Language)
    - Aligns value chains with subdomains (core, supporting, generic)
*   **[2 pts]** Implement `BusinessAnalystAgent` (Claude Sonnet 4) for industry expertise.
    - Assumes deep expertise for any industry/value chain
    - Identifies relevant KPIs and metrics
    - Provides industry benchmarks and best practices
*   **[2 pts]** Implement `DataAnalystAgent` (Claude Sonnet 4) for set-based KPI design.
    - Designs set-based KPIs with multi-step calculation workflows
    - Creates cohort analysis metrics (retention, churn, engagement)
    - Optimizes KPIs for TimescaleDB continuous aggregates
*   **[2 pts]** Implement `DeploymentSpecialistAgent` (Claude Sonnet 4) for Azure deployment.
    - Generates Azure infrastructure templates (ARM/Bicep)
    - Creates Kubernetes manifests and Helm charts
    - Configures CI/CD pipelines (GitHub Actions, Azure DevOps)
    - Produces deployment checklists and runbooks
*   **[2 pts]** Implement `DeveloperAgent` (Claude Sonnet 4) for code generation.
    - Generates TimescaleDB schemas
    - Creates Pydantic model definitions
    - Builds KPI calculation formulas
*   **[1 pt]** Implement `TesterAgent` (Claude Sonnet 4) for validation.
    - Validates schema integrity
    - Tests KPI formula correctness
    - Generates test cases
*   **[1 pt]** Implement `DocumenterAgent` (Claude Sonnet 4) for documentation.
    - Generates comprehensive documentation
    - Creates data dictionaries and API docs
*   **[2 pts]** Implement `ProjectManagerAgent` (Claude Sonnet 4) for Agile planning.
    - Analyzes scope from design artifacts to create epics
    - Plans sprints with goals, capacity, and story selection
    - Generates user stories with acceptance criteria (Given-When-Then)
    - Creates technical tasks for infrastructure, refactoring, spikes
    - Generates project roadmaps with milestones
    - Identifies risks with probability, impact, and mitigation strategies
*   **[2 pts]** Implement `AgentOrchestrator` for session management.
    - Manages multi-agent design sessions
    - Coordinates parallel agent execution
    - Aggregates and synthesizes results
*   **[2 pts]** Implement REST and WebSocket API endpoints for multi-agent design.
    - `POST /agents/design-session` - Create new design session
    - `POST /agents/sessions/{id}/message` - Send message to session
    - `POST /agents/sessions/{id}/analyze` - Run parallel analysis
    - `POST /agents/sessions/{id}/finalize` - Finalize and generate artifacts
    - `WebSocket /agents/ws/{id}` - Real-time streaming responses
*   **[2 pts]** Implement `SalesManagerAgent` (Claude Sonnet 4) for CRM lifecycle.
    - Manages prospect → lead → opportunity → client lifecycle
    - Designs sales pipeline stages and conversion metrics
    - Coordinates with Marketing Manager for MQL handoffs
*   **[2 pts]** Implement `AccountantAgent` (Claude Sonnet 4) for financial documents.
    - Generates proposals, SOW, and invoicing workflows
    - Designs AR/AP tracking and financial reporting
*   **[2 pts]** Implement `MarketingManagerAgent` (Claude Sonnet 4) for marketing strategy.
    - Designs campaigns, lead scoring models, and buyer personas
    - Creates content calendars and marketing analytics
    - Coordinates with Sales Manager for lead handoffs
*   **[2 pts]** Implement `UIDesignerAgent` (Claude Sonnet 4) for dashboard design.
    - Creates dashboard layouts, stylesheets, and component specifications
    - Ensures accessibility and responsive design
*   **[2 pts]** Implement `OperationsManagerAgent` (Claude Sonnet 4) for holistic KPI analysis.
    - Analyzes KPI results across all business areas
    - Identifies correlating patterns and bottlenecks
    - Makes optimization recommendations
*   **[2 pts]** Implement `CustomerSuccessManagerAgent` (Claude Sonnet 4) for customer health.
    - Designs health scores, churn risk models, and NPS tracking
    - Creates onboarding and expansion playbooks
*   **[2 pts]** Implement `HRTalentAnalystAgent` (Claude Sonnet 4) for people analytics.
    - Designs retention, engagement, and skills gap metrics
    - Creates compensation and workforce planning models
*   **[2 pts]** Implement `RiskComplianceOfficerAgent` (Claude Sonnet 4) for risk management.
    - Designs risk assessment frameworks and compliance tracking
    - Creates audit support and control monitoring
*   **[2 pts]** Implement `SupplyChainAnalystAgent` (Claude Sonnet 4) for SCOR model.
    - Applies ASCM SCOR framework for supply chain analytics
    - Designs inventory, supplier, and logistics metrics
*   **[2 pts]** Implement `ITILManagerAgent` (Claude Sonnet 4) for IT service management.
    - Applies ITIL 4 framework for incident/problem/change management
    - Designs SLA tracking, CMDB, and CSI metrics
*   **[2 pts]** Implement `MappingSpecialistAgent` (Claude Sonnet 4) for data mapping.
    - Designs source-to-analytics attribute mappings
    - Creates transformation rules and data lineage
*   **[2 pts]** Implement `ConnectionSpecialistAgent` (Claude Sonnet 4) for system integration.
    - Designs API wrappers, webhooks, and event handlers
    - Creates connector configurations for external systems
*   **[2 pts]** Implement `DocumentAnalyzerAgent` (Claude Sonnet 4) for document analysis.
    - Analyzes business documents, technical specs, and data dictionaries
    - Extracts entities, processes, KPIs, and terminology
    - Identifies gaps and generates clarification questions
    - Routes findings to Architect and Business Analyst agents
*   **[2 pts]** Implement `CompetitiveAnalystAgent` (Claude Sonnet 4) for competitive intelligence.
    - Searches for peer companies with similar business models via web search
    - Profiles competitors (identity, business model, offerings, position)
    - Analyzes competitive landscape using Porter's Five Forces
    - Identifies market gaps and differentiation opportunities
    - Triggered automatically by Business Strategist after model elicitation

#### Feature: Adaptive Communication Style [COMPLETED]
**Description:** Master Coordinator adapts response format to match interviewee's communication style.
*   **[2 pts]** Implement style detection to identify Executive, Technical, or Analyst communication patterns.
    - Executive indicators: vision, growth, ROI, stakeholders, strategic
    - Technical indicators: API, database, schema, architecture, microservices
    - Analyst indicators: metrics, KPI, dashboard, trend, correlation
*   **[2 pts]** Implement `CommunicationStyleProfile` to track session-level style preferences.
    - Detected role, abstraction level, vocabulary type, detail preference
    - Preferred response agent for formatting
*   **[2 pts]** Implement dynamic detail level adjustment (1=Summary to 4=Comprehensive).
    - Detect drill-down requests ("tell me more", "dig deeper")
    - Detect zoom-out requests ("summarize", "high level", "bottom line")
    - Maintain core communication style while adjusting depth
*   **[1 pt]** Implement response formatting delegation to appropriate agent based on style.

#### Feature: Cross-Agent Collaboration Framework [COMPLETED]
**Description:** Agents collaborate behind the scenes without overwhelming the interviewee.
*   **[2 pts]** Implement collaboration request/response pattern via context artifacts.
    - Request tools: `request_entity_validation`, `request_kpi_requirements`, etc.
    - Response tools: `share_entity_validation`, `share_schema_artifacts`, etc.
*   **[2 pts]** Implement Business Strategist → Competitive Analyst trigger.
    - Automatically triggers competitive analysis after business model elicitation
    - Passes business description, industry, and generic strategy
*   **[1 pt]** Implement collaboration tracking in `context.artifacts["collaboration_requests"]`.

### 5. Connector Service
**Bounded Context:** Data Connectivity & Adapters

#### Feature: Connection Management [COMPLETED]
**Description:** Securely managing data source credentials and configurations.
*   **[1 pt]** Define `ConnectionProfile` model (Type, Host, Auth methods).
*   **[2 pts]** Implement secure storage for credentials (integration with Azure KeyVault or encrypted DB fields).
*   **[2 pts]** Implement connection testing API (`POST /connections/test`).

#### Feature: Schema Discovery [COMPLETED]
**Description:** Introspecting sources to map available data.
*   **[2 pts]** Implement adapter pattern for different sources (SQL, REST, GraphQL).
*   **[2 pts]** Implement logic to fetch and normalize source schema (tables, columns, types) into `DataSourceDefinition`.
*   **[1 pt]** Implement API to preview sample data from a selected source entity.

### 6. Ingestion Service
**Bounded Context:** Data Movement & Scheduling

#### Feature: Ingestion Pipeline [COMPLETED]
**Description:** Configuring and executing data fetch jobs.
*   **[2 pts]** Implement `IngestionJob` scheduler (batch/cron).
*   **[2 pts]** Implement `DataExtractor` to fetch data via Connector Service and publish to `ingestion.events`.
*   **[1 pt]** Implement error handling and retry logic for network failures.

#### Feature: Data Standardization [COMPLETED]
**Description:** Normalizing incoming data streams.
*   **[2 pts]** Implement transformation logic to map raw source data to `EntityDefinition` schema.
*   **[1 pt]** Implement validation against `DataQualityRuleDefinition`s (integration with Data Governance).

#### Feature: Transformation Logic [COMPLETED]
**Description:** Handling conditional mapping and data refinement.
*   **[2 pts]** Implement **SQL Expression Builder** in the Data Mapping UI for defining column transformations (e.g., `CASE WHEN`, `CONCAT`).
*   **[2 pts]** Implement **Python Sandbox** (using WebAssembly/Pyodide or isolated containers) for advanced custom ETL scripts.
*   **[1 pt]** Implement validation to ensure custom logic produces the expected target data type.

### 7. Entity Resolution Service
**Bounded Context:** Master Data Management
**Architecture Pattern:** Lambda Architecture (Eventually Consistent)

#### Feature: Matching Engine [COMPLETED]
**Description:** identifying duplicate records using batch processing.
*   **[2 pts]** Implement `BatchMatcher` to run nightly fuzzy matching algorithms (Levenshtein, Jaro-Winkler).
*   **[2 pts]** Implement blocking strategy to optimize search space.

#### Feature: Golden Record Management [COMPLETED]
**Description:** Creating a single source of truth with eventual consistency.
*   **[2 pts]** Implement merge logic to combine attributes from multiple sources into a canonical record.
*   **[1 pt]** Implement persistent storage for canonical "Golden Records".
*   **[2 pts]** Implement "Retroactive Fix" logic to recalculate downstream KPIs when Entity Resolution merges identities.

### 8. Metadata Ingestion Service
**Bounded Context:** Knowledge Acquisition & Semantic Understanding

#### Feature: Industry Knowledge Base [COMPLETED]
**Description:** Constructing industry-specific metadata sets via Pluggable Content Packs.
*   **[2 pts]** Implement `NAICClassificationIterator` to process industry codes.
*   **[2 pts]** Implement logic to load **Industry Content Packs** (e.g., Standard Model for Supply Chain, Standard Model for Healthcare) as standardized `ValueChainSet`s and `BestPracticeKPI`s.
*   **[2 pts]** Implement persistence to Business Metadata Service, ensuring the core platform remains agnostic while supporting deep vertical functionality.

#### Feature: Semantic Mapping Engine [COMPLETED]
**Description:** Decomposing definitions into ontology components using NLP-based semantic analysis via Entity Resolution Service.
*   **[2 pts]** **Entity Extraction from Descriptions**: Integrate with Entity Resolution Service for NLP-based semantic entity extraction to identify business objects (e.g., "Customer", "Order", "Revenue") from KPI names, descriptions, and formulas.
    - Use Entity Resolution Service's semantic analysis to extract nouns and domain terms
    - Leverage NLP models (spaCy/LLM) for Part-of-Speech tagging and noun phrase extraction
    - Match extracted entities against existing definitions in Business Metadata Service
    - Populate `required_objects` array with matched entity codes
    - No predefined keywords - dynamically identifies entities from any business domain

*   **[2 pts]** **Value Chain Inference**: Integrate with Entity Resolution Service for semantic domain classification to map KPIs to appropriate value chains.
    - Use NLP-based semantic similarity to classify business domain from extracted entities
    - Query Business Metadata Service for existing value chain definitions
    - Auto-create value chain definitions if none exist for detected domain
    - Assign KPI to inferred value chain via metadata

*   **[2 pts]** **Module Assignment**: Integrate with Entity Resolution Service for semantic module clustering to group related KPIs.
    - Use NLP-based semantic analysis to detect module context from KPI metadata
    - Create or update module definitions in Business Metadata Service
    - Populate `modules` array with assigned module codes
    - Auto-generate module display names from detected business context

*   **[2 pts]** **Formula Decomposition Enhancement**: Extend existing `KPIDecomposer.decompose_formula()` to extract entity.attribute references from formulas.
    - Parse formula syntax to identify entity references (e.g., "Order.Revenue", "Customer.Count")
    - Validate extracted entities against ontology
    - Map formula variables to canonical entity attributes
    - Store decomposition results in KPI metadata for calculation engine

*   **[1 pt]** **Integration into Excel Upload Flow**: Wire decomposition pipeline into `/import/upload` endpoint.
    - Call decomposition for each valid KPI after initial parsing
    - Enrich KPI data structure with extracted metadata before caching
    - Log decomposition results for debugging and audit
    - Handle decomposition failures gracefully (continue import with warnings)

*   **[2 pts]** **Ontology Synchronization**: Implement logic to create missing ontology objects discovered during decomposition.
    - Auto-create entity definitions for newly discovered business objects
    - Auto-create value chain definitions for new domains
    - Auto-create/update module definitions with KPI assignments
    - Publish ontology change events to Business Metadata Service

*   **[1 pt]** **Testing & Validation**: Create integration tests for decomposition pipeline.
    - Test entity extraction from various KPI description formats
    - Test value chain inference accuracy
    - Test module assignment logic
    - Verify ontology synchronization with Business Metadata Service

*   **[2 pts]** **Time-Agnostic Formula Normalization**: Replace time-specific modifiers with generic "period" placeholders.
    - Replace duration units (day, week, month, year) with "period" (preserving plurality: days → periods)
    - Replace over-period terms (YoY, MoM, QoQ) with "Period over Period"
    - Replace to-date terms (YTD, MTD, QTD) with "Period to Date"
    - Store original formula in metadata for reference
    - Enables formulas to be applied to any time granularity

*   **[2 pts]** **Formula-Only Entity Extraction**: Extract only calculation-relevant entities for `required_objects`.
    - Parse formula syntax to identify business entities (e.g., "Revenue", "Cost", "Customer")
    - Filter out common terms (Total, Number, Sum, Average, etc.) using stop word list
    - Separate description entities (for domain inference) from formula entities (for calculations)
    - Only formula entities populate `required_objects` array

*   **[2 pts]** **LLM Fallback for Domain Inference**: Use LLM when spaCy NLP is unavailable.
    - Primary: spaCy word vector similarity for semantic domain classification
    - Fallback: OpenAI/Azure OpenAI LLM-based domain inference
    - Valid domains: supply_chain, sales, marketing, finance, hr, operations, customer_service, sustainability
    - Returns domain and confidence score

*   **[1 pt]** **Sustainability Domain Support**: Added sustainability as a recognized business domain.
    - Domain seed concepts: emission, carbon, environmental, ESG, CSR, climate, biodiversity, welfare, ethics, diversity, inclusion
    - Maps to "sustainability" value chain
    - Properly classifies CSR and environmental KPIs

*   **[1 pt]** **spaCy Model Caching**: Persist NLP models in Docker volume for faster startup.
    - spaCy models stored in `spacy_models` volume
    - Model downloaded on first startup, cached for subsequent restarts
    - Fallback to smaller model (en_core_web_sm) if primary (en_core_web_md) fails

**Expected Outcome:** Imported KPIs automatically organized into hierarchical structure (Value Chain → Module → KPI) with proper entity relationships, time-agnostic formulas, and accurate domain classification including sustainability, enabling immediate use in Config Page tree view without manual categorization.

---

## Frontend Services

### 1. API Gateway
**Bounded Context:** Ingress & Cross-Cutting Concerns

#### Feature: Routing Infrastructure [COMPLETED]
**Description:** Central entry point for all client requests.
*   **[1 pt]** Setup FastAPI app with versioned routing (`/api/v1`).
*   **[2 pts]** Implement proxy logic to route requests to backend services (Metadata, Calculation, Config).
*   **[1 pt]** Implement unified Swagger/OpenAPI documentation aggregator.

#### Feature: Service Clients [COMPLETED]
**Description:** Robust internal communication.
*   **[1 pt]** Implement `MetadataServiceClient` with timeout and retry logic.
*   **[1 pt]** Implement `CalculationEngineClient` with specialized timeout configuration for long-running jobs.
*   **[1 pt]** Implement `DemoConfigServiceClient` for config management.

#### Feature: Security & Reliability [COMPLETED]
**Description:** Policy enforcement at the edge.
*   **[2 pts]** Implement JWT authentication middleware.
*   **[2 pts]** Implement rate limiting middleware (per client IP/token).
*   **[2 pts]** Implement response caching middleware (Redis) for Metadata endpoints.
*   **[2 pts]** Implement Circuit Breaker pattern for backend service stability.

#### Feature: TLS Termination [COMPLETED]
**Description:** Secure transport layer.
*   **[1 pt]** Configure Uvicorn to use `server.crt` and `server.key` for SSL/TLS.
*   **[1 pt]** Implement HSTS (HTTP Strict Transport Security) header enforcement.

#### Feature: WebSocket Support [COMPLETED]
**Description:** Real-time bi-directional communication.
*   **[2 pts]** Implement WebSocket endpoint for client connections (`/ws`).
*   **[2 pts]** Implement Redis Pub/Sub listener to broadcast messages to connected clients.
*   **[2 pts]** Offload WebSocket state management to a dedicated infrastructure component (e.g., separate service or gateway) to ensure scalability.
*   **[1 pt]** Implement connection heartbeat and cleanup logic.

### 2. Demo/Config UI
**Bounded Context:** User Interaction & Visualization

#### Page: KPI Configuration (`ConfigPage`) [COMPLETED]
**Description:** The primary workspace for selecting and configuring metrics.
*   **[2 pts]** Implement **Metric Selection Tree** with tabbed navigation for Industries and Value Chains.
*   **[2 pts]** Implement **Shopping Cart** state management for selected KPIs (`useCart` context).
*   **[2 pts]** Implement **Resizable Split Layout** to toggle between navigation and details.
*   **[2 pts]** Implement **KPI Preview Panel** showing sample visualizations and metadata summaries.
*   **[2 pts]** Implement **Custom KPI Derivation** modal to create new metrics from existing ones.

#### Page: KPI Details (`KPIDetailPage`) [COMPLETED]
**Description:** Deep-dive analysis view for a single metric.
*   **[2 pts]** Implement **Tabbed Interface** (Overview, Formula, Objects, Benchmarks, Metadata).
*   **[1 pt]** Implement **Formula Visualization** displaying the calculation logic.
*   **[2 pts]** Implement **Required Objects Integration** listing dependencies with links to the Object Browser.
*   **[1 pt]** Implement **Contextual Actions** (Add to Cart, Edit/Derive).

#### Page: Object Model Browser (`ObjectModelsBrowser` / `ObjectModelViewer`) [COMPLETED]
**Description:** Explorer for the platform's ontology and data structures.
*   **[2 pts]** Implement **Module-based Grouping** and filtering of object models.
*   **[2 pts]** Implement **Search Functionality** across model names, codes, and descriptions.
*   **[2 pts]** Implement **UML Visualization** (`ObjectModelDiagram`) using D3.js/SVG to render entity relationships.
*   **[2 pts]** Implement **Relationship Parsing** to extract and display UML associations/compositions from schema definitions.

#### Page: Required Objects Analysis (`RequiredObjectsView`) [COMPLETED]
**Description:** Dependency impact analysis for selected KPIs.
*   **[2 pts]** Implement **Consolidated Dependency Graph** generating a combined UML diagram for all selected KPIs.
*   **[1 pt]** Implement **Cross-linking** navigation to detailed Object Model views.

#### Page: Demo Dashboard (`DemoPage`) [COMPLETED]
**Description:** Landing page and system status overview.
*   **[1 pt]** Implement **Service Health Indicators** checking status of backend microservices.
*   **[1 pt]** Implement **Quick Actions** navigation.
*   **[2 pts]** Implement **Real-time Widgets** integrated with Calculation Engine for live metric streams (WebSocket).

#### Page: Visual Data Mapper [COMPLETED]
**Description:** Interactive tool for binding source data to the ontology.
*   **[2 pts]** Implement **Source Schema Tree** displaying available attributes from Ingestion Service.
*   **[2 pts]** Implement **Target Ontology Tree** displaying required Entity Attributes.
*   **[2 pts]** Implement **Drag-and-Drop Mapping** logic (`dnd-kit`) to create semantic bindings.

#### Page: Service Proposal (`ServiceProposal`) [COMPLETED]
**Description:** Generating SOWs, cost estimates, and implementation timelines.
*   **[2 pts]** Implement **Pricing Calculator Form** to input license types, user counts, and infrastructure needs.
*   **[2 pts]** Implement **Resource Scheduler** to visualize team availability and assign consultants to project phases.
*   **[2 pts]** Implement **Gantt Chart Visualization** (using `d3-gantt` or similar) to display the generated project timeline and critical path.
*   **[1 pt]** Implement **SOW Export** to generate PDF/Word documents from the configured proposal data.

#### Page: Data Source Config (`DataSourceConfig`) [COMPLETED]
**Description:** Managing connections, schema discovery, and ingestion schedules.
*   **[2 pts]** Implement **Connection Profile Manager** to add/edit SQL, API, and File-based connections with credential validation.
*   **[2 pts]** Implement **Schema Discovery Wizard** to introspect source tables and select columns for ingestion.
*   **[2 pts]** Implement **Ingestion Scheduler** to configure cron expressions for batch jobs (e.g., "Daily at 2 AM").
*   **[1 pt]** Implement **Data Preview Grid** to sample live data from the configured connection.

#### Page: Admin Console (`AdminPage`) [COMPLETED]
**Description:** System-wide configuration, license management, and health monitoring.
*   **[2 pts]** Implement **License Manager** to view active licenses, expiry dates, and upload new license keys.
*   **[2 pts]** Implement **System Health Dashboard** displaying real-time CPU/Memory usage and service heartbeat status.
*   **[2 pts]** Implement **Retention Policy Manager** to configure archival rules (e.g., "Archive after 1 year") and view hypertable chunk status.
*   **[2 pts]** Implement **Alerting Configuration** to set thresholds for system metrics and configure notification channels (Slack/Email).
*   **[1 pt]** Implement **Log Viewer** to stream logs from the backend services via WebSockets.

#### Page: Data Governance Console (`GovernancePage`) [COMPLETED]
**Description:** Centralized management of data quality, security, and lineage.
*   **[2 pts]** Implement **Data Quality Rules CRUD** to define and manage validation logic.
*   **[2 pts]** Implement **Data Lineage Graph** (using React Flow or D3) to visualize upstream/downstream dependencies.
*   **[2 pts]** Implement **Access Control Manager** to configure Role-Based Access Control (RBAC) and Row-Level Security policies.

    *   **Build Plan:** Create `src/pages/GovernancePage.tsx`.
**Description:** OAuth2/OIDC integration with Azure AD for enterprise users.
*   **[1 pt]** Implement `AzureADAuthProvider` for handling authorization URL generation and token exchange.
*   **[1 pt]** Implement `validate_token` logic for verifying JWT signatures and claims.
*   **[2 pts]** Create API endpoints for login, callback, and logout flows.

#### Feature: Directory Synchronization [COMPLETED]
**Description:** Syncing users and groups from Azure Graph API.
*   **[2 pts]** Implement `AzureADSyncService` to fetch users and groups via Microsoft Graph.
*   **[2 pts]** Implement scheduled background task for periodic synchronization.
*   **[1 pt]** Define database models for `AzureADUser` and `AzureADGroup`.

#### Feature: Role Mapping [COMPLETED]
**Description:** Automating access control based on AD groups.
*   **[1 pt]** Define `RoleMapping` model linking AD groups to Client roles.
*   **[2 pts]** Implement logic to auto-provision/deprovision roles based on group membership changes.
*   **[1 pt]** Create API for managing role mapping rules.

#### Feature: Multi-Tenant Configuration [COMPLETED]
**Description:** Supporting multiple client AD tenants.
*   **[1 pt]** Define `AzureADConfig` model for storing tenant ID, client ID, and secrets.
*   **[2 pts]** Implement API for creating and managing tenant configurations securely.

### 2. Mock Identity Service (Development / Local)
**Bounded Context:** Identity & Access Management for Internal Dev

#### Feature: Mock Identity Provider [COMPLETED]
**Description:** OIDC-compatible mock provider to mirror Production Auth.
*   **[1 pt]** Implement `MockOIDCProvider` container (e.g., using a lightweight OIDC server image) to issue valid JWTs.
*   **[2 pts]** Configure Local Environment to use the Mock Provider for token issuance.
*   **[2 pts]** Ensure strict parity between Mock and Azure AD token claims to prevent environment-specific bugs.
*   **[2 pts]** Implement integration with **Database Service** to persist user profiles and roles consistent with Prod.

#### Feature: Data Quality Rules [COMPLETED]
**Description:** Defining and enforcing data quality.
*   **[2 pts]** Implement rule evaluation logic (e.g., uniqueness, non-null, format).
*   **[2 pts]** Implement validation API to check data against defined rules.

#### Feature: Lineage Tracking [COMPLETED]
**Description:** Tracing data provenance.
*   **[2 pts]** Implement graph model for tracking data movement between entities.
*   **[2 pts]** Implement API to query upstream sources and downstream consumers.
*   **[1 pt]** Implement visualization for lineage graph.

### 4. Machine Learning Service
**Bounded Context:** Predictive Analytics

#### Feature: Model Management [COMPLETED]
**Description:** Lifecycle of ML models.
*   **[2 pts]** Implement Model Registry for versioning trained models (`MLModel`, `MLModelVersion` Pydantic models).
*   **[2 pts]** Implement Inference API for serving predictions (`POST /inference/{model_id}`).
*   **[1 pt]** Implement health check and telemetry for model serving.

#### Feature: Training Pipeline [COMPLETED]
**Description:** Automating model updates.
*   **[2 pts]** Implement job queue for training tasks (`TrainModelCommand`).
*   **[2 pts]** Integration with Database Service to fetch training datasets (via Event-Driven Architecture).
*   **[2 pts]** Implement `JobStatus` tracking and event publication (`training.job.completed`).

### 5. Systems Monitor
**Bounded Context:** Infrastructure Health (Planned)

#### Feature: Resource Monitoring [COMPLETED]
**Description:** Tracking server stats.
*   **[1 pt]** Implement collection of CPU, Memory, Disk usage metrics.
*   **[1 pt]** Expose metrics via Prometheus endpoint (if not handled by Observability).

#### Feature: Alerting [COMPLETED]
**Description:** Notifying on issues.
*   **[2 pts]** Implement rule-based alerting logic.
*   **[1 pt]** Integration with Messaging Service for alert delivery.

---

## DevOps & Automation

### 1. CI/CD Pipeline
**Bounded Context:** Release Engineering

#### Feature: Automated Testing [COMPLETED]
**Description:** Continuous verification of code quality.
*   **[1 pt]** Configure GitHub Actions workflow for Pytest execution on Pull Requests.
*   **[1 pt]** Implement service-specific test discovery logic.

#### Feature: Container Delivery [COMPLETED]
**Description:** Build and push Docker images.
*   **[2 pts]** Configure matrix strategy for building 19+ microservices in parallel.
*   **[1 pt]** Implement Docker Hub authentication and image tagging strategy.

### 2. Documentation Automation
**Bounded Context:** Knowledge Management

#### Feature: Auto-Generated Docs [COMPLETED]
**Description:** Keeping documentation in sync with code.
*   **[2 pts]** Implement `scripts/generate_docs.py` to extract metadata from Python code.
*   **[1 pt]** Configure GitHub Action to commit and push generated docs back to repository.

### 3. Test Infrastructure
**Bounded Context:** Quality Assurance & Developer Experience

#### Feature: Mock Container Environment [COMPLETED]
**Description:** Infrastructure for simulating external dependencies and service failures.
*   **[2 pts]** Implement `MockServiceContainer` (e.g., using WireMock or a custom FastAPI stub) to simulate HTTP responses and error states for negative testing.
*   **[2 pts]** Create `docker-compose.mock.yml` profile to spin up mock instances alongside or instead of real services.
*   **[1 pt]** Implement configuration mechanism (`.env.test`) to dynamically route service traffic to mocks.

#### Feature: Hybrid Debugging Workflow [COMPLETED]
**Description:** Workflow for debugging a local service instance against containerized peers.
*   **[2 pts]** Implement `debug_service.ps1` script to spin up dependencies (DB, Redis, other services) while excluding the target service under debug.
*   **[2 pts]** Configure service discovery/networking to allow the local process (host) to communicate with containerized services.
*   **[1 pt]** Implement toggle logic to select between Real Peers and Mock Containers for specific dependencies.

### 4. Infrastructure Management
**Bounded Context:** Cloud Engineering & Orchestration

#### Feature: Kubernetes Configuration [COMPLETED]
**Description:** Production deployment manifests and management.
*   **[2 pts]** Create Helm charts for all services (`/charts`).
*   **[2 pts]** Define Kubernetes manifests for Deployments, Services, Ingress, ConfigMaps, and Secrets.
*   **[1 pt]** Implement `values.yaml` profiles for Dev, Staging, and Production environments.

#### Feature: Observability Stack Setup [COMPLETED]
**Description:** Infrastructure-level monitoring configuration.
*   **[2 pts]** Configure Prometheus Operator and Grafana Helm charts.
*   **[2 pts]** Set up Jaeger/Zipkin for distributed tracing.
*   **[1 pt]** Create default Grafana dashboards for system health and business metrics.

---

## Developer Tools & Governance

### 1. KPI Excel Processor
**Bounded Context:** Rapid Prototyping & Bulk Import

#### Feature: Bulk Definition Import [COMPLETED]
**Description:** Generating KPI code from spreadsheet templates.
*   **[2 pts]** Implement CSV/Excel parser to extract KPI metadata and formulas.
*   **[2 pts]** Implement Python code generator to create standardized `MetricDefinition` files.
*   **[1 pt]** Implement validation logic to ensure imported formulas reference valid objects.

#### Feature: Formula Safety & Validation [COMPLETED]
**Description:** Mitigating risks of procedural or recursive Excel formulas (SQL Translation Safety).
*   **[1 pt]** Implement **Blacklist Mechanism** to explicitly reject unsupported functions (e.g., `VLOOKUP`, `OFFSET`, `INDIRECT`) that cannot be translated to SQL.
*   **[1 pt]** Implement **Context Boundary Validation** to reject cross-sheet references (`!`) ensuring all data maps to defined Ontology Entities.
*   **[1 pt]** Integrate validation hooks into `KPIExcelProcessor` pipeline to reject invalid rows while preserving valid ones.

#### Page: KPI Excel Import (`ExcelImportPage`) [COMPLETED]
**Description:** Interface for bulk uploading and validating KPI definitions from spreadsheets.
*   **[2 pts]** Implement **File Upload Zone** with drag-and-drop support for `.xlsx` and `.csv` files.
*   **[2 pts]** Implement **Validation Report Viewer** to display row-by-row errors (e.g., "Invalid Function", "Circular Reference") returned by the `KPIExcelProcessor`.
*   **[1 pt]** Implement **Bulk Commit Action** to save valid definitions to the Metadata Service.

#### Page: Ontology Studio (`OntologyManagerPage`) [COMPLETED]
**Description:** Visual editor for defining and modifying the business ontology (Entities, Relationships).
*   **[2 pts]** Implement **Entity Editor Form** to add/edit entities and their attributes.
*   **[2 pts]** Implement **Relationship Builder** to define associations between entities visually.
*   **[1 pt]** Implement **Version History View** to track changes to the ontology definitions.

#### Page: Simulation Controller (`SimulationPage`) [COMPLETED]
**Description:** Control center for generating demo data and running scenarios.
*   **[2 pts]** Implement **Scenario Selector** (e.g., "Churn Spike", "Seasonal Peak") to configure generation parameters.
*   **[1 pt]** Implement **Date Range Picker** to define the simulation window.
*   **[2 pts]** Implement **Job Progress Monitor** to track the status of background generation tasks via WebSockets.

#### Page: ML Model Registry (`MLDashboardPage`) [COMPLETED]
**Description:** Dashboard for managing machine learning models and training jobs.
*   **[2 pts]** Implement **Model List View** showing version, accuracy metrics, and status.
*   **[2 pts]** Implement **Training Job Launcher** to trigger new model training runs on selected datasets.
*   **[1 pt]** Implement **Inference Playground** to test model predictions with manual input.

### 2. Object Model Governance
**Bounded Context:** Schema Consistency & Code Gen

#### Feature: Meta-Model Synchronization [COMPLETED]
**Description:** Keeping code, UML, and JSON definitions in sync via the Business Metadata Service.
*   **[2 pts]** Implement `ConsistencyChecker` background job (in Metadata Service) to validate referential integrity between Entities and KPIs.
*   **[2 pts]** Implement API endpoint `GET /metadata/graph/uml` to generate PlantUML/D3 diagrams dynamically from the current ontology state.

#### Feature: KPI Consolidation [COMPLETED]
**Description:** Identifying and merging duplicate metrics using NLP-based semantic similarity.
*   **[2 pts]** Implement `SimilarityEngine` in **Metadata Ingestion Service** integrating with **Entity Resolution Service** for NLP-based duplicate detection.
    - Use Entity Resolution Service's semantic extraction to compare KPI names and descriptions
    - Calculate Jaccard similarity on extracted entities and noun phrases (not string fuzzy matching)
    - Return shared entities and phrases as evidence for duplicate candidates
    - Fallback to rapidfuzz when Entity Resolution Service is unavailable
*   **[2 pts]** Implement API endpoint `POST /metadata/kpis/merge` to execute consolidation logic transactionally in the database.

#### Feature: Code Generation [COMPLETED]
**Description:** Automating boilerplate creation via CLI wrappers.
*   **[2 pts]** Implement `tools/codegen/generate_models.py` as a CLI wrapper that calls the Metadata Service API to fetch definitions and generate Pydantic/SQLAlchemy files.
*   **[1 pt]** Implement `tools/codegen/validate_schema.py` to check deployed DB schema against Metadata Service definitions (CI/CD step).

### 3. Migration & Schema Utilities
**Bounded Context:** Database Schema Management & Automation

#### Feature: Schema Extraction [COMPLETED]
**Description:** Extract table schemas from object models to JSON files for CQRS automation.
*   **[2 pts]** Implement `extract_table_schemas.py` to read object models and generate JSON schema definitions.
*   **[1 pt]** Support extraction for specific domains (e.g., SCOR) or all object models.
*   **[1 pt]** Generate schema files with metadata (entity name, code, description, module).

#### Feature: CQRS Schema Generation [COMPLETED]
**Description:** Automate addition of schema objects with proper CQRS pattern.
*   **[2 pts]** Implement `add_cqrs_schema.ps1` to add write models to `app/models.py` and read models to domain folders.
*   **[2 pts]** Implement automatic Alembic migration generation with validation.
*   **[1 pt]** Implement duplicate detection and import conflict prevention.
*   **[1 pt]** Support dry-run mode for previewing changes.

#### Feature: CQRS Validation [COMPLETED]
**Description:** Validate CQRS model consistency across services.
*   **[2 pts]** Implement `validate_cqrs_models.ps1` to check write/read model alignment.
*   **[1 pt]** Validate field names, data types, and model completeness.
*   **[1 pt]** Generate validation reports with actionable recommendations.

#### Feature: Migration Management [COMPLETED]
**Description:** Helper scripts for Alembic migration lifecycle management.
*   **[1 pt]** Implement `create_revision_clean.ps1` for creating clean Alembic migrations.
*   **[1 pt]** Implement `upgrade_service.ps1` for upgrading service migrations.
*   **[1 pt]** Implement `run_migration_reset.ps1` for development migration resets.
*   **[1 pt]** Implement `resolve_service_heads.ps1` for resolving migration conflicts.

#### Feature: CI/CD Integration [COMPLETED]
**Description:** Integration scripts for continuous integration and deployment.
*   **[2 pts]** Implement `ci_cd_integration.ps1` for automated migration validation.
*   **[2 pts]** Implement `enhanced_docker_deploy.ps1` for deployment with migrations.
*   **[1 pt]** Support migration validation in GitHub Actions workflows.

## Execution Lifecycle Example
**Scenario:** Health Insurer Retention Analysis

### Phase 1: Definition & Ingestion
*   **Business Metadata Service:** Define `Policy` and `Member` entities. Define `RetentionRate` metric with formula: `1 - ((StartCount - EndCount) / StartCount)`.
*   **Connector Service (or Demo Data Generator):** Configure connection to Insurer's Policy Admin System (SQL Database) OR generate synthetic "Retention Scenario" data for demonstration.
*   **Ingestion Service:** Schedule daily job to fetch `PolicyStatus` snapshots.

### Phase 2: Mapping & Configuration
*   **Demo/Config UI:** Use **Visual Data Mapping** to bind Source `Policy_ID`, `Status`, `Effective_Date` to Ontology attributes.
*   **Ingestion Service (Data Standardization):** Normalize `Status` codes (e.g., 'Active', 'Terminated') to standard enums.
*   **Entity Resolution Service:** Resolve `Member` identities across different policy periods to track tenure.

### Phase 3: Processing & Calculation
*   **1. Event Trigger:**
    *   **Connector Service** finishes daily batch -> Publishes `ingestion.completed` event to `Messaging Service`.
    *   **Calculation Engine (Stream Processor)** subscribes to `ingestion.completed`. Triggers recalculation for "Daily Retention".
*   **2. Data Retrieval:**
    *   **Calculation Engine** queries **Database Service** for raw counts:
        *   *Query A (Start Count $S$)*: `SELECT count(distinct policy_id) FROM policy_snapshots WHERE date = $T_{start} AND status='Active'`
        *   *Query B (End Count $E$)*: `SELECT count(distinct policy_id) FROM policy_snapshots WHERE date = $T_{end} AND status='Active'`
        *   *Query C (New Count $N$)*: `SELECT count(distinct policy_id) FROM policy_snapshots WHERE date = $T_{end} AND start_date > $T_{start}`
*   **3. Execution Logic:**
    *   **Domain Handler** applies formula: $Retention = \frac{E - N}{S}$ (Standard Industry Definition).
    *   *Example:* Start=1000, End=950, New=50.
    *   $Retained = 950 - 50 = 900$.
    *   $Rate = 900 / 1000 = 90.0\%$.
*   **4. Publication & Caching:**
    *   **Calculation Engine** publishes result event `{ "metric": "Retention", "value": 0.90, "dims": {"LOB": "Health"} }` to `Messaging Service`.
    *   **Calculation Engine** writes result to Redis (via **Result Caching** feature) with 24h TTL for instant API access.
    *   **Database Service** subscribes to result event -> Persists to `metric_history` table for long-term trend analysis.

### Phase 4: Visualization & Action
*   **API Gateway:** Route dashboard request for "Q3 Retention".
*   **Demo/Config UI (Dashboard):** Visualize Retention Rate trend. Drill down into "Dropped" bucket (Set A - Set B).
*   **Observability Service (Alerting):** Trigger Slack alert if Retention drops below 85%.

## Execution Lifecycle Example 2
**Scenario:** Sales KPI Dashboard from Excel Definitions

### Phase 1: Ontology Deconstruction (Metadata Ingestion)
*   **KPI Excel Processor:** Admin uploads `KPI_Definitions.xlsx` containing business logic (e.g., "Sales Efficiency = Revenue / Headcount").
*   **Semantic Mapping Engine:** Decomposes formulas into required Entities (`SalesPerson`, `Order`) and Attributes (`Revenue`, `Count`).
*   **Industry Knowledge Base:** Maps identified entities to the "Sales Management" Value Chain.
*   **Business Metadata Service:** Persists the new Ontology (Entities + Metrics) and Value Chain relationships.

### Phase 2: Execution Artifact Generation
*   **Business Metadata Service:** Triggers `generate_timescaledb_schemas` event.
*   **Database Service:** Automatically creates new Hypertables (`sales_orders`, `sales_people`) and Relational Tables based on the defined Ontology.
*   **Dynamic Calculation Engine:** Compiles the Excel formulas into SQL ASTs ready for execution against the new schema.

### Phase 3: Scenario Simulation
*   **Demo/Config Service:** User selects "Sales Growth Scenario" in the Data Generator.
*   **Scenario Generator:** Populates the newly created `sales_orders` hypertables with synthetic data matching the defined attributes (Date, Amount, Region).
*   **Calculation Engine:** Executes the dynamic SQL formulas against the generated data to compute the KPIs.

### Phase 4: Visualization (Reference UI)
*   **Demo/Config UI:** User selects "Sales Management" Dashboard.
*   **UI Customization:** React components render charts matching the look-and-feel of `C:\Users\Arthu\OneDrive\Documents\CascadeProjects\sales_demo` (HTML Reference).
*   **API Gateway:** Serves aggregated JSON: `GET /metrics/sales?group_by=region`.

## Execution Lifecycle Example 3
**Scenario:** Chatbot-Driven Design (Supply Chain)

### Phase 1: Dialogue Capture
*   **Conversation Service:** CEO engages with Chatbot: "I need to see inventory turnover in real-time from my ERP."
*   **Session Management:** Service maintains context, asking clarifying questions: "Which ERP system? SAP or Oracle?"
*   **LLM & NLP Pipeline:** Parses utterances to extract Business Intents: `[Monitor Inventory]`, `[Real-time Latency]`, `[Source: ERP]`.

### Phase 2: Semantic Deconstruction
*   **Pattern Matching Engine:** Matches "Inventory Turnover" intent to the **Standard Supply Chain Model**.
*   **Strategic Recommendation:** Queries **Metadata Ingestion Service** for "Best Practice Supply Chain KPIs".
*   **Gap Analysis:** Identifies that standard "Turnover" requires `COGS` and `Average Inventory` entities.

### Phase 3: Solution Design
*   **Design Suggestion Engine:** Proposes a `ValueChainModel` containing:
    *   **Entities:** `Product`, `Warehouse`, `InventoryTransaction`.
    *   **KPIs:** `Inventory Turnover Ratio`, `Days Sales of Inventory`.
*   **Service Proposal Generation:** **Demo/Config Service** generates a PDF SOW: "Implementation of Real-Time Supply Chain Analytics".

### Phase 4: Confirmation & Build
*   **Interactive API:** User clicks "Approve Proposal" in the Chat UI.
*   **Execution Artifact Generation:** System automatically generates the TimescaleDB schema for `inventory_transactions` and configures the `Connector Service` for the ERP.

### Phase 5: Validation & Deployment
*   **Visual Data Mapping (UI):** CEO/Admin uses drag-and-drop to map ERP columns (e.g., `MATNR`, `WERKS`) to the proposed Ontology attributes (`Product_ID`, `Warehouse_ID`).
*   **Connection Testing:** Connector Service runs a sample query against the ERP using the provided credentials to verify connectivity and schema alignment.
*   **Mapping Verification:** Ingestion Service runs a "Dry Run" ETL job to ensure 100 rows can be successfully transformed without errors.
*   **Dashboard Preview:** User views the "Inventory Analytics" dashboard with live sample data to confirm the "Turnover Ratio" calculation is accurate.


## Execution Lifecycle Example 4
**Scenario:** Developer debugging

* Developer is able to debug the service they have checked out while utilizing the full cotainer services of the rest of the application.