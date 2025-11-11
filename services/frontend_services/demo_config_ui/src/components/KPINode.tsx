/**
 * KPINode Component
 * Renders a KPI leaf node with selection capability
 */

import { Box, Typography, Checkbox, Chip, Tooltip } from '@mui/material';
import AnalyticsIcon from '@mui/icons-material/Analytics';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import type { KPI } from '../types/metricTree';

interface KPINodeProps {
  kpi: KPI;
  selected: boolean;
  inCart: boolean;
  onToggleCart: () => void;
  onViewDetails: () => void;
}

export default function KPINode({ kpi, selected, inCart, onToggleCart, onViewDetails }: KPINodeProps) {
  return (
    <Box
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
        '&:hover': {
          bgcolor: selected ? 'primary.100' : 'grey.50',
          borderColor: selected ? 'primary.dark' : 'grey.300',
        },
      }}
    >
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
    </Box>
  );
}
