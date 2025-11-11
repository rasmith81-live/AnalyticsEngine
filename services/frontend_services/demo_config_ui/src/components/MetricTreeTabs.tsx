/**
 * MetricTreeTabs Component
 * Container with tabs for switching between Industry and Value Chain navigation modes
 */

import { useState } from 'react';
import { Box, Tabs, Tab, Paper } from '@mui/material';
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

  const handleModeChange = (_event: React.SyntheticEvent, newMode: TreeMode) => {
    setMode(newMode);
  };

  return (
    <Paper elevation={2} sx={{ p: 2 }}>
      <Box sx={{ borderBottom: 1, borderColor: 'divider', mb: 2 }}>
        <Tabs value={mode} onChange={handleModeChange} aria-label="metric tree navigation">
          <Tab
            icon={<AccountTreeIcon />}
            iconPosition="start"
            label="By Value Chain"
            value="value-chain"
          />
          <Tab
            icon={<BusinessIcon />}
            iconPosition="start"
            label="By Industry"
            value="industry"
          />
        </Tabs>
      </Box>

      <Box sx={{ mt: 2 }}>
        <MetricTree
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
