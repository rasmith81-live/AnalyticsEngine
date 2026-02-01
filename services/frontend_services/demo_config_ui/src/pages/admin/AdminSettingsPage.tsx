import { useState } from 'react';
import { 
  Shield, 
  Save,
  ToggleLeft,
  ToggleRight,
  AlertTriangle,
  Server,
  Percent,
} from 'lucide-react';

interface AgentSettings {
  multiAgentServiceEnabled: boolean;
  blackboardRolloutPercent: number;
  contractEnforcementEnabled: boolean;
  peerReviewRequired: boolean;
  circuitBreakerFailureThreshold: number;
  circuitBreakerRecoveryTimeout: number;
  fallbackToLocalEnabled: boolean;
  announceDegradedMode: boolean;
}

const defaultSettings: AgentSettings = {
  multiAgentServiceEnabled: true,
  blackboardRolloutPercent: 100,
  contractEnforcementEnabled: true,
  peerReviewRequired: true,
  circuitBreakerFailureThreshold: 3,
  circuitBreakerRecoveryTimeout: 60,
  fallbackToLocalEnabled: true,
  announceDegradedMode: true,
};

export default function AdminSettingsPage() {
  const [settings, setSettings] = useState<AgentSettings>(defaultSettings);
  const [isSaving, setIsSaving] = useState(false);
  const [saveSuccess, setSaveSuccess] = useState(false);

  const handleSave = async () => {
    setIsSaving(true);
    await new Promise(resolve => setTimeout(resolve, 1000));
    setIsSaving(false);
    setSaveSuccess(true);
    setTimeout(() => setSaveSuccess(false), 3000);
  };

  const Toggle = ({ enabled, onChange }: { enabled: boolean; onChange: (v: boolean) => void }) => (
    <button
      onClick={() => onChange(!enabled)}
      className={`relative w-12 h-6 rounded-full transition-colors ${
        enabled ? 'bg-emerald-500' : 'bg-gray-600'
      }`}
    >
      <div className={`absolute top-1 w-4 h-4 rounded-full bg-white transition-transform ${
        enabled ? 'left-7' : 'left-1'
      }`} />
    </button>
  );

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title">System Settings</h1>
          <p className="mt-2 theme-text-secondary">
            Configure multi-agent service behavior and feature flags
          </p>
        </div>
        <div className="flex items-center gap-3">
          {saveSuccess && (
            <span className="text-sm text-emerald-400">Settings saved!</span>
          )}
          <button
            onClick={handleSave}
            disabled={isSaving}
            className="px-4 py-2 rounded-lg bg-alpha-500 hover:bg-alpha-600 text-white flex items-center gap-2"
          >
            <Save className="w-4 h-4" />
            {isSaving ? 'Saving...' : 'Save Settings'}
          </button>
        </div>
      </div>

      {/* Warning */}
      <div className="theme-card rounded-xl p-4 border border-amber-500/30 bg-amber-500/5">
        <div className="flex items-start gap-3">
          <AlertTriangle className="w-5 h-5 text-amber-400 flex-shrink-0 mt-0.5" />
          <div>
            <h3 className="font-medium text-amber-400">Admin Only</h3>
            <p className="text-sm theme-text-secondary mt-1">
              These settings affect all users and the entire agent system. Changes take effect immediately.
            </p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-6">
        {/* Feature Flags */}
        <div className="theme-card rounded-xl p-6">
          <div className="flex items-center gap-3 mb-6">
            <div className="w-10 h-10 rounded-lg bg-alpha-500/10 flex items-center justify-center">
              {settings.multiAgentServiceEnabled ? (
                <ToggleRight className="w-5 h-5 text-alpha-400" />
              ) : (
                <ToggleLeft className="w-5 h-5 text-alpha-400" />
              )}
            </div>
            <div>
              <h2 className="font-semibold theme-text-title">Feature Flags</h2>
              <p className="text-sm theme-text-muted">Control system behavior</p>
            </div>
          </div>

          <div className="space-y-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium theme-text-title">Multi-Agent Service</p>
                <p className="text-sm theme-text-muted">Enable distributed agent coordination</p>
              </div>
              <Toggle
                enabled={settings.multiAgentServiceEnabled}
                onChange={(v) => setSettings({ ...settings, multiAgentServiceEnabled: v })}
              />
            </div>

            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium theme-text-title">Contract Enforcement</p>
                <p className="text-sm theme-text-muted">Enforce tiered contract rules</p>
              </div>
              <Toggle
                enabled={settings.contractEnforcementEnabled}
                onChange={(v) => setSettings({ ...settings, contractEnforcementEnabled: v })}
              />
            </div>

            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium theme-text-title">Peer Review Required</p>
                <p className="text-sm theme-text-muted">Require reviewer approval for agent outputs</p>
              </div>
              <Toggle
                enabled={settings.peerReviewRequired}
                onChange={(v) => setSettings({ ...settings, peerReviewRequired: v })}
              />
            </div>

            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium theme-text-title">Fallback to Local</p>
                <p className="text-sm theme-text-muted">Use local processing if service unavailable</p>
              </div>
              <Toggle
                enabled={settings.fallbackToLocalEnabled}
                onChange={(v) => setSettings({ ...settings, fallbackToLocalEnabled: v })}
              />
            </div>

            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium theme-text-title">Announce Degraded Mode</p>
                <p className="text-sm theme-text-muted">Show notification when in degraded mode</p>
              </div>
              <Toggle
                enabled={settings.announceDegradedMode}
                onChange={(v) => setSettings({ ...settings, announceDegradedMode: v })}
              />
            </div>
          </div>
        </div>

        {/* Configuration Values */}
        <div className="space-y-6">
          {/* Rollout */}
          <div className="theme-card rounded-xl p-6">
            <div className="flex items-center gap-3 mb-6">
              <div className="w-10 h-10 rounded-lg bg-emerald-500/10 flex items-center justify-center">
                <Percent className="w-5 h-5 text-emerald-400" />
              </div>
              <div>
                <h2 className="font-semibold theme-text-title">Blackboard Rollout</h2>
                <p className="text-sm theme-text-muted">Percentage of sessions using blackboard coordination</p>
              </div>
            </div>

            <div>
              <div className="flex items-center justify-between mb-2">
                <span className="text-sm theme-text-muted">Rollout Percentage</span>
                <span className="text-sm font-medium theme-text-title">{settings.blackboardRolloutPercent}%</span>
              </div>
              <input
                type="range"
                min="0"
                max="100"
                value={settings.blackboardRolloutPercent}
                onChange={(e) => setSettings({ ...settings, blackboardRolloutPercent: parseInt(e.target.value) })}
                className="w-full h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer"
              />
              <div className="flex justify-between text-xs theme-text-muted mt-1">
                <span>0%</span>
                <span>50%</span>
                <span>100%</span>
              </div>
            </div>
          </div>

          {/* Circuit Breaker */}
          <div className="theme-card rounded-xl p-6">
            <div className="flex items-center gap-3 mb-6">
              <div className="w-10 h-10 rounded-lg bg-red-500/10 flex items-center justify-center">
                <Shield className="w-5 h-5 text-red-400" />
              </div>
              <div>
                <h2 className="font-semibold theme-text-title">Circuit Breaker</h2>
                <p className="text-sm theme-text-muted">Failure protection settings</p>
              </div>
            </div>

            <div className="space-y-4">
              <div>
                <label className="block text-sm theme-text-muted mb-2">Failure Threshold</label>
                <div className="flex items-center gap-3">
                  <input
                    type="number"
                    min="1"
                    max="10"
                    value={settings.circuitBreakerFailureThreshold}
                    onChange={(e) => setSettings({ ...settings, circuitBreakerFailureThreshold: parseInt(e.target.value) || 3 })}
                    className="w-24 px-3 py-2 rounded-lg theme-input"
                  />
                  <span className="text-sm theme-text-muted">failures before circuit opens</span>
                </div>
              </div>

              <div>
                <label className="block text-sm theme-text-muted mb-2">Recovery Timeout</label>
                <div className="flex items-center gap-3">
                  <input
                    type="number"
                    min="10"
                    max="300"
                    value={settings.circuitBreakerRecoveryTimeout}
                    onChange={(e) => setSettings({ ...settings, circuitBreakerRecoveryTimeout: parseInt(e.target.value) || 60 })}
                    className="w-24 px-3 py-2 rounded-lg theme-input"
                  />
                  <span className="text-sm theme-text-muted">seconds before retry</span>
                </div>
              </div>
            </div>
          </div>

          {/* Service Info */}
          <div className="theme-card rounded-xl p-6">
            <div className="flex items-center gap-3 mb-6">
              <div className="w-10 h-10 rounded-lg bg-blue-500/10 flex items-center justify-center">
                <Server className="w-5 h-5 text-blue-400" />
              </div>
              <div>
                <h2 className="font-semibold theme-text-title">Service Configuration</h2>
                <p className="text-sm theme-text-muted">Connection settings (read-only)</p>
              </div>
            </div>

            <div className="space-y-3 text-sm">
              <div className="flex justify-between">
                <span className="theme-text-muted">Service URL</span>
                <code className="font-mono theme-text-secondary">http://multi_agent_service:8000</code>
              </div>
              <div className="flex justify-between">
                <span className="theme-text-muted">Timeout</span>
                <code className="font-mono theme-text-secondary">30.0s</code>
              </div>
              <div className="flex justify-between">
                <span className="theme-text-muted">Status</span>
                <span className="text-emerald-400 flex items-center gap-1">
                  <span className="w-2 h-2 rounded-full bg-emerald-400"></span>
                  Connected
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
