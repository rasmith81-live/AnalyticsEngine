import axios from 'axios';

const BASE_URL = 'http://localhost:8090/api/v1/observability';

const api = axios.create({
  baseURL: BASE_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface LogEntry {
  timestamp: string;
  level: string;
  service: string;
  message: string;
  correlation_id?: string;
  metadata?: Record<string, any>;
}

export interface MetricPoint {
  name: string;
  value: number;
  unit: string;
  timestamp: string;
  labels?: Record<string, string>;
}

export const observabilityApi = {
  async sendTelemetry(data: any): Promise<{ status: string; correlation_id: string }> {
    const response = await api.post('/telemetry', data);
    return response.data;
  },

  async getLogs(params: {
    service?: string;
    level?: string;
    start_time?: string;
    end_time?: string;
    limit?: number;
  }): Promise<LogEntry[]> {
    const response = await api.get('/logs', { params });
    return response.data;
  },

  async getMetrics(params: {
    name?: string;
    start_time?: string;
    end_time?: string;
    interval?: string;
  }): Promise<MetricPoint[]> {
    const response = await api.get('/metrics', { params });
    return response.data;
  },
};

export default observabilityApi;
