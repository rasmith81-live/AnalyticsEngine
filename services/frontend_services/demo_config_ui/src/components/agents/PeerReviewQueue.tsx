/**
 * Peer Review Queue
 * 
 * Displays artifacts pending review and completed reviews.
 * Shows review status, creator, reviewer, and verdict.
 */

import { useState } from 'react';
import {
  Eye,
  CheckCircle2,
  XCircle,
  Clock,
  User,
  FileText,
  ChevronRight,
} from 'lucide-react';
import { cn } from '../../lib/utils';

// =============================================================================
// Types
// =============================================================================

export interface PendingReview {
  artifactId: string;
  artifactType: string;
  creatorRole: string;
  reviewerRole: string;
  submittedAt: string;
  title?: string;
}

export interface CompletedReview {
  artifactId: string;
  artifactType: string;
  creatorRole: string;
  reviewerRole: string;
  verdict: 'approved' | 'rejected' | 'revision_needed';
  comments?: string;
  reviewedAt: string;
}

export interface PeerReviewQueueProps {
  sessionId: string;
  pendingReviews: PendingReview[];
  completedReviews?: CompletedReview[];
  onViewArtifact?: (artifactId: string) => void;
}

// =============================================================================
// Helper Components
// =============================================================================

function VerdictBadge({ verdict }: { verdict: string }) {
  const config = {
    approved: { icon: CheckCircle2, color: 'text-green-400 bg-green-500/20', label: 'Approved' },
    rejected: { icon: XCircle, color: 'text-red-400 bg-red-500/20', label: 'Rejected' },
    revision_needed: { icon: Clock, color: 'text-amber-400 bg-amber-500/20', label: 'Revision Needed' },
  }[verdict] || { icon: Clock, color: 'text-gray-400 bg-gray-500/20', label: verdict };

  const Icon = config.icon;

  return (
    <span className={cn("flex items-center gap-1 px-2 py-0.5 rounded text-xs", config.color)}>
      <Icon className="w-3 h-3" />
      {config.label}
    </span>
  );
}

function ArtifactTypeBadge({ type }: { type: string }) {
  const typeColors: Record<string, string> = {
    schema: 'bg-blue-500/20 text-blue-400',
    entity: 'bg-purple-500/20 text-purple-400',
    kpi: 'bg-green-500/20 text-green-400',
    value_chain: 'bg-amber-500/20 text-amber-400',
    documentation: 'bg-cyan-500/20 text-cyan-400',
    default: 'bg-gray-500/20 text-gray-400',
  };

  const color = typeColors[type.toLowerCase()] || typeColors.default;

  return (
    <span className={cn("px-2 py-0.5 rounded text-xs", color)}>
      {type}
    </span>
  );
}

function PendingReviewItem({ review, onView }: {
  review: PendingReview;
  onView?: () => void;
}) {
  const timeSince = (dateStr: string) => {
    const date = new Date(dateStr);
    const now = new Date();
    const diffMs = now.getTime() - date.getTime();
    const diffMins = Math.floor(diffMs / 60000);
    
    if (diffMins < 1) return 'just now';
    if (diffMins < 60) return `${diffMins}m ago`;
    const diffHours = Math.floor(diffMins / 60);
    if (diffHours < 24) return `${diffHours}h ago`;
    return `${Math.floor(diffHours / 24)}d ago`;
  };

  return (
    <div className="flex items-center justify-between p-3 hover:bg-gray-800/50 transition-colors">
      <div className="flex items-center gap-3">
        <div className="w-8 h-8 rounded-full bg-amber-500/20 flex items-center justify-center">
          <Clock className="w-4 h-4 text-amber-400" />
        </div>
        <div>
          <div className="flex items-center gap-2">
            <ArtifactTypeBadge type={review.artifactType} />
            <span className="text-sm font-medium">
              {review.title || `Artifact ${review.artifactId.slice(0, 8)}`}
            </span>
          </div>
          <div className="flex items-center gap-2 text-xs text-gray-400 mt-1">
            <User className="w-3 h-3" />
            <span>{review.creatorRole}</span>
            <ChevronRight className="w-3 h-3" />
            <span>{review.reviewerRole}</span>
            <span>•</span>
            <span>{timeSince(review.submittedAt)}</span>
          </div>
        </div>
      </div>
      
      {onView && (
        <button
          onClick={onView}
          className="p-2 rounded hover:bg-gray-700 transition-colors"
          title="View artifact"
        >
          <Eye className="w-4 h-4 text-gray-400" />
        </button>
      )}
    </div>
  );
}

function CompletedReviewItem({ review }: { review: CompletedReview }) {
  return (
    <div className="flex items-center justify-between p-3 hover:bg-gray-800/50 transition-colors">
      <div className="flex items-center gap-3">
        <div className={cn(
          "w-8 h-8 rounded-full flex items-center justify-center",
          review.verdict === 'approved' ? 'bg-green-500/20' : 
          review.verdict === 'rejected' ? 'bg-red-500/20' : 'bg-amber-500/20'
        )}>
          {review.verdict === 'approved' ? (
            <CheckCircle2 className="w-4 h-4 text-green-400" />
          ) : review.verdict === 'rejected' ? (
            <XCircle className="w-4 h-4 text-red-400" />
          ) : (
            <Clock className="w-4 h-4 text-amber-400" />
          )}
        </div>
        <div>
          <div className="flex items-center gap-2">
            <ArtifactTypeBadge type={review.artifactType} />
            <VerdictBadge verdict={review.verdict} />
          </div>
          <div className="flex items-center gap-2 text-xs text-gray-400 mt-1">
            <span>{review.creatorRole}</span>
            <ChevronRight className="w-3 h-3" />
            <span>{review.reviewerRole}</span>
          </div>
        </div>
      </div>
    </div>
  );
}

// =============================================================================
// Main Component
// =============================================================================

export function PeerReviewQueue({
  sessionId: _sessionId,
  pendingReviews,
  completedReviews = [],
  onViewArtifact,
}: PeerReviewQueueProps) {
  void _sessionId; // Reserved for future use
  const [showCompleted, setShowCompleted] = useState(false);

  return (
    <div className="rounded-lg border border-gray-700 bg-gray-900/50 overflow-hidden">
      {/* Header */}
      <div className="flex items-center justify-between px-4 py-3 border-b border-gray-700 bg-gray-800/50">
        <div className="flex items-center gap-2">
          <FileText className="w-5 h-5 text-alpha-400" />
          <h3 className="font-semibold">Peer Reviews</h3>
          {pendingReviews.length > 0 && (
            <span className="px-2 py-0.5 rounded-full bg-amber-500 text-white text-xs font-medium">
              {pendingReviews.length}
            </span>
          )}
        </div>
        
        {completedReviews.length > 0 && (
          <button
            onClick={() => setShowCompleted(!showCompleted)}
            className="text-xs text-gray-400 hover:text-white transition-colors"
          >
            {showCompleted ? 'Hide completed' : `Show ${completedReviews.length} completed`}
          </button>
        )}
      </div>

      {/* Pending Reviews */}
      <div className="divide-y divide-gray-700">
        {pendingReviews.length === 0 ? (
          <div className="p-4 text-center text-gray-400 text-sm">
            No pending reviews
          </div>
        ) : (
          pendingReviews.map(review => (
            <PendingReviewItem
              key={review.artifactId}
              review={review}
              onView={onViewArtifact ? () => onViewArtifact(review.artifactId) : undefined}
            />
          ))
        )}
      </div>

      {/* Completed Reviews */}
      {showCompleted && completedReviews.length > 0 && (
        <>
          <div className="px-4 py-2 bg-gray-800/30 border-t border-gray-700">
            <span className="text-xs text-gray-400 font-medium">Completed Reviews</span>
          </div>
          <div className="divide-y divide-gray-700">
            {completedReviews.map(review => (
              <CompletedReviewItem key={review.artifactId} review={review} />
            ))}
          </div>
        </>
      )}
    </div>
  );
}

export default PeerReviewQueue;
