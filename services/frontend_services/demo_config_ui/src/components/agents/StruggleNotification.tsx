/**
 * Struggle Notification
 * 
 * Displays struggle signals from agents when they need help or synchronization.
 * Based on the struggle protocol from the agent contracts.
 */

import { useState } from 'react';
import {
  AlertOctagon,
  HelpCircle,
  RefreshCw,
  MessageSquare,
  X,
  ChevronDown,
  ChevronUp,
} from 'lucide-react';
import { cn } from '../../lib/utils';

// =============================================================================
// Types
// =============================================================================

export interface StruggleSignal {
  id: string;
  agentRole: string;
  signalType: 'sync_needed' | 'blocked' | 'needs_clarification' | 'resource_needed';
  whatIUnderstand: string;
  whatITried: { action: string; result: string }[];
  whereImStuck: string;
  whatWouldHelp: string;
  timestamp: string;
}

export interface StruggleNotificationProps {
  signal: StruggleSignal;
  onAcknowledge?: (signalId: string) => void;
  onDismiss?: (signalId: string) => void;
  compact?: boolean;
}

// =============================================================================
// Helper Components
// =============================================================================

function SignalTypeIcon({ type }: { type: string }) {
  const icons: Record<string, { icon: typeof AlertOctagon; color: string }> = {
    sync_needed: { icon: RefreshCw, color: 'text-amber-400' },
    blocked: { icon: AlertOctagon, color: 'text-red-400' },
    needs_clarification: { icon: HelpCircle, color: 'text-blue-400' },
    resource_needed: { icon: MessageSquare, color: 'text-purple-400' },
  };

  const config = icons[type] || { icon: HelpCircle, color: 'text-gray-400' };
  const Icon = config.icon;

  return <Icon className={cn("w-5 h-5", config.color)} />;
}

function SignalTypeLabel({ type }: { type: string }) {
  const labels: Record<string, { text: string; color: string }> = {
    sync_needed: { text: 'SYNC NEEDED', color: 'bg-amber-500/20 text-amber-400' },
    blocked: { text: 'BLOCKED', color: 'bg-red-500/20 text-red-400' },
    needs_clarification: { text: 'NEEDS CLARIFICATION', color: 'bg-blue-500/20 text-blue-400' },
    resource_needed: { text: 'RESOURCE NEEDED', color: 'bg-purple-500/20 text-purple-400' },
  };

  const config = labels[type] || { text: type.toUpperCase(), color: 'bg-gray-500/20 text-gray-400' };

  return (
    <span className={cn("px-2 py-0.5 rounded text-xs font-medium", config.color)}>
      {config.text}
    </span>
  );
}

// =============================================================================
// Main Component
// =============================================================================

export function StruggleNotification({
  signal,
  onAcknowledge,
  onDismiss,
  compact = false,
}: StruggleNotificationProps) {
  const [expanded, setExpanded] = useState(!compact);

  const borderColor = {
    sync_needed: 'border-amber-500/50',
    blocked: 'border-red-500/50',
    needs_clarification: 'border-blue-500/50',
    resource_needed: 'border-purple-500/50',
  }[signal.signalType] || 'border-gray-500/50';

  const bgColor = {
    sync_needed: 'bg-amber-500/5',
    blocked: 'bg-red-500/5',
    needs_clarification: 'bg-blue-500/5',
    resource_needed: 'bg-purple-500/5',
  }[signal.signalType] || 'bg-gray-500/5';

  return (
    <div
      className={cn(
        "rounded-lg border-l-4 overflow-hidden",
        borderColor,
        bgColor
      )}
      data-testid="struggle-notification"
    >
      {/* Header */}
      <div className="flex items-center justify-between p-3">
        <div className="flex items-center gap-3">
          <SignalTypeIcon type={signal.signalType} />
          <div>
            <div className="flex items-center gap-2">
              <span className="font-medium text-sm">{signal.agentRole}</span>
              <SignalTypeLabel type={signal.signalType} />
            </div>
            {compact && !expanded && (
              <p className="text-xs text-gray-400 mt-0.5 line-clamp-1">
                {signal.whereImStuck}
              </p>
            )}
          </div>
        </div>

        <div className="flex items-center gap-2">
          {compact && (
            <button
              onClick={() => setExpanded(!expanded)}
              className="p-1 rounded hover:bg-gray-700/50 transition-colors"
            >
              {expanded ? (
                <ChevronUp className="w-4 h-4 text-gray-400" />
              ) : (
                <ChevronDown className="w-4 h-4 text-gray-400" />
              )}
            </button>
          )}
          {onDismiss && (
            <button
              onClick={() => onDismiss(signal.id)}
              className="p-1 rounded hover:bg-gray-700/50 transition-colors"
              title="Dismiss"
            >
              <X className="w-4 h-4 text-gray-400" />
            </button>
          )}
        </div>
      </div>

      {/* Expanded Content */}
      {expanded && (
        <div className="px-4 pb-4 space-y-4">
          {/* What I Understand */}
          <div>
            <h4 className="text-xs font-medium text-gray-400 uppercase mb-1">
              What I understand
            </h4>
            <p className="text-sm text-gray-200">{signal.whatIUnderstand}</p>
          </div>

          {/* What I Tried */}
          {signal.whatITried.length > 0 && (
            <div>
              <h4 className="text-xs font-medium text-gray-400 uppercase mb-1">
                What I tried
              </h4>
              <ul className="space-y-1">
                {signal.whatITried.map((attempt, i) => (
                  <li key={i} className="text-sm">
                    <span className="text-gray-300">{attempt.action}</span>
                    <span className="text-gray-500"> → </span>
                    <span className="text-gray-400">{attempt.result}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Where I'm Stuck */}
          <div>
            <h4 className="text-xs font-medium text-gray-400 uppercase mb-1">
              Where I'm stuck
            </h4>
            <p className="text-sm text-gray-200">{signal.whereImStuck}</p>
          </div>

          {/* What Would Help */}
          <div>
            <h4 className="text-xs font-medium text-gray-400 uppercase mb-1">
              What would help
            </h4>
            <p className="text-sm text-gray-200">{signal.whatWouldHelp}</p>
          </div>

          {/* Actions */}
          {onAcknowledge && (
            <div className="pt-2">
              <button
                onClick={() => onAcknowledge(signal.id)}
                className="px-4 py-2 rounded bg-alpha-500 hover:bg-alpha-600 text-white text-sm font-medium transition-colors"
              >
                Acknowledge & Assist
              </button>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default StruggleNotification;
