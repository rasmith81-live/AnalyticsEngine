/**
 * Hook to fetch all object models from the metadata service
 */

import { useQuery } from '@tanstack/react-query';
import { metadataApi } from '../api/metadataApi';
import type { ObjectModel } from '../types';

export function useObjectModels() {
  return useQuery<ObjectModel[]>({
    queryKey: ['objectModels'],
    queryFn: async () => {
      const models = await metadataApi.getObjectModels();
      return models || [];
    },
    staleTime: 5 * 60 * 1000, // 5 minutes
  });
}

export function useObjectModelsByModule(moduleCode?: string) {
  return useQuery<ObjectModel[]>({
    queryKey: ['objectModels', 'module', moduleCode],
    queryFn: async () => {
      const models = await metadataApi.getObjectModels();
      
      if (!moduleCode) return models;
      
      return models.filter((model: ObjectModel) => 
        model.metadata_?.modules?.includes(moduleCode)
      );
    },
    enabled: !!moduleCode,
    staleTime: 5 * 60 * 1000,
  });
}
