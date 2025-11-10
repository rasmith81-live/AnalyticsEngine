import { Typography, Paper, Box } from '@mui/material';

export default function RequiredObjectsViewer() {
  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Required Objects Analysis
      </Typography>
      <Paper sx={{ p: 3, mt: 2 }}>
        <Typography variant="body1">
          Analysis of required object models for selected KPIs.
        </Typography>
        <Typography variant="body2" sx={{ mt: 2 }}>
          Coming soon: Consolidated UML diagram showing all dependencies
        </Typography>
      </Paper>
    </Box>
  );
}
