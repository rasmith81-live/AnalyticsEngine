import React, { useState, useEffect } from 'react';
import {
  Typography,
  Paper,
  Box,
  Tabs,
  Tab,
  TextField,
  Button,
  Grid,
  Card,
  CardContent,
  CardHeader,
  List,
  ListItem,
  ListItemText,
  Switch,
  FormControlLabel,
  Divider,
  Chip,
  LinearProgress,
} from '@mui/material';
import {
  VpnKey as KeyIcon,
  HealthAndSafety as HealthIcon,
  DeleteForever as RetentionIcon,
  NotificationsActive as AlertIcon,
  CheckCircle as HealthyIcon,
  Error as ErrorIcon,
  Warning as WarningIcon,
  Save as SaveIcon,
  Refresh as RefreshIcon,
  Terminal as TerminalIcon,
  Block as StopIcon,
  PlayArrow as StartIcon,
} from '@mui/icons-material';
import { configApi, ClientConfig } from '../api/configApi';

interface LogEntry {
  timestamp: string;
  level: 'INFO' | 'WARN' | 'ERROR' | 'DEBUG';
  service: string;
  message: string;
}

interface TabPanelProps {
  children?: React.ReactNode;
  index: number;
  value: number;
}

function TabPanel(props: TabPanelProps) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`admin-tabpanel-${index}`}
      aria-labelledby={`admin-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          {children}
        </Box>
      )}
    </div>
  );
}

export default function AdminPage() {
  const [value, setValue] = useState(0);
  const [loading, setLoading] = useState(false);
  const [config, setConfig] = useState<ClientConfig | null>(null);
  const [healthStatus, setHealthStatus] = useState<Record<string, string>>({});
  const [licenseKey, setLicenseKey] = useState('');
  const [logs, setLogs] = useState<LogEntry[]>([]);
  const [isLive, setIsLive] = useState(true);
  
  // Mock settings for retention and alerts
  const [retentionSettings, setRetentionSettings] = useState({
    logRetentionDays: 30,
    dataRetentionDays: 365,
    archiveEnabled: true,
  });

  const [alertSettings, setAlertSettings] = useState({
    emailNotifications: true,
    slackNotifications: false,
    errorThreshold: 10,
    emailAddress: 'admin@example.com',
  });

  // Mock services for health check
  const SERVICES = [
    'API Gateway',
    'Metadata Service',
    'Calculation Engine',
    'Config Service',
    'Ingestion Service',
    'Entity Resolution',
  ];

  useEffect(() => {
    fetchConfig();
    checkHealth();
  }, []);

  // Simulate Log Streaming
  useEffect(() => {
    if (!isLive) return;

    const interval = setInterval(() => {
      const services = ['API Gateway', 'Calculation Engine', 'Metadata Service', 'Ingestion'];
      const levels: LogEntry['level'][] = ['INFO', 'INFO', 'INFO', 'WARN', 'DEBUG', 'ERROR'];
      const messages = [
        'Processing request id: req_' + Math.floor(Math.random() * 10000),
        'Cache hit for key: kpi_' + Math.floor(Math.random() * 100),
        'Database connection pool utilization: ' + Math.floor(Math.random() * 100) + '%',
        'Received heartbeat from service',
        'Batch job started',
        'Batch job completed in ' + Math.floor(Math.random() * 500) + 'ms',
        'Connection timeout retrying...',
        'Schema validation failed for object order_123'
      ];

      const newLog: LogEntry = {
        timestamp: new Date().toISOString(),
        service: services[Math.floor(Math.random() * services.length)],
        level: levels[Math.floor(Math.random() * levels.length)],
        message: messages[Math.floor(Math.random() * messages.length)]
      };

      setLogs(prev => [...prev.slice(-99), newLog]); // Keep last 100
    }, 1500);

    return () => clearInterval(interval);
  }, [isLive]);

  const fetchConfig = async () => {
    setLoading(true);
    try {
      // Fetch first client config for demo purposes
      const configs = await configApi.getClientConfigs();
      if (configs.length > 0) {
        setConfig(configs[0]);
        setLicenseKey(configs[0].license_key || '');
      }
    } catch (error) {
      console.error('Error fetching config:', error);
    } finally {
      setLoading(false);
    }
  };

  const checkHealth = async () => {
    // In a real app, we would hit health endpoints for each service
    // For now, we'll mock it or use observability API if available
    const status: Record<string, string> = {};
    SERVICES.forEach(service => {
      // Randomly assign status for demo
      status[service] = Math.random() > 0.1 ? 'healthy' : 'degraded';
    });
    setHealthStatus(status);
  };

  const handleChange = (_: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
  };

  const handleUpdateLicense = async () => {
    if (!config) return;
    try {
      await configApi.updateClientConfig(config.client_id, {
        license_key: licenseKey
      });
      alert('License key updated successfully');
    } catch (error) {
      console.error('Error updating license:', error);
      alert('Failed to update license key');
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'healthy': return 'success';
      case 'degraded': return 'warning';
      case 'down': return 'error';
      default: return 'default';
    }
  };

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'healthy': return <HealthyIcon color="success" />;
      case 'degraded': return <WarningIcon color="warning" />;
      case 'down': return <ErrorIcon color="error" />;
      default: return <ErrorIcon />;
    }
  };

  return (
    <Box sx={{ width: '100%' }}>
      <Typography variant="h4" gutterBottom>
        Administration
      </Typography>

      {loading && <LinearProgress sx={{ mb: 2 }} />}

      <Paper sx={{ width: '100%', mb: 2 }}>
        <Tabs value={value} onChange={handleChange} aria-label="admin tabs">
          <Tab icon={<KeyIcon />} label="License" />
          <Tab icon={<HealthIcon />} label="System Health" />
          <Tab icon={<RetentionIcon />} label="Retention" />
          <Tab icon={<AlertIcon />} label="Alerts" />
          <Tab icon={<TerminalIcon />} label="Live Logs" />
        </Tabs>
      </Paper>

      {/* License Management */}
      <TabPanel value={value} index={0}>
        <Grid container spacing={3}>
          <Grid item xs={12} md={6}>
            <Card>
              <CardHeader title="License Configuration" subheader="Manage your enterprise license" />
              <CardContent>
                <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                  <TextField
                    label="License Key"
                    value={licenseKey}
                    onChange={(e) => setLicenseKey(e.target.value)}
                    fullWidth
                    type="password"
                    helperText="Enter your 32-character enterprise license key"
                  />
                  <Box sx={{ display: 'flex', gap: 2, alignItems: 'center' }}>
                    <Typography variant="body2" color="text.secondary">
                      Status: 
                    </Typography>
                    <Chip 
                      label={licenseKey ? "Active" : "No License"} 
                      color={licenseKey ? "success" : "default"} 
                      size="small" 
                    />
                  </Box>
                  <Button 
                    variant="contained" 
                    startIcon={<SaveIcon />}
                    onClick={handleUpdateLicense}
                    disabled={!config}
                  >
                    Update License
                  </Button>
                </Box>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} md={6}>
            <Card>
              <CardHeader title="License Details" />
              <CardContent>
                <List>
                  <ListItem>
                    <ListItemText primary="Plan Type" secondary="Enterprise" />
                  </ListItem>
                  <Divider />
                  <ListItem>
                    <ListItemText primary="Expiration Date" secondary="2025-12-31" />
                  </ListItem>
                  <Divider />
                  <ListItem>
                    <ListItemText primary="Max Users" secondary="Unlimited" />
                  </ListItem>
                  <Divider />
                  <ListItem>
                    <ListItemText primary="Max Data Storage" secondary="10 TB" />
                  </ListItem>
                </List>
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      </TabPanel>

      {/* System Health */}
      <TabPanel value={value} index={1}>
        <Box sx={{ display: 'flex', justifyContent: 'flex-end', mb: 2 }}>
          <Button startIcon={<RefreshIcon />} onClick={checkHealth}>
            Refresh Status
          </Button>
        </Box>
        <Grid container spacing={3}>
          {SERVICES.map((service) => (
            <Grid item xs={12} md={4} key={service}>
              <Card>
                <CardContent>
                  <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                    <Typography variant="h6">{service}</Typography>
                    {getStatusIcon(healthStatus[service] || 'unknown')}
                  </Box>
                  <Typography 
                    variant="body2" 
                    color={`text.${getStatusColor(healthStatus[service] || 'unknown')}`}
                    sx={{ mt: 1, textTransform: 'capitalize' }}
                  >
                    {healthStatus[service] || 'Unknown'}
                  </Typography>
                  <Typography variant="caption" color="text.secondary" display="block" sx={{ mt: 1 }}>
                    Last check: {new Date().toLocaleTimeString()}
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      </TabPanel>

      {/* Retention Policies */}
      <TabPanel value={value} index={2}>
        <Card>
          <CardHeader title="Data Retention Policies" />
          <CardContent>
            <Grid container spacing={3}>
              <Grid item xs={12} md={6}>
                <TextField
                  label="Log Retention (Days)"
                  type="number"
                  fullWidth
                  value={retentionSettings.logRetentionDays}
                  onChange={(e) => setRetentionSettings({...retentionSettings, logRetentionDays: parseInt(e.target.value)})}
                  helperText="How long to keep application logs"
                />
              </Grid>
              <Grid item xs={12} md={6}>
                <TextField
                  label="Historical Data Retention (Days)"
                  type="number"
                  fullWidth
                  value={retentionSettings.dataRetentionDays}
                  onChange={(e) => setRetentionSettings({...retentionSettings, dataRetentionDays: parseInt(e.target.value)})}
                  helperText="How long to keep historical analysis data"
                />
              </Grid>
              <Grid item xs={12}>
                <FormControlLabel
                  control={
                    <Switch
                      checked={retentionSettings.archiveEnabled}
                      onChange={(e) => setRetentionSettings({...retentionSettings, archiveEnabled: e.target.checked})}
                    />
                  }
                  label="Enable Automatic Archiving"
                />
              </Grid>
              <Grid item xs={12}>
                <Button variant="contained" startIcon={<SaveIcon />}>
                  Save Retention Settings
                </Button>
              </Grid>
            </Grid>
          </CardContent>
        </Card>
      </TabPanel>

      {/* Alerts Configuration */}
      <TabPanel value={value} index={3}>
        <Card>
          <CardHeader title="Alert Configuration" />
          <CardContent>
            <Box sx={{ display: 'flex', flexDirection: 'column', gap: 3 }}>
              <FormControlLabel
                control={
                  <Switch
                    checked={alertSettings.emailNotifications}
                    onChange={(e) => setAlertSettings({...alertSettings, emailNotifications: e.target.checked})}
                  />
                }
                label="Enable Email Notifications"
              />
              
              {alertSettings.emailNotifications && (
                <TextField
                  label="Alert Email Address"
                  fullWidth
                  value={alertSettings.emailAddress}
                  onChange={(e) => setAlertSettings({...alertSettings, emailAddress: e.target.value})}
                />
              )}

              <FormControlLabel
                control={
                  <Switch
                    checked={alertSettings.slackNotifications}
                    onChange={(e) => setAlertSettings({...alertSettings, slackNotifications: e.target.checked})}
                  />
                }
                label="Enable Slack Notifications"
              />

              <TextField
                label="Error Threshold (per minute)"
                type="number"
                fullWidth
                value={alertSettings.errorThreshold}
                onChange={(e) => setAlertSettings({...alertSettings, errorThreshold: parseInt(e.target.value)})}
                helperText="Trigger alert if error count exceeds this value"
              />

              <Button variant="contained" startIcon={<SaveIcon />} sx={{ width: 'fit-content' }}>
                Save Alert Settings
              </Button>
            </Box>
          </CardContent>
        </Card>
      </TabPanel>

      {/* Live Logs */}
      <TabPanel value={value} index={4}>
        <Card sx={{ bgcolor: '#1e1e1e', color: '#f0f0f0' }}>
          <Box sx={{ p: 2, display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid #333' }}>
            <Typography variant="h6" sx={{ color: '#fff' }}>
              System Logs Stream
            </Typography>
            <Box sx={{ display: 'flex', gap: 1 }}>
              <Button 
                startIcon={isLive ? <StopIcon /> : <StartIcon />} 
                onClick={() => setIsLive(!isLive)}
                variant="contained"
                color={isLive ? "error" : "success"}
                size="small"
              >
                {isLive ? "Pause Stream" : "Resume Stream"}
              </Button>
              <Button 
                startIcon={<RefreshIcon />} 
                onClick={() => setLogs([])}
                variant="outlined"
                sx={{ color: '#fff', borderColor: '#666' }}
                size="small"
              >
                Clear
              </Button>
            </Box>
          </Box>
          <CardContent sx={{ p: 0 }}>
            <Box sx={{ height: '500px', overflow: 'auto', p: 2, fontFamily: 'monospace', fontSize: '0.875rem' }}>
              {logs.length === 0 ? (
                <Typography sx={{ color: '#666', fontStyle: 'italic' }}>Waiting for logs...</Typography>
              ) : (
                logs.map((log, i) => (
                  <Box key={i} sx={{ mb: 0.5, display: 'flex', gap: 2 }}>
                    <span style={{ color: '#888' }}>{new Date(log.timestamp).toLocaleTimeString()}</span>
                    <span style={{ 
                      color: log.level === 'ERROR' ? '#ff5252' : 
                             log.level === 'WARN' ? '#ffb74d' : 
                             log.level === 'DEBUG' ? '#4fc3f7' : '#66bb6a',
                      fontWeight: 'bold',
                      minWidth: '60px'
                    }}>{log.level}</span>
                    <span style={{ color: '#ba68c8', minWidth: '150px' }}>[{log.service}]</span>
                    <span>{log.message}</span>
                  </Box>
                ))
              )}
            </Box>
          </CardContent>
        </Card>
      </TabPanel>
    </Box>
  );
}
