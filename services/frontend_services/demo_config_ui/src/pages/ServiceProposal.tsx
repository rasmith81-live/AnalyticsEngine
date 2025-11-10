import { Typography, Paper, Box } from '@mui/material';

export default function ServiceProposal() {
  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Service Proposal Generator
      </Typography>
      <Paper sx={{ p: 3, mt: 2 }}>
        <Typography variant="body1">
          Generate Statement of Work (SOW) with cost estimates.
        </Typography>
        <Typography variant="body2" sx={{ mt: 2 }}>
          Coming soon: Automated proposal generation with timeline and cost breakdown
        </Typography>
      </Paper>
    </Box>
  );
}
