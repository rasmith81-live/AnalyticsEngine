import { useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { 
  ArrowLeft, 
  Shield, 
  Edit3, 
  Save, 
  X,
  AlertTriangle,
  CheckCircle,
  Plus,
  Trash2,
  Play,
  Users,
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
  Loader2,
} from 'lucide-react';

// Core agents that cannot be modified or deleted via UI - only human users can change their code
// These agents form the agent modification pipeline itself
const PROTECTED_AGENTS = ['business_analyst', 'architect', 'developer', 'tester', 'documenter'];

interface ContractRule {
  id: string;
  text: string;
  isNew?: boolean;
}

interface AgentContract {
  id: string;
  name: string;
  role: string;
  category: 'business' | 'sub';
  description: string;
  icon: React.ReactNode;
  tier0Rules: ContractRule[];
  tier1Rules: ContractRule[];
  tier2Rules: ContractRule[];
  domainExpertise: string[];
  artifactsProduced: string[];
  reviewer: string;
  model: string;
  maxTokens: number;
  temperature: number;
}

const agentContracts: Record<string, AgentContract> = {
  'business_strategist': {
    id: 'business_strategist',
    name: 'Business Strategist Agent',
    role: 'business_strategist',
    category: 'business',
    description: "Porter's strategic frameworks analysis",
    icon: <Briefcase className="w-6 h-6" />,
    tier0Rules: [
      { id: 't0-1', text: 'Never recommend strategy without citing industry evidence' },
      { id: 't0-2', text: 'Never ignore competitive context' },
      { id: 't0-3', text: 'Always validate strategic fit with business model' },
    ],
    tier1Rules: [
      { id: 't1-1', text: 'Apply appropriate strategy frameworks (Porter, SWOT, etc.)' },
      { id: 't1-2', text: 'Ground recommendations in market data' },
      { id: 't1-3', text: 'Validate with Business Analyst before finalizing' },
    ],
    tier2Rules: [
      { id: 't2-1', text: 'Consider long-term strategic implications' },
      { id: 't2-2', text: 'Document assumptions explicitly' },
    ],
    domainExpertise: ['Strategy frameworks', 'Industry analysis', 'Competitive positioning'],
    artifactsProduced: ['Strategic frameworks', 'Positioning documents'],
    reviewer: 'business_analyst',
    model: 'claude-sonnet-4-20250514',
    maxTokens: 4096,
    temperature: 0.5,
  },
  'architect': {
    id: 'architect',
    name: 'Architect Agent',
    role: 'architect',
    category: 'sub',
    description: 'Value chain structure and entity design',
    icon: <Network className="w-6 h-6" />,
    tier0Rules: [
      { id: 't0-1', text: 'Never create circular dependencies in entity relationships' },
      { id: 't0-2', text: 'Always validate entity schemas against existing ontology' },
      { id: 't0-3', text: 'Never bypass data governance requirements' },
    ],
    tier1Rules: [
      { id: 't1-1', text: 'Design for extensibility and future requirements' },
      { id: 't1-2', text: 'Document architectural decisions with ADRs' },
      { id: 't1-3', text: 'Validate designs with Developer before implementation' },
    ],
    tier2Rules: [
      { id: 't2-1', text: 'Optimize for query performance' },
      { id: 't2-2', text: 'Consider multi-tenant implications' },
    ],
    domainExpertise: ['System design', 'Data modeling', 'Value chain architecture'],
    artifactsProduced: ['Entity schemas', 'Architecture diagrams', 'ADRs'],
    reviewer: 'business_strategist',
    model: 'claude-sonnet-4-20250514',
    maxTokens: 4096,
    temperature: 0.3,
  },
  'developer': {
    id: 'developer',
    name: 'Developer Agent',
    role: 'developer',
    category: 'sub',
    description: 'Code and schema generation',
    icon: <Code className="w-6 h-6" />,
    tier0Rules: [
      { id: 't0-1', text: 'Never commit code without passing tests' },
      { id: 't0-2', text: 'Always follow established coding standards' },
      { id: 't0-3', text: 'Never hardcode sensitive credentials' },
    ],
    tier1Rules: [
      { id: 't1-1', text: 'Write comprehensive unit tests for new code' },
      { id: 't1-2', text: 'Document public APIs and complex logic' },
      { id: 't1-3', text: 'Review with Architect before merging' },
      { id: 't1-4', text: 'Follow DRY and SOLID principles' },
    ],
    tier2Rules: [
      { id: 't2-1', text: 'Optimize for readability over cleverness' },
      { id: 't2-2', text: 'Consider backward compatibility' },
    ],
    domainExpertise: ['Python', 'TypeScript', 'SQL', 'API design'],
    artifactsProduced: ['Source code', 'Database migrations', 'API endpoints'],
    reviewer: 'architect',
    model: 'claude-sonnet-4-20250514',
    maxTokens: 8192,
    temperature: 0.2,
  },
  'tester': {
    id: 'tester',
    name: 'Tester Agent',
    role: 'tester',
    category: 'sub',
    description: 'Validation and quality assurance',
    icon: <TestTube className="w-6 h-6" />,
    tier0Rules: [
      { id: 't0-1', text: 'Never approve code with failing critical tests' },
      { id: 't0-2', text: 'Always test edge cases and error conditions' },
      { id: 't0-3', text: 'Never skip security vulnerability checks' },
    ],
    tier1Rules: [
      { id: 't1-1', text: 'Achieve minimum 80% code coverage' },
      { id: 't1-2', text: 'Document test scenarios and expected outcomes' },
      { id: 't1-3', text: 'Validate with Developer on test failures' },
    ],
    tier2Rules: [
      { id: 't2-1', text: 'Include performance benchmarks' },
      { id: 't2-2', text: 'Test for accessibility compliance' },
    ],
    domainExpertise: ['Test automation', 'QA processes', 'Security testing'],
    artifactsProduced: ['Test suites', 'Coverage reports', 'Bug reports'],
    reviewer: 'developer',
    model: 'claude-sonnet-4-20250514',
    maxTokens: 4096,
    temperature: 0.2,
  },
};

const iconMap: Record<string, React.ReactNode> = {
  'architect': <Network className="w-6 h-6" />,
  'business_analyst': <ClipboardList className="w-6 h-6" />,
  'developer': <Code className="w-6 h-6" />,
  'tester': <TestTube className="w-6 h-6" />,
  'documenter': <FileText className="w-6 h-6" />,
  'data_analyst': <Database className="w-6 h-6" />,
  'deployment_specialist': <Rocket className="w-6 h-6" />,
  'project_manager': <ClipboardList className="w-6 h-6" />,
  'itil_manager': <Settings className="w-6 h-6" />,
  'mapping_specialist': <GitBranch className="w-6 h-6" />,
  'connection_specialist': <Link className="w-6 h-6" />,
  'document_analyzer': <FileSearch className="w-6 h-6" />,
  'librarian_curator': <BookOpen className="w-6 h-6" />,
  'sales_manager': <TrendingUp className="w-6 h-6" />,
  'accountant': <BarChart3 className="w-6 h-6" />,
  'data_governance_specialist': <Shield className="w-6 h-6" />,
  'data_scientist': <Brain className="w-6 h-6" />,
  'marketing_manager': <Target className="w-6 h-6" />,
  'ui_designer': <Palette className="w-6 h-6" />,
  'business_strategist': <Briefcase className="w-6 h-6" />,
  'operations_manager': <Activity className="w-6 h-6" />,
  'customer_success_manager': <UserCheck className="w-6 h-6" />,
  'hr_talent_analyst': <Users2 className="w-6 h-6" />,
  'risk_compliance_officer': <ShieldCheck className="w-6 h-6" />,
  'supply_chain_analyst': <Truck className="w-6 h-6" />,
  'competitive_analyst': <LineChart className="w-6 h-6" />,
  'process_scenario_modeler': <Workflow className="w-6 h-6" />,
};

export default function AgentProfileDetailPage() {
  const { agentId } = useParams<{ agentId: string }>();
  const navigate = useNavigate();
  const [isEditing, setIsEditing] = useState(false);
  const [isSaving, setIsSaving] = useState(false);
  const [newRule, setNewRule] = useState({ tier: '', text: '' });
  
  const contract = agentId ? agentContracts[agentId] : null;
  
  const [editedContract, setEditedContract] = useState<AgentContract | null>(contract);

  if (!contract) {
    return (
      <div className="space-y-6">
        <button
          onClick={() => navigate('/admin/agents')}
          className="flex items-center gap-2 theme-text-secondary hover:theme-text-title transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          Back to Agent Profiles
        </button>
        <div className="theme-card rounded-xl p-8 text-center">
          <Users className="w-12 h-12 mx-auto mb-4 theme-text-muted" />
          <h2 className="text-xl font-semibold theme-text-title mb-2">Agent Not Found</h2>
          <p className="theme-text-muted">
            Contract profile for agent "{agentId}" is not yet loaded.
          </p>
          <p className="theme-text-muted mt-2 text-sm">
            The full contract will be fetched from the backend when the API is connected.
          </p>
        </div>
      </div>
    );
  }

  const handleSave = async () => {
    setIsSaving(true);
    
    // This would send the changes to the orchestrator to be processed by
    // Architect → Developer → Tester pipeline
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    setIsSaving(false);
    setIsEditing(false);
  };

  const handleAddRule = (tier: 'tier0' | 'tier1' | 'tier2') => {
    if (!newRule.text.trim() || !editedContract) return;
    
    const ruleKey = `${tier}Rules` as 'tier0Rules' | 'tier1Rules' | 'tier2Rules';
    const newRuleObj: ContractRule = {
      id: `${tier}-new-${Date.now()}`,
      text: newRule.text,
      isNew: true,
    };
    
    setEditedContract({
      ...editedContract,
      [ruleKey]: [...editedContract[ruleKey], newRuleObj],
    });
    setNewRule({ tier: '', text: '' });
  };

  const handleRemoveRule = (tier: 'tier0' | 'tier1' | 'tier2', ruleId: string) => {
    if (!editedContract) return;
    
    const ruleKey = `${tier}Rules` as 'tier0Rules' | 'tier1Rules' | 'tier2Rules';
    setEditedContract({
      ...editedContract,
      [ruleKey]: editedContract[ruleKey].filter(r => r.id !== ruleId),
    });
  };

  const displayContract = isEditing ? editedContract : contract;
  if (!displayContract) return null;

  const isProtected = PROTECTED_AGENTS.includes(contract.role);

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-4">
          <button
            onClick={() => navigate('/admin/agents')}
            className="flex items-center gap-2 theme-text-secondary hover:theme-text-title transition-colors"
          >
            <ArrowLeft className="w-4 h-4" />
            Back
          </button>
          <div className={`w-14 h-14 rounded-xl flex items-center justify-center ${
            contract.category === 'business' ? 'bg-emerald-500/10' : 'bg-blue-500/10'
          }`}>
            <span className={contract.category === 'business' ? 'text-emerald-400' : 'text-blue-400'}>
              {iconMap[contract.role] || contract.icon}
            </span>
          </div>
          <div>
            <h1 className="text-2xl font-bold theme-text-title">{contract.name}</h1>
            <p className="theme-text-secondary">{contract.description}</p>
            {isProtected && (
              <span className="inline-flex items-center gap-1 mt-1 text-xs px-2 py-0.5 rounded bg-amber-500/10 text-amber-400">
                <Shield className="w-3 h-3" />
                Core Agent - Human Edit Only
              </span>
            )}
          </div>
        </div>
        <div className="flex items-center gap-3">
          {isEditing ? (
            <>
              <button
                onClick={() => {
                  setIsEditing(false);
                  setEditedContract(contract);
                }}
                className="px-4 py-2 rounded-lg theme-card hover:bg-[var(--card-hover)] theme-text-secondary flex items-center gap-2"
              >
                <X className="w-4 h-4" />
                Cancel
              </button>
              <button
                onClick={handleSave}
                disabled={isSaving}
                className="px-4 py-2 rounded-lg bg-alpha-500 hover:bg-alpha-600 text-white flex items-center gap-2"
              >
                {isSaving ? (
                  <>
                    <Loader2 className="w-4 h-4 animate-spin" />
                    Submitting to Agents...
                  </>
                ) : (
                  <>
                    <Save className="w-4 h-4" />
                    Save Changes
                  </>
                )}
              </button>
            </>
          ) : isProtected ? (
            <div className="px-4 py-2 rounded-lg bg-amber-500/10 text-amber-400 text-sm flex items-center gap-2">
              <Shield className="w-4 h-4" />
              Protected - Edit via source code only
            </div>
          ) : (
            <button
              onClick={() => setIsEditing(true)}
              className="px-4 py-2 rounded-lg bg-alpha-500 hover:bg-alpha-600 text-white flex items-center gap-2"
            >
              <Edit3 className="w-4 h-4" />
              Edit Contract
            </button>
          )}
        </div>
      </div>

      {/* Agent Pipeline Notice */}
      {isEditing && (
        <div className="theme-card rounded-xl p-4 border border-amber-500/30 bg-amber-500/5">
          <div className="flex items-start gap-3">
            <AlertTriangle className="w-5 h-5 text-amber-400 flex-shrink-0 mt-0.5" />
            <div>
              <h3 className="font-medium text-amber-400">Agent-Driven Modification</h3>
              <p className="text-sm theme-text-secondary mt-1">
                Changes will be processed by the <strong>Architect → Developer → Tester</strong> pipeline. 
                The agents will update the source code in <code className="text-xs bg-black/20 px-1 rounded">contracts.py</code> and validate the changes before deployment.
              </p>
            </div>
          </div>
        </div>
      )}

      <div className="grid grid-cols-3 gap-6">
        {/* Main Content */}
        <div className="col-span-2 space-y-6">
          {/* Tier 0 Rules - Critical */}
          <div className="theme-card rounded-xl p-6">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-3">
                <div className="w-8 h-8 rounded-lg bg-red-500/10 flex items-center justify-center">
                  <AlertTriangle className="w-4 h-4 text-red-400" />
                </div>
                <div>
                  <h3 className="font-semibold theme-text-title">Tier 0 Rules</h3>
                  <p className="text-xs theme-text-muted">Hard stops - Never violated</p>
                </div>
              </div>
              {isEditing && (
                <span className="text-xs px-2 py-1 rounded bg-red-500/10 text-red-400">
                  Critical
                </span>
              )}
            </div>
            <ul className="space-y-2">
              {displayContract.tier0Rules.map((rule) => (
                <li key={rule.id} className="flex items-start gap-3 p-3 rounded-lg bg-red-500/5 border border-red-500/20">
                  <Shield className="w-4 h-4 text-red-400 flex-shrink-0 mt-0.5" />
                  <span className="text-sm theme-text-secondary flex-1">{rule.text}</span>
                  {isEditing && rule.isNew && (
                    <button
                      onClick={() => handleRemoveRule('tier0', rule.id)}
                      className="text-red-400 hover:text-red-300"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  )}
                </li>
              ))}
            </ul>
            {isEditing && (
              <div className="mt-4 flex gap-2">
                <input
                  type="text"
                  placeholder="Add new Tier 0 rule..."
                  value={newRule.tier === 'tier0' ? newRule.text : ''}
                  onChange={(e) => setNewRule({ tier: 'tier0', text: e.target.value })}
                  onKeyDown={(e) => e.key === 'Enter' && handleAddRule('tier0')}
                  className="flex-1 px-3 py-2 rounded-lg theme-input text-sm"
                />
                <button
                  onClick={() => handleAddRule('tier0')}
                  className="px-3 py-2 rounded-lg bg-red-500/10 hover:bg-red-500/20 text-red-400"
                >
                  <Plus className="w-4 h-4" />
                </button>
              </div>
            )}
          </div>

          {/* Tier 1 Rules - Standard */}
          <div className="theme-card rounded-xl p-6">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-3">
                <div className="w-8 h-8 rounded-lg bg-amber-500/10 flex items-center justify-center">
                  <CheckCircle className="w-4 h-4 text-amber-400" />
                </div>
                <div>
                  <h3 className="font-semibold theme-text-title">Tier 1 Rules</h3>
                  <p className="text-xs theme-text-muted">Standard practices - Should follow</p>
                </div>
              </div>
            </div>
            <ul className="space-y-2">
              {displayContract.tier1Rules.map((rule) => (
                <li key={rule.id} className="flex items-start gap-3 p-3 rounded-lg bg-amber-500/5 border border-amber-500/20">
                  <CheckCircle className="w-4 h-4 text-amber-400 flex-shrink-0 mt-0.5" />
                  <span className="text-sm theme-text-secondary flex-1">{rule.text}</span>
                  {isEditing && rule.isNew && (
                    <button
                      onClick={() => handleRemoveRule('tier1', rule.id)}
                      className="text-amber-400 hover:text-amber-300"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  )}
                </li>
              ))}
            </ul>
            {isEditing && (
              <div className="mt-4 flex gap-2">
                <input
                  type="text"
                  placeholder="Add new Tier 1 rule..."
                  value={newRule.tier === 'tier1' ? newRule.text : ''}
                  onChange={(e) => setNewRule({ tier: 'tier1', text: e.target.value })}
                  onKeyDown={(e) => e.key === 'Enter' && handleAddRule('tier1')}
                  className="flex-1 px-3 py-2 rounded-lg theme-input text-sm"
                />
                <button
                  onClick={() => handleAddRule('tier1')}
                  className="px-3 py-2 rounded-lg bg-amber-500/10 hover:bg-amber-500/20 text-amber-400"
                >
                  <Plus className="w-4 h-4" />
                </button>
              </div>
            )}
          </div>

          {/* Tier 2 Rules - Best Practice */}
          <div className="theme-card rounded-xl p-6">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-3">
                <div className="w-8 h-8 rounded-lg bg-blue-500/10 flex items-center justify-center">
                  <CheckCircle className="w-4 h-4 text-blue-400" />
                </div>
                <div>
                  <h3 className="font-semibold theme-text-title">Tier 2 Rules</h3>
                  <p className="text-xs theme-text-muted">Best practices - Nice to have</p>
                </div>
              </div>
            </div>
            <ul className="space-y-2">
              {displayContract.tier2Rules.map((rule) => (
                <li key={rule.id} className="flex items-start gap-3 p-3 rounded-lg bg-blue-500/5 border border-blue-500/20">
                  <CheckCircle className="w-4 h-4 text-blue-400 flex-shrink-0 mt-0.5" />
                  <span className="text-sm theme-text-secondary flex-1">{rule.text}</span>
                  {isEditing && rule.isNew && (
                    <button
                      onClick={() => handleRemoveRule('tier2', rule.id)}
                      className="text-blue-400 hover:text-blue-300"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  )}
                </li>
              ))}
            </ul>
            {isEditing && (
              <div className="mt-4 flex gap-2">
                <input
                  type="text"
                  placeholder="Add new Tier 2 rule..."
                  value={newRule.tier === 'tier2' ? newRule.text : ''}
                  onChange={(e) => setNewRule({ tier: 'tier2', text: e.target.value })}
                  onKeyDown={(e) => e.key === 'Enter' && handleAddRule('tier2')}
                  className="flex-1 px-3 py-2 rounded-lg theme-input text-sm"
                />
                <button
                  onClick={() => handleAddRule('tier2')}
                  className="px-3 py-2 rounded-lg bg-blue-500/10 hover:bg-blue-500/20 text-blue-400"
                >
                  <Plus className="w-4 h-4" />
                </button>
              </div>
            )}
          </div>
        </div>

        {/* Sidebar */}
        <div className="space-y-6">
          {/* Configuration */}
          <div className="theme-card rounded-xl p-6">
            <h3 className="font-semibold theme-text-title mb-4">Configuration</h3>
            <div className="space-y-4">
              <div>
                <p className="text-xs theme-text-muted mb-1">Model</p>
                <p className="text-sm font-mono theme-text-secondary">{contract.model}</p>
              </div>
              <div>
                <p className="text-xs theme-text-muted mb-1">Max Tokens</p>
                <p className="text-sm theme-text-secondary">{contract.maxTokens.toLocaleString()}</p>
              </div>
              <div>
                <p className="text-xs theme-text-muted mb-1">Temperature</p>
                <p className="text-sm theme-text-secondary">{contract.temperature}</p>
              </div>
              <div>
                <p className="text-xs theme-text-muted mb-1">Reviewer</p>
                <p className="text-sm theme-text-secondary capitalize">{contract.reviewer.replace('_', ' ')}</p>
              </div>
            </div>
          </div>

          {/* Domain Expertise */}
          <div className="theme-card rounded-xl p-6">
            <h3 className="font-semibold theme-text-title mb-4">Domain Expertise</h3>
            <div className="flex flex-wrap gap-2">
              {contract.domainExpertise.map((expertise, idx) => (
                <span key={idx} className="px-3 py-1 rounded-full bg-alpha-500/10 text-alpha-400 text-xs">
                  {expertise}
                </span>
              ))}
            </div>
          </div>

          {/* Artifacts Produced */}
          <div className="theme-card rounded-xl p-6">
            <h3 className="font-semibold theme-text-title mb-4">Artifacts Produced</h3>
            <ul className="space-y-2">
              {contract.artifactsProduced.map((artifact, idx) => (
                <li key={idx} className="flex items-center gap-2 text-sm theme-text-secondary">
                  <FileText className="w-4 h-4 theme-text-muted" />
                  {artifact}
                </li>
              ))}
            </ul>
          </div>

          {/* Actions */}
          <div className="theme-card rounded-xl p-6">
            <h3 className="font-semibold theme-text-title mb-4">Actions</h3>
            <div className="space-y-2">
              <button className="w-full px-4 py-2 rounded-lg bg-emerald-500/10 hover:bg-emerald-500/20 text-emerald-400 text-sm flex items-center gap-2 justify-center">
                <Play className="w-4 h-4" />
                Test Agent
              </button>
              {isProtected ? (
                <div className="w-full px-4 py-2 rounded-lg bg-gray-500/10 text-gray-500 text-sm flex items-center gap-2 justify-center">
                  <Shield className="w-4 h-4" />
                  Cannot Delete Core Agent
                </div>
              ) : (
                <button className="w-full px-4 py-2 rounded-lg bg-red-500/10 hover:bg-red-500/20 text-red-400 text-sm flex items-center gap-2 justify-center">
                  <Trash2 className="w-4 h-4" />
                  Delete Agent
                </button>
              )}
            </div>
            {isProtected && (
              <p className="text-xs theme-text-muted mt-3">
                The 4 core agents (Business Analyst, Architect, Developer, Tester) perform the 
                agent-driven code modifications. Only a human user can modify their source code directly.
              </p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
