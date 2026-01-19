import { useState } from 'react';
import {
  Lightbulb,
  TrendingUp,
  TrendingDown,
  AlertTriangle,
  Shield,
  Zap,
  Filter,
  Search,
  Check,
  X,
  ArrowRight,
  Clock,
  User,
  BarChart3,
  Target,
  DollarSign,
  Users,
  RefreshCw,
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { cn } from '../lib/utils';

type InsightCategory = 'all' | 'growth' | 'risk' | 'efficiency' | 'competitive' | 'anomaly';
type InsightStatus = 'new' | 'reviewed' | 'actioned' | 'dismissed';

interface Insight {
  id: string;
  title: string;
  description: string;
  category: InsightCategory;
  impact: 'high' | 'medium' | 'low';
  agent: string;
  timestamp: string;
  status: InsightStatus;
  metrics?: { label: string; value: string; change?: number }[];
  recommendation?: string;
}

const mockInsights: Insight[] = [
  {
    id: '1',
    title: 'Price Optimization Opportunity',
    description: 'Analysis of price elasticity data suggests a 7% price increase would maximize revenue with minimal churn impact. Historical data from Q3 2024 supports this finding.',
    category: 'growth',
    impact: 'high',
    agent: 'Data Scientist',
    timestamp: '2 hours ago',
    status: 'new',
    metrics: [
      { label: 'Potential Revenue', value: '+$2.8M', change: 12 },
      { label: 'Churn Risk', value: '+2.1%', change: 2.1 },
    ],
    recommendation: 'Consider phased rollout starting with enterprise segment.',
  },
  {
    id: '2',
    title: 'Process Bottleneck Identified',
    description: 'Order fulfillment step 3 is causing 40% of delays. Resource utilization at 95% indicates capacity constraint.',
    category: 'efficiency',
    impact: 'high',
    agent: 'Operations Manager',
    timestamp: '4 hours ago',
    status: 'new',
    metrics: [
      { label: 'Delay Reduction', value: '-40%' },
      { label: 'Cost Savings', value: '$180K/year' },
    ],
    recommendation: 'Add 1 additional resource or implement automation.',
  },
  {
    id: '3',
    title: 'Churn Risk Alert: Enterprise Segment',
    description: '3 enterprise customers showing declining engagement patterns over the past 30 days. Combined ARR at risk: $450K.',
    category: 'risk',
    impact: 'high',
    agent: 'Customer Success Manager',
    timestamp: '5 hours ago',
    status: 'reviewed',
    metrics: [
      { label: 'ARR at Risk', value: '$450K' },
      { label: 'Customers', value: '3' },
    ],
    recommendation: 'Schedule executive check-ins within 48 hours.',
  },
  {
    id: '4',
    title: 'Competitor X Launched Similar Feature',
    description: 'Competitor X announced a feature similar to our Process Modeler. Early market response is mixed.',
    category: 'competitive',
    impact: 'medium',
    agent: 'Competitive Analyst',
    timestamp: '1 day ago',
    status: 'new',
    metrics: [
      { label: 'Market Overlap', value: '35%' },
      { label: 'Price Comparison', value: '-15%' },
    ],
    recommendation: 'Accelerate differentiation messaging and feature roadmap.',
  },
  {
    id: '5',
    title: 'Unusual Spike in API Errors',
    description: 'API error rate increased by 300% in the last 2 hours. Primary source: payment processing endpoint.',
    category: 'anomaly',
    impact: 'high',
    agent: 'System Monitor',
    timestamp: '30 min ago',
    status: 'actioned',
    metrics: [
      { label: 'Error Rate', value: '4.2%', change: 300 },
      { label: 'Affected Transactions', value: '127' },
    ],
    recommendation: 'Engineering team investigating. ETA: 1 hour.',
  },
  {
    id: '6',
    title: 'Enterprise Segment Growing 2x Faster',
    description: 'Enterprise segment revenue growth is 2x faster than SMB. Consider resource reallocation.',
    category: 'growth',
    impact: 'medium',
    agent: 'Business Strategist',
    timestamp: '1 day ago',
    status: 'reviewed',
    metrics: [
      { label: 'Enterprise Growth', value: '+24%' },
      { label: 'SMB Growth', value: '+12%' },
    ],
    recommendation: 'Shift 20% of sales resources to enterprise.',
  },
];

const categoryConfig: Record<InsightCategory, { label: string; icon: React.ReactNode; color: string }> = {
  all: { label: 'All', icon: <Lightbulb className="w-4 h-4" />, color: 'bg-alpha-500' },
  growth: { label: 'Growth', icon: <TrendingUp className="w-4 h-4" />, color: 'bg-green-500' },
  risk: { label: 'Risk', icon: <AlertTriangle className="w-4 h-4" />, color: 'bg-red-500' },
  efficiency: { label: 'Efficiency', icon: <Zap className="w-4 h-4" />, color: 'bg-amber-500' },
  competitive: { label: 'Competitive', icon: <Shield className="w-4 h-4" />, color: 'bg-blue-500' },
  anomaly: { label: 'Anomaly', icon: <BarChart3 className="w-4 h-4" />, color: 'bg-purple-500' },
};

const impactColors = {
  high: 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400',
  medium: 'bg-amber-100 text-amber-700 dark:bg-amber-900/30 dark:text-amber-400',
  low: 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400',
};

function InsightCard({ insight, onAction }: { insight: Insight; onAction: (id: string, action: string) => void }) {
  const category = categoryConfig[insight.category];
  
  return (
    <Card className="overflow-hidden">
      <div className={cn('h-1', category.color)} />
      <CardContent className="p-6">
        {/* Header */}
        <div className="flex items-start justify-between mb-4">
          <div className="flex items-center gap-3">
            <div className={cn('p-2 rounded-lg', category.color, 'bg-opacity-20')}>
              {category.icon}
            </div>
            <div>
              <span className={cn('px-2 py-0.5 rounded-full text-xs font-medium', impactColors[insight.impact])}>
                {insight.impact.toUpperCase()} IMPACT
              </span>
            </div>
          </div>
          <div className="flex items-center gap-2 text-xs theme-text-muted">
            <User className="w-3 h-3" />
            <span>{insight.agent}</span>
            <span>•</span>
            <Clock className="w-3 h-3" />
            <span>{insight.timestamp}</span>
          </div>
        </div>

        {/* Content */}
        <h3 className="text-lg font-semibold theme-text-title mb-2">{insight.title}</h3>
        <p className="text-sm theme-text-muted mb-4">{insight.description}</p>

        {/* Metrics */}
        {insight.metrics && (
          <div className="flex flex-wrap gap-4 mb-4">
            {insight.metrics.map((metric, index) => (
              <div key={index} className="p-3 rounded-lg theme-card-bg">
                <span className="text-xs theme-text-muted block">{metric.label}</span>
                <span className="text-lg font-bold theme-text-title">{metric.value}</span>
                {metric.change !== undefined && (
                  <span className={cn(
                    'text-xs ml-1',
                    metric.change > 0 ? 'text-green-500' : 'text-red-500'
                  )}>
                    {metric.change > 0 ? '↑' : '↓'} {Math.abs(metric.change)}%
                  </span>
                )}
              </div>
            ))}
          </div>
        )}

        {/* Recommendation */}
        {insight.recommendation && (
          <div className="p-3 rounded-lg bg-alpha-500/10 border border-alpha-500/30 mb-4">
            <span className="text-xs font-medium theme-text-vibrant">Recommendation:</span>
            <p className="text-sm theme-text mt-1">{insight.recommendation}</p>
          </div>
        )}

        {/* Actions */}
        <div className="flex items-center justify-between pt-4 border-t theme-border">
          <div className="flex items-center gap-2">
            {insight.status === 'new' && (
              <>
                <Button size="sm" onClick={() => onAction(insight.id, 'action')}>
                  <Check className="w-4 h-4 mr-1" />
                  Take Action
                </Button>
                <Button variant="outline" size="sm" onClick={() => onAction(insight.id, 'dismiss')}>
                  <X className="w-4 h-4 mr-1" />
                  Dismiss
                </Button>
              </>
            )}
            {insight.status === 'reviewed' && (
              <span className="text-xs theme-text-muted flex items-center gap-1">
                <Check className="w-3 h-3" /> Reviewed
              </span>
            )}
            {insight.status === 'actioned' && (
              <span className="text-xs text-green-500 flex items-center gap-1">
                <Check className="w-3 h-3" /> Action Taken
              </span>
            )}
          </div>
          <button className="flex items-center gap-1 text-sm font-medium theme-text-vibrant hover:gap-2 transition-all duration-200">
            Explore <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </CardContent>
    </Card>
  );
}

export default function InsightsFeedPage() {
  const [selectedCategory, setSelectedCategory] = useState<InsightCategory>('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [insights, setInsights] = useState(mockInsights);

  const filteredInsights = insights.filter(insight => {
    const matchesCategory = selectedCategory === 'all' || insight.category === selectedCategory;
    const matchesSearch = insight.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          insight.description.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCategory && matchesSearch;
  });

  const handleAction = (id: string, action: string) => {
    setInsights(insights.map(i => 
      i.id === id ? { ...i, status: action === 'dismiss' ? 'dismissed' as InsightStatus : 'actioned' as InsightStatus } : i
    ));
  };

  const stats = {
    total: insights.length,
    new: insights.filter(i => i.status === 'new').length,
    highImpact: insights.filter(i => i.impact === 'high').length,
  };

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Page Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title tracking-wide">Insights Feed</h1>
          <p className="theme-text-muted mt-1">AI-discovered opportunities and recommendations</p>
        </div>
        <Button variant="outline">
          <RefreshCw className="w-4 h-4 mr-2" />
          Refresh
        </Button>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card className="p-4">
          <div className="flex items-center gap-3">
            <div className="p-2 rounded-lg bg-alpha-500/20">
              <Lightbulb className="w-5 h-5 text-alpha-500" />
            </div>
            <div>
              <span className="text-2xl font-bold theme-text-title">{stats.total}</span>
              <p className="text-xs theme-text-muted">Total Insights</p>
            </div>
          </div>
        </Card>
        <Card className="p-4">
          <div className="flex items-center gap-3">
            <div className="p-2 rounded-lg bg-blue-500/20">
              <Target className="w-5 h-5 text-blue-500" />
            </div>
            <div>
              <span className="text-2xl font-bold theme-text-title">{stats.new}</span>
              <p className="text-xs theme-text-muted">New Insights</p>
            </div>
          </div>
        </Card>
        <Card className="p-4">
          <div className="flex items-center gap-3">
            <div className="p-2 rounded-lg bg-red-500/20">
              <AlertTriangle className="w-5 h-5 text-red-500" />
            </div>
            <div>
              <span className="text-2xl font-bold theme-text-title">{stats.highImpact}</span>
              <p className="text-xs theme-text-muted">High Impact</p>
            </div>
          </div>
        </Card>
        <Card className="p-4">
          <div className="flex items-center gap-3">
            <div className="p-2 rounded-lg bg-green-500/20">
              <DollarSign className="w-5 h-5 text-green-500" />
            </div>
            <div>
              <span className="text-2xl font-bold theme-text-title">$3.4M</span>
              <p className="text-xs theme-text-muted">Potential Value</p>
            </div>
          </div>
        </Card>
      </div>

      {/* Filters */}
      <div className="flex flex-col md:flex-row gap-4">
        {/* Search */}
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 theme-text-muted" />
          <input
            type="text"
            placeholder="Search insights..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full h-10 pl-10 pr-4 rounded-xl theme-card-bg border theme-border
              focus:outline-none focus:ring-2 focus:ring-alpha-500 focus:border-transparent
              theme-text placeholder:theme-text-muted transition-all duration-200"
          />
        </div>

        {/* Category Filters */}
        <div className="flex items-center gap-2 overflow-x-auto pb-2 md:pb-0">
          <Filter className="w-4 h-4 theme-text-muted flex-shrink-0" />
          {(Object.keys(categoryConfig) as InsightCategory[]).map((cat) => (
            <button
              key={cat}
              onClick={() => setSelectedCategory(cat)}
              className={cn(
                'flex items-center gap-2 px-3 py-2 rounded-lg text-sm font-medium whitespace-nowrap transition-all duration-200',
                selectedCategory === cat
                  ? 'bg-alpha-600 text-white'
                  : 'theme-card-bg border theme-border theme-text hover:border-alpha-500'
              )}
            >
              {categoryConfig[cat].icon}
              {categoryConfig[cat].label}
            </button>
          ))}
        </div>
      </div>

      {/* Insights List */}
      <div className="space-y-4">
        {filteredInsights.length > 0 ? (
          filteredInsights.map((insight) => (
            <InsightCard key={insight.id} insight={insight} onAction={handleAction} />
          ))
        ) : (
          <Card className="p-12 text-center">
            <Lightbulb className="w-12 h-12 mx-auto theme-text-muted mb-4" />
            <h3 className="text-lg font-semibold theme-text-title mb-2">No insights found</h3>
            <p className="theme-text-muted">Try adjusting your filters or check back later.</p>
          </Card>
        )}
      </div>
    </div>
  );
}
