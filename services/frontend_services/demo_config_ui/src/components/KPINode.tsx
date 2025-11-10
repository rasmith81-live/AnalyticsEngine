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
  onSelect: () => void;
}

export default function KPINode({ kpi, selected, onSelect }: KPINodeProps) {
  return (
    <Box
      onClick={onSelect}
      sx={{
        display: 'flex',
        alignItems: 'center',
        p: 1,
        mb: 0.5,
        bgcolor: selected ? 'success.50' : 'white',
        border: 1,
        borderColor: selected ? 'success.main' : 'grey.200',
        borderRadius: 1,
        cursor: 'pointer',
        transition: 'all 0.2s',
        '&:hover': {
          bgcolor: selected ? 'success.100' : 'grey.50',
          borderColor: selected ? 'success.dark' : 'grey.300',
        },
      }}
    >
      <Checkbox
        checked={selected}
        onChange={onSelect}
        onClick={(e) => e.stopPropagation()}
        icon={<AnalyticsIcon />}
        checkedIcon={<CheckCircleIcon />}
        sx={{ mr: 1 }}
      />
      
      <Box sx={{ flexGrow: 1, minWidth: 0 }}>
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
