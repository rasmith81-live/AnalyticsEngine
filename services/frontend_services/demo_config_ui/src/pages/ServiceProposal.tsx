import { useState } from 'react';
import {
  FileText,
  Clock,
  DollarSign,
  Zap,
  CheckCircle,
  Download,
  Send,
  Database,
  Building2,
  Users,
  Server,
  Loader2,
  AlertCircle,
} from 'lucide-react';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { cn } from '../lib/utils';
import { useCart } from '../contexts/CartContext';
import { configApi, ServiceProposal as ServiceProposalType } from '../api/configApi';
import ResourceScheduler from '../components/proposal/ResourceScheduler';
import ProjectGanttChart from '../components/proposal/ProjectGanttChart';

// Mock client ID for demo purposes
const DEMO_CLIENT_ID = 'demo-client-123';

const PROPOSAL_STEPS = ['KPI Selection', 'Integration Strategy', 'Review Estimate', 'Finalize SOW'];

export default function ServiceProposal() {
  const { selectedKPIs } = useCart();
  const [activeStep, setActiveStep] = useState(0);
  const [integrationMethod, setIntegrationMethod] = useState<'batch' | 'realtime'>('batch');
  const [licenseTier, setLicenseTier] = useState<'starter' | 'professional' | 'enterprise'>('professional');
  const [userCount, setUserCount] = useState<number>(10);
  const [infrastructure, setInfrastructure] = useState<'cloud' | 'onprem'>('cloud');
  
  const [loading, setLoading] = useState(false);
  const [proposal, setProposal] = useState<ServiceProposalType | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleGenerateProposal = async () => {
    setLoading(true);
    setError(null);
    try {
      // @ts-ignore - Extending the API call with new parameters
      const result = await configApi.generateProposal(DEMO_CLIENT_ID, {
        integration_method: integrationMethod,
        included_kpis: selectedKPIs,
        license_tier: licenseTier,
        user_count: userCount,
        infrastructure: infrastructure
      });
      setProposal(result);
      setActiveStep(2);
    } catch (err) {
      console.error('Error generating proposal:', err);
      setError('Failed to generate proposal. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleUpdateStatus = async (status: 'sent' | 'signed') => {
    if (!proposal || !proposal.id) return;
    
    try {
      const updated = await configApi.updateProposal(DEMO_CLIENT_ID, {
        status: status
      });
      setProposal(updated);
      setActiveStep(3);
    } catch (err) {
      console.error('Error updating proposal:', err);
      setError('Failed to update proposal status.');
    }
  };

  const handleExportSOW = () => {
    if (!proposal) return;
    // Stub implementation for PDF export
    console.log('Exporting SOW for proposal:', proposal.id);
    
    const content = `
      STATEMENT OF WORK
      ----------------
      Client ID: ${DEMO_CLIENT_ID}
      Date: ${new Date().toLocaleDateString()}
      
      Scope:
      - ${selectedKPIs.length} KPIs selected
      - Integration Method: ${integrationMethod}
      - License Tier: ${licenseTier}
      - Infrastructure: ${infrastructure}
      
      Timeline: ${proposal.timeline_weeks} weeks
      Total Estimated Cost: $${proposal.estimated_cost}
    `;
    
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `SOW_${DEMO_CLIENT_ID}_${new Date().toISOString().split('T')[0]}.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      maximumFractionDigits: 0,
    }).format(amount);
  };

  if (selectedKPIs.length === 0) {
    return (
      <div className="p-6 text-center">
        <Card className="p-10 max-w-md mx-auto">
          <FileText className="w-16 h-16 mx-auto mb-4 theme-text-muted" />
          <h2 className="text-xl font-semibold theme-text-title mb-2">
            No KPIs Selected
          </h2>
          <p className="theme-text-muted mb-6">
            Please select KPIs from the Metric Tree or Object Models to generate a proposal.
          </p>
          <Button onClick={() => window.location.href = '/demo'}>
            Go to Metric Tree
          </Button>
        </Card>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold theme-text-title">
        Service Proposal Generator
      </h1>
      
      {/* Stepper */}
      <div className="flex items-center justify-between mb-6">
        {PROPOSAL_STEPS.map((label, index) => (
          <div key={label} className="flex items-center flex-1">
            <div className="flex items-center">
              <div
                className={cn(
                  "w-8 h-8 rounded-full flex items-center justify-center text-sm font-medium border-2 transition-colors",
                  index < activeStep && "bg-green-500 border-green-500 text-white",
                  index === activeStep && "bg-alpha-500 border-alpha-500 text-white",
                  index > activeStep && "border-alpha-faded-300 dark:border-alpha-faded-600 theme-text-muted"
                )}
              >
                {index < activeStep ? <CheckCircle className="w-4 h-4" /> : index + 1}
              </div>
              <span className={cn(
                "ml-2 text-sm hidden sm:inline",
                index <= activeStep ? "theme-text-title font-medium" : "theme-text-muted"
              )}>
                {label}
              </span>
            </div>
            {index < PROPOSAL_STEPS.length - 1 && (
              <div className={cn(
                "flex-1 h-0.5 mx-4",
                index < activeStep ? "bg-green-500" : "bg-alpha-faded-200 dark:bg-alpha-faded-700"
              )} />
            )}
          </div>
        ))}
      </div>

      {error && (
        <div className="flex items-center gap-2 p-3 rounded-lg bg-red-500/10 border border-red-500/30 text-red-400">
          <AlertCircle className="w-5 h-5" />
          <span>{error}</span>
        </div>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Configuration Panel */}
        <div className="lg:col-span-5">
          <Card className="p-5 h-full">
            <h2 className="text-lg font-semibold theme-text-title mb-4">
              Proposal Configuration
            </h2>
            
            {/* Selected KPIs */}
            <div className="mb-4">
              <p className="text-sm font-medium theme-text mb-2">
                Selected KPIs ({selectedKPIs.length})
              </p>
              <div className="flex flex-wrap gap-1.5">
                {selectedKPIs.map((kpi) => (
                  <span
                    key={kpi}
                    className="px-2 py-0.5 rounded text-xs theme-card-bg border theme-border theme-text"
                  >
                    {kpi}
                  </span>
                ))}
              </div>
            </div>

            <div className="border-t theme-border my-4" />

            {/* License Configuration */}
            <div className="mb-4">
              <div className="flex items-center gap-2 mb-3">
                <Building2 className="w-4 h-4 theme-text-muted" />
                <span className="text-sm font-medium theme-text">License Configuration</span>
              </div>
              
              <div className="mb-3">
                <label className="block text-xs theme-text-muted mb-1">License Tier</label>
                <select
                  value={licenseTier}
                  onChange={(e) => setLicenseTier(e.target.value as any)}
                  className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text text-sm focus:outline-none focus:ring-2 focus:ring-alpha-500"
                >
                  <option value="starter">Starter (Up to 5 Users)</option>
                  <option value="professional">Professional (Up to 50 Users)</option>
                  <option value="enterprise">Enterprise (Unlimited)</option>
                </select>
              </div>

              <div>
                <label className="block text-xs theme-text-muted mb-1">User Count: {userCount}</label>
                <div className="flex items-center gap-3">
                  <Users className="w-4 h-4 theme-text-muted" />
                  <input
                    type="range"
                    value={userCount}
                    onChange={(e) => setUserCount(Number(e.target.value))}
                    min={1}
                    max={100}
                    className="flex-1 h-2 bg-alpha-faded-200 dark:bg-alpha-faded-700 rounded-lg appearance-none cursor-pointer accent-alpha-500"
                  />
                  <input
                    type="number"
                    value={userCount}
                    onChange={(e) => setUserCount(Number(e.target.value))}
                    className="w-16 px-2 py-1 rounded theme-card-bg border theme-border theme-text text-sm text-center focus:outline-none focus:ring-2 focus:ring-alpha-500"
                  />
                </div>
              </div>
            </div>

            {/* Infrastructure */}
            <div className="mb-4">
              <div className="flex items-center gap-2 mb-3">
                <Server className="w-4 h-4 theme-text-muted" />
                <span className="text-sm font-medium theme-text">Infrastructure</span>
              </div>
              
              <select
                value={infrastructure}
                onChange={(e) => setInfrastructure(e.target.value as any)}
                className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text text-sm focus:outline-none focus:ring-2 focus:ring-alpha-500"
              >
                <option value="cloud">Managed Cloud (SaaS)</option>
                <option value="onprem">On-Premise / Private Cloud</option>
              </select>
            </div>

            {/* Integration Strategy */}
            <div className="mb-6">
              <p className="text-sm font-medium theme-text mb-3">Integration Strategy</p>
              <div className="grid grid-cols-2 gap-3">
                <button
                  onClick={() => setIntegrationMethod('batch')}
                  className={cn(
                    "p-4 rounded-lg border-2 transition-all text-center",
                    integrationMethod === 'batch'
                      ? "border-alpha-500 bg-alpha-500/10"
                      : "border-alpha-faded-200 dark:border-alpha-faded-700 hover:border-alpha-faded-400"
                  )}
                >
                  <Database className={cn(
                    "w-6 h-6 mx-auto mb-2",
                    integrationMethod === 'batch' ? "text-alpha-500" : "theme-text-muted"
                  )} />
                  <p className="font-medium text-sm theme-text">Batch Processing</p>
                  <p className="text-xs theme-text-muted mt-1">Lower cost, T+1 latency</p>
                </button>
                <button
                  onClick={() => setIntegrationMethod('realtime')}
                  className={cn(
                    "p-4 rounded-lg border-2 transition-all text-center",
                    integrationMethod === 'realtime'
                      ? "border-alpha-500 bg-alpha-500/10"
                      : "border-alpha-faded-200 dark:border-alpha-faded-700 hover:border-alpha-faded-400"
                  )}
                >
                  <Zap className={cn(
                    "w-6 h-6 mx-auto mb-2",
                    integrationMethod === 'realtime' ? "text-alpha-500" : "theme-text-muted"
                  )} />
                  <p className="font-medium text-sm theme-text">Real-time Stream</p>
                  <p className="text-xs theme-text-muted mt-1">Higher cost, instant updates</p>
                </button>
              </div>
            </div>

            <Button
              className="w-full"
              size="lg"
              onClick={handleGenerateProposal}
              disabled={loading}
            >
              {loading ? (
                <>
                  <Loader2 className="w-5 h-5 mr-2 animate-spin" />
                  Analyzing Requirements...
                </>
              ) : (
                <>
                  <FileText className="w-5 h-5 mr-2" />
                  Generate Estimate
                </>
              )}
            </Button>
          </Card>
        </div>

        {/* Results Panel */}
        <div className="lg:col-span-7">
          {proposal ? (
            <Card className="p-5">
              <div className="flex items-center justify-between mb-4">
                <h2 className="text-xl font-semibold theme-text-title">Statement of Work Estimate</h2>
                <span className={cn(
                  "px-3 py-1 rounded-full text-xs font-medium uppercase",
                  proposal.status === 'signed' 
                    ? "bg-green-500/20 text-green-400" 
                    : "bg-alpha-500/20 text-alpha-400"
                )}>
                  {proposal.status}
                </span>
              </div>

              {/* Summary Stats */}
              <div className="grid grid-cols-3 gap-4 mb-6">
                <Card className="p-4 text-center">
                  <DollarSign className="w-8 h-8 mx-auto text-alpha-500 mb-2" />
                  <p className="text-xl font-bold theme-text-title">{formatCurrency(proposal.estimated_cost)}</p>
                  <p className="text-xs theme-text-muted">Estimated Cost</p>
                </Card>
                <Card className="p-4 text-center">
                  <Clock className="w-8 h-8 mx-auto text-alpha-500 mb-2" />
                  <p className="text-xl font-bold theme-text-title">{proposal.timeline_weeks} Weeks</p>
                  <p className="text-xs theme-text-muted">Timeline</p>
                </Card>
                <Card className="p-4 text-center">
                  <CheckCircle className="w-8 h-8 mx-auto text-alpha-500 mb-2" />
                  <p className="text-xl font-bold theme-text-title">{proposal.required_objects.length}</p>
                  <p className="text-xs theme-text-muted">Data Objects</p>
                </Card>
              </div>

              {/* Charts */}
              <div className="space-y-4 mb-6">
                <ProjectGanttChart timelineWeeks={proposal.timeline_weeks} />
                <ResourceScheduler timelineWeeks={proposal.timeline_weeks} />
              </div>

              {/* Required Data Objects */}
              <div className="mb-4">
                <p className="text-sm font-medium theme-text mb-2">Required Data Objects</p>
                <div className="flex flex-wrap gap-1.5">
                  {proposal.required_objects.map(obj => (
                    <span
                      key={obj}
                      className="px-2 py-0.5 rounded text-xs border theme-border theme-text-muted"
                    >
                      {obj}
                    </span>
                  ))}
                </div>
              </div>

              <div className="border-t theme-border my-4" />

              {/* Actions */}
              <div className="flex justify-end gap-3">
                <Button variant="outline" onClick={handleExportSOW}>
                  <Download className="w-4 h-4 mr-2" />
                  Export PDF
                </Button>
                {proposal.status === 'draft' && (
                  <Button
                    className="bg-green-600 hover:bg-green-700"
                    onClick={() => handleUpdateStatus('sent')}
                  >
                    <Send className="w-4 h-4 mr-2" />
                    Send to Client
                  </Button>
                )}
                {proposal.status === 'sent' && (
                  <Button onClick={() => handleUpdateStatus('signed')}>
                    Mark as Signed
                  </Button>
                )}
              </div>
            </Card>
          ) : (
            <Card className="p-8 h-full flex flex-col items-center justify-center text-center min-h-[400px]">
              <Clock className="w-20 h-20 theme-text-muted opacity-50 mb-4" />
              <h3 className="text-lg font-semibold theme-text-muted mb-2">
                Generate a proposal to see cost and timeline estimates
              </h3>
              <p className="text-sm theme-text-muted max-w-md">
                Our engine analyzes the data lineage of your selected KPIs to determine exactly which data objects are required.
              </p>
            </Card>
          )}
        </div>
      </div>
    </div>
  );
}
