import { useState } from 'react';
import {
  Typography,
  Paper,
  Box,
  Button,
  Grid,
  Card,
  CardContent,
  Divider,
  Chip,
  Stepper,
  Step,
  StepLabel,
  CircularProgress,
  ToggleButton,
  ToggleButtonGroup,
  Alert,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Slider,
  TextField,
  Stack,
} from '@mui/material';
import {
  Description as DocumentIcon,
  Timeline as TimelineIcon,
  AttachMoney as MoneyIcon,
  Speed as SpeedIcon,
  CheckCircle as CheckIcon,
  CloudDownload as DownloadIcon,
  Send as SendIcon,
  Storage as StorageIcon,
  Business as BusinessIcon,
  Group as GroupIcon,
  Dns as DnsIcon,
} from '@mui/icons-material';
import { useCart } from '../contexts/CartContext';
import { configApi, ServiceProposal as ServiceProposalType } from '../api/configApi';
import ResourceScheduler from '../components/proposal/ResourceScheduler';
import ProjectGanttChart from '../components/proposal/ProjectGanttChart';

// Mock client ID for demo purposes
const DEMO_CLIENT_ID = 'demo-client-123';

const PROPOSAL_STEPS = ['KPI Selection', 'Integration Strategy', 'Review Estimate', 'Finalize SOW'];

export default function ServiceProposal() {
  const { selectedKPIs } = useCart();
  const [activeStep, setActiveStep] = useState(0);
  const [integrationMethod, setIntegrationMethod] = useState<'batch' | 'realtime'>('batch');
  const [licenseTier, setLicenseTier] = useState<'starter' | 'professional' | 'enterprise'>('professional');
  const [userCount, setUserCount] = useState<number>(10);
  const [infrastructure, setInfrastructure] = useState<'cloud' | 'onprem'>('cloud');
  
  const [loading, setLoading] = useState(false);
  const [proposal, setProposal] = useState<ServiceProposalType | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleGenerateProposal = async () => {
    setLoading(true);
    setError(null);
    try {
      // @ts-ignore - Extending the API call with new parameters
      const result = await configApi.generateProposal(DEMO_CLIENT_ID, {
        integration_method: integrationMethod,
        included_kpis: selectedKPIs,
        license_tier: licenseTier,
        user_count: userCount,
        infrastructure: infrastructure
      });
      setProposal(result);
      setActiveStep(2);
    } catch (err) {
      console.error('Error generating proposal:', err);
      setError('Failed to generate proposal. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleUpdateStatus = async (status: 'sent' | 'signed') => {
    if (!proposal || !proposal.id) return;
    
    try {
      const updated = await configApi.updateProposal(DEMO_CLIENT_ID, {
        status: status
      });
      setProposal(updated);
      setActiveStep(3);
    } catch (err) {
      console.error('Error updating proposal:', err);
      setError('Failed to update proposal status.');
    }
  };

  const handleExportSOW = () => {
    if (!proposal) return;
    // Stub implementation for PDF export
    // In a real app, this would generate a PDF blob or call an endpoint
    console.log('Exporting SOW for proposal:', proposal.id);
    
    const content = `
      STATEMENT OF WORK
      ----------------
      Client ID: ${DEMO_CLIENT_ID}
      Date: ${new Date().toLocaleDateString()}
      
      Scope:
      - ${selectedKPIs.length} KPIs selected
      - Integration Method: ${integrationMethod}
      - License Tier: ${licenseTier}
      - Infrastructure: ${infrastructure}
      
      Timeline: ${proposal.timeline_weeks} weeks
      Total Estimated Cost: $${proposal.estimated_cost}
    `;
    
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `SOW_${DEMO_CLIENT_ID}_${new Date().toISOString().split('T')[0]}.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      maximumFractionDigits: 0,
    }).format(amount);
  };

  if (selectedKPIs.length === 0) {
    return (
      <Box sx={{ p: 3, textAlign: 'center' }}>
        <Paper sx={{ p: 5 }}>
          <DocumentIcon sx={{ fontSize: 60, color: 'text.secondary', mb: 2 }} />
          <Typography variant="h5" gutterBottom>
            No KPIs Selected
          </Typography>
          <Typography color="text.secondary" paragraph>
            Please select KPIs from the Metric Tree or Object Models to generate a proposal.
          </Typography>
          <Button variant="contained" href="/demo">
            Go to Metric Tree
          </Button>
        </Paper>
      </Box>
    );
  }

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Service Proposal Generator
      </Typography>
      
      <Stepper activeStep={activeStep} sx={{ mb: 4, mt: 2 }}>
        {PROPOSAL_STEPS.map((label) => (
          <Step key={label}>
            <StepLabel>{label}</StepLabel>
          </Step>
        ))}
      </Stepper>

      {error && (
        <Alert severity="error" sx={{ mb: 3 }}>
          {error}
        </Alert>
      )}

      <Grid container spacing={3}>
        {/* Configuration Panel */}
        <Grid item xs={12} md={5}>
          <Paper sx={{ p: 3, height: '100%' }}>
            <Typography variant="h6" gutterBottom>
              Proposal Configuration
            </Typography>
            
            <Box sx={{ mb: 3 }}>
              <Typography variant="subtitle2" gutterBottom>
                Selected KPIs ({selectedKPIs.length})
              </Typography>
              <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1 }}>
                {selectedKPIs.map((kpi) => (
                  <Chip key={kpi} label={kpi} size="small" />
                ))}
              </Box>
            </Box>

            <Divider sx={{ my: 3 }} />

            <Box sx={{ mb: 3 }}>
              <Stack direction="row" alignItems="center" spacing={1} sx={{ mb: 2 }}>
                <BusinessIcon color="action" />
                <Typography variant="subtitle2">License Configuration</Typography>
              </Stack>
              
              <FormControl fullWidth size="small" sx={{ mb: 2 }}>
                <InputLabel>License Tier</InputLabel>
                <Select
                  value={licenseTier}
                  label="License Tier"
                  onChange={(e) => setLicenseTier(e.target.value as any)}
                >
                  <MenuItem value="starter">Starter (Up to 5 Users)</MenuItem>
                  <MenuItem value="professional">Professional (Up to 50 Users)</MenuItem>
                  <MenuItem value="enterprise">Enterprise (Unlimited)</MenuItem>
                </Select>
              </FormControl>

              <Typography variant="caption" gutterBottom component="div">
                User Count: {userCount}
              </Typography>
              <Stack direction="row" spacing={2} alignItems="center">
                <GroupIcon color="action" fontSize="small" />
                <Slider
                  value={userCount}
                  onChange={(_, val) => setUserCount(val as number)}
                  min={1}
                  max={100}
                  valueLabelDisplay="auto"
                />
                <TextField
                  value={userCount}
                  onChange={(e) => setUserCount(Number(e.target.value))}
                  size="small"
                  type="number"
                  sx={{ width: 80 }}
                />
              </Stack>
            </Box>

            <Box sx={{ mb: 3 }}>
              <Stack direction="row" alignItems="center" spacing={1} sx={{ mb: 2 }}>
                <DnsIcon color="action" />
                <Typography variant="subtitle2">Infrastructure</Typography>
              </Stack>
              
              <FormControl fullWidth size="small">
                <InputLabel>Deployment Model</InputLabel>
                <Select
                  value={infrastructure}
                  label="Deployment Model"
                  onChange={(e) => setInfrastructure(e.target.value as any)}
                >
                  <MenuItem value="cloud">Managed Cloud (SaaS)</MenuItem>
                  <MenuItem value="onprem">On-Premise / Private Cloud</MenuItem>
                </Select>
              </FormControl>
            </Box>

            <Box sx={{ mb: 4 }}>
              <Typography variant="subtitle2" gutterBottom>
                Integration Strategy
              </Typography>
              <ToggleButtonGroup
                color="primary"
                value={integrationMethod}
                exclusive
                onChange={(_, value) => value && setIntegrationMethod(value)}
                fullWidth
                size="small"
              >
                <ToggleButton value="batch">
                  <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', py: 1 }}>
                    <StorageIcon sx={{ mb: 1 }} />
                    <Typography variant="button">Batch Processing</Typography>
                    <Typography variant="caption" sx={{ textTransform: 'none' }}>
                      Lower cost, T+1 latency
                    </Typography>
                  </Box>
                </ToggleButton>
                <ToggleButton value="realtime">
                  <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', py: 1 }}>
                    <SpeedIcon sx={{ mb: 1 }} />
                    <Typography variant="button">Real-time Stream</Typography>
                    <Typography variant="caption" sx={{ textTransform: 'none' }}>
                      Higher cost, instant updates
                    </Typography>
                  </Box>
                </ToggleButton>
              </ToggleButtonGroup>
            </Box>

            <Button
              variant="contained"
              size="large"
              fullWidth
              onClick={handleGenerateProposal}
              disabled={loading}
              startIcon={loading ? <CircularProgress size={20} /> : <DocumentIcon />}
            >
              {loading ? 'Analyzing Requirements...' : 'Generate Estimate'}
            </Button>
          </Paper>
        </Grid>

        {/* Results Panel */}
        <Grid item xs={12} md={7}>
          {proposal ? (
            <Paper sx={{ p: 3 }}>
              <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3 }}>
                <Typography variant="h5">Statement of Work Estimate</Typography>
                <Chip 
                  label={proposal.status.toUpperCase()} 
                  color={proposal.status === 'signed' ? 'success' : 'primary'} 
                />
              </Box>

              <Grid container spacing={2} sx={{ mb: 4 }}>
                <Grid item xs={4}>
                  <Card variant="outlined">
                    <CardContent sx={{ textAlign: 'center' }}>
                      <MoneyIcon color="primary" fontSize="large" />
                      <Typography variant="h5">{formatCurrency(proposal.estimated_cost)}</Typography>
                      <Typography variant="caption" color="text.secondary">Estimated Cost</Typography>
                    </CardContent>
                  </Card>
                </Grid>
                <Grid item xs={4}>
                  <Card variant="outlined">
                    <CardContent sx={{ textAlign: 'center' }}>
                      <TimelineIcon color="primary" fontSize="large" />
                      <Typography variant="h5">{proposal.timeline_weeks} Weeks</Typography>
                      <Typography variant="caption" color="text.secondary">Timeline</Typography>
                    </CardContent>
                  </Card>
                </Grid>
                <Grid item xs={4}>
                  <Card variant="outlined">
                    <CardContent sx={{ textAlign: 'center' }}>
                      <CheckIcon color="primary" fontSize="large" />
                      <Typography variant="h5">{proposal.required_objects.length}</Typography>
                      <Typography variant="caption" color="text.secondary">Data Objects</Typography>
                    </CardContent>
                  </Card>
                </Grid>
              </Grid>

              <Box sx={{ mb: 4 }}>
                <ProjectGanttChart timelineWeeks={proposal.timeline_weeks} />
              </Box>

              <Box sx={{ mb: 4 }}>
                <ResourceScheduler timelineWeeks={proposal.timeline_weeks} />
              </Box>

              <Typography variant="subtitle1" gutterBottom>
                Required Data Objects
              </Typography>
              <Box sx={{ mb: 3, display: 'flex', flexWrap: 'wrap', gap: 1 }}>
                {proposal.required_objects.map(obj => (
                  <Chip key={obj} label={obj} variant="outlined" size="small" />
                ))}
              </Box>

              <Divider sx={{ my: 3 }} />

              <Box sx={{ display: 'flex', gap: 2, justifyContent: 'flex-end' }}>
                <Button startIcon={<DownloadIcon />} onClick={handleExportSOW}>
                  Export PDF
                </Button>
                {proposal.status === 'draft' && (
                  <Button 
                    variant="contained" 
                    color="success" 
                    startIcon={<SendIcon />}
                    onClick={() => handleUpdateStatus('sent')}
                  >
                    Send to Client
                  </Button>
                )}
                {proposal.status === 'sent' && (
                  <Button 
                    variant="contained" 
                    color="primary" 
                    onClick={() => handleUpdateStatus('signed')}
                  >
                    Mark as Signed
                  </Button>
                )}
              </Box>
            </Paper>
          ) : (
            <Paper sx={{ p: 4, textAlign: 'center', height: '100%', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', bgcolor: 'grey.50' }}>
              <TimelineIcon sx={{ fontSize: 80, color: 'text.disabled', mb: 2 }} />
              <Typography variant="h6" color="text.secondary">
                Generate a proposal to see cost and timeline estimates
              </Typography>
              <Typography variant="body2" color="text.secondary" sx={{ maxWidth: 400, mt: 1 }}>
                Our engine analyzes the data lineage of your selected KPIs to determine exactly which data objects are required.
              </Typography>
            </Paper>
          )}
        </Grid>
      </Grid>
    </Box>
  );
}


