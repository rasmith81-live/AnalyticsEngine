/**
 * Metadata API Client
 * Handles communication with the analytics_metadata_service
 */

import axios from 'axios';
import type { KPI, ObjectModel, Module, ValueChain, Industry } from '../types';

const BASE_URL = 'http://localhost:8090/api/v1/metadata';

const api = axios.create({
  baseURL: BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const metadataApi = {
  // KPI endpoints
  async getKPIs(): Promise<KPI[]> {
    const response = await api.get('/kpis');
    return response.data;
  },

  async getKPI(code: string): Promise<KPI> {
    const response = await api.get(`/kpis/${code}`);
    return response.data;
  },

  async getKPIsByModule(moduleCode: string): Promise<KPI[]> {
    const response = await api.get(`/kpis/module/${moduleCode}`);
    return response.data;
  },

  async getKPIsByValueChain(valueChain: string): Promise<KPI[]> {
    const response = await api.get(`/kpis/value-chain/${valueChain}`);
    return response.data;
  },

  // Object Model endpoints
  async getObjectModels(): Promise<ObjectModel[]> {
    const response = await api.get('/object-models');
    return response.data;
  },

  async getObjectModel(code: string): Promise<ObjectModel> {
    const response = await api.get(`/object-models/${code}`);
    return response.data;
  },

  async getObjectModelsByModule(moduleCode: string): Promise<ObjectModel[]> {
    const response = await api.get(`/object-models/module/${moduleCode}`);
    return response.data;
  },

  // Module endpoints
  async getModules(): Promise<Module[]> {
    const response = await api.get('/modules');
    return response.data;
  },

  async getModule(code: string): Promise<Module> {
    const response = await api.get(`/modules/${code}`);
    return response.data;
  },

  async getModulesByValueChain(valueChainCode: string): Promise<Module[]> {
    const response = await api.get(`/modules/value-chain/${valueChainCode}`);
    return response.data;
  },

  // Value Chain endpoints
  async getValueChains(): Promise<ValueChain[]> {
    const response = await api.get('/value-chains');
    return response.data;
  },

  async getValueChain(code: string): Promise<ValueChain> {
    // Note: Gateway needs get_value_chain implementation if singular fetch is needed
    // Assuming list + client-side filter or implement get_value_chain in backend
    // For now, let's implement get_value_chain in backend later if needed, or assume list returns full objects
    // Actually, useValueChain hook uses this.
    // I'll add getValueChain to the API, assuming backend supports /value-chains/{code}
    // Checking metadata_client.py -> I didn't add get_value_chain(code).
    // I should add it.
    const response = await api.get(`/value-chains/${code}`);
    return response.data;
  },

  // Industry endpoints
  async getIndustries(): Promise<Industry[]> {
    const response = await api.get('/industries');
    return response.data;
  },

  async getIndustryValueChains(code: string): Promise<ValueChain[]> {
    const response = await api.get(`/industries/${code}/value-chains`);
    return response.data;
  },
};

export default metadataApi;
