import { useMemo } from 'react';
import { Card } from '../ui/Card';

interface Task {
  id: string;
  name: string;
  startWeek: number;
  durationWeeks: number;
  type: 'planning' | 'implementation' | 'qa' | 'deployment';
}

interface ProjectGanttChartProps {
  timelineWeeks: number;
}

export default function ProjectGanttChart({ timelineWeeks }: ProjectGanttChartProps) {
  // Generate tasks based on timeline
  const tasks: Task[] = useMemo(() => {
    // Basic heuristics for phase duration based on total timeline
    const discoveryDuration = Math.max(1, Math.round(timelineWeeks * 0.2));
    const implDuration = Math.max(1, Math.round(timelineWeeks * 0.5));
    const qaDuration = Math.max(1, Math.round(timelineWeeks * 0.2));
    const deployDuration = Math.max(1, timelineWeeks - discoveryDuration - implDuration - qaDuration);

    return [
      { id: '1', name: 'Discovery & Requirements', startWeek: 0, durationWeeks: discoveryDuration, type: 'planning' },
      { id: '2', name: 'Data Integration & Modeling', startWeek: discoveryDuration, durationWeeks: implDuration, type: 'implementation' },
      { id: '3', name: 'Validation & QA', startWeek: discoveryDuration + implDuration, durationWeeks: qaDuration, type: 'qa' },
      { id: '4', name: 'Deployment & Training', startWeek: discoveryDuration + implDuration + qaDuration, durationWeeks: deployDuration, type: 'deployment' },
    ];
  }, [timelineWeeks]);

  const getColor = (type: Task['type']) => {
    switch (type) {
      case 'planning': return '#8b5cf6'; // violet-500
      case 'implementation': return '#22c55e'; // green-500
      case 'qa': return '#f59e0b'; // amber-500
      case 'deployment': return '#f97316'; // orange-500
      default: return '#6b7280';
    }
  };

  return (
    <Card className="p-4">
      <h3 className="text-base font-semibold theme-text-title mb-3">
        Project Implementation Timeline
      </h3>
      <div className="w-full overflow-x-auto">
        <svg width="100%" height={200} viewBox={`0 0 ${Math.max(timelineWeeks * 50, 600)} 200`}>
          {/* Header */}
          <g transform="translate(150, 0)">
            {Array.from({ length: timelineWeeks }).map((_, i) => (
              <text
                key={i}
                x={i * 50 + 25}
                y={20}
                textAnchor="middle"
                fontSize="12"
                className="fill-current"
                style={{ fill: 'var(--color-text-muted, #9ca3af)' }}
              >
                W{i + 1}
              </text>
            ))}
          </g>

          {/* Grid lines */}
          <g transform="translate(150, 30)">
            {Array.from({ length: timelineWeeks + 1 }).map((_, i) => (
              <line
                key={i}
                x1={i * 50}
                y1={0}
                x2={i * 50}
                y2={150}
                stroke="currentColor"
                strokeWidth="1"
                className="text-alpha-faded-200 dark:text-alpha-faded-700"
                style={{ stroke: 'var(--color-border, #374151)' }}
              />
            ))}
          </g>

          {/* Tasks */}
          <g transform="translate(0, 30)">
            {tasks.map((task, index) => (
              <g key={task.id} transform={`translate(0, ${index * 40})`}>
                {/* Task Name */}
                <text
                  x={140}
                  y={25}
                  textAnchor="end"
                  fontSize="12"
                  fontWeight="500"
                  style={{ fill: 'var(--color-text, #e5e7eb)' }}
                >
                  {task.name}
                </text>

                {/* Task Bar */}
                <rect
                  x={150 + task.startWeek * 50}
                  y={10}
                  width={task.durationWeeks * 50}
                  height={24}
                  rx={4}
                  fill={getColor(task.type)}
                  opacity={0.9}
                />
              </g>
            ))}
          </g>
        </svg>
      </div>
      <p className="text-xs theme-text-muted mt-2">
        Estimated timeline based on selected KPIs and complexity.
      </p>
    </Card>
  );
}
