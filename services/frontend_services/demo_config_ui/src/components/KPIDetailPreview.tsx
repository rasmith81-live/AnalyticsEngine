/**
 * KPIDetailPreview Component
 * Shows full KPI profile when selected, like a product detail page
 */

import { useState } from 'react';
import {
  Plus,
  GitBranch,
  Calculator,
  Info,
  ExternalLink,
  RefreshCw,
  AlertTriangle,
} from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import { Card } from './ui/Card';
import { Button } from './ui/Button';
import { cn } from '../lib/utils';
import { useKPIDetail } from '../hooks/useKPIDetails';
import { useObjectModels } from '../hooks/useObjectModelDetails';
import ObjectModelDiagram from './ObjectModelDiagram';
import type { KPI } from '../types';

interface KPIDetailPreviewProps {
  kpiCode: string | null;
  onAddToCart: (kpiCode: string) => void;
  onDeriveCustomKPI: (kpiCode: string) => void;
  isInCart: boolean;
}

function TabButton({ active, onClick, children }: { active: boolean; onClick: () => void; children: React.ReactNode }) {
  return (
    <button
      onClick={onClick}
      className={cn(
        "flex-1 py-2 text-sm font-medium transition-colors border-b-2",
        active ? "text-alpha-500 border-alpha-500" : "theme-text-muted border-transparent hover:theme-text"
      )}
    >
      {children}
    </button>
  );
}

function ObjectModelDiagramsSection({ requiredObjects }: { requiredObjects: string[] }) {
  const { data: objectModels, isLoading, error } = useObjectModels(requiredObjects);
  const [selectedModel, setSelectedModel] = useState<string | null>(null);

  if (isLoading) {
    return (
      <div className="flex justify-center p-4">
        <RefreshCw className="w-5 h-5 text-alpha-500 animate-spin" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-3 rounded-lg bg-amber-500/10 border border-amber-500/30 text-amber-400 text-sm">
        Unable to load object model diagrams. The metadata service may be unavailable.
      </div>
    );
  }

  if (!objectModels || objectModels.length === 0) return null;

  const modelWithSchema = objectModels.find(model => model.schema_definition);
  if (!modelWithSchema) {
    return (
      <div className="p-3 rounded-lg bg-blue-500/10 border border-blue-500/30 text-blue-400 text-sm">
        Object model diagrams are not available for the required objects.
      </div>
    );
  }

  return (
    <div>
      <p className="text-xs theme-text-muted mb-2">Relationship Diagram</p>
      <ObjectModelDiagram
        schemaDefinition={modelWithSchema.schema_definition || ''}
        highlightEntity={selectedModel || undefined}
        onEntityClick={(entityName) => setSelectedModel(entityName)}
      />
      {selectedModel && (
        <div className="mt-2">
          <span className="inline-flex items-center gap-1 px-2 py-1 rounded-full text-xs bg-alpha-500/20 text-alpha-400">
            Selected: {selectedModel}
            <button onClick={() => setSelectedModel(null)} className="ml-1 hover:text-white">×</button>
          </span>
        </div>
      )}
    </div>
  );
}

export default function KPIDetailPreview({ kpiCode, onAddToCart, onDeriveCustomKPI, isInCart }: KPIDetailPreviewProps) {
  const navigate = useNavigate();
  const [activeTab, setActiveTab] = useState(0);
  const { data: kpi, isLoading, error } = useKPIDetail(kpiCode || '');

  if (!kpiCode) {
    return (
      <Card className="h-full flex items-center justify-center">
        <div className="text-center p-8">
          <Info className="w-16 h-16 mx-auto theme-text-muted opacity-30 mb-4" />
          <h3 className="text-lg font-semibold theme-text-muted mb-1">Select a KPI to view details</h3>
          <p className="text-sm theme-text-muted">Click on any KPI in the tree to see its full profile</p>
        </div>
      </Card>
    );
  }

  if (isLoading) {
    return (
      <Card className="h-full flex items-center justify-center">
        <RefreshCw className="w-8 h-8 text-alpha-500 animate-spin" />
      </Card>
    );
  }

  if (error || !kpi) {
    return (
      <Card className="p-4">
        <div className="p-3 rounded-lg bg-red-500/10 border border-red-500/30 text-red-400">
          Failed to load KPI details
        </div>
      </Card>
    );
  }

  const getDisplayName = (kpi: KPI) => kpi.display_name || kpi.name || kpi.code;

  return (
    <Card className="h-full flex flex-col overflow-hidden">
      {/* Header */}
      <div className="p-4 border-b theme-border">
        <div className="flex items-start justify-between mb-2">
          <div className="flex-1 min-w-0">
            <h2 className="text-xl font-bold theme-text-title truncate">{getDisplayName(kpi)}</h2>
            <p className="text-xs theme-text-muted">{kpi.code}</p>
          </div>
          {isInCart && (
            <span className="px-2 py-1 rounded-full text-xs bg-green-500/20 text-green-400 border border-green-500/30">In Cart</span>
          )}
        </div>

        {/* Action Buttons */}
        <div className="flex gap-2 mt-3">
          <Button onClick={() => onAddToCart(kpi.code)} disabled={isInCart} className="flex-1">
            <Plus className="w-4 h-4 mr-1" />
            {isInCart ? 'Added' : 'Add to Cart'}
          </Button>
          <Button variant="outline" onClick={() => onDeriveCustomKPI(kpi.code)} className="flex-1">
            <Calculator className="w-4 h-4 mr-1" />
            Derive Custom
          </Button>
        </div>
        <button
          onClick={() => navigate(`/kpi/${kpi.code}`)}
          className="w-full mt-2 py-2 text-sm text-alpha-500 hover:underline flex items-center justify-center gap-1"
        >
          <ExternalLink className="w-4 h-4" />
          View Full Details
        </button>
      </div>

      {/* Tabs */}
      <div className="flex border-b theme-border">
        <TabButton active={activeTab === 0} onClick={() => setActiveTab(0)}>Overview</TabButton>
        <TabButton active={activeTab === 1} onClick={() => setActiveTab(1)}>Formula</TabButton>
        <TabButton active={activeTab === 2} onClick={() => setActiveTab(2)}>Objects</TabButton>
      </div>

      {/* Tab Content */}
      <div className="flex-1 overflow-y-auto p-4">
        {/* Overview Tab */}
        {activeTab === 0 && (
          <div className="space-y-4">
            {kpi.description && (
              <div>
                <p className="text-xs theme-text-muted mb-1">Description</p>
                <p className="text-sm theme-text">{kpi.description}</p>
              </div>
            )}

            {kpi.full_kpi_definition && (
              <div>
                <p className="text-xs theme-text-muted mb-1">Full Definition</p>
                <div className="p-3 rounded-lg theme-card-bg border theme-border text-sm theme-text whitespace-pre-wrap">
                  {kpi.full_kpi_definition}
                </div>
              </div>
            )}

            {kpi.diagnostic_questions && (
              <div>
                <p className="text-xs theme-text-muted mb-1">Diagnostic Questions</p>
                <div className="p-3 rounded-lg bg-blue-500/10 border border-blue-500/30 text-sm text-blue-400 whitespace-pre-wrap">
                  {kpi.diagnostic_questions}
                </div>
              </div>
            )}

            {kpi.risk_warnings && (
              <div>
                <p className="text-xs theme-text-muted mb-1">Risk Warnings</p>
                <div className="p-3 rounded-lg bg-amber-500/10 border border-amber-500/30 text-sm text-amber-400 flex gap-2">
                  <AlertTriangle className="w-4 h-4 flex-shrink-0 mt-0.5" />
                  <span className="whitespace-pre-wrap">{kpi.risk_warnings}</span>
                </div>
              </div>
            )}

            <div>
              <p className="text-xs theme-text-muted mb-1">Unit</p>
              <span className="px-2 py-1 rounded-full text-xs theme-card-bg border theme-border theme-text">{kpi.unit || 'N/A'}</span>
            </div>

            {kpi.metadata_ && (
              <>
                {kpi.metadata_.modules && kpi.metadata_.modules.length > 0 && (
                  <div>
                    <p className="text-xs theme-text-muted mb-1">Modules</p>
                    <div className="flex flex-wrap gap-1">
                      {kpi.metadata_.modules.map((module) => (
                        <span key={module} className="px-2 py-0.5 rounded-full text-xs border theme-border theme-text">{module}</span>
                      ))}
                    </div>
                  </div>
                )}

                {kpi.metadata_.value_chains && kpi.metadata_.value_chains.length > 0 && (
                  <div>
                    <p className="text-xs theme-text-muted mb-1">Value Chains</p>
                    <div className="flex flex-wrap gap-1">
                      {kpi.metadata_.value_chains.map((vc) => (
                        <span key={vc} className="px-2 py-0.5 rounded-full text-xs bg-alpha-500/20 text-alpha-400 border border-alpha-500/30">{vc}</span>
                      ))}
                    </div>
                  </div>
                )}

                {kpi.metadata_.category && (
                  <div>
                    <p className="text-xs theme-text-muted mb-1">Category</p>
                    <span className="px-2 py-0.5 rounded-full text-xs bg-purple-500/20 text-purple-400 border border-purple-500/30">{kpi.metadata_.category}</span>
                  </div>
                )}
              </>
            )}

            {kpi.benchmarks && Object.keys(kpi.benchmarks).length > 0 && (
              <div>
                <p className="text-xs theme-text-muted mb-1">Benchmarks</p>
                <div className="p-3 rounded-lg theme-card-bg border theme-border">
                  {Object.entries(kpi.benchmarks).map(([key, value]) => (
                    <div key={key} className="flex justify-between text-xs mb-1 last:mb-0">
                      <span className="theme-text-muted">{key}:</span>
                      <span className="font-semibold theme-text">{String(value)}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}

        {/* Formula Tab */}
        {activeTab === 1 && (
          <div className="space-y-4">
            <div>
              <p className="text-xs theme-text-muted mb-1">Formula</p>
              <div className="p-3 rounded-lg theme-card-bg border theme-border font-mono text-sm theme-text">
                {kpi.formula}
              </div>
            </div>

            {kpi.calculation_logic && (
              <div>
                <p className="text-xs theme-text-muted mb-1">Calculation Logic</p>
                <p className="text-sm theme-text whitespace-pre-wrap">{kpi.calculation_logic}</p>
              </div>
            )}
          </div>
        )}

        {/* Objects Tab */}
        {activeTab === 2 && (
          <div className="space-y-4">
            <div>
              <p className="text-xs theme-text-muted mb-2">Required Objects ({kpi.required_objects?.length || 0})</p>
              {kpi.required_objects && kpi.required_objects.length > 0 ? (
                <div className="space-y-2">
                  {kpi.required_objects.map((obj) => (
                    <div
                      key={obj}
                      className="p-3 rounded-lg border theme-border flex items-center justify-between hover:bg-alpha-faded-50 dark:hover:bg-alpha-faded-900 transition-colors"
                    >
                      <div className="flex items-center gap-2">
                        <GitBranch className="w-4 h-4 text-alpha-500" />
                        <span className="text-sm theme-text">{obj}</span>
                      </div>
                      <button
                        onClick={() => console.log('View object model:', obj)}
                        className="text-xs text-alpha-500 hover:underline"
                      >
                        View Schema
                      </button>
                    </div>
                  ))}
                </div>
              ) : (
                <p className="text-sm theme-text-muted">No required objects defined</p>
              )}
            </div>

            {kpi.required_objects && kpi.required_objects.length > 0 && (
              <ObjectModelDiagramsSection requiredObjects={kpi.required_objects} />
            )}
          </div>
        )}
      </div>
    </Card>
  );
}
