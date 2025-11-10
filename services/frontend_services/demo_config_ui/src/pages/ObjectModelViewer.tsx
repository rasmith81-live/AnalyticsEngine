import { Typography, Paper, Box } from '@mui/material';
import { useParams } from 'react-router-dom';

export default function ObjectModelViewer() {
  const { modelCode } = useParams<{ modelCode: string }>();

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Object Model: {modelCode}
      </Typography>
      <Paper sx={{ p: 3, mt: 2 }}>
        <Typography variant="body1">
          UML class diagram will be displayed here.
        </Typography>
        <Typography variant="body2" sx={{ mt: 2 }}>
          Coming soon: D3.js UML diagram with relationships
        </Typography>
      </Paper>
    </Box>
  );
}
