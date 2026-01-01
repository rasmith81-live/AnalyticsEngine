import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8090/api/v1/conversation';

const api = axios.create({
  baseURL: BASE_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface ChatMessage {
  role: 'user' | 'assistant' | 'system';
  content: string;
  timestamp?: string;
}

export interface ChatSession {
  session_id: string;
  user_id: string;
  messages: ChatMessage[];
  context?: Record<string, any>;
  created_at: string;
  updated_at: string;
}

export interface ChatResponse {
  response: string;
  session_id: string;
  intent?: string;
  entities?: Record<string, any>;
}

// Client Configuration Types
export interface ClientConfigurationRequest {
  client_id: string;
  client_name: string;
  name: string;
  description?: string;
  source_session_id?: string;
}

export interface SaveRecordingRequest {
  session_id: string;
  transcript: string;
  duration_seconds?: number;
  speaker_count?: number;
  recorded_at: string;
  segments?: Array<{
    id: string;
    text: string;
    timestamp: string;
    isFinal: boolean;
  }>;
}

export interface SaveIntentRequest {
  name: string;
  description?: string;
  confidence: number;
  domain: string;
  category?: string;
  target_entities?: string[];
  requested_metrics?: string[];
  parameters?: Record<string, any>;
  source_utterance?: string;
}

export interface SaveEntityRequest {
  name: string;
  entity_type: string;
  description?: string;
  properties?: Record<string, any>;
  extraction_confidence?: number;
  source_context?: string;
}

export interface ValueChainNodeRequest {
  id: string;
  name: string;
  type: string;
  description?: string;
  properties?: Record<string, any>;
}

export interface ValueChainLinkRequest {
  source_id: string;
  target_id: string;
  type: string;
}

export interface SaveValueChainModelRequest {
  name: string;
  description?: string;
  version?: string;
  nodes: ValueChainNodeRequest[];
  links: ValueChainLinkRequest[];
  generated_from_session?: string;
  generation_method?: string;
}

export interface SaveFullConfigurationRequest {
  configuration: ClientConfigurationRequest;
  recordings?: SaveRecordingRequest[];
  intents?: SaveIntentRequest[];
  entities?: SaveEntityRequest[];
  value_chain_model?: SaveValueChainModelRequest;
}

export interface ClientConfigurationResponse {
  id: number;
  uuid: string;
  client_id: string;
  client_name: string;
  name: string;
  description?: string;
  version: string;
  status: string;
  source_session_id?: string;
  created_at: string;
  updated_at: string;
  recording_count: number;
  intent_count: number;
  entity_count: number;
  model_count: number;
}

export interface FullClientConfigurationResponse {
  configuration: ClientConfigurationResponse;
  recordings: any[];
  intents: any[];
  entities: any[];
  value_chain_models: any[];
}

export interface ClientConfigurationListResponse {
  items: ClientConfigurationResponse[];
  total: number;
  page: number;
  page_size: number;
}

export const conversationApi = {
  async startSession(userId: string): Promise<ChatSession> {
    const response = await api.post('/session', null, {
      params: { user_id: userId },
    });
    return response.data;
  },

  async getSession(sessionId: string): Promise<ChatSession> {
    const response = await api.get(`/session/${sessionId}`);
    return response.data;
  },

  async processUtterance(sessionId: string, utterance: string): Promise<ChatResponse> {
    const response = await api.post('/utterance', {
      session_id: sessionId,
      utterance,
    });
    return response.data;
  },

  // Client Configuration API
  async saveFullConfiguration(request: SaveFullConfigurationRequest): Promise<FullClientConfigurationResponse> {
    const response = await api.post('/client-config/save-full', request);
    return response.data;
  },

  async getClientConfigurations(
    clientId: string,
    page: number = 1,
    pageSize: number = 20,
    status?: string
  ): Promise<ClientConfigurationListResponse> {
    const params: Record<string, any> = { page, page_size: pageSize };
    if (status) params.status = status;
    const response = await api.get(`/client-config/clients/${clientId}/configurations`, { params });
    return response.data;
  },

  async searchConfigurations(
    clientName?: string,
    dateFrom?: string,
    dateTo?: string,
    status?: string,
    page: number = 1,
    pageSize: number = 20
  ): Promise<ClientConfigurationListResponse> {
    const params: Record<string, any> = { page, page_size: pageSize };
    if (clientName) params.client_name = clientName;
    if (dateFrom) params.date_from = dateFrom;
    if (dateTo) params.date_to = dateTo;
    if (status) params.status = status;
    const response = await api.get('/client-config/search', { params });
    return response.data;
  },

  async getConfiguration(configId: number): Promise<FullClientConfigurationResponse> {
    const response = await api.get(`/client-config/configurations/${configId}`);
    return response.data;
  },

  async deleteConfiguration(configId: number): Promise<void> {
    await api.delete(`/client-config/configurations/${configId}`);
  },

  async updateConfigurationStatus(configId: number, status: string): Promise<ClientConfigurationResponse> {
    const response = await api.patch(`/client-config/configurations/${configId}`, { status });
    return response.data;
  },
};

export default conversationApi;
