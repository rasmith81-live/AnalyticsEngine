/**
 * Hook for fetching KPI details
 * Fetches full KPI information for selected KPIs
 */

import { useQuery } from '@tanstack/react-query';
import { metadataApi } from '../services/api';
import type { KPI } from '../types';

export function useKPIDetail(kpiCode: string) {
  return useQuery<KPI>({
    queryKey: ['kpi', kpiCode],
    queryFn: () => metadataApi.getKPI(kpiCode),
    enabled: !!kpiCode,
    staleTime: 5 * 60 * 1000, // 5 minutes
  });
}

export function useKPIDetails(kpiCodes: string[]) {
  return useQuery<KPI[]>({
    queryKey: ['kpis', 'batch', kpiCodes],
    queryFn: async () => {
      // Fetch all KPIs in parallel
      const promises = kpiCodes.map(code => metadataApi.getKPI(code));
      return Promise.all(promises);
    },
    enabled: kpiCodes.length > 0,
    staleTime: 5 * 60 * 1000, // 5 minutes
  });
}
