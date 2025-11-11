/**
 * Hook for fetching object model details
 */

import { useQuery } from '@tanstack/react-query';
import { metadataApi } from '../api/metadataApi';
import type { ObjectModel } from '../types';

export function useObjectModelDetails(modelCode: string) {
  return useQuery<ObjectModel>({
    queryKey: ['objectModel', modelCode],
    queryFn: () => metadataApi.getObjectModel(modelCode),
    enabled: !!modelCode,
    staleTime: 10 * 60 * 1000, // 10 minutes
  });
}

export function useObjectModels(modelCodes: string[]) {
  return useQuery<ObjectModel[]>({
    queryKey: ['objectModels', modelCodes.sort().join(',')],
    queryFn: async () => {
      if (modelCodes.length === 0) return [];
      const promises = modelCodes.map(code => metadataApi.getObjectModel(code));
      return Promise.all(promises);
    },
    enabled: modelCodes.length > 0,
    staleTime: 10 * 60 * 1000,
  });
}
