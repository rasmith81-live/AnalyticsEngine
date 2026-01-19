import {
  TrendingUp,
  TrendingDown,
  AlertTriangle,
  CheckCircle,
  Lightbulb,
  Activity,
  Users,
  DollarSign,
  Target,
  Clock,
  ArrowRight,
  Zap,
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { cn } from '../lib/utils';

interface MetricCardProps {
  title: string;
  value: string;
  change: number;
  trend: 'up' | 'down';
  icon: React.ReactNode;
}

function MetricCard({ title, value, change, trend, icon }: MetricCardProps) {
  const isPositive = (trend === 'up' && change > 0) || (trend === 'down' && change < 0);
  
  return (
    <Card className="p-6">
      <div className="flex items-start justify-between">
        <div>
          <p className="text-sm theme-text-muted font-medium">{title}</p>
          <p className="text-3xl font-bold theme-text-title mt-2">{value}</p>
          <div className={cn(
            'flex items-center gap-1 mt-2 text-sm font-medium',
            isPositive ? 'text-green-500' : 'text-red-500'
          )}>
            {change > 0 ? <TrendingUp className="w-4 h-4" /> : <TrendingDown className="w-4 h-4" />}
            <span>{Math.abs(change)}% vs last month</span>
          </div>
        </div>
        <div className="p-3 rounded-xl bg-alpha-100 dark:bg-alpha-900">
          {icon}
        </div>
      </div>
    </Card>
  );
}

interface AlertItemProps {
  type: 'warning' | 'success' | 'info';
  title: string;
  description: string;
  time: string;
}

function AlertItem({ type, title, description, time }: AlertItemProps) {
  const icons = {
    warning: <AlertTriangle className="w-5 h-5 text-amber-500" />,
    success: <CheckCircle className="w-5 h-5 text-green-500" />,
    info: <Lightbulb className="w-5 h-5 text-beta-600" />,
  };

  return (
    <div className="flex items-start gap-4 p-4 rounded-xl theme-card-bg hover:theme-card-bg-hover transition-all duration-200">
      <div className="mt-0.5">{icons[type]}</div>
      <div className="flex-1 min-w-0">
        <p className="font-medium theme-text-title">{title}</p>
        <p className="text-sm theme-text-muted mt-1 line-clamp-2">{description}</p>
      </div>
      <span className="text-xs theme-text-muted whitespace-nowrap">{time}</span>
    </div>
  );
}

interface InsightCardProps {
  title: string;
  description: string;
  impact: 'high' | 'medium' | 'low';
  agent: string;
}

function InsightCard({ title, description, impact, agent }: InsightCardProps) {
  const impactColors = {
    high: 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400',
    medium: 'bg-amber-100 text-amber-700 dark:bg-amber-900/30 dark:text-amber-400',
    low: 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400',
  };

  return (
    <div className="p-4 rounded-xl theme-card-bg border theme-border hover:theme-card-bg-hover transition-all duration-200 cursor-pointer group">
      <div className="flex items-start justify-between mb-3">
        <span className={cn('px-2 py-1 rounded-full text-xs font-medium', impactColors[impact])}>
          {impact.toUpperCase()} IMPACT
        </span>
        <span className="text-xs theme-text-muted">{agent}</span>
      </div>
      <h4 className="font-semibold theme-text-title mb-2">{title}</h4>
      <p className="text-sm theme-text-muted line-clamp-2">{description}</p>
      <button className="flex items-center gap-1 mt-3 text-sm font-medium theme-text-vibrant group-hover:gap-2 transition-all duration-200">
        Explore <ArrowRight className="w-4 h-4" />
      </button>
    </div>
  );
}

interface WorkflowStepProps {
  step: number;
  title: string;
  status: 'completed' | 'current' | 'upcoming';
}

function WorkflowStep({ step, title, status }: WorkflowStepProps) {
  return (
    <div className="flex items-center gap-3">
      <div className={cn(
        'w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold',
        status === 'completed' && 'bg-green-500 text-white',
        status === 'current' && 'bg-alpha-500 text-white animate-pulse-glow',
        status === 'upcoming' && 'bg-alpha-faded-200 dark:bg-alpha-faded-800 theme-text-muted'
      )}>
        {status === 'completed' ? <CheckCircle className="w-4 h-4" /> : step}
      </div>
      <span className={cn(
        'text-sm font-medium',
        status === 'current' ? 'theme-text-vibrant' : 'theme-text-muted'
      )}>
        {title}
      </span>
    </div>
  );
}

export default function StrategyCenterPage() {
  const healthScore = 78;

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Page Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title tracking-wide">Strategy Center</h1>
          <p className="theme-text-muted mt-1">Real-time health of your business strategy</p>
        </div>
        <Button>
          <Zap className="w-4 h-4 mr-2" />
          Quick Actions
        </Button>
      </div>

      {/* Strategy Health Score */}
      <Card className="p-6 bg-gradient-to-r from-alpha-600 to-alpha-800 border-none">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-lg font-medium text-alpha-100">Strategy Health Score</h2>
            <div className="flex items-baseline gap-2 mt-2">
              <span className="text-5xl font-bold text-white">{healthScore}</span>
              <span className="text-xl text-alpha-200">/100</span>
            </div>
            <p className="text-alpha-200 mt-2">
              Your strategy is performing well. 3 areas need attention.
            </p>
          </div>
          <div className="relative w-32 h-32">
            <svg className="w-full h-full transform -rotate-90">
              <circle
                cx="64"
                cy="64"
                r="56"
                stroke="currentColor"
                strokeWidth="12"
                fill="none"
                className="text-alpha-900/30"
              />
              <circle
                cx="64"
                cy="64"
                r="56"
                stroke="currentColor"
                strokeWidth="12"
                fill="none"
                strokeDasharray={`${(healthScore / 100) * 352} 352`}
                strokeLinecap="round"
                className="text-white"
              />
            </svg>
            <div className="absolute inset-0 flex items-center justify-center">
              <Activity className="w-10 h-10 text-white" />
            </div>
          </div>
        </div>
      </Card>

      {/* Key Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard
          title="Revenue"
          value="$2.4M"
          change={12.5}
          trend="up"
          icon={<DollarSign className="w-6 h-6 text-alpha-600" />}
        />
        <MetricCard
          title="Customer Satisfaction"
          value="4.6/5"
          change={8.2}
          trend="up"
          icon={<Users className="w-6 h-6 text-alpha-600" />}
        />
        <MetricCard
          title="Goal Completion"
          value="67%"
          change={-3.1}
          trend="up"
          icon={<Target className="w-6 h-6 text-alpha-600" />}
        />
        <MetricCard
          title="Avg Response Time"
          value="2.3h"
          change={-15.4}
          trend="down"
          icon={<Clock className="w-6 h-6 text-alpha-600" />}
        />
      </div>

      {/* Main Content Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Alerts Column */}
        <Card className="lg:col-span-1">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <AlertTriangle className="w-5 h-5 text-amber-500" />
              Active Alerts
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            <AlertItem
              type="warning"
              title="Churn Risk Detected"
              description="3 enterprise customers showing declining engagement patterns"
              time="2h ago"
            />
            <AlertItem
              type="success"
              title="Revenue Target Achieved"
              description="Q4 revenue target exceeded by 12%"
              time="5h ago"
            />
            <AlertItem
              type="info"
              title="New Correlation Found"
              description="Customer support response time correlates with NPS score"
              time="1d ago"
            />
            <AlertItem
              type="warning"
              title="Supply Chain Delay"
              description="Vendor delivery times increased by 20% this week"
              time="1d ago"
            />
          </CardContent>
        </Card>

        {/* Quick Insights Column */}
        <Card className="lg:col-span-2">
          <CardHeader>
            <div className="flex items-center justify-between">
              <CardTitle className="flex items-center gap-2">
                <Lightbulb className="w-5 h-5 text-beta-600" />
                Quick Insights
              </CardTitle>
              <Button variant="ghost" size="sm">
                View All <ArrowRight className="w-4 h-4 ml-1" />
              </Button>
            </div>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <InsightCard
                title="Price Optimization Opportunity"
                description="Analysis suggests 7% price increase would maximize revenue with minimal churn impact"
                impact="high"
                agent="Data Scientist"
              />
              <InsightCard
                title="Process Bottleneck Identified"
                description="Order fulfillment step 3 is causing 40% of delays. Consider automation."
                impact="high"
                agent="Operations Manager"
              />
              <InsightCard
                title="Customer Segment Growth"
                description="Enterprise segment growing 2x faster than SMB. Consider resource reallocation."
                impact="medium"
                agent="Business Strategist"
              />
              <InsightCard
                title="Competitive Movement"
                description="Competitor X launched similar feature. Monitor customer response."
                impact="low"
                agent="Competitive Analyst"
              />
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Workflow Progress & System Status */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Workflow Progress */}
        <Card>
          <CardHeader>
            <CardTitle>Workflow Progress</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex items-center justify-between">
              <WorkflowStep step={1} title="Design" status="completed" />
              <div className="flex-1 h-0.5 mx-2 bg-green-500" />
              <WorkflowStep step={2} title="Simulate" status="completed" />
              <div className="flex-1 h-0.5 mx-2 bg-green-500" />
              <WorkflowStep step={3} title="Deploy" status="current" />
              <div className="flex-1 h-0.5 mx-2 bg-alpha-faded-300 dark:bg-alpha-faded-700" />
              <WorkflowStep step={4} title="Analyze" status="upcoming" />
              <div className="flex-1 h-0.5 mx-2 bg-alpha-faded-300 dark:bg-alpha-faded-700" />
              <WorkflowStep step={5} title="Evolve" status="upcoming" />
            </div>
            <div className="mt-6 p-4 rounded-xl theme-card-bg">
              <p className="text-sm theme-text-muted">
                <span className="font-medium theme-text-title">Current Phase:</span> Connecting to corporate systems and mapping data attributes.
              </p>
              <Button variant="outline" size="sm" className="mt-3">
                Continue Setup
              </Button>
            </div>
          </CardContent>
        </Card>

        {/* System Status */}
        <Card>
          <CardHeader>
            <CardTitle>Connected Systems</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {[
                { name: 'Salesforce CRM', status: 'connected', lastSync: '2 min ago' },
                { name: 'SAP ERP', status: 'connected', lastSync: '5 min ago' },
                { name: 'Snowflake DW', status: 'connected', lastSync: '1 min ago' },
                { name: 'HubSpot Marketing', status: 'pending', lastSync: 'Not connected' },
              ].map((system) => (
                <div
                  key={system.name}
                  className="flex items-center justify-between p-3 rounded-xl theme-card-bg"
                >
                  <div className="flex items-center gap-3">
                    <div className={cn(
                      'w-2 h-2 rounded-full',
                      system.status === 'connected' ? 'bg-green-500' : 'bg-amber-500'
                    )} />
                    <span className="font-medium theme-text-title">{system.name}</span>
                  </div>
                  <span className="text-sm theme-text-muted">{system.lastSync}</span>
                </div>
              ))}
            </div>
            <Button variant="outline" size="sm" className="mt-4 w-full">
              Manage Connections
            </Button>
          </CardContent>
        </Card>
      </div>

      {/* Recent Activity */}
      <Card>
        <CardHeader>
          <CardTitle>Recent Activity</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {[
              { action: 'KPI "Customer Lifetime Value" updated', user: 'AI Strategist', time: '10 min ago' },
              { action: 'New data source "Stripe Payments" connected', user: 'System', time: '1 hour ago' },
              { action: 'Simulation "Q1 Forecast" completed', user: 'John Doe', time: '2 hours ago' },
              { action: 'Insight "Churn Risk" generated', user: 'Data Scientist Agent', time: '3 hours ago' },
              { action: 'Business model updated with new process', user: 'Jane Smith', time: '5 hours ago' },
            ].map((activity, index) => (
              <div key={index} className="flex items-center gap-4">
                <div className="w-2 h-2 rounded-full bg-alpha-500" />
                <div className="flex-1">
                  <p className="text-sm theme-text-title">{activity.action}</p>
                  <p className="text-xs theme-text-muted">by {activity.user}</p>
                </div>
                <span className="text-xs theme-text-muted">{activity.time}</span>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
