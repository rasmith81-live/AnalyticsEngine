import axios from 'axios';

const BASE_URL = 'http://localhost:8090/api/v1/connector';

const api = axios.create({
  baseURL: BASE_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface ConnectionProfile {
  id: string;
  name: string;
  type: 'sql_postgres' | 'sql_mssql' | 'rest_api' | 'excel_file';
  host?: string;
  port?: number;
  database?: string;
  username?: string;
  password?: string;
  api_url?: string;
  file_path?: string;
  extra_params?: Record<string, string>;
  schedule?: {
    frequency: 'manual' | 'daily' | 'weekly' | 'custom';
    time?: string;
    cron_expression?: string;
    active: boolean;
  };
  selected_tables?: string[]; // List of table names to ingest
}

export interface TableDefinition {
  name: string;
  columns: {
    name: string;
    data_type: string;
    is_nullable: boolean;
    is_primary_key: boolean;
  }[];
}

export const connectorApi = {
  async createConnection(profile: ConnectionProfile): Promise<{ message: string; id: string }> {
    const response = await api.post('/connections', profile);
    return response.data;
  },

  async updateConnection(id: string, profile: Partial<ConnectionProfile>): Promise<ConnectionProfile> {
    const response = await api.put(`/connections/${id}`, profile);
    return response.data;
  },

  async deleteConnection(id: string): Promise<void> {
    await api.delete(`/connections/${id}`);
  },

  async getConnection(connectionId: string): Promise<ConnectionProfile> {
    const response = await api.get(`/connections/${connectionId}`);
    return response.data;
  },

  async testConnection(profile: ConnectionProfile): Promise<{ success: boolean }> {
    const response = await api.post('/connections/test', profile);
    return response.data;
  },

  async discoverSchema(connectionId: string): Promise<TableDefinition[]> {
    const response = await api.post('/discovery/schema', null, {
      params: { connection_id: connectionId }
    });
    return response.data;
  },

  async previewData(connectionId: string, tableName: string, limit: number = 5): Promise<Record<string, any>[]> {
    const response = await api.post('/discovery/preview', null, {
      params: { 
        connection_id: connectionId,
        table_name: tableName,
        limit
      }
    });
    return response.data;
  },
};

export default connectorApi;
