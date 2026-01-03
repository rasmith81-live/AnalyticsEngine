import { useState, useEffect, useCallback } from 'react';
import {
  Box,
  Typography,
  Paper,
  Grid,
  Card,
  CardContent,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Chip,
  Stack,
  Alert,
  Divider,
  IconButton,
  Tooltip,
  ToggleButton,
  ToggleButtonGroup,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
} from '@mui/material';
import {
  TrendingUp as TrendingUpIcon,
  TrendingDown as TrendingDownIcon,
  TrendingFlat as TrendingFlatIcon,
  Refresh as RefreshIcon,
  Timeline as TimelineIcon,
  BarChart as BarChartIcon,
  ShowChart as LineChartIcon,
  People as PeopleIcon,
  Analytics as AnalyticsIcon,
  PlayCircle as ActiveIcon,
  PauseCircle as PausedIcon,
  ZoomIn as ZoomInIcon,
  ZoomOut as ZoomOutIcon,
} from '@mui/icons-material';
import {
  LineChart,
  Line,
  AreaChart,
  Area,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip as RechartsTooltip,
  Legend,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
} from 'recharts';

const API_BASE = '/api/v1/simulator';

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
  metrics: Record<string, number>;
}

interface KPICardData {
  code: string;
  name: string;
  value: number;
  previousValue: number;
  trend: 'up' | 'down' | 'flat';
  changePercent: number;
  unit: string;
  color: string;
  history: { time: string; value: number }[];
}

const KPI_COLORS = [
  '#2196F3', '#4CAF50', '#FF9800', '#E91E63', '#9C27B0',
  '#00BCD4', '#FF5722', '#795548', '#607D8B', '#3F51B5',
];

const KPI_UNITS: Record<string, string> = {
  WIN_RATE: '%',
  CONVERSION_RATE: '%',
  CHURN_RATE: '%',
  RETENTION_RATE: '%',
  MRR: '$',
  ARR: '$',
  CLV: '$',
  REVENUE: '$',
  AVG_ORDER_VALUE: '$',
  MQL_COUNT: '',
};

const KPI_NAMES: Record<string, string> = {
  WIN_RATE: 'Win Rate',
  CONVERSION_RATE: 'Conversion Rate',
  CHURN_RATE: 'Churn Rate',
  RETENTION_RATE: 'Retention Rate',
  MRR: 'Monthly Recurring Revenue',
  ARR: 'Annual Recurring Revenue',
  CLV: 'Customer Lifetime Value',
  REVENUE: 'Total Revenue',
  AVG_ORDER_VALUE: 'Average Order Value',
  MQL_COUNT: 'Marketing Qualified Leads',
};

export default function AnalyticsDemoPage() {
  const [simulations, setSimulations] = useState<Simulation[]>([]);
  const [selectedSimulation, setSelectedSimulation] = useState<string>('');
  const [tickHistory, setTickHistory] = useState<SimulationTick[]>([]);
  const [kpiCards, setKpiCards] = useState<KPICardData[]>([]);
  const [chartType, setChartType] = useState<'line' | 'area' | 'bar'>('area');
  const [refreshInterval] = useState(2000);
  const [zoomLevel, setZoomLevel] = useState(50);

  const fetchSimulations = useCallback(async () => {
    try {
      const response = await fetch(`${API_BASE}/simulations`);
      if (response.ok) {
        const data = await response.json();
        setSimulations(data.filter((s: Simulation) => s.status === 'running' || s.status === 'paused'));
      }
    } catch (err) {
      console.error('Failed to fetch simulations:', err);
    }
  }, []);

  const fetchTickHistory = useCallback(async () => {
    if (!selectedSimulation) return;
    
    try {
      const response = await fetch(`${API_BASE}/simulations/${selectedSimulation}/ticks?limit=50`);
      if (response.ok) {
        const data = await response.json();
        setTickHistory(data.ticks || []);
      }
    } catch (err) {
      console.error('Failed to fetch ticks:', err);
    }
  }, [selectedSimulation]);

  useEffect(() => {
    if (tickHistory.length === 0) {
      setKpiCards([]);
      return;
    }

    const latestTick = tickHistory[tickHistory.length - 1];
    const previousTick = tickHistory.length > 1 ? tickHistory[tickHistory.length - 2] : null;
    
    const cards: KPICardData[] = Object.entries(latestTick.metrics).map(([code, value], index) => {
      const prevValue = previousTick?.metrics[code] ?? value;
      const change = value - prevValue;
      const changePercent = prevValue !== 0 ? (change / prevValue) * 100 : 0;
      
      const history = tickHistory.map(tick => ({
        time: new Date(tick.simulated_time).toLocaleTimeString(),
        value: tick.metrics[code] ?? 0,
      }));

      return {
        code,
        name: KPI_NAMES[code] || code,
        value,
        previousValue: prevValue,
        trend: change > 0.01 ? 'up' : change < -0.01 ? 'down' : 'flat',
        changePercent,
        unit: KPI_UNITS[code] || '',
        color: KPI_COLORS[index % KPI_COLORS.length],
        history,
      };
    });

    setKpiCards(cards);
  }, [tickHistory]);

  useEffect(() => {
    fetchSimulations();
    const simInterval = setInterval(fetchSimulations, 5000);
    return () => clearInterval(simInterval);
  }, [fetchSimulations]);

  useEffect(() => {
    if (!selectedSimulation) return;
    
    fetchTickHistory();
    const tickInterval = setInterval(fetchTickHistory, refreshInterval);
    return () => clearInterval(tickInterval);
  }, [selectedSimulation, fetchTickHistory, refreshInterval]);

  useEffect(() => {
    if (!selectedSimulation && simulations.length > 0) {
      const running = simulations.find(s => s.status === 'running');
      if (running) {
        setSelectedSimulation(running.simulation_id);
      }
    }
  }, [simulations, selectedSimulation]);

  const selectedSim = simulations.find(s => s.simulation_id === selectedSimulation);
  const latestTick = tickHistory[tickHistory.length - 1];

  const formatValue = (value: number, unit: string) => {
    if (unit === '$') {
      return value >= 1000000 
        ? `$${(value / 1000000).toFixed(2)}M`
        : value >= 1000 
          ? `$${(value / 1000).toFixed(1)}K`
          : `$${value.toFixed(2)}`;
    }
    if (unit === '%') {
      return `${value.toFixed(1)}%`;
    }
    return value >= 1000 ? `${(value / 1000).toFixed(1)}K` : value.toFixed(0);
  };

  const getTrendIcon = (trend: 'up' | 'down' | 'flat') => {
    switch (trend) {
      case 'up': return <TrendingUpIcon sx={{ color: 'success.main' }} />;
      case 'down': return <TrendingDownIcon sx={{ color: 'error.main' }} />;
      default: return <TrendingFlatIcon sx={{ color: 'text.secondary' }} />;
    }
  };

  const zoomedTickHistory = tickHistory.slice(-zoomLevel);
  
  const chartData = zoomedTickHistory.map(tick => {
    const dataPoint: Record<string, any> = {
      time: new Date(tick.simulated_time).toLocaleTimeString(),
      tick: tick.tick_number,
    };
    Object.entries(tick.metrics).forEach(([code, value]) => {
      dataPoint[code] = value;
    });
    return dataPoint;
  });

  const handleZoomIn = () => {
    setZoomLevel(prev => Math.max(5, Math.floor(prev / 2)));
  };

  const handleZoomOut = () => {
    setZoomLevel(prev => Math.min(tickHistory.length, prev * 2));
  };

  const entityData = latestTick ? Object.entries(latestTick.entity_counts)
    .filter(([key]) => !key.includes('_churned') && !key.includes('_new'))
    .map(([name, value], index) => ({
      name: name.charAt(0).toUpperCase() + name.slice(1),
      value,
      color: KPI_COLORS[index % KPI_COLORS.length],
    })) : [];

  return (
    <Box sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
        <Typography variant="h4">
          <AnalyticsIcon sx={{ mr: 1, verticalAlign: 'middle' }} />
          Analytics Demo Dashboard
        </Typography>
        <Stack direction="row" spacing={2} alignItems="center">
          <FormControl size="small" sx={{ minWidth: 300 }}>
            <InputLabel>Active Simulation</InputLabel>
            <Select
              value={selectedSimulation}
              label="Active Simulation"
              onChange={(e) => setSelectedSimulation(e.target.value)}
            >
              {simulations.length === 0 && (
                <MenuItem value="" disabled>No active simulations</MenuItem>
              )}
              {simulations.map((sim) => (
                <MenuItem key={sim.simulation_id} value={sim.simulation_id}>
                  <Stack direction="row" spacing={1} alignItems="center">
                    {sim.status === 'running' ? (
                      <ActiveIcon fontSize="small" color="success" />
                    ) : (
                      <PausedIcon fontSize="small" color="warning" />
                    )}
                    <span>{sim.name}</span>
                    <Chip size="small" label={`${sim.ticks_completed} ticks`} />
                  </Stack>
                </MenuItem>
              ))}
            </Select>
          </FormControl>
          <Tooltip title="Refresh">
            <IconButton onClick={fetchTickHistory}>
              <RefreshIcon />
            </IconButton>
          </Tooltip>
        </Stack>
      </Box>

      {!selectedSimulation && (
        <Alert severity="info" sx={{ mb: 2 }}>
          No active simulation selected. Start a simulation from the Simulation Controller page to see live analytics.
        </Alert>
      )}

      {selectedSimulation && selectedSim && (
        <>
          <Paper sx={{ p: 2, mb: 2 }}>
            <Stack direction="row" spacing={3} alignItems="center" flexWrap="wrap">
              <Chip 
                icon={selectedSim.status === 'running' ? <ActiveIcon /> : <PausedIcon />}
                label={selectedSim.status.toUpperCase()}
                color={selectedSim.status === 'running' ? 'success' : 'warning'}
              />
              <Typography variant="body2">
                <strong>Scenario:</strong> {selectedSim.scenario}
              </Typography>
              <Typography variant="body2">
                <strong>Simulated Time:</strong> {latestTick ? new Date(latestTick.simulated_time).toLocaleString() : 'N/A'}
              </Typography>
              <Typography variant="body2">
                <strong>Ticks:</strong> {selectedSim.ticks_completed}
              </Typography>
              <Typography variant="body2">
                <strong>Speed:</strong> {selectedSim.time_acceleration.acceleration_factor}x
              </Typography>
            </Stack>
          </Paper>

          {kpiCards.length > 0 ? (
            <Grid container spacing={2} sx={{ mb: 3 }}>
              {kpiCards.map((kpi) => (
                <Grid item xs={12} sm={6} md={4} lg={3} key={kpi.code}>
                  <Card sx={{ height: '100%', borderLeft: `4px solid ${kpi.color}` }}>
                    <CardContent>
                      <Stack direction="row" justifyContent="space-between" alignItems="flex-start">
                        <Box>
                          <Typography variant="caption" color="text.secondary" gutterBottom>
                            {kpi.name}
                          </Typography>
                          <Typography variant="h4" sx={{ fontWeight: 'bold', color: kpi.color }}>
                            {formatValue(kpi.value, kpi.unit)}
                          </Typography>
                        </Box>
                        {getTrendIcon(kpi.trend)}
                      </Stack>
                      <Stack direction="row" spacing={1} alignItems="center" sx={{ mt: 1 }}>
                        <Typography 
                          variant="body2" 
                          sx={{ 
                            color: kpi.trend === 'up' ? 'success.main' : kpi.trend === 'down' ? 'error.main' : 'text.secondary' 
                          }}
                        >
                          {kpi.changePercent >= 0 ? '+' : ''}{kpi.changePercent.toFixed(2)}%
                        </Typography>
                        <Typography variant="caption" color="text.secondary">
                          vs previous tick
                        </Typography>
                      </Stack>
                      <Box sx={{ height: 40, mt: 1 }}>
                        <ResponsiveContainer width="100%" height="100%">
                          <AreaChart data={kpi.history.slice(-10)}>
                            <Area 
                              type="monotone" 
                              dataKey="value" 
                              stroke={kpi.color} 
                              fill={kpi.color} 
                              fillOpacity={0.2}
                              strokeWidth={2}
                            />
                          </AreaChart>
                        </ResponsiveContainer>
                      </Box>
                    </CardContent>
                  </Card>
                </Grid>
              ))}
            </Grid>
          ) : (
            <Alert severity="info" sx={{ mb: 2 }}>
              Waiting for KPI data... Make sure the simulation is running.
            </Alert>
          )}

          <Grid container spacing={2}>
            <Grid item xs={12} lg={8}>
              <Paper sx={{ p: 2, height: 400 }}>
                <Stack direction="row" justifyContent="space-between" alignItems="center" sx={{ mb: 2 }}>
                  <Typography variant="h6">
                    <TimelineIcon sx={{ mr: 1, verticalAlign: 'middle' }} />
                    KPI Trends Over Time
                  </Typography>
                  <Stack direction="row" spacing={1} alignItems="center">
                    <Tooltip title="Zoom In (fewer data points)">
                      <IconButton size="small" onClick={handleZoomIn} disabled={zoomLevel <= 5}>
                        <ZoomInIcon fontSize="small" />
                      </IconButton>
                    </Tooltip>
                    <Tooltip title="Zoom Out (more data points)">
                      <IconButton size="small" onClick={handleZoomOut} disabled={zoomLevel >= tickHistory.length}>
                        <ZoomOutIcon fontSize="small" />
                      </IconButton>
                    </Tooltip>
                    <Chip size="small" label={`${Math.min(zoomLevel, tickHistory.length)} pts`} />
                    <Divider orientation="vertical" flexItem sx={{ mx: 1 }} />
                    <ToggleButtonGroup
                      value={chartType}
                      exclusive
                      onChange={(_, value) => value && setChartType(value)}
                      size="small"
                    >
                      <ToggleButton value="line">
                        <LineChartIcon fontSize="small" />
                      </ToggleButton>
                      <ToggleButton value="area">
                        <BarChartIcon fontSize="small" />
                      </ToggleButton>
                      <ToggleButton value="bar">
                        <BarChartIcon fontSize="small" />
                      </ToggleButton>
                    </ToggleButtonGroup>
                  </Stack>
                </Stack>
                <ResponsiveContainer width="100%" height="85%">
                  {chartType === 'line' ? (
                    <LineChart data={chartData}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="time" tick={{ fontSize: 10 }} />
                      <YAxis />
                      <RechartsTooltip />
                      <Legend />
                      {kpiCards.map((kpi) => (
                        <Line
                          key={kpi.code}
                          type="monotone"
                          dataKey={kpi.code}
                          name={kpi.name}
                          stroke={kpi.color}
                          strokeWidth={2}
                          dot={false}
                        />
                      ))}
                    </LineChart>
                  ) : chartType === 'area' ? (
                    <AreaChart data={chartData}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="time" tick={{ fontSize: 10 }} />
                      <YAxis />
                      <RechartsTooltip />
                      <Legend />
                      {kpiCards.map((kpi) => (
                        <Area
                          key={kpi.code}
                          type="monotone"
                          dataKey={kpi.code}
                          name={kpi.name}
                          stroke={kpi.color}
                          fill={kpi.color}
                          fillOpacity={0.3}
                        />
                      ))}
                    </AreaChart>
                  ) : (
                    <BarChart data={chartData}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="time" tick={{ fontSize: 10 }} />
                      <YAxis />
                      <RechartsTooltip />
                      <Legend />
                      {kpiCards.map((kpi) => (
                        <Bar
                          key={kpi.code}
                          dataKey={kpi.code}
                          name={kpi.name}
                          fill={kpi.color}
                        />
                      ))}
                    </BarChart>
                  )}
                </ResponsiveContainer>
              </Paper>
            </Grid>

            <Grid item xs={12} lg={4}>
              <Paper sx={{ p: 2, height: 400 }}>
                <Typography variant="h6" sx={{ mb: 2 }}>
                  <PeopleIcon sx={{ mr: 1, verticalAlign: 'middle' }} />
                  Entity Distribution
                </Typography>
                {entityData.length > 0 ? (
                  <>
                    <ResponsiveContainer width="100%" height="60%">
                      <PieChart>
                        <Pie
                          data={entityData}
                          cx="50%"
                          cy="50%"
                          innerRadius={40}
                          outerRadius={80}
                          paddingAngle={2}
                          dataKey="value"
                          label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                          labelLine={false}
                        >
                          {entityData.map((entry, index) => (
                            <Cell key={`cell-${index}`} fill={entry.color} />
                          ))}
                        </Pie>
                        <RechartsTooltip />
                      </PieChart>
                    </ResponsiveContainer>
                    <Divider sx={{ my: 1 }} />
                    <Stack spacing={0.5}>
                      {entityData.map((entity) => (
                        <Stack key={entity.name} direction="row" justifyContent="space-between">
                          <Stack direction="row" spacing={1} alignItems="center">
                            <Box sx={{ width: 12, height: 12, borderRadius: '50%', bgcolor: entity.color }} />
                            <Typography variant="body2">{entity.name}</Typography>
                          </Stack>
                          <Typography variant="body2" fontWeight="bold">
                            {entity.value.toLocaleString()}
                          </Typography>
                        </Stack>
                      ))}
                    </Stack>
                  </>
                ) : (
                  <Typography color="text.secondary">No entity data available</Typography>
                )}
              </Paper>
            </Grid>

            <Grid item xs={12}>
              <Paper sx={{ p: 2 }}>
                <Typography variant="h6" sx={{ mb: 2 }}>
                  Entity Activity Summary
                </Typography>
                {latestTick && (
                  <Table size="small">
                    <TableHead>
                      <TableRow>
                        <TableCell>Entity Type</TableCell>
                        <TableCell align="right">Active Count</TableCell>
                        <TableCell align="right">New (This Tick)</TableCell>
                        <TableCell align="right">Churned (This Tick)</TableCell>
                        <TableCell align="right">Net Change</TableCell>
                      </TableRow>
                    </TableHead>
                    <TableBody>
                      {Object.entries(latestTick.entity_counts)
                        .filter(([key]) => !key.includes('_churned') && !key.includes('_new'))
                        .map(([entityName, count]) => {
                          const newCount = latestTick.entity_counts[`${entityName}_new`] || 0;
                          const churnedCount = latestTick.entity_counts[`${entityName}_churned`] || 0;
                          const netChange = newCount - churnedCount;
                          return (
                            <TableRow key={entityName}>
                              <TableCell>
                                <Stack direction="row" spacing={1} alignItems="center">
                                  <PeopleIcon fontSize="small" color="primary" />
                                  <Typography>{entityName.charAt(0).toUpperCase() + entityName.slice(1)}</Typography>
                                </Stack>
                              </TableCell>
                              <TableCell align="right">
                                <Typography fontWeight="bold">{count.toLocaleString()}</Typography>
                              </TableCell>
                              <TableCell align="right">
                                <Chip 
                                  size="small" 
                                  label={`+${newCount}`} 
                                  color="success" 
                                  variant={newCount > 0 ? 'filled' : 'outlined'}
                                />
                              </TableCell>
                              <TableCell align="right">
                                <Chip 
                                  size="small" 
                                  label={`-${churnedCount}`} 
                                  color="error" 
                                  variant={churnedCount > 0 ? 'filled' : 'outlined'}
                                />
                              </TableCell>
                              <TableCell align="right">
                                <Typography 
                                  fontWeight="bold"
                                  color={netChange > 0 ? 'success.main' : netChange < 0 ? 'error.main' : 'text.secondary'}
                                >
                                  {netChange >= 0 ? '+' : ''}{netChange}
                                </Typography>
                              </TableCell>
                            </TableRow>
                          );
                        })}
                    </TableBody>
                  </Table>
                )}
              </Paper>
            </Grid>
          </Grid>
        </>
      )}
    </Box>
  );
}
