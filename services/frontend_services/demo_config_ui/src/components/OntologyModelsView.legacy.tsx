import { useState, useEffect } from 'react';
import {
  Box,
  Typography,
  IconButton,
  Collapse,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Paper,
  Divider,
  Chip,
  Tooltip,
  Alert
} from '@mui/material';
import {
  ExpandMore as ExpandMoreIcon,
  ChevronRight as ChevronRightIcon,
  Refresh as RefreshIcon,
  Category as CategoryIcon,
  Assessment as MetricIcon,
  Storage as EntityIcon,
  Business as ValueChainIcon,
  Settings as ProcessIcon,
  Person as ActorIcon,
  Link as RelationshipIcon,
  Code as CodeIcon
} from '@mui/icons-material';
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

// Define the ontology model hierarchy based on ontology_models.py
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

const MODEL_ICONS: Record<string, JSX.Element> = {
  'node_definition': <CategoryIcon />,
  'entity_definition': <EntityIcon sx={{ color: '#9c27b0' }} />,
  'process_definition': <ProcessIcon sx={{ color: '#00bcd4' }} />,
  'metric_definition': <MetricIcon sx={{ color: '#ff9800' }} />,
  'value_chain_pattern_definition': <ValueChainIcon sx={{ color: '#4caf50' }} />,
  'business_process_definition': <ProcessIcon sx={{ color: '#2196f3' }} />,
  'edge_definition': <RelationshipIcon sx={{ color: '#607d8b' }} />,
  'actor_definition': <ActorIcon sx={{ color: '#e91e63' }} />,
  'value_set_definition': <CodeIcon sx={{ color: '#795548' }} />,
  'code_system_definition': <CodeIcon sx={{ color: '#795548' }} />,
  'constraint_definition': <CodeIcon sx={{ color: '#f44336' }} />,
};

export default function OntologyModelsView({ onSnackbar }: OntologyModelsViewProps) {
  const [expandedModels, setExpandedModels] = useState<Set<string>>(new Set(['node_definition']));
  const [selectedModel, setSelectedModel] = useState<OntologyModel | null>(null);
  const [instanceCounts, setInstanceCounts] = useState<Record<string, number>>({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchInstanceCounts();
  }, []);

  const fetchInstanceCounts = async () => {
    setLoading(true);
    try {
      const kinds = [
        'entity_definition',
        'metric_definition', 
        'value_chain_pattern_definition',
        'business_process_definition',
        'actor_definition',
        'value_set_definition',
        'code_system_definition',
      ];
      
      const counts: Record<string, number> = {};
      
      await Promise.all(kinds.map(async (kind) => {
        try {
          const response = await axios.get(`${BASE_URL}/definitions/${kind}`, { params: { limit: 1000 } });
          counts[kind] = response.data?.length || 0;
        } catch {
          counts[kind] = 0;
        }
      }));
      
      // Get relationship count
      try {
        const relResponse = await axios.get(`${BASE_URL}/relationships`);
        counts['relationship_definition'] = relResponse.data?.length || 0;
      } catch {
        counts['relationship_definition'] = 0;
      }
      
      setInstanceCounts(counts);
    } catch (err) {
      console.error('Failed to fetch instance counts:', err);
      onSnackbar?.('Failed to fetch instance counts', 'error');
    } finally {
      setLoading(false);
    }
  };

  const toggleModel = (kind: string) => {
    setExpandedModels(prev => {
      const next = new Set(prev);
      if (next.has(kind)) {
        next.delete(kind);
      } else {
        next.add(kind);
      }
      return next;
    });
  };

  const handleModelClick = (model: OntologyModel) => {
    setSelectedModel(model);
  };

  // Build hierarchy tree
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

  const renderModelNode = (model: OntologyModel, depth: number = 0, childrenMap: Map<string, OntologyModel[]>) => {
    const children = childrenMap.get(model.kind) || [];
    const hasChildren = children.length > 0;
    const isExpanded = expandedModels.has(model.kind);
    const isSelected = selectedModel?.kind === model.kind;
    const count = instanceCounts[model.kind];

    return (
      <Box key={model.kind}>
        <ListItem
          sx={{
            pl: depth * 3,
            backgroundColor: isSelected ? 'action.selected' : 'transparent',
            '&:hover': { backgroundColor: 'action.hover' },
            cursor: 'pointer',
            borderLeft: `3px solid ${isSelected ? '#1976d2' : 'transparent'}`,
          }}
          onClick={() => handleModelClick(model)}
        >
          <ListItemIcon sx={{ minWidth: 32 }}>
            {hasChildren ? (
              <IconButton size="small" onClick={(e) => { e.stopPropagation(); toggleModel(model.kind); }}>
                {isExpanded ? <ExpandMoreIcon /> : <ChevronRightIcon />}
              </IconButton>
            ) : (
              <Box sx={{ width: 32 }} />
            )}
          </ListItemIcon>
          <ListItemIcon sx={{ minWidth: 32 }}>
            {MODEL_ICONS[model.kind] || <CategoryIcon />}
          </ListItemIcon>
          <ListItemText
            primary={
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                <Typography variant="body2" fontWeight={isSelected ? 600 : 400}>
                  {model.name}
                </Typography>
                {count !== undefined && count > 0 && (
                  <Chip 
                    label={count} 
                    size="small" 
                    color="primary"
                    variant="outlined"
                    sx={{ fontSize: '0.65rem', height: 18 }}
                  />
                )}
              </Box>
            }
            secondary={model.description.substring(0, 50) + (model.description.length > 50 ? '...' : '')}
          />
        </ListItem>
        {hasChildren && (
          <Collapse in={isExpanded}>
            {children.map(child => renderModelNode(child, depth + 1, childrenMap))}
          </Collapse>
        )}
      </Box>
    );
  };

  const renderDetailsPanel = () => {
    if (!selectedModel) {
      return (
        <Box sx={{ p: 2, textAlign: 'center', color: 'text.secondary' }}>
          <Typography>Select a model to view its schema</Typography>
        </Box>
      );
    }

    const count = instanceCounts[selectedModel.kind];

    return (
      <Box sx={{ p: 2 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 2 }}>
          {MODEL_ICONS[selectedModel.kind] || <CategoryIcon />}
          <Typography variant="h6">{selectedModel.name}</Typography>
          {count !== undefined && (
            <Chip label={`${count} instances`} size="small" color="primary" />
          )}
        </Box>
        
        <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
          {selectedModel.description}
        </Typography>
        
        {selectedModel.parent && (
          <Box sx={{ mb: 2 }}>
            <Chip 
              label={`Extends: ${selectedModel.parent}`} 
              size="small" 
              variant="outlined"
              color="secondary"
            />
          </Box>
        )}
        
        <Divider sx={{ mb: 2 }} />
        
        <Typography variant="subtitle2" sx={{ mb: 1 }}>Fields</Typography>
        
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
          {selectedModel.fields.map(field => (
            <Paper key={field.name} variant="outlined" sx={{ p: 1.5 }}>
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 0.5 }}>
                <Typography variant="body2" fontWeight={600} fontFamily="monospace">
                  {field.name}
                </Typography>
                <Chip 
                  label={field.type} 
                  size="small" 
                  sx={{ fontSize: '0.65rem', height: 18 }}
                />
                {field.required && (
                  <Chip 
                    label="required" 
                    size="small" 
                    color="error"
                    variant="outlined"
                    sx={{ fontSize: '0.65rem', height: 18 }}
                  />
                )}
              </Box>
              {field.description && (
                <Typography variant="caption" color="text.secondary">
                  {field.description}
                </Typography>
              )}
              {field.default && (
                <Typography variant="caption" color="text.secondary" display="block">
                  Default: {field.default}
                </Typography>
              )}
            </Paper>
          ))}
        </Box>
        
        {selectedModel.parent && (
          <Box sx={{ mt: 2 }}>
            <Typography variant="caption" color="text.secondary">
              + Inherits all fields from {selectedModel.parent}
            </Typography>
          </Box>
        )}
      </Box>
    );
  };

  const { rootModels, childrenMap } = buildModelTree();

  if (loading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', p: 4 }}>
        <Typography>Loading models...</Typography>
      </Box>
    );
  }

  return (
    <Box sx={{ display: 'flex', gap: 2, height: '100%' }}>
      {/* Tree Panel */}
      <Paper sx={{ flex: 2, overflow: 'auto', maxHeight: 600 }}>
        <Box sx={{ p: 1, display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: 1, borderColor: 'divider' }}>
          <Typography variant="subtitle1" fontWeight={600}>Ontology Model Types</Typography>
          <Tooltip title="Refresh counts">
            <IconButton size="small" onClick={fetchInstanceCounts}>
              <RefreshIcon />
            </IconButton>
          </Tooltip>
        </Box>
        
        {rootModels.length === 0 ? (
          <Box sx={{ p: 3, textAlign: 'center' }}>
            <Alert severity="info">No models defined.</Alert>
          </Box>
        ) : (
          <List dense disablePadding>
            {rootModels.map(model => renderModelNode(model, 0, childrenMap))}
          </List>
        )}
      </Paper>
      
      {/* Details Panel */}
      <Paper sx={{ flex: 1, minWidth: 350, maxHeight: 600, overflow: 'auto' }}>
        <Box sx={{ p: 1, borderBottom: 1, borderColor: 'divider' }}>
          <Typography variant="subtitle1" fontWeight={600}>Model Schema</Typography>
        </Box>
        {renderDetailsPanel()}
      </Paper>
    </Box>
  );
}
