import axios from 'axios';

const BASE_URL = 'http://localhost:8090/api/v1/metadata-ingestion';

const api = axios.create({
  baseURL: BASE_URL,
  timeout: 60000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface KPIDecomposition {
  decomposed: Record<string, any>;
  resolved_components: Record<string, any>;
}

export const metadataIngestionApi = {
  async listIndustries(): Promise<Record<string, any>[]> {
    const response = await api.get('/knowledge/industries');
    return response.data;
  },

  async getIndustryValueChain(code: string): Promise<Record<string, any>> {
    const response = await api.get(`/knowledge/industries/${code}/value-chain`);
    return response.data;
  },

  async getIndustryKPIs(code: string): Promise<Record<string, any>> {
    const response = await api.get(`/knowledge/industries/${code}/kpis`);
    return response.data;
  },

  async decomposeKPI(formula: string): Promise<KPIDecomposition> {
    const response = await api.post('/mapping/decompose', { formula });
    return response.data;
  },

  // KPI Excel Import
  async uploadExcel(file: File): Promise<{
    importId: string;
    totalRows: number;
    validRows: number;
    errors: Array<{ row: number; column: string; message: string; data: any }>;
    preview: any[];
    duplicates: Array<{ kpi: any; matches: any[] }>;
  }> {
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await api.post('/import/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  },

  async commitImport(importId: string): Promise<{ success: boolean; count: number; ids: string[] }> {
    const response = await api.post(`/import/${importId}/commit`);
    return response.data;
  }
};

export default metadataIngestionApi;
