/**
 * Required Objects View Page
 * Shows consolidated UML diagram of all object models required for selected KPIs
 */

import { useLocation, useNavigate } from 'react-router-dom';
import {
  Box,
  Typography,
  Paper,
  Stack,
  Chip,
  Button,
  CircularProgress,
  Alert,
  Breadcrumbs,
  Link,
  Divider,
  List,
  ListItem,
  ListItemText,
  Grid,
} from '@mui/material';
import {
  ArrowBack as ArrowBackIcon,
  AccountTree as ObjectsIcon,
  OpenInNew as OpenInNewIcon,
} from '@mui/icons-material';
import { useKPIDetails } from '../hooks/useKPIDetails';
import { useObjectModels } from '../hooks/useObjectModelDetails';
import ObjectModelDiagram from '../components/ObjectModelDiagram';

export default function RequiredObjectsView() {
  const location = useLocation();
  const navigate = useNavigate();
  const kpiCodes = (location.state?.kpiCodes as string[]) || [];

  const { data: kpiDetails, isLoading: kpisLoading } = useKPIDetails(kpiCodes);

  // Get all unique required objects from all KPIs
  const allRequiredObjects = Array.from(
    new Set(
      kpiDetails?.flatMap((kpi) => kpi.required_objects || []) || []
    )
  );

  const { data: objectModels, isLoading: modelsLoading } = useObjectModels(allRequiredObjects);

  const isLoading = kpisLoading || modelsLoading;

  // Generate consolidated UML diagram
  const generateConsolidatedUML = () => {
    if (!objectModels || objectModels.length === 0) return '';

    // Combine all schema definitions
    const allSchemas = objectModels
      .map((model) => model.schema_definition)
      .filter(Boolean)
      .join('\n\n');

    return allSchemas;
  };

  const consolidatedUML = generateConsolidatedUML();

  if (kpiCodes.length === 0) {
    return (
      <Box sx={{ p: 3 }}>
        <Alert severity="info">
          No KPIs selected. Please select KPIs from the KPI Configuration page first.
        </Alert>
        <Button
          variant="contained"
          startIcon={<ArrowBackIcon />}
          onClick={() => navigate('/config')}
          sx={{ mt: 2 }}
        >
          Go to KPI Configuration
        </Button>
      </Box>
    );
  }

  if (isLoading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100%', p: 3 }}>
        <CircularProgress />
      </Box>
    );
  }

  return (
    <Box sx={{ p: 3 }}>
      {/* Breadcrumbs */}
      <Breadcrumbs sx={{ mb: 2 }}>
        <Link
          component="button"
          variant="body2"
          onClick={() => navigate('/config')}
          sx={{ cursor: 'pointer' }}
        >
          KPI Configuration
        </Link>
        <Typography variant="body2" color="text.primary">
          Required Objects
        </Typography>
      </Breadcrumbs>

      {/* Header */}
      <Stack direction="row" spacing={2} alignItems="center" sx={{ mb: 3 }}>
        <Button
          startIcon={<ArrowBackIcon />}
          onClick={() => navigate('/config')}
          variant="outlined"
          size="small"
        >
          Back
        </Button>
        <Box sx={{ flex: 1 }}>
          <Stack direction="row" spacing={1} alignItems="center">
            <ObjectsIcon color="primary" sx={{ fontSize: 32 }} />
            <Typography variant="h4" fontWeight="bold">
              Required Objects Analysis
            </Typography>
          </Stack>
          <Typography variant="body2" color="text.secondary">
            Object models required for {kpiCodes.length} selected KPI{kpiCodes.length !== 1 ? 's' : ''}
          </Typography>
        </Box>
      </Stack>

      <Grid container spacing={3}>
        {/* Left Column - Summary */}
        <Grid item xs={12} md={4}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>
              Selected KPIs ({kpiCodes.length})
            </Typography>
            <List dense>
              {kpiDetails?.map((kpi) => (
                <ListItem key={kpi.code} disablePadding>
                  <ListItemText
                    primary={kpi.display_name || kpi.name}
                    secondary={`${kpi.required_objects?.length || 0} objects`}
                  />
                </ListItem>
              ))}
            </List>

            <Divider sx={{ my: 2 }} />

            <Typography variant="h6" gutterBottom>
              Required Objects ({allRequiredObjects.length})
            </Typography>
            <Stack spacing={1}>
              {objectModels?.map((model) => (
                <Chip
                  key={model.code}
                  label={model.display_name || model.name}
                  size="small"
                  icon={<ObjectsIcon />}
                  onClick={() => navigate(`/object-model/${model.code}`)}
                  clickable
                  sx={{ justifyContent: 'flex-start' }}
                />
              ))}
            </Stack>
          </Paper>
        </Grid>

        {/* Right Column - UML Diagram */}
        <Grid item xs={12} md={8}>
          <Paper sx={{ p: 3 }}>
            <Stack direction="row" justifyContent="space-between" alignItems="center" sx={{ mb: 2 }}>
              <Typography variant="h6">
                Consolidated Entity Relationships
              </Typography>
              <Button
                size="small"
                startIcon={<OpenInNewIcon />}
                onClick={() => navigate('/object-models')}
              >
                Browse All Models
              </Button>
            </Stack>

            {consolidatedUML ? (
              <Box sx={{ bgcolor: 'grey.50', p: 2, borderRadius: 1, minHeight: 400 }}>
                <ObjectModelDiagram
                  schemaDefinition={consolidatedUML}
                  highlightEntity=""
                />
              </Box>
            ) : (
              <Alert severity="info">
                No UML diagrams available for the required objects.
              </Alert>
            )}

            <Typography variant="caption" color="text.secondary" sx={{ mt: 2, display: 'block' }}>
              This diagram shows all entity relationships for the object models required by your selected KPIs.
              Click on any object model chip above to view detailed information.
            </Typography>
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
}
