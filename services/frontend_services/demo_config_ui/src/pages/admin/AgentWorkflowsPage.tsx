import { useState, useMemo } from 'react';
import {
  Network,
  ArrowRight,
  Filter,
  Search,
  RefreshCw,
  Download,
  ZoomIn,
  ZoomOut,
  Maximize2,
  Info,
  CheckCircle,
  AlertCircle,
  Clock,
  ChevronDown,
  ChevronRight,
  Brain,
  Code,
  TestTube,
  FileText,
  Database,
  Users,
  Target,
  Shield,
  Settings,
  Briefcase,
  TrendingUp,
  BarChart3,
  LineChart,
  Workflow,
  BookOpen,
  GitBranch,
  Link,
  Activity,
  UserCheck,
  Palette,
  Rocket,
  ClipboardList,
  ShieldCheck,
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';
import { cn } from '../../lib/utils';

interface HandoffDefinition {
  name: string;
  toolName: string;
  sourceAgent: string;
  targetAgent: string;
  category: string;
  description: string;
  requiredInputs: string[];
  expectedOutputs: string[];
  bidirectional: boolean;
  responseTool?: string;
  validationStatus: 'passed' | 'failed' | 'pending';
}

interface WorkflowCategory {
  id: string;
  name: string;
  color: string;
  bgColor: string;
  borderColor: string;
}

const WORKFLOW_CATEGORIES: WorkflowCategory[] = [
  { id: 'entity_design', name: 'Entity Design', color: 'text-blue-400', bgColor: 'bg-blue-500/10', borderColor: 'border-blue-500/30' },
  { id: 'ml_predictive', name: 'ML/Predictive', color: 'text-purple-400', bgColor: 'bg-purple-500/10', borderColor: 'border-purple-500/30' },
  { id: 'analytics', name: 'Analytics', color: 'text-cyan-400', bgColor: 'bg-cyan-500/10', borderColor: 'border-cyan-500/30' },
  { id: 'sales_pipeline', name: 'Sales Pipeline', color: 'text-green-400', bgColor: 'bg-green-500/10', borderColor: 'border-green-500/30' },
  { id: 'customer_success', name: 'Customer Success', color: 'text-amber-400', bgColor: 'bg-amber-500/10', borderColor: 'border-amber-500/30' },
  { id: 'operations', name: 'Operations', color: 'text-orange-400', bgColor: 'bg-orange-500/10', borderColor: 'border-orange-500/30' },
  { id: 'governance', name: 'Governance', color: 'text-red-400', bgColor: 'bg-red-500/10', borderColor: 'border-red-500/30' },
  { id: 'integration', name: 'Integration', color: 'text-teal-400', bgColor: 'bg-teal-500/10', borderColor: 'border-teal-500/30' },
  { id: 'knowledge_curation', name: 'Knowledge Curation', color: 'text-indigo-400', bgColor: 'bg-indigo-500/10', borderColor: 'border-indigo-500/30' },
  { id: 'release', name: 'Release Management', color: 'text-pink-400', bgColor: 'bg-pink-500/10', borderColor: 'border-pink-500/30' },
];

const HANDOFF_REGISTRY: HandoffDefinition[] = [
  // Entity Design Workflow
  { name: 'Architect requests entity validation', toolName: 'request_entity_validation', sourceAgent: 'ArchitectAgent', targetAgent: 'BusinessAnalystAgent', category: 'entity_design', description: 'Architect requests Business Analyst to validate entity design', requiredInputs: ['entity_name', 'entity_type', 'proposed_attributes'], expectedOutputs: ['validation_status', 'recommendations'], bidirectional: true, responseTool: 'share_entity_validation', validationStatus: 'passed' },
  { name: 'Architect requests KPI requirements', toolName: 'request_kpi_requirements', sourceAgent: 'ArchitectAgent', targetAgent: 'BusinessAnalystAgent', category: 'entity_design', description: 'Architect requests Business Analyst to identify KPIs', requiredInputs: ['entity_name', 'business_context'], expectedOutputs: ['kpi_list', 'measurement_requirements'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Architect requests schema generation', toolName: 'request_schema_generation', sourceAgent: 'ArchitectAgent', targetAgent: 'DeveloperAgent', category: 'entity_design', description: 'Architect requests Developer to generate schemas', requiredInputs: ['entity_definitions', 'schema_type'], expectedOutputs: ['schema_artifacts'], bidirectional: true, responseTool: 'share_schema_artifacts', validationStatus: 'passed' },
  { name: 'Developer requests test specification', toolName: 'request_test_specification', sourceAgent: 'DeveloperAgent', targetAgent: 'TesterAgent', category: 'entity_design', description: 'Developer requests Tester to create test specifications', requiredInputs: ['code_artifact', 'test_requirements'], expectedOutputs: ['test_specification', 'test_cases'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Developer requests documentation', toolName: 'request_documentation', sourceAgent: 'DeveloperAgent', targetAgent: 'DocumenterAgent', category: 'entity_design', description: 'Developer requests Documenter to create documentation', requiredInputs: ['code_artifact', 'doc_type'], expectedOutputs: ['documentation'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Tester requests test documentation', toolName: 'request_test_documentation', sourceAgent: 'TesterAgent', targetAgent: 'DocumenterAgent', category: 'entity_design', description: 'Tester requests Documenter to create test documentation', requiredInputs: ['test_suite', 'test_cases'], expectedOutputs: ['test_documentation'], bidirectional: false, validationStatus: 'passed' },
  
  // ML/Predictive Workflow
  { name: 'Data Scientist handoff to Architect', toolName: 'handoff_to_architect_for_model_design', sourceAgent: 'DataScientistAgent', targetAgent: 'ArchitectAgent', category: 'ml_predictive', description: 'Data Scientist hands off correlation analysis for ML architecture design', requiredInputs: ['correlation_analysis_id', 'model_type', 'target_variable', 'features'], expectedOutputs: ['model_architecture'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Data Scientist handoff to Developer', toolName: 'handoff_to_developer_for_implementation', sourceAgent: 'DataScientistAgent', targetAgent: 'DeveloperAgent', category: 'ml_predictive', description: 'Data Scientist hands off model specification for implementation', requiredInputs: ['model_specification_id', 'architecture_id'], expectedOutputs: ['implementation_artifacts'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Data Scientist requests architecture review', toolName: 'request_architecture_review', sourceAgent: 'DataScientistAgent', targetAgent: 'ArchitectAgent', category: 'ml_predictive', description: 'Data Scientist requests architecture review', requiredInputs: ['model_specification', 'architecture_proposal'], expectedOutputs: ['review_feedback', 'approval_status'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Architect handoff ML to Developer', toolName: 'handoff_model_architecture_to_developer', sourceAgent: 'ArchitectAgent', targetAgent: 'DeveloperAgent', category: 'ml_predictive', description: 'Architect hands off ML architecture for implementation', requiredInputs: ['architecture_id', 'model_specification_id'], expectedOutputs: ['implementation_plan'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Developer handoff ML to Tester', toolName: 'handoff_ml_to_tester', sourceAgent: 'DeveloperAgent', targetAgent: 'TesterAgent', category: 'ml_predictive', description: 'Developer hands off ML implementation for testing', requiredInputs: ['model_specification_id', 'implementation_id', 'model_type'], expectedOutputs: ['test_plan', 'test_results'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Developer handoff ML to Documenter', toolName: 'handoff_ml_to_documenter', sourceAgent: 'DeveloperAgent', targetAgent: 'DocumenterAgent', category: 'ml_predictive', description: 'Developer hands off ML model for documentation', requiredInputs: ['model_specification_id', 'model_name', 'model_purpose'], expectedOutputs: ['model_documentation', 'api_documentation', 'user_guide'], bidirectional: false, validationStatus: 'passed' },
  
  // Analytics Workflow
  { name: 'Business Analyst requests KPI calculation', toolName: 'request_kpi_calculation_design', sourceAgent: 'BusinessAnalystAgent', targetAgent: 'DataAnalystAgent', category: 'analytics', description: 'Business Analyst requests KPI calculation design', requiredInputs: ['kpi_list', 'calculation_requirements'], expectedOutputs: ['calculation_definitions'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Business Analyst requests predictive analysis', toolName: 'request_predictive_analysis', sourceAgent: 'BusinessAnalystAgent', targetAgent: 'DataScientistAgent', category: 'analytics', description: 'Business Analyst requests predictive analysis', requiredInputs: ['kpi_ids'], expectedOutputs: ['predictive_opportunities', 'correlation_analysis'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Data Steward requests statistical validation', toolName: 'request_statistical_validation', sourceAgent: 'DataStewardAgent', targetAgent: 'DataScientistAgent', category: 'analytics', description: 'Data Steward requests statistical validation', requiredInputs: ['kpi_pairs', 'suspected_correlations'], expectedOutputs: ['statistical_validation', 'p_values'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Data Steward requests ML model design', toolName: 'request_ml_model_design', sourceAgent: 'DataStewardAgent', targetAgent: 'DataScientistAgent', category: 'analytics', description: 'Data Steward collaborates on ML model design', requiredInputs: ['target_kpi', 'feature_kpis'], expectedOutputs: ['model_design', 'feature_importance'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Formula Builder requests review', toolName: 'request_data_analyst_review', sourceAgent: 'FormulaBuilderAgent', targetAgent: 'DataAnalystAgent', category: 'analytics', description: 'Formula Builder requests calculation review', requiredInputs: ['formula_definition', 'calculation_steps'], expectedOutputs: ['review_feedback', 'optimization_suggestions'], bidirectional: false, validationStatus: 'passed' },
  
  // Sales Pipeline Workflow
  { name: 'Sales requests MQL from Marketing', toolName: 'request_mql_from_marketing', sourceAgent: 'SalesManagerAgent', targetAgent: 'MarketingManagerAgent', category: 'sales_pipeline', description: 'Sales Manager requests Marketing Qualified Leads', requiredInputs: ['lead_criteria', 'quantity_needed'], expectedOutputs: ['mql_list'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Sales requests deal pricing', toolName: 'request_deal_pricing', sourceAgent: 'SalesManagerAgent', targetAgent: 'AccountantAgent', category: 'sales_pipeline', description: 'Sales Manager requests deal pricing', requiredInputs: ['deal_id', 'pricing_requirements'], expectedOutputs: ['pricing_proposal', 'financial_terms'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Sales handoff to Project Manager', toolName: 'handoff_to_project_manager', sourceAgent: 'SalesManagerAgent', targetAgent: 'ProjectManagerAgent', category: 'sales_pipeline', description: 'Sales Manager hands off deal for onboarding', requiredInputs: ['deal_id', 'client_info', 'contract_terms'], expectedOutputs: ['onboarding_plan'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Marketing handoff MQL to Sales', toolName: 'handoff_mql_to_sales', sourceAgent: 'MarketingManagerAgent', targetAgent: 'SalesManagerAgent', category: 'sales_pipeline', description: 'Marketing hands off qualified leads', requiredInputs: ['lead_list', 'qualification_criteria'], expectedOutputs: ['acceptance_status'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Marketing requests campaign analytics', toolName: 'request_campaign_analytics', sourceAgent: 'MarketingManagerAgent', targetAgent: 'DataScientistAgent', category: 'sales_pipeline', description: 'Marketing requests campaign analysis', requiredInputs: ['campaign_id'], expectedOutputs: ['performance_analysis', 'recommendations'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Marketing requests design assets', toolName: 'request_design_assets', sourceAgent: 'MarketingManagerAgent', targetAgent: 'UIDesignerAgent', category: 'sales_pipeline', description: 'Marketing requests design assets', requiredInputs: ['campaign_brief', 'asset_requirements'], expectedOutputs: ['design_assets'], bidirectional: false, validationStatus: 'passed' },
  
  // Customer Success Workflow
  { name: 'CS requests churn prediction', toolName: 'request_churn_prediction_model', sourceAgent: 'CustomerSuccessAgent', targetAgent: 'DataScientistAgent', category: 'customer_success', description: 'Customer Success requests churn prediction', requiredInputs: ['customer_segment', 'prediction_requirements'], expectedOutputs: ['churn_model', 'risk_scores'], bidirectional: false, validationStatus: 'passed' },
  { name: 'CS handoff expansion to Sales', toolName: 'handoff_expansion_to_sales', sourceAgent: 'CustomerSuccessAgent', targetAgent: 'SalesManagerAgent', category: 'customer_success', description: 'Customer Success hands off expansion opportunity', requiredInputs: ['customer_id', 'expansion_opportunity'], expectedOutputs: ['sales_engagement_plan'], bidirectional: false, validationStatus: 'passed' },
  
  // Operations Workflow
  { name: 'Operations requests demand forecast', toolName: 'request_demand_forecast_model', sourceAgent: 'OperationsManagerAgent', targetAgent: 'DataScientistAgent', category: 'operations', description: 'Operations requests demand forecasting', requiredInputs: ['forecast_horizon', 'product_categories'], expectedOutputs: ['forecast_model', 'predictions'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Process Engineer requests ops review', toolName: 'request_operations_review', sourceAgent: 'ProcessEngineerAgent', targetAgent: 'OperationsManagerAgent', category: 'operations', description: 'Process Engineer requests operations review', requiredInputs: ['simulation_id', 'process_changes'], expectedOutputs: ['review_feedback', 'approval_status'], bidirectional: false, validationStatus: 'passed' },
  
  // Governance Workflow
  { name: 'Architect requests governance review', toolName: 'request_governance_review', sourceAgent: 'ArchitectAgent', targetAgent: 'DataGovernanceAgent', category: 'governance', description: 'Architect requests governance compliance review', requiredInputs: ['entity_definition', 'compliance_requirements'], expectedOutputs: ['compliance_status', 'recommendations'], bidirectional: false, validationStatus: 'passed' },
  
  // Integration Workflow
  { name: 'Integration requests mapping help', toolName: 'request_mapping_assistance', sourceAgent: 'IntegrationSpecialistAgent', targetAgent: 'MappingSpecialistAgent', category: 'integration', description: 'Integration Specialist requests mapping assistance', requiredInputs: ['source_schema', 'target_schema'], expectedOutputs: ['field_mappings', 'transformation_rules'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Integration requests custom dev', toolName: 'request_custom_development', sourceAgent: 'IntegrationSpecialistAgent', targetAgent: 'DeveloperAgent', category: 'integration', description: 'Integration Specialist requests custom development', requiredInputs: ['integration_requirements', 'api_specifications'], expectedOutputs: ['integration_code'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Data Quality requests profiling', toolName: 'request_data_profiling', sourceAgent: 'DataQualityAgent', targetAgent: 'DataAnalystAgent', category: 'integration', description: 'Data Quality Analyst requests data profiling', requiredInputs: ['data_source', 'profiling_requirements'], expectedOutputs: ['data_profile', 'quality_metrics'], bidirectional: false, validationStatus: 'passed' },
  
  // Knowledge Curation Workflow
  { name: 'Librarian requests Architect review', toolName: 'request_architect_review', sourceAgent: 'LibrarianCuratorAgent', targetAgent: 'ArchitectAgent', category: 'knowledge_curation', description: 'Librarian requests entity review for DDD', requiredInputs: ['extracted_entities', 'domain_context'], expectedOutputs: ['design_feedback', 'entity_refinements'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Librarian requests BA review', toolName: 'request_business_analyst_review', sourceAgent: 'LibrarianCuratorAgent', targetAgent: 'BusinessAnalystAgent', category: 'knowledge_curation', description: 'Librarian requests KPI review', requiredInputs: ['extracted_kpis', 'business_context'], expectedOutputs: ['kpi_validation', 'business_alignment'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Strategist requests competitive analysis', toolName: 'request_competitive_analysis', sourceAgent: 'BusinessStrategistAgent', targetAgent: 'CompetitiveAnalystAgent', category: 'knowledge_curation', description: 'Strategist requests competitive analysis', requiredInputs: ['business_model', 'market_segment'], expectedOutputs: ['competitive_landscape', 'peer_analysis'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Analyst requests strategist review', toolName: 'request_strategist_review', sourceAgent: 'CompetitiveAnalystAgent', targetAgent: 'BusinessStrategistAgent', category: 'knowledge_curation', description: 'Analyst requests strategic review', requiredInputs: ['competitive_findings', 'market_analysis'], expectedOutputs: ['strategic_implications', 'recommendations'], bidirectional: false, validationStatus: 'passed' },
  
  // Release Management Workflow
  { name: 'Developer requests deployment config', toolName: 'request_deployment_config', sourceAgent: 'DeveloperAgent', targetAgent: 'DeploymentSpecialistAgent', category: 'release', description: 'Developer requests deployment configuration', requiredInputs: ['artifact_id', 'deployment_target'], expectedOutputs: ['deployment_config', 'infrastructure_requirements'], bidirectional: false, validationStatus: 'passed' },
  { name: 'Release Manager requests review', toolName: 'request_deployment_review', sourceAgent: 'ReleaseManagerAgent', targetAgent: 'DeploymentSpecialistAgent', category: 'release', description: 'Release Manager requests deployment review', requiredInputs: ['release_plan', 'deployment_schedule'], expectedOutputs: ['review_feedback', 'approval_status'], bidirectional: false, validationStatus: 'passed' },
];

const AGENT_ICONS: Record<string, React.ReactNode> = {
  ArchitectAgent: <Network className="w-4 h-4" />,
  BusinessAnalystAgent: <ClipboardList className="w-4 h-4" />,
  DeveloperAgent: <Code className="w-4 h-4" />,
  TesterAgent: <TestTube className="w-4 h-4" />,
  DocumenterAgent: <FileText className="w-4 h-4" />,
  DataAnalystAgent: <Database className="w-4 h-4" />,
  DataScientistAgent: <Brain className="w-4 h-4" />,
  DataGovernanceAgent: <Shield className="w-4 h-4" />,
  SalesManagerAgent: <TrendingUp className="w-4 h-4" />,
  MarketingManagerAgent: <Target className="w-4 h-4" />,
  AccountantAgent: <BarChart3 className="w-4 h-4" />,
  ProjectManagerAgent: <ClipboardList className="w-4 h-4" />,
  CustomerSuccessAgent: <UserCheck className="w-4 h-4" />,
  OperationsManagerAgent: <Activity className="w-4 h-4" />,
  ProcessEngineerAgent: <Workflow className="w-4 h-4" />,
  IntegrationSpecialistAgent: <Link className="w-4 h-4" />,
  MappingSpecialistAgent: <GitBranch className="w-4 h-4" />,
  DataQualityAgent: <ShieldCheck className="w-4 h-4" />,
  LibrarianCuratorAgent: <BookOpen className="w-4 h-4" />,
  BusinessStrategistAgent: <Briefcase className="w-4 h-4" />,
  CompetitiveAnalystAgent: <LineChart className="w-4 h-4" />,
  UIDesignerAgent: <Palette className="w-4 h-4" />,
  DeploymentSpecialistAgent: <Rocket className="w-4 h-4" />,
  ReleaseManagerAgent: <Settings className="w-4 h-4" />,
  DataStewardAgent: <Shield className="w-4 h-4" />,
  FormulaBuilderAgent: <Database className="w-4 h-4" />,
};

function getAgentShortName(agent: string): string {
  return agent.replace('Agent', '').replace(/([A-Z])/g, ' $1').trim();
}

function HandoffCard({ handoff, category }: { handoff: HandoffDefinition; category: WorkflowCategory }) {
  const [expanded, setExpanded] = useState(false);
  
  return (
    <div 
      className={cn(
        "border rounded-lg p-3 transition-all cursor-pointer",
        category.bgColor, category.borderColor,
        "hover:border-opacity-60"
      )}
      onClick={() => setExpanded(!expanded)}
    >
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="flex items-center gap-1">
            <div className="p-1.5 rounded bg-slate-700/50">
              {AGENT_ICONS[handoff.sourceAgent] || <Users className="w-4 h-4" />}
            </div>
            <ArrowRight className={cn("w-4 h-4", category.color)} />
            <div className="p-1.5 rounded bg-slate-700/50">
              {AGENT_ICONS[handoff.targetAgent] || <Users className="w-4 h-4" />}
            </div>
          </div>
          <span className="text-sm font-medium theme-text">{handoff.name}</span>
        </div>
        <div className="flex items-center gap-2">
          {handoff.validationStatus === 'passed' && <CheckCircle className="w-4 h-4 text-green-400" />}
          {handoff.validationStatus === 'failed' && <AlertCircle className="w-4 h-4 text-red-400" />}
          {handoff.validationStatus === 'pending' && <Clock className="w-4 h-4 text-amber-400" />}
          {expanded ? <ChevronDown className="w-4 h-4 theme-text-muted" /> : <ChevronRight className="w-4 h-4 theme-text-muted" />}
        </div>
      </div>
      
      {expanded && (
        <div className="mt-3 pt-3 border-t border-slate-600/30 space-y-2">
          <p className="text-xs theme-text-muted">{handoff.description}</p>
          <div className="flex gap-4 text-xs">
            <div>
              <span className="theme-text-muted">Tool: </span>
              <code className="px-1 py-0.5 bg-slate-700/50 rounded text-xs">{handoff.toolName}</code>
            </div>
            {handoff.bidirectional && (
              <div className="flex items-center gap-1 text-amber-400">
                <ArrowRight className="w-3 h-3" />
                <span>Bidirectional</span>
              </div>
            )}
          </div>
          <div className="grid grid-cols-2 gap-2 text-xs">
            <div>
              <span className="theme-text-muted">Inputs: </span>
              <span className="theme-text">{handoff.requiredInputs.join(', ')}</span>
            </div>
            <div>
              <span className="theme-text-muted">Outputs: </span>
              <span className="theme-text">{handoff.expectedOutputs.join(', ')}</span>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

function NetworkDiagram({ handoffs, selectedCategory }: { handoffs: HandoffDefinition[]; selectedCategory: string | null }) {
  const filteredHandoffs = selectedCategory 
    ? handoffs.filter(h => h.category === selectedCategory)
    : handoffs;
  
  // Get unique agents
  const agents = useMemo(() => {
    const agentSet = new Set<string>();
    filteredHandoffs.forEach(h => {
      agentSet.add(h.sourceAgent);
      agentSet.add(h.targetAgent);
    });
    return Array.from(agentSet);
  }, [filteredHandoffs]);
  
  // Calculate positions in a circle
  const agentPositions = useMemo(() => {
    const positions: Record<string, { x: number; y: number }> = {};
    const centerX = 400;
    const centerY = 300;
    const radius = 250;
    
    agents.forEach((agent, index) => {
      const angle = (2 * Math.PI * index) / agents.length - Math.PI / 2;
      positions[agent] = {
        x: centerX + radius * Math.cos(angle),
        y: centerY + radius * Math.sin(angle),
      };
    });
    
    return positions;
  }, [agents]);
  
  const getCategoryColor = (categoryId: string): string => {
    const cat = WORKFLOW_CATEGORIES.find(c => c.id === categoryId);
    return cat?.color.replace('text-', '') || 'slate-400';
  };
  
  return (
    <div className="w-full h-[600px] bg-slate-900/50 rounded-lg border theme-border overflow-hidden">
      <svg width="100%" height="100%" viewBox="0 0 800 600" preserveAspectRatio="xMidYMid meet">
        <defs>
          <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
            <polygon points="0 0, 10 3.5, 0 7" fill="currentColor" className="text-slate-400" />
          </marker>
          {WORKFLOW_CATEGORIES.map(cat => (
            <marker 
              key={cat.id}
              id={`arrowhead-${cat.id}`} 
              markerWidth="10" 
              markerHeight="7" 
              refX="9" 
              refY="3.5" 
              orient="auto"
            >
              <polygon points="0 0, 10 3.5, 0 7" className={cat.color} fill="currentColor" />
            </marker>
          ))}
        </defs>
        
        {/* Draw edges */}
        {filteredHandoffs.map((handoff, index) => {
          const source = agentPositions[handoff.sourceAgent];
          const target = agentPositions[handoff.targetAgent];
          if (!source || !target) return null;
          
          // Calculate control point for curved lines
          const midX = (source.x + target.x) / 2;
          const midY = (source.y + target.y) / 2;
          const dx = target.x - source.x;
          const dy = target.y - source.y;
          const offset = 30 + (index % 3) * 15;
          const controlX = midX - dy * 0.2 + (index % 2 === 0 ? offset : -offset);
          const controlY = midY + dx * 0.2;
          
          const colorClass = getCategoryColor(handoff.category);
          
          return (
            <g key={`${handoff.toolName}-${index}`}>
              <path
                d={`M ${source.x} ${source.y} Q ${controlX} ${controlY} ${target.x} ${target.y}`}
                fill="none"
                stroke={`var(--${colorClass})`}
                strokeWidth="1.5"
                strokeOpacity="0.6"
                markerEnd={`url(#arrowhead-${handoff.category})`}
                className={`stroke-current ${WORKFLOW_CATEGORIES.find(c => c.id === handoff.category)?.color || 'text-slate-400'}`}
              />
            </g>
          );
        })}
        
        {/* Draw nodes */}
        {agents.map((agent) => {
          const pos = agentPositions[agent];
          if (!pos) return null;
          
          return (
            <g key={agent} transform={`translate(${pos.x}, ${pos.y})`}>
              <circle
                r="35"
                fill="rgb(30, 41, 59)"
                stroke="rgb(71, 85, 105)"
                strokeWidth="2"
              />
              <text
                textAnchor="middle"
                dy="-45"
                className="fill-slate-300 text-[10px] font-medium"
              >
                {getAgentShortName(agent)}
              </text>
              <foreignObject x="-12" y="-12" width="24" height="24">
                <div className="flex items-center justify-center w-full h-full text-slate-300">
                  {AGENT_ICONS[agent] || <Users className="w-5 h-5" />}
                </div>
              </foreignObject>
            </g>
          );
        })}
      </svg>
    </div>
  );
}

export default function AgentWorkflowsPage() {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null);
  const [viewMode, setViewMode] = useState<'diagram' | 'list'>('diagram');
  
  const filteredHandoffs = useMemo(() => {
    let result = HANDOFF_REGISTRY;
    
    if (selectedCategory) {
      result = result.filter(h => h.category === selectedCategory);
    }
    
    if (searchQuery) {
      const query = searchQuery.toLowerCase();
      result = result.filter(h => 
        h.name.toLowerCase().includes(query) ||
        h.sourceAgent.toLowerCase().includes(query) ||
        h.targetAgent.toLowerCase().includes(query) ||
        h.toolName.toLowerCase().includes(query)
      );
    }
    
    return result;
  }, [selectedCategory, searchQuery]);
  
  const stats = useMemo(() => {
    const byCategory: Record<string, number> = {};
    const sourceAgents = new Set<string>();
    const targetAgents = new Set<string>();
    
    HANDOFF_REGISTRY.forEach(h => {
      byCategory[h.category] = (byCategory[h.category] || 0) + 1;
      sourceAgents.add(h.sourceAgent);
      targetAgents.add(h.targetAgent);
    });
    
    return {
      total: HANDOFF_REGISTRY.length,
      byCategory,
      uniqueSourceAgents: sourceAgents.size,
      uniqueTargetAgents: targetAgents.size,
      passed: HANDOFF_REGISTRY.filter(h => h.validationStatus === 'passed').length,
    };
  }, []);
  
  return (
    <div className="space-y-6 p-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold theme-text flex items-center gap-3">
            <Network className="w-7 h-7 text-alpha-500" />
            Agent Workflow Handoffs
          </h1>
          <p className="theme-text-muted mt-1">
            Visualization of all agent collaboration patterns and workflow handoffs
          </p>
        </div>
        <div className="flex items-center gap-2">
          <Button variant="outline" size="sm" className="gap-2">
            <RefreshCw className="w-4 h-4" />
            Validate All
          </Button>
          <Button variant="outline" size="sm" className="gap-2">
            <Download className="w-4 h-4" />
            Export
          </Button>
        </div>
      </div>
      
      {/* Stats Cards */}
      <div className="grid grid-cols-5 gap-4">
        <Card className="theme-card">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm theme-text-muted">Total Handoffs</p>
                <p className="text-2xl font-bold theme-text">{stats.total}</p>
              </div>
              <Network className="w-8 h-8 text-alpha-500" />
            </div>
          </CardContent>
        </Card>
        <Card className="theme-card">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm theme-text-muted">Categories</p>
                <p className="text-2xl font-bold theme-text">{Object.keys(stats.byCategory).length}</p>
              </div>
              <Filter className="w-8 h-8 text-purple-400" />
            </div>
          </CardContent>
        </Card>
        <Card className="theme-card">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm theme-text-muted">Source Agents</p>
                <p className="text-2xl font-bold theme-text">{stats.uniqueSourceAgents}</p>
              </div>
              <Users className="w-8 h-8 text-cyan-400" />
            </div>
          </CardContent>
        </Card>
        <Card className="theme-card">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm theme-text-muted">Target Agents</p>
                <p className="text-2xl font-bold theme-text">{stats.uniqueTargetAgents}</p>
              </div>
              <Users className="w-8 h-8 text-green-400" />
            </div>
          </CardContent>
        </Card>
        <Card className="theme-card">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm theme-text-muted">Validation</p>
                <p className="text-2xl font-bold text-green-400">{stats.passed}/{stats.total}</p>
              </div>
              <CheckCircle className="w-8 h-8 text-green-400" />
            </div>
          </CardContent>
        </Card>
      </div>
      
      {/* Filters & Controls */}
      <Card className="theme-card">
        <CardContent className="p-4">
          <div className="flex items-center justify-between gap-4">
            <div className="flex items-center gap-2 flex-1">
              <div className="relative flex-1 max-w-md">
                <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 theme-text-muted" />
                <input
                  type="text"
                  placeholder="Search handoffs, agents, or tools..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full pl-10 pr-4 py-2 bg-slate-800/50 border border-slate-600/30 rounded-lg text-sm theme-text placeholder-slate-500 focus:outline-none focus:border-alpha-500"
                />
              </div>
              <select
                value={selectedCategory || ''}
                onChange={(e) => setSelectedCategory(e.target.value || null)}
                className="px-3 py-2 bg-slate-800/50 border border-slate-600/30 rounded-lg text-sm theme-text focus:outline-none focus:border-alpha-500"
              >
                <option value="">All Categories</option>
                {WORKFLOW_CATEGORIES.map(cat => (
                  <option key={cat.id} value={cat.id}>{cat.name}</option>
                ))}
              </select>
            </div>
            <div className="flex items-center gap-2 border-l border-slate-600/30 pl-4">
              <Button
                variant={viewMode === 'diagram' ? 'primary' : 'outline'}
                size="sm"
                onClick={() => setViewMode('diagram')}
              >
                <Network className="w-4 h-4 mr-1" />
                Diagram
              </Button>
              <Button
                variant={viewMode === 'list' ? 'primary' : 'outline'}
                size="sm"
                onClick={() => setViewMode('list')}
              >
                <ClipboardList className="w-4 h-4 mr-1" />
                List
              </Button>
            </div>
          </div>
        </CardContent>
      </Card>
      
      {/* Category Legend */}
      <div className="flex flex-wrap gap-2">
        {WORKFLOW_CATEGORIES.map(cat => (
          <button
            key={cat.id}
            onClick={() => setSelectedCategory(selectedCategory === cat.id ? null : cat.id)}
            className={cn(
              "px-3 py-1.5 rounded-full text-xs font-medium transition-all",
              cat.bgColor, cat.borderColor, "border",
              selectedCategory === cat.id ? "ring-2 ring-white/30" : "",
              cat.color
            )}
          >
            {cat.name} ({stats.byCategory[cat.id] || 0})
          </button>
        ))}
      </div>
      
      {/* Main Content */}
      {viewMode === 'diagram' ? (
        <Card className="theme-card">
          <CardHeader>
            <CardTitle className="flex items-center justify-between">
              <span>Workflow Diagram</span>
              <div className="flex items-center gap-2">
                <Button variant="ghost" size="sm"><ZoomOut className="w-4 h-4" /></Button>
                <Button variant="ghost" size="sm"><ZoomIn className="w-4 h-4" /></Button>
                <Button variant="ghost" size="sm"><Maximize2 className="w-4 h-4" /></Button>
              </div>
            </CardTitle>
          </CardHeader>
          <CardContent>
            <NetworkDiagram handoffs={filteredHandoffs} selectedCategory={selectedCategory} />
            <div className="mt-4 p-3 bg-slate-800/30 rounded-lg">
              <div className="flex items-center gap-2 text-xs theme-text-muted">
                <Info className="w-4 h-4" />
                <span>
                  Showing {filteredHandoffs.length} handoffs between {new Set([...filteredHandoffs.map(h => h.sourceAgent), ...filteredHandoffs.map(h => h.targetAgent)]).size} agents.
                  {selectedCategory && ` Filtered by: ${WORKFLOW_CATEGORIES.find(c => c.id === selectedCategory)?.name}`}
                </span>
              </div>
            </div>
          </CardContent>
        </Card>
      ) : (
        <div className="space-y-4">
          {WORKFLOW_CATEGORIES.filter(cat => !selectedCategory || cat.id === selectedCategory).map(category => {
            const categoryHandoffs = filteredHandoffs.filter(h => h.category === category.id);
            if (categoryHandoffs.length === 0) return null;
            
            return (
              <Card key={category.id} className="theme-card">
                <CardHeader>
                  <CardTitle className={cn("flex items-center gap-2", category.color)}>
                    <div className={cn("w-3 h-3 rounded-full", category.bgColor, "border", category.borderColor)} />
                    {category.name}
                    <span className="text-sm font-normal theme-text-muted">({categoryHandoffs.length} handoffs)</span>
                  </CardTitle>
                </CardHeader>
                <CardContent className="space-y-2">
                  {categoryHandoffs.map((handoff) => (
                    <HandoffCard key={handoff.toolName} handoff={handoff} category={category} />
                  ))}
                </CardContent>
              </Card>
            );
          })}
        </div>
      )}
    </div>
  );
}
