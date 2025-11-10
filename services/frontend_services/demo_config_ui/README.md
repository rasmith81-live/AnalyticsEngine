# Demo/Config UI

**Analytics Engine - Demo and Configuration Application**

## Overview

The Demo/Config UI is a React-based web application for:
1. **Demonstrating** analytics capabilities to prospects
2. **Configuring** client-specific KPI selections
3. **Creating** custom derived KPIs
4. **Analyzing** required object models
5. **Generating** service proposals (SOW)

## Features

### 1. Demo Page
- Sample analytics dashboards with D3.js visualizations
- Interactive KPI displays
- Real-time calculation demonstrations

### 2. Config Page
- Tree view of all metrics (Industry → Value Chain → Module → KPI)
- Checkbox selection for client KPIs
- Drill-down into object models and KPIs
- UML diagram viewer

### 3. KPI Detail Page
- Complete KPI definition display
- Formula and calculation logic
- Benchmarks
- Required objects
- Custom KPI derivation

### 4. Object Model Viewer
- UML class diagrams (D3.js)
- Object relationships
- Table schemas
- Associated KPIs

### 5. Required Objects Viewer
- Analysis of selected KPIs
- Complete object model dependencies
- Consolidated UML diagram

### 6. Data Source Config
- Connection setup (batch/real-time)
- Connector configuration
- Connection testing

### 7. Service Proposal
- Automated SOW generation
- Timeline and cost estimation
- Integration plan

## Technology Stack

- **Framework**: React 18 + TypeScript
- **Build Tool**: Vite
- **UI Library**: Material-UI (MUI)
- **Visualization**: D3.js, Recharts
- **State Management**: Zustand
- **API Client**: Axios + React Query
- **Routing**: React Router v6

## Project Structure

```
demo_config_ui/
├── src/
│   ├── components/          # Reusable components
│   │   ├── Layout.tsx
│   │   ├── MetricTree.tsx
│   │   ├── UMLDiagram.tsx
│   │   ├── KPICard.tsx
│   │   └── ...
│   ├── pages/               # Page components
│   │   ├── DemoPage.tsx
│   │   ├── ConfigPage.tsx
│   │   ├── KPIDetailPage.tsx
│   │   ├── ObjectModelViewer.tsx
│   │   ├── RequiredObjectsViewer.tsx
│   │   ├── DataSourceConfig.tsx
│   │   └── ServiceProposal.tsx
│   ├── services/            # API services
│   │   └── api.ts
│   ├── types/               # TypeScript types
│   │   └── index.ts
│   ├── utils/               # Utility functions
│   ├── App.tsx              # Main app component
│   └── main.tsx             # Entry point
├── public/                  # Static assets
├── package.json
├── tsconfig.json
├── vite.config.ts
└── README.md
```

## Setup Instructions

### Prerequisites
- Node.js 18+ and npm
- Analytics Metadata Service running on port 8020
- Demo/Config Service running on port 8022

### Installation

```powershell
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\services\frontend_services\demo_config_ui

# Install dependencies
npm install

# Create .env file
Copy-Item .env.example .env

# Edit .env with your configuration
notepad .env
```

### Environment Variables

Create `.env` file:

```env
# API URLs
VITE_API_URL=http://localhost:8020
VITE_CONFIG_API_URL=http://localhost:8022

# Feature flags
VITE_ENABLE_DEMO=true
VITE_ENABLE_CUSTOM_KPIS=true
```

### Development

```powershell
# Start development server
npm run dev

# Open browser to http://localhost:3000
```

### Build for Production

```powershell
# Build production bundle
npm run build

# Preview production build
npm run preview
```

### Linting and Formatting

```powershell
# Run ESLint
npm run lint

# Format code with Prettier
npm run format
```

## API Integration

### Metadata Service (Port 8020)
- `/kpis` - List all KPIs
- `/kpis/{code}` - Get KPI details
- `/object-models` - List object models
- `/modules` - List modules
- `/value-chains` - List value chains

### Demo/Config Service (Port 8022)
- `/api/configs` - Client configurations
- `/api/configs/{id}/custom-kpis` - Custom KPIs
- `/api/analysis/required-objects` - Object analysis
- `/api/proposals` - Service proposals

## Key Components

### MetricTree Component
```typescript
// Hierarchical tree view of metrics
<MetricTree
  onKPISelect={(kpi) => handleKPISelect(kpi)}
  onObjectModelSelect={(model) => handleModelSelect(model)}
  selectedKPIs={selectedKPIs}
/>
```

### UMLDiagram Component
```typescript
// D3.js UML class diagram
<UMLDiagram
  objectModels={objectModels}
  relationships={relationships}
  onNodeClick={(node) => handleNodeClick(node)}
/>
```

### KPICard Component
```typescript
// KPI display card
<KPICard
  kpi={kpi}
  selected={isSelected}
  onSelect={() => handleSelect(kpi)}
  onViewDetails={() => navigate(`/kpi/${kpi.code}`)}
/>
```

## Features Implementation Status

- [x] Project structure
- [x] TypeScript types
- [x] API service layer
- [x] App routing
- [ ] Layout component
- [ ] Demo page
- [ ] Config page with metric tree
- [ ] KPI detail page
- [ ] UML diagram viewer
- [ ] Custom KPI creator
- [ ] Required objects analyzer
- [ ] Data source configuration
- [ ] Service proposal generator

## Development Workflow

1. **Start backend services**:
   ```powershell
   docker-compose up -d analytics_metadata_service
   docker-compose up -d demo_config_service
   ```

2. **Start frontend**:
   ```powershell
   cd services/frontend_services/demo_config_ui
   npm run dev
   ```

3. **Access application**:
   - Frontend: http://localhost:3000
   - API Docs (Metadata): http://localhost:8020/docs
   - API Docs (Config): http://localhost:8022/docs

## Testing

```powershell
# Run unit tests
npm test

# Run with coverage
npm run test:coverage

# Run E2E tests
npm run test:e2e
```

## Deployment

### Docker Build

```dockerfile
# Dockerfile
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### Build and Run

```powershell
# Build Docker image
docker build -t demo-config-ui .

# Run container
docker run -p 3000:80 demo-config-ui
```

## Next Steps

1. Implement Layout component
2. Build Demo page with sample dashboards
3. Create MetricTree component
4. Implement UML diagram viewer with D3.js
5. Build KPI detail page
6. Create custom KPI creator
7. Implement required objects analyzer
8. Build data source configuration
9. Create service proposal generator

## Support

For issues or questions, contact the development team.

## License

Proprietary - All rights reserved
