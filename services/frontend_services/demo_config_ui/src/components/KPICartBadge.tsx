/**
 * KPICartBadge Component
 * Cart badge for header showing KPI count with dropdown
 */

import {
  Box,
  IconButton,
  Badge,
  Popover,
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
  Typography,
  Button,
  Divider,
  Tooltip,
} from '@mui/material';
import {
  ShoppingCart as CartIcon,
  Delete as DeleteIcon,
  DeleteSweep as ClearIcon,
  Save as SaveIcon,
  Visibility as ViewIcon,
} from '@mui/icons-material';
import { useState } from 'react';
import { useKPIDetails } from '../hooks/useKPIDetails';

interface KPICartBadgeProps {
  selectedKPIs: string[];
  onRemoveKPI: (kpiCode: string) => void;
  onClearAll: () => void;
  onSaveConfiguration: () => void;
  onViewKPI: (kpiCode: string) => void;
  currentViewKPI: string | null;
}

export default function KPICartBadge({
  selectedKPIs,
  onRemoveKPI,
  onClearAll,
  onSaveConfiguration,
  onViewKPI,
  currentViewKPI,
}: KPICartBadgeProps) {
  const [anchorEl, setAnchorEl] = useState<HTMLButtonElement | null>(null);
  const { data: kpiDetails } = useKPIDetails(selectedKPIs);

  const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const open = Boolean(anchorEl);

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
    <>
      <Tooltip title="View KPI Cart">
        <IconButton
          color="inherit"
          onClick={handleClick}
          sx={{ ml: 2 }}
        >
          <Badge badgeContent={selectedKPIs.length} color="error">
            <CartIcon />
          </Badge>
        </IconButton>
      </Tooltip>

      <Popover
        open={open}
        anchorEl={anchorEl}
        onClose={handleClose}
        anchorOrigin={{
          vertical: 'bottom',
          horizontal: 'right',
        }}
        transformOrigin={{
          vertical: 'top',
          horizontal: 'right',
        }}
        PaperProps={{
          sx: { width: 350, maxHeight: 500 },
        }}
      >
        {/* Header */}
        <Box sx={{ p: 2, bgcolor: 'primary.main', color: 'primary.contrastText' }}>
          <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <Typography variant="h6">KPI Cart</Typography>
            {selectedKPIs.length > 0 && (
              <Tooltip title="Clear All">
                <IconButton
                  size="small"
                  onClick={() => {
                    onClearAll();
                    handleClose();
                  }}
                  sx={{ color: 'inherit' }}
                >
                  <ClearIcon />
                </IconButton>
              </Tooltip>
            )}
          </Box>
        </Box>

        {/* Empty State */}
        {selectedKPIs.length === 0 ? (
          <Box sx={{ p: 4, textAlign: 'center' }}>
            <CartIcon sx={{ fontSize: 48, color: 'text.secondary', mb: 1 }} />
            <Typography variant="body2" color="text.secondary">
              Your cart is empty
            </Typography>
            <Typography variant="caption" color="text.secondary">
              Select KPIs to add them to your cart
            </Typography>
          </Box>
        ) : (
          <>
            {/* Summary Stats */}
            <Box sx={{ p: 2, bgcolor: 'grey.50' }}>
              <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.5 }}>
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

            <Divider />

            {/* KPI List */}
            <List dense sx={{ maxHeight: 300, overflowY: 'auto' }}>
              {selectedKPIs.map((kpiCode, index) => (
                <Box key={kpiCode}>
                  <ListItem
                    sx={{
                      bgcolor: currentViewKPI === kpiCode ? 'action.selected' : 'transparent',
                      '&:hover': { bgcolor: 'action.hover' },
                      cursor: 'pointer',
                    }}
                    onClick={() => {
                      onViewKPI(kpiCode);
                      handleClose();
                    }}
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
                              handleClose();
                            }}
                          >
                            <ViewIcon fontSize="small" />
                          </IconButton>
                        </Tooltip>
                        <Tooltip title="Remove">
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

            <Divider />

            {/* Actions */}
            <Box sx={{ p: 2 }}>
              <Button
                variant="contained"
                color="primary"
                fullWidth
                startIcon={<SaveIcon />}
                onClick={() => {
                  onSaveConfiguration();
                  handleClose();
                }}
              >
                Save Configuration
              </Button>
            </Box>
          </>
        )}
      </Popover>
    </>
  );
}
