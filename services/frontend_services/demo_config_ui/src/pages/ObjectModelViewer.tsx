import {
  ArrowLeft,
  GitBranch,
  Database,
  Link2,
  ArrowRight,
  ArrowLeftRight,
  RefreshCw,
} from 'lucide-react';
import { useParams, useNavigate, Link as RouterLink } from 'react-router-dom';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { cn } from '../lib/utils';
import { useObjectModels } from '../hooks/useObjectModelDetails';
import ObjectModelDiagram from '../components/ObjectModelDiagram';

export default function ObjectModelViewer() {
  const { modelCode } = useParams<{ modelCode: string }>();
  const navigate = useNavigate();

  const { data: objectModels, isLoading, error } = useObjectModels(
    modelCode ? [modelCode] : []
  );

  const model = objectModels?.[0];

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <RefreshCw className="w-8 h-8 text-alpha-500 animate-spin" />
      </div>
    );
  }

  if (error || !model) {
    return (
      <div className="p-6 space-y-4">
        <div className="p-4 rounded-xl bg-red-500/10 border border-red-500/30 text-red-400">
          Failed to load object model. The model may not exist or the metadata service is unavailable.
        </div>
        <button onClick={() => navigate(-1)} className="p-2 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800">
          <ArrowLeft className="w-5 h-5 theme-text-muted" />
        </button>
      </div>
    );
  }

  const parseSchema = (schema: string) => {
    const fields: Array<{ name: string; type: string; nullable: boolean }> = [];
    const relationships: Array<{ from: string; to: string; type: string; cardinality: string; label: string; direction: 'forward' | 'backward' | 'bidirectional' }> = [];

    if (!schema) return { fields, relationships };

    const lines = schema.split('\n');
    const associationPattern = /([A-Za-z0-9_]+)\s+"([^"]+)"\s+(--)\s+"([^"]+)"\s+([A-Za-z0-9_]+)\s*:\s*(.+?)(?:\s*>)?$/;
    const compositionPattern = /([A-Za-z0-9_]+)\s+"([^"]+)"\s+(\*--)\s+"([^"]+)"\s+([A-Za-z0-9_]+)\s*:\s*(.+?)(?:\s*>)?$/;
    const aggregationPattern = /([A-Za-z0-9_]+)\s+"([^"]+)"\s+(o--)\s+"([^"]+)"\s+([A-Za-z0-9_]+)\s*:\s*(.+?)(?:\s*>)?$/;
    const generalizationPattern = /([A-Za-z0-9_]+)\s+(--\|>)\s+([A-Za-z0-9_]+)/;

    for (const line of lines) {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith("'") || trimmed.startsWith('@')) continue;

      let match;
      let relType = 'association';
      let from = '', to = '', fromCard = '', toCard = '', label = '';
      
      if ((match = trimmed.match(compositionPattern))) {
        [, from, fromCard, , toCard, to, label] = match;
        relType = 'composition';
      } else if ((match = trimmed.match(aggregationPattern))) {
        [, from, fromCard, , toCard, to, label] = match;
        relType = 'aggregation';
      } else if ((match = trimmed.match(generalizationPattern))) {
        [, from, , to] = match;
        relType = 'generalization';
        label = 'inherits from';
      } else if ((match = trimmed.match(associationPattern))) {
        [, from, fromCard, , toCard, to, label] = match;
        relType = 'association';
      }
      
      if (match && (from === model?.code || to === model?.code)) {
        const direction: 'forward' | 'backward' | 'bidirectional' = 
          relType === 'generalization' ? (from === model?.code ? 'forward' : 'backward') : 'bidirectional';
        relationships.push({ from, to, type: relType, cardinality: fromCard && toCard ? `${fromCard} to ${toCard}` : '', label: label.trim(), direction });
      }
    }

    return { fields, relationships };
  };

  const { fields, relationships } = parseSchema(model.schema_definition || '');

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Breadcrumbs */}
      <nav className="flex items-center gap-2 text-sm">
        <RouterLink to="/" className="theme-text-muted hover:theme-text">Home</RouterLink>
        <span className="theme-text-muted">/</span>
        <RouterLink to="/config" className="theme-text-muted hover:theme-text">Configuration</RouterLink>
        <span className="theme-text-muted">/</span>
        <span className="theme-text">{model.display_name}</span>
      </nav>

      {/* Header */}
      <div className="flex items-center gap-4">
        <button onClick={() => navigate(-1)} className="p-2 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800">
          <ArrowLeft className="w-5 h-5 theme-text-muted" />
        </button>
        <div className="flex-1">
          <h1 className="text-3xl font-bold theme-text-title">{model.display_name}</h1>
          <div className="flex flex-wrap gap-2 mt-2">
            <span className="px-2 py-1 rounded-full text-xs bg-alpha-500/20 text-alpha-400 border border-alpha-500/30">{model.code}</span>
            <span className="px-2 py-1 rounded-full text-xs border theme-border theme-text-muted flex items-center gap-1">
              <Database className="w-3 h-3" />{model.table_name || 'No table'}
            </span>
            {model.metadata_?.modules && model.metadata_.modules.length > 0 && (
              <span className="px-2 py-1 rounded-full text-xs border theme-border theme-text-muted">
                {model.metadata_.modules.length} modules
              </span>
            )}
          </div>
        </div>
      </div>

      {/* Description */}
      {model.description && (
        <Card>
          <CardContent className="p-4">
            <p className="theme-text-muted">{model.description}</p>
          </CardContent>
        </Card>
      )}

      {/* UML Diagram */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <GitBranch className="w-5 h-5 theme-info-icon" />
            UML Class Diagram
          </CardTitle>
        </CardHeader>
        <CardContent>
          {model.schema_definition ? (
            <ObjectModelDiagram schemaDefinition={model.schema_definition} />
          ) : (
            <div className="p-4 rounded-xl bg-blue-500/10 border border-blue-500/30 text-blue-400">
              No schema definition available for this object model.
            </div>
          )}
        </CardContent>
      </Card>

      {/* Relationships */}
      {relationships.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Link2 className="w-5 h-5 theme-info-icon" />
              UML Relationships ({relationships.length})
            </CardTitle>
          </CardHeader>
          <CardContent>
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
      )}

      {/* Module Usage */}
      {model.metadata_?.modules && model.metadata_.modules.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle>Used in Modules</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex flex-wrap gap-2">
              {model.metadata_.modules.map((module: string) => (
                <span key={module} className="px-3 py-1 rounded-full text-sm border theme-border theme-text">
                  {module}
                </span>
              ))}
            </div>
          </CardContent>
        </Card>
      )}

      {/* Technical Details */}
      <Card>
        <CardHeader>
          <CardTitle>Technical Details</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div className="p-4 rounded-xl theme-card-bg border theme-border">
              <p className="text-xs theme-text-muted mb-1">Object Code</p>
              <p className="font-mono theme-text">{model.code}</p>
            </div>
            <div className="p-4 rounded-xl theme-card-bg border theme-border">
              <p className="text-xs theme-text-muted mb-1">Table Name</p>
              <p className="font-mono theme-text">{model.table_name || 'N/A'}</p>
            </div>
            <div className="p-4 rounded-xl theme-card-bg border theme-border">
              <p className="text-xs theme-text-muted mb-1">Fields Count</p>
              <p className="text-2xl font-bold theme-text-title">{fields.length}</p>
            </div>
            <div className="p-4 rounded-xl theme-card-bg border theme-border">
              <p className="text-xs theme-text-muted mb-1">Relationships</p>
              <p className="text-2xl font-bold theme-text-title">{relationships.length}</p>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Raw Schema */}
      {model.schema_definition && (
        <Card>
          <CardHeader>
            <CardTitle>Raw Schema Definition</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="p-4 rounded-xl bg-[#1a1a2e] border border-[#2a2a4a] overflow-auto max-h-[400px]">
              <pre className="text-sm font-mono text-gray-300 whitespace-pre-wrap">{model.schema_definition}</pre>
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
