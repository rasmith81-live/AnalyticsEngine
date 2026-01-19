import { useState, useMemo } from 'react';
import {
  ChevronDown,
  ChevronRight,
  Search,
  GitBranch,
  Folder,
  Calculator,
  X,
} from 'lucide-react';
import { cn } from '../lib/utils';

export interface KPIInfo {
  code: string;
  name: string;
  calculation_type: string;
  required_objects: string[];
  formula?: string;
  category?: string;
  value_chain?: string;
  module?: string;
  description?: string;
}

interface KPITreeSelectorProps {
  kpis: KPIInfo[];
  selectedKPIs: KPIInfo[];
  onSelectionChange: (selected: KPIInfo[]) => void;
  loading?: boolean;
}

interface TreeNode {
  id: string;
  label: string;
  type: 'value_chain' | 'module' | 'kpi';
  children?: TreeNode[];
  kpi?: KPIInfo;
  kpiCount?: number;
}

function Checkbox({ 
  checked, 
  indeterminate, 
  onChange 
}: { 
  checked: boolean; 
  indeterminate?: boolean; 
  onChange: () => void;
}) {
  return (
    <button
      onClick={(e) => { e.stopPropagation(); onChange(); }}
      className={cn(
        "w-4 h-4 rounded border-2 flex items-center justify-center transition-colors",
        checked 
          ? "bg-alpha-500 border-alpha-500" 
          : indeterminate 
            ? "bg-alpha-500/50 border-alpha-500" 
            : "border-gray-500 hover:border-alpha-400"
      )}
    >
      {checked && (
        <svg className="w-3 h-3 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
        </svg>
      )}
      {indeterminate && !checked && (
        <div className="w-2 h-0.5 bg-white rounded" />
      )}
    </button>
  );
}

export default function KPITreeSelector({
  kpis,
  selectedKPIs,
  onSelectionChange,
  loading = false,
}: KPITreeSelectorProps) {
  const [searchTerm, setSearchTerm] = useState('');
  const [expandedNodes, setExpandedNodes] = useState<Set<string>>(new Set());

  const treeData = useMemo(() => {
    const valueChainMap = new Map<string, Map<string, KPIInfo[]>>();

    const filteredKPIs = kpis.filter((kpi) => {
      if (!searchTerm) return true;
      const search = searchTerm.toLowerCase();
      return (
        kpi.code.toLowerCase().includes(search) ||
        kpi.name.toLowerCase().includes(search) ||
        kpi.description?.toLowerCase().includes(search) ||
        kpi.value_chain?.toLowerCase().includes(search) ||
        kpi.module?.toLowerCase().includes(search)
      );
    });

    filteredKPIs.forEach((kpi) => {
      const valueChain = kpi.value_chain || 'General';
      const module = kpi.module || 'Uncategorized';

      if (!valueChainMap.has(valueChain)) {
        valueChainMap.set(valueChain, new Map());
      }
      const moduleMap = valueChainMap.get(valueChain)!;

      if (!moduleMap.has(module)) {
        moduleMap.set(module, []);
      }
      moduleMap.get(module)!.push(kpi);
    });

    const tree: TreeNode[] = [];
    valueChainMap.forEach((moduleMap, valueChain) => {
      const moduleNodes: TreeNode[] = [];
      let vcKpiCount = 0;

      moduleMap.forEach((kpiList, module) => {
        vcKpiCount += kpiList.length;
        moduleNodes.push({
          id: `${valueChain}/${module}`,
          label: module,
          type: 'module',
          kpiCount: kpiList.length,
          children: kpiList.map((kpi) => ({
            id: kpi.code,
            label: kpi.name,
            type: 'kpi' as const,
            kpi,
          })),
        });
      });

      moduleNodes.sort((a, b) => a.label.localeCompare(b.label));

      tree.push({
        id: valueChain,
        label: valueChain,
        type: 'value_chain',
        kpiCount: vcKpiCount,
        children: moduleNodes,
      });
    });

    tree.sort((a, b) => a.label.localeCompare(b.label));
    return tree;
  }, [kpis, searchTerm]);

  useMemo(() => {
    if (searchTerm) {
      const allNodes = new Set<string>();
      treeData.forEach((vc) => {
        allNodes.add(vc.id);
        vc.children?.forEach((mod) => {
          allNodes.add(mod.id);
        });
      });
      setExpandedNodes(allNodes);
    }
  }, [searchTerm, treeData]);

  const toggleNode = (nodeId: string) => {
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

  const isKPISelected = (kpi: KPIInfo) => {
    return selectedKPIs.some((s) => s.code === kpi.code);
  };

  const toggleKPI = (kpi: KPIInfo) => {
    if (isKPISelected(kpi)) {
      onSelectionChange(selectedKPIs.filter((s) => s.code !== kpi.code));
    } else {
      onSelectionChange([...selectedKPIs, kpi]);
    }
  };

  const selectAllInModule = (moduleNode: TreeNode) => {
    const moduleKPIs = moduleNode.children?.map((n) => n.kpi!).filter(Boolean) || [];
    const allSelected = moduleKPIs.every((kpi) => isKPISelected(kpi));

    if (allSelected) {
      const moduleCodes = new Set(moduleKPIs.map((k) => k.code));
      onSelectionChange(selectedKPIs.filter((s) => !moduleCodes.has(s.code)));
    } else {
      const newSelection = [...selectedKPIs];
      moduleKPIs.forEach((kpi) => {
        if (!isKPISelected(kpi)) {
          newSelection.push(kpi);
        }
      });
      onSelectionChange(newSelection);
    }
  };

  const selectAllInValueChain = (vcNode: TreeNode) => {
    const vcKPIs: KPIInfo[] = [];
    vcNode.children?.forEach((mod) => {
      mod.children?.forEach((kpiNode) => {
        if (kpiNode.kpi) vcKPIs.push(kpiNode.kpi);
      });
    });

    const allSelected = vcKPIs.every((kpi) => isKPISelected(kpi));

    if (allSelected) {
      const vcCodes = new Set(vcKPIs.map((k) => k.code));
      onSelectionChange(selectedKPIs.filter((s) => !vcCodes.has(s.code)));
    } else {
      const newSelection = [...selectedKPIs];
      vcKPIs.forEach((kpi) => {
        if (!isKPISelected(kpi)) {
          newSelection.push(kpi);
        }
      });
      onSelectionChange(newSelection);
    }
  };

  const getModuleSelectionState = (moduleNode: TreeNode): 'none' | 'some' | 'all' => {
    const moduleKPIs = moduleNode.children?.map((n) => n.kpi!).filter(Boolean) || [];
    if (moduleKPIs.length === 0) return 'none';
    const selectedCount = moduleKPIs.filter((kpi) => isKPISelected(kpi)).length;
    if (selectedCount === 0) return 'none';
    if (selectedCount === moduleKPIs.length) return 'all';
    return 'some';
  };

  const getValueChainSelectionState = (vcNode: TreeNode): 'none' | 'some' | 'all' => {
    const states = vcNode.children?.map((mod) => getModuleSelectionState(mod)) || [];
    if (states.every((s) => s === 'all')) return 'all';
    if (states.every((s) => s === 'none')) return 'none';
    return 'some';
  };

  const renderKPINode = (node: TreeNode, depth: number) => {
    const kpi = node.kpi!;
    const selected = isKPISelected(kpi);

    return (
      <div
        key={node.id}
        onClick={() => toggleKPI(kpi)}
        className={cn(
          "flex items-center gap-2 py-1.5 px-2 rounded-lg cursor-pointer transition-colors",
          selected ? "bg-alpha-500/20" : "hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800"
        )}
        style={{ paddingLeft: `${depth * 24 + 8}px` }}
      >
        <Checkbox checked={selected} onChange={() => toggleKPI(kpi)} />
        <Calculator className="w-4 h-4 theme-text-muted flex-shrink-0" />
        <div className="flex-1 min-w-0">
          <p className="text-sm theme-text truncate">{kpi.name}</p>
          <p className="text-xs theme-text-muted truncate">
            {kpi.code} • {kpi.calculation_type}
            {kpi.required_objects.length > 0 && ` • ${kpi.required_objects.length} entities`}
          </p>
        </div>
        {kpi.calculation_type === 'set_based' && (
          <span className="px-2 py-0.5 rounded-full text-xs bg-alpha-500/20 text-alpha-400 flex-shrink-0">
            Set-Based
          </span>
        )}
      </div>
    );
  };

  const renderModuleNode = (node: TreeNode, depth: number) => {
    const isExpanded = expandedNodes.has(node.id);
    const selectionState = getModuleSelectionState(node);

    return (
      <div key={node.id}>
        <div
          className="flex items-center gap-2 py-2 px-2 rounded-lg cursor-pointer hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 transition-colors"
          style={{ paddingLeft: `${depth * 24 + 8}px` }}
        >
          <button onClick={() => toggleNode(node.id)} className="p-0.5">
            {isExpanded ? (
              <ChevronDown className="w-4 h-4 theme-text-muted" />
            ) : (
              <ChevronRight className="w-4 h-4 theme-text-muted" />
            )}
          </button>
          <Checkbox
            checked={selectionState === 'all'}
            indeterminate={selectionState === 'some'}
            onChange={() => selectAllInModule(node)}
          />
          <Folder className="w-4 h-4 text-amber-500 flex-shrink-0" />
          <span
            className="flex-1 text-sm font-medium theme-text cursor-pointer"
            onClick={() => toggleNode(node.id)}
          >
            {node.label}
          </span>
          <span className="text-xs theme-text-muted">{node.kpiCount}</span>
        </div>
        {isExpanded && (
          <div>
            {node.children?.map((child) => renderKPINode(child, depth + 1))}
          </div>
        )}
      </div>
    );
  };

  const renderValueChainNode = (node: TreeNode) => {
    const isExpanded = expandedNodes.has(node.id);
    const selectionState = getValueChainSelectionState(node);

    return (
      <div key={node.id} className="mb-2">
        <div className="flex items-center gap-2 py-2 px-2 rounded-lg theme-card-bg cursor-pointer hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 transition-colors">
          <button onClick={() => toggleNode(node.id)} className="p-0.5">
            {isExpanded ? (
              <ChevronDown className="w-4 h-4 theme-text-muted" />
            ) : (
              <ChevronRight className="w-4 h-4 theme-text-muted" />
            )}
          </button>
          <Checkbox
            checked={selectionState === 'all'}
            indeterminate={selectionState === 'some'}
            onChange={() => selectAllInValueChain(node)}
          />
          <GitBranch className="w-4 h-4 theme-info-icon flex-shrink-0" />
          <span
            className="flex-1 text-sm font-semibold theme-text-title cursor-pointer"
            onClick={() => toggleNode(node.id)}
          >
            {node.label}
          </span>
          <span className="px-2 py-0.5 rounded-full text-xs border theme-border theme-text-muted">
            {node.kpiCount} KPIs
          </span>
        </div>
        {isExpanded && (
          <div className="ml-4 border-l-2 border-alpha-faded-300 dark:border-alpha-faded-700 pl-2">
            {node.children?.map((child) => renderModuleNode(child, 1))}
          </div>
        )}
      </div>
    );
  };

  return (
    <div className="rounded-xl theme-card-bg border theme-border p-4">
      {/* Search */}
      <div className="relative mb-3">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 theme-text-muted" />
        <input
          type="text"
          placeholder="Search KPIs by name, code, or description..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="w-full h-10 pl-10 pr-10 rounded-lg theme-card-bg border theme-border
            focus:outline-none focus:ring-2 focus:ring-alpha-500 focus:border-transparent
            theme-text placeholder:theme-text-muted text-sm transition-all duration-200"
        />
        {searchTerm && (
          <button
            onClick={() => setSearchTerm('')}
            className="absolute right-3 top-1/2 -translate-y-1/2 p-1 rounded hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800"
          >
            <X className="w-4 h-4 theme-text-muted" />
          </button>
        )}
      </div>

      {/* Selected KPIs summary */}
      {selectedKPIs.length > 0 && (
        <div className="mb-3 p-3 rounded-lg bg-alpha-500/10 border border-alpha-500/30">
          <div className="flex items-center justify-between mb-2">
            <span className="text-sm font-medium theme-text-vibrant">
              {selectedKPIs.length} KPI{selectedKPIs.length !== 1 ? 's' : ''} selected
            </span>
            <button
              onClick={() => onSelectionChange([])}
              className="text-xs theme-text-muted hover:theme-text transition-colors"
            >
              Clear all
            </button>
          </div>
          <div className="flex flex-wrap gap-1.5">
            {selectedKPIs.slice(0, 10).map((kpi) => (
              <span
                key={kpi.code}
                className={cn(
                  "inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs",
                  kpi.calculation_type === 'set_based'
                    ? "bg-alpha-500/20 text-alpha-400"
                    : "theme-card-bg border theme-border theme-text"
                )}
              >
                {kpi.code}
                <button
                  onClick={() => toggleKPI(kpi)}
                  className="hover:text-red-400 transition-colors"
                >
                  <X className="w-3 h-3" />
                </button>
              </span>
            ))}
            {selectedKPIs.length > 10 && (
              <span className="px-2 py-0.5 rounded-full text-xs border theme-border theme-text-muted">
                +{selectedKPIs.length - 10} more
              </span>
            )}
          </div>
        </div>
      )}

      {/* Tree view */}
      <div className="max-h-80 overflow-y-auto rounded-lg border theme-border p-2">
        {loading ? (
          <p className="text-center py-8 theme-text-muted">Loading KPIs...</p>
        ) : treeData.length === 0 ? (
          <p className="text-center py-8 theme-text-muted">
            {searchTerm ? 'No KPIs match your search' : 'No KPIs available'}
          </p>
        ) : (
          treeData.map((node) => renderValueChainNode(node))
        )}
      </div>

      {/* Stats */}
      <div className="mt-2 flex justify-between text-xs theme-text-muted">
        <span>
          {kpis.length} total KPIs across {new Set(kpis.map((k) => k.value_chain)).size} value chains
        </span>
        {searchTerm && (
          <span>
            Showing {treeData.reduce((sum, vc) => sum + (vc.kpiCount || 0), 0)} results
          </span>
        )}
      </div>
    </div>
  );
}
