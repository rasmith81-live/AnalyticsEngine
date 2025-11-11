import {
  Box,
  Paper,
  Typography,
  Chip,
  Button,
  Stack,
  CircularProgress,
  Alert,
  Tabs,
  Tab,
  Breadcrumbs,
  Link,
  Grid,
  Card,
  CardContent,
  List,
  ListItem,
  ListItemText,
  IconButton,
} from '@mui/material';
import {
  ArrowBack as ArrowBackIcon,
  Add as AddIcon,
  Functions as FunctionsIcon,
  AccountTree as AccountTreeIcon,
  TrendingUp as TrendingUpIcon,
  Info as InfoIcon,
  Category as CategoryIcon,
  Edit as EditIcon,
} from '@mui/icons-material';
import { useState } from 'react';
import { useParams, useNavigate, Link as RouterLink } from 'react-router-dom';
import { useKPIDetail } from '../hooks/useKPIDetails';
import { useObjectModels } from '../hooks/useObjectModelDetails';
import { useCart } from '../contexts/CartContext';
import ObjectModelDiagram from '../components/ObjectModelDiagram';

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
      id={`kpi-tabpanel-${index}`}
      aria-labelledby={`kpi-tab-${index}`}
      {...other}
    >
      {value === index && <Box sx={{ py: 3 }}>{children}</Box>}
    </div>
  );
}

export default function KPIDetailPage() {
  const { kpiCode } = useParams<{ kpiCode: string }>();
  const navigate = useNavigate();
  const { addToCart, isInCart } = useCart();
  const [activeTab, setActiveTab] = useState(0);

  const { data: kpi, isLoading, error } = useKPIDetail(kpiCode || '');
  const { data: objectModels, isLoading: modelsLoading } = useObjectModels(
    kpi?.required_objects || []
  );

  const handleTabChange = (_event: React.SyntheticEvent, newValue: number) => {
    setActiveTab(newValue);
  };

  const handleAddToCart = () => {
    if (kpiCode) {
      addToCart(kpiCode);
    }
  };

  if (isLoading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '60vh' }}>
        <CircularProgress />
      </Box>
    );
  }

  if (error || !kpi) {
    return (
      <Box sx={{ p: 3 }}>
        <Alert severity="error">
          Failed to load KPI details. The KPI may not exist or the metadata service is unavailable.
        </Alert>
        {error && (
          <Alert severity="info" sx={{ mt: 2 }}>
            <Typography variant="body2">
              <strong>Debug Info:</strong><br />
              KPI Code: {kpiCode}<br />
              Attempting to load from: http://localhost:8020/kpis/{kpiCode}
            </Typography>
          </Alert>
        )}
        <Button
          startIcon={<ArrowBackIcon />}
          onClick={() => navigate(-1)}
          sx={{ mt: 2 }}
        >
          Go Back
        </Button>
      </Box>
    );
  }

  return (
    <Box sx={{ p: 3 }}>
      {/* Breadcrumbs */}
      <Breadcrumbs aria-label="breadcrumb" sx={{ mb: 2 }}>
        <Link component={RouterLink} to="/" underline="hover" color="inherit">
          Home
        </Link>
        <Link component={RouterLink} to="/config" underline="hover" color="inherit">
          Configuration
        </Link>
        <Typography color="text.primary">{kpi.display_name}</Typography>
      </Breadcrumbs>

      {/* Header */}
      <Box sx={{ display: 'flex', alignItems: 'center', mb: 3 }}>
        <IconButton onClick={() => navigate(-1)} sx={{ mr: 2 }}>
          <ArrowBackIcon />
        </IconButton>
        <Box sx={{ flexGrow: 1 }}>
          <Typography variant="h4" gutterBottom>
            {kpi.display_name}
          </Typography>
          <Stack direction="row" spacing={1} sx={{ mt: 1 }}>
            <Chip label={kpi.code} size="small" color="primary" />
            {kpi.metadata_?.value_chains && kpi.metadata_.value_chains[0] && (
              <Chip label={kpi.metadata_.value_chains[0]} size="small" variant="outlined" />
            )}
            {kpi.module_code && <Chip label={kpi.module_code} size="small" variant="outlined" />}
            {kpi.unit && <Chip label={kpi.unit} size="small" icon={<TrendingUpIcon />} />}
          </Stack>
        </Box>
        <Stack direction="row" spacing={2}>
          <Button
            variant="outlined"
            startIcon={<EditIcon />}
            onClick={() => {/* TODO: Open derive custom KPI modal */}}
          >
            Derive Custom KPI
          </Button>
          <Button
            variant={isInCart(kpiCode || '') ? 'outlined' : 'contained'}
            startIcon={<AddIcon />}
            onClick={handleAddToCart}
            disabled={isInCart(kpiCode || '')}
          >
            {isInCart(kpiCode || '') ? 'In Cart' : 'Add to Cart'}
          </Button>
        </Stack>
      </Box>

      {/* Description */}
      <Paper sx={{ p: 3, mb: 3 }}>
        <Typography variant="body1" color="text.secondary">
          {kpi.description}
        </Typography>
      </Paper>

      {/* Tabs */}
      <Paper sx={{ mb: 3 }}>
        <Tabs value={activeTab} onChange={handleTabChange} aria-label="KPI detail tabs">
          <Tab label="Overview" icon={<InfoIcon />} iconPosition="start" />
          <Tab label="Formula" icon={<FunctionsIcon />} iconPosition="start" />
          <Tab label="Objects & Relationships" icon={<AccountTreeIcon />} iconPosition="start" />
          <Tab label="Benchmarks" icon={<TrendingUpIcon />} iconPosition="start" />
          <Tab label="Metadata" icon={<CategoryIcon />} iconPosition="start" />
        </Tabs>
      </Paper>

      {/* Tab Panels */}
      <TabPanel value={activeTab} index={0}>
        {/* Overview Tab */}
        <Grid container spacing={3}>
          <Grid item xs={12} md={6}>
            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  Key Information
                </Typography>
                <List dense>
                  <ListItem>
                    <ListItemText
                      primary="KPI Code"
                      secondary={kpi.code}
                    />
                  </ListItem>
                  <ListItem>
                    <ListItemText
                      primary="Value Chain"
                      secondary={kpi.metadata_?.value_chains?.[0] || 'N/A'}
                    />
                  </ListItem>
                  <ListItem>
                    <ListItemText
                      primary="Module"
                      secondary={kpi.module_code || 'N/A'}
                    />
                  </ListItem>
                  <ListItem>
                    <ListItemText
                      primary="Unit of Measure"
                      secondary={kpi.unit || 'N/A'}
                    />
                  </ListItem>
                  <ListItem>
                    <ListItemText
                      primary="Category"
                      secondary={kpi.category || 'N/A'}
                    />
                  </ListItem>
                </List>
              </CardContent>
            </Card>
          </Grid>

          <Grid item xs={12} md={6}>
            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  Required Objects
                </Typography>
                {kpi.required_objects && kpi.required_objects.length > 0 ? (
                  <Stack direction="row" spacing={1} flexWrap="wrap" useFlexGap>
                    {kpi.required_objects.map((obj) => (
                      <Chip
                        key={obj}
                        label={obj}
                        component={RouterLink}
                        to={`/object-model/${obj}`}
                        clickable
                        size="small"
                        sx={{ mb: 1 }}
                      />
                    ))}
                  </Stack>
                ) : (
                  <Typography variant="body2" color="text.secondary">
                    No required objects specified
                  </Typography>
                )}
              </CardContent>
            </Card>
          </Grid>

          <Grid item xs={12}>
            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  Description
                </Typography>
                <Typography variant="body1">
                  {kpi.description}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      </TabPanel>

      <TabPanel value={activeTab} index={1}>
        {/* Formula Tab */}
        <Card>
          <CardContent>
            <Typography variant="h6" gutterBottom>
              Calculation Formula
            </Typography>
            {kpi.formula ? (
              <Paper
                sx={{
                  p: 2,
                  bgcolor: 'grey.50',
                  fontFamily: 'monospace',
                  fontSize: '0.95rem',
                  overflowX: 'auto',
                }}
              >
                <pre style={{ margin: 0 }}>{kpi.formula}</pre>
              </Paper>
            ) : (
              <Alert severity="info">
                Formula not available for this KPI. It may be calculated using a custom handler.
              </Alert>
            )}

            {kpi.category && (
              <Box sx={{ mt: 3 }}>
                <Typography variant="subtitle2" gutterBottom>
                  Category
                </Typography>
                <Chip label={kpi.category} />
              </Box>
            )}
          </CardContent>
        </Card>
      </TabPanel>

      <TabPanel value={activeTab} index={2}>
        {/* Objects & Relationships Tab */}
        <Stack spacing={3}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Required Objects
              </Typography>
              {kpi.required_objects && kpi.required_objects.length > 0 ? (
                <Grid container spacing={2}>
                  {kpi.required_objects.map((obj) => (
                    <Grid item xs={12} sm={6} md={4} key={obj}>
                      <Paper
                        sx={{
                          p: 2,
                          cursor: 'pointer',
                          '&:hover': { bgcolor: 'action.hover' },
                        }}
                        component={RouterLink}
                        to={`/object-model/${obj}`}
                      >
                        <Stack direction="row" alignItems="center" spacing={1}>
                          <AccountTreeIcon color="primary" />
                          <Typography variant="body1">{obj}</Typography>
                        </Stack>
                      </Paper>
                    </Grid>
                  ))}
                </Grid>
              ) : (
                <Typography variant="body2" color="text.secondary">
                  No required objects specified
                </Typography>
              )}
            </CardContent>
          </Card>

          {/* UML Diagrams */}
          {modelsLoading ? (
            <Box sx={{ display: 'flex', justifyContent: 'center', p: 3 }}>
              <CircularProgress />
            </Box>
          ) : objectModels && objectModels.length > 0 ? (
            objectModels
              .filter((model) => model.schema_definition)
              .map((model) => (
                <Card key={model.code}>
                  <CardContent>
                    <Typography variant="h6" gutterBottom>
                      {model.display_name} - Relationship Diagram
                    </Typography>
                    <ObjectModelDiagram
                      schemaDefinition={model.schema_definition || ''}
                    />
                  </CardContent>
                </Card>
              ))
          ) : (
            <Alert severity="info">
              No object model diagrams available for this KPI.
            </Alert>
          )}
        </Stack>
      </TabPanel>

      <TabPanel value={activeTab} index={3}>
        {/* Benchmarks Tab */}
        <Card>
          <CardContent>
            <Typography variant="h6" gutterBottom>
              Industry Benchmarks
            </Typography>
            {kpi.benchmarks && Object.keys(kpi.benchmarks).length > 0 ? (
              <Grid container spacing={2}>
                {Object.entries(kpi.benchmarks).map(([key, value]) => (
                  <Grid item xs={12} sm={6} md={4} key={key}>
                    <Paper sx={{ p: 2, bgcolor: 'grey.50' }}>
                      <Typography variant="subtitle2" color="text.secondary">
                        {key.replace(/_/g, ' ').toUpperCase()}
                      </Typography>
                      <Typography variant="h5">
                        {value} {kpi.unit}
                      </Typography>
                    </Paper>
                  </Grid>
                ))}
              </Grid>
            ) : (
              <Alert severity="info">
                No benchmark data available for this KPI.
              </Alert>
            )}
          </CardContent>
        </Card>
      </TabPanel>

      <TabPanel value={activeTab} index={4}>
        {/* Metadata Tab */}
        <Card>
          <CardContent>
            <Typography variant="h6" gutterBottom>
              Complete Metadata
            </Typography>
            <Paper
              sx={{
                p: 2,
                bgcolor: 'grey.50',
                fontFamily: 'monospace',
                fontSize: '0.85rem',
                overflowX: 'auto',
                maxHeight: '600px',
                overflow: 'auto',
              }}
            >
              <pre style={{ margin: 0 }}>
                {JSON.stringify(kpi, null, 2)}
              </pre>
            </Paper>
          </CardContent>
        </Card>
      </TabPanel>
    </Box>
  );
}
