import {
  LayoutDashboard,
  Settings,
  Upload,
  HeartPulse,
  Zap,
  Server,
  Brain,
  Database,
  Radio,
  Shield,
  ExternalLink,
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/Card';
import { Button } from '../components/ui/Button';

const QUICK_START_STEPS = [
  {
    step: 1,
    title: 'Configure Your KPIs',
    description: 'Browse the metric tree and select KPIs relevant to your business. Choose from Supply Chain, CRM, Sales, and Financial value chains.',
    href: '/config',
    icon: <Settings className="w-4 h-4" />,
    buttonText: 'Go to KPI Configuration',
  },
  {
    step: 2,
    title: 'Import KPI Definitions',
    description: 'Upload Excel files with KPI definitions for bulk import. The system validates formulas and object references automatically.',
    href: '/excel-import',
    icon: <Upload className="w-4 h-4" />,
    buttonText: 'Go to Excel Import',
  },
  {
    step: 3,
    title: 'Explore Object Models',
    description: 'View UML diagrams and understand the data structures required for your selected KPIs.',
    href: '/object-models',
    icon: <LayoutDashboard className="w-4 h-4" />,
    buttonText: 'Browse Object Models',
  },
  {
    step: 4,
    title: 'Monitor System Health',
    description: 'Check the status of all backend services and view real-time system metrics.',
    href: '/system-monitor',
    icon: <HeartPulse className="w-4 h-4" />,
    buttonText: 'View System Monitor',
  },
];

const CAPABILITIES = [
  { title: 'Real-Time Analytics', description: 'On-demand KPI calculations with sub-second latency. No pre-computed batch processing - all metrics calculated in real-time.', icon: <Zap className="w-5 h-5" /> },
  { title: 'Microservices Architecture', description: '21 independent services working together. Scale calculation engines independently based on workload requirements.', icon: <Server className="w-5 h-5" /> },
  { title: 'AI-Powered Guidance', description: 'OpenAI-powered conversation service helps you select the right KPIs and design your analytics value chain.', icon: <Brain className="w-5 h-5" /> },
  { title: 'TimescaleDB Integration', description: 'Optimized time-series database with hypertables and continuous aggregates for high-performance analytics.', icon: <Database className="w-5 h-5" /> },
  { title: 'Event-Driven Updates', description: 'Redis-powered messaging ensures all services stay synchronized. Real-time data propagation across the platform.', icon: <Radio className="w-5 h-5" /> },
  { title: 'Enterprise Ready', description: 'Built-in data governance, row-level security, audit logging, and compliance features for enterprise deployments.', icon: <Shield className="w-5 h-5" /> },
];

const API_DOCS = [
  { name: 'Business Metadata API', url: 'http://localhost:8020/docs' },
  { name: 'Calculation Engine API', url: 'http://localhost:8021/docs' },
  { name: 'Demo Config API', url: 'http://localhost:8022/docs' },
  { name: 'Metadata Ingestion API', url: 'http://localhost:8025/docs' },
  { name: 'Conversation API', url: 'http://localhost:8026/docs' },
  { name: 'API Gateway', url: 'http://127.0.0.1:8090/docs' },
];

export default function DemoPage() {
  return (
    <div className="space-y-6 animate-fade-in">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold theme-text-title tracking-wide">Analytics Engine Demo</h1>
        <p className="theme-text-muted mt-1">
          Welcome to the Analytics Engine - a real-time, microservices-based analytics platform for on-demand KPI calculations.
        </p>
      </div>

      {/* Quick Start Guide */}
      <Card>
        <CardHeader>
          <CardTitle>Quick Start Guide</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {QUICK_START_STEPS.map((item) => (
              <div key={item.step} className="flex gap-4">
                <div className="flex-shrink-0 w-8 h-8 rounded-full bg-alpha-500 text-white flex items-center justify-center font-bold text-sm">
                  {item.step}
                </div>
                <div className="flex-1">
                  <h3 className="font-semibold theme-text-title mb-1">{item.title}</h3>
                  <p className="text-sm theme-text-muted mb-3">{item.description}</p>
                  <a href={item.href}>
                    <Button variant="outline" size="sm">
                      {item.icon}
                      <span className="ml-2">{item.buttonText}</span>
                    </Button>
                  </a>
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>

      {/* Platform Capabilities */}
      <Card>
        <CardHeader>
          <CardTitle>Platform Capabilities</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {CAPABILITIES.map((cap) => (
              <div key={cap.title} className="flex gap-3">
                <div className="flex-shrink-0 p-2 rounded-lg bg-alpha-500/20 text-alpha-500 h-fit">
                  {cap.icon}
                </div>
                <div>
                  <h3 className="font-semibold theme-text-title mb-1">{cap.title}</h3>
                  <p className="text-sm theme-text-muted">{cap.description}</p>
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>

      {/* API Documentation */}
      <Card>
        <CardHeader>
          <CardTitle>API Documentation</CardTitle>
          <p className="text-sm theme-text-muted">Explore the interactive API documentation for each service</p>
        </CardHeader>
        <CardContent>
          <div className="flex flex-wrap gap-2">
            {API_DOCS.map((api) => (
              <a key={api.name} href={api.url} target="_blank" rel="noopener noreferrer">
                <Button variant="outline" size="sm">
                  {api.name}
                  <ExternalLink className="w-3 h-3 ml-2" />
                </Button>
              </a>
            ))}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
