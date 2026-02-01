import { useState } from 'react';
import { MessageSquare, Send, User, Bot, ChevronRight, ChevronLeft, Sparkles, Building2, Target, BarChart3 } from 'lucide-react';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
}

interface InterviewPhase {
  id: string;
  name: string;
  icon: React.ReactNode;
  description: string;
  completed: boolean;
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

const initialMessages: Message[] = [
  {
    id: '1',
    role: 'assistant',
    content: "Welcome to the Northstar AI Interview! I'm your Strategy Coordinator, and I'll guide you through designing your business analytics.\n\nLet's start with understanding your business. What industry is your organization in, and what are your primary business activities?",
    timestamp: new Date(),
  },
];

export default function DemoInterviewPage() {
  const [messages, setMessages] = useState<Message[]>(initialMessages);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [currentPhase, setCurrentPhase] = useState(phases[0]);

  const handleSend = () => {
    if (!input.trim()) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: input,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setIsTyping(true);

    // Simulate AI response
    setTimeout(() => {
      const aiResponse: Message = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: "Thank you for sharing that information! Based on your industry, I can see several value chain patterns that would be relevant.\n\nLet me ask a follow-up question: What are the top 3 business challenges you're trying to address with analytics? This will help me recommend the most impactful KPIs for your organization.",
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, aiResponse]);
      setIsTyping(false);
    }, 2000);
  };

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
        <div className="flex items-center gap-2 px-4 py-2 rounded-lg bg-alpha-500/10 text-alpha-400">
          <MessageSquare className="w-5 h-5" />
          <span className="font-medium">Step 3 of 6</span>
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
                  <p className="whitespace-pre-wrap">{message.content}</p>
                  <p className="text-xs theme-text-muted mt-2">
                    {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                  </p>
                </div>
              </div>
            ))}
            {isTyping && (
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
          </div>

          {/* Input */}
          <div className="p-4 border-t theme-border">
            <div className="flex gap-4">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && handleSend()}
                placeholder="Type your response..."
                className="flex-1 px-4 py-3 rounded-xl theme-input"
              />
              <button
                onClick={handleSend}
                disabled={!input.trim()}
                className="px-6 py-3 rounded-xl bg-alpha-500 hover:bg-alpha-600 disabled:opacity-50 disabled:cursor-not-allowed text-white font-medium transition-colors flex items-center gap-2"
              >
                <Send className="w-5 h-5" />
                Send
              </button>
            </div>
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
