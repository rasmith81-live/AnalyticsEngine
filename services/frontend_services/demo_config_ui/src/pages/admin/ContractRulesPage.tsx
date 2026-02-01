import { useState } from 'react';
import { 
  ScrollText, 
  Shield, 
  AlertTriangle,
  CheckCircle,
  Search,
  Filter,
} from 'lucide-react';

interface ContractRule {
  id: string;
  agentRole: string;
  agentName: string;
  tier: 0 | 1 | 2;
  text: string;
}

const allRules: ContractRule[] = [
  // Tier 0 Rules
  { id: 'bs-t0-1', agentRole: 'business_strategist', agentName: 'Business Strategist', tier: 0, text: 'Never recommend strategy without citing industry evidence' },
  { id: 'bs-t0-2', agentRole: 'business_strategist', agentName: 'Business Strategist', tier: 0, text: 'Never ignore competitive context' },
  { id: 'bs-t0-3', agentRole: 'business_strategist', agentName: 'Business Strategist', tier: 0, text: 'Always validate strategic fit with business model' },
  { id: 'ba-t0-1', agentRole: 'business_analyst', agentName: 'Business Analyst', tier: 0, text: 'Never define KPIs without stakeholder validation' },
  { id: 'ba-t0-2', agentRole: 'business_analyst', agentName: 'Business Analyst', tier: 0, text: 'Never assume data availability without verification' },
  { id: 'ba-t0-3', agentRole: 'business_analyst', agentName: 'Business Analyst', tier: 0, text: 'Always trace KPIs to business objectives' },
  { id: 'dev-t0-1', agentRole: 'developer', agentName: 'Developer', tier: 0, text: 'Never commit code without passing tests' },
  { id: 'dev-t0-2', agentRole: 'developer', agentName: 'Developer', tier: 0, text: 'Always follow established coding standards' },
  { id: 'dev-t0-3', agentRole: 'developer', agentName: 'Developer', tier: 0, text: 'Never hardcode sensitive credentials' },
  { id: 'arc-t0-1', agentRole: 'architect', agentName: 'Architect', tier: 0, text: 'Never create circular dependencies in entity relationships' },
  { id: 'arc-t0-2', agentRole: 'architect', agentName: 'Architect', tier: 0, text: 'Always validate entity schemas against existing ontology' },
  { id: 'test-t0-1', agentRole: 'tester', agentName: 'Tester', tier: 0, text: 'Never approve code with failing critical tests' },
  { id: 'test-t0-2', agentRole: 'tester', agentName: 'Tester', tier: 0, text: 'Always test edge cases and error conditions' },
  { id: 'dg-t0-1', agentRole: 'data_governance_specialist', agentName: 'Data Governance Specialist', tier: 0, text: 'Never bypass data classification requirements' },
  { id: 'dg-t0-2', agentRole: 'data_governance_specialist', agentName: 'Data Governance Specialist', tier: 0, text: 'Always enforce data retention policies' },
  
  // Tier 1 Rules
  { id: 'bs-t1-1', agentRole: 'business_strategist', agentName: 'Business Strategist', tier: 1, text: 'Apply appropriate strategy frameworks (Porter, SWOT, etc.)' },
  { id: 'bs-t1-2', agentRole: 'business_strategist', agentName: 'Business Strategist', tier: 1, text: 'Ground recommendations in market data' },
  { id: 'ba-t1-1', agentRole: 'business_analyst', agentName: 'Business Analyst', tier: 1, text: 'Document KPI definitions with calculation methods' },
  { id: 'ba-t1-2', agentRole: 'business_analyst', agentName: 'Business Analyst', tier: 1, text: 'Map data sources for each KPI' },
  { id: 'dev-t1-1', agentRole: 'developer', agentName: 'Developer', tier: 1, text: 'Write comprehensive unit tests for new code' },
  { id: 'dev-t1-2', agentRole: 'developer', agentName: 'Developer', tier: 1, text: 'Document public APIs and complex logic' },
  { id: 'arc-t1-1', agentRole: 'architect', agentName: 'Architect', tier: 1, text: 'Design for extensibility and future requirements' },
  { id: 'test-t1-1', agentRole: 'tester', agentName: 'Tester', tier: 1, text: 'Achieve minimum 80% code coverage' },
  
  // Tier 2 Rules
  { id: 'bs-t2-1', agentRole: 'business_strategist', agentName: 'Business Strategist', tier: 2, text: 'Consider long-term strategic implications' },
  { id: 'bs-t2-2', agentRole: 'business_strategist', agentName: 'Business Strategist', tier: 2, text: 'Document assumptions explicitly' },
  { id: 'ba-t2-1', agentRole: 'business_analyst', agentName: 'Business Analyst', tier: 2, text: 'Consider edge cases in calculations' },
  { id: 'dev-t2-1', agentRole: 'developer', agentName: 'Developer', tier: 2, text: 'Optimize for readability over cleverness' },
  { id: 'arc-t2-1', agentRole: 'architect', agentName: 'Architect', tier: 2, text: 'Optimize for query performance' },
  { id: 'test-t2-1', agentRole: 'tester', agentName: 'Tester', tier: 2, text: 'Include performance benchmarks' },
];

export default function ContractRulesPage() {
  const [searchTerm, setSearchTerm] = useState('');
  const [tierFilter, setTierFilter] = useState<'all' | 0 | 1 | 2>('all');

  const filteredRules = allRules.filter(rule => {
    const matchesSearch = rule.text.toLowerCase().includes(searchTerm.toLowerCase()) ||
                          rule.agentName.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesTier = tierFilter === 'all' || rule.tier === tierFilter;
    return matchesSearch && matchesTier;
  });

  const tier0Rules = filteredRules.filter(r => r.tier === 0);
  const tier1Rules = filteredRules.filter(r => r.tier === 1);
  const tier2Rules = filteredRules.filter(r => r.tier === 2);

  const getTierColor = (tier: number) => {
    switch (tier) {
      case 0: return 'text-red-400 bg-red-500/10 border-red-500/20';
      case 1: return 'text-amber-400 bg-amber-500/10 border-amber-500/20';
      case 2: return 'text-blue-400 bg-blue-500/10 border-blue-500/20';
      default: return '';
    }
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title">Contract Rules</h1>
          <p className="mt-2 theme-text-secondary">
            Browse all tiered rules across the 27 agent contracts
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
              <ScrollText className="w-5 h-5 text-alpha-400" />
            </div>
            <div>
              <p className="text-2xl font-bold theme-text-title">{allRules.length}</p>
              <p className="text-sm theme-text-muted">Total Rules</p>
            </div>
          </div>
        </div>
        <div className="theme-card rounded-xl p-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-lg bg-red-500/10 flex items-center justify-center">
              <AlertTriangle className="w-5 h-5 text-red-400" />
            </div>
            <div>
              <p className="text-2xl font-bold theme-text-title">{allRules.filter(r => r.tier === 0).length}</p>
              <p className="text-sm theme-text-muted">Tier 0 (Critical)</p>
            </div>
          </div>
        </div>
        <div className="theme-card rounded-xl p-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-lg bg-amber-500/10 flex items-center justify-center">
              <CheckCircle className="w-5 h-5 text-amber-400" />
            </div>
            <div>
              <p className="text-2xl font-bold theme-text-title">{allRules.filter(r => r.tier === 1).length}</p>
              <p className="text-sm theme-text-muted">Tier 1 (Standard)</p>
            </div>
          </div>
        </div>
        <div className="theme-card rounded-xl p-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-lg bg-blue-500/10 flex items-center justify-center">
              <CheckCircle className="w-5 h-5 text-blue-400" />
            </div>
            <div>
              <p className="text-2xl font-bold theme-text-title">{allRules.filter(r => r.tier === 2).length}</p>
              <p className="text-sm theme-text-muted">Tier 2 (Best Practice)</p>
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
              placeholder="Search rules or agents..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-9 pr-4 py-2 rounded-lg theme-input text-sm"
            />
          </div>
          <div className="flex items-center gap-2">
            <Filter className="w-4 h-4 theme-text-muted" />
            <button
              onClick={() => setTierFilter('all')}
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                tierFilter === 'all' ? 'bg-alpha-500 text-white' : 'theme-card hover:bg-[var(--card-hover)] theme-text-secondary'
              }`}
            >
              All
            </button>
            <button
              onClick={() => setTierFilter(0)}
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                tierFilter === 0 ? 'bg-red-500 text-white' : 'theme-card hover:bg-[var(--card-hover)] theme-text-secondary'
              }`}
            >
              Tier 0
            </button>
            <button
              onClick={() => setTierFilter(1)}
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                tierFilter === 1 ? 'bg-amber-500 text-white' : 'theme-card hover:bg-[var(--card-hover)] theme-text-secondary'
              }`}
            >
              Tier 1
            </button>
            <button
              onClick={() => setTierFilter(2)}
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                tierFilter === 2 ? 'bg-blue-500 text-white' : 'theme-card hover:bg-[var(--card-hover)] theme-text-secondary'
              }`}
            >
              Tier 2
            </button>
          </div>
        </div>
      </div>

      {/* Rules by Tier */}
      <div className="space-y-6">
        {/* Tier 0 */}
        {tier0Rules.length > 0 && (tierFilter === 'all' || tierFilter === 0) && (
          <div>
            <h2 className="text-lg font-semibold theme-text-title mb-4 flex items-center gap-2">
              <AlertTriangle className="w-5 h-5 text-red-400" />
              Tier 0 - Critical Rules ({tier0Rules.length})
            </h2>
            <div className="theme-card rounded-xl divide-y divide-[var(--border-color)]">
              {tier0Rules.map((rule) => (
                <div key={rule.id} className="p-4 flex items-start gap-4">
                  <div className={`px-2 py-1 rounded text-xs font-medium ${getTierColor(rule.tier)}`}>
                    T0
                  </div>
                  <div className="flex-1">
                    <p className="text-sm theme-text-title">{rule.text}</p>
                    <p className="text-xs theme-text-muted mt-1">{rule.agentName} Agent</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Tier 1 */}
        {tier1Rules.length > 0 && (tierFilter === 'all' || tierFilter === 1) && (
          <div>
            <h2 className="text-lg font-semibold theme-text-title mb-4 flex items-center gap-2">
              <CheckCircle className="w-5 h-5 text-amber-400" />
              Tier 1 - Standard Rules ({tier1Rules.length})
            </h2>
            <div className="theme-card rounded-xl divide-y divide-[var(--border-color)]">
              {tier1Rules.map((rule) => (
                <div key={rule.id} className="p-4 flex items-start gap-4">
                  <div className={`px-2 py-1 rounded text-xs font-medium ${getTierColor(rule.tier)}`}>
                    T1
                  </div>
                  <div className="flex-1">
                    <p className="text-sm theme-text-title">{rule.text}</p>
                    <p className="text-xs theme-text-muted mt-1">{rule.agentName} Agent</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Tier 2 */}
        {tier2Rules.length > 0 && (tierFilter === 'all' || tierFilter === 2) && (
          <div>
            <h2 className="text-lg font-semibold theme-text-title mb-4 flex items-center gap-2">
              <CheckCircle className="w-5 h-5 text-blue-400" />
              Tier 2 - Best Practice Rules ({tier2Rules.length})
            </h2>
            <div className="theme-card rounded-xl divide-y divide-[var(--border-color)]">
              {tier2Rules.map((rule) => (
                <div key={rule.id} className="p-4 flex items-start gap-4">
                  <div className={`px-2 py-1 rounded text-xs font-medium ${getTierColor(rule.tier)}`}>
                    T2
                  </div>
                  <div className="flex-1">
                    <p className="text-sm theme-text-title">{rule.text}</p>
                    <p className="text-xs theme-text-muted mt-1">{rule.agentName} Agent</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {filteredRules.length === 0 && (
          <div className="text-center py-12 theme-text-muted">
            <ScrollText className="w-12 h-12 mx-auto mb-4 opacity-50" />
            <p>No rules found matching your search</p>
          </div>
        )}
      </div>
    </div>
  );
}
