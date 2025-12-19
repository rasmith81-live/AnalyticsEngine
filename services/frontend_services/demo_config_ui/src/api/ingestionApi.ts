import axios from 'axios';

const BASE_URL = 'http://localhost:8090/api/v1/ingestion';

const api = axios.create({
  baseURL: BASE_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface IngestionJob {
  job_id?: string;
  connection_id: string;
  target_entity: string;
  schedule: string; // Cron or "immediate"
  status: string;
  last_run?: string;
}

export const ingestionApi = {
  async createJob(job: IngestionJob): Promise<{ job_id: string; status: string }> {
    const response = await api.post('/jobs', job);
    return response.data;
  },

  async runJob(jobId: string): Promise<{ message: string; job_id: string }> {
    const response = await api.post(`/jobs/${jobId}/run`);
    return response.data;
  },

  async getJobStatus(jobId: string): Promise<IngestionJob> {
    const response = await api.get(`/jobs/${jobId}`);
    return response.data;
  },

  async previewTransformation(data: any[], rules: any[]): Promise<any[]> {
    const response = await api.post('/transform/preview', { data, rules });
    return response.data;
  },
};

export default ingestionApi;
