import { useState, useEffect } from 'react';
import {
  Box,
  Typography,
  IconButton,
  TextField,
  Button,
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
  Checkbox,
  InputAdornment,
  CircularProgress,
  Alert
} from '@mui/material';
import {
  ExpandMore as ExpandMoreIcon,
  ChevronRight as ChevronRightIcon,
  Business as ValueChainIcon,
  Category as ModuleIcon,
  Assessment as KPIIcon,
  Storage as EntityIcon,
  Refresh as RefreshIcon,
  Search as SearchIcon,
  Clear as ClearIcon,
  ShoppingCart as CartIcon
} from '@mui/icons-material';
import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8090/api/v1/metadata';

interface OntologyNode {
  id?: string;
  code: string;
  name: string;
  kind: string;
  description?: string;
  children?: OntologyNode[];
  fields?: Record<string, any>;
}

interface Relationship {
  id: string;
  from_entity_id?: string;
  to_entity_id?: string;
  from_entity_code: string;
  to_entity_code: string;
  relationship_type: string;
}

interface KPITreeViewProps {
  onKPIToggleCart?: (kpiCode: string) => void;
  onKPIViewDetails?: (kpiCode: string) => void;
  selectedKPIs?: string[];
  currentViewKPI?: string | null;
  onSnackbar?: (message: string, severity: 'success' | 'error') => void;
}

const KIND_COLORS: Record<string, string> = {
  'value_chain_pattern_definition': '#4caf50',
  'business_process_definition': '#2196f3',
  'metric_definition': '#ff9800',
  'entity_definition': '#9c27b0',
};

export default function KPITreeView({ 
  onKPIToggleCart, 
  onKPIViewDetails, 
  selectedKPIs = [],
  currentViewKPI = null,
  onSnackbar 
}: KPITreeViewProps) {
  const [treeData, setTreeData] = useState<OntologyNode[]>([]);
  const [expandedNodes, setExpandedNodes] = useState<Set<string>>(new Set(['root']));
  const [selectedNode, setSelectedNode] = useState<OntologyNode | null>(null);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    fetchOntologyData();
  }, []);

  const fetchOntologyData = async () => {
    setLoading(true);
    try {
      const [vcRes, modRes, kpiRes, entityRes, relRes] = await Promise.all([
        axios.get(`${BASE_URL}/definitions/value_chain_pattern_definition`, { params: { limit: 100 } }),
        axios.get(`${BASE_URL}/definitions/business_process_definition`, { params: { limit: 100 } }),
        axios.get(`${BASE_URL}/definitions/metric_definition`, { params: { limit: 500 } }).catch(() => ({ data: [] })),
        axios.get(`${BASE_URL}/definitions/entity_definition`, { params: { limit: 100 } }).catch(() => ({ data: [] })),
        axios.get(`${BASE_URL}/relationships`).catch(() => ({ data: [] }))
      ]);

      const valueChains = vcRes.data || [];
      const modules = modRes.data || [];
      const kpis = kpiRes.data || [];
      const entities = entityRes.data || [];
      const rels = relRes.data || [];
      
      const tree = buildTree(valueChains, modules, kpis, entities, rels);
      setTreeData(tree);
      
      // Auto-expand first level
      const firstLevelCodes = tree.map(n => n.code);
      setExpandedNodes(new Set(['root', ...firstLevelCodes]));
    } catch (err) {
      console.error('Failed to fetch ontology data:', err);
      onSnackbar?.('Failed to fetch KPI data', 'error');
    } finally {
      setLoading(false);
    }
  };

  const buildTree = (
    valueChains: any[],
    modules: any[],
    kpis: any[],
    _entities: any[],
    relationships: Relationship[]
  ): OntologyNode[] => {
    // Use lowercase keys for case-insensitive matching
    const modulesByCode = new Map(modules.map(m => [m.code.toLowerCase(), m]));
    const kpisByCode = new Map(kpis.map(k => [k.code.toLowerCase(), k]));
    
    // Maps use lowercase keys for case-insensitive matching
    const moduleToVC = new Map<string, string>();
    const kpiToModule = new Map<string, string>();
    const kpiToVC = new Map<string, string>();
    const kpiToEntities = new Map<string, Set<string>>();
    
    relationships.forEach(rel => {
      const fromLower = rel.from_entity_code.toLowerCase();
      const toLower = rel.to_entity_code.toLowerCase();
      
      if (rel.relationship_type === 'belongs_to' || rel.relationship_type === 'belongs_to_value_chain') {
        if (modulesByCode.has(fromLower)) {
          moduleToVC.set(fromLower, toLower);
        }
        if (kpisByCode.has(fromLower) && !modulesByCode.has(toLower)) {
          kpiToVC.set(fromLower, toLower);
        }
      }
      if (rel.relationship_type === 'belongs_to_module') {
        kpiToModule.set(fromLower, toLower);
      }
      // 'contains' is Module -> KPI (opposite direction)
      if (rel.relationship_type === 'contains') {
        if (modulesByCode.has(fromLower) && kpisByCode.has(toLower)) {
          kpiToModule.set(toLower, fromLower);
        }
      }
      if (rel.relationship_type === 'uses' || rel.relationship_type === 'uses_entity') {
        if (!kpiToEntities.has(fromLower)) {
          kpiToEntities.set(fromLower, new Set());
        }
        kpiToEntities.get(fromLower)!.add(toLower);
      }
    });
    
    const tree: OntologyNode[] = [];
    
    // Value Chains as root nodes
    valueChains.forEach(vc => {
      const vcNode: OntologyNode = {
        id: vc.id,
        code: vc.code,
        name: vc.name,
        kind: 'value_chain_pattern_definition',
        description: vc.description,
        fields: { domain: vc.domain },
        children: []
      };
      
      // Find modules belonging to this value chain
      modules.forEach(mod => {
        if (moduleToVC.get(mod.code.toLowerCase()) === vc.code.toLowerCase()) {
          const modNode: OntologyNode = {
            id: mod.id,
            code: mod.code,
            name: mod.name,
            kind: 'business_process_definition',
            description: mod.description,
            fields: { process_type: mod.process_type },
            children: []
          };
          
          // Find KPIs belonging to this module
          kpis.forEach(kpi => {
            if (kpiToModule.get(kpi.code.toLowerCase()) === mod.code.toLowerCase()) {
              const kpiEntitiesSet = kpiToEntities.get(kpi.code.toLowerCase());
              const kpiEntities = kpiEntitiesSet ? Array.from(kpiEntitiesSet) : [];
              const kpiNode: OntologyNode = {
                id: kpi.id,
                code: kpi.code,
                name: kpi.name,
                kind: 'metric_definition',
                description: kpi.description,
                fields: { 
                  formula: kpi.formula,
                  math_expression: kpi.math_expression,
                  unit: kpi.unit,
                  required_objects: kpi.required_objects,
                  entities: kpiEntities
                },
                children: []
              };
              modNode.children!.push(kpiNode);
            }
          });
          
          vcNode.children!.push(modNode);
        }
      });
      
      // Find KPIs directly under value chain (not in a module)
      kpis.forEach(kpi => {
        const kpiLower = kpi.code.toLowerCase();
        if (kpiToVC.get(kpiLower) === vc.code.toLowerCase() && !kpiToModule.has(kpiLower)) {
          const kpiEntitiesSet = kpiToEntities.get(kpiLower);
          const kpiEntities = kpiEntitiesSet ? Array.from(kpiEntitiesSet) : [];
          const kpiNode: OntologyNode = {
            id: kpi.id,
            code: kpi.code,
            name: kpi.name,
            kind: 'metric_definition',
            description: kpi.description,
            fields: { 
              formula: kpi.formula,
              math_expression: kpi.math_expression,
              unit: kpi.unit,
              required_objects: kpi.required_objects,
              entities: kpiEntities
            },
            children: []
          };
          vcNode.children!.push(kpiNode);
        }
      });
      
      tree.push(vcNode);
    });
    
    // Add orphan modules (not linked to any value chain)
    const orphanModules: OntologyNode[] = [];
    modules.forEach(mod => {
      if (!moduleToVC.has(mod.code.toLowerCase())) {
        const modNode: OntologyNode = {
          id: mod.id,
          code: mod.code,
          name: mod.name,
          kind: 'business_process_definition',
          description: mod.description,
          fields: { process_type: mod.process_type },
          children: []
        };
        
        // Find KPIs for this orphan module
        kpis.forEach(kpi => {
          if (kpiToModule.get(kpi.code.toLowerCase()) === mod.code.toLowerCase()) {
            const kpiEntitiesSet = kpiToEntities.get(kpi.code.toLowerCase());
            const kpiEntities = kpiEntitiesSet ? Array.from(kpiEntitiesSet) : [];
            modNode.children!.push({
              id: kpi.id,
              code: kpi.code,
              name: kpi.name,
              kind: 'metric_definition',
              description: kpi.description,
              fields: { 
                formula: kpi.formula,
                math_expression: kpi.math_expression,
                unit: kpi.unit,
                required_objects: kpi.required_objects,
                entities: kpiEntities
              },
              children: []
            });
          }
        });
        
        orphanModules.push(modNode);
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
      const kpiLower = kpi.code.toLowerCase();
      if (!kpiToModule.has(kpiLower) && !kpiToVC.has(kpiLower)) {
        const kpiEntitiesSet = kpiToEntities.get(kpiLower);
        const kpiEntities = kpiEntitiesSet ? Array.from(kpiEntitiesSet) : [];
        orphanKpis.push({
          id: kpi.id,
          code: kpi.code,
          name: kpi.name,
          kind: 'metric_definition',
          description: kpi.description,
          fields: { 
            formula: kpi.formula,
            math_expression: kpi.math_expression,
            unit: kpi.unit,
            required_objects: kpi.required_objects,
            entities: kpiEntities
          },
          children: []
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
    if (node.kind === 'metric_definition' && onKPIViewDetails) {
      onKPIViewDetails(node.code);
    }
  };

  const handleCartToggle = (kpiCode: string, e: React.MouseEvent) => {
    e.stopPropagation();
    if (onKPIToggleCart) {
      onKPIToggleCart(kpiCode);
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

  // Filter tree based on search query
  const filterTree = (nodes: OntologyNode[], query: string): OntologyNode[] => {
    if (!query) return nodes;
    
    const lowerQuery = query.toLowerCase();
    
    return nodes.reduce<OntologyNode[]>((acc, node) => {
      const matchesName = node.name?.toLowerCase().includes(lowerQuery);
      const matchesCode = node.code?.toLowerCase().includes(lowerQuery);
      const matchesDescription = node.description?.toLowerCase().includes(lowerQuery);
      
      const filteredChildren = node.children ? filterTree(node.children, query) : [];
      
      if (matchesName || matchesCode || matchesDescription || filteredChildren.length > 0) {
        acc.push({
          ...node,
          children: filteredChildren.length > 0 ? filteredChildren : node.children
        });
      }
      
      return acc;
    }, []);
  };

  const filteredTreeData = filterTree(treeData, searchQuery);

  const countKPIs = (nodes: OntologyNode[]): number => {
    return nodes.reduce((count, node) => {
      if (node.kind === 'metric_definition') return count + 1;
      if (node.children) return count + countKPIs(node.children);
      return count;
    }, 0);
  };

  const renderTreeNode = (node: OntologyNode, depth: number = 0) => {
    const hasChildren = node.children && node.children.length > 0;
    const isExpanded = expandedNodes.has(node.code);
    const isSelected = selectedNode?.code === node.code || currentViewKPI === node.code;
    const isFolder = node.kind === 'folder';
    const isKPI = node.kind === 'metric_definition';
    const isInCart = isKPI && selectedKPIs.includes(node.code);
    
    return (
      <Box key={node.code}>
        <ListItem
          sx={{
            pl: depth * 2.5,
            py: 0.5,
            backgroundColor: isSelected ? 'action.selected' : 'transparent',
            '&:hover': { backgroundColor: 'action.hover' },
            cursor: 'pointer',
            borderLeft: !isFolder ? `3px solid ${KIND_COLORS[node.kind] || '#ccc'}` : 'none',
          }}
          onClick={() => handleNodeClick(node)}
        >
          <ListItemIcon sx={{ minWidth: 28 }}>
            {hasChildren ? (
              <IconButton size="small" onClick={(e) => { e.stopPropagation(); toggleNode(node.code); }}>
                {isExpanded ? <ExpandMoreIcon fontSize="small" /> : <ChevronRightIcon fontSize="small" />}
              </IconButton>
            ) : (
              <Box sx={{ width: 28 }} />
            )}
          </ListItemIcon>
          <ListItemIcon sx={{ minWidth: 28 }}>
            {getIcon(node.kind)}
          </ListItemIcon>
          <ListItemText
            primary={
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
                <Typography variant="body2" fontWeight={isSelected ? 600 : 400} noWrap>
                  {node.name}
                </Typography>
                {hasChildren && !isKPI && (
                  <Chip 
                    label={countKPIs(node.children || [])} 
                    size="small" 
                    sx={{ fontSize: '0.65rem', height: 16, ml: 0.5 }}
                  />
                )}
              </Box>
            }
            secondary={
              isKPI && node.fields?.formula ? (
                <Typography variant="caption" color="text.secondary" noWrap sx={{ maxWidth: 200, display: 'block' }}>
                  {node.fields.formula.substring(0, 40)}{node.fields.formula.length > 40 ? '...' : ''}
                </Typography>
              ) : null
            }
          />
          {isKPI && (
            <ListItemSecondaryAction>
              <Tooltip title={isInCart ? "Remove from cart" : "Add to cart"}>
                <Checkbox
                  size="small"
                  checked={isInCart}
                  onClick={(e) => handleCartToggle(node.code, e)}
                  icon={<CartIcon fontSize="small" />}
                  checkedIcon={<CartIcon fontSize="small" color="primary" />}
                />
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
          <Typography>Select a KPI to view details</Typography>
        </Box>
      );
    }

    const isKPI = selectedNode.kind === 'metric_definition';
    const isInCart = isKPI && selectedKPIs.includes(selectedNode.code);

    return (
      <Box sx={{ p: 2 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 2 }}>
          {getIcon(selectedNode.kind)}
          <Typography variant="h6" noWrap sx={{ flex: 1 }}>{selectedNode.name}</Typography>
          {isKPI && (
            <Chip 
              label={isInCart ? "In Cart" : "Not in Cart"} 
              color={isInCart ? "primary" : "default"}
              size="small"
            />
          )}
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
              {selectedNode.kind === 'value_chain_pattern_definition' ? 'Value Chain' :
               selectedNode.kind === 'business_process_definition' ? 'Module' :
               selectedNode.kind === 'metric_definition' ? 'KPI/Metric' : selectedNode.kind}
            </Typography>
          </Box>
          
          {selectedNode.description && (
            <Box>
              <Typography variant="caption" color="text.secondary">Description</Typography>
              <Typography variant="body2">{selectedNode.description}</Typography>
            </Box>
          )}
          
          {selectedNode.fields?.formula && (
            <Box>
              <Typography variant="caption" color="text.secondary">Formula</Typography>
              <Typography variant="body2" sx={{ fontStyle: 'italic' }}>{selectedNode.fields.formula}</Typography>
            </Box>
          )}
          
          {selectedNode.fields?.math_expression && (
            <Box>
              <Typography variant="caption" color="text.secondary">Math Expression</Typography>
              <Typography variant="body2" fontFamily="monospace" sx={{ bgcolor: 'grey.100', p: 1, borderRadius: 1 }}>
                {selectedNode.fields.math_expression}
              </Typography>
            </Box>
          )}
          
          {selectedNode.fields?.unit && (
            <Box>
              <Typography variant="caption" color="text.secondary">Unit</Typography>
              <Typography variant="body2">{selectedNode.fields.unit}</Typography>
            </Box>
          )}
          
          {selectedNode.fields?.required_objects?.length > 0 && (
            <Box>
              <Typography variant="caption" color="text.secondary">Required Entities</Typography>
              <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5, mt: 0.5 }}>
                {selectedNode.fields?.required_objects?.map((obj: string) => (
                  <Chip key={obj} label={obj} size="small" variant="outlined" />
                ))}
              </Box>
            </Box>
          )}
          
          {selectedNode.fields?.entities?.length > 0 && (
            <Box>
              <Typography variant="caption" color="text.secondary">Linked Entities</Typography>
              <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5, mt: 0.5 }}>
                {selectedNode.fields?.entities?.map((entity: string) => (
                  <Chip key={entity} label={entity} size="small" color="secondary" variant="outlined" />
                ))}
              </Box>
            </Box>
          )}
        </Box>
        
        {isKPI && (
          <Box sx={{ mt: 3, display: 'flex', gap: 1 }}>
            <Button 
              variant={isInCart ? "outlined" : "contained"}
              size="small" 
              startIcon={<CartIcon />}
              onClick={() => onKPIToggleCart?.(selectedNode.code)}
            >
              {isInCart ? 'Remove from Cart' : 'Add to Cart'}
            </Button>
          </Box>
        )}
      </Box>
    );
  };

  if (loading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', p: 4, height: '100%' }}>
        <CircularProgress size={24} sx={{ mr: 2 }} />
        <Typography>Loading KPIs...</Typography>
      </Box>
    );
  }

  return (
    <Box sx={{ display: 'flex', gap: 2, height: '100%' }}>
      {/* Tree Panel */}
      <Paper sx={{ flex: 2, overflow: 'hidden', display: 'flex', flexDirection: 'column' }}>
        <Box sx={{ p: 1, display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: 1, borderColor: 'divider' }}>
          <Typography variant="subtitle1" fontWeight={600}>KPI Hierarchy</Typography>
          <Tooltip title="Refresh">
            <IconButton size="small" onClick={fetchOntologyData}>
              <RefreshIcon />
            </IconButton>
          </Tooltip>
        </Box>
        
        {/* Search */}
        <Box sx={{ p: 1, borderBottom: 1, borderColor: 'divider' }}>
          <TextField
            size="small"
            fullWidth
            placeholder="Search KPIs..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <SearchIcon fontSize="small" />
                </InputAdornment>
              ),
              endAdornment: searchQuery && (
                <InputAdornment position="end">
                  <IconButton size="small" onClick={() => setSearchQuery('')}>
                    <ClearIcon fontSize="small" />
                  </IconButton>
                </InputAdornment>
              )
            }}
          />
        </Box>
        
        <Box sx={{ flex: 1, overflow: 'auto' }}>
          {filteredTreeData.length === 0 ? (
            <Box sx={{ p: 3, textAlign: 'center' }}>
              <Alert severity="info">
                {searchQuery ? 'No KPIs match your search.' : 'No KPI data found.'}
              </Alert>
            </Box>
          ) : (
            <List dense disablePadding>
              {filteredTreeData.map(node => renderTreeNode(node))}
            </List>
          )}
        </Box>
        
        {/* Stats footer */}
        <Box sx={{ p: 1, borderTop: 1, borderColor: 'divider', bgcolor: 'grey.50' }}>
          <Typography variant="caption" color="text.secondary">
            {countKPIs(treeData)} KPIs total • {selectedKPIs.length} in cart
          </Typography>
        </Box>
      </Paper>
      
      {/* Details Panel */}
      <Paper sx={{ flex: 1, minWidth: 280, overflow: 'auto' }}>
        <Box sx={{ p: 1, borderBottom: 1, borderColor: 'divider' }}>
          <Typography variant="subtitle1" fontWeight={600}>Details</Typography>
        </Box>
        {renderDetailsPanel()}
      </Paper>
    </Box>
  );
}
