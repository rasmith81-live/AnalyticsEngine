import { useState, useEffect } from 'react';
import {
  Box,
  Typography,
  Paper,
  Tabs,
  Tab,
  Grid,
  Card,
  CardContent,
  Button,
  TextField,
  IconButton,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Chip,
  CircularProgress,
  Alert,
  Snackbar
} from '@mui/material';
import {
  Edit as EditIcon,
  Delete as DeleteIcon,
  Business as ValueChainIcon,
  Category as ModuleIcon,
  Refresh as RefreshIcon
} from '@mui/icons-material';
import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8090/api/v1/metadata';

interface ValueChain {
  code: string;
  name: string;
  description?: string;
  domain?: string;
  metadata_?: Record<string, any>;
}

interface Module {
  code: string;
  name: string;
  description?: string;
  process_type?: string;
  metadata_?: Record<string, any>;
}

interface TabPanelProps {
  children?: React.ReactNode;
  index: number;
  value: number;
}

function TabPanel(props: TabPanelProps) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`ontology-tabpanel-${index}`}
      aria-labelledby={`ontology-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          {children}
        </Box>
      )}
    </div>
  );
}

export default function OntologyManagerPage() {
  const [tabValue, setTabValue] = useState(0);
  const [valueChains, setValueChains] = useState<ValueChain[]>([]);
  const [modules, setModules] = useState<Module[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [snackbar, setSnackbar] = useState<{open: boolean, message: string, severity: 'success' | 'error'}>({open: false, message: '', severity: 'success'});

  // Edit Dialog State
  const [editDialog, setEditDialog] = useState<{open: boolean, type: 'valueChain' | 'module', item: any}>({open: false, type: 'valueChain', item: null});
  const [editForm, setEditForm] = useState({name: '', description: ''});

  // Fetch data on mount
  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    setLoading(true);
    setError(null);
    try {
      const [vcRes, modRes] = await Promise.all([
        axios.get(`${BASE_URL}/definitions/value_chain_pattern_definition`, { params: { limit: 100 } }),
        axios.get(`${BASE_URL}/definitions/business_process_definition`, { params: { limit: 100 } })
      ]);
      setValueChains(vcRes.data || []);
      setModules(modRes.data || []);
    } catch (err: any) {
      setError(err.message || 'Failed to fetch data');
    } finally {
      setLoading(false);
    }
  };

  const handleTabChange = (_: React.SyntheticEvent, newValue: number) => {
    setTabValue(newValue);
  };

  const handleEdit = (type: 'valueChain' | 'module', item: any) => {
    setEditForm({ name: item.name || '', description: item.description || '' });
    setEditDialog({ open: true, type, item });
  };

  const handleSaveEdit = async () => {
    const { type, item } = editDialog;
    const kind = type === 'valueChain' ? 'value_chain_pattern_definition' : 'business_process_definition';
    
    try {
      const updatedData = { ...item, name: editForm.name, description: editForm.description };
      await axios.put(`${BASE_URL}/definitions/${kind}/${item.code}`, updatedData, {
        params: { changed_by: 'admin' }
      });
      
      setSnackbar({ open: true, message: `${type === 'valueChain' ? 'Value Chain' : 'Module'} updated successfully`, severity: 'success' });
      setEditDialog({ open: false, type: 'valueChain', item: null });
      fetchData(); // Refresh data
    } catch (err: any) {
      setSnackbar({ open: true, message: `Failed to update: ${err.message}`, severity: 'error' });
    }
  };

  const handleDelete = async (type: 'valueChain' | 'module', code: string, name: string) => {
    if (!window.confirm(`Are you sure you want to delete "${name}"?`)) return;
    
    const kind = type === 'valueChain' ? 'value_chain_pattern_definition' : 'business_process_definition';
    
    try {
      await axios.delete(`${BASE_URL}/definitions/${kind}/${code}`, {
        params: { deleted_by: 'admin' }
      });
      
      setSnackbar({ open: true, message: `${type === 'valueChain' ? 'Value Chain' : 'Module'} deleted successfully`, severity: 'success' });
      fetchData(); // Refresh data
    } catch (err: any) {
      setSnackbar({ open: true, message: `Failed to delete: ${err.message}`, severity: 'error' });
    }
  };

  if (loading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '50vh' }}>
        <CircularProgress />
      </Box>
    );
  }

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
        <Typography variant="h4">
          Ontology Studio
        </Typography>
        <Button variant="outlined" startIcon={<RefreshIcon />} onClick={fetchData}>
          Refresh
        </Button>
      </Box>

      {error && (
        <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>
      )}

      <Paper sx={{ width: '100%', mb: 2 }}>
        <Tabs value={tabValue} onChange={handleTabChange} aria-label="ontology tabs">
          <Tab icon={<ValueChainIcon />} label="Value Chains" />
          <Tab icon={<ModuleIcon />} label="Modules" />
        </Tabs>
      </Paper>

      {/* Value Chains Tab */}
      <TabPanel value={tabValue} index={0}>
        <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
          Manage value chains - click edit to rename or delete to remove.
        </Typography>
        <Grid container spacing={3}>
          {valueChains.length === 0 ? (
            <Grid item xs={12}>
              <Alert severity="info">No value chains found.</Alert>
            </Grid>
          ) : (
            valueChains.map((vc) => (
              <Grid item xs={12} md={6} lg={4} key={vc.code}>
                <Card variant="outlined">
                  <CardContent>
                    <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 1 }}>
                      <Box>
                        <Typography variant="h6">{vc.name}</Typography>
                        <Typography variant="caption" color="text.secondary">
                          Code: {vc.code}
                        </Typography>
                      </Box>
                      <Box>
                        <IconButton size="small" onClick={() => handleEdit('valueChain', vc)} title="Edit">
                          <EditIcon fontSize="small" />
                        </IconButton>
                        <IconButton size="small" onClick={() => handleDelete('valueChain', vc.code, vc.name)} color="error" title="Delete">
                          <DeleteIcon fontSize="small" />
                        </IconButton>
                      </Box>
                    </Box>
                    {vc.description && (
                      <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
                        {vc.description}
                      </Typography>
                    )}
                    {vc.domain && (
                      <Chip label={vc.domain} size="small" sx={{ mt: 1 }} />
                    )}
                  </CardContent>
                </Card>
              </Grid>
            ))
          )}
        </Grid>
      </TabPanel>

      {/* Modules Tab */}
      <TabPanel value={tabValue} index={1}>
        <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
          Manage modules (business processes) - click edit to rename or delete to remove.
        </Typography>
        <Grid container spacing={3}>
          {modules.length === 0 ? (
            <Grid item xs={12}>
              <Alert severity="info">No modules found.</Alert>
            </Grid>
          ) : (
            modules.map((mod) => (
              <Grid item xs={12} md={6} lg={4} key={mod.code}>
                <Card variant="outlined">
                  <CardContent>
                    <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 1 }}>
                      <Box>
                        <Typography variant="h6">{mod.name}</Typography>
                        <Typography variant="caption" color="text.secondary">
                          Code: {mod.code}
                        </Typography>
                      </Box>
                      <Box>
                        <IconButton size="small" onClick={() => handleEdit('module', mod)} title="Edit">
                          <EditIcon fontSize="small" />
                        </IconButton>
                        <IconButton size="small" onClick={() => handleDelete('module', mod.code, mod.name)} color="error" title="Delete">
                          <DeleteIcon fontSize="small" />
                        </IconButton>
                      </Box>
                    </Box>
                    {mod.description && (
                      <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
                        {mod.description}
                      </Typography>
                    )}
                    {mod.metadata_?.value_chain && (
                      <Chip label={`Value Chain: ${mod.metadata_.value_chain}`} size="small" sx={{ mt: 1 }} variant="outlined" />
                    )}
                  </CardContent>
                </Card>
              </Grid>
            ))
          )}
        </Grid>
      </TabPanel>

      {/* Edit Dialog */}
      <Dialog open={editDialog.open} onClose={() => setEditDialog({...editDialog, open: false})} maxWidth="sm" fullWidth>
        <DialogTitle>
          Edit {editDialog.type === 'valueChain' ? 'Value Chain' : 'Module'}
        </DialogTitle>
        <DialogContent>
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2, mt: 1 }}>
            <TextField
              label="Name"
              value={editForm.name}
              onChange={(e) => setEditForm({ ...editForm, name: e.target.value })}
              fullWidth
              autoFocus
            />
            <TextField
              label="Description"
              value={editForm.description}
              onChange={(e) => setEditForm({ ...editForm, description: e.target.value })}
              fullWidth
              multiline
              rows={3}
            />
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setEditDialog({...editDialog, open: false})}>Cancel</Button>
          <Button variant="contained" onClick={handleSaveEdit}>Save</Button>
        </DialogActions>
      </Dialog>

      {/* Snackbar for notifications */}
      <Snackbar 
        open={snackbar.open} 
        autoHideDuration={4000} 
        onClose={() => setSnackbar({...snackbar, open: false})}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      >
        <Alert severity={snackbar.severity} onClose={() => setSnackbar({...snackbar, open: false})}>
          {snackbar.message}
        </Alert>
      </Snackbar>
    </Box>
  );
}
