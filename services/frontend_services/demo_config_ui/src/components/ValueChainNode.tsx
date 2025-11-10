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
  onKPISelect: (kpiCode: string) => void;
  selectedKPIs: string[];
  searchQuery?: string;
}

export default function ValueChainNode({
  valueChain,
  expanded,
  onToggle,
  onKPISelect,
  selectedKPIs,
  searchQuery = ''
}: ValueChainNodeProps) {
  const totalKPIs = valueChain.modules?.reduce((sum, module) => sum + (module.kpi_count || 0), 0) || 0;

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
          label={`${valueChain.module_count || 0} modules`}
          size="small"
          sx={{ mr: 1 }}
        />
        <Chip
          label={`${totalKPIs} KPIs`}
          size="small"
          color="primary"
        />
      </Box>

      {/* Modules */}
      <Collapse in={expanded} timeout="auto" unmountOnExit>
        <Box sx={{ ml: 4, mt: 1 }}>
          {valueChain.modules && valueChain.modules.length > 0 ? (
            valueChain.modules.map((module) => (
              <ModuleNode
                key={module.code}
                module={module}
                onKPISelect={onKPISelect}
                selectedKPIs={selectedKPIs}
                searchQuery={searchQuery}
              />
            ))
          ) : (
            <Typography variant="body2" color="text.secondary" sx={{ p: 2 }}>
              No modules found
            </Typography>
          )}
        </Box>
      </Collapse>
    </Box>
  );
}
