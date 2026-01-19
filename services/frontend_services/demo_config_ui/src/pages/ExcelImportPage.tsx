import React, { useState, useRef } from 'react';
import {
  Upload,
  CheckCircle,
  XCircle,
  FileSpreadsheet,
  Save,
  AlertTriangle,
  GitBranch,
  Folder,
  Box as BoxIcon,
  Link2,
  ChevronDown,
  BarChart3,
  Plus,
  Sparkles,
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { cn } from '../lib/utils';
import { metadataIngestionApi } from '../api/metadataIngestionApi';
import ImportItemMenu from '../components/ImportItemMenu';

interface ImportError {
  row: number;
  column: string;
  message: string;
  data: any;
}

interface DuplicateWarning {
  kpi: { Name: string; Code: string; [key: string]: any };
  matches: Array<{ score: number; kpi: { name: string; code: string; [key: string]: any } }>;
}

interface OntologySync {
  value_chains_created: string[];
  modules_created: string[];
  entities_created: string[];
  relationships_created: string[];
  errors: string[];
}

interface ImportResult {
  importId: string;
  totalRows: number;
  validRows: number;
  errors: ImportError[];
  preview: any[];
  duplicates: DuplicateWarning[];
  ontology_sync?: OntologySync;
  allKpiCodes?: string[];
  enriched?: boolean;
}

function TabButton({ active, onClick, icon, children }: { active: boolean; onClick: () => void; icon: React.ReactNode; children: React.ReactNode }) {
  return (
    <button onClick={onClick} className={cn("flex items-center gap-2 px-4 py-3 text-sm font-medium transition-colors border-b-2", active ? "text-alpha-500 border-alpha-500" : "theme-text-muted border-transparent hover:theme-text")}>
      {icon}{children}
    </button>
  );
}

function AccordionSection({ title, icon, count, children, defaultOpen = true }: { title: string; icon: React.ReactNode; count: number; children: React.ReactNode; defaultOpen?: boolean }) {
  const [isOpen, setIsOpen] = useState(defaultOpen);
  return (
    <div className="rounded-xl border theme-border overflow-hidden">
      <button onClick={() => setIsOpen(!isOpen)} className="w-full p-4 flex items-center justify-between theme-card-bg hover:bg-alpha-faded-50 dark:hover:bg-alpha-faded-900 transition-colors">
        <div className="flex items-center gap-2">
          {icon}
          <span className="font-semibold theme-text-title">{title} ({count})</span>
        </div>
        <ChevronDown className={cn("w-4 h-4 theme-text-muted transition-transform", isOpen && "rotate-180")} />
      </button>
      {isOpen && <div className="p-4 border-t theme-border">{children}</div>}
    </div>
  );
}

export default function ExcelImportPage() {
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);
  const [importResult, setImportResult] = useState<ImportResult | null>(null);
  const [committing, setCommitting] = useState(false);
  const [commitSuccess, setCommitSuccess] = useState<number | null>(null);
  const [lastImportedFileName, setLastImportedFileName] = useState<string | null>(null);
  const [uploadError, setUploadError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState(0);
  const [newValueChain, setNewValueChain] = useState('');
  const [newModule, setNewModule] = useState('');
  const [newEntity, setNewEntity] = useState('');
  const [enriching, setEnriching] = useState(false);
  const [enrichError, setEnrichError] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const updateRelationshipsForRename = (oldName: string, newName: string) => {
    if (!importResult?.ontology_sync?.relationships_created) return;
    const updatedRelationships = importResult.ontology_sync.relationships_created.map(rel => {
      const parts = rel.split(' -> ');
      if (parts[1] === oldName) return `${parts[0]} -> ${newName}`;
      return rel;
    });
    setImportResult({ ...importResult, ontology_sync: { ...importResult.ontology_sync, relationships_created: updatedRelationships } });
  };

  const updateRelationshipsForDelete = (deletedName: string) => {
    if (!importResult?.ontology_sync?.relationships_created) return;
    const updatedRelationships = importResult.ontology_sync.relationships_created.filter(rel => {
      const parts = rel.split(' -> ');
      return parts[1] !== deletedName;
    });
    setImportResult({ ...importResult, ontology_sync: { ...importResult.ontology_sync, relationships_created: updatedRelationships } });
  };

  const handleAddValueChain = () => {
    if (!newValueChain.trim() || !importResult?.ontology_sync) return;
    const vcName = newValueChain.trim();
    const updatedVCs = [...(importResult.ontology_sync.value_chains_created || []), vcName];
    const existingVCs = new Set(importResult.ontology_sync.value_chains_created || []);
    const existingMods = importResult.ontology_sync.modules_created || [];
    const existingRelationships = importResult.ontology_sync.relationships_created || [];
    const modSet = new Set(existingMods);
    const filteredRelationships = existingRelationships.filter(rel => {
      const parts = rel.split(' -> ');
      return !(modSet.has(parts[0]) && existingVCs.has(parts[1]));
    });
    const newModuleRelationships = existingMods.map(mod => `${mod} -> ${vcName}`);
    setImportResult({ ...importResult, ontology_sync: { ...importResult.ontology_sync, value_chains_created: updatedVCs, relationships_created: [...filteredRelationships, ...newModuleRelationships] } });
    setNewValueChain('');
  };

  const handleAddModule = () => {
    if (!newModule.trim() || !importResult?.ontology_sync) return;
    const modName = newModule.trim();
    const updatedMods = [...(importResult.ontology_sync.modules_created || []), modName];
    const allKpis = importResult.allKpiCodes || importResult.preview.map(kpi => kpi.Code || kpi.Name);
    const existingMods = new Set(importResult.ontology_sync.modules_created || []);
    const existingVCs = importResult.ontology_sync.value_chains_created || [];
    const existingRelationships = importResult.ontology_sync.relationships_created || [];
    const filteredRelationships = existingRelationships.filter(rel => !existingMods.has(rel.split(' -> ')[0]));
    const newModuleToKpiRelationships = allKpis.map(code => `${modName} -> ${code}`);
    const newModuleToVCRelationships = existingVCs.map(vc => `${modName} -> ${vc}`);
    setImportResult({ ...importResult, ontology_sync: { ...importResult.ontology_sync, modules_created: updatedMods, relationships_created: [...filteredRelationships, ...newModuleToKpiRelationships, ...newModuleToVCRelationships] } });
    setNewModule('');
  };

  const handleAddEntity = () => {
    if (!newEntity.trim() || !importResult?.ontology_sync) return;
    const updatedEntities = [...(importResult.ontology_sync.entities_created || []), newEntity.trim()];
    setImportResult({ ...importResult, ontology_sync: { ...importResult.ontology_sync, entities_created: updatedEntities } });
    setNewEntity('');
  };

  const handleFileSelect = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files[0]) {
      setFile(event.target.files[0]);
      setImportResult(null);
      setCommitSuccess(null);
    }
  };

  const handleDrop = (event: React.DragEvent<HTMLDivElement>) => {
    event.preventDefault();
    if (event.dataTransfer.files && event.dataTransfer.files[0]) {
      setFile(event.dataTransfer.files[0]);
      setImportResult(null);
      setCommitSuccess(null);
    }
  };

  const handleUpload = async () => {
    if (!file) return;
    setUploading(true);
    setUploadError(null);
    try {
      const result = await metadataIngestionApi.uploadExcel(file);
      setImportResult(result);
    } catch (error: any) {
      setUploadError(error?.response?.data?.detail || error?.message || 'Upload failed. Please try again.');
    } finally {
      setUploading(false);
    }
  };

  const handleCommit = async () => {
    if (!importResult) return;
    setCommitting(true);
    try {
      const result = await metadataIngestionApi.commitImport(importResult.importId, importResult.ontology_sync);
      if (result.success) {
        setCommitSuccess(result.count);
        setLastImportedFileName(file?.name || 'Unknown File');
        setImportResult(null);
        setFile(null);
      }
    } catch (error) {
      console.error('Commit failed:', error);
    } finally {
      setCommitting(false);
    }
  };

  const handleEnrich = async () => {
    if (!importResult) return;
    setEnriching(true);
    setEnrichError(null);
    try {
      const result = await metadataIngestionApi.enrichImport(importResult.importId);
      setImportResult({ ...importResult, preview: result.preview, ontology_sync: result.ontology_sync, allKpiCodes: result.allKpiCodes });
    } catch (error: any) {
      setEnrichError(error?.response?.data?.detail || error?.message || 'AI enrichment failed.');
    } finally {
      setEnriching(false);
    }
  };

  const handleReset = () => {
    setFile(null);
    setImportResult(null);
    setCommitSuccess(null);
    setLastImportedFileName(null);
    setUploadError(null);
    setEnrichError(null);
    if (fileInputRef.current) fileInputRef.current.value = '';
  };

  return (
    <div className="space-y-6 animate-fade-in">
      <div>
        <h1 className="text-3xl font-bold theme-text-title tracking-wide">KPI Bulk Import</h1>
        <p className="theme-text-muted mt-1">Upload Excel (.xlsx) or CSV files to define KPIs in bulk. The processor will validate formulas and object references.</p>
      </div>

      {/* Success Message */}
      {commitSuccess !== null && (
        <div className="space-y-4">
          <div className="p-4 rounded-xl bg-green-500/10 border border-green-500/30">
            <div className="flex items-center gap-2 text-green-400 font-semibold mb-1">
              <CheckCircle className="w-5 h-5" /> Import Successful
            </div>
            <p className="text-sm text-green-400/80">Successfully imported {commitSuccess} KPI definitions from <strong>{lastImportedFileName}</strong> into the metadata repository.</p>
          </div>
          <Button onClick={handleReset} className="w-full"><Upload className="w-4 h-4 mr-2" />Upload Another File</Button>
        </div>
      )}

      {/* Upload Error */}
      {uploadError && (
        <div className="p-4 rounded-xl bg-red-500/10 border border-red-500/30">
          <div className="flex items-center gap-2 text-red-400 font-semibold mb-1">
            <XCircle className="w-5 h-5" /> Upload Failed
          </div>
          <p className="text-sm text-red-400/80">{uploadError}</p>
        </div>
      )}

      {/* File Upload Area */}
      {!importResult && !commitSuccess && (
        <div
          className={cn(
            "p-12 border-2 border-dashed rounded-2xl text-center cursor-pointer transition-all",
            file ? "border-alpha-500 bg-alpha-500/5" : "border-gray-600 hover:border-alpha-500 hover:bg-alpha-500/5"
          )}
          onDrop={handleDrop}
          onDragOver={(e) => e.preventDefault()}
          onClick={() => fileInputRef.current?.click()}
        >
          <input type="file" hidden ref={fileInputRef} onChange={handleFileSelect} accept=".xlsx,.xls,.csv" />
          {file ? (
            <div>
              <FileSpreadsheet className="w-16 h-16 mx-auto text-alpha-500 mb-4" />
              <h3 className="text-xl font-semibold theme-text-title">{file.name}</h3>
              <p className="text-sm theme-text-muted">{(file.size / 1024).toFixed(1)} KB</p>
              <div className="flex justify-center gap-3 mt-6">
                <Button onClick={(e) => { e.stopPropagation(); handleUpload(); }} disabled={uploading}>
                  {uploading ? 'Processing...' : 'Analyze File'}
                </Button>
                <Button variant="outline" onClick={(e) => { e.stopPropagation(); handleReset(); }} disabled={uploading}>
                  Remove
                </Button>
              </div>
              {uploading && <div className="mt-4 h-1 max-w-xs mx-auto rounded-full bg-alpha-faded-200 dark:bg-alpha-faded-800 overflow-hidden"><div className="h-full bg-alpha-500 animate-pulse" style={{ width: '60%' }} /></div>}
            </div>
          ) : (
            <div>
              <Upload className="w-16 h-16 mx-auto theme-text-muted mb-4" />
              <h3 className="text-xl font-semibold theme-text-title">Drag & Drop or Click to Upload</h3>
              <p className="text-sm theme-text-muted">Supported formats: .xlsx, .csv</p>
            </div>
          )}
        </div>
      )}

      {/* Validation Results */}
      {importResult && (
        <div className="space-y-6">
          {/* Stats Cards */}
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
            <Card><CardContent className="p-5 text-center"><p className="text-3xl font-bold theme-text-title">{importResult.totalRows}</p><p className="text-sm theme-text-muted">Total Rows</p></CardContent></Card>
            <Card className="bg-green-500/10 border-green-500/30"><CardContent className="p-5 text-center"><p className="text-3xl font-bold text-green-400">{importResult.validRows}</p><p className="text-sm text-green-400/80">Valid Definitions</p><CheckCircle className="w-5 h-5 mx-auto mt-2 text-green-400" /></CardContent></Card>
            <Card className={cn(importResult.duplicates.length > 0 ? "bg-amber-500/10 border-amber-500/30" : "")}><CardContent className="p-5 text-center"><p className={cn("text-3xl font-bold", importResult.duplicates.length > 0 ? "text-amber-400" : "theme-text-title")}>{importResult.duplicates.length}</p><p className={cn("text-sm", importResult.duplicates.length > 0 ? "text-amber-400/80" : "theme-text-muted")}>Duplicates</p>{importResult.duplicates.length > 0 && <AlertTriangle className="w-5 h-5 mx-auto mt-2 text-amber-400" />}</CardContent></Card>
            <Card className={cn(importResult.errors.length > 0 ? "bg-red-500/10 border-red-500/30" : "")}><CardContent className="p-5 text-center"><p className={cn("text-3xl font-bold", importResult.errors.length > 0 ? "text-red-400" : "theme-text-title")}>{importResult.errors.length}</p><p className={cn("text-sm", importResult.errors.length > 0 ? "text-red-400/80" : "theme-text-muted")}>Errors Found</p>{importResult.errors.length > 0 && <XCircle className="w-5 h-5 mx-auto mt-2 text-red-400" />}</CardContent></Card>
          </div>

          {/* Enrich Error */}
          {enrichError && <div className="p-4 rounded-xl bg-red-500/10 border border-red-500/30 text-red-400"><strong>AI Enrichment Failed:</strong> {enrichError}</div>}
          {enriching && <div className="p-4 rounded-xl bg-blue-500/10 border border-blue-500/30 text-blue-400"><strong>AI Enrichment in Progress</strong> - Extracting entities, value chains, and modules using AI...<div className="mt-2 h-1 rounded-full bg-blue-500/30 overflow-hidden"><div className="h-full bg-blue-500 animate-pulse" style={{ width: '60%' }} /></div></div>}

          {/* Action Buttons */}
          <div className="flex justify-end gap-3">
            <Button variant="outline" onClick={handleReset}>Cancel</Button>
            <Button variant="outline" onClick={handleEnrich} disabled={enriching || committing || importResult.enriched}>
              <Sparkles className="w-4 h-4 mr-2" />
              {importResult.enriched ? 'Analysis Complete' : (enriching ? 'Enriching...' : 'Enrich with AI')}
            </Button>
            <Button onClick={handleCommit} disabled={committing || enriching || importResult.validRows === 0}>
              <Save className="w-4 h-4 mr-2" />
              {committing ? 'Importing...' : `Import ${importResult.validRows} Valid KPIs`}
            </Button>
          </div>

          {/* Tabs */}
          <Card>
            <div className="p-4 border-b theme-border flex items-center gap-3">
              <FileSpreadsheet className="w-5 h-5 text-alpha-500" />
              <span className="font-semibold theme-text-title">{file?.name}</span>
              <span className="ml-auto px-2 py-0.5 rounded-full text-xs bg-green-500/20 text-green-400 border border-green-500/30">Ready for Import</span>
            </div>
            <div className="border-b theme-border">
              <div className="flex">
                <TabButton active={activeTab === 0} onClick={() => setActiveTab(0)} icon={<BarChart3 className="w-4 h-4" />}>KPIs ({importResult.validRows})</TabButton>
                <TabButton active={activeTab === 1} onClick={() => setActiveTab(1)} icon={<GitBranch className="w-4 h-4" />}>Ontology ({(importResult.ontology_sync?.value_chains_created?.length || 0) + (importResult.ontology_sync?.modules_created?.length || 0) + (importResult.ontology_sync?.entities_created?.length || 0)})</TabButton>
                <TabButton active={activeTab === 2} onClick={() => setActiveTab(2)} icon={<Link2 className="w-4 h-4" />}>Relationships ({importResult.ontology_sync?.relationships_created?.length || 0})</TabButton>
              </div>
            </div>

            {/* Tab 0: KPIs */}
            {activeTab === 0 && (
              <CardContent>
                <h3 className="font-semibold theme-text-title mb-2">KPI Preview (First 20)</h3>
                <div className="p-3 rounded-lg bg-blue-500/10 border border-blue-500/30 text-blue-400 text-sm mb-4">
                  <strong>Formula Description</strong> shows the original text. <strong>Math Expression</strong> shows the parsed formula for the calculation engine.
                </div>
                <div className="overflow-x-auto">
                  <table className="w-full text-sm">
                    <thead><tr className="border-b theme-border"><th className="px-3 py-2 text-left theme-text-muted font-medium">Name</th><th className="px-3 py-2 text-left theme-text-muted font-medium">Formula Description</th><th className="px-3 py-2 text-left theme-text-muted font-medium">Math Expression</th><th className="px-3 py-2 text-left theme-text-muted font-medium">Entities</th><th className="px-3 py-2 w-10"></th></tr></thead>
                    <tbody>
                      {importResult.preview.map((row, idx) => (
                        <tr key={idx} className="border-b theme-border">
                          <td className="px-3 py-2 theme-text">{row.Name}</td>
                          <td className="px-3 py-2 text-xs theme-text-muted max-w-[200px] truncate">{row.Formula}</td>
                          <td className="px-3 py-2 font-mono text-xs text-alpha-500 bg-alpha-faded-50 dark:bg-alpha-faded-900">{row.Metadata?.decomposition?.math_expression || row.MathExpression || '-'}</td>
                          <td className="px-3 py-2">
                            <div className="flex flex-wrap gap-1">
                              {(row.Metadata?.decomposition?.formula_entities || row.RequiredObjects || []).map((entity: string, i: number) => (
                                <span key={i} className="px-1.5 py-0.5 rounded text-xs bg-green-500/20 text-green-400 border border-green-500/30">{entity}</span>
                              ))}
                              {!(row.Metadata?.decomposition?.formula_entities?.length || row.RequiredObjects?.length) && <span className="text-xs theme-text-muted">-</span>}
                            </div>
                          </td>
                          <td className="px-3 py-2">
                            <ImportItemMenu name={row.Name} onRename={(newName) => { const updatedPreview = [...importResult.preview]; updatedPreview[idx] = { ...row, Name: newName }; setImportResult({ ...importResult, preview: updatedPreview }); }} onDelete={() => { const updatedPreview = importResult.preview.filter((_, i) => i !== idx); setImportResult({ ...importResult, preview: updatedPreview, validRows: importResult.validRows - 1 }); }} />
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </CardContent>
            )}

            {/* Tab 1: Ontology */}
            {activeTab === 1 && (
              <CardContent>
                <div className="p-3 rounded-lg bg-blue-500/10 border border-blue-500/30 text-blue-400 text-sm mb-4">Add, edit, or delete ontology items below. Changes will update the Relationships tab automatically.</div>
                {importResult.ontology_sync ? (
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <AccordionSection title="Value Chains" icon={<GitBranch className="w-4 h-4 text-alpha-500" />} count={importResult.ontology_sync.value_chains_created?.length || 0}>
                      <div className="flex gap-2 mb-3">
                        <input type="text" placeholder="Add value chain..." value={newValueChain} onChange={(e) => setNewValueChain(e.target.value)} onKeyPress={(e) => e.key === 'Enter' && handleAddValueChain()} className="flex-1 px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text text-sm focus:outline-none focus:ring-2 focus:ring-alpha-500" />
                        <button onClick={handleAddValueChain} disabled={!newValueChain.trim()} className="p-2 rounded-lg bg-alpha-500 text-white disabled:opacity-50"><Plus className="w-4 h-4" /></button>
                      </div>
                      {importResult.ontology_sync.value_chains_created?.length > 0 ? (
                        <div className="space-y-1">{importResult.ontology_sync.value_chains_created.map((vc, idx) => (
                          <div key={idx} className="flex items-center justify-between p-2 rounded-lg hover:bg-alpha-faded-50 dark:hover:bg-alpha-faded-900">
                            <div className="flex items-center gap-2"><GitBranch className="w-4 h-4 text-alpha-500" /><span className="text-sm theme-text">{vc}</span></div>
                            <ImportItemMenu name={vc} onRename={(newName) => { const oldName = importResult.ontology_sync!.value_chains_created[idx]; const updated = [...importResult.ontology_sync!.value_chains_created]; updated[idx] = newName; setImportResult({ ...importResult, ontology_sync: { ...importResult.ontology_sync!, value_chains_created: updated } }); updateRelationshipsForRename(oldName, newName); }} onDelete={() => { const deletedName = importResult.ontology_sync!.value_chains_created[idx]; const updated = importResult.ontology_sync!.value_chains_created.filter((_, i) => i !== idx); setImportResult({ ...importResult, ontology_sync: { ...importResult.ontology_sync!, value_chains_created: updated } }); updateRelationshipsForDelete(deletedName); }} />
                          </div>
                        ))}</div>
                      ) : <p className="text-sm theme-text-muted">No value chains - add one above</p>}
                    </AccordionSection>

                    <AccordionSection title="Modules" icon={<Folder className="w-4 h-4 text-amber-500" />} count={importResult.ontology_sync.modules_created?.length || 0}>
                      <div className="flex gap-2 mb-3">
                        <input type="text" placeholder="Add module..." value={newModule} onChange={(e) => setNewModule(e.target.value)} onKeyPress={(e) => e.key === 'Enter' && handleAddModule()} className="flex-1 px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text text-sm focus:outline-none focus:ring-2 focus:ring-amber-500" />
                        <button onClick={handleAddModule} disabled={!newModule.trim()} className="p-2 rounded-lg bg-amber-500 text-white disabled:opacity-50"><Plus className="w-4 h-4" /></button>
                      </div>
                      {importResult.ontology_sync.modules_created?.length > 0 ? (
                        <div className="space-y-1">{importResult.ontology_sync.modules_created.map((mod, idx) => (
                          <div key={idx} className="flex items-center justify-between p-2 rounded-lg hover:bg-alpha-faded-50 dark:hover:bg-alpha-faded-900">
                            <div className="flex items-center gap-2"><Folder className="w-4 h-4 text-amber-500" /><span className="text-sm theme-text">{mod}</span></div>
                            <ImportItemMenu name={mod} onRename={(newName) => { const oldName = importResult.ontology_sync!.modules_created[idx]; const updated = [...importResult.ontology_sync!.modules_created]; updated[idx] = newName; setImportResult({ ...importResult, ontology_sync: { ...importResult.ontology_sync!, modules_created: updated } }); updateRelationshipsForRename(oldName, newName); }} onDelete={() => { const deletedName = importResult.ontology_sync!.modules_created[idx]; const updated = importResult.ontology_sync!.modules_created.filter((_, i) => i !== idx); setImportResult({ ...importResult, ontology_sync: { ...importResult.ontology_sync!, modules_created: updated } }); updateRelationshipsForDelete(deletedName); }} />
                          </div>
                        ))}</div>
                      ) : <p className="text-sm theme-text-muted">No modules - add one above</p>}
                    </AccordionSection>

                    <AccordionSection title="Entities" icon={<BoxIcon className="w-4 h-4 text-green-500" />} count={importResult.ontology_sync.entities_created?.length || 0}>
                      <div className="flex gap-2 mb-3">
                        <input type="text" placeholder="Add entity..." value={newEntity} onChange={(e) => setNewEntity(e.target.value)} onKeyPress={(e) => e.key === 'Enter' && handleAddEntity()} className="flex-1 px-3 py-2 rounded-lg theme-card-bg border theme-border theme-text text-sm focus:outline-none focus:ring-2 focus:ring-green-500" />
                        <button onClick={handleAddEntity} disabled={!newEntity.trim()} className="p-2 rounded-lg bg-green-500 text-white disabled:opacity-50"><Plus className="w-4 h-4" /></button>
                      </div>
                      {importResult.ontology_sync.entities_created?.length > 0 ? (
                        <div className="space-y-1">{importResult.ontology_sync.entities_created.map((entity, idx) => (
                          <div key={idx} className="flex items-center justify-between p-2 rounded-lg hover:bg-alpha-faded-50 dark:hover:bg-alpha-faded-900">
                            <div className="flex items-center gap-2"><BoxIcon className="w-4 h-4 text-green-500" /><span className="text-sm theme-text">{entity}</span></div>
                            <ImportItemMenu name={entity} onRename={(newName) => { const oldName = importResult.ontology_sync!.entities_created[idx]; const updated = [...importResult.ontology_sync!.entities_created]; updated[idx] = newName; setImportResult({ ...importResult, ontology_sync: { ...importResult.ontology_sync!, entities_created: updated } }); updateRelationshipsForRename(oldName, newName); }} onDelete={() => { const deletedName = importResult.ontology_sync!.entities_created[idx]; const updated = importResult.ontology_sync!.entities_created.filter((_, i) => i !== idx); setImportResult({ ...importResult, ontology_sync: { ...importResult.ontology_sync!, entities_created: updated } }); updateRelationshipsForDelete(deletedName); }} />
                          </div>
                        ))}</div>
                      ) : <p className="text-sm theme-text-muted">No entities - add one above</p>}
                    </AccordionSection>
                  </div>
                ) : <div className="p-4 rounded-xl bg-blue-500/10 border border-blue-500/30 text-blue-400">Ontology extraction data not available</div>}
              </CardContent>
            )}

            {/* Tab 2: Relationships */}
            {activeTab === 2 && (
              <CardContent>
                {(importResult.ontology_sync?.relationships_created?.length ?? 0) > 0 ? (
                  <div className="overflow-x-auto">
                    <table className="w-full text-sm">
                      <thead><tr className="border-b theme-border"><th className="px-3 py-2 text-left theme-text-muted font-medium">From</th><th className="px-3 py-2 text-center theme-text-muted font-medium">Relationship</th><th className="px-3 py-2 text-left theme-text-muted font-medium">To</th><th className="px-3 py-2 w-10"></th></tr></thead>
                      <tbody>
                        {importResult.ontology_sync!.relationships_created.map((rel, idx) => {
                          const parts = rel.split(' -> ');
                          return (
                            <tr key={idx} className="border-b theme-border">
                              <td className="px-3 py-2"><span className="px-2 py-0.5 rounded-full text-xs bg-alpha-500/20 text-alpha-400 border border-alpha-500/30">{parts[0]}</span></td>
                              <td className="px-3 py-2 text-center"><Link2 className="w-4 h-4 theme-text-muted inline" /></td>
                              <td className="px-3 py-2"><span className="px-2 py-0.5 rounded-full text-xs bg-purple-500/20 text-purple-400 border border-purple-500/30">{parts[1] || rel}</span></td>
                              <td className="px-3 py-2"><ImportItemMenu name={rel} onRename={(newName) => { const updated = [...importResult.ontology_sync!.relationships_created]; updated[idx] = newName; setImportResult({ ...importResult, ontology_sync: { ...importResult.ontology_sync!, relationships_created: updated } }); }} onDelete={() => { const updated = importResult.ontology_sync!.relationships_created.filter((_, i) => i !== idx); setImportResult({ ...importResult, ontology_sync: { ...importResult.ontology_sync!, relationships_created: updated } }); }} /></td>
                            </tr>
                          );
                        })}
                      </tbody>
                    </table>
                  </div>
                ) : <div className="p-4 rounded-xl bg-blue-500/10 border border-blue-500/30 text-blue-400">No relationships identified in this import</div>}
              </CardContent>
            )}
          </Card>

          {/* Duplicates Warning */}
          {importResult.duplicates.length > 0 && (
            <Card className="border-amber-500/30 bg-amber-500/5">
              <CardHeader><CardTitle className="flex items-center gap-2 text-amber-400"><AlertTriangle className="w-5 h-5" />Potential Duplicates Detected</CardTitle></CardHeader>
              <CardContent>
                <p className="text-sm theme-text-muted mb-4">The following new KPIs look similar to existing ones. They will still be imported if you proceed.</p>
                <div className="overflow-x-auto">
                  <table className="w-full text-sm">
                    <thead><tr className="border-b theme-border"><th className="px-3 py-2 text-left theme-text-muted font-medium">New KPI Name</th><th className="px-3 py-2 text-left theme-text-muted font-medium">Similar To (Existing)</th><th className="px-3 py-2 text-left theme-text-muted font-medium">Similarity Score</th></tr></thead>
                    <tbody>
                      {importResult.duplicates.map((dup, idx) => (
                        <tr key={idx} className="border-b theme-border">
                          <td className="px-3 py-2 font-semibold theme-text">{dup.kpi.Name}</td>
                          <td className="px-3 py-2 theme-text-muted">{dup.matches.map((m, i) => <div key={i}>{m.kpi.name} ({m.kpi.code})</div>)}</td>
                          <td className="px-3 py-2 theme-text-muted">{dup.matches.map((m, i) => <div key={i}>{m.score.toFixed(1)}%</div>)}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </CardContent>
            </Card>
          )}

          {/* Errors */}
          {importResult.errors.length > 0 && (
            <Card className="border-red-500/30">
              <CardHeader><CardTitle className="flex items-center gap-2 text-red-400"><XCircle className="w-5 h-5" />Validation Errors</CardTitle></CardHeader>
              <CardContent>
                <div className="overflow-x-auto">
                  <table className="w-full text-sm">
                    <thead><tr className="border-b theme-border"><th className="px-3 py-2 text-left theme-text-muted font-medium">Row</th><th className="px-3 py-2 text-left theme-text-muted font-medium">Column</th><th className="px-3 py-2 text-left theme-text-muted font-medium">Issue</th><th className="px-3 py-2 text-left theme-text-muted font-medium">Data</th></tr></thead>
                    <tbody>
                      {importResult.errors.map((error, idx) => (
                        <tr key={idx} className="border-b theme-border bg-red-500/5">
                          <td className="px-3 py-2 theme-text">{error.row}</td>
                          <td className="px-3 py-2 theme-text">{error.column}</td>
                          <td className="px-3 py-2 theme-text">{error.message}</td>
                          <td className="px-3 py-2 font-mono text-xs theme-text-muted">{JSON.stringify(error.data)}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </CardContent>
            </Card>
          )}
        </div>
      )}
    </div>
  );
}
