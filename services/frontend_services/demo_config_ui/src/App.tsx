import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider, createTheme, CssBaseline } from '@mui/material';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

// Pages - import without @ alias to test
import DemoPage from './pages/DemoPage';
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
import Layout from './components/Layout';
import { CartProvider } from './contexts/CartContext';
import { TreeActionsProvider } from './contexts/TreeActionsContext';
import TreeActionsDialogs from './components/TreeActionsDialogs';

// Create theme
const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

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
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <CartProvider>
          <TreeActionsProvider>
            <BrowserRouter>
              <Layout>
                <Routes>
                  <Route path="/" element={<Navigate to="/demo" replace />} />
                  <Route path="/demo" element={<DemoPage />} />
                  <Route path="/config" element={<ConfigPage />} />
                  <Route path="/kpi/:kpiCode" element={<KPIDetailPage />} />
                  <Route path="/object-models" element={<ObjectModelsBrowser />} />
                  <Route path="/object-model/:modelCode" element={<ObjectModelViewer />} />
                  <Route path="/required-objects-view" element={<RequiredObjectsView />} />
                  <Route path="/data-sources" element={<DataSourceConfig />} />
                  <Route path="/proposal" element={<ServiceProposal />} />
                  <Route path="/admin" element={<AdminPage />} />
                  <Route path="/governance" element={<GovernancePage />} />
                  <Route path="/excel-import" element={<ExcelImportPage />} />
                  <Route path="/ontology-studio" element={<OntologyManagerPage />} />
                  <Route path="/simulation" element={<SimulationPage />} />
                  <Route path="/ml-registry" element={<MLDashboardPage />} />
                  <Route path="/system-monitor" element={<SystemMonitorPage />} />
                </Routes>
              </Layout>
            </BrowserRouter>
            <TreeActionsDialogs />
          </TreeActionsProvider>
        </CartProvider>
      </ThemeProvider>
    </QueryClientProvider>
  );
}

export default App;
