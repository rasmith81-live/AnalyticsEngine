import { useState } from 'react';
import {
  Mic,
  Send,
  TrendingUp,
  TrendingDown,
  AlertTriangle,
  CheckCircle,
  HelpCircle,
  ArrowRight,
  BarChart3,
  Target,
  Sliders,
  FileText,
  RefreshCw,
  Download,
  Info,
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';
import { cn } from '../../lib/utils';

interface KPIImpact {
  kpi: string;
  impact: number;
  confidence: number;
  direction: 'positive' | 'negative';
}

interface CascadeEffect {
  from: string;
  to: string;
  impact: number;
  type: 'direct' | 'indirect';
}

const quickQuestions = [
  'Price +10%',
  'Capacity +20%',
  'New Product',
  'Market Expansion',
  'Reduce Costs 15%',
];

const mockImpacts: KPIImpact[] = [
  { kpi: 'Revenue', impact: 8, confidence: 87, direction: 'positive' },
  { kpi: 'Churn Rate', impact: 3, confidence: 82, direction: 'negative' },
  { kpi: 'Profit Margin', impact: 12, confidence: 91, direction: 'positive' },
  { kpi: 'Market Share', impact: -2, confidence: 75, direction: 'negative' },
];

const mockCascadeEffects: CascadeEffect[] = [
  { from: 'Price', to: 'Revenue', impact: 8, type: 'direct' },
  { from: 'Revenue', to: 'Profit', impact: 12, type: 'direct' },
  { from: 'Price', to: 'Churn', impact: 3, type: 'direct' },
  { from: 'Churn', to: 'Customer LTV', impact: -5, type: 'indirect' },
  { from: 'Customer LTV', to: 'Long-term Revenue', impact: -2, type: 'indirect' },
  { from: 'Price', to: 'Market Share', impact: -2, type: 'direct' },
];

function ImpactCard({ impact }: { impact: KPIImpact }) {
  const isPositive = (impact.direction === 'positive' && impact.impact > 0) || 
                     (impact.direction === 'negative' && impact.impact < 0);
  
  return (
    <div className="p-4 rounded-xl theme-card-bg border theme-border">
      <div className="flex items-center justify-between mb-2">
        <span className="text-sm theme-text-muted">{impact.kpi}</span>
        <div className="flex items-center gap-1">
          {isPositive ? (
            <TrendingUp className="w-4 h-4 text-green-500" />
          ) : (
            <TrendingDown className="w-4 h-4 text-red-500" />
          )}
        </div>
      </div>
      <div className="flex items-baseline gap-1">
        <span className={cn(
          'text-2xl font-bold',
          isPositive ? 'text-green-500' : 'text-red-500'
        )}>
          {impact.impact > 0 ? '+' : ''}{impact.impact}%
        </span>
      </div>
      <div className="mt-2 flex items-center gap-2">
        <div className="flex-1 h-1.5 rounded-full bg-alpha-faded-200 dark:bg-alpha-faded-800">
          <div 
            className="h-full rounded-full bg-alpha-500"
            style={{ width: `${impact.confidence}%` }}
          />
        </div>
        <span className="text-xs theme-text-muted">±{(100 - impact.confidence) / 10}%</span>
      </div>
    </div>
  );
}

function CascadeNode({ label, impact, isSource }: { label: string; impact?: number; isSource?: boolean }) {
  return (
    <div className={cn(
      'px-3 py-2 rounded-lg text-sm font-medium',
      isSource ? 'bg-alpha-600 text-white' : 'theme-card-bg border theme-border theme-text'
    )}>
      {label}
      {impact !== undefined && (
        <span className={cn(
          'ml-2',
          impact > 0 ? 'text-green-400' : 'text-red-400'
        )}>
          ({impact > 0 ? '+' : ''}{impact}%)
        </span>
      )}
    </div>
  );
}

export default function PredictiveWhatIfPage() {
  const [question, setQuestion] = useState('What if we increase prices by 10%?');
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [hasResults, setHasResults] = useState(true);
  const [sensitivityValue, setSensitivityValue] = useState(10);

  const handleAnalyze = () => {
    setIsAnalyzing(true);
    setTimeout(() => {
      setIsAnalyzing(false);
      setHasResults(true);
    }, 2000);
  };

  const overallConfidence = 87;

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Page Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title tracking-wide">Predictive What-If Analysis</h1>
          <p className="theme-text-muted mt-1">Ask strategic questions and get AI-powered predictions</p>
        </div>
        <div className="flex items-center gap-3">
          <Button variant="outline">
            <Download className="w-4 h-4 mr-2" />
            Export Report
          </Button>
        </div>
      </div>

      {/* Question Input */}
      <Card className="overflow-hidden">
        <CardContent className="p-6">
          <div className="flex items-center gap-2 mb-4">
            <HelpCircle className="w-5 h-5 theme-info-icon" />
            <span className="font-semibold theme-text-title">Ask a What-If Question</span>
          </div>
          
          <div className="relative">
            <input
              type="text"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="What if we increase prices by 10%?"
              className="w-full px-4 py-4 pr-24 rounded-xl theme-card-bg border theme-border
                theme-text placeholder:theme-text-muted text-lg
                focus:outline-none focus:ring-2 focus:ring-alpha-500"
            />
            <div className="absolute right-2 top-1/2 -translate-y-1/2 flex items-center gap-2">
              <button className="p-2 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 transition-colors">
                <Mic className="w-5 h-5 theme-text-muted" />
              </button>
              <Button onClick={handleAnalyze} disabled={isAnalyzing} size="sm">
                {isAnalyzing ? (
                  <RefreshCw className="w-4 h-4 animate-spin" />
                ) : (
                  <Send className="w-4 h-4" />
                )}
              </Button>
            </div>
          </div>

          {/* Quick Questions */}
          <div className="flex flex-wrap gap-2 mt-4">
            <span className="text-sm theme-text-muted">Quick questions:</span>
            {quickQuestions.map((q) => (
              <button
                key={q}
                onClick={() => setQuestion(`What if we ${q.toLowerCase()}?`)}
                className="px-3 py-1.5 rounded-full text-sm font-medium
                  theme-card-bg border theme-border hover:border-alpha-500
                  theme-text transition-all duration-200"
              >
                {q}
              </button>
            ))}
          </div>
        </CardContent>
      </Card>

      {/* Results */}
      {hasResults && (
        <>
          {/* Confidence Banner */}
          <div className="flex items-center justify-between p-4 rounded-xl bg-alpha-600/10 border border-alpha-500/30">
            <div className="flex items-center gap-3">
              <div className="p-2 rounded-lg bg-alpha-600">
                <BarChart3 className="w-5 h-5 text-white" />
              </div>
              <div>
                <span className="font-semibold theme-text-title">Prediction Results</span>
                <p className="text-sm theme-text-muted">Based on 24 months of historical data</p>
              </div>
            </div>
            <div className="flex items-center gap-3">
              <span className="text-sm theme-text-muted">Overall Confidence:</span>
              <div className="flex items-center gap-2">
                <div className="w-24 h-2 rounded-full bg-alpha-faded-200 dark:bg-alpha-faded-800">
                  <div 
                    className="h-full rounded-full bg-alpha-500"
                    style={{ width: `${overallConfidence}%` }}
                  />
                </div>
                <span className="font-bold theme-text-vibrant">{overallConfidence}%</span>
              </div>
            </div>
          </div>

          {/* Primary Impacts */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <TrendingUp className="w-5 h-5 theme-info-icon" />
                Primary Impacts
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                {mockImpacts.map((impact) => (
                  <ImpactCard key={impact.kpi} impact={impact} />
                ))}
              </div>
            </CardContent>
          </Card>

          {/* Cascade Effects & Net Impact */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Cascade Effects */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <ArrowRight className="w-5 h-5 theme-info-icon" />
                  Cascade Effects
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  {/* Main cascade flow */}
                  <div className="p-4 rounded-xl theme-card-bg">
                    <div className="flex items-center gap-2 flex-wrap">
                      <CascadeNode label="Price +10%" isSource />
                      <ArrowRight className="w-4 h-4 theme-text-muted" />
                      <CascadeNode label="Revenue" impact={8} />
                      <ArrowRight className="w-4 h-4 theme-text-muted" />
                      <CascadeNode label="Profit" impact={12} />
                    </div>
                  </div>
                  
                  {/* Secondary effects */}
                  <div className="p-4 rounded-xl theme-card-bg">
                    <div className="flex items-center gap-2 flex-wrap">
                      <CascadeNode label="Price +10%" isSource />
                      <ArrowRight className="w-4 h-4 theme-text-muted" />
                      <CascadeNode label="Churn" impact={3} />
                      <ArrowRight className="w-4 h-4 theme-text-muted" />
                      <CascadeNode label="Customer LTV" impact={-5} />
                      <ArrowRight className="w-4 h-4 theme-text-muted" />
                      <CascadeNode label="Long-term Rev" impact={-2} />
                    </div>
                  </div>

                  {/* Tertiary effects */}
                  <div className="p-4 rounded-xl theme-card-bg">
                    <div className="flex items-center gap-2 flex-wrap">
                      <CascadeNode label="Price +10%" isSource />
                      <ArrowRight className="w-4 h-4 theme-text-muted" />
                      <CascadeNode label="Market Share" impact={-2} />
                      <ArrowRight className="w-4 h-4 theme-text-muted" />
                      <CascadeNode label="Competitive Position" />
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Net Impact Summary */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Target className="w-5 h-5 theme-info-icon" />
                  Net Impact Summary
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <div className="p-4 rounded-xl bg-green-500/10 border border-green-500/30">
                    <div className="flex items-center gap-2 mb-2">
                      <TrendingUp className="w-5 h-5 text-green-500" />
                      <span className="text-sm font-medium text-green-600 dark:text-green-400">Revenue Impact</span>
                    </div>
                    <span className="text-2xl font-bold text-green-600 dark:text-green-400">+$2.4M/year</span>
                  </div>
                  <div className="p-4 rounded-xl bg-green-500/10 border border-green-500/30">
                    <div className="flex items-center gap-2 mb-2">
                      <TrendingUp className="w-5 h-5 text-green-500" />
                      <span className="text-sm font-medium text-green-600 dark:text-green-400">Profit Impact</span>
                    </div>
                    <span className="text-2xl font-bold text-green-600 dark:text-green-400">+$1.8M/year</span>
                  </div>
                </div>

                <div className="p-4 rounded-xl bg-amber-500/10 border border-amber-500/30">
                  <div className="flex items-center gap-2 mb-2">
                    <AlertTriangle className="w-5 h-5 text-amber-500" />
                    <span className="text-sm font-medium text-amber-600 dark:text-amber-400">Risk Factors</span>
                  </div>
                  <ul className="text-sm text-amber-700 dark:text-amber-300 space-y-1">
                    <li>• Churn increase of 3% expected</li>
                    <li>• Potential competitive response</li>
                    <li>• Market share erosion risk</li>
                  </ul>
                </div>

                <div className="p-4 rounded-xl bg-alpha-500/10 border border-alpha-500/30">
                  <div className="flex items-center gap-2 mb-2">
                    <CheckCircle className="w-5 h-5 text-alpha-500" />
                    <span className="text-sm font-medium theme-text-vibrant">Recommendation</span>
                  </div>
                  <p className="text-sm theme-text">
                    <strong>PROCEED WITH CAUTION</strong> - The net financial impact is positive, but monitor churn closely. 
                    Consider a phased rollout to minimize risk.
                  </p>
                </div>
              </CardContent>
            </Card>
          </div>

          {/* Sensitivity Analysis & Optimal Value */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Sensitivity Analysis */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Sliders className="w-5 h-5 theme-info-icon" />
                  Sensitivity Analysis
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="mb-4">
                  <label className="text-sm theme-text-muted block mb-2">Price Change: {sensitivityValue}%</label>
                  <input
                    type="range"
                    min="-20"
                    max="30"
                    value={sensitivityValue}
                    onChange={(e) => setSensitivityValue(Number(e.target.value))}
                    className="w-full h-2 rounded-full bg-alpha-faded-200 dark:bg-alpha-faded-800 appearance-none cursor-pointer
                      [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-4 [&::-webkit-slider-thumb]:h-4 
                      [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:bg-alpha-500"
                  />
                  <div className="flex justify-between text-xs theme-text-muted mt-1">
                    <span>-20%</span>
                    <span>0%</span>
                    <span>+30%</span>
                  </div>
                </div>

                {/* Sensitivity Chart Placeholder */}
                <div className="h-48 rounded-xl theme-card-bg border theme-border flex items-center justify-center">
                  <div className="text-center">
                    <BarChart3 className="w-12 h-12 mx-auto theme-text-muted mb-2" />
                    <p className="text-sm theme-text-muted">Revenue vs Price Change Curve</p>
                    <p className="text-xs theme-text-muted mt-1">Interactive chart showing sensitivity</p>
                  </div>
                </div>

                <div className="mt-4 p-3 rounded-lg theme-card-bg">
                  <p className="text-sm theme-text">
                    <strong>Insight:</strong> Revenue peaks at +7% price increase, then declines due to churn acceleration.
                  </p>
                </div>
              </CardContent>
            </Card>

            {/* Optimal Value Finder */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Target className="w-5 h-5 theme-info-icon" />
                  Optimal Value Finder
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="text-xs theme-text-muted block mb-1">Optimize For</label>
                    <select className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text">
                      <option>Revenue</option>
                      <option>Profit</option>
                      <option>Market Share</option>
                      <option>Customer Satisfaction</option>
                    </select>
                  </div>
                  <div>
                    <label className="text-xs theme-text-muted block mb-1">Variable</label>
                    <select className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text">
                      <option>Price Change</option>
                      <option>Capacity</option>
                      <option>Marketing Spend</option>
                    </select>
                  </div>
                </div>

                <div>
                  <label className="text-xs theme-text-muted block mb-1">Constraint</label>
                  <div className="flex items-center gap-2">
                    <select className="flex-1 px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text">
                      <option>Churn Rate</option>
                      <option>Cost</option>
                      <option>Market Share</option>
                    </select>
                    <select className="w-20 px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text">
                      <option>&lt;</option>
                      <option>&gt;</option>
                      <option>=</option>
                    </select>
                    <input
                      type="number"
                      value="5"
                      className="w-20 px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text"
                    />
                    <span className="theme-text-muted">%</span>
                  </div>
                </div>

                <Button className="w-full">
                  <Target className="w-4 h-4 mr-2" />
                  Find Optimal Value
                </Button>

                {/* Optimal Result */}
                <div className="p-4 rounded-xl bg-green-500/10 border border-green-500/30">
                  <h4 className="font-semibold text-green-600 dark:text-green-400 mb-3">Optimal Solution Found</h4>
                  <div className="space-y-2 text-sm">
                    <div className="flex justify-between">
                      <span className="theme-text-muted">Optimal Price:</span>
                      <span className="font-medium text-green-600 dark:text-green-400">+7.2%</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="theme-text-muted">Predicted Revenue:</span>
                      <span className="font-medium text-green-600 dark:text-green-400">+$2.8M</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="theme-text-muted">Churn stays at:</span>
                      <span className="font-medium text-green-600 dark:text-green-400">4.8%</span>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>

          {/* Methodology Panel */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <FileText className="w-5 h-5 theme-info-icon" />
                Methodology & Evidence
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="p-4 rounded-xl theme-card-bg">
                  <h4 className="font-semibold theme-text-title mb-2">Models Used</h4>
                  <ul className="text-sm theme-text-muted space-y-1">
                    <li>• Price Elasticity Model (R²=0.89)</li>
                    <li>• Churn Predictor (AUC=0.92)</li>
                    <li>• Revenue Forecaster (MAPE=4.2%)</li>
                  </ul>
                </div>
                <div className="p-4 rounded-xl theme-card-bg">
                  <h4 className="font-semibold theme-text-title mb-2">Data Period</h4>
                  <ul className="text-sm theme-text-muted space-y-1">
                    <li>• Last 24 months</li>
                    <li>• 1,248 data points</li>
                    <li>• 3 similar price events</li>
                  </ul>
                </div>
                <div className="p-4 rounded-xl theme-card-bg">
                  <h4 className="font-semibold theme-text-title mb-2">Historical Evidence</h4>
                  <ul className="text-sm theme-text-muted space-y-1">
                    <li>• Q3 2024: +5% price → +4% revenue</li>
                    <li>• Q1 2024: +8% price → +2% churn</li>
                    <li>• Pattern confidence: High</li>
                  </ul>
                </div>
              </div>
              <div className="flex items-center gap-4 mt-4">
                <Button variant="outline" size="sm">
                  <Info className="w-4 h-4 mr-1" />
                  View Full Methodology
                </Button>
                <Button variant="outline" size="sm">
                  <Download className="w-4 h-4 mr-1" />
                  Export Report
                </Button>
              </div>
            </CardContent>
          </Card>
        </>
      )}
    </div>
  );
}
