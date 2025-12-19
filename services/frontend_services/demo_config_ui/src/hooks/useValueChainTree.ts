/**
 * Hook for fetching Value Chain tree data
 * Mode: Value Chain → Module → KPI
 */

import { useQuery } from '@tanstack/react-query';
import { metadataApi } from '../api/metadataApi';
import type { ValueChain } from '../types/metricTree';

export function useValueChainTree() {
  return useQuery<ValueChain[]>({
    queryKey: ['valueChainTree'],
    queryFn: async () => {
      // Fetch all value chains
      const valueChains = await metadataApi.getValueChains();
      
      // For each value chain, fetch its modules
      const valueChainTreeData = await Promise.all(
        valueChains.map(async (vc: any) => {
          try {
            // Fetch modules for this value chain
            const modulesResponse = await metadataApi.getModulesByValueChain(vc.code);
            
            // For each module, fetch its KPIs
            const modulesWithKPIs = await Promise.all(
              modulesResponse.map(async (module: any) => {
                try {
                  const kpisResponse = await metadataApi.getKPIsByModule(module.code);
                  const mappedKPIs = kpisResponse.map((k: any) => ({
                    ...k,
                    display_name: k.display_name || k.name,
                    description: k.description || '',
                    module_code: k.module_code || module.code,
                  }));
                  
                  return {
                    code: module.code,
                    name: module.name,
                    display_name: module.display_name || module.name,
                    description: module.description,
                    value_chain_code: module.metadata_?.value_chain || vc.code,
                    kpis: mappedKPIs,
                    kpi_count: mappedKPIs.length
                  };
                } catch (error) {
                  console.error(`Error loading KPIs for module ${module.code}:`, error);
                  return {
                    code: module.code,
                    name: module.name,
                    display_name: module.display_name || module.name,
                    description: module.description,
                    value_chain_code: module.metadata_?.value_chain || vc.code,
                    kpis: [],
                    kpi_count: 0
                  };
                }
              })
            );
            
            return {
              code: vc.code,
              name: vc.name,
              display_name: vc.display_name || vc.name,
              description: vc.description,
              modules: modulesWithKPIs,
              module_count: modulesWithKPIs.length
            };
          } catch (error) {
            console.error(`Error loading modules for value chain ${vc.code}:`, error);
            return {
              code: vc.code,
              name: vc.name,
              display_name: vc.display_name || vc.name,
              description: vc.description,
              modules: [],
              module_count: 0
            };
          }
        })
      );
      
      return valueChainTreeData;
    },
    staleTime: 5 * 60 * 1000, // 5 minutes
    gcTime: 10 * 60 * 1000, // 10 minutes (formerly cacheTime)
  });
}

export function useValueChain(valueChainCode: string) {
  return useQuery<ValueChain>({
    queryKey: ['valueChain', valueChainCode],
    queryFn: async () => {
      const valueChain = await metadataApi.getValueChain(valueChainCode);
      const modules = await metadataApi.getModulesByValueChain(valueChainCode);
      
      const modulesWithKPIs = await Promise.all(
        modules.map(async (module: any) => {
          const kpis = await metadataApi.getKPIsByModule(module.code);
          const mappedKPIs = kpis.map((k: any) => ({
            ...k,
            display_name: k.display_name || k.name,
            description: k.description || '',
            module_code: k.module_code || module.code,
          }));
          
          return {
            code: module.code,
            name: module.name,
            display_name: module.display_name || module.name,
            description: module.description,
            value_chain_code: module.metadata_?.value_chain || valueChain.code,
            kpis: mappedKPIs,
            kpi_count: mappedKPIs.length
          };
        })
      );
      
      return {
        code: valueChain.code,
        name: valueChain.name,
        display_name: valueChain.display_name || valueChain.name,
        description: valueChain.description,
        industry_codes: valueChain.metadata_?.industries || [],
        modules: modulesWithKPIs,
        module_count: modulesWithKPIs.length
      };
    },
    enabled: !!valueChainCode,
    staleTime: 5 * 60 * 1000,
  });
}
