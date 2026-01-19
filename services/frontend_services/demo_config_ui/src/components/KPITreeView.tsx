import { useState, useEffect } from 'react';
import {
  ChevronDown,
  ChevronRight,
  Building2,
  Layers,
  BarChart3,
  Database,
  RefreshCw,
  Search,
  X,
  ShoppingCart,
} from 'lucide-react';
import { cn } from '../lib/utils';
import { Card } from './ui/Card';
import { Button } from './ui/Button';
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
  'value_chain_pattern_definition': 'text-green-500',
  'business_process_definition': 'text-blue-500',
  'metric_definition': 'text-amber-500',
  'entity_definition': 'text-purple-500',
};

const KIND_BORDER_COLORS: Record<string, string> = {
  'value_chain_pattern_definition': 'border-l-green-500',
  'business_process_definition': 'border-l-blue-500',
  'metric_definition': 'border-l-amber-500',
  'entity_definition': 'border-l-purple-500',
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

  useEffect(() => { fetchOntologyData(); }, []);

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
      const tree = buildTree(vcRes.data || [], modRes.data || [], kpiRes.data || [], entityRes.data || [], relRes.data || []);
      setTreeData(tree);
      setExpandedNodes(new Set(['root', ...tree.map(n => n.code)]));
    } catch (err) {
      console.error('Failed to fetch ontology data:', err);
      onSnackbar?.('Failed to fetch KPI data', 'error');
    } finally {
      setLoading(false);
    }
  };

  const buildTree = (valueChains: any[], modules: any[], kpis: any[], _entities: any[], relationships: Relationship[]): OntologyNode[] => {
    const modulesByCode = new Map(modules.map(m => [m.code.toLowerCase(), m]));
    const kpisByCode = new Map(kpis.map(k => [k.code.toLowerCase(), k]));
    const moduleToVC = new Map<string, string>();
    const kpiToModule = new Map<string, string>();
    const kpiToVC = new Map<string, string>();
    const kpiToEntities = new Map<string, Set<string>>();
    
    relationships.forEach(rel => {
      const fromLower = rel.from_entity_code.toLowerCase();
      const toLower = rel.to_entity_code.toLowerCase();
      if (rel.relationship_type === 'belongs_to' || rel.relationship_type === 'belongs_to_value_chain') {
        if (modulesByCode.has(fromLower)) moduleToVC.set(fromLower, toLower);
        if (kpisByCode.has(fromLower) && !modulesByCode.has(toLower)) kpiToVC.set(fromLower, toLower);
      }
      if (rel.relationship_type === 'belongs_to_module') kpiToModule.set(fromLower, toLower);
      if (rel.relationship_type === 'contains' && modulesByCode.has(fromLower) && kpisByCode.has(toLower)) kpiToModule.set(toLower, fromLower);
      if (rel.relationship_type === 'uses' || rel.relationship_type === 'uses_entity') {
        if (!kpiToEntities.has(fromLower)) kpiToEntities.set(fromLower, new Set());
        kpiToEntities.get(fromLower)!.add(toLower);
      }
    });
    
    const tree: OntologyNode[] = [];
    
    valueChains.forEach(vc => {
      const vcNode: OntologyNode = { id: vc.id, code: vc.code, name: vc.name, kind: 'value_chain_pattern_definition', description: vc.description, fields: { domain: vc.domain }, children: [] };
      modules.forEach(mod => {
        if (moduleToVC.get(mod.code.toLowerCase()) === vc.code.toLowerCase()) {
          const modNode: OntologyNode = { id: mod.id, code: mod.code, name: mod.name, kind: 'business_process_definition', description: mod.description, fields: { process_type: mod.process_type }, children: [] };
          kpis.forEach(kpi => {
            if (kpiToModule.get(kpi.code.toLowerCase()) === mod.code.toLowerCase()) {
              const kpiEntities = kpiToEntities.get(kpi.code.toLowerCase());
              modNode.children!.push({ id: kpi.id, code: kpi.code, name: kpi.name, kind: 'metric_definition', description: kpi.description, fields: { formula: kpi.formula, math_expression: kpi.math_expression, unit: kpi.unit, required_objects: kpi.required_objects, entities: kpiEntities ? Array.from(kpiEntities) : [] }, children: [] });
            }
          });
          vcNode.children!.push(modNode);
        }
      });
      kpis.forEach(kpi => {
        const kpiLower = kpi.code.toLowerCase();
        if (kpiToVC.get(kpiLower) === vc.code.toLowerCase() && !kpiToModule.has(kpiLower)) {
          const kpiEntities = kpiToEntities.get(kpiLower);
          vcNode.children!.push({ id: kpi.id, code: kpi.code, name: kpi.name, kind: 'metric_definition', description: kpi.description, fields: { formula: kpi.formula, math_expression: kpi.math_expression, unit: kpi.unit, required_objects: kpi.required_objects, entities: kpiEntities ? Array.from(kpiEntities) : [] }, children: [] });
        }
      });
      tree.push(vcNode);
    });
    
    const orphanModules: OntologyNode[] = [];
    modules.forEach(mod => {
      if (!moduleToVC.has(mod.code.toLowerCase())) {
        const modNode: OntologyNode = { id: mod.id, code: mod.code, name: mod.name, kind: 'business_process_definition', description: mod.description, fields: { process_type: mod.process_type }, children: [] };
        kpis.forEach(kpi => {
          if (kpiToModule.get(kpi.code.toLowerCase()) === mod.code.toLowerCase()) {
            const kpiEntities = kpiToEntities.get(kpi.code.toLowerCase());
            modNode.children!.push({ id: kpi.id, code: kpi.code, name: kpi.name, kind: 'metric_definition', description: kpi.description, fields: { formula: kpi.formula, math_expression: kpi.math_expression, unit: kpi.unit, required_objects: kpi.required_objects, entities: kpiEntities ? Array.from(kpiEntities) : [] }, children: [] });
          }
        });
        orphanModules.push(modNode);
      }
    });
    if (orphanModules.length > 0) tree.push({ code: '_orphan_modules', name: 'Unassigned Modules', kind: 'folder', children: orphanModules });
    
    const orphanKpis: OntologyNode[] = [];
    kpis.forEach(kpi => {
      const kpiLower = kpi.code.toLowerCase();
      if (!kpiToModule.has(kpiLower) && !kpiToVC.has(kpiLower)) {
        const kpiEntities = kpiToEntities.get(kpiLower);
        orphanKpis.push({ id: kpi.id, code: kpi.code, name: kpi.name, kind: 'metric_definition', description: kpi.description, fields: { formula: kpi.formula, math_expression: kpi.math_expression, unit: kpi.unit, required_objects: kpi.required_objects, entities: kpiEntities ? Array.from(kpiEntities) : [] }, children: [] });
      }
    });
    if (orphanKpis.length > 0) tree.push({ code: '_orphan_kpis', name: 'Unassigned KPIs', kind: 'folder', children: orphanKpis });
    
    return tree;
  };

  const toggleNode = (code: string) => {
    setExpandedNodes(prev => {
      const next = new Set(prev);
      if (next.has(code)) next.delete(code);
      else next.add(code);
      return next;
    });
  };

  const handleNodeClick = (node: OntologyNode) => {
    setSelectedNode(node);
    if (node.kind === 'metric_definition' && onKPIViewDetails) onKPIViewDetails(node.code);
  };

  const handleCartToggle = (kpiCode: string, e: React.MouseEvent) => {
    e.stopPropagation();
    onKPIToggleCart?.(kpiCode);
  };

  const getIcon = (kind: string) => {
    const colorClass = KIND_COLORS[kind] || 'theme-text-muted';
    switch (kind) {
      case 'value_chain_pattern_definition': return <Building2 className={cn("w-4 h-4", colorClass)} />;
      case 'business_process_definition': return <Layers className={cn("w-4 h-4", colorClass)} />;
      case 'metric_definition': return <BarChart3 className={cn("w-4 h-4", colorClass)} />;
      case 'entity_definition': return <Database className={cn("w-4 h-4", colorClass)} />;
      default: return <ChevronRight className="w-4 h-4 theme-text-muted" />;
    }
  };

  const filterTree = (nodes: OntologyNode[], query: string): OntologyNode[] => {
    if (!query) return nodes;
    const lowerQuery = query.toLowerCase();
    return nodes.reduce<OntologyNode[]>((acc, node) => {
      const matches = node.name?.toLowerCase().includes(lowerQuery) || node.code?.toLowerCase().includes(lowerQuery) || node.description?.toLowerCase().includes(lowerQuery);
      const filteredChildren = node.children ? filterTree(node.children, query) : [];
      if (matches || filteredChildren.length > 0) acc.push({ ...node, children: filteredChildren.length > 0 ? filteredChildren : node.children });
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
      <div key={node.code}>
        <div
          className={cn(
            "flex items-center py-1.5 px-2 cursor-pointer transition-colors hover:bg-alpha-faded-50 dark:hover:bg-alpha-faded-900",
            isSelected && "bg-alpha-500/10",
            !isFolder && "border-l-2",
            !isFolder && KIND_BORDER_COLORS[node.kind]
          )}
          style={{ paddingLeft: `${depth * 20 + 8}px` }}
          onClick={() => handleNodeClick(node)}
        >
          <div className="w-6 flex-shrink-0">
            {hasChildren ? (
              <button onClick={(e) => { e.stopPropagation(); toggleNode(node.code); }} className="p-0.5 hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 rounded">
                {isExpanded ? <ChevronDown className="w-4 h-4 theme-text-muted" /> : <ChevronRight className="w-4 h-4 theme-text-muted" />}
              </button>
            ) : null}
          </div>
          <div className="w-6 flex-shrink-0">{getIcon(node.kind)}</div>
          <div className="flex-1 min-w-0 flex items-center gap-1">
            <span className={cn("text-sm truncate", isSelected ? "font-semibold theme-text-title" : "theme-text")}>{node.name}</span>
            {hasChildren && !isKPI && (
              <span className="px-1.5 py-0.5 rounded text-[10px] theme-card-bg border theme-border theme-text-muted">{countKPIs(node.children || [])}</span>
            )}
          </div>
          {isKPI && (
            <button
              onClick={(e) => handleCartToggle(node.code, e)}
              className={cn("p-1 rounded transition-colors", isInCart ? "text-alpha-500" : "theme-text-muted hover:text-alpha-500")}
              title={isInCart ? "Remove from cart" : "Add to cart"}
            >
              <ShoppingCart className="w-4 h-4" />
            </button>
          )}
        </div>
        {hasChildren && isExpanded && (
          <div>{node.children!.map(child => renderTreeNode(child, depth + 1))}</div>
        )}
      </div>
    );
  };

  const renderDetailsPanel = () => {
    if (!selectedNode || selectedNode.kind === 'folder') {
      return <div className="p-4 text-center theme-text-muted">Select a KPI to view details</div>;
    }
    const isKPI = selectedNode.kind === 'metric_definition';
    const isInCart = isKPI && selectedKPIs.includes(selectedNode.code);

    return (
      <div className="p-4 space-y-4">
        <div className="flex items-center gap-2">
          {getIcon(selectedNode.kind)}
          <h3 className="font-semibold theme-text-title flex-1 truncate">{selectedNode.name}</h3>
          {isKPI && (
            <span className={cn("px-2 py-0.5 rounded-full text-xs", isInCart ? "bg-alpha-500/20 text-alpha-400" : "theme-card-bg border theme-border theme-text-muted")}>
              {isInCart ? "In Cart" : "Not in Cart"}
            </span>
          )}
        </div>
        <div className="border-t theme-border" />
        <div className="space-y-3 text-sm">
          <div><p className="text-xs theme-text-muted">Code</p><p className="font-mono theme-text">{selectedNode.code}</p></div>
          <div><p className="text-xs theme-text-muted">Type</p><p className="theme-text">{selectedNode.kind === 'value_chain_pattern_definition' ? 'Value Chain' : selectedNode.kind === 'business_process_definition' ? 'Module' : selectedNode.kind === 'metric_definition' ? 'KPI/Metric' : selectedNode.kind}</p></div>
          {selectedNode.description && <div><p className="text-xs theme-text-muted">Description</p><p className="theme-text">{selectedNode.description}</p></div>}
          {selectedNode.fields?.formula && <div><p className="text-xs theme-text-muted">Formula</p><p className="theme-text italic">{selectedNode.fields.formula}</p></div>}
          {selectedNode.fields?.math_expression && <div><p className="text-xs theme-text-muted">Math Expression</p><p className="font-mono text-xs p-2 rounded-lg theme-card-bg border theme-border">{selectedNode.fields.math_expression}</p></div>}
          {selectedNode.fields?.unit && <div><p className="text-xs theme-text-muted">Unit</p><p className="theme-text">{selectedNode.fields.unit}</p></div>}
          {(selectedNode.fields?.required_objects?.length ?? 0) > 0 && (
            <div>
              <p className="text-xs theme-text-muted mb-1">Required Entities</p>
              <div className="flex flex-wrap gap-1">{selectedNode.fields!.required_objects.map((obj: string) => <span key={obj} className="px-2 py-0.5 rounded-full text-xs border theme-border theme-text">{obj}</span>)}</div>
            </div>
          )}
          {(selectedNode.fields?.entities?.length ?? 0) > 0 && (
            <div>
              <p className="text-xs theme-text-muted mb-1">Linked Entities</p>
              <div className="flex flex-wrap gap-1">{selectedNode.fields!.entities.map((entity: string) => <span key={entity} className="px-2 py-0.5 rounded-full text-xs bg-purple-500/20 text-purple-400 border border-purple-500/30">{entity}</span>)}</div>
            </div>
          )}
        </div>
        {isKPI && (
          <Button variant={isInCart ? "outline" : "primary"} size="sm" onClick={() => onKPIToggleCart?.(selectedNode.code)}>
            <ShoppingCart className="w-4 h-4 mr-2" />
            {isInCart ? 'Remove from Cart' : 'Add to Cart'}
          </Button>
        )}
      </div>
    );
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center p-8 h-full">
        <RefreshCw className="w-5 h-5 text-alpha-500 animate-spin mr-2" />
        <span className="theme-text-muted">Loading KPIs...</span>
      </div>
    );
  }

  return (
    <div className="flex gap-4 h-full">
      {/* Tree Panel */}
      <Card className="flex-[2] overflow-hidden flex flex-col">
        <div className="p-3 flex items-center justify-between border-b theme-border">
          <h3 className="font-semibold theme-text-title">KPI Hierarchy</h3>
          <button onClick={fetchOntologyData} className="p-1.5 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800" title="Refresh">
            <RefreshCw className="w-4 h-4 theme-text-muted" />
          </button>
        </div>
        <div className="p-2 border-b theme-border">
          <div className="relative">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 theme-text-muted" />
            <input
              type="text"
              placeholder="Search KPIs..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-9 pr-8 py-2 rounded-lg theme-card-bg border theme-border theme-text text-sm focus:outline-none focus:ring-2 focus:ring-alpha-500"
            />
            {searchQuery && (
              <button onClick={() => setSearchQuery('')} className="absolute right-2 top-1/2 -translate-y-1/2 p-1 hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 rounded">
                <X className="w-4 h-4 theme-text-muted" />
              </button>
            )}
          </div>
        </div>
        <div className="flex-1 overflow-auto">
          {filteredTreeData.length === 0 ? (
            <div className="p-4 text-center">
              <div className="p-3 rounded-xl bg-blue-500/10 border border-blue-500/30 text-blue-400 text-sm">
                {searchQuery ? 'No KPIs match your search.' : 'No KPI data found.'}
              </div>
            </div>
          ) : (
            <div>{filteredTreeData.map(node => renderTreeNode(node))}</div>
          )}
        </div>
        <div className="p-2 border-t theme-border theme-card-bg">
          <p className="text-xs theme-text-muted">{countKPIs(treeData)} KPIs total • {selectedKPIs.length} in cart</p>
        </div>
      </Card>
      
      {/* Details Panel */}
      <Card className="flex-1 min-w-[280px] overflow-auto">
        <div className="p-3 border-b theme-border">
          <h3 className="font-semibold theme-text-title">Details</h3>
        </div>
        {renderDetailsPanel()}
      </Card>
    </div>
  );
}
