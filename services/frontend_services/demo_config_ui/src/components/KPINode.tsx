/**
 * KPINode Component
 * Renders a KPI leaf node with selection capability
 */

import { useState, DragEvent } from 'react';
import { Box, Typography, Checkbox, Chip, Tooltip } from '@mui/material';
import AnalyticsIcon from '@mui/icons-material/Analytics';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import DragIndicatorIcon from '@mui/icons-material/DragIndicator';
import TreeItemMenu from './TreeItemMenu';
import { useTreeActions } from '../contexts/TreeActionsContext';
import type { KPI } from '../types/metricTree';

interface KPINodeProps {
  kpi: KPI;
  selected: boolean;
  inCart: boolean;
  onToggleCart: () => void;
  onViewDetails: () => void;
  moduleCode?: string;
  valueChainCode?: string;
}

export default function KPINode({ kpi, selected, inCart, onToggleCart, onViewDetails, moduleCode, valueChainCode }: KPINodeProps) {
  const { setDragItem } = useTreeActions();
  const [isDragging, setIsDragging] = useState(false);

  const handleDragStart = (e: DragEvent) => {
    e.stopPropagation();
    // Required for HTML5 drag-and-drop to work properly
    e.dataTransfer.setData('text/plain', kpi.code);
    e.dataTransfer.effectAllowed = 'move';
    setIsDragging(true);
    setDragItem({
      type: 'kpi',
      code: kpi.code,
      name: kpi.display_name || kpi.name,
      sourceModuleCode: moduleCode,
      sourceValueChainCode: valueChainCode
    });
  };

  const handleDragEnd = () => {
    setIsDragging(false);
    setDragItem(null);
  };

  return (
    <Box
      draggable
      onDragStart={handleDragStart}
      onDragEnd={handleDragEnd}
      sx={{
        display: 'flex',
        alignItems: 'center',
        p: 1,
        mb: 0.5,
        bgcolor: selected ? 'primary.50' : 'white',
        border: 1,
        borderColor: selected ? 'primary.main' : 'grey.200',
        borderRadius: 1,
        transition: 'all 0.2s',
        opacity: isDragging ? 0.5 : 1,
        cursor: 'grab',
        '&:hover': {
          bgcolor: selected ? 'primary.100' : 'grey.50',
          borderColor: selected ? 'primary.dark' : 'grey.300',
        },
        '&:active': {
          cursor: 'grabbing',
        },
      }}
    >
      <DragIndicatorIcon sx={{ color: 'grey.400', mr: 0.5, cursor: 'grab' }} fontSize="small" />
      <Checkbox
        checked={inCart}
        onChange={(e) => {
          e.stopPropagation();
          onToggleCart();
        }}
        onClick={(e) => e.stopPropagation()}
        icon={<AnalyticsIcon />}
        checkedIcon={<CheckCircleIcon />}
        sx={{ mr: 1 }}
      />
      
      <Box 
        sx={{ 
          flexGrow: 1, 
          minWidth: 0,
          cursor: 'pointer',
        }}
        onClick={onViewDetails}
      >
        <Typography variant="body2" sx={{ fontWeight: selected ? 600 : 400 }}>
          {kpi.display_name || kpi.name}
        </Typography>
        {kpi.description && (
          <Tooltip title={kpi.description} arrow>
            <Typography
              variant="caption"
              color="text.secondary"
              sx={{
                display: 'block',
                overflow: 'hidden',
                textOverflow: 'ellipsis',
                whiteSpace: 'nowrap',
              }}
            >
              {kpi.description}
            </Typography>
          </Tooltip>
        )}
      </Box>

      {kpi.unit && (
        <Chip
          label={kpi.unit}
          size="small"
          variant="outlined"
          sx={{ ml: 1, fontSize: '0.7rem' }}
        />
      )}
      <TreeItemMenu 
        type="kpi" 
        code={kpi.code} 
        name={kpi.display_name || kpi.name} 
      />
    </Box>
  );
}
