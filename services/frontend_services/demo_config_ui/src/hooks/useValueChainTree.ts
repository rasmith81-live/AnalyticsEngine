/**
 * Hook for fetching Value Chain tree data
 * Mode: Value Chain → Module → KPI
 */

import { useQuery, useInfiniteQuery } from '@tanstack/react-query';
import { metadataApi } from '../api/metadataApi';
import type { ValueChain } from '../types/metricTree';

const KPIS_PER_PAGE = 20;

// Hook for infinite loading of KPIs with server-side pagination (global - for fallback)
export function useInfiniteKPIs() {
  return useInfiniteQuery({
    queryKey: ['kpis-infinite'],
    queryFn: async ({ pageParam = 0 }) => {
      const kpis = await metadataApi.getKPIs(KPIS_PER_PAGE, pageParam);
      return {
        kpis,
        nextOffset: kpis.length === KPIS_PER_PAGE ? pageParam + KPIS_PER_PAGE : undefined,
      };
    },
    getNextPageParam: (lastPage) => lastPage.nextOffset,
    initialPageParam: 0,
  });
}

// Hook for infinite loading of KPIs for a specific module
export function useModuleKPIs(moduleCode: string, enabled: boolean = true) {
  return useInfiniteQuery({
    queryKey: ['module-kpis', moduleCode],
    queryFn: async ({ pageParam = 0 }) => {
      // Fetch KPIs and filter by module
      const allKpis = await metadataApi.getKPIs(KPIS_PER_PAGE * 5, pageParam); // Fetch more to filter
      const moduleKpis = allKpis.filter((kpi: any) => 
        kpi.modules?.includes(moduleCode)
      );
      return {
        kpis: moduleKpis.slice(0, KPIS_PER_PAGE), // Return only KPIS_PER_PAGE
        nextOffset: allKpis.length >= KPIS_PER_PAGE * 5 ? pageParam + KPIS_PER_PAGE * 5 : undefined,
        totalFetched: allKpis.length,
      };
    },
    getNextPageParam: (lastPage) => lastPage.nextOffset,
    initialPageParam: 0,
    enabled: enabled && !!moduleCode,
  });
}

export function useValueChainTree() {
  return useQuery<ValueChain[]>({
    queryKey: ['valueChainTree'],
    queryFn: async () => {
      try {
        console.log('Fetching value chain tree data using relationships...');
        
        // Fetch all entities and relationships in parallel
        const [valueChains, allModules, kpisBatch1, relationships] = await Promise.all([
          metadataApi.getValueChains(),
          metadataApi.getModules(),
          metadataApi.getKPIs(100, 0),
          metadataApi.getAllRelationships(),
        ]);
        
        // Load additional KPI batches if needed
        let allKPIs = [...kpisBatch1];
        if (kpisBatch1.length === 100) {
          const [batch2, batch3, batch4, batch5] = await Promise.all([
            metadataApi.getKPIs(100, 100),
            metadataApi.getKPIs(100, 200),
            metadataApi.getKPIs(100, 300),
            metadataApi.getKPIs(100, 400),
          ]);
          allKPIs = [...allKPIs, ...batch2, ...batch3, ...batch4, ...batch5];
        }
        
        console.log(`Loaded: ${valueChains?.length || 0} value chains, ${allModules?.length || 0} modules, ${allKPIs.length} KPIs, ${relationships?.length || 0} relationships`);
        
        // If no value chains exist, create a fallback
        if (!valueChains || valueChains.length === 0) {
          return [{
            code: 'all',
            name: 'All KPIs',
            display_name: 'All KPIs',
            description: 'Imported KPIs',
            modules: [{
              code: 'imported',
              name: 'Imported KPIs',
              display_name: 'Imported KPIs',
              description: 'KPIs imported from Excel',
              value_chain_code: 'all',
              kpis: [],
              kpi_count: 0,
              _usesInfiniteScroll: true,
            }],
            module_count: 1
          }];
        }
        
        // Build relationship lookups from the relationships table
        // module -> value_chain (from belongs_to_value_chain relationships where from is module)
        const moduleToValueChain: Record<string, string> = {};
        // kpi -> modules (from belongs_to_module relationships)
        const kpiToModules: Record<string, string[]> = {};
        
        for (const rel of relationships || []) {
          if (rel.relationship_type === 'belongs_to_value_chain') {
            // Check if from_entity is a module (not a KPI)
            const isModule = allModules.some((m: any) => m.code === rel.from_entity_code);
            if (isModule) {
              moduleToValueChain[rel.from_entity_code] = rel.to_entity_code;
            }
          }
          if (rel.relationship_type === 'belongs_to_module') {
            if (!kpiToModules[rel.from_entity_code]) {
              kpiToModules[rel.from_entity_code] = [];
            }
            kpiToModules[rel.from_entity_code].push(rel.to_entity_code);
          }
        }
        
        // Build KPI lookup by module code using relationships
        const kpisByModule: Record<string, any[]> = {};
        for (const kpi of allKPIs) {
          const modules = kpiToModules[kpi.code] || [];
          for (const modCode of modules) {
            if (!kpisByModule[modCode]) {
              kpisByModule[modCode] = [];
            }
            kpisByModule[modCode].push({
              ...kpi,
              display_name: kpi.display_name || kpi.name,
              description: kpi.description || '',
              module_code: modCode,
            });
          }
        }
        
        // Build module lookup by value chain using relationships
        const modulesByValueChain: Record<string, any[]> = {};
        for (const mod of allModules) {
          const vcCode = moduleToValueChain[mod.code];
          if (vcCode) {
            if (!modulesByValueChain[vcCode]) {
              modulesByValueChain[vcCode] = [];
            }
            modulesByValueChain[vcCode].push(mod);
          }
        }
        
        // Build the tree structure
        const valueChainTreeData = valueChains.map((vc: any) => {
          const vcModules = modulesByValueChain[vc.code] || [];
          
          const modulesWithKPIs = vcModules.map((module: any) => ({
            code: module.code,
            name: module.name,
            display_name: module.display_name || module.name,
            description: module.description,
            value_chain_code: vc.code,
            kpis: kpisByModule[module.code] || [],
            kpi_count: (kpisByModule[module.code] || []).length,
          }));
          
          return {
            code: vc.code,
            name: vc.name,
            display_name: vc.display_name || vc.name,
            description: vc.description,
            modules: modulesWithKPIs,
            module_count: modulesWithKPIs.length
          };
        });
        
        return valueChainTreeData;
      } catch (error) {
        console.error('Error in useValueChainTree:', error);
        throw error;
      }
    },
    staleTime: 1 * 60 * 1000,
    gcTime: 5 * 60 * 1000,
    retry: false,
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
