import { useState, useEffect } from 'react';
import { Workflow, Play, Pause, Settings, Database, Activity, ChevronRight, ChevronLeft, RefreshCw, Zap, Sparkles } from 'lucide-react';

interface DataEntity {
  id: string;
  name: string;
  description: string;
  recordsPerMinute: number;
  enabled: boolean;
  status: 'running' | 'paused' | 'stopped';
  source?: 'interview' | 'default';
}

interface DesignArtifact {
  type: string;
  name: string;
  details?: {
    code?: string;
    category?: string;
    description?: string;
  };
}

const defaultEntities: DataEntity[] = [
  {
    id: 'customers',
    name: 'Customers',
    description: 'Customer profiles and segments',
    recordsPerMinute: 50,
    enabled: true,
    status: 'running',
    source: 'default',
  },
  {
    id: 'orders',
    name: 'Orders',
    description: 'Sales orders and transactions',
    recordsPerMinute: 200,
    enabled: true,
    status: 'running',
    source: 'default',
  },
  {
    id: 'products',
    name: 'Products',
    description: 'Product catalog and inventory',
    recordsPerMinute: 25,
    enabled: true,
    status: 'paused',
    source: 'default',
  },
  {
    id: 'suppliers',
    name: 'Suppliers',
    description: 'Supplier information and performance',
    recordsPerMinute: 10,
    enabled: false,
    status: 'stopped',
    source: 'default',
  },
];

export default function DataSimulatorPage() {
  const [entities, setEntities] = useState<DataEntity[]>(defaultEntities);
  const [isSimulatorRunning, setIsSimulatorRunning] = useState(true);
  const [hasInterviewData, setHasInterviewData] = useState(false);

  // Load entities from interview design
  useEffect(() => {
    loadInterviewEntities();
  }, []);

  const loadInterviewEntities = () => {
    try {
      const storedDesign = localStorage.getItem('demo_interview_design');
      if (storedDesign) {
        const design = JSON.parse(storedDesign);
        
        // Check if there are entities from the interview
        if (design.entities && design.entities.length > 0) {
          const interviewEntities: DataEntity[] = design.entities.map((e: DesignArtifact, i: number) => ({
            id: e.details?.code || `entity_${i}`,
            name: e.name,
            description: e.details?.description || `Entity from ${design.industry || 'business'} design`,
            recordsPerMinute: Math.floor(Math.random() * 150) + 50,
            enabled: true,
            status: 'running' as const,
            source: 'interview' as const,
          }));
          setEntities(interviewEntities);
          setHasInterviewData(true);
        } else if (design.kpis && design.kpis.length > 0) {
          // Derive entities from KPIs if no explicit entities
          const kpiBasedEntities = deriveEntitiesFromKPIs(design.kpis, design.industry);
          if (kpiBasedEntities.length > 0) {
            setEntities(kpiBasedEntities);
            setHasInterviewData(true);
          }
        }
      }
    } catch (err) {
      console.error('Failed to load interview entities:', err);
    }
  };

  const deriveEntitiesFromKPIs = (kpis: DesignArtifact[], industry?: string): DataEntity[] => {
    const entityMap: Record<string, DataEntity> = {};
    
    // Derive entities based on KPI categories
    kpis.forEach((kpi) => {
      const category = kpi.details?.category || 'General';
      
      if (!entityMap[category]) {
        entityMap[category] = {
          id: category.toLowerCase().replace(/\s+/g, '_'),
          name: `${category} Data`,
          description: `${category} metrics for ${industry || 'business'} analytics`,
          recordsPerMinute: Math.floor(Math.random() * 100) + 25,
          enabled: true,
          status: 'running',
          source: 'interview',
        };
      }
    });
    
    // Add some standard entities based on industry
    if (industry?.toLowerCase().includes('retail')) {
      entityMap['transactions'] = {
        id: 'transactions',
        name: 'Transactions',
        description: 'Sales transactions and order data',
        recordsPerMinute: 150,
        enabled: true,
        status: 'running',
        source: 'interview',
      };
    } else if (industry?.toLowerCase().includes('manufacturing')) {
      entityMap['production'] = {
        id: 'production',
        name: 'Production Runs',
        description: 'Manufacturing batch and production data',
        recordsPerMinute: 75,
        enabled: true,
        status: 'running',
        source: 'interview',
      };
    }
    
    return Object.values(entityMap);
  };

  const toggleEntity = (id: string) => {
    setEntities((prev) =>
      prev.map((e) =>
        e.id === id
          ? { ...e, enabled: !e.enabled, status: e.enabled ? 'stopped' : 'running' }
          : e
      )
    );
  };

  const updateRate = (id: string, rate: number) => {
    setEntities((prev) =>
      prev.map((e) => (e.id === id ? { ...e, recordsPerMinute: rate } : e))
    );
  };

  const activeCount = entities.filter((e) => e.enabled).length;
  const totalRecordsPerMin = entities
    .filter((e) => e.enabled)
    .reduce((sum, e) => sum + e.recordsPerMinute, 0);

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title">Data Simulator</h1>
          <p className="mt-2 theme-text-secondary">
            Configure simulated data streams for your identified entities
          </p>
        </div>
        <div className="flex items-center gap-2 px-4 py-2 rounded-lg bg-alpha-500/10 text-alpha-400">
          <Workflow className="w-5 h-5" />
          <span className="font-medium">Step 4 of 6</span>
        </div>
      </div>

      {/* Simulator Status */}
      <div className="theme-card rounded-2xl p-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-6">
            <button
              onClick={() => setIsSimulatorRunning(!isSimulatorRunning)}
              className={`w-16 h-16 rounded-2xl flex items-center justify-center transition-all duration-300 ${
                isSimulatorRunning
                  ? 'bg-emerald-500/20 text-emerald-400 hover:bg-emerald-500/30'
                  : 'bg-slate-700 text-slate-400 hover:bg-slate-600'
              }`}
            >
              {isSimulatorRunning ? (
                <Pause className="w-8 h-8" />
              ) : (
                <Play className="w-8 h-8" />
              )}
            </button>
            <div>
              <h2 className="text-xl font-semibold theme-text-title">
                Simulator {isSimulatorRunning ? 'Running' : 'Paused'}
              </h2>
              <p className="theme-text-secondary">
                {activeCount} entities active • {totalRecordsPerMin.toLocaleString()} records/min
              </p>
            </div>
          </div>
          <div className="flex items-center gap-4">
            <div className="text-right">
              <p className="text-sm theme-text-muted">Total Generated</p>
              <p className="text-2xl font-bold text-emerald-400">12,847</p>
            </div>
            <div className="w-px h-12 bg-slate-700" />
            <div className="text-right">
              <p className="text-sm theme-text-muted">Uptime</p>
              <p className="text-2xl font-bold theme-text-title">00:04:32</p>
            </div>
          </div>
        </div>
      </div>

      {/* Entity Configuration */}
      <div className="grid grid-cols-2 gap-6">
        {entities.map((entity) => (
          <div
            key={entity.id}
            className={`theme-card rounded-2xl p-6 transition-all duration-200 ${
              entity.enabled ? 'border-l-4 border-l-emerald-500' : 'opacity-60'
            }`}
          >
            <div className="flex items-start justify-between mb-4">
              <div className="flex items-center gap-3">
                <div className={`w-12 h-12 rounded-xl flex items-center justify-center ${
                  entity.enabled ? 'bg-emerald-500/20 text-emerald-400' : 'bg-slate-700 text-slate-400'
                }`}>
                  <Database className="w-6 h-6" />
                </div>
                <div>
                  <h3 className="font-semibold theme-text-title">{entity.name}</h3>
                  <p className="text-sm theme-text-muted">{entity.description}</p>
                </div>
              </div>
              <button
                onClick={() => toggleEntity(entity.id)}
                className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                  entity.enabled
                    ? 'bg-emerald-500/20 text-emerald-400 hover:bg-emerald-500/30'
                    : 'bg-slate-700 text-slate-400 hover:bg-slate-600'
                }`}
              >
                {entity.enabled ? 'Active' : 'Inactive'}
              </button>
            </div>

            {/* Rate Slider */}
            <div className="space-y-2">
              <div className="flex items-center justify-between text-sm">
                <span className="theme-text-muted">Generation Rate</span>
                <span className="font-medium theme-text-title">{entity.recordsPerMinute} records/min</span>
              </div>
              <input
                type="range"
                min="10"
                max="500"
                value={entity.recordsPerMinute}
                onChange={(e) => updateRate(entity.id, parseInt(e.target.value))}
                disabled={!entity.enabled}
                className="w-full h-2 bg-slate-700 rounded-full appearance-none cursor-pointer [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-4 [&::-webkit-slider-thumb]:h-4 [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:bg-alpha-500"
              />
            </div>

            {/* Status Indicator */}
            {entity.enabled && (
              <div className="mt-4 flex items-center gap-2">
                <Activity className="w-4 h-4 text-emerald-400 animate-pulse" />
                <span className="text-sm text-emerald-400">Streaming data...</span>
                <div className="flex-1" />
                <RefreshCw className="w-4 h-4 theme-text-muted animate-spin" />
              </div>
            )}
          </div>
        ))}
      </div>

      {/* Info Banner */}
      <div className={`theme-card rounded-2xl p-6 bg-gradient-to-r ${hasInterviewData ? 'from-emerald-500/10 to-alpha-500/10 border-emerald-500/20' : 'from-alpha-500/10 to-purple-500/10 border-alpha-500/20'} border`}>
        <div className="flex items-center gap-4">
          <div className={`w-12 h-12 rounded-xl flex items-center justify-center ${hasInterviewData ? 'bg-emerald-500/20' : 'bg-alpha-500/20'}`}>
            {hasInterviewData ? <Sparkles className="w-6 h-6 text-emerald-400" /> : <Zap className="w-6 h-6 text-alpha-400" />}
          </div>
          <div className="flex-1">
            <h3 className="font-semibold theme-text-title">
              {hasInterviewData ? 'Interview-Driven Entities' : 'Simulated Data Ready'}
            </h3>
            <p className="text-sm theme-text-secondary">
              {hasInterviewData 
                ? `These entities were derived from your AI interview. ${entities.length} data streams configured based on your business design.`
                : 'Your simulated data streams are configured based on the entities identified during your AI interview. The Sample Analytics page will use this data to show you live dashboards.'}
            </p>
          </div>
          <Settings className="w-6 h-6 theme-text-muted" />
        </div>
      </div>

      {/* Navigation */}
      <div className="flex justify-between">
        <a
          href="/demo/interview"
          className="px-6 py-3 rounded-xl theme-card hover:bg-[var(--card-hover)] font-medium transition-colors flex items-center gap-2"
        >
          <ChevronLeft className="w-5 h-5" />
          Back to Interview
        </a>
        <a
          href="/demo/analytics"
          className="px-6 py-3 rounded-xl bg-alpha-500 hover:bg-alpha-600 text-white font-medium transition-colors flex items-center gap-2"
        >
          View Sample Analytics
          <ChevronRight className="w-5 h-5" />
        </a>
      </div>
    </div>
  );
}
