import { useState, useEffect, useRef, useCallback } from 'react';
import { 
  MessageSquare, Send, User, Bot, ChevronRight, ChevronLeft, Sparkles, 
  Building2, Target, BarChart3, Mic, Square, AlertCircle, Loader2,
  AudioWaveform
} from 'lucide-react';
import { cn } from '../../lib/utils';
import { agentsApi, AgentWebSocket, WSMessage, DesignProgress } from '../../api/agentsApi';
import { getIndustryByName, getAllKPIsForIndustry, getAllEntitiesForIndustry } from '../../data/industryValueChains';

declare global {
  interface Window {
    SpeechRecognition: any;
    webkitSpeechRecognition: any;
  }
}

interface Message {
  id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  timestamp: Date;
  agentRole?: string;
}

interface InterviewPhase {
  id: string;
  name: string;
  icon: React.ReactNode;
  description: string;
  completed: boolean;
}

interface DesignArtifact {
  type: 'kpi' | 'entity' | 'dashboard' | 'value_chain';
  name: string;
  details: any;
}

const phases: InterviewPhase[] = [
  {
    id: 'strategy',
    name: 'Business Strategy',
    icon: <Building2 className="w-5 h-5" />,
    description: 'Define your business model and strategic objectives',
    completed: false,
  },
  {
    id: 'kpis',
    name: 'KPI Selection',
    icon: <Target className="w-5 h-5" />,
    description: 'Identify key performance indicators for your value chain',
    completed: false,
  },
  {
    id: 'analytics',
    name: 'Analytics Design',
    icon: <BarChart3 className="w-5 h-5" />,
    description: 'Design dashboards and reports for your metrics',
    completed: false,
  },
];

export default function DemoInterviewPage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);
  const [currentPhase, setCurrentPhase] = useState(phases[0]);
  const [error, setError] = useState<string | null>(null);
  
  // Session state
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const [_sessionId, setSessionId] = useState<string | null>(null);
  const [isConnecting, setIsConnecting] = useState(true);
  
  // Speech recognition state
  const [isListening, setIsListening] = useState(false);
  const [currentTranscript, setCurrentTranscript] = useState('');
  const [audioLevel, setAudioLevel] = useState(0);
  const [speechSupported, setSpeechSupported] = useState(true);
  
  // Design artifacts collected during interview
  const [designArtifacts, setDesignArtifacts] = useState<DesignArtifact[]>([]);
  
  // Refs
  const chatEndRef = useRef<HTMLDivElement>(null);
  const wsRef = useRef<any>(null);
  const recognitionRef = useRef<any>(null);
  const isListeningRef = useRef(false);
  const audioContextRef = useRef<AudioContext | null>(null);
  const analyserRef = useRef<AnalyserNode | null>(null);
  const animationFrameRef = useRef<number | null>(null);

  // Check speech recognition support
  useEffect(() => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      setSpeechSupported(false);
    }
  }, []);

  // Initialize session on mount
  useEffect(() => {
    initSession();
    return () => {
      if (wsRef.current) {
        wsRef.current.disconnect();
      }
      cleanupAudioMonitoring();
    };
  }, []);

  // Auto-scroll to bottom
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // Save design artifacts to localStorage for analytics page
  useEffect(() => {
    if (designArtifacts.length > 0) {
      const design = {
        kpis: designArtifacts.filter(a => a.type === 'kpi'),
        entities: designArtifacts.filter(a => a.type === 'entity'),
        dashboards: designArtifacts.filter(a => a.type === 'dashboard'),
        industry: detectIndustryFromArtifacts(designArtifacts),
        updatedAt: new Date().toISOString()
      };
      localStorage.setItem('demo_interview_design', JSON.stringify(design));
    }
  }, [designArtifacts]);

  const detectIndustryFromArtifacts = (artifacts: DesignArtifact[]): string => {
    const allText = artifacts.map(a => `${a.name} ${JSON.stringify(a.details)}`).join(' ').toLowerCase();
    if (allText.includes('retail') || allText.includes('ecommerce')) return 'Retail';
    if (allText.includes('manufacturing') || allText.includes('production')) return 'Manufacturing';
    if (allText.includes('healthcare') || allText.includes('patient')) return 'Healthcare';
    if (allText.includes('financial') || allText.includes('banking')) return 'Financial Services';
    if (allText.includes('saas') || allText.includes('software')) return 'Technology';
    return 'General Business';
  };

  const initSession = async () => {
    setIsConnecting(true);
    setError(null);
    
    try {
      // Create session via agentsApi
      const response = await agentsApi.createSession({
        user_id: 'demo_user',
        industry: 'general',
        business_description: 'Demo interview session'
      });
      
      setSessionId(response.session_id);
      
      // Connect WebSocket for real-time updates
      const ws = new AgentWebSocket(response.session_id, {
        onMessage: handleAgentMessage,
        onActivity: (activity) => console.log('Agent activity:', activity),
        onProgress: handleDesignProgress,
        onError: (err) => setError(err),
        onConnect: () => console.log('WebSocket connected'),
        onDisconnect: () => console.log('WebSocket disconnected'),
      });
      ws.connect();
      wsRef.current = ws;
      
      // Add welcome message
      setMessages([{
        id: '1',
        role: 'assistant',
        content: "Welcome to the Northstar AI Interview! I'm your Strategy Coordinator, and I'll guide you through designing your business analytics.\n\nLet's start with understanding your business. What industry is your organization in, and what are your primary business activities?",
        timestamp: new Date(),
        agentRole: 'Strategy Coordinator'
      }]);
      
      setIsConnecting(false);
    } catch (err) {
      console.error('Failed to create agent session:', err);
      // Fallback to demo mode
      const demoSessionId = `demo_${Date.now()}`;
      setSessionId(demoSessionId);
      
      setMessages([{
        id: '1',
        role: 'assistant',
        content: "Welcome to the Northstar AI Interview! I'm your Strategy Coordinator, and I'll guide you through designing your business analytics.\n\nLet's start with understanding your business. What industry is your organization in, and what are your primary business activities?",
        timestamp: new Date(),
        agentRole: 'Strategy Coordinator'
      }]);
      
      setIsConnecting(false);
      setError('Running in demo mode - agent service unavailable.');
    }
  };
  
  // Handle messages from real agent WebSocket
  const handleAgentMessage = (message: WSMessage) => {
    if (message.type === 'complete' || message.type === 'chunk') {
      const content = message.content || message.message || '';
      if (content) {
        setMessages(prev => [...prev, {
          id: `msg_${Date.now()}`,
          role: 'assistant',
          content,
          timestamp: new Date(),
          agentRole: 'Strategy Coordinator'
        }]);
      }
      if (message.type === 'complete') {
        setIsProcessing(false);
        // Extract artifacts from response if available
        if (message.results) {
          extractArtifactsFromAgentResponse(message.results);
        }
      }
    } else if (message.type === 'processing' || message.type === 'analyzing') {
      setIsProcessing(true);
    } else if (message.type === 'finalized') {
      setIsProcessing(false);
    }
  };
  
  // Handle design progress updates
  const handleDesignProgress = (progress: DesignProgress) => {
    // Convert progress to artifacts for analytics page
    if (progress.kpis?.findings) {
      progress.kpis.findings.forEach(kpi => {
        setDesignArtifacts(prev => {
          if (prev.some(a => a.name === kpi)) return prev;
          return [...prev, { type: 'kpi', name: kpi, details: { category: 'General' } }];
        });
      });
    }
    if (progress.entities?.findings) {
      progress.entities.findings.forEach(entity => {
        setDesignArtifacts(prev => {
          if (prev.some(a => a.name === entity)) return prev;
          return [...prev, { type: 'entity', name: entity, details: {} }];
        });
      });
    }
  };
  
  // Extract artifacts from agent response
  const extractArtifactsFromAgentResponse = (results: Record<string, any>) => {
    if (results.identified_kpis) {
      results.identified_kpis.forEach((kpi: string) => {
        setDesignArtifacts(prev => {
          if (prev.some(a => a.name === kpi)) return prev;
          return [...prev, { type: 'kpi', name: kpi, details: { category: 'General' } }];
        });
      });
    }
    if (results.identified_entities) {
      results.identified_entities.forEach((entity: string) => {
        setDesignArtifacts(prev => {
          if (prev.some(a => a.name === entity)) return prev;
          return [...prev, { type: 'entity', name: entity, details: {} }];
        });
      });
    }
  };

  // Extract design artifacts from demo response for analytics page
  const extractArtifactsFromResponse = (userInput: string, _response: string) => {
    const lower = userInput.toLowerCase();
    
    // Try to match industry from reference data
    const industry = getIndustryByName(userInput);
    
    if (industry) {
      // Use comprehensive industry value chain data
      const kpis = getAllKPIsForIndustry(industry);
      const entities = getAllEntitiesForIndustry(industry);
      
      // Add KPIs (limit to first 8 for demo)
      const kpiArtifacts = kpis.slice(0, 8).map(kpi => ({
        type: 'kpi' as const,
        name: kpi.name,
        details: { code: kpi.code, category: kpi.category, unit: kpi.unit, icon: kpi.icon }
      }));
      
      // Add entities
      const entityArtifacts = entities.slice(0, 6).map(entity => ({
        type: 'entity' as const,
        name: entity.name,
        details: { code: entity.code, description: entity.description, recordsPerMinute: entity.recordsPerMinute }
      }));
      
      setDesignArtifacts(prev => [...prev, ...kpiArtifacts, ...entityArtifacts]);
    } else if (lower.includes('challenge') || lower.includes('problem') || lower.includes('dashboard')) {
      setDesignArtifacts(prev => [...prev,
        { type: 'dashboard', name: 'Executive Dashboard', details: { layout: 'grid', columns: 4 } },
      ]);
    }
  };

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
        handleSendMessage(finalTranscript);
      }
    };

    recognitionRef.current.onerror = (event: any) => {
      console.error('Speech recognition error:', event.error);
      if (event.error !== 'no-speech') {
        setError(`Speech recognition error: ${event.error}`);
      }
    };

    recognitionRef.current.onend = () => {
      if (isListeningRef.current && recognitionRef.current) {
        recognitionRef.current.start();
      }
    };

    recognitionRef.current.start();
  }, [setupAudioMonitoring]);

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

  // Handle send message
  const handleSendMessage = async (text?: string) => {
    const messageText = text || input;
    if (!messageText.trim() || isProcessing) return;

    const userMessage: Message = {
      id: `msg_${Date.now()}`,
      role: 'user',
      content: messageText,
      timestamp: new Date()
    };
    
    setMessages(prev => [...prev, userMessage]);
    if (!text) setInput('');
    setIsProcessing(true);
    setError(null);

    // Try WebSocket first, then REST API, then demo mode
    if (wsRef.current && wsRef.current.isConnected()) {
      wsRef.current.sendMessage(messageText);
    } else if (_sessionId && !_sessionId.startsWith('demo_')) {
      // Use REST API fallback
      try {
        const response = await agentsApi.sendMessage(_sessionId, messageText);
        setMessages(prev => [...prev, {
          id: `msg_${Date.now()}`,
          role: 'assistant',
          content: response.content,
          timestamp: new Date(),
          agentRole: response.agent_role || 'Strategy Coordinator'
        }]);
        if (response.artifacts) {
          extractArtifactsFromAgentResponse(response.artifacts);
        }
        setIsProcessing(false);
      } catch (err) {
        console.error('REST API failed, falling back to demo mode:', err);
        // Fall through to demo mode
        const response = generateDemoResponse(messageText);
        setMessages(prev => [...prev, {
          id: `msg_${Date.now()}`,
          role: 'assistant',
          content: response,
          timestamp: new Date(),
          agentRole: 'Strategy Coordinator'
        }]);
        extractArtifactsFromResponse(messageText, response);
        setIsProcessing(false);
      }
    } else {
      // Demo mode - simulate agent response
      setTimeout(() => {
        const response = generateDemoResponse(messageText);
        setMessages(prev => [...prev, {
          id: `msg_${Date.now()}`,
          role: 'assistant',
          content: response,
          timestamp: new Date(),
          agentRole: 'Strategy Coordinator'
        }]);
        
        // Extract design artifacts from demo response
        extractArtifactsFromResponse(messageText, response);
        setIsProcessing(false);
      }, 1500);
    }
  };

  // Demo mode response generator
  const generateDemoResponse = (userInput: string): string => {
    const lower = userInput.toLowerCase();
    if (lower.includes('retail') || lower.includes('ecommerce') || lower.includes('store')) {
      return "Excellent! Retail is a great fit for our analytics platform. Based on your industry, I recommend focusing on these value chains:\n\n• **Customer Acquisition** - Traffic, conversion, CAC\n• **Order Fulfillment** - Order accuracy, delivery time, returns\n• **Inventory Management** - Turnover, stockouts, carrying cost\n\nWhat are the top 3 business challenges you're trying to address with analytics?";
    } else if (lower.includes('manufacturing') || lower.includes('production')) {
      return "Manufacturing analytics is one of our strongest areas! I recommend focusing on:\n\n• **Production Efficiency** - OEE, cycle time, throughput\n• **Quality Control** - Defect rate, first-pass yield, scrap\n• **Supply Chain** - Supplier lead time, inventory turns, on-time delivery\n\nWhat specific pain points are you looking to address?";
    } else if (lower.includes('challenge') || lower.includes('problem') || lower.includes('pain')) {
      return "Thank you for sharing those challenges. Let me delegate to our specialists to design the right KPIs for you.\n\n*Consulting with Business Analyst and Data Scientist...*\n\nBased on your needs, I recommend these KPIs:\n\n1. **Revenue per Customer** - Track customer value over time\n2. **Operational Efficiency Ratio** - Measure process effectiveness\n3. **Customer Satisfaction Score** - Monitor experience quality\n\nShall I design a dashboard layout for these metrics?";
    } else {
      return "Thank you for that information! I'm analyzing your requirements with our specialist agents.\n\nCould you tell me more about your key business objectives? What does success look like for your organization in the next 12 months?";
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  // Loading state
  if (isConnecting) {
    return (
      <div className="flex items-center justify-center h-96">
        <div className="text-center">
          <Loader2 className="w-12 h-12 animate-spin text-alpha-400 mx-auto mb-4" />
          <p className="theme-text-secondary">Connecting to agent service...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title">AI Interview</h1>
          <p className="mt-2 theme-text-secondary">
            Design your business strategy and analytics through conversation
          </p>
        </div>
        <div className="flex items-center gap-4">
          {error && (
            <div className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-amber-500/20 text-amber-400 text-sm">
              <AlertCircle className="w-4 h-4" />
              Demo Mode
            </div>
          )}
          <div className="flex items-center gap-2 px-4 py-2 rounded-lg bg-alpha-500/10 text-alpha-400">
            <MessageSquare className="w-5 h-5" />
            <span className="font-medium">Step 3 of 6</span>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="grid grid-cols-4 gap-6 h-[calc(100vh-280px)]">
        {/* Interview Phases */}
        <div className="theme-card rounded-2xl p-6">
          <h3 className="font-semibold theme-text-title mb-4">Interview Phases</h3>
          <div className="space-y-3">
            {phases.map((phase, index) => (
              <button
                key={phase.id}
                onClick={() => setCurrentPhase(phase)}
                className={`w-full p-4 rounded-xl text-left transition-all duration-200 ${
                  currentPhase.id === phase.id
                    ? 'bg-alpha-500/20 border border-alpha-500/50'
                    : phase.completed
                    ? 'bg-emerald-500/10 border border-emerald-500/30'
                    : 'hover:bg-[var(--card-hover)]'
                }`}
              >
                <div className="flex items-center gap-3 mb-2">
                  <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${
                    currentPhase.id === phase.id
                      ? 'bg-alpha-500/20 text-alpha-400'
                      : phase.completed
                      ? 'bg-emerald-500/20 text-emerald-400'
                      : 'bg-slate-700 text-slate-400'
                  }`}>
                    {phase.icon}
                  </div>
                  <div>
                    <p className={`font-medium ${
                      currentPhase.id === phase.id ? 'text-alpha-400' : 'theme-text-title'
                    }`}>
                      {phase.name}
                    </p>
                    <p className="text-xs theme-text-muted">Phase {index + 1}</p>
                  </div>
                </div>
                <p className="text-sm theme-text-secondary">{phase.description}</p>
              </button>
            ))}
          </div>

          {/* Agent Info */}
          <div className="mt-6 p-4 rounded-xl bg-gradient-to-br from-alpha-500/10 to-purple-500/10 border border-alpha-500/20">
            <div className="flex items-center gap-3 mb-2">
              <Sparkles className="w-5 h-5 text-alpha-400" />
              <span className="font-medium theme-text-title">Active Agents</span>
            </div>
            <p className="text-sm theme-text-secondary">
              Strategy Coordinator, Business Analyst, and KPI Specialist are assisting you.
            </p>
          </div>

          {/* Design Artifacts Collected */}
          {designArtifacts.length > 0 && (
            <div className="mt-4 p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/20">
              <div className="flex items-center gap-2 mb-2">
                <Target className="w-4 h-4 text-emerald-400" />
                <span className="text-sm font-medium text-emerald-400">
                  {designArtifacts.length} Design Artifacts
                </span>
              </div>
              <p className="text-xs theme-text-muted">
                KPIs, entities, and dashboards captured
              </p>
            </div>
          )}
        </div>

        {/* Chat Interface */}
        <div className="col-span-3 theme-card rounded-2xl flex flex-col">
          {/* Messages */}
          <div className="flex-1 overflow-y-auto p-6 space-y-4">
            {messages.map((message) => (
              <div
                key={message.id}
                className={`flex gap-3 ${message.role === 'user' ? 'flex-row-reverse' : ''}`}
              >
                <div className={`w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0 ${
                  message.role === 'user'
                    ? 'bg-alpha-500/20 text-alpha-400'
                    : 'bg-gradient-to-br from-purple-500 to-alpha-500 text-white'
                }`}>
                  {message.role === 'user' ? (
                    <User className="w-5 h-5" />
                  ) : (
                    <Bot className="w-5 h-5" />
                  )}
                </div>
                <div className={`max-w-[70%] p-4 rounded-2xl ${
                  message.role === 'user'
                    ? 'bg-alpha-500/20 text-alpha-100'
                    : 'theme-bg-secondary'
                }`}>
                  {message.agentRole && message.role === 'assistant' && (
                    <p className="text-xs text-alpha-400 mb-1 font-medium">{message.agentRole}</p>
                  )}
                  <p className="whitespace-pre-wrap">{message.content}</p>
                  <p className="text-xs theme-text-muted mt-2">
                    {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                  </p>
                </div>
              </div>
            ))}
            {isProcessing && (
              <div className="flex gap-3">
                <div className="w-10 h-10 rounded-full bg-gradient-to-br from-purple-500 to-alpha-500 flex items-center justify-center">
                  <Bot className="w-5 h-5 text-white" />
                </div>
                <div className="p-4 rounded-2xl theme-bg-secondary">
                  <div className="flex gap-1">
                    <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" />
                    <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }} />
                    <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }} />
                  </div>
                </div>
              </div>
            )}
            <div ref={chatEndRef} />
          </div>

          {/* Voice Transcript Display */}
          {currentTranscript && (
            <div className="px-6 py-2 border-t theme-border bg-alpha-500/5">
              <div className="flex items-center gap-2">
                <AudioWaveform className="w-4 h-4 text-alpha-400 animate-pulse" />
                <p className="text-sm theme-text-secondary italic">{currentTranscript}</p>
              </div>
            </div>
          )}

          {/* Input */}
          <div className="p-4 border-t theme-border">
            <div className="flex gap-3">
              {/* Voice Button */}
              <button
                onClick={toggleListening}
                disabled={!speechSupported}
                className={cn(
                  "w-12 h-12 rounded-xl flex items-center justify-center transition-all flex-shrink-0",
                  isListening 
                    ? "bg-red-500 hover:bg-red-600 text-white" 
                    : "bg-alpha-500/20 hover:bg-alpha-500/30 text-alpha-400",
                  !speechSupported && "opacity-50 cursor-not-allowed"
                )}
                title={isListening ? "Stop listening" : "Start speaking"}
                style={isListening ? { boxShadow: `0 0 ${20 + audioLevel * 30}px rgba(239, 68, 68, ${0.3 + audioLevel * 0.5})` } : {}}
              >
                {isListening ? <Square className="w-5 h-5" /> : <Mic className="w-5 h-5" />}
              </button>

              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={handleKeyPress}
                placeholder={isListening ? "Listening... speak now" : "Type your response or click mic to speak..."}
                className="flex-1 px-4 py-3 rounded-xl theme-input"
                disabled={isProcessing}
              />
              <button
                onClick={() => handleSendMessage()}
                disabled={!input.trim() || isProcessing}
                className="px-6 py-3 rounded-xl bg-alpha-500 hover:bg-alpha-600 disabled:opacity-50 disabled:cursor-not-allowed text-white font-medium transition-colors flex items-center gap-2"
              >
                <Send className="w-5 h-5" />
                Send
              </button>
            </div>
            {!speechSupported && (
              <p className="text-xs text-amber-400 mt-2">
                Voice input not supported in this browser. Please use Chrome or Edge.
              </p>
            )}
          </div>
        </div>
      </div>

      {/* Navigation */}
      <div className="flex justify-between">
        <a
          href="/demo/training"
          className="px-6 py-3 rounded-xl theme-card hover:bg-[var(--card-hover)] font-medium transition-colors flex items-center gap-2"
        >
          <ChevronLeft className="w-5 h-5" />
          Back to Training
        </a>
        <a
          href="/demo/simulator"
          className="px-6 py-3 rounded-xl bg-alpha-500 hover:bg-alpha-600 text-white font-medium transition-colors flex items-center gap-2"
        >
          Configure Simulator
          <ChevronRight className="w-5 h-5" />
        </a>
      </div>
    </div>
  );
}
