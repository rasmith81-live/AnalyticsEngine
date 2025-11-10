/**
 * MetricTreeTabs Component
 * Container with tabs for switching between Industry and Value Chain navigation modes
 */

import { useState } from 'react';
import { Box, Tabs, Tab, Paper, Typography } from '@mui/material';
import AccountTreeIcon from '@mui/icons-material/AccountTree';
import BusinessIcon from '@mui/icons-material/Business';
import MetricTree from './MetricTree';
import type { TreeMode } from '../types/metricTree';

interface MetricTreeTabsProps {
  onKPISelect?: (kpiCode: string) => void;
  selectedKPIs?: string[];
}

export default function MetricTreeTabs({ onKPISelect, selectedKPIs = [] }: MetricTreeTabsProps) {
  const [mode, setMode] = useState<TreeMode>('value-chain');

  const handleModeChange = (_event: React.SyntheticEvent, newMode: TreeMode) => {
    setMode(newMode);
  };

  return (
    <Paper elevation={2} sx={{ p: 2 }}>
      <Typography variant="h6" gutterBottom>
        Browse KPIs
      </Typography>
      
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
          onKPISelect={onKPISelect}
          selectedKPIs={selectedKPIs}
        />
      </Box>
    </Paper>
  );
}
