import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8090/api/v1/calculations';

const api = axios.create({
  baseURL: BASE_URL,
  timeout: 60000, // Longer timeout for calculations
  headers: {
    'Content-Type': 'application/json',
  },
});

export const calculationApi = {
  async calculateKPI(params: {
    kpi_code: string;
    time_period?: { start_date: string; end_date: string };
    filters?: Record<string, any>;
    aggregation?: string;
  }) {
    const response = await api.post('/calculate', params);
    return response.data;
  },

  async calculateBatch(params: {
    kpi_codes: string[];
    time_period?: { start_date: string; end_date: string };
    filters?: Record<string, any>;
  }) {
    const response = await api.post('/calculate/batch', params);
    return response.data;
  },

  async calculateDashboard(config: {
    dashboard_id: string;
    kpi_codes: string[];
    time_period?: { start_date: string; end_date: string };
    filters?: Record<string, any>;
  }) {
    const response = await api.post('/calculate/dashboard', config);
    return response.data;
  },

  async scheduleBatchJob(jobConfig: {
    job_name: string;
    schedule: { frequency: string; time: string; timezone: string };
    kpi_codes: string[];
    filters?: Record<string, any>;
    output?: { store_results: boolean; cache_ttl: number; notify_on_completion: boolean };
  }) {
    const response = await api.post('/batch/schedule', jobConfig);
    return response.data;
  },
};

export default calculationApi;
