import { useState } from 'react';
import {
  Play,
  Plus,
  Settings,
  GitBranch,
  Clock,
  Users,
  DollarSign,
  AlertTriangle,
  TrendingUp,
  TrendingDown,
  BarChart3,
  Layers,
  ArrowRight,
  RefreshCw,
  Download,
  Check,
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';
import { cn } from '../../lib/utils';

interface ProcessStep {
  id: string;
  name: string;
  type: 'start' | 'task' | 'decision' | 'end';
  duration: number;
  cost: number;
  resources: number;
  defectRate: number;
  utilization?: number;
  waitTime?: number;
}

interface Scenario {
  id: string;
  name: string;
  isBaseline: boolean;
  changes: { stepId: string; field: string; oldValue: number; newValue: number }[];
  selected: boolean;
}

const mockSteps: ProcessStep[] = [
  { id: '1', name: 'Order Received', type: 'start', duration: 0, cost: 0, resources: 0, defectRate: 0 },
  { id: '2', name: 'Order Processing', type: 'task', duration: 10, cost: 5, resources: 2, defectRate: 2, utilization: 95, waitTime: 12 },
  { id: '3', name: 'Inventory Check', type: 'decision', duration: 2, cost: 1, resources: 1, defectRate: 0, utilization: 72, waitTime: 3 },
  { id: '4', name: 'Quality Check', type: 'task', duration: 5, cost: 3, resources: 1, defectRate: 1, utilization: 68, waitTime: 2 },
  { id: '5', name: 'Shipping', type: 'task', duration: 15, cost: 8, resources: 2, defectRate: 0.5, utilization: 45, waitTime: 1 },
  { id: '6', name: 'Order Complete', type: 'end', duration: 0, cost: 0, resources: 0, defectRate: 0 },
];

const mockScenarios: Scenario[] = [
  { id: '1', name: 'Baseline (Current)', isBaseline: true, changes: [], selected: true },
  { id: '2', name: '+20% Capacity', isBaseline: false, changes: [
    { stepId: '2', field: 'resources', oldValue: 2, newValue: 3 },
  ], selected: true },
  { id: '3', name: 'Automation Option', isBaseline: false, changes: [
    { stepId: '2', field: 'duration', oldValue: 10, newValue: 6 },
    { stepId: '2', field: 'defectRate', oldValue: 2, newValue: 0.5 },
  ], selected: false },
];


function ProcessNode({ step, isSelected, onClick }: { step: ProcessStep; isSelected: boolean; onClick: () => void }) {
  const nodeStyles = {
    start: 'rounded-full bg-green-500',
    task: 'rounded-xl bg-alpha-600',
    decision: 'rotate-45 bg-amber-500',
    end: 'rounded-full bg-red-500',
  };

  return (
    <button
      onClick={onClick}
      className={cn(
        'relative flex items-center justify-center transition-all duration-200',
        step.type === 'decision' ? 'w-12 h-12' : 'w-24 h-12',
        nodeStyles[step.type],
        isSelected && 'ring-2 ring-white ring-offset-2 ring-offset-[var(--background)]',
        'hover:scale-105'
      )}
    >
      <span className={cn(
        'text-white text-xs font-medium text-center px-1',
        step.type === 'decision' && '-rotate-45'
      )}>
        {step.type === 'start' ? '●' : step.type === 'end' ? '●' : step.name.split(' ')[0]}
      </span>
      {step.utilization && step.utilization > 90 && (
        <div className="absolute -top-1 -right-1 w-4 h-4 bg-red-500 rounded-full flex items-center justify-center">
          <AlertTriangle className="w-3 h-3 text-white" />
        </div>
      )}
    </button>
  );
}

function MetricCard({ label, value, change, unit, icon }: { 
  label: string; 
  value: string; 
  change?: number; 
  unit?: string;
  icon: React.ReactNode;
}) {
  return (
    <div className="p-4 rounded-xl theme-card-bg border theme-border">
      <div className="flex items-center justify-between mb-2">
        <span className="text-sm theme-text-muted">{label}</span>
        {icon}
      </div>
      <div className="flex items-baseline gap-1">
        <span className="text-2xl font-bold theme-text-title">{value}</span>
        {unit && <span className="text-sm theme-text-muted">{unit}</span>}
      </div>
      {change !== undefined && (
        <div className={cn(
          'flex items-center gap-1 mt-1 text-sm font-medium',
          change < 0 ? 'text-green-500' : change > 0 ? 'text-red-500' : 'theme-text-muted'
        )}>
          {change < 0 ? <TrendingDown className="w-3 h-3" /> : change > 0 ? <TrendingUp className="w-3 h-3" /> : null}
          <span>{change > 0 ? '+' : ''}{change}%</span>
        </div>
      )}
    </div>
  );
}

export default function ProcessScenarioModelerPage() {
  const [selectedStep, setSelectedStep] = useState<ProcessStep | null>(mockSteps[1]);
  const [scenarios, setScenarios] = useState(mockScenarios);
  const [isSimulating, setIsSimulating] = useState(false);
  const [hasResults, setHasResults] = useState(true);

  const handleRunSimulation = () => {
    setIsSimulating(true);
    setTimeout(() => {
      setIsSimulating(false);
      setHasResults(true);
    }, 2000);
  };

  const toggleScenario = (id: string) => {
    setScenarios(scenarios.map(s => 
      s.id === id ? { ...s, selected: !s.selected } : s
    ));
  };

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Page Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title tracking-wide">Process Scenario Modeler</h1>
          <p className="theme-text-muted mt-1">Test process changes before implementing them</p>
        </div>
        <div className="flex items-center gap-3">
          <Button variant="outline">
            <Download className="w-4 h-4 mr-2" />
            Export
          </Button>
          <Button onClick={handleRunSimulation} disabled={isSimulating}>
            {isSimulating ? (
              <>
                <RefreshCw className="w-4 h-4 mr-2 animate-spin" />
                Simulating...
              </>
            ) : (
              <>
                <Play className="w-4 h-4 mr-2" />
                Run Simulation
              </>
            )}
          </Button>
        </div>
      </div>

      {/* Main Content */}
      <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
        {/* Process Designer - 3 columns */}
        <div className="lg:col-span-3 space-y-6">
          {/* Process Canvas */}
          <Card>
            <CardHeader>
              <div className="flex items-center justify-between">
                <CardTitle className="flex items-center gap-2">
                  <GitBranch className="w-5 h-5 theme-info-icon" />
                  Process Designer
                </CardTitle>
                <div className="flex items-center gap-2">
                  <Button variant="ghost" size="sm">
                    <Plus className="w-4 h-4 mr-1" /> Add Step
                  </Button>
                  <Button variant="ghost" size="sm">
                    <Layers className="w-4 h-4 mr-1" /> Add Decision
                  </Button>
                </div>
              </div>
            </CardHeader>
            <CardContent>
              {/* Process Flow Visualization */}
              <div className="flex items-center justify-center gap-4 py-8 overflow-x-auto">
                {mockSteps.map((step, index) => (
                  <div key={step.id} className="flex items-center">
                    <ProcessNode
                      step={step}
                      isSelected={selectedStep?.id === step.id}
                      onClick={() => setSelectedStep(step)}
                    />
                    {index < mockSteps.length - 1 && (
                      <ArrowRight className="w-6 h-6 mx-2 theme-text-muted" />
                    )}
                  </div>
                ))}
              </div>

              {/* Step Properties Panel */}
              {selectedStep && selectedStep.type !== 'start' && selectedStep.type !== 'end' && (
                <div className="mt-6 p-4 rounded-xl theme-card-bg border theme-border">
                  <div className="flex items-center justify-between mb-4">
                    <h3 className="font-semibold theme-text-title flex items-center gap-2">
                      <Settings className="w-4 h-4" />
                      {selectedStep.name} Properties
                    </h3>
                  </div>
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <div>
                      <label className="text-xs theme-text-muted block mb-1">Duration (min)</label>
                      <input
                        type="number"
                        value={selectedStep.duration}
                        className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text focus:ring-2 focus:ring-alpha-500"
                      />
                    </div>
                    <div>
                      <label className="text-xs theme-text-muted block mb-1">Cost ($)</label>
                      <input
                        type="number"
                        value={selectedStep.cost}
                        className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text focus:ring-2 focus:ring-alpha-500"
                      />
                    </div>
                    <div>
                      <label className="text-xs theme-text-muted block mb-1">Resources</label>
                      <input
                        type="number"
                        value={selectedStep.resources}
                        className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text focus:ring-2 focus:ring-alpha-500"
                      />
                    </div>
                    <div>
                      <label className="text-xs theme-text-muted block mb-1">Defect Rate (%)</label>
                      <input
                        type="number"
                        value={selectedStep.defectRate}
                        step="0.1"
                        className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text focus:ring-2 focus:ring-alpha-500"
                      />
                    </div>
                  </div>
                </div>
              )}
            </CardContent>
          </Card>

          {/* Simulation Results */}
          {hasResults && (
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <BarChart3 className="w-5 h-5 theme-info-icon" />
                  Simulation Results
                </CardTitle>
              </CardHeader>
              <CardContent>
                {/* Metrics Summary */}
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
                  <MetricCard
                    label="Cycle Time"
                    value="3.6"
                    change={-15}
                    unit="hours"
                    icon={<Clock className="w-4 h-4 theme-info-icon" />}
                  />
                  <MetricCard
                    label="Throughput"
                    value="55"
                    change={22}
                    unit="/hour"
                    icon={<TrendingUp className="w-4 h-4 theme-info-icon" />}
                  />
                  <MetricCard
                    label="Utilization"
                    value="78"
                    unit="%"
                    icon={<Users className="w-4 h-4 theme-info-icon" />}
                  />
                  <MetricCard
                    label="Cost per Unit"
                    value="$11"
                    change={-8}
                    icon={<DollarSign className="w-4 h-4 theme-info-icon" />}
                  />
                </div>

                {/* Bottleneck Analysis */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <h4 className="font-semibold theme-text-title mb-3 flex items-center gap-2">
                      <AlertTriangle className="w-4 h-4 text-amber-500" />
                      Bottleneck Analysis
                    </h4>
                    <div className="space-y-2">
                      {mockSteps.filter(s => s.utilization).map(step => (
                        <div key={step.id} className="flex items-center justify-between p-3 rounded-lg theme-card-bg">
                          <span className="text-sm theme-text">{step.name}</span>
                          <div className="flex items-center gap-4">
                            <div className="flex items-center gap-2">
                              <span className="text-xs theme-text-muted">Util:</span>
                              <span className={cn(
                                'text-sm font-medium',
                                step.utilization! > 90 ? 'text-red-500' : 
                                step.utilization! > 70 ? 'text-amber-500' : 'text-green-500'
                              )}>
                                {step.utilization}%
                              </span>
                            </div>
                            <div className="flex items-center gap-2">
                              <span className="text-xs theme-text-muted">Wait:</span>
                              <span className="text-sm theme-text">{step.waitTime}m</span>
                            </div>
                            {step.utilization! > 90 && (
                              <AlertTriangle className="w-4 h-4 text-red-500" />
                            )}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>

                  <div>
                    <h4 className="font-semibold theme-text-title mb-3 flex items-center gap-2">
                      <TrendingUp className="w-4 h-4 theme-info-icon" />
                      KPI Impact Prediction
                    </h4>
                    <div className="space-y-2">
                      {[
                        { kpi: 'Order Cycle Time', impact: -15, direction: 'decrease' },
                        { kpi: 'Customer Satisfaction', impact: 8, direction: 'increase' },
                        { kpi: 'Operating Cost', impact: -8, direction: 'decrease' },
                        { kpi: 'Defect Rate', impact: -25, direction: 'decrease' },
                      ].map((item, index) => (
                        <div key={index} className="flex items-center justify-between p-3 rounded-lg theme-card-bg">
                          <span className="text-sm theme-text">{item.kpi}</span>
                          <span className={cn(
                            'text-sm font-medium',
                            (item.direction === 'decrease' && item.impact < 0) || 
                            (item.direction === 'increase' && item.impact > 0)
                              ? 'text-green-500' : 'text-red-500'
                          )}>
                            {item.impact > 0 ? '+' : ''}{item.impact}%
                          </span>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          )}
        </div>

        {/* Scenario Panel - 1 column */}
        <div className="space-y-6">
          <Card>
            <CardHeader>
              <div className="flex items-center justify-between">
                <CardTitle>Scenarios</CardTitle>
                <Button variant="ghost" size="sm">
                  <Plus className="w-4 h-4" />
                </Button>
              </div>
            </CardHeader>
            <CardContent className="space-y-3">
              {scenarios.map(scenario => (
                <button
                  key={scenario.id}
                  onClick={() => toggleScenario(scenario.id)}
                  className={cn(
                    'w-full p-3 rounded-xl border text-left transition-all duration-200',
                    scenario.selected 
                      ? 'border-alpha-500 bg-alpha-500/10' 
                      : 'theme-border theme-card-bg hover:theme-card-bg-hover'
                  )}
                >
                  <div className="flex items-center justify-between">
                    <span className="font-medium theme-text-title text-sm">{scenario.name}</span>
                    {scenario.selected && <Check className="w-4 h-4 text-alpha-500" />}
                  </div>
                  {scenario.isBaseline && (
                    <span className="text-xs theme-text-muted">Current state</span>
                  )}
                  {scenario.changes.length > 0 && (
                    <div className="mt-2 space-y-1">
                      {scenario.changes.map((change, idx) => (
                        <div key={idx} className="text-xs theme-text-muted">
                          {mockSteps.find(s => s.id === change.stepId)?.name}: {change.field} {change.oldValue} → {change.newValue}
                        </div>
                      ))}
                    </div>
                  )}
                </button>
              ))}
            </CardContent>
          </Card>

          {/* Parameter Changes */}
          <Card>
            <CardHeader>
              <CardTitle>Parameter Changes</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <div>
                  <label className="text-xs theme-text-muted block mb-1">Step</label>
                  <select className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text">
                    {mockSteps.filter(s => s.type === 'task').map(step => (
                      <option key={step.id} value={step.id}>{step.name}</option>
                    ))}
                  </select>
                </div>
                <div>
                  <label className="text-xs theme-text-muted block mb-1">Parameter</label>
                  <select className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text">
                    <option value="duration">Duration</option>
                    <option value="cost">Cost</option>
                    <option value="resources">Resources</option>
                    <option value="defectRate">Defect Rate</option>
                  </select>
                </div>
                <div className="grid grid-cols-2 gap-2">
                  <div>
                    <label className="text-xs theme-text-muted block mb-1">From</label>
                    <input
                      type="number"
                      value="10"
                      className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text"
                      disabled
                    />
                  </div>
                  <div>
                    <label className="text-xs theme-text-muted block mb-1">To</label>
                    <input
                      type="number"
                      value="8"
                      className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text"
                    />
                  </div>
                </div>
                <Button variant="secondary" size="sm" className="w-full">
                  <Plus className="w-4 h-4 mr-1" />
                  Add Change
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}
