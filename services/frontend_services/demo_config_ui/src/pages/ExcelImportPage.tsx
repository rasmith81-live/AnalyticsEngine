import React, { useState, useRef } from 'react';
import {
  Box,
  Typography,
  Paper,
  Button,
  Grid,
  Card,
  CardContent,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Alert,
  AlertTitle,
  LinearProgress,
  Chip,
  Stack,
  Tabs,
  Tab,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Accordion,
  AccordionSummary,
  AccordionDetails,
  TextField,
  IconButton
} from '@mui/material';
import {
  CloudUpload as UploadIcon,
  CheckCircle as CheckIcon,
  Error as ErrorIcon,
  Description as FileIcon,
  Save as SaveIcon,
  Warning as WarningIcon,
  AccountTree as ValueChainIcon,
  Folder as ModuleIcon,
  Category as EntityIcon,
  Link as RelationshipIcon,
  ExpandMore as ExpandMoreIcon,
  Analytics as KPIIcon,
  Add as AddIcon
} from '@mui/icons-material';
import { metadataIngestionApi } from '../api/metadataIngestionApi';
import ImportItemMenu from '../components/ImportItemMenu';

interface ImportError {
  row: number;
  column: string;
  message: string;
  data: any;
}

interface DuplicateWarning {
  kpi: {
    Name: string;
    Code: string;
    [key: string]: any;
  };
  matches: Array<{
    score: number;
    kpi: {
      name: string;
      code: string;
      [key: string]: any;
    };
  }>;
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

  // Helper to update relationships when ontology items change
  const updateRelationshipsForRename = (oldName: string, newName: string) => {
    if (!importResult?.ontology_sync?.relationships_created) return;
    const updatedRelationships = importResult.ontology_sync.relationships_created.map(rel => {
      // Relationships are in format "KPI_NAME -> target"
      const parts = rel.split(' -> ');
      if (parts[1] === oldName) {
        return `${parts[0]} -> ${newName}`;
      }
      return rel;
    });
    setImportResult({
      ...importResult,
      ontology_sync: { ...importResult.ontology_sync, relationships_created: updatedRelationships }
    });
  };

  const updateRelationshipsForDelete = (deletedName: string) => {
    if (!importResult?.ontology_sync?.relationships_created) return;
    const updatedRelationships = importResult.ontology_sync.relationships_created.filter(rel => {
      const parts = rel.split(' -> ');
      return parts[1] !== deletedName;
    });
    setImportResult({
      ...importResult,
      ontology_sync: { ...importResult.ontology_sync, relationships_created: updatedRelationships }
    });
  };

  // Add new ontology items - replaces old value chain/module relationships for ALL KPIs
  const handleAddValueChain = () => {
    if (!newValueChain.trim() || !importResult?.ontology_sync) return;
    const vcName = newValueChain.trim();
    const updatedVCs = [...(importResult.ontology_sync.value_chains_created || []), vcName];
    
    // Use allKpiCodes for full list, fallback to preview
    const allKpis = importResult.allKpiCodes || importResult.preview.map(kpi => kpi.Code || kpi.Name);
    const kpiCodes = new Set(allKpis);
    
    // Remove old value chain relationships for KPIs, keep module relationships
    const existingRelationships = importResult.ontology_sync.relationships_created || [];
    
    // Filter out KPI -> old_value_chain relationships (keep KPI -> module relationships)
    const filteredRelationships = existingRelationships.filter(rel => {
      const parts = rel.split(' -> ');
      const fromCode = parts[0];
      const toCode = parts[1];
      // Keep if it's not a KPI, or if the target is a module (in modules_created)
      const isKpiRelationship = kpiCodes.has(fromCode);
      const isModuleTarget = (importResult.ontology_sync?.modules_created || []).includes(toCode);
      return !isKpiRelationship || isModuleTarget;
    });
    
    // Create new relationships from ALL KPIs to this value chain
    const newRelationships = allKpis.map(code => `${code} -> ${vcName}`);
    
    setImportResult({
      ...importResult,
      ontology_sync: { 
        ...importResult.ontology_sync, 
        value_chains_created: updatedVCs,
        relationships_created: [...filteredRelationships, ...newRelationships]
      }
    });
    setNewValueChain('');
  };

  const handleAddModule = () => {
    if (!newModule.trim() || !importResult?.ontology_sync) return;
    const modName = newModule.trim();
    const updatedMods = [...(importResult.ontology_sync.modules_created || []), modName];
    
    // Use allKpiCodes for full list, fallback to preview
    const allKpis = importResult.allKpiCodes || importResult.preview.map(kpi => kpi.Code || kpi.Name);
    const kpiCodes = new Set(allKpis);
    
    // Remove old module relationships for KPIs, keep value chain relationships
    const existingRelationships = importResult.ontology_sync.relationships_created || [];
    
    // Filter out KPI -> old_module relationships (keep KPI -> value_chain relationships)
    const filteredRelationships = existingRelationships.filter(rel => {
      const parts = rel.split(' -> ');
      const fromCode = parts[0];
      const toCode = parts[1];
      // Keep if it's not a KPI, or if the target is a value chain (in value_chains_created)
      const isKpiRelationship = kpiCodes.has(fromCode);
      const isValueChainTarget = (importResult.ontology_sync?.value_chains_created || []).includes(toCode);
      return !isKpiRelationship || isValueChainTarget;
    });
    
    // Create new relationships from ALL KPIs to this module
    const newRelationships = allKpis.map(code => `${code} -> ${modName}`);
    
    setImportResult({
      ...importResult,
      ontology_sync: { 
        ...importResult.ontology_sync, 
        modules_created: updatedMods,
        relationships_created: [...filteredRelationships, ...newRelationships]
      }
    });
    setNewModule('');
  };

  const handleAddEntity = () => {
    if (!newEntity.trim() || !importResult?.ontology_sync) return;
    const entityName = newEntity.trim();
    const updatedEntities = [...(importResult.ontology_sync.entities_created || []), entityName];
    
    // Entities don't automatically get relationships - they're inferred from formulas
    setImportResult({
      ...importResult,
      ontology_sync: { ...importResult.ontology_sync, entities_created: updatedEntities }
    });
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

  const handleDragOver = (event: React.DragEvent<HTMLDivElement>) => {
    event.preventDefault();
  };

  const handleUpload = async () => {
    if (!file) {
      console.log('No file selected');
      return;
    }

    console.log('Starting upload for file:', file.name);
    setUploading(true);
    setUploadError(null);
    
    try {
      console.log('Calling metadataIngestionApi.uploadExcel...');
      const result = await metadataIngestionApi.uploadExcel(file);
      console.log('Upload successful:', result);
      setImportResult(result);
    } catch (error: any) {
      console.error('Upload failed:', error);
      const errorMessage = error?.response?.data?.detail || error?.message || 'Upload failed. Please try again.';
      setUploadError(errorMessage);
    } finally {
      setUploading(false);
    }
  };

  const handleCommit = async () => {
    if (!importResult) return;

    setCommitting(true);
    try {
      // Pass edited ontology data to commit
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
      console.log('Starting AI enrichment for import:', importResult.importId);
      const result = await metadataIngestionApi.enrichImport(importResult.importId);
      console.log('AI enrichment successful:', result);
      
      // Update import result with enriched data
      setImportResult({
        ...importResult,
        preview: result.preview,
        ontology_sync: result.ontology_sync,
        allKpiCodes: result.allKpiCodes,
      });
    } catch (error: any) {
      console.error('AI enrichment failed:', error);
      const errorMessage = error?.response?.data?.detail || error?.message || 'AI enrichment failed. Please try again.';
      setEnrichError(errorMessage);
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
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        KPI Bulk Import
      </Typography>
      <Typography variant="body1" color="text.secondary" paragraph>
        Upload Excel (.xlsx) or CSV files to define KPIs in bulk. The processor will validate formulas and object references.
      </Typography>

      {/* Success Message */}
      {commitSuccess !== null && (
        <Box sx={{ mb: 3 }}>
          <Alert severity="success" sx={{ mb: 2 }}>
            <AlertTitle>Import Successful</AlertTitle>
            Successfully imported {commitSuccess} KPI definitions from <strong>{lastImportedFileName}</strong> into the metadata repository.
          </Alert>
          <Button
            variant="contained"
            startIcon={<UploadIcon />}
            onClick={handleReset}
            fullWidth
          >
            Upload Another File
          </Button>
        </Box>
      )}

      {/* Upload Error */}
      {uploadError && (
        <Alert severity="error" sx={{ mb: 3 }} onClose={() => setUploadError(null)}>
          <AlertTitle>Upload Failed</AlertTitle>
          {uploadError}
        </Alert>
      )}

      {/* File Upload Area */}
      {!importResult && !commitSuccess && (
        <Paper
          sx={{
            p: 5,
            border: '2px dashed',
            borderColor: file ? 'primary.main' : 'grey.300',
            bgcolor: file ? 'primary.main' + '08' : 'grey.50',
            textAlign: 'center',
            cursor: 'pointer',
            transition: 'all 0.2s',
            '&:hover': {
              borderColor: 'primary.main',
              bgcolor: 'action.hover'
            }
          }}
          onDrop={handleDrop}
          onDragOver={handleDragOver}
          onClick={() => fileInputRef.current?.click()}
        >
          <input
            type="file"
            hidden
            ref={fileInputRef}
            onChange={handleFileSelect}
            accept=".xlsx,.xls,.csv"
          />
          
          {file ? (
            <Box>
              <FileIcon sx={{ fontSize: 60, color: 'primary.main', mb: 2 }} />
              <Typography variant="h6">{file.name}</Typography>
              <Typography variant="body2" color="text.secondary">
                {(file.size / 1024).toFixed(1)} KB
              </Typography>
              <Stack direction="row" spacing={2} justifyContent="center" sx={{ mt: 3 }}>
                <Button 
                  variant="contained" 
                  onClick={(e) => { e.stopPropagation(); handleUpload(); }}
                  disabled={uploading}
                >
                  {uploading ? 'Processing...' : 'Analyze File'}
                </Button>
                <Button 
                  variant="outlined" 
                  color="error" 
                  onClick={(e) => { e.stopPropagation(); handleReset(); }}
                  disabled={uploading}
                >
                  Remove
                </Button>
              </Stack>
              {uploading && <LinearProgress sx={{ mt: 3, maxWidth: 300, mx: 'auto' }} />}
            </Box>
          ) : (
            <Box>
              <UploadIcon sx={{ fontSize: 60, color: 'text.secondary', mb: 2 }} />
              <Typography variant="h6" gutterBottom>
                Drag & Drop or Click to Upload
              </Typography>
              <Typography variant="body2" color="text.secondary">
                Supported formats: .xlsx, .csv
              </Typography>
            </Box>
          )}
        </Paper>
      )}

      {/* Validation Results */}
      {importResult && (
        <Box sx={{ mt: 3 }}>
          <Grid container spacing={3} sx={{ mb: 3 }}>
            <Grid item xs={12} md={3}>
              <Card>
                <CardContent sx={{ textAlign: 'center' }}>
                  <Typography color="text.secondary" gutterBottom>Total Rows</Typography>
                  <Typography variant="h4">{importResult.totalRows}</Typography>
                </CardContent>
              </Card>
            </Grid>
            <Grid item xs={12} md={3}>
              <Card sx={{ bgcolor: 'success.light', color: 'success.contrastText' }}>
                <CardContent sx={{ textAlign: 'center' }}>
                  <Typography color="inherit" gutterBottom>Valid Definitions</Typography>
                  <Typography variant="h4">{importResult.validRows}</Typography>
                  <CheckIcon sx={{ mt: 1, opacity: 0.8 }} />
                </CardContent>
              </Card>
            </Grid>
            <Grid item xs={12} md={3}>
              <Card sx={{ bgcolor: importResult.duplicates.length > 0 ? 'warning.light' : 'grey.100', color: importResult.duplicates.length > 0 ? 'warning.contrastText' : 'text.primary' }}>
                <CardContent sx={{ textAlign: 'center' }}>
                  <Typography color="inherit" gutterBottom>Duplicates</Typography>
                  <Typography variant="h4">{importResult.duplicates.length}</Typography>
                  {importResult.duplicates.length > 0 && <WarningIcon sx={{ mt: 1, opacity: 0.8 }} />}
                </CardContent>
              </Card>
            </Grid>
            <Grid item xs={12} md={3}>
              <Card sx={{ bgcolor: importResult.errors.length > 0 ? 'error.light' : 'grey.100', color: importResult.errors.length > 0 ? 'error.contrastText' : 'text.primary' }}>
                <CardContent sx={{ textAlign: 'center' }}>
                  <Typography color="inherit" gutterBottom>Errors Found</Typography>
                  <Typography variant="h4">{importResult.errors.length}</Typography>
                  {importResult.errors.length > 0 && <ErrorIcon sx={{ mt: 1, opacity: 0.8 }} />}
                </CardContent>
              </Card>
            </Grid>
          </Grid>

          {/* AI Enrichment Error */}
          {enrichError && (
            <Alert severity="error" sx={{ mb: 2 }} onClose={() => setEnrichError(null)}>
              <AlertTitle>AI Enrichment Failed</AlertTitle>
              {enrichError}
            </Alert>
          )}

          {/* AI Enrichment Progress */}
          {enriching && (
            <Alert severity="info" sx={{ mb: 2 }}>
              <AlertTitle>AI Enrichment in Progress</AlertTitle>
              Extracting entities, value chains, and modules using AI. This may take a few minutes...
              <LinearProgress sx={{ mt: 1 }} />
            </Alert>
          )}

          {/* Action Buttons */}
          <Box sx={{ display: 'flex', justifyContent: 'flex-end', gap: 2, mb: 3 }}>
            <Button variant="outlined" onClick={handleReset}>Cancel</Button>
            <Button 
              variant="outlined" 
              color="secondary" 
              onClick={handleEnrich}
              disabled={enriching || committing || importResult.enriched}
            >
              {importResult.enriched ? 'Analysis Complete' : (enriching ? 'Enriching...' : '✨ Enrich with AI (Optional)')}
            </Button>
            <Button 
              variant="contained" 
              color="primary" 
              startIcon={<SaveIcon />}
              onClick={handleCommit}
              disabled={committing || enriching || importResult.validRows === 0}
            >
              {committing ? 'Importing...' : `Import ${importResult.validRows} Valid KPIs`}
            </Button>
          </Box>

          {/* Tabs for KPIs and Ontology */}
          <Paper sx={{ mb: 3 }}>
            <Box sx={{ p: 2, borderBottom: 1, borderColor: 'divider', display: 'flex', alignItems: 'center', gap: 2, bgcolor: 'grey.50' }}>
               <FileIcon color="primary" />
               <Typography variant="subtitle1" fontWeight="bold">
                 {file?.name}
               </Typography>
               <Chip label="Ready for Import" size="small" color="success" variant="outlined" sx={{ ml: 'auto' }} />
            </Box>
            <Tabs value={activeTab} onChange={(_, v) => setActiveTab(v)} sx={{ borderBottom: 1, borderColor: 'divider' }}>
              <Tab icon={<KPIIcon />} label={`KPIs (${importResult.validRows})`} iconPosition="start" />
              <Tab 
                icon={<ValueChainIcon />} 
                label={`Ontology (${(importResult.ontology_sync?.value_chains_created?.length || 0) + (importResult.ontology_sync?.modules_created?.length || 0) + (importResult.ontology_sync?.entities_created?.length || 0)})`} 
                iconPosition="start" 
              />
              <Tab 
                icon={<RelationshipIcon />} 
                label={`Relationships (${importResult.ontology_sync?.relationships_created?.length || 0})`} 
                iconPosition="start" 
              />
            </Tabs>

            {/* Tab 0: KPIs */}
            {activeTab === 0 && (
              <Box sx={{ p: 2 }}>
                <Typography variant="h6" gutterBottom>KPI Preview (First 20)</Typography>
                <Alert severity="info" sx={{ mb: 2 }}>
                  <strong>Formula Description</strong> shows the original text. <strong>Math Expression</strong> shows the parsed formula for the calculation engine.
                </Alert>
                <TableContainer>
                  <Table size="small">
                    <TableHead>
                      <TableRow>
                        <TableCell>Name</TableCell>
                        <TableCell>Formula Description</TableCell>
                        <TableCell>Math Expression</TableCell>
                        <TableCell>Entities</TableCell>
                        <TableCell width={50}></TableCell>
                      </TableRow>
                    </TableHead>
                    <TableBody>
                      {importResult.preview.map((row, idx) => (
                        <TableRow key={idx}>
                          <TableCell>{row.Name}</TableCell>
                          <TableCell sx={{ fontSize: '0.85rem', maxWidth: 250 }}>{row.Formula}</TableCell>
                          <TableCell sx={{ fontFamily: 'monospace', fontSize: '0.85rem', color: 'primary.main', bgcolor: 'grey.50' }}>
                            {row.Metadata?.decomposition?.math_expression || row.MathExpression || '-'}
                          </TableCell>
                          <TableCell>
                            <Stack direction="row" spacing={0.5} flexWrap="wrap" useFlexGap>
                              {(row.Metadata?.decomposition?.formula_entities || row.RequiredObjects || []).map((entity: string, i: number) => (
                                <Chip key={i} label={entity} size="small" color="success" variant="outlined" sx={{ fontSize: '0.7rem' }} />
                              ))}
                              {!(row.Metadata?.decomposition?.formula_entities?.length || row.RequiredObjects?.length) && (
                                <Typography variant="caption" color="text.secondary">-</Typography>
                              )}
                            </Stack>
                          </TableCell>
                          <TableCell>
                            <ImportItemMenu
                              name={row.Name}
                              onRename={(newName) => {
                                const updatedPreview = [...importResult.preview];
                                updatedPreview[idx] = { ...row, Name: newName };
                                setImportResult({ ...importResult, preview: updatedPreview });
                              }}
                              onDelete={() => {
                                const updatedPreview = importResult.preview.filter((_, i) => i !== idx);
                                setImportResult({ 
                                  ...importResult, 
                                  preview: updatedPreview,
                                  validRows: importResult.validRows - 1
                                });
                              }}
                            />
                          </TableCell>
                        </TableRow>
                      ))}
                    </TableBody>
                  </Table>
                </TableContainer>
              </Box>
            )}

            {/* Tab 1: Ontology (Value Chains, Modules, Entities) */}
            {activeTab === 1 && (
              <Box sx={{ p: 2 }}>
                <Alert severity="info" sx={{ mb: 2 }}>
                  Add, edit, or delete ontology items below. Changes will update the Relationships tab automatically.
                </Alert>
                {importResult.ontology_sync ? (
                  <Grid container spacing={2}>
                    {/* Value Chains */}
                    <Grid item xs={12} md={4}>
                      <Accordion defaultExpanded>
                        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                          <ValueChainIcon sx={{ mr: 1, color: 'primary.main' }} />
                          <Typography fontWeight="bold">
                            Value Chains ({importResult.ontology_sync.value_chains_created?.length || 0})
                          </Typography>
                        </AccordionSummary>
                        <AccordionDetails>
                          <Box sx={{ display: 'flex', gap: 1, mb: 1 }}>
                            <TextField
                              size="small"
                              placeholder="Add value chain..."
                              value={newValueChain}
                              onChange={(e) => setNewValueChain(e.target.value)}
                              onKeyPress={(e) => e.key === 'Enter' && handleAddValueChain()}
                              fullWidth
                            />
                            <IconButton color="primary" onClick={handleAddValueChain} disabled={!newValueChain.trim()}>
                              <AddIcon />
                            </IconButton>
                          </Box>
                          {importResult.ontology_sync.value_chains_created?.length > 0 ? (
                            <List dense>
                              {importResult.ontology_sync.value_chains_created.map((vc, idx) => (
                                <ListItem key={idx} secondaryAction={
                                  <ImportItemMenu
                                    name={vc}
                                    onRename={(newName) => {
                                      const oldName = importResult.ontology_sync!.value_chains_created[idx];
                                      const updated = [...importResult.ontology_sync!.value_chains_created];
                                      updated[idx] = newName;
                                      setImportResult({
                                        ...importResult,
                                        ontology_sync: { ...importResult.ontology_sync!, value_chains_created: updated }
                                      });
                                      updateRelationshipsForRename(oldName, newName);
                                    }}
                                    onDelete={() => {
                                      const deletedName = importResult.ontology_sync!.value_chains_created[idx];
                                      const updated = importResult.ontology_sync!.value_chains_created.filter((_, i) => i !== idx);
                                      setImportResult({
                                        ...importResult,
                                        ontology_sync: { ...importResult.ontology_sync!, value_chains_created: updated }
                                      });
                                      updateRelationshipsForDelete(deletedName);
                                    }}
                                  />
                                }>
                                  <ListItemIcon><ValueChainIcon fontSize="small" color="primary" /></ListItemIcon>
                                  <ListItemText primary={vc} />
                                </ListItem>
                              ))}
                            </List>
                          ) : (
                            <Typography variant="body2" color="text.secondary">No value chains - add one above</Typography>
                          )}
                        </AccordionDetails>
                      </Accordion>
                    </Grid>

                    {/* Modules */}
                    <Grid item xs={12} md={4}>
                      <Accordion defaultExpanded>
                        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                          <ModuleIcon sx={{ mr: 1, color: 'warning.main' }} />
                          <Typography fontWeight="bold">
                            Modules ({importResult.ontology_sync.modules_created?.length || 0})
                          </Typography>
                        </AccordionSummary>
                        <AccordionDetails>
                          <Box sx={{ display: 'flex', gap: 1, mb: 1 }}>
                            <TextField
                              size="small"
                              placeholder="Add module..."
                              value={newModule}
                              onChange={(e) => setNewModule(e.target.value)}
                              onKeyPress={(e) => e.key === 'Enter' && handleAddModule()}
                              fullWidth
                            />
                            <IconButton color="warning" onClick={handleAddModule} disabled={!newModule.trim()}>
                              <AddIcon />
                            </IconButton>
                          </Box>
                          {importResult.ontology_sync.modules_created?.length > 0 ? (
                            <List dense>
                              {importResult.ontology_sync.modules_created.map((mod, idx) => (
                                <ListItem key={idx} secondaryAction={
                                  <ImportItemMenu
                                    name={mod}
                                    onRename={(newName) => {
                                      const oldName = importResult.ontology_sync!.modules_created[idx];
                                      const updated = [...importResult.ontology_sync!.modules_created];
                                      updated[idx] = newName;
                                      setImportResult({
                                        ...importResult,
                                        ontology_sync: { ...importResult.ontology_sync!, modules_created: updated }
                                      });
                                      updateRelationshipsForRename(oldName, newName);
                                    }}
                                    onDelete={() => {
                                      const deletedName = importResult.ontology_sync!.modules_created[idx];
                                      const updated = importResult.ontology_sync!.modules_created.filter((_, i) => i !== idx);
                                      setImportResult({
                                        ...importResult,
                                        ontology_sync: { ...importResult.ontology_sync!, modules_created: updated }
                                      });
                                      updateRelationshipsForDelete(deletedName);
                                    }}
                                  />
                                }>
                                  <ListItemIcon><ModuleIcon fontSize="small" color="warning" /></ListItemIcon>
                                  <ListItemText primary={mod} />
                                </ListItem>
                              ))}
                            </List>
                          ) : (
                            <Typography variant="body2" color="text.secondary">No modules - add one above</Typography>
                          )}
                        </AccordionDetails>
                      </Accordion>
                    </Grid>

                    {/* Entities */}
                    <Grid item xs={12} md={4}>
                      <Accordion defaultExpanded>
                        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                          <EntityIcon sx={{ mr: 1, color: 'success.main' }} />
                          <Typography fontWeight="bold">
                            Entities ({importResult.ontology_sync.entities_created?.length || 0})
                          </Typography>
                        </AccordionSummary>
                        <AccordionDetails>
                          <Box sx={{ display: 'flex', gap: 1, mb: 1 }}>
                            <TextField
                              size="small"
                              placeholder="Add entity..."
                              value={newEntity}
                              onChange={(e) => setNewEntity(e.target.value)}
                              onKeyPress={(e) => e.key === 'Enter' && handleAddEntity()}
                              fullWidth
                            />
                            <IconButton color="success" onClick={handleAddEntity} disabled={!newEntity.trim()}>
                              <AddIcon />
                            </IconButton>
                          </Box>
                          {importResult.ontology_sync.entities_created?.length > 0 ? (
                            <List dense>
                              {importResult.ontology_sync.entities_created.map((entity, idx) => (
                                <ListItem key={idx} secondaryAction={
                                  <ImportItemMenu
                                    name={entity}
                                    onRename={(newName) => {
                                      const oldName = importResult.ontology_sync!.entities_created[idx];
                                      const updated = [...importResult.ontology_sync!.entities_created];
                                      updated[idx] = newName;
                                      setImportResult({
                                        ...importResult,
                                        ontology_sync: { ...importResult.ontology_sync!, entities_created: updated }
                                      });
                                      updateRelationshipsForRename(oldName, newName);
                                    }}
                                    onDelete={() => {
                                      const deletedName = importResult.ontology_sync!.entities_created[idx];
                                      const updated = importResult.ontology_sync!.entities_created.filter((_, i) => i !== idx);
                                      setImportResult({
                                        ...importResult,
                                        ontology_sync: { ...importResult.ontology_sync!, entities_created: updated }
                                      });
                                      updateRelationshipsForDelete(deletedName);
                                    }}
                                  />
                                }>
                                  <ListItemIcon><EntityIcon fontSize="small" color="success" /></ListItemIcon>
                                  <ListItemText primary={entity} />
                                </ListItem>
                              ))}
                            </List>
                          ) : (
                            <Typography variant="body2" color="text.secondary">No entities - add one above</Typography>
                          )}
                        </AccordionDetails>
                      </Accordion>
                    </Grid>
                  </Grid>
                ) : (
                  <Alert severity="info">Ontology extraction data not available</Alert>
                )}
              </Box>
            )}

            {/* Tab 2: Relationships */}
            {activeTab === 2 && (
              <Box sx={{ p: 2 }}>
                {importResult.ontology_sync && importResult.ontology_sync.relationships_created && importResult.ontology_sync.relationships_created.length > 0 ? (
                  <TableContainer>
                    <Table size="small">
                      <TableHead>
                        <TableRow>
                          <TableCell>From</TableCell>
                          <TableCell>Relationship</TableCell>
                          <TableCell>To</TableCell>
                          <TableCell width={50}></TableCell>
                        </TableRow>
                      </TableHead>
                      <TableBody>
                        {importResult.ontology_sync.relationships_created.map((rel, idx) => {
                          const parts = rel.split(' -> ');
                          return (
                            <TableRow key={idx}>
                              <TableCell>
                                <Chip label={parts[0]} size="small" color="primary" variant="outlined" />
                              </TableCell>
                              <TableCell>
                                <RelationshipIcon sx={{ color: 'grey.500' }} fontSize="small" />
                              </TableCell>
                              <TableCell>
                                <Chip label={parts[1] || rel} size="small" color="secondary" variant="outlined" />
                              </TableCell>
                              <TableCell>
                                <ImportItemMenu
                                  name={rel}
                                  onRename={(newName) => {
                                    const updated = [...importResult.ontology_sync!.relationships_created];
                                    updated[idx] = newName;
                                    setImportResult({
                                      ...importResult,
                                      ontology_sync: { ...importResult.ontology_sync!, relationships_created: updated }
                                    });
                                  }}
                                  onDelete={() => {
                                    const updated = importResult.ontology_sync!.relationships_created.filter((_, i) => i !== idx);
                                    setImportResult({
                                      ...importResult,
                                      ontology_sync: { ...importResult.ontology_sync!, relationships_created: updated }
                                    });
                                  }}
                                />
                              </TableCell>
                            </TableRow>
                          );
                        })}
                      </TableBody>
                    </Table>
                  </TableContainer>
                ) : (
                  <Alert severity="info">No relationships identified in this import</Alert>
                )}
              </Box>
            )}
          </Paper>

          {/* Duplicates Warning Table */}
          {importResult.duplicates.length > 0 && (
            <Paper sx={{ mb: 3, p: 2, border: '1px solid', borderColor: 'warning.light', bgcolor: 'warning.light', bgOpacity: 0.1 }}>
              <Typography variant="h6" color="warning.dark" gutterBottom sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                <WarningIcon /> Potential Duplicates Detected
              </Typography>
              <Typography variant="body2" paragraph>
                The following new KPIs look similar to existing ones. They will still be imported if you proceed.
              </Typography>
              <TableContainer component={Paper} elevation={0}>
                <Table size="small">
                  <TableHead>
                    <TableRow>
                      <TableCell>New KPI Name</TableCell>
                      <TableCell>Similar To (Existing)</TableCell>
                      <TableCell>Similarity Score</TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {importResult.duplicates.map((dup, idx) => (
                      <TableRow key={idx}>
                        <TableCell sx={{ fontWeight: 'bold' }}>{dup.kpi.Name}</TableCell>
                        <TableCell>
                          {dup.matches.map((m, i) => (
                            <div key={i}>{m.kpi.name} ({m.kpi.code})</div>
                          ))}
                        </TableCell>
                        <TableCell>
                          {dup.matches.map((m, i) => (
                            <div key={i}>{m.score.toFixed(1)}%</div>
                          ))}
                        </TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </TableContainer>
            </Paper>
          )}

          {/* Error Table */}
          {importResult.errors.length > 0 && (
            <Paper sx={{ mb: 3, p: 2, border: '1px solid', borderColor: 'error.light' }}>
              <Typography variant="h6" color="error" gutterBottom sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                <ErrorIcon /> Validation Errors
              </Typography>
              <TableContainer>
                <Table size="small">
                  <TableHead>
                    <TableRow>
                      <TableCell>Row</TableCell>
                      <TableCell>Column</TableCell>
                      <TableCell>Issue</TableCell>
                      <TableCell>Data</TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {importResult.errors.map((error, idx) => (
                      <TableRow key={idx} sx={{ bgcolor: 'error.main', opacity: 0.1 }}>
                        <TableCell>{error.row}</TableCell>
                        <TableCell>{error.column}</TableCell>
                        <TableCell>{error.message}</TableCell>
                        <TableCell sx={{ fontFamily: 'monospace', fontSize: '0.8rem' }}>
                          {JSON.stringify(error.data)}
                        </TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </TableContainer>
            </Paper>
          )}

        </Box>
      )}
    </Box>
  );
}
