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
};

export default conversationApi;
