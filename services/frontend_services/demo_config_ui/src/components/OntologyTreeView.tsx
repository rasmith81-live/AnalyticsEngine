import { useState, useEffect } from 'react';
import {
  Box,
  Typography,
  IconButton,
  TextField,
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Collapse,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  ListItemSecondaryAction,
  Chip,
  Tooltip,
  Paper,
  Divider,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Alert
} from '@mui/material';
import {
  ExpandMore as ExpandMoreIcon,
  ChevronRight as ChevronRightIcon,
  Add as AddIcon,
  Edit as EditIcon,
  Delete as DeleteIcon,
  Business as ValueChainIcon,
  Category as ModuleIcon,
  Assessment as KPIIcon,
  Storage as EntityIcon,
  Refresh as RefreshIcon
} from '@mui/icons-material';
import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8090/api/v1/metadata';

interface OntologyNode {
  code: string;
  name: string;
  kind: string;
  description?: string;
  children?: OntologyNode[];
  fields?: Record<string, any>;
}

interface Relationship {
  from_entity_code: string;
  to_entity_code: string;
  relationship_type: string;
}

interface OntologyTreeViewProps {
  onRefresh?: () => void;
  onSnackbar?: (message: string, severity: 'success' | 'error') => void;
}

const DEFINITION_KINDS = [
  { kind: 'value_chain_pattern_definition', label: 'Value Chain', icon: <ValueChainIcon /> },
  { kind: 'business_process_definition', label: 'Module/Process', icon: <ModuleIcon /> },
  { kind: 'metric_definition', label: 'KPI/Metric', icon: <KPIIcon /> },
  { kind: 'entity_definition', label: 'Entity', icon: <EntityIcon /> },
];

const KIND_COLORS: Record<string, string> = {
  'value_chain_pattern_definition': '#4caf50',
  'business_process_definition': '#2196f3',
  'metric_definition': '#ff9800',
  'entity_definition': '#9c27b0',
};

export default function OntologyTreeView({ onRefresh, onSnackbar }: OntologyTreeViewProps) {
  const [treeData, setTreeData] = useState<OntologyNode[]>([]);
  const [expandedNodes, setExpandedNodes] = useState<Set<string>>(new Set(['root', '_orphan_kpis', '_orphan_modules', '_entities']));
  const [selectedNode, setSelectedNode] = useState<OntologyNode | null>(null);
  const [loading, setLoading] = useState(true);
  
  // Dialog states
  const [editDialogOpen, setEditDialogOpen] = useState(false);
  const [addDialogOpen, setAddDialogOpen] = useState(false);
  const [deleteDialogOpen, setDeleteDialogOpen] = useState(false);
  const [dialogMode, setDialogMode] = useState<'add' | 'edit'>('add');
  const [parentForAdd, setParentForAdd] = useState<OntologyNode | null>(null);
  
  // Form state
  const [formData, setFormData] = useState({
    code: '',
    name: '',
    description: '',
    kind: 'value_chain_pattern_definition',
    process_type: 'core',
    formula: '',
    unit: '',
  });

  useEffect(() => {
    fetchOntologyData();
  }, []);

  const fetchOntologyData = async () => {
    setLoading(true);
    try {
      const [vcRes, modRes, kpiRes, entityRes, relRes] = await Promise.all([
        axios.get(`${BASE_URL}/definitions/value_chain_pattern_definition`, { params: { limit: 100 } }),
        axios.get(`${BASE_URL}/definitions/business_process_definition`, { params: { limit: 100 } }),
        axios.get(`${BASE_URL}/definitions/metric_definition`, { params: { limit: 100 } }).catch(() => ({ data: [] })),
        axios.get(`${BASE_URL}/definitions/entity_definition`, { params: { limit: 100 } }).catch(() => ({ data: [] })),
        axios.get(`${BASE_URL}/relationships`).catch(() => ({ data: [] }))
      ]);

      const valueChains = vcRes.data || [];
      const modules = modRes.data || [];
      const kpis = kpiRes.data || [];
      const entities = entityRes.data || [];
      const rels = relRes.data || [];
      
      // Build tree structure based on relationships
      const tree = buildTree(valueChains, modules, kpis, entities, rels);
      setTreeData(tree);
    } catch (err) {
      console.error('Failed to fetch ontology data:', err);
      onSnackbar?.('Failed to fetch ontology data', 'error');
    } finally {
      setLoading(false);
    }
  };

  const buildTree = (
    valueChains: any[],
    modules: any[],
    kpis: any[],
    entities: any[],
    relationships: Relationship[]
  ): OntologyNode[] => {
    // Create lookup maps (case-insensitive for matching)
    const modulesByCode = new Map(modules.map(m => [m.code.toLowerCase(), m]));
    const kpisByCode = new Map(kpis.map(k => [k.code.toLowerCase(), k]));
    const entitiesByCode = new Map(entities.map(e => [e.code.toLowerCase(), e]));
    
    // Build relationship maps (store original codes for display)
    const moduleToVC = new Map<string, string>();
    const kpiToModule = new Map<string, string>();
    const kpiToVC = new Map<string, string>();
    const entityToKpi = new Map<string, Set<string>>();
    const kpiToEntities = new Map<string, Set<string>>();
    
    // Build relationships based on existence, not type
    // Determine parent-child by checking what kind of entity is on each side
    // Use lowercase for comparison to handle mixed-case codes
    relationships.forEach(rel => {
      const fromLower = rel.from_entity_code.toLowerCase();
      const toLower = rel.to_entity_code.toLowerCase();
      const fromIsModule = modulesByCode.has(fromLower);
      const fromIsKpi = kpisByCode.has(fromLower);
      const toIsVC = valueChains.some(vc => vc.code.toLowerCase() === toLower);
      const toIsModule = modulesByCode.has(toLower);
      const toIsKpi = kpisByCode.has(toLower);
      
      // Module -> ValueChain relationship
      if (fromIsModule && toIsVC) {
        moduleToVC.set(fromLower, toLower);
      }
      // Module -> KPI relationship (module contains KPI)
      else if (fromIsModule && toIsKpi) {
        kpiToModule.set(toLower, fromLower);
      }
      // KPI -> Module relationship (KPI belongs to module)
      else if (fromIsKpi && toIsModule) {
        kpiToModule.set(fromLower, toLower);
      }
      // KPI -> ValueChain relationship (direct, no module)
      else if (fromIsKpi && toIsVC) {
        kpiToVC.set(fromLower, toLower);
      }
      // KPI -> Entity relationship
      else if (fromIsKpi && !toIsVC && !toIsModule && !toIsKpi) {
        if (!entityToKpi.has(toLower)) {
          entityToKpi.set(toLower, new Set());
        }
        entityToKpi.get(toLower)!.add(fromLower);
        
        // Also track entities per KPI (for adding entities as children of KPIs)
        if (!kpiToEntities.has(fromLower)) {
          kpiToEntities.set(fromLower, new Set());
        }
        kpiToEntities.get(fromLower)!.add(toLower);
      }
    });
    
    // Build tree nodes
    const tree: OntologyNode[] = [];
    
    // Value Chains as root nodes
    valueChains.forEach(vc => {
      const vcNode: OntologyNode = {
        code: vc.code,
        name: vc.name,
        kind: 'value_chain_pattern_definition',
        description: vc.description,
        fields: { domain: vc.domain },
        children: []
      };
      
      // Find modules belonging to this value chain
      modules.forEach(mod => {
        const modCodeLower = mod.code.toLowerCase();
        const vcCodeLower = vc.code.toLowerCase();
        if (moduleToVC.get(modCodeLower) === vcCodeLower) {
          const modNode: OntologyNode = {
            code: mod.code,
            name: mod.name,
            kind: 'business_process_definition',
            description: mod.description,
            fields: { process_type: mod.process_type },
            children: []
          };
          
          // Find KPIs belonging to this module
          kpis.forEach(kpi => {
            const kpiCodeLower = kpi.code.toLowerCase();
            if (kpiToModule.get(kpiCodeLower) === modCodeLower) {
              // Build entity children for this KPI
              const entityChildren: OntologyNode[] = [];
              const entityCodes = kpiToEntities.get(kpiCodeLower) || new Set<string>();
              entityCodes.forEach(entityCodeLower => {
                const entity = entitiesByCode.get(entityCodeLower);
                if (entity) {
                  entityChildren.push({
                    code: entity.code,
                    name: entity.name,
                    kind: 'entity_definition',
                    description: entity.description,
                    children: []
                  });
                }
              });
              
              const kpiNode: OntologyNode = {
                code: kpi.code,
                name: kpi.name,
                kind: 'metric_definition',
                description: kpi.description,
                fields: { 
                  formula: kpi.formula,
                  math_expression: kpi.math_expression,
                  unit: kpi.unit 
                },
                children: entityChildren
              };
              modNode.children!.push(kpiNode);
            }
          });
          
          vcNode.children!.push(modNode);
        }
      });
      
      // Find KPIs directly under value chain (not in a module)
      kpis.forEach(kpi => {
        const kpiCodeLower = kpi.code.toLowerCase();
        const vcCodeLower = vc.code.toLowerCase();
        if (kpiToVC.get(kpiCodeLower) === vcCodeLower && !kpiToModule.has(kpiCodeLower)) {
          // Build entity children for this KPI
          const entityChildren: OntologyNode[] = [];
          const entityCodes = kpiToEntities.get(kpiCodeLower) || new Set<string>();
          entityCodes.forEach(entityCodeLower => {
            const entity = entitiesByCode.get(entityCodeLower);
            if (entity) {
              entityChildren.push({
                code: entity.code,
                name: entity.name,
                kind: 'entity_definition',
                description: entity.description,
                children: []
              });
            }
          });
          
          const kpiNode: OntologyNode = {
            code: kpi.code,
            name: kpi.name,
            kind: 'metric_definition',
            description: kpi.description,
            fields: { 
              formula: kpi.formula,
              math_expression: kpi.math_expression,
              unit: kpi.unit 
            },
            children: entityChildren
          };
          vcNode.children!.push(kpiNode);
        }
      });
      
      tree.push(vcNode);
    });
    
    // Add orphan modules (not linked to any value chain)
    const orphanModules: OntologyNode[] = [];
    modules.forEach(mod => {
      const modCodeLower = mod.code.toLowerCase();
      if (!moduleToVC.has(modCodeLower)) {
        orphanModules.push({
          code: mod.code,
          name: mod.name,
          kind: 'business_process_definition',
          description: mod.description,
          fields: { process_type: mod.process_type },
          children: []
        });
      }
    });
    
    if (orphanModules.length > 0) {
      tree.push({
        code: '_orphan_modules',
        name: 'Unassigned Modules',
        kind: 'folder',
        children: orphanModules
      });
    }
    
    // Add orphan KPIs
    const orphanKpis: OntologyNode[] = [];
    kpis.forEach(kpi => {
      const kpiCodeLower = kpi.code.toLowerCase();
      if (!kpiToModule.has(kpiCodeLower) && !kpiToVC.has(kpiCodeLower)) {
        // Build entity children for this orphan KPI
        const entityChildren: OntologyNode[] = [];
        const entityCodes = kpiToEntities.get(kpiCodeLower) || new Set<string>();
        entityCodes.forEach(entityCodeLower => {
          const entity = entitiesByCode.get(entityCodeLower);
          if (entity) {
            entityChildren.push({
              code: entity.code,
              name: entity.name,
              kind: 'entity_definition',
              description: entity.description,
              children: []
            });
          }
        });
        
        orphanKpis.push({
          code: kpi.code,
          name: kpi.name,
          kind: 'metric_definition',
          description: kpi.description,
          fields: { formula: kpi.formula, unit: kpi.unit },
          children: entityChildren
        });
      }
    });
    
    if (orphanKpis.length > 0) {
      tree.push({
        code: '_orphan_kpis',
        name: 'Unassigned KPIs',
        kind: 'folder',
        children: orphanKpis
      });
    }
    
    // Add orphan entities section (entities not linked to any KPI)
    const orphanEntities = entities.filter(e => !entityToKpi.has(e.code.toLowerCase()));
    if (orphanEntities.length > 0) {
      tree.push({
        code: '_orphan_entities',
        name: 'Unassigned Entities',
        kind: 'folder',
        children: orphanEntities.map(e => ({
          code: e.code,
          name: e.name,
          kind: 'entity_definition',
          description: e.description,
          fields: e,
          children: []
        }))
      });
    }
    
    return tree;
  };

  const toggleNode = (code: string) => {
    setExpandedNodes(prev => {
      const next = new Set(prev);
      if (next.has(code)) {
        next.delete(code);
      } else {
        next.add(code);
      }
      return next;
    });
  };

  const handleNodeClick = (node: OntologyNode) => {
    setSelectedNode(node);
  };

  const handleAddClick = (parentNode?: OntologyNode) => {
    setParentForAdd(parentNode || null);
    setDialogMode('add');
    
    // Set default kind based on parent
    let defaultKind = 'value_chain_pattern_definition';
    if (parentNode) {
      if (parentNode.kind === 'value_chain_pattern_definition') {
        defaultKind = 'business_process_definition';
      } else if (parentNode.kind === 'business_process_definition') {
        defaultKind = 'metric_definition';
      }
    }
    
    setFormData({
      code: '',
      name: '',
      description: '',
      kind: defaultKind,
      process_type: 'core',
      formula: '',
      unit: '',
    });
    setAddDialogOpen(true);
  };

  const handleEditClick = (node: OntologyNode) => {
    setSelectedNode(node);
    setDialogMode('edit');
    setFormData({
      code: node.code,
      name: node.name,
      description: node.description || '',
      kind: node.kind,
      process_type: node.fields?.process_type || 'core',
      formula: node.fields?.formula || '',
      unit: node.fields?.unit || '',
    });
    setEditDialogOpen(true);
  };

  const handleDeleteClick = (node: OntologyNode) => {
    setSelectedNode(node);
    setDeleteDialogOpen(true);
  };

  const handleSave = async () => {
    try {
      const definition: any = {
        code: formData.code,
        name: formData.name,
        description: formData.description,
      };
      
      // Add kind-specific fields
      if (formData.kind === 'business_process_definition') {
        definition.process_type = formData.process_type;
      }
      if (formData.kind === 'metric_definition') {
        definition.formula = formData.formula;
        definition.unit = formData.unit;
      }
      
      if (dialogMode === 'add') {
        await axios.post(`${BASE_URL}/definitions`, {
          ...definition,
          kind: formData.kind
        }, {
          params: { created_by: 'admin' }
        });
        
        // Create relationship if parent exists
        if (parentForAdd && parentForAdd.kind !== 'folder') {
          let relType = 'belongs_to';
          if (parentForAdd.kind === 'value_chain_pattern_definition') {
            relType = 'belongs_to';
          } else if (parentForAdd.kind === 'business_process_definition') {
            relType = 'belongs_to_module';
          }
          
          await axios.post(`${BASE_URL}/relationships`, {
            from_entity_code: formData.code,
            to_entity_code: parentForAdd.code,
            relationship_type: relType
          }, {
            params: { created_by: 'admin' }
          });
        }
        
        onSnackbar?.(`${formData.name} created successfully`, 'success');
      } else {
        await axios.put(`${BASE_URL}/definitions/${selectedNode?.kind}/${selectedNode?.code}`, definition, {
          params: { changed_by: 'admin' }
        });
        onSnackbar?.(`${formData.name} updated successfully`, 'success');
      }
      
      setAddDialogOpen(false);
      setEditDialogOpen(false);
      fetchOntologyData();
      onRefresh?.();
    } catch (err: any) {
      onSnackbar?.(`Failed to save: ${err.message}`, 'error');
    }
  };

  const handleDelete = async () => {
    if (!selectedNode) return;
    
    try {
      await axios.delete(`${BASE_URL}/definitions/${selectedNode.kind}/${selectedNode.code}`, {
        params: { deleted_by: 'admin' }
      });
      onSnackbar?.(`${selectedNode.name} deleted successfully`, 'success');
      setDeleteDialogOpen(false);
      setSelectedNode(null);
      fetchOntologyData();
      onRefresh?.();
    } catch (err: any) {
      onSnackbar?.(`Failed to delete: ${err.message}`, 'error');
    }
  };

  const getIcon = (kind: string) => {
    switch (kind) {
      case 'value_chain_pattern_definition': return <ValueChainIcon sx={{ color: KIND_COLORS[kind] }} />;
      case 'business_process_definition': return <ModuleIcon sx={{ color: KIND_COLORS[kind] }} />;
      case 'metric_definition': return <KPIIcon sx={{ color: KIND_COLORS[kind] }} />;
      case 'entity_definition': return <EntityIcon sx={{ color: KIND_COLORS[kind] }} />;
      case 'folder': return <ChevronRightIcon />;
      default: return <ChevronRightIcon />;
    }
  };

  const renderTreeNode = (node: OntologyNode, depth: number = 0) => {
    const hasChildren = node.children && node.children.length > 0;
    const isExpanded = expandedNodes.has(node.code);
    const isSelected = selectedNode?.code === node.code;
    const isFolder = node.kind === 'folder';
    
    return (
      <Box key={node.code}>
        <ListItem
          sx={{
            pl: depth * 3,
            backgroundColor: isSelected ? 'action.selected' : 'transparent',
            '&:hover': { backgroundColor: 'action.hover' },
            cursor: 'pointer',
            borderLeft: !isFolder ? `3px solid ${KIND_COLORS[node.kind] || '#ccc'}` : 'none',
          }}
          onClick={() => !isFolder && handleNodeClick(node)}
        >
          <ListItemIcon sx={{ minWidth: 32 }}>
            {hasChildren ? (
              <IconButton size="small" onClick={(e) => { e.stopPropagation(); toggleNode(node.code); }}>
                {isExpanded ? <ExpandMoreIcon /> : <ChevronRightIcon />}
              </IconButton>
            ) : (
              <Box sx={{ width: 32 }} />
            )}
          </ListItemIcon>
          <ListItemIcon sx={{ minWidth: 32 }}>
            {getIcon(node.kind)}
          </ListItemIcon>
          <ListItemText
            primary={
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                <Typography variant="body2" fontWeight={isSelected ? 600 : 400}>
                  {node.name}
                </Typography>
                {!isFolder && (
                  <Chip 
                    label={node.code} 
                    size="small" 
                    variant="outlined"
                    sx={{ fontSize: '0.65rem', height: 18 }}
                  />
                )}
              </Box>
            }
            secondary={node.description ? node.description.substring(0, 60) + (node.description.length > 60 ? '...' : '') : null}
          />
          {!isFolder && (
            <ListItemSecondaryAction>
              <Tooltip title="Add child">
                <IconButton size="small" onClick={(e) => { e.stopPropagation(); handleAddClick(node); }}>
                  <AddIcon fontSize="small" />
                </IconButton>
              </Tooltip>
              <Tooltip title="Edit">
                <IconButton size="small" onClick={(e) => { e.stopPropagation(); handleEditClick(node); }}>
                  <EditIcon fontSize="small" />
                </IconButton>
              </Tooltip>
              <Tooltip title="Delete">
                <IconButton size="small" color="error" onClick={(e) => { e.stopPropagation(); handleDeleteClick(node); }}>
                  <DeleteIcon fontSize="small" />
                </IconButton>
              </Tooltip>
            </ListItemSecondaryAction>
          )}
        </ListItem>
        {hasChildren && (
          <Collapse in={isExpanded}>
            {node.children!.map(child => renderTreeNode(child, depth + 1))}
          </Collapse>
        )}
      </Box>
    );
  };

  const renderDetailsPanel = () => {
    if (!selectedNode || selectedNode.kind === 'folder') {
      return (
        <Box sx={{ p: 2, textAlign: 'center', color: 'text.secondary' }}>
          <Typography>Select a node to view details</Typography>
        </Box>
      );
    }

    return (
      <Box sx={{ p: 2 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 2 }}>
          {getIcon(selectedNode.kind)}
          <Typography variant="h6">{selectedNode.name}</Typography>
        </Box>
        
        <Divider sx={{ mb: 2 }} />
        
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1.5 }}>
          <Box>
            <Typography variant="caption" color="text.secondary">Code</Typography>
            <Typography variant="body2" fontFamily="monospace">{selectedNode.code}</Typography>
          </Box>
          
          <Box>
            <Typography variant="caption" color="text.secondary">Type</Typography>
            <Typography variant="body2">
              {DEFINITION_KINDS.find(k => k.kind === selectedNode.kind)?.label || selectedNode.kind}
            </Typography>
          </Box>
          
          {selectedNode.description && (
            <Box>
              <Typography variant="caption" color="text.secondary">Description</Typography>
              <Typography variant="body2">{selectedNode.description}</Typography>
            </Box>
          )}
          
          {selectedNode.fields && Object.keys(selectedNode.fields).length > 0 && (
            <>
              <Divider sx={{ my: 1 }} />
              <Typography variant="subtitle2" color="text.secondary">Fields</Typography>
              {Object.entries(selectedNode.fields).map(([key, value]) => (
                value && (
                  <Box key={key}>
                    <Typography variant="caption" color="text.secondary">{key}</Typography>
                    <Typography variant="body2" sx={{ wordBreak: 'break-word' }}>
                      {typeof value === 'object' ? JSON.stringify(value) : String(value)}
                    </Typography>
                  </Box>
                )
              ))}
            </>
          )}
        </Box>
        
        <Box sx={{ mt: 3, display: 'flex', gap: 1 }}>
          <Button 
            variant="outlined" 
            size="small" 
            startIcon={<EditIcon />}
            onClick={() => handleEditClick(selectedNode)}
          >
            Edit
          </Button>
          <Button 
            variant="outlined" 
            size="small" 
            color="error"
            startIcon={<DeleteIcon />}
            onClick={() => handleDeleteClick(selectedNode)}
          >
            Delete
          </Button>
        </Box>
      </Box>
    );
  };

  if (loading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', p: 4 }}>
        <Typography>Loading ontology...</Typography>
      </Box>
    );
  }

  return (
    <Box sx={{ display: 'flex', gap: 2, height: '100%' }}>
      {/* Tree Panel */}
      <Paper sx={{ flex: 2, overflow: 'auto', maxHeight: 600 }}>
        <Box sx={{ p: 1, display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: 1, borderColor: 'divider' }}>
          <Typography variant="subtitle1" fontWeight={600}>Ontology Structure</Typography>
          <Box>
            <Tooltip title="Add Value Chain">
              <IconButton size="small" onClick={() => handleAddClick()}>
                <AddIcon />
              </IconButton>
            </Tooltip>
            <Tooltip title="Refresh">
              <IconButton size="small" onClick={fetchOntologyData}>
                <RefreshIcon />
              </IconButton>
            </Tooltip>
          </Box>
        </Box>
        
        {treeData.length === 0 ? (
          <Box sx={{ p: 3, textAlign: 'center' }}>
            <Alert severity="info">
              No ontology data found. Click the + button to add a value chain.
            </Alert>
          </Box>
        ) : (
          <List dense disablePadding>
            {treeData.map(node => renderTreeNode(node))}
          </List>
        )}
      </Paper>
      
      {/* Details Panel */}
      <Paper sx={{ flex: 1, minWidth: 300, maxHeight: 600, overflow: 'auto' }}>
        <Box sx={{ p: 1, borderBottom: 1, borderColor: 'divider' }}>
          <Typography variant="subtitle1" fontWeight={600}>Details</Typography>
        </Box>
        {renderDetailsPanel()}
      </Paper>
      
      {/* Add/Edit Dialog */}
      <Dialog open={addDialogOpen || editDialogOpen} onClose={() => { setAddDialogOpen(false); setEditDialogOpen(false); }} maxWidth="sm" fullWidth>
        <DialogTitle>
          {dialogMode === 'add' ? 'Add New' : 'Edit'} {DEFINITION_KINDS.find(k => k.kind === formData.kind)?.label || 'Item'}
          {parentForAdd && dialogMode === 'add' && (
            <Typography variant="body2" color="text.secondary">
              Under: {parentForAdd.name}
            </Typography>
          )}
        </DialogTitle>
        <DialogContent>
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2, mt: 1 }}>
            {dialogMode === 'add' && (
              <FormControl fullWidth>
                <InputLabel>Type</InputLabel>
                <Select
                  value={formData.kind}
                  label="Type"
                  onChange={(e) => setFormData({ ...formData, kind: e.target.value })}
                >
                  {DEFINITION_KINDS.map(k => (
                    <MenuItem key={k.kind} value={k.kind}>{k.label}</MenuItem>
                  ))}
                </Select>
              </FormControl>
            )}
            
            <TextField
              label="Code"
              value={formData.code}
              onChange={(e) => setFormData({ ...formData, code: e.target.value.toLowerCase().replace(/\s+/g, '_') })}
              fullWidth
              disabled={dialogMode === 'edit'}
              helperText="Unique identifier (lowercase, underscores)"
            />
            
            <TextField
              label="Name"
              value={formData.name}
              onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              fullWidth
              autoFocus
            />
            
            <TextField
              label="Description"
              value={formData.description}
              onChange={(e) => setFormData({ ...formData, description: e.target.value })}
              fullWidth
              multiline
              rows={2}
            />
            
            {formData.kind === 'business_process_definition' && (
              <FormControl fullWidth>
                <InputLabel>Process Type</InputLabel>
                <Select
                  value={formData.process_type}
                  label="Process Type"
                  onChange={(e) => setFormData({ ...formData, process_type: e.target.value })}
                >
                  <MenuItem value="core">Core</MenuItem>
                  <MenuItem value="support">Support</MenuItem>
                  <MenuItem value="management">Management</MenuItem>
                </Select>
              </FormControl>
            )}
            
            {formData.kind === 'metric_definition' && (
              <>
                <TextField
                  label="Formula"
                  value={formData.formula}
                  onChange={(e) => setFormData({ ...formData, formula: e.target.value })}
                  fullWidth
                  multiline
                  rows={2}
                  helperText="Natural language formula description"
                />
                <TextField
                  label="Unit"
                  value={formData.unit}
                  onChange={(e) => setFormData({ ...formData, unit: e.target.value })}
                  fullWidth
                  placeholder="e.g., %, USD, count"
                />
              </>
            )}
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => { setAddDialogOpen(false); setEditDialogOpen(false); }}>Cancel</Button>
          <Button 
            variant="contained" 
            onClick={handleSave}
            disabled={!formData.code || !formData.name}
          >
            {dialogMode === 'add' ? 'Create' : 'Save'}
          </Button>
        </DialogActions>
      </Dialog>
      
      {/* Delete Confirmation Dialog */}
      <Dialog open={deleteDialogOpen} onClose={() => setDeleteDialogOpen(false)}>
        <DialogTitle>Confirm Delete</DialogTitle>
        <DialogContent>
          <Typography>
            Are you sure you want to delete "{selectedNode?.name}"?
          </Typography>
          <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
            This action cannot be undone.
          </Typography>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setDeleteDialogOpen(false)}>Cancel</Button>
          <Button variant="contained" color="error" onClick={handleDelete}>
            Delete
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
}
