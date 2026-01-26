import { useState, useEffect } from 'react';
import {
  Play,
  Square,
  Pause,
  PlayCircle,
  CheckCircle,
  RefreshCw,
  Cloud,
  Zap,
  Trash2,
  ChevronDown,
  ChevronUp,
  Database,
  Clock,
  Activity,
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { cn } from '../lib/utils';
import KPITreeSelector, { KPIInfo } from '../components/KPITreeSelector';

const API_BASE = '/api/v1/simulator';

const SCENARIOS = [
  { id: 'healthy', name: 'Healthy Business', description: 'Low churn (1%), steady growth (7.5%)' },
  { id: 'struggling', name: 'Struggling Business', description: 'High churn (4%), low growth (1.5%)' },
  { id: 'seasonal', name: 'Seasonal Patterns', description: 'Cyclical variations throughout the year' },
  { id: 'growth_spurt', name: 'Growth Spurt', description: 'Rapid expansion (15% growth), low churn' },
  { id: 'stable', name: 'Stable', description: 'Minimal change, steady state' },
  { id: 'volatile', name: 'Volatile', description: 'High variance, unpredictable patterns' },
];

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

interface EntityEvent {
  event_type: string;
  entity_name: string;
  entity_id: string;
  timestamp: string;
  attributes: Record<string, any>;
}

interface SimulationTick {
  tick_number: number;
  simulated_time: string;
  real_time: string;
  entity_counts: Record<string, number>;
  events: EntityEvent[];
  metrics: Record<string, number>;
}

function StatusBadge({ status }: { status: string }) {
  const config: Record<string, { color: string; icon: React.ReactNode }> = {
    running: { color: 'bg-blue-500/20 text-blue-400 border-blue-500/30', icon: <RefreshCw className="w-3 h-3 animate-spin" /> },
    completed: { color: 'bg-green-500/20 text-green-400 border-green-500/30', icon: <CheckCircle className="w-3 h-3" /> },
    paused: { color: 'bg-amber-500/20 text-amber-400 border-amber-500/30', icon: <Pause className="w-3 h-3" /> },
    stopped: { color: 'bg-red-500/20 text-red-400 border-red-500/30', icon: <Square className="w-3 h-3" /> },
    pending: { color: 'bg-gray-500/20 text-gray-400 border-gray-500/30', icon: <Clock className="w-3 h-3" /> },
  };
  
  const { color, icon } = config[status] || config.pending;
  
  return (
    <span className={cn('inline-flex items-center gap-1.5 px-2 py-1 rounded-full text-xs font-medium border', color)}>
      {icon}
      {status}
    </span>
  );
}

export default function SimulationPage() {
  const [availableKPIs, setAvailableKPIs] = useState<KPIInfo[]>([]);
  const [selectedKPIs, setSelectedKPIs] = useState<KPIInfo[]>([]);
  const [loadingKPIs, setLoadingKPIs] = useState(false);
  
  const [simulationName, setSimulationName] = useState('');
  const [selectedScenario, setSelectedScenario] = useState('healthy');
  const [realIntervalSeconds, setRealIntervalSeconds] = useState(10);
  const [simulatedIntervalHours, setSimulatedIntervalHours] = useState(1);
  const [autoStart, setAutoStart] = useState(true);
  
  const [simulations, setSimulations] = useState<Simulation[]>([]);
  const [expandedSimulation, setExpandedSimulation] = useState<string | null>(null);
  const [simulationTicks, setSimulationTicks] = useState<Record<string, SimulationTick[]>>({});
  
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchAvailableKPIs();
    fetchSimulations();
    const interval = setInterval(fetchSimulations, 3000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    if (!expandedSimulation) return;
    fetchSimulationTicks(expandedSimulation);
    const tickInterval = setInterval(() => {
      fetchSimulationTicks(expandedSimulation);
    }, 2000);
    return () => clearInterval(tickInterval);
  }, [expandedSimulation]);

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

  const accelerationFactor = (simulatedIntervalHours * 3600) / realIntervalSeconds;
  const getAccelerationText = () => {
    if (accelerationFactor >= 24) {
      return `${(accelerationFactor / 24).toFixed(1)} days/minute`;
    }
    return `${accelerationFactor.toFixed(1)} hours/minute`;
  };

  const selectedEntities = [...new Set(selectedKPIs.flatMap(k => k.required_objects))];
  const currentScenario = SCENARIOS.find(s => s.id === selectedScenario);

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Page Header */}
      <div>
        <h1 className="text-3xl font-bold theme-text-title tracking-wide">KPI Data Simulator</h1>
        <p className="theme-text-muted mt-1">Generate realistic demo data for selected KPIs with configurable time acceleration.</p>
      </div>

      {/* Error Alert */}
      {error && (
        <div className="p-4 rounded-xl bg-red-500/10 border border-red-500/30 text-red-400 flex items-center justify-between">
          <span>{error}</span>
          <button onClick={() => setError(null)} className="text-red-400 hover:text-red-300">×</button>
        </div>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-5 gap-6">
        {/* Configuration Panel */}
        <div className="lg:col-span-2">
          <Card>
            <CardHeader>
              <CardTitle>New Simulation</CardTitle>
            </CardHeader>
            <CardContent className="space-y-5">
              {/* KPI Selection */}
              <div>
                <label className="text-sm font-medium theme-text-title block mb-2">Select KPIs</label>
                <KPITreeSelector
                  kpis={availableKPIs}
                  selectedKPIs={selectedKPIs}
                  onSelectionChange={setSelectedKPIs}
                  loading={loadingKPIs}
                />
              </div>

              {/* Selected Entities */}
              {selectedEntities.length > 0 && (
                <div className="p-3 rounded-xl theme-card-bg border theme-border">
                  <div className="flex items-center gap-2 mb-2">
                    <Database className="w-4 h-4 theme-info-icon" />
                    <span className="text-sm font-medium theme-text-title">Required Entities ({selectedEntities.length})</span>
                  </div>
                  <div className="flex flex-wrap gap-1.5">
                    {selectedEntities.map(entity => (
                      <span key={entity} className="px-2 py-0.5 rounded-full text-xs theme-card-bg border theme-border theme-text">
                        {entity}
                      </span>
                    ))}
                  </div>
                </div>
              )}

              {/* Simulation Name */}
              <div>
                <label className="text-sm font-medium theme-text-title block mb-2">Simulation Name</label>
                <input
                  type="text"
                  value={simulationName}
                  onChange={(e) => setSimulationName(e.target.value)}
                  placeholder="Auto-generated if empty"
                  className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border
                    theme-text placeholder:theme-text-muted
                    focus:outline-none focus:ring-2 focus:ring-alpha-500"
                />
              </div>

              {/* Scenario Selection */}
              <div>
                <label className="text-sm font-medium theme-text-title block mb-2">Scenario</label>
                <select
                  value={selectedScenario}
                  onChange={(e) => setSelectedScenario(e.target.value)}
                  className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border
                    theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                >
                  {SCENARIOS.map((s) => (
                    <option key={s.id} value={s.id}>{s.name}</option>
                  ))}
                </select>
                {currentScenario && (
                  <p className="text-xs theme-text-muted mt-1">{currentScenario.description}</p>
                )}
              </div>

              {/* Time Acceleration */}
              <div className="space-y-4">
                <div className="flex items-center gap-2">
                  <Zap className="w-4 h-4 theme-info-icon" />
                  <span className="text-sm font-medium theme-text-title">Time Acceleration</span>
                </div>

                <div>
                  <div className="flex justify-between text-sm mb-2">
                    <span className="theme-text-muted">Real-time Interval: {realIntervalSeconds} seconds</span>
                  </div>
                  <input
                    type="range"
                    min="1"
                    max="60"
                    value={realIntervalSeconds}
                    onChange={(e) => setRealIntervalSeconds(Number(e.target.value))}
                    className="w-full h-2 rounded-full bg-alpha-faded-200 dark:bg-alpha-faded-800 appearance-none cursor-pointer
                      [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-4 [&::-webkit-slider-thumb]:h-4 
                      [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:bg-alpha-500"
                  />
                  <div className="flex justify-between text-xs theme-text-muted mt-1">
                    <span>1s</span>
                    <span>10s</span>
                    <span>30s</span>
                    <span>60s</span>
                  </div>
                </div>

                <div>
                  <div className="flex justify-between text-sm mb-2">
                    <span className="theme-text-muted">Simulated Time per Interval: {simulatedIntervalHours} hour(s)</span>
                  </div>
                  <input
                    type="range"
                    min="1"
                    max="24"
                    value={simulatedIntervalHours}
                    onChange={(e) => setSimulatedIntervalHours(Number(e.target.value))}
                    className="w-full h-2 rounded-full bg-alpha-faded-200 dark:bg-alpha-faded-800 appearance-none cursor-pointer
                      [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-4 [&::-webkit-slider-thumb]:h-4 
                      [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:bg-alpha-500"
                  />
                  <div className="flex justify-between text-xs theme-text-muted mt-1">
                    <span>1h</span>
                    <span>6h</span>
                    <span>12h</span>
                    <span>24h</span>
                  </div>
                </div>

                <div className="p-3 rounded-xl bg-alpha-500/10 border border-alpha-500/30">
                  <p className="text-sm theme-text-vibrant font-medium">
                    Acceleration: {getAccelerationText()} of real time
                  </p>
                  <p className="text-xs theme-text-muted mt-1">
                    Every {realIntervalSeconds}s = {simulatedIntervalHours}h simulated
                  </p>
                </div>
              </div>

              {/* Auto-start Toggle */}
              <label className="flex items-center gap-3 cursor-pointer">
                <div className="relative">
                  <input
                    type="checkbox"
                    checked={autoStart}
                    onChange={(e) => setAutoStart(e.target.checked)}
                    className="sr-only peer"
                  />
                  <div className="w-10 h-6 rounded-full bg-alpha-faded-300 dark:bg-alpha-faded-700 
                    peer-checked:bg-alpha-500 transition-colors"></div>
                  <div className="absolute left-1 top-1 w-4 h-4 rounded-full bg-white 
                    peer-checked:translate-x-4 transition-transform"></div>
                </div>
                <span className="text-sm theme-text">Auto-start simulation</span>
              </label>

              {/* Create Button */}
              <Button
                onClick={handleCreateSimulation}
                disabled={selectedKPIs.length === 0 || loading}
                className="w-full"
              >
                {loading ? (
                  <>
                    <RefreshCw className="w-4 h-4 mr-2 animate-spin" />
                    Creating...
                  </>
                ) : (
                  <>
                    <Play className="w-4 h-4 mr-2" />
                    Create Simulation
                  </>
                )}
              </Button>
            </CardContent>
          </Card>
        </div>

        {/* Active Simulations */}
        <div className="lg:col-span-3">
          <Card className="h-full">
            <CardHeader>
              <div className="flex items-center justify-between">
                <CardTitle className="flex items-center gap-2">
                  <Activity className="w-5 h-5 theme-info-icon" />
                  Active Simulations
                </CardTitle>
                <button
                  onClick={fetchSimulations}
                  className="p-2 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 transition-colors"
                >
                  <RefreshCw className="w-4 h-4 theme-text-muted" />
                </button>
              </div>
            </CardHeader>
            <CardContent>
              {simulations.length === 0 ? (
                <div className="text-center py-12">
                  <Cloud className="w-16 h-16 mx-auto theme-text-muted mb-4" />
                  <p className="theme-text-muted">No active simulations</p>
                  <p className="text-sm theme-text-muted">Create a simulation to get started</p>
                </div>
              ) : (
                <div className="space-y-3">
                  {simulations.map((sim) => (
                    <div key={sim.simulation_id} className="rounded-xl theme-card-bg border theme-border overflow-hidden">
                      {/* Simulation Header */}
                      <div className="p-4">
                        <div className="flex items-start justify-between">
                          <div className="flex-1 min-w-0">
                            <h3 className="font-semibold theme-text-title truncate">{sim.name}</h3>
                            <div className="flex flex-wrap items-center gap-2 mt-2">
                              <StatusBadge status={sim.status} />
                              <span className="px-2 py-0.5 rounded-full text-xs border theme-border theme-text-muted">
                                {sim.scenario}
                              </span>
                              <span className="px-2 py-0.5 rounded-full text-xs border theme-border theme-text-muted flex items-center gap-1">
                                <Zap className="w-3 h-3" />
                                {sim.time_acceleration.acceleration_factor.toFixed(0)}x
                              </span>
                            </div>
                            <p className="text-xs theme-text-muted mt-2">
                              Ticks: {sim.ticks_completed} • 
                              Entities: {Object.entries(sim.entity_counts).map(([k, v]) => `${k}: ${v}`).join(', ')}
                            </p>
                          </div>
                          
                          {/* Action Buttons */}
                          <div className="flex items-center gap-1 ml-4">
                            {sim.status === 'pending' && (
                              <button
                                onClick={() => handleStartSimulation(sim.simulation_id)}
                                className="p-2 rounded-lg hover:bg-green-500/20 text-green-400 transition-colors"
                                title="Start"
                              >
                                <Play className="w-4 h-4" />
                              </button>
                            )}
                            {sim.status === 'running' && (
                              <button
                                onClick={() => handlePauseSimulation(sim.simulation_id)}
                                className="p-2 rounded-lg hover:bg-amber-500/20 text-amber-400 transition-colors"
                                title="Pause"
                              >
                                <Pause className="w-4 h-4" />
                              </button>
                            )}
                            {sim.status === 'paused' && (
                              <button
                                onClick={() => handleResumeSimulation(sim.simulation_id)}
                                className="p-2 rounded-lg hover:bg-green-500/20 text-green-400 transition-colors"
                                title="Resume"
                              >
                                <PlayCircle className="w-4 h-4" />
                              </button>
                            )}
                            {(sim.status === 'running' || sim.status === 'paused') && (
                              <button
                                onClick={() => handleStopSimulation(sim.simulation_id)}
                                className="p-2 rounded-lg hover:bg-red-500/20 text-red-400 transition-colors"
                                title="Stop"
                              >
                                <Square className="w-4 h-4" />
                              </button>
                            )}
                            <button
                              onClick={() => handleDeleteSimulation(sim.simulation_id)}
                              className="p-2 rounded-lg hover:bg-red-500/20 text-red-400 transition-colors"
                              title="Delete"
                            >
                              <Trash2 className="w-4 h-4" />
                            </button>
                            <button
                              onClick={() => toggleExpanded(sim.simulation_id)}
                              className="p-2 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 transition-colors"
                            >
                              {expandedSimulation === sim.simulation_id ? (
                                <ChevronUp className="w-4 h-4 theme-text-muted" />
                              ) : (
                                <ChevronDown className="w-4 h-4 theme-text-muted" />
                              )}
                            </button>
                          </div>
                        </div>
                      </div>

                      {/* Expanded Tick Stream */}
                      {expandedSimulation === sim.simulation_id && (
                        <div className="border-t theme-border p-4 bg-[var(--background)]">
                          <div className="flex items-center justify-between mb-3">
                            <div className="flex items-center gap-2">
                              <RefreshCw className={cn(
                                "w-4 h-4 theme-info-icon",
                                sim.status === 'running' && "animate-spin"
                              )} />
                              <span className="text-sm font-medium theme-text-title">Live Tick Stream</span>
                            </div>
                            <span className="text-xs theme-text-muted">
                              {simulationTicks[sim.simulation_id]?.length || 0} ticks buffered
                            </span>
                          </div>

                          {simulationTicks[sim.simulation_id]?.length > 0 ? (
                            <div className="max-h-96 overflow-y-auto space-y-2">
                              {[...simulationTicks[sim.simulation_id]].reverse().slice(0, 20).map((tick) => (
                                <div
                                  key={tick.tick_number}
                                  className={cn(
                                    "p-3 rounded-lg theme-card-bg border-l-2",
                                    tick.tick_number === simulationTicks[sim.simulation_id].length
                                      ? "border-l-green-500"
                                      : "border-l-gray-600"
                                  )}
                                >
                                  <div className="flex items-center justify-between mb-2">
                                    <span className="text-sm font-semibold theme-text-title">
                                      Tick #{tick.tick_number}
                                    </span>
                                    <div className="flex items-center gap-2">
                                      <span className="text-xs theme-text-muted">
                                        {new Date(tick.simulated_time).toLocaleString()}
                                      </span>
                                      <span className={cn(
                                        "px-2 py-0.5 rounded-full text-xs",
                                        tick.events?.length > 0
                                          ? "bg-alpha-500/20 text-alpha-400"
                                          : "bg-gray-500/20 text-gray-400"
                                      )}>
                                        {tick.events?.length || 0} events
                                      </span>
                                    </div>
                                  </div>

                                  {/* Entity Counts */}
                                  <div className="mb-2">
                                    <span className="text-xs font-medium theme-text-muted">Entity Counts:</span>
                                    <div className="flex flex-wrap gap-1 mt-1">
                                      {Object.entries(tick.entity_counts)
                                        .filter(([k]) => !k.includes('_'))
                                        .map(([entity, count]) => (
                                          <span key={entity} className="px-2 py-0.5 rounded text-xs theme-card-bg border theme-border">
                                            {entity}: {count}
                                          </span>
                                        ))}
                                    </div>
                                  </div>

                                  {/* KPI Metrics */}
                                  {tick.metrics && Object.keys(tick.metrics).length > 0 && (
                                    <div className="mb-2">
                                      <span className="text-xs font-medium theme-text-muted">KPI Calculations:</span>
                                      <div className="grid grid-cols-2 gap-2 mt-1">
                                        {Object.entries(tick.metrics).map(([kpi, value]) => (
                                          <div key={kpi} className="flex justify-between text-xs">
                                            <span className="theme-text font-medium">{kpi}</span>
                                            <span className="font-mono theme-text-muted">
                                              {typeof value === 'number' ? value.toLocaleString(undefined, { maximumFractionDigits: 2 }) : value}
                                            </span>
                                          </div>
                                        ))}
                                      </div>
                                    </div>
                                  )}

                                  {/* Events */}
                                  {tick.events && tick.events.length > 0 && (
                                    <div>
                                      <span className="text-xs font-medium theme-text-muted">Events:</span>
                                      <div className="mt-1 space-y-1 max-h-32 overflow-y-auto">
                                        {tick.events.slice(0, 10).map((event, idx) => (
                                          <div key={idx} className="flex items-center gap-2 text-xs">
                                            <span className={cn(
                                              "px-1.5 py-0.5 rounded text-xs",
                                              event.event_type === 'created' ? "bg-green-500/20 text-green-400" :
                                              event.event_type === 'updated' ? "bg-blue-500/20 text-blue-400" :
                                              event.event_type === 'deleted' ? "bg-red-500/20 text-red-400" :
                                              "bg-gray-500/20 text-gray-400"
                                            )}>
                                              {event.event_type}
                                            </span>
                                            <span className="font-mono theme-text-muted">
                                              {event.entity_name}:{event.entity_id?.slice(0, 8)}
                                            </span>
                                          </div>
                                        ))}
                                        {tick.events.length > 10 && (
                                          <span className="text-xs theme-text-muted">
                                            ... and {tick.events.length - 10} more events
                                          </span>
                                        )}
                                      </div>
                                    </div>
                                  )}
                                </div>
                              ))}
                            </div>
                          ) : (
                            <div className="text-center py-8">
                              <RefreshCw className="w-10 h-10 mx-auto theme-text-muted mb-2" />
                              <p className="text-sm theme-text-muted">No ticks recorded yet</p>
                              <p className="text-xs theme-text-muted">Start the simulation to see live data</p>
                            </div>
                          )}
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              )}
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}
