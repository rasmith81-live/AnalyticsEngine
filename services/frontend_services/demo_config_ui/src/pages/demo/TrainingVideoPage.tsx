import { useState } from 'react';
import { Video, Play, Pause, Volume2, Maximize, ChevronRight, ChevronLeft, Clock, CheckCircle } from 'lucide-react';

interface VideoChapter {
  id: string;
  title: string;
  duration: string;
  completed: boolean;
}

const chapters: VideoChapter[] = [
  { id: '1', title: 'Introduction to Northstar', duration: '2:30', completed: true },
  { id: '2', title: 'Understanding Value Chains', duration: '4:15', completed: true },
  { id: '3', title: 'The AI Interview Process', duration: '5:45', completed: false },
  { id: '4', title: 'Configuring Data Simulators', duration: '3:20', completed: false },
  { id: '5', title: 'Viewing Your Analytics', duration: '4:00', completed: false },
  { id: '6', title: 'Finalizing Your Contract', duration: '2:45', completed: false },
];

export default function TrainingVideoPage() {
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentChapter, setCurrentChapter] = useState(chapters[2]);

  const completedCount = chapters.filter((c) => c.completed).length;
  const progressPercent = (completedCount / chapters.length) * 100;

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title">AI Training Video</h1>
          <p className="mt-2 theme-text-secondary">
            Learn how to use Northstar to design your business analytics
          </p>
        </div>
        <div className="flex items-center gap-2 px-4 py-2 rounded-lg bg-alpha-500/10 text-alpha-400">
          <Video className="w-5 h-5" />
          <span className="font-medium">Step 2 of 6</span>
        </div>
      </div>

      {/* Video Player and Chapters */}
      <div className="grid grid-cols-3 gap-6">
        {/* Video Player */}
        <div className="col-span-2 space-y-4">
          <div className="relative aspect-video rounded-2xl overflow-hidden theme-card">
            {/* Video Placeholder */}
            <div className="absolute inset-0 bg-gradient-to-br from-slate-900 to-slate-800 flex items-center justify-center">
              <div className="text-center">
                <div className="w-24 h-24 rounded-full bg-alpha-500/20 flex items-center justify-center mx-auto mb-4 cursor-pointer hover:bg-alpha-500/30 transition-colors"
                     onClick={() => setIsPlaying(!isPlaying)}>
                  {isPlaying ? (
                    <Pause className="w-12 h-12 text-alpha-400" />
                  ) : (
                    <Play className="w-12 h-12 text-alpha-400 ml-2" />
                  )}
                </div>
                <h3 className="text-xl font-semibold text-white mb-2">{currentChapter.title}</h3>
                <p className="text-slate-400">AI-generated training content</p>
              </div>
            </div>

            {/* Video Controls */}
            <div className="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/80 to-transparent">
              {/* Progress Bar */}
              <div className="w-full h-1 bg-slate-700 rounded-full mb-4 cursor-pointer">
                <div className="h-full w-1/3 bg-alpha-500 rounded-full relative">
                  <div className="absolute right-0 top-1/2 -translate-y-1/2 w-3 h-3 bg-white rounded-full shadow-lg" />
                </div>
              </div>

              {/* Controls */}
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-4">
                  <button
                    onClick={() => setIsPlaying(!isPlaying)}
                    className="p-2 rounded-lg hover:bg-white/10 transition-colors"
                  >
                    {isPlaying ? (
                      <Pause className="w-5 h-5 text-white" />
                    ) : (
                      <Play className="w-5 h-5 text-white" />
                    )}
                  </button>
                  <button className="p-2 rounded-lg hover:bg-white/10 transition-colors">
                    <Volume2 className="w-5 h-5 text-white" />
                  </button>
                  <span className="text-sm text-white">1:45 / {currentChapter.duration}</span>
                </div>
                <button className="p-2 rounded-lg hover:bg-white/10 transition-colors">
                  <Maximize className="w-5 h-5 text-white" />
                </button>
              </div>
            </div>
          </div>

          {/* Video Description */}
          <div className="theme-card rounded-xl p-6">
            <h3 className="font-semibold theme-text-title mb-2">About This Chapter</h3>
            <p className="theme-text-secondary">
              In this chapter, you'll learn how the AI Interview process works. Our specialized AI agents 
              will guide you through defining your business strategy, identifying key performance indicators, 
              and mapping your analytics requirements. This interactive session typically takes 15-30 minutes.
            </p>
          </div>
        </div>

        {/* Chapter List */}
        <div className="theme-card rounded-2xl p-6">
          <div className="flex items-center justify-between mb-6">
            <h3 className="font-semibold theme-text-title">Chapters</h3>
            <span className="text-sm theme-text-muted">{completedCount}/{chapters.length} completed</span>
          </div>

          {/* Progress Bar */}
          <div className="w-full h-2 bg-slate-700 rounded-full mb-6">
            <div
              className="h-full bg-emerald-500 rounded-full transition-all duration-500"
              style={{ width: `${progressPercent}%` }}
            />
          </div>

          {/* Chapter List */}
          <div className="space-y-2">
            {chapters.map((chapter) => (
              <button
                key={chapter.id}
                onClick={() => setCurrentChapter(chapter)}
                className={`w-full p-4 rounded-xl text-left transition-all duration-200 ${
                  currentChapter.id === chapter.id
                    ? 'bg-alpha-500/20 border border-alpha-500/50'
                    : 'hover:bg-[var(--card-hover)]'
                }`}
              >
                <div className="flex items-center gap-3">
                  <div className={`w-8 h-8 rounded-full flex items-center justify-center ${
                    chapter.completed
                      ? 'bg-emerald-500/20 text-emerald-400'
                      : currentChapter.id === chapter.id
                      ? 'bg-alpha-500/20 text-alpha-400'
                      : 'bg-slate-700 text-slate-400'
                  }`}>
                    {chapter.completed ? (
                      <CheckCircle className="w-4 h-4" />
                    ) : (
                      <span className="text-sm font-medium">{chapter.id}</span>
                    )}
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className={`font-medium truncate ${
                      currentChapter.id === chapter.id ? 'text-alpha-400' : 'theme-text-title'
                    }`}>
                      {chapter.title}
                    </p>
                    <div className="flex items-center gap-1 text-xs theme-text-muted">
                      <Clock className="w-3 h-3" />
                      {chapter.duration}
                    </div>
                  </div>
                </div>
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Navigation */}
      <div className="flex justify-between">
        <a
          href="/demo/value-chains"
          className="px-6 py-3 rounded-xl theme-card hover:bg-[var(--card-hover)] font-medium transition-colors flex items-center gap-2"
        >
          <ChevronLeft className="w-5 h-5" />
          Back to Value Chains
        </a>
        <a
          href="/demo/interview"
          className="px-6 py-3 rounded-xl bg-alpha-500 hover:bg-alpha-600 text-white font-medium transition-colors flex items-center gap-2"
        >
          Start AI Interview
          <ChevronRight className="w-5 h-5" />
        </a>
      </div>
    </div>
  );
}
