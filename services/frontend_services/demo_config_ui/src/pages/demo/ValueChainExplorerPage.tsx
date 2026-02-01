import { useState, useMemo } from 'react';
import { Search, GitBranch, ChevronRight, ChevronDown, Home, Folder, FolderOpen, Target, ArrowLeft, Loader2, Database, RefreshCw } from 'lucide-react';
import { useValueChainTree } from '../../hooks/useValueChainTree';
import type { ValueChain } from '../../types/metricTree';

interface TreeNode {
  id: string;
  name: string;
  type: 'root' | 'value-chain' | 'module' | 'kpi';
  children?: TreeNode[];
  kpiCount?: number;
  description?: string;
  source?: 'reference' | 'customer';
}

function buildTreeFromValueChains(valueChains: ValueChain[]): TreeNode {
  const totalKpis = valueChains.reduce((sum, vc) => 
    sum + (vc.modules?.reduce((mSum, m) => mSum + (m.kpi_count || m.kpis?.length || 0), 0) || 0), 0
  );

  return {
    id: 'root',
    name: 'Value Chain Library',
    type: 'root',
    kpiCount: totalKpis,
    children: valueChains.map((vc) => ({
      id: vc.code,
      name: vc.display_name || vc.name,
      type: 'value-chain' as const,
      description: vc.description,
      kpiCount: vc.modules?.reduce((sum, m) => sum + (m.kpi_count || m.kpis?.length || 0), 0) || 0,
      source: 'reference' as const,
      children: vc.modules?.map((module) => ({
        id: module.code,
        name: module.display_name || module.name,
        type: 'module' as const,
        description: module.description,
        kpiCount: module.kpi_count || module.kpis?.length || 0,
        children: module.kpis?.map((kpi) => ({
          id: kpi.code,
          name: kpi.display_name || kpi.name,
          type: 'kpi' as const,
          description: kpi.description,
          kpiCount: 1,
        })),
      })),
    })),
  };
}

export default function ValueChainExplorerPage() {
  const { data: valueChains, isLoading, error, refetch } = useValueChainTree();
  
  const treeData = useMemo(() => {
    if (!valueChains || valueChains.length === 0) {
      return {
        id: 'root',
        name: 'Value Chain Library',
        type: 'root' as const,
        kpiCount: 0,
        children: [],
      };
    }
    return buildTreeFromValueChains(valueChains);
  }, [valueChains]);

  const [searchTerm, setSearchTerm] = useState('');
  const [currentNode, setCurrentNode] = useState<TreeNode | null>(null);
  const [breadcrumbs, setBreadcrumbs] = useState<TreeNode[]>([]);
  const [expandedNodes, setExpandedNodes] = useState<Set<string>>(new Set());

  // Initialize current node when data loads
  useMemo(() => {
    if (treeData && !currentNode) {
      setCurrentNode(treeData);
      setBreadcrumbs([treeData]);
    }
  }, [treeData, currentNode]);

  const drillDown = (node: TreeNode) => {
    // Allow drilling into any node including KPIs (leaf nodes)
    setCurrentNode(node);
    setBreadcrumbs([...breadcrumbs, node]);
  };

  const navigateTo = (index: number) => {
    const newBreadcrumbs = breadcrumbs.slice(0, index + 1);
    setBreadcrumbs(newBreadcrumbs);
    setCurrentNode(newBreadcrumbs[newBreadcrumbs.length - 1]);
  };

  const goBack = () => {
    if (breadcrumbs.length > 1) {
      const newBreadcrumbs = breadcrumbs.slice(0, -1);
      setBreadcrumbs(newBreadcrumbs);
      setCurrentNode(newBreadcrumbs[newBreadcrumbs.length - 1]);
    }
  };

  const toggleExpand = (nodeId: string) => {
    setExpandedNodes((prev) => {
      const next = new Set(prev);
      if (next.has(nodeId)) {
        next.delete(nodeId);
      } else {
        next.add(nodeId);
      }
      return next;
    });
  };

  const filteredChildren = currentNode?.children?.filter(
    (child) => child.name.toLowerCase().includes(searchTerm.toLowerCase())
  ) || [];

  const getTypeLabel = (type: string) => {
    switch (type) {
      case 'root': return 'Library';
      case 'value-chain': return 'Value Chain';
      case 'module': return 'Module';
      case 'kpi': return 'KPI';
      default: return type;
    }
  };

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-96">
        <div className="text-center">
          <Loader2 className="w-12 h-12 animate-spin text-alpha-400 mx-auto mb-4" />
          <p className="theme-text-secondary">Loading value chains from metadata library...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center h-96">
        <div className="text-center">
          <Database className="w-12 h-12 text-red-400 mx-auto mb-4" />
          <p className="theme-text-title mb-2">Failed to load value chains</p>
          <p className="theme-text-muted text-sm mb-4">Make sure the metadata service is running</p>
          <button
            onClick={() => refetch()}
            className="px-4 py-2 rounded-lg bg-alpha-500 hover:bg-alpha-600 text-white flex items-center gap-2 mx-auto"
          >
            <RefreshCw className="w-4 h-4" />
            Retry
          </button>
        </div>
      </div>
    );
  }

  if (!currentNode) {
    return (
      <div className="flex items-center justify-center h-96">
        <Loader2 className="w-8 h-8 animate-spin text-alpha-400" />
      </div>
    );
  }

  const renderTreeItem = (node: TreeNode, depth: number = 0) => {
    const hasChildren = node.children && node.children.length > 0;
    const isExpanded = expandedNodes.has(node.id);

    return (
      <div key={node.id} className="select-none">
        <div
          className={`flex items-center gap-2 px-3 py-2 rounded-lg cursor-pointer transition-colors hover:bg-[var(--card-hover)] ${
            depth > 0 ? 'ml-' + (depth * 4) : ''
          }`}
          style={{ marginLeft: depth * 16 }}
          onClick={() => hasChildren && toggleExpand(node.id)}
          onDoubleClick={() => drillDown(node)}
        >
          {hasChildren ? (
            isExpanded ? (
              <ChevronDown className="w-4 h-4 text-alpha-400 flex-shrink-0" />
            ) : (
              <ChevronRight className="w-4 h-4 theme-text-muted flex-shrink-0" />
            )
          ) : (
            <Target className="w-4 h-4 theme-text-muted flex-shrink-0" />
          )}
          
          {hasChildren ? (
            isExpanded ? (
              <FolderOpen className="w-5 h-5 text-amber-400 flex-shrink-0" />
            ) : (
              <Folder className="w-5 h-5 text-amber-400 flex-shrink-0" />
            )
          ) : (
            <div className="w-5 h-5" />
          )}
          
          <span className="flex-1 theme-text-title text-sm font-medium">{node.name}</span>
          
          {node.kpiCount && (
            <span className="px-2 py-0.5 rounded-full bg-alpha-500/10 text-alpha-400 text-xs">
              {node.kpiCount.toLocaleString()} KPIs
            </span>
          )}
          
          {hasChildren && (
            <button
              onClick={(e) => {
                e.stopPropagation();
                drillDown(node);
              }}
              className="px-2 py-1 rounded bg-alpha-500/10 hover:bg-alpha-500/20 text-alpha-400 text-xs transition-colors"
            >
              Drill Down →
            </button>
          )}
        </div>
        
        {isExpanded && hasChildren && (
          <div className="mt-1">
            {node.children!.map((child) => renderTreeItem(child, depth + 1))}
          </div>
        )}
      </div>
    );
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title">Value Chain Explorer</h1>
          <p className="mt-2 theme-text-secondary">
            Drill down through value chains to discover KPIs
          </p>
        </div>
        <div className="flex items-center gap-2 px-4 py-2 rounded-lg bg-alpha-500/10 text-alpha-400">
          <GitBranch className="w-5 h-5" />
          <span className="font-medium">Step 1 of 6</span>
        </div>
      </div>

      {/* Breadcrumb Navigation */}
      <div className="theme-card rounded-xl p-4">
        <div className="flex items-center gap-2 flex-wrap">
          {breadcrumbs.map((crumb, index) => (
            <div key={crumb.id} className="flex items-center gap-2">
              {index > 0 && <ChevronRight className="w-4 h-4 theme-text-muted" />}
              <button
                onClick={() => navigateTo(index)}
                className={`flex items-center gap-2 px-3 py-1.5 rounded-lg transition-colors ${
                  index === breadcrumbs.length - 1
                    ? 'bg-alpha-500/20 text-alpha-400'
                    : 'hover:bg-[var(--card-hover)] theme-text-secondary'
                }`}
              >
                {index === 0 ? <Home className="w-4 h-4" /> : <Folder className="w-4 h-4" />}
                <span className="text-sm font-medium">{crumb.name}</span>
              </button>
            </div>
          ))}
        </div>
      </div>

      {/* Main Content */}
      <div className="grid grid-cols-3 gap-6">
        {/* Left: Current Level Items */}
        <div className="col-span-2 theme-card rounded-2xl p-6">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-3">
              {breadcrumbs.length > 1 && (
                <button
                  onClick={goBack}
                  className="p-2 rounded-lg hover:bg-[var(--card-hover)] transition-colors"
                >
                  <ArrowLeft className="w-5 h-5 theme-text-muted" />
                </button>
              )}
              <div>
                <h2 className="text-xl font-semibold theme-text-title">{currentNode.name}</h2>
                <p className="text-sm theme-text-muted">
                  {getTypeLabel(currentNode.type)} • {currentNode.kpiCount?.toLocaleString()} KPIs
                </p>
              </div>
            </div>
            <div className="relative">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 theme-text-muted" />
              <input
                type="text"
                placeholder="Filter..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="pl-9 pr-4 py-2 rounded-lg theme-input text-sm w-48"
              />
            </div>
          </div>

          {/* Items Grid/List or KPI Detail */}
          {currentNode.type === 'kpi' ? (
            <div className="space-y-4">
              <div className="p-4 rounded-xl bg-alpha-500/10 border border-alpha-500/30">
                <div className="flex items-center gap-3 mb-3">
                  <Target className="w-6 h-6 text-alpha-400" />
                  <span className="text-xs font-medium text-alpha-400 uppercase tracking-wide">KPI Details</span>
                </div>
                <h3 className="text-lg font-semibold theme-text-title mb-2">{currentNode.name}</h3>
                <p className="text-sm theme-text-secondary mb-4">{currentNode.description || 'No description available'}</p>
                <div className="grid grid-cols-2 gap-4 text-sm">
                  <div>
                    <span className="theme-text-muted">Code:</span>
                    <span className="ml-2 font-mono theme-text-title">{currentNode.id}</span>
                  </div>
                  <div>
                    <span className="theme-text-muted">Type:</span>
                    <span className="ml-2 theme-text-title">Metric Definition</span>
                  </div>
                </div>
              </div>
              <p className="text-sm theme-text-muted text-center">
                This KPI can be selected for your analytics model in the AI Interview step.
              </p>
            </div>
          ) : filteredChildren.length > 0 ? (
            <div className="space-y-1 max-h-[500px] overflow-y-auto">
              {filteredChildren.map((child) => (
                <div
                  key={child.id}
                  onClick={() => child.type === 'kpi' ? drillDown(child) : drillDown(child)}
                  className="flex items-center gap-4 p-4 rounded-xl hover:bg-[var(--card-hover)] cursor-pointer transition-colors group"
                >
                  <div className="w-12 h-12 rounded-xl bg-alpha-500/10 flex items-center justify-center flex-shrink-0">
                    {child.type === 'kpi' ? (
                      <Target className="w-6 h-6 text-emerald-400" />
                    ) : child.children && child.children.length > 0 ? (
                      <Folder className="w-6 h-6 text-alpha-400" />
                    ) : (
                      <Target className="w-6 h-6 text-alpha-400" />
                    )}
                  </div>
                  <div className="flex-1 min-w-0">
                    <h3 className="font-semibold theme-text-title group-hover:text-alpha-400 transition-colors">
                      {child.name}
                    </h3>
                    <p className="text-sm theme-text-muted">
                      {getTypeLabel(child.type)}
                      {child.type !== 'kpi' && ` • ${child.kpiCount?.toLocaleString()} KPIs`}
                      {child.children && child.children.length > 0 && ` • ${child.children.length} sub-items`}
                    </p>
                    {child.description && (
                      <p className="text-xs theme-text-muted mt-1 truncate">{child.description}</p>
                    )}
                  </div>
                  <ChevronRight className="w-5 h-5 theme-text-muted group-hover:text-alpha-400 transition-colors" />
                </div>
              ))}
            </div>
          ) : (
            <div className="text-center py-12 theme-text-muted">
              <Target className="w-12 h-12 mx-auto mb-4 opacity-50" />
              <p>No items found</p>
            </div>
          )}
        </div>

        {/* Right: Tree View */}
        <div className="theme-card rounded-2xl p-6">
          <h3 className="font-semibold theme-text-title mb-4">Hierarchy View</h3>
          <div className="max-h-[500px] overflow-y-auto space-y-1">
            {treeData.children?.map((node) => renderTreeItem(node))}
          </div>
        </div>
      </div>

      {/* Navigation */}
      <div className="flex justify-end">
        <a
          href="/demo/training"
          className="px-6 py-3 rounded-xl bg-alpha-500 hover:bg-alpha-600 text-white font-medium transition-colors flex items-center gap-2"
        >
          Continue to Training Video
          <ChevronRight className="w-5 h-5" />
        </a>
      </div>
    </div>
  );
}
