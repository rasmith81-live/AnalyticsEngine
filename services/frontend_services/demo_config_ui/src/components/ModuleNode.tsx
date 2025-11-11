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
  onKPIToggleCart: (kpiCode: string) => void;
  onKPIViewDetails: (kpiCode: string) => void;
  selectedKPIs: string[];
  currentViewKPI: string | null;
  searchQuery?: string;
}

export default function ModuleNode({
  module,
  onKPIToggleCart,
  onKPIViewDetails,
  selectedKPIs,
  currentViewKPI,
  searchQuery = ''
}: ModuleNodeProps) {
  const [expanded, setExpanded] = useState(false);

  const handleToggle = () => {
    setExpanded(!expanded);
  };

  // Filter KPIs based on search
  const filteredKPIs = module.kpis?.filter(kpi => {
    if (searchQuery === '') return true;
    
    const query = searchQuery.toLowerCase();
    return (
      kpi.name?.toLowerCase().includes(query) ||
      kpi.display_name?.toLowerCase().includes(query) ||
      kpi.description?.toLowerCase().includes(query) ||
      kpi.code?.toLowerCase().includes(query)
    );
  }) || [];

  // Auto-expand if search matches
  const shouldExpand = Boolean(searchQuery && filteredKPIs.length > 0);

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
          label={`${filteredKPIs.length} KPIs`}
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
                selected={currentViewKPI === kpi.code}
                inCart={selectedKPIs.includes(kpi.code)}
                onToggleCart={() => onKPIToggleCart(kpi.code)}
                onViewDetails={() => onKPIViewDetails(kpi.code)}
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
