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
  Stack
} from '@mui/material';
import {
  CloudUpload as UploadIcon,
  CheckCircle as CheckIcon,
  Error as ErrorIcon,
  Description as FileIcon,
  Save as SaveIcon,
  Warning as WarningIcon
} from '@mui/icons-material';
import { metadataIngestionApi } from '../api/metadataIngestionApi';

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

interface ImportResult {
  importId: string;
  totalRows: number;
  validRows: number;
  errors: ImportError[];
  preview: any[];
  duplicates: DuplicateWarning[];
}

export default function ExcelImportPage() {
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);
  const [importResult, setImportResult] = useState<ImportResult | null>(null);
  const [committing, setCommitting] = useState(false);
  const [commitSuccess, setCommitSuccess] = useState<number | null>(null);
  
  const fileInputRef = useRef<HTMLInputElement>(null);

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
    if (!file) return;

    setUploading(true);
    try {
      const result = await metadataIngestionApi.uploadExcel(file);
      setImportResult(result);
    } catch (error) {
      console.error('Upload failed:', error);
      // Handle error
    } finally {
      setUploading(false);
    }
  };

  const handleCommit = async () => {
    if (!importResult) return;

    setCommitting(true);
    try {
      const result = await metadataIngestionApi.commitImport(importResult.importId);
      if (result.success) {
        setCommitSuccess(result.count);
        setImportResult(null);
        setFile(null);
      }
    } catch (error) {
      console.error('Commit failed:', error);
    } finally {
      setCommitting(false);
    }
  };

  const handleReset = () => {
    setFile(null);
    setImportResult(null);
    setCommitSuccess(null);
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
        <Alert severity="success" sx={{ mb: 3 }} onClose={() => setCommitSuccess(null)}>
          <AlertTitle>Import Successful</AlertTitle>
          Successfully imported {commitSuccess} KPI definitions into the metadata repository.
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

          {/* Action Buttons */}
          <Box sx={{ display: 'flex', justifyContent: 'flex-end', gap: 2, mb: 3 }}>
            <Button variant="outlined" onClick={handleReset}>Cancel</Button>
            <Button 
              variant="contained" 
              color="primary" 
              startIcon={<SaveIcon />}
              onClick={handleCommit}
              disabled={committing || importResult.validRows === 0}
            >
              {committing ? 'Importing...' : `Import ${importResult.validRows} Valid KPIs`}
            </Button>
          </Box>

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

          {/* Preview Table */}
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>Preview (First 5 Valid Rows)</Typography>
            <TableContainer>
              <Table>
                <TableHead>
                  <TableRow>
                    <TableCell>Name</TableCell>
                    <TableCell>Formula</TableCell>
                    <TableCell>Unit</TableCell>
                    <TableCell>Owner</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {importResult.preview.map((row, idx) => (
                    <TableRow key={idx}>
                      <TableCell>{row.Name}</TableCell>
                      <TableCell sx={{ fontFamily: 'monospace' }}>{row.Formula}</TableCell>
                      <TableCell><Chip label={row.Unit} size="small" /></TableCell>
                      <TableCell>{row.Owner}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </TableContainer>
          </Paper>
        </Box>
      )}
    </Box>
  );
}
