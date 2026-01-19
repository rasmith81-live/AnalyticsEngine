/**
 * Object Models Browser Page
 * Browse all object models organized by module/value chain
 */

import { useState } from 'react';
import {
  Search,
  GitBranch,
  Database,
  ArrowRight,
  ArrowLeft,
  ArrowLeftRight,
  RefreshCw,
} from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import { Card, CardContent } from '../components/ui/Card';
import { cn } from '../lib/utils';
import { useObjectModels } from '../hooks/useObjectModels';
import ResizableSplitPanel from '../components/ResizableSplitPanel';
import ObjectModelDiagram from '../components/ObjectModelDiagram';
import type { ObjectModel } from '../types';

interface Relationship {
  from: string;
  to: string;
  type: string;
  cardinality: string;
  label?: string;
  direction: 'forward' | 'backward' | 'bidirectional';
}

function parseRelationships(uml: string, entityCode: string): Relationship[] {
  const relationships: Relationship[] = [];
  const lines = uml.split('\n');
  
  const associationPattern = /([A-Za-z0-9_]+)\s+"([^"]+)"\s+(--)\s+"([^"]+)"\s+([A-Za-z0-9_]+)\s*:\s*(.+?)(?:\s*>)?$/;
  const compositionPattern = /([A-Za-z0-9_]+)\s+"([^"]+)"\s+(\*--)\s+"([^"]+)"\s+([A-Za-z0-9_]+)\s*:\s*(.+?)(?:\s*>)?$/;
  const aggregationPattern = /([A-Za-z0-9_]+)\s+"([^"]+)"\s+(o--)\s+"([^"]+)"\s+([A-Za-z0-9_]+)\s*:\s*(.+?)(?:\s*>)?$/;
  const generalizationPattern = /([A-Za-z0-9_]+)\s+(--\|>)\s+([A-Za-z0-9_]+)/;
  const dependencyPattern = /([A-Za-z0-9_]+)\s+(\.\.>)\s+([A-Za-z0-9_]+)\s*:\s*(.+?)(?:\s*>)?$/;
  
  for (const line of lines) {
    if (line.trim().startsWith("'")) continue;
    
    let match;
    let type = 'association';
    let fromCard = '';
    let toCard = '';
    let from = '';
    let to = '';
    let label = '';
    
    if ((match = line.match(compositionPattern))) {
      [, from, fromCard, , toCard, to, label] = match;
      type = 'composition';
    } else if ((match = line.match(aggregationPattern))) {
      [, from, fromCard, , toCard, to, label] = match;
      type = 'aggregation';
    } else if ((match = line.match(generalizationPattern))) {
      [, from, , to] = match;
      type = 'generalization';
      label = 'inherits from';
    } else if ((match = line.match(dependencyPattern))) {
      [, from, , to, label] = match;
      type = 'dependency';
    } else if ((match = line.match(associationPattern))) {
      [, from, fromCard, , toCard, to, label] = match;
      type = 'association';
    }
    
    if (match && (from === entityCode || to === entityCode)) {
      let direction: 'forward' | 'backward' | 'bidirectional' = 'bidirectional';
      if (type === 'generalization') {
        direction = from === entityCode ? 'forward' : 'backward';
      } else if (type === 'dependency') {
        direction = 'forward';
      }
      
      const cardinality = fromCard && toCard ? `${fromCard} to ${toCard}` : '';
      relationships.push({ from, to, type, cardinality, label: label.trim(), direction });
    }
  }
  
  return relationships;
}

export default function ObjectModelsBrowser() {
  const navigate = useNavigate();
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedModel, setSelectedModel] = useState<string | null>(null);
  
  const { data: objectModels, isLoading, error } = useObjectModels();

  const filteredModels = objectModels?.filter(model => {
    if (!searchQuery) return true;
    const query = searchQuery.toLowerCase();
    return (
      model.name?.toLowerCase().includes(query) ||
      model.display_name?.toLowerCase().includes(query) ||
      model.code?.toLowerCase().includes(query) ||
      model.description?.toLowerCase().includes(query) ||
      model.metadata_?.modules?.some(m => m.toLowerCase().includes(query))
    );
  });

  const modelsByModule = filteredModels?.reduce((acc, model) => {
    const modules = model.metadata_?.modules || ['Other'];
    modules.forEach(module => {
      if (!acc[module]) acc[module] = [];
      acc[module].push(model);
    });
    return acc;
  }, {} as Record<string, ObjectModel[]>);

  const selectedModelData = objectModels?.find(m => m.code === selectedModel);

  const handleModelClick = (modelCode: string) => setSelectedModel(modelCode);
  const handleViewFullDetails = (modelCode: string) => navigate(`/object-model/${modelCode}`);

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-full">
        <RefreshCw className="w-8 h-8 text-alpha-500 animate-spin" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-4 rounded-xl bg-red-500/10 border border-red-500/30 text-red-400">
        Failed to load object models. Please check if the metadata service is running.
      </div>
    );
  }

  const leftPanel = (
    <div className="h-full flex flex-col">
      {/* Header */}
      <div className="p-4 border-b theme-border">
        <div className="flex items-center gap-2 mb-4">
          <GitBranch className="w-6 h-6 text-alpha-500" />
          <h2 className="text-xl font-bold theme-text-title">Object Models</h2>
        </div>
        
        {/* Search */}
        <div className="relative">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 theme-text-muted" />
          <input
            type="text"
            placeholder="Search object models..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-10 pr-4 py-2 rounded-xl theme-card-bg border theme-border theme-text text-sm focus:outline-none focus:ring-2 focus:ring-alpha-500"
          />
        </div>
        
        <p className="text-xs theme-text-muted mt-2">{filteredModels?.length || 0} object models</p>
      </div>

      {/* Models List */}
      <div className="flex-1 overflow-auto">
        {modelsByModule && Object.entries(modelsByModule).map(([module, models]) => (
          <div key={module}>
            <div className="px-4 py-2 theme-card-bg border-b theme-border">
              <span className="text-sm font-semibold text-alpha-500">{module}</span>
            </div>
            <div className="divide-y theme-border">
              {models.map((model) => (
                <button
                  key={model.code}
                  onClick={() => handleModelClick(model.code)}
                  className={cn(
                    "w-full px-4 py-3 text-left hover:bg-alpha-faded-50 dark:hover:bg-alpha-faded-900 transition-colors",
                    selectedModel === model.code && "bg-alpha-500/10 border-l-2 border-alpha-500"
                  )}
                >
                  <div className="flex items-center gap-2">
                    <Database className="w-4 h-4 theme-text-muted flex-shrink-0" />
                    <span className="text-sm font-medium theme-text truncate">
                      {model.display_name || model.name}
                    </span>
                  </div>
                  {model.description && (
                    <p className="text-xs theme-text-muted mt-1 truncate pl-6">{model.description}</p>
                  )}
                </button>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );

  const rightPanel = selectedModelData ? (
    <div className="h-full overflow-auto p-6 space-y-6">
      {/* Header */}
      <div className="flex items-start justify-between">
        <div>
          <h2 className="text-2xl font-bold theme-text-title">
            {selectedModelData.display_name || selectedModelData.name}
          </h2>
          <p className="text-sm theme-text-muted mt-1">{selectedModelData.description}</p>
        </div>
        <span className="px-2 py-1 rounded-full text-xs theme-card-bg border theme-border theme-text-muted">
          {selectedModelData.code}
        </span>
      </div>

      {/* Modules */}
      {selectedModelData.metadata_?.modules && selectedModelData.metadata_.modules.length > 0 && (
        <div>
          <h3 className="text-sm font-medium theme-text-muted mb-2">Used in Modules</h3>
          <div className="flex flex-wrap gap-2">
            {selectedModelData.metadata_.modules.map((module) => (
              <span key={module} className="px-2 py-1 rounded-full text-xs border theme-border theme-text">
                {module}
              </span>
            ))}
          </div>
        </div>
      )}

      <div className="border-t theme-border" />

      {/* Technical Details */}
      <Card>
        <CardContent className="p-4 space-y-3">
          <h3 className="font-semibold theme-text-title">Technical Details</h3>
          <div className="grid grid-cols-2 gap-4">
            <div>
              <p className="text-xs theme-text-muted">Table Name</p>
              <p className="text-sm font-mono theme-text">{selectedModelData.table_name}</p>
            </div>
            <div>
              <p className="text-xs theme-text-muted">Schema</p>
              <p className="text-sm font-mono theme-text">
                {typeof selectedModelData.table_schema === 'string' ? selectedModelData.table_schema : 'public'}
              </p>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Relationships Table */}
      {selectedModelData.schema_definition && (() => {
        const relationships = parseRelationships(selectedModelData.schema_definition, selectedModelData.code);
        return relationships.length > 0 && (
          <Card>
            <CardContent className="p-4">
              <h3 className="font-semibold theme-text-title mb-3">Relationships ({relationships.length})</h3>
              <div className="overflow-x-auto">
                <table className="w-full text-sm">
                  <thead>
                    <tr className="border-b theme-border">
                      <th className="px-3 py-2 text-left theme-text-muted font-medium">From</th>
                      <th className="px-3 py-2 text-center theme-text-muted font-medium">Direction</th>
                      <th className="px-3 py-2 text-left theme-text-muted font-medium">To</th>
                      <th className="px-3 py-2 text-left theme-text-muted font-medium">Type</th>
                      <th className="px-3 py-2 text-left theme-text-muted font-medium">Cardinality</th>
                      <th className="px-3 py-2 text-left theme-text-muted font-medium">Relationship</th>
                    </tr>
                  </thead>
                  <tbody>
                    {relationships.map((rel, index) => (
                      <tr key={index} className="border-b theme-border hover:bg-alpha-faded-50 dark:hover:bg-alpha-faded-900">
                        <td className="px-3 py-2 font-medium theme-text">{rel.from}</td>
                        <td className="px-3 py-2 text-center">
                          {rel.direction === 'forward' && <ArrowRight className="w-4 h-4 theme-text-muted inline" />}
                          {rel.direction === 'backward' && <ArrowLeft className="w-4 h-4 theme-text-muted inline" />}
                          {rel.direction === 'bidirectional' && <ArrowLeftRight className="w-4 h-4 theme-text-muted inline" />}
                        </td>
                        <td className="px-3 py-2 font-medium theme-text">{rel.to}</td>
                        <td className="px-3 py-2">
                          <span className={cn(
                            "px-2 py-0.5 rounded-full text-xs border",
                            rel.type === 'composition' && "bg-red-500/20 text-red-400 border-red-500/30",
                            rel.type === 'aggregation' && "bg-amber-500/20 text-amber-400 border-amber-500/30",
                            rel.type === 'generalization' && "bg-blue-500/20 text-blue-400 border-blue-500/30",
                            rel.type === 'dependency' && "bg-purple-500/20 text-purple-400 border-purple-500/30",
                            rel.type === 'association' && "bg-gray-500/20 theme-text-muted border-gray-500/30"
                          )}>
                            {rel.type}
                          </span>
                        </td>
                        <td className="px-3 py-2 font-mono text-xs theme-text-muted">{rel.cardinality || '-'}</td>
                        <td className="px-3 py-2 theme-text-muted">{rel.label || '-'}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </CardContent>
          </Card>
        );
      })()}

      {/* UML Diagram */}
      {selectedModelData.schema_definition && (
        <Card>
          <CardContent className="p-4">
            <h3 className="font-semibold theme-text-title mb-3">Entity Relationships Diagram</h3>
            <div className="p-4 rounded-xl theme-card-bg border theme-border">
              <ObjectModelDiagram
                schemaDefinition={selectedModelData.schema_definition}
                highlightEntity={selectedModelData.code}
              />
            </div>
          </CardContent>
        </Card>
      )}

      {/* View Full Details */}
      <button
        onClick={() => handleViewFullDetails(selectedModelData.code)}
        className="text-sm text-alpha-500 hover:underline"
      >
        View Full Details →
      </button>
    </div>
  ) : (
    <div className="h-full flex items-center justify-center">
      <div className="text-center">
        <GitBranch className="w-16 h-16 mx-auto theme-text-muted opacity-30 mb-4" />
        <p className="text-lg theme-text-muted">Select an object model to view details</p>
      </div>
    </div>
  );

  return (
    <div className="h-full">
      <ResizableSplitPanel
        leftPanel={leftPanel}
        rightPanel={rightPanel}
        defaultLeftWidth={50}
        minLeftWidth={30}
      />
    </div>
  );
}
