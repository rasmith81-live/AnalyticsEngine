import { useState, useMemo } from 'react';
import {
  Box,
  Typography,
  Paper,
  TextField,
  Checkbox,
  Chip,
  IconButton,
  Collapse,
  InputAdornment,
  Badge,
  Tooltip,
  Stack,
} from '@mui/material';
import {
  ExpandMore as ExpandIcon,
  ChevronRight as CollapseIcon,
  Search as SearchIcon,
  AccountTree as ValueChainIcon,
  Folder as ModuleIcon,
  Functions as KPIIcon,
  Clear as ClearIcon,
} from '@mui/icons-material';

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

export default function KPITreeSelector({
  kpis,
  selectedKPIs,
  onSelectionChange,
  loading = false,
}: KPITreeSelectorProps) {
  const [searchTerm, setSearchTerm] = useState('');
  const [expandedNodes, setExpandedNodes] = useState<Set<string>>(new Set());

  // Build hierarchical tree from flat KPI list
  const treeData = useMemo(() => {
    const valueChainMap = new Map<string, Map<string, KPIInfo[]>>();

    // Filter KPIs based on search
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

    // Group by value chain -> module -> KPIs
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

    // Convert to tree structure
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

      // Sort modules alphabetically
      moduleNodes.sort((a, b) => a.label.localeCompare(b.label));

      tree.push({
        id: valueChain,
        label: valueChain,
        type: 'value_chain',
        kpiCount: vcKpiCount,
        children: moduleNodes,
      });
    });

    // Sort value chains alphabetically
    tree.sort((a, b) => a.label.localeCompare(b.label));

    return tree;
  }, [kpis, searchTerm]);

  // Auto-expand when searching
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
      // Deselect all in module
      const moduleCodes = new Set(moduleKPIs.map((k) => k.code));
      onSelectionChange(selectedKPIs.filter((s) => !moduleCodes.has(s.code)));
    } else {
      // Select all in module
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
      <Box
        key={node.id}
        sx={{
          display: 'flex',
          alignItems: 'center',
          py: 0.5,
          px: 1,
          pl: depth * 3 + 1,
          cursor: 'pointer',
          borderRadius: 1,
          bgcolor: selected ? 'primary.50' : 'transparent',
          '&:hover': { bgcolor: selected ? 'primary.100' : 'grey.100' },
        }}
        onClick={() => toggleKPI(kpi)}
      >
        <Checkbox
          size="small"
          checked={selected}
          sx={{ p: 0.5, mr: 1 }}
        />
        <KPIIcon sx={{ fontSize: 16, mr: 1, color: 'text.secondary' }} />
        <Box sx={{ flex: 1, minWidth: 0 }}>
          <Typography variant="body2" noWrap>
            {kpi.name}
          </Typography>
          <Typography variant="caption" color="text.secondary" noWrap>
            {kpi.code} • {kpi.calculation_type}
            {kpi.required_objects.length > 0 && ` • ${kpi.required_objects.length} entities`}
          </Typography>
        </Box>
        {kpi.calculation_type === 'set_based' && (
          <Chip size="small" label="Set-Based" color="primary" sx={{ ml: 1, height: 20 }} />
        )}
      </Box>
    );
  };

  const renderModuleNode = (node: TreeNode, depth: number) => {
    const isExpanded = expandedNodes.has(node.id);
    const selectionState = getModuleSelectionState(node);

    return (
      <Box key={node.id}>
        <Box
          sx={{
            display: 'flex',
            alignItems: 'center',
            py: 0.75,
            px: 1,
            pl: depth * 3 + 1,
            cursor: 'pointer',
            borderRadius: 1,
            '&:hover': { bgcolor: 'grey.100' },
          }}
        >
          <IconButton size="small" onClick={() => toggleNode(node.id)} sx={{ p: 0.25, mr: 0.5 }}>
            {isExpanded ? <ExpandIcon fontSize="small" /> : <CollapseIcon fontSize="small" />}
          </IconButton>
          <Checkbox
            size="small"
            checked={selectionState === 'all'}
            indeterminate={selectionState === 'some'}
            onClick={(e) => {
              e.stopPropagation();
              selectAllInModule(node);
            }}
            sx={{ p: 0.5, mr: 1 }}
          />
          <ModuleIcon sx={{ fontSize: 18, mr: 1, color: 'warning.main' }} />
          <Typography
            variant="body2"
            fontWeight={500}
            sx={{ flex: 1, cursor: 'pointer' }}
            onClick={() => toggleNode(node.id)}
          >
            {node.label}
          </Typography>
          <Badge badgeContent={node.kpiCount} color="default" sx={{ mr: 1 }}>
            <Box />
          </Badge>
        </Box>
        <Collapse in={isExpanded}>
          {node.children?.map((child) => renderKPINode(child, depth + 1))}
        </Collapse>
      </Box>
    );
  };

  const renderValueChainNode = (node: TreeNode) => {
    const isExpanded = expandedNodes.has(node.id);
    const selectionState = getValueChainSelectionState(node);

    return (
      <Box key={node.id} sx={{ mb: 1 }}>
        <Box
          sx={{
            display: 'flex',
            alignItems: 'center',
            py: 1,
            px: 1,
            cursor: 'pointer',
            borderRadius: 1,
            bgcolor: 'grey.50',
            '&:hover': { bgcolor: 'grey.100' },
          }}
        >
          <IconButton size="small" onClick={() => toggleNode(node.id)} sx={{ p: 0.25, mr: 0.5 }}>
            {isExpanded ? <ExpandIcon /> : <CollapseIcon />}
          </IconButton>
          <Checkbox
            size="small"
            checked={selectionState === 'all'}
            indeterminate={selectionState === 'some'}
            onClick={(e) => {
              e.stopPropagation();
              selectAllInValueChain(node);
            }}
            sx={{ p: 0.5, mr: 1 }}
          />
          <ValueChainIcon sx={{ fontSize: 20, mr: 1, color: 'primary.main' }} />
          <Typography
            variant="subtitle2"
            fontWeight={600}
            sx={{ flex: 1, cursor: 'pointer' }}
            onClick={() => toggleNode(node.id)}
          >
            {node.label}
          </Typography>
          <Chip
            size="small"
            label={`${node.kpiCount} KPIs`}
            variant="outlined"
            sx={{ height: 24 }}
          />
        </Box>
        <Collapse in={isExpanded}>
          <Box sx={{ ml: 1, borderLeft: '2px solid', borderColor: 'grey.200', pl: 1 }}>
            {node.children?.map((child) => renderModuleNode(child, 1))}
          </Box>
        </Collapse>
      </Box>
    );
  };

  return (
    <Paper variant="outlined" sx={{ p: 2 }}>
      <Box sx={{ mb: 2 }}>
        <Typography variant="subtitle1" fontWeight={600} gutterBottom>
          Select KPIs
        </Typography>
        <TextField
          fullWidth
          size="small"
          placeholder="Search KPIs by name, code, or description..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <SearchIcon fontSize="small" color="action" />
              </InputAdornment>
            ),
            endAdornment: searchTerm && (
              <InputAdornment position="end">
                <IconButton size="small" onClick={() => setSearchTerm('')}>
                  <ClearIcon fontSize="small" />
                </IconButton>
              </InputAdornment>
            ),
          }}
        />
      </Box>

      {/* Selected KPIs summary */}
      {selectedKPIs.length > 0 && (
        <Box sx={{ mb: 2, p: 1.5, bgcolor: 'primary.50', borderRadius: 1 }}>
          <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 1 }}>
            <Typography variant="body2" fontWeight={500} color="primary.main">
              {selectedKPIs.length} KPI{selectedKPIs.length !== 1 ? 's' : ''} selected
            </Typography>
            <Tooltip title="Clear all">
              <IconButton size="small" onClick={() => onSelectionChange([])}>
                <ClearIcon fontSize="small" />
              </IconButton>
            </Tooltip>
          </Stack>
          <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
            {selectedKPIs.slice(0, 10).map((kpi) => (
              <Chip
                key={kpi.code}
                label={kpi.code}
                size="small"
                onDelete={() => toggleKPI(kpi)}
                color={kpi.calculation_type === 'set_based' ? 'primary' : 'default'}
              />
            ))}
            {selectedKPIs.length > 10 && (
              <Chip
                label={`+${selectedKPIs.length - 10} more`}
                size="small"
                variant="outlined"
              />
            )}
          </Box>
        </Box>
      )}

      {/* Tree view */}
      <Box
        sx={{
          maxHeight: 400,
          overflow: 'auto',
          border: '1px solid',
          borderColor: 'grey.200',
          borderRadius: 1,
          p: 1,
        }}
      >
        {loading ? (
          <Typography color="text.secondary" sx={{ p: 2, textAlign: 'center' }}>
            Loading KPIs...
          </Typography>
        ) : treeData.length === 0 ? (
          <Typography color="text.secondary" sx={{ p: 2, textAlign: 'center' }}>
            {searchTerm ? 'No KPIs match your search' : 'No KPIs available'}
          </Typography>
        ) : (
          treeData.map((node) => renderValueChainNode(node))
        )}
      </Box>

      {/* Stats */}
      <Box sx={{ mt: 1, display: 'flex', justifyContent: 'space-between' }}>
        <Typography variant="caption" color="text.secondary">
          {kpis.length} total KPIs across {new Set(kpis.map((k) => k.value_chain)).size} value chains
        </Typography>
        {searchTerm && (
          <Typography variant="caption" color="text.secondary">
            Showing {treeData.reduce((sum, vc) => sum + (vc.kpiCount || 0), 0)} results
          </Typography>
        )}
      </Box>
    </Paper>
  );
}
