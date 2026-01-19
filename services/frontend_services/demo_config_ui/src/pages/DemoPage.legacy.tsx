import { Typography, Paper, Box, Grid, Button } from '@mui/material';
import DashboardIcon from '@mui/icons-material/Dashboard';
import SettingsIcon from '@mui/icons-material/Settings';
import UploadFileIcon from '@mui/icons-material/UploadFile';
import MonitorHeartIcon from '@mui/icons-material/MonitorHeart';

export default function DemoPage() {

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Analytics Engine Demo
      </Typography>
      <Typography variant="body1" color="text.secondary" paragraph>
        Welcome to the Analytics Engine - a real-time, microservices-based analytics platform for on-demand KPI calculations.
      </Typography>

      {/* Quick Start Guide */}
      <Paper sx={{ p: 3, mb: 3 }}>
        <Typography variant="h6" gutterBottom>
          Quick Start Guide
        </Typography>
        <Grid container spacing={3} sx={{ mt: 1 }}>
          <Grid item xs={12} md={6}>
            <Box sx={{ display: 'flex', alignItems: 'flex-start', mb: 2 }}>
              <Box sx={{ bgcolor: 'primary.main', color: 'white', borderRadius: '50%', width: 32, height: 32, display: 'flex', alignItems: 'center', justifyContent: 'center', mr: 2, flexShrink: 0 }}>
                1
              </Box>
              <Box>
                <Typography variant="subtitle1" fontWeight="bold" gutterBottom>
                  Configure Your KPIs
                </Typography>
                <Typography variant="body2" color="text.secondary" paragraph>
                  Browse the metric tree and select KPIs relevant to your business. Choose from Supply Chain, CRM, Sales, and Financial value chains.
                </Typography>
                <Button variant="outlined" size="small" href="/config" startIcon={<SettingsIcon />}>
                  Go to KPI Configuration
                </Button>
              </Box>
            </Box>
          </Grid>

          <Grid item xs={12} md={6}>
            <Box sx={{ display: 'flex', alignItems: 'flex-start', mb: 2 }}>
              <Box sx={{ bgcolor: 'primary.main', color: 'white', borderRadius: '50%', width: 32, height: 32, display: 'flex', alignItems: 'center', justifyContent: 'center', mr: 2, flexShrink: 0 }}>
                2
              </Box>
              <Box>
                <Typography variant="subtitle1" fontWeight="bold" gutterBottom>
                  Import KPI Definitions
                </Typography>
                <Typography variant="body2" color="text.secondary" paragraph>
                  Upload Excel files with KPI definitions for bulk import. The system validates formulas and object references automatically.
                </Typography>
                <Button variant="outlined" size="small" href="/excel-import" startIcon={<UploadFileIcon />}>
                  Go to Excel Import
                </Button>
              </Box>
            </Box>
          </Grid>

          <Grid item xs={12} md={6}>
            <Box sx={{ display: 'flex', alignItems: 'flex-start', mb: 2 }}>
              <Box sx={{ bgcolor: 'primary.main', color: 'white', borderRadius: '50%', width: 32, height: 32, display: 'flex', alignItems: 'center', justifyContent: 'center', mr: 2, flexShrink: 0 }}>
                3
              </Box>
              <Box>
                <Typography variant="subtitle1" fontWeight="bold" gutterBottom>
                  Explore Object Models
                </Typography>
                <Typography variant="body2" color="text.secondary" paragraph>
                  View UML diagrams and understand the data structures required for your selected KPIs.
                </Typography>
                <Button variant="outlined" size="small" href="/object-models" startIcon={<DashboardIcon />}>
                  Browse Object Models
                </Button>
              </Box>
            </Box>
          </Grid>

          <Grid item xs={12} md={6}>
            <Box sx={{ display: 'flex', alignItems: 'flex-start', mb: 2 }}>
              <Box sx={{ bgcolor: 'primary.main', color: 'white', borderRadius: '50%', width: 32, height: 32, display: 'flex', alignItems: 'center', justifyContent: 'center', mr: 2, flexShrink: 0 }}>
                4
              </Box>
              <Box>
                <Typography variant="subtitle1" fontWeight="bold" gutterBottom>
                  Monitor System Health
                </Typography>
                <Typography variant="body2" color="text.secondary" paragraph>
                  Check the status of all backend services and view real-time system metrics.
                </Typography>
                <Button variant="outlined" size="small" href="/system-monitor" startIcon={<MonitorHeartIcon />}>
                  View System Monitor
                </Button>
              </Box>
            </Box>
          </Grid>
        </Grid>
      </Paper>

      {/* Key Features */}
      <Paper sx={{ p: 3, mb: 3 }}>
        <Typography variant="h6" gutterBottom>
          Platform Capabilities
        </Typography>
        <Grid container spacing={3} sx={{ mt: 1 }}>
          <Grid item xs={12} md={4}>
            <Typography variant="subtitle2" gutterBottom fontWeight="bold">
              Real-Time Analytics
            </Typography>
            <Typography variant="body2" color="text.secondary">
              On-demand KPI calculations with sub-second latency. No pre-computed batch processing - all metrics calculated in real-time.
            </Typography>
          </Grid>
          <Grid item xs={12} md={4}>
            <Typography variant="subtitle2" gutterBottom fontWeight="bold">
              Microservices Architecture
            </Typography>
            <Typography variant="body2" color="text.secondary">
              21 independent services working together. Scale calculation engines independently based on workload requirements.
            </Typography>
          </Grid>
          <Grid item xs={12} md={4}>
            <Typography variant="subtitle2" gutterBottom fontWeight="bold">
              AI-Powered Guidance
            </Typography>
            <Typography variant="body2" color="text.secondary">
              OpenAI-powered conversation service helps you select the right KPIs and design your analytics value chain.
            </Typography>
          </Grid>
          <Grid item xs={12} md={4}>
            <Typography variant="subtitle2" gutterBottom fontWeight="bold">
              TimescaleDB Integration
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Optimized time-series database with hypertables and continuous aggregates for high-performance analytics.
            </Typography>
          </Grid>
          <Grid item xs={12} md={4}>
            <Typography variant="subtitle2" gutterBottom fontWeight="bold">
              Event-Driven Updates
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Redis-powered messaging ensures all services stay synchronized. Real-time data propagation across the platform.
            </Typography>
          </Grid>
          <Grid item xs={12} md={4}>
            <Typography variant="subtitle2" gutterBottom fontWeight="bold">
              Enterprise Ready
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Built-in data governance, row-level security, audit logging, and compliance features for enterprise deployments.
            </Typography>
          </Grid>
        </Grid>
      </Paper>

      {/* API Documentation */}
      <Paper sx={{ p: 3 }}>
        <Typography variant="h6" gutterBottom>
          API Documentation
        </Typography>
        <Typography variant="body2" color="text.secondary" paragraph>
          Explore the interactive API documentation for each service:
        </Typography>
        <Grid container spacing={2}>
          <Grid item>
            <Button variant="outlined" size="small" href="http://localhost:8020/docs" target="_blank">
              Business Metadata API
            </Button>
          </Grid>
          <Grid item>
            <Button variant="outlined" size="small" href="http://localhost:8021/docs" target="_blank">
              Calculation Engine API
            </Button>
          </Grid>
          <Grid item>
            <Button variant="outlined" size="small" href="http://localhost:8022/docs" target="_blank">
              Demo Config API
            </Button>
          </Grid>
          <Grid item>
            <Button variant="outlined" size="small" href="http://localhost:8025/docs" target="_blank">
              Metadata Ingestion API
            </Button>
          </Grid>
          <Grid item>
            <Button variant="outlined" size="small" href="http://localhost:8026/docs" target="_blank">
              Conversation API
            </Button>
          </Grid>
          <Grid item>
            <Button variant="outlined" size="small" href="http://127.0.0.1:8090/docs" target="_blank">
              API Gateway
            </Button>
          </Grid>
        </Grid>
      </Paper>
    </Box>
  );
}
