import { useState, useEffect, useRef, useCallback } from 'react';
import {
  Box, Typography, Paper, Button, Chip, Stack,
  Card, CardContent, List, ListItem,
  CircularProgress, Alert, Tabs, Tab, Tooltip, Badge,
  LinearProgress, IconButton, Divider, TextField
} from '@mui/material';
import {
  Mic as MicIcon,
  Psychology as IntentIcon,
  AccountTree as EntityIcon,
  Link as RelationshipIcon,
  Refresh as RefreshIcon,
  Hub as HubIcon,
  GraphicEq as WaveformIcon,
  RecordVoiceOver as SpeakerIcon,
  Stop as StopIcon,
  FiberManualRecord as RecordIcon,
  Delete as ClearIcon,
  Send as SendIcon
} from '@mui/icons-material';

// Types
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

// Extend Window interface for SpeechRecognition
declare global {
  interface Window {
    SpeechRecognition: any;
    webkitSpeechRecognition: any;
  }
}

// API Base URL
const API_BASE = 'http://127.0.0.1:8090/api/v1/conversation';

export default function ConversationServicePage() {
  // Audio/Speech Recognition State
  const [isListening, setIsListening] = useState(false);
  const [transcript, setTranscript] = useState<TranscriptSegment[]>([]);
  const [currentTranscript, setCurrentTranscript] = useState('');
  const [audioLevel, setAudioLevel] = useState(0);
  const [speechSupported, setSpeechSupported] = useState(true);
  
  // Text input fallback
  const [textInput, setTextInput] = useState('');
  
  // Session and Intent State
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [allIntents, setAllIntents] = useState<BusinessIntent[]>([]);
  const [generatedModel, setGeneratedModel] = useState<ValueChainModel | null>(null);
  const [isGeneratingModel, setIsGeneratingModel] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState(0);
  
  // Refs
  const recognitionRef = useRef<any>(null);
  const transcriptEndRef = useRef<HTMLDivElement>(null);
  const audioContextRef = useRef<AudioContext | null>(null);
  const analyserRef = useRef<AnalyserNode | null>(null);
  const animationFrameRef = useRef<number | null>(null);
  const sessionIdRef = useRef<string | null>(null);
  
  const userId = 'demo_user';

  // Keep sessionIdRef in sync with sessionId state
  useEffect(() => {
    sessionIdRef.current = sessionId;
  }, [sessionId]);

  // Scroll to bottom of transcript
  const scrollToBottom = () => {
    transcriptEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [transcript, currentTranscript]);

  // Check for speech recognition support
  useEffect(() => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      setSpeechSupported(false);
      setError('Speech recognition is not supported in this browser. Please use Chrome or Edge.');
    }
  }, []);

  // Create a new session
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

  // Initialize session on mount
  useEffect(() => {
    createSession();
  }, [createSession]);

  // Process transcript segment through the conversation service
  const processTranscript = useCallback(async (text: string, segmentId: string) => {
    const currentSessionId = sessionIdRef.current;
    if (!text.trim()) return;

    // If no session yet, create one first
    if (!currentSessionId) {
      console.log('No session ID available, skipping processing');
      return;
    }

    setIsProcessing(true);
    try {
      console.log('Processing transcript:', text, 'Session:', currentSessionId);
      const response = await fetch(`${API_BASE}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          session_id: currentSessionId,
          user_id: userId,
          message: text,
          skip_response: true,  // Skip LLM response generation for faster intent extraction
        }),
      });

      if (!response.ok) {
        console.error('API response not ok:', response.status, response.statusText);
        throw new Error('Failed to process transcript');
      }

      const data = await response.json();
      console.log('API response:', data);

      // Update the transcript segment with intents
      if (data.intents && data.intents.length > 0) {
        console.log('Extracted intents:', data.intents);
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

  // Setup audio level monitoring
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

  // Cleanup audio monitoring
  const cleanupAudioMonitoring = useCallback(() => {
    if (animationFrameRef.current) {
      cancelAnimationFrame(animationFrameRef.current);
    }
    if (audioContextRef.current) {
      audioContextRef.current.close();
    }
    setAudioLevel(0);
  }, []);

  // Start listening
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
        
        // Process the final transcript for intent extraction
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
      // Restart if still supposed to be listening
      if (isListening && recognitionRef.current) {
        recognitionRef.current.start();
      }
    };

    recognitionRef.current.start();
  }, [isListening, setupAudioMonitoring, processTranscript]);

  // Stop listening
  const stopListening = useCallback(() => {
    setIsListening(false);
    if (recognitionRef.current) {
      recognitionRef.current.stop();
      recognitionRef.current = null;
    }
    cleanupAudioMonitoring();
  }, [cleanupAudioMonitoring]);

  // Toggle listening
  const toggleListening = () => {
    if (isListening) {
      stopListening();
    } else {
      startListening();
    }
  };

  // Clear transcript
  const clearTranscript = () => {
    setTranscript([]);
    setCurrentTranscript('');
    setAllIntents([]);
  };

  // Manual text submission (fallback for when speech doesn't work)
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
    
    // Process the text for intent extraction
    await processTranscript(inputText, segmentId);
  };

  // Handle Enter key for text input
  const handleTextKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      submitTextInput();
    }
  };

  // Generate Value Chain Model
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

  // Get intent color based on confidence
  const getIntentColor = (confidence: number): 'success' | 'warning' | 'error' => {
    if (confidence >= 0.8) return 'success';
    if (confidence >= 0.5) return 'warning';
    return 'error';
  };

  // Get node type color
  const getNodeTypeColor = (type: string): string => {
    const colors: Record<string, string> = {
      'Process': '#F79767',
      'Activity': '#DA7194',
      'Metric': '#4C8EDA',
      'Entity': '#6DCE9E',
    };
    return colors[type] || '#888';
  };

  // Format timestamp
  const formatTime = (date: Date) => {
    return date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
  };

  return (
    <Box sx={{ height: 'calc(100vh - 120px)', display: 'flex', flexDirection: 'column' }}>
      {/* Header */}
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
        <Box>
          <Typography variant="h4">
            Conversation Listener
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Listen to conversations and extract business entities & relationships in real-time
          </Typography>
        </Box>
        <Stack direction="row" spacing={1}>
          <Button
            variant="outlined"
            startIcon={<RefreshIcon />}
            onClick={createSession}
            size="small"
          >
            New Session
          </Button>
          <Button
            variant="contained"
            startIcon={<HubIcon />}
            onClick={generateValueChainModel}
            disabled={transcript.length === 0 || isGeneratingModel}
            size="small"
          >
            {isGeneratingModel ? 'Generating...' : 'Generate Model'}
          </Button>
        </Stack>
      </Box>

      {error && (
        <Alert severity="error" sx={{ mb: 2 }} onClose={() => setError(null)}>
          {error}
        </Alert>
      )}

      <Box sx={{ display: 'flex', gap: 2, flex: 1, minHeight: 0 }}>
        {/* Left Panel - Audio Listener & Transcript */}
        <Paper sx={{ flex: 2, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
          {/* Audio Controls */}
          <Box sx={{ p: 2, borderBottom: 1, borderColor: 'divider', bgcolor: isListening ? 'error.light' : 'grey.100' }}>
            <Stack direction="row" alignItems="center" spacing={2}>
              <IconButton
                onClick={toggleListening}
                disabled={!speechSupported}
                sx={{
                  width: 64,
                  height: 64,
                  bgcolor: isListening ? 'error.main' : 'primary.main',
                  color: 'white',
                  '&:hover': {
                    bgcolor: isListening ? 'error.dark' : 'primary.dark',
                  },
                  animation: isListening ? 'pulse 1.5s infinite' : 'none',
                  '@keyframes pulse': {
                    '0%': { boxShadow: '0 0 0 0 rgba(244, 67, 54, 0.4)' },
                    '70%': { boxShadow: '0 0 0 15px rgba(244, 67, 54, 0)' },
                    '100%': { boxShadow: '0 0 0 0 rgba(244, 67, 54, 0)' },
                  },
                }}
              >
                {isListening ? <StopIcon sx={{ fontSize: 32 }} /> : <MicIcon sx={{ fontSize: 32 }} />}
              </IconButton>
              
              <Box sx={{ flex: 1 }}>
                <Stack direction="row" alignItems="center" spacing={1}>
                  {isListening && <RecordIcon sx={{ color: 'error.main', fontSize: 16 }} />}
                  <Typography variant="h6" fontWeight="bold">
                    {isListening ? 'Listening...' : 'Click to Start Listening'}
                  </Typography>
                </Stack>
                {isListening && (
                  <Box sx={{ mt: 1 }}>
                    <LinearProgress 
                      variant="determinate" 
                      value={audioLevel * 100} 
                      sx={{ 
                        height: 8, 
                        borderRadius: 4,
                        bgcolor: 'rgba(0,0,0,0.1)',
                        '& .MuiLinearProgress-bar': {
                          bgcolor: audioLevel > 0.5 ? 'success.main' : 'primary.main',
                        }
                      }} 
                    />
                    <Stack direction="row" alignItems="center" spacing={1} sx={{ mt: 0.5 }}>
                      <WaveformIcon sx={{ fontSize: 16, color: 'text.secondary' }} />
                      <Typography variant="caption" color="text.secondary">
                        Audio Level
                      </Typography>
                    </Stack>
                  </Box>
                )}
              </Box>

              <Button
                variant="outlined"
                startIcon={<ClearIcon />}
                onClick={clearTranscript}
                disabled={transcript.length === 0}
                size="small"
              >
                Clear
              </Button>
            </Stack>
          </Box>

          {/* Transcript Display */}
          <Box sx={{ flex: 1, overflow: 'auto', p: 2 }}>
            {transcript.length === 0 && !currentTranscript ? (
              <Box sx={{ textAlign: 'center', py: 8, color: 'text.secondary' }}>
                <SpeakerIcon sx={{ fontSize: 64, mb: 2, opacity: 0.3 }} />
                <Typography variant="h6">
                  Ready to Listen
                </Typography>
                <Typography variant="body2" sx={{ mt: 1 }}>
                  Click the microphone button to start listening to your conversation.
                  <br />
                  The system will transcribe speech and extract business intents in real-time.
                </Typography>
              </Box>
            ) : (
              <Stack spacing={2}>
                {transcript.map((segment) => (
                  <Card key={segment.id} variant="outlined">
                    <CardContent sx={{ py: 1.5, '&:last-child': { pb: 1.5 } }}>
                      <Stack direction="row" alignItems="flex-start" spacing={1}>
                        <SpeakerIcon sx={{ color: 'primary.main', mt: 0.5 }} />
                        <Box sx={{ flex: 1 }}>
                          <Typography variant="body1">
                            {segment.text}
                          </Typography>
                          <Typography variant="caption" color="text.secondary">
                            {formatTime(segment.timestamp)}
                          </Typography>
                          {segment.intents && segment.intents.length > 0 && (
                            <Stack direction="row" spacing={0.5} sx={{ mt: 1, flexWrap: 'wrap', gap: 0.5 }}>
                              {segment.intents.map((intent, idx) => (
                                <Tooltip key={idx} title={intent.description || intent.name}>
                                  <Chip
                                    size="small"
                                    icon={<IntentIcon />}
                                    label={`${intent.name} (${Math.round(intent.confidence * 100)}%)`}
                                    color={getIntentColor(intent.confidence)}
                                    variant="outlined"
                                  />
                                </Tooltip>
                              ))}
                            </Stack>
                          )}
                        </Box>
                      </Stack>
                    </CardContent>
                  </Card>
                ))}
                
                {/* Current (interim) transcript */}
                {currentTranscript && (
                  <Card variant="outlined" sx={{ bgcolor: 'grey.50', borderStyle: 'dashed' }}>
                    <CardContent sx={{ py: 1.5, '&:last-child': { pb: 1.5 } }}>
                      <Stack direction="row" alignItems="flex-start" spacing={1}>
                        <SpeakerIcon sx={{ color: 'grey.400', mt: 0.5 }} />
                        <Box sx={{ flex: 1 }}>
                          <Typography variant="body1" sx={{ color: 'text.secondary', fontStyle: 'italic' }}>
                            {currentTranscript}
                          </Typography>
                          <Typography variant="caption" color="text.secondary">
                            Listening...
                          </Typography>
                        </Box>
                      </Stack>
                    </CardContent>
                  </Card>
                )}
                
                <div ref={transcriptEndRef} />
              </Stack>
            )}
          </Box>

          {/* Text Input (fallback for speech) */}
          <Box sx={{ p: 2, borderTop: 1, borderColor: 'divider' }}>
            <Typography variant="caption" color="text.secondary" sx={{ mb: 1, display: 'block' }}>
              Or type to simulate conversation input:
            </Typography>
            <Stack direction="row" spacing={1}>
              <TextField
                fullWidth
                size="small"
                placeholder="Type what you would say in a conversation..."
                value={textInput}
                onChange={(e) => setTextInput(e.target.value)}
                onKeyPress={handleTextKeyPress}
                disabled={isProcessing}
              />
              <Button
                variant="contained"
                onClick={submitTextInput}
                disabled={!textInput.trim() || isProcessing}
                startIcon={isProcessing ? <CircularProgress size={16} /> : <SendIcon />}
              >
                Send
              </Button>
            </Stack>
          </Box>

          {/* Status Bar */}
          <Box sx={{ p: 1, borderTop: 1, borderColor: 'divider', bgcolor: 'grey.50' }}>
            <Stack direction="row" justifyContent="space-between" alignItems="center">
              <Typography variant="caption" color="text.secondary">
                {sessionId ? `Session: ${sessionId.substring(0, 8)}...` : 'No session'}
              </Typography>
              <Stack direction="row" spacing={2}>
                <Typography variant="caption" color="text.secondary">
                  Segments: {transcript.length}
                </Typography>
                <Typography variant="caption" color="text.secondary">
                  Intents: {allIntents.length}
                </Typography>
                {isProcessing && (
                  <Stack direction="row" alignItems="center" spacing={0.5}>
                    <CircularProgress size={12} />
                    <Typography variant="caption" color="primary">
                      Processing...
                    </Typography>
                  </Stack>
                )}
              </Stack>
            </Stack>
          </Box>
        </Paper>

        {/* Right Panel - Extracted Data */}
        <Paper sx={{ flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
          <Tabs value={activeTab} onChange={(_, v) => setActiveTab(v)} sx={{ borderBottom: 1, borderColor: 'divider' }}>
            <Tab label={<Badge badgeContent={allIntents.length} color="primary">Intents</Badge>} />
            <Tab label="Entities" />
            <Tab label="Model" />
          </Tabs>

          <Box sx={{ flex: 1, overflow: 'auto', p: 2 }}>
            {/* Intents Tab */}
            {activeTab === 0 && (
              <Box>
                {allIntents.length === 0 ? (
                  <Box sx={{ textAlign: 'center', py: 4, color: 'text.secondary' }}>
                    <IntentIcon sx={{ fontSize: 48, mb: 2, opacity: 0.5 }} />
                    <Typography variant="body2">
                      Business intents will appear here as you speak
                    </Typography>
                  </Box>
                ) : (
                  <List dense>
                    {allIntents.map((intent, idx) => (
                      <ListItem key={idx} sx={{ mb: 1, px: 0 }}>
                        <Card variant="outlined" sx={{ width: '100%' }}>
                          <CardContent sx={{ py: 1, '&:last-child': { pb: 1 } }}>
                            <Stack direction="row" justifyContent="space-between" alignItems="center">
                              <Typography variant="subtitle2" fontWeight="bold">
                                {intent.name}
                              </Typography>
                              <Chip
                                size="small"
                                label={`${Math.round(intent.confidence * 100)}%`}
                                color={getIntentColor(intent.confidence)}
                              />
                            </Stack>
                            {intent.description && (
                              <Typography variant="caption" color="text.secondary" display="block">
                                {intent.description}
                              </Typography>
                            )}
                            {intent.target_entities && intent.target_entities.length > 0 && (
                              <Box sx={{ mt: 0.5 }}>
                                {intent.target_entities.map((e, i) => (
                                  <Chip key={i} size="small" label={e} sx={{ mr: 0.5, mt: 0.5 }} variant="outlined" />
                                ))}
                              </Box>
                            )}
                          </CardContent>
                        </Card>
                      </ListItem>
                    ))}
                  </List>
                )}
              </Box>
            )}

            {/* Entities Tab */}
            {activeTab === 1 && (
              <Box>
                {allIntents.length === 0 ? (
                  <Box sx={{ textAlign: 'center', py: 4, color: 'text.secondary' }}>
                    <EntityIcon sx={{ fontSize: 48, mb: 2, opacity: 0.5 }} />
                    <Typography variant="body2">
                      Extracted entities will appear here
                    </Typography>
                  </Box>
                ) : (
                  <Box>
                    <Typography variant="subtitle2" gutterBottom fontWeight="bold">
                      Entities ({[...new Set(allIntents.flatMap(i => i.target_entities || []))].length})
                    </Typography>
                    <Stack spacing={1} sx={{ mb: 2 }}>
                      {[...new Set(allIntents.flatMap(i => i.target_entities || []))].map((entity, idx) => (
                        <Card key={idx} variant="outlined">
                          <CardContent sx={{ py: 1, '&:last-child': { pb: 1 } }}>
                            <Stack direction="row" alignItems="center" spacing={1}>
                              <EntityIcon color="primary" fontSize="small" />
                              <Typography variant="body2">{entity}</Typography>
                            </Stack>
                          </CardContent>
                        </Card>
                      ))}
                    </Stack>
                    
                    <Divider sx={{ my: 2 }} />
                    
                    <Typography variant="subtitle2" gutterBottom fontWeight="bold">
                      Metrics ({[...new Set(allIntents.flatMap(i => i.requested_metrics || []))].length})
                    </Typography>
                    <Stack spacing={1}>
                      {[...new Set(allIntents.flatMap(i => i.requested_metrics || []))].map((metric, idx) => (
                        <Card key={`m-${idx}`} variant="outlined">
                          <CardContent sx={{ py: 1, '&:last-child': { pb: 1 } }}>
                            <Stack direction="row" alignItems="center" spacing={1}>
                              <IntentIcon color="secondary" fontSize="small" />
                              <Typography variant="body2">{metric}</Typography>
                            </Stack>
                          </CardContent>
                        </Card>
                      ))}
                    </Stack>
                  </Box>
                )}
              </Box>
            )}

            {/* Model Tab */}
            {activeTab === 2 && (
              <Box>
                {!generatedModel ? (
                  <Box sx={{ textAlign: 'center', py: 4, color: 'text.secondary' }}>
                    <HubIcon sx={{ fontSize: 48, mb: 2, opacity: 0.5 }} />
                    <Typography variant="body2">
                      Click "Generate Model" to create a value chain model from the conversation
                    </Typography>
                  </Box>
                ) : (
                  <Box>
                    <Typography variant="subtitle1" fontWeight="bold" gutterBottom>
                      {generatedModel.name}
                    </Typography>
                    
                    <Typography variant="subtitle2" sx={{ mt: 2, mb: 1 }}>
                      Nodes ({generatedModel.nodes.length})
                    </Typography>
                    <Stack spacing={1}>
                      {generatedModel.nodes.map((node) => (
                        <Card key={node.id} variant="outlined">
                          <CardContent sx={{ py: 1, '&:last-child': { pb: 1 } }}>
                            <Stack direction="row" alignItems="center" spacing={1}>
                              <Box
                                sx={{
                                  width: 12,
                                  height: 12,
                                  borderRadius: '50%',
                                  bgcolor: getNodeTypeColor(node.type),
                                }}
                              />
                              <Typography variant="body2" fontWeight="bold">
                                {node.name}
                              </Typography>
                              <Chip size="small" label={node.type} />
                            </Stack>
                            {node.description && (
                              <Typography variant="caption" color="text.secondary" display="block" sx={{ mt: 0.5 }}>
                                {node.description}
                              </Typography>
                            )}
                          </CardContent>
                        </Card>
                      ))}
                    </Stack>

                    <Typography variant="subtitle2" sx={{ mt: 2, mb: 1 }}>
                      Relationships ({generatedModel.links.length})
                    </Typography>
                    <Stack spacing={1}>
                      {generatedModel.links.map((link, idx) => {
                        const sourceNode = generatedModel.nodes.find(n => n.id === link.source_id);
                        const targetNode = generatedModel.nodes.find(n => n.id === link.target_id);
                        return (
                          <Card key={idx} variant="outlined">
                            <CardContent sx={{ py: 1, '&:last-child': { pb: 1 } }}>
                              <Stack direction="row" alignItems="center" spacing={1} flexWrap="wrap">
                                <RelationshipIcon color="action" fontSize="small" />
                                <Typography variant="body2">
                                  {sourceNode?.name || link.source_id}
                                </Typography>
                                <Chip size="small" label={link.type} color="primary" variant="outlined" />
                                <Typography variant="body2">
                                  {targetNode?.name || link.target_id}
                                </Typography>
                              </Stack>
                            </CardContent>
                          </Card>
                        );
                      })}
                    </Stack>
                  </Box>
                )}
              </Box>
            )}
          </Box>
        </Paper>
      </Box>
    </Box>
  );
}
