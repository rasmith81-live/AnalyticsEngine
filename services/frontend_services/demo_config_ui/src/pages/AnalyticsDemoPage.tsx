import { Box, Typography, Paper } from '@mui/material';

export default function AnalyticsDemoPage() {
  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Analytics Demo
      </Typography>
      <Paper sx={{ p: 3 }}>
        <Typography variant="body1">
          Analytics Demo dashboard will appear here.
        </Typography>
      </Paper>
    </Box>
  );
}
