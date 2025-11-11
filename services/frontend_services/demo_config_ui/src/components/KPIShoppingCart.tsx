/**
 * KPIShoppingCart Component
 * Shopping cart-style interface for selected KPIs
 */

import {
  Box,
  Paper,
  Typography,
  IconButton,
  Button,
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
  Divider,
  Badge,
  Tooltip,
} from '@mui/material';
import {
  ShoppingCart as CartIcon,
  Delete as DeleteIcon,
  DeleteSweep as ClearIcon,
  Save as SaveIcon,
  Visibility as ViewIcon,
} from '@mui/icons-material';
import { useKPIDetails } from '../hooks/useKPIDetails';

interface KPIShoppingCartProps {
  selectedKPIs: string[];
  onRemoveKPI: (kpiCode: string) => void;
  onClearAll: () => void;
  onSaveConfiguration: () => void;
  onViewKPI: (kpiCode: string) => void;
  currentViewKPI: string | null;
}

export default function KPIShoppingCart({
  selectedKPIs,
  onRemoveKPI,
  onClearAll,
  onSaveConfiguration,
  onViewKPI,
  currentViewKPI,
}: KPIShoppingCartProps) {
  const { data: kpiDetails } = useKPIDetails(selectedKPIs);

  const getKPIDisplayName = (kpiCode: string): string => {
    const kpi = kpiDetails?.find((k) => k.code === kpiCode);
    return kpi?.display_name || kpi?.name || kpiCode;
  };

  const getTotalRequiredObjects = (): number => {
    if (!kpiDetails) return 0;
    const uniqueObjects = new Set<string>();
    kpiDetails.forEach((kpi) => {
      kpi.required_objects?.forEach((obj) => uniqueObjects.add(obj));
    });
    return uniqueObjects.size;
  };

  return (
    <Paper elevation={2} sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
      {/* Header */}
      <Box
        sx={{
          p: 2,
          bgcolor: 'primary.main',
          color: 'primary.contrastText',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
        }}
      >
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
          <Badge badgeContent={selectedKPIs.length} color="error">
            <CartIcon />
          </Badge>
          <Typography variant="h6">KPI Cart</Typography>
        </Box>
        {selectedKPIs.length > 0 && (
          <Tooltip title="Clear All">
            <IconButton size="small" onClick={onClearAll} sx={{ color: 'inherit' }}>
              <ClearIcon />
            </IconButton>
          </Tooltip>
        )}
      </Box>

      {/* Empty State */}
      {selectedKPIs.length === 0 ? (
        <Box sx={{ p: 4, textAlign: 'center', flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <Box>
            <CartIcon sx={{ fontSize: 64, color: 'text.secondary', mb: 2 }} />
            <Typography variant="body2" color="text.secondary">
              Your cart is empty
            </Typography>
            <Typography variant="caption" color="text.secondary">
              Select KPIs from the tree to add them to your cart
            </Typography>
          </Box>
        </Box>
      ) : (
        <>
          {/* Summary Stats */}
          <Box sx={{ p: 2, bgcolor: 'grey.50', borderBottom: 1, borderColor: 'divider' }}>
            <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 1 }}>
              <Typography variant="body2" color="text.secondary">
                Total KPIs:
              </Typography>
              <Typography variant="body2" fontWeight="bold">
                {selectedKPIs.length}
              </Typography>
            </Box>
            <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
              <Typography variant="body2" color="text.secondary">
                Required Objects:
              </Typography>
              <Typography variant="body2" fontWeight="bold">
                {getTotalRequiredObjects()}
              </Typography>
            </Box>
          </Box>

          {/* KPI List */}
          <Box sx={{ flex: 1, overflowY: 'auto' }}>
            <List dense>
              {selectedKPIs.map((kpiCode, index) => (
                <Box key={kpiCode}>
                  <ListItem
                    sx={{
                      bgcolor: currentViewKPI === kpiCode ? 'action.selected' : 'transparent',
                      '&:hover': { bgcolor: 'action.hover' },
                      cursor: 'pointer',
                    }}
                    onClick={() => onViewKPI(kpiCode)}
                  >
                    <ListItemText
                      primary={
                        <Typography variant="body2" noWrap>
                          {getKPIDisplayName(kpiCode)}
                        </Typography>
                      }
                      secondary={
                        <Typography variant="caption" color="text.secondary" noWrap>
                          {kpiCode}
                        </Typography>
                      }
                    />
                    <ListItemSecondaryAction>
                      <Box sx={{ display: 'flex', gap: 0.5 }}>
                        <Tooltip title="View Details">
                          <IconButton
                            edge="end"
                            size="small"
                            onClick={(e) => {
                              e.stopPropagation();
                              onViewKPI(kpiCode);
                            }}
                          >
                            <ViewIcon fontSize="small" />
                          </IconButton>
                        </Tooltip>
                        <Tooltip title="Remove from Cart">
                          <IconButton
                            edge="end"
                            size="small"
                            onClick={(e) => {
                              e.stopPropagation();
                              onRemoveKPI(kpiCode);
                            }}
                            color="error"
                          >
                            <DeleteIcon fontSize="small" />
                          </IconButton>
                        </Tooltip>
                      </Box>
                    </ListItemSecondaryAction>
                  </ListItem>
                  {index < selectedKPIs.length - 1 && <Divider />}
                </Box>
              ))}
            </List>
          </Box>

          {/* Checkout Actions */}
          <Box sx={{ p: 2, borderTop: 1, borderColor: 'divider' }}>
            <Button
              variant="contained"
              color="primary"
              fullWidth
              startIcon={<SaveIcon />}
              onClick={onSaveConfiguration}
              size="large"
            >
              Save Configuration
            </Button>
          </Box>
        </>
      )}
    </Paper>
  );
}
