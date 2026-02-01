# Demo Flow Build Plan - From Mockups to Production

## Executive Summary

This document outlines the build plan to transform the 6-step demo flow from static mockups into a fully functional, agent-driven experience. Each page currently displays mock data but needs to be connected to real backend services and agent workflows.

---

## 1. Value Chain Explorer - Industry Population Plan

### Current State
- Page loads from `useValueChainTree()` hook which calls `metadataApi.getValueChains()`
- Returns empty when no value chains exist in the database
- UI is fully functional but has no data to display

### Build Steps

#### Phase 1: Define Industry Templates (Week 1)
1. **Create Industry Value Chain Definitions**
   - Define 10+ industry templates with complete value chain hierarchies:
     - **Retail/E-Commerce**: Sourcing → Inventory → Sales → Fulfillment → Customer Service
     - **Manufacturing**: R&D → Procurement → Production → Distribution → After-Sales
     - **Healthcare**: Patient Acquisition → Care Delivery → Billing → Outcomes Management
     - **Financial Services**: Client Onboarding → Portfolio Management → Risk → Compliance
     - **Technology/SaaS**: Product Development → Marketing → Sales → Customer Success
     - **Logistics/Supply Chain**: Planning → Procurement → Warehousing → Transportation → Delivery
     - **Professional Services**: Business Development → Engagement → Delivery → Billing
     - **Hospitality**: Reservations → Guest Services → Operations → Revenue Management
     - **Energy/Utilities**: Generation → Transmission → Distribution → Customer Service
     - **Telecommunications**: Network Planning → Service Delivery → Customer Care → Billing

2. **Map KPIs to Each Module**
   - Link existing SCOR/APQC/industry-standard KPIs to each value chain module
   - Ensure 20-50 KPIs per value chain with proper categorization

#### Phase 2: Database Population (Week 2)
1. **Create Migration Script**
   ```
   scripts/populate_industry_value_chains.py
   ```
   - Load industry definitions from JSON/YAML templates
   - Create value_chain, module, and kpi entities
   - Establish proper relationships via the relationship table

2. **Seed Data Files**
   ```
   data/templates/industries/
   ├── retail.yaml
   ├── manufacturing.yaml
   ├── healthcare.yaml
   ├── financial_services.yaml
   ├── technology_saas.yaml
   ├── logistics.yaml
   ├── professional_services.yaml
   ├── hospitality.yaml
   ├── energy_utilities.yaml
   └── telecommunications.yaml
   ```

#### Phase 3: UI Enhancement (Week 3)
1. **Add Industry Selector**
   - Allow users to select their industry on page entry
   - Filter value chains to show industry-specific content
   - Add "All Industries" option for browsing

2. **Add "Add to My Model" Functionality**
   - Enable users to select KPIs for their business model
   - Store selections in session/context for use in Interview step

### Dependencies
- `business_metadata` service running
- `database_service` with proper schema
- Relationship data properly seeded

### Success Criteria
- User can browse 10+ industry value chains
- Each value chain has 3-5 modules
- Each module has 10-30 associated KPIs
- Selections persist to Interview step

---

## 2. Training Video Page - AI Video Generation Plan

### Current State
- Static mockup with placeholder video thumbnail
- No actual video content or recording capability

### Build Steps

#### Phase 1: Video Content Strategy (Week 1)
1. **Define Video Scripts**
   - Create 6 training video scripts (one per demo step):
     1. "Understanding Value Chains" (2-3 min)
     2. "Training Overview" (1-2 min)
     3. "AI Interview Process" (3-4 min)
     4. "Data Simulation Explained" (2-3 min)
     5. "Reading Your Analytics" (3-4 min)
     6. "Implementation & Next Steps" (2-3 min)

2. **Script Template Structure**
   ```
   - Introduction (15 sec)
   - Key Concepts (1-2 min)
   - Walkthrough Demo (1-2 min)
   - Summary & Next Steps (15 sec)
   ```

#### Phase 2: AI Video Generation Options (Week 2-3)

**Option A: AI Avatar + Text-to-Speech (Recommended)**
1. **Technology Stack**
   - **Synthesia** or **HeyGen** for AI avatar generation
   - **ElevenLabs** for realistic voice synthesis
   - **D-ID** as alternative for talking head videos

2. **Implementation**
   - Create API integration service:
     ```
     services/support_services/video_generation_service/
     ├── app/
     │   ├── main.py
     │   ├── api/endpoints.py
     │   └── services/
     │       ├── synthesia_client.py
     │       ├── elevenlabs_client.py
     │       └── video_composer.py
     ```
   - Store generated videos in Azure Blob Storage (Azurite locally)
   - Cache video URLs for playback

**Option B: Screen Recording + AI Voiceover**
1. **Technology Stack**
   - **Puppeteer/Playwright** for automated screen recording
   - **ElevenLabs** for AI narration
   - **FFmpeg** for video composition

2. **Implementation**
   - Record actual UI interactions programmatically
   - Overlay AI-generated narration
   - Produce MP4 output

**Option C: Dynamic Slide-Based Videos**
1. **Technology Stack**
   - **Remotion** (React-based video generation)
   - **ElevenLabs** for narration
   - Generate videos on-demand from React components

2. **Implementation**
   - Create Remotion compositions for each training topic
   - Generate videos at build time or on-demand
   - Personalize with user's industry/company name

#### Phase 3: UI Integration (Week 3-4)
1. **Video Player Component**
   - Implement HTML5 video player with controls
   - Add chapter markers/navigation
   - Track viewing progress

2. **Dynamic Content**
   - Allow videos to reference user's selected industry
   - Show relevant examples based on user context

### Recommended Approach
**Start with Option C (Remotion)** for cost-effectiveness and flexibility:
- No external API costs during development
- Full control over content
- Can be generated dynamically
- Upgrade to Option A for production polish

### Dependencies
- Video storage solution (Azure Blob/S3)
- API keys for chosen AI services
- FFmpeg for video processing

### Success Criteria
- 6 training videos available and playable
- Videos load within 3 seconds
- Progress tracking works
- Can skip between chapters

---

## 3. AI Interview Page - Voice Recording Restoration

### Current State
- `DemoInterviewPage.tsx` is a **simplified mockup** with no voice capability
- `ConversationServicePage.tsx` has **full voice support** but is in Design Studio section
- Voice recording code exists but the Demo Interview page doesn't use it

### Build Steps

#### Phase 1: Immediate Fix - Add Voice Button (Day 1)
1. **Copy Voice Components from ConversationServicePage**
   - Import speech recognition hooks and state
   - Add microphone button to input area
   - Wire up speech-to-text processing

2. **Code Changes to `DemoInterviewPage.tsx`**
   ```tsx
   // Add imports
   import { Mic, Square, AudioWaveform } from 'lucide-react';
   
   // Add state
   const [isListening, setIsListening] = useState(false);
   const [currentTranscript, setCurrentTranscript] = useState('');
   const [speechSupported, setSpeechSupported] = useState(true);
   const recognitionRef = useRef<any>(null);
   
   // Add speech recognition logic (copy from ConversationServicePage)
   // Add microphone button next to Send button
   ```

#### Phase 2: Connect to Agent Coordinator (Week 1)
1. **Wire Up WebSocket Connection**
   - Connect to `conversation_service` WebSocket endpoint
   - Send user messages to agent coordinator
   - Receive and display agent responses

2. **Implement Real Agent Responses**
   - Replace `setTimeout` mock with actual WebSocket messages
   - Parse agent activities and artifacts
   - Update phase progress based on agent outputs

#### Phase 3: Test Agent Response Time (Week 1-2)
1. **Performance Benchmarks**
   - Measure time from user input to first agent response
   - Target: < 2 seconds for initial acknowledgment
   - Target: < 10 seconds for substantive response

2. **Optimization if Needed**
   - Add streaming responses for long outputs
   - Implement typing indicators during processing
   - Cache common response patterns

### Dependencies
- `conversation_service` running
- `multi_agent_service` running
- WebSocket connectivity

### Success Criteria
- Voice button visible and functional
- Browser speech recognition works
- Agent responds within 10 seconds
- Conversation flows naturally through phases

---

## 4. Data Simulator - Real Entity Connection

### Current State
- 4 hardcoded mock entities: Customers, Orders, Products, Suppliers
- No connection to entities identified in Interview

### Build Steps

#### Phase 1: Entity Discovery from Interview (Week 1)
1. **Create Entity Storage in Session Context**
   - Store entities identified during Interview in session state
   - Pass entity list to Simulator page via React context or URL params

2. **API Endpoint for Session Entities**
   ```
   GET /api/sessions/{session_id}/entities
   Response: { entities: [{ code, name, type, properties }] }
   ```

#### Phase 2: Dynamic Entity Display (Week 1)
1. **Fetch Entities on Page Load**
   ```tsx
   const { data: sessionEntities } = useQuery({
     queryKey: ['session-entities', sessionId],
     queryFn: () => api.getSessionEntities(sessionId)
   });
   ```

2. **Replace Mock Data**
   - Remove `mockEntities` constant
   - Map session entities to simulator entity cards
   - Default to sample entities if no session exists

#### Phase 3: Connect to Real Simulator Service (Week 2)
1. **Wire Up `data_simulator_service`**
   - Start/stop simulation via API
   - Configure generation rates per entity
   - Stream simulated data to analytics page

2. **Real-Time Updates**
   - Show actual record counts from simulator
   - Display real uptime and throughput metrics

### Dependencies
- `data_simulator_service` running
- Session management in `conversation_service`
- Entity extraction working in Interview

### Success Criteria
- Entities shown match those from Interview
- Simulator can start/stop real data generation
- Metrics reflect actual simulation activity

---

## 5. Sample Analytics Page - Agent-Driven Generation

### Current State
- Static mockup with hardcoded metrics, charts, and KPI table
- No connection to design outputs or real data

### Build Steps

#### Phase 1: Design Output Extraction (Week 1)
1. **Capture Analytics Design from Interview**
   - Store selected KPIs in session context
   - Store dashboard preferences (chart types, layouts)
   - Store metric thresholds and targets

2. **Design Artifact Structure**
   ```typescript
   interface AnalyticsDesign {
     dashboardName: string;
     selectedKpis: KPISelection[];
     chartPreferences: ChartConfig[];
     layout: DashboardLayout;
     refreshInterval: number;
   }
   ```

#### Phase 2: Dynamic Dashboard Rendering (Week 2)
1. **Dashboard Configuration Engine**
   - Parse design artifacts to render components
   - Support multiple chart types (bar, line, pie, gauge)
   - Auto-layout based on number of metrics

2. **Component Mapping**
   ```tsx
   const renderChart = (config: ChartConfig) => {
     switch (config.type) {
       case 'bar': return <BarChart data={config.data} />;
       case 'line': return <LineChart data={config.data} />;
       case 'pie': return <PieChart data={config.data} />;
       case 'metric': return <MetricCard data={config.data} />;
     }
   };
   ```

#### Phase 3: Real-Time Data Connection (Week 2-3)
1. **Connect to Simulated Data Stream**
   - Subscribe to `data_simulator_service` WebSocket
   - Map simulated entity data to KPI calculations
   - Update charts in real-time

2. **KPI Calculation Engine Integration**
   - Use `calculation_engine_service` for complex KPIs
   - Cache and batch calculations for performance

#### Phase 4: Agent-Driven Code Generation (Week 3-4)
1. **Proof of Concept: Developer Agent Generates Dashboard**
   - Feed design artifacts to Developer Agent
   - Agent produces React component code
   - Hot-reload generated component into page

2. **Code Generation Workflow**
   ```
   Interview Design → Design Artifacts → Developer Agent → 
   React Component → Dynamic Import → Rendered Dashboard
   ```

### Dependencies
- `calculation_engine_service` for KPI formulas
- `data_simulator_service` for live data
- Developer Agent code generation capability

### Success Criteria
- Dashboard reflects Interview selections
- Charts update with simulated data
- Layout matches user preferences
- Agent can generate basic dashboard code

---

## 6. Executive Summary - ProjectManager Integration

### Current State
- Static mock timeline with hardcoded phases
- Fixed contract pricing, no dynamic calculation

### Build Steps

#### Phase 1: Project Manager Agent Integration (Week 1)
1. **Create Implementation Plan Tool**
   - Add `generate_implementation_plan` tool to ProjectManagerAgent
   - Input: selected KPIs, data sources, complexity score
   - Output: phased timeline with tasks and durations

2. **Dynamic Timeline Generation**
   ```typescript
   interface ImplementationPlan {
     phases: Phase[];
     totalDuration: string;
     estimatedStartDate: Date;
     risks: Risk[];
     dependencies: Dependency[];
   }
   ```

#### Phase 2: Connect UI to Agent Output (Week 1-2)
1. **Fetch Plan from Session**
   ```tsx
   const { data: plan } = useQuery({
     queryKey: ['implementation-plan', sessionId],
     queryFn: () => api.getImplementationPlan(sessionId)
   });
   ```

2. **Render Dynamic Timeline**
   - Map agent-generated phases to timeline UI
   - Show task details and durations
   - Highlight critical path

#### Phase 3: Dynamic Pricing Calculation (Week 2)
1. **Pricing Engine**
   - Calculate license cost based on KPI count
   - Calculate implementation cost based on complexity
   - Calculate managed services based on scope

2. **Contract Summary from Design**
   - Count selected KPIs from Interview
   - Count dashboards from analytics design
   - Count data sources from integration design
   - Calculate user count from organization profile

#### Phase 4: PDF Generation (Week 3)
1. **Server-Side PDF Generation**
   - Use `react-pdf` or `puppeteer` for PDF creation
   - Include all summary data and timeline
   - Generate downloadable contract document

### Dependencies
- ProjectManagerAgent with planning tools
- Pricing configuration
- PDF generation library

### Success Criteria
- Timeline reflects actual project complexity
- Pricing is calculated dynamically
- PDF download works
- All summary cards show real data

---

## Implementation Priority & Timeline

### Week 1-2: Foundation
| Priority | Item | Effort |
|----------|------|--------|
| P0 | 3. Voice Button Restoration | 2 days |
| P0 | 1. Industry Templates (3 industries) | 3 days |
| P1 | 4. Session Entity Connection | 2 days |
| P1 | 6. ProjectManager Plan Tool | 2 days |

### Week 3-4: Integration
| Priority | Item | Effort |
|----------|------|--------|
| P1 | 5. Dynamic Dashboard Rendering | 4 days |
| P1 | 1. Complete Industry Population | 3 days |
| P2 | 6. Dynamic Pricing | 2 days |
| P2 | 4. Real Simulator Connection | 2 days |

### Week 5-6: Polish
| Priority | Item | Effort |
|----------|------|--------|
| P2 | 2. Training Video (Remotion) | 5 days |
| P2 | 5. Agent Code Generation | 3 days |
| P3 | 6. PDF Generation | 2 days |

---

## Technical Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Demo Flow UI                             │
├─────────┬─────────┬─────────┬─────────┬─────────┬─────────────┤
│ Value   │Training │Interview│Simulator│Analytics│  Summary    │
│ Chain   │ Video   │  (AI)   │ Config  │Dashboard│             │
└────┬────┴────┬────┴────┬────┴────┬────┴────┬────┴──────┬──────┘
     │         │         │         │         │           │
     ▼         ▼         ▼         ▼         ▼           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Session Context Store                        │
│  - Selected Industry    - Design Artifacts                      │
│  - Selected KPIs        - Entity Definitions                    │
│  - Chat History         - Implementation Plan                   │
└─────────────────────────────────────────────────────────────────┘
     │         │         │         │         │           │
     ▼         ▼         ▼         ▼         ▼           ▼
┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────────┐
│business │ video   │conversa-│ data    │calculat-│ multi_agent │
│metadata │ service │tion_svc │simulator│ion_eng  │  service    │
└─────────┴─────────┴─────────┴─────────┴─────────┴─────────────┘
```

---

## Next Steps

1. **Review this plan** with stakeholder
2. **Prioritize** based on demo timeline needs
3. **Begin with P0 items** (Voice button, 3 industry templates)
4. **Set up tracking** for implementation progress

---

*Document generated: 2026-02-01*
*Status: Ready for Review*
