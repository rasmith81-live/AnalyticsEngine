/**
 * KPISampleVisualization Component
 * Shows sample visualization based on KPI type and visualization suggestions
 */

import { useState } from 'react';
import { TrendingUp, BarChart3, PieChart, Gauge } from 'lucide-react';
import { Card } from './ui/Card';
import { cn } from '../lib/utils';
import { useKPIDetail } from '../hooks/useKPIDetails';

interface KPISampleVisualizationProps {
  kpiCode: string | null;
}

type ChartType = 'line' | 'bar' | 'pie' | 'gauge';

const parseVisualizationSuggestions = (suggestions: string): ChartType[] => {
  if (!suggestions) return ['line', 'bar'];
  const lower = suggestions.toLowerCase();
  const types: ChartType[] = [];
  if (lower.includes('line') || lower.includes('trend') || lower.includes('time series')) types.push('line');
  if (lower.includes('bar') || lower.includes('column') || lower.includes('comparison')) types.push('bar');
  if (lower.includes('pie') || lower.includes('donut') || lower.includes('distribution')) types.push('pie');
  if (lower.includes('gauge') || lower.includes('meter') || lower.includes('speedometer')) types.push('gauge');
  return types.length > 0 ? types : ['line', 'bar'];
};

export default function KPISampleVisualization({ kpiCode }: KPISampleVisualizationProps) {
  const { data: kpi } = useKPIDetail(kpiCode || '');
  const suggestedChartTypes = kpi?.visualization_suggestions ? parseVisualizationSuggestions(kpi.visualization_suggestions) : ['line', 'bar'];
  const [chartType, setChartType] = useState<ChartType>(suggestedChartTypes[0] as ChartType);

  if (!kpiCode || !kpi) return null;

  const sampleData = kpi.sample_data?.time_series ? 
    kpi.sample_data.time_series.dates.slice(0, 6).map((date: string, index: number) => ({
      month: new Date(date).toLocaleDateString('en-US', { month: 'short' }),
      value: kpi.sample_data!.time_series.values[index],
    })) :
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
        {[0, 25, 50, 75, 100].map((y) => (
          <line key={y} x1="0" y1={height - (y / 100) * height} x2={width} y2={height - (y / 100) * height} stroke="currentColor" strokeOpacity="0.1" strokeWidth="0.5" />
        ))}
        <polyline
          points={sampleData.map((d, i) => `${(i / (sampleData.length - 1)) * width},${height - (d.value / maxValue) * height}`).join(' ')}
          fill="none" stroke="#7d44ee" strokeWidth="2"
        />
        {sampleData.map((d, i) => (
          <circle key={i} cx={(i / (sampleData.length - 1)) * width} cy={height - (d.value / maxValue) * height} r="2" fill="#7d44ee" />
        ))}
        {sampleData.map((d, i) => (
          <text key={i} x={(i / (sampleData.length - 1)) * width} y={height - 5} fontSize="8" textAnchor="middle" fill="currentColor" fillOpacity="0.5">{d.month}</text>
        ))}
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
        {sampleData.map((d, i) => {
          const x = (i * width) / sampleData.length + 1;
          const barHeight = (d.value / maxValue) * (height - 20);
          const y = height - barHeight - 15;
          return (
            <g key={i}>
              <rect x={x} y={y} width={barWidth} height={barHeight} fill="#7d44ee" rx="1" />
              <text x={x + barWidth / 2} y={height - 5} fontSize="8" textAnchor="middle" fill="currentColor" fillOpacity="0.5">{d.month}</text>
            </g>
          );
        })}
      </svg>
    );
  };

  const renderGauge = () => {
    const currentValue = kpi.sample_data?.current?.value || sampleData[sampleData.length - 1].value;
    const maxValue = kpi.sample_data?.statistics?.max || 200;
    const percentage = (currentValue / maxValue) * 100;
    const angle = (percentage / 100) * 180 - 90;
    return (
      <div className="flex flex-col items-center py-4">
        <svg width="150" height="100" viewBox="0 0 150 100">
          <path d="M 25 75 A 50 50 0 0 1 125 75" fill="none" stroke="currentColor" strokeOpacity="0.2" strokeWidth="10" strokeLinecap="round" />
          <path d="M 25 75 A 50 50 0 0 1 125 75" fill="none" stroke="#7d44ee" strokeWidth="10" strokeLinecap="round" strokeDasharray={`${(percentage / 100) * 157} 157`} />
          <line x1="75" y1="75" x2={75 + Math.cos((angle * Math.PI) / 180) * 40} y2={75 + Math.sin((angle * Math.PI) / 180) * 40} stroke="currentColor" strokeWidth="2" />
          <circle cx="75" cy="75" r="3" fill="currentColor" />
        </svg>
        <p className="text-3xl font-bold text-alpha-500">{currentValue.toFixed(1)}</p>
        <p className="text-xs theme-text-muted">{kpi.sample_data?.time_series?.unit || kpi.unit || ''}</p>
      </div>
    );
  };

  const renderPieChart = () => {
    const pieData = kpi.sample_data?.breakdown ? kpi.sample_data.breakdown.map((item: any) => ({ month: item.category, value: item.value })) : sampleData;
    const total = pieData.reduce((sum, d) => sum + d.value, 0);
    let currentAngle = 0;
    const radius = 40;
    const cx = 50;
    const cy = 50;
    const colors = ['#7d44ee', '#9d6af0', '#bd90f2', '#ddb5f4', '#e8d0f7', '#f3e8fb'];
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
          return <path key={i} d={`M ${cx} ${cy} L ${x1} ${y1} A ${radius} ${radius} 0 ${largeArc} 1 ${x2} ${y2} Z`} fill={colors[i % colors.length]} />;
        })}
        {pieData.slice(0, 3).map((d, i) => (
          <g key={i}>
            <rect x="5" y={100 + i * 6} width="4" height="4" fill={colors[i]} />
            <text x="11" y={103 + i * 6} fontSize="5" fill="currentColor" fillOpacity="0.6">{d.month.length > 10 ? d.month.substring(0, 10) + '...' : d.month}</text>
          </g>
        ))}
      </svg>
    );
  };

  const chartIcons = {
    line: <TrendingUp className="w-4 h-4" />,
    bar: <BarChart3 className="w-4 h-4" />,
    gauge: <Gauge className="w-4 h-4" />,
    pie: <PieChart className="w-4 h-4" />,
  };

  return (
    <Card className="p-4 h-full">
      <div className="flex items-center justify-between mb-3">
        <p className="text-sm theme-text-muted">Sample Visualization</p>
        <div className="flex rounded-lg overflow-hidden border theme-border">
          {suggestedChartTypes.map((type) => (
            <button
              key={type}
              onClick={() => setChartType(type as ChartType)}
              className={cn(
                "p-1.5 transition-colors",
                chartType === type ? "bg-alpha-500 text-white" : "theme-text-muted hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800"
              )}
              title={type}
            >
              {chartIcons[type as ChartType]}
            </button>
          ))}
        </div>
      </div>

      <div className="p-2 rounded-lg bg-blue-500/10 border border-blue-500/30 text-blue-400 text-xs mb-3">
        {kpi.sample_data ? 'Based on KPI sample data' : 'Sample data - actual values will vary'}
      </div>

      <div className="p-4 rounded-xl theme-card-bg border theme-border min-h-[180px]">
        {chartType === 'line' && renderLineChart()}
        {chartType === 'bar' && renderBarChart()}
        {chartType === 'gauge' && renderGauge()}
        {chartType === 'pie' && renderPieChart()}
      </div>

      <p className="text-xs theme-text-muted mt-2">
        {kpi.display_name || kpi.name} - {kpi.sample_data?.time_series?.unit || kpi.unit || ''}
      </p>
      
      {kpi.sample_data?.current && (
        <p className="text-xs text-alpha-500 font-semibold mt-1">
          Current: {kpi.sample_data.current.value} {kpi.sample_data.current.unit} ({kpi.sample_data.current.trend})
        </p>
      )}
    </Card>
  );
}
