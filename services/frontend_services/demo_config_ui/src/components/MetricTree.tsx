/**
 * MetricTree Component
 * Main tree component that renders either Industry or Value Chain mode
 */

import { Box, CircularProgress, Alert, TextField, InputAdornment, IconButton } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import ClearIcon from '@mui/icons-material/Clear';
import { useValueChainTree } from '../hooks/useValueChainTree';
import { useCart } from '../contexts/CartContext';
import ValueChainNode from './ValueChainNode';
import type { TreeMode } from '../types/metricTree';

interface MetricTreeProps {
  mode: TreeMode;
  onKPIToggleCart?: (kpiCode: string) => void;
  onKPIViewDetails?: (kpiCode: string) => void;
  selectedKPIs?: string[];
  currentViewKPI?: string | null;
}

export default function MetricTree({ 
  mode, 
  onKPIToggleCart, 
  onKPIViewDetails, 
  selectedKPIs = [],
  currentViewKPI = null 
}: MetricTreeProps) {
  const { treeExpandedNodes, setTreeExpandedNodes, treeSearchQuery, setTreeSearchQuery } = useCart();

  // Fetch data based on mode
  const { data: valueChains, isLoading, error } = useValueChainTree();

  const handleNodeToggle = (nodeId: string) => {
    setTreeExpandedNodes(
      treeExpandedNodes.includes(nodeId)
        ? treeExpandedNodes.filter((id: string) => id !== nodeId)
        : [...treeExpandedNodes, nodeId]
    );
  };

  const handleKPIToggleCart = (kpiCode: string) => {
    if (onKPIToggleCart) {
      onKPIToggleCart(kpiCode);
    }
  };

  const handleKPIViewDetails = (kpiCode: string) => {
    if (onKPIViewDetails) {
      onKPIViewDetails(kpiCode);
    }
  };

  // Filter value chains based on search - search through all levels
  const filteredValueChains = valueChains?.filter(vc => {
    if (treeSearchQuery === '') return true;
    
    const query = treeSearchQuery.toLowerCase();
    
    // Check value chain name
    if (vc.name?.toLowerCase().includes(query) || 
        vc.display_name?.toLowerCase().includes(query)) {
      return true;
    }
    
    // Check modules and KPIs
    return vc.modules?.some(module => {
      // Check module name
      if (module.name?.toLowerCase().includes(query) ||
          module.display_name?.toLowerCase().includes(query)) {
        return true;
      }
      
      // Check KPIs in module
      return module.kpis?.some(kpi =>
        kpi.name?.toLowerCase().includes(query) ||
        kpi.display_name?.toLowerCase().includes(query) ||
        kpi.description?.toLowerCase().includes(query) ||
        kpi.code?.toLowerCase().includes(query)
      );
    });
  });

  if (isLoading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', p: 4 }}>
        <CircularProgress />
      </Box>
    );
  }

  if (error) {
    return (
      <Alert severity="error">
        Failed to load KPI tree. Please check if the metadata service is running.
      </Alert>
    );
  }

  if (!valueChains || valueChains.length === 0) {
    return (
      <Alert severity="info">
        No KPIs found. The metadata service may not have any data loaded.
      </Alert>
    );
  }

  return (
    <Box>
      {/* Search */}
      <TextField
        fullWidth
        size="small"
        placeholder={mode === 'industry' ? 'Search industries, value chains, modules, or KPIs...' : 'Search value chains, modules, or KPIs...'}
        value={treeSearchQuery}
        onChange={(e) => setTreeSearchQuery(e.target.value)}
        InputProps={{
          startAdornment: (
            <InputAdornment position="start">
              <SearchIcon />
            </InputAdornment>
          ),
          endAdornment: treeSearchQuery && (
            <InputAdornment position="end">
              <IconButton
                size="small"
                onClick={() => setTreeSearchQuery('')}
                edge="end"
                aria-label="clear search"
              >
                <ClearIcon fontSize="small" />
              </IconButton>
            </InputAdornment>
          ),
        }}
        sx={{ mb: 2 }}
      />

      {/* Tree */}
      <Box>
        {mode === 'value-chain' && filteredValueChains && (
          <Box>
            {filteredValueChains.map((valueChain) => (
              <ValueChainNode
                key={valueChain.code}
                valueChain={valueChain}
                expanded={treeExpandedNodes.includes(valueChain.code)}
                onToggle={() => handleNodeToggle(valueChain.code)}
                onKPIToggleCart={handleKPIToggleCart}
                onKPIViewDetails={handleKPIViewDetails}
                selectedKPIs={selectedKPIs}
                currentViewKPI={currentViewKPI}
                searchQuery={treeSearchQuery}
              />
            ))}
          </Box>
        )}

        {mode === 'industry' && (
          <Alert severity="info" sx={{ mt: 2 }}>
            Industry mode coming soon! For now, use "By Value Chain" tab.
          </Alert>
        )}
      </Box>

      {/* Summary */}
      {filteredValueChains && filteredValueChains.length > 0 && (
        <Box sx={{ mt: 2, p: 2, bgcolor: 'grey.50', borderRadius: 1 }}>
          <Box sx={{ fontSize: '0.875rem', color: 'text.secondary' }}>
            Showing {filteredValueChains.length} value chain{filteredValueChains.length !== 1 ? 's' : ''}
            {treeSearchQuery && ` matching "${treeSearchQuery}"`}
          </Box>
        </Box>
      )}
    </Box>
  );
}
