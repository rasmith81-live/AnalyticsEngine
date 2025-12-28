import { Box, Typography, Paper } from '@mui/material';

export default function MappingPage() {
  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Source to Target Mapping
      </Typography>
      <Paper sx={{ p: 3 }}>
        <Typography variant="body1">
          Source to Target Mapping configuration will appear here.
        </Typography>
      </Paper>
    </Box>
  );
}
