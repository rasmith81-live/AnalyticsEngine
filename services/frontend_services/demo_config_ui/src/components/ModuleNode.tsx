/**
 * ModuleNode Component
 * Renders a module node with its KPIs
 */

import { useState } from 'react';
import { Box, Collapse, Typography, Chip } from '@mui/material';
import { ExpandMore, ChevronRight } from '@mui/icons-material';
import FolderIcon from '@mui/icons-material/Folder';
import KPINode from './KPINode';
import type { Module } from '../types/metricTree';

interface ModuleNodeProps {
  module: Module;
  onKPISelect: (kpiCode: string) => void;
  selectedKPIs: string[];
  searchQuery?: string;
}

export default function ModuleNode({
  module,
  onKPISelect,
  selectedKPIs,
  searchQuery = ''
}: ModuleNodeProps) {
  const [expanded, setExpanded] = useState(false);

  const handleToggle = () => {
    setExpanded(!expanded);
  };

  // Filter KPIs based on search
  const filteredKPIs = module.kpis?.filter(kpi =>
    searchQuery === '' ||
    kpi.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    kpi.display_name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    kpi.description?.toLowerCase().includes(searchQuery.toLowerCase())
  ) || [];

  // Auto-expand if search matches
  const shouldExpand = searchQuery && filteredKPIs.length > 0;

  return (
    <Box sx={{ mb: 1 }}>
      {/* Module Header */}
      <Box
        onClick={handleToggle}
        sx={{
          display: 'flex',
          alignItems: 'center',
          p: 1,
          bgcolor: 'grey.50',
          borderRadius: 1,
          cursor: 'pointer',
          '&:hover': {
            bgcolor: 'grey.100',
          },
        }}
      >
        {expanded || shouldExpand ? <ExpandMore /> : <ChevronRight />}
        <FolderIcon sx={{ ml: 1, mr: 1, color: 'warning.main' }} />
        <Typography variant="body1" sx={{ flexGrow: 1 }}>
          {module.display_name || module.name}
        </Typography>
        <Chip
          label={`${module.kpi_count || 0} KPIs`}
          size="small"
          variant="outlined"
        />
      </Box>

      {/* KPIs */}
      <Collapse in={expanded || shouldExpand} timeout="auto" unmountOnExit>
        <Box sx={{ ml: 4, mt: 0.5 }}>
          {filteredKPIs.length > 0 ? (
            filteredKPIs.map((kpi) => (
              <KPINode
                key={kpi.code}
                kpi={kpi}
                selected={selectedKPIs.includes(kpi.code)}
                onSelect={() => onKPISelect(kpi.code)}
              />
            ))
          ) : (
            <Typography variant="body2" color="text.secondary" sx={{ p: 1 }}>
              {searchQuery ? 'No KPIs match your search' : 'No KPIs found'}
            </Typography>
          )}
        </Box>
      </Collapse>
    </Box>
  );
}
