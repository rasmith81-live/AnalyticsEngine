import { Typography, Paper, Box, Grid, Card, CardContent, Chip, Button, CircularProgress } from '@mui/material';
import { useState, useEffect } from 'react';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import ErrorIcon from '@mui/icons-material/Error';
import TrendingUpIcon from '@mui/icons-material/TrendingUp';
import TrendingDownIcon from '@mui/icons-material/TrendingDown';
import PeopleIcon from '@mui/icons-material/People';
import SpeedIcon from '@mui/icons-material/Speed';
import DataUsageIcon from '@mui/icons-material/DataUsage';
import { useWebSocket } from '../hooks/useWebSocket';

interface ServiceStatus {
  name: string;
  url: string;
  status: 'healthy' | 'error' | 'checking';
  details?: any;
}

interface RealTimeMetrics {
  activeUsers: number;
  transactionsPerSecond: number;
  avgLatencyMs: number;
  cpuUsage: number;
}

export default function DemoPage() {
  const [services, setServices] = useState<ServiceStatus[]>([
    { name: 'Metadata Service', url: 'http://localhost:8020/health', status: 'checking' },
    { name: 'Calculation Engine', url: 'http://localhost:8021/health', status: 'checking' },
    { name: 'Demo/Config Service', url: 'http://localhost:8022/health', status: 'checking' },
  ]);

  const [metrics, setMetrics] = useState<RealTimeMetrics>({
    activeUsers: 142,
    transactionsPerSecond: 45,
    avgLatencyMs: 120,
    cpuUsage: 35
  });

  const { isConnected, lastMessage } = useWebSocket({
    url: 'ws://localhost:8020/ws',
    onOpen: () => console.log('Dashboard connected to websocket'),
  });

  // Handle incoming websocket messages
  useEffect(() => {
    if (lastMessage && lastMessage.type === 'dashboard_update') {
      setMetrics(prev => ({
        ...prev,
        ...lastMessage.payload
      }));
    }
  }, [lastMessage]);

  // Simulate real-time updates if connected (demo mode)
  useEffect(() => {
    if (!isConnected) return;

    const interval = setInterval(() => {
      setMetrics(prev => ({
        activeUsers: Math.max(0, prev.activeUsers + Math.floor(Math.random() * 10) - 5),
        transactionsPerSecond: Math.max(0, prev.transactionsPerSecond + Math.floor(Math.random() * 20) - 10),
        avgLatencyMs: Math.max(0, 100 + Math.floor(Math.random() * 50) - 25),
        cpuUsage: Math.min(100, Math.max(0, prev.cpuUsage + Math.floor(Math.random() * 10) - 5))
      }));
    }, 2000);

    return () => clearInterval(interval);
  }, [isConnected]);

  useEffect(() => {
    // Check service health
    services.forEach((service, index) => {
      fetch(service.url)
        .then(res => res.json())
        .then(data => {
          setServices(prev => {
            const updated = [...prev];
            updated[index] = { ...updated[index], status: 'healthy', details: data };
            return updated;
          });
        })
        .catch(() => {
          setServices(prev => {
            const updated = [...prev];
            updated[index] = { ...updated[index], status: 'error' };
            return updated;
          });
        });
    });
  }, []);

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3 }}>
        <Box>
          <Typography variant="h4" gutterBottom>
            Analytics Engine Demo
          </Typography>
          <Typography variant="body1" color="text.secondary">
            Welcome to the Analytics Engine Demo & Configuration Application
          </Typography>
        </Box>
        <Chip 
          icon={isConnected ? <CheckCircleIcon /> : <CircularProgress size={16} />} 
          label={isConnected ? "Live Stream Connected" : "Connecting Stream..."}
          color={isConnected ? "success" : "default"}
          variant="outlined"
        />
      </Box>

      {/* Real-time Dashboard Widgets */}
      <Grid container spacing={3} sx={{ mb: 3 }}>
        <Grid item xs={12} sm={6} md={3}>
          <Card sx={{ bgcolor: 'primary.main', color: 'primary.contrastText' }}>
            <CardContent>
              <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <Box>
                  <Typography variant="overline" sx={{ opacity: 0.8 }}>Active Users</Typography>
                  <Typography variant="h4">{metrics.activeUsers}</Typography>
                </Box>
                <PeopleIcon sx={{ opacity: 0.8, fontSize: 40 }} />
              </Box>
              <Box sx={{ display: 'flex', alignItems: 'center', mt: 1, opacity: 0.8 }}>
                <TrendingUpIcon fontSize="small" sx={{ mr: 0.5 }} />
                <Typography variant="caption">+12% since last hour</Typography>
              </Box>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} sm={6} md={3}>
          <Card>
            <CardContent>
              <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <Box>
                  <Typography variant="overline" color="text.secondary">TPS</Typography>
                  <Typography variant="h4">{metrics.transactionsPerSecond}</Typography>
                </Box>
                <DataUsageIcon color="action" sx={{ fontSize: 40 }} />
              </Box>
              <Box sx={{ display: 'flex', alignItems: 'center', mt: 1 }}>
                <Chip label="High Load" size="small" color="warning" sx={{ height: 20, fontSize: '0.7rem' }} />
              </Box>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} sm={6} md={3}>
          <Card>
            <CardContent>
              <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <Box>
                  <Typography variant="overline" color="text.secondary">Avg Latency</Typography>
                  <Typography variant="h4">{metrics.avgLatencyMs}<Typography component="span" variant="caption" sx={{ ml: 0.5 }}>ms</Typography></Typography>
                </Box>
                <SpeedIcon color="action" sx={{ fontSize: 40 }} />
              </Box>
              <Box sx={{ display: 'flex', alignItems: 'center', mt: 1, color: 'success.main' }}>
                <TrendingDownIcon fontSize="small" sx={{ mr: 0.5 }} />
                <Typography variant="caption">Improving</Typography>
              </Box>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} sm={6} md={3}>
          <Card>
            <CardContent>
              <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <Box>
                  <Typography variant="overline" color="text.secondary">System CPU</Typography>
                  <Typography variant="h4">{metrics.cpuUsage}%</Typography>
                </Box>
                <Box sx={{ position: 'relative', display: 'inline-flex' }}>
                  <CircularProgress variant="determinate" value={metrics.cpuUsage} color={metrics.cpuUsage > 80 ? 'error' : 'primary'} />
                  <Box
                    sx={{
                      top: 0,
                      left: 0,
                      bottom: 0,
                      right: 0,
                      position: 'absolute',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                    }}
                  >
                  </Box>
                </Box>
              </Box>
              <Box sx={{ display: 'flex', alignItems: 'center', mt: 1, color: 'text.secondary' }}>
                <Typography variant="caption">4 Cores Active</Typography>
              </Box>
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      {/* Service Status */}
      <Paper sx={{ p: 3, mb: 3 }}>
        <Typography variant="h6" gutterBottom>
          Backend Services Status
        </Typography>
        <Grid container spacing={2} sx={{ mt: 1 }}>
          {services.map((service) => (
            <Grid item xs={12} md={4} key={service.name}>
              <Card variant="outlined">
                <CardContent>
                  <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
                    {service.status === 'healthy' && <CheckCircleIcon color="success" sx={{ mr: 1 }} />}
                    {service.status === 'error' && <ErrorIcon color="error" sx={{ mr: 1 }} />}
                    <Typography variant="subtitle1">{service.name}</Typography>
                  </Box>
                  <Chip 
                    label={service.status === 'healthy' ? 'Healthy' : service.status === 'error' ? 'Error' : 'Checking...'}
                    color={service.status === 'healthy' ? 'success' : service.status === 'error' ? 'error' : 'default'}
                    size="small"
                  />
                  {service.details && (
                    <Typography variant="caption" display="block" sx={{ mt: 1 }}>
                      {JSON.stringify(service.details, null, 2).substring(0, 100)}...
                    </Typography>
                  )}
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      </Paper>

      {/* Quick Actions */}
      <Paper sx={{ p: 3, mt: 3 }}>
        <Typography variant="h6" gutterBottom>
          Quick Actions
        </Typography>
        <Grid container spacing={2} sx={{ mt: 1 }}>
          <Grid item>
            <Button variant="contained" href="/config">
              Configure KPIs
            </Button>
          </Grid>
          <Grid item>
            <Button variant="outlined" href="http://localhost:8020/docs" target="_blank">
              Metadata API Docs
            </Button>
          </Grid>
          <Grid item>
            <Button variant="outlined" href="http://localhost:8021/docs" target="_blank">
              Calculation Engine Docs
            </Button>
          </Grid>
          <Grid item>
            <Button variant="outlined" href="http://localhost:8022/docs" target="_blank">
              Config API Docs
            </Button>
          </Grid>
        </Grid>
      </Paper>

      {/* Features */}
      <Paper sx={{ p: 3, mt: 3 }}>
        <Typography variant="h6" gutterBottom>
          Features
        </Typography>
        <Grid container spacing={2} sx={{ mt: 1 }}>
          <Grid item xs={12} md={6}>
            <Typography variant="subtitle2" gutterBottom>
              ✅ Metric Selection
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Browse and select from 500+ KPIs across multiple industries and value chains
            </Typography>
          </Grid>
          <Grid item xs={12} md={6}>
            <Typography variant="subtitle2" gutterBottom>
              ✅ UML Diagrams
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Visualize object models and their relationships with D3.js
            </Typography>
          </Grid>
          <Grid item xs={12} md={6}>
            <Typography variant="subtitle2" gutterBottom>
              ✅ Custom KPIs
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Create client-specific derived KPIs with RBAC
            </Typography>
          </Grid>
          <Grid item xs={12} md={6}>
            <Typography variant="subtitle2" gutterBottom>
              ✅ Service Proposals
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Generate automated SOW with cost estimates and timelines
            </Typography>
          </Grid>
        </Grid>
      </Paper>

      {/* Coming Soon */}
      <Paper sx={{ p: 3, mt: 3 }}>
        <Typography variant="h6" gutterBottom>
          Coming Soon
        </Typography>
        <Typography variant="body2" color="text.secondary">
          • Real-time KPI calculations<br />
          • Interactive D3.js visualizations<br />
          • Drag-and-drop data mapping<br />
          • Client app compilation<br />
          • Centralized monitoring dashboard
        </Typography>
      </Paper>
    </Box>
  );
}
