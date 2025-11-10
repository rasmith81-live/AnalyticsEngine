import { Typography, Box, Grid, Paper, Chip } from '@mui/material';
import { useState } from 'react';
import MetricTreeTabs from '../components/MetricTreeTabs';

export default function ConfigPage() {
  const [selectedKPIs, setSelectedKPIs] = useState<string[]>([]);

  const handleKPISelect = (kpiCode: string) => {
    setSelectedKPIs(prev =>
      prev.includes(kpiCode)
        ? prev.filter(code => code !== kpiCode)
        : [...prev, kpiCode]
    );
  };

  const handleRemoveKPI = (kpiCode: string) => {
    setSelectedKPIs(prev => prev.filter(code => code !== kpiCode));
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        KPI Configuration
      </Typography>
      <Typography variant="body2" color="text.secondary" gutterBottom>
        Browse and select KPIs for your analytics configuration
      </Typography>

      <Grid container spacing={3} sx={{ mt: 1 }}>
        {/* Left: Metric Tree */}
        <Grid item xs={12} md={8}>
          <MetricTreeTabs
            onKPISelect={handleKPISelect}
            selectedKPIs={selectedKPIs}
          />
        </Grid>

        {/* Right: Selected KPIs */}
        <Grid item xs={12} md={4}>
          <Paper elevation={2} sx={{ p: 2, position: 'sticky', top: 16 }}>
            <Typography variant="h6" gutterBottom>
              Selected KPIs
            </Typography>
            
            {selectedKPIs.length === 0 ? (
              <Typography variant="body2" color="text.secondary">
                No KPIs selected yet. Browse the tree on the left to select KPIs.
              </Typography>
            ) : (
              <Box>
                <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
                  {selectedKPIs.length} KPI{selectedKPIs.length !== 1 ? 's' : ''} selected
                </Typography>
                <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1 }}>
                  {selectedKPIs.map((kpiCode) => (
                    <Chip
                      key={kpiCode}
                      label={kpiCode}
                      onDelete={() => handleRemoveKPI(kpiCode)}
                      color="primary"
                      size="small"
                    />
                  ))}
                </Box>
              </Box>
            )}
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
}
