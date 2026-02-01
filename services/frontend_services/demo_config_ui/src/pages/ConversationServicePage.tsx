import { useState, useEffect, useRef, useCallback } from 'react';
import {
  Send,
  RefreshCw,
  Network,
  Brain,
  GitBranch,
  Link2,
  ChevronRight,
  X,
  Users,
  Activity,
  CheckCircle2,
  Circle,
  ArrowRight,
  Zap,
  Database,
  MessageSquare,
  Bot,
  User,
  Loader2,
  AlertCircle,
  Mic,
  Square,
  AudioWaveform,
} from 'lucide-react';
import { Card, CardHeader, CardTitle } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { cn } from '../lib/utils';
import {
  agentsApi,
  AgentWebSocket,
  AgentActivity,
  DesignProgress,
  DESIGN_CATEGORIES,
  getProgressPercentage,
  WSMessage,
  SendMessageResponse,
} from '../api/agentsApi';

// =============================================================================
// Types
// =============================================================================

interface ChatMessage {
  id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  timestamp: Date;
  agentRole?: string;
  isStreaming?: boolean;
}

interface ValueChainNode {
  id: string;
  name: string;
  type: string;
  description?: string;
  properties?: Record<string, any>;
}

interface ValueChainLink {
  source_id: string;
  target_id: string;
  type: string;
}

declare global {
  interface Window {
    SpeechRecognition: any;
    webkitSpeechRecognition: any;
  }
}

// =============================================================================
// Components
// =============================================================================

function TabButton({ active, onClick, children, badge }: { 
  active: boolean; 
  onClick: () => void; 
  children: React.ReactNode;
  badge?: number;
}) {
  return (
    <button
      onClick={onClick}
      className={cn(
        "px-4 py-2 text-sm font-medium transition-colors relative",
        active 
          ? "text-alpha-500 border-b-2 border-alpha-500" 
          : "theme-text-muted hover:theme-text"
      )}
    >
      {children}
      {badge !== undefined && badge > 0 && (
        <span className="absolute -top-1 -right-1 w-5 h-5 rounded-full bg-alpha-500 text-white text-xs flex items-center justify-center">
          {badge}
        </span>
      )}
    </button>
  );
}

function ProgressBar({ progress }: { progress: DesignProgress }) {
  const percentage = getProgressPercentage(progress);
  
  return (
    <div className="mb-4">
      <div className="flex items-center justify-between mb-2">
        <span className="text-sm font-medium theme-text-title">Design Progress</span>
        <span className="text-sm theme-text-muted">{percentage}%</span>
      </div>
      <div className="h-2 rounded-full bg-alpha-faded-200 dark:bg-alpha-faded-800 overflow-hidden">
        <div 
          className="h-full bg-gradient-to-r from-alpha-500 to-green-500 transition-all duration-500"
          style={{ width: `${percentage}%` }}
        />
      </div>
      <div className="flex flex-wrap gap-1 mt-2">
        {Object.entries(DESIGN_CATEGORIES).map(([key, cat]) => {
          const categoryProgress = progress[key as keyof DesignProgress];
          const status = categoryProgress?.status || 'not_started';
          return (
            <span 
              key={key}
              className={cn(
                "px-2 py-0.5 rounded-full text-xs",
                status === 'complete' && "bg-green-500/20 text-green-400",
                status === 'partially_complete' && "bg-amber-500/20 text-amber-400",
                status === 'in_progress' && "bg-blue-500/20 text-blue-400",
                status === 'not_started' && "bg-gray-500/20 text-gray-400"
              )}
              title={cat.description}
            >
              {cat.icon} {cat.name}
            </span>
          );
        })}
      </div>
    </div>
  );
}

function AgentActivityItem({ activity }: { activity: AgentActivity }) {
  const getIcon = () => {
    switch (activity.type) {
      case 'delegation': return <ArrowRight className="w-4 h-4 text-blue-400" />;
      case 'peer_consultation': return <Users className="w-4 h-4 text-purple-400" />;
      case 'mcp_tool': return <Database className="w-4 h-4 text-green-400" />;
      case 'external_service': return <Zap className="w-4 h-4 text-amber-400" />;
      case 'synthesis': return <Brain className="w-4 h-4 text-pink-400" />;
      case 'tool_call': return <Activity className="w-4 h-4 text-cyan-400" />;
      case 'ready_signal': return <CheckCircle2 className="w-4 h-4 text-green-400" />;
      default: return <Circle className="w-4 h-4 text-gray-400" />;
    }
  };

  const getLabel = () => {
    switch (activity.type) {
      case 'delegation': return `${activity.source} → ${activity.target}`;
      case 'peer_consultation': return `${activity.source} ⟷ ${activity.target}`;
      case 'mcp_tool': return `${activity.source} → MCP: ${activity.tool}`;
      case 'external_service': return `${activity.source} → Service: ${activity.target}`;
      case 'synthesis': return `${activity.source} synthesizing...`;
      case 'tool_call': return `${activity.source}: ${activity.tool}`;
      case 'ready_signal': return `${activity.source} ready`;
      default: return activity.details || 'Unknown activity';
    }
  };

  return (
    <div className="flex items-center gap-2 py-1.5 px-2 rounded-lg theme-card-bg-hover">
      {getIcon()}
      <span className="text-xs theme-text flex-1">{getLabel()}</span>
      <span className="text-xs theme-text-muted">
        {activity.timestamp.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', second: '2-digit' })}
      </span>
    </div>
  );
}

// =============================================================================
// Main Component
// =============================================================================

export default function ConversationServicePage() {
  // Session state
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [isConnected, setIsConnected] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [successMessage, setSuccessMessage] = useState<string | null>(null);

  // Chat state
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [textInput, setTextInput] = useState('');
  const [streamingContent, setStreamingContent] = useState('');

  // Agent activity state
  const [activities, setActivities] = useState<AgentActivity[]>([]);
  const [designProgress, setDesignProgress] = useState<DesignProgress>({});

  // Phase 17: Contract event state
  const [, setContractViolations] = useState<any[]>([]);
  const [, setStruggleSignals] = useState<any[]>([]);
  const [, setDegradedMode] = useState<{active: boolean; reason: string} | null>(null);

  // Artifacts state
  const [entities, setEntities] = useState<string[]>([]);
  const [kpis, setKpis] = useState<string[]>([]);
  const [valueChainNodes, setValueChainNodes] = useState<ValueChainNode[]>([]);
  const [valueChainLinks, setValueChainLinks] = useState<ValueChainLink[]>([]);

  // UI state
  const [activeTab, setActiveTab] = useState(0); // 0=Agents, 1=Intents, 2=Entities, 3=Model

  // Speech recognition state
  const [isListening, setIsListening] = useState(false);
  const [currentTranscript, setCurrentTranscript] = useState('');
  const [audioLevel, setAudioLevel] = useState(0);
  const [speechSupported, setSpeechSupported] = useState(true);

  // Refs
  const chatEndRef = useRef<HTMLDivElement>(null);
  const activityEndRef = useRef<HTMLDivElement>(null);
  const wsRef = useRef<AgentWebSocket | null>(null);
  const recognitionRef = useRef<any>(null);
  const audioContextRef = useRef<AudioContext | null>(null);
  const analyserRef = useRef<AnalyserNode | null>(null);
  const animationFrameRef = useRef<number | null>(null);
  const isListeningRef = useRef(false); // Ref to avoid stale closure in onend

  const userId = 'demo_user';

  // Check speech recognition support
  useEffect(() => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      setSpeechSupported(false);
    }
  }, []);

  // Auto-scroll chat
  const scrollToBottom = useCallback(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages, streamingContent, scrollToBottom]);

  // Auto-scroll activity feed
  useEffect(() => {
    activityEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [activities]);

  // Create session on mount
  const createSession = useCallback(async () => {
    try {
      setIsProcessing(true);
      setError(null);
      
      const response = await agentsApi.createSession({
        user_id: userId,
      });
      
      setSessionId(response.session_id);
      setMessages([{
        id: `msg_${Date.now()}`,
        role: 'assistant',
        content: response.message,
        timestamp: new Date(),
        agentRole: 'coordinator'
      }]);
      setActivities([]);
      setDesignProgress({});
      setEntities([]);
      setKpis([]);
      setValueChainNodes([]);
      setValueChainLinks([]);
      
    } catch (err) {
      console.error('Failed to create session:', err);
      setError('Failed to create session. Is the Conversation Service running on port 8026?');
    } finally {
      setIsProcessing(false);
    }
  }, [userId]);

  useEffect(() => {
    createSession();
  }, [createSession]);

  // WebSocket connection
  useEffect(() => {
    if (!sessionId) return;

    const ws = new AgentWebSocket(sessionId, {
      onMessage: (message: WSMessage) => {
        if (message.type === 'chunk') {
          setStreamingContent(prev => prev + (message.content || ''));
        } else if (message.type === 'complete') {
          // Finalize streaming message
          if (streamingContent || message.content) {
            setMessages(prev => [...prev, {
              id: `msg_${Date.now()}`,
              role: 'assistant',
              content: message.content || streamingContent,
              timestamp: new Date(),
              agentRole: 'coordinator'
            }]);
            setStreamingContent('');
          }
          setIsProcessing(false);
        } else if (message.type === 'processing') {
          setIsProcessing(true);
        } else if (message.type === 'analysis_complete' || message.type === 'finalized') {
          setIsProcessing(false);
          fetchArtifacts();
        }
        // Phase 17: Handle contract-related message types
        else if (message.type === 'contract_violation') {
          setContractViolations(prev => [...prev, {
            id: `violation_${Date.now()}`,
            agentRole: message.agentRole,
            tier: message.tier,
            ruleId: message.ruleId,
            description: message.description,
            timestamp: message.timestamp || new Date().toISOString()
          }]);
        } else if (message.type === 'struggle_signal') {
          setStruggleSignals(prev => [...prev, {
            id: `struggle_${Date.now()}`,
            agentRole: message.agentRole,
            signalType: message.signalType,
            whatIUnderstand: message.whatIUnderstand,
            whatITried: message.whatITried,
            whereImStuck: message.whereImStuck,
            whatWouldHelp: message.whatWouldHelp,
            timestamp: message.timestamp || new Date().toISOString()
          }]);
        } else if (message.type === 'degraded_mode') {
          setDegradedMode({
            active: message.active ?? true,
            reason: message.reason || 'Multi-agent service unavailable'
          });
        } else if (message.type === 'hard_stop') {
          // Hard stop - add as a system message
          setMessages(prev => [...prev, {
            id: `msg_${Date.now()}`,
            role: 'system',
            content: `⛔ HARD STOP: ${message.reason} (Agent: ${message.agentRole})`,
            timestamp: new Date()
          }]);
          setIsProcessing(false);
        }
      },
      onActivity: (activity: AgentActivity) => {
        setActivities(prev => {
          // Check for duplicate user->coordinator activities (aggregate them)
          const isDuplicate = prev.some(a => 
            a.type === activity.type && 
            a.source === activity.source && 
            a.target === activity.target &&
            // Within 5 seconds is considered duplicate
            Math.abs(new Date(a.timestamp).getTime() - new Date(activity.timestamp).getTime()) < 5000
          );
          if (isDuplicate) {
            return prev; // Don't add duplicate
          }
          return [...prev, activity];
        });
      },
      onProgress: (progress: DesignProgress) => {
        setDesignProgress(progress);
      },
      onError: (errorMsg: string) => {
        // Only show errors that aren't WebSocket connection issues
        // REST fallback will handle those cases
        if (!errorMsg.includes('WebSocket') && !errorMsg.includes('Session') ) {
          setError(errorMsg);
        }
        setIsProcessing(false);
      },
      onConnect: () => {
        setIsConnected(true);
      },
      onDisconnect: () => {
        setIsConnected(false);
      }
    });

    ws.connect();
    wsRef.current = ws;

    return () => {
      ws.disconnect();
      wsRef.current = null;
    };
  }, [sessionId]);

  // Fetch artifacts
  const fetchArtifacts = useCallback(async () => {
    if (!sessionId) return;
    
    try {
      const artifacts = await agentsApi.getArtifacts(sessionId);
      setEntities(artifacts.entities || []);
      setKpis(artifacts.kpis || []);
      
      // Extract value chain from artifacts if present
      if (artifacts.artifacts?.value_chain) {
        const vc = artifacts.artifacts.value_chain;
        setValueChainNodes(vc.nodes || []);
        setValueChainLinks(vc.links || []);
      }
    } catch (err) {
      console.error('Failed to fetch artifacts:', err);
    }
  }, [sessionId]);

  // Audio monitoring for visual feedback
  const setupAudioMonitoring = useCallback(async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      audioContextRef.current = new AudioContext();
      analyserRef.current = audioContextRef.current.createAnalyser();
      const source = audioContextRef.current.createMediaStreamSource(stream);
      source.connect(analyserRef.current);
      analyserRef.current.fftSize = 256;

      const updateLevel = () => {
        if (analyserRef.current) {
          const dataArray = new Uint8Array(analyserRef.current.frequencyBinCount);
          analyserRef.current.getByteFrequencyData(dataArray);
          const average = dataArray.reduce((a, b) => a + b) / dataArray.length;
          setAudioLevel(average / 255);
        }
        animationFrameRef.current = requestAnimationFrame(updateLevel);
      };
      updateLevel();
    } catch (err) {
      console.error('Error setting up audio monitoring:', err);
    }
  }, []);

  const cleanupAudioMonitoring = useCallback(() => {
    if (animationFrameRef.current) {
      cancelAnimationFrame(animationFrameRef.current);
    }
    if (audioContextRef.current) {
      audioContextRef.current.close();
    }
    setAudioLevel(0);
  }, []);

  // Process speech transcript
  const processSpeechTranscript = useCallback(async (text: string) => {
    if (!text.trim() || !sessionId) return;

    const userMessage: ChatMessage = {
      id: `msg_${Date.now()}`,
      role: 'user',
      content: text,
      timestamp: new Date()
    };
    
    setMessages(prev => [...prev, userMessage]);
    setIsProcessing(true);
    setError(null);

    try {
      if (wsRef.current?.isConnected()) {
        // WebSocket will send activities from backend
        wsRef.current.sendMessage(text);
      } else {
        // REST fallback - add activity locally
        setActivities(prev => [...prev, {
          id: `act_${Date.now()}`,
          type: 'delegation',
          source: 'user',
          target: 'coordinator',
          timestamp: new Date()
        }]);
        const response = await agentsApi.sendMessage(sessionId, text);
        setMessages(prev => [...prev, {
          id: `msg_${Date.now()}`,
          role: 'assistant',
          content: response.content,
          timestamp: new Date(),
          agentRole: response.agent_role
        }]);
        await fetchArtifacts();
        setIsProcessing(false);
      }
    } catch (err) {
      console.error('Failed to send message:', err);
      setError('Failed to send message. Please try again.');
      setIsProcessing(false);
    }
  }, [sessionId, fetchArtifacts]);

  // Speech recognition
  const startListening = useCallback(() => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) return;

    recognitionRef.current = new SpeechRecognition();
    recognitionRef.current.continuous = true;
    recognitionRef.current.interimResults = true;
    recognitionRef.current.lang = 'en-US';

    recognitionRef.current.onstart = () => {
      setIsListening(true);
      isListeningRef.current = true;
      setupAudioMonitoring();
    };

    recognitionRef.current.onresult = (event: any) => {
      let interimTranscript = '';
      let finalTranscript = '';

      for (let i = event.resultIndex; i < event.results.length; i++) {
        const transcriptText = event.results[i][0].transcript;
        if (event.results[i].isFinal) {
          finalTranscript += transcriptText;
        } else {
          interimTranscript += transcriptText;
        }
      }

      setCurrentTranscript(interimTranscript);

      if (finalTranscript) {
        setCurrentTranscript('');
        processSpeechTranscript(finalTranscript);
      }
    };

    recognitionRef.current.onerror = (event: any) => {
      console.error('Speech recognition error:', event.error);
      if (event.error !== 'no-speech') {
        setError(`Speech recognition error: ${event.error}`);
      }
    };

    recognitionRef.current.onend = () => {
      // Use ref to avoid stale closure - isListeningRef stays current
      if (isListeningRef.current && recognitionRef.current) {
        recognitionRef.current.start();
      }
    };

    recognitionRef.current.start();
  }, [setupAudioMonitoring, processSpeechTranscript]);

  const stopListening = useCallback(() => {
    setIsListening(false);
    isListeningRef.current = false;
    if (recognitionRef.current) {
      recognitionRef.current.stop();
      recognitionRef.current = null;
    }
    cleanupAudioMonitoring();
  }, [cleanupAudioMonitoring]);

  const toggleListening = () => {
    if (isListening) {
      stopListening();
    } else {
      startListening();
    }
  };

  // Send message via REST (fallback if WS not connected)
  const sendMessageRest = async (message: string): Promise<SendMessageResponse> => {
    if (!sessionId) throw new Error('No session');
    return await agentsApi.sendMessage(sessionId, message);
  };

  // Handle send message
  const handleSendMessage = async () => {
    if (!textInput.trim() || isProcessing || !sessionId) return;

    const userMessage: ChatMessage = {
      id: `msg_${Date.now()}`,
      role: 'user',
      content: textInput,
      timestamp: new Date()
    };
    
    setMessages(prev => [...prev, userMessage]);
    const inputText = textInput;
    setTextInput('');
    setIsProcessing(true);
    setError(null);

    try {
      // Try WebSocket first, fallback to REST
      if (wsRef.current?.isConnected()) {
        // WebSocket will send activities from backend
        wsRef.current.sendMessage(inputText);
      } else {
        // REST fallback - add activity locally
        setActivities(prev => [...prev, {
          id: `act_${Date.now()}`,
          type: 'delegation',
          source: 'user',
          target: 'coordinator',
          timestamp: new Date()
        }]);
        const response = await sendMessageRest(inputText);
        
        setMessages(prev => [...prev, {
          id: `msg_${Date.now()}`,
          role: 'assistant',
          content: response.content,
          timestamp: new Date(),
          agentRole: response.agent_role
        }]);

        // Parse artifacts from response for activities
        if (response.artifacts) {
          parseArtifactsForActivities(response.artifacts);
        }

        await fetchArtifacts();
        setIsProcessing(false);
      }
    } catch (err) {
      console.error('Failed to send message:', err);
      setError('Failed to send message. Please try again.');
      setIsProcessing(false);
    }
  };

  // Parse artifacts to extract agent activities
  const parseArtifactsForActivities = (artifacts: Record<string, any>) => {
    const newActivities: AgentActivity[] = [];
    
    // Check for delegations
    if (artifacts.delegations) {
      for (const delegation of artifacts.delegations) {
        newActivities.push({
          id: `act_${Date.now()}_${Math.random()}`,
          type: 'delegation',
          source: 'coordinator',
          target: delegation.agent || delegation.target,
          details: delegation.task,
          timestamp: new Date()
        });
      }
    }

    // Check for peer consultations
    if (artifacts.peer_consultations) {
      for (const consultation of artifacts.peer_consultations) {
        newActivities.push({
          id: `act_${Date.now()}_${Math.random()}`,
          type: 'peer_consultation',
          source: consultation.from,
          target: consultation.to,
          details: consultation.question,
          timestamp: new Date()
        });
      }
    }

    // Check for tool calls
    if (artifacts.tool_calls) {
      for (const tool of artifacts.tool_calls) {
        newActivities.push({
          id: `act_${Date.now()}_${Math.random()}`,
          type: tool.is_mcp ? 'mcp_tool' : 'tool_call',
          source: tool.agent,
          tool: tool.name,
          details: tool.result,
          timestamp: new Date()
        });
      }
    }

    // Check for synthesis
    if (artifacts.synthesis) {
      newActivities.push({
        id: `act_${Date.now()}_${Math.random()}`,
        type: 'synthesis',
        source: 'coordinator',
        details: 'Synthesizing agent results',
        timestamp: new Date()
      });
    }

    if (newActivities.length > 0) {
      setActivities(prev => [...prev, ...newActivities]);
    }

    // Update design progress from artifacts
    if (artifacts.design_progress) {
      setDesignProgress(artifacts.design_progress);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const getNodeTypeColor = (type: string): string => {
    const colors: Record<string, string> = {
      'Process': 'bg-orange-500',
      'Activity': 'bg-pink-500',
      'Metric': 'bg-blue-500',
      'Entity': 'bg-green-500',
    };
    return colors[type] || 'bg-gray-500';
  };

  return (
    <div className="h-[calc(100vh-120px)] flex flex-col animate-fade-in">
      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <div>
          <h1 className="text-3xl font-bold theme-text-title tracking-wide">AI Interview</h1>
          <p className="theme-text-muted mt-1">
            Multi-agent design system for business value chain modeling
          </p>
        </div>
        <div className="flex items-center gap-2">
          <div className={cn(
            "flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs",
            isConnected 
              ? "bg-green-500/20 text-green-400" 
              : "bg-amber-500/20 text-amber-400"
          )}>
            <Circle className={cn("w-2 h-2", isConnected && "animate-pulse")} />
            {isConnected ? 'Connected' : 'Connecting...'}
          </div>
          <Button variant="outline" size="sm" onClick={createSession} disabled={isProcessing}>
            <RefreshCw className={cn("w-4 h-4 mr-2", isProcessing && "animate-spin")} />
            New Session
          </Button>
        </div>
      </div>

      {/* Alerts */}
      {successMessage && (
        <div className="mb-4 p-4 rounded-xl bg-green-500/10 border border-green-500/30 text-green-400 flex items-center justify-between">
          <span>{successMessage}</span>
          <button onClick={() => setSuccessMessage(null)}><X className="w-4 h-4" /></button>
        </div>
      )}

      {error && (
        <div className="mb-4 p-4 rounded-xl bg-red-500/10 border border-red-500/30 text-red-400 flex items-center justify-between">
          <AlertCircle className="w-5 h-5 mr-2" />
          <span className="flex-1">{error}</span>
          <button onClick={() => setError(null)}><X className="w-4 h-4" /></button>
        </div>
      )}

      {/* Main Content */}
      <div className="flex gap-4 flex-1 min-h-0">
        {/* Left Panel - Conversation */}
        <Card className="flex-1 flex flex-col overflow-hidden">
          <CardHeader className="py-3 border-b theme-border">
            <div className="flex items-center justify-between">
              <CardTitle className="text-base flex items-center gap-2">
                <MessageSquare className="w-5 h-5 text-alpha-500" />
                Conversation
              </CardTitle>
              <span className="text-xs theme-text-muted">
                {sessionId ? `Session: ${sessionId.substring(0, 8)}...` : 'No session'}
              </span>
            </div>
          </CardHeader>

          {/* Chat Messages */}
          <div className="flex-1 overflow-y-auto p-4 space-y-3">
            {messages.length === 0 && !isProcessing ? (
              <div className="text-center py-16">
                <Bot className="w-16 h-16 mx-auto theme-text-muted opacity-30 mb-4" />
                <h3 className="text-lg font-semibold theme-text-title mb-2">Ready to Design</h3>
                <p className="theme-text-muted text-sm max-w-md mx-auto">
                  Start a conversation to design your business value chain model.
                  Our multi-agent system will analyze and collaborate to create a comprehensive design.
                </p>
              </div>
            ) : (
              <>
                {messages.map((msg) => (
                  <div 
                    key={msg.id} 
                    className={cn(
                      "flex gap-3",
                      msg.role === 'user' ? "justify-end" : "justify-start"
                    )}
                  >
                    {msg.role !== 'user' && (
                      <div className="w-8 h-8 rounded-full bg-alpha-500/20 flex items-center justify-center flex-shrink-0">
                        <Bot className="w-5 h-5 text-alpha-500" />
                      </div>
                    )}
                    <div className={cn(
                      "max-w-[80%] rounded-xl px-4 py-3",
                      msg.role === 'user' 
                        ? "bg-alpha-500 text-white" 
                        : "theme-card-bg border theme-border"
                    )}>
                      {msg.agentRole && msg.role !== 'user' && (
                        <div className="text-xs theme-text-muted mb-1 capitalize">
                          {msg.agentRole}
                        </div>
                      )}
                      <div className={cn(
                        "text-sm whitespace-pre-wrap",
                        msg.role === 'user' ? "text-white" : "theme-text"
                      )}>
                        {msg.content}
                      </div>
                      <div className={cn(
                        "text-xs mt-1",
                        msg.role === 'user' ? "text-white/70" : "theme-text-muted"
                      )}>
                        {msg.timestamp.toLocaleTimeString('en-US', { 
                          hour: '2-digit', 
                          minute: '2-digit' 
                        })}
                      </div>
                    </div>
                    {msg.role === 'user' && (
                      <div className="w-8 h-8 rounded-full bg-gray-500/20 flex items-center justify-center flex-shrink-0">
                        <User className="w-5 h-5 theme-text-muted" />
                      </div>
                    )}
                  </div>
                ))}
                
                {/* Streaming message */}
                {streamingContent && (
                  <div className="flex gap-3 justify-start">
                    <div className="w-8 h-8 rounded-full bg-alpha-500/20 flex items-center justify-center flex-shrink-0">
                      <Bot className="w-5 h-5 text-alpha-500" />
                    </div>
                    <div className="max-w-[80%] rounded-xl px-4 py-3 theme-card-bg border theme-border">
                      <div className="text-sm whitespace-pre-wrap theme-text">
                        {streamingContent}
                        <span className="inline-block w-2 h-4 bg-alpha-500 animate-pulse ml-1" />
                      </div>
                    </div>
                  </div>
                )}

                {/* Processing indicator */}
                {isProcessing && !streamingContent && (
                  <div className="flex gap-3 justify-start">
                    <div className="w-8 h-8 rounded-full bg-alpha-500/20 flex items-center justify-center flex-shrink-0">
                      <Bot className="w-5 h-5 text-alpha-500" />
                    </div>
                    <div className="rounded-xl px-4 py-3 theme-card-bg border theme-border">
                      <div className="flex items-center gap-2 text-sm theme-text-muted">
                        <Loader2 className="w-4 h-4 animate-spin" />
                        Agents are processing...
                      </div>
                    </div>
                  </div>
                )}
                
                <div ref={chatEndRef} />
              </>
            )}
          </div>

          {/* Speech Recognition & Input */}
          <div className="p-4 border-t theme-border">
            {/* Current transcript display */}
            {currentTranscript && (
              <div className="mb-2 p-2 rounded-lg theme-card-bg border border-dashed theme-border">
                <div className="flex items-center gap-2">
                  <AudioWaveform className="w-4 h-4 text-red-400 animate-pulse" />
                  <span className="text-sm theme-text-muted italic">{currentTranscript}</span>
                </div>
              </div>
            )}
            
            {/* Audio level indicator */}
            {isListening && (
              <div className="mb-2">
                <div className="h-1.5 rounded-full bg-alpha-faded-200 dark:bg-alpha-faded-800 overflow-hidden">
                  <div 
                    className={cn(
                      "h-full transition-all duration-100",
                      audioLevel > 0.5 ? "bg-green-500" : "bg-red-500"
                    )}
                    style={{ width: `${audioLevel * 100}%` }}
                  />
                </div>
              </div>
            )}
            
            <div className="flex gap-2">
              {/* Microphone button */}
              <button
                onClick={toggleListening}
                disabled={!speechSupported || !sessionId}
                className={cn(
                  "w-11 h-11 rounded-xl flex items-center justify-center transition-all flex-shrink-0",
                  isListening 
                    ? "bg-red-500 hover:bg-red-600 animate-pulse" 
                    : "bg-alpha-500 hover:bg-alpha-600",
                  "text-white disabled:opacity-50 disabled:cursor-not-allowed"
                )}
                title={isListening ? "Stop listening" : "Start speaking"}
              >
                {isListening ? <Square className="w-5 h-5" /> : <Mic className="w-5 h-5" />}
              </button>
              
              <input
                type="text"
                placeholder="Type or speak to describe your business..."
                value={textInput}
                onChange={(e) => setTextInput(e.target.value)}
                onKeyPress={handleKeyPress}
                disabled={isProcessing || !sessionId}
                className="flex-1 px-4 py-2.5 rounded-xl theme-card-bg border theme-border
                  theme-text placeholder:theme-text-muted text-sm
                  focus:outline-none focus:ring-2 focus:ring-alpha-500"
              />
              <Button
                onClick={handleSendMessage}
                disabled={!textInput.trim() || isProcessing || !sessionId}
              >
                {isProcessing ? (
                  <Loader2 className="w-4 h-4 animate-spin" />
                ) : (
                  <Send className="w-4 h-4" />
                )}
              </Button>
            </div>
          </div>
        </Card>

        {/* Right Panel - Agent Activity & Artifacts */}
        <Card className="flex-1 flex flex-col overflow-hidden">
          {/* Design Progress */}
          <div className="p-4 border-b theme-border">
            <ProgressBar progress={designProgress} />
          </div>

          {/* Tabs */}
          <div className="flex border-b theme-border">
            <TabButton active={activeTab === 0} onClick={() => setActiveTab(0)} badge={activities.length}>
              <Brain className="w-4 h-4 mr-1.5 inline" />
              Agents
            </TabButton>
            <TabButton active={activeTab === 1} onClick={() => setActiveTab(1)}>
              <Activity className="w-4 h-4 mr-1.5 inline" />
              KPIs
            </TabButton>
            <TabButton active={activeTab === 2} onClick={() => setActiveTab(2)}>
              <GitBranch className="w-4 h-4 mr-1.5 inline" />
              Entities
            </TabButton>
            <TabButton active={activeTab === 3} onClick={() => setActiveTab(3)}>
              <Network className="w-4 h-4 mr-1.5 inline" />
              Model
            </TabButton>
          </div>

          {/* Tab Content */}
          <div className="flex-1 overflow-y-auto p-4">
            {/* Agents Tab */}
            {activeTab === 0 && (
              <div>
                {activities.length === 0 ? (
                  <div className="text-center py-12">
                    <Activity className="w-12 h-12 mx-auto theme-text-muted opacity-50 mb-4" />
                    <p className="theme-text-muted text-sm">
                      Agent activity will appear here as they collaborate on your design
                    </p>
                  </div>
                ) : (
                  <div className="space-y-1">
                    {activities.map((activity) => (
                      <AgentActivityItem key={activity.id} activity={activity} />
                    ))}
                    <div ref={activityEndRef} />
                  </div>
                )}
              </div>
            )}

            {/* KPIs Tab */}
            {activeTab === 1 && (
              <div>
                {kpis.length === 0 ? (
                  <div className="text-center py-12">
                    <Brain className="w-12 h-12 mx-auto theme-text-muted opacity-50 mb-4" />
                    <p className="theme-text-muted text-sm">
                      KPIs and metrics will appear here as they are identified
                    </p>
                  </div>
                ) : (
                  <div className="space-y-2">
                    {kpis.map((kpi, idx) => (
                      <div key={idx} className="p-3 rounded-xl theme-card-bg border theme-border">
                        <div className="flex items-center gap-2">
                          <Brain className="w-4 h-4 text-purple-400" />
                          <span className="text-sm theme-text">{kpi}</span>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            )}

            {/* Entities Tab */}
            {activeTab === 2 && (
              <div>
                {entities.length === 0 ? (
                  <div className="text-center py-12">
                    <GitBranch className="w-12 h-12 mx-auto theme-text-muted opacity-50 mb-4" />
                    <p className="theme-text-muted text-sm">
                      Business entities will appear here as they are discovered
                    </p>
                  </div>
                ) : (
                  <div className="space-y-2">
                    {entities.map((entity, idx) => (
                      <div key={idx} className="p-3 rounded-xl theme-card-bg border theme-border">
                        <div className="flex items-center gap-2">
                          <GitBranch className="w-4 h-4 theme-info-icon" />
                          <span className="text-sm theme-text">{entity}</span>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            )}

            {/* Model Tab */}
            {activeTab === 3 && (
              <div>
                {valueChainNodes.length === 0 ? (
                  <div className="text-center py-12">
                    <Network className="w-12 h-12 mx-auto theme-text-muted opacity-50 mb-4" />
                    <p className="theme-text-muted text-sm">
                      The value chain model will appear here once agents complete the design
                    </p>
                  </div>
                ) : (
                  <div className="space-y-4">
                    <div>
                      <h4 className="text-sm font-medium theme-text-title mb-2">
                        Nodes ({valueChainNodes.length})
                      </h4>
                      <div className="space-y-1">
                        {valueChainNodes.map((node) => (
                          <div key={node.id} className="p-2 rounded-lg theme-card-bg border theme-border">
                            <div className="flex items-center gap-2">
                              <div className={cn("w-3 h-3 rounded-full", getNodeTypeColor(node.type))} />
                              <span className="font-medium theme-text text-sm">{node.name}</span>
                              <span className="px-2 py-0.5 rounded-full text-xs border theme-border theme-text-muted">
                                {node.type}
                              </span>
                            </div>
                            {node.description && (
                              <p className="text-xs theme-text-muted mt-1 ml-5">{node.description}</p>
                            )}
                          </div>
                        ))}
                      </div>
                    </div>

                    {valueChainLinks.length > 0 && (
                      <div>
                        <h4 className="text-sm font-medium theme-text-title mb-2">
                          Relationships ({valueChainLinks.length})
                        </h4>
                        <div className="space-y-1">
                          {valueChainLinks.map((link, idx) => {
                            const sourceNode = valueChainNodes.find(n => n.id === link.source_id);
                            const targetNode = valueChainNodes.find(n => n.id === link.target_id);
                            return (
                              <div key={idx} className="p-2 rounded-lg theme-card-bg border theme-border">
                                <div className="flex items-center gap-2 flex-wrap text-sm">
                                  <Link2 className="w-4 h-4 theme-text-muted" />
                                  <span className="theme-text">{sourceNode?.name || link.source_id}</span>
                                  <ChevronRight className="w-4 h-4 theme-text-muted" />
                                  <span className="px-2 py-0.5 rounded-full text-xs bg-alpha-500/20 text-alpha-400 border border-alpha-500/30">
                                    {link.type}
                                  </span>
                                  <ChevronRight className="w-4 h-4 theme-text-muted" />
                                  <span className="theme-text">{targetNode?.name || link.target_id}</span>
                                </div>
                              </div>
                            );
                          })}
                        </div>
                      </div>
                    )}
                  </div>
                )}
              </div>
            )}
          </div>
        </Card>
      </div>
    </div>
  );
}
