import { useState, useEffect, lazy, Suspense } from 'react';
import { RefreshCw, GitBranch, List, Database, X } from 'lucide-react';
import { Card } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { cn } from '../lib/utils';
import axios from 'axios';

const OntologyGraph = lazy(() => import('../components/OntologyGraph'));
import OntologyTreeView from '../components/OntologyTreeView';
import OntologyModelsView from '../components/OntologyModelsView';

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

const BASE_URL = 'http://127.0.0.1:8090/api/v1/metadata';

interface ValueChain { code: string; name: string; description?: string; domain?: string; metadata_?: Record<string, any>; }
interface Module { code: string; name: string; description?: string; process_type?: string; metadata_?: Record<string, any>; }
interface KPI { code: string; name: string; description?: string; metadata_?: Record<string, any>; }
interface ObjectModelDef { code: string; name: string; description?: string; metadata_?: Record<string, any>; }

function TabButton({ active, onClick, icon, label }: { active: boolean; onClick: () => void; icon: React.ReactNode; label: string }) {
  return (
    <button
      onClick={onClick}
      className={cn(
        "flex items-center gap-2 px-4 py-3 text-sm font-medium transition-colors border-b-2",
        active ? "text-alpha-500 border-alpha-500" : "theme-text-muted border-transparent hover:theme-text"
      )}
    >
      {icon}
      {label}
    </button>
  );
}

export default function OntologyManagerPage() {
  const [tabValue, setTabValue] = useState(0);
  const [valueChains, setValueChains] = useState<ValueChain[]>([]);
  const [, setModules] = useState<Module[]>([]);
  const [, setKpis] = useState<KPI[]>([]);
  const [, setObjectModels] = useState<ObjectModelDef[]>([]);
  const [graphData, setGraphData] = useState<GraphData>({ nodes: [], links: [] });
  const [filteredGraphData, setFilteredGraphData] = useState<GraphData>({ nodes: [], links: [] });
  const [selectedValueChain, setSelectedValueChain] = useState<string>('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [snackbar, setSnackbar] = useState<{open: boolean, message: string, severity: 'success' | 'error'}>({open: false, message: '', severity: 'success'});
  const [editDialog, setEditDialog] = useState<{open: boolean, type: 'valueChain' | 'module' | 'kpi' | 'objectModel', item: any, isNew: boolean}>({open: false, type: 'valueChain', item: null, isNew: false});
  const [editForm, setEditForm] = useState({code: '', name: '', description: '', valueChain: ''});

  useEffect(() => { fetchData(); }, []);

  const fetchData = async () => {
    setLoading(true);
    setError(null);
    try {
      const [vcRes, modRes, kpiRes, objRes, relRes] = await Promise.all([
        axios.get(`${BASE_URL}/definitions/value_chain_pattern_definition`, { params: { limit: 100 } }),
        axios.get(`${BASE_URL}/definitions/business_process_definition`, { params: { limit: 100 } }),
        axios.get(`${BASE_URL}/definitions/metric_definition`, { params: { limit: 100 } }).catch(() => ({ data: [] })),
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
      const gd = buildGraphData(vcData, modData, kpiData, objData, relData);
      setGraphData(gd);
      setFilteredGraphData(gd);
    } catch (err: any) {
      setError(err.message || 'Failed to fetch data');
    } finally {
      setLoading(false);
    }
  };

  const buildGraphData = (vcs: ValueChain[], mods: Module[], kpiList: KPI[], objs: ObjectModelDef[], relationships: Array<{from_entity_code: string; to_entity_code: string; relationship_type: string}>): GraphData => {
    const nodes: GraphNode[] = [];
    const links: GraphLink[] = [];
    const vcCodeToId = new Map<string, string>();
    const modCodeToId = new Map<string, string>();
    const kpiCodeToId = new Map<string, string>();
    const objCodeToId = new Map<string, string>();

    vcs.forEach(vc => {
      const nodeId = `vc-${vc.code}`;
      vcCodeToId.set(vc.code.toLowerCase(), nodeId);
      nodes.push({ id: nodeId, name: vc.name, type: 'ValueChain', code: vc.code, description: vc.description });
    });

    mods.forEach(mod => {
      const nodeId = `mod-${mod.code}`;
      modCodeToId.set(mod.code.toLowerCase(), nodeId);
      nodes.push({ id: nodeId, name: mod.name, type: 'Module', code: mod.code, description: mod.description });
    });

    kpiList.forEach(kpi => {
      const nodeId = `kpi-${kpi.code}`;
      kpiCodeToId.set(kpi.code.toLowerCase(), nodeId);
      nodes.push({ id: nodeId, name: kpi.name, type: 'KPI', code: kpi.code, description: kpi.description });
    });

    objs.forEach(obj => {
      const nodeId = `obj-${obj.code}`;
      objCodeToId.set(obj.code.toLowerCase(), nodeId);
      nodes.push({ id: nodeId, name: obj.name, type: 'ObjectModel', code: obj.code, description: obj.description });
    });

    relationships.forEach(rel => {
      const fromCodeLower = rel.from_entity_code.toLowerCase();
      const toCodeLower = rel.to_entity_code.toLowerCase();

      if (rel.relationship_type === 'belongs_to' || rel.relationship_type === 'belongs_to_value_chain') {
        if (modCodeToId.has(fromCodeLower) && vcCodeToId.has(toCodeLower)) {
          const sourceId = vcCodeToId.get(toCodeLower);
          const targetId = modCodeToId.get(fromCodeLower);
          if (sourceId && targetId) links.push({ source: sourceId, target: targetId, type: 'CONTAINS' });
        }
      }

      if (rel.relationship_type === 'contains') {
        const sourceId = modCodeToId.get(fromCodeLower);
        const targetId = kpiCodeToId.get(toCodeLower);
        if (sourceId && targetId) links.push({ source: sourceId, target: targetId, type: 'HAS_KPI' });
      }

      if (rel.relationship_type === 'belongs_to_module') {
        if (!kpiCodeToId.has(fromCodeLower)) {
          const nodeId = `kpi-${rel.from_entity_code}`;
          kpiCodeToId.set(fromCodeLower, nodeId);
          nodes.push({ id: nodeId, name: rel.from_entity_code.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase()), type: 'KPI', code: rel.from_entity_code, description: 'Discovered from relationship' });
        }
        const sourceId = modCodeToId.get(toCodeLower);
        const targetId = kpiCodeToId.get(fromCodeLower);
        if (sourceId && targetId) links.push({ source: sourceId, target: targetId, type: 'HAS_KPI' });
      }

      if (rel.relationship_type === 'uses' || rel.relationship_type === 'uses_object') {
        const sourceId = kpiCodeToId.get(fromCodeLower);
        const targetId = objCodeToId.get(toCodeLower);
        if (sourceId && targetId) links.push({ source: sourceId, target: targetId, type: 'USES' });
      }
    });

    return { nodes, links };
  };

  const handleValueChainFilter = (vcCode: string) => {
    setSelectedValueChain(vcCode);
    if (!vcCode) { setFilteredGraphData(graphData); return; }
    const vcNodeId = `vc-${vcCode}`;
    const includedNodeIds = new Set<string>([vcNodeId]);

    graphData.links.forEach(link => {
      const sourceId = typeof link.source === 'object' ? (link.source as GraphNode).id : link.source;
      const targetId = typeof link.target === 'object' ? (link.target as GraphNode).id : link.target;
      if (sourceId === vcNodeId && (targetId as string).startsWith('mod-')) includedNodeIds.add(targetId as string);
    });

    const moduleNodeIds = new Set<string>();
    includedNodeIds.forEach(nodeId => { if ((nodeId as string).startsWith('mod-')) moduleNodeIds.add(nodeId); });

    graphData.links.forEach(link => {
      const sourceId = typeof link.source === 'object' ? (link.source as GraphNode).id : link.source;
      const targetId = typeof link.target === 'object' ? (link.target as GraphNode).id : link.target;
      if (moduleNodeIds.has(sourceId as string) && (targetId as string).startsWith('kpi-')) includedNodeIds.add(targetId as string);
    });

    const kpiNodeIds = new Set<string>();
    includedNodeIds.forEach(nodeId => { if ((nodeId as string).startsWith('kpi-')) kpiNodeIds.add(nodeId); });

    graphData.links.forEach(link => {
      const sourceId = typeof link.source === 'object' ? (link.source as GraphNode).id : link.source;
      const targetId = typeof link.target === 'object' ? (link.target as GraphNode).id : link.target;
      if (kpiNodeIds.has(sourceId as string) && (targetId as string).startsWith('obj-')) includedNodeIds.add(targetId as string);
    });

    const filteredNodes = graphData.nodes.filter(n => includedNodeIds.has(n.id));
    const filteredLinks = graphData.links.filter(link => {
      const sourceId = typeof link.source === 'object' ? (link.source as GraphNode).id : link.source;
      const targetId = typeof link.target === 'object' ? (link.target as GraphNode).id : link.target;
      return includedNodeIds.has(sourceId as string) && includedNodeIds.has(targetId as string);
    });
    setFilteredGraphData({ nodes: filteredNodes, links: filteredLinks });
  };

  const handleNodeAdd = (type: GraphNode['type']) => {
    const typeMap: Record<string, 'valueChain' | 'module' | 'kpi' | 'objectModel'> = { 'ValueChain': 'valueChain', 'Module': 'module', 'KPI': 'kpi', 'ObjectModel': 'objectModel' };
    setEditForm({ code: '', name: '', description: '', valueChain: selectedValueChain });
    setEditDialog({ open: true, type: typeMap[type], item: null, isNew: true });
  };

  const handleNodeEdit = (node: GraphNode) => {
    const typeMap: Record<string, 'valueChain' | 'module' | 'kpi' | 'objectModel'> = { 'ValueChain': 'valueChain', 'Module': 'module', 'KPI': 'kpi', 'ObjectModel': 'objectModel' };
    setEditForm({ code: node.code || '', name: node.name, description: node.description || '', valueChain: '' });
    setEditDialog({ open: true, type: typeMap[node.type], item: node, isNew: false });
  };

  const handleNodeDelete = async (node: GraphNode) => {
    const typeMap: Record<string, string> = { 'ValueChain': 'value_chain_pattern_definition', 'Module': 'business_process_definition', 'KPI': 'kpi_definition', 'ObjectModel': 'entity_definition' };
    if (!window.confirm(`Are you sure you want to delete "${node.name}"?`)) return;
    try {
      await axios.delete(`${BASE_URL}/definitions/${typeMap[node.type]}/${node.code}`, { params: { deleted_by: 'admin' } });
      setSnackbar({ open: true, message: `${node.type} deleted successfully`, severity: 'success' });
      fetchData();
    } catch (err: any) {
      setSnackbar({ open: true, message: `Failed to delete: ${err.message}`, severity: 'error' });
    }
  };

  const handleLinkAdd = async (source: GraphNode, target: GraphNode, linkType: string) => {
    try {
      const relationshipTypeMap: Record<string, string> = { 'CONTAINS': 'contains', 'BELONGS_TO': 'belongs_to', 'HAS_KPI': 'has_kpi', 'USES': 'uses', 'RELATES_TO': 'relates_to' };
      const relType = relationshipTypeMap[linkType] || linkType.toLowerCase();
      await axios.post(`${BASE_URL}/relationships`, { from_entity_code: source.code, to_entity_code: target.code, relationship_type: relType }, { params: { created_by: 'admin' } });
      setSnackbar({ open: true, message: `Relationship ${source.name} → ${target.name} created successfully`, severity: 'success' });
      fetchData();
    } catch (err: any) {
      let errorMsg = 'Failed to create relationship';
      if (err.response?.data?.detail) {
        const detail = err.response.data.detail;
        if (typeof detail === 'string') {
          errorMsg = detail.includes('duplicate') || detail.includes('already exists') ? `Relationship already exists: ${source.name} → ${target.name}` : detail;
        } else { errorMsg = JSON.stringify(detail); }
      } else if (err.message) { errorMsg = err.message; }
      setSnackbar({ open: true, message: errorMsg, severity: 'error' });
    }
  };

  const handleSaveEdit = async () => {
    const { type, item, isNew } = editDialog;
    const kindMap: Record<string, string> = { 'valueChain': 'value_chain_pattern_definition', 'module': 'business_process_definition', 'kpi': 'kpi_definition', 'objectModel': 'entity_definition' };
    const kind = kindMap[type];
    try {
      if (isNew) {
        const newData: any = { code: editForm.code, name: editForm.name, description: editForm.description };
        if (type === 'module' && editForm.valueChain) newData.metadata_ = { value_chain: editForm.valueChain };
        await axios.post(`${BASE_URL}/definitions/${kind}`, newData, { params: { created_by: 'admin' } });
        setSnackbar({ open: true, message: `${type} created successfully`, severity: 'success' });
      } else {
        const updatedData = { ...item, name: editForm.name, description: editForm.description };
        if (item.code) await axios.put(`${BASE_URL}/definitions/${kind}/${item.code}`, updatedData, { params: { changed_by: 'admin' } });
        setSnackbar({ open: true, message: `${type} updated successfully`, severity: 'success' });
      }
      setEditDialog({ open: false, type: 'valueChain', item: null, isNew: false });
      fetchData();
    } catch (err: any) {
      setSnackbar({ open: true, message: `Failed to save: ${err.message}`, severity: 'error' });
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-[50vh]">
        <RefreshCw className="w-8 h-8 text-alpha-500 animate-spin" />
      </div>
    );
  }

  return (
    <div className="space-y-4">
      {/* Header */}
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold theme-text-title">Ontology Studio</h1>
        <Button variant="outline" onClick={fetchData}>
          <RefreshCw className="w-4 h-4 mr-2" />
          Refresh
        </Button>
      </div>

      {error && (
        <div className="p-3 rounded-lg bg-red-500/10 border border-red-500/30 text-red-400">{error}</div>
      )}

      {/* Tabs */}
      <Card className="overflow-hidden">
        <div className="flex border-b theme-border">
          <TabButton active={tabValue === 0} onClick={() => setTabValue(0)} icon={<GitBranch className="w-4 h-4" />} label="Graph View" />
          <TabButton active={tabValue === 1} onClick={() => setTabValue(1)} icon={<List className="w-4 h-4" />} label="Ontology" />
          <TabButton active={tabValue === 2} onClick={() => setTabValue(2)} icon={<Database className="w-4 h-4" />} label="Models" />
        </div>

        {/* Graph View Tab */}
        {tabValue === 0 && (
          <div className="p-4">
            <p className="text-sm theme-text-muted mb-4">
              Interactive graph visualization of value chains, modules, KPIs, and object models.
              Click on nodes to see details. Drag to reposition. Scroll to zoom.
            </p>
            <div className="h-[600px] rounded-xl overflow-hidden border theme-border bg-[#1a1a2e]">
              <Suspense fallback={
                <div className="flex items-center justify-center h-full">
                  <RefreshCw className="w-8 h-8 text-white animate-spin" />
                </div>
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
            </div>
          </div>
        )}

        {/* Ontology Tree View Tab */}
        {tabValue === 1 && (
          <div className="p-4">
            <p className="text-sm theme-text-muted mb-4">
              Hierarchical tree view of the ontology structure. Click on nodes to view details, use buttons to add, edit, or delete components.
            </p>
            <OntologyTreeView
              onRefresh={fetchData}
              onSnackbar={(message, severity) => setSnackbar({ open: true, message, severity })}
            />
          </div>
        )}

        {/* Models Tab */}
        {tabValue === 2 && (
          <div className="p-4">
            <p className="text-sm theme-text-muted mb-4">
              View the ontology model schema - the types and fields that define ontology components.
            </p>
            <OntologyModelsView
              onSnackbar={(message, severity) => setSnackbar({ open: true, message, severity })}
            />
          </div>
        )}
      </Card>

      {/* Edit Dialog */}
      {editDialog.open && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="w-full max-w-md rounded-xl theme-card-bg border theme-border shadow-2xl">
            <div className="p-4 border-b theme-border flex items-center justify-between">
              <h2 className="text-lg font-semibold theme-text-title">
                {editDialog.isNew ? 'Add' : 'Edit'} {editDialog.type === 'valueChain' ? 'Value Chain' : editDialog.type === 'module' ? 'Module' : editDialog.type === 'kpi' ? 'KPI' : 'Object Model'}
              </h2>
              <button onClick={() => setEditDialog({...editDialog, open: false})} className="p-1 hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 rounded">
                <X className="w-5 h-5 theme-text-muted" />
              </button>
            </div>
            <div className="p-4 space-y-4">
              {editDialog.isNew && (
                <div>
                  <label className="block text-sm font-medium theme-text mb-1">Code</label>
                  <input
                    type="text"
                    value={editForm.code}
                    onChange={(e) => setEditForm({ ...editForm, code: e.target.value })}
                    className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                    placeholder="Unique identifier (e.g., my_value_chain)"
                    autoFocus
                  />
                </div>
              )}
              <div>
                <label className="block text-sm font-medium theme-text mb-1">Name</label>
                <input
                  type="text"
                  value={editForm.name}
                  onChange={(e) => setEditForm({ ...editForm, name: e.target.value })}
                  className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                  autoFocus={!editDialog.isNew}
                />
              </div>
              <div>
                <label className="block text-sm font-medium theme-text mb-1">Description</label>
                <textarea
                  value={editForm.description}
                  onChange={(e) => setEditForm({ ...editForm, description: e.target.value })}
                  rows={3}
                  className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500 resize-none"
                />
              </div>
              {editDialog.isNew && editDialog.type === 'module' && (
                <div>
                  <label className="block text-sm font-medium theme-text mb-1">Value Chain</label>
                  <select
                    value={editForm.valueChain}
                    onChange={(e) => setEditForm({ ...editForm, valueChain: e.target.value })}
                    className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                  >
                    <option value="">Select Value Chain</option>
                    {valueChains.map(vc => (
                      <option key={vc.code} value={vc.code}>{vc.name}</option>
                    ))}
                  </select>
                </div>
              )}
            </div>
            <div className="p-4 border-t theme-border flex justify-end gap-2">
              <Button variant="outline" onClick={() => setEditDialog({...editDialog, open: false})}>Cancel</Button>
              <Button onClick={handleSaveEdit} disabled={editDialog.isNew && (!editForm.code || !editForm.name)}>
                {editDialog.isNew ? 'Create' : 'Save'}
              </Button>
            </div>
          </div>
        </div>
      )}

      {/* Snackbar */}
      {snackbar.open && (
        <div className="fixed bottom-4 left-1/2 -translate-x-1/2 z-50">
          <div className={cn(
            "px-4 py-3 rounded-lg shadow-lg flex items-center gap-3",
            snackbar.severity === 'success' ? "bg-green-500/20 border border-green-500/30 text-green-400" : "bg-red-500/20 border border-red-500/30 text-red-400"
          )}>
            <span>{snackbar.message}</span>
            <button onClick={() => setSnackbar({...snackbar, open: false})} className="p-1 hover:bg-white/10 rounded">
              <X className="w-4 h-4" />
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
