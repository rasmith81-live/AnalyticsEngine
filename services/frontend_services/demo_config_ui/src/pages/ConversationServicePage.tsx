import { useState, useEffect, useRef, useCallback } from 'react';
import {
  Mic,
  Brain,
  GitBranch,
  Link2,
  RefreshCw,
  Network,
  AudioWaveform,
  Volume2,
  Square,
  Circle,
  Trash2,
  Send,
  Save,
  FolderOpen,
  Search,
  X,
  ChevronRight,
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { cn } from '../lib/utils';
import { 
  conversationApi, 
  SaveFullConfigurationRequest,
  ClientConfigurationResponse
} from '../api/conversationApi';

interface BusinessIntent {
  name: string;
  confidence: number;
  parameters: Record<string, any>;
  description?: string;
  domain?: string;
  target_entities?: string[];
  requested_metrics?: string[];
}

interface TranscriptSegment {
  id: string;
  text: string;
  timestamp: Date;
  isFinal: boolean;
  intents?: BusinessIntent[];
}

interface SessionInfo {
  id: string;
  user_id: string;
  start_time: string;
  last_activity: string;
  status: string;
  intents_identified: BusinessIntent[];
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

interface ValueChainModel {
  id: string;
  name: string;
  nodes: ValueChainNode[];
  links: ValueChainLink[];
  created_at: string;
}

declare global {
  interface Window {
    SpeechRecognition: any;
    webkitSpeechRecognition: any;
  }
}

const API_BASE = 'http://127.0.0.1:8090/api/v1/conversation';

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

export default function ConversationServicePage() {
  const [isListening, setIsListening] = useState(false);
  const [transcript, setTranscript] = useState<TranscriptSegment[]>([]);
  const [currentTranscript, setCurrentTranscript] = useState('');
  const [audioLevel, setAudioLevel] = useState(0);
  const [speechSupported, setSpeechSupported] = useState(true);
  const [textInput, setTextInput] = useState('');
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [allIntents, setAllIntents] = useState<BusinessIntent[]>([]);
  const [generatedModel, setGeneratedModel] = useState<ValueChainModel | null>(null);
  const [isGeneratingModel, setIsGeneratingModel] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [isSaving, setIsSaving] = useState(false);
  const [saveSuccess, setSaveSuccess] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState(0);
  const [loadDialogOpen, setLoadDialogOpen] = useState(false);
  const [searchClientName, setSearchClientName] = useState('');
  const [searchDateFrom, setSearchDateFrom] = useState('');
  const [searchDateTo, setSearchDateTo] = useState('');
  const [searchResults, setSearchResults] = useState<ClientConfigurationResponse[]>([]);
  const [isSearching, setIsSearching] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const recognitionRef = useRef<any>(null);
  const transcriptEndRef = useRef<HTMLDivElement>(null);
  const audioContextRef = useRef<AudioContext | null>(null);
  const analyserRef = useRef<AnalyserNode | null>(null);
  const animationFrameRef = useRef<number | null>(null);
  const sessionIdRef = useRef<string | null>(null);

  const userId = 'demo_user';

  useEffect(() => {
    sessionIdRef.current = sessionId;
  }, [sessionId]);

  const scrollToBottom = () => {
    transcriptEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [transcript, currentTranscript]);

  useEffect(() => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      setSpeechSupported(false);
      setError('Speech recognition is not supported in this browser. Please use Chrome or Edge.');
    }
  }, []);

  const createSession = useCallback(async () => {
    try {
      const response = await fetch(`${API_BASE}/sessions?user_id=${userId}`, {
        method: 'POST',
      });
      if (!response.ok) throw new Error('Failed to create session');
      const session: SessionInfo = await response.json();
      setSessionId(session.id);
      setTranscript([]);
      setAllIntents([]);
      setGeneratedModel(null);
      setError(null);
    } catch (err) {
      setError('Failed to create session. Is the Conversation Service running?');
    }
  }, [userId]);

  useEffect(() => {
    createSession();
  }, [createSession]);

  const processTranscript = useCallback(async (text: string, segmentId: string) => {
    const currentSessionId = sessionIdRef.current;
    if (!text.trim() || !currentSessionId) return;

    setIsProcessing(true);
    try {
      const response = await fetch(`${API_BASE}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          session_id: currentSessionId,
          user_id: userId,
          message: text,
          skip_response: true,
        }),
      });

      if (!response.ok) throw new Error('Failed to process transcript');

      const data = await response.json();

      if (data.intents && data.intents.length > 0) {
        setTranscript(prev => prev.map(seg => 
          seg.id === segmentId ? { ...seg, intents: data.intents } : seg
        ));
        setAllIntents(prev => [...prev, ...data.intents]);
      }

      if (data.session_id) {
        setSessionId(data.session_id);
      }
    } catch (err) {
      console.error('Error processing transcript:', err);
    } finally {
      setIsProcessing(false);
    }
  }, [userId]);

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

  const startListening = useCallback(() => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) return;

    recognitionRef.current = new SpeechRecognition();
    recognitionRef.current.continuous = true;
    recognitionRef.current.interimResults = true;
    recognitionRef.current.lang = 'en-US';

    recognitionRef.current.onstart = () => {
      setIsListening(true);
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
        const segmentId = `seg_${Date.now()}`;
        const newSegment: TranscriptSegment = {
          id: segmentId,
          text: finalTranscript,
          timestamp: new Date(),
          isFinal: true,
        };
        setTranscript(prev => [...prev, newSegment]);
        setCurrentTranscript('');
        processTranscript(finalTranscript, segmentId);
      }
    };

    recognitionRef.current.onerror = (event: any) => {
      console.error('Speech recognition error:', event.error);
      if (event.error !== 'no-speech') {
        setError(`Speech recognition error: ${event.error}`);
      }
    };

    recognitionRef.current.onend = () => {
      if (isListening && recognitionRef.current) {
        recognitionRef.current.start();
      }
    };

    recognitionRef.current.start();
  }, [isListening, setupAudioMonitoring, processTranscript]);

  const stopListening = useCallback(() => {
    setIsListening(false);
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

  const clearTranscript = () => {
    setTranscript([]);
    setCurrentTranscript('');
    setAllIntents([]);
  };

  const submitTextInput = async () => {
    if (!textInput.trim() || isProcessing) return;
    
    const segmentId = `seg_${Date.now()}`;
    const newSegment: TranscriptSegment = {
      id: segmentId,
      text: textInput,
      timestamp: new Date(),
      isFinal: true,
    };
    setTranscript(prev => [...prev, newSegment]);
    const inputText = textInput;
    setTextInput('');
    await processTranscript(inputText, segmentId);
  };

  const handleTextKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      submitTextInput();
    }
  };

  const generateValueChainModel = async () => {
    if (!sessionId || transcript.length === 0) return;

    setIsGeneratingModel(true);
    setError(null);

    try {
      const response = await fetch(`${API_BASE}/sessions/${sessionId}/model`, {
        method: 'POST',
      });

      if (!response.ok) throw new Error('Failed to generate model');

      const model: ValueChainModel = await response.json();
      setGeneratedModel(model);
      setActiveTab(2);
    } catch (err) {
      setError('Failed to generate value chain model. Need more conversation context.');
    } finally {
      setIsGeneratingModel(false);
    }
  };

  const saveConfiguration = async () => {
    if (!sessionId || (transcript.length === 0 && allIntents.length === 0)) {
      setError('Nothing to save. Start a conversation first.');
      return;
    }

    setIsSaving(true);
    setError(null);
    setSaveSuccess(null);

    try {
      const fullTranscript = transcript.map(seg => seg.text).join('\n');
      const uniqueEntities = [...new Set(allIntents.flatMap(i => i.target_entities || []))];
      const uniqueMetrics = [...new Set(allIntents.flatMap(i => i.requested_metrics || []))];

      const request: SaveFullConfigurationRequest = {
        configuration: {
          client_id: userId,
          client_name: 'Demo Client',
          name: `Conversation ${new Date().toLocaleDateString()} ${new Date().toLocaleTimeString()}`,
          description: `Configuration extracted from conversation session ${sessionId}`,
          source_session_id: sessionId,
        },
        recordings: [{
          session_id: sessionId,
          transcript: fullTranscript,
          recorded_at: new Date().toISOString(),
          segments: transcript.map(seg => ({
            id: seg.id,
            text: seg.text,
            timestamp: seg.timestamp.toISOString(),
            isFinal: seg.isFinal,
          })),
        }],
        intents: allIntents.map(intent => ({
          name: intent.name,
          description: intent.description,
          confidence: intent.confidence,
          domain: intent.domain || 'general',
          target_entities: intent.target_entities,
          requested_metrics: intent.requested_metrics,
          parameters: intent.parameters,
        })),
        entities: [
          ...uniqueEntities.map(name => ({
            name,
            entity_type: 'Entity',
            description: `Entity extracted from conversation`,
          })),
          ...uniqueMetrics.map(name => ({
            name,
            entity_type: 'Metric',
            description: `Metric extracted from conversation`,
          })),
        ],
        value_chain_model: generatedModel ? {
          name: generatedModel.name,
          nodes: generatedModel.nodes.map(n => ({
            id: n.id,
            name: n.name,
            type: n.type,
            description: n.description,
            properties: n.properties,
          })),
          links: generatedModel.links.map(l => ({
            source_id: l.source_id,
            target_id: l.target_id,
            type: l.type,
          })),
          generated_from_session: sessionId,
          generation_method: 'llm',
        } : undefined,
      };

      const result = await conversationApi.saveFullConfiguration(request);
      setSaveSuccess(`Configuration saved successfully! ID: ${result.configuration.uuid}`);
    } catch (err) {
      console.error('Error saving configuration:', err);
      setError('Failed to save configuration. Please try again.');
    } finally {
      setIsSaving(false);
    }
  };

  const searchConfigurations = async () => {
    setIsSearching(true);
    setError(null);
    
    try {
      const result = await conversationApi.searchConfigurations(
        searchClientName || undefined,
        searchDateFrom || undefined,
        searchDateTo || undefined
      );
      setSearchResults(result.items);
    } catch (err) {
      console.error('Error searching configurations:', err);
      setError('Failed to search configurations.');
    } finally {
      setIsSearching(false);
    }
  };

  const loadConfiguration = async (configId: number) => {
    setIsLoading(true);
    setError(null);
    
    try {
      const config = await conversationApi.getConfiguration(configId);
      
      if (config.recordings.length > 0) {
        const recording = config.recordings[0];
        if (recording.segments) {
          const loadedTranscript: TranscriptSegment[] = recording.segments.map((seg: any) => ({
            id: seg.id,
            text: seg.text,
            timestamp: new Date(seg.timestamp),
            isFinal: seg.isFinal,
          }));
          setTranscript(loadedTranscript);
        }
      }
      
      if (config.intents.length > 0) {
        const loadedIntents: BusinessIntent[] = config.intents.map((intent: any) => ({
          name: intent.name,
          confidence: intent.confidence,
          parameters: intent.parameters || {},
          description: intent.description,
          domain: intent.domain,
          target_entities: intent.target_entities,
          requested_metrics: intent.requested_metrics,
        }));
        setAllIntents(loadedIntents);
      }
      
      if (config.value_chain_models.length > 0) {
        const model = config.value_chain_models[0];
        setGeneratedModel({
          id: model.uuid,
          name: model.name,
          nodes: model.nodes,
          links: model.links,
          created_at: model.created_at,
        });
      }
      
      setLoadDialogOpen(false);
      setSaveSuccess(`Configuration "${config.configuration.name}" loaded successfully!`);
    } catch (err) {
      console.error('Error loading configuration:', err);
      setError('Failed to load configuration.');
    } finally {
      setIsLoading(false);
    }
  };

  const getIntentColor = (confidence: number) => {
    if (confidence >= 0.8) return 'bg-green-500/20 text-green-400 border-green-500/30';
    if (confidence >= 0.5) return 'bg-amber-500/20 text-amber-400 border-amber-500/30';
    return 'bg-red-500/20 text-red-400 border-red-500/30';
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

  const formatTime = (date: Date) => {
    return date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
  };

  const uniqueEntities = [...new Set(allIntents.flatMap(i => i.target_entities || []))];
  const uniqueMetrics = [...new Set(allIntents.flatMap(i => i.requested_metrics || []))];

  return (
    <div className="h-[calc(100vh-120px)] flex flex-col animate-fade-in">
      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <div>
          <h1 className="text-3xl font-bold theme-text-title tracking-wide">AI Interview</h1>
          <p className="theme-text-muted mt-1">Listen to conversations and extract business entities & relationships in real-time</p>
        </div>
        <div className="flex items-center gap-2">
          <Button variant="outline" size="sm" onClick={createSession}>
            <RefreshCw className="w-4 h-4 mr-2" />
            New Session
          </Button>
          <Button 
            size="sm" 
            onClick={generateValueChainModel}
            disabled={transcript.length === 0 || isGeneratingModel}
          >
            <Network className="w-4 h-4 mr-2" />
            {isGeneratingModel ? 'Generating...' : 'Generate Model'}
          </Button>
          <Button 
            variant="secondary" 
            size="sm"
            onClick={saveConfiguration}
            disabled={isSaving || (transcript.length === 0 && allIntents.length === 0)}
          >
            {isSaving ? (
              <RefreshCw className="w-4 h-4 mr-2 animate-spin" />
            ) : (
              <Save className="w-4 h-4 mr-2" />
            )}
            {isSaving ? 'Saving...' : 'Save'}
          </Button>
          <Button variant="outline" size="sm" onClick={() => setLoadDialogOpen(true)}>
            <FolderOpen className="w-4 h-4 mr-2" />
            Load
          </Button>
        </div>
      </div>

      {/* Alerts */}
      {saveSuccess && (
        <div className="mb-4 p-4 rounded-xl bg-green-500/10 border border-green-500/30 text-green-400 flex items-center justify-between">
          <span>{saveSuccess}</span>
          <button onClick={() => setSaveSuccess(null)}><X className="w-4 h-4" /></button>
        </div>
      )}

      {error && (
        <div className="mb-4 p-4 rounded-xl bg-red-500/10 border border-red-500/30 text-red-400 flex items-center justify-between">
          <span>{error}</span>
          <button onClick={() => setError(null)}><X className="w-4 h-4" /></button>
        </div>
      )}

      {/* Main Content */}
      <div className="flex gap-4 flex-1 min-h-0">
        {/* Left Panel - Audio Listener & Transcript */}
        <Card className="flex-[2] flex flex-col overflow-hidden">
          {/* Audio Controls */}
          <div className={cn(
            "p-4 border-b theme-border",
            isListening ? "bg-red-500/10" : "theme-card-bg"
          )}>
            <div className="flex items-center gap-4">
              <button
                onClick={toggleListening}
                disabled={!speechSupported}
                className={cn(
                  "w-16 h-16 rounded-full flex items-center justify-center transition-all",
                  isListening 
                    ? "bg-red-500 hover:bg-red-600 animate-pulse" 
                    : "bg-alpha-500 hover:bg-alpha-600",
                  "text-white"
                )}
              >
                {isListening ? <Square className="w-8 h-8" /> : <Mic className="w-8 h-8" />}
              </button>
              
              <div className="flex-1">
                <div className="flex items-center gap-2">
                  {isListening && <Circle className="w-3 h-3 text-red-500 animate-pulse" />}
                  <span className="text-lg font-semibold theme-text-title">
                    {isListening ? 'Listening...' : 'Click to Start Listening'}
                  </span>
                </div>
                {isListening && (
                  <div className="mt-2">
                    <div className="h-2 rounded-full bg-alpha-faded-200 dark:bg-alpha-faded-800 overflow-hidden">
                      <div 
                        className={cn(
                          "h-full transition-all duration-100",
                          audioLevel > 0.5 ? "bg-green-500" : "bg-alpha-500"
                        )}
                        style={{ width: `${audioLevel * 100}%` }}
                      />
                    </div>
                    <div className="flex items-center gap-1 mt-1">
                      <AudioWaveform className="w-3 h-3 theme-text-muted" />
                      <span className="text-xs theme-text-muted">Audio Level</span>
                    </div>
                  </div>
                )}
              </div>

              <Button
                variant="outline"
                size="sm"
                onClick={clearTranscript}
                disabled={transcript.length === 0}
              >
                <Trash2 className="w-4 h-4 mr-1" />
                Clear
              </Button>
            </div>
          </div>

          {/* Transcript Display */}
          <div className="flex-1 overflow-y-auto p-4">
            {transcript.length === 0 && !currentTranscript ? (
              <div className="text-center py-16">
                <Volume2 className="w-16 h-16 mx-auto theme-text-muted opacity-30 mb-4" />
                <h3 className="text-lg font-semibold theme-text-title mb-2">Ready to Listen</h3>
                <p className="theme-text-muted text-sm max-w-md mx-auto">
                  Click the microphone button to start listening to your conversation.
                  The system will transcribe speech and extract business intents in real-time.
                </p>
              </div>
            ) : (
              <div className="space-y-3">
                {transcript.map((segment) => (
                  <div key={segment.id} className="p-3 rounded-xl theme-card-bg border theme-border">
                    <div className="flex items-start gap-3">
                      <Volume2 className="w-5 h-5 theme-info-icon mt-0.5 flex-shrink-0" />
                      <div className="flex-1 min-w-0">
                        <p className="theme-text">{segment.text}</p>
                        <p className="text-xs theme-text-muted mt-1">{formatTime(segment.timestamp)}</p>
                        {segment.intents && segment.intents.length > 0 && (
                          <div className="flex flex-wrap gap-1.5 mt-2">
                            {segment.intents.map((intent, idx) => (
                              <span
                                key={idx}
                                className={cn(
                                  "inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs border",
                                  getIntentColor(intent.confidence)
                                )}
                                title={intent.description || intent.name}
                              >
                                <Brain className="w-3 h-3" />
                                {intent.name} ({Math.round(intent.confidence * 100)}%)
                              </span>
                            ))}
                          </div>
                        )}
                      </div>
                    </div>
                  </div>
                ))}
                
                {currentTranscript && (
                  <div className="p-3 rounded-xl theme-card-bg border border-dashed theme-border opacity-70">
                    <div className="flex items-start gap-3">
                      <Volume2 className="w-5 h-5 theme-text-muted mt-0.5 flex-shrink-0" />
                      <div className="flex-1">
                        <p className="theme-text-muted italic">{currentTranscript}</p>
                        <p className="text-xs theme-text-muted mt-1">Listening...</p>
                      </div>
                    </div>
                  </div>
                )}
                
                <div ref={transcriptEndRef} />
              </div>
            )}
          </div>

          {/* Text Input */}
          <div className="p-4 border-t theme-border">
            <p className="text-xs theme-text-muted mb-2">Or type to simulate conversation input:</p>
            <div className="flex gap-2">
              <input
                type="text"
                placeholder="Type what you would say in a conversation..."
                value={textInput}
                onChange={(e) => setTextInput(e.target.value)}
                onKeyPress={handleTextKeyPress}
                disabled={isProcessing}
                className="flex-1 px-4 py-2 rounded-xl theme-card-bg border theme-border
                  theme-text placeholder:theme-text-muted text-sm
                  focus:outline-none focus:ring-2 focus:ring-alpha-500"
              />
              <Button
                onClick={submitTextInput}
                disabled={!textInput.trim() || isProcessing}
              >
                {isProcessing ? (
                  <RefreshCw className="w-4 h-4 animate-spin" />
                ) : (
                  <Send className="w-4 h-4" />
                )}
              </Button>
            </div>
          </div>

          {/* Status Bar */}
          <div className="px-4 py-2 border-t theme-border theme-card-bg">
            <div className="flex items-center justify-between text-xs theme-text-muted">
              <span>{sessionId ? `Session: ${sessionId.substring(0, 8)}...` : 'No session'}</span>
              <div className="flex items-center gap-4">
                <span>Segments: {transcript.length}</span>
                <span>Intents: {allIntents.length}</span>
                {isProcessing && (
                  <span className="flex items-center gap-1 text-alpha-400">
                    <RefreshCw className="w-3 h-3 animate-spin" />
                    Processing...
                  </span>
                )}
              </div>
            </div>
          </div>
        </Card>

        {/* Right Panel - Extracted Data */}
        <Card className="flex-1 flex flex-col overflow-hidden">
          {/* Tabs */}
          <div className="flex border-b theme-border">
            <TabButton active={activeTab === 0} onClick={() => setActiveTab(0)} badge={allIntents.length}>
              Intents
            </TabButton>
            <TabButton active={activeTab === 1} onClick={() => setActiveTab(1)}>
              Entities
            </TabButton>
            <TabButton active={activeTab === 2} onClick={() => setActiveTab(2)}>
              Model
            </TabButton>
          </div>

          {/* Tab Content */}
          <div className="flex-1 overflow-y-auto p-4">
            {/* Intents Tab */}
            {activeTab === 0 && (
              <div>
                {allIntents.length === 0 ? (
                  <div className="text-center py-12">
                    <Brain className="w-12 h-12 mx-auto theme-text-muted opacity-50 mb-4" />
                    <p className="theme-text-muted text-sm">Business intents will appear here as you speak</p>
                  </div>
                ) : (
                  <div className="space-y-2">
                    {allIntents.map((intent, idx) => (
                      <div key={idx} className="p-3 rounded-xl theme-card-bg border theme-border">
                        <div className="flex items-center justify-between mb-1">
                          <span className="font-semibold theme-text-title text-sm">{intent.name}</span>
                          <span className={cn(
                            "px-2 py-0.5 rounded-full text-xs border",
                            getIntentColor(intent.confidence)
                          )}>
                            {Math.round(intent.confidence * 100)}%
                          </span>
                        </div>
                        {intent.description && (
                          <p className="text-xs theme-text-muted mb-2">{intent.description}</p>
                        )}
                        {intent.target_entities && intent.target_entities.length > 0 && (
                          <div className="flex flex-wrap gap-1">
                            {intent.target_entities.map((e, i) => (
                              <span key={i} className="px-2 py-0.5 rounded-full text-xs border theme-border theme-text-muted">
                                {e}
                              </span>
                            ))}
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                )}
              </div>
            )}

            {/* Entities Tab */}
            {activeTab === 1 && (
              <div>
                {allIntents.length === 0 ? (
                  <div className="text-center py-12">
                    <GitBranch className="w-12 h-12 mx-auto theme-text-muted opacity-50 mb-4" />
                    <p className="theme-text-muted text-sm">Extracted entities will appear here</p>
                  </div>
                ) : (
                  <div className="space-y-4">
                    <div>
                      <h4 className="font-semibold theme-text-title text-sm mb-2">
                        Entities ({uniqueEntities.length})
                      </h4>
                      <div className="space-y-1">
                        {uniqueEntities.map((entity, idx) => (
                          <div key={idx} className="p-2 rounded-lg theme-card-bg border theme-border flex items-center gap-2">
                            <GitBranch className="w-4 h-4 theme-info-icon" />
                            <span className="text-sm theme-text">{entity}</span>
                          </div>
                        ))}
                      </div>
                    </div>
                    
                    <div className="border-t theme-border pt-4">
                      <h4 className="font-semibold theme-text-title text-sm mb-2">
                        Metrics ({uniqueMetrics.length})
                      </h4>
                      <div className="space-y-1">
                        {uniqueMetrics.map((metric, idx) => (
                          <div key={`m-${idx}`} className="p-2 rounded-lg theme-card-bg border theme-border flex items-center gap-2">
                            <Brain className="w-4 h-4 text-purple-400" />
                            <span className="text-sm theme-text">{metric}</span>
                          </div>
                        ))}
                      </div>
                    </div>
                  </div>
                )}
              </div>
            )}

            {/* Model Tab */}
            {activeTab === 2 && (
              <div>
                {!generatedModel ? (
                  <div className="text-center py-12">
                    <Network className="w-12 h-12 mx-auto theme-text-muted opacity-50 mb-4" />
                    <p className="theme-text-muted text-sm">Click "Generate Model" to create a value chain model from the conversation</p>
                  </div>
                ) : (
                  <div className="space-y-4">
                    <h3 className="font-semibold theme-text-title">{generatedModel.name}</h3>
                    
                    <div>
                      <h4 className="text-sm font-medium theme-text-title mb-2">
                        Nodes ({generatedModel.nodes.length})
                      </h4>
                      <div className="space-y-1">
                        {generatedModel.nodes.map((node) => (
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

                    <div>
                      <h4 className="text-sm font-medium theme-text-title mb-2">
                        Relationships ({generatedModel.links.length})
                      </h4>
                      <div className="space-y-1">
                        {generatedModel.links.map((link, idx) => {
                          const sourceNode = generatedModel.nodes.find(n => n.id === link.source_id);
                          const targetNode = generatedModel.nodes.find(n => n.id === link.target_id);
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
                  </div>
                )}
              </div>
            )}
          </div>
        </Card>
      </div>

      {/* Load Configuration Dialog */}
      {loadDialogOpen && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="w-full max-w-3xl mx-4 rounded-2xl theme-card-bg border theme-border shadow-2xl">
            <div className="p-6 border-b theme-border">
              <h2 className="text-xl font-bold theme-text-title">Load Saved Configuration</h2>
            </div>
            <div className="p-6 space-y-4">
              <p className="text-sm theme-text-muted">
                Search for saved configurations by client name and/or date range.
              </p>
              
              <div className="flex gap-3">
                <input
                  type="text"
                  placeholder="Client name..."
                  value={searchClientName}
                  onChange={(e) => setSearchClientName(e.target.value)}
                  className="flex-1 px-4 py-2 rounded-xl theme-card-bg border theme-border
                    theme-text placeholder:theme-text-muted text-sm
                    focus:outline-none focus:ring-2 focus:ring-alpha-500"
                />
                <input
                  type="date"
                  value={searchDateFrom}
                  onChange={(e) => setSearchDateFrom(e.target.value)}
                  className="px-4 py-2 rounded-xl theme-card-bg border theme-border
                    theme-text text-sm focus:outline-none focus:ring-2 focus:ring-alpha-500"
                />
                <input
                  type="date"
                  value={searchDateTo}
                  onChange={(e) => setSearchDateTo(e.target.value)}
                  className="px-4 py-2 rounded-xl theme-card-bg border theme-border
                    theme-text text-sm focus:outline-none focus:ring-2 focus:ring-alpha-500"
                />
                <Button onClick={searchConfigurations} disabled={isSearching}>
                  {isSearching ? (
                    <RefreshCw className="w-4 h-4 animate-spin" />
                  ) : (
                    <Search className="w-4 h-4" />
                  )}
                </Button>
              </div>

              {searchResults.length > 0 && (
                <div className="rounded-xl border theme-border overflow-hidden">
                  <table className="w-full text-sm">
                    <thead className="theme-card-bg">
                      <tr>
                        <th className="px-4 py-2 text-left theme-text-muted font-medium">Client</th>
                        <th className="px-4 py-2 text-left theme-text-muted font-medium">Name</th>
                        <th className="px-4 py-2 text-left theme-text-muted font-medium">Created</th>
                        <th className="px-4 py-2 text-left theme-text-muted font-medium">Intents</th>
                        <th className="px-4 py-2 text-left theme-text-muted font-medium">Entities</th>
                        <th className="px-4 py-2 text-left theme-text-muted font-medium">Action</th>
                      </tr>
                    </thead>
                    <tbody>
                      {searchResults.map((config) => (
                        <tr key={config.id} className="border-t theme-border hover:theme-card-bg-hover">
                          <td className="px-4 py-2 theme-text">{config.client_name}</td>
                          <td className="px-4 py-2 theme-text">{config.name}</td>
                          <td className="px-4 py-2 theme-text-muted">
                            {new Date(config.created_at).toLocaleDateString()}
                          </td>
                          <td className="px-4 py-2 theme-text-muted">{config.intent_count}</td>
                          <td className="px-4 py-2 theme-text-muted">{config.entity_count}</td>
                          <td className="px-4 py-2">
                            <Button
                              size="sm"
                              variant="outline"
                              onClick={() => loadConfiguration(config.id)}
                              disabled={isLoading}
                            >
                              {isLoading ? 'Loading...' : 'Load'}
                            </Button>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}

              {searchResults.length === 0 && !isSearching && (
                <div className="text-center py-12">
                  <FolderOpen className="w-12 h-12 mx-auto theme-text-muted opacity-50 mb-4" />
                  <p className="theme-text-muted text-sm">No configurations found. Try searching with different criteria.</p>
                </div>
              )}
            </div>
            <div className="p-6 border-t theme-border flex justify-end">
              <Button variant="outline" onClick={() => setLoadDialogOpen(false)}>
                Cancel
              </Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
