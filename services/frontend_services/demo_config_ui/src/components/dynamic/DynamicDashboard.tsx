import { useState, useEffect } from 'react';
import { BarChart3, TrendingUp, TrendingDown, RefreshCw, Target, DollarSign, Users, Package, Activity, Zap, PieChart } from 'lucide-react';

// Component configuration types
export interface MetricCardConfig {
  id: string;
  type: 'metric_card';
  title: string;
  kpiCode: string;
  icon?: string;
  format?: 'number' | 'currency' | 'percent';
  showTrend?: boolean;
}

export interface ChartConfig {
  id: string;
  type: 'bar_chart' | 'line_chart' | 'pie_chart' | 'area_chart';
  title: string;
  dataKey: string;
  size?: 'small' | 'medium' | 'large' | 'full';
}

export interface TableConfig {
  id: string;
  type: 'table';
  title: string;
  columns: { key: string; label: string; format?: string }[];
  dataSource: string;
}

export type ComponentConfig = MetricCardConfig | ChartConfig | TableConfig;

export interface DashboardLayout {
  id: string;
  title: string;
  subtitle?: string;
  industry?: string;
  columns: number;
  refreshInterval?: number;
  sections: {
    id: string;
    title?: string;
    layout: 'grid' | 'flex' | 'stack';
    columns?: number;
    components: ComponentConfig[];
  }[];
}

interface DynamicDashboardProps {
  layout: DashboardLayout;
  data?: Record<string, any>;
  onRefresh?: () => void;
}

const iconMap: Record<string, React.ReactNode> = {
  'dollar': <DollarSign className="w-6 h-6" />,
  'users': <Users className="w-6 h-6" />,
  'package': <Package className="w-6 h-6" />,
  'trending': <TrendingUp className="w-6 h-6" />,
  'target': <Target className="w-6 h-6" />,
  'activity': <Activity className="w-6 h-6" />,
  'zap': <Zap className="w-6 h-6" />,
  'chart': <BarChart3 className="w-6 h-6" />,
  'pie': <PieChart className="w-6 h-6" />,
  'default': <BarChart3 className="w-6 h-6" />,
};

// Dynamic Metric Card Component
function DynamicMetricCard({ config, value, change }: { config: MetricCardConfig; value: any; change?: number }) {
  const trend = change !== undefined ? (change >= 0 ? 'up' : 'down') : undefined;
  const icon = iconMap[config.icon || 'default'] || iconMap['default'];
  
  const formatValue = (val: any): string => {
    if (val === undefined || val === null) return '--';
    if (config.format === 'currency') return `$${Number(val).toLocaleString()}`;
    if (config.format === 'percent') return `${val}%`;
    return typeof val === 'number' ? val.toLocaleString() : String(val);
  };

  return (
    <div className="theme-card rounded-2xl p-6">
      <div className="flex items-center justify-between mb-4">
        <div className={`w-12 h-12 rounded-xl flex items-center justify-center ${
          trend === 'up' ? 'bg-emerald-500/20 text-emerald-400' : 
          trend === 'down' ? 'bg-red-500/20 text-red-400' : 
          'bg-alpha-500/20 text-alpha-400'
        }`}>
          {icon}
        </div>
        {config.showTrend !== false && change !== undefined && (
          <div className={`flex items-center gap-1 text-sm font-medium ${
            trend === 'up' ? 'text-emerald-400' : 'text-red-400'
          }`}>
            {trend === 'up' ? <TrendingUp className="w-4 h-4" /> : <TrendingDown className="w-4 h-4" />}
            {change > 0 ? '+' : ''}{change.toFixed(1)}%
          </div>
        )}
      </div>
      <p className="text-sm theme-text-muted mb-1">{config.title}</p>
      <p className="text-3xl font-bold theme-text-title">{formatValue(value)}</p>
    </div>
  );
}

// Dynamic Bar Chart Component
function DynamicBarChart({ config, data }: { config: ChartConfig; data?: number[] }) {
  const chartData = data || [65, 45, 75, 55, 80, 70, 90];
  const days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
  
  return (
    <div className="theme-card rounded-2xl p-6">
      <h3 className="font-semibold theme-text-title mb-4">{config.title}</h3>
      <div className="h-64 flex items-end gap-2">
        {chartData.map((height, i) => (
          <div key={i} className="flex-1 flex flex-col items-center gap-2">
            <div
              className="w-full bg-gradient-to-t from-alpha-600 to-alpha-400 rounded-t-lg transition-all duration-500"
              style={{ height: `${height}%` }}
            />
            <span className="text-xs theme-text-muted">{days[i] || i + 1}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

// Dynamic Pie Chart Component
function DynamicPieChart({ config, data }: { config: ChartConfig; data?: { label: string; value: number; color: string }[] }) {
  const chartData = data || [
    { label: 'Category A', value: 30, color: '#8b5cf6' },
    { label: 'Category B', value: 25, color: '#06b6d4' },
    { label: 'Category C', value: 20, color: '#10b981' },
    { label: 'Category D', value: 25, color: '#f59e0b' },
  ];
  
  return (
    <div className="theme-card rounded-2xl p-6">
      <h3 className="font-semibold theme-text-title mb-4">{config.title}</h3>
      <div className="h-64 flex items-center justify-center">
        <div className="relative w-48 h-48">
          <svg className="w-full h-full transform -rotate-90">
            <circle cx="96" cy="96" r="80" fill="none" stroke="var(--card-bg)" strokeWidth="32" />
            {chartData.map((item, i) => {
              const offset = chartData.slice(0, i).reduce((sum, d) => sum + d.value, 0);
              return (
                <circle
                  key={i}
                  cx="96"
                  cy="96"
                  r="80"
                  fill="none"
                  stroke={item.color}
                  strokeWidth="32"
                  strokeDasharray={`${item.value * 5.03} 503`}
                  strokeDashoffset={-offset * 5.03}
                />
              );
            })}
          </svg>
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="text-center">
              <p className="text-2xl font-bold theme-text-title">
                {chartData.reduce((sum, d) => sum + d.value, 0)}
              </p>
              <p className="text-sm theme-text-muted">Total</p>
            </div>
          </div>
        </div>
      </div>
      <div className="flex justify-center gap-4 mt-4">
        {chartData.map((item) => (
          <div key={item.label} className="flex items-center gap-2">
            <div className="w-3 h-3 rounded-full" style={{ backgroundColor: item.color }} />
            <span className="text-sm theme-text-muted">{item.label}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

// Dynamic Table Component
function DynamicTable({ config, data }: { config: TableConfig; data?: Record<string, any>[] }) {
  const tableData = data || [];
  
  return (
    <div className="theme-card rounded-2xl p-6">
      <h3 className="font-semibold theme-text-title mb-4">{config.title}</h3>
      <div className="overflow-x-auto">
        <table className="w-full">
          <thead>
            <tr className="border-b theme-border">
              {config.columns.map((col) => (
                <th key={col.key} className="text-left py-3 px-4 text-sm font-medium theme-text-muted">
                  {col.label}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {tableData.map((row, i) => (
              <tr key={i} className="border-b theme-border hover:bg-[var(--card-hover)]">
                {config.columns.map((col) => (
                  <td key={col.key} className="py-3 px-4 text-sm theme-text-secondary">
                    {row[col.key]}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

// Main Dynamic Dashboard Component
export default function DynamicDashboard({ layout, data = {}, onRefresh }: DynamicDashboardProps) {
  const [isLive, setIsLive] = useState(true);
  const [liveData, setLiveData] = useState<Record<string, any>>(data);

  // Simulate live data updates
  useEffect(() => {
    if (!isLive || !layout.refreshInterval) return;
    
    const interval = setInterval(() => {
      setLiveData(prev => {
        const updated = { ...prev };
        Object.keys(updated).forEach(key => {
          if (typeof updated[key] === 'number') {
            updated[key] = updated[key] + (Math.random() - 0.5) * updated[key] * 0.1;
          }
          if (updated[key]?.change !== undefined) {
            updated[key] = {
              ...updated[key],
              change: updated[key].change + (Math.random() - 0.5) * 2
            };
          }
        });
        return updated;
      });
    }, (layout.refreshInterval || 5) * 1000);

    return () => clearInterval(interval);
  }, [isLive, layout.refreshInterval]);

  const renderComponent = (config: ComponentConfig) => {
    const componentData = liveData[config.id] || {};
    
    switch (config.type) {
      case 'metric_card':
        return (
          <DynamicMetricCard
            key={config.id}
            config={config}
            value={componentData.value}
            change={componentData.change}
          />
        );
      case 'bar_chart':
      case 'line_chart':
      case 'area_chart':
        return <DynamicBarChart key={config.id} config={config} data={componentData.values} />;
      case 'pie_chart':
        return <DynamicPieChart key={config.id} config={config} data={componentData.segments} />;
      case 'table':
        return <DynamicTable key={config.id} config={config} data={componentData.rows} />;
      default:
        return null;
    }
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title">{layout.title}</h1>
          {layout.subtitle && (
            <p className="mt-1 theme-text-secondary">{layout.subtitle}</p>
          )}
        </div>
        <div className="flex items-center gap-4">
          <button
            onClick={() => setIsLive(!isLive)}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-colors ${
              isLive ? 'bg-emerald-500/20 text-emerald-400' : 'bg-slate-700 text-slate-400'
            }`}
          >
            <RefreshCw className={`w-4 h-4 ${isLive ? 'animate-spin' : ''}`} />
            {isLive ? 'Live' : 'Paused'}
          </button>
          {onRefresh && (
            <button
              onClick={onRefresh}
              className="px-4 py-2 rounded-lg bg-alpha-500/20 text-alpha-400 hover:bg-alpha-500/30"
            >
              Refresh Layout
            </button>
          )}
        </div>
      </div>

      {/* Sections */}
      {layout.sections.map((section) => (
        <div key={section.id}>
          {section.title && (
            <h2 className="text-xl font-semibold theme-text-title mb-4">{section.title}</h2>
          )}
          <div className={`grid grid-cols-${section.columns || layout.columns || 4} gap-6`}>
            {section.components.map(renderComponent)}
          </div>
        </div>
      ))}
    </div>
  );
}
