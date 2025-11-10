/**
 * MetricTree Component
 * Main tree component that renders either Industry or Value Chain mode
 */

import { Box, CircularProgress, Alert, TextField, InputAdornment } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import { useState } from 'react';
import { useValueChainTree } from '../hooks/useValueChainTree';
import ValueChainNode from './ValueChainNode';
import type { TreeMode } from '../types/metricTree';

interface MetricTreeProps {
  mode: TreeMode;
  onKPISelect?: (kpiCode: string) => void;
  selectedKPIs?: string[];
}

export default function MetricTree({ mode, onKPISelect, selectedKPIs = [] }: MetricTreeProps) {
  const [searchQuery, setSearchQuery] = useState('');
  const [expandedNodes, setExpandedNodes] = useState<string[]>([]);

  // Fetch data based on mode
  const { data: valueChains, isLoading, error } = useValueChainTree();

  const handleNodeToggle = (nodeId: string) => {
    setExpandedNodes(prev =>
      prev.includes(nodeId)
        ? prev.filter(id => id !== nodeId)
        : [...prev, nodeId]
    );
  };

  const handleKPISelect = (kpiCode: string) => {
    if (onKPISelect) {
      onKPISelect(kpiCode);
    }
  };

  // Filter value chains based on search
  const filteredValueChains = valueChains?.filter(vc =>
    searchQuery === '' ||
    vc.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    vc.display_name.toLowerCase().includes(searchQuery.toLowerCase())
  );

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
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
        InputProps={{
          startAdornment: (
            <InputAdornment position="start">
              <SearchIcon />
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
                expanded={expandedNodes.includes(valueChain.code)}
                onToggle={() => handleNodeToggle(valueChain.code)}
                onKPISelect={handleKPISelect}
                selectedKPIs={selectedKPIs}
                searchQuery={searchQuery}
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
            {searchQuery && ` matching "${searchQuery}"`}
          </Box>
        </Box>
      )}
    </Box>
  );
}
