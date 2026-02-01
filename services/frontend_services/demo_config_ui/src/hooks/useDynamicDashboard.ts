import { useState, useEffect, useCallback } from 'react';
import type { DashboardLayout, MetricCardConfig } from '../components/dynamic/DynamicDashboard';

interface DesignArtifact {
  type: string;
  name: string;
  details?: {
    code?: string;
    category?: string;
    unit?: string;
    visualization?: string;
  };
}

interface SessionDesign {
  kpis: DesignArtifact[];
  entities: DesignArtifact[];
  dashboards: DesignArtifact[];
  industry?: string;
  updatedAt?: string;
}

interface UseDynamicDashboardResult {
  layout: DashboardLayout | null;
  data: Record<string, any>;
  isLoading: boolean;
  error: string | null;
  refreshLayout: () => void;
  hasCustomLayout: boolean;
}

const iconForCategory: Record<string, string> = {
  'Financial': 'dollar',
  'Customer': 'users',
  'Operations': 'package',
  'Sales': 'trending',
  'Quality': 'target',
  'Efficiency': 'zap',
  'Performance': 'activity',
  'default': 'chart',
};

const formatForUnit: Record<string, 'number' | 'currency' | 'percent'> = {
  'currency': 'currency',
  '$': 'currency',
  'percent': 'percent',
  '%': 'percent',
  'default': 'number',
};

export function useDynamicDashboard(): UseDynamicDashboardResult {
  const [layout, setLayout] = useState<DashboardLayout | null>(null);
  const [data, setData] = useState<Record<string, any>>({});
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [hasCustomLayout, setHasCustomLayout] = useState(false);

  const generateLayoutFromDesign = useCallback((design: SessionDesign): DashboardLayout => {
    const kpis = design.kpis || [];
    const industry = design.industry || 'Business';

    // Create metric cards from KPIs
    const metricCards: MetricCardConfig[] = kpis.slice(0, 6).map((kpi, i) => ({
      id: kpi.details?.code || `kpi_${i}`,
      type: 'metric_card' as const,
      title: kpi.name,
      kpiCode: kpi.details?.code || `kpi_${i}`,
      icon: iconForCategory[kpi.details?.category || 'default'] || iconForCategory['default'],
      format: formatForUnit[kpi.details?.unit || 'default'] || 'number',
      showTrend: true,
    }));

    // Determine chart types based on KPI categories
    const categories = [...new Set(kpis.map(k => k.details?.category || 'General'))];
    
    const layout: DashboardLayout = {
      id: `dashboard_${Date.now()}`,
      title: `${industry} Analytics Dashboard`,
      subtitle: `Real-time analytics powered by AI-designed KPIs`,
      industry,
      columns: Math.min(metricCards.length, 4),
      refreshInterval: 5,
      sections: [
        {
          id: 'metrics',
          title: 'Key Metrics',
          layout: 'grid',
          columns: Math.min(metricCards.length, 4),
          components: metricCards,
        },
        {
          id: 'charts',
          title: 'Trend Analysis',
          layout: 'grid',
          columns: 2,
          components: [
            {
              id: 'trend_chart',
              type: 'bar_chart' as const,
              title: `${industry} Performance Trend`,
              dataKey: 'trend_data',
              size: 'medium' as const,
            },
            {
              id: 'distribution_chart',
              type: 'pie_chart' as const,
              title: `${categories[0] || 'Category'} Distribution`,
              dataKey: 'distribution_data',
              size: 'medium' as const,
            },
          ],
        },
      ],
    };

    // Add KPI table if there are more than 4 KPIs
    if (kpis.length > 4) {
      layout.sections.push({
        id: 'kpi_table',
        title: 'All KPIs',
        layout: 'stack',
        components: [
          {
            id: 'kpi_performance_table',
            type: 'table' as const,
            title: 'KPI Performance Summary',
            columns: [
              { key: 'name', label: 'KPI Name' },
              { key: 'category', label: 'Category' },
              { key: 'current', label: 'Current' },
              { key: 'target', label: 'Target' },
              { key: 'status', label: 'Status' },
            ],
            dataSource: 'kpi_data',
          },
        ],
      });
    }

    return layout;
  }, []);

  const generateDataFromDesign = useCallback((design: SessionDesign): Record<string, any> => {
    const kpis = design.kpis || [];
    const data: Record<string, any> = {};

    // Generate metric data
    kpis.slice(0, 6).forEach((kpi, i) => {
      const id = kpi.details?.code || `kpi_${i}`;
      const isPercent = kpi.details?.unit === 'percent' || kpi.details?.unit === '%';
      const isCurrency = kpi.details?.unit === 'currency' || kpi.details?.unit === '$';
      
      data[id] = {
        value: isPercent 
          ? Math.floor(Math.random() * 40 + 60) 
          : isCurrency 
            ? Math.floor(Math.random() * 2000000 + 500000)
            : Math.floor(Math.random() * 10000 + 1000),
        change: Math.round((Math.random() * 20 - 5) * 10) / 10,
      };
    });

    // Generate chart data
    data['trend_chart'] = {
      values: [65, 45, 75, 55, 80, 70, 90].map(v => v + Math.random() * 20 - 10),
    };

    data['distribution_chart'] = {
      segments: [
        { label: 'Category A', value: 30, color: '#8b5cf6' },
        { label: 'Category B', value: 25, color: '#06b6d4' },
        { label: 'Category C', value: 25, color: '#10b981' },
        { label: 'Category D', value: 20, color: '#f59e0b' },
      ],
    };

    // Generate table data
    data['kpi_performance_table'] = {
      rows: kpis.map((kpi) => ({
        name: kpi.name,
        category: kpi.details?.category || 'General',
        current: kpi.details?.unit === '%' 
          ? `${Math.floor(Math.random() * 30 + 70)}%` 
          : Math.floor(Math.random() * 1000).toLocaleString(),
        target: kpi.details?.unit === '%' 
          ? `${Math.floor(Math.random() * 10 + 85)}%` 
          : Math.floor(Math.random() * 1000).toLocaleString(),
        status: Math.random() > 0.3 ? 'On Track' : 'Needs Attention',
      })),
    };

    return data;
  }, []);

  const loadLayout = useCallback(() => {
    setIsLoading(true);
    setError(null);

    try {
      // Check localStorage for design artifacts from interview
      const storedDesign = localStorage.getItem('demo_interview_design');
      
      if (storedDesign) {
        const design = JSON.parse(storedDesign) as SessionDesign;
        
        if (design.kpis && design.kpis.length > 0) {
          const generatedLayout = generateLayoutFromDesign(design);
          const generatedData = generateDataFromDesign(design);
          
          setLayout(generatedLayout);
          setData(generatedData);
          setHasCustomLayout(true);
        } else {
          // No KPIs, use default
          setLayout(null);
          setHasCustomLayout(false);
        }
      } else {
        // No design stored
        setLayout(null);
        setHasCustomLayout(false);
      }
    } catch (err) {
      console.error('Failed to load dashboard layout:', err);
      setError('Failed to load dashboard configuration');
      setLayout(null);
      setHasCustomLayout(false);
    } finally {
      setIsLoading(false);
    }
  }, [generateLayoutFromDesign, generateDataFromDesign]);

  const refreshLayout = useCallback(() => {
    loadLayout();
  }, [loadLayout]);

  // Load on mount
  useEffect(() => {
    loadLayout();
  }, [loadLayout]);

  // Listen for storage changes (hot-reload when interview updates design)
  useEffect(() => {
    const handleStorageChange = (e: StorageEvent) => {
      if (e.key === 'demo_interview_design') {
        loadLayout();
      }
    };

    window.addEventListener('storage', handleStorageChange);
    return () => window.removeEventListener('storage', handleStorageChange);
  }, [loadLayout]);

  return {
    layout,
    data,
    isLoading,
    error,
    refreshLayout,
    hasCustomLayout,
  };
}

export default useDynamicDashboard;
