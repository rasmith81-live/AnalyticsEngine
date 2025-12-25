import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8090/api/v1/metadata-ingestion';

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

  // KPI Excel Import (fast - no LLM)
  async uploadExcel(file: File): Promise<{
    importId: string;
    totalRows: number;
    validRows: number;
    errors: Array<{ row: number; column: string; message: string; data: any }>;
    preview: any[];
    duplicates: Array<{ kpi: any; matches: any[] }>;
    enriched: boolean;
    allKpiCodes?: string[];
  }> {
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await api.post('/import/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      timeout: 60000, // 1 minute - fast parsing only
    });
    return response.data;
  },

  // Optional AI enrichment (uses LLM)
  async enrichImport(importId: string): Promise<{
    importId: string;
    enriched: boolean;
    kpiCount: number;
    preview: any[];
    ontology_sync?: {
      value_chains_created: string[];
      modules_created: string[];
      entities_created: string[];
      relationships_created: string[];
      errors: string[];
    };
    allKpiCodes?: string[];
  }> {
    const response = await api.post(`/import/${importId}/enrich`, null, {
      timeout: 300000, // 5 minutes for LLM processing
    });
    return response.data;
  },

  async commitImport(importId: string, ontologyEdits?: any): Promise<{ success: boolean; count: number; ids: string[] }> {
    const response = await api.post(`/import/${importId}/commit`, ontologyEdits ? { ontology: ontologyEdits } : undefined);
    return response.data;
  },

  async getValueChains(): Promise<Array<{ code: string; name: string; description?: string }>> {
    const response = await axios.get('http://127.0.0.1:8090/api/v1/metadata/definitions/value_chain_pattern_definition');
    return response.data;
  },

  async getModules(): Promise<Array<{ code: string; name: string }>> {
    const response = await axios.get('http://127.0.0.1:8090/api/v1/metadata/definitions/business_process_definition');
    return response.data;
  }
};

export default metadataIngestionApi;
