/**
 * MetricTreeTabs Component
 * Container with tabs for switching between Industry and Value Chain navigation modes
 * Click on the same tab to refresh the tree data
 */

import { useState } from 'react';
import { Box, Tabs, Tab, Paper, Tooltip } from '@mui/material';
import { useQueryClient } from '@tanstack/react-query';
import AccountTreeIcon from '@mui/icons-material/AccountTree';
import BusinessIcon from '@mui/icons-material/Business';
import MetricTree from './MetricTree';
import type { TreeMode } from '../types/metricTree';

interface MetricTreeTabsProps {
  onKPIToggleCart?: (kpiCode: string) => void;
  onKPIViewDetails?: (kpiCode: string) => void;
  selectedKPIs?: string[];
  currentViewKPI?: string | null;
}

export default function MetricTreeTabs({ 
  onKPIToggleCart, 
  onKPIViewDetails, 
  selectedKPIs = [],
  currentViewKPI = null 
}: MetricTreeTabsProps) {
  const [mode, setMode] = useState<TreeMode>('value-chain');
  const [refreshKey, setRefreshKey] = useState(0);
  const queryClient = useQueryClient();

  const handleTabClick = (clickedMode: TreeMode) => {
    if (clickedMode === mode) {
      // Same tab clicked - invalidate cache and trigger refresh
      queryClient.invalidateQueries({ queryKey: ['valueChainTree'] });
      queryClient.invalidateQueries({ queryKey: ['infiniteKPIs'] });
      setRefreshKey(prev => prev + 1);
    } else {
      // Different tab - switch mode
      setMode(clickedMode);
    }
  };

  return (
    <Paper elevation={2} sx={{ p: 2 }}>
      <Box sx={{ borderBottom: 1, borderColor: 'divider', mb: 2 }}>
        <Tabs value={mode} aria-label="metric tree navigation">
          <Tab
            icon={<AccountTreeIcon />}
            iconPosition="start"
            label={
              <Tooltip title="Click again to refresh" placement="top">
                <span>By Value Chain</span>
              </Tooltip>
            }
            value="value-chain"
            onClick={() => handleTabClick('value-chain')}
          />
          <Tab
            icon={<BusinessIcon />}
            iconPosition="start"
            label={
              <Tooltip title="Click again to refresh" placement="top">
                <span>By Industry</span>
              </Tooltip>
            }
            value="industry"
            onClick={() => handleTabClick('industry')}
          />
        </Tabs>
      </Box>

      <Box sx={{ mt: 2 }}>
        <MetricTree
          key={refreshKey}
          mode={mode}
          onKPIToggleCart={onKPIToggleCart}
          onKPIViewDetails={onKPIViewDetails}
          selectedKPIs={selectedKPIs}
          currentViewKPI={currentViewKPI}
        />
      </Box>
    </Paper>
  );
}
