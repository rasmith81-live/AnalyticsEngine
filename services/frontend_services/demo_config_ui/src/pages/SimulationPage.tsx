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
  List,
  ListItem,
  ListItemText,
  ListItemIcon,
  Chip,
  Stack,
  Alert,
  Autocomplete,
  Slider,
  Divider,
  IconButton,
  Tooltip,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  CircularProgress,
  Collapse,
  Switch,
  FormControlLabel,
} from '@mui/material';
import {
  PlayArrow as RunIcon,
  Stop as StopIcon,
  Pause as PauseIcon,
  PlayCircle as ResumeIcon,
  Timeline as GraphIcon,
  CheckCircle as SuccessIcon,
  Autorenew as RunningIcon,
  CloudQueue as CloudIcon,
  Speed as SpeedIcon,
  Delete as DeleteIcon,
  ExpandMore as ExpandIcon,
  ExpandLess as CollapseIcon,
  Refresh as RefreshIcon,
  Storage as EntityIcon,
} from '@mui/icons-material';

const API_BASE = '/api/v1/simulator';

// Scenario options
const SCENARIOS = [
  { id: 'healthy', name: 'Healthy Business', description: 'Low churn (1%), steady growth (7.5%)' },
  { id: 'struggling', name: 'Struggling Business', description: 'High churn (4%), low growth (1.5%)' },
  { id: 'seasonal', name: 'Seasonal Patterns', description: 'Cyclical variations throughout the year' },
  { id: 'growth_spurt', name: 'Growth Spurt', description: 'Rapid expansion (15% growth), low churn' },
  { id: 'stable', name: 'Stable', description: 'Minimal change, steady state' },
  { id: 'volatile', name: 'Volatile', description: 'High variance, unpredictable patterns' },
];

interface KPIInfo {
  code: string;
  name: string;
  calculation_type: string;
  required_objects: string[];
  formula?: string;
  category?: string;
}

interface Simulation {
  simulation_id: string;
  name: string;
  status: string;
  scenario: string;
  time_acceleration: {
    real_interval_seconds: number;
    simulated_interval_hours: number;
    acceleration_factor: number;
  };
  entity_counts: Record<string, number>;
  ticks_completed: number;
  current_simulated_time: string | null;
  started_at: string | null;
}

interface SimulationTick {
  tick_number: number;
  simulated_time: string;
  real_time: string;
  entity_counts: Record<string, number>;
  events: any[];
}

export default function SimulationPage() {
  // KPI Selection
  const [availableKPIs, setAvailableKPIs] = useState<KPIInfo[]>([]);
  const [selectedKPIs, setSelectedKPIs] = useState<KPIInfo[]>([]);
  const [loadingKPIs, setLoadingKPIs] = useState(false);
  
  // Simulation Configuration
  const [simulationName, setSimulationName] = useState('');
  const [selectedScenario, setSelectedScenario] = useState('healthy');
  const [realIntervalSeconds, setRealIntervalSeconds] = useState(10);
  const [simulatedIntervalHours, setSimulatedIntervalHours] = useState(1);
  const [autoStart, setAutoStart] = useState(true);
  
  // Active Simulations
  const [simulations, setSimulations] = useState<Simulation[]>([]);
  const [expandedSimulation, setExpandedSimulation] = useState<string | null>(null);
  const [simulationTicks, setSimulationTicks] = useState<Record<string, SimulationTick[]>>({});
  
  // UI State
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Fetch available KPIs on mount
  useEffect(() => {
    fetchAvailableKPIs();
    fetchSimulations();
    
    // Poll for simulation updates every 5 seconds
    const interval = setInterval(fetchSimulations, 5000);
    return () => clearInterval(interval);
  }, []);

  const fetchAvailableKPIs = async () => {
    setLoadingKPIs(true);
    try {
      const response = await fetch(`${API_BASE}/kpis`);
      if (response.ok) {
        const kpis = await response.json();
        setAvailableKPIs(kpis);
      }
    } catch (e) {
      console.error('Failed to fetch KPIs:', e);
    } finally {
      setLoadingKPIs(false);
    }
  };

  const fetchSimulations = async () => {
    try {
      const response = await fetch(`${API_BASE}/simulations`);
      if (response.ok) {
        const sims = await response.json();
        setSimulations(sims);
      }
    } catch (e) {
      console.error('Failed to fetch simulations:', e);
    }
  };

  const fetchSimulationTicks = async (simulationId: string) => {
    try {
      const response = await fetch(`${API_BASE}/simulations/${simulationId}/ticks?limit=20`);
      if (response.ok) {
        const data = await response.json();
        setSimulationTicks(prev => ({
          ...prev,
          [simulationId]: data.ticks,
        }));
      }
    } catch (e) {
      console.error('Failed to fetch ticks:', e);
    }
  };

  const handleCreateSimulation = async () => {
    if (selectedKPIs.length === 0) {
      setError('Please select at least one KPI');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await fetch(`${API_BASE}/simulations`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: simulationName || `Simulation - ${selectedKPIs.map(k => k.code).join(', ')}`,
          kpi_codes: selectedKPIs.map(k => k.code),
          scenario: selectedScenario,
          real_interval_seconds: realIntervalSeconds,
          simulated_interval_hours: simulatedIntervalHours,
          auto_start: autoStart,
        }),
      });

      if (response.ok) {
        await fetchSimulations();
        setSelectedKPIs([]);
        setSimulationName('');
      } else {
        const err = await response.json();
        setError(err.detail || 'Failed to create simulation');
      }
    } catch (e) {
      setError('Failed to connect to simulator service');
    } finally {
      setLoading(false);
    }
  };

  const handleStartSimulation = async (simulationId: string) => {
    try {
      await fetch(`${API_BASE}/simulations/${simulationId}/start`, { method: 'POST' });
      await fetchSimulations();
    } catch (e) {
      console.error('Failed to start simulation:', e);
    }
  };

  const handlePauseSimulation = async (simulationId: string) => {
    try {
      await fetch(`${API_BASE}/simulations/${simulationId}/pause`, { method: 'POST' });
      await fetchSimulations();
    } catch (e) {
      console.error('Failed to pause simulation:', e);
    }
  };

  const handleResumeSimulation = async (simulationId: string) => {
    try {
      await fetch(`${API_BASE}/simulations/${simulationId}/resume`, { method: 'POST' });
      await fetchSimulations();
    } catch (e) {
      console.error('Failed to resume simulation:', e);
    }
  };

  const handleStopSimulation = async (simulationId: string) => {
    try {
      await fetch(`${API_BASE}/simulations/${simulationId}/stop`, { method: 'POST' });
      await fetchSimulations();
    } catch (e) {
      console.error('Failed to stop simulation:', e);
    }
  };

  const handleDeleteSimulation = async (simulationId: string) => {
    try {
      await fetch(`${API_BASE}/simulations/${simulationId}`, { method: 'DELETE' });
      await fetchSimulations();
    } catch (e) {
      console.error('Failed to delete simulation:', e);
    }
  };

  const toggleExpanded = (simulationId: string) => {
    if (expandedSimulation === simulationId) {
      setExpandedSimulation(null);
    } else {
      setExpandedSimulation(simulationId);
      fetchSimulationTicks(simulationId);
    }
  };

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'running': return <RunningIcon className="spin" color="primary" />;
      case 'completed': return <SuccessIcon color="success" />;
      case 'paused': return <PauseIcon color="warning" />;
      case 'stopped': return <StopIcon color="error" />;
      default: return <CloudIcon color="disabled" />;
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'running': return 'primary';
      case 'completed': return 'success';
      case 'paused': return 'warning';
      case 'stopped': return 'error';
      default: return 'default';
    }
  };

  // Calculate acceleration display
  const accelerationFactor = (simulatedIntervalHours * 3600) / realIntervalSeconds;
  const getAccelerationText = () => {
    if (accelerationFactor >= 24) {
      return `${(accelerationFactor / 24).toFixed(1)} days/minute`;
    }
    return `${accelerationFactor.toFixed(1)} hours/minute`;
  };

  // Get unique entities from selected KPIs
  const selectedEntities = [...new Set(selectedKPIs.flatMap(k => k.required_objects))];

  return (
    <Box>
      <Box sx={{ mb: 3 }}>
        <Typography variant="h4" gutterBottom>
          KPI Data Simulator
        </Typography>
        <Typography variant="body1" color="text.secondary">
          Generate realistic demo data for selected KPIs with configurable time acceleration.
        </Typography>
      </Box>

      {error && (
        <Alert severity="error" sx={{ mb: 3 }} onClose={() => setError(null)}>
          {error}
        </Alert>
      )}

      <Grid container spacing={3}>
        {/* Configuration Panel */}
        <Grid item xs={12} md={5}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                New Simulation
              </Typography>
              
              <Stack spacing={3} sx={{ mt: 2 }}>
                {/* KPI Selection */}
                <Autocomplete
                  multiple
                  options={availableKPIs}
                  getOptionLabel={(option) => `${option.name} (${option.code})`}
                  value={selectedKPIs}
                  onChange={(_, newValue) => setSelectedKPIs(newValue)}
                  loading={loadingKPIs}
                  renderInput={(params) => (
                    <TextField
                      {...params}
                      label="Select KPIs"
                      placeholder="Search KPIs..."
                      helperText="Select KPIs to generate data for"
                    />
                  )}
                  renderOption={(props, option) => (
                    <li {...props}>
                      <Box sx={{ display: 'flex', flexDirection: 'column' }}>
                        <Typography variant="body2">{option.name}</Typography>
                        <Typography variant="caption" color="text.secondary">
                          {option.code} • {option.calculation_type} • {option.required_objects.length} entities
                        </Typography>
                      </Box>
                    </li>
                  )}
                  renderTags={(value, getTagProps) =>
                    value.map((option, index) => (
                      <Chip
                        {...getTagProps({ index })}
                        key={option.code}
                        label={option.code}
                        size="small"
                        color={option.calculation_type === 'set_based' ? 'primary' : 'default'}
                      />
                    ))
                  }
                />

                {/* Selected Entities Display */}
                {selectedEntities.length > 0 && (
                  <Paper variant="outlined" sx={{ p: 2, bgcolor: 'grey.50' }}>
                    <Typography variant="subtitle2" sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
                      <EntityIcon fontSize="small" /> Required Entities
                    </Typography>
                    <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
                      {selectedEntities.map(entity => (
                        <Chip key={entity} label={entity} size="small" variant="outlined" />
                      ))}
                    </Box>
                  </Paper>
                )}

                <TextField
                  label="Simulation Name"
                  value={simulationName}
                  onChange={(e) => setSimulationName(e.target.value)}
                  placeholder="Auto-generated if empty"
                  fullWidth
                />

                {/* Scenario Selection */}
                <FormControl fullWidth>
                  <InputLabel>Scenario</InputLabel>
                  <Select
                    value={selectedScenario}
                    label="Scenario"
                    onChange={(e) => setSelectedScenario(e.target.value)}
                  >
                    {SCENARIOS.map((s) => (
                      <MenuItem key={s.id} value={s.id}>
                        <Box>
                          <Typography variant="body2">{s.name}</Typography>
                          <Typography variant="caption" color="text.secondary">{s.description}</Typography>
                        </Box>
                      </MenuItem>
                    ))}
                  </Select>
                </FormControl>

                <Divider />

                {/* Time Acceleration Settings */}
                <Typography variant="subtitle2" sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  <SpeedIcon fontSize="small" /> Time Acceleration
                </Typography>

                <Box>
                  <Typography variant="body2" gutterBottom>
                    Real-time Interval: {realIntervalSeconds} seconds
                  </Typography>
                  <Slider
                    value={realIntervalSeconds}
                    onChange={(_, value) => setRealIntervalSeconds(value as number)}
                    min={1}
                    max={60}
                    step={1}
                    marks={[
                      { value: 1, label: '1s' },
                      { value: 10, label: '10s' },
                      { value: 30, label: '30s' },
                      { value: 60, label: '60s' },
                    ]}
                  />
                </Box>

                <Box>
                  <Typography variant="body2" gutterBottom>
                    Simulated Time per Interval: {simulatedIntervalHours} hour(s)
                  </Typography>
                  <Slider
                    value={simulatedIntervalHours}
                    onChange={(_, value) => setSimulatedIntervalHours(value as number)}
                    min={0.5}
                    max={24}
                    step={0.5}
                    marks={[
                      { value: 1, label: '1h' },
                      { value: 6, label: '6h' },
                      { value: 12, label: '12h' },
                      { value: 24, label: '24h' },
                    ]}
                  />
                </Box>

                <Paper variant="outlined" sx={{ p: 2, bgcolor: 'primary.50' }}>
                  <Typography variant="body2" color="primary.main">
                    <strong>Acceleration:</strong> {getAccelerationText()} of real time
                  </Typography>
                  <Typography variant="caption" color="text.secondary">
                    Every {realIntervalSeconds}s = {simulatedIntervalHours}h simulated
                  </Typography>
                </Paper>

                <FormControlLabel
                  control={
                    <Switch
                      checked={autoStart}
                      onChange={(e) => setAutoStart(e.target.checked)}
                    />
                  }
                  label="Auto-start simulation"
                />

                <Button
                  variant="contained"
                  size="large"
                  startIcon={loading ? <CircularProgress size={20} color="inherit" /> : <RunIcon />}
                  onClick={handleCreateSimulation}
                  disabled={selectedKPIs.length === 0 || loading}
                  fullWidth
                >
                  {loading ? 'Creating...' : 'Create Simulation'}
                </Button>
              </Stack>
            </CardContent>
          </Card>
        </Grid>

        {/* Active Simulations */}
        <Grid item xs={12} md={7}>
          <Card sx={{ height: '100%' }}>
            <CardContent>
              <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
                <Typography variant="h6" sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  <GraphIcon /> Active Simulations
                </Typography>
                <IconButton onClick={fetchSimulations} size="small">
                  <RefreshIcon />
                </IconButton>
              </Box>
              
              {simulations.length === 0 ? (
                <Box sx={{ textAlign: 'center', py: 5, color: 'text.disabled' }}>
                  <CloudIcon sx={{ fontSize: 60, mb: 1 }} />
                  <Typography>No active simulations</Typography>
                  <Typography variant="caption">Create a simulation to get started</Typography>
                </Box>
              ) : (
                <List disablePadding>
                  {simulations.map((sim) => (
                    <Paper key={sim.simulation_id} variant="outlined" sx={{ mb: 2 }}>
                      <ListItem
                        secondaryAction={
                          <Stack direction="row" spacing={1}>
                            {sim.status === 'pending' && (
                              <Tooltip title="Start">
                                <IconButton onClick={() => handleStartSimulation(sim.simulation_id)} color="primary">
                                  <RunIcon />
                                </IconButton>
                              </Tooltip>
                            )}
                            {sim.status === 'running' && (
                              <Tooltip title="Pause">
                                <IconButton onClick={() => handlePauseSimulation(sim.simulation_id)} color="warning">
                                  <PauseIcon />
                                </IconButton>
                              </Tooltip>
                            )}
                            {sim.status === 'paused' && (
                              <Tooltip title="Resume">
                                <IconButton onClick={() => handleResumeSimulation(sim.simulation_id)} color="primary">
                                  <ResumeIcon />
                                </IconButton>
                              </Tooltip>
                            )}
                            {(sim.status === 'running' || sim.status === 'paused') && (
                              <Tooltip title="Stop">
                                <IconButton onClick={() => handleStopSimulation(sim.simulation_id)} color="error">
                                  <StopIcon />
                                </IconButton>
                              </Tooltip>
                            )}
                            <Tooltip title="Delete">
                              <IconButton onClick={() => handleDeleteSimulation(sim.simulation_id)} color="error">
                                <DeleteIcon />
                              </IconButton>
                            </Tooltip>
                            <IconButton onClick={() => toggleExpanded(sim.simulation_id)}>
                              {expandedSimulation === sim.simulation_id ? <CollapseIcon /> : <ExpandIcon />}
                            </IconButton>
                          </Stack>
                        }
                      >
                        <ListItemIcon>
                          {getStatusIcon(sim.status)}
                        </ListItemIcon>
                        <ListItemText
                          primary={sim.name}
                          secondary={
                            <Box sx={{ mt: 0.5 }}>
                              <Stack direction="row" spacing={1} sx={{ mb: 0.5 }}>
                                <Chip
                                  size="small"
                                  label={sim.status}
                                  color={getStatusColor(sim.status) as any}
                                />
                                <Chip
                                  size="small"
                                  label={sim.scenario}
                                  variant="outlined"
                                />
                                <Chip
                                  size="small"
                                  icon={<SpeedIcon />}
                                  label={`${sim.time_acceleration.acceleration_factor.toFixed(0)}x`}
                                  variant="outlined"
                                />
                              </Stack>
                              <Typography variant="caption" color="text.secondary">
                                Ticks: {sim.ticks_completed} • 
                                Entities: {Object.entries(sim.entity_counts).map(([k, v]) => `${k}: ${v}`).join(', ')}
                              </Typography>
                            </Box>
                          }
                        />
                      </ListItem>
                      
                      <Collapse in={expandedSimulation === sim.simulation_id}>
                        <Box sx={{ p: 2, bgcolor: 'grey.50' }}>
                          <Typography variant="subtitle2" gutterBottom>Recent Ticks</Typography>
                          {simulationTicks[sim.simulation_id]?.length > 0 ? (
                            <Table size="small">
                              <TableHead>
                                <TableRow>
                                  <TableCell>Tick</TableCell>
                                  <TableCell>Simulated Time</TableCell>
                                  <TableCell>Events</TableCell>
                                  <TableCell>Entity Counts</TableCell>
                                </TableRow>
                              </TableHead>
                              <TableBody>
                                {simulationTicks[sim.simulation_id].slice(-5).map((tick) => (
                                  <TableRow key={tick.tick_number}>
                                    <TableCell>{tick.tick_number}</TableCell>
                                    <TableCell>
                                      {new Date(tick.simulated_time).toLocaleString()}
                                    </TableCell>
                                    <TableCell>{tick.events?.length || 0}</TableCell>
                                    <TableCell>
                                      {Object.entries(tick.entity_counts)
                                        .filter(([k]) => !k.includes('_'))
                                        .map(([k, v]) => `${k}: ${v}`)
                                        .join(', ')}
                                    </TableCell>
                                  </TableRow>
                                ))}
                              </TableBody>
                            </Table>
                          ) : (
                            <Typography variant="body2" color="text.secondary">
                              No ticks recorded yet
                            </Typography>
                          )}
                        </Box>
                      </Collapse>
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
