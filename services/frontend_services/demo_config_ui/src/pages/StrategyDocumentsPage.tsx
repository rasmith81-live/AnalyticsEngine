import { useState } from 'react';
import {
  FileText,
  Download,
  Share2,
  Clock,
  User,
  Search,
  Plus,
  MoreVertical,
  Eye,
  Edit,
  Trash2,
  FileSpreadsheet,
  Presentation,
  FileBarChart,
  Filter,
  Calendar,
  CheckCircle,
  AlertCircle,
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { cn } from '../lib/utils';

type DocumentType = 'all' | 'executive' | 'board' | 'kpi' | 'competitive' | 'implementation';
type DocumentStatus = 'draft' | 'review' | 'approved' | 'published';

interface Document {
  id: string;
  title: string;
  type: DocumentType;
  status: DocumentStatus;
  author: string;
  lastModified: string;
  version: string;
  description: string;
  pages?: number;
}

const mockDocuments: Document[] = [
  {
    id: '1',
    title: 'Q4 2025 Executive Summary',
    type: 'executive',
    status: 'published',
    author: 'AI Strategist',
    lastModified: '2 hours ago',
    version: 'v2.1',
    description: 'One-page strategy overview highlighting key achievements and focus areas.',
    pages: 1,
  },
  {
    id: '2',
    title: 'Board Strategy Deck - January 2026',
    type: 'board',
    status: 'review',
    author: 'John Doe',
    lastModified: '1 day ago',
    version: 'v1.3',
    description: 'Quarterly strategy presentation for board review.',
    pages: 24,
  },
  {
    id: '3',
    title: 'KPI Performance Report - December',
    type: 'kpi',
    status: 'approved',
    author: 'Data Analyst Agent',
    lastModified: '3 days ago',
    version: 'v1.0',
    description: 'Monthly KPI performance metrics and trend analysis.',
    pages: 12,
  },
  {
    id: '4',
    title: 'Competitive Landscape Analysis',
    type: 'competitive',
    status: 'draft',
    author: 'Competitive Analyst',
    lastModified: '5 days ago',
    version: 'v0.8',
    description: 'Market positioning report with competitor profiles.',
    pages: 18,
  },
  {
    id: '5',
    title: 'Implementation Roadmap 2026',
    type: 'implementation',
    status: 'published',
    author: 'Operations Manager',
    lastModified: '1 week ago',
    version: 'v1.0',
    description: 'Technical deployment guide and timeline.',
    pages: 32,
  },
];

const documentTypeConfig: Record<DocumentType, { label: string; icon: React.ReactNode; color: string }> = {
  all: { label: 'All Documents', icon: <FileText className="w-4 h-4" />, color: 'bg-alpha-500' },
  executive: { label: 'Executive Summary', icon: <FileText className="w-4 h-4" />, color: 'bg-blue-500' },
  board: { label: 'Board Deck', icon: <Presentation className="w-4 h-4" />, color: 'bg-purple-500' },
  kpi: { label: 'KPI Report', icon: <FileBarChart className="w-4 h-4" />, color: 'bg-green-500' },
  competitive: { label: 'Competitive Analysis', icon: <FileSpreadsheet className="w-4 h-4" />, color: 'bg-amber-500' },
  implementation: { label: 'Implementation Plan', icon: <FileText className="w-4 h-4" />, color: 'bg-red-500' },
};

const statusConfig: Record<DocumentStatus, { label: string; color: string; icon: React.ReactNode }> = {
  draft: { label: 'Draft', color: 'bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300', icon: <Edit className="w-3 h-3" /> },
  review: { label: 'In Review', color: 'bg-amber-100 text-amber-700 dark:bg-amber-900/30 dark:text-amber-400', icon: <AlertCircle className="w-3 h-3" /> },
  approved: { label: 'Approved', color: 'bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400', icon: <CheckCircle className="w-3 h-3" /> },
  published: { label: 'Published', color: 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400', icon: <CheckCircle className="w-3 h-3" /> },
};

function DocumentCard({ document }: { document: Document }) {
  const [showMenu, setShowMenu] = useState(false);
  const typeConfig = documentTypeConfig[document.type];
  const status = statusConfig[document.status];

  return (
    <Card className="group overflow-hidden">
      <div className={cn('h-1', typeConfig.color)} />
      <CardContent className="p-5">
        <div className="flex items-start justify-between mb-3">
          <div className={cn('p-2 rounded-lg', typeConfig.color, 'bg-opacity-20')}>
            {typeConfig.icon}
          </div>
          <div className="relative">
            <button
              onClick={() => setShowMenu(!showMenu)}
              className="p-1 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 transition-colors"
            >
              <MoreVertical className="w-4 h-4 theme-text-muted" />
            </button>
            {showMenu && (
              <div className="absolute right-0 top-8 w-40 py-2 rounded-xl theme-card-bg border theme-border shadow-xl z-10">
                <button className="w-full px-4 py-2 text-left text-sm theme-text hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 flex items-center gap-2">
                  <Eye className="w-4 h-4" /> View
                </button>
                <button className="w-full px-4 py-2 text-left text-sm theme-text hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 flex items-center gap-2">
                  <Edit className="w-4 h-4" /> Edit
                </button>
                <button className="w-full px-4 py-2 text-left text-sm theme-text hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 flex items-center gap-2">
                  <Download className="w-4 h-4" /> Download
                </button>
                <button className="w-full px-4 py-2 text-left text-sm theme-text hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 flex items-center gap-2">
                  <Share2 className="w-4 h-4" /> Share
                </button>
                <hr className="my-2 theme-border" />
                <button className="w-full px-4 py-2 text-left text-sm text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 flex items-center gap-2">
                  <Trash2 className="w-4 h-4" /> Delete
                </button>
              </div>
            )}
          </div>
        </div>

        <h3 className="font-semibold theme-text-title mb-1 line-clamp-2">{document.title}</h3>
        <p className="text-sm theme-text-muted mb-3 line-clamp-2">{document.description}</p>

        <div className="flex items-center gap-2 mb-3">
          <span className={cn('px-2 py-0.5 rounded-full text-xs font-medium flex items-center gap-1', status.color)}>
            {status.icon}
            {status.label}
          </span>
          <span className="text-xs theme-text-muted">{document.version}</span>
          {document.pages && (
            <span className="text-xs theme-text-muted">{document.pages} pages</span>
          )}
        </div>

        <div className="flex items-center justify-between text-xs theme-text-muted pt-3 border-t theme-border">
          <div className="flex items-center gap-1">
            <User className="w-3 h-3" />
            <span>{document.author}</span>
          </div>
          <div className="flex items-center gap-1">
            <Clock className="w-3 h-3" />
            <span>{document.lastModified}</span>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}

export default function StrategyDocumentsPage() {
  const [selectedType, setSelectedType] = useState<DocumentType>('all');
  const [searchQuery, setSearchQuery] = useState('');

  const filteredDocuments = mockDocuments.filter(doc => {
    const matchesType = selectedType === 'all' || doc.type === selectedType;
    const matchesSearch = doc.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          doc.description.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesType && matchesSearch;
  });

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Page Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title tracking-wide">Strategy Documents</h1>
          <p className="theme-text-muted mt-1">Auto-generated strategy presentations and reports</p>
        </div>
        <Button>
          <Plus className="w-4 h-4 mr-2" />
          Generate Document
        </Button>
      </div>

      {/* Quick Actions */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        {[
          { label: 'Executive Summary', icon: <FileText className="w-5 h-5" />, action: 'Generate 1-page overview' },
          { label: 'Board Deck', icon: <Presentation className="w-5 h-5" />, action: 'Create quarterly presentation' },
          { label: 'KPI Report', icon: <FileBarChart className="w-5 h-5" />, action: 'Generate performance report' },
          { label: 'Competitive Analysis', icon: <FileSpreadsheet className="w-5 h-5" />, action: 'Create market report' },
        ].map((item, index) => (
          <Card key={index} className="p-4 cursor-pointer hover:border-alpha-500 transition-all duration-200">
            <div className="flex items-center gap-3">
              <div className="p-2 rounded-lg bg-alpha-500/20">
                {item.icon}
              </div>
              <div>
                <h3 className="font-medium theme-text-title">{item.label}</h3>
                <p className="text-xs theme-text-muted">{item.action}</p>
              </div>
            </div>
          </Card>
        ))}
      </div>

      {/* Filters */}
      <div className="flex flex-col md:flex-row gap-4">
        {/* Search */}
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 theme-text-muted" />
          <input
            type="text"
            placeholder="Search documents..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full h-10 pl-10 pr-4 rounded-xl theme-card-bg border theme-border
              focus:outline-none focus:ring-2 focus:ring-alpha-500 focus:border-transparent
              theme-text placeholder:theme-text-muted transition-all duration-200"
          />
        </div>

        {/* Type Filters */}
        <div className="flex items-center gap-2 overflow-x-auto pb-2 md:pb-0">
          <Filter className="w-4 h-4 theme-text-muted flex-shrink-0" />
          {(Object.keys(documentTypeConfig) as DocumentType[]).map((type) => (
            <button
              key={type}
              onClick={() => setSelectedType(type)}
              className={cn(
                'flex items-center gap-2 px-3 py-2 rounded-lg text-sm font-medium whitespace-nowrap transition-all duration-200',
                selectedType === type
                  ? 'bg-alpha-600 text-white'
                  : 'theme-card-bg border theme-border theme-text hover:border-alpha-500'
              )}
            >
              {documentTypeConfig[type].icon}
              {documentTypeConfig[type].label}
            </button>
          ))}
        </div>
      </div>

      {/* Documents Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {filteredDocuments.length > 0 ? (
          filteredDocuments.map((doc) => (
            <DocumentCard key={doc.id} document={doc} />
          ))
        ) : (
          <Card className="col-span-full p-12 text-center">
            <FileText className="w-12 h-12 mx-auto theme-text-muted mb-4" />
            <h3 className="text-lg font-semibold theme-text-title mb-2">No documents found</h3>
            <p className="theme-text-muted mb-4">Try adjusting your filters or generate a new document.</p>
            <Button>
              <Plus className="w-4 h-4 mr-2" />
              Generate Document
            </Button>
          </Card>
        )}
      </div>

      {/* Recent Activity */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Calendar className="w-5 h-5 theme-info-icon" />
            Recent Activity
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            {[
              { action: 'Q4 Executive Summary published', user: 'AI Strategist', time: '2 hours ago' },
              { action: 'Board Deck v1.3 submitted for review', user: 'John Doe', time: '1 day ago' },
              { action: 'KPI Report approved by management', user: 'Jane Smith', time: '3 days ago' },
              { action: 'Competitive Analysis draft created', user: 'Competitive Analyst', time: '5 days ago' },
            ].map((activity, index) => (
              <div key={index} className="flex items-center gap-4 p-3 rounded-lg theme-card-bg">
                <div className="w-2 h-2 rounded-full bg-alpha-500" />
                <div className="flex-1">
                  <p className="text-sm theme-text">{activity.action}</p>
                  <p className="text-xs theme-text-muted">by {activity.user}</p>
                </div>
                <span className="text-xs theme-text-muted">{activity.time}</span>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
