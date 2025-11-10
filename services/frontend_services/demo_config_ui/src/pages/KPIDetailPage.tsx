import { Typography, Paper, Box } from '@mui/material';
import { useParams } from 'react-router-dom';

export default function KPIDetailPage() {
  const { kpiCode } = useParams<{ kpiCode: string }>();

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        KPI Detail: {kpiCode}
      </Typography>
      <Paper sx={{ p: 3, mt: 2 }}>
        <Typography variant="body1">
          Detailed KPI information will be displayed here.
        </Typography>
        <Typography variant="body2" sx={{ mt: 2 }}>
          Coming soon: Formula, benchmarks, required objects, and custom KPI creator
        </Typography>
      </Paper>
    </Box>
  );
}
