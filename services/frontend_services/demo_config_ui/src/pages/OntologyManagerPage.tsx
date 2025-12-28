import { useState, useEffect, lazy, Suspense } from 'react';
import {
  Box,
  Typography,
  Paper,
  Tabs,
  Tab,
  Grid,
  Card,
  CardContent,
  Button,
  TextField,
  IconButton,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Chip,
  CircularProgress,
  Alert,
  Snackbar
} from '@mui/material';
import {
  Edit as EditIcon,
  Delete as DeleteIcon,
  Business as ValueChainIcon,
  Category as ModuleIcon,
  Refresh as RefreshIcon,
  AccountTree as GraphIcon
} from '@mui/icons-material';

// Lazy load the graph component to avoid SSR issues
const OntologyGraph = lazy(() => import('../components/OntologyGraph'));

// Graph types (matching OntologyGraph component)
interface GraphNode {
  id: string;
  name: string;
  type: 'ValueChain' | 'Module' | 'KPI' | 'ObjectModel';
  description?: string;
  code?: string;
}

interface GraphLink {
  source: string;
  target: string;
  type: string;
}

interface GraphData {
  nodes: GraphNode[];
  links: GraphLink[];
}
import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8090/api/v1/metadata';

interface ValueChain {
  code: string;
  name: string;
  description?: string;
  domain?: string;
  metadata_?: Record<string, any>;
}

interface Module {
  code: string;
  name: string;
  description?: string;
  process_type?: string;
  metadata_?: Record<string, any>;
}

interface KPI {
  code: string;
  name: string;
  description?: string;
  metadata_?: Record<string, any>;
}

interface ObjectModelDef {
  code: string;
  name: string;
  description?: string;
  metadata_?: Record<string, any>;
}

interface TabPanelProps {
  children?: React.ReactNode;
  index: number;
  value: number;
}

function TabPanel(props: TabPanelProps) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`ontology-tabpanel-${index}`}
      aria-labelledby={`ontology-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          {children}
        </Box>
      )}
    </div>
  );
}

export default function OntologyManagerPage() {
  const [tabValue, setTabValue] = useState(0);
  const [valueChains, setValueChains] = useState<ValueChain[]>([]);
  const [modules, setModules] = useState<Module[]>([]);
  const [, setKpis] = useState<KPI[]>([]);
  const [, setObjectModels] = useState<ObjectModelDef[]>([]);
  const [graphData, setGraphData] = useState<GraphData>({ nodes: [], links: [] });
  const [filteredGraphData, setFilteredGraphData] = useState<GraphData>({ nodes: [], links: [] });
  const [selectedValueChain, setSelectedValueChain] = useState<string>('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [snackbar, setSnackbar] = useState<{open: boolean, message: string, severity: 'success' | 'error'}>({open: false, message: '', severity: 'success'});

  // Edit Dialog State
  const [editDialog, setEditDialog] = useState<{open: boolean, type: 'valueChain' | 'module' | 'kpi' | 'objectModel', item: any, isNew: boolean}>({open: false, type: 'valueChain', item: null, isNew: false});
  const [editForm, setEditForm] = useState({code: '', name: '', description: '', valueChain: ''});

  // Fetch data on mount
  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    setLoading(true);
    setError(null);
    try {
      const [vcRes, modRes, kpiRes, objRes, relRes] = await Promise.all([
        axios.get(`${BASE_URL}/definitions/value_chain_pattern_definition`, { params: { limit: 100 } }),
        axios.get(`${BASE_URL}/definitions/business_process_definition`, { params: { limit: 100 } }),
        axios.get(`${BASE_URL}/definitions/kpi_definition`, { params: { limit: 100 } }).catch(() => ({ data: [] })),
        axios.get(`${BASE_URL}/definitions/entity_definition`, { params: { limit: 100 } }).catch(() => ({ data: [] })),
        axios.get(`${BASE_URL}/relationships`).catch(() => ({ data: [] }))
      ]);
      const vcData = vcRes.data || [];
      const modData = modRes.data || [];
      const kpiData = kpiRes.data || [];
      const objData = objRes.data || [];
      const relData = relRes.data || [];
      
      setValueChains(vcData);
      setModules(modData);
      setKpis(kpiData);
      setObjectModels(objData);
      
      // Build graph data using relationships from API
      const gd = buildGraphData(vcData, modData, kpiData, objData, relData);
      setGraphData(gd);
      setFilteredGraphData(gd);
    } catch (err: any) {
      setError(err.message || 'Failed to fetch data');
    } finally {
      setLoading(false);
    }
  };

  const buildGraphData = (
    vcs: ValueChain[], 
    mods: Module[], 
    kpiList: KPI[], 
    objs: ObjectModelDef[],
    relationships: Array<{from_entity_code: string; to_entity_code: string; relationship_type: string}>
  ): GraphData => {
    const nodes: GraphNode[] = [];
    const links: GraphLink[] = [];
    const nodeCodeToId = new Map<string, string>();
    
    // Add Value Chain nodes
    vcs.forEach(vc => {
      const nodeId = `vc-${vc.code}`;
      nodeCodeToId.set(vc.code, nodeId);
      nodes.push({
        id: nodeId,
        name: vc.name,
        type: 'ValueChain',
        code: vc.code,
        description: vc.description
      });
    });
    
    // Add Module nodes
    mods.forEach(mod => {
      const nodeId = `mod-${mod.code}`;
      nodeCodeToId.set(mod.code, nodeId);
      nodes.push({
        id: nodeId,
        name: mod.name,
        type: 'Module',
        code: mod.code,
        description: mod.description
      });
    });
    
    // Add KPI nodes
    kpiList.forEach(kpi => {
      const nodeId = `kpi-${kpi.code}`;
      nodeCodeToId.set(kpi.code, nodeId);
      nodes.push({
        id: nodeId,
        name: kpi.name,
        type: 'KPI',
        code: kpi.code,
        description: kpi.description
      });
    });
    
    // Add Object Model nodes
    objs.forEach(obj => {
      const nodeId = `obj-${obj.code}`;
      nodeCodeToId.set(obj.code, nodeId);
      nodes.push({
        id: nodeId,
        name: obj.name,
        type: 'ObjectModel',
        code: obj.code,
        description: obj.description
      });
    });
    
    // Build hierarchy links from relationships table ONLY:
    // - ValueChain → Module (from belongs_to_value_chain where from=module)
    // - Module → KPI (from belongs_to_module where from=kpi)
    // - KPI → ObjectModel (from uses/uses_object)
    
    const moduleCodeSet = new Set(mods.map(m => m.code));
    
    relationships.forEach(rel => {
      // Module belongs_to_value_chain → create VC → Module link
      if (rel.relationship_type === 'belongs_to_value_chain') {
        const fromCode = rel.from_entity_code;
        const vcCode = rel.to_entity_code;
        
        // Only process if from_entity is a module
        if (moduleCodeSet.has(fromCode)) {
          const sourceId = nodeCodeToId.get(vcCode);     // ValueChain is source
          const targetId = nodeCodeToId.get(fromCode);   // Module is target
          
          if (sourceId && targetId) {
            links.push({
              source: sourceId,
              target: targetId,
              type: 'CONTAINS'
            });
          }
        }
      }
      
      // KPI belongs_to_module → create Module → KPI link
      if (rel.relationship_type === 'belongs_to_module') {
        const kpiCode = rel.from_entity_code;
        const moduleCode = rel.to_entity_code;
        
        // Create KPI node if it doesn't exist
        if (!nodeCodeToId.has(kpiCode)) {
          const nodeId = `kpi-${kpiCode}`;
          nodeCodeToId.set(kpiCode, nodeId);
          nodes.push({
            id: nodeId,
            name: kpiCode.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase()),
            type: 'KPI',
            code: kpiCode,
            description: 'Discovered from relationship'
          });
        }
        
        const sourceId = nodeCodeToId.get(moduleCode); // Module is source
        const targetId = nodeCodeToId.get(kpiCode);    // KPI is target
        
        if (sourceId && targetId) {
          links.push({
            source: sourceId,
            target: targetId,
            type: 'HAS_KPI'
          });
        }
      }
      
      // KPI uses ObjectModel
      if (rel.relationship_type === 'uses' || rel.relationship_type === 'uses_object') {
        const sourceId = nodeCodeToId.get(rel.from_entity_code);
        const targetId = nodeCodeToId.get(rel.to_entity_code);
        
        if (sourceId && targetId) {
          links.push({
            source: sourceId,
            target: targetId,
            type: 'USES'
          });
        }
      }
    });
    
    return { nodes, links };
  };

  // Filter graph data by value chain - follows hierarchy: VC → Module → KPI → ObjectModel
  const handleValueChainFilter = (vcCode: string) => {
    setSelectedValueChain(vcCode);
    
    if (!vcCode) {
      setFilteredGraphData(graphData);
      return;
    }
    
    const vcNodeId = `vc-${vcCode}`;
    const includedNodeIds = new Set<string>([vcNodeId]);
    
    // Step 1: Find modules connected to this value chain (VC → Module links)
    graphData.links.forEach(link => {
      const sourceId = typeof link.source === 'object' ? (link.source as GraphNode).id : link.source;
      const targetId = typeof link.target === 'object' ? (link.target as GraphNode).id : link.target;
      
      if (sourceId === vcNodeId && (targetId as string).startsWith('mod-')) {
        includedNodeIds.add(targetId as string);
      }
    });
    
    // Step 2: Find KPIs connected to those modules (Module → KPI links)
    const moduleNodeIds = new Set<string>();
    includedNodeIds.forEach(nodeId => {
      if ((nodeId as string).startsWith('mod-')) {
        moduleNodeIds.add(nodeId);
      }
    });
    
    graphData.links.forEach(link => {
      const sourceId = typeof link.source === 'object' ? (link.source as GraphNode).id : link.source;
      const targetId = typeof link.target === 'object' ? (link.target as GraphNode).id : link.target;
      
      if (moduleNodeIds.has(sourceId as string) && (targetId as string).startsWith('kpi-')) {
        includedNodeIds.add(targetId as string);
      }
    });
    
    // Step 3: Find ObjectModels connected to those KPIs (KPI → ObjectModel links)
    const kpiNodeIds = new Set<string>();
    includedNodeIds.forEach(nodeId => {
      if ((nodeId as string).startsWith('kpi-')) {
        kpiNodeIds.add(nodeId);
      }
    });
    
    graphData.links.forEach(link => {
      const sourceId = typeof link.source === 'object' ? (link.source as GraphNode).id : link.source;
      const targetId = typeof link.target === 'object' ? (link.target as GraphNode).id : link.target;
      
      if (kpiNodeIds.has(sourceId as string) && (targetId as string).startsWith('obj-')) {
        includedNodeIds.add(targetId as string);
      }
    });
    
    // Filter nodes and links
    const filteredNodes = graphData.nodes.filter(n => includedNodeIds.has(n.id));
    const filteredLinks = graphData.links.filter(link => {
      const sourceId = typeof link.source === 'object' ? (link.source as GraphNode).id : link.source;
      const targetId = typeof link.target === 'object' ? (link.target as GraphNode).id : link.target;
      return includedNodeIds.has(sourceId as string) && includedNodeIds.has(targetId as string);
    });
    
    setFilteredGraphData({ nodes: filteredNodes, links: filteredLinks });
  };

  // Handle node add from graph
  const handleNodeAdd = (type: GraphNode['type']) => {
    const typeMap: Record<string, 'valueChain' | 'module' | 'kpi' | 'objectModel'> = {
      'ValueChain': 'valueChain',
      'Module': 'module',
      'KPI': 'kpi',
      'ObjectModel': 'objectModel'
    };
    setEditForm({ code: '', name: '', description: '', valueChain: selectedValueChain });
    setEditDialog({ open: true, type: typeMap[type], item: null, isNew: true });
  };

  // Handle node edit from graph
  const handleNodeEdit = (node: GraphNode) => {
    const typeMap: Record<string, 'valueChain' | 'module' | 'kpi' | 'objectModel'> = {
      'ValueChain': 'valueChain',
      'Module': 'module',
      'KPI': 'kpi',
      'ObjectModel': 'objectModel'
    };
    setEditForm({ 
      code: node.code || '', 
      name: node.name, 
      description: node.description || '',
      valueChain: ''
    });
    setEditDialog({ open: true, type: typeMap[node.type], item: node, isNew: false });
  };

  // Handle node delete from graph
  const handleNodeDelete = async (node: GraphNode) => {
    const typeMap: Record<string, string> = {
      'ValueChain': 'value_chain_pattern_definition',
      'Module': 'business_process_definition',
      'KPI': 'kpi_definition',
      'ObjectModel': 'entity_definition'
    };
    
    if (!window.confirm(`Are you sure you want to delete "${node.name}"?`)) return;
    
    try {
      await axios.delete(`${BASE_URL}/definitions/${typeMap[node.type]}/${node.code}`, {
        params: { deleted_by: 'admin' }
      });
      setSnackbar({ open: true, message: `${node.type} deleted successfully`, severity: 'success' });
      fetchData();
    } catch (err: any) {
      setSnackbar({ open: true, message: `Failed to delete: ${err.message}`, severity: 'error' });
    }
  };

  // Handle link add from graph
  const handleLinkAdd = async (source: GraphNode, target: GraphNode, linkType: string) => {
    try {
      // Map UI link types to API relationship types
      const relationshipTypeMap: Record<string, string> = {
        'CONTAINS': 'contains',
        'BELONGS_TO': 'belongs_to_value_chain',
        'HAS_KPI': 'has_kpi',
        'USES': 'uses',
        'RELATES_TO': 'relates_to'
      };
      
      await axios.post(`${BASE_URL}/relationships`, {
        from_entity_code: source.code,
        to_entity_code: target.code,
        relationship_type: relationshipTypeMap[linkType] || linkType.toLowerCase()
      }, {
        params: { created_by: 'admin' }
      });
      
      setSnackbar({ 
        open: true, 
        message: `Relationship ${source.name} → ${target.name} created successfully`, 
        severity: 'success' 
      });
      fetchData(); // Refresh to show new relationship
    } catch (err: any) {
      setSnackbar({ open: true, message: `Failed to create relationship: ${err.message}`, severity: 'error' });
    }
  };

  const handleTabChange = (_: React.SyntheticEvent, newValue: number) => {
    setTabValue(newValue);
  };

  const handleEdit = (type: 'valueChain' | 'module', item: any) => {
    setEditForm({ code: item.code || '', name: item.name || '', description: item.description || '', valueChain: item.metadata_?.value_chain || '' });
    setEditDialog({ open: true, type, item, isNew: false });
  };

  const handleSaveEdit = async () => {
    const { type, item, isNew } = editDialog;
    const kindMap: Record<string, string> = {
      'valueChain': 'value_chain_pattern_definition',
      'module': 'business_process_definition',
      'kpi': 'kpi_definition',
      'objectModel': 'entity_definition'
    };
    const kind = kindMap[type];
    
    try {
      if (isNew) {
        // Create new item
        const newData: any = { 
          code: editForm.code, 
          name: editForm.name, 
          description: editForm.description 
        };
        if (type === 'module' && editForm.valueChain) {
          newData.metadata_ = { value_chain: editForm.valueChain };
        }
        await axios.post(`${BASE_URL}/definitions/${kind}`, newData, {
          params: { created_by: 'admin' }
        });
        setSnackbar({ open: true, message: `${type} created successfully`, severity: 'success' });
      } else {
        // Update existing item
        const updatedData = { ...item, name: editForm.name, description: editForm.description };
        if (item.code) {
          await axios.put(`${BASE_URL}/definitions/${kind}/${item.code}`, updatedData, {
            params: { changed_by: 'admin' }
          });
        }
        setSnackbar({ open: true, message: `${type} updated successfully`, severity: 'success' });
      }
      
      setEditDialog({ open: false, type: 'valueChain', item: null, isNew: false });
      fetchData();
    } catch (err: any) {
      setSnackbar({ open: true, message: `Failed to save: ${err.message}`, severity: 'error' });
    }
  };

  const handleDelete = async (type: 'valueChain' | 'module', code: string, name: string) => {
    if (!window.confirm(`Are you sure you want to delete "${name}"?`)) return;
    
    const kind = type === 'valueChain' ? 'value_chain_pattern_definition' : 'business_process_definition';
    
    try {
      await axios.delete(`${BASE_URL}/definitions/${kind}/${code}`, {
        params: { deleted_by: 'admin' }
      });
      
      setSnackbar({ open: true, message: `${type === 'valueChain' ? 'Value Chain' : 'Module'} deleted successfully`, severity: 'success' });
      fetchData(); // Refresh data
    } catch (err: any) {
      setSnackbar({ open: true, message: `Failed to delete: ${err.message}`, severity: 'error' });
    }
  };

  if (loading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '50vh' }}>
        <CircularProgress />
      </Box>
    );
  }

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
        <Typography variant="h4">
          Ontology Studio
        </Typography>
        <Button variant="outlined" startIcon={<RefreshIcon />} onClick={fetchData}>
          Refresh
        </Button>
      </Box>

      {error && (
        <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>
      )}

      <Paper sx={{ width: '100%', mb: 2 }}>
        <Tabs value={tabValue} onChange={handleTabChange} aria-label="ontology tabs">
          <Tab icon={<GraphIcon />} label="Graph View" />
          <Tab icon={<ValueChainIcon />} label="Value Chains" />
          <Tab icon={<ModuleIcon />} label="Modules" />
        </Tabs>
      </Paper>

      {/* Graph View Tab */}
      <TabPanel value={tabValue} index={0}>
        <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
          Interactive graph visualization of value chains, modules, KPIs, and object models.
          Click on nodes to see details. Drag to reposition. Scroll to zoom.
        </Typography>
        <Paper sx={{ height: 600, overflow: 'hidden', borderRadius: 2 }}>
          <Suspense fallback={
            <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100%', backgroundColor: '#1a1a2e' }}>
              <CircularProgress sx={{ color: '#fff' }} />
            </Box>
          }>
            <OntologyGraph 
              data={filteredGraphData} 
              width={typeof window !== 'undefined' ? window.innerWidth - 350 : 800} 
              height={580}
              valueChains={valueChains.map(vc => ({ code: vc.code, name: vc.name }))}
              selectedValueChain={selectedValueChain}
              onValueChainChange={handleValueChainFilter}
              onNodeClick={(node: GraphNode) => console.log('Node clicked:', node)}
              onNodeAdd={handleNodeAdd}
              onNodeEdit={handleNodeEdit}
              onNodeDelete={handleNodeDelete}
              onLinkAdd={handleLinkAdd}
            />
          </Suspense>
        </Paper>
      </TabPanel>

      {/* Value Chains Tab */}
      <TabPanel value={tabValue} index={1}>
        <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
          Manage value chains - click edit to rename or delete to remove.
        </Typography>
        <Grid container spacing={3}>
          {valueChains.length === 0 ? (
            <Grid item xs={12}>
              <Alert severity="info">No value chains found.</Alert>
            </Grid>
          ) : (
            valueChains.map((vc) => (
              <Grid item xs={12} md={6} lg={4} key={vc.code}>
                <Card variant="outlined">
                  <CardContent>
                    <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 1 }}>
                      <Box>
                        <Typography variant="h6">{vc.name}</Typography>
                        <Typography variant="caption" color="text.secondary">
                          Code: {vc.code}
                        </Typography>
                      </Box>
                      <Box>
                        <IconButton size="small" onClick={() => handleEdit('valueChain', vc)} title="Edit">
                          <EditIcon fontSize="small" />
                        </IconButton>
                        <IconButton size="small" onClick={() => handleDelete('valueChain', vc.code, vc.name)} color="error" title="Delete">
                          <DeleteIcon fontSize="small" />
                        </IconButton>
                      </Box>
                    </Box>
                    {vc.description && (
                      <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
                        {vc.description}
                      </Typography>
                    )}
                    {vc.domain && (
                      <Chip label={vc.domain} size="small" sx={{ mt: 1 }} />
                    )}
                  </CardContent>
                </Card>
              </Grid>
            ))
          )}
        </Grid>
      </TabPanel>

      {/* Modules Tab */}
      <TabPanel value={tabValue} index={2}>
        <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
          Manage modules (business processes) - click edit to rename or delete to remove.
        </Typography>
        <Grid container spacing={3}>
          {modules.length === 0 ? (
            <Grid item xs={12}>
              <Alert severity="info">No modules found.</Alert>
            </Grid>
          ) : (
            modules.map((mod) => (
              <Grid item xs={12} md={6} lg={4} key={mod.code}>
                <Card variant="outlined">
                  <CardContent>
                    <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 1 }}>
                      <Box>
                        <Typography variant="h6">{mod.name}</Typography>
                        <Typography variant="caption" color="text.secondary">
                          Code: {mod.code}
                        </Typography>
                      </Box>
                      <Box>
                        <IconButton size="small" onClick={() => handleEdit('module', mod)} title="Edit">
                          <EditIcon fontSize="small" />
                        </IconButton>
                        <IconButton size="small" onClick={() => handleDelete('module', mod.code, mod.name)} color="error" title="Delete">
                          <DeleteIcon fontSize="small" />
                        </IconButton>
                      </Box>
                    </Box>
                    {mod.description && (
                      <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
                        {mod.description}
                      </Typography>
                    )}
                    {mod.metadata_?.value_chain && (
                      <Chip label={`Value Chain: ${mod.metadata_.value_chain}`} size="small" sx={{ mt: 1 }} variant="outlined" />
                    )}
                  </CardContent>
                </Card>
              </Grid>
            ))
          )}
        </Grid>
      </TabPanel>

      {/* Edit Dialog */}
      <Dialog open={editDialog.open} onClose={() => setEditDialog({...editDialog, open: false})} maxWidth="sm" fullWidth>
        <DialogTitle>
          {editDialog.isNew ? 'Add' : 'Edit'} {editDialog.type === 'valueChain' ? 'Value Chain' : editDialog.type === 'module' ? 'Module' : editDialog.type === 'kpi' ? 'KPI' : 'Object Model'}
        </DialogTitle>
        <DialogContent>
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2, mt: 1 }}>
            {editDialog.isNew && (
              <TextField
                label="Code"
                value={editForm.code}
                onChange={(e) => setEditForm({ ...editForm, code: e.target.value })}
                fullWidth
                autoFocus
                helperText="Unique identifier (e.g., my_value_chain)"
              />
            )}
            <TextField
              label="Name"
              value={editForm.name}
              onChange={(e) => setEditForm({ ...editForm, name: e.target.value })}
              fullWidth
              autoFocus={!editDialog.isNew}
            />
            <TextField
              label="Description"
              value={editForm.description}
              onChange={(e) => setEditForm({ ...editForm, description: e.target.value })}
              fullWidth
              multiline
              rows={3}
            />
            {editDialog.isNew && editDialog.type === 'module' && (
              <TextField
                select
                label="Value Chain"
                value={editForm.valueChain}
                onChange={(e) => setEditForm({ ...editForm, valueChain: e.target.value })}
                fullWidth
                SelectProps={{ native: true }}
              >
                <option value="">Select Value Chain</option>
                {valueChains.map(vc => (
                  <option key={vc.code} value={vc.code}>{vc.name}</option>
                ))}
              </TextField>
            )}
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setEditDialog({...editDialog, open: false})}>Cancel</Button>
          <Button 
            variant="contained" 
            onClick={handleSaveEdit}
            disabled={editDialog.isNew && (!editForm.code || !editForm.name)}
          >
            {editDialog.isNew ? 'Create' : 'Save'}
          </Button>
        </DialogActions>
      </Dialog>

      {/* Snackbar for notifications */}
      <Snackbar 
        open={snackbar.open} 
        autoHideDuration={4000} 
        onClose={() => setSnackbar({...snackbar, open: false})}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      >
        <Alert severity={snackbar.severity} onClose={() => setSnackbar({...snackbar, open: false})}>
          {snackbar.message}
        </Alert>
      </Snackbar>
    </Box>
  );
}
