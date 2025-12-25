/**
 * ModuleNode Component
 * Renders a module node with its KPIs
 */

import { useState, useEffect, useRef, DragEvent } from 'react';
import { Box, Collapse, Typography, Chip, CircularProgress } from '@mui/material';
import { ExpandMore, ChevronRight } from '@mui/icons-material';
import FolderIcon from '@mui/icons-material/Folder';
import DragIndicatorIcon from '@mui/icons-material/DragIndicator';
import KPINode from './KPINode';
import TreeItemMenu from './TreeItemMenu';
import { useTreeActions } from '../contexts/TreeActionsContext';
import type { Module } from '../types/metricTree';

interface ModuleNodeProps {
  module: Module;
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
  valueChainCode?: string;
  onRefresh?: () => void;
}

export default function ModuleNode({
  module,
  onKPIToggleCart,
  onKPIViewDetails,
  selectedKPIs,
  currentViewKPI,
  searchQuery = '',
  infiniteScrollData,
  valueChainCode,
  onRefresh
}: ModuleNodeProps) {
  const [expanded, setExpanded] = useState(false);
  const scrollContainerRef = useRef<HTMLDivElement>(null);
  const { setDragItem, dragItem, handleDrop, isDragging } = useTreeActions();
  const [isDropTarget, setIsDropTarget] = useState(false);
  const [isDraggingThis, setIsDraggingThis] = useState(false);
  
  // Use infinite scroll data if provided (fallback "All KPIs" case), otherwise use module's preloaded KPIs
  const usesGlobalInfiniteScroll = (module as any)._usesInfiniteScroll;
  const allKPIs = usesGlobalInfiniteScroll && infiniteScrollData 
    ? infiniteScrollData.kpis 
    : (module.kpis || []);
  
  // Scroll control - only for global infinite scroll case
  const scrollControl = usesGlobalInfiniteScroll && infiniteScrollData
    ? infiniteScrollData
    : { fetchNextPage: () => {}, hasNextPage: false, isFetchingNextPage: false };

  // Allow KPIs to be dropped on modules
  const canAcceptDrop = isDragging && dragItem?.type === 'kpi';

  const handleToggle = () => {
    setExpanded(!expanded);
  };

  const handleDragStart = (e: DragEvent) => {
    e.stopPropagation();
    // Required for HTML5 drag-and-drop to work properly
    e.dataTransfer.setData('text/plain', module.code);
    e.dataTransfer.effectAllowed = 'move';
    setIsDraggingThis(true);
    setDragItem({
      type: 'module',
      code: module.code,
      name: module.display_name || module.name,
      sourceValueChainCode: valueChainCode
    });
  };

  const handleDragEnd = () => {
    setIsDraggingThis(false);
    setDragItem(null);
  };

  const handleDragOver = (e: DragEvent) => {
    if (canAcceptDrop) {
      e.preventDefault();
      e.stopPropagation();
      setIsDropTarget(true);
    }
  };

  const handleDragLeave = () => {
    setIsDropTarget(false);
  };

  const handleDropEvent = async (e: DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDropTarget(false);
    if (canAcceptDrop) {
      await handleDrop('module', module.code);
    }
  };

  // Filter KPIs based on search
  const filteredKPIs = allKPIs.filter(kpi => {
    if (searchQuery === '') return true;
    
    const query = searchQuery.toLowerCase();
    return (
      kpi.name?.toLowerCase().includes(query) ||
      kpi.display_name?.toLowerCase().includes(query) ||
      kpi.description?.toLowerCase().includes(query) ||
      kpi.code?.toLowerCase().includes(query)
    );
  });

  // Auto-expand if search matches
  const shouldExpand = Boolean(searchQuery && filteredKPIs.length > 0);

  // Infinite scroll handler - fetch next page from server
  useEffect(() => {
    if (!expanded) return; // Only setup scroll when expanded
    
    const container = scrollContainerRef.current;
    if (!container) return;

    const handleScroll = () => {
      const { scrollTop, scrollHeight, clientHeight } = container;
      const scrollPercentage = (scrollTop + clientHeight) / scrollHeight;
      
      // Load more when scrolled to 80% of content
      if (scrollPercentage >= 0.8) {
        if (scrollControl.hasNextPage && !scrollControl.isFetchingNextPage) {
          scrollControl.fetchNextPage();
        }
      }
    };

    container.addEventListener('scroll', handleScroll);
    return () => container.removeEventListener('scroll', handleScroll);
  }, [expanded, scrollControl]);

  return (
    <Box sx={{ mb: 1, opacity: isDraggingThis ? 0.5 : 1 }}>
      {/* Module Header */}
      <Box
        draggable
        onDragStart={handleDragStart}
        onDragEnd={handleDragEnd}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDropEvent}
        onClick={handleToggle}
        sx={{
          display: 'flex',
          alignItems: 'center',
          p: 1,
          bgcolor: isDropTarget ? 'success.light' : 'grey.50',
          borderRadius: 1,
          cursor: 'grab',
          border: isDropTarget ? '2px dashed' : 'none',
          borderColor: 'success.main',
          transition: 'all 0.2s',
          '&:hover': {
            bgcolor: isDropTarget ? 'success.light' : 'grey.100',
          },
          '&:active': {
            cursor: 'grabbing',
          },
        }}
      >
        <DragIndicatorIcon sx={{ color: 'grey.400', mr: 0.5, cursor: 'grab' }} fontSize="small" />
        {expanded || shouldExpand ? <ExpandMore /> : <ChevronRight />}
        <FolderIcon sx={{ ml: 0.5, mr: 1, color: 'warning.main' }} />
        <Typography variant="body1" sx={{ flexGrow: 1 }}>
          {module.display_name || module.name}
        </Typography>
        <Chip
          label={`${filteredKPIs.length} KPIs`}
          size="small"
          variant="outlined"
        />
        <TreeItemMenu 
          type="module" 
          code={module.code} 
          name={module.display_name || module.name}
          onRefresh={onRefresh}
        />
      </Box>

      {/* KPIs */}
      <Collapse in={expanded || shouldExpand} timeout="auto" unmountOnExit>
        <Box 
          ref={scrollContainerRef}
          sx={{ 
            ml: 4, 
            mt: 0.5, 
            maxHeight: '500px', 
            overflowY: 'auto',
            '&::-webkit-scrollbar': {
              width: '8px',
            },
            '&::-webkit-scrollbar-track': {
              bgcolor: 'grey.100',
            },
            '&::-webkit-scrollbar-thumb': {
              bgcolor: 'grey.400',
              borderRadius: '4px',
            },
          }}
        >
          {filteredKPIs.length > 0 ? (
            <>
              {filteredKPIs.map((kpi, index) => (
                <KPINode
                  key={`${kpi.code}-${index}`}
                  kpi={kpi}
                  selected={currentViewKPI === kpi.code}
                  inCart={selectedKPIs.includes(kpi.code)}
                  onToggleCart={() => onKPIToggleCart(kpi.code)}
                  onViewDetails={() => onKPIViewDetails(kpi.code)}
                  moduleCode={module.code}
                  valueChainCode={valueChainCode}
                />
              ))}
              {(scrollControl.hasNextPage || scrollControl.isFetchingNextPage) && (
                <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', p: 2 }}>
                  {scrollControl.isFetchingNextPage && <CircularProgress size={20} />}
                  <Typography variant="caption" color="text.secondary" sx={{ ml: 1 }}>
                    {scrollControl.isFetchingNextPage 
                      ? 'Loading more KPIs...' 
                      : `Loaded ${filteredKPIs.length} KPIs - scroll for more`}
                  </Typography>
                </Box>
              )}
            </>
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
