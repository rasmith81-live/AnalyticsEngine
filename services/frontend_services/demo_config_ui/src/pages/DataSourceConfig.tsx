import { useState, useEffect } from 'react';
import {
  Typography,
  Paper,
  Box,
  Button,
  Grid,
  Card,
  CardContent,
  CardActions,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  MenuItem,
  Alert,
  CircularProgress,
  Chip,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Divider,
  Switch,
  FormControlLabel,
  FormControl,
  InputLabel,
  Select,
  SelectChangeEvent,
  Checkbox,
} from '@mui/material';
import {
  Add as AddIcon,
  Refresh as RefreshIcon,
  Storage as StorageIcon,
  Code as CodeIcon,
  Description as FileIcon,
  CheckCircle as CheckIcon,
  Error as ErrorIcon,
  Search as SearchIcon,
  Delete as DeleteIcon,
  Edit as EditIcon,
  AccessTime as TimeIcon,
} from '@mui/icons-material';
import { connectorApi, ConnectionProfile, TableDefinition } from '../api/connectorApi';

const CONNECTION_TYPES = [
  { value: 'sql_postgres', label: 'PostgreSQL', icon: <StorageIcon /> },
  { value: 'sql_mssql', label: 'SQL Server', icon: <StorageIcon /> },
  { value: 'rest_api', label: 'REST API', icon: <CodeIcon /> },
  { value: 'excel_file', label: 'Excel File', icon: <FileIcon /> },
];

export default function DataSourceConfig() {
  const [connections, setConnections] = useState<ConnectionProfile[]>([]);
  const [openDialog, setOpenDialog] = useState(false);
  const [testStatus, setTestStatus] = useState<Record<string, boolean | null>>({});
  const [testingConnection, setTestingConnection] = useState<string | null>(null);
  const [discoveringSchema, setDiscoveringSchema] = useState<string | null>(null);
  const [schemaResult, setSchemaResult] = useState<{ connectionId: string; tables: TableDefinition[] } | null>(null);
  const [openSchemaDialog, setOpenSchemaDialog] = useState(false);
  const [selectedTables, setSelectedTables] = useState<string[]>([]);

  const [editingId, setEditingId] = useState<string | null>(null);
  const [previewData, setPreviewData] = useState<{ tableName: string; rows: any[] } | null>(null);
  const [loadingPreview, setLoadingPreview] = useState<string | null>(null);

  const [newConnection, setNewConnection] = useState<Partial<ConnectionProfile>>({
    name: '',
    type: 'sql_postgres',
    host: 'localhost',
    port: 5432,
    username: '',
    password: '',
    database: '',
    api_url: '',
    file_path: '',
    schedule: {
      frequency: 'manual',
      active: false,
    },
    selected_tables: [],
  });

  // Mock initial load (replace with API call when list endpoint is available)
  useEffect(() => {
    // Ideally, we would fetch the list of connections here
    // For now, we rely on local state or manually added ones
  }, []);

  const handleCreateOrUpdateConnection = async () => {
    try {
      if (editingId) {
        // Update existing
        // In real app: await connectorApi.updateConnection(editingId, newConnection);
        setConnections(prev => prev.map(c => c.id === editingId ? { ...c, ...newConnection } as ConnectionProfile : c));
      } else {
        // Create new
        const id = `conn_${Date.now()}`;
        const profile: ConnectionProfile = {
          id,
          ...newConnection as any,
        };
        await connectorApi.createConnection(profile);
        setConnections([...connections, profile]);
      }
      
      setOpenDialog(false);
      resetForm();
    } catch (error) {
      console.error('Failed to save connection:', error);
      alert('Failed to save connection');
    }
  };

  const handleDeleteConnection = async (id: string) => {
    if (!window.confirm('Are you sure you want to delete this connection?')) return;
    try {
      // In real app: await connectorApi.deleteConnection(id);
      setConnections(prev => prev.filter(c => c.id !== id));
    } catch (error) {
      console.error('Failed to delete connection:', error);
      alert('Failed to delete connection');
    }
  };

  const resetForm = () => {
    setNewConnection({
      name: '',
      type: 'sql_postgres',
      host: 'localhost',
      port: 5432,
      username: '',
      password: '',
      database: '',
      api_url: '',
      file_path: '',
      schedule: {
        frequency: 'manual',
        active: false,
      },
      selected_tables: [],
    });
    setEditingId(null);
  };

  const handleEditConnection = (conn: ConnectionProfile) => {
    setNewConnection({
        ...conn,
        schedule: conn.schedule || { frequency: 'manual', active: false },
        selected_tables: conn.selected_tables || [],
    });
    setEditingId(conn.id);
    setOpenDialog(true);
  };

  const handleTestConnection = async (profile: ConnectionProfile) => {
    setTestingConnection(profile.id);
    try {
      const result = await connectorApi.testConnection(profile);
      setTestStatus((prev) => ({ ...prev, [profile.id]: result.success }));
    } catch (error) {
      console.error('Connection test failed:', error);
      setTestStatus((prev) => ({ ...prev, [profile.id]: false }));
    } finally {
      setTestingConnection(null);
    }
  };

  const handleDiscoverSchema = async (profile: ConnectionProfile) => {
    setDiscoveringSchema(profile.id);
    try {
      const tables = await connectorApi.discoverSchema(profile.id);
      setSchemaResult({ connectionId: profile.id, tables });
      setSelectedTables(profile.selected_tables || []);
      setOpenSchemaDialog(true);
    } catch (error) {
      console.error('Schema discovery failed:', error);
      alert('Schema discovery failed. Check connection settings.');
    } finally {
      setDiscoveringSchema(null);
    }
  };

  const handleToggleTable = (tableName: string) => {
    setSelectedTables(prev => {
      if (prev.includes(tableName)) {
        return prev.filter(t => t !== tableName);
      } else {
        return [...prev, tableName];
      }
    });
  };

  const handleSaveSchemaSelection = async () => {
    if (!schemaResult) return;
    try {
      const connectionId = schemaResult.connectionId;
      // Update local state first for immediate feedback
      setConnections(prev => prev.map(c => 
        c.id === connectionId ? { ...c, selected_tables: selectedTables } : c
      ));
      
      // In real app: await connectorApi.updateConnection(connectionId, { selected_tables: selectedTables });
      // leveraging the API we added
      await connectorApi.updateConnection(connectionId, { selected_tables: selectedTables });

      setOpenSchemaDialog(false);
    } catch (error) {
      console.error('Failed to save schema selection:', error);
      alert('Failed to save schema selection');
    }
  };

  const handlePreviewData = async (connectionId: string, tableName: string) => {
    setLoadingPreview(tableName);
    try {
      const rows = await connectorApi.previewData(connectionId, tableName, 5);
      setPreviewData({ tableName, rows });
    } catch (error) {
      console.error('Failed to preview data:', error);
      alert('Failed to preview data');
    } finally {
      setLoadingPreview(null);
    }
  };

  const renderConnectionForm = () => {
    return (
      <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2, mt: 1 }}>
        <TextField
          label="Connection Name"
          fullWidth
          value={newConnection.name}
          onChange={(e) => setNewConnection({ ...newConnection, name: e.target.value })}
        />
        <FormControl fullWidth>
          <InputLabel>Connection Type</InputLabel>
          <Select
            label="Connection Type"
            value={newConnection.type}
            onChange={(e: SelectChangeEvent) => setNewConnection({ ...newConnection, type: e.target.value as any })}
          >
            {CONNECTION_TYPES.map((type) => (
              <MenuItem key={type.value} value={type.value}>
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  {type.icon}
                  {type.label}
                </Box>
              </MenuItem>
            ))}
          </Select>
        </FormControl>

        {(newConnection.type === 'sql_postgres' || newConnection.type === 'sql_mssql') && (
          <>
            <Box sx={{ display: 'flex', gap: 2 }}>
              <TextField
                label="Host"
                fullWidth
                value={newConnection.host}
                onChange={(e) => setNewConnection({ ...newConnection, host: e.target.value })}
              />
              <TextField
                label="Port"
                type="number"
                sx={{ width: 120 }}
                value={newConnection.port}
                onChange={(e) => setNewConnection({ ...newConnection, port: parseInt(e.target.value) })}
              />
            </Box>
            <TextField
              label="Database Name"
              fullWidth
              value={newConnection.database}
              onChange={(e) => setNewConnection({ ...newConnection, database: e.target.value })}
            />
            <TextField
              label="Username"
              fullWidth
              value={newConnection.username}
              onChange={(e) => setNewConnection({ ...newConnection, username: e.target.value })}
            />
            <TextField
              label="Password"
              type="password"
              fullWidth
              value={newConnection.password}
              onChange={(e) => setNewConnection({ ...newConnection, password: e.target.value })}
            />
          </>
        )}

        {newConnection.type === 'rest_api' && (
          <TextField
            label="API Base URL"
            fullWidth
            value={newConnection.api_url}
            onChange={(e) => setNewConnection({ ...newConnection, api_url: e.target.value })}
          />
        )}

        {newConnection.type === 'excel_file' && (
          <TextField
            label="File Path"
            fullWidth
            helperText="Absolute path to the Excel file on the server"
            value={newConnection.file_path}
            onChange={(e) => setNewConnection({ ...newConnection, file_path: e.target.value })}
          />
        )}

        <Divider sx={{ my: 1 }} />
        
        <Box>
          <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
            <TimeIcon color="action" sx={{ mr: 1 }} />
            <Typography variant="subtitle1">Ingestion Schedule</Typography>
          </Box>
          
          <FormControlLabel
            control={
              <Switch
                checked={newConnection.schedule?.active || false}
                onChange={(e: React.ChangeEvent<HTMLInputElement>) => setNewConnection({
                  ...newConnection,
                  schedule: { ...(newConnection.schedule || { frequency: 'manual' }), active: e.target.checked }
                })}
              />
            }
            label="Enable Scheduled Ingestion"
          />

          {newConnection.schedule?.active && (
            <Box sx={{ mt: 2, display: 'flex', flexDirection: 'column', gap: 2, pl: 2, borderLeft: '2px solid #eee' }}>
              <FormControl fullWidth size="small">
                <InputLabel>Frequency</InputLabel>
                <Select
                  label="Frequency"
                  value={newConnection.schedule?.frequency || 'manual'}
                  onChange={(e: SelectChangeEvent) => setNewConnection({
                    ...newConnection,
                    schedule: { ...newConnection.schedule!, frequency: e.target.value as any }
                  })}
                >
                  <MenuItem value="manual">Manual Trigger Only</MenuItem>
                  <MenuItem value="daily">Daily</MenuItem>
                  <MenuItem value="weekly">Weekly</MenuItem>
                  <MenuItem value="custom">Custom Cron Expression</MenuItem>
                </Select>
              </FormControl>

              {(newConnection.schedule?.frequency === 'daily' || newConnection.schedule?.frequency === 'weekly') && (
                 <TextField
                   label="Time (HH:MM)"
                   type="time"
                   size="small"
                   fullWidth
                   InputLabelProps={{ shrink: true }}
                   value={newConnection.schedule?.time || '00:00'}
                   onChange={(e) => setNewConnection({
                     ...newConnection,
                     schedule: { ...newConnection.schedule!, time: e.target.value }
                   })}
                 />
              )}

              {newConnection.schedule?.frequency === 'custom' && (
                <TextField
                  label="Cron Expression"
                  size="small"
                  fullWidth
                  placeholder="0 0 * * *"
                  helperText="Standard cron format"
                  value={newConnection.schedule?.cron_expression || ''}
                  onChange={(e) => setNewConnection({
                    ...newConnection,
                    schedule: { ...newConnection.schedule!, cron_expression: e.target.value }
                  })}
                />
              )}
            </Box>
          )}
        </Box>
      </Box>
    );
  };

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3 }}>
        <Typography variant="h4">Data Source Configuration</Typography>
        <Button
          variant="contained"
          startIcon={<AddIcon />}
          onClick={() => {
            resetForm();
            setOpenDialog(true);
          }}
        >
          Add Data Source
        </Button>
      </Box>

      {connections.length === 0 ? (
        <Paper sx={{ p: 4, textAlign: 'center', color: 'text.secondary' }}>
          <Typography variant="h6">No data sources configured</Typography>
          <Typography>Add a connection to start ingesting data.</Typography>
        </Paper>
      ) : (
        <Grid container spacing={3}>
          {connections.map((conn) => (
            <Grid item xs={12} md={6} lg={4} key={conn.id}>
              <Card>
                <CardContent>
                  <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                      {CONNECTION_TYPES.find(t => t.value === conn.type)?.icon}
                      <Typography variant="h6">{conn.name}</Typography>
                    </Box>
                    <Chip
                      label={conn.type.replace('_', ' ').toUpperCase()}
                      size="small"
                      color="primary"
                      variant="outlined"
                    />
                  </Box>
                  <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
                    {conn.type.includes('sql') ? `${conn.host}:${conn.port} / ${conn.database}` : 
                     conn.type === 'rest_api' ? conn.api_url : conn.file_path}
                  </Typography>

                  {testStatus[conn.id] !== undefined && (
                    <Alert
                      severity={testStatus[conn.id] ? 'success' : 'error'}
                      sx={{ mt: 2, py: 0 }}
                      icon={testStatus[conn.id] ? <CheckIcon fontSize="inherit" /> : <ErrorIcon fontSize="inherit" />}
                    >
                      {testStatus[conn.id] ? 'Connection Successful' : 'Connection Failed'}
                    </Alert>
                  )}
                </CardContent>
                <CardActions sx={{ justifyContent: 'space-between' }}>
                  <Box>
                    <Button
                      size="small"
                      startIcon={<EditIcon />}
                      onClick={() => handleEditConnection(conn)}
                    >
                      Edit
                    </Button>
                    <Button
                      size="small"
                      color="error"
                      startIcon={<DeleteIcon />}
                      onClick={() => handleDeleteConnection(conn.id)}
                    >
                      Delete
                    </Button>
                  </Box>
                  <Box>
                    <Button
                      size="small"
                      startIcon={testingConnection === conn.id ? <CircularProgress size={16} /> : <RefreshIcon />}
                      onClick={() => handleTestConnection(conn)}
                      disabled={testingConnection === conn.id}
                    >
                      Test
                    </Button>
                    <Button
                      size="small"
                      startIcon={discoveringSchema === conn.id ? <CircularProgress size={16} /> : <SearchIcon />}
                      onClick={() => handleDiscoverSchema(conn)}
                      disabled={discoveringSchema === conn.id}
                    >
                      Schema
                    </Button>
                  </Box>
                </CardActions>
              </Card>
            </Grid>
          ))}
        </Grid>
      )}

      {/* Add Connection Dialog */}
      <Dialog open={openDialog} onClose={() => setOpenDialog(false)} maxWidth="sm" fullWidth>
        <DialogTitle>{editingId ? 'Edit Data Source' : 'Add New Data Source'}</DialogTitle>
        <DialogContent>
          {renderConnectionForm()}
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenDialog(false)}>Cancel</Button>
          <Button variant="contained" onClick={handleCreateOrUpdateConnection}>
            {editingId ? 'Save Changes' : 'Add Connection'}
          </Button>
        </DialogActions>
      </Dialog>

      {/* Schema Discovery Result Dialog */}
      <Dialog
        open={openSchemaDialog}
        onClose={() => setOpenSchemaDialog(false)}
        maxWidth="md"
        fullWidth
      >
        <DialogTitle>Discovered Schema</DialogTitle>
        <DialogContent>
          {schemaResult && (
            <Box sx={{ mt: 2 }}>
              {schemaResult.tables.length === 0 ? (
                <Typography>No tables or schema information found.</Typography>
              ) : (
                schemaResult.tables.map((table) => (
                  <Box key={table.name} sx={{ mb: 4 }}>
                    <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 1 }}>
                      <Box sx={{ display: 'flex', alignItems: 'center' }}>
                        <Checkbox 
                          checked={selectedTables.includes(table.name)}
                          onChange={() => handleToggleTable(table.name)}
                        />
                        <Typography variant="h6" color="primary">
                          Table: {table.name}
                        </Typography>
                      </Box>
                      <Button 
                        size="small" 
                        variant="outlined" 
                        onClick={() => handlePreviewData(schemaResult.connectionId, table.name)}
                        startIcon={loadingPreview === table.name ? <CircularProgress size={16} /> : undefined}
                        disabled={loadingPreview === table.name}
                      >
                        Preview Data
                      </Button>
                    </Box>
                    <TableContainer component={Paper} variant="outlined">
                      <Table size="small">
                        <TableHead>
                          <TableRow sx={{ bgcolor: 'action.hover' }}>
                            <TableCell>Column Name</TableCell>
                            <TableCell>Data Type</TableCell>
                            <TableCell align="center">Nullable</TableCell>
                            <TableCell align="center">Primary Key</TableCell>
                          </TableRow>
                        </TableHead>
                        <TableBody>
                          {table.columns.map((col) => (
                            <TableRow key={col.name}>
                              <TableCell>{col.name}</TableCell>
                              <TableCell>{col.data_type}</TableCell>
                              <TableCell align="center">{col.is_nullable ? 'Yes' : 'No'}</TableCell>
                              <TableCell align="center">{col.is_primary_key ? 'Yes' : '-'}</TableCell>
                            </TableRow>
                          ))}
                        </TableBody>
                      </Table>
                    </TableContainer>

                    {/* Data Preview Section */}
                    {previewData && previewData.tableName === table.name && (
                      <Box sx={{ mt: 2, p: 2, bgcolor: 'grey.50', borderRadius: 1 }}>
                        <Typography variant="subtitle2" gutterBottom>Data Preview (First 5 Rows)</Typography>
                        <TableContainer component={Paper} variant="outlined" sx={{ maxHeight: 200 }}>
                          <Table size="small" stickyHeader>
                            <TableHead>
                              <TableRow>
                                {Object.keys(previewData.rows[0] || {}).map(key => (
                                  <TableCell key={key}>{key}</TableCell>
                                ))}
                              </TableRow>
                            </TableHead>
                            <TableBody>
                              {previewData.rows.map((row, idx) => (
                                <TableRow key={idx}>
                                  {Object.values(row).map((val: any, i) => (
                                    <TableCell key={i}>{String(val)}</TableCell>
                                  ))}
                                </TableRow>
                              ))}
                            </TableBody>
                          </Table>
                        </TableContainer>
                      </Box>
                    )}
                  </Box>
                ))
              )}
            </Box>
          )}
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenSchemaDialog(false)}>Cancel</Button>
          <Button variant="contained" onClick={handleSaveSchemaSelection}>
            Save Selection ({selectedTables.length})
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
}
