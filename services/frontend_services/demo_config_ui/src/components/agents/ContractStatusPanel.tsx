/**
 * Contract Status Panel
 * 
 * Displays contract compliance status for all agents in a session.
 * Shows current state, violation count, and state machine transitions.
 */

import { useState } from 'react';
import {
  Shield,
  AlertTriangle,
  CheckCircle2,
  XCircle,
  Clock,
  ChevronDown,
  ChevronUp,
} from 'lucide-react';
import { cn } from '../../lib/utils';

// =============================================================================
// Types
// =============================================================================

export interface AgentContractStatus {
  agentRole: string;
  currentState: string;
  assumptionCount: number;
  failedAttempts: number;
  lastTransition: string | null;
  contractViolations: number;
}

export interface ContractStatusPanelProps {
  sessionId: string;
  agents: AgentContractStatus[];
  degradedMode: boolean;
  degradedReason?: string;
  onRefresh?: () => void;
}

// =============================================================================
// Helper Components
// =============================================================================

function StateIndicator({ state }: { state: string }) {
  const stateColors: Record<string, string> = {
    idle: 'bg-gray-500',
    analysis: 'bg-blue-500',
    approval: 'bg-amber-500',
    execution: 'bg-purple-500',
    validation: 'bg-cyan-500',
    done: 'bg-green-500',
    hard_stop: 'bg-red-500',
    unknown: 'bg-gray-400',
  };

  const color = stateColors[state.toLowerCase()] || stateColors.unknown;

  return (
    <span className={cn(
      "px-2 py-0.5 rounded-full text-xs font-medium text-white",
      color
    )}>
      {state}
    </span>
  );
}

function ViolationBadge({ count }: { count: number }) {
  if (count === 0) {
    return (
      <span className="flex items-center gap-1 text-green-400 text-xs">
        <CheckCircle2 className="w-3 h-3" />
        Clean
      </span>
    );
  }

  return (
    <span className={cn(
      "flex items-center gap-1 text-xs",
      count >= 3 ? "text-red-400" : "text-amber-400"
    )}>
      <AlertTriangle className="w-3 h-3" />
      {count} violation{count !== 1 ? 's' : ''}
    </span>
  );
}

function AgentStatusRow({ agent, expanded, onToggle }: {
  agent: AgentContractStatus;
  expanded: boolean;
  onToggle: () => void;
}) {
  return (
    <div className="border-b border-gray-700 last:border-b-0">
      <div
        className="flex items-center justify-between p-3 cursor-pointer hover:bg-gray-800/50"
        onClick={onToggle}
      >
        <div className="flex items-center gap-3">
          <Shield className="w-4 h-4 text-alpha-400" />
          <span className="font-medium text-sm">{agent.agentRole}</span>
        </div>
        
        <div className="flex items-center gap-4">
          <StateIndicator state={agent.currentState} />
          <ViolationBadge count={agent.contractViolations} />
          {expanded ? (
            <ChevronUp className="w-4 h-4 text-gray-400" />
          ) : (
            <ChevronDown className="w-4 h-4 text-gray-400" />
          )}
        </div>
      </div>
      
      {expanded && (
        <div className="px-3 pb-3 pl-10 text-sm space-y-2">
          <div className="grid grid-cols-2 gap-4">
            <div>
              <span className="text-gray-400">Assumptions:</span>
              <span className="ml-2 text-white">{agent.assumptionCount}</span>
            </div>
            <div>
              <span className="text-gray-400">Failed Attempts:</span>
              <span className={cn(
                "ml-2",
                agent.failedAttempts >= 2 ? "text-red-400" : "text-white"
              )}>
                {agent.failedAttempts}
              </span>
            </div>
          </div>
          {agent.lastTransition && (
            <div className="flex items-center gap-2 text-gray-400">
              <Clock className="w-3 h-3" />
              <span>Last transition: {agent.lastTransition}</span>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

// =============================================================================
// Main Component
// =============================================================================

export function ContractStatusPanel({
  sessionId: _sessionId,
  agents,
  degradedMode,
  degradedReason,
  onRefresh,
}: ContractStatusPanelProps) {
  const [expandedAgents, setExpandedAgents] = useState<Set<string>>(new Set());

  const toggleAgent = (role: string) => {
    setExpandedAgents(prev => {
      const next = new Set(prev);
      if (next.has(role)) {
        next.delete(role);
      } else {
        next.add(role);
      }
      return next;
    });
  };

  const totalViolations = agents.reduce((sum, a) => sum + a.contractViolations, 0);
  const hasHardStop = agents.some(a => a.currentState === 'hard_stop');

  return (
    <div className="rounded-lg border border-gray-700 bg-gray-900/50 overflow-hidden">
      {/* Header */}
      <div className="flex items-center justify-between px-4 py-3 border-b border-gray-700 bg-gray-800/50">
        <div className="flex items-center gap-2">
          <Shield className="w-5 h-5 text-alpha-400" />
          <h3 className="font-semibold">Contract Status</h3>
        </div>
        
        <div className="flex items-center gap-3">
          {hasHardStop && (
            <span className="flex items-center gap-1 px-2 py-1 rounded bg-red-500/20 text-red-400 text-xs">
              <XCircle className="w-3 h-3" />
              HARD STOP
            </span>
          )}
          {totalViolations > 0 && (
            <span className="flex items-center gap-1 px-2 py-1 rounded bg-amber-500/20 text-amber-400 text-xs">
              <AlertTriangle className="w-3 h-3" />
              {totalViolations} violations
            </span>
          )}
          {onRefresh && (
            <button
              onClick={onRefresh}
              className="text-gray-400 hover:text-white transition-colors"
              title="Refresh status"
            >
              ↻
            </button>
          )}
        </div>
      </div>

      {/* Degraded Mode Banner */}
      {degradedMode && (
        <div className="px-4 py-2 bg-amber-500/10 border-b border-amber-500/30">
          <div className="flex items-center gap-2 text-amber-400 text-sm">
            <AlertTriangle className="w-4 h-4" />
            <span className="font-medium">DEGRADED MODE</span>
          </div>
          {degradedReason && (
            <p className="text-xs text-amber-400/70 mt-1 ml-6">{degradedReason}</p>
          )}
        </div>
      )}

      {/* Agent List */}
      <div className="divide-y divide-gray-700">
        {agents.length === 0 ? (
          <div className="p-4 text-center text-gray-400 text-sm">
            No agents active in this session
          </div>
        ) : (
          agents.map(agent => (
            <AgentStatusRow
              key={agent.agentRole}
              agent={agent}
              expanded={expandedAgents.has(agent.agentRole)}
              onToggle={() => toggleAgent(agent.agentRole)}
            />
          ))
        )}
      </div>
    </div>
  );
}

export default ContractStatusPanel;
