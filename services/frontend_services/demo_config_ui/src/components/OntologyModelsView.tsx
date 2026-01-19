import { useState, useEffect } from 'react';
import {
  ChevronDown,
  ChevronRight,
  RefreshCw,
  Layers,
  BarChart3,
  Database,
  Building2,
  Settings,
  User,
  Link2,
  Code,
} from 'lucide-react';
import { cn } from '../lib/utils';
import { Card } from './ui/Card';
import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8090/api/v1/metadata';

interface ModelField {
  name: string;
  type: string;
  required: boolean;
  description?: string;
  default?: string;
}

interface OntologyModel {
  kind: string;
  name: string;
  description: string;
  parent?: string;
  fields: ModelField[];
  instanceCount?: number;
}

interface OntologyModelsViewProps {
  onSnackbar?: (message: string, severity: 'success' | 'error') => void;
}

const ONTOLOGY_MODELS: OntologyModel[] = [
  {
    kind: 'node_definition',
    name: 'NodeDefinition',
    description: 'Base ontology class for all node definitions in the knowledge graph',
    fields: [
      { name: 'id', type: 'string', required: false, description: 'Unique identifier' },
      { name: 'kind', type: 'string', required: true, description: 'Type discriminator' },
      { name: 'name', type: 'string', required: true, description: 'Display name' },
      { name: 'description', type: 'string', required: false, description: 'Description' },
      { name: 'metadata_', type: 'object', required: false, description: 'Additional metadata' },
    ]
  },
  {
    kind: 'entity_definition',
    name: 'EntityDefinition',
    description: 'Business entity/object model definition (data/noun)',
    parent: 'NodeDefinition',
    fields: [
      { name: 'code', type: 'string', required: true, description: 'Unique code identifier' },
      { name: 'table_schema', type: 'TableSchemaDefinition', required: false, description: 'Database table schema' },
      { name: 'schema_definition', type: 'string', required: false, description: 'UML/graph snippet' },
    ]
  },
  {
    kind: 'process_definition',
    name: 'ProcessDefinition',
    description: 'Base class for all process/workflow definitions (action/verb)',
    parent: 'NodeDefinition',
    fields: [
      { name: 'code', type: 'string', required: true, description: 'Unique code identifier' },
      { name: 'process_type', type: 'string', required: false, description: 'Type: value_chain, business_process, workflow' },
      { name: 'graph_pattern', type: 'GraphPatternDefinition', required: false, description: 'Graph pattern for process flow' },
      { name: 'associated_metrics', type: 'string[]', required: false, description: 'Associated metric codes' },
      { name: 'business_purpose', type: 'string', required: false, description: 'Business purpose' },
      { name: 'intended_value', type: 'string', required: false, description: 'Intended value' },
    ]
  },
  {
    kind: 'metric_definition',
    name: 'MetricDefinition',
    description: 'KPI/Metric definition with aggregation and time period support',
    parent: 'NodeDefinition',
    fields: [
      { name: 'code', type: 'string', required: true, description: 'Unique code identifier' },
      { name: 'category', type: 'string', required: false, description: 'Metric category' },
      { name: 'modules', type: 'string[]', required: false, description: 'Associated modules' },
      { name: 'required_objects', type: 'string[]', required: false, description: 'Required entity codes' },
      { name: 'formula', type: 'string', required: false, description: 'Natural language formula' },
      { name: 'math_expression', type: 'string', required: false, description: 'Parsed mathematical expression' },
      { name: 'unit', type: 'string', required: false, description: 'Unit of measure' },
      { name: 'data_type', type: 'string', required: false, default: 'decimal', description: 'Data type' },
      { name: 'aggregation_methods', type: 'string[]', required: false, description: 'Available aggregations' },
      { name: 'time_periods', type: 'string[]', required: false, description: 'Available time periods' },
      { name: 'dimensions', type: 'string[]', required: false, description: 'Available dimensions' },
    ]
  },
  {
    kind: 'value_chain_pattern_definition',
    name: 'ValueChainPatternDefinition',
    description: 'Value chain pattern at any granularity level',
    parent: 'ProcessDefinition',
    fields: [
      { name: 'domain', type: 'string', required: false, description: 'Granularity: company, industry, module, process' },
      { name: 'applicability', type: 'object', required: false, description: 'Applicability rules' },
      { name: 'dimension_bindings', type: 'DimensionBinding[]', required: false, description: 'Dimension bindings' },
    ]
  },
  {
    kind: 'business_process_definition',
    name: 'BusinessProcessDefinition',
    description: 'Business process - low-level value chain pattern with execution details',
    parent: 'ValueChainPatternDefinition',
    fields: [
      { name: 'performed_by_actors', type: 'string[]', required: false, description: 'Actor codes' },
      { name: 'uses_entities', type: 'string[]', required: false, description: 'Entity codes used' },
      { name: 'produces_event_types', type: 'string[]', required: false, description: 'Event types produced' },
    ]
  },
  {
    kind: 'edge_definition',
    name: 'EdgeDefinition',
    description: 'Edge (relationship) between nodes in the knowledge graph',
    fields: [
      { name: 'id', type: 'string', required: false, description: 'Unique identifier' },
      { name: 'from_entity', type: 'string', required: true, description: 'Source node code' },
      { name: 'to_entity', type: 'string', required: true, description: 'Target node code' },
      { name: 'relationship_type', type: 'string', required: true, description: 'Type of edge/relationship' },
      { name: 'from_cardinality', type: 'string', required: false, description: 'Source cardinality' },
      { name: 'to_cardinality', type: 'string', required: false, description: 'Target cardinality' },
    ]
  },
  {
    kind: 'actor_definition',
    name: 'ActorDefinition',
    description: 'Actors that perform actions and participate in processes',
    parent: 'NodeDefinition',
    fields: [
      { name: 'code', type: 'string', required: true, description: 'Unique code identifier' },
      { name: 'actor_type', type: 'string', required: true, description: 'Type: person, role, organization, system' },
      { name: 'responsibilities', type: 'string[]', required: false, description: 'Actor responsibilities' },
      { name: 'permissions', type: 'string[]', required: false, description: 'Permission codes' },
    ]
  },
  {
    kind: 'value_set_definition',
    name: 'ValueSetDefinition',
    description: 'Enumerated set of valid codes',
    parent: 'NodeDefinition',
    fields: [
      { name: 'codes', type: 'string[]', required: true, description: 'List of valid codes' },
    ]
  },
  {
    kind: 'code_system_definition',
    name: 'CodeSystemDefinition',
    description: 'Code system with code-to-label mappings',
    parent: 'NodeDefinition',
    fields: [
      { name: 'codes', type: 'object', required: false, description: 'Map of code to label' },
    ]
  },
  {
    kind: 'constraint_definition',
    name: 'ConstraintDefinition',
    description: 'Validation constraint for entities',
    parent: 'NodeDefinition',
    fields: [
      { name: 'target_entity', type: 'string', required: true, description: 'Entity to constrain' },
      { name: 'constraint_type', type: 'string', required: true, description: 'Type of constraint' },
      { name: 'expression', type: 'string', required: true, description: 'Constraint expression' },
      { name: 'error_message', type: 'string', required: false, description: 'Error message' },
    ]
  },
];

const MODEL_ICONS: Record<string, { icon: React.ReactNode; color: string }> = {
  'node_definition': { icon: <Layers className="w-4 h-4" />, color: 'text-gray-400' },
  'entity_definition': { icon: <Database className="w-4 h-4" />, color: 'text-purple-500' },
  'process_definition': { icon: <Settings className="w-4 h-4" />, color: 'text-cyan-500' },
  'metric_definition': { icon: <BarChart3 className="w-4 h-4" />, color: 'text-amber-500' },
  'value_chain_pattern_definition': { icon: <Building2 className="w-4 h-4" />, color: 'text-green-500' },
  'business_process_definition': { icon: <Settings className="w-4 h-4" />, color: 'text-blue-500' },
  'edge_definition': { icon: <Link2 className="w-4 h-4" />, color: 'text-slate-500' },
  'actor_definition': { icon: <User className="w-4 h-4" />, color: 'text-pink-500' },
  'value_set_definition': { icon: <Code className="w-4 h-4" />, color: 'text-amber-700' },
  'code_system_definition': { icon: <Code className="w-4 h-4" />, color: 'text-amber-700' },
  'constraint_definition': { icon: <Code className="w-4 h-4" />, color: 'text-red-500' },
};

export default function OntologyModelsView({ onSnackbar }: OntologyModelsViewProps) {
  const [expandedModels, setExpandedModels] = useState<Set<string>>(new Set(['node_definition']));
  const [selectedModel, setSelectedModel] = useState<OntologyModel | null>(null);
  const [instanceCounts, setInstanceCounts] = useState<Record<string, number>>({});
  const [loading, setLoading] = useState(true);

  useEffect(() => { fetchInstanceCounts(); }, []);

  const fetchInstanceCounts = async () => {
    setLoading(true);
    try {
      const kinds = ['entity_definition', 'metric_definition', 'value_chain_pattern_definition', 'business_process_definition', 'actor_definition', 'value_set_definition', 'code_system_definition'];
      const counts: Record<string, number> = {};
      await Promise.all(kinds.map(async (kind) => {
        try {
          const response = await axios.get(`${BASE_URL}/definitions/${kind}`, { params: { limit: 1000 } });
          counts[kind] = response.data?.length || 0;
        } catch { counts[kind] = 0; }
      }));
      try {
        const relResponse = await axios.get(`${BASE_URL}/relationships`);
        counts['relationship_definition'] = relResponse.data?.length || 0;
      } catch { counts['relationship_definition'] = 0; }
      setInstanceCounts(counts);
    } catch (err) {
      console.error('Failed to fetch instance counts:', err);
      onSnackbar?.('Failed to fetch instance counts', 'error');
    } finally { setLoading(false); }
  };

  const toggleModel = (kind: string) => {
    setExpandedModels(prev => {
      const next = new Set(prev);
      if (next.has(kind)) next.delete(kind);
      else next.add(kind);
      return next;
    });
  };

  const buildModelTree = () => {
    const rootModels = ONTOLOGY_MODELS.filter(m => !m.parent);
    const childrenMap = new Map<string, OntologyModel[]>();
    ONTOLOGY_MODELS.forEach(model => {
      if (model.parent) {
        const parentKind = ONTOLOGY_MODELS.find(m => m.name === model.parent)?.kind || model.parent.toLowerCase().replace(/([A-Z])/g, '_$1').slice(1) + '_definition';
        const children = childrenMap.get(parentKind) || [];
        children.push(model);
        childrenMap.set(parentKind, children);
      }
    });
    return { rootModels, childrenMap };
  };

  const getIcon = (kind: string) => {
    const config = MODEL_ICONS[kind] || { icon: <Layers className="w-4 h-4" />, color: 'theme-text-muted' };
    return <span className={config.color}>{config.icon}</span>;
  };

  const renderModelNode = (model: OntologyModel, depth: number = 0, childrenMap: Map<string, OntologyModel[]>) => {
    const children = childrenMap.get(model.kind) || [];
    const hasChildren = children.length > 0;
    const isExpanded = expandedModels.has(model.kind);
    const isSelected = selectedModel?.kind === model.kind;
    const count = instanceCounts[model.kind];

    return (
      <div key={model.kind}>
        <div
          className={cn(
            "flex items-center py-2 px-2 cursor-pointer transition-colors hover:bg-alpha-faded-50 dark:hover:bg-alpha-faded-900",
            isSelected && "bg-alpha-500/10 border-l-2 border-l-alpha-500"
          )}
          style={{ paddingLeft: `${depth * 24 + 8}px` }}
          onClick={() => setSelectedModel(model)}
        >
          <div className="w-7 flex-shrink-0">
            {hasChildren ? (
              <button onClick={(e) => { e.stopPropagation(); toggleModel(model.kind); }} className="p-0.5 hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 rounded">
                {isExpanded ? <ChevronDown className="w-4 h-4 theme-text-muted" /> : <ChevronRight className="w-4 h-4 theme-text-muted" />}
              </button>
            ) : null}
          </div>
          <div className="w-6 flex-shrink-0">{getIcon(model.kind)}</div>
          <div className="flex-1 min-w-0 flex items-center gap-2">
            <span className={cn("text-sm truncate", isSelected ? "font-semibold theme-text-title" : "theme-text")}>{model.name}</span>
            {count !== undefined && count > 0 && (
              <span className="px-1.5 py-0.5 rounded text-[10px] bg-alpha-500/20 text-alpha-400 border border-alpha-500/30">{count}</span>
            )}
          </div>
        </div>
        {hasChildren && isExpanded && (
          <div>{children.map(child => renderModelNode(child, depth + 1, childrenMap))}</div>
        )}
      </div>
    );
  };

  const renderDetailsPanel = () => {
    if (!selectedModel) {
      return <div className="p-4 text-center theme-text-muted">Select a model to view its schema</div>;
    }
    const count = instanceCounts[selectedModel.kind];

    return (
      <div className="p-4 space-y-4">
        <div className="flex items-center gap-2">
          {getIcon(selectedModel.kind)}
          <h3 className="font-semibold theme-text-title flex-1">{selectedModel.name}</h3>
          {count !== undefined && (
            <span className="px-2 py-0.5 rounded-full text-xs bg-alpha-500/20 text-alpha-400">{count} instances</span>
          )}
        </div>
        <p className="text-sm theme-text-muted">{selectedModel.description}</p>
        {selectedModel.parent && (
          <span className="inline-block px-2 py-0.5 rounded-full text-xs border border-purple-500/30 text-purple-400">Extends: {selectedModel.parent}</span>
        )}
        <div className="border-t theme-border pt-4">
          <p className="text-sm font-semibold theme-text-title mb-2">Fields</p>
          <div className="space-y-2">
            {selectedModel.fields.map(field => (
              <div key={field.name} className="p-3 rounded-lg border theme-border theme-card-bg">
                <div className="flex items-center gap-2 mb-1">
                  <span className="font-mono text-sm font-semibold theme-text">{field.name}</span>
                  <span className="px-1.5 py-0.5 rounded text-[10px] theme-card-bg border theme-border theme-text-muted">{field.type}</span>
                  {field.required && (
                    <span className="px-1.5 py-0.5 rounded text-[10px] bg-red-500/20 text-red-400 border border-red-500/30">required</span>
                  )}
                </div>
                {field.description && <p className="text-xs theme-text-muted">{field.description}</p>}
                {field.default && <p className="text-xs theme-text-muted">Default: {field.default}</p>}
              </div>
            ))}
          </div>
          {selectedModel.parent && (
            <p className="text-xs theme-text-muted mt-3">+ Inherits all fields from {selectedModel.parent}</p>
          )}
        </div>
      </div>
    );
  };

  const { rootModels, childrenMap } = buildModelTree();

  if (loading) {
    return (
      <div className="flex items-center justify-center p-8">
        <RefreshCw className="w-5 h-5 text-alpha-500 animate-spin mr-2" />
        <span className="theme-text-muted">Loading models...</span>
      </div>
    );
  }

  return (
    <div className="flex gap-4 h-full">
      {/* Tree Panel */}
      <Card className="flex-[2] overflow-hidden flex flex-col max-h-[600px]">
        <div className="p-3 flex items-center justify-between border-b theme-border">
          <h3 className="font-semibold theme-text-title">Ontology Model Types</h3>
          <button onClick={fetchInstanceCounts} className="p-1.5 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800" title="Refresh counts">
            <RefreshCw className="w-4 h-4 theme-text-muted" />
          </button>
        </div>
        <div className="flex-1 overflow-auto">
          {rootModels.length === 0 ? (
            <div className="p-4">
              <div className="p-3 rounded-lg bg-blue-500/10 border border-blue-500/30 text-blue-400 text-sm">No models defined.</div>
            </div>
          ) : (
            <div>{rootModels.map(model => renderModelNode(model, 0, childrenMap))}</div>
          )}
        </div>
      </Card>

      {/* Details Panel */}
      <Card className="flex-1 min-w-[350px] max-h-[600px] overflow-auto">
        <div className="p-3 border-b theme-border">
          <h3 className="font-semibold theme-text-title">Model Schema</h3>
        </div>
        {renderDetailsPanel()}
      </Card>
    </div>
  );
}
