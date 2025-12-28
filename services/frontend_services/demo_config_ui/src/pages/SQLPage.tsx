import { Box, Typography, Paper } from '@mui/material';

export default function SQLPage() {
  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        SQL Interface
      </Typography>
      <Paper sx={{ p: 3 }}>
        <Typography variant="body1">
          SQL Query Interface will appear here.
        </Typography>
      </Paper>
    </Box>
  );
}
