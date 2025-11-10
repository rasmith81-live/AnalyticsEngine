import { Typography, Paper, Box } from '@mui/material';

export default function ConfigPage() {
  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Configuration Page
      </Typography>
      <Paper sx={{ p: 3, mt: 2 }}>
        <Typography variant="body1">
          This is the configuration page where clients can select KPIs.
        </Typography>
        <Typography variant="body2" sx={{ mt: 2 }}>
          Coming soon: Metric tree view with Industry → Value Chain → Module → KPI hierarchy
        </Typography>
      </Paper>
    </Box>
  );
}
