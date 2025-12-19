import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer
} from 'recharts';
import { Paper, Typography, Box } from '@mui/material';

interface ResourceSchedulerProps {
  timelineWeeks: number;
}

export default function ResourceScheduler({ timelineWeeks }: ResourceSchedulerProps) {
  // Generate mock resource allocation data based on timeline
  const generateData = () => {
    const data = [];
    for (let w = 1; w <= timelineWeeks; w++) {
      // Logic to vary resource intensity based on project phase/week
      // Discovery (early): More Architect/Analyst
      // Implementation (mid): More Engineer
      // QA/Deploy (late): Balanced/Tapering
      
      const progress = w / timelineWeeks;
      let pm = 0.2; // 20% PM always
      let architect = 0;
      let engineer = 0;
      let analyst = 0;

      if (progress < 0.2) {
        // Discovery
        architect = 0.5;
        analyst = 0.8;
        engineer = 0.2;
      } else if (progress < 0.7) {
        // Implementation
        architect = 0.2;
        analyst = 0.2;
        engineer = 1.0; // Full time engineer
      } else {
        // QA / Deploy
        architect = 0.1;
        analyst = 0.2;
        engineer = 0.5;
      }

      data.push({
        week: `Week ${w}`,
        'Project Manager': pm,
        'Solution Architect': architect,
        'Data Engineer': engineer,
        'Business Analyst': analyst,
      });
    }
    return data;
  };

  const data = generateData();

  return (
    <Paper sx={{ p: 2 }}>
      <Typography variant="h6" gutterBottom>
        Resource Allocation Plan
      </Typography>
      <Box sx={{ height: 300, width: '100%' }}>
        <ResponsiveContainer>
          <BarChart
            data={data}
            margin={{
              top: 20,
              right: 30,
              left: 20,
              bottom: 5,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="week" />
            <YAxis label={{ value: 'FTE Allocation', angle: -90, position: 'insideLeft' }} />
            <Tooltip />
            <Legend />
            <Bar dataKey="Project Manager" stackId="a" fill="#8884d8" />
            <Bar dataKey="Solution Architect" stackId="a" fill="#82ca9d" />
            <Bar dataKey="Data Engineer" stackId="a" fill="#ffc658" />
            <Bar dataKey="Business Analyst" stackId="a" fill="#ff7300" />
          </BarChart>
        </ResponsiveContainer>
      </Box>
      <Typography variant="caption" color="text.secondary">
        Estimated resource requirements per week (FTE) based on project scope.
      </Typography>
    </Paper>
  );
}
