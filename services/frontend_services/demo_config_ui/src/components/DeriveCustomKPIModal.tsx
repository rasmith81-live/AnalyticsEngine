/**
 * DeriveCustomKPIModal Component
 * Modal for creating custom/derived KPIs from a base KPI
 */

import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  TextField,
  Box,
  Typography,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Chip,
  Alert,
  Stack,
} from '@mui/material';
import { useState } from 'react';
import { useKPIDetail } from '../hooks/useKPIDetails';
import type { KPI } from '../types';

interface DeriveCustomKPIModalProps {
  open: boolean;
  baseKPICode: string | null;
  onClose: () => void;
  onSave: (customKPI: Partial<KPI>) => void;
}

export default function DeriveCustomKPIModal({
  open,
  baseKPICode,
  onClose,
  onSave,
}: DeriveCustomKPIModalProps) {
  const { data: baseKPI } = useKPIDetail(baseKPICode || '');
  const [customName, setCustomName] = useState('');
  const [customCode, setCustomCode] = useState('');
  const [customFormula, setCustomFormula] = useState('');
  const [aggregation, setAggregation] = useState('average');
  const [timePeriod, setTimePeriod] = useState('monthly');

  const handleSave = () => {
    if (!baseKPI) return;

    const customKPI: Partial<KPI> = {
      code: customCode || `${baseKPI.code}_CUSTOM`,
      name: customName || `${baseKPI.name} (Custom)`,
      display_name: customName,
      formula: customFormula || `${aggregation}(${baseKPI.formula})`,
      unit: baseKPI.unit,
      description: `Custom KPI derived from ${baseKPI.name}`,
      required_objects: baseKPI.required_objects,
      metadata_: {
        ...baseKPI.metadata_,
        category: 'custom',
      },
    };

    onSave(customKPI);
    handleClose();
  };

  const handleClose = () => {
    setCustomName('');
    setCustomCode('');
    setCustomFormula('');
    setAggregation('average');
    setTimePeriod('monthly');
    onClose();
  };

  if (!baseKPI) return null;

  return (
    <Dialog open={open} onClose={handleClose} maxWidth="md" fullWidth>
      <DialogTitle>Derive Custom KPI</DialogTitle>
      <DialogContent>
        <Stack spacing={3} sx={{ mt: 1 }}>
          {/* Base KPI Info */}
          <Alert severity="info">
            <Typography variant="body2" gutterBottom>
              <strong>Base KPI:</strong> {baseKPI.display_name || baseKPI.name}
            </Typography>
            <Typography variant="caption" display="block">
              Code: {baseKPI.code}
            </Typography>
            <Typography variant="caption" display="block">
              Formula: {baseKPI.formula}
            </Typography>
          </Alert>

          {/* Custom KPI Name */}
          <TextField
            fullWidth
            label="Custom KPI Name"
            value={customName}
            onChange={(e) => setCustomName(e.target.value)}
            placeholder={`${baseKPI.name} (Custom)`}
            helperText="Give your custom KPI a descriptive name"
          />

          {/* Custom KPI Code */}
          <TextField
            fullWidth
            label="Custom KPI Code"
            value={customCode}
            onChange={(e) => setCustomCode(e.target.value.toUpperCase().replace(/\s/g, '_'))}
            placeholder={`${baseKPI.code}_CUSTOM`}
            helperText="Unique identifier for your custom KPI (auto-generated if left blank)"
          />

          {/* Aggregation Method */}
          <FormControl fullWidth>
            <InputLabel>Aggregation Method</InputLabel>
            <Select
              value={aggregation}
              label="Aggregation Method"
              onChange={(e) => setAggregation(e.target.value)}
            >
              <MenuItem value="average">Average</MenuItem>
              <MenuItem value="sum">Sum</MenuItem>
              <MenuItem value="min">Minimum</MenuItem>
              <MenuItem value="max">Maximum</MenuItem>
              <MenuItem value="median">Median</MenuItem>
              <MenuItem value="count">Count</MenuItem>
            </Select>
          </FormControl>

          {/* Time Period */}
          <FormControl fullWidth>
            <InputLabel>Time Period</InputLabel>
            <Select
              value={timePeriod}
              label="Time Period"
              onChange={(e) => setTimePeriod(e.target.value)}
            >
              <MenuItem value="daily">Daily</MenuItem>
              <MenuItem value="weekly">Weekly</MenuItem>
              <MenuItem value="monthly">Monthly</MenuItem>
              <MenuItem value="quarterly">Quarterly</MenuItem>
              <MenuItem value="annually">Annually</MenuItem>
              <MenuItem value="custom">Custom Range</MenuItem>
            </Select>
          </FormControl>

          {/* Custom Formula (Advanced) */}
          <TextField
            fullWidth
            label="Custom Formula (Advanced)"
            value={customFormula}
            onChange={(e) => setCustomFormula(e.target.value)}
            multiline
            rows={3}
            placeholder={`${aggregation}(${baseKPI.formula}) OVER ${timePeriod}`}
            helperText="Leave blank to use aggregation + time period, or write a custom formula"
          />

          {/* Preview */}
          <Box sx={{ p: 2, bgcolor: 'grey.50', borderRadius: 1 }}>
            <Typography variant="caption" color="text.secondary" gutterBottom display="block">
              Preview Formula:
            </Typography>
            <Typography variant="body2" sx={{ fontFamily: 'monospace' }}>
              {customFormula || `${aggregation}(${baseKPI.formula}) OVER ${timePeriod}`}
            </Typography>
          </Box>

          {/* Required Objects */}
          <Box>
            <Typography variant="caption" color="text.secondary" gutterBottom display="block">
              Required Objects (inherited from base KPI):
            </Typography>
            <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5, mt: 1 }}>
              {baseKPI.required_objects?.map((obj) => (
                <Chip key={obj} label={obj} size="small" variant="outlined" />
              ))}
            </Box>
          </Box>
        </Stack>
      </DialogContent>
      <DialogActions>
        <Button onClick={handleClose}>Cancel</Button>
        <Button
          onClick={handleSave}
          variant="contained"
          disabled={!customName && !customCode}
        >
          Create Custom KPI
        </Button>
      </DialogActions>
    </Dialog>
  );
}
