import { useState, useEffect } from 'react';
import { PieChart, TrendingUp, TrendingDown, DollarSign, Users, Package, ChevronRight, ChevronLeft, RefreshCw, Sparkles } from 'lucide-react';

interface MetricCard {
  id: string;
  name: string;
  value: string;
  change: number;
  trend: 'up' | 'down';
  icon: React.ReactNode;
}

const metrics: MetricCard[] = [
  { id: 'revenue', name: 'Total Revenue', value: '$1.2M', change: 12.5, trend: 'up', icon: <DollarSign className="w-6 h-6" /> },
  { id: 'customers', name: 'Active Customers', value: '8,432', change: 8.2, trend: 'up', icon: <Users className="w-6 h-6" /> },
  { id: 'orders', name: 'Orders Today', value: '1,847', change: -2.4, trend: 'down', icon: <Package className="w-6 h-6" /> },
  { id: 'conversion', name: 'Conversion Rate', value: '3.8%', change: 0.5, trend: 'up', icon: <TrendingUp className="w-6 h-6" /> },
];

export default function SampleAnalyticsPage() {
  const [liveData, setLiveData] = useState(metrics);
  const [isLive, setIsLive] = useState(true);

  useEffect(() => {
    if (!isLive) return;

    const interval = setInterval(() => {
      setLiveData((prev) =>
        prev.map((m) => ({
          ...m,
          change: parseFloat((m.change + (Math.random() - 0.5) * 2).toFixed(1)),
        }))
      );
    }, 3000);

    return () => clearInterval(interval);
  }, [isLive]);

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title">Sample Analytics</h1>
          <p className="mt-2 theme-text-secondary">
            Your designed dashboards powered by simulated data
          </p>
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
          <div className="flex items-center gap-2 px-4 py-2 rounded-lg bg-alpha-500/10 text-alpha-400">
            <PieChart className="w-5 h-5" />
            <span className="font-medium">Step 5 of 6</span>
          </div>
        </div>
      </div>

      {/* Success Banner */}
      <div className="theme-card rounded-2xl p-6 bg-gradient-to-r from-emerald-500/10 to-alpha-500/10 border border-emerald-500/20">
        <div className="flex items-center gap-4">
          <div className="w-14 h-14 rounded-2xl bg-gradient-to-br from-emerald-500 to-alpha-500 flex items-center justify-center">
            <Sparkles className="w-7 h-7 text-white" />
          </div>
          <div className="flex-1">
            <h2 className="text-xl font-semibold theme-text-title">Your Analytics Are Live!</h2>
            <p className="theme-text-secondary">
              This is exactly what your dashboards will look like with real data.
              These metrics are based on your interview selections and powered by the simulator.
            </p>
          </div>
        </div>
      </div>

      {/* Metric Cards */}
      <div className="grid grid-cols-4 gap-6">
        {liveData.map((metric) => (
          <div key={metric.id} className="theme-card rounded-2xl p-6">
            <div className="flex items-center justify-between mb-4">
              <div className={`w-12 h-12 rounded-xl flex items-center justify-center ${
                metric.trend === 'up' ? 'bg-emerald-500/20 text-emerald-400' : 'bg-red-500/20 text-red-400'
              }`}>
                {metric.icon}
              </div>
              <div className={`flex items-center gap-1 text-sm font-medium ${
                metric.trend === 'up' ? 'text-emerald-400' : 'text-red-400'
              }`}>
                {metric.trend === 'up' ? <TrendingUp className="w-4 h-4" /> : <TrendingDown className="w-4 h-4" />}
                {metric.change > 0 ? '+' : ''}{metric.change}%
              </div>
            </div>
            <p className="text-sm theme-text-muted mb-1">{metric.name}</p>
            <p className="text-3xl font-bold theme-text-title">{metric.value}</p>
          </div>
        ))}
      </div>

      {/* Charts Row */}
      <div className="grid grid-cols-2 gap-6">
        {/* Revenue Chart */}
        <div className="theme-card rounded-2xl p-6">
          <div className="flex items-center justify-between mb-6">
            <h3 className="font-semibold theme-text-title">Revenue Trend</h3>
            <select className="px-3 py-1 rounded-lg theme-bg-secondary text-sm theme-text-secondary">
              <option>Last 7 days</option>
              <option>Last 30 days</option>
              <option>Last 90 days</option>
            </select>
          </div>
          {/* Placeholder Chart */}
          <div className="h-64 flex items-end gap-2">
            {[65, 45, 75, 55, 80, 70, 90].map((height, i) => (
              <div key={i} className="flex-1 flex flex-col items-center gap-2">
                <div
                  className="w-full bg-gradient-to-t from-alpha-600 to-alpha-400 rounded-t-lg transition-all duration-500"
                  style={{ height: `${height}%` }}
                />
                <span className="text-xs theme-text-muted">
                  {['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][i]}
                </span>
              </div>
            ))}
          </div>
        </div>

        {/* Distribution Chart */}
        <div className="theme-card rounded-2xl p-6">
          <div className="flex items-center justify-between mb-6">
            <h3 className="font-semibold theme-text-title">Order Distribution</h3>
            <span className="text-sm theme-text-muted">By Category</span>
          </div>
          {/* Placeholder Pie */}
          <div className="h-64 flex items-center justify-center">
            <div className="relative w-48 h-48">
              <svg className="w-full h-full transform -rotate-90">
                <circle cx="96" cy="96" r="80" fill="none" stroke="var(--card-bg)" strokeWidth="32" />
                <circle cx="96" cy="96" r="80" fill="none" stroke="#8b5cf6" strokeWidth="32" strokeDasharray="150 503" />
                <circle cx="96" cy="96" r="80" fill="none" stroke="#06b6d4" strokeWidth="32" strokeDasharray="125 503" strokeDashoffset="-150" />
                <circle cx="96" cy="96" r="80" fill="none" stroke="#10b981" strokeWidth="32" strokeDasharray="100 503" strokeDashoffset="-275" />
                <circle cx="96" cy="96" r="80" fill="none" stroke="#f59e0b" strokeWidth="32" strokeDasharray="128 503" strokeDashoffset="-375" />
              </svg>
              <div className="absolute inset-0 flex items-center justify-center">
                <div className="text-center">
                  <p className="text-2xl font-bold theme-text-title">1,847</p>
                  <p className="text-sm theme-text-muted">Total</p>
                </div>
              </div>
            </div>
          </div>
          {/* Legend */}
          <div className="flex justify-center gap-6 mt-4">
            {[
              { color: 'bg-purple-500', label: 'Electronics' },
              { color: 'bg-cyan-500', label: 'Clothing' },
              { color: 'bg-emerald-500', label: 'Home' },
              { color: 'bg-amber-500', label: 'Other' },
            ].map((item) => (
              <div key={item.label} className="flex items-center gap-2">
                <div className={`w-3 h-3 rounded-full ${item.color}`} />
                <span className="text-sm theme-text-muted">{item.label}</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* KPI Table */}
      <div className="theme-card rounded-2xl p-6">
        <h3 className="font-semibold theme-text-title mb-4">Selected KPIs Performance</h3>
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead>
              <tr className="border-b theme-border">
                <th className="text-left py-3 px-4 text-sm font-medium theme-text-muted">KPI Name</th>
                <th className="text-left py-3 px-4 text-sm font-medium theme-text-muted">Category</th>
                <th className="text-right py-3 px-4 text-sm font-medium theme-text-muted">Current</th>
                <th className="text-right py-3 px-4 text-sm font-medium theme-text-muted">Target</th>
                <th className="text-right py-3 px-4 text-sm font-medium theme-text-muted">Status</th>
              </tr>
            </thead>
            <tbody>
              {[
                { name: 'Customer Satisfaction Score', category: 'Customer Service', current: '87%', target: '85%', status: 'above' },
                { name: 'Order Fulfillment Rate', category: 'Operations', current: '94%', target: '95%', status: 'below' },
                { name: 'Average Order Value', category: 'Sales', current: '$156', target: '$150', status: 'above' },
                { name: 'Inventory Turnover', category: 'Supply Chain', current: '8.2', target: '8.0', status: 'above' },
                { name: 'Employee Productivity', category: 'HR', current: '112%', target: '110%', status: 'above' },
              ].map((kpi, i) => (
                <tr key={i} className="border-b theme-border hover:bg-[var(--card-hover)]">
                  <td className="py-3 px-4 font-medium theme-text-title">{kpi.name}</td>
                  <td className="py-3 px-4 text-sm theme-text-secondary">{kpi.category}</td>
                  <td className="py-3 px-4 text-right font-medium theme-text-title">{kpi.current}</td>
                  <td className="py-3 px-4 text-right text-sm theme-text-muted">{kpi.target}</td>
                  <td className="py-3 px-4 text-right">
                    <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                      kpi.status === 'above' ? 'bg-emerald-500/20 text-emerald-400' : 'bg-amber-500/20 text-amber-400'
                    }`}>
                      {kpi.status === 'above' ? 'On Track' : 'Needs Attention'}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Navigation */}
      <div className="flex justify-between">
        <a
          href="/demo/simulator"
          className="px-6 py-3 rounded-xl theme-card hover:bg-[var(--card-hover)] font-medium transition-colors flex items-center gap-2"
        >
          <ChevronLeft className="w-5 h-5" />
          Back to Simulator
        </a>
        <a
          href="/demo/summary"
          className="px-6 py-3 rounded-xl bg-alpha-500 hover:bg-alpha-600 text-white font-medium transition-colors flex items-center gap-2"
        >
          View Executive Summary
          <ChevronRight className="w-5 h-5" />
        </a>
      </div>
    </div>
  );
}
