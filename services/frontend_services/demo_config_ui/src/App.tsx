import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider, createTheme, CssBaseline } from '@mui/material';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

// Pages - import without @ alias to test
import DemoPage from './pages/DemoPage';
import ConfigPage from './pages/ConfigPage';
import KPIDetailPage from './pages/KPIDetailPage';
import ObjectModelViewer from './pages/ObjectModelViewer';
import RequiredObjectsViewer from './pages/RequiredObjectsViewer';
import DataSourceConfig from './pages/DataSourceConfig';
import ServiceProposal from './pages/ServiceProposal';
import Layout from './components/Layout';
import { CartProvider } from './contexts/CartContext';

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
          <BrowserRouter>
            <Layout>
              <Routes>
                <Route path="/" element={<Navigate to="/demo" replace />} />
                <Route path="/demo" element={<DemoPage />} />
                <Route path="/config" element={<ConfigPage />} />
                <Route path="/kpi/:kpiCode" element={<KPIDetailPage />} />
                <Route path="/object-model/:modelCode" element={<ObjectModelViewer />} />
                <Route path="/required-objects" element={<RequiredObjectsViewer />} />
                <Route path="/data-sources" element={<DataSourceConfig />} />
                <Route path="/proposal" element={<ServiceProposal />} />
              </Routes>
            </Layout>
          </BrowserRouter>
        </CartProvider>
      </ThemeProvider>
    </QueryClientProvider>
  );
}

export default App;
