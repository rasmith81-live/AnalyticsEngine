/**
 * API Service - Handles all API calls to backend services
 */

import axios from 'axios';
import type { KPI, ObjectModel, Module, ValueChain, Industry, ClientConfig, ServiceProposal } from '@/types';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8090';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Metadata Service APIs
export const metadataApi = {
  // KPIs
  getKPIs: async (filters?: { module?: string; value_chain?: string; industry?: string }) => {
    const { data } = await apiClient.get<{ kpis: KPI[] }>('/kpis', { params: filters });
    return data.kpis;
  },

  getKPI: async (code: string) => {
    const { data } = await apiClient.get<KPI>(`/kpis/${code}`);
    return data;
  },

  getKPIFormula: async (code: string) => {
    const { data } = await apiClient.get(`/kpis/${code}/formula`);
    return data;
  },

  getKPIBenchmarks: async (code: string) => {
    const { data } = await apiClient.get(`/kpis/${code}/benchmarks`);
    return data;
  },

  getKPIRequiredObjects: async (code: string) => {
    const { data } = await apiClient.get<{ required_objects: string[] }>(`/kpis/${code}/required-objects`);
    return data.required_objects;
  },

  // Object Models
  getObjectModels: async () => {
    const { data } = await apiClient.get<{ object_models: ObjectModel[] }>('/object-models');
    return data.object_models;
  },

  getObjectModel: async (code: string) => {
    const { data } = await apiClient.get<ObjectModel>(`/object-models/${code}`);
    return data;
  },

  getObjectModelSchema: async (code: string) => {
    const { data } = await apiClient.get(`/object-models/${code}/schema`);
    return data;
  },

  getObjectModelRelationships: async (code: string) => {
    const { data } = await apiClient.get(`/object-models/${code}/relationships`);
    return data;
  },

  // Modules
  getModules: async () => {
    const { data } = await apiClient.get<{ modules: Module[] }>('/modules');
    return data.modules;
  },

  getModule: async (code: string) => {
    const { data} = await apiClient.get<Module>(`/modules/${code}`);
    return data;
  },

  getModuleKPIs: async (code: string) => {
    const { data } = await apiClient.get<{ kpis: KPI[] }>(`/modules/${code}/kpis`);
    return data.kpis;
  },

  getModuleObjectModels: async (code: string) => {
    const { data } = await apiClient.get<{ object_models: ObjectModel[] }>(`/modules/${code}/object-models`);
    return data.object_models;
  },

  // Value Chains
  getValueChains: async () => {
    const { data } = await apiClient.get<{ value_chains: ValueChain[] }>('/value-chains');
    return data.value_chains;
  },

  getValueChain: async (code: string) => {
    const { data } = await apiClient.get<ValueChain>(`/value-chains/${code}`);
    return data;
  },

  getValueChainKPIs: async (code: string) => {
    const { data } = await apiClient.get<{ kpis: KPI[] }>(`/value-chains/${code}/kpis`);
    return data.kpis;
  },

  getValueChainObjectModels: async (code: string) => {
    const { data } = await apiClient.get<{ object_models: ObjectModel[] }>(`/value-chains/${code}/object-models`);
    return data.object_models;
  },

  getValueChainModules: async (code: string) => {
    const { data } = await apiClient.get<{ modules: Module[] }>(`/value-chains/${code}/modules`);
    return data.modules;
  },

  // Helper methods for tree navigation
  getModulesByValueChain: async (valueChainCode: string) => {
    const { data } = await apiClient.get<{ modules: Module[] }>(`/value-chains/${valueChainCode}/modules`);
    return data.modules;
  },

  getKPIsByModule: async (moduleCode: string) => {
    const { data } = await apiClient.get<{ kpis: KPI[] }>(`/modules/${moduleCode}/kpis`);
    return data.kpis;
  },

  // Industries
  getIndustries: async () => {
    const { data } = await apiClient.get<{ industries: Industry[] }>('/industries');
    return data.industries;
  },

  getIndustry: async (code: string) => {
    const { data } = await apiClient.get<Industry>(`/industries/${code}`);
    return data;
  },

  getIndustryValueChains: async (code: string) => {
    const { data } = await apiClient.get<{ value_chains: ValueChain[] }>(`/industries/${code}/value-chains`);
    return data.value_chains;
  },

  // Stats
  getStats: async () => {
    const { data } = await apiClient.get('/stats');
    return data;
  },
};

// Demo/Config Service APIs
const CONFIG_API_URL = import.meta.env.VITE_CONFIG_API_URL || 'http://127.0.0.1:8090/api/v1/config';

const configClient = axios.create({
  baseURL: CONFIG_API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const configApi = {
  // Client Configurations
  getClientConfigs: async () => {
    const { data } = await configClient.get<ClientConfig[]>('/api/configs');
    return data;
  },

  getClientConfig: async (clientId: string) => {
    const { data } = await configClient.get<ClientConfig>(`/api/configs/${clientId}`);
    return data;
  },

  createClientConfig: async (config: Partial<ClientConfig>) => {
    const { data } = await configClient.post<ClientConfig>('/api/configs', config);
    return data;
  },

  updateClientConfig: async (clientId: string, config: Partial<ClientConfig>) => {
    const { data } = await configClient.put<ClientConfig>(`/api/configs/${clientId}`, config);
    return data;
  },

  deleteClientConfig: async (clientId: string) => {
    await configClient.delete(`/api/configs/${clientId}`);
  },

  // Custom KPIs
  createCustomKPI: async (clientId: string, kpi: Partial<KPI>) => {
    const { data } = await configClient.post(`/api/configs/${clientId}/custom-kpis`, kpi);
    return data;
  },

  getCustomKPIs: async (clientId: string) => {
    const { data } = await configClient.get(`/api/configs/${clientId}/custom-kpis`);
    return data;
  },

  // Required Objects Analysis
  analyzeRequiredObjects: async (kpiCodes: string[]) => {
    const { data } = await configClient.post('/api/analysis/required-objects', { kpi_codes: kpiCodes });
    return data;
  },

  // Service Proposals
  generateProposal: async (clientId: string, kpiCodes: string[], integrationMethod: 'batch' | 'realtime') => {
    const { data } = await configClient.post<ServiceProposal>('/api/proposals', {
      client_id: clientId,
      kpi_codes: kpiCodes,
      integration_method: integrationMethod,
    });
    return data;
  },

  getProposal: async (proposalId: string) => {
    const { data } = await configClient.get<ServiceProposal>(`/api/proposals/${proposalId}`);
    return data;
  },
};

export default { metadataApi, configApi };
