import { useState, useEffect } from 'react';
import {
  Box,
  Typography,
  Paper,
  Grid,
  Card,
  CardContent,
  Button,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  TextField,
  LinearProgress,
  List,
  ListItem,
  ListItemText,
  ListItemIcon,
  Chip,
  Stack,
  Alert
} from '@mui/material';
import {
  PlayArrow as RunIcon,
  Schedule as TimeIcon,
  Timeline as GraphIcon,
  CheckCircle as SuccessIcon,
  Error as FailIcon,
  Autorenew as RunningIcon,
  CloudQueue as CloudIcon
} from '@mui/icons-material';
import { useWebSocket } from '../hooks/useWebSocket';

// Mock Scenarios
const SCENARIOS = [
  { id: 'sc_seasonal', name: 'Seasonal Peak', description: 'Simulates 3x traffic spike during Q4 holidays', duration: '2 hours' },
  { id: 'sc_churn', name: 'Churn Event', description: 'Simulates 15% customer drop-off over 1 week', duration: '4 hours' },
  { id: 'sc_new_market', name: 'New Market Entry', description: 'Simulates exponential growth from zero in new region', duration: '1 hour' },
  { id: 'sc_supply_shock', name: 'Supply Chain Disruption', description: 'Simulates inventory stockouts and delivery delays', duration: '3 hours' },
];

interface SimulationJob {
  id: string;
  scenarioName: string;
  status: 'pending' | 'running' | 'completed' | 'failed';
  progress: number;
  startTime: string;
  message?: string;
}

export default function SimulationPage() {
  const [selectedScenario, setSelectedScenario] = useState('');
  const [startDate, setStartDate] = useState('2024-01-01');
  const [endDate, setEndDate] = useState('2024-12-31');
  const [activeJobs, setActiveJobs] = useState<SimulationJob[]>([]);
  
  const { isConnected, lastMessage } = useWebSocket({
    url: 'ws://127.0.0.1:8090/ws/simulation', // Config Service WebSocket via Gateway
  });

  // Handle incoming websocket updates
  useEffect(() => {
    if (lastMessage && lastMessage.type === 'job_update') {
      setActiveJobs(prev => prev.map(job => 
        job.id === lastMessage.payload.id ? { ...job, ...lastMessage.payload } : job
      ));
    }
  }, [lastMessage]);

  const handleRunSimulation = () => {
    if (!selectedScenario) return;

    const scenario = SCENARIOS.find(s => s.id === selectedScenario);
    const newJob: SimulationJob = {
      id: `job_${Date.now()}`,
      scenarioName: scenario?.name || 'Unknown',
      status: 'pending',
      progress: 0,
      startTime: new Date().toLocaleTimeString()
    };

    setActiveJobs([newJob, ...activeJobs]);

    // Simulate backend job execution (since we might not have the full backend running)
    simulateJobExecution(newJob.id);
  };

  const simulateJobExecution = (jobId: string) => {
    let progress = 0;
    const interval = setInterval(() => {
      progress += Math.floor(Math.random() * 10) + 5;
      
      setActiveJobs(prev => prev.map(job => {
        if (job.id !== jobId) return job;
        
        if (progress >= 100) {
          clearInterval(interval);
          return { ...job, status: 'completed', progress: 100, message: 'Data generation complete' };
        }
        
        return { 
          ...job, 
          status: 'running', 
          progress, 
          message: `Generating batch ${Math.floor(progress)}/100...` 
        };
      }));
    }, 1000);
  };

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'running': return <RunningIcon className="spin" color="primary" />; // Note: Needs CSS for spin
      case 'completed': return <SuccessIcon color="success" />;
      case 'failed': return <FailIcon color="error" />;
      default: return <CloudIcon color="disabled" />;
    }
  };

  return (
    <Box>
      <Box sx={{ mb: 3 }}>
        <Typography variant="h4" gutterBottom>
          Simulation Controller
        </Typography>
        <Typography variant="body1" color="text.secondary">
          Generate synthetic data scenarios to test KPIs and dashboards under different conditions.
        </Typography>
      </Box>

      {!isConnected && (
        <Alert severity="warning" sx={{ mb: 3 }}>
          WebSocket disconnected. Real-time updates may be delayed.
        </Alert>
      )}

      <Grid container spacing={3}>
        {/* Configuration Panel */}
        <Grid item xs={12} md={4}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                New Simulation Run
              </Typography>
              <Stack spacing={3} sx={{ mt: 2 }}>
                <FormControl fullWidth>
                  <InputLabel>Scenario</InputLabel>
                  <Select
                    value={selectedScenario}
                    label="Scenario"
                    onChange={(e) => setSelectedScenario(e.target.value)}
                  >
                    {SCENARIOS.map((s) => (
                      <MenuItem key={s.id} value={s.id}>{s.name}</MenuItem>
                    ))}
                  </Select>
                </FormControl>

                {selectedScenario && (
                  <Paper variant="outlined" sx={{ p: 2, bgcolor: 'grey.50' }}>
                    <Typography variant="subtitle2">Description:</Typography>
                    <Typography variant="body2" color="text.secondary" paragraph>
                      {SCENARIOS.find(s => s.id === selectedScenario)?.description}
                    </Typography>
                    <Chip size="small" icon={<TimeIcon />} label={`Est. Duration: ${SCENARIOS.find(s => s.id === selectedScenario)?.duration}`} />
                  </Paper>
                )}

                <TextField
                  label="Start Date"
                  type="date"
                  value={startDate}
                  onChange={(e) => setStartDate(e.target.value)}
                  InputLabelProps={{ shrink: true }}
                  fullWidth
                />
                <TextField
                  label="End Date"
                  type="date"
                  value={endDate}
                  onChange={(e) => setEndDate(e.target.value)}
                  InputLabelProps={{ shrink: true }}
                  fullWidth
                />

                <Button
                  variant="contained"
                  size="large"
                  startIcon={<RunIcon />}
                  onClick={handleRunSimulation}
                  disabled={!selectedScenario}
                >
                  Start Simulation
                </Button>
              </Stack>
            </CardContent>
          </Card>
        </Grid>

        {/* Active Jobs Monitor */}
        <Grid item xs={12} md={8}>
          <Card sx={{ height: '100%' }}>
            <CardContent>
              <Typography variant="h6" gutterBottom sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                <GraphIcon /> Active Jobs
              </Typography>
              
              {activeJobs.length === 0 ? (
                <Box sx={{ textAlign: 'center', py: 5, color: 'text.disabled' }}>
                  <CloudIcon sx={{ fontSize: 60, mb: 1 }} />
                  <Typography>No active simulation jobs</Typography>
                </Box>
              ) : (
                <List>
                  {activeJobs.map((job) => (
                    <Paper key={job.id} variant="outlined" sx={{ mb: 2 }}>
                      <ListItem>
                        <ListItemIcon>
                          {getStatusIcon(job.status)}
                        </ListItemIcon>
                        <ListItemText
                          primary={job.scenarioName}
                          secondary={
                            <Box sx={{ mt: 1 }}>
                              <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.5 }}>
                                <Typography variant="caption" color="text.secondary">
                                  {job.message || job.status.toUpperCase()}
                                </Typography>
                                <Typography variant="caption" color="text.secondary">
                                  {job.progress}%
                                </Typography>
                              </Box>
                              <LinearProgress 
                                variant="determinate" 
                                value={job.progress} 
                                color={job.status === 'failed' ? 'error' : 'primary'}
                              />
                            </Box>
                          }
                        />
                        <Typography variant="caption" sx={{ ml: 2, minWidth: 70, textAlign: 'right' }}>
                          {job.startTime}
                        </Typography>
                      </ListItem>
                    </Paper>
                  ))}
                </List>
              )}
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
}
