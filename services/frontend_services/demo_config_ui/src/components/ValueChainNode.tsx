/**
 * ValueChainNode Component
 * Renders a value chain node with its modules
 */

import { Box, Collapse, Typography, Chip } from '@mui/material';
import { ExpandMore, ChevronRight } from '@mui/icons-material';
import AccountTreeIcon from '@mui/icons-material/AccountTree';
import ModuleNode from './ModuleNode';
import type { ValueChain } from '../types/metricTree';

interface ValueChainNodeProps {
  valueChain: ValueChain;
  expanded: boolean;
  onToggle: () => void;
  onKPIToggleCart: (kpiCode: string) => void;
  onKPIViewDetails: (kpiCode: string) => void;
  selectedKPIs: string[];
  currentViewKPI: string | null;
  searchQuery?: string;
}

export default function ValueChainNode({
  valueChain,
  expanded,
  onToggle,
  onKPIToggleCart,
  onKPIViewDetails,
  selectedKPIs,
  currentViewKPI,
  searchQuery = ''
}: ValueChainNodeProps) {
  // Filter modules based on search query
  const filteredModules = valueChain.modules?.filter(module => {
    if (!searchQuery) return true;
    
    const query = searchQuery.toLowerCase();
    
    // Check module name
    if (module.name?.toLowerCase().includes(query) ||
        module.display_name?.toLowerCase().includes(query)) {
      return true;
    }
    
    // Check if any KPI matches
    return module.kpis?.some(kpi =>
      kpi.name?.toLowerCase().includes(query) ||
      kpi.display_name?.toLowerCase().includes(query) ||
      kpi.description?.toLowerCase().includes(query) ||
      kpi.code?.toLowerCase().includes(query)
    );
  });
  
  // Calculate counts based on filtered modules
  const displayModuleCount = filteredModules?.length || 0;
  const displayKPICount = filteredModules?.reduce((sum, module) => {
    if (!searchQuery) {
      return sum + (module.kpi_count || 0);
    }
    // Count only matching KPIs when searching
    const matchingKPIs = module.kpis?.filter(kpi => {
      const query = searchQuery.toLowerCase();
      return (
        kpi.name?.toLowerCase().includes(query) ||
        kpi.display_name?.toLowerCase().includes(query) ||
        kpi.description?.toLowerCase().includes(query) ||
        kpi.code?.toLowerCase().includes(query)
      );
    });
    return sum + (matchingKPIs?.length || 0);
  }, 0) || 0;

  return (
    <Box sx={{ mb: 1 }}>
      {/* Value Chain Header */}
      <Box
        onClick={onToggle}
        sx={{
          display: 'flex',
          alignItems: 'center',
          p: 1.5,
          bgcolor: 'primary.50',
          borderRadius: 1,
          cursor: 'pointer',
          '&:hover': {
            bgcolor: 'primary.100',
          },
        }}
      >
        {expanded ? <ExpandMore /> : <ChevronRight />}
        <AccountTreeIcon sx={{ ml: 1, mr: 1, color: 'primary.main' }} />
        <Typography variant="subtitle1" sx={{ flexGrow: 1, fontWeight: 600 }}>
          {valueChain.display_name || valueChain.name}
        </Typography>
        <Chip
          label={`${displayModuleCount} modules`}
          size="small"
          sx={{ mr: 1 }}
        />
        <Chip
          label={`${displayKPICount} KPIs`}
          size="small"
          color="primary"
        />
      </Box>

      {/* Modules */}
      <Collapse in={expanded} timeout="auto" unmountOnExit>
        <Box sx={{ ml: 4, mt: 1 }}>
          {filteredModules && filteredModules.length > 0 ? (
            filteredModules.map((module) => (
              <ModuleNode
                key={module.code}
                module={module}
                onKPIToggleCart={onKPIToggleCart}
                onKPIViewDetails={onKPIViewDetails}
                selectedKPIs={selectedKPIs}
                currentViewKPI={currentViewKPI}
                searchQuery={searchQuery}
              />
            ))
          ) : (
            <Typography variant="body2" color="text.secondary" sx={{ p: 2 }}>
              {searchQuery ? 'No matching modules found' : 'No modules found'}
            </Typography>
          )}
        </Box>
      </Collapse>
    </Box>
  );
}
