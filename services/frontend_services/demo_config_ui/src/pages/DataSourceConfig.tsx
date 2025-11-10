import { Typography, Paper, Box } from '@mui/material';

export default function DataSourceConfig() {
  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Data Source Configuration
      </Typography>
      <Paper sx={{ p: 3, mt: 2 }}>
        <Typography variant="body1">
          Configure data source connections (batch/real-time).
        </Typography>
        <Typography variant="body2" sx={{ mt: 2 }}>
          Coming soon: Connection setup, connector configuration, and testing
        </Typography>
      </Paper>
    </Box>
  );
}
