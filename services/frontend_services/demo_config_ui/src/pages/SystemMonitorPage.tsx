import { useState, useEffect } from 'react';
import {
  CheckCircle,
  XCircle,
  RefreshCw,
  Users,
  Gauge,
  Activity,
  Cpu,
  TrendingUp,
  TrendingDown,
  Wifi,
  WifiOff,
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

const ALL_SERVICES = [
  { name: 'Database Service', url: 'http://localhost:8000/health' },
  { name: 'Messaging Service', url: 'http://localhost:8002/health' },
  { name: 'Observability Service', url: 'http://localhost:8080/health' },
  { name: 'Archival Service', url: 'http://localhost:8005/health' },
  { name: 'Business Metadata', url: 'http://localhost:8020/health' },
  { name: 'Calculation Engine', url: 'http://localhost:8021/health' },
  { name: 'Demo Config Service', url: 'http://localhost:8022/health' },
  { name: 'Connector Service', url: 'http://localhost:8023/health' },
  { name: 'Ingestion Service', url: 'http://localhost:8024/health' },
  { name: 'Metadata Ingestion', url: 'http://localhost:8025/health' },
  { name: 'Conversation Service', url: 'http://localhost:8026/health' },
  { name: 'Systems Monitor', url: 'http://localhost:8010/health' },
  { name: 'Entity Resolution', url: 'http://localhost:8012/health' },
  { name: 'Data Governance', url: 'http://localhost:8013/health' },
  { name: 'Machine Learning', url: 'http://localhost:8014/health' },
  { name: 'API Gateway', url: 'http://127.0.0.1:8090/health' },
];

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
  const [services, setServices] = useState<ServiceStatus[]>(
    ALL_SERVICES.map(s => ({ ...s, status: 'checking' as const }))
  );

  const [metrics, setMetrics] = useState<RealTimeMetrics>({
    activeUsers: 142,
    transactionsPerSecond: 45,
    avgLatencyMs: 120,
    cpuUsage: 35
  });

  const { isConnected, lastMessage } = useWebSocket({
    url: 'ws://127.0.0.1:8090/ws',
    onOpen: () => console.log('System Monitor connected to websocket'),
  });

  useEffect(() => {
    if (lastMessage && lastMessage.type === 'dashboard_update') {
      setMetrics(prev => ({ ...prev, ...lastMessage.payload }));
    }
  }, [lastMessage]);

  useEffect(() => {
    if (!isConnected) return;

    const interval = setInterval(() => {
      setMetrics(prev => ({
        activeUsers: Math.max(0, prev.activeUsers + Math.floor(Math.random() * 10) - 5),
        transactionsPerSecond: Math.max(0, prev.transactionsPerSecond + Math.floor(Math.random() * 20) - 10),
        avgLatencyMs: Math.max(0, 100 + Math.floor(Math.random() * 50) - 25),
        cpuUsage: Math.min(100, Math.max(0, prev.cpuUsage + Math.floor(Math.random() * 10) - 5))
      }));
    }, 2000);

    return () => clearInterval(interval);
  }, [isConnected]);

  useEffect(() => {
    const checkServices = () => {
      services.forEach((service, index) => {
        fetch(service.url)
          .then(res => res.json())
          .then(data => {
            setServices(prev => {
              const updated = [...prev];
              updated[index] = { ...updated[index], status: 'healthy', details: data };
              return updated;
            });
          })
          .catch(() => {
            setServices(prev => {
              const updated = [...prev];
              updated[index] = { ...updated[index], status: 'error' };
              return updated;
            });
          });
      });
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
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
