import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8090/api/v1/config';

const api = axios.create({
  baseURL: BASE_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface ClientConfig {
  id: string;
  client_id: string;
  client_name: string;
  industry?: string;
  selected_kpis: string[];
  custom_kpis?: CustomKPI[];
  data_sources?: any[];
  deployment_config?: Record<string, any>;
  license_key?: string;
  license_expiration?: string;
  created_at?: string;
  updated_at?: string;
}

export interface CustomKPI {
  code: string;
  name: string;
  formula: string;
  description?: string;
}

export interface ServiceProposal {
  id?: string;
  client_id: string;
  required_objects: string[];
  integration_method: 'batch' | 'realtime';
  estimated_hours: number;
  estimated_cost: number;
  timeline_weeks: number;
  status: 'draft' | 'sent' | 'signed';
  breakdown?: any;
  created_at?: string;
}

export const configApi = {
  // Client Configurations
  async getClientConfigs(): Promise<ClientConfig[]> {
    const response = await api.get('/clients');
    return response.data;
  },

  async getClientConfig(clientId: string): Promise<ClientConfig> {
    const response = await api.get(`/clients/${clientId}`);
    return response.data;
  },

  async createClientConfig(config: Omit<ClientConfig, 'id'>): Promise<ClientConfig> {
    const response = await api.post('/clients', config);
    return response.data;
  },

  async updateClientConfig(clientId: string, config: Partial<ClientConfig>): Promise<ClientConfig> {
    const response = await api.put(`/clients/${clientId}`, config);
    return response.data;
  },

  async deleteClientConfig(clientId: string): Promise<void> {
    await api.delete(`/clients/${clientId}`);
  },

  // Custom KPIs
  async createCustomKPI(clientId: string, kpi: CustomKPI): Promise<CustomKPI> {
    const response = await api.post(`/clients/${clientId}/custom-kpis`, kpi);
    return response.data;
  },

  async getCustomKPIs(clientId: string): Promise<CustomKPI[]> {
    const response = await api.get(`/clients/${clientId}/custom-kpis`);
    return response.data;
  },

  // Service Proposals
  async generateProposal(clientId: string, options: { 
    integration_method: 'batch' | 'realtime'; 
    included_kpis: string[];
    license_tier?: 'starter' | 'professional' | 'enterprise';
    user_count?: number;
    infrastructure?: 'cloud' | 'onprem';
  }): Promise<ServiceProposal> {
    const response = await api.post(`/clients/${clientId}/proposal`, options);
    return response.data;
  },

  async getProposal(clientId: string): Promise<ServiceProposal> {
    const response = await api.get(`/clients/${clientId}/proposal`);
    return response.data;
  },

  async updateProposal(clientId: string, proposal: Partial<ServiceProposal>): Promise<ServiceProposal> {
    const response = await api.put(`/clients/${clientId}/proposal`, proposal);
    return response.data;
  },
};

export default configApi;
