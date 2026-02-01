import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

// Styles
import './styles/globals.css';

// Theme
import { ThemeProvider } from './components/theme/ThemeProvider';

// Layout
import { AppLayout } from './components/layout/AppLayout';

// New Portal Pages
import StrategyCenterPage from './pages/StrategyCenterPage';
import InsightsFeedPage from './pages/InsightsFeedPage';
import StrategyDocumentsPage from './pages/StrategyDocumentsPage';
import { ProcessScenarioModelerPage, PredictiveWhatIfPage } from './pages/analytics';

// Demo Section Pages
import {
  ValueChainExplorerPage,
  TrainingVideoPage,
  DemoInterviewPage,
  DataSimulatorPage,
  SampleAnalyticsPage,
  ExecutiveSummaryPage,
} from './pages/demo';

// Admin Section Pages
import {
  AgentProfilesPage,
  AgentProfileDetailPage,
  NewAgentPage,
  ContractRulesPage,
  AdminSettingsPage,
  AgentWorkflowsPage,
} from './pages/admin';

// Legacy Pages (to be migrated)
import ConfigPage from './pages/ConfigPage';
import KPIDetailPage from './pages/KPIDetailPage';
import ObjectModelViewer from './pages/ObjectModelViewer';
import ObjectModelsBrowser from './pages/ObjectModelsBrowser';
import RequiredObjectsView from './pages/RequiredObjectsView';
import DataSourceConfig from './pages/DataSourceConfig';
import ServiceProposal from './pages/ServiceProposal';
import AdminPage from './pages/AdminPage';
import GovernancePage from './pages/GovernancePage';
import ExcelImportPage from './pages/ExcelImportPage';
import OntologyManagerPage from './pages/OntologyManagerPage';
import SimulationPage from './pages/SimulationPage';
import MLDashboardPage from './pages/MLDashboardPage';
import SystemMonitorPage from './pages/SystemMonitorPage';
import ServiceTrafficPage from './pages/ServiceTrafficPage';
import ConversationServicePage from './pages/ConversationServicePage';
import AnalyticsDemoPage from './pages/AnalyticsDemoPage';
import MappingPage from './pages/MappingPage';
import SQLPage from './pages/SQLPage';

// Contexts
import { CartProvider } from './contexts/CartContext';
import { TreeActionsProvider } from './contexts/TreeActionsContext';
import TreeActionsDialogs from './components/TreeActionsDialogs';

// Create React Query client
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      retry: 1,
      staleTime: 5 * 60 * 1000, // 5 minutes
    },
  },
});

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider defaultTheme="dark">
        <CartProvider>
          <TreeActionsProvider>
            <BrowserRouter>
              <AppLayout>
                <Routes>
                  {/* Demo Section */}
                  <Route path="/demo" element={<Navigate to="/demo/value-chains" replace />} />
                  <Route path="/demo/value-chains" element={<ValueChainExplorerPage />} />
                  <Route path="/demo/training" element={<TrainingVideoPage />} />
                  <Route path="/demo/interview" element={<DemoInterviewPage />} />
                  <Route path="/demo/simulator" element={<DataSimulatorPage />} />
                  <Route path="/demo/analytics" element={<SampleAnalyticsPage />} />
                  <Route path="/demo/summary" element={<ExecutiveSummaryPage />} />
                  
                  {/* Strategy Center (Home) */}
                  <Route path="/" element={<StrategyCenterPage />} />
                  
                  {/* Design Studio */}
                  <Route path="/design" element={<Navigate to="/design/interview" replace />} />
                  <Route path="/design/interview" element={<ConversationServicePage />} />
                  <Route path="/design/business-model" element={<OntologyManagerPage />} />
                  <Route path="/design/kpis" element={<ConfigPage />} />
                  <Route path="/design/objects" element={<ObjectModelsBrowser />} />
                  <Route path="/design/gaps" element={<RequiredObjectsView />} />
                  <Route path="/design/import" element={<ExcelImportPage />} />
                  
                  {/* Analytics Hub */}
                  <Route path="/analytics" element={<Navigate to="/analytics/dashboards" replace />} />
                  <Route path="/analytics/simulation" element={<SimulationPage />} />
                  <Route path="/analytics/dashboards" element={<AnalyticsDemoPage />} />
                  <Route path="/analytics/process-modeler" element={<ProcessScenarioModelerPage />} />
                  <Route path="/analytics/what-if" element={<PredictiveWhatIfPage />} />
                  <Route path="/analytics/ml" element={<MLDashboardPage />} />
                  
                  {/* Insights Feed */}
                  <Route path="/insights" element={<InsightsFeedPage />} />
                  
                  {/* Strategy Documents */}
                  <Route path="/documents" element={<StrategyDocumentsPage />} />
                  
                  {/* Deployment Center */}
                  <Route path="/deployment" element={<Navigate to="/deployment/sources" replace />} />
                  <Route path="/deployment/sources" element={<DataSourceConfig />} />
                  <Route path="/deployment/mapping" element={<MappingPage />} />
                  <Route path="/deployment/governance" element={<GovernancePage />} />
                  <Route path="/deployment/admin" element={<AdminPage />} />
                  <Route path="/deployment/monitor" element={<SystemMonitorPage />} />
                  <Route path="/deployment/traffic" element={<ServiceTrafficPage />} />
                  <Route path="/deployment/sql" element={<SQLPage />} />
                  
                  {/* Proposal Center */}
                  <Route path="/proposal" element={<Navigate to="/proposal/estimate" replace />} />
                  <Route path="/proposal/estimate" element={<ServiceProposal />} />
                  <Route path="/proposal/contract" element={<ServiceProposal />} />
                  <Route path="/proposal/project" element={<ServiceProposal />} />
                  
                  {/* Admin Section */}
                  <Route path="/admin" element={<Navigate to="/admin/agents" replace />} />
                  <Route path="/admin/agents" element={<AgentProfilesPage />} />
                  <Route path="/admin/agents/new" element={<NewAgentPage />} />
                  <Route path="/admin/agents/:agentId" element={<AgentProfileDetailPage />} />
                  <Route path="/admin/workflows" element={<AgentWorkflowsPage />} />
                  <Route path="/admin/contracts" element={<ContractRulesPage />} />
                  <Route path="/admin/settings" element={<AdminSettingsPage />} />
                  
                  {/* Legacy Routes (redirects) */}
                  <Route path="/demo" element={<Navigate to="/" replace />} />
                  <Route path="/config" element={<Navigate to="/design/kpis" replace />} />
                  <Route path="/kpi/:kpiCode" element={<KPIDetailPage />} />
                  <Route path="/object-models" element={<Navigate to="/design/objects" replace />} />
                  <Route path="/object-model/:modelCode" element={<ObjectModelViewer />} />
                  <Route path="/required-objects-view" element={<Navigate to="/design/gaps" replace />} />
                  <Route path="/data-sources" element={<Navigate to="/deployment/sources" replace />} />
                  <Route path="/governance" element={<Navigate to="/deployment/governance" replace />} />
                  <Route path="/excel-import" element={<Navigate to="/design/import" replace />} />
                  <Route path="/ontology-studio" element={<Navigate to="/design/business-model" replace />} />
                  <Route path="/simulation" element={<Navigate to="/analytics/simulation" replace />} />
                  <Route path="/ml-registry" element={<Navigate to="/analytics/ml" replace />} />
                  <Route path="/system-monitor" element={<Navigate to="/deployment/monitor" replace />} />
                  <Route path="/conversation-service" element={<Navigate to="/design/interview" replace />} />
                  <Route path="/analytics-demo" element={<Navigate to="/analytics/dashboards" replace />} />
                  <Route path="/mapping" element={<Navigate to="/deployment/mapping" replace />} />
                  <Route path="/sql" element={<Navigate to="/deployment/sql" replace />} />
                  <Route path="/admin" element={<Navigate to="/deployment/admin" replace />} />
                </Routes>
              </AppLayout>
            </BrowserRouter>
            <TreeActionsDialogs />
          </TreeActionsProvider>
        </CartProvider>
      </ThemeProvider>
    </QueryClientProvider>
  );
}

export default App;
