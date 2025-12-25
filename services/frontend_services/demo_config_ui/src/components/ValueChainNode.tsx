/**
 * ValueChainNode Component
 * Renders a value chain node with its modules
 */

import { useState, DragEvent } from 'react';
import { Box, Collapse, Typography, Chip } from '@mui/material';
import { ExpandMore, ChevronRight } from '@mui/icons-material';
import AccountTreeIcon from '@mui/icons-material/AccountTree';
import ModuleNode from './ModuleNode';
import TreeItemMenu from './TreeItemMenu';
import { useTreeActions } from '../contexts/TreeActionsContext';
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
  infiniteScrollData?: {
    kpis: any[];
    fetchNextPage: () => void;
    hasNextPage: boolean;
    isFetchingNextPage: boolean;
  };
  onRefresh?: () => void;
}

export default function ValueChainNode({
  valueChain,
  expanded,
  onToggle,
  onKPIToggleCart,
  onKPIViewDetails,
  selectedKPIs,
  currentViewKPI,
  searchQuery = '',
  infiniteScrollData,
  onRefresh
}: ValueChainNodeProps) {
  const { dragItem, handleDrop, isDragging } = useTreeActions();
  const [isDropTarget, setIsDropTarget] = useState(false);

  // Allow modules to be dropped on value chains
  const canAcceptDrop = isDragging && dragItem?.type === 'module';

  const handleDragOver = (e: DragEvent) => {
    if (canAcceptDrop) {
      e.preventDefault();
      setIsDropTarget(true);
    }
  };

  const handleDragLeave = () => {
    setIsDropTarget(false);
  };

  const handleDropEvent = async (e: DragEvent) => {
    e.preventDefault();
    setIsDropTarget(false);
    if (canAcceptDrop) {
      await handleDrop('valueChain', valueChain.code);
    }
  };
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
    const usesInfiniteScroll = (module as any)._usesInfiniteScroll;
    
    if (!searchQuery) {
      // Use infiniteScrollData count if this module uses infinite scroll, otherwise use module count
      if (usesInfiniteScroll && infiniteScrollData) {
        return sum + infiniteScrollData.kpis.length;
      }
      return sum + (module.kpi_count || 0);
    }
    // Count only matching KPIs when searching
    const kpisToSearch = (usesInfiniteScroll && infiniteScrollData) ? infiniteScrollData.kpis : (module.kpis || []);
    const matchingKPIs = kpisToSearch.filter(kpi => {
      const query = searchQuery.toLowerCase();
      return (
        kpi.name?.toLowerCase().includes(query) ||
        kpi.display_name?.toLowerCase().includes(query) ||
        kpi.description?.toLowerCase().includes(query) ||
        kpi.code?.toLowerCase().includes(query)
      );
    });
    return sum + matchingKPIs.length;
  }, 0) || 0;

  return (
    <Box sx={{ mb: 1 }}>
      {/* Value Chain Header */}
      <Box
        onClick={onToggle}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDropEvent}
        sx={{
          display: 'flex',
          alignItems: 'center',
          p: 1.5,
          bgcolor: isDropTarget ? 'success.light' : 'primary.50',
          borderRadius: 1,
          cursor: 'pointer',
          border: isDropTarget ? '2px dashed' : 'none',
          borderColor: 'success.main',
          transition: 'all 0.2s',
          '&:hover': {
            bgcolor: isDropTarget ? 'success.light' : 'primary.100',
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
        <TreeItemMenu 
          type="valueChain" 
          code={valueChain.code} 
          name={valueChain.display_name || valueChain.name}
          onRefresh={onRefresh}
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
                infiniteScrollData={(module as any)._usesInfiniteScroll ? infiniteScrollData : undefined}
                valueChainCode={valueChain.code}
                onRefresh={onRefresh}
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
