import { useState, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  CheckCircle,
  XCircle,
  RefreshCw,
  Gauge,
  Activity,
  Cpu,
  TrendingUp,
  TrendingDown,
  Wifi,
  WifiOff,
  MoreVertical,
  History,
  RotateCcw,
  Hammer,
  X,
  Network,
  Users,
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/Card';
import { cn } from '../lib/utils';
import { useWebSocket } from '../hooks/useWebSocket';

interface ServiceStatus {
  name: string;
  url: string;
  status: 'healthy' | 'error' | 'checking';
  details?: any;
}

interface RealTimeMetrics {
  activeUsers: number;
  transactionsPerSecond: number;
  avgLatencyMs: number;
  cpuUsage: number;
}

const HEALTH_SERVICES_URL = '/api/health/services';
const CONTAINER_API_URL = '/api/v1/containers';
const STATS_URL = '/api/v1/observability/stats/realtime';

function MetricCard({ 
  label, 
  value, 
  unit, 
  icon, 
  trend, 
  trendLabel 
}: { 
  label: string; 
  value: number; 
  unit?: string; 
  icon: React.ReactNode;
  trend?: 'up' | 'down';
  trendLabel?: string;
}) {
  return (
    <Card>
      <CardContent className="p-5">
        <div className="flex items-start justify-between">
          <div>
            <p className="text-xs uppercase tracking-wide theme-text-muted mb-1">{label}</p>
            <p className="text-3xl font-bold theme-text-title">
              {value}
              {unit && <span className="text-sm font-normal theme-text-muted ml-1">{unit}</span>}
            </p>
          </div>
          <div className="p-2 rounded-lg bg-alpha-500/20">
            {icon}
          </div>
        </div>
        {trendLabel && (
          <div className={cn(
            "flex items-center gap-1 mt-2 text-xs",
            trend === 'up' ? "text-green-400" : trend === 'down' ? "text-green-400" : "theme-text-muted"
          )}>
            {trend === 'up' && <TrendingUp className="w-3 h-3" />}
            {trend === 'down' && <TrendingDown className="w-3 h-3" />}
            <span>{trendLabel}</span>
          </div>
        )}
      </CardContent>
    </Card>
  );
}

export default function SystemMonitorPage() {
  const [services, setServices] = useState<ServiceStatus[]>([]);
  const [openMenu, setOpenMenu] = useState<string | null>(null);
  const [historyModal, setHistoryModal] = useState<{ service: string; data: any[] } | null>(null);
  const [actionLoading, setActionLoading] = useState<string | null>(null);

  const handleServiceAction = async (serviceName: string, action: 'restart' | 'rebuild') => {
    setActionLoading(`${serviceName}-${action}`);
    setOpenMenu(null);
    try {
      const response = await fetch(`${CONTAINER_API_URL}/${serviceName}/${action}`, {
        method: 'POST',
      });
      if (response.ok) {
        console.log(`${action} initiated for ${serviceName}`);
      } else {
        console.error(`Failed to ${action} ${serviceName}`);
      }
    } catch (error) {
      console.error(`Error ${action}ing ${serviceName}:`, error);
    } finally {
      setActionLoading(null);
    }
  };

  const handleViewHistory = async (serviceName: string) => {
    setOpenMenu(null);
    try {
      const response = await fetch(`/api/v1/observability/health/${serviceName}/history`);
      if (response.ok) {
        const data = await response.json();
        setHistoryModal({ service: serviceName, data: data.history || [] });
      } else {
        setHistoryModal({ service: serviceName, data: [] });
      }
    } catch (error) {
      console.error(`Error fetching history for ${serviceName}:`, error);
      setHistoryModal({ service: serviceName, data: [] });
    }
  };

  const navigate = useNavigate();
  const [metrics, setMetrics] = useState<RealTimeMetrics>({
    activeUsers: 0,
    transactionsPerSecond: 0,
    avgLatencyMs: 0,
    cpuUsage: 0
  });

  const { isConnected, lastMessage } = useWebSocket({
    url: 'ws://127.0.0.1:8090/ws',
    onOpen: () => console.log('System Monitor connected to websocket'),
  });

  const fetchRealTimeStats = useCallback(async () => {
    try {
      const response = await fetch(STATS_URL);
      if (response.ok) {
        const data = await response.json();
        setMetrics({
          activeUsers: data.activeConnections || 0,
          transactionsPerSecond: data.messagesPerSecond || 0,
          avgLatencyMs: data.avgLatencyMs || 0,
          cpuUsage: data.cpuUsage || 0
        });
      }
    } catch (error) {
      console.error('Error fetching real-time stats:', error);
    }
  }, [metrics]);

  useEffect(() => {
    fetchRealTimeStats();
    const interval = setInterval(fetchRealTimeStats, 5000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    if (lastMessage && lastMessage.type === 'dashboard_update') {
      setMetrics(prev => ({ ...prev, ...lastMessage.payload }));
    }
  }, [lastMessage]);

  useEffect(() => {
    const checkServices = async () => {
      try {
        const response = await fetch(HEALTH_SERVICES_URL);
        if (response.ok) {
          const data = await response.json();
          const serviceStatuses: ServiceStatus[] = data.services.map((svc: any) => ({
            name: svc.service || svc.name,
            url: svc.url,
            status: svc.status === 'healthy' ? 'healthy' : 'error',
            details: svc.details
          }));
          setServices(serviceStatuses);
        } else {
          console.error('Failed to fetch service health:', response.status);
        }
      } catch (error) {
        console.error('Error checking services:', error);
      }
    };

    checkServices();
    const interval = setInterval(checkServices, 30000);
    return () => clearInterval(interval);
  }, []);

  const healthyCount = services.filter(s => s.status === 'healthy').length;
  const errorCount = services.filter(s => s.status === 'error').length;
  const checkingCount = services.filter(s => s.status === 'checking').length;

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title tracking-wide">System Monitor</h1>
          <p className="theme-text-muted mt-1">Real-time monitoring of all Analytics Engine services and system metrics</p>
        </div>
        <div className="flex items-center gap-3">
          <button
            onClick={() => navigate('/deployment/traffic')}
            className="flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors"
          >
            <Network className="w-4 h-4" />
            Service Traffic
          </button>
          <div className={cn(
          "flex items-center gap-2 px-3 py-2 rounded-full border text-sm",
          isConnected 
            ? "bg-green-500/10 border-green-500/30 text-green-400"
            : "bg-gray-500/10 border-gray-500/30 theme-text-muted"
        )}>
            {isConnected ? <Wifi className="w-4 h-4" /> : <WifiOff className="w-4 h-4" />}
            {isConnected ? "Live Stream Connected" : "Connecting Stream..."}
          </div>
        </div>
      </div>

      {/* System Health Summary */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card className="bg-green-500/10 border-green-500/30">
          <CardContent className="p-5">
            <p className="text-4xl font-bold text-green-400">{healthyCount}/{services.length}</p>
            <p className="text-sm text-green-400/80">Services Healthy</p>
          </CardContent>
        </Card>
        <Card className={cn(
          errorCount > 0 ? "bg-red-500/10 border-red-500/30" : "theme-card-bg"
        )}>
          <CardContent className="p-5">
            <p className={cn("text-4xl font-bold", errorCount > 0 ? "text-red-400" : "theme-text-title")}>
              {errorCount}
            </p>
            <p className={cn("text-sm", errorCount > 0 ? "text-red-400/80" : "theme-text-muted")}>
              Services Down
            </p>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="p-5">
            <p className="text-4xl font-bold theme-text-title">{checkingCount}</p>
            <p className="text-sm theme-text-muted">Checking...</p>
          </CardContent>
        </Card>
      </div>

      {/* Real-time System Metrics */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Activity className="w-5 h-5 theme-info-icon" />
            Real-time System Metrics
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <MetricCard
              label="Active Users"
              value={metrics.activeUsers}
              icon={<Users className="w-5 h-5 text-alpha-500" />}
              trend="up"
              trendLabel="+12% since last hour"
            />
            <MetricCard
              label="TPS"
              value={metrics.transactionsPerSecond}
              icon={<Activity className="w-5 h-5 text-alpha-500" />}
              trendLabel="High Load"
            />
            <MetricCard
              label="Avg Latency"
              value={metrics.avgLatencyMs}
              unit="ms"
              icon={<Gauge className="w-5 h-5 text-alpha-500" />}
              trend="down"
              trendLabel="Improving"
            />
            <div className="p-5 rounded-xl theme-card-bg border theme-border">
              <div className="flex items-start justify-between">
                <div>
                  <p className="text-xs uppercase tracking-wide theme-text-muted mb-1">System CPU</p>
                  <p className="text-3xl font-bold theme-text-title">{metrics.cpuUsage}%</p>
                </div>
                <div className="relative w-12 h-12">
                  <svg className="w-12 h-12 -rotate-90">
                    <circle
                      cx="24"
                      cy="24"
                      r="20"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="4"
                      className="text-alpha-faded-200 dark:text-alpha-faded-800"
                    />
                    <circle
                      cx="24"
                      cy="24"
                      r="20"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="4"
                      strokeDasharray={`${metrics.cpuUsage * 1.26} 126`}
                      className={metrics.cpuUsage > 80 ? "text-red-500" : "text-alpha-500"}
                    />
                  </svg>
                  <Cpu className="w-4 h-4 absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 theme-text-muted" />
                </div>
              </div>
              <p className="text-xs theme-text-muted mt-2">4 Cores Active</p>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Service Status Table */}
      <Card>
        <CardHeader>
          <CardTitle>All Services Status</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b theme-border">
                  <th className="px-4 py-3 text-left theme-text-muted font-medium">Service Name</th>
                  <th className="px-4 py-3 text-left theme-text-muted font-medium">Status</th>
                  <th className="px-4 py-3 text-left theme-text-muted font-medium">Endpoint</th>
                  <th className="px-4 py-3 text-left theme-text-muted font-medium">Details</th>
                  <th className="px-4 py-3 text-right theme-text-muted font-medium">Actions</th>
                </tr>
              </thead>
              <tbody>
                {services.map((service) => (
                  <tr key={service.name} className="border-b theme-border hover:theme-card-bg-hover">
                    <td className="px-4 py-3">
                      <div className="flex items-center gap-2">
                        {service.status === 'healthy' && <CheckCircle className="w-4 h-4 text-green-500" />}
                        {service.status === 'error' && <XCircle className="w-4 h-4 text-red-500" />}
                        {service.status === 'checking' && <RefreshCw className="w-4 h-4 theme-text-muted animate-spin" />}
                        <span className="theme-text">{service.name}</span>
                      </div>
                    </td>
                    <td className="px-4 py-3">
                      <span className={cn(
                        "px-2 py-1 rounded-full text-xs font-medium",
                        service.status === 'healthy' && "bg-green-500/20 text-green-400",
                        service.status === 'error' && "bg-red-500/20 text-red-400",
                        service.status === 'checking' && "bg-gray-500/20 theme-text-muted"
                      )}>
                        {service.status === 'healthy' ? 'Healthy' : service.status === 'error' ? 'Error' : 'Checking...'}
                      </span>
                    </td>
                    <td className="px-4 py-3">
                      <code className="text-xs theme-text-muted">{service.url}</code>
                    </td>
                    <td className="px-4 py-3">
                      {service.details && (
                        <span className="text-xs theme-text-muted">
                          {service.details.service || 'OK'}
                        </span>
                      )}
                    </td>
                    <td className="px-4 py-3 text-right relative">
                      {actionLoading === `${service.name}-restart` || actionLoading === `${service.name}-rebuild` ? (
                        <RefreshCw className="w-4 h-4 animate-spin inline-block theme-text-muted" />
                      ) : (
                        <button
                          onClick={() => setOpenMenu(openMenu === service.name ? null : service.name)}
                          className="p-1 rounded hover:bg-alpha-500/20 transition-colors"
                        >
                          <MoreVertical className="w-4 h-4 theme-text-muted" />
                        </button>
                      )}
                      {openMenu === service.name && (
                        <div className="absolute right-0 top-full mt-1 w-48 rounded-lg shadow-lg theme-card-bg border theme-border z-50">
                          <button
                            onClick={() => handleViewHistory(service.name)}
                            className="w-full px-4 py-2 text-left text-sm theme-text hover:bg-alpha-500/10 flex items-center gap-2 rounded-t-lg"
                          >
                            <History className="w-4 h-4" />
                            View History
                          </button>
                          <button
                            onClick={() => handleServiceAction(service.name, 'restart')}
                            className="w-full px-4 py-2 text-left text-sm theme-text hover:bg-alpha-500/10 flex items-center gap-2"
                          >
                            <RotateCcw className="w-4 h-4" />
                            Restart Container
                          </button>
                          <button
                            onClick={() => handleServiceAction(service.name, 'rebuild')}
                            className="w-full px-4 py-2 text-left text-sm text-amber-400 hover:bg-amber-500/10 flex items-center gap-2 rounded-b-lg"
                          >
                            <Hammer className="w-4 h-4" />
                            Rebuild (No Cache)
                          </button>
                        </div>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </CardContent>
      </Card>

      {/* History Modal */}
      {historyModal && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="theme-card-bg rounded-xl shadow-2xl w-full max-w-2xl mx-4 max-h-[80vh] flex flex-col">
            <div className="flex items-center justify-between p-4 border-b theme-border">
              <h3 className="text-lg font-semibold theme-text">
                Health History: {historyModal.service}
              </h3>
              <button
                onClick={() => setHistoryModal(null)}
                className="p-1 rounded hover:bg-alpha-500/20 transition-colors"
              >
                <X className="w-5 h-5 theme-text-muted" />
              </button>
            </div>
            <div className="p-4 overflow-y-auto flex-1">
              {historyModal.data.length === 0 ? (
                <p className="text-center theme-text-muted py-8">
                  No health history available yet. History will be recorded as services push their status.
                </p>
              ) : (
                <table className="w-full text-sm">
                  <thead>
                    <tr className="border-b theme-border">
                      <th className="px-3 py-2 text-left theme-text-muted">Timestamp</th>
                      <th className="px-3 py-2 text-left theme-text-muted">Status</th>
                      <th className="px-3 py-2 text-left theme-text-muted">Details</th>
                    </tr>
                  </thead>
                  <tbody>
                    {historyModal.data.map((entry: any, idx: number) => (
                      <tr key={idx} className="border-b theme-border">
                        <td className="px-3 py-2 theme-text-muted text-xs">
                          {new Date(entry.timestamp).toLocaleString()}
                        </td>
                        <td className="px-3 py-2">
                          <span className={cn(
                            "px-2 py-0.5 rounded-full text-xs",
                            entry.status === 'healthy' && "bg-green-500/20 text-green-400",
                            entry.status !== 'healthy' && "bg-red-500/20 text-red-400"
                          )}>
                            {entry.status}
                          </span>
                        </td>
                        <td className="px-3 py-2 theme-text-muted text-xs">
                          {entry.details ? JSON.stringify(entry.details).slice(0, 50) : '-'}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
