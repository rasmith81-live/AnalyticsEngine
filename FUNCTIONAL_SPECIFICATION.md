# Analytics Engine - Functional Specification

**Version**: 1.0  
**Date**: November 11, 2025  
**Status**: Living Document (Updated as requirements evolve)

---

## 📋 Document Purpose

This document captures all design requirements, architectural decisions, and functional specifications for the Analytics Engine platform. It serves as the single source of truth for system design and will be updated continuously as new requirements are discussed.

---

## 🎯 System Overview

### **Product Vision**
A real-time, streaming-first analytics platform that provides on-demand KPI calculations with configurable refresh periods, supporting both continuous monitoring and ad-hoc analysis.

### **Core Premise**
- **Real-time on-demand calculation** (NOT pre-computed batch analytics)
- **Streaming-first architecture** (80% streaming, 20% one-time queries)
- **Microservices architecture** for independent scaling and performance isolation
- **TimescaleDB** for time-series data and continuous aggregates

---

## 🏗️ Architecture Overview

### **Service Classification**

#### **Business Services** (Core business value, client-facing)
- `analytics_metadata_service` - KPI definitions, object models, modules, value chains
- `calculation_engine_service` - Real-time KPI calculations (streaming + on-demand)
- `demo_config_service` - Client configuration, custom KPIs, service proposals

#### **Backend Services** (Infrastructure support)
- `messaging_service` - Redis pub/sub for inter-service communication
- `database_service` - TimescaleDB data access and stream publishing
- `archival_service` - Data archival and retention management (integrates with database_service)

#### **Frontend Services** (User interfaces)
- `demo_config_ui` - React-based configuration and visualization UI
- `api_gateway` - Unified API entry point, WebSocket support

#### **Support Services** (Optional capabilities)
- `machine_learning_service` - ML-based analytics
- `entity_resolution_service` - Data quality
- `systems_monitor` - Observability and monitoring

---

## 📊 Communication Patterns

### **Pattern 1: Frontend → Business Services**
```
Frontend → API Gateway → Business Services (HTTP REST)
```
**Use Cases:**
- Fetch KPI definitions
- Fetch object models
- Client configuration management
- Initial dashboard load

### **Pattern 2: Backend ↔ Backend Services**
```
Backend Service ↔ Backend Service (Redis Pub/Sub via Messaging Service)
```
**Use Cases:**
- Event notifications
- Service-to-service messaging
- Asynchronous workflows

### **Pattern 3: Backend → Business Services**
```
Backend Service → Business Service (HTTP REST via API Gateway)
```
**Use Cases:**
- Database Service → Metadata Service
- Support Services → Business Services

### **Pattern 4: Streaming Analytics (PRIMARY - 80%)**
```
Data Sources → Database Service → Messaging Service (Pub/Sub)
                                        ↓
                                  Calculation Engine (Subscribe)
                                        ↓
                                  Messaging Service (Publish results)
                                        ↓
                                  API Gateway (WebSocket)
                                        ↓
                                  Frontend (Real-time updates)
```
**Use Cases:**
- Real-time dashboards
- Continuous monitoring
- Live KPI updates
- Configurable refresh periods (minute/hour/day)

### **Pattern 5: One-Time Queries (SECONDARY - 20%)**
```
Frontend → API Gateway → Calculation Engine → Database Service (HTTP)
                              ↓
                         HTTP Response
                              ↓
                          Frontend
```
**Use Cases:**
- Ad-hoc analysis
- Historical reports
- One-time calculations
- Custom queries

---

## 🎨 Service Interplay

### **The Three Business Services**

#### **1. Analytics Metadata Service** = "The Menu"
**Role**: Catalog of what can be measured

**Responsibilities:**
- ✅ Store KPI definitions (formula, description, required objects)
- ✅ Store object model schemas (tables, relationships, UML)
- ✅ Store module and value chain metadata
- ✅ Provide sample data for UI previews
- ✅ Serve as single source of truth for "what can be measured"

**Does NOT:**
- ❌ Calculate actual KPI values
- ❌ Store client configurations
- ❌ Connect to client data sources
- ❌ Perform any real-time calculations

**Endpoints:**
```
GET  /kpis                           # List all KPIs
GET  /kpis/{code}                    # Get single KPI
GET  /kpis/module/{code}             # Get KPIs by module
GET  /object-models                  # List all object models
GET  /object-models/{code}           # Get single object model
GET  /modules                        # List all modules
GET  /value-chains                   # List all value chains
```

#### **2. Calculation Engine Service** = "The Kitchen"
**Role**: Computes actual values from client data

**Responsibilities:**
- ✅ Execute KPI calculations using real client data
- ✅ Handle both streaming and on-demand calculations
- ✅ Query databases for raw data
- ✅ Apply formulas from metadata service
- ✅ Cache results for performance
- ✅ Publish results to messaging service
- ✅ Support configurable refresh periods

**Does NOT:**
- ❌ Define what KPIs exist (gets from metadata service)
- ❌ Store client preferences
- ❌ Manage data source connections

**Endpoints:**
```
POST /calculate                      # Calculate single KPI (on-demand)
POST /calculate/batch                # Calculate multiple KPIs
POST /calculate/dashboard            # Calculate dashboard KPIs
POST /batch/schedule                 # Schedule batch calculation job
GET  /batch/jobs                     # List scheduled batch jobs
```

**Data Access:**
- **Streaming Mode (80%)**: Subscribe to data streams from Database Service via Messaging
- **Query Mode (20%)**: HTTP REST calls to Database Service for one-time queries

#### **3. Demo Config Service** = "Your Order"
**Role**: Client-specific configurations

**Responsibilities:**
- ✅ Store which KPIs each client has selected
- ✅ Store custom KPI definitions (client-specific variations)
- ✅ Manage data source connections (client's database, APIs)
- ✅ Map client data fields to object models
- ✅ Generate service proposals (SOW)
- ✅ Generate demo data for visualization

**Does NOT:**
- ❌ Define standard KPIs (uses metadata service)
- ❌ Calculate KPI values (uses calculation engine)
- ❌ Store object model schemas

**Endpoints:**
```
GET    /clients                      # List all client configs
GET    /clients/{id}                 # Get client config
POST   /clients                      # Create client config
PUT    /clients/{id}                 # Update client config
POST   /analysis/required-objects    # Analyze required objects
POST   /proposals                    # Generate service proposal
POST   /proposals/questionnaire      # Get retention policy questionnaire
POST   /demo/generate                # Generate demo data
```

**Service Proposal Generation:**
The service proposal includes a comprehensive questionnaire and cost estimation covering:
1. Selected KPIs and required objects
2. **Licensing options** (value chain-based pricing with multi-year discounts)
3. **Statement of Work (SOW)** for integration work
4. **Data source integration methods** (batch vs streaming, conformed vs non-conformed)
5. **KPI implementation complexity** (OTB, Custom Basic, RBAC, Dynamic RBAC)
6. **Environment setup** (On-Prem, Azure, AWS, GCP, Oracle, or no setup)
7. **Data retention policies** (staged source data and analytics data)
8. **Infrastructure cost estimation** (compute, storage, networking)
9. **Managed services options** (annual retainer + hourly support)
10. **Resource scheduling** (developer, architect, access specialist, cloud architect)

---

## 💼 Service Proposal & Pricing Model

### **Overview**
The service proposal generator creates a comprehensive quote including licensing, integration SOW, infrastructure costs, and managed services based on client selections and requirements.

### **1. Licensing Model**

#### **Value Chain-Based Licensing**
**Base Pricing:**
- **$35,000/year** per value chain (1-year license)
- **$32,500/year** per value chain (3-year license) - 7% discount
- **$30,000/year** per value chain (5-year license) - 14% discount

**What's Included:**
- Unlimited KPIs within selected value chain(s)
- All modules under the value chain
- Platform access and updates
- Standard support during business hours

**Example Calculations:**
```typescript
// Client selects 2 value chains (SCOR, CRM) with 3-year license
const valueChains = ['SCOR', 'CRM'];
const licenseTerm = 3; // years
const annualCostPerChain = 32500; // 3-year rate

const annualLicenseCost = valueChains.length * annualCostPerChain;
// = 2 × $32,500 = $65,000/year

const totalLicenseCost = annualLicenseCost * licenseTerm;
// = $65,000 × 3 = $195,000 (total 3-year cost)
```

#### **Licensing Questionnaire**
```
"Which value chains do you need?"
☐ SCOR (Supply Chain Operations Reference)
☐ CRM (Customer Relationship Management)
☐ Sales Analytics
☐ Financial Analytics
☐ [Other value chains...]

"What license term would you prefer?"
○ 1 Year ($35,000/year per value chain)
○ 3 Years ($32,500/year per value chain) - Save 7%
○ 5 Years ($30,000/year per value chain) - Save 14%

Selected: [X] value chains × $[X]/year = $[X]/year
Total [X]-year cost: $[X]
```

---

### **2. Statement of Work (SOW) - Integration Costs**

#### **Data Source Integration Pricing**

##### **Batch Source Integration**
For each object model table requiring batch integration:

| Integration Type | Checkbox | Hours | Internal Cost | Client Charge |
|-----------------|----------|-------|---------------|---------------|
| **Batch Conformed/Cleansed** | ☐ | 15 | $70/hr | **$1,500** |
| **Batch Non-Conformed - Single Source** | ☐ | 20 | $70/hr | **$2,500** |
| **Batch Non-Conformed - Multi Source** | ☐ | 30 | $70/hr | **$3,500** |
| **Batch Non-Conformed - Entity Resolution** | ☐ | 30 | $70/hr | **$3,500** |

**Source System:** [Text field for client to specify]

**Definitions:**
- **Conformed/Cleansed**: Data already matches target schema, minimal transformation
- **Non-Conformed - Single Source**: Data needs transformation from one source system
- **Non-Conformed - Multi Source**: Data needs merging and transformation from multiple sources
- **Entity Resolution**: Requires deduplication and entity matching across sources

##### **Streaming Source Integration**
For each object model table requiring streaming integration:

| Integration Type | Checkbox | Hours | Internal Cost | Client Charge |
|-----------------|----------|-------|---------------|---------------|
| **API/Architected** | ☐ | 20 | $70/hr | **$2,500** |
| **API/Non-Architected** | ☐ | T&M | $175/hr | **TBD** |

**Source System:** [Text field for client to specify]

**Definitions:**
- **API/Architected**: Well-documented REST/GraphQL API with clear schema
- **API/Non-Architected**: Legacy API, requires reverse engineering, T&M pricing

---

#### **KPI Implementation Pricing**

For each KPI selected:

| KPI Type | Checkbox | Hours | Internal Cost | Client Charge |
|----------|----------|-------|---------------|---------------|
| **OTB (Out-of-the-Box)** | ☐ | 0.5 | $70/hr | **$50** |
| **Custom Basic** | ☐ | 0.5 | $70/hr | **$50** |
| **RBAC (Role-Based Access Control)** | ☐ | 1.0 | $70/hr | **$100** |
| **Dynamic RBAC** (e.g., Sales Hierarchy Commission) | ☐ | T&M | $175/hr | **TBD** |

**Definitions:**
- **OTB**: Standard KPI from catalog, no customization
- **Custom Basic**: Simple formula modification or custom calculation
- **RBAC**: KPI with role-based data filtering (e.g., manager sees only their team)
- **Dynamic RBAC**: Complex hierarchical access (e.g., commission calculations with inheritance)

---

#### **Environment Setup**

| Environment | Checkbox | Setup Cost | Notes |
|------------|----------|------------|-------|
| **On-Premises** | ☐ | T&M | Requires Cloud Architect |
| **Azure Cloud** | ☐ | T&M | Requires Cloud Architect |
| **AWS** | ☐ | T&M | Requires Cloud Architect |
| **GCP** | ☐ | T&M | Requires Cloud Architect |
| **Oracle Cloud** | ☐ | T&M | Requires Cloud Architect |
| **No Environment Setup** | ☐ | $0 | Client has existing environment |

**If environment setup required:**
- Cloud Architect assigned (T&M at $175/hr)
- Access Specialist assigned (fixed cost, included in setup)
- Estimated hours: 40-80 hours depending on complexity

---

### **3. Infrastructure Cost Estimation**

#### **Compute Costs**
```typescript
interface ComputeCosts {
  // API Gateway
  apiGateway: {
    instanceType: string;      // e.g., "t3.medium"
    instanceCount: number;      // Based on expected load
    monthlyCost: number;        // e.g., $50/instance/month
  };
  
  // Business Services (3 services)
  businessServices: {
    instanceType: string;       // e.g., "t3.large"
    instanceCount: number;      // 3 services × replicas
    monthlyCost: number;        // e.g., $100/instance/month
  };
  
  // Backend Services (3 services)
  backendServices: {
    instanceType: string;       // e.g., "t3.xlarge"
    instanceCount: number;      // 3 services × replicas
    monthlyCost: number;        // e.g., $150/instance/month
  };
  
  totalMonthlyCompute: number;
}
```

#### **Storage Costs**
```typescript
interface StorageCosts {
  // Active Database (TimescaleDB)
  activeDatabase: {
    storageGB: number;          // Based on data volume + retention
    costPerGB: number;          // e.g., $0.10/GB/month (hot storage)
    monthlyCost: number;
  };
  
  // Archived Data (Cold Storage)
  archivedData: {
    storageGB: number;          // Based on archival policy
    costPerGB: number;          // e.g., $0.01/GB/month (cold storage)
    monthlyCost: number;
  };
  
  // Redis (Messaging/Caching)
  redis: {
    instanceType: string;       // e.g., "cache.m5.large"
    monthlyCost: number;        // e.g., $100/month
  };
  
  totalMonthlyStorage: number;
}
```

#### **Network Costs**
```typescript
interface NetworkCosts {
  dataTransferGB: number;       // Estimated monthly data transfer
  costPerGB: number;            // e.g., $0.09/GB
  monthlyCost: number;
}
```

#### **Total Infrastructure Estimate**
```typescript
interface InfrastructureCosts {
  compute: ComputeCosts;
  storage: StorageCosts;
  network: NetworkCosts;
  
  monthlyTotal: number;
  annualTotal: number;
  
  // Cost breakdown by component
  breakdown: {
    apiGateway: number;
    businessServices: number;
    backendServices: number;
    database: number;
    archival: number;
    redis: number;
    network: number;
  };
}
```

**Estimation Inputs:**
- Expected daily data volume (GB)
- Number of concurrent users
- Refresh period (minute/hour/day)
- Number of KPIs
- Retention policies
- Expected query frequency

---

### **4. Managed Services**

#### **Annual Support Retainer**
**$5,000/year** - Includes:
- 66.67 hours of support at $75/hr
- Business hours support (9am-5pm client timezone)
- Email and phone support
- Bug fixes and patches
- Platform updates

#### **Additional Support Hours**
**$75/hr** - Beyond retainer hours:
- Extended support hours
- Custom feature requests
- Performance optimization
- Training sessions
- Consulting

#### **Managed Services Questionnaire**
```
"Would you like managed services support?"
○ Yes, include $5,000 annual retainer
○ No, we'll handle support internally

[If Yes] "Estimated additional hours needed per year?"
○ 0-50 hours (covered by retainer)
○ 50-100 hours (retainer + $3,750-7,500)
○ 100-200 hours (retainer + $7,500-15,000)
○ Custom estimate: ___ hours
```

---

### **5. Resource Scheduling & Roles**

#### **Integration Team Roles**

##### **Integration Developer/Analyst**
**Responsibilities:**
- All fixed-cost integration work
- Batch source integration (conformed, non-conformed)
- Streaming API/Architected integration
- OTB and Custom Basic KPI implementation
- RBAC KPI implementation

**Rate:** $70/hr (internal cost, fixed pricing to client)  
**Availability:** Assigned based on project schedule

##### **Integration Architect**
**Responsibilities:**
- All Time & Materials (T&M) work
- API/Non-Architected integration
- Dynamic RBAC KPI implementation
- Complex custom calculations
- Architecture design and review

**Rate:** $175/hr (T&M to client)  
**Availability:** Assigned as needed for T&M tasks

##### **Access Specialist**
**Responsibilities:**
- Set up integration to client's existing cloud environment
- Configure network access, VPNs, firewalls
- Set up service accounts and permissions
- Security configuration

**Assignment:** Beginning of engagement  
**Cost:** Included in environment setup (if applicable)

##### **Cloud Architect**
**Responsibilities:**
- Set up new cloud subscription (if client doesn't have one)
- Design cloud infrastructure
- Configure compute, storage, networking
- Implement security best practices
- Cost optimization

**Rate:** $175/hr (T&M to client)  
**Assignment:** Only if environment setup required

---

### **6. Service Proposal Questionnaire Flow**

#### **Step 1: KPI Selection (Already in Cart)**
- Client has selected KPIs from catalog
- System identifies required object models
- System identifies value chains

#### **Step 2: Licensing**
```
Value Chains Required: [Auto-detected from KPI selection]
- SCOR
- CRM

License Term:
○ 1 Year ($35,000/year per chain)
○ 3 Years ($32,500/year per chain)
○ 5 Years ($30,000/year per chain)
```

#### **Step 3: Data Source Integration**
For each required object model:
```
Object Model: Customer
Source System: [Text: "Salesforce CRM"]

Integration Method:
○ Batch - Conformed/Cleansed ($1,500)
○ Batch - Non-Conformed Single Source ($2,500)
○ Batch - Non-Conformed Multi Source ($3,500)
○ Batch - Entity Resolution ($3,500)
○ Streaming - API/Architected ($2,500)
○ Streaming - API/Non-Architected (T&M at $175/hr)
```

#### **Step 4: KPI Implementation Complexity**
For each selected KPI:
```
KPI: Perfect Order Fulfillment
Complexity:
○ OTB - Standard implementation ($50)
○ Custom Basic - Minor customization ($50)
○ RBAC - Role-based filtering ($100)
○ Dynamic RBAC - Complex hierarchy (T&M at $175/hr)
```

#### **Step 5: Environment Setup**
```
Where will the Analytics Engine run?
○ On-Premises (T&M - Cloud Architect required)
○ Azure Cloud (T&M - Cloud Architect required)
○ AWS (T&M - Cloud Architect required)
○ GCP (T&M - Cloud Architect required)
○ Oracle Cloud (T&M - Cloud Architect required)
○ No Setup - We have existing environment ($0)
```

#### **Step 6: Data Retention Policies**
[See Data Archival section above]

#### **Step 7: Infrastructure Estimation**
```
Expected Data Volume:
- Daily data ingestion: ___ GB/day
- Number of concurrent users: ___
- Refresh period: Minute / Hour / Day
- Number of KPIs: [Auto-filled from selection]

Estimated Monthly Infrastructure Cost: $___
Estimated Annual Infrastructure Cost: $___
```

#### **Step 8: Managed Services**
```
Support Options:
○ Yes - Include $5,000 annual retainer (66.67 hours at $75/hr)
○ No - We'll handle support internally

Estimated additional hours needed: ___ hours/year
Additional cost: $___ at $75/hr
```

---

### **7. Service Proposal Output**

#### **Proposal Document Structure**

```markdown
# Analytics Engine Service Proposal
**Client:** [Client Name]
**Date:** [Date]
**Valid Until:** [Date + 30 days]

---

## Executive Summary
This proposal outlines the licensing, implementation, infrastructure, and 
support costs for deploying the Analytics Engine platform.

---

## 1. Licensing
**Value Chains:** SCOR, CRM (2 chains)
**License Term:** 3 years
**Annual Cost:** $65,000/year ($32,500 per chain)
**Total 3-Year Cost:** $195,000

**Included:**
- Unlimited KPIs within selected value chains
- Platform access and updates
- Standard business hours support

---

## 2. Implementation - Statement of Work

### Data Source Integration
| Object Model | Source System | Integration Type | Cost |
|--------------|---------------|------------------|------|
| Customer | Salesforce CRM | Streaming - API/Architected | $2,500 |
| Order | SAP ERP | Batch - Non-Conformed Single | $2,500 |
| Product | Internal DB | Batch - Conformed | $1,500 |
| ... | ... | ... | ... |

**Subtotal Data Integration:** $XX,XXX

### KPI Implementation
| KPI Code | KPI Name | Complexity | Cost |
|----------|----------|------------|------|
| POF | Perfect Order Fulfillment | OTB | $50 |
| OTD | On-Time Delivery | RBAC | $100 |
| ... | ... | ... | ... |

**Subtotal KPI Implementation:** $X,XXX

### Environment Setup
**Platform:** AWS
**Setup Required:** Yes
**Cloud Architect:** 60 hours at $175/hr = $10,500
**Access Specialist:** Included

**Subtotal Environment:** $10,500

### Time & Materials (T&M) Items
| Item | Estimated Hours | Rate | Estimated Cost |
|------|----------------|------|----------------|
| API/Non-Architected Integration | 40-60 | $175/hr | $7,000-10,500 |
| Dynamic RBAC KPIs | 20-30 | $175/hr | $3,500-5,250 |

**T&M Range:** $10,500 - $15,750

**Total Implementation Cost:** $XX,XXX - $XX,XXX

---

## 3. Infrastructure Costs (Annual)

### Compute
- API Gateway: 2 × t3.medium = $100/month
- Business Services: 6 × t3.large = $600/month
- Backend Services: 6 × t3.xlarge = $900/month
**Subtotal:** $1,600/month = $19,200/year

### Storage
- Active Database: 500 GB × $0.10/GB = $50/month
- Archived Data: 2000 GB × $0.01/GB = $20/month
- Redis: cache.m5.large = $100/month
**Subtotal:** $170/month = $2,040/year

### Network
- Data Transfer: 1000 GB × $0.09/GB = $90/month
**Subtotal:** $90/month = $1,080/year

**Total Annual Infrastructure:** $22,320

---

## 4. Managed Services (Annual)
**Support Retainer:** $5,000/year (66.67 hours at $75/hr)
**Estimated Additional Hours:** 50 hours = $3,750
**Total Managed Services:** $8,750/year

---

## 5. Total Cost Summary

### Year 1
- Licensing: $65,000
- Implementation (One-time): $XX,XXX - $XX,XXX
- Infrastructure: $22,320
- Managed Services: $8,750
**Year 1 Total:** $XXX,XXX - $XXX,XXX

### Years 2-3 (Annual)
- Licensing: $65,000
- Infrastructure: $22,320
- Managed Services: $8,750
**Annual Cost:** $96,070

### 3-Year Total
**Total Investment:** $XXX,XXX - $XXX,XXX

---

## 6. Resource Schedule

### Integration Team
- **Integration Developer/Analyst:** [Name] - Weeks 1-8
- **Integration Architect:** [Name] - As needed for T&M
- **Access Specialist:** [Name] - Week 1
- **Cloud Architect:** [Name] - Weeks 1-2

### Timeline
- Environment Setup: Weeks 1-2
- Data Integration: Weeks 2-6
- KPI Implementation: Weeks 4-8
- Testing & UAT: Weeks 7-9
- Go-Live: Week 10

---

## 7. Terms & Conditions
[Standard T&Cs]

---

## 8. Next Steps
1. Review and approve proposal
2. Sign license agreement
3. Kick-off meeting
4. Begin implementation

**Proposal Valid Until:** [Date]
```

---

### **8. Proposal Calculation Logic**

```typescript
interface ServiceProposal {
  // Licensing
  licensing: {
    valueChains: string[];
    licenseTerm: 1 | 3 | 5;
    annualCostPerChain: number;
    annualTotal: number;
    termTotal: number;
  };
  
  // Implementation SOW
  implementation: {
    dataIntegration: {
      objectModel: string;
      sourceSystem: string;
      integrationType: string;
      cost: number;
    }[];
    kpiImplementation: {
      kpiCode: string;
      kpiName: string;
      complexity: string;
      cost: number;
    }[];
    environmentSetup: {
      platform: string;
      cloudArchitectHours: number;
      cost: number;
    };
    tmItems: {
      description: string;
      estimatedHours: string;
      rate: number;
      estimatedCost: string;
    }[];
    
    fixedCostTotal: number;
    tmCostRange: { min: number; max: number };
    implementationTotal: { min: number; max: number };
  };
  
  // Infrastructure
  infrastructure: {
    compute: { monthly: number; annual: number };
    storage: { monthly: number; annual: number };
    network: { monthly: number; annual: number };
    total: { monthly: number; annual: number };
  };
  
  // Managed Services
  managedServices: {
    retainer: number;
    estimatedAdditionalHours: number;
    additionalCost: number;
    annualTotal: number;
  };
  
  // Totals
  totals: {
    year1: { min: number; max: number };
    yearlyRecurring: number;
    termTotal: { min: number; max: number };
  };
  
  // Resource Schedule
  resources: {
    role: string;
    name: string;
    weeks: string;
    rate: number;
  }[];
  
  // Timeline
  timeline: {
    phase: string;
    weeks: string;
    resources: string[];
  }[];
}

function calculateProposal(
  selectedKPIs: KPI[],
  questionnaire: QuestionnaireAnswers
): ServiceProposal {
  // Implementation logic
  // ...
}
```

---

## 🔄 Real-Time Dashboard Architecture

### **User Scenario**
```
User opens dashboard at 8:00 AM
  ↓
Selects KPIs to monitor
  ↓
Sets refresh period (minute/hour/day)
  ↓
Dashboard stays open all day
  ↓
KPIs update automatically based on period
  ↓
User switches between visualizations
  ↓
Each visualization subscribes to its own data stream
  ↓
User leaves at 5:00 PM (9 hours of continuous updates)
```

### **Hybrid Architecture: Initial Load + Continuous Updates**

#### **Step 1: Initial Page Load (HTTP REST)**
```
User opens dashboard
  ↓ HTTP GET /kpi/{code}
API Gateway → Calculation Engine → Database Service
  ↓ HTTP Response (1-2 seconds)
Frontend displays current value immediately
```

**Why HTTP:**
- Fast initial feedback
- User doesn't wait
- Simple request-response
- Current value from cache or quick query

#### **Step 2: Subscribe to Updates (WebSocket + Pub/Sub)**
```
Frontend establishes WebSocket connection
  ↓ ws://gateway/ws/kpi/{code}?period=minute
API Gateway subscribes to messaging channel
  ↓ Subscribe to "kpi.updates.{code}.{period}"
Database Service starts publishing (if not already)
  ↓ Publishes updates every minute/hour/day
API Gateway receives updates
  ↓ WebSocket push to Frontend
Frontend updates UI automatically
```

**Why WebSocket + Pub/Sub:**
- Continuous updates without polling
- Configurable refresh period
- Efficient (only publish when subscribers exist)
- Scalable (multiple users, multiple KPIs)
- No page refresh needed

### **TimescaleDB Continuous Aggregates**

**Purpose**: Pre-compute period-based aggregates for efficient streaming

```sql
-- Minute-level aggregates (auto-refreshed every minute)
CREATE MATERIALIZED VIEW kpi_values_minute
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('1 minute', timestamp) AS bucket,
    kpi_code,
    AVG(value) as avg_value,
    MIN(value) as min_value,
    MAX(value) as max_value,
    COUNT(*) as data_points
FROM kpi_raw_data
GROUP BY bucket, kpi_code;

-- Hourly aggregates
CREATE MATERIALIZED VIEW kpi_values_hour
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('1 hour', timestamp) AS bucket,
    kpi_code,
    AVG(value) as avg_value,
    MIN(value) as min_value,
    MAX(value) as max_value,
    COUNT(*) as data_points
FROM kpi_raw_data
GROUP BY bucket, kpi_code;

-- Daily aggregates
CREATE MATERIALIZED VIEW kpi_values_day
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('1 day', timestamp) AS bucket,
    kpi_code,
    AVG(value) as avg_value,
    MIN(value) as min_value,
    MAX(value) as max_value,
    COUNT(*) as data_points
FROM kpi_raw_data
GROUP BY bucket, kpi_code;

-- Auto-refresh policy (refreshes every minute)
SELECT add_continuous_aggregate_policy('kpi_values_minute',
    start_offset => INTERVAL '1 hour',
    end_offset => INTERVAL '1 minute',
    schedule_interval => INTERVAL '1 minute');
```

### **Smart Publishing (Resource Efficiency)**

**Database Service tracks subscribers:**
```python
# Only publish if there are active subscribers
if subscriber_count[kpi_code][period] > 0:
    publish_update()
else:
    # No subscribers, don't publish
    pass
```

**Benefits:**
- No wasted resources
- Stops publishing when user closes dashboard
- Starts publishing when first user subscribes
- Scales efficiently with user count

---

## 🎯 Use Case Distribution

### **80% - Streaming Analytics (PRIMARY)**

**Characteristics:**
- Continuous data flow
- Real-time updates
- Configurable refresh periods (minute/hour/day)
- Multiple concurrent users
- Dashboard stays open for hours
- User switches between visualizations
- WebSocket connections
- Pub/Sub messaging

**Examples:**
- Real-time supply chain dashboard
- Live sales metrics
- Continuous monitoring
- Operations center displays

### **20% - One-Time Queries (SECONDARY)**

**Characteristics:**
- Request-response
- Fast (1-2 seconds)
- Ad-hoc analysis
- Historical data
- Custom date ranges
- Export to reports
- HTTP REST calls

**Examples:**
- "What was Perfect Order Fulfillment in Q3 2024?"
- "Compare this month vs last month"
- "Generate annual report"
- "Export to Excel"

---

## 🔧 Calculation Engine Modes

### **Mode 1: Streaming Calculation (80%)**

**Trigger**: Data arrives on subscribed channel  
**Pattern**: Event-driven, continuous

```python
# Calculation Engine subscribes to data streams
await messaging_client.subscribe(
    channel="data.stream.scor",
    handler=process_stream_data
)

# When data arrives, calculate and publish
async def process_stream_data(data):
    result = calculate_kpi(data)
    await publish_result(result)
```

**Data Source**: Pub/Sub stream from Database Service  
**Output**: Pub/Sub to result channels  
**Frequency**: Continuous (as data arrives)

### **Mode 2: On-Demand Calculation (20%)**

**Trigger**: HTTP request from user  
**Pattern**: Request-response, synchronous

```python
# User requests calculation
@app.post("/calculate")
async def calculate_kpi(params: CalculationParams):
    # Query data via HTTP
    data = await database_client.query(...)
    
    # Calculate
    result = calculate(data)
    
    # Return immediately
    return result
```

**Data Source**: HTTP query to Database Service  
**Output**: HTTP response  
**Frequency**: One-time (user-triggered)

### **Mode 3: Scheduled Batch (Future)**

**Trigger**: Scheduled job (cron, scheduler)  
**Pattern**: Asynchronous, batch processing

```python
# Scheduler publishes batch command
await messaging_client.publish_command(
    command_type="calculate_batch",
    payload={
        "job_id": "daily_metrics",
        "kpi_codes": [...],
        "schedule": "daily"
    }
)

# Calculation Engine processes batch
# Publishes results when complete
```

**Data Source**: HTTP query (large dataset)  
**Output**: Pub/Sub (batch results)  
**Frequency**: Scheduled (daily, weekly, etc.)

---

## 📱 Frontend Requirements

### **Demo/Config UI Features**

#### **1. KPI Catalog Browser**
- Browse KPIs by value chain, module, industry
- View KPI details (formula, description, required objects)
- Preview sample visualizations
- Add KPIs to cart
- UML diagram viewer for object model relationships

#### **2. Real-Time Dashboard**
- Display multiple KPIs simultaneously
- Configurable refresh period (minute/hour/day)
- Live updates via WebSocket
- Visual indicators (live/disconnected)
- Historical trend charts
- Drill-down capabilities

#### **3. Configuration Management**
- Create client configurations
- Select KPIs for client
- Configure data sources
- Map client fields to object models
- Generate service proposals

#### **4. Visualization Options**
- Line charts (time series)
- Bar charts (comparisons)
- Pie charts (breakdowns)
- Gauge charts (current value)
- Sparklines (trends)
- Tables (detailed data)

### **User Experience Requirements**

**Initial Load:**
- ✅ Display current value within 1-2 seconds
- ✅ Show loading indicator
- ✅ Graceful error handling

**Streaming Updates:**
- ✅ Smooth transitions (no flashing)
- ✅ Visual indicator of update (subtle animation)
- ✅ Show timestamp of last update
- ✅ Display connection status (connected/disconnected)
- ✅ Auto-reconnect on disconnect

**Period Selection:**
- ✅ Dropdown or buttons (Minute/Hour/Day)
- ✅ Instant switch (disconnect old, connect new)
- ✅ Remember user preference
- ✅ Show next update time

**Multiple Visualizations:**
- ✅ Each KPI has independent WebSocket
- ✅ Switch visualizations without page refresh
- ✅ Lazy load (only connect when visible)
- ✅ Cleanup on unmount

---

## 🗄️ Data Architecture & Archival

### **Database Service ↔ Archival Service Integration**

**Purpose**: Manage data lifecycle and retention policies for both source data and analytics data

**Architecture:**
```
┌─────────────────────────────────────────────────────────────┐
│ Database Service (TimescaleDB)                              │
│ ├─ Active data (hot storage)                                │
│ ├─ Monitors data age                                        │
│ └─ Triggers archival based on retention policy              │
└─────────────────────────────────────────────────────────────┘
                           ↓ HTTP REST
┌─────────────────────────────────────────────────────────────┐
│ Archival Service                                            │
│ ├─ Receives archival requests                               │
│ ├─ Compresses and stores to cold storage                    │
│ ├─ Maintains archive index                                  │
│ └─ Provides retrieval on demand                             │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Cold Storage (S3, Azure Blob, etc.)                        │
│ ├─ Compressed archived data                                 │
│ ├─ Cost-effective long-term storage                         │
│ └─ Retrievable for historical analysis                      │
└─────────────────────────────────────────────────────────────┘
```

### **Data Types Subject to Archival**

#### **1. Staged Source Data**
**Definition**: Raw data ingested from client systems before processing

**Examples:**
- Raw order data from ERP
- Raw customer data from CRM
- Raw transaction data from POS
- Raw sensor data from IoT devices

**Retention Considerations:**
- Compliance requirements (GDPR, SOX, etc.)
- Audit trail needs
- Data reprocessing capability
- Storage costs

#### **2. Analytics Data**
**Definition**: Calculated KPI values and aggregated metrics

**Examples:**
- Historical KPI values
- Time-series aggregates
- Dashboard snapshots
- Calculation results

**Retention Considerations:**
- Historical trend analysis needs
- Regulatory reporting requirements
- Year-over-year comparisons
- Storage costs vs query frequency

### **Client Retention Policy Configuration**

**Required in Service Proposal Questionnaire:**

```typescript
interface DataRetentionPolicy {
  // Staged Source Data Retention
  stagedSourceData: {
    retentionPeriod: number;        // Days to keep in active database
    retentionUnit: 'days' | 'months' | 'years';
    archivalEnabled: boolean;       // Archive or delete?
    archivalPeriod: number;         // Days in cold storage (if archived)
    archivalUnit: 'months' | 'years' | 'indefinite';
  };
  
  // Analytics Data Retention
  analyticsData: {
    retentionPeriod: number;        // Days to keep in active database
    retentionUnit: 'days' | 'months' | 'years';
    archivalEnabled: boolean;       // Archive or delete?
    archivalPeriod: number;         // Days in cold storage (if archived)
    archivalUnit: 'months' | 'years' | 'indefinite';
  };
  
  // Granularity Settings
  granularity: {
    rawData: boolean;               // Keep raw data points?
    minuteAggregates: boolean;      // Keep minute-level aggregates?
    hourlyAggregates: boolean;      // Keep hourly aggregates?
    dailyAggregates: boolean;       // Keep daily aggregates?
    monthlyAggregates: boolean;     // Keep monthly aggregates?
  };
}
```

### **Service Proposal Questionnaire - Data Retention Section**

**Questions to Ask Client:**

#### **Question 1: Staged Source Data Retention**
```
"How long do you need to retain raw source data in the active database?"

Options:
○ 30 days (Recommended for real-time analytics only)
○ 90 days (Standard for most use cases)
○ 180 days (6 months)
○ 365 days (1 year)
○ Custom: ___ days

"Do you want to archive source data after this period?"
○ Yes, archive to cold storage
○ No, delete permanently

[If Yes] "How long should archived data be retained?"
○ 1 year
○ 3 years
○ 5 years (Common for compliance)
○ 7 years (Financial/SOX compliance)
○ 10 years
○ Indefinitely
```

#### **Question 2: Analytics Data Retention**
```
"How long do you need to retain calculated analytics data in the active database?"

Options:
○ 90 days (3 months of historical trends)
○ 180 days (6 months)
○ 365 days (1 year - Recommended)
○ 730 days (2 years)
○ Custom: ___ days

"Do you want to archive analytics data after this period?"
○ Yes, archive to cold storage
○ No, delete permanently

[If Yes] "How long should archived analytics be retained?"
○ 3 years
○ 5 years (Recommended)
○ 7 years
○ 10 years
○ Indefinitely
```

#### **Question 3: Data Granularity**
```
"Which levels of data granularity do you need to retain?"

☑ Raw data points (highest detail, largest storage)
☑ Minute-level aggregates
☑ Hourly aggregates (Recommended minimum)
☑ Daily aggregates (Recommended)
☑ Monthly aggregates (Recommended)

Note: Lower granularity = less storage cost, but less detail for analysis
```

#### **Question 4: Compliance Requirements**
```
"Do you have specific compliance or regulatory requirements?"

☐ GDPR (EU data protection)
☐ SOX (Financial reporting - 7 years)
☐ HIPAA (Healthcare - 6 years)
☐ ISO 27001 (Information security)
☐ Industry-specific: ___________

[If selected] Retention periods will be automatically adjusted to meet compliance requirements.
```

### **Archival Service Capabilities**

#### **Automatic Archival**
```python
# Database Service monitors data age
if data_age > retention_policy.active_retention:
    # Trigger archival
    await archival_service.archive_data(
        schema=schema_name,
        table=table_name,
        date_range={
            'start': retention_cutoff_date,
            'end': now
        },
        compression='gzip',
        metadata={
            'client_id': client_id,
            'data_type': 'staged_source' | 'analytics',
            'retention_policy': policy
        }
    )
    
    # Delete from active database after successful archive
    await database_service.delete_archived_data(...)
```

#### **On-Demand Retrieval**
```python
# User requests historical data beyond active retention
@app.get("/analytics/historical/{kpi_code}")
async def get_historical_data(
    kpi_code: str,
    start_date: date,
    end_date: date
):
    # Check if data is in active database
    active_data = await database_service.query(...)
    
    # If date range extends beyond active retention, retrieve from archive
    if start_date < active_retention_cutoff:
        archived_data = await archival_service.retrieve_data(
            kpi_code=kpi_code,
            date_range={'start': start_date, 'end': active_retention_cutoff}
        )
        
        # Merge active + archived data
        return merge_data(active_data, archived_data)
    
    return active_data
```

#### **Cost Estimation in Service Proposal**

**Storage Cost Calculation:**
```python
def calculate_storage_costs(
    data_volume_gb_per_day: float,
    retention_policy: DataRetentionPolicy
) -> StorageCostEstimate:
    # Active database storage (hot)
    active_days = retention_policy.stagedSourceData.retentionPeriod
    active_storage_gb = data_volume_gb_per_day * active_days
    active_cost = active_storage_gb * HOT_STORAGE_COST_PER_GB  # e.g., $0.10/GB/month
    
    # Archived storage (cold)
    if retention_policy.stagedSourceData.archivalEnabled:
        archive_days = retention_policy.stagedSourceData.archivalPeriod
        archive_storage_gb = data_volume_gb_per_day * archive_days
        archive_cost = archive_storage_gb * COLD_STORAGE_COST_PER_GB  # e.g., $0.01/GB/month
    else:
        archive_cost = 0
    
    return StorageCostEstimate(
        active_storage_gb=active_storage_gb,
        active_monthly_cost=active_cost,
        archive_storage_gb=archive_storage_gb,
        archive_monthly_cost=archive_cost,
        total_monthly_cost=active_cost + archive_cost
    )
```

### **TimescaleDB Retention Policies**

**Automatic Data Retention:**
```sql
-- Drop chunks older than retention period
SELECT add_retention_policy('scor_data.orders', INTERVAL '90 days');

-- Before dropping, trigger archival
CREATE OR REPLACE FUNCTION archive_before_drop()
RETURNS TRIGGER AS $$
BEGIN
    -- Call archival service via pg_notify
    PERFORM pg_notify(
        'archival_trigger',
        json_build_object(
            'schema', TG_TABLE_SCHEMA,
            'table', TG_TABLE_NAME,
            'chunk_id', OLD.chunk_id,
            'time_range', OLD.time_range
        )::text
    );
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;
```

### **Separate Schemas per Domain**
```
scor_data       - Supply chain data
crm_data        - Customer relationship data
sales_data      - Sales data
financial_data  - Financial data
```

**Benefits:**
- Performance isolation
- Independent scaling
- Clear ownership
- Easier maintenance

### **TimescaleDB Hypertables**
```sql
-- Orders hypertable (partitioned by time)
CREATE TABLE scor_data.orders (
    order_id BIGSERIAL,
    timestamp TIMESTAMPTZ NOT NULL,
    customer_id BIGINT,
    order_value DECIMAL,
    status VARCHAR(50),
    ...
);

SELECT create_hypertable('scor_data.orders', 'timestamp');
```

### **Continuous Aggregates for Streaming**
- Pre-computed period buckets (minute/hour/day)
- Auto-refreshed by TimescaleDB
- Efficient queries for streaming updates
- Reduced calculation load

---

## 🔐 Security & Performance

### **Authentication & Authorization**
- JWT tokens validated at API Gateway
- Service-to-service authentication
- Client-specific data isolation
- Role-based access control (RBAC)

### **Rate Limiting**
- Applied at API Gateway
- Per-client limits
- Protects backend services
- Prevents abuse

### **Caching Strategy**
- **Metadata**: Long cache (hours) - rarely changes
- **Calculation Results**: Short cache (minutes) - frequently changes
- **Streaming Updates**: No cache - real-time
- **One-Time Queries**: Medium cache (configurable)

### **Circuit Breaker**
- Protects against cascading failures
- Automatic failover
- Health checks
- Graceful degradation

### **Performance Targets**
- Initial page load: < 2 seconds
- Streaming update latency: < 1 second
- One-time query: < 3 seconds
- WebSocket connection: < 500ms
- Support 1000+ concurrent users
- Support 100+ KPIs per dashboard

---

## 📊 Monitoring & Observability

### **Metrics to Track**
- Request count per endpoint
- Response time per service
- Error rate per service
- WebSocket connection count
- Active subscriber count per KPI
- Cache hit rate
- Circuit breaker state
- Database query performance

### **Distributed Tracing**
- OpenTelemetry integration
- Trace requests across services
- Correlation IDs
- Performance bottleneck identification

### **Health Checks**
- Service health endpoints
- Aggregate health at API Gateway
- Database connection status
- Messaging service status
- Redis connection pool

---

## 🚀 Implementation Phases

### **Phase 1: Core Infrastructure (COMPLETE)**
- ✅ Analytics Metadata Service
- ✅ Calculation Engine Service (stub methods)
- ✅ Demo Config Service
- ✅ Service classification
- ✅ Architecture documentation

### **Phase 2: Streaming Infrastructure (IN PROGRESS)**
- ⚠️ Database Service stream publisher
- ⚠️ Calculation Engine stream processor
- ⚠️ API Gateway WebSocket support
- ⚠️ Frontend streaming hooks
- ⚠️ TimescaleDB continuous aggregates

### **Phase 3: One-Time Query Support**
- ⚠️ HTTP query endpoints
- ⚠️ Synchronous calculation path
- ⚠️ Database Service HTTP client
- ⚠️ Calculation Engine query mode

### **Phase 4: Demo/Config UI**
- ⚠️ API Gateway integration
- ⚠️ KPI catalog browser
- ⚠️ Real-time dashboard
- ⚠️ Configuration management
- ⚠️ UML diagram viewer (COMPLETE)

### **Phase 5: Optimization**
- ⬜ Caching layer
- ⬜ Performance tuning
- ⬜ Load testing
- ⬜ Security hardening

---

## 📝 Key Design Decisions

### **Decision 1: Microservices Architecture**
**Rationale**: Real-time calculation requires independent scaling and performance isolation

### **Decision 2: Streaming-First (80/20 Split)**
**Rationale**: Primary use case is real-time dashboards with continuous monitoring

### **Decision 3: Hybrid Data Access**
**Rationale**: 
- Streaming (Pub/Sub) for continuous updates
- HTTP REST for one-time queries
- Best of both worlds

### **Decision 4: TimescaleDB Continuous Aggregates**
**Rationale**: Pre-computed period buckets enable efficient streaming without heavy calculation load

### **Decision 5: WebSocket for Frontend**
**Rationale**: Persistent connection for real-time updates, better than polling

### **Decision 6: Smart Publishing**
**Rationale**: Only publish when subscribers exist, saves resources

### **Decision 7: Calculation Engine as Business Service**
**Rationale**: Provides core business value, client-facing via API Gateway

---

## 🔄 Living Document Updates

**This document will be updated as:**
- New requirements are discussed
- Architectural decisions are made
- Implementation details are finalized
- User feedback is incorporated
- Performance requirements change
- New features are added

**Update Process:**
1. Discuss requirement in conversation
2. Update relevant section in this document
3. Add to CHANGELOG.md
4. Notify team of changes

---

## 📚 Related Documents

- `SERVICE_INTERPLAY_ARCHITECTURE.md` - How the three business services work together
- `STREAMING_FIRST_ARCHITECTURE.md` - Streaming analytics architecture
- `REAL_TIME_DASHBOARD_ARCHITECTURE.md` - Dashboard implementation details
- `DATA_ACCESS_PATTERN_ANALYSIS.md` - Comparison of data access patterns
- `API_GATEWAY_BUSINESS_SERVICES_INTEGRATION_PLAN.md` - API Gateway integration
- `CHANGELOG.md` - All changes and updates

---

**Last Updated**: November 11, 2025  
**Version**: 1.0  
**Status**: Active Development
