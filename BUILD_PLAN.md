# Analytics Engine - Build Plan

**Version**: 1.0  
**Date**: November 11, 2025  
**Status**: Active Development

---

## 🎯 Project Status Overview

### **Completed ✅**
- ✅ Architecture design and documentation
- ✅ Service classification (Business, Backend, Frontend, Support)
- ✅ Analytics Metadata Service (fully operational)
- ✅ Calculation Engine Service (architecture complete, methods stubbed)
- ✅ Demo Config Service (architecture complete, methods stubbed)
- ✅ Functional specification document
- ✅ Service interplay documentation
- ✅ Data access architecture decisions
- ✅ Service proposal and pricing model design
- ✅ UML diagram viewer (frontend)

### **In Progress ⚠️**
- ⚠️ Streaming infrastructure implementation
- ⚠️ Database Service stream publisher
- ⚠️ Calculation Engine stream processor
- ⚠️ API Gateway WebSocket support

### **Not Started ⬜**
- ⬜ Service proposal generator implementation
- ⬜ Resource scheduling tool
- ⬜ Infrastructure cost calculator
- ⬜ Frontend integration with business services
- ⬜ Authentication and authorization
- ⬜ Production deployment configuration

---

## 📋 Build Phases

### **Phase 1: Core Streaming Infrastructure (HIGH PRIORITY)**
**Goal**: Enable real-time dashboard with configurable refresh periods

**Estimated Duration**: 3-4 weeks  
**Team**: 2 developers

#### **1.1 Database Service - Stream Publisher**
**Priority**: CRITICAL  
**Estimated**: 1 week

**Tasks:**
- [ ] Implement `PeriodBasedPublisher` class
  - [ ] Monitor TimescaleDB continuous aggregates
  - [ ] Publish updates to messaging service
  - [ ] Support minute/hour/day periods
  - [ ] Track subscriber counts
  - [ ] Start/stop publishing based on subscribers

- [ ] Create TimescaleDB continuous aggregates
  - [ ] `kpi_values_minute` view
  - [ ] `kpi_values_hour` view
  - [ ] `kpi_values_day` view
  - [ ] Auto-refresh policies

- [ ] Implement subscriber management
  - [ ] `add_subscriber()` endpoint
  - [ ] `remove_subscriber()` endpoint
  - [ ] Subscriber count tracking per KPI/period

- [ ] Add HTTP endpoints
  - [ ] `POST /stream/start` - Start publishing for KPI/period
  - [ ] `POST /stream/stop` - Stop publishing
  - [ ] `GET /stream/status` - Get active streams

**Files to Create/Modify:**
```
services/backend_services/database_service/
├── app/
│   ├── stream_publisher.py          # NEW
│   ├── subscriber_manager.py        # NEW
│   └── main.py                      # MODIFY - add stream endpoints
└── migrations/
    └── create_continuous_aggregates.sql  # NEW
```

**Testing:**
- [ ] Unit tests for publisher
- [ ] Integration tests with messaging service
- [ ] Load test with 100+ concurrent streams

---

#### **1.2 Calculation Engine - Stream Processor**
**Priority**: CRITICAL  
**Estimated**: 1 week

**Tasks:**
- [ ] Implement `StreamProcessor` class
  - [ ] Subscribe to data streams from messaging service
  - [ ] Process incoming data continuously
  - [ ] Calculate KPIs in real-time
  - [ ] Publish results to messaging service

- [ ] Implement streaming calculation methods
  - [ ] `calculate_streaming()` in base handler
  - [ ] Update SCOR handler for streaming
  - [ ] Update CRM handler for streaming (future)
  - [ ] Update Sales handler for streaming (future)

- [ ] Implement result publishing
  - [ ] Publish to `kpi.updates.{code}.{period}` channel
  - [ ] Include metadata (timestamp, data points, etc.)
  - [ ] Handle errors gracefully

- [ ] Add subscription management
  - [ ] Subscribe on startup
  - [ ] Unsubscribe on shutdown
  - [ ] Reconnect on disconnect

**Files to Create/Modify:**
```
services/business_services/calculation_engine_service/
├── app/
│   ├── stream_processor.py          # NEW
│   ├── handlers/
│   │   ├── base_handler.py          # MODIFY - add streaming methods
│   │   └── scor_handler.py          # MODIFY - implement streaming
│   └── main.py                      # MODIFY - start stream processor
```

**Testing:**
- [ ] Unit tests for stream processor
- [ ] Integration tests with messaging service
- [ ] End-to-end test with database → calculation → results

---

#### **1.3 API Gateway - WebSocket Support**
**Priority**: CRITICAL  
**Estimated**: 1 week

**Tasks:**
- [ ] Implement WebSocket endpoints
  - [ ] `/ws/kpi/{code}` - Stream single KPI
  - [ ] `/ws/dashboard/{id}` - Stream multiple KPIs
  - [ ] Query parameter: `?period=minute|hour|day`

- [ ] Implement WebSocket connection management
  - [ ] Accept connections
  - [ ] Subscribe to messaging channels
  - [ ] Forward messages to clients
  - [ ] Handle disconnections
  - [ ] Notify database service of subscriber changes

- [ ] Implement pub/sub bridge
  - [ ] Subscribe to messaging service channels
  - [ ] Queue messages for WebSocket clients
  - [ ] Handle backpressure

- [ ] Add connection monitoring
  - [ ] Track active connections
  - [ ] Health checks
  - [ ] Automatic reconnection

**Files to Create/Modify:**
```
services/frontend_services/api_gateway/
├── app/
│   ├── websocket/
│   │   ├── __init__.py              # NEW
│   │   ├── kpi_stream.py            # NEW
│   │   ├── dashboard_stream.py      # NEW
│   │   └── connection_manager.py    # NEW
│   └── main.py                      # MODIFY - add WebSocket routes
```

**Testing:**
- [ ] Unit tests for WebSocket handlers
- [ ] Integration tests with messaging service
- [ ] Load test with 1000+ concurrent connections
- [ ] Test reconnection logic

---

#### **1.4 Frontend - Streaming Dashboard**
**Priority**: HIGH  
**Estimated**: 1 week

**Tasks:**
- [ ] Create streaming KPI hooks
  - [ ] `useStreamingKPI(code, period)` hook
  - [ ] `useStreamingDashboard(kpis, period)` hook
  - [ ] WebSocket connection management
  - [ ] Automatic reconnection

- [ ] Create streaming UI components
  - [ ] `StreamingKPICard` component
  - [ ] `StreamingDashboard` component
  - [ ] Period selector (minute/hour/day)
  - [ ] Connection status indicator
  - [ ] Last update timestamp

- [ ] Implement initial HTTP load
  - [ ] Fetch current value via REST
  - [ ] Display immediately
  - [ ] Then connect WebSocket for updates

- [ ] Add error handling
  - [ ] Connection errors
  - [ ] Timeout handling
  - [ ] Retry logic
  - [ ] User notifications

**Files to Create/Modify:**
```
services/frontend_services/demo_config_ui/src/
├── hooks/
│   ├── useStreamingKPI.ts           # NEW
│   └── useStreamingDashboard.ts     # NEW
├── components/
│   ├── StreamingKPICard.tsx         # NEW
│   ├── StreamingDashboard.tsx       # NEW
│   └── PeriodSelector.tsx           # NEW
└── pages/
    └── DashboardPage.tsx            # NEW
```

**Testing:**
- [ ] Unit tests for hooks
- [ ] Component tests
- [ ] Integration tests with API Gateway
- [ ] User acceptance testing

---

### **Phase 2: One-Time Query Support (MEDIUM PRIORITY)**
**Goal**: Support ad-hoc queries and historical analysis

**Estimated Duration**: 2 weeks  
**Team**: 1 developer

#### **2.1 Database Service - HTTP Query Client**
**Priority**: MEDIUM  
**Estimated**: 3 days

**Tasks:**
- [ ] Implement query endpoints
  - [ ] `POST /query` - Execute SQL query
  - [ ] `POST /query/kpi` - Query KPI data
  - [ ] `GET /query/history/{code}` - Historical data

- [ ] Implement query builder
  - [ ] Build SQL from parameters
  - [ ] Support filters, date ranges
  - [ ] Support aggregations

- [ ] Add caching layer
  - [ ] Cache query results
  - [ ] TTL-based expiration
  - [ ] Cache invalidation

**Files to Create/Modify:**
```
services/backend_services/database_service/
├── app/
│   ├── query_builder.py             # NEW
│   ├── query_cache.py               # NEW
│   └── api/
│       └── queries.py               # NEW
```

---

#### **2.2 Calculation Engine - On-Demand Mode**
**Priority**: MEDIUM  
**Estimated**: 4 days

**Tasks:**
- [ ] Implement HTTP query methods
  - [ ] `query_data()` in base handler
  - [ ] HTTP client for database service
  - [ ] Error handling and retries

- [ ] Implement synchronous calculation
  - [ ] Query data via HTTP
  - [ ] Calculate KPI
  - [ ] Return result immediately

- [ ] Add result caching
  - [ ] Cache calculation results
  - [ ] Configurable TTL
  - [ ] Cache key generation

**Files to Create/Modify:**
```
services/business_services/calculation_engine_service/
├── app/
│   ├── clients/
│   │   └── database_client.py       # NEW
│   ├── handlers/
│   │   └── base_handler.py          # MODIFY - implement query_data()
│   └── cache/
│       └── result_cache.py          # NEW
```

---

#### **2.3 Frontend - Ad-Hoc Query UI**
**Priority**: MEDIUM  
**Estimated**: 3 days

**Tasks:**
- [ ] Create query builder UI
  - [ ] KPI selector
  - [ ] Date range picker
  - [ ] Filter builder
  - [ ] Aggregation selector

- [ ] Create results display
  - [ ] Table view
  - [ ] Chart view
  - [ ] Export to CSV/Excel

**Files to Create/Modify:**
```
services/frontend_services/demo_config_ui/src/
├── components/
│   ├── QueryBuilder.tsx             # NEW
│   ├── QueryResults.tsx             # NEW
│   └── DataExport.tsx               # NEW
└── pages/
    └── QueryPage.tsx                # NEW
```

---

### **Phase 3: Service Proposal Generator (HIGH PRIORITY)**
**Goal**: Automate proposal generation from KPI cart

**Estimated Duration**: 3 weeks  
**Team**: 2 developers

#### **3.1 Proposal Calculation Engine**
**Priority**: HIGH  
**Estimated**: 1 week

**Tasks:**
- [ ] Implement pricing calculator
  - [ ] Licensing calculator (value chain-based)
  - [ ] SOW calculator (integration + KPI costs)
  - [ ] Infrastructure cost estimator
  - [ ] Managed services calculator

- [ ] Implement questionnaire logic
  - [ ] 8-step questionnaire flow
  - [ ] Validation rules
  - [ ] Default values
  - [ ] Conditional questions

- [ ] Implement proposal generator
  - [ ] Generate proposal document
  - [ ] Calculate totals (Year 1, recurring, term)
  - [ ] Format as PDF/Word
  - [ ] Include all sections

**Files to Create/Modify:**
```
services/business_services/demo_config_service/
├── app/
│   ├── proposal/
│   │   ├── __init__.py              # NEW
│   │   ├── calculator.py            # NEW
│   │   ├── questionnaire.py         # NEW
│   │   ├── generator.py             # NEW
│   │   └── templates/
│   │       └── proposal_template.md # NEW
│   └── api/
│       └── proposals.py             # MODIFY - add endpoints
```

**Testing:**
- [ ] Unit tests for calculators
- [ ] Integration tests
- [ ] Test with various scenarios
- [ ] Validate pricing accuracy

---

#### **3.2 Resource Scheduling Tool**
**Priority**: HIGH  
**Estimated**: 1 week

**Tasks:**
- [ ] Implement resource availability tracking
  - [ ] Define resource types (Developer, Architect, etc.)
  - [ ] Track availability calendar
  - [ ] Track current assignments

- [ ] Implement scheduling algorithm
  - [ ] Assign resources to tasks
  - [ ] Respect availability constraints
  - [ ] Optimize for timeline
  - [ ] Handle conflicts

- [ ] Implement timeline generator
  - [ ] Calculate project timeline
  - [ ] Generate Gantt chart data
  - [ ] Identify critical path

**Files to Create/Modify:**
```
services/business_services/demo_config_service/
├── app/
│   ├── scheduling/
│   │   ├── __init__.py              # NEW
│   │   ├── resource_manager.py      # NEW
│   │   ├── scheduler.py             # NEW
│   │   └── timeline_generator.py    # NEW
│   └── models/
│       └── resource.py              # NEW
```

---

#### **3.3 Proposal UI**
**Priority**: HIGH  
**Estimated**: 1 week

**Tasks:**
- [ ] Create questionnaire wizard
  - [ ] 8-step wizard component
  - [ ] Progress indicator
  - [ ] Navigation (next/back)
  - [ ] Form validation

- [ ] Create proposal preview
  - [ ] Live cost calculation
  - [ ] Section-by-section preview
  - [ ] Edit capability
  - [ ] Export options (PDF, Word)

- [ ] Create resource schedule view
  - [ ] Gantt chart visualization
  - [ ] Resource allocation view
  - [ ] Timeline view

**Files to Create/Modify:**
```
services/frontend_services/demo_config_ui/src/
├── components/
│   ├── ProposalWizard/
│   │   ├── Step1_Licensing.tsx      # NEW
│   │   ├── Step2_DataIntegration.tsx # NEW
│   │   ├── Step3_KPIComplexity.tsx  # NEW
│   │   ├── Step4_Environment.tsx    # NEW
│   │   ├── Step5_Retention.tsx      # NEW
│   │   ├── Step6_Infrastructure.tsx # NEW
│   │   ├── Step7_ManagedServices.tsx # NEW
│   │   └── Step8_Review.tsx         # NEW
│   ├── ProposalPreview.tsx          # NEW
│   └── ResourceSchedule.tsx         # NEW
└── pages/
    └── ProposalPage.tsx             # NEW
```

---

### **Phase 4: Data Archival Implementation (MEDIUM PRIORITY)**
**Goal**: Implement data lifecycle management

**Estimated Duration**: 2 weeks  
**Team**: 1 developer

#### **4.1 Archival Service Implementation**
**Priority**: MEDIUM  
**Estimated**: 1 week

**Tasks:**
- [ ] Implement archival endpoints
  - [ ] `POST /archive` - Archive data
  - [ ] `GET /archive/{id}` - Retrieve archived data
  - [ ] `GET /archive/status` - Archive status

- [ ] Implement compression
  - [ ] gzip compression
  - [ ] Parquet format for analytics data
  - [ ] Metadata storage

- [ ] Implement cold storage integration
  - [ ] S3/Azure Blob integration
  - [ ] Upload compressed archives
  - [ ] Download on demand

**Files to Create/Modify:**
```
services/backend_services/archival_service/
├── app/
│   ├── archiver.py                  # NEW
│   ├── compressor.py                # NEW
│   ├── storage/
│   │   ├── s3_storage.py            # NEW
│   │   └── azure_storage.py         # NEW
│   └── api/
│       └── archival.py              # NEW
```

---

#### **4.2 Database Service - Retention Policies**
**Priority**: MEDIUM  
**Estimated**: 3 days

**Tasks:**
- [ ] Implement retention policy management
  - [ ] Store policies per client
  - [ ] Monitor data age
  - [ ] Trigger archival automatically

- [ ] Implement pre-archival hooks
  - [ ] TimescaleDB trigger functions
  - [ ] Call archival service before drop
  - [ ] Verify successful archive

**Files to Create/Modify:**
```
services/backend_services/database_service/
├── app/
│   ├── retention/
│   │   ├── __init__.py              # NEW
│   │   ├── policy_manager.py        # NEW
│   │   └── archival_trigger.py      # NEW
│   └── migrations/
│       └── add_retention_triggers.sql # NEW
```

---

#### **4.3 Historical Data Retrieval**
**Priority**: MEDIUM  
**Estimated**: 4 days

**Tasks:**
- [ ] Implement seamless retrieval
  - [ ] Check active database first
  - [ ] Query archival service if needed
  - [ ] Merge active + archived data

- [ ] Add to calculation engine
  - [ ] Support historical date ranges
  - [ ] Retrieve from archive automatically
  - [ ] Cache retrieved data

**Files to Create/Modify:**
```
services/business_services/calculation_engine_service/
├── app/
│   ├── clients/
│   │   └── archival_client.py       # NEW
│   └── handlers/
│       └── base_handler.py          # MODIFY - add archive support
```

---

### **Phase 5: Authentication & Authorization (HIGH PRIORITY)**
**Goal**: Secure the platform

**Estimated Duration**: 2 weeks  
**Team**: 1 developer

#### **5.1 Authentication Service**
**Priority**: HIGH  
**Estimated**: 1 week

**Tasks:**
- [ ] Implement JWT authentication
  - [ ] Login endpoint
  - [ ] Token generation
  - [ ] Token validation
  - [ ] Refresh tokens

- [ ] Implement user management
  - [ ] User registration
  - [ ] Password hashing
  - [ ] Password reset
  - [ ] User profiles

**Files to Create/Modify:**
```
services/support_services/auth_service/      # NEW
├── app/
│   ├── auth.py
│   ├── users.py
│   └── tokens.py
```

---

#### **5.2 Authorization (RBAC)**
**Priority**: HIGH  
**Estimated**: 1 week

**Tasks:**
- [ ] Implement role-based access control
  - [ ] Define roles (Admin, User, Viewer)
  - [ ] Define permissions
  - [ ] Role assignment

- [ ] Implement data-level security
  - [ ] Client data isolation
  - [ ] KPI-level permissions
  - [ ] Dashboard permissions

- [ ] Add to API Gateway
  - [ ] Middleware for auth validation
  - [ ] Permission checks
  - [ ] Audit logging

**Files to Create/Modify:**
```
services/frontend_services/api_gateway/
├── app/
│   ├── middleware/
│   │   ├── auth_middleware.py       # NEW
│   │   └── rbac_middleware.py       # NEW
│   └── security/
│       └── permissions.py           # NEW
```

---

### **Phase 6: Production Deployment (CRITICAL)**
**Goal**: Deploy to production environment

**Estimated Duration**: 2 weeks  
**Team**: 2 developers + 1 DevOps

#### **6.1 Docker & Kubernetes**
**Priority**: CRITICAL  
**Estimated**: 1 week

**Tasks:**
- [ ] Create Dockerfiles for all services
- [ ] Create docker-compose for local dev
- [ ] Create Kubernetes manifests
  - [ ] Deployments
  - [ ] Services
  - [ ] Ingress
  - [ ] ConfigMaps
  - [ ] Secrets

- [ ] Set up CI/CD pipeline
  - [ ] GitHub Actions / GitLab CI
  - [ ] Build and push images
  - [ ] Deploy to staging
  - [ ] Deploy to production

**Files to Create:**
```
AnalyticsEngine/
├── docker/
│   ├── api_gateway.Dockerfile
│   ├── metadata_service.Dockerfile
│   ├── calculation_engine.Dockerfile
│   ├── database_service.Dockerfile
│   └── messaging_service.Dockerfile
├── k8s/
│   ├── deployments/
│   ├── services/
│   ├── ingress/
│   └── configmaps/
└── .github/
    └── workflows/
        └── deploy.yml
```

---

#### **6.2 Monitoring & Observability**
**Priority**: CRITICAL  
**Estimated**: 1 week

**Tasks:**
- [ ] Set up Prometheus metrics
  - [ ] Service metrics
  - [ ] Business metrics
  - [ ] Custom metrics

- [ ] Set up Grafana dashboards
  - [ ] System health dashboard
  - [ ] Business metrics dashboard
  - [ ] Alert dashboard

- [ ] Set up distributed tracing
  - [ ] OpenTelemetry integration
  - [ ] Jaeger/Zipkin setup
  - [ ] Trace all requests

- [ ] Set up logging
  - [ ] Centralized logging (ELK/Loki)
  - [ ] Log aggregation
  - [ ] Log search

**Files to Create/Modify:**
```
AnalyticsEngine/
├── monitoring/
│   ├── prometheus/
│   │   └── prometheus.yml
│   ├── grafana/
│   │   └── dashboards/
│   └── alerts/
│       └── alert_rules.yml
```

---

## 🎯 Priority Matrix

### **Critical Path (Must Complete First)**
1. ✅ Architecture & Design (COMPLETE)
2. 🔄 Phase 1: Streaming Infrastructure (IN PROGRESS)
3. ⏳ Phase 5: Authentication & Authorization
4. ⏳ Phase 6: Production Deployment

### **High Priority (Core Features)**
1. ⏳ Phase 3: Service Proposal Generator
2. ⏳ Phase 2: One-Time Query Support

### **Medium Priority (Enhancement Features)**
1. ⏳ Phase 4: Data Archival Implementation

---

## 📅 Recommended Timeline

### **Sprint 1-2 (Weeks 1-4): Streaming Infrastructure**
- Database Service stream publisher
- Calculation Engine stream processor
- API Gateway WebSocket support
- Frontend streaming dashboard

**Deliverable**: Working real-time dashboard with minute/hour/day refresh

---

### **Sprint 3-4 (Weeks 5-8): Service Proposal Generator**
- Proposal calculation engine
- Resource scheduling tool
- Proposal UI wizard
- PDF/Word export

**Deliverable**: Automated proposal generation from KPI cart

---

### **Sprint 5 (Weeks 9-10): One-Time Queries**
- Database Service query endpoints
- Calculation Engine on-demand mode
- Frontend query builder UI

**Deliverable**: Ad-hoc query and historical analysis capability

---

### **Sprint 6 (Weeks 11-12): Authentication & Security**
- Authentication service
- RBAC implementation
- API Gateway security middleware

**Deliverable**: Secure, multi-tenant platform

---

### **Sprint 7-8 (Weeks 13-16): Production Deployment**
- Docker & Kubernetes setup
- CI/CD pipeline
- Monitoring & observability
- Load testing

**Deliverable**: Production-ready deployment

---

### **Sprint 9 (Weeks 17-18): Data Archival**
- Archival service implementation
- Retention policy management
- Historical data retrieval

**Deliverable**: Complete data lifecycle management

---

## 🧪 Testing Strategy

### **Unit Tests**
- All business logic
- Calculators and algorithms
- Data transformations
- Target: 80% code coverage

### **Integration Tests**
- Service-to-service communication
- Database operations
- Messaging service integration
- API endpoints

### **End-to-End Tests**
- Complete user workflows
- Real-time dashboard updates
- Proposal generation
- Query execution

### **Performance Tests**
- Load testing (1000+ concurrent users)
- Stress testing
- Streaming performance
- Database query performance

### **Security Tests**
- Authentication bypass attempts
- Authorization checks
- SQL injection
- XSS attacks

---

## 📊 Success Metrics

### **Performance Targets**
- Initial page load: < 2 seconds
- Streaming update latency: < 1 second
- One-time query: < 3 seconds
- WebSocket connection: < 500ms
- Support 1000+ concurrent users
- 99.9% uptime

### **Business Metrics**
- Proposal generation time: < 5 minutes
- Proposal accuracy: 100%
- Resource scheduling efficiency: > 90%
- Customer satisfaction: > 4.5/5

---

## 🚀 Next Immediate Actions

### **This Week (Week 1)**
1. ✅ Complete architecture documentation (DONE)
2. ✅ Complete functional specification (DONE)
3. 🔄 Start Phase 1.1: Database Service stream publisher
4. 🔄 Set up development environment
5. 🔄 Create project board with all tasks

### **Next Week (Week 2)**
1. Complete Database Service stream publisher
2. Start Calculation Engine stream processor
3. Begin API Gateway WebSocket implementation
4. Write unit tests for completed components

### **Week 3**
1. Complete Calculation Engine stream processor
2. Complete API Gateway WebSocket support
3. Begin frontend streaming dashboard
4. Integration testing

### **Week 4**
1. Complete frontend streaming dashboard
2. End-to-end testing
3. Performance testing
4. Demo to stakeholders

---

## 📝 Notes

### **Technical Debt to Address**
- Calculation Engine has stubbed methods (query_data, publish_result)
- Need to implement actual database queries in SCOR handler
- Need to add comprehensive error handling
- Need to add logging throughout

### **Dependencies**
- TimescaleDB setup required
- Redis setup required
- Message broker configuration
- Cloud infrastructure (AWS/Azure/GCP)

### **Risks & Mitigations**
- **Risk**: WebSocket scalability issues
  - **Mitigation**: Load balancing, connection pooling
- **Risk**: Streaming data volume too high
  - **Mitigation**: Backpressure handling, rate limiting
- **Risk**: Complex proposal calculations
  - **Mitigation**: Thorough testing, validation rules

---

**Last Updated**: November 11, 2025  
**Next Review**: End of Sprint 1 (Week 2)
