/**
 * KPIDetailPreview Component
 * Shows full KPI profile when selected, like a product detail page
 */

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
  Link,
  Tooltip,
} from '@mui/material';
import {
  Add as AddIcon,
  AccountTree as AccountTreeIcon,
  Functions as FunctionsIcon,
  Info as InfoIcon,
  OpenInNew as OpenInNewIcon,
} from '@mui/icons-material';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useKPIDetail } from '../hooks/useKPIDetails';
import { useObjectModels } from '../hooks/useObjectModelDetails';
import ObjectModelDiagram from './ObjectModelDiagram';
import type { KPI } from '../types';

interface KPIDetailPreviewProps {
  kpiCode: string | null;
  onAddToCart: (kpiCode: string) => void;
  onDeriveCustomKPI: (kpiCode: string) => void;
  isInCart: boolean;
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
      id={`kpi-tabpanel-${index}`}
      aria-labelledby={`kpi-tab-${index}`}
      {...other}
    >
      {value === index && <Box>{children}</Box>}
    </div>
  );
}

// Object Model Diagrams Section Component
function ObjectModelDiagramsSection({ requiredObjects }: { requiredObjects: string[] }) {
  const { data: objectModels, isLoading, error } = useObjectModels(requiredObjects);
  const [selectedModel, setSelectedModel] = useState<string | null>(null);

  if (isLoading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', p: 3 }}>
        <CircularProgress size={24} />
      </Box>
    );
  }

  if (error) {
    return (
      <Alert severity="warning">
        Unable to load object model diagrams. The metadata service may be unavailable.
      </Alert>
    );
  }

  if (!objectModels || objectModels.length === 0) {
    return null;
  }

  // Find the first model with a schema definition
  const modelWithSchema = objectModels.find(model => model.schema_definition);

  if (!modelWithSchema) {
    return (
      <Alert severity="info">
        Object model diagrams are not available for the required objects.
      </Alert>
    );
  }

  return (
    <Box>
      <Typography variant="subtitle2" color="text.secondary" gutterBottom>
        Relationship Diagram
      </Typography>
      <ObjectModelDiagram
        schemaDefinition={modelWithSchema.schema_definition || ''}
        highlightEntity={selectedModel || undefined}
        onEntityClick={(entityName) => setSelectedModel(entityName)}
      />
      {selectedModel && (
        <Box sx={{ mt: 1 }}>
          <Chip
            label={`Selected: ${selectedModel}`}
            onDelete={() => setSelectedModel(null)}
            size="small"
            color="primary"
          />
        </Box>
      )}
    </Box>
  );
}

export default function KPIDetailPreview({
  kpiCode,
  onAddToCart,
  onDeriveCustomKPI,
  isInCart,
}: KPIDetailPreviewProps) {
  const navigate = useNavigate();
  const [activeTab, setActiveTab] = useState(0);
  const { data: kpi, isLoading, error } = useKPIDetail(kpiCode || '');

  if (!kpiCode) {
    return (
      <Paper elevation={2} sx={{ p: 4, height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <Box sx={{ textAlign: 'center' }}>
          <InfoIcon sx={{ fontSize: 64, color: 'text.secondary', mb: 2 }} />
          <Typography variant="h6" color="text.secondary" gutterBottom>
            Select a KPI to view details
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Click on any KPI in the tree to see its full profile
          </Typography>
        </Box>
      </Paper>
    );
  }

  if (isLoading) {
    return (
      <Paper elevation={2} sx={{ p: 4, height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <CircularProgress />
      </Paper>
    );
  }

  if (error || !kpi) {
    return (
      <Paper elevation={2} sx={{ p: 3 }}>
        <Alert severity="error">Failed to load KPI details</Alert>
      </Paper>
    );
  }

  const getDisplayName = (kpi: KPI) => kpi.display_name || kpi.name || kpi.code;

  return (
    <Paper elevation={2} sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
      {/* Header */}
      <Box sx={{ p: 2, borderBottom: 1, borderColor: 'divider' }}>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 1 }}>
          <Box sx={{ flex: 1 }}>
            <Typography variant="h5" gutterBottom>
              {getDisplayName(kpi)}
            </Typography>
            <Typography variant="caption" color="text.secondary">
              {kpi.code}
            </Typography>
          </Box>
          <Box>
            {isInCart ? (
              <Chip label="In Cart" color="success" size="small" />
            ) : null}
          </Box>
        </Box>

        {/* Action Buttons */}
        <Stack direction="row" spacing={1} sx={{ mt: 2 }}>
          <Button
            variant="contained"
            color="primary"
            startIcon={<AddIcon />}
            onClick={() => onAddToCart(kpi.code)}
            disabled={isInCart}
            fullWidth
          >
            {isInCart ? 'Added to Cart' : 'Add to Cart'}
          </Button>
          <Button
            variant="outlined"
            startIcon={<FunctionsIcon />}
            onClick={() => onDeriveCustomKPI(kpi.code)}
            fullWidth
          >
            Derive Custom KPI
          </Button>
        </Stack>
        <Button
          variant="text"
          startIcon={<OpenInNewIcon />}
          onClick={() => navigate(`/kpi/${kpi.code}`)}
          fullWidth
          sx={{ mt: 1 }}
        >
          View Full Details
        </Button>
      </Box>

      {/* Tabs */}
      <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
        <Tabs value={activeTab} onChange={(_, newValue) => setActiveTab(newValue)} variant="fullWidth">
          <Tab label="Overview" />
          <Tab label="Formula" />
          <Tab label="Objects" />
        </Tabs>
      </Box>

      {/* Tab Content - Scrollable */}
      <Box sx={{ flex: 1, overflowY: 'auto', p: 2 }}>
        {/* Overview Tab */}
        <TabPanel value={activeTab} index={0}>
          <Stack spacing={2}>
            {/* Description */}
            {kpi.description && (
              <Box>
                <Typography variant="subtitle2" color="text.secondary" gutterBottom>
                  Description
                </Typography>
                <Typography variant="body2">{kpi.description}</Typography>
              </Box>
            )}

            {/* Full KPI Definition */}
            {kpi.full_kpi_definition && (
              <Box>
                <Typography variant="subtitle2" color="text.secondary" gutterBottom>
                  Full Definition
                </Typography>
                <Paper variant="outlined" sx={{ p: 2, bgcolor: 'grey.50' }}>
                  <Typography variant="body2" sx={{ whiteSpace: 'pre-wrap' }}>
                    {kpi.full_kpi_definition}
                  </Typography>
                </Paper>
              </Box>
            )}

            {/* Diagnostic Questions */}
            {kpi.diagnostic_questions && (
              <Box>
                <Typography variant="subtitle2" color="text.secondary" gutterBottom>
                  Diagnostic Questions
                </Typography>
                <Paper variant="outlined" sx={{ p: 2, bgcolor: 'info.50', borderColor: 'info.main' }}>
                  <Typography variant="body2" sx={{ whiteSpace: 'pre-wrap' }}>
                    {kpi.diagnostic_questions}
                  </Typography>
                </Paper>
              </Box>
            )}

            {/* Risk Warnings */}
            {kpi.risk_warnings && (
              <Box>
                <Typography variant="subtitle2" color="text.secondary" gutterBottom>
                  Risk Warnings
                </Typography>
                <Alert severity="warning" sx={{ '& .MuiAlert-message': { width: '100%' } }}>
                  <Typography variant="body2" sx={{ whiteSpace: 'pre-wrap' }}>
                    {kpi.risk_warnings}
                  </Typography>
                </Alert>
              </Box>
            )}

            {/* Unit */}
            <Box>
              <Typography variant="subtitle2" color="text.secondary" gutterBottom>
                Unit
              </Typography>
              <Chip label={kpi.unit || 'N/A'} size="small" />
            </Box>

            {/* Metadata */}
            {kpi.metadata_ && (
              <>
                {kpi.metadata_.modules && kpi.metadata_.modules.length > 0 && (
                  <Box>
                    <Typography variant="subtitle2" color="text.secondary" gutterBottom>
                      Modules
                    </Typography>
                    <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
                      {kpi.metadata_.modules.map((module) => (
                        <Chip key={module} label={module} size="small" variant="outlined" />
                      ))}
                    </Box>
                  </Box>
                )}

                {kpi.metadata_.value_chains && kpi.metadata_.value_chains.length > 0 && (
                  <Box>
                    <Typography variant="subtitle2" color="text.secondary" gutterBottom>
                      Value Chains
                    </Typography>
                    <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
                      {kpi.metadata_.value_chains.map((vc) => (
                        <Chip key={vc} label={vc} size="small" variant="outlined" color="primary" />
                      ))}
                    </Box>
                  </Box>
                )}

                {kpi.metadata_.category && (
                  <Box>
                    <Typography variant="subtitle2" color="text.secondary" gutterBottom>
                      Category
                    </Typography>
                    <Chip label={kpi.metadata_.category} size="small" color="secondary" />
                  </Box>
                )}
              </>
            )}

            {/* Benchmarks */}
            {kpi.benchmarks && Object.keys(kpi.benchmarks).length > 0 && (
              <Box>
                <Typography variant="subtitle2" color="text.secondary" gutterBottom>
                  Benchmarks
                </Typography>
                <Box sx={{ p: 1.5, bgcolor: 'grey.50', borderRadius: 1 }}>
                  {Object.entries(kpi.benchmarks).map(([key, value]) => (
                    <Box key={key} sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.5 }}>
                      <Typography variant="caption">{key}:</Typography>
                      <Typography variant="caption" fontWeight="bold">
                        {String(value)}
                      </Typography>
                    </Box>
                  ))}
                </Box>
              </Box>
            )}
          </Stack>
        </TabPanel>

        {/* Formula Tab */}
        <TabPanel value={activeTab} index={1}>
          <Stack spacing={2}>
            <Box>
              <Typography variant="subtitle2" color="text.secondary" gutterBottom>
                Formula
              </Typography>
              <Paper variant="outlined" sx={{ p: 2, bgcolor: 'grey.50', fontFamily: 'monospace', fontSize: '0.875rem' }}>
                {kpi.formula}
              </Paper>
            </Box>

            {kpi.calculation_logic && (
              <Box>
                <Typography variant="subtitle2" color="text.secondary" gutterBottom>
                  Calculation Logic
                </Typography>
                <Typography variant="body2" sx={{ whiteSpace: 'pre-wrap' }}>
                  {kpi.calculation_logic}
                </Typography>
              </Box>
            )}
          </Stack>
        </TabPanel>

        {/* Objects Tab */}
        <TabPanel value={activeTab} index={2}>
          <Stack spacing={3}>
            {/* Required Objects List */}
            <Box>
              <Typography variant="subtitle2" color="text.secondary" gutterBottom>
                Required Objects ({kpi.required_objects?.length || 0})
              </Typography>
              {kpi.required_objects && kpi.required_objects.length > 0 ? (
                <Stack spacing={1}>
                  {kpi.required_objects.map((obj) => (
                    <Paper
                      key={obj}
                      variant="outlined"
                      sx={{
                        p: 1.5,
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'space-between',
                        '&:hover': { bgcolor: 'action.hover' },
                      }}
                    >
                      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                        <AccountTreeIcon fontSize="small" color="primary" />
                        <Typography variant="body2">{obj}</Typography>
                      </Box>
                      <Tooltip title="View Object Model">
                        <Link
                          component="button"
                          variant="caption"
                          onClick={() => {
                            // TODO: Navigate to object model viewer
                            console.log('View object model:', obj);
                          }}
                        >
                          View Schema
                        </Link>
                      </Tooltip>
                    </Paper>
                  ))}
                </Stack>
              ) : (
                <Typography variant="body2" color="text.secondary">
                  No required objects defined
                </Typography>
              )}
            </Box>

            {/* Object Model Diagrams */}
            {kpi.required_objects && kpi.required_objects.length > 0 && (
              <ObjectModelDiagramsSection requiredObjects={kpi.required_objects} />
            )}
          </Stack>
        </TabPanel>

      </Box>
    </Paper>
  );
}
