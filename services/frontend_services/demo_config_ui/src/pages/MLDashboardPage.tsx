import { useState } from 'react';
import {
  Brain,
  Play,
  FlaskConical,
  Sparkles,
  Plus,
  MoreVertical,
  CheckCircle,
  XCircle,
  Clock,
  X,
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { cn } from '../lib/utils';

const MOCK_MODELS = [
  { id: 'mod_churn_v1', name: 'Customer Churn Predictor', version: '1.2.0', type: 'Classification', status: 'production', accuracy: '87.5%', lastTrained: '2023-12-10' },
  { id: 'mod_demand_v2', name: 'Demand Forecast', version: '2.1.0', type: 'Regression', status: 'staging', accuracy: '92.1%', lastTrained: '2023-12-15' },
  { id: 'mod_segment_v1', name: 'User Segmentation', version: '1.0.0', type: 'Clustering', status: 'archived', accuracy: '0.65 (Silhouette)', lastTrained: '2023-11-20' },
];

const MOCK_JOBS = [
  { id: 'job_101', model: 'Customer Churn Predictor', status: 'completed', duration: '45m', startedAt: '2023-12-18 09:00' },
  { id: 'job_102', model: 'Demand Forecast', status: 'running', progress: 65, duration: '1h 20m', startedAt: '2023-12-18 10:30' },
  { id: 'job_103', model: 'Inventory Opt', status: 'failed', duration: '5m', startedAt: '2023-12-18 11:15' },
];

function TabButton({ active, onClick, icon, children }: { 
  active: boolean; 
  onClick: () => void; 
  icon: React.ReactNode;
  children: React.ReactNode;
}) {
  return (
    <button
      onClick={onClick}
      className={cn(
        "flex items-center gap-2 px-4 py-3 text-sm font-medium transition-colors border-b-2",
        active 
          ? "text-alpha-500 border-alpha-500" 
          : "theme-text-muted border-transparent hover:theme-text"
      )}
    >
      {icon}
      {children}
    </button>
  );
}

export default function MLDashboardPage() {
  const [tabValue, setTabValue] = useState(0);
  const [openTrainDialog, setOpenTrainDialog] = useState(false);
  const [inferenceInput, setInferenceInput] = useState('');
  const [inferenceResult, setInferenceResult] = useState<any>(null);
  const [selectedModel, setSelectedModel] = useState(MOCK_MODELS[0].id);

  const handleInference = () => {
    setInferenceResult({
      prediction: 'High Risk',
      probability: 0.89,
      factors: ['Low Usage', 'Recent Support Ticket']
    });
  };

  const getStatusStyle = (status: string) => {
    switch (status) {
      case 'production': return 'bg-green-500/20 text-green-400 border-green-500/30';
      case 'staging': return 'bg-amber-500/20 text-amber-400 border-amber-500/30';
      case 'archived': return 'bg-gray-500/20 text-gray-400 border-gray-500/30';
      case 'completed': return 'bg-green-500/20 text-green-400 border-green-500/30';
      case 'running': return 'bg-blue-500/20 text-blue-400 border-blue-500/30';
      case 'failed': return 'bg-red-500/20 text-red-400 border-red-500/30';
      default: return 'bg-gray-500/20 text-gray-400 border-gray-500/30';
    }
  };

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title tracking-wide">ML Model Registry</h1>
          <p className="theme-text-muted mt-1">Manage, train, and deploy machine learning models</p>
        </div>
        <Button onClick={() => setOpenTrainDialog(true)}>
          <Plus className="w-4 h-4 mr-2" />
          New Training Job
        </Button>
      </div>

      {/* Tabs */}
      <div className="border-b theme-border">
        <div className="flex">
          <TabButton active={tabValue === 0} onClick={() => setTabValue(0)} icon={<Brain className="w-4 h-4" />}>
            Models
          </TabButton>
          <TabButton active={tabValue === 1} onClick={() => setTabValue(1)} icon={<FlaskConical className="w-4 h-4" />}>
            Training Jobs
          </TabButton>
          <TabButton active={tabValue === 2} onClick={() => setTabValue(2)} icon={<Sparkles className="w-4 h-4" />}>
            Inference Playground
          </TabButton>
        </div>
      </div>

      {/* Models Tab */}
      {tabValue === 0 && (
        <Card>
          <CardContent className="p-0">
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b theme-border">
                    <th className="px-4 py-3 text-left theme-text-muted font-medium">Model Name</th>
                    <th className="px-4 py-3 text-left theme-text-muted font-medium">Version</th>
                    <th className="px-4 py-3 text-left theme-text-muted font-medium">Type</th>
                    <th className="px-4 py-3 text-left theme-text-muted font-medium">Status</th>
                    <th className="px-4 py-3 text-left theme-text-muted font-medium">Performance</th>
                    <th className="px-4 py-3 text-left theme-text-muted font-medium">Last Trained</th>
                    <th className="px-4 py-3 text-right theme-text-muted font-medium">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {MOCK_MODELS.map((row) => (
                    <tr key={row.id} className="border-b theme-border hover:theme-card-bg-hover">
                      <td className="px-4 py-3 font-semibold theme-text-title">{row.name}</td>
                      <td className="px-4 py-3">
                        <span className="px-2 py-0.5 rounded-full text-xs border theme-border theme-text-muted">
                          {row.version}
                        </span>
                      </td>
                      <td className="px-4 py-3 theme-text-muted">{row.type}</td>
                      <td className="px-4 py-3">
                        <span className={cn("px-2 py-1 rounded-full text-xs font-medium border", getStatusStyle(row.status))}>
                          {row.status.toUpperCase()}
                        </span>
                      </td>
                      <td className="px-4 py-3 theme-text">{row.accuracy}</td>
                      <td className="px-4 py-3 theme-text-muted">{row.lastTrained}</td>
                      <td className="px-4 py-3 text-right">
                        <button className="p-1 rounded hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800">
                          <MoreVertical className="w-4 h-4 theme-text-muted" />
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Training Jobs Tab */}
      {tabValue === 1 && (
        <div className="space-y-3">
          {MOCK_JOBS.map((job) => (
            <Card key={job.id}>
              <CardContent className="p-4">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    {job.status === 'completed' && <CheckCircle className="w-5 h-5 text-green-500" />}
                    {job.status === 'failed' && <XCircle className="w-5 h-5 text-red-500" />}
                    {job.status === 'running' && <Clock className="w-5 h-5 text-blue-500 animate-pulse" />}
                    
                    <div>
                      <p className="font-semibold theme-text-title">{job.model}</p>
                      <p className="text-xs theme-text-muted">ID: {job.id} • Started: {job.startedAt}</p>
                    </div>
                  </div>

                  {job.status === 'running' && job.progress && (
                    <div className="w-1/4">
                      <div className="flex justify-end mb-1">
                        <span className="text-xs theme-text-muted">{job.progress}%</span>
                      </div>
                      <div className="h-2 rounded-full bg-alpha-faded-200 dark:bg-alpha-faded-800 overflow-hidden">
                        <div 
                          className="h-full bg-alpha-500 transition-all duration-300"
                          style={{ width: `${job.progress}%` }}
                        />
                      </div>
                    </div>
                  )}

                  <div className="flex items-center gap-3">
                    <span className={cn("px-2 py-1 rounded-full text-xs font-medium border", getStatusStyle(job.status))}>
                      {job.status}
                    </span>
                    <span className="text-xs theme-text-muted">{job.duration}</span>
                  </div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      )}

      {/* Inference Tab */}
      {tabValue === 2 && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <Card>
            <CardHeader>
              <CardTitle>Input Parameters</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div>
                <label className="text-sm font-medium theme-text-title block mb-2">Select Model</label>
                <select
                  value={selectedModel}
                  onChange={(e) => setSelectedModel(e.target.value)}
                  className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                >
                  {MOCK_MODELS.map(m => (
                    <option key={m.id} value={m.id}>{m.name} ({m.version})</option>
                  ))}
                </select>
              </div>
              
              <div>
                <label className="text-sm font-medium theme-text-title block mb-2">Feature Vector (JSON)</label>
                <textarea
                  value={inferenceInput}
                  onChange={(e) => setInferenceInput(e.target.value)}
                  placeholder={'{\n  "age": 34,\n  "usage_score": 0.85,\n  "last_login_days": 2\n}'}
                  rows={8}
                  className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text font-mono text-sm focus:outline-none focus:ring-2 focus:ring-alpha-500"
                />
              </div>
              
              <Button onClick={handleInference} className="w-full">
                <Play className="w-4 h-4 mr-2" />
                Run Prediction
              </Button>
            </CardContent>
          </Card>
          
          <Card className="theme-card-bg">
            <CardHeader>
              <CardTitle>Prediction Result</CardTitle>
            </CardHeader>
            <CardContent>
              {inferenceResult ? (
                <div className="space-y-4">
                  <div className="p-6 rounded-xl border theme-border text-center">
                    <p className="text-xs uppercase tracking-wide theme-text-muted mb-2">Class Label</p>
                    <p className="text-4xl font-bold theme-text-vibrant">{inferenceResult.prediction}</p>
                  </div>
                  
                  <div>
                    <p className="text-sm font-medium theme-text-title mb-2">Confidence Score</p>
                    <div className="flex items-center gap-3">
                      <div className="flex-1 h-3 rounded-full bg-alpha-faded-200 dark:bg-alpha-faded-800 overflow-hidden">
                        <div 
                          className="h-full bg-alpha-500 transition-all duration-500"
                          style={{ width: `${inferenceResult.probability * 100}%` }}
                        />
                      </div>
                      <span className="text-sm font-medium theme-text">{Math.round(inferenceResult.probability * 100)}%</span>
                    </div>
                  </div>

                  <div>
                    <p className="text-sm font-medium theme-text-title mb-2">Top Contributing Factors</p>
                    <div className="flex flex-wrap gap-2">
                      {inferenceResult.factors.map((f: string) => (
                        <span key={f} className="px-3 py-1 rounded-full text-sm theme-card-bg border theme-border theme-text">
                          {f}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>
              ) : (
                <div className="flex flex-col items-center justify-center py-16 text-center">
                  <Sparkles className="w-16 h-16 theme-text-muted opacity-30 mb-4" />
                  <p className="theme-text-muted">Run a prediction to see results</p>
                </div>
              )}
            </CardContent>
          </Card>
        </div>
      )}

      {/* New Training Job Dialog */}
      {openTrainDialog && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="w-full max-w-lg mx-4 rounded-2xl theme-card-bg border theme-border shadow-2xl">
            <div className="p-6 border-b theme-border flex items-center justify-between">
              <h2 className="text-xl font-bold theme-text-title">Start Training Job</h2>
              <button onClick={() => setOpenTrainDialog(false)} className="p-2 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800">
                <X className="w-5 h-5 theme-text-muted" />
              </button>
            </div>
            <div className="p-6 space-y-4">
              <div>
                <label className="text-sm font-medium theme-text-title block mb-2">Dataset</label>
                <select className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500">
                  <option value="">Select a dataset...</option>
                  <option value="ds_churn_training">Churn Training Set (Dec 2023)</option>
                  <option value="ds_sales_hist">Sales History (2020-2023)</option>
                </select>
              </div>
              <div>
                <label className="text-sm font-medium theme-text-title block mb-2">Algorithm</label>
                <select className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500">
                  <option value="">Select an algorithm...</option>
                  <option value="xgboost">XGBoost Classifier</option>
                  <option value="random_forest">Random Forest</option>
                  <option value="linear_reg">Linear Regression</option>
                </select>
              </div>
              <div>
                <label className="text-sm font-medium theme-text-title block mb-2">Hyperparameters (JSON)</label>
                <textarea
                  defaultValue="{}"
                  rows={4}
                  className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text font-mono text-sm focus:outline-none focus:ring-2 focus:ring-alpha-500"
                />
              </div>
            </div>
            <div className="p-6 border-t theme-border flex justify-end gap-3">
              <Button variant="outline" onClick={() => setOpenTrainDialog(false)}>Cancel</Button>
              <Button onClick={() => setOpenTrainDialog(false)}>Launch Job</Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
