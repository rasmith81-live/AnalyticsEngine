/**
 * Metadata API Client
 * Handles communication with the analytics_metadata_service
 */

import axios from 'axios';
import type { KPI, ObjectModel, Module } from '../types';

const BASE_URL = 'http://localhost:8020/api/v1';

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
    const response = await api.get(`/kpis/by-module/${moduleCode}`);
    return response.data;
  },

  async getKPIsByValueChain(valueChain: string): Promise<KPI[]> {
    const response = await api.get(`/kpis/by-value-chain/${valueChain}`);
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
    const response = await api.get(`/object-models/by-module/${moduleCode}`);
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

  // Value Chain endpoints
  async getValueChains(): Promise<string[]> {
    const response = await api.get('/value-chains');
    return response.data;
  },

  // Industry endpoints
  async getIndustries(): Promise<string[]> {
    const response = await api.get('/industries');
    return response.data;
  },
};

export default metadataApi;
