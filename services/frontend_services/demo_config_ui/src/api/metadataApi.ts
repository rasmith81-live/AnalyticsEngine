/**
 * Metadata API Client
 * Handles communication with the analytics_metadata_service
 */

import axios from 'axios';
import type { KPI, ObjectModel, Module, ValueChain, Industry } from '../types';

const BASE_URL = 'http://127.0.0.1:8090/api/v1/metadata';

const api = axios.create({
  baseURL: BASE_URL,
  timeout: 30000, // Increased to 30s for large datasets
  headers: {
    'Content-Type': 'application/json',
  },
});

export const metadataApi = {
  // KPI/Metric endpoints - using the actual business_metadata API structure
  async getKPIs(limit?: number, offset?: number): Promise<KPI[]> {
    const params: any = {};
    if (limit) params.limit = limit;
    if (offset) params.offset = offset;
    const response = await api.get('/definitions/metric_definition', { params });
    return response.data;
  },

  async getKPI(code: string): Promise<KPI> {
    // Use pagination to search for KPI by code to avoid loading all KPIs
    let offset = 0;
    const limit = 100;
    
    while (true) {
      const kpis = await this.getKPIs(limit, offset);
      if (kpis.length === 0) break;
      
      const kpi = kpis.find((k: any) => k.code === code);
      if (kpi) return kpi;
      
      if (kpis.length < limit) break;
      offset += limit;
    }
    
    throw new Error(`KPI with code ${code} not found`);
  },

  async getKPIsByModule(moduleCode: string): Promise<KPI[]> {
    // Use pagination to avoid loading all KPIs at once
    const results: KPI[] = [];
    let offset = 0;
    const limit = 100;
    
    while (true) {
      const kpis = await this.getKPIs(limit, offset);
      if (kpis.length === 0) break;
      
      results.push(...kpis.filter((kpi: any) => kpi.modules?.includes(moduleCode)));
      
      if (kpis.length < limit) break;
      offset += limit;
    }
    
    return results;
  },

  async getKPIsByValueChain(valueChain: string): Promise<KPI[]> {
    // Use pagination to avoid loading all KPIs at once
    const results: KPI[] = [];
    let offset = 0;
    const limit = 100;
    
    while (true) {
      const kpis = await this.getKPIs(limit, offset);
      if (kpis.length === 0) break;
      
      results.push(...kpis.filter((kpi: any) => kpi.value_chain === valueChain));
      
      if (kpis.length < limit) break;
      offset += limit;
    }
    
    return results;
  },

  // Object Model endpoints - using entity_definition
  async getObjectModels(): Promise<ObjectModel[]> {
    const response = await api.get('/definitions/entity_definition');
    return response.data;
  },

  async getObjectModel(code: string): Promise<ObjectModel> {
    const response = await api.get(`/entities/${code}`);
    return response.data;
  },

  async getObjectModelsByModule(moduleCode: string): Promise<ObjectModel[]> {
    const allModels = await this.getObjectModels();
    return allModels.filter((model: any) => 
      model.metadata_?.modules?.includes(moduleCode)
    );
  },

  // Module endpoints - using business_process_definition
  async getModules(): Promise<Module[]> {
    const response = await api.get('/definitions/business_process_definition');
    return response.data;
  },

  // Relationship-based queries (graph architecture)
  async getAllRelationships(relationshipType?: string): Promise<Array<{
    from_entity_code: string;
    to_entity_code: string;
    relationship_type: string;
    metadata_?: Record<string, any>;
  }>> {
    const params: any = {};
    if (relationshipType) {
      params.relationship_types = relationshipType;
    }
    const response = await api.get('/relationships', { params });
    return response.data;
  },

  async getEntityRelationships(entityCode: string, direction: string = 'both'): Promise<Array<{
    from_entity_code: string;
    to_entity_code: string;
    relationship_type: string;
  }>> {
    const response = await api.get(`/relationships/${entityCode}`, { params: { direction } });
    return response.data;
  },

  async getModule(code: string): Promise<Module> {
    const response = await api.get(`/business-processes/${code}`);
    return response.data;
  },

  async getModulesByValueChain(valueChainCode: string): Promise<Module[]> {
    const allModules = await this.getModules();
    // Check both top-level value_chain and metadata_.value_chain
    return allModules.filter((module: any) => 
      module.value_chain === valueChainCode || 
      module.metadata_?.value_chain === valueChainCode
    );
  },

  // Value Chain endpoints
  async getValueChains(): Promise<ValueChain[]> {
    const response = await api.get('/definitions/value_chain_pattern_definition', {
      params: { limit: 100, offset: 0 }
    });
    return response.data;
  },

  async getValueChain(code: string): Promise<ValueChain> {
    const response = await api.get(`/value-chains/${code}`);
    return response.data;
  },

  // Industry endpoints - using naics_industry_definition
  async getIndustries(): Promise<Industry[]> {
    const response = await api.get('/definitions/naics_industry_definition');
    return response.data;
  },

  async getIndustryValueChains(code: string): Promise<ValueChain[]> {
    const allValueChains = await this.getValueChains();
    return allValueChains.filter((vc: any) => vc.industry === code);
  },

  // Update endpoints
  async updateDefinition(kind: string, code: string, data: any): Promise<void> {
    await api.put(`/definitions/${kind}/${code}`, data, {
      params: { changed_by: 'admin' }
    });
  },

  async updateValueChain(code: string, data: any): Promise<void> {
    await this.updateDefinition('value_chain_pattern_definition', code, data);
  },

  async updateModule(code: string, data: any): Promise<void> {
    await this.updateDefinition('business_process_definition', code, data);
  },

  async updateKPI(code: string, data: any): Promise<void> {
    await this.updateDefinition('metric_definition', code, data);
  },

  // Delete endpoints
  async deleteDefinition(kind: string, code: string): Promise<void> {
    await api.delete(`/definitions/${kind}/${code}`, {
      params: { deleted_by: 'admin' }
    });
  },

  async deleteValueChain(code: string): Promise<void> {
    await this.deleteDefinition('value_chain_pattern_definition', code);
  },

  async deleteModule(code: string): Promise<void> {
    await this.deleteDefinition('business_process_definition', code);
  },

  async deleteKPI(code: string): Promise<void> {
    await this.deleteDefinition('metric_definition', code);
  },

  // Relationship management
  async updateKPIRelationship(kpiCode: string, newModuleCode: string, newValueChainCode: string): Promise<void> {
    // Get the current KPI data
    const kpi = await this.getKPI(kpiCode);
    
    // Update modules array and value_chain
    const updatedKPI = {
      ...kpi,
      modules: [newModuleCode],
      value_chain: newValueChainCode,
      metadata_: {
        ...(kpi as any).metadata_,
        value_chain: newValueChainCode
      }
    };
    
    await this.updateKPI(kpiCode, updatedKPI);
  },

  async moveModuleToValueChain(moduleCode: string, newValueChainCode: string): Promise<void> {
    const allModules = await this.getModules();
    const module = allModules.find((m: any) => m.code === moduleCode);
    if (!module) throw new Error(`Module ${moduleCode} not found`);
    
    const updatedModule = {
      ...module,
      value_chain: newValueChainCode,
      metadata_: {
        ...(module as any).metadata_,
        value_chain: newValueChainCode
      }
    };
    
    await this.updateModule(moduleCode, updatedModule);
  },
};

export default metadataApi;
