/**
 * KPISampleVisualization Component
 * Shows sample visualization based on KPI type and visualization suggestions
 */

import {
  Box,
  Paper,
  Typography,
  ToggleButtonGroup,
  ToggleButton,
  Alert,
} from '@mui/material';
import {
  ShowChart as LineChartIcon,
  BarChart as BarChartIcon,
  PieChart as PieChartIcon,
  Speed as GaugeIcon,
} from '@mui/icons-material';
import { useState } from 'react';
import { useKPIDetail } from '../hooks/useKPIDetails';

interface KPISampleVisualizationProps {
  kpiCode: string | null;
}

type ChartType = 'line' | 'bar' | 'pie' | 'gauge';

// Parse visualization suggestions to determine available chart types
const parseVisualizationSuggestions = (suggestions: string): ChartType[] => {
  if (!suggestions) return ['line', 'bar'];
  
  const lower = suggestions.toLowerCase();
  const types: ChartType[] = [];
  
  if (lower.includes('line') || lower.includes('trend') || lower.includes('time series')) {
    types.push('line');
  }
  if (lower.includes('bar') || lower.includes('column') || lower.includes('comparison')) {
    types.push('bar');
  }
  if (lower.includes('pie') || lower.includes('donut') || lower.includes('distribution')) {
    types.push('pie');
  }
  if (lower.includes('gauge') || lower.includes('meter') || lower.includes('speedometer')) {
    types.push('gauge');
  }
  
  // Default to line and bar if no matches
  return types.length > 0 ? types : ['line', 'bar'];
};

export default function KPISampleVisualization({ kpiCode }: KPISampleVisualizationProps) {
  const { data: kpi } = useKPIDetail(kpiCode || '');
  
  // Parse suggested chart types from KPI
  const suggestedChartTypes = kpi?.visualization_suggestions 
    ? parseVisualizationSuggestions(kpi.visualization_suggestions)
    : ['line', 'bar'];
  
  const [chartType, setChartType] = useState<ChartType>(suggestedChartTypes[0] as ChartType);

  if (!kpiCode || !kpi) {
    return null;
  }

  // Use actual sample_data from KPI if available
  const sampleData = kpi.sample_data?.time_series ? 
    kpi.sample_data.time_series.dates.slice(0, 6).map((date: string, index: number) => ({
      month: new Date(date).toLocaleDateString('en-US', { month: 'short' }),
      value: kpi.sample_data!.time_series.values[index],
    })) :
    // Fallback to generated data if sample_data not available
    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'].map((month, index) => ({
      month,
      value: Math.floor(Math.random() * 100) + 50 + index * 10,
    }));

  const renderLineChart = () => {
    const maxValue = Math.max(...sampleData.map((d) => d.value));
    const height = 150;
    const width = 100;

    return (
      <svg width="100%" height={height} viewBox={`0 0 ${width} ${height}`}>
        {/* Grid lines */}
        {[0, 25, 50, 75, 100].map((y) => (
          <line
            key={y}
            x1="0"
            y1={height - (y / 100) * height}
            x2={width}
            y2={height - (y / 100) * height}
            stroke="#e0e0e0"
            strokeWidth="0.5"
          />
        ))}

        {/* Line */}
        <polyline
          points={sampleData
            .map((d, i) => {
              const x = (i / (sampleData.length - 1)) * width;
              const y = height - (d.value / maxValue) * height;
              return `${x},${y}`;
            })
            .join(' ')}
          fill="none"
          stroke="#1976d2"
          strokeWidth="2"
        />

        {/* Points */}
        {sampleData.map((d, i) => {
          const x = (i / (sampleData.length - 1)) * width;
          const y = height - (d.value / maxValue) * height;
          return <circle key={i} cx={x} cy={y} r="2" fill="#1976d2" />;
        })}

        {/* Labels */}
        {sampleData.map((d, i) => {
          const x = (i / (sampleData.length - 1)) * width;
          return (
            <text key={i} x={x} y={height - 5} fontSize="8" textAnchor="middle" fill="#666">
              {d.month}
            </text>
          );
        })}
      </svg>
    );
  };

  const renderBarChart = () => {
    const maxValue = Math.max(...sampleData.map((d) => d.value));
    const height = 150;
    const width = 100;
    const barWidth = width / sampleData.length - 2;

    return (
      <svg width="100%" height={height} viewBox={`0 0 ${width} ${height}`}>
        {/* Bars */}
        {sampleData.map((d, i) => {
          const x = (i * width) / sampleData.length + 1;
          const barHeight = (d.value / maxValue) * (height - 20);
          const y = height - barHeight - 15;
          return (
            <g key={i}>
              <rect x={x} y={y} width={barWidth} height={barHeight} fill="#1976d2" rx="1" />
              <text x={x + barWidth / 2} y={height - 5} fontSize="8" textAnchor="middle" fill="#666">
                {d.month}
              </text>
            </g>
          );
        })}
      </svg>
    );
  };

  const renderGauge = () => {
    // Use current value from sample_data if available
    const currentValue = kpi.sample_data?.current?.value || sampleData[sampleData.length - 1].value;
    const maxValue = kpi.sample_data?.statistics?.max || 200;
    const percentage = (currentValue / maxValue) * 100;
    const angle = (percentage / 100) * 180 - 90;

    return (
      <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', py: 2 }}>
        <svg width="150" height="100" viewBox="0 0 150 100">
          {/* Background arc */}
          <path
            d="M 25 75 A 50 50 0 0 1 125 75"
            fill="none"
            stroke="#e0e0e0"
            strokeWidth="10"
            strokeLinecap="round"
          />
          {/* Value arc */}
          <path
            d="M 25 75 A 50 50 0 0 1 125 75"
            fill="none"
            stroke="#1976d2"
            strokeWidth="10"
            strokeLinecap="round"
            strokeDasharray={`${(percentage / 100) * 157} 157`}
          />
          {/* Needle */}
          <line
            x1="75"
            y1="75"
            x2={75 + Math.cos((angle * Math.PI) / 180) * 40}
            y2={75 + Math.sin((angle * Math.PI) / 180) * 40}
            stroke="#333"
            strokeWidth="2"
          />
          <circle cx="75" cy="75" r="3" fill="#333" />
        </svg>
        <Typography variant="h4" color="primary">
          {currentValue.toFixed(1)}
        </Typography>
        <Typography variant="caption" color="text.secondary">
          {kpi.sample_data?.time_series?.unit || kpi.unit || ''}
        </Typography>
      </Box>
    );
  };

  const renderPieChart = () => {
    // Use breakdown data if available, otherwise use time series
    const pieData = kpi.sample_data?.breakdown ? 
      kpi.sample_data.breakdown.map((item: any) => ({
        month: item.category,
        value: item.value,
      })) :
      sampleData;
    
    const total = pieData.reduce((sum, d) => sum + d.value, 0);
    let currentAngle = 0;
    const radius = 40;
    const cx = 50;
    const cy = 50;

    return (
      <svg width="100%" height="120" viewBox="0 0 100 120">
        {pieData.map((d, i) => {
          const angle = (d.value / total) * 360;
          const startAngle = currentAngle;
          const endAngle = currentAngle + angle;
          currentAngle = endAngle;

          const x1 = cx + radius * Math.cos((startAngle * Math.PI) / 180);
          const y1 = cy + radius * Math.sin((startAngle * Math.PI) / 180);
          const x2 = cx + radius * Math.cos((endAngle * Math.PI) / 180);
          const y2 = cy + radius * Math.sin((endAngle * Math.PI) / 180);

          const largeArc = angle > 180 ? 1 : 0;
          const colors = ['#1976d2', '#42a5f5', '#64b5f6', '#90caf9', '#bbdefb', '#e3f2fd'];

          return (
            <path
              key={i}
              d={`M ${cx} ${cy} L ${x1} ${y1} A ${radius} ${radius} 0 ${largeArc} 1 ${x2} ${y2} Z`}
              fill={colors[i % colors.length]}
            />
          );
        })}
        {/* Legend */}
        {pieData.slice(0, 3).map((d, i) => (
          <g key={i}>
            <rect x="5" y={100 + i * 6} width="4" height="4" fill={['#1976d2', '#42a5f5', '#64b5f6'][i]} />
            <text x="11" y={103 + i * 6} fontSize="5" fill="#666">
              {d.month.length > 10 ? d.month.substring(0, 10) + '...' : d.month}
            </text>
          </g>
        ))}
      </svg>
    );
  };

  return (
    <Paper elevation={1} sx={{ p: 2, height: '100%' }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
        <Typography variant="subtitle2" color="text.secondary">
          Sample Visualization
        </Typography>
        <ToggleButtonGroup
          value={chartType}
          exclusive
          onChange={(_, newType) => newType && setChartType(newType)}
          size="small"
        >
          {suggestedChartTypes.includes('line') && (
            <ToggleButton value="line" aria-label="line chart">
              <LineChartIcon fontSize="small" />
            </ToggleButton>
          )}
          {suggestedChartTypes.includes('bar') && (
            <ToggleButton value="bar" aria-label="bar chart">
              <BarChartIcon fontSize="small" />
            </ToggleButton>
          )}
          {suggestedChartTypes.includes('gauge') && (
            <ToggleButton value="gauge" aria-label="gauge">
              <GaugeIcon fontSize="small" />
            </ToggleButton>
          )}
          {suggestedChartTypes.includes('pie') && (
            <ToggleButton value="pie" aria-label="pie chart">
              <PieChartIcon fontSize="small" />
            </ToggleButton>
          )}
        </ToggleButtonGroup>
      </Box>

      <Alert severity="info" sx={{ mb: 2, py: 0.5 }}>
        <Typography variant="caption">
          {kpi.sample_data ? 'Based on KPI sample data' : 'Sample data - actual values will vary'}
        </Typography>
      </Alert>

      <Box sx={{ bgcolor: 'grey.50', borderRadius: 1, p: 2, minHeight: 180 }}>
        {chartType === 'line' && renderLineChart()}
        {chartType === 'bar' && renderBarChart()}
        {chartType === 'gauge' && renderGauge()}
        {chartType === 'pie' && renderPieChart()}
      </Box>

      <Typography variant="caption" color="text.secondary" sx={{ mt: 1, display: 'block' }}>
        {kpi.display_name || kpi.name} - {kpi.sample_data?.time_series?.unit || kpi.unit || ''}
      </Typography>
      
      {kpi.sample_data?.current && (
        <Typography variant="caption" color="primary" sx={{ mt: 0.5, display: 'block', fontWeight: 600 }}>
          Current: {kpi.sample_data.current.value} {kpi.sample_data.current.unit} 
          ({kpi.sample_data.current.trend})
        </Typography>
      )}
    </Paper>
  );
}
