# Metric Tree Design - Dual Navigation

**Date**: November 10, 2025  
**Component**: MetricTree  
**Purpose**: Flexible KPI browsing with dual navigation paths

---

## Navigation Paths

### **Path 1: Industry-Based Navigation**
```
📊 Industry
  └─ 🔗 Value Chain
      └─ 📦 Module
          └─ 📈 KPI
```

**Use Case**: Users who want industry-specific context
- Browse by industry (Healthcare, Manufacturing, Retail, etc.)
- See value chains relevant to that industry
- Drill down to modules and KPIs

**Example**:
```
📊 Healthcare
  └─ 🔗 Patient Care
      └─ 📦 Emergency Services
          └─ 📈 Emergency Room Wait Time
          └─ 📈 Patient Satisfaction Score
```

---

### **Path 2: Direct Value Chain Navigation**
```
🔗 Value Chain
  └─ 📦 Module
      └─ 📈 KPI
```

**Use Case**: Users who already know their value chain
- Skip industry selection
- Go directly to value chain
- Faster navigation for experienced users

**Example**:
```
🔗 Supply Chain
  └─ 📦 Procurement
      └─ 📈 Supplier Lead Time
      └─ 📈 Purchase Order Cycle Time
  └─ 📦 Inventory Management
      └─ 📈 Inventory Turnover
      └─ 📈 Stock Accuracy
```

---

## UI Design

### **Tab-Based Navigation**

```
┌─────────────────────────────────────────────────┐
│  [By Industry]  [By Value Chain]                │
├─────────────────────────────────────────────────┤
│                                                  │
│  Tab 1: By Industry                              │
│  📊 Healthcare                                   │
│    └─ 🔗 Patient Care                           │
│        └─ 📦 Emergency Services                 │
│            └─ 📈 ER Wait Time                   │
│  📊 Manufacturing                                │
│    └─ 🔗 Production                             │
│        └─ 📦 Assembly                           │
│            └─ 📈 Cycle Time                     │
│                                                  │
│  Tab 2: By Value Chain                           │
│  🔗 Supply Chain                                │
│    └─ 📦 Procurement                            │
│        └─ 📈 Supplier Lead Time                 │
│  🔗 Sales Management                             │
│    └─ 📦 Lead Generation                        │
│        └─ 📈 Lead Conversion Rate               │
│                                                  │
└─────────────────────────────────────────────────┘
```

---

## Component Structure

### **MetricTree Component**

```typescript
interface MetricTreeProps {
  mode: 'industry' | 'value-chain';
  onKPISelect: (kpi: KPI) => void;
  selectedKPIs: string[];
}

// Two modes:
// 1. Industry mode: Industry → Value Chain → Module → KPI
// 2. Value Chain mode: Value Chain → Module → KPI
```

### **Tree Structure**

```typescript
// Industry Mode
interface IndustryTree {
  industries: Industry[];
}

interface Industry {
  code: string;
  name: string;
  valueChains: ValueChain[];
}

// Value Chain Mode (Direct)
interface ValueChainTree {
  valueChains: ValueChain[];
}

// Shared structures
interface ValueChain {
  code: string;
  name: string;
  modules: Module[];
}

interface Module {
  code: string;
  name: string;
  kpis: KPI[];
}

interface KPI {
  code: string;
  name: string;
  description: string;
  formula: string;
}
```

---

## API Endpoints

### **For Industry Mode**

```typescript
// Get all industries with nested structure
GET /api/industries?include=value_chains,modules,kpis

// Response:
{
  "industries": [
    {
      "code": "HEALTHCARE",
      "name": "Healthcare",
      "value_chains": [
        {
          "code": "PATIENT_CARE",
          "name": "Patient Care",
          "modules": [...]
        }
      ]
    }
  ]
}
```

### **For Value Chain Mode**

```typescript
// Get all value chains with nested structure
GET /api/value-chains?include=modules,kpis

// Response:
{
  "value_chains": [
    {
      "code": "SUPPLY_CHAIN",
      "name": "Supply Chain",
      "modules": [
        {
          "code": "PROCUREMENT",
          "name": "Procurement",
          "kpis": [...]
        }
      ]
    }
  ]
}
```

---

## Implementation Plan

### **Phase 1: Basic Structure**

1. **Create MetricTreeTabs component**
   ```typescript
   // src/components/MetricTreeTabs.tsx
   // Container with Material-UI Tabs
   // Switches between Industry and Value Chain modes
   ```

2. **Create MetricTree component**
   ```typescript
   // src/components/MetricTree.tsx
   // Accepts mode prop
   // Renders appropriate tree structure
   ```

3. **Create tree nodes**
   ```typescript
   // src/components/IndustryNode.tsx
   // src/components/ValueChainNode.tsx
   // src/components/ModuleNode.tsx
   // src/components/KPINode.tsx
   ```

### **Phase 2: Data Fetching**

1. **Create hooks**
   ```typescript
   // src/hooks/useIndustryTree.ts
   // Fetch industry-based hierarchy
   
   // src/hooks/useValueChainTree.ts
   // Fetch value chain-based hierarchy
   ```

2. **Add caching**
   ```typescript
   // Use React Query for caching
   // Cache separately for each mode
   ```

### **Phase 3: Features**

1. **Search across both modes**
2. **Filter by industry/value chain**
3. **Expand/collapse all**
4. **Remember user's last mode**
5. **Highlight selected KPIs**

---

## User Experience

### **Scenario 1: New User (Industry Mode)**

1. User opens Config page
2. Sees "By Industry" tab (default)
3. Browses industries: Healthcare, Manufacturing, etc.
4. Selects Healthcare
5. Sees Patient Care, Clinical Operations value chains
6. Drills down to modules and KPIs

### **Scenario 2: Experienced User (Value Chain Mode)**

1. User opens Config page
2. Clicks "By Value Chain" tab
3. Immediately sees Supply Chain, Sales Management, etc.
4. Selects Supply Chain
5. Sees Procurement, Inventory, Logistics modules
6. Selects KPIs directly

### **Scenario 3: Search**

1. User types "lead time" in search
2. Results show in both tabs:
   - Industry tab: Manufacturing → Supply Chain → Procurement → Supplier Lead Time
   - Value Chain tab: Supply Chain → Procurement → Supplier Lead Time
3. User can navigate via either path

---

## Benefits of Dual Navigation

### **Industry Mode Benefits**
- ✅ Industry context and benchmarking
- ✅ Discover value chains relevant to industry
- ✅ Better for new users
- ✅ Industry-specific recommendations

### **Value Chain Mode Benefits**
- ✅ Faster navigation for experienced users
- ✅ Cross-industry value chains visible
- ✅ Focus on business processes
- ✅ Cleaner hierarchy (one less level)

### **Combined Benefits**
- ✅ Flexibility for different user types
- ✅ Multiple ways to find same KPI
- ✅ Better user experience
- ✅ Supports different mental models

---

## Data Model Relationships

```
Industry (1) ──────> (N) Value Chain
                           │
                           │ (1)
                           ↓
                         (N) Module
                           │
                           │ (1)
                           ↓
                         (N) KPI

// Key insight: Value Chains can belong to multiple Industries
// This allows both navigation paths to work
```

### **Example: Supply Chain Value Chain**

**Appears in multiple industries**:
- Manufacturing → Supply Chain
- Retail → Supply Chain
- Healthcare → Supply Chain

**Direct access**:
- Supply Chain → Procurement → Supplier Lead Time

---

## Component File Structure

```
src/
├── components/
│   ├── MetricTreeTabs.tsx          # Tab container
│   ├── MetricTree.tsx               # Main tree component
│   ├── IndustryNode.tsx             # Industry level node
│   ├── ValueChainNode.tsx           # Value chain level node
│   ├── ModuleNode.tsx               # Module level node
│   ├── KPINode.tsx                  # KPI level node (leaf)
│   ├── TreeSearch.tsx               # Search component
│   └── TreeControls.tsx             # Expand/collapse controls
├── hooks/
│   ├── useIndustryTree.ts           # Industry mode data
│   ├── useValueChainTree.ts         # Value chain mode data
│   └── useTreeSearch.ts             # Search functionality
└── types/
    └── metricTree.ts                # TypeScript interfaces
```

---

## API Requirements

### **Metadata Service Needs to Provide**

1. **Industry endpoint**
   ```
   GET /api/industries
   GET /api/industries/{code}
   GET /api/industries/{code}/value-chains
   ```

2. **Value Chain endpoint**
   ```
   GET /api/value-chains
   GET /api/value-chains/{code}
   GET /api/value-chains/{code}/modules
   ```

3. **Module endpoint**
   ```
   GET /api/modules
   GET /api/modules/{code}
   GET /api/modules/{code}/kpis
   ```

4. **Nested queries**
   ```
   GET /api/industries?include=value_chains,modules,kpis
   GET /api/value-chains?include=modules,kpis
   ```

---

## Implementation Priority

### **Phase 1: Value Chain Mode First** (Simpler)
- ✅ Fewer levels in hierarchy
- ✅ Faster to implement
- ✅ Proves the concept
- ✅ Most users will use this

### **Phase 2: Industry Mode** (Add context)
- ✅ Adds industry dimension
- ✅ Better for discovery
- ✅ Industry benchmarking
- ✅ Marketing value

### **Phase 3: Polish**
- ✅ Search across both modes
- ✅ Filters and sorting
- ✅ Remember user preference
- ✅ Performance optimization

---

## Success Criteria

### **Must Have**
- ✅ Both navigation modes work
- ✅ Can select KPIs from either mode
- ✅ Search works across both modes
- ✅ Performance is acceptable (< 1s load)

### **Should Have**
- ✅ Smooth transitions between modes
- ✅ Remember expanded nodes
- ✅ Keyboard navigation
- ✅ Responsive design

### **Nice to Have**
- ✅ Drag and drop KPIs
- ✅ Bulk selection
- ✅ Export tree structure
- ✅ Custom grouping

---

## Example Implementation

### **MetricTreeTabs Component**

```typescript
import { useState } from 'react';
import { Tabs, Tab, Box } from '@mui/material';
import MetricTree from './MetricTree';

export default function MetricTreeTabs() {
  const [mode, setMode] = useState<'industry' | 'value-chain'>('value-chain');

  return (
    <Box>
      <Tabs value={mode} onChange={(e, v) => setMode(v)}>
        <Tab label="By Industry" value="industry" />
        <Tab label="By Value Chain" value="value-chain" />
      </Tabs>
      
      <Box sx={{ mt: 2 }}>
        <MetricTree mode={mode} />
      </Box>
    </Box>
  );
}
```

---

## Summary

### **Dual Navigation Design**

**Path 1**: Industry → Value Chain → Module → KPI  
**Path 2**: Value Chain → Module → KPI

**Implementation**: Tab-based UI with shared components

**Benefits**:
- Flexibility for different user types
- Faster navigation for experienced users
- Industry context for new users
- Better overall UX

**Next Step**: Implement Value Chain mode first, then add Industry mode

---

Ready to start building with this dual navigation approach! 🚀
