/**
 * Degraded Mode Banner
 * 
 * Displays when the multi_agent_service is unavailable and 
 * the system is operating in degraded mode with reduced functionality.
 */

import { AlertTriangle, X, Info } from 'lucide-react';

// =============================================================================
// Types
// =============================================================================

export interface DegradedModeInfo {
  active: boolean;
  reason: string;
  suspendedFeatures: string[];
  activeFeatures: string[];
}

export interface DegradedModeBannerProps {
  info: DegradedModeInfo;
  onDismiss?: () => void;
  variant?: 'full' | 'compact';
}

// =============================================================================
// Main Component
// =============================================================================

export function DegradedModeBanner({
  info,
  onDismiss,
  variant = 'full',
}: DegradedModeBannerProps) {
  if (!info.active) {
    return null;
  }

  if (variant === 'compact') {
    return (
      <div 
        className="flex items-center gap-2 px-3 py-2 bg-amber-500/10 border border-amber-500/30 rounded-lg"
        data-testid="degraded-mode-banner"
      >
        <AlertTriangle className="w-4 h-4 text-amber-400 flex-shrink-0" />
        <span className="text-sm text-amber-400">
          <span className="font-medium">DEGRADED MODE</span>
          {info.reason && <span className="ml-1 text-amber-400/70">— {info.reason}</span>}
        </span>
        {onDismiss && (
          <button
            onClick={onDismiss}
            className="ml-auto p-1 rounded hover:bg-amber-500/20 transition-colors"
          >
            <X className="w-3 h-3 text-amber-400" />
          </button>
        )}
      </div>
    );
  }

  return (
    <div 
      className="rounded-lg border border-amber-500/30 bg-amber-500/5 overflow-hidden"
      data-testid="degraded-mode-banner"
    >
      {/* Header */}
      <div className="flex items-center justify-between px-4 py-3 bg-amber-500/10 border-b border-amber-500/30">
        <div className="flex items-center gap-2">
          <AlertTriangle className="w-5 h-5 text-amber-400" />
          <span className="font-semibold text-amber-400">DEGRADED MODE ACTIVE</span>
        </div>
        {onDismiss && (
          <button
            onClick={onDismiss}
            className="p-1 rounded hover:bg-amber-500/20 transition-colors"
          >
            <X className="w-4 h-4 text-amber-400" />
          </button>
        )}
      </div>

      {/* Content */}
      <div className="p-4 space-y-4">
        {/* Reason */}
        {info.reason && (
          <div className="flex items-start gap-2">
            <Info className="w-4 h-4 text-amber-400 mt-0.5 flex-shrink-0" />
            <p className="text-sm text-amber-300">{info.reason}</p>
          </div>
        )}

        {/* Suspended Features */}
        {info.suspendedFeatures.length > 0 && (
          <div>
            <h4 className="text-xs font-medium text-amber-400/70 uppercase mb-2">
              Suspended Features
            </h4>
            <ul className="space-y-1">
              {info.suspendedFeatures.map((feature, i) => (
                <li key={i} className="flex items-center gap-2 text-sm text-amber-300/80">
                  <span className="w-1.5 h-1.5 rounded-full bg-amber-500/50" />
                  {feature}
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Still Active */}
        {info.activeFeatures.length > 0 && (
          <div>
            <h4 className="text-xs font-medium text-green-400/70 uppercase mb-2">
              Still Active (Tier 0 Rules)
            </h4>
            <ul className="space-y-1">
              {info.activeFeatures.map((feature, i) => (
                <li key={i} className="flex items-center gap-2 text-sm text-green-300/80">
                  <span className="w-1.5 h-1.5 rounded-full bg-green-500/50" />
                  {feature}
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Tier 0 Notice */}
        <div className="pt-2 border-t border-amber-500/20">
          <p className="text-xs text-amber-400/60">
            <strong>Note:</strong> Tier 0 contract rules remain in effect. Agents will not 
            fabricate success, modify tests to pass, or proceed without signaling when stuck.
          </p>
        </div>
      </div>
    </div>
  );
}

export default DegradedModeBanner;
