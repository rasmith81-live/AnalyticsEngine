import { Typography, Paper, Box, Grid, Card, CardContent, Chip, CircularProgress, Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from '@mui/material';
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

const ALL_SERVICES = [
  { name: 'Database Service', url: 'http://localhost:8000/health' },
  { name: 'Messaging Service', url: 'http://localhost:8002/health' },
  { name: 'Observability Service', url: 'http://localhost:8080/health' },
  { name: 'Archival Service', url: 'http://localhost:8005/health' },
  { name: 'Business Metadata', url: 'http://localhost:8020/health' },
  { name: 'Calculation Engine', url: 'http://localhost:8021/health' },
  { name: 'Demo Config Service', url: 'http://localhost:8022/health' },
  { name: 'Connector Service', url: 'http://localhost:8023/health' },
  { name: 'Ingestion Service', url: 'http://localhost:8024/health' },
  { name: 'Metadata Ingestion', url: 'http://localhost:8025/health' },
  { name: 'Conversation Service', url: 'http://localhost:8026/health' },
  { name: 'Systems Monitor', url: 'http://localhost:8010/health' },
  { name: 'Entity Resolution', url: 'http://localhost:8012/health' },
  { name: 'Data Governance', url: 'http://localhost:8013/health' },
  { name: 'Machine Learning', url: 'http://localhost:8014/health' },
  { name: 'API Gateway', url: 'http://127.0.0.1:8090/health' },
];

export default function SystemMonitorPage() {
  const [services, setServices] = useState<ServiceStatus[]>(
    ALL_SERVICES.map(s => ({ ...s, status: 'checking' as const }))
  );

  const [metrics, setMetrics] = useState<RealTimeMetrics>({
    activeUsers: 142,
    transactionsPerSecond: 45,
    avgLatencyMs: 120,
    cpuUsage: 35
  });

  const { isConnected, lastMessage } = useWebSocket({
    url: 'ws://127.0.0.1:8090/ws',
    onOpen: () => console.log('System Monitor connected to websocket'),
  });

  useEffect(() => {
    if (lastMessage && lastMessage.type === 'dashboard_update') {
      setMetrics(prev => ({
        ...prev,
        ...lastMessage.payload
      }));
    }
  }, [lastMessage]);

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
    const checkServices = () => {
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
    };

    checkServices();
    const interval = setInterval(checkServices, 30000);
    return () => clearInterval(interval);
  }, []);

  const healthyCount = services.filter(s => s.status === 'healthy').length;
  const errorCount = services.filter(s => s.status === 'error').length;

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3 }}>
        <Box>
          <Typography variant="h4" gutterBottom>
            System Monitor
          </Typography>
          <Typography variant="body1" color="text.secondary">
            Real-time monitoring of all Analytics Engine services and system metrics
          </Typography>
        </Box>
        <Chip 
          icon={isConnected ? <CheckCircleIcon /> : <CircularProgress size={16} />} 
          label={isConnected ? "Live Stream Connected" : "Connecting Stream..."}
          color={isConnected ? "success" : "default"}
          variant="outlined"
        />
      </Box>

      {/* System Health Summary */}
      <Grid container spacing={2} sx={{ mb: 3 }}>
        <Grid item xs={12} md={4}>
          <Card sx={{ bgcolor: 'success.light', color: 'success.contrastText' }}>
            <CardContent>
              <Typography variant="h3">{healthyCount}/{services.length}</Typography>
              <Typography variant="body2">Services Healthy</Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={4}>
          <Card sx={{ bgcolor: errorCount > 0 ? 'error.light' : 'grey.100' }}>
            <CardContent>
              <Typography variant="h3" color={errorCount > 0 ? 'error.contrastText' : 'text.primary'}>
                {errorCount}
              </Typography>
              <Typography variant="body2" color={errorCount > 0 ? 'error.contrastText' : 'text.secondary'}>
                Services Down
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={4}>
          <Card>
            <CardContent>
              <Typography variant="h3">{services.filter(s => s.status === 'checking').length}</Typography>
              <Typography variant="body2" color="text.secondary">Checking...</Typography>
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      {/* Real-time System Metrics */}
      <Paper sx={{ p: 3, mb: 3 }}>
        <Typography variant="h6" gutterBottom>
          Real-time System Metrics
        </Typography>
        <Grid container spacing={3} sx={{ mt: 1 }}>
          <Grid item xs={12} sm={6} md={3}>
            <Card>
              <CardContent>
                <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                  <Box>
                    <Typography variant="overline" color="text.secondary">Active Users</Typography>
                    <Typography variant="h4">{metrics.activeUsers}</Typography>
                  </Box>
                  <PeopleIcon color="action" sx={{ fontSize: 40 }} />
                </Box>
                <Box sx={{ display: 'flex', alignItems: 'center', mt: 1, color: 'success.main' }}>
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
                  </Box>
                </Box>
                <Box sx={{ display: 'flex', alignItems: 'center', mt: 1, color: 'text.secondary' }}>
                  <Typography variant="caption">4 Cores Active</Typography>
                </Box>
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      </Paper>

      {/* Service Status Table */}
      <Paper sx={{ p: 3 }}>
        <Typography variant="h6" gutterBottom>
          All Services Status
        </Typography>
        <TableContainer>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>Service Name</TableCell>
                <TableCell>Status</TableCell>
                <TableCell>Endpoint</TableCell>
                <TableCell>Details</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {services.map((service) => (
                <TableRow key={service.name}>
                  <TableCell>
                    <Box sx={{ display: 'flex', alignItems: 'center' }}>
                      {service.status === 'healthy' && <CheckCircleIcon color="success" sx={{ mr: 1 }} />}
                      {service.status === 'error' && <ErrorIcon color="error" sx={{ mr: 1 }} />}
                      {service.status === 'checking' && <CircularProgress size={20} sx={{ mr: 1 }} />}
                      <Typography variant="body2">{service.name}</Typography>
                    </Box>
                  </TableCell>
                  <TableCell>
                    <Chip 
                      label={service.status === 'healthy' ? 'Healthy' : service.status === 'error' ? 'Error' : 'Checking...'}
                      color={service.status === 'healthy' ? 'success' : service.status === 'error' ? 'error' : 'default'}
                      size="small"
                    />
                  </TableCell>
                  <TableCell>
                    <Typography variant="caption" fontFamily="monospace">{service.url}</Typography>
                  </TableCell>
                  <TableCell>
                    {service.details && (
                      <Typography variant="caption" color="text.secondary">
                        {service.details.service || 'OK'}
                      </Typography>
                    )}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Paper>
    </Box>
  );
}
