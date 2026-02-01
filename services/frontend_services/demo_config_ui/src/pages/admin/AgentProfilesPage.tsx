import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { 
  Search, 
  Users, 
  Shield, 
  ChevronRight,
  Brain,
  Code,
  TestTube,
  FileText,
  Database,
  Rocket,
  ClipboardList,
  Network,
  Settings,
  TrendingUp,
  Target,
  BarChart3,
  Briefcase,
  UserCheck,
  Truck,
  LineChart,
  Workflow,
  Palette,
  Activity,
  Users2,
  ShieldCheck,
  GitBranch,
  Link,
  FileSearch,
  BookOpen,
} from 'lucide-react';

interface AgentInfo {
  id: string;
  name: string;
  role: string;
  category: 'business' | 'sub';
  description: string;
  icon: React.ReactNode;
  tier0Rules: number;
  tier1Rules: number;
  tier2Rules: number;
  reviewer: string;
}

const agents: AgentInfo[] = [
  // Sub-Agents (Technical)
  { id: 'architect', name: 'Architect Agent', role: 'architect', category: 'sub', description: 'Value chain structure and entity design', icon: <Network className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 3, tier2Rules: 2, reviewer: 'business_strategist' },
  { id: 'business_analyst', name: 'Business Analyst Agent', role: 'business_analyst', category: 'sub', description: 'Industry expertise and KPI identification', icon: <ClipboardList className="w-5 h-5" />, tier0Rules: 4, tier1Rules: 5, tier2Rules: 3, reviewer: 'business_strategist' },
  { id: 'developer', name: 'Developer Agent', role: 'developer', category: 'sub', description: 'Code and schema generation', icon: <Code className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 4, tier2Rules: 2, reviewer: 'architect' },
  { id: 'tester', name: 'Tester Agent', role: 'tester', category: 'sub', description: 'Validation and quality assurance', icon: <TestTube className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 3, tier2Rules: 2, reviewer: 'developer' },
  { id: 'documenter', name: 'Documenter Agent', role: 'documenter', category: 'sub', description: 'Documentation generation', icon: <FileText className="w-5 h-5" />, tier0Rules: 2, tier1Rules: 3, tier2Rules: 2, reviewer: 'architect' },
  { id: 'data_analyst', name: 'Data Analyst Agent', role: 'data_analyst', category: 'sub', description: 'Set-based KPI design and calculation optimization', icon: <Database className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 4, tier2Rules: 3, reviewer: 'business_analyst' },
  { id: 'deployment_specialist', name: 'Deployment Specialist Agent', role: 'deployment_specialist', category: 'sub', description: 'Azure infrastructure and deployment', icon: <Rocket className="w-5 h-5" />, tier0Rules: 4, tier1Rules: 4, tier2Rules: 2, reviewer: 'architect' },
  { id: 'project_manager', name: 'Project Manager Agent', role: 'project_manager', category: 'sub', description: 'Agile planning and work breakdown', icon: <ClipboardList className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 4, tier2Rules: 2, reviewer: 'coordinator' },
  { id: 'itil_manager', name: 'ITIL Manager Agent', role: 'itil_manager', category: 'sub', description: 'IT Service Management (ITIL 4 framework)', icon: <Settings className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 4, tier2Rules: 2, reviewer: 'architect' },
  { id: 'mapping_specialist', name: 'Mapping Specialist Agent', role: 'mapping_specialist', category: 'sub', description: 'Source-to-analytics attribute mapping', icon: <GitBranch className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 4, tier2Rules: 2, reviewer: 'data_analyst' },
  { id: 'connection_specialist', name: 'Connection Specialist Agent', role: 'connection_specialist', category: 'sub', description: 'System connections design and automation', icon: <Link className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 4, tier2Rules: 2, reviewer: 'architect' },
  { id: 'document_analyzer', name: 'Document Analyzer Agent', role: 'document_analyzer', category: 'sub', description: 'Analyzes documentation from interviewees', icon: <FileSearch className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 3, tier2Rules: 2, reviewer: 'business_analyst' },
  { id: 'librarian_curator', name: 'Librarian Curator Agent', role: 'librarian_curator', category: 'sub', description: 'Ontology management and curation', icon: <BookOpen className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 4, tier2Rules: 2, reviewer: 'architect' },
  
  // Business Agents
  { id: 'sales_manager', name: 'Sales Manager Agent', role: 'sales_manager', category: 'business', description: 'CRM lifecycle management', icon: <TrendingUp className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 4, tier2Rules: 2, reviewer: 'business_strategist' },
  { id: 'accountant', name: 'Accountant Agent', role: 'accountant', category: 'business', description: 'Financial operations management', icon: <BarChart3 className="w-5 h-5" />, tier0Rules: 4, tier1Rules: 4, tier2Rules: 2, reviewer: 'business_analyst' },
  { id: 'data_governance_specialist', name: 'Data Governance Specialist Agent', role: 'data_governance_specialist', category: 'business', description: 'DAMA DMBOK data governance principles', icon: <Shield className="w-5 h-5" />, tier0Rules: 4, tier1Rules: 5, tier2Rules: 3, reviewer: 'architect' },
  { id: 'data_scientist', name: 'Data Scientist Agent', role: 'data_scientist', category: 'business', description: 'KPI correlation analysis and ML recommendations', icon: <Brain className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 4, tier2Rules: 3, reviewer: 'data_analyst' },
  { id: 'marketing_manager', name: 'Marketing Manager Agent', role: 'marketing_manager', category: 'business', description: 'Marketing strategy and campaign management', icon: <Target className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 4, tier2Rules: 2, reviewer: 'business_strategist' },
  { id: 'ui_designer', name: 'UI Designer Agent', role: 'ui_designer', category: 'business', description: 'Analytics dashboard design and styling', icon: <Palette className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 4, tier2Rules: 2, reviewer: 'architect' },
  { id: 'business_strategist', name: 'Business Strategist Agent', role: 'business_strategist', category: 'business', description: "Porter's strategic frameworks analysis", icon: <Briefcase className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 3, tier2Rules: 2, reviewer: 'business_analyst' },
  { id: 'operations_manager', name: 'Operations Manager Agent', role: 'operations_manager', category: 'business', description: 'Holistic KPI analysis and performance optimization', icon: <Activity className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 4, tier2Rules: 2, reviewer: 'business_strategist' },
  { id: 'customer_success_manager', name: 'Customer Success Manager Agent', role: 'customer_success_manager', category: 'business', description: 'Post-sale customer lifecycle', icon: <UserCheck className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 4, tier2Rules: 2, reviewer: 'sales_manager' },
  { id: 'hr_talent_analyst', name: 'HR/Talent Analyst Agent', role: 'hr_talent_analyst', category: 'business', description: 'People analytics and workforce optimization', icon: <Users2 className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 4, tier2Rules: 2, reviewer: 'business_analyst' },
  { id: 'risk_compliance_officer', name: 'Risk & Compliance Officer Agent', role: 'risk_compliance_officer', category: 'business', description: 'Risk management and regulatory compliance', icon: <ShieldCheck className="w-5 h-5" />, tier0Rules: 4, tier1Rules: 5, tier2Rules: 3, reviewer: 'data_governance_specialist' },
  { id: 'supply_chain_analyst', name: 'Supply Chain Analyst Agent', role: 'supply_chain_analyst', category: 'business', description: 'Supply chain optimization', icon: <Truck className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 4, tier2Rules: 2, reviewer: 'operations_manager' },
  { id: 'competitive_analyst', name: 'Competitive Analyst Agent', role: 'competitive_analyst', category: 'business', description: 'Competitive intelligence research', icon: <LineChart className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 4, tier2Rules: 2, reviewer: 'business_strategist' },
  { id: 'process_scenario_modeler', name: 'Process Scenario Modeler Agent', role: 'process_scenario_modeler', category: 'business', description: 'Process simulation and what-if analysis', icon: <Workflow className="w-5 h-5" />, tier0Rules: 3, tier1Rules: 4, tier2Rules: 2, reviewer: 'operations_manager' },
];

export default function AgentProfilesPage() {
  const navigate = useNavigate();
  const [searchTerm, setSearchTerm] = useState('');
  const [categoryFilter, setCategoryFilter] = useState<'all' | 'business' | 'sub'>('all');

  const filteredAgents = agents.filter((agent) => {
    const matchesSearch = agent.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                          agent.description.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesCategory = categoryFilter === 'all' || agent.category === categoryFilter;
    return matchesSearch && matchesCategory;
  });

  const businessAgents = filteredAgents.filter(a => a.category === 'business');
  const subAgents = filteredAgents.filter(a => a.category === 'sub');

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title">Agent Profiles</h1>
          <p className="mt-2 theme-text-secondary">
            View and manage the 27 AI agent contracts that power the platform
          </p>
        </div>
        <div className="flex items-center gap-2 px-4 py-2 rounded-lg bg-amber-500/10 text-amber-400">
          <Shield className="w-5 h-5" />
          <span className="font-medium">Admin Access</span>
        </div>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-4 gap-4">
        <div className="theme-card rounded-xl p-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-lg bg-alpha-500/10 flex items-center justify-center">
              <Users className="w-5 h-5 text-alpha-400" />
            </div>
            <div>
              <p className="text-2xl font-bold theme-text-title">{agents.length}</p>
              <p className="text-sm theme-text-muted">Total Agents</p>
            </div>
          </div>
        </div>
        <div className="theme-card rounded-xl p-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-lg bg-emerald-500/10 flex items-center justify-center">
              <Briefcase className="w-5 h-5 text-emerald-400" />
            </div>
            <div>
              <p className="text-2xl font-bold theme-text-title">{agents.filter(a => a.category === 'business').length}</p>
              <p className="text-sm theme-text-muted">Business Agents</p>
            </div>
          </div>
        </div>
        <div className="theme-card rounded-xl p-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-lg bg-blue-500/10 flex items-center justify-center">
              <Code className="w-5 h-5 text-blue-400" />
            </div>
            <div>
              <p className="text-2xl font-bold theme-text-title">{agents.filter(a => a.category === 'sub').length}</p>
              <p className="text-sm theme-text-muted">Sub-Agents</p>
            </div>
          </div>
        </div>
        <div className="theme-card rounded-xl p-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-lg bg-red-500/10 flex items-center justify-center">
              <Shield className="w-5 h-5 text-red-400" />
            </div>
            <div>
              <p className="text-2xl font-bold theme-text-title">{agents.reduce((sum, a) => sum + a.tier0Rules, 0)}</p>
              <p className="text-sm theme-text-muted">Tier 0 Rules</p>
            </div>
          </div>
        </div>
      </div>

      {/* Filters */}
      <div className="theme-card rounded-xl p-4">
        <div className="flex items-center gap-4">
          <div className="relative flex-1">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 theme-text-muted" />
            <input
              type="text"
              placeholder="Search agents..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-9 pr-4 py-2 rounded-lg theme-input text-sm"
            />
          </div>
          <div className="flex items-center gap-2">
            <button
              onClick={() => setCategoryFilter('all')}
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                categoryFilter === 'all' 
                  ? 'bg-alpha-500 text-white' 
                  : 'theme-card hover:bg-[var(--card-hover)] theme-text-secondary'
              }`}
            >
              All
            </button>
            <button
              onClick={() => setCategoryFilter('business')}
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                categoryFilter === 'business' 
                  ? 'bg-emerald-500 text-white' 
                  : 'theme-card hover:bg-[var(--card-hover)] theme-text-secondary'
              }`}
            >
              Business
            </button>
            <button
              onClick={() => setCategoryFilter('sub')}
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                categoryFilter === 'sub' 
                  ? 'bg-blue-500 text-white' 
                  : 'theme-card hover:bg-[var(--card-hover)] theme-text-secondary'
              }`}
            >
              Sub-Agents
            </button>
          </div>
        </div>
      </div>

      {/* Business Agents */}
      {businessAgents.length > 0 && (categoryFilter === 'all' || categoryFilter === 'business') && (
        <div>
          <h2 className="text-lg font-semibold theme-text-title mb-4 flex items-center gap-2">
            <Briefcase className="w-5 h-5 text-emerald-400" />
            Business Agents ({businessAgents.length})
          </h2>
          <div className="grid grid-cols-2 gap-4">
            {businessAgents.map((agent) => (
              <div
                key={agent.id}
                onClick={() => navigate(`/admin/agents/${agent.id}`)}
                className="theme-card rounded-xl p-4 hover:bg-[var(--card-hover)] cursor-pointer transition-colors group"
              >
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 rounded-xl bg-emerald-500/10 flex items-center justify-center flex-shrink-0">
                    <span className="text-emerald-400">{agent.icon}</span>
                  </div>
                  <div className="flex-1 min-w-0">
                    <h3 className="font-semibold theme-text-title group-hover:text-alpha-400 transition-colors">
                      {agent.name}
                    </h3>
                    <p className="text-sm theme-text-muted mt-1">{agent.description}</p>
                    <div className="flex items-center gap-3 mt-3">
                      <span className="text-xs px-2 py-1 rounded bg-red-500/10 text-red-400">
                        T0: {agent.tier0Rules}
                      </span>
                      <span className="text-xs px-2 py-1 rounded bg-amber-500/10 text-amber-400">
                        T1: {agent.tier1Rules}
                      </span>
                      <span className="text-xs px-2 py-1 rounded bg-blue-500/10 text-blue-400">
                        T2: {agent.tier2Rules}
                      </span>
                      <span className="text-xs theme-text-muted">
                        Reviewer: {agent.reviewer}
                      </span>
                    </div>
                  </div>
                  <ChevronRight className="w-5 h-5 theme-text-muted group-hover:text-alpha-400 transition-colors" />
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Sub-Agents */}
      {subAgents.length > 0 && (categoryFilter === 'all' || categoryFilter === 'sub') && (
        <div>
          <h2 className="text-lg font-semibold theme-text-title mb-4 flex items-center gap-2">
            <Code className="w-5 h-5 text-blue-400" />
            Sub-Agents ({subAgents.length})
          </h2>
          <div className="grid grid-cols-2 gap-4">
            {subAgents.map((agent) => (
              <div
                key={agent.id}
                onClick={() => navigate(`/admin/agents/${agent.id}`)}
                className="theme-card rounded-xl p-4 hover:bg-[var(--card-hover)] cursor-pointer transition-colors group"
              >
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 rounded-xl bg-blue-500/10 flex items-center justify-center flex-shrink-0">
                    <span className="text-blue-400">{agent.icon}</span>
                  </div>
                  <div className="flex-1 min-w-0">
                    <h3 className="font-semibold theme-text-title group-hover:text-alpha-400 transition-colors">
                      {agent.name}
                    </h3>
                    <p className="text-sm theme-text-muted mt-1">{agent.description}</p>
                    <div className="flex items-center gap-3 mt-3">
                      <span className="text-xs px-2 py-1 rounded bg-red-500/10 text-red-400">
                        T0: {agent.tier0Rules}
                      </span>
                      <span className="text-xs px-2 py-1 rounded bg-amber-500/10 text-amber-400">
                        T1: {agent.tier1Rules}
                      </span>
                      <span className="text-xs px-2 py-1 rounded bg-blue-500/10 text-blue-400">
                        T2: {agent.tier2Rules}
                      </span>
                      <span className="text-xs theme-text-muted">
                        Reviewer: {agent.reviewer}
                      </span>
                    </div>
                  </div>
                  <ChevronRight className="w-5 h-5 theme-text-muted group-hover:text-alpha-400 transition-colors" />
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {filteredAgents.length === 0 && (
        <div className="text-center py-12 theme-text-muted">
          <Users className="w-12 h-12 mx-auto mb-4 opacity-50" />
          <p>No agents found matching your search</p>
        </div>
      )}
    </div>
  );
}
