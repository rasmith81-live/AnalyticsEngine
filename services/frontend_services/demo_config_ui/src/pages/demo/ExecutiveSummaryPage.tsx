import { useState, useEffect } from 'react';
import { ClipboardCheck, Calendar, DollarSign, Check, ChevronLeft, Download, Send, Building2, Target, BarChart3, Users } from 'lucide-react';

interface TimelinePhase {
  id: string;
  name: string;
  duration: string;
  tasks: string[];
}

interface DesignArtifact {
  type: string;
  name: string;
  details?: {
    code?: string;
    category?: string;
  };
}

interface SessionDesign {
  kpis: DesignArtifact[];
  entities: DesignArtifact[];
  dashboards: DesignArtifact[];
  industry?: string;
}

const defaultTimeline: TimelinePhase[] = [
  {
    id: 'discovery',
    name: 'Discovery & Planning',
    duration: 'Week 1-2',
    tasks: ['Requirements validation', 'Data source assessment', 'Architecture finalization'],
  },
  {
    id: 'integration',
    name: 'Data Integration',
    duration: 'Week 3-5',
    tasks: ['Source system connections', 'Data pipeline setup', 'Quality validation'],
  },
  {
    id: 'configuration',
    name: 'Platform Configuration',
    duration: 'Week 6-8',
    tasks: ['KPI configuration', 'Dashboard setup', 'Alert rules definition'],
  },
  {
    id: 'training',
    name: 'Training & Go-Live',
    duration: 'Week 9-10',
    tasks: ['User training', 'UAT testing', 'Production deployment'],
  },
];

export default function ExecutiveSummaryPage() {
  const [agreed, setAgreed] = useState(false);
  const [sessionDesign, setSessionDesign] = useState<SessionDesign | null>(null);
  const [timeline, setTimeline] = useState<TimelinePhase[]>(defaultTimeline);

  // Load design from interview
  useEffect(() => {
    loadSessionDesign();
  }, []);

  const loadSessionDesign = () => {
    try {
      const storedDesign = localStorage.getItem('demo_interview_design');
      if (storedDesign) {
        const design = JSON.parse(storedDesign) as SessionDesign;
        setSessionDesign(design);
        
        // Adjust timeline based on complexity
        const kpiCount = design.kpis?.length || 0;
        const entityCount = design.entities?.length || 0;
        
        if (kpiCount > 10 || entityCount > 5) {
          // Complex project - extend timeline
          setTimeline([
            { id: 'discovery', name: 'Discovery & Planning', duration: 'Week 1-3', tasks: ['Detailed requirements', 'Data source mapping', 'Architecture design', 'Stakeholder alignment'] },
            { id: 'integration', name: 'Data Integration', duration: 'Week 4-7', tasks: [`Connect ${entityCount} data sources`, 'ETL pipeline development', 'Data quality rules', 'Integration testing'] },
            { id: 'configuration', name: 'Platform Configuration', duration: 'Week 8-11', tasks: [`Configure ${kpiCount} KPIs`, 'Dashboard development', 'Alert configuration', 'User roles setup'] },
            { id: 'training', name: 'Training & Go-Live', duration: 'Week 12-14', tasks: ['Admin training', 'End-user training', 'UAT testing', 'Production deployment'] },
          ]);
        }
      }
    } catch (err) {
      console.error('Failed to load session design:', err);
    }
  };

  // Calculate contract summary from design
  const contractSummary = {
    kpis: sessionDesign?.kpis?.length || 48,
    dashboards: sessionDesign?.dashboards?.length || 6,
    dataSources: sessionDesign?.entities?.length || 4,
    users: 25,
    annualLicense: Math.max(25000, (sessionDesign?.kpis?.length || 48) * 750),
    implementation: Math.max(50000, ((sessionDesign?.kpis?.length || 0) + (sessionDesign?.entities?.length || 0)) * 2500),
    managedServices: 8000,
  };

  const totalYear1 = contractSummary.annualLicense + contractSummary.implementation + contractSummary.managedServices;

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title">Executive Summary</h1>
          <p className="mt-2 theme-text-secondary">
            Your complete implementation plan and license agreement
          </p>
        </div>
        <div className="flex items-center gap-2 px-4 py-2 rounded-lg bg-alpha-500/10 text-alpha-400">
          <ClipboardCheck className="w-5 h-5" />
          <span className="font-medium">Step 6 of 6</span>
        </div>
      </div>

      {/* Summary Cards */}
      <div className="grid grid-cols-4 gap-6">
        <div className="theme-card rounded-2xl p-6">
          <div className="w-12 h-12 rounded-xl bg-purple-500/20 text-purple-400 flex items-center justify-center mb-4">
            <Target className="w-6 h-6" />
          </div>
          <p className="text-sm theme-text-muted mb-1">Selected KPIs</p>
          <p className="text-3xl font-bold theme-text-title">{contractSummary.kpis}</p>
        </div>
        <div className="theme-card rounded-2xl p-6">
          <div className="w-12 h-12 rounded-xl bg-blue-500/20 text-blue-400 flex items-center justify-center mb-4">
            <BarChart3 className="w-6 h-6" />
          </div>
          <p className="text-sm theme-text-muted mb-1">Dashboards</p>
          <p className="text-3xl font-bold theme-text-title">{contractSummary.dashboards}</p>
        </div>
        <div className="theme-card rounded-2xl p-6">
          <div className="w-12 h-12 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center mb-4">
            <Building2 className="w-6 h-6" />
          </div>
          <p className="text-sm theme-text-muted mb-1">Data Sources</p>
          <p className="text-3xl font-bold theme-text-title">{contractSummary.dataSources}</p>
        </div>
        <div className="theme-card rounded-2xl p-6">
          <div className="w-12 h-12 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center mb-4">
            <Users className="w-6 h-6" />
          </div>
          <p className="text-sm theme-text-muted mb-1">Licensed Users</p>
          <p className="text-3xl font-bold theme-text-title">{contractSummary.users}</p>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-8">
        {/* Implementation Timeline */}
        <div className="theme-card rounded-2xl p-6">
          <div className="flex items-center gap-3 mb-6">
            <Calendar className="w-6 h-6 text-alpha-400" />
            <h2 className="text-xl font-semibold theme-text-title">Implementation Timeline</h2>
          </div>
          <p className="text-sm theme-text-muted mb-6">
            Generated by Project Manager Agent based on your configuration
          </p>

          <div className="space-y-4">
            {timeline.map((phase: TimelinePhase, index: number) => (
              <div key={phase.id} className="relative pl-8">
                {/* Timeline Line */}
                {index < timeline.length - 1 && (
                  <div className="absolute left-3 top-8 w-0.5 h-full bg-slate-700" />
                )}
                {/* Timeline Dot */}
                <div className="absolute left-0 top-1 w-6 h-6 rounded-full bg-alpha-500/20 border-2 border-alpha-500 flex items-center justify-center">
                  <div className="w-2 h-2 rounded-full bg-alpha-500" />
                </div>
                
                <div className="pb-6">
                  <div className="flex items-center justify-between mb-2">
                    <h3 className="font-semibold theme-text-title">{phase.name}</h3>
                    <span className="text-sm px-3 py-1 rounded-full bg-alpha-500/10 text-alpha-400">
                      {phase.duration}
                    </span>
                  </div>
                  <ul className="space-y-1">
                    {phase.tasks.map((task: string, i: number) => (
                      <li key={i} className="text-sm theme-text-secondary flex items-center gap-2">
                        <div className="w-1 h-1 rounded-full bg-slate-500" />
                        {task}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* License Agreement */}
        <div className="theme-card rounded-2xl p-6">
          <div className="flex items-center gap-3 mb-6">
            <DollarSign className="w-6 h-6 text-emerald-400" />
            <h2 className="text-xl font-semibold theme-text-title">5-Year License Agreement</h2>
          </div>

          {/* Pricing Breakdown */}
          <div className="space-y-4 mb-6">
            <div className="flex items-center justify-between py-3 border-b theme-border">
              <div>
                <p className="font-medium theme-text-title">Annual Platform License</p>
                <p className="text-sm theme-text-muted">Full access to Northstar platform</p>
              </div>
              <p className="text-lg font-semibold theme-text-title">
                ${contractSummary.annualLicense.toLocaleString()}/yr
              </p>
            </div>
            <div className="flex items-center justify-between py-3 border-b theme-border">
              <div>
                <p className="font-medium theme-text-title">Implementation Services</p>
                <p className="text-sm theme-text-muted">One-time setup and configuration</p>
              </div>
              <p className="text-lg font-semibold theme-text-title">
                ${contractSummary.implementation.toLocaleString()}
              </p>
            </div>
            <div className="flex items-center justify-between py-3 border-b theme-border">
              <div>
                <p className="font-medium theme-text-title">Managed Services</p>
                <p className="text-sm theme-text-muted">Ongoing support and maintenance</p>
              </div>
              <p className="text-lg font-semibold theme-text-title">
                ${contractSummary.managedServices.toLocaleString()}/yr
              </p>
            </div>
          </div>

          {/* Total */}
          <div className="p-4 rounded-xl bg-gradient-to-r from-emerald-500/10 to-alpha-500/10 border border-emerald-500/20 mb-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm theme-text-muted">Year 1 Total Investment</p>
                <p className="text-3xl font-bold text-emerald-400">${totalYear1.toLocaleString()}</p>
              </div>
              <div className="text-right">
                <p className="text-sm theme-text-muted">Years 2-5 (Annual)</p>
                <p className="text-xl font-semibold theme-text-title">
                  ${(contractSummary.annualLicense + contractSummary.managedServices).toLocaleString()}
                </p>
              </div>
            </div>
          </div>

          {/* Agreement Checkbox */}
          <label className="flex items-start gap-3 p-4 rounded-xl theme-bg-secondary cursor-pointer mb-6">
            <input
              type="checkbox"
              checked={agreed}
              onChange={(e) => setAgreed(e.target.checked)}
              className="mt-1 w-5 h-5 rounded border-slate-600 bg-slate-700 text-alpha-500 focus:ring-alpha-500"
            />
            <div>
              <p className="font-medium theme-text-title">I agree to the terms and conditions</p>
              <p className="text-sm theme-text-muted">
                By checking this box, you acknowledge that you have reviewed and agree to the 
                Northstar Platform License Agreement and Implementation Services Agreement.
              </p>
            </div>
          </label>

          {/* Action Buttons */}
          <div className="flex gap-4">
            <button className="flex-1 px-6 py-3 rounded-xl theme-card hover:bg-[var(--card-hover)] font-medium transition-colors flex items-center justify-center gap-2">
              <Download className="w-5 h-5" />
              Download PDF
            </button>
            <button
              disabled={!agreed}
              className="flex-1 px-6 py-3 rounded-xl bg-emerald-500 hover:bg-emerald-600 disabled:opacity-50 disabled:cursor-not-allowed text-white font-medium transition-colors flex items-center justify-center gap-2"
            >
              <Send className="w-5 h-5" />
              Submit Agreement
            </button>
          </div>
        </div>
      </div>

      {/* Navigation */}
      <div className="flex justify-between">
        <a
          href="/demo/analytics"
          className="px-6 py-3 rounded-xl theme-card hover:bg-[var(--card-hover)] font-medium transition-colors flex items-center gap-2"
        >
          <ChevronLeft className="w-5 h-5" />
          Back to Analytics
        </a>
        <div className="flex items-center gap-2 text-sm theme-text-muted">
          <Check className="w-5 h-5 text-emerald-400" />
          Demo Complete — Thank you for exploring Northstar!
        </div>
      </div>
    </div>
  );
}
