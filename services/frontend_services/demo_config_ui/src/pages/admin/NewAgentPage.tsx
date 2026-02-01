import { useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { 
  ArrowLeft, 
  Plus, 
  Brain,
  AlertTriangle,
  CheckCircle,
  Loader2,
  Sparkles,
  Code,
  Users,
  Upload,
  FileText,
  X,
  FileSearch,
  Network,
  ThumbsUp,
  ThumbsDown,
  AlertCircle,
  Layers,
  GitMerge,
} from 'lucide-react';

interface ArchitectAssessment {
  recommendation: 'approve' | 'caution' | 'reject';
  summary: string;
  gapAnalysis: {
    addressesGap: boolean;
    gapDescription: string;
    createsGap: boolean;
    newGapDescription: string;
  };
  overlapAnalysis: {
    hasOverlap: boolean;
    overlappingAgents: string[];
    overlapDetails: string;
  };
  suggestions: string[];
}

interface UploadedDocument {
  name: string;
  size: number;
  content: string;
  analyzedSpec?: string;
}

interface NewAgentForm {
  name: string;
  role: string;
  category: 'business' | 'sub';
  description: string;
  model: string;
  maxTokens: number;
  temperature: number;
  reviewer: string;
  tier0Rules: string[];
  tier1Rules: string[];
  tier2Rules: string[];
  domainExpertise: string[];
  artifactsProduced: string[];
  documents: UploadedDocument[];
}

const initialForm: NewAgentForm = {
  name: '',
  role: '',
  category: 'sub',
  description: '',
  model: 'claude-sonnet-4-20250514',
  maxTokens: 4096,
  temperature: 0.3,
  documents: [],
  reviewer: '',
  tier0Rules: [''],
  tier1Rules: [''],
  tier2Rules: [''],
  domainExpertise: [''],
  artifactsProduced: [''],
};

const existingAgents = [
  'architect', 'business_analyst', 'developer', 'tester', 'documenter',
  'data_analyst', 'deployment_specialist', 'project_manager', 'itil_manager',
  'mapping_specialist', 'connection_specialist', 'document_analyzer', 'librarian_curator',
  'sales_manager', 'accountant', 'data_governance_specialist', 'data_scientist',
  'marketing_manager', 'ui_designer', 'business_strategist', 'operations_manager',
  'customer_success_manager', 'hr_talent_analyst', 'risk_compliance_officer',
  'supply_chain_analyst', 'competitive_analyst', 'process_scenario_modeler',
];

// Core agents that cannot be modified via UI - only human users can change their code
// These agents form the agent modification pipeline itself
const PROTECTED_AGENTS = ['business_analyst', 'architect', 'developer', 'tester', 'documenter'];

export default function NewAgentPage() {
  const navigate = useNavigate();
  const [form, setForm] = useState<NewAgentForm>(initialForm);
  const [step, setStep] = useState(1);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [agentProgress, setAgentProgress] = useState<string[]>([]);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [isAssessing, setIsAssessing] = useState(false);
  const [architectAssessment, setArchitectAssessment] = useState<ArchitectAssessment | null>(null);

  const handleArrayFieldChange = (
    field: 'tier0Rules' | 'tier1Rules' | 'tier2Rules' | 'domainExpertise' | 'artifactsProduced',
    index: number,
    value: string
  ) => {
    const newArray = [...form[field]];
    newArray[index] = value;
    setForm({ ...form, [field]: newArray });
  };

  const handleAddArrayItem = (
    field: 'tier0Rules' | 'tier1Rules' | 'tier2Rules' | 'domainExpertise' | 'artifactsProduced'
  ) => {
    setForm({ ...form, [field]: [...form[field], ''] });
  };

  const handleRemoveArrayItem = (
    field: 'tier0Rules' | 'tier1Rules' | 'tier2Rules' | 'domainExpertise' | 'artifactsProduced',
    index: number
  ) => {
    const newArray = form[field].filter((_, i) => i !== index);
    setForm({ ...form, [field]: newArray.length ? newArray : [''] });
  };

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (!files) return;

    const newDocs: UploadedDocument[] = [];
    
    for (const file of Array.from(files)) {
      const content = await file.text();
      newDocs.push({
        name: file.name,
        size: file.size,
        content: content,
      });
    }

    setForm({ ...form, documents: [...form.documents, ...newDocs] });
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  const handleAnalyzeDocuments = async () => {
    if (form.documents.length === 0) return;
    
    setIsAnalyzing(true);
    
    // Simulate Business Analyst Agent analyzing documents
    await new Promise(resolve => setTimeout(resolve, 3000));
    
    // Update documents with analyzed specs
    const analyzedDocs = form.documents.map(doc => ({
      ...doc,
      analyzedSpec: `## Agent Specification from ${doc.name}\n\nAnalyzed by Business Analyst Agent.\n\n### Extracted Requirements:\n- Domain expertise identified from document\n- Suggested contract rules based on content\n- Recommended artifacts based on responsibilities\n\n*This spec will be saved as a .md file for auditability.*`
    }));
    
    setForm({ ...form, documents: analyzedDocs });
    setIsAnalyzing(false);
  };

  const handleRemoveDocument = (index: number) => {
    setForm({ ...form, documents: form.documents.filter((_, i) => i !== index) });
  };

  const handleArchitectAssessment = async () => {
    setIsAssessing(true);
    setArchitectAssessment(null);

    // Simulate Architect Agent analyzing the new agent proposal
    await new Promise(resolve => setTimeout(resolve, 3000));

    // Generate a simulated assessment based on the form data
    const hasOverlapWithBA = form.domainExpertise.some(e => 
      e.toLowerCase().includes('kpi') || e.toLowerCase().includes('requirement')
    );
    const hasOverlapWithArch = form.domainExpertise.some(e => 
      e.toLowerCase().includes('design') || e.toLowerCase().includes('schema')
    );
    
    const overlappingAgents: string[] = [];
    if (hasOverlapWithBA) overlappingAgents.push('business_analyst');
    if (hasOverlapWithArch) overlappingAgents.push('architect');
    
    const assessment: ArchitectAssessment = {
      recommendation: overlappingAgents.length > 1 ? 'caution' : 'approve',
      summary: overlappingAgents.length > 1 
        ? `The proposed ${form.name} has some responsibility overlap with existing agents. Consider refining the scope.`
        : `The proposed ${form.name} addresses a clear functional need and fits well within the agent ecosystem.`,
      gapAnalysis: {
        addressesGap: true,
        gapDescription: `Addresses the need for specialized ${form.category === 'business' ? 'business domain' : 'technical'} capabilities in ${form.domainExpertise.filter(e => e.trim())[0] || 'the specified domain'}.`,
        createsGap: false,
        newGapDescription: '',
      },
      overlapAnalysis: {
        hasOverlap: overlappingAgents.length > 0,
        overlappingAgents,
        overlapDetails: overlappingAgents.length > 0 
          ? `Some domain expertise overlaps with: ${overlappingAgents.join(', ')}. Ensure clear boundaries in contract rules.`
          : 'No significant overlap detected with existing agents.',
      },
      suggestions: [
        'Ensure Tier 0 rules clearly differentiate this agent from similar roles',
        overlappingAgents.length > 0 ? `Coordinate with ${overlappingAgents[0]} reviewer to avoid duplicate work` : 'Consider adding peer consultation with related domain agents',
        'Document the specific scenarios where this agent should be invoked',
      ],
    };

    setArchitectAssessment(assessment);
    setIsAssessing(false);
  };

  const handleSubmit = async () => {
    setIsSubmitting(true);
    setAgentProgress([]);

    // Build agent pipeline steps based on whether documents were uploaded
    const steps = form.documents.length > 0 ? [
      'Submitting to Coordinator...',
      'Business Analyst Agent analyzing uploaded documents...',
      'BA Agent generated specification document...',
      'Saving spec to docs/agent_specs/' + form.role + '_spec.md...',
      'Architect Agent reviewing design with BA specs...',
      'Architect approved. Routing to Developer...',
      'Developer Agent generating code...',
      'Code generated. Routing to Tester...',
      'Tester Agent validating changes...',
      'All tests passed. Routing to Documenter...',
      'Documenter Agent updating MULTI_AGENT_ARCHITECTURE.md...',
      'Documenter Agent updating MULTI_AGENT_SERVICE_SUMMARY.md...',
      'Documentation updated. Committing all changes...',
      'Agent successfully created!',
    ] : [
      'Submitting to Coordinator...',
      'Architect Agent reviewing design...',
      'Architect approved. Routing to Developer...',
      'Developer Agent generating code...',
      'Code generated. Routing to Tester...',
      'Tester Agent validating changes...',
      'All tests passed. Routing to Documenter...',
      'Documenter Agent updating MULTI_AGENT_ARCHITECTURE.md...',
      'Documenter Agent updating MULTI_AGENT_SERVICE_SUMMARY.md...',
      'Documentation updated. Committing all changes...',
      'Agent successfully created!',
    ];

    for (const step of steps) {
      await new Promise(resolve => setTimeout(resolve, 1500));
      setAgentProgress(prev => [...prev, step]);
    }

    setTimeout(() => {
      navigate('/admin/agents');
    }, 1000);
  };

  const isRoleProtected = PROTECTED_AGENTS.includes(form.role);
  const isStep1Valid = form.name && form.role && form.description && form.reviewer && !isRoleProtected;
  const isStep2Valid = form.tier0Rules.some(r => r.trim()) && form.tier1Rules.some(r => r.trim());

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center gap-4">
        <button
          onClick={() => navigate('/admin/agents')}
          className="flex items-center gap-2 theme-text-secondary hover:theme-text-title transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          Back
        </button>
        <div>
          <h1 className="text-2xl font-bold theme-text-title">Create New Agent</h1>
          <p className="theme-text-secondary">Define a new AI agent to extend platform capabilities</p>
        </div>
      </div>

      {/* Progress */}
      <div className="flex items-center gap-4">
        {[1, 2, 3].map((s) => (
          <div key={s} className="flex items-center gap-2">
            <div className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-medium ${
              step === s ? 'bg-alpha-500 text-white' :
              step > s ? 'bg-emerald-500 text-white' :
              'theme-card theme-text-muted'
            }`}>
              {step > s ? <CheckCircle className="w-4 h-4" /> : s}
            </div>
            <span className={`text-sm ${step >= s ? 'theme-text-title' : 'theme-text-muted'}`}>
              {s === 1 ? 'Basic Info' : s === 2 ? 'Contract Rules' : 'Review & Create'}
            </span>
            {s < 3 && <div className="w-16 h-px bg-[var(--border-color)]" />}
          </div>
        ))}
      </div>

      {/* Agent Pipeline Notice */}
      <div className="theme-card rounded-xl p-4 border border-alpha-500/30 bg-alpha-500/5">
        <div className="flex items-start gap-3">
          <Sparkles className="w-5 h-5 text-alpha-400 flex-shrink-0 mt-0.5" />
          <div>
            <h3 className="font-medium text-alpha-400">Agent-Driven Creation</h3>
            <p className="text-sm theme-text-secondary mt-1">
              New agents are created through the <strong>Architect → Developer → Tester</strong> pipeline. 
              Your input will be processed by the agents to generate proper code and validate the new agent.
            </p>
          </div>
        </div>
      </div>

      {/* Step 1: Basic Info */}
      {step === 1 && (
        <div className="theme-card rounded-xl p-6 space-y-6">
          <h2 className="text-lg font-semibold theme-text-title">Basic Information</h2>
          
          <div className="grid grid-cols-2 gap-6">
            <div>
              <label className="block text-sm font-medium theme-text-secondary mb-2">Agent Name</label>
              <input
                type="text"
                value={form.name}
                onChange={(e) => setForm({ ...form, name: e.target.value })}
                placeholder="e.g., Quality Assurance Manager Agent"
                className="w-full px-4 py-2 rounded-lg theme-input"
              />
            </div>
            <div>
              <label className="block text-sm font-medium theme-text-secondary mb-2">Role ID</label>
              <input
                type="text"
                value={form.role}
                onChange={(e) => setForm({ ...form, role: e.target.value.toLowerCase().replace(/\s+/g, '_') })}
                placeholder="e.g., qa_manager"
                className="w-full px-4 py-2 rounded-lg theme-input font-mono"
              />
              {form.role && existingAgents.includes(form.role) && (
                <p className="text-xs text-red-400 mt-1">This role ID already exists</p>
              )}
              {form.role && isRoleProtected && (
                <p className="text-xs text-amber-400 mt-1">This is a protected core agent role and cannot be created via UI</p>
              )}
            </div>
          </div>

          <div>
            <label className="block text-sm font-medium theme-text-secondary mb-2">Description</label>
            <textarea
              value={form.description}
              onChange={(e) => setForm({ ...form, description: e.target.value })}
              placeholder="Describe what this agent does and its primary responsibilities..."
              rows={3}
              className="w-full px-4 py-2 rounded-lg theme-input resize-none"
            />
          </div>

          {/* Document Upload Section */}
          <div className="border border-dashed border-[var(--border-color)] rounded-xl p-6">
            <div className="flex items-center gap-3 mb-4">
              <FileSearch className="w-5 h-5 text-alpha-400" />
              <div>
                <h3 className="font-medium theme-text-title">Reference Documents (Optional)</h3>
                <p className="text-xs theme-text-muted">
                  Upload documents for Business Analyst Agent to analyze and generate specs
                </p>
              </div>
            </div>
            
            <input
              ref={fileInputRef}
              type="file"
              multiple
              accept=".txt,.md,.pdf,.doc,.docx"
              onChange={handleFileUpload}
              className="hidden"
              id="doc-upload"
            />
            
            <div className="flex items-center gap-4 mb-4">
              <label
                htmlFor="doc-upload"
                className="px-4 py-2 rounded-lg border border-[var(--border-color)] hover:bg-[var(--card-hover)] theme-text-secondary cursor-pointer flex items-center gap-2 transition-colors"
              >
                <Upload className="w-4 h-4" />
                Upload Documents
              </label>
              
              {form.documents.length > 0 && !form.documents.some(d => d.analyzedSpec) && (
                <button
                  onClick={handleAnalyzeDocuments}
                  disabled={isAnalyzing}
                  className="px-4 py-2 rounded-lg bg-alpha-500/10 hover:bg-alpha-500/20 text-alpha-400 flex items-center gap-2 transition-colors"
                >
                  {isAnalyzing ? (
                    <>
                      <Loader2 className="w-4 h-4 animate-spin" />
                      Analyzing...
                    </>
                  ) : (
                    <>
                      <Brain className="w-4 h-4" />
                      Analyze with BA Agent
                    </>
                  )}
                </button>
              )}
            </div>

            {/* Uploaded Documents List */}
            {form.documents.length > 0 && (
              <div className="space-y-2">
                {form.documents.map((doc, idx) => (
                  <div key={idx} className="flex items-center gap-3 p-3 rounded-lg bg-[var(--card-hover)]">
                    <FileText className="w-5 h-5 text-alpha-400 flex-shrink-0" />
                    <div className="flex-1 min-w-0">
                      <p className="text-sm font-medium theme-text-title truncate">{doc.name}</p>
                      <p className="text-xs theme-text-muted">
                        {(doc.size / 1024).toFixed(1)} KB
                        {doc.analyzedSpec && (
                          <span className="ml-2 text-emerald-400">✓ Analyzed</span>
                        )}
                      </p>
                    </div>
                    <button
                      onClick={() => handleRemoveDocument(idx)}
                      className="p-1 rounded hover:bg-red-500/10 text-red-400"
                    >
                      <X className="w-4 h-4" />
                    </button>
                  </div>
                ))}
              </div>
            )}

            {form.documents.some(d => d.analyzedSpec) && (
              <div className="mt-4 p-4 rounded-lg bg-emerald-500/5 border border-emerald-500/20">
                <div className="flex items-center gap-2 mb-2">
                  <CheckCircle className="w-4 h-4 text-emerald-400" />
                  <span className="text-sm font-medium text-emerald-400">Documents Analyzed</span>
                </div>
                <p className="text-xs theme-text-muted">
                  Specs will be saved as .md files in <code className="bg-black/20 px-1 rounded">docs/agent_specs/</code> for auditability.
                  The Architect Agent will use these specs when designing the agent.
                </p>
              </div>
            )}
          </div>

          <div className="grid grid-cols-2 gap-6">
            <div>
              <label className="block text-sm font-medium theme-text-secondary mb-2">Category</label>
              <div className="flex gap-4">
                <button
                  onClick={() => setForm({ ...form, category: 'sub' })}
                  className={`flex-1 px-4 py-3 rounded-lg border transition-colors flex items-center justify-center gap-2 ${
                    form.category === 'sub' 
                      ? 'border-blue-500 bg-blue-500/10 text-blue-400' 
                      : 'border-[var(--border-color)] theme-text-secondary hover:bg-[var(--card-hover)]'
                  }`}
                >
                  <Code className="w-4 h-4" />
                  Sub-Agent
                </button>
                <button
                  onClick={() => setForm({ ...form, category: 'business' })}
                  className={`flex-1 px-4 py-3 rounded-lg border transition-colors flex items-center justify-center gap-2 ${
                    form.category === 'business' 
                      ? 'border-emerald-500 bg-emerald-500/10 text-emerald-400' 
                      : 'border-[var(--border-color)] theme-text-secondary hover:bg-[var(--card-hover)]'
                  }`}
                >
                  <Users className="w-4 h-4" />
                  Business Agent
                </button>
              </div>
            </div>
            <div>
              <label className="block text-sm font-medium theme-text-secondary mb-2">Reviewer</label>
              <select
                value={form.reviewer}
                onChange={(e) => setForm({ ...form, reviewer: e.target.value })}
                className="w-full px-4 py-2 rounded-lg theme-input"
              >
                <option value="">Select reviewer...</option>
                {existingAgents.map(agent => (
                  <option key={agent} value={agent}>{agent.replace(/_/g, ' ')}</option>
                ))}
              </select>
            </div>
          </div>

          <div className="grid grid-cols-3 gap-6">
            <div>
              <label className="block text-sm font-medium theme-text-secondary mb-2">Model</label>
              <select
                value={form.model}
                onChange={(e) => setForm({ ...form, model: e.target.value })}
                className="w-full px-4 py-2 rounded-lg theme-input"
              >
                <option value="claude-sonnet-4-20250514">Claude Sonnet 4</option>
                <option value="claude-opus-4-20250514">Claude Opus 4</option>
                <option value="gpt-4o">GPT-4o</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium theme-text-secondary mb-2">Max Tokens</label>
              <input
                type="number"
                value={form.maxTokens}
                onChange={(e) => setForm({ ...form, maxTokens: parseInt(e.target.value) || 4096 })}
                className="w-full px-4 py-2 rounded-lg theme-input"
              />
            </div>
            <div>
              <label className="block text-sm font-medium theme-text-secondary mb-2">Temperature</label>
              <input
                type="number"
                step="0.1"
                min="0"
                max="1"
                value={form.temperature}
                onChange={(e) => setForm({ ...form, temperature: parseFloat(e.target.value) || 0.3 })}
                className="w-full px-4 py-2 rounded-lg theme-input"
              />
            </div>
          </div>

          <div className="flex justify-end">
            <button
              onClick={() => setStep(2)}
              disabled={!isStep1Valid || existingAgents.includes(form.role)}
              className="px-6 py-2 rounded-lg bg-alpha-500 hover:bg-alpha-600 text-white disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Continue
            </button>
          </div>
        </div>
      )}

      {/* Step 2: Contract Rules */}
      {step === 2 && (
        <div className="theme-card rounded-xl p-6 space-y-6">
          <h2 className="text-lg font-semibold theme-text-title">Contract Rules</h2>

          {/* Tier 0 */}
          <div>
            <div className="flex items-center gap-2 mb-3">
              <AlertTriangle className="w-4 h-4 text-red-400" />
              <label className="text-sm font-medium text-red-400">Tier 0 Rules (Critical - Never Violated)</label>
            </div>
            {form.tier0Rules.map((rule, idx) => (
              <div key={idx} className="flex gap-2 mb-2">
                <input
                  type="text"
                  value={rule}
                  onChange={(e) => handleArrayFieldChange('tier0Rules', idx, e.target.value)}
                  placeholder="e.g., Never recommend without evidence..."
                  className="flex-1 px-4 py-2 rounded-lg theme-input"
                />
                <button
                  onClick={() => handleRemoveArrayItem('tier0Rules', idx)}
                  className="px-3 py-2 rounded-lg theme-card hover:bg-red-500/10 text-red-400"
                >
                  ×
                </button>
              </div>
            ))}
            <button
              onClick={() => handleAddArrayItem('tier0Rules')}
              className="text-sm text-alpha-400 hover:text-alpha-300 flex items-center gap-1"
            >
              <Plus className="w-3 h-3" /> Add rule
            </button>
          </div>

          {/* Tier 1 */}
          <div>
            <div className="flex items-center gap-2 mb-3">
              <CheckCircle className="w-4 h-4 text-amber-400" />
              <label className="text-sm font-medium text-amber-400">Tier 1 Rules (Standard Practices)</label>
            </div>
            {form.tier1Rules.map((rule, idx) => (
              <div key={idx} className="flex gap-2 mb-2">
                <input
                  type="text"
                  value={rule}
                  onChange={(e) => handleArrayFieldChange('tier1Rules', idx, e.target.value)}
                  placeholder="e.g., Document all decisions..."
                  className="flex-1 px-4 py-2 rounded-lg theme-input"
                />
                <button
                  onClick={() => handleRemoveArrayItem('tier1Rules', idx)}
                  className="px-3 py-2 rounded-lg theme-card hover:bg-amber-500/10 text-amber-400"
                >
                  ×
                </button>
              </div>
            ))}
            <button
              onClick={() => handleAddArrayItem('tier1Rules')}
              className="text-sm text-alpha-400 hover:text-alpha-300 flex items-center gap-1"
            >
              <Plus className="w-3 h-3" /> Add rule
            </button>
          </div>

          {/* Tier 2 */}
          <div>
            <div className="flex items-center gap-2 mb-3">
              <CheckCircle className="w-4 h-4 text-blue-400" />
              <label className="text-sm font-medium text-blue-400">Tier 2 Rules (Best Practices)</label>
            </div>
            {form.tier2Rules.map((rule, idx) => (
              <div key={idx} className="flex gap-2 mb-2">
                <input
                  type="text"
                  value={rule}
                  onChange={(e) => handleArrayFieldChange('tier2Rules', idx, e.target.value)}
                  placeholder="e.g., Consider edge cases..."
                  className="flex-1 px-4 py-2 rounded-lg theme-input"
                />
                <button
                  onClick={() => handleRemoveArrayItem('tier2Rules', idx)}
                  className="px-3 py-2 rounded-lg theme-card hover:bg-blue-500/10 text-blue-400"
                >
                  ×
                </button>
              </div>
            ))}
            <button
              onClick={() => handleAddArrayItem('tier2Rules')}
              className="text-sm text-alpha-400 hover:text-alpha-300 flex items-center gap-1"
            >
              <Plus className="w-3 h-3" /> Add rule
            </button>
          </div>

          {/* Domain & Artifacts */}
          <div className="grid grid-cols-2 gap-6">
            <div>
              <label className="block text-sm font-medium theme-text-secondary mb-3">Domain Expertise</label>
              {form.domainExpertise.map((item, idx) => (
                <div key={idx} className="flex gap-2 mb-2">
                  <input
                    type="text"
                    value={item}
                    onChange={(e) => handleArrayFieldChange('domainExpertise', idx, e.target.value)}
                    placeholder="e.g., Process optimization"
                    className="flex-1 px-4 py-2 rounded-lg theme-input"
                  />
                  <button
                    onClick={() => handleRemoveArrayItem('domainExpertise', idx)}
                    className="px-3 py-2 rounded-lg theme-card hover:bg-[var(--card-hover)] theme-text-muted"
                  >
                    ×
                  </button>
                </div>
              ))}
              <button
                onClick={() => handleAddArrayItem('domainExpertise')}
                className="text-sm text-alpha-400 hover:text-alpha-300 flex items-center gap-1"
              >
                <Plus className="w-3 h-3" /> Add expertise
              </button>
            </div>
            <div>
              <label className="block text-sm font-medium theme-text-secondary mb-3">Artifacts Produced</label>
              {form.artifactsProduced.map((item, idx) => (
                <div key={idx} className="flex gap-2 mb-2">
                  <input
                    type="text"
                    value={item}
                    onChange={(e) => handleArrayFieldChange('artifactsProduced', idx, e.target.value)}
                    placeholder="e.g., Analysis reports"
                    className="flex-1 px-4 py-2 rounded-lg theme-input"
                  />
                  <button
                    onClick={() => handleRemoveArrayItem('artifactsProduced', idx)}
                    className="px-3 py-2 rounded-lg theme-card hover:bg-[var(--card-hover)] theme-text-muted"
                  >
                    ×
                  </button>
                </div>
              ))}
              <button
                onClick={() => handleAddArrayItem('artifactsProduced')}
                className="text-sm text-alpha-400 hover:text-alpha-300 flex items-center gap-1"
              >
                <Plus className="w-3 h-3" /> Add artifact
              </button>
            </div>
          </div>

          <div className="flex justify-between">
            <button
              onClick={() => setStep(1)}
              className="px-6 py-2 rounded-lg theme-card hover:bg-[var(--card-hover)] theme-text-secondary"
            >
              Back
            </button>
            <button
              onClick={() => setStep(3)}
              disabled={!isStep2Valid}
              className="px-6 py-2 rounded-lg bg-alpha-500 hover:bg-alpha-600 text-white disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Continue
            </button>
          </div>
        </div>
      )}

      {/* Step 3: Review & Create */}
      {step === 3 && (
        <div className="space-y-6">
          {!isSubmitting ? (
            <>
              <div className="theme-card rounded-xl p-6">
                <h2 className="text-lg font-semibold theme-text-title mb-4">Review Agent Configuration</h2>
                
                <div className="grid grid-cols-2 gap-6">
                  <div>
                    <h3 className="text-sm font-medium theme-text-muted mb-2">Basic Info</h3>
                    <div className="space-y-2 text-sm">
                      <p><span className="theme-text-muted">Name:</span> <span className="theme-text-title">{form.name}</span></p>
                      <p><span className="theme-text-muted">Role:</span> <span className="font-mono theme-text-title">{form.role}</span></p>
                      <p><span className="theme-text-muted">Category:</span> <span className="theme-text-title capitalize">{form.category}</span></p>
                      <p><span className="theme-text-muted">Reviewer:</span> <span className="theme-text-title">{form.reviewer}</span></p>
                    </div>
                  </div>
                  <div>
                    <h3 className="text-sm font-medium theme-text-muted mb-2">Configuration</h3>
                    <div className="space-y-2 text-sm">
                      <p><span className="theme-text-muted">Model:</span> <span className="font-mono theme-text-title">{form.model}</span></p>
                      <p><span className="theme-text-muted">Max Tokens:</span> <span className="theme-text-title">{form.maxTokens}</span></p>
                      <p><span className="theme-text-muted">Temperature:</span> <span className="theme-text-title">{form.temperature}</span></p>
                    </div>
                  </div>
                </div>

                <div className="mt-6 grid grid-cols-3 gap-4">
                  <div className="p-3 rounded-lg bg-red-500/5 border border-red-500/20">
                    <p className="text-xs font-medium text-red-400 mb-2">Tier 0 Rules ({form.tier0Rules.filter(r => r.trim()).length})</p>
                    <ul className="text-xs theme-text-muted space-y-1">
                      {form.tier0Rules.filter(r => r.trim()).map((r, i) => (
                        <li key={i}>• {r}</li>
                      ))}
                    </ul>
                  </div>
                  <div className="p-3 rounded-lg bg-amber-500/5 border border-amber-500/20">
                    <p className="text-xs font-medium text-amber-400 mb-2">Tier 1 Rules ({form.tier1Rules.filter(r => r.trim()).length})</p>
                    <ul className="text-xs theme-text-muted space-y-1">
                      {form.tier1Rules.filter(r => r.trim()).map((r, i) => (
                        <li key={i}>• {r}</li>
                      ))}
                    </ul>
                  </div>
                  <div className="p-3 rounded-lg bg-blue-500/5 border border-blue-500/20">
                    <p className="text-xs font-medium text-blue-400 mb-2">Tier 2 Rules ({form.tier2Rules.filter(r => r.trim()).length})</p>
                    <ul className="text-xs theme-text-muted space-y-1">
                      {form.tier2Rules.filter(r => r.trim()).map((r, i) => (
                        <li key={i}>• {r}</li>
                      ))}
                    </ul>
                  </div>
                </div>
              </div>

              {/* Architect Assessment Section */}
              <div className="theme-card rounded-xl p-6">
                <div className="flex items-center justify-between mb-4">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 rounded-lg bg-blue-500/10 flex items-center justify-center">
                      <Network className="w-5 h-5 text-blue-400" />
                    </div>
                    <div>
                      <h2 className="text-lg font-semibold theme-text-title">Architect Agent Assessment</h2>
                      <p className="text-xs theme-text-muted">Gap analysis, role overlap detection, and recommendations</p>
                    </div>
                  </div>
                  {!architectAssessment && !isAssessing && (
                    <button
                      onClick={handleArchitectAssessment}
                      className="px-4 py-2 rounded-lg bg-blue-500/10 hover:bg-blue-500/20 text-blue-400 flex items-center gap-2 text-sm"
                    >
                      <Network className="w-4 h-4" />
                      Run Assessment
                    </button>
                  )}
                </div>

                {isAssessing && (
                  <div className="flex items-center gap-3 p-4 rounded-lg bg-blue-500/5 border border-blue-500/20">
                    <Loader2 className="w-5 h-5 animate-spin text-blue-400" />
                    <div>
                      <p className="text-sm font-medium text-blue-400">Architect Agent analyzing proposal...</p>
                      <p className="text-xs theme-text-muted">Checking functional gaps and role overlaps</p>
                    </div>
                  </div>
                )}

                {architectAssessment && (
                  <div className="space-y-4">
                    {/* Recommendation Banner */}
                    <div className={`p-4 rounded-lg flex items-start gap-3 ${
                      architectAssessment.recommendation === 'approve' 
                        ? 'bg-emerald-500/10 border border-emerald-500/20' 
                        : architectAssessment.recommendation === 'caution'
                        ? 'bg-amber-500/10 border border-amber-500/20'
                        : 'bg-red-500/10 border border-red-500/20'
                    }`}>
                      {architectAssessment.recommendation === 'approve' ? (
                        <ThumbsUp className="w-5 h-5 text-emerald-400 flex-shrink-0 mt-0.5" />
                      ) : architectAssessment.recommendation === 'caution' ? (
                        <AlertCircle className="w-5 h-5 text-amber-400 flex-shrink-0 mt-0.5" />
                      ) : (
                        <ThumbsDown className="w-5 h-5 text-red-400 flex-shrink-0 mt-0.5" />
                      )}
                      <div>
                        <p className={`font-medium ${
                          architectAssessment.recommendation === 'approve' ? 'text-emerald-400' :
                          architectAssessment.recommendation === 'caution' ? 'text-amber-400' : 'text-red-400'
                        }`}>
                          {architectAssessment.recommendation === 'approve' ? 'Recommended to Proceed' :
                           architectAssessment.recommendation === 'caution' ? 'Proceed with Caution' : 'Not Recommended'}
                        </p>
                        <p className="text-sm theme-text-secondary mt-1">{architectAssessment.summary}</p>
                      </div>
                    </div>

                    <div className="grid grid-cols-2 gap-4">
                      {/* Gap Analysis */}
                      <div className="p-4 rounded-lg bg-[var(--card-hover)]">
                        <div className="flex items-center gap-2 mb-3">
                          <Layers className="w-4 h-4 text-alpha-400" />
                          <h3 className="font-medium theme-text-title text-sm">Gap Analysis</h3>
                        </div>
                        <div className="space-y-2 text-sm">
                          <div className="flex items-start gap-2">
                            {architectAssessment.gapAnalysis.addressesGap ? (
                              <CheckCircle className="w-4 h-4 text-emerald-400 flex-shrink-0 mt-0.5" />
                            ) : (
                              <X className="w-4 h-4 text-red-400 flex-shrink-0 mt-0.5" />
                            )}
                            <div>
                              <p className="theme-text-secondary">
                                {architectAssessment.gapAnalysis.addressesGap ? 'Addresses Functional Gap' : 'No Clear Gap Addressed'}
                              </p>
                              <p className="text-xs theme-text-muted">{architectAssessment.gapAnalysis.gapDescription}</p>
                            </div>
                          </div>
                          {architectAssessment.gapAnalysis.createsGap && (
                            <div className="flex items-start gap-2">
                              <AlertTriangle className="w-4 h-4 text-amber-400 flex-shrink-0 mt-0.5" />
                              <div>
                                <p className="text-amber-400">Creates New Gap</p>
                                <p className="text-xs theme-text-muted">{architectAssessment.gapAnalysis.newGapDescription}</p>
                              </div>
                            </div>
                          )}
                        </div>
                      </div>

                      {/* Overlap Analysis */}
                      <div className="p-4 rounded-lg bg-[var(--card-hover)]">
                        <div className="flex items-center gap-2 mb-3">
                          <GitMerge className="w-4 h-4 text-alpha-400" />
                          <h3 className="font-medium theme-text-title text-sm">Role Overlap Analysis</h3>
                        </div>
                        <div className="space-y-2 text-sm">
                          <div className="flex items-start gap-2">
                            {architectAssessment.overlapAnalysis.hasOverlap ? (
                              <AlertCircle className="w-4 h-4 text-amber-400 flex-shrink-0 mt-0.5" />
                            ) : (
                              <CheckCircle className="w-4 h-4 text-emerald-400 flex-shrink-0 mt-0.5" />
                            )}
                            <div>
                              <p className={architectAssessment.overlapAnalysis.hasOverlap ? 'text-amber-400' : 'theme-text-secondary'}>
                                {architectAssessment.overlapAnalysis.hasOverlap ? 'Overlap Detected' : 'No Significant Overlap'}
                              </p>
                              <p className="text-xs theme-text-muted">{architectAssessment.overlapAnalysis.overlapDetails}</p>
                              {architectAssessment.overlapAnalysis.overlappingAgents.length > 0 && (
                                <div className="flex gap-1 mt-2">
                                  {architectAssessment.overlapAnalysis.overlappingAgents.map((agent, i) => (
                                    <span key={i} className="text-xs px-2 py-0.5 rounded bg-amber-500/10 text-amber-400">
                                      {agent}
                                    </span>
                                  ))}
                                </div>
                              )}
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    {/* Suggestions */}
                    <div className="p-4 rounded-lg bg-[var(--card-hover)]">
                      <h3 className="font-medium theme-text-title text-sm mb-2">Architect Suggestions</h3>
                      <ul className="space-y-1">
                        {architectAssessment.suggestions.map((suggestion, i) => (
                          <li key={i} className="flex items-start gap-2 text-sm theme-text-secondary">
                            <span className="text-alpha-400">•</span>
                            {suggestion}
                          </li>
                        ))}
                      </ul>
                    </div>
                  </div>
                )}

                {!architectAssessment && !isAssessing && (
                  <p className="text-sm theme-text-muted text-center py-4">
                    Run the assessment to get Architect Agent's analysis of this agent proposal
                  </p>
                )}
              </div>

              <div className="flex justify-between">
                <button
                  onClick={() => setStep(2)}
                  className="px-6 py-2 rounded-lg theme-card hover:bg-[var(--card-hover)] theme-text-secondary"
                >
                  Back
                </button>
                <button
                  onClick={handleSubmit}
                  disabled={!architectAssessment}
                  className="px-6 py-2 rounded-lg bg-emerald-500 hover:bg-emerald-600 text-white flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <Brain className="w-4 h-4" />
                  Create Agent via Pipeline
                </button>
              </div>
            </>
          ) : (
            <div className="theme-card rounded-xl p-8">
              <div className="text-center mb-6">
                <Loader2 className="w-12 h-12 animate-spin text-alpha-400 mx-auto mb-4" />
                <h2 className="text-lg font-semibold theme-text-title">Creating Agent via Pipeline</h2>
                <p className="text-sm theme-text-muted">Agents are processing your request...</p>
              </div>
              
              <div className="max-w-md mx-auto space-y-3">
                {agentProgress.map((progress, idx) => (
                  <div key={idx} className="flex items-center gap-3 p-3 rounded-lg bg-alpha-500/5 border border-alpha-500/20">
                    <CheckCircle className="w-4 h-4 text-emerald-400" />
                    <span className="text-sm theme-text-secondary">{progress}</span>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
