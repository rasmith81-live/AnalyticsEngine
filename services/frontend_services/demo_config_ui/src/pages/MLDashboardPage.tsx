import { useState } from 'react';
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
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Chip,
  IconButton,
  TextField,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Stack,
  LinearProgress,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions
} from '@mui/material';
import {
  ModelTraining as ModelIcon,
  PlayArrow as RunIcon,
  Science as ExperimentIcon,
  Psychology as InferenceIcon,
  Add as AddIcon,
  MoreVert as MoreIcon,
  CheckCircle as SuccessIcon,
  Error as ErrorIcon,
  Schedule as PendingIcon
} from '@mui/icons-material';

// Mock Data
const MOCK_MODELS = [
  { id: 'mod_churn_v1', name: 'Customer Churn Predictor', version: '1.2.0', type: 'Classification', status: 'production', accuracy: '87.5%', lastTrained: '2023-12-10' },
  { id: 'mod_demand_v2', name: 'Demand Forecast', version: '2.1.0', type: 'Regression', status: 'staging', accuracy: '92.1%', lastTrained: '2023-12-15' },
  { id: 'mod_segment_v1', name: 'User Segmentation', version: '1.0.0', type: 'Clustering', status: 'archived', accuracy: '0.65 (Silhouette)', lastTrained: '2023-11-20' },
];

const MOCK_JOBS = [
  { id: 'job_101', model: 'Customer Churn Predictor', status: 'completed', duration: '45m', startedAt: '2023-12-18 09:00' },
  { id: 'job_102', model: 'Demand Forecast', status: 'running', progress: 65, duration: '1h 20m', startedAt: '2023-12-18 10:30' },
  { id: 'job_103', model: 'Inventory Opt', status: 'failed', duration: '5m', startedAt: '2023-12-18 11:15' },
];

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
      id={`ml-tabpanel-${index}`}
      aria-labelledby={`ml-tab-${index}`}
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

export default function MLDashboardPage() {
  const [tabValue, setTabValue] = useState(0);
  const [openTrainDialog, setOpenTrainDialog] = useState(false);
  const [inferenceInput, setInferenceInput] = useState('');
  const [inferenceResult, setInferenceResult] = useState<any>(null);

  const handleTabChange = (_: React.SyntheticEvent, newValue: number) => {
    setTabValue(newValue);
  };

  const handleInference = () => {
    // Mock inference
    setInferenceResult({
      prediction: 'High Risk',
      probability: 0.89,
      factors: ['Low Usage', 'Recent Support Ticket']
    });
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'production': return 'success';
      case 'staging': return 'warning';
      case 'archived': return 'default';
      case 'completed': return 'success';
      case 'running': return 'info';
      case 'failed': return 'error';
      default: return 'default';
    }
  };

  return (
    <Box>
      <Box sx={{ mb: 3, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <Box>
          <Typography variant="h4" gutterBottom>
            ML Model Registry
          </Typography>
          <Typography variant="body1" color="text.secondary">
            Manage, train, and deploy machine learning models.
          </Typography>
        </Box>
        <Button 
          variant="contained" 
          startIcon={<AddIcon />}
          onClick={() => setOpenTrainDialog(true)}
        >
          New Training Job
        </Button>
      </Box>

      <Paper sx={{ width: '100%', mb: 2 }}>
        <Tabs value={tabValue} onChange={handleTabChange}>
          <Tab icon={<ModelIcon />} label="Models" />
          <Tab icon={<ExperimentIcon />} label="Training Jobs" />
          <Tab icon={<InferenceIcon />} label="Inference Playground" />
        </Tabs>
      </Paper>

      {/* Models Tab */}
      <TabPanel value={tabValue} index={0}>
        <TableContainer component={Paper} variant="outlined">
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>Model Name</TableCell>
                <TableCell>Version</TableCell>
                <TableCell>Type</TableCell>
                <TableCell>Status</TableCell>
                <TableCell>Performance</TableCell>
                <TableCell>Last Trained</TableCell>
                <TableCell align="right">Actions</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {MOCK_MODELS.map((row) => (
                <TableRow key={row.id}>
                  <TableCell sx={{ fontWeight: 'bold' }}>{row.name}</TableCell>
                  <TableCell><Chip label={row.version} size="small" variant="outlined" /></TableCell>
                  <TableCell>{row.type}</TableCell>
                  <TableCell>
                    <Chip 
                      label={row.status.toUpperCase()} 
                      size="small" 
                      color={getStatusColor(row.status) as any} 
                    />
                  </TableCell>
                  <TableCell>{row.accuracy}</TableCell>
                  <TableCell>{row.lastTrained}</TableCell>
                  <TableCell align="right">
                    <IconButton size="small"><MoreIcon /></IconButton>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </TabPanel>

      {/* Training Jobs Tab */}
      <TabPanel value={tabValue} index={1}>
        <Grid container spacing={3}>
          {MOCK_JOBS.map((job) => (
            <Grid item xs={12} key={job.id}>
              <Card variant="outlined">
                <CardContent sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                  <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
                    {job.status === 'completed' && <SuccessIcon color="success" />}
                    {job.status === 'failed' && <ErrorIcon color="error" />}
                    {job.status === 'running' && <PendingIcon color="primary" className="spin" />}
                    
                    <Box>
                      <Typography variant="subtitle1">{job.model}</Typography>
                      <Typography variant="caption" color="text.secondary">ID: {job.id} • Started: {job.startedAt}</Typography>
                    </Box>
                  </Box>

                  <Box sx={{ width: '30%', mr: 4 }}>
                    {job.status === 'running' && (
                      <Box>
                        <Typography variant="caption" display="block" align="right" gutterBottom>
                          {job.progress}%
                        </Typography>
                        <LinearProgress variant="determinate" value={job.progress} />
                      </Box>
                    )}
                  </Box>

                  <Box>
                    <Chip label={job.status} color={getStatusColor(job.status) as any} size="small" sx={{ mr: 2 }} />
                    <Typography variant="caption" color="text.secondary">{job.duration}</Typography>
                  </Box>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      </TabPanel>

      {/* Inference Tab */}
      <TabPanel value={tabValue} index={2}>
        <Grid container spacing={3}>
          <Grid item xs={12} md={6}>
            <Paper sx={{ p: 3, height: '100%' }}>
              <Typography variant="h6" gutterBottom>Input Parameters</Typography>
              <FormControl fullWidth sx={{ mb: 3 }}>
                <InputLabel>Select Model</InputLabel>
                <Select defaultValue={MOCK_MODELS[0].id} label="Select Model">
                  {MOCK_MODELS.map(m => (
                    <MenuItem key={m.id} value={m.id}>{m.name} ({m.version})</MenuItem>
                  ))}
                </Select>
              </FormControl>
              
              <TextField
                label="Feature Vector (JSON)"
                multiline
                rows={8}
                fullWidth
                value={inferenceInput}
                onChange={(e) => setInferenceInput(e.target.value)}
                placeholder={'{\n  "age": 34,\n  "usage_score": 0.85,\n  "last_login_days": 2\n}'}
                sx={{ mb: 3, fontFamily: 'monospace' }}
              />
              
              <Button 
                variant="contained" 
                startIcon={<RunIcon />} 
                fullWidth 
                onClick={handleInference}
              >
                Run Prediction
              </Button>
            </Paper>
          </Grid>
          
          <Grid item xs={12} md={6}>
            <Paper sx={{ p: 3, height: '100%', bgcolor: 'grey.50' }}>
              <Typography variant="h6" gutterBottom>Prediction Result</Typography>
              
              {inferenceResult ? (
                <Box>
                  <Card variant="outlined" sx={{ mb: 3, bgcolor: 'background.paper' }}>
                    <CardContent sx={{ textAlign: 'center' }}>
                      <Typography color="text.secondary" gutterBottom>Class Label</Typography>
                      <Typography variant="h3" color="primary">{inferenceResult.prediction}</Typography>
                    </CardContent>
                  </Card>
                  
                  <Typography variant="subtitle2" gutterBottom>Confidence Score</Typography>
                  <Box sx={{ display: 'flex', alignItems: 'center', mb: 3 }}>
                    <Box sx={{ width: '100%', mr: 1 }}>
                      <LinearProgress variant="determinate" value={inferenceResult.probability * 100} />
                    </Box>
                    <Box sx={{ minWidth: 35 }}>
                      <Typography variant="body2" color="text.secondary">{`${Math.round(inferenceResult.probability * 100)}%`}</Typography>
                    </Box>
                  </Box>

                  <Typography variant="subtitle2" gutterBottom>Top Contributing Factors</Typography>
                  <Stack direction="row" spacing={1}>
                    {inferenceResult.factors.map((f: string) => (
                      <Chip key={f} label={f} size="small" />
                    ))}
                  </Stack>
                </Box>
              ) : (
                <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '300px', color: 'text.disabled' }}>
                  <InferenceIcon sx={{ fontSize: 60, mb: 2, opacity: 0.3 }} />
                  <Typography>Run a prediction to see results</Typography>
                </Box>
              )}
            </Paper>
          </Grid>
        </Grid>
      </TabPanel>

      {/* New Training Job Dialog */}
      <Dialog open={openTrainDialog} onClose={() => setOpenTrainDialog(false)} maxWidth="sm" fullWidth>
        <DialogTitle>Start Training Job</DialogTitle>
        <DialogContent>
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2, mt: 1 }}>
            <FormControl fullWidth>
              <InputLabel>Dataset</InputLabel>
              <Select label="Dataset" defaultValue="">
                <MenuItem value="ds_churn_training">Churn Training Set (Dec 2023)</MenuItem>
                <MenuItem value="ds_sales_hist">Sales History (2020-2023)</MenuItem>
              </Select>
            </FormControl>
            <FormControl fullWidth>
              <InputLabel>Algorithm</InputLabel>
              <Select label="Algorithm" defaultValue="">
                <MenuItem value="xgboost">XGBoost Classifier</MenuItem>
                <MenuItem value="random_forest">Random Forest</MenuItem>
                <MenuItem value="linear_reg">Linear Regression</MenuItem>
              </Select>
            </FormControl>
            <TextField label="Hyperparameters (JSON)" multiline rows={4} defaultValue="{}" />
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenTrainDialog(false)}>Cancel</Button>
          <Button variant="contained" onClick={() => setOpenTrainDialog(false)}>Launch Job</Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
}
