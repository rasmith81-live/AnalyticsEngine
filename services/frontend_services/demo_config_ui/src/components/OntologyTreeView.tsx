import { useState, useEffect } from 'react';
import {
  ChevronDown,
  ChevronRight,
  Plus,
  Pencil,
  Trash2,
  Building2,
  Layers,
  BarChart3,
  Database,
  RefreshCw,
  X,
} from 'lucide-react';
import { Card } from './ui/Card';
import { Button } from './ui/Button';
import { cn } from '../lib/utils';
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
  { kind: 'value_chain_pattern_definition', label: 'Value Chain' },
  { kind: 'business_process_definition', label: 'Module/Process' },
  { kind: 'metric_definition', label: 'KPI/Metric' },
  { kind: 'entity_definition', label: 'Entity' },
];

const KIND_COLORS: Record<string, string> = {
  'value_chain_pattern_definition': 'border-l-green-500',
  'business_process_definition': 'border-l-blue-500',
  'metric_definition': 'border-l-amber-500',
  'entity_definition': 'border-l-purple-500',
};

const KIND_ICON_COLORS: Record<string, string> = {
  'value_chain_pattern_definition': 'text-green-500',
  'business_process_definition': 'text-blue-500',
  'metric_definition': 'text-amber-500',
  'entity_definition': 'text-purple-500',
};

export default function OntologyTreeView({ onRefresh, onSnackbar }: OntologyTreeViewProps) {
  const [treeData, setTreeData] = useState<OntologyNode[]>([]);
  const [expandedNodes, setExpandedNodes] = useState<Set<string>>(new Set(['root', '_orphan_kpis', '_orphan_modules', '_entities']));
  const [selectedNode, setSelectedNode] = useState<OntologyNode | null>(null);
  const [loading, setLoading] = useState(true);
  const [editDialogOpen, setEditDialogOpen] = useState(false);
  const [addDialogOpen, setAddDialogOpen] = useState(false);
  const [deleteDialogOpen, setDeleteDialogOpen] = useState(false);
  const [dialogMode, setDialogMode] = useState<'add' | 'edit'>('add');
  const [parentForAdd, setParentForAdd] = useState<OntologyNode | null>(null);
  const [formData, setFormData] = useState({ code: '', name: '', description: '', kind: 'value_chain_pattern_definition', process_type: 'core', formula: '', unit: '' });

  useEffect(() => { fetchOntologyData(); }, []);

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
      const tree = buildTree(vcRes.data || [], modRes.data || [], kpiRes.data || [], entityRes.data || [], relRes.data || []);
      setTreeData(tree);
    } catch (err) {
      console.error('Failed to fetch ontology data:', err);
      onSnackbar?.('Failed to fetch ontology data', 'error');
    } finally { setLoading(false); }
  };

  const buildTree = (valueChains: any[], modules: any[], kpis: any[], entities: any[], relationships: Relationship[]): OntologyNode[] => {
    const modulesByCode = new Map(modules.map(m => [m.code.toLowerCase(), m]));
    const kpisByCode = new Map(kpis.map(k => [k.code.toLowerCase(), k]));
    const entitiesByCode = new Map(entities.map(e => [e.code.toLowerCase(), e]));
    const moduleToVC = new Map<string, string>();
    const kpiToModule = new Map<string, string>();
    const kpiToVC = new Map<string, string>();
    const entityToKpi = new Map<string, Set<string>>();
    const kpiToEntities = new Map<string, Set<string>>();

    relationships.forEach(rel => {
      const fromLower = rel.from_entity_code.toLowerCase();
      const toLower = rel.to_entity_code.toLowerCase();
      const fromIsModule = modulesByCode.has(fromLower);
      const fromIsKpi = kpisByCode.has(fromLower);
      const toIsVC = valueChains.some(vc => vc.code.toLowerCase() === toLower);
      const toIsModule = modulesByCode.has(toLower);
      const toIsKpi = kpisByCode.has(toLower);

      if (fromIsModule && toIsVC) moduleToVC.set(fromLower, toLower);
      else if (fromIsModule && toIsKpi) kpiToModule.set(toLower, fromLower);
      else if (fromIsKpi && toIsModule) kpiToModule.set(fromLower, toLower);
      else if (fromIsKpi && toIsVC) kpiToVC.set(fromLower, toLower);
      else if (fromIsKpi && !toIsVC && !toIsModule && !toIsKpi) {
        if (!entityToKpi.has(toLower)) entityToKpi.set(toLower, new Set());
        entityToKpi.get(toLower)!.add(fromLower);
        if (!kpiToEntities.has(fromLower)) kpiToEntities.set(fromLower, new Set());
        kpiToEntities.get(fromLower)!.add(toLower);
      }
    });

    const tree: OntologyNode[] = [];

    valueChains.forEach(vc => {
      const vcNode: OntologyNode = { code: vc.code, name: vc.name, kind: 'value_chain_pattern_definition', description: vc.description, fields: { domain: vc.domain }, children: [] };
      modules.forEach(mod => {
        if (moduleToVC.get(mod.code.toLowerCase()) === vc.code.toLowerCase()) {
          const modNode: OntologyNode = { code: mod.code, name: mod.name, kind: 'business_process_definition', description: mod.description, fields: { process_type: mod.process_type }, children: [] };
          kpis.forEach(kpi => {
            if (kpiToModule.get(kpi.code.toLowerCase()) === mod.code.toLowerCase()) {
              const entityChildren: OntologyNode[] = [];
              (kpiToEntities.get(kpi.code.toLowerCase()) || new Set()).forEach(entityCodeLower => {
                const entity = entitiesByCode.get(entityCodeLower);
                if (entity) entityChildren.push({ code: entity.code, name: entity.name, kind: 'entity_definition', description: entity.description, children: [] });
              });
              modNode.children!.push({ code: kpi.code, name: kpi.name, kind: 'metric_definition', description: kpi.description, fields: { formula: kpi.formula, math_expression: kpi.math_expression, unit: kpi.unit }, children: entityChildren });
            }
          });
          vcNode.children!.push(modNode);
        }
      });
      kpis.forEach(kpi => {
        if (kpiToVC.get(kpi.code.toLowerCase()) === vc.code.toLowerCase() && !kpiToModule.has(kpi.code.toLowerCase())) {
          const entityChildren: OntologyNode[] = [];
          (kpiToEntities.get(kpi.code.toLowerCase()) || new Set()).forEach(entityCodeLower => {
            const entity = entitiesByCode.get(entityCodeLower);
            if (entity) entityChildren.push({ code: entity.code, name: entity.name, kind: 'entity_definition', description: entity.description, children: [] });
          });
          vcNode.children!.push({ code: kpi.code, name: kpi.name, kind: 'metric_definition', description: kpi.description, fields: { formula: kpi.formula, math_expression: kpi.math_expression, unit: kpi.unit }, children: entityChildren });
        }
      });
      tree.push(vcNode);
    });

    const orphanModules = modules.filter(mod => !moduleToVC.has(mod.code.toLowerCase())).map(mod => ({ code: mod.code, name: mod.name, kind: 'business_process_definition', description: mod.description, fields: { process_type: mod.process_type }, children: [] }));
    if (orphanModules.length > 0) tree.push({ code: '_orphan_modules', name: 'Unassigned Modules', kind: 'folder', children: orphanModules });

    const orphanKpis = kpis.filter(kpi => !kpiToModule.has(kpi.code.toLowerCase()) && !kpiToVC.has(kpi.code.toLowerCase())).map(kpi => {
      const entityChildren: OntologyNode[] = [];
      (kpiToEntities.get(kpi.code.toLowerCase()) || new Set()).forEach(entityCodeLower => {
        const entity = entitiesByCode.get(entityCodeLower);
        if (entity) entityChildren.push({ code: entity.code, name: entity.name, kind: 'entity_definition', description: entity.description, children: [] });
      });
      return { code: kpi.code, name: kpi.name, kind: 'metric_definition', description: kpi.description, fields: { formula: kpi.formula, unit: kpi.unit }, children: entityChildren };
    });
    if (orphanKpis.length > 0) tree.push({ code: '_orphan_kpis', name: 'Unassigned KPIs', kind: 'folder', children: orphanKpis });

    const orphanEntities = entities.filter(e => !entityToKpi.has(e.code.toLowerCase())).map(e => ({ code: e.code, name: e.name, kind: 'entity_definition', description: e.description, fields: e, children: [] }));
    if (orphanEntities.length > 0) tree.push({ code: '_orphan_entities', name: 'Unassigned Entities', kind: 'folder', children: orphanEntities });

    return tree;
  };

  const toggleNode = (code: string) => {
    setExpandedNodes(prev => { const next = new Set(prev); if (next.has(code)) next.delete(code); else next.add(code); return next; });
  };

  const handleAddClick = (parentNode?: OntologyNode) => {
    setParentForAdd(parentNode || null);
    setDialogMode('add');
    let defaultKind = 'value_chain_pattern_definition';
    if (parentNode) {
      if (parentNode.kind === 'value_chain_pattern_definition') defaultKind = 'business_process_definition';
      else if (parentNode.kind === 'business_process_definition') defaultKind = 'metric_definition';
    }
    setFormData({ code: '', name: '', description: '', kind: defaultKind, process_type: 'core', formula: '', unit: '' });
    setAddDialogOpen(true);
  };

  const handleEditClick = (node: OntologyNode) => {
    setSelectedNode(node);
    setDialogMode('edit');
    setFormData({ code: node.code, name: node.name, description: node.description || '', kind: node.kind, process_type: node.fields?.process_type || 'core', formula: node.fields?.formula || '', unit: node.fields?.unit || '' });
    setEditDialogOpen(true);
  };

  const handleDeleteClick = (node: OntologyNode) => { setSelectedNode(node); setDeleteDialogOpen(true); };

  const handleSave = async () => {
    try {
      const definition: any = { code: formData.code, name: formData.name, description: formData.description };
      if (formData.kind === 'business_process_definition') definition.process_type = formData.process_type;
      if (formData.kind === 'metric_definition') { definition.formula = formData.formula; definition.unit = formData.unit; }

      if (dialogMode === 'add') {
        await axios.post(`${BASE_URL}/definitions`, { ...definition, kind: formData.kind }, { params: { created_by: 'admin' } });
        if (parentForAdd && parentForAdd.kind !== 'folder') {
          let relType = 'belongs_to';
          if (parentForAdd.kind === 'value_chain_pattern_definition') relType = 'belongs_to';
          else if (parentForAdd.kind === 'business_process_definition') relType = 'belongs_to_module';
          await axios.post(`${BASE_URL}/relationships`, { from_entity_code: formData.code, to_entity_code: parentForAdd.code, relationship_type: relType }, { params: { created_by: 'admin' } });
        }
        onSnackbar?.(`${formData.name} created successfully`, 'success');
      } else {
        await axios.put(`${BASE_URL}/definitions/${selectedNode?.kind}/${selectedNode?.code}`, definition, { params: { changed_by: 'admin' } });
        onSnackbar?.(`${formData.name} updated successfully`, 'success');
      }
      setAddDialogOpen(false);
      setEditDialogOpen(false);
      fetchOntologyData();
      onRefresh?.();
    } catch (err: any) { onSnackbar?.(`Failed to save: ${err.message}`, 'error'); }
  };

  const handleDelete = async () => {
    if (!selectedNode) return;
    try {
      await axios.delete(`${BASE_URL}/definitions/${selectedNode.kind}/${selectedNode.code}`, { params: { deleted_by: 'admin' } });
      onSnackbar?.(`${selectedNode.name} deleted successfully`, 'success');
      setDeleteDialogOpen(false);
      setSelectedNode(null);
      fetchOntologyData();
      onRefresh?.();
    } catch (err: any) { onSnackbar?.(`Failed to delete: ${err.message}`, 'error'); }
  };

  const getIcon = (kind: string) => {
    const colorClass = KIND_ICON_COLORS[kind] || 'theme-text-muted';
    switch (kind) {
      case 'value_chain_pattern_definition': return <Building2 className={cn("w-4 h-4", colorClass)} />;
      case 'business_process_definition': return <Layers className={cn("w-4 h-4", colorClass)} />;
      case 'metric_definition': return <BarChart3 className={cn("w-4 h-4", colorClass)} />;
      case 'entity_definition': return <Database className={cn("w-4 h-4", colorClass)} />;
      default: return <ChevronRight className="w-4 h-4 theme-text-muted" />;
    }
  };

  const renderTreeNode = (node: OntologyNode, depth: number = 0) => {
    const hasChildren = node.children && node.children.length > 0;
    const isExpanded = expandedNodes.has(node.code);
    const isSelected = selectedNode?.code === node.code;
    const isFolder = node.kind === 'folder';

    return (
      <div key={node.code}>
        <div
          className={cn(
            "flex items-center py-2 px-2 cursor-pointer transition-colors hover:bg-alpha-faded-50 dark:hover:bg-alpha-faded-900 group",
            isSelected && "bg-alpha-500/10",
            !isFolder && "border-l-2",
            !isFolder && KIND_COLORS[node.kind]
          )}
          style={{ paddingLeft: `${depth * 24 + 8}px` }}
          onClick={() => !isFolder && setSelectedNode(node)}
        >
          <div className="w-7 flex-shrink-0">
            {hasChildren ? (
              <button onClick={(e) => { e.stopPropagation(); toggleNode(node.code); }} className="p-0.5 hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 rounded">
                {isExpanded ? <ChevronDown className="w-4 h-4 theme-text-muted" /> : <ChevronRight className="w-4 h-4 theme-text-muted" />}
              </button>
            ) : null}
          </div>
          <div className="w-6 flex-shrink-0">{getIcon(node.kind)}</div>
          <div className="flex-1 min-w-0 flex items-center gap-2">
            <span className={cn("text-sm truncate", isSelected ? "font-semibold theme-text-title" : "theme-text")}>{node.name}</span>
            {!isFolder && <span className="px-1.5 py-0.5 rounded text-[10px] theme-card-bg border theme-border theme-text-muted">{node.code}</span>}
          </div>
          {!isFolder && (
            <div className="hidden group-hover:flex items-center gap-1">
              <button onClick={(e) => { e.stopPropagation(); handleAddClick(node); }} className="p-1 hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 rounded" title="Add child"><Plus className="w-3.5 h-3.5 theme-text-muted" /></button>
              <button onClick={(e) => { e.stopPropagation(); handleEditClick(node); }} className="p-1 hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 rounded" title="Edit"><Pencil className="w-3.5 h-3.5 theme-text-muted" /></button>
              <button onClick={(e) => { e.stopPropagation(); handleDeleteClick(node); }} className="p-1 hover:bg-red-500/20 rounded text-red-400" title="Delete"><Trash2 className="w-3.5 h-3.5" /></button>
            </div>
          )}
        </div>
        {hasChildren && isExpanded && <div>{node.children!.map(child => renderTreeNode(child, depth + 1))}</div>}
      </div>
    );
  };

  const renderDetailsPanel = () => {
    if (!selectedNode || selectedNode.kind === 'folder') {
      return <div className="p-4 text-center theme-text-muted">Select a node to view details</div>;
    }
    return (
      <div className="p-4 space-y-4">
        <div className="flex items-center gap-2">
          {getIcon(selectedNode.kind)}
          <h3 className="font-semibold theme-text-title">{selectedNode.name}</h3>
        </div>
        <div className="border-t theme-border" />
        <div className="space-y-3 text-sm">
          <div><p className="text-xs theme-text-muted">Code</p><p className="font-mono theme-text">{selectedNode.code}</p></div>
          <div><p className="text-xs theme-text-muted">Type</p><p className="theme-text">{DEFINITION_KINDS.find(k => k.kind === selectedNode.kind)?.label || selectedNode.kind}</p></div>
          {selectedNode.description && <div><p className="text-xs theme-text-muted">Description</p><p className="theme-text">{selectedNode.description}</p></div>}
          {selectedNode.fields && Object.keys(selectedNode.fields).length > 0 && (
            <>
              <div className="border-t theme-border pt-3"><p className="text-xs theme-text-muted mb-2">Fields</p></div>
              {Object.entries(selectedNode.fields).map(([key, value]) => value && (
                <div key={key}><p className="text-xs theme-text-muted">{key}</p><p className="theme-text break-words">{typeof value === 'object' ? JSON.stringify(value) : String(value)}</p></div>
              ))}
            </>
          )}
        </div>
        <div className="flex gap-2 pt-2">
          <Button variant="outline" size="sm" onClick={() => handleEditClick(selectedNode)}><Pencil className="w-4 h-4 mr-1" />Edit</Button>
          <Button variant="outline" size="sm" className="text-red-400 border-red-500/30 hover:bg-red-500/10" onClick={() => handleDeleteClick(selectedNode)}><Trash2 className="w-4 h-4 mr-1" />Delete</Button>
        </div>
      </div>
    );
  };

  if (loading) {
    return <div className="flex items-center justify-center p-8"><RefreshCw className="w-5 h-5 text-alpha-500 animate-spin mr-2" /><span className="theme-text-muted">Loading ontology...</span></div>;
  }

  return (
    <div className="flex gap-4 h-full">
      {/* Tree Panel */}
      <Card className="flex-[2] overflow-hidden flex flex-col max-h-[600px]">
        <div className="p-3 flex items-center justify-between border-b theme-border">
          <h3 className="font-semibold theme-text-title">Ontology Structure</h3>
          <div className="flex items-center gap-1">
            <button onClick={() => handleAddClick()} className="p-1.5 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800" title="Add Value Chain"><Plus className="w-4 h-4 theme-text-muted" /></button>
            <button onClick={fetchOntologyData} className="p-1.5 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800" title="Refresh"><RefreshCw className="w-4 h-4 theme-text-muted" /></button>
          </div>
        </div>
        <div className="flex-1 overflow-auto">
          {treeData.length === 0 ? (
            <div className="p-4"><div className="p-3 rounded-lg bg-blue-500/10 border border-blue-500/30 text-blue-400 text-sm">No ontology data found. Click the + button to add a value chain.</div></div>
          ) : (
            <div>{treeData.map(node => renderTreeNode(node))}</div>
          )}
        </div>
      </Card>

      {/* Details Panel */}
      <Card className="flex-1 min-w-[300px] max-h-[600px] overflow-auto">
        <div className="p-3 border-b theme-border"><h3 className="font-semibold theme-text-title">Details</h3></div>
        {renderDetailsPanel()}
      </Card>

      {/* Add/Edit Dialog */}
      {(addDialogOpen || editDialogOpen) && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="w-full max-w-md rounded-xl theme-card-bg border theme-border shadow-2xl">
            <div className="p-4 border-b theme-border flex items-center justify-between">
              <div>
                <h2 className="text-lg font-semibold theme-text-title">{dialogMode === 'add' ? 'Add New' : 'Edit'} {DEFINITION_KINDS.find(k => k.kind === formData.kind)?.label || 'Item'}</h2>
                {parentForAdd && dialogMode === 'add' && <p className="text-xs theme-text-muted">Under: {parentForAdd.name}</p>}
              </div>
              <button onClick={() => { setAddDialogOpen(false); setEditDialogOpen(false); }} className="p-1 hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 rounded"><X className="w-5 h-5 theme-text-muted" /></button>
            </div>
            <div className="p-4 space-y-4">
              {dialogMode === 'add' && (
                <div>
                  <label className="block text-sm font-medium theme-text mb-1">Type</label>
                  <select value={formData.kind} onChange={(e) => setFormData({ ...formData, kind: e.target.value })} className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500">
                    {DEFINITION_KINDS.map(k => <option key={k.kind} value={k.kind}>{k.label}</option>)}
                  </select>
                </div>
              )}
              <div>
                <label className="block text-sm font-medium theme-text mb-1">Code</label>
                <input type="text" value={formData.code} onChange={(e) => setFormData({ ...formData, code: e.target.value.toLowerCase().replace(/\s+/g, '_') })} disabled={dialogMode === 'edit'} className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500 disabled:opacity-50" placeholder="Unique identifier (lowercase, underscores)" />
              </div>
              <div>
                <label className="block text-sm font-medium theme-text mb-1">Name</label>
                <input type="text" value={formData.name} onChange={(e) => setFormData({ ...formData, name: e.target.value })} className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500" autoFocus />
              </div>
              <div>
                <label className="block text-sm font-medium theme-text mb-1">Description</label>
                <textarea value={formData.description} onChange={(e) => setFormData({ ...formData, description: e.target.value })} rows={2} className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500 resize-none" />
              </div>
              {formData.kind === 'business_process_definition' && (
                <div>
                  <label className="block text-sm font-medium theme-text mb-1">Process Type</label>
                  <select value={formData.process_type} onChange={(e) => setFormData({ ...formData, process_type: e.target.value })} className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500">
                    <option value="core">Core</option>
                    <option value="support">Support</option>
                    <option value="management">Management</option>
                  </select>
                </div>
              )}
              {formData.kind === 'metric_definition' && (
                <>
                  <div>
                    <label className="block text-sm font-medium theme-text mb-1">Formula</label>
                    <textarea value={formData.formula} onChange={(e) => setFormData({ ...formData, formula: e.target.value })} rows={2} className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500 resize-none" placeholder="Natural language formula description" />
                  </div>
                  <div>
                    <label className="block text-sm font-medium theme-text mb-1">Unit</label>
                    <input type="text" value={formData.unit} onChange={(e) => setFormData({ ...formData, unit: e.target.value })} className="w-full px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500" placeholder="e.g., %, USD, count" />
                  </div>
                </>
              )}
            </div>
            <div className="p-4 border-t theme-border flex justify-end gap-2">
              <Button variant="outline" onClick={() => { setAddDialogOpen(false); setEditDialogOpen(false); }}>Cancel</Button>
              <Button onClick={handleSave} disabled={!formData.code || !formData.name}>{dialogMode === 'add' ? 'Create' : 'Save'}</Button>
            </div>
          </div>
        </div>
      )}

      {/* Delete Confirmation Dialog */}
      {deleteDialogOpen && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="w-full max-w-sm rounded-xl theme-card-bg border theme-border shadow-2xl">
            <div className="p-4 border-b theme-border"><h2 className="text-lg font-semibold theme-text-title">Confirm Delete</h2></div>
            <div className="p-4">
              <p className="theme-text">Are you sure you want to delete "{selectedNode?.name}"?</p>
              <p className="text-sm theme-text-muted mt-1">This action cannot be undone.</p>
            </div>
            <div className="p-4 border-t theme-border flex justify-end gap-2">
              <Button variant="outline" onClick={() => setDeleteDialogOpen(false)}>Cancel</Button>
              <Button className="bg-red-500 hover:bg-red-600" onClick={handleDelete}>Delete</Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
