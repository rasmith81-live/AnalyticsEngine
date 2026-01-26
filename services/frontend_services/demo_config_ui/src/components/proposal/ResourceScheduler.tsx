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
import { Card } from '../ui/Card';

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
    <Card className="p-4">
      <h3 className="text-base font-semibold theme-text-title mb-3">
        Resource Allocation Plan
      </h3>
      <div className="h-72 w-full">
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
            <CartesianGrid strokeDasharray="3 3" stroke="var(--color-border, #374151)" />
            <XAxis 
              dataKey="week" 
              tick={{ fill: 'var(--color-text-muted, #9ca3af)', fontSize: 12 }}
              axisLine={{ stroke: 'var(--color-border, #374151)' }}
            />
            <YAxis 
              label={{ 
                value: 'FTE Allocation', 
                angle: -90, 
                position: 'insideLeft',
                fill: 'var(--color-text-muted, #9ca3af)',
                fontSize: 12
              }}
              tick={{ fill: 'var(--color-text-muted, #9ca3af)', fontSize: 12 }}
              axisLine={{ stroke: 'var(--color-border, #374151)' }}
            />
            <Tooltip 
              contentStyle={{ 
                backgroundColor: 'var(--color-card-bg, #1f2937)',
                border: '1px solid var(--color-border, #374151)',
                borderRadius: '8px',
                color: 'var(--color-text, #e5e7eb)'
              }}
            />
            <Legend 
              wrapperStyle={{ 
                color: 'var(--color-text-muted, #9ca3af)',
                fontSize: 12
              }}
            />
            <Bar dataKey="Project Manager" stackId="a" fill="#8b5cf6" />
            <Bar dataKey="Solution Architect" stackId="a" fill="#22c55e" />
            <Bar dataKey="Data Engineer" stackId="a" fill="#f59e0b" />
            <Bar dataKey="Business Analyst" stackId="a" fill="#f97316" />
          </BarChart>
        </ResponsiveContainer>
      </div>
      <p className="text-xs theme-text-muted mt-2">
        Estimated resource requirements per week (FTE) based on project scope.
      </p>
    </Card>
  );
}
