import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8090/api/v1/entity-resolution';

const api = axios.create({
  baseURL: BASE_URL,
  timeout: 60000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface SourceRecord {
  record_id: string;
  source_system: string;
  entity_type: string;
  attributes: Record<string, any>;
  timestamp?: string;
}

export interface MatchResult {
  job_id: string;
  status: string;
  message?: string;
}

export const entityResolutionApi = {
  async runMatchingJob(sourceRecords: SourceRecord[], threshold: number = 0.85): Promise<MatchResult> {
    const response = await api.post('/matching/run', {
      source_records: sourceRecords,
      threshold,
    });
    return response.data;
  },

  async createGoldenRecord(matchCandidateIds: string[], strategy: string = 'frequency_based'): Promise<{ golden_record_id: string; status: string }> {
    const response = await api.post('/merging/create-golden-record', {
      match_candidate_ids: matchCandidateIds,
      strategy,
    });
    return response.data;
  },

  async triggerRetroactiveFix(entityId: string): Promise<{ task_id: string; status: string }> {
    const response = await api.post('/retroactive/fix', null, {
      params: { entity_id: entityId },
    });
    return response.data;
  },
};

export default entityResolutionApi;
