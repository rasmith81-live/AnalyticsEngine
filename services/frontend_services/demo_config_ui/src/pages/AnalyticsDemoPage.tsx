import { useState, useEffect, useCallback } from 'react';
import {
  TrendingUp,
  TrendingDown,
  Minus,
  RefreshCw,
  BarChart3,
  Users,
  PlayCircle,
  PauseCircle,
  ZoomIn,
  ZoomOut,
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/Card';
import { cn } from '../lib/utils';
import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip as RechartsTooltip,
  ResponsiveContainer,
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
  '#7d44ee', '#00998a', '#F79767', '#DA7194', '#9C27B0',
  '#00BCD4', '#FF5722', '#795548', '#607D8B', '#3F51B5',
];

const KPI_UNITS: Record<string, string> = {
  WIN_RATE: '%', CONVERSION_RATE: '%', CHURN_RATE: '%', RETENTION_RATE: '%',
  MRR: '$', ARR: '$', CLV: '$', REVENUE: '$', AVG_ORDER_VALUE: '$', MQL_COUNT: '',
};

const KPI_NAMES: Record<string, string> = {
  WIN_RATE: 'Win Rate', CONVERSION_RATE: 'Conversion Rate', CHURN_RATE: 'Churn Rate',
  RETENTION_RATE: 'Retention Rate', MRR: 'Monthly Recurring Revenue', ARR: 'Annual Recurring Revenue',
  CLV: 'Customer Lifetime Value', REVENUE: 'Total Revenue', AVG_ORDER_VALUE: 'Average Order Value',
  MQL_COUNT: 'Marketing Qualified Leads',
};

const AGGREGATION_OPTIONS = [
  { value: 'raw', label: 'Raw' },
  { value: 'minute', label: 'Min' },
  { value: 'hour', label: 'Hour' },
  { value: 'day', label: 'Day' },
  { value: 'week', label: 'Week' },
  { value: 'month', label: 'Month' },
  { value: 'quarter', label: 'Qtr' },
];

export default function AnalyticsDemoPage() {
  const [simulations, setSimulations] = useState<Simulation[]>([]);
  const [selectedSimulation, setSelectedSimulation] = useState<string>('');
  const [tickHistory, setTickHistory] = useState<SimulationTick[]>([]);
  const [kpiCards, setKpiCards] = useState<KPICardData[]>([]);
  const [refreshInterval] = useState(2000);
  const [zoomLevel, setZoomLevel] = useState(50);
  const [aggregationPeriod, setAggregationPeriod] = useState<string>('raw');

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
    if (tickHistory.length === 0) { setKpiCards([]); return; }
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
        code, name: KPI_NAMES[code] || code, value, previousValue: prevValue,
        trend: change > 0.01 ? 'up' : change < -0.01 ? 'down' : 'flat',
        changePercent, unit: KPI_UNITS[code] || '', color: KPI_COLORS[index % KPI_COLORS.length], history,
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
      if (running) setSelectedSimulation(running.simulation_id);
    }
  }, [simulations, selectedSimulation]);

  const selectedSim = simulations.find(s => s.simulation_id === selectedSimulation);
  const latestTick = tickHistory[tickHistory.length - 1];

  const formatValue = (value: number, unit: string) => {
    if (unit === '$') {
      return value >= 1000000 ? `$${(value / 1000000).toFixed(2)}M` : value >= 1000 ? `$${(value / 1000).toFixed(1)}K` : `$${value.toFixed(2)}`;
    }
    if (unit === '%') return `${value.toFixed(1)}%`;
    return value >= 1000 ? `${(value / 1000).toFixed(1)}K` : value.toFixed(0);
  };

  const aggregateTickData = useCallback((ticks: SimulationTick[], period: string): SimulationTick[] => {
    if (period === 'raw' || ticks.length === 0) return ticks;
    const getGroupKey = (date: Date): string => {
      switch (period) {
        case 'minute': return `${date.getFullYear()}-${date.getMonth()}-${date.getDate()}-${date.getHours()}-${date.getMinutes()}`;
        case 'hour': return `${date.getFullYear()}-${date.getMonth()}-${date.getDate()}-${date.getHours()}`;
        case 'day': return `${date.getFullYear()}-${date.getMonth()}-${date.getDate()}`;
        case 'week': const ws = new Date(date); ws.setDate(date.getDate() - date.getDay()); return `${ws.getFullYear()}-${ws.getMonth()}-${ws.getDate()}`;
        case 'month': return `${date.getFullYear()}-${date.getMonth()}`;
        case 'quarter': return `${date.getFullYear()}-Q${Math.floor(date.getMonth() / 3)}`;
        default: return date.toISOString();
      }
    };
    const groups = new Map<string, SimulationTick[]>();
    ticks.forEach(tick => { const key = getGroupKey(new Date(tick.simulated_time)); if (!groups.has(key)) groups.set(key, []); groups.get(key)!.push(tick); });
    return Array.from(groups.entries()).map(([_, groupTicks]) => {
      const lastTick = groupTicks[groupTicks.length - 1];
      const aggregatedMetrics: Record<string, number> = {};
      Object.keys(groupTicks[0].metrics).forEach(key => { aggregatedMetrics[key] = groupTicks.map(t => t.metrics[key]).reduce((a, b) => a + b, 0) / groupTicks.length; });
      return { ...lastTick, metrics: aggregatedMetrics };
    });
  }, []);

  const aggregatedTickHistory = aggregateTickData(tickHistory, aggregationPeriod);
  const zoomedTickHistory = aggregatedTickHistory.slice(-zoomLevel);

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Header */}
      <div className="flex items-center justify-between flex-wrap gap-4">
        <div>
          <h1 className="text-3xl font-bold theme-text-title tracking-wide flex items-center gap-2">
            <BarChart3 className="w-8 h-8 theme-info-icon" />
            Live Dashboards
          </h1>
          <p className="theme-text-muted mt-1">Real-time KPI visualization from active simulations</p>
        </div>
        <div className="flex items-center gap-3">
          <select
            value={selectedSimulation}
            onChange={(e) => setSelectedSimulation(e.target.value)}
            className="px-4 py-2 rounded-xl theme-card-bg border theme-border theme-text min-w-[300px] focus:outline-none focus:ring-2 focus:ring-alpha-500"
          >
            {simulations.length === 0 && <option value="" disabled>No active simulations</option>}
            {simulations.map((sim) => (
              <option key={sim.simulation_id} value={sim.simulation_id}>
                {sim.status === 'running' ? '▶' : '⏸'} {sim.name} ({sim.ticks_completed} ticks)
              </option>
            ))}
          </select>
          <button onClick={fetchTickHistory} className="p-2 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 transition-colors">
            <RefreshCw className="w-5 h-5 theme-text-muted" />
          </button>
        </div>
      </div>

      {!selectedSimulation && (
        <div className="p-4 rounded-xl bg-blue-500/10 border border-blue-500/30 text-blue-400">
          No active simulation selected. Start a simulation from the Simulation page to see live analytics.
        </div>
      )}

      {selectedSimulation && selectedSim && (
        <>
          {/* Status Bar */}
          <Card>
            <CardContent className="p-4">
              <div className="flex items-center gap-4 flex-wrap">
                <span className={cn(
                  "flex items-center gap-1.5 px-3 py-1 rounded-full text-sm font-medium",
                  selectedSim.status === 'running' ? "bg-green-500/20 text-green-400" : "bg-amber-500/20 text-amber-400"
                )}>
                  {selectedSim.status === 'running' ? <PlayCircle className="w-4 h-4" /> : <PauseCircle className="w-4 h-4" />}
                  {selectedSim.status.toUpperCase()}
                </span>
                <span className="text-sm theme-text"><strong>Scenario:</strong> {selectedSim.scenario}</span>
                <span className="text-sm theme-text"><strong>Time:</strong> {latestTick ? new Date(latestTick.simulated_time).toLocaleString() : 'N/A'}</span>
                <span className="text-sm theme-text"><strong>Ticks:</strong> {selectedSim.ticks_completed}</span>
                <span className="text-sm theme-text"><strong>Speed:</strong> {selectedSim.time_acceleration.acceleration_factor}x</span>
                <div className="ml-auto flex items-center gap-2">
                  <span className="text-sm theme-text-muted">Aggregate:</span>
                  <div className="flex rounded-lg overflow-hidden border theme-border">
                    {AGGREGATION_OPTIONS.map((opt) => (
                      <button
                        key={opt.value}
                        onClick={() => setAggregationPeriod(opt.value)}
                        className={cn(
                          "px-2 py-1 text-xs font-medium transition-colors",
                          aggregationPeriod === opt.value ? "bg-alpha-500 text-white" : "theme-text-muted hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800"
                        )}
                      >
                        {opt.label}
                      </button>
                    ))}
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>

          {/* KPI Cards */}
          {kpiCards.length > 0 ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              {kpiCards.map((kpi) => (
                <Card key={kpi.code} className="overflow-hidden" style={{ borderLeftColor: kpi.color, borderLeftWidth: '4px' }}>
                  <CardContent className="p-4">
                    <div className="flex items-start justify-between">
                      <div>
                        <p className="text-xs theme-text-muted mb-1">{kpi.name}</p>
                        <p className="text-2xl font-bold" style={{ color: kpi.color }}>{formatValue(kpi.value, kpi.unit)}</p>
                      </div>
                      {kpi.trend === 'up' && <TrendingUp className="w-5 h-5 text-green-500" />}
                      {kpi.trend === 'down' && <TrendingDown className="w-5 h-5 text-red-500" />}
                      {kpi.trend === 'flat' && <Minus className="w-5 h-5 theme-text-muted" />}
                    </div>
                    <div className="flex items-center gap-2 mt-1">
                      <span className={cn("text-sm font-medium", kpi.trend === 'up' ? "text-green-500" : kpi.trend === 'down' ? "text-red-500" : "theme-text-muted")}>
                        {kpi.changePercent >= 0 ? '+' : ''}{kpi.changePercent.toFixed(2)}%
                      </span>
                      <span className="text-xs theme-text-muted">vs previous</span>
                    </div>
                    <div className="h-10 mt-2">
                      <ResponsiveContainer width="100%" height="100%">
                        <AreaChart data={kpi.history.slice(-10)}>
                          <Area type="monotone" dataKey="value" stroke={kpi.color} fill={kpi.color} fillOpacity={0.2} strokeWidth={2} />
                        </AreaChart>
                      </ResponsiveContainer>
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          ) : (
            <div className="p-4 rounded-xl bg-blue-500/10 border border-blue-500/30 text-blue-400">
              Waiting for KPI data... Make sure the simulation is running.
            </div>
          )}

          {/* Charts */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
            {kpiCards.map((kpi) => (
              <Card key={kpi.code}>
                <CardHeader>
                  <div className="flex items-center justify-between">
                    <CardTitle className="flex items-center gap-2" style={{ color: kpi.color }}>
                      <BarChart3 className="w-5 h-5" />
                      {kpi.name}
                    </CardTitle>
                    <div className="flex items-center gap-2">
                      <button onClick={() => setZoomLevel(prev => Math.max(5, Math.floor(prev / 2)))} disabled={zoomLevel <= 5} className="p-1 rounded hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 disabled:opacity-50">
                        <ZoomIn className="w-4 h-4 theme-text-muted" />
                      </button>
                      <button onClick={() => setZoomLevel(prev => Math.min(tickHistory.length, prev * 2))} disabled={zoomLevel >= tickHistory.length} className="p-1 rounded hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 disabled:opacity-50">
                        <ZoomOut className="w-4 h-4 theme-text-muted" />
                      </button>
                      <span className="text-xs theme-text-muted">{Math.min(zoomLevel, tickHistory.length)} pts</span>
                    </div>
                  </div>
                </CardHeader>
                <CardContent>
                  <div className="h-64">
                    <ResponsiveContainer width="100%" height="100%">
                      <AreaChart data={zoomedTickHistory.map(tick => ({ time: new Date(tick.simulated_time).toLocaleTimeString(), value: tick.metrics[kpi.code] ?? 0 }))}>
                        <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" />
                        <XAxis dataKey="time" tick={{ fontSize: 10, fill: 'var(--text-muted)' }} />
                        <YAxis domain={['auto', 'auto']} tick={{ fontSize: 10, fill: 'var(--text-muted)' }} tickFormatter={(value) => kpi.unit === '$' ? `$${value >= 1000 ? (value/1000).toFixed(0) + 'K' : value}` : kpi.unit === '%' ? `${value}%` : value} />
                        <RechartsTooltip formatter={(value: number) => [formatValue(value, kpi.unit), kpi.name]} contentStyle={{ backgroundColor: 'var(--card-background)', border: '1px solid var(--border)', borderRadius: '8px' }} />
                        <Area type="monotone" dataKey="value" name={kpi.name} stroke={kpi.color} fill={kpi.color} fillOpacity={0.3} strokeWidth={2} />
                      </AreaChart>
                    </ResponsiveContainer>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>

          {/* Entity Activity */}
          {latestTick && (
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Users className="w-5 h-5 theme-info-icon" />
                  Entity Activity Summary
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="overflow-x-auto">
                  <table className="w-full text-sm">
                    <thead>
                      <tr className="border-b theme-border">
                        <th className="px-4 py-2 text-left theme-text-muted font-medium">Entity Type</th>
                        <th className="px-4 py-2 text-right theme-text-muted font-medium">Active Count</th>
                        <th className="px-4 py-2 text-right theme-text-muted font-medium">New</th>
                        <th className="px-4 py-2 text-right theme-text-muted font-medium">Churned</th>
                        <th className="px-4 py-2 text-right theme-text-muted font-medium">Net Change</th>
                      </tr>
                    </thead>
                    <tbody>
                      {Object.entries(latestTick.entity_counts)
                        .filter(([key]) => !key.includes('_churned') && !key.includes('_new'))
                        .map(([entityName, count]) => {
                          const newCount = latestTick.entity_counts[`${entityName}_new`] || 0;
                          const churnedCount = latestTick.entity_counts[`${entityName}_churned`] || 0;
                          const netChange = newCount - churnedCount;
                          return (
                            <tr key={entityName} className="border-b theme-border">
                              <td className="px-4 py-2">
                                <div className="flex items-center gap-2">
                                  <Users className="w-4 h-4 theme-info-icon" />
                                  <span className="theme-text">{entityName.charAt(0).toUpperCase() + entityName.slice(1)}</span>
                                </div>
                              </td>
                              <td className="px-4 py-2 text-right font-bold theme-text">{count.toLocaleString()}</td>
                              <td className="px-4 py-2 text-right">
                                <span className={cn("px-2 py-0.5 rounded-full text-xs", newCount > 0 ? "bg-green-500/20 text-green-400" : "theme-text-muted")}>+{newCount}</span>
                              </td>
                              <td className="px-4 py-2 text-right">
                                <span className={cn("px-2 py-0.5 rounded-full text-xs", churnedCount > 0 ? "bg-red-500/20 text-red-400" : "theme-text-muted")}>-{churnedCount}</span>
                              </td>
                              <td className="px-4 py-2 text-right">
                                <span className={cn("font-bold", netChange > 0 ? "text-green-500" : netChange < 0 ? "text-red-500" : "theme-text-muted")}>
                                  {netChange >= 0 ? '+' : ''}{netChange}
                                </span>
                              </td>
                            </tr>
                          );
                        })}
                    </tbody>
                  </table>
                </div>
              </CardContent>
            </Card>
          )}
        </>
      )}
    </div>
  );
}
