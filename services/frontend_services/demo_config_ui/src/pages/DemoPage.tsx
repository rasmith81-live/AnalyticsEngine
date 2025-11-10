import { Typography, Paper, Box, Grid, Card, CardContent, Chip, Button } from '@mui/material';
import { useState, useEffect } from 'react';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import ErrorIcon from '@mui/icons-material/Error';

interface ServiceStatus {
  name: string;
  url: string;
  status: 'healthy' | 'error' | 'checking';
  details?: any;
}

export default function DemoPage() {
  const [services, setServices] = useState<ServiceStatus[]>([
    { name: 'Metadata Service', url: 'http://localhost:8020/health', status: 'checking' },
    { name: 'Calculation Engine', url: 'http://localhost:8021/health', status: 'checking' },
    { name: 'Demo/Config Service', url: 'http://localhost:8022/health', status: 'checking' },
  ]);

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
      <Typography variant="h4" gutterBottom>
        Analytics Engine Demo
      </Typography>
      <Typography variant="body1" color="text.secondary" gutterBottom>
        Welcome to the Analytics Engine Demo & Configuration Application
      </Typography>

      {/* Service Status */}
      <Paper sx={{ p: 3, mt: 3 }}>
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
