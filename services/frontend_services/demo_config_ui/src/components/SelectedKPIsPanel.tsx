/**
 * SelectedKPIsPanel Component
 * Enhanced panel for displaying selected KPIs with details and actions
 */

import {
  Box,
  Paper,
  Typography,
  Chip,
  Button,
  Tooltip,
  CircularProgress,
  Alert,
  Divider,
  Stack,
} from '@mui/material';
import {
  Delete as DeleteIcon,
  Save as SaveIcon,
  Visibility as ViewIcon,
  Info as InfoIcon,
} from '@mui/icons-material';
import { useNavigate } from 'react-router-dom';
import { useKPIDetails } from '../hooks/useKPIDetails';
import type { KPI } from '../types';

interface SelectedKPIsPanelProps {
  selectedKPIs: string[];
  onRemoveKPI: (kpiCode: string) => void;
  onClearAll: () => void;
  onSaveConfiguration?: () => void;
}

export default function SelectedKPIsPanel({
  selectedKPIs,
  onRemoveKPI,
  onClearAll,
  onSaveConfiguration,
}: SelectedKPIsPanelProps) {
  const navigate = useNavigate();
  const { data: kpiDetails, isLoading, error } = useKPIDetails(selectedKPIs);

  const handleViewDetails = (kpiCode: string) => {
    navigate(`/kpi/${kpiCode}`);
  };

  const getTruncatedFormula = (formula: string, maxLength: number = 60): string => {
    if (!formula) return 'No formula available';
    if (formula.length <= maxLength) return formula;
    return formula.substring(0, maxLength) + '...';
  };

  const getKPIDisplayName = (kpi: KPI): string => {
    return kpi.display_name || kpi.name || kpi.code;
  };

  const getTotalRequiredObjects = (): number => {
    if (!kpiDetails) return 0;
    const uniqueObjects = new Set<string>();
    kpiDetails.forEach(kpi => {
      kpi.required_objects?.forEach(obj => uniqueObjects.add(obj));
    });
    return uniqueObjects.size;
  };

  return (
    <Paper elevation={2} sx={{ p: 2, position: 'sticky', top: 16 }}>
      {/* Header */}
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
        <Typography variant="h6">
          Selected KPIs
        </Typography>
        {selectedKPIs.length > 0 && (
          <Chip
            label={selectedKPIs.length}
            color="primary"
            size="small"
          />
        )}
      </Box>

      {/* Empty State */}
      {selectedKPIs.length === 0 ? (
        <Box sx={{ textAlign: 'center', py: 4 }}>
          <InfoIcon sx={{ fontSize: 48, color: 'text.secondary', mb: 2 }} />
          <Typography variant="body2" color="text.secondary">
            No KPIs selected yet
          </Typography>
          <Typography variant="caption" color="text.secondary">
            Browse the tree on the left to select KPIs
          </Typography>
        </Box>
      ) : (
        <>
          {/* Loading State */}
          {isLoading && (
            <Box sx={{ display: 'flex', justifyContent: 'center', py: 2 }}>
              <CircularProgress size={24} />
            </Box>
          )}

          {/* Error State */}
          {error && (
            <Alert severity="warning" sx={{ mb: 2 }}>
              Could not load KPI details
            </Alert>
          )}

          {/* Summary Stats */}
          {kpiDetails && (
            <Box sx={{ mb: 2, p: 1.5, bgcolor: 'grey.50', borderRadius: 1 }}>
              <Stack spacing={1}>
                <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
                  <Typography variant="caption" color="text.secondary">
                    Total KPIs:
                  </Typography>
                  <Typography variant="caption" fontWeight="bold">
                    {selectedKPIs.length}
                  </Typography>
                </Box>
                <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
                  <Typography variant="caption" color="text.secondary">
                    Required Objects:
                  </Typography>
                  <Typography variant="caption" fontWeight="bold">
                    {getTotalRequiredObjects()}
                  </Typography>
                </Box>
              </Stack>
            </Box>
          )}

          <Divider sx={{ my: 2 }} />

          {/* KPI List */}
          <Box sx={{ maxHeight: 400, overflowY: 'auto', mb: 2 }}>
            <Stack spacing={1}>
              {kpiDetails?.map((kpi) => (
                <Tooltip
                  key={kpi.code}
                  title={
                    <Box>
                      <Typography variant="caption" fontWeight="bold">
                        {getKPIDisplayName(kpi)}
                      </Typography>
                      <Typography variant="caption" display="block" sx={{ mt: 0.5 }}>
                        Formula: {getTruncatedFormula(kpi.formula)}
                      </Typography>
                      <Typography variant="caption" display="block" sx={{ mt: 0.5 }}>
                        Objects: {kpi.required_objects?.length || 0}
                      </Typography>
                    </Box>
                  }
                  placement="left"
                  arrow
                >
                  <Box
                    sx={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: 1,
                      p: 1,
                      borderRadius: 1,
                      bgcolor: 'background.paper',
                      border: '1px solid',
                      borderColor: 'divider',
                      '&:hover': {
                        bgcolor: 'action.hover',
                      },
                    }}
                  >
                    <Box sx={{ flex: 1, minWidth: 0 }}>
                      <Typography
                        variant="body2"
                        fontWeight="medium"
                        noWrap
                        sx={{ mb: 0.5 }}
                      >
                        {getKPIDisplayName(kpi)}
                      </Typography>
                      <Typography
                        variant="caption"
                        color="text.secondary"
                        noWrap
                      >
                        {kpi.code}
                      </Typography>
                    </Box>
                    <Box sx={{ display: 'flex', gap: 0.5 }}>
                      <Tooltip title="View Details">
                        <Button
                          size="small"
                          variant="text"
                          onClick={() => handleViewDetails(kpi.code)}
                          sx={{ minWidth: 'auto', p: 0.5 }}
                        >
                          <ViewIcon fontSize="small" />
                        </Button>
                      </Tooltip>
                      <Tooltip title="Remove">
                        <Button
                          size="small"
                          variant="text"
                          color="error"
                          onClick={() => onRemoveKPI(kpi.code)}
                          sx={{ minWidth: 'auto', p: 0.5 }}
                        >
                          <DeleteIcon fontSize="small" />
                        </Button>
                      </Tooltip>
                    </Box>
                  </Box>
                </Tooltip>
              ))}

              {/* Show loading placeholders for KPIs without details yet */}
              {selectedKPIs.length > (kpiDetails?.length || 0) && (
                <>
                  {selectedKPIs
                    .filter(code => !kpiDetails?.find(kpi => kpi.code === code))
                    .map(code => (
                      <Box
                        key={code}
                        sx={{
                          display: 'flex',
                          alignItems: 'center',
                          gap: 1,
                          p: 1,
                          borderRadius: 1,
                          bgcolor: 'background.paper',
                          border: '1px solid',
                          borderColor: 'divider',
                        }}
                      >
                        <Box sx={{ flex: 1 }}>
                          <Typography variant="body2" color="text.secondary">
                            {code}
                          </Typography>
                        </Box>
                        <CircularProgress size={16} />
                      </Box>
                    ))}
                </>
              )}
            </Stack>
          </Box>

          <Divider sx={{ my: 2 }} />

          {/* Action Buttons */}
          <Stack spacing={1}>
            {onSaveConfiguration && (
              <Button
                variant="contained"
                color="primary"
                fullWidth
                startIcon={<SaveIcon />}
                onClick={onSaveConfiguration}
              >
                Save Configuration
              </Button>
            )}
            <Button
              variant="outlined"
              color="error"
              fullWidth
              startIcon={<DeleteIcon />}
              onClick={onClearAll}
            >
              Clear All
            </Button>
          </Stack>
        </>
      )}
    </Paper>
  );
}
