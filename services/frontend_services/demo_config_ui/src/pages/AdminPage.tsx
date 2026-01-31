import React, { useState, useEffect } from 'react';
import {
  Key,
  HeartPulse,
  Trash2,
  Bell,
  Terminal,
  CheckCircle,
  XCircle,
  AlertTriangle,
  Save,
  RefreshCw,
  Square,
  Play,
  Shield,
  Eye,
  EyeOff,
  Loader2,
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { cn } from '../lib/utils';
import { configApi, ClientConfig } from '../api/configApi';

interface LogEntry {
  timestamp: string;
  level: 'INFO' | 'WARN' | 'ERROR' | 'DEBUG';
  service: string;
  message: string;
}

const SERVICES = [
  'API Gateway', 'Metadata Service', 'Calculation Engine',
  'Config Service', 'Ingestion Service', 'Entity Resolution',
];

function TabButton({ active, onClick, icon, children }: { 
  active: boolean; onClick: () => void; icon: React.ReactNode; children: React.ReactNode;
}) {
  return (
    <button
      onClick={onClick}
      className={cn(
        "flex items-center gap-2 px-4 py-3 text-sm font-medium transition-colors border-b-2",
        active ? "text-alpha-500 border-alpha-500" : "theme-text-muted border-transparent hover:theme-text"
      )}
    >
      {icon}
      {children}
    </button>
  );
}

export default function AdminPage() {
  const [tabValue, setTabValue] = useState(0);
  const [loading, setLoading] = useState(false);
  const [config, setConfig] = useState<ClientConfig | null>(null);
  const [healthStatus, setHealthStatus] = useState<Record<string, string>>({});
  const [licenseKey, setLicenseKey] = useState('');
  const [logs, setLogs] = useState<LogEntry[]>([]);
  const [isLive, setIsLive] = useState(true);
  
  const [retentionSettings, setRetentionSettings] = useState({
    logRetentionDays: 30, dataRetentionDays: 365, archiveEnabled: true,
  });

  // API Key Management State
  const [anthropicApiKey, setAnthropicApiKey] = useState('');
  const [showApiKey, setShowApiKey] = useState(false);
  const [apiKeyStatus, setApiKeyStatus] = useState<'unknown' | 'checking' | 'valid' | 'invalid' | 'not_set'>('unknown');
  const [apiKeySaving, setApiKeySaving] = useState(false);

  const [alertSettings, setAlertSettings] = useState({
    emailNotifications: true, slackNotifications: false, errorThreshold: 10, emailAddress: 'admin@example.com',
  });

  useEffect(() => { fetchConfig(); checkHealth(); checkApiKeyStatus(); }, []);

  const checkApiKeyStatus = async () => {
    setApiKeyStatus('checking');
    try {
      const response = await fetch('/api/v1/admin/api-keys/anthropic/status');
      if (response.ok) {
        const data = await response.json();
        setApiKeyStatus(data.configured ? (data.valid ? 'valid' : 'invalid') : 'not_set');
      } else {
        setApiKeyStatus('unknown');
      }
    } catch (error) {
      console.error('Error checking API key status:', error);
      setApiKeyStatus('unknown');
    }
  };

  const handleSaveApiKey = async () => {
    if (!anthropicApiKey.trim()) return;
    setApiKeySaving(true);
    try {
      const response = await fetch('/api/v1/admin/api-keys/anthropic', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ api_key: anthropicApiKey }),
      });
      if (response.ok) {
        const data = await response.json();
        setApiKeyStatus(data.valid ? 'valid' : 'invalid');
        setAnthropicApiKey('');
        setShowApiKey(false);
        if (data.valid) {
          alert('API key saved and verified successfully!');
        } else {
          alert('API key saved but verification failed. Please check if the key is correct.');
        }
      } else {
        alert('Failed to save API key');
      }
    } catch (error) {
      console.error('Error saving API key:', error);
      alert('Failed to save API key');
    } finally {
      setApiKeySaving(false);
    }
  };

  useEffect(() => {
    if (!isLive) return;
    const interval = setInterval(() => {
      const services = ['API Gateway', 'Calculation Engine', 'Metadata Service', 'Ingestion'];
      const levels: LogEntry['level'][] = ['INFO', 'INFO', 'INFO', 'WARN', 'DEBUG', 'ERROR'];
      const messages = [
        'Processing request id: req_' + Math.floor(Math.random() * 10000),
        'Cache hit for key: kpi_' + Math.floor(Math.random() * 100),
        'Database connection pool utilization: ' + Math.floor(Math.random() * 100) + '%',
        'Received heartbeat from service', 'Batch job started',
        'Batch job completed in ' + Math.floor(Math.random() * 500) + 'ms',
        'Connection timeout retrying...', 'Schema validation failed for object order_123'
      ];
      const newLog: LogEntry = {
        timestamp: new Date().toISOString(),
        service: services[Math.floor(Math.random() * services.length)],
        level: levels[Math.floor(Math.random() * levels.length)],
        message: messages[Math.floor(Math.random() * messages.length)]
      };
      setLogs(prev => [...prev.slice(-99), newLog]);
    }, 1500);
    return () => clearInterval(interval);
  }, [isLive]);

  const fetchConfig = async () => {
    setLoading(true);
    try {
      const configs = await configApi.getClientConfigs();
      if (configs.length > 0) { setConfig(configs[0]); setLicenseKey(configs[0].license_key || ''); }
    } catch (error) { console.error('Error fetching config:', error); }
    finally { setLoading(false); }
  };

  const checkHealth = async () => {
    const status: Record<string, string> = {};
    SERVICES.forEach(service => { status[service] = Math.random() > 0.1 ? 'healthy' : 'degraded'; });
    setHealthStatus(status);
  };

  const handleUpdateLicense = async () => {
    if (!config) return;
    try {
      await configApi.updateClientConfig(config.client_id, { license_key: licenseKey });
      alert('License key updated successfully');
    } catch (error) { alert('Failed to update license key'); }
  };

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'healthy': return <CheckCircle className="w-5 h-5 text-green-500" />;
      case 'degraded': return <AlertTriangle className="w-5 h-5 text-amber-500" />;
      case 'down': return <XCircle className="w-5 h-5 text-red-500" />;
      default: return <XCircle className="w-5 h-5 theme-text-muted" />;
    }
  };

  const getLogColor = (level: string) => {
    switch (level) {
      case 'ERROR': return 'text-red-400';
      case 'WARN': return 'text-amber-400';
      case 'DEBUG': return 'text-blue-400';
      default: return 'text-green-400';
    }
  };

  return (
    <div className="space-y-6 animate-fade-in">
      <div>
        <h1 className="text-3xl font-bold theme-text-title tracking-wide">Administration</h1>
        <p className="theme-text-muted mt-1">System configuration, health monitoring, and settings</p>
      </div>

      {loading && (
        <div className="h-1 bg-alpha-faded-200 dark:bg-alpha-faded-800 rounded overflow-hidden">
          <div className="h-full bg-alpha-500 animate-pulse" style={{ width: '60%' }} />
        </div>
      )}

      {/* Tabs */}
      <div className="border-b theme-border">
        <div className="flex flex-wrap">
          <TabButton active={tabValue === 0} onClick={() => setTabValue(0)} icon={<Key className="w-4 h-4" />}>License</TabButton>
          <TabButton active={tabValue === 1} onClick={() => setTabValue(1)} icon={<HeartPulse className="w-4 h-4" />}>System Health</TabButton>
          <TabButton active={tabValue === 2} onClick={() => setTabValue(2)} icon={<Trash2 className="w-4 h-4" />}>Retention</TabButton>
          <TabButton active={tabValue === 3} onClick={() => setTabValue(3)} icon={<Bell className="w-4 h-4" />}>Alerts</TabButton>
          <TabButton active={tabValue === 4} onClick={() => setTabValue(4)} icon={<Terminal className="w-4 h-4" />}>Live Logs</TabButton>
        </div>
      </div>

      {/* License Tab */}
      {tabValue === 0 && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <Card>
            <CardHeader>
              <CardTitle>License Configuration</CardTitle>
              <p className="text-sm theme-text-muted">Manage your enterprise license</p>
            </CardHeader>
            <CardContent className="space-y-4">
              <div>
                <label className="text-sm font-medium theme-text-title block mb-2">License Key</label>
                <input
                  type="password"
                  value={licenseKey}
                  onChange={(e) => setLicenseKey(e.target.value)}
                  className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                />
                <p className="text-xs theme-text-muted mt-1">Enter your 32-character enterprise license key</p>
              </div>
              <div className="flex items-center gap-2">
                <span className="text-sm theme-text-muted">Status:</span>
                <span className={cn("px-2 py-0.5 rounded-full text-xs font-medium", licenseKey ? "bg-green-500/20 text-green-400" : "bg-gray-500/20 theme-text-muted")}>
                  {licenseKey ? "Active" : "No License"}
                </span>
              </div>
              <Button onClick={handleUpdateLicense} disabled={!config}>
                <Save className="w-4 h-4 mr-2" />
                Update License
              </Button>
            </CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle>License Details</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="divide-y theme-border">
                {[
                  { label: 'Plan Type', value: 'Enterprise' },
                  { label: 'Expiration Date', value: '2025-12-31' },
                  { label: 'Max Users', value: 'Unlimited' },
                  { label: 'Max Data Storage', value: '10 TB' },
                ].map((item) => (
                  <div key={item.label} className="py-3 flex justify-between">
                    <span className="theme-text-muted">{item.label}</span>
                    <span className="font-medium theme-text">{item.value}</span>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>

          {/* API Keys Section */}
          <Card className="lg:col-span-2">
            <CardHeader>
              <div className="flex items-center gap-2">
                <Shield className="w-5 h-5 text-alpha-500" />
                <CardTitle>AI Service API Keys</CardTitle>
              </div>
              <p className="text-sm theme-text-muted">Configure API keys for AI-powered features</p>
            </CardHeader>
            <CardContent className="space-y-6">
              {/* Anthropic API Key */}
              <div className="p-4 rounded-xl border theme-border theme-card-bg">
                <div className="flex items-center justify-between mb-4">
                  <div>
                    <h4 className="font-semibold theme-text-title">Anthropic API Key</h4>
                    <p className="text-sm theme-text-muted">Required for AI conversation and analysis features</p>
                  </div>
                  <div className="flex items-center gap-2">
                    {apiKeyStatus === 'checking' && (
                      <span className="flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium bg-blue-500/20 text-blue-400">
                        <Loader2 className="w-3 h-3 animate-spin" />
                        Checking...
                      </span>
                    )}
                    {apiKeyStatus === 'valid' && (
                      <span className="flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium bg-green-500/20 text-green-400">
                        <CheckCircle className="w-3 h-3" />
                        Configured & Valid
                      </span>
                    )}
                    {apiKeyStatus === 'invalid' && (
                      <span className="flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium bg-red-500/20 text-red-400">
                        <XCircle className="w-3 h-3" />
                        Invalid Key
                      </span>
                    )}
                    {apiKeyStatus === 'not_set' && (
                      <span className="flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium bg-amber-500/20 text-amber-400">
                        <AlertTriangle className="w-3 h-3" />
                        Not Configured
                      </span>
                    )}
                    {apiKeyStatus === 'unknown' && (
                      <span className="px-2 py-0.5 rounded-full text-xs font-medium bg-gray-500/20 theme-text-muted">
                        Unknown
                      </span>
                    )}
                  </div>
                </div>
                
                <div className="space-y-3">
                  <div className="relative">
                    <input
                      type={showApiKey ? 'text' : 'password'}
                      value={anthropicApiKey}
                      onChange={(e) => setAnthropicApiKey(e.target.value)}
                      placeholder="sk-ant-api03-..."
                      className="w-full px-4 py-3 pr-12 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                    />
                    <button
                      type="button"
                      onClick={() => setShowApiKey(!showApiKey)}
                      className="absolute right-3 top-1/2 -translate-y-1/2 theme-text-muted hover:theme-text"
                    >
                      {showApiKey ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                    </button>
                  </div>
                  <p className="text-xs theme-text-muted">
                    Get your API key from <a href="https://console.anthropic.com/" target="_blank" rel="noopener noreferrer" className="text-alpha-500 hover:underline">console.anthropic.com</a>
                  </p>
                  <div className="flex gap-2">
                    <Button onClick={handleSaveApiKey} disabled={apiKeySaving || !anthropicApiKey.trim()}>
                      {apiKeySaving ? (
                        <>
                          <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                          Saving...
                        </>
                      ) : (
                        <>
                          <Save className="w-4 h-4 mr-2" />
                          Save & Verify Key
                        </>
                      )}
                    </Button>
                    <Button variant="outline" onClick={checkApiKeyStatus}>
                      <RefreshCw className="w-4 h-4 mr-2" />
                      Check Status
                    </Button>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      )}

      {/* System Health Tab */}
      {tabValue === 1 && (
        <div className="space-y-4">
          <div className="flex justify-end">
            <Button variant="outline" onClick={checkHealth}>
              <RefreshCw className="w-4 h-4 mr-2" />
              Refresh Status
            </Button>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {SERVICES.map((service) => (
              <Card key={service}>
                <CardContent className="p-5">
                  <div className="flex items-center justify-between mb-2">
                    <h3 className="font-semibold theme-text-title">{service}</h3>
                    {getStatusIcon(healthStatus[service] || 'unknown')}
                  </div>
                  <p className={cn("text-sm capitalize", 
                    healthStatus[service] === 'healthy' ? "text-green-400" : 
                    healthStatus[service] === 'degraded' ? "text-amber-400" : "theme-text-muted"
                  )}>
                    {healthStatus[service] || 'Unknown'}
                  </p>
                  <p className="text-xs theme-text-muted mt-2">Last check: {new Date().toLocaleTimeString()}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      )}

      {/* Retention Tab */}
      {tabValue === 2 && (
        <Card>
          <CardHeader>
            <CardTitle>Data Retention Policies</CardTitle>
          </CardHeader>
          <CardContent className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label className="text-sm font-medium theme-text-title block mb-2">Log Retention (Days)</label>
                <input
                  type="number"
                  value={retentionSettings.logRetentionDays}
                  onChange={(e) => setRetentionSettings({...retentionSettings, logRetentionDays: parseInt(e.target.value)})}
                  className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                />
                <p className="text-xs theme-text-muted mt-1">How long to keep application logs</p>
              </div>
              <div>
                <label className="text-sm font-medium theme-text-title block mb-2">Historical Data Retention (Days)</label>
                <input
                  type="number"
                  value={retentionSettings.dataRetentionDays}
                  onChange={(e) => setRetentionSettings({...retentionSettings, dataRetentionDays: parseInt(e.target.value)})}
                  className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                />
                <p className="text-xs theme-text-muted mt-1">How long to keep historical analysis data</p>
              </div>
            </div>
            <label className="flex items-center gap-3 cursor-pointer">
              <div className="relative">
                <input
                  type="checkbox"
                  checked={retentionSettings.archiveEnabled}
                  onChange={(e) => setRetentionSettings({...retentionSettings, archiveEnabled: e.target.checked})}
                  className="sr-only peer"
                />
                <div className="w-10 h-6 rounded-full bg-alpha-faded-300 dark:bg-alpha-faded-700 peer-checked:bg-alpha-500 transition-colors"></div>
                <div className="absolute left-1 top-1 w-4 h-4 rounded-full bg-white peer-checked:translate-x-4 transition-transform"></div>
              </div>
              <span className="theme-text">Enable Automatic Archiving</span>
            </label>
            <Button>
              <Save className="w-4 h-4 mr-2" />
              Save Retention Settings
            </Button>
          </CardContent>
        </Card>
      )}

      {/* Alerts Tab */}
      {tabValue === 3 && (
        <Card>
          <CardHeader>
            <CardTitle>Alert Configuration</CardTitle>
          </CardHeader>
          <CardContent className="space-y-6">
            <label className="flex items-center gap-3 cursor-pointer">
              <div className="relative">
                <input type="checkbox" checked={alertSettings.emailNotifications} onChange={(e) => setAlertSettings({...alertSettings, emailNotifications: e.target.checked})} className="sr-only peer" />
                <div className="w-10 h-6 rounded-full bg-alpha-faded-300 dark:bg-alpha-faded-700 peer-checked:bg-alpha-500 transition-colors"></div>
                <div className="absolute left-1 top-1 w-4 h-4 rounded-full bg-white peer-checked:translate-x-4 transition-transform"></div>
              </div>
              <span className="theme-text">Enable Email Notifications</span>
            </label>
            {alertSettings.emailNotifications && (
              <div>
                <label className="text-sm font-medium theme-text-title block mb-2">Alert Email Address</label>
                <input
                  type="email"
                  value={alertSettings.emailAddress}
                  onChange={(e) => setAlertSettings({...alertSettings, emailAddress: e.target.value})}
                  className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                />
              </div>
            )}
            <label className="flex items-center gap-3 cursor-pointer">
              <div className="relative">
                <input type="checkbox" checked={alertSettings.slackNotifications} onChange={(e) => setAlertSettings({...alertSettings, slackNotifications: e.target.checked})} className="sr-only peer" />
                <div className="w-10 h-6 rounded-full bg-alpha-faded-300 dark:bg-alpha-faded-700 peer-checked:bg-alpha-500 transition-colors"></div>
                <div className="absolute left-1 top-1 w-4 h-4 rounded-full bg-white peer-checked:translate-x-4 transition-transform"></div>
              </div>
              <span className="theme-text">Enable Slack Notifications</span>
            </label>
            <div>
              <label className="text-sm font-medium theme-text-title block mb-2">Error Threshold (per minute)</label>
              <input
                type="number"
                value={alertSettings.errorThreshold}
                onChange={(e) => setAlertSettings({...alertSettings, errorThreshold: parseInt(e.target.value)})}
                className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
              />
              <p className="text-xs theme-text-muted mt-1">Trigger alert if error count exceeds this value</p>
            </div>
            <Button>
              <Save className="w-4 h-4 mr-2" />
              Save Alert Settings
            </Button>
          </CardContent>
        </Card>
      )}

      {/* Live Logs Tab */}
      {tabValue === 4 && (
        <Card className="bg-[#1a1a2e] border-[#2a2a4a]">
          <div className="p-4 border-b border-[#2a2a4a] flex items-center justify-between">
            <h3 className="font-semibold text-white">System Logs Stream</h3>
            <div className="flex gap-2">
              <button
                onClick={() => setIsLive(!isLive)}
                className={cn(
                  "flex items-center gap-1 px-3 py-1.5 rounded-lg text-sm font-medium text-white transition-colors",
                  isLive ? "bg-red-600 hover:bg-red-700" : "bg-green-600 hover:bg-green-700"
                )}
              >
                {isLive ? <Square className="w-4 h-4" /> : <Play className="w-4 h-4" />}
                {isLive ? "Pause" : "Resume"}
              </button>
              <button onClick={() => setLogs([])} className="flex items-center gap-1 px-3 py-1.5 rounded-lg text-sm font-medium border border-[#444] text-gray-300 hover:bg-[#2a2a4a] transition-colors">
                <RefreshCw className="w-4 h-4" />
                Clear
              </button>
            </div>
          </div>
          <CardContent className="p-0">
            <div className="h-[500px] overflow-auto p-4 font-mono text-sm">
              {logs.length === 0 ? (
                <p className="text-gray-500 italic">Waiting for logs...</p>
              ) : (
                logs.map((log, i) => (
                  <div key={i} className="flex gap-4 mb-1 text-gray-300">
                    <span className="text-gray-500">{new Date(log.timestamp).toLocaleTimeString()}</span>
                    <span className={cn("font-bold min-w-[50px]", getLogColor(log.level))}>{log.level}</span>
                    <span className="text-purple-400 min-w-[140px]">[{log.service}]</span>
                    <span>{log.message}</span>
                  </div>
                ))
              )}
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
