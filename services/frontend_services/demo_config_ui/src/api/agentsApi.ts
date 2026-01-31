/**
 * Multi-Agent Design API
 * 
 * API client for the multi-agent design system endpoints.
 * Provides real-time agent interaction via REST and WebSocket.
 */

import axios from 'axios';

const BASE_URL = 'http://localhost:8026/api/v1/agents';

const api = axios.create({
  baseURL: BASE_URL,
  timeout: 300000, // 5 minutes for LLM responses
  headers: {
    'Content-Type': 'application/json',
  },
});

// =============================================================================
// Types
// =============================================================================

export interface CreateSessionRequest {
  user_id: string;
  business_description?: string;
  industry?: string;
}

export interface CreateSessionResponse {
  session_id: string;
  user_id: string;
  status: string;
  message: string;
}

export interface SendMessageRequest {
  message: string;
}

export interface SendMessageResponse {
  session_id: string;
  agent_role: string;
  content: string;
  artifacts: Record<string, any>;
  success: boolean;
  error?: string;
}

export interface SessionDetails {
  session_id: string;
  user_id: string;
  status: string;
  created_at: string;
  updated_at: string;
  message_count: number;
  artifacts_generated: boolean;
  context: {
    industry?: string;
    value_chain_type?: string;
    identified_entities: string[];
    identified_kpis: string[];
  };
}

export interface SessionArtifacts {
  session_id: string;
  artifacts: Record<string, any>;
  entities: string[];
  kpis: string[];
}

export interface FinalizeSessionResponse {
  success: boolean;
  session_id: string;
  status: string;
  value_chain: Record<string, any>;
  artifacts: Record<string, any>;
  validation: Record<string, any>;
}

export interface SessionListItem {
  session_id: string;
  user_id: string;
  status: string;
  created_at: string;
  message_count: number;
}

export interface ParallelAnalysisResponse {
  session_id: string;
  results: Record<string, {
    agent_role: string;
    content: string;
    artifacts: Record<string, any>;
    success: boolean;
    error?: string;
  }>;
}

// Design Progress Types
export type DesignCategoryStatus = 'not_started' | 'in_progress' | 'partially_complete' | 'complete';

export interface DesignCategoryProgress {
  status: DesignCategoryStatus;
  findings: string[];
  outstanding: string[];
  contributing_agents: string[];
}

export interface DesignProgress {
  business_model?: DesignCategoryProgress;
  value_chain?: DesignCategoryProgress;
  entities?: DesignCategoryProgress;
  kpis?: DesignCategoryProgress;
  data_architecture?: DesignCategoryProgress;
  integrations?: DesignCategoryProgress;
  governance?: DesignCategoryProgress;
  analytics_use_cases?: DesignCategoryProgress;
}

// Agent Activity Types
export type AgentActivityType = 
  | 'delegation'
  | 'peer_consultation'
  | 'mcp_tool'
  | 'external_service'
  | 'synthesis'
  | 'tool_call'
  | 'ready_signal';

export interface AgentActivity {
  id: string;
  type: AgentActivityType;
  source: string;
  target?: string;
  tool?: string;
  details?: string;
  timestamp: Date;
}

// WebSocket Message Types
export type WSMessageType = 
  | 'connected'
  | 'processing'
  | 'chunk'
  | 'complete'
  | 'analyzing'
  | 'analysis_complete'
  | 'finalizing'
  | 'finalized'
  | 'agent_activity'
  | 'design_progress'
  | 'error'
  | 'pong'
  // Phase 17: Contract-related message types
  | 'contract_violation'
  | 'state_transition'
  | 'peer_review_required'
  | 'peer_review_complete'
  | 'struggle_signal'
  | 'hard_stop'
  | 'degraded_mode';

// Phase 17: Contract Event Interfaces
export interface ContractViolationMessage {
  type: 'contract_violation';
  agentRole: string;
  tier: number;
  ruleId: string;
  description: string;
  timestamp: string;
}

export interface StateTransitionMessage {
  type: 'state_transition';
  agentRole: string;
  fromState: string;
  toState: string;
  rationale: string;
  timestamp: string;
}

export interface PeerReviewMessage {
  type: 'peer_review_required' | 'peer_review_complete';
  artifactId: string;
  artifactType: string;
  creatorRole: string;
  reviewerRole: string;
  verdict?: 'approved' | 'rejected' | 'revision_needed';
  timestamp: string;
}

export interface StruggleSignalMessage {
  type: 'struggle_signal';
  agentRole: string;
  signalType: 'sync_needed' | 'blocked' | 'needs_clarification' | 'resource_needed';
  whatIUnderstand: string;
  whatITried: { action: string; result: string }[];
  whereImStuck: string;
  whatWouldHelp: string;
  timestamp: string;
}

export interface HardStopMessage {
  type: 'hard_stop';
  agentRole: string;
  triggerType: string;
  reason: string;
  timestamp: string;
}

export interface DegradedModeMessage {
  type: 'degraded_mode';
  active: boolean;
  reason: string;
  suspendedFeatures: string[];
  activeFeatures: string[];
  timestamp: string;
}

export interface WSMessage {
  type: WSMessageType;
  content?: string;
  message?: string;
  session_id?: string;
  status?: string;
  results?: Record<string, any>;
  result?: Record<string, any>;
  activity?: AgentActivity;
  progress?: DesignProgress;
  // Phase 17: Contract event fields
  agentRole?: string;
  tier?: number;
  ruleId?: string;
  description?: string;
  fromState?: string;
  toState?: string;
  rationale?: string;
  artifactId?: string;
  artifactType?: string;
  creatorRole?: string;
  reviewerRole?: string;
  verdict?: string;
  signalType?: string;
  whatIUnderstand?: string;
  whatITried?: { action: string; result: string }[];
  whereImStuck?: string;
  whatWouldHelp?: string;
  triggerType?: string;
  reason?: string;
  active?: boolean;
  suspendedFeatures?: string[];
  activeFeatures?: string[];
  timestamp?: string;
}

// =============================================================================
// REST API
// =============================================================================

export const agentsApi = {
  /**
   * Create a new design session
   */
  async createSession(request: CreateSessionRequest): Promise<CreateSessionResponse> {
    const response = await api.post('/design-session', request);
    return response.data;
  },

  /**
   * Get session details
   */
  async getSession(sessionId: string): Promise<SessionDetails> {
    const response = await api.get(`/sessions/${sessionId}`);
    return response.data;
  },

  /**
   * Send a message to a design session
   */
  async sendMessage(sessionId: string, message: string): Promise<SendMessageResponse> {
    const response = await api.post(`/sessions/${sessionId}/message`, { message });
    return response.data;
  },

  /**
   * Run parallel analysis with multiple agents
   */
  async runParallelAnalysis(
    sessionId: string, 
    analysisType: string = 'comprehensive'
  ): Promise<ParallelAnalysisResponse> {
    const response = await api.post(`/sessions/${sessionId}/analyze`, { 
      analysis_type: analysisType 
    });
    return response.data;
  },

  /**
   * Get session artifacts
   */
  async getArtifacts(sessionId: string): Promise<SessionArtifacts> {
    const response = await api.get(`/sessions/${sessionId}/artifacts`);
    return response.data;
  },

  /**
   * Finalize a design session
   */
  async finalizeSession(sessionId: string): Promise<FinalizeSessionResponse> {
    const response = await api.post(`/sessions/${sessionId}/finalize`);
    return response.data;
  },

  /**
   * Cancel a design session
   */
  async cancelSession(sessionId: string): Promise<{ success: boolean; session_id: string; status: string }> {
    const response = await api.delete(`/sessions/${sessionId}`);
    return response.data;
  },

  /**
   * List all sessions
   */
  async listSessions(userId?: string): Promise<{ sessions: SessionListItem[] }> {
    const params = userId ? { user_id: userId } : {};
    const response = await api.get('/sessions', { params });
    return response.data;
  },
};

// =============================================================================
// WebSocket Client
// =============================================================================

export class AgentWebSocket {
  private ws: WebSocket | null = null;
  private sessionId: string;
  private onMessage: (message: WSMessage) => void;
  private onActivity: (activity: AgentActivity) => void;
  private onProgress: (progress: DesignProgress) => void;
  private onError: (error: string) => void;
  private onConnect: () => void;
  private onDisconnect: () => void;
  private reconnectAttempts = 0;
  private maxReconnectAttempts = 3;
  private pingInterval: ReturnType<typeof setInterval> | null = null;
  private intentionalClose = false;
  private hasConnected = false;

  constructor(
    sessionId: string,
    callbacks: {
      onMessage: (message: WSMessage) => void;
      onActivity: (activity: AgentActivity) => void;
      onProgress: (progress: DesignProgress) => void;
      onError: (error: string) => void;
      onConnect: () => void;
      onDisconnect: () => void;
    }
  ) {
    this.sessionId = sessionId;
    this.onMessage = callbacks.onMessage;
    this.onActivity = callbacks.onActivity;
    this.onProgress = callbacks.onProgress;
    this.onError = callbacks.onError;
    this.onConnect = callbacks.onConnect;
    this.onDisconnect = callbacks.onDisconnect;
  }

  connect(): void {
    const wsUrl = `ws://localhost:8026/api/v1/agents/ws/${this.sessionId}`;
    this.ws = new WebSocket(wsUrl);

    this.ws.onopen = () => {
      console.log(`WebSocket connected to session ${this.sessionId}`);
      this.reconnectAttempts = 0;
      this.hasConnected = true;
      this.onConnect();
      this.startPing();
    };

    this.ws.onmessage = (event) => {
      try {
        const message: WSMessage = JSON.parse(event.data);
        
        // Handle special message types
        if (message.type === 'agent_activity' && message.activity) {
          this.onActivity({
            ...message.activity,
            timestamp: new Date(message.activity.timestamp)
          });
        } else if (message.type === 'design_progress' && message.progress) {
          this.onProgress(message.progress);
        } else if (message.type === 'error') {
          this.onError(message.message || 'Unknown error');
        } else {
          this.onMessage(message);
        }
      } catch (e) {
        console.error('Failed to parse WebSocket message:', e);
      }
    };

    this.ws.onerror = (error) => {
      console.error('WebSocket error:', error);
      // Only show error if we haven't connected yet and it's the first attempt
      if (!this.hasConnected && this.reconnectAttempts === 0) {
        // Don't show error - we'll fall back to REST API
        console.log('WebSocket connection failed, will use REST API fallback');
      }
    };

    this.ws.onclose = (event) => {
      console.log('WebSocket disconnected', event.code, event.reason);
      this.stopPing();
      this.onDisconnect();
      
      // Only attempt reconnect if it wasn't intentional and we had previously connected
      if (!this.intentionalClose && this.hasConnected && this.reconnectAttempts < this.maxReconnectAttempts) {
        this.reconnectAttempts++;
        console.log(`Reconnect attempt ${this.reconnectAttempts}/${this.maxReconnectAttempts}`);
        setTimeout(() => this.connect(), 2000 * this.reconnectAttempts);
      }
    };
  }

  private startPing(): void {
    this.pingInterval = setInterval(() => {
      this.send({ type: 'ping' });
    }, 30000);
  }

  private stopPing(): void {
    if (this.pingInterval) {
      clearInterval(this.pingInterval);
      this.pingInterval = null;
    }
  }

  send(data: { type: string; content?: string; analysis_type?: string }): void {
    if (this.ws && this.ws.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify(data));
    }
  }

  sendMessage(content: string): void {
    this.send({ type: 'message', content });
  }

  requestAnalysis(analysisType: string = 'comprehensive'): void {
    this.send({ type: 'analyze', analysis_type: analysisType });
  }

  requestFinalize(): void {
    this.send({ type: 'finalize' });
  }

  disconnect(): void {
    this.intentionalClose = true;
    this.stopPing();
    if (this.ws) {
      this.ws.close();
      this.ws = null;
    }
  }

  isConnected(): boolean {
    return this.ws !== null && this.ws.readyState === WebSocket.OPEN;
  }
}

// =============================================================================
// Design Category Helpers
// =============================================================================

export const DESIGN_CATEGORIES: Record<string, { name: string; description: string; icon: string }> = {
  business_model: {
    name: 'Business Model',
    description: 'Business model and strategic positioning',
    icon: '🏢'
  },
  value_chain: {
    name: 'Value Chain',
    description: 'Value chain structure and processes',
    icon: '🔗'
  },
  entities: {
    name: 'Entities',
    description: 'Core business entities and relationships',
    icon: '📦'
  },
  kpis: {
    name: 'KPIs',
    description: 'Key Performance Indicators and metrics',
    icon: '📊'
  },
  data_architecture: {
    name: 'Data Architecture',
    description: 'Data architecture and storage design',
    icon: '🗄️'
  },
  integrations: {
    name: 'Integrations',
    description: 'System integrations and data flows',
    icon: '🔌'
  },
  governance: {
    name: 'Governance',
    description: 'Data governance and quality rules',
    icon: '📋'
  },
  analytics_use_cases: {
    name: 'Analytics',
    description: 'Analytics use cases and dashboards',
    icon: '📈'
  }
};

export function getProgressPercentage(progress: DesignProgress): number {
  const categories = Object.keys(DESIGN_CATEGORIES);
  let completed = 0;
  
  for (const category of categories) {
    const categoryProgress = progress[category as keyof DesignProgress];
    if (categoryProgress?.status === 'complete') {
      completed += 1;
    } else if (categoryProgress?.status === 'partially_complete') {
      completed += 0.5;
    } else if (categoryProgress?.status === 'in_progress') {
      completed += 0.25;
    }
  }
  
  return Math.round((completed / categories.length) * 100);
}

export default agentsApi;
