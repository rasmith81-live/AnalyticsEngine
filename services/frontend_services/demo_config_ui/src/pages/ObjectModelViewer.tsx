import {
  Box,
  Paper,
  Typography,
  Chip,
  Stack,
  CircularProgress,
  Alert,
  Breadcrumbs,
  Link,
  Grid,
  Card,
  CardContent,
  List,
  ListItem,
  ListItemText,
  IconButton,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from '@mui/material';
import {
  ArrowBack as ArrowBackIcon,
  AccountTree as AccountTreeIcon,
  Storage as StorageIcon,
  Link as LinkIcon,
} from '@mui/icons-material';
import { useParams, useNavigate, Link as RouterLink } from 'react-router-dom';
import { useObjectModels } from '../hooks/useObjectModelDetails';
import ObjectModelDiagram from '../components/ObjectModelDiagram';

export default function ObjectModelViewer() {
  const { modelCode } = useParams<{ modelCode: string }>();
  const navigate = useNavigate();

  const { data: objectModels, isLoading, error } = useObjectModels(
    modelCode ? [modelCode] : []
  );

  const model = objectModels?.[0];

  if (isLoading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '60vh' }}>
        <CircularProgress />
      </Box>
    );
  }

  if (error || !model) {
    return (
      <Box sx={{ p: 3 }}>
        <Alert severity="error">
          Failed to load object model. The model may not exist or the metadata service is unavailable.
        </Alert>
        <IconButton onClick={() => navigate(-1)} sx={{ mt: 2 }}>
          <ArrowBackIcon />
        </IconButton>
      </Box>
    );
  }

  // Parse schema definition to extract fields and relationships
  const parseSchema = (schema: string) => {
    const fields: Array<{ name: string; type: string; nullable: boolean }> = [];
    const relationships: Array<{ name: string; target: string; type: string }> = [];

    if (!schema) return { fields, relationships };

    const lines = schema.split('\n');
    let inRelationships = false;

    for (const line of lines) {
      const trimmed = line.trim();

      // Check if we're in relationships section
      if (trimmed.startsWith("' Relationships")) {
        inRelationships = true;
        continue;
      }

      // Skip empty lines and comments
      if (!trimmed || trimmed.startsWith("'")) continue;

      if (inRelationships) {
        // Parse relationship: field_name --> TargetModel
        const relMatch = trimmed.match(/(\w+)\s*-->\s*(\w+)/);
        if (relMatch) {
          relationships.push({
            name: relMatch[1],
            target: relMatch[2],
            type: 'association',
          });
        }
      } else {
        // Parse field: field_name : type
        const fieldMatch = trimmed.match(/(\w+)\s*:\s*(\w+)(\?)?/);
        if (fieldMatch) {
          fields.push({
            name: fieldMatch[1],
            type: fieldMatch[2],
            nullable: !!fieldMatch[3],
          });
        }
      }
    }

    return { fields, relationships };
  };

  const { fields, relationships } = parseSchema(model.schema_definition || '');

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
        <Typography color="text.primary">{model.display_name}</Typography>
      </Breadcrumbs>

      {/* Header */}
      <Box sx={{ display: 'flex', alignItems: 'center', mb: 3 }}>
        <IconButton onClick={() => navigate(-1)} sx={{ mr: 2 }}>
          <ArrowBackIcon />
        </IconButton>
        <Box sx={{ flexGrow: 1 }}>
          <Typography variant="h4" gutterBottom>
            {model.display_name}
          </Typography>
          <Stack direction="row" spacing={1} sx={{ mt: 1 }}>
            <Chip label={model.code} size="small" color="primary" />
            <Chip
              label={model.table_name || 'No table'}
              size="small"
              variant="outlined"
              icon={<StorageIcon />}
            />
            {model.metadata_?.modules && model.metadata_.modules.length > 0 && (
              <Chip
                label={`${model.metadata_.modules.length} modules`}
                size="small"
                variant="outlined"
              />
            )}
          </Stack>
        </Box>
      </Box>

      {/* Description */}
      {model.description && (
        <Paper sx={{ p: 3, mb: 3 }}>
          <Typography variant="body1" color="text.secondary">
            {model.description}
          </Typography>
        </Paper>
      )}

      <Grid container spacing={3}>
        {/* UML Diagram */}
        <Grid item xs={12}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                <AccountTreeIcon sx={{ mr: 1, verticalAlign: 'middle' }} />
                UML Class Diagram
              </Typography>
              {model.schema_definition ? (
                <ObjectModelDiagram schemaDefinition={model.schema_definition} />
              ) : (
                <Alert severity="info">
                  No schema definition available for this object model.
                </Alert>
              )}
            </CardContent>
          </Card>
        </Grid>

        {/* Fields/Attributes */}
        {fields.length > 0 && (
          <Grid item xs={12} md={6}>
            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  Fields & Attributes
                </Typography>
                <TableContainer>
                  <Table size="small">
                    <TableHead>
                      <TableRow>
                        <TableCell><strong>Field Name</strong></TableCell>
                        <TableCell><strong>Type</strong></TableCell>
                        <TableCell><strong>Nullable</strong></TableCell>
                      </TableRow>
                    </TableHead>
                    <TableBody>
                      {fields.map((field) => (
                        <TableRow key={field.name}>
                          <TableCell>
                            <code>{field.name}</code>
                          </TableCell>
                          <TableCell>
                            <Chip label={field.type} size="small" variant="outlined" />
                          </TableCell>
                          <TableCell>
                            {field.nullable ? (
                              <Chip label="Yes" size="small" color="default" />
                            ) : (
                              <Chip label="No" size="small" color="primary" />
                            )}
                          </TableCell>
                        </TableRow>
                      ))}
                    </TableBody>
                  </Table>
                </TableContainer>
              </CardContent>
            </Card>
          </Grid>
        )}

        {/* Relationships */}
        {relationships.length > 0 && (
          <Grid item xs={12} md={6}>
            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  <LinkIcon sx={{ mr: 1, verticalAlign: 'middle' }} />
                  Relationships
                </Typography>
                <List>
                  {relationships.map((rel, index) => (
                    <ListItem key={index}>
                      <ListItemText
                        primary={
                          <Stack direction="row" spacing={1} alignItems="center">
                            <Typography variant="body2" component="span">
                              <code>{rel.name}</code>
                            </Typography>
                            <Typography variant="body2" color="text.secondary">
                              →
                            </Typography>
                            <Chip
                              label={rel.target}
                              size="small"
                              clickable
                              component={RouterLink}
                              to={`/object-model/${rel.target}`}
                            />
                          </Stack>
                        }
                        secondary={rel.type}
                      />
                    </ListItem>
                  ))}
                </List>
              </CardContent>
            </Card>
          </Grid>
        )}

        {/* Module Usage */}
        {model.metadata_?.modules && model.metadata_.modules.length > 0 && (
          <Grid item xs={12}>
            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  Used in Modules
                </Typography>
                <Stack direction="row" spacing={1} flexWrap="wrap" useFlexGap>
                  {model.metadata_.modules.map((module: string) => (
                    <Chip
                      key={module}
                      label={module}
                      size="medium"
                      variant="outlined"
                    />
                  ))}
                </Stack>
              </CardContent>
            </Card>
          </Grid>
        )}

        {/* Technical Details */}
        <Grid item xs={12}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Technical Details
              </Typography>
              <Grid container spacing={2}>
                <Grid item xs={12} sm={6} md={3}>
                  <Paper sx={{ p: 2, bgcolor: 'grey.50' }}>
                    <Typography variant="subtitle2" color="text.secondary">
                      Object Code
                    </Typography>
                    <Typography variant="body1">
                      <code>{model.code}</code>
                    </Typography>
                  </Paper>
                </Grid>
                <Grid item xs={12} sm={6} md={3}>
                  <Paper sx={{ p: 2, bgcolor: 'grey.50' }}>
                    <Typography variant="subtitle2" color="text.secondary">
                      Table Name
                    </Typography>
                    <Typography variant="body1">
                      <code>{model.table_name || 'N/A'}</code>
                    </Typography>
                  </Paper>
                </Grid>
                <Grid item xs={12} sm={6} md={3}>
                  <Paper sx={{ p: 2, bgcolor: 'grey.50' }}>
                    <Typography variant="subtitle2" color="text.secondary">
                      Fields Count
                    </Typography>
                    <Typography variant="h5">{fields.length}</Typography>
                  </Paper>
                </Grid>
                <Grid item xs={12} sm={6} md={3}>
                  <Paper sx={{ p: 2, bgcolor: 'grey.50' }}>
                    <Typography variant="subtitle2" color="text.secondary">
                      Relationships
                    </Typography>
                    <Typography variant="h5">{relationships.length}</Typography>
                  </Paper>
                </Grid>
              </Grid>
            </CardContent>
          </Card>
        </Grid>

        {/* Raw Schema */}
        {model.schema_definition && (
          <Grid item xs={12}>
            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  Raw Schema Definition
                </Typography>
                <Paper
                  sx={{
                    p: 2,
                    bgcolor: 'grey.50',
                    fontFamily: 'monospace',
                    fontSize: '0.85rem',
                    overflowX: 'auto',
                    maxHeight: '400px',
                    overflow: 'auto',
                  }}
                >
                  <pre style={{ margin: 0 }}>{model.schema_definition}</pre>
                </Paper>
              </CardContent>
            </Card>
          </Grid>
        )}
      </Grid>
    </Box>
  );
}
