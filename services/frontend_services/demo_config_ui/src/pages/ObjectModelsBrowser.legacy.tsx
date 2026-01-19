/**
 * Object Models Browser Page
 * Browse all object models organized by module/value chain
 */

import { useState } from 'react';
import {
  Box,
  Typography,
  Paper,
  TextField,
  InputAdornment,
  List,
  ListItem,
  ListItemButton,
  ListItemText,
  Chip,
  Stack,
  CircularProgress,
  Alert,
  Divider,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import AccountTreeIcon from '@mui/icons-material/AccountTree';
import StorageIcon from '@mui/icons-material/Storage';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import SwapHorizIcon from '@mui/icons-material/SwapHoriz';
import { useNavigate } from 'react-router-dom';
import { useObjectModels } from '../hooks/useObjectModels';
import ResizableSplitPanel from '../components/ResizableSplitPanel';
import ObjectModelDiagram from '../components/ObjectModelDiagram';
import type { ObjectModel } from '../types';

interface Relationship {
  from: string;
  to: string;
  type: string;
  cardinality: string;
  label?: string;
  direction: 'forward' | 'backward' | 'bidirectional';
}

// Parse PlantUML UML class diagram relationships
function parseRelationships(uml: string, entityCode: string): Relationship[] {
  const relationships: Relationship[] = [];
  const lines = uml.split('\n');
  
  console.log('Parsing relationships for entity:', entityCode);
  console.log('UML content:', uml);
  
  // Regex patterns for different UML relationship types
  // Association: Entity1 "1" -- "0..*" Entity2 : label
  // Composition: Entity1 "1" *-- "0..*" Entity2 : label
  // Aggregation: Entity1 "1" o-- "0..*" Entity2 : label
  // Generalization: Entity1 --|> Entity2
  // Dependency: Entity1 ..> Entity2
  
  // Use [A-Za-z0-9_]+ to match entity names (including camelCase and PascalCase)
  const associationPattern = /([A-Za-z0-9_]+)\s+"([^"]+)"\s+(--)\s+"([^"]+)"\s+([A-Za-z0-9_]+)\s*:\s*(.+?)(?:\s*>)?$/;
  const compositionPattern = /([A-Za-z0-9_]+)\s+"([^"]+)"\s+(\*--)\s+"([^"]+)"\s+([A-Za-z0-9_]+)\s*:\s*(.+?)(?:\s*>)?$/;
  const aggregationPattern = /([A-Za-z0-9_]+)\s+"([^"]+)"\s+(o--)\s+"([^"]+)"\s+([A-Za-z0-9_]+)\s*:\s*(.+?)(?:\s*>)?$/;
  const generalizationPattern = /([A-Za-z0-9_]+)\s+(--\|>)\s+([A-Za-z0-9_]+)/;
  const dependencyPattern = /([A-Za-z0-9_]+)\s+(\.\.>)\s+([A-Za-z0-9_]+)\s*:\s*(.+?)(?:\s*>)?$/;
  
  for (const line of lines) {
    // Skip comments
    if (line.trim().startsWith("'")) continue;
    
    let match;
    let type = 'association';
    let fromCard = '';
    let toCard = '';
    let from = '';
    let to = '';
    let label = '';
    
    // Try composition
    if ((match = line.match(compositionPattern))) {
      [, from, fromCard, , toCard, to, label] = match;
      type = 'composition';
    }
    // Try aggregation
    else if ((match = line.match(aggregationPattern))) {
      [, from, fromCard, , toCard, to, label] = match;
      type = 'aggregation';
    }
    // Try generalization
    else if ((match = line.match(generalizationPattern))) {
      [, from, , to] = match;
      type = 'generalization';
      fromCard = '';
      toCard = '';
      label = 'inherits from';
    }
    // Try dependency
    else if ((match = line.match(dependencyPattern))) {
      [, from, , to, label] = match;
      type = 'dependency';
      fromCard = '';
      toCard = '';
    }
    // Try association
    else if ((match = line.match(associationPattern))) {
      [, from, fromCard, , toCard, to, label] = match;
      type = 'association';
    }
    
    if (match && (from === entityCode || to === entityCode)) {
      let direction: 'forward' | 'backward' | 'bidirectional' = 'bidirectional';
      
      // Determine direction based on position
      if (type === 'generalization') {
        direction = from === entityCode ? 'forward' : 'backward';
      } else if (type === 'dependency') {
        direction = 'forward';
      } else {
        // For association, composition, aggregation
        direction = 'bidirectional';
      }
      
      const cardinality = fromCard && toCard ? `${fromCard} to ${toCard}` : '';
      
      relationships.push({
        from,
        to,
        type,
        cardinality,
        label: label.trim(),
        direction
      });
      
      console.log('Found relationship:', { from, to, type, cardinality, label: label.trim() });
    }
  }
  
  console.log('Total relationships found:', relationships.length);
  return relationships;
}

export default function ObjectModelsBrowser() {
  const navigate = useNavigate();
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedModel, setSelectedModel] = useState<string | null>(null);
  
  const { data: objectModels, isLoading, error } = useObjectModels();

  // Filter object models based on search
  const filteredModels = objectModels?.filter(model => {
    if (!searchQuery) return true;
    const query = searchQuery.toLowerCase();
    return (
      model.name?.toLowerCase().includes(query) ||
      model.display_name?.toLowerCase().includes(query) ||
      model.code?.toLowerCase().includes(query) ||
      model.description?.toLowerCase().includes(query) ||
      model.metadata_?.modules?.some(m => m.toLowerCase().includes(query))
    );
  });

  // Group models by module
  const modelsByModule = filteredModels?.reduce((acc, model) => {
    const modules = model.metadata_?.modules || ['Other'];
    modules.forEach(module => {
      if (!acc[module]) acc[module] = [];
      acc[module].push(model);
    });
    return acc;
  }, {} as Record<string, ObjectModel[]>);

  const selectedModelData = objectModels?.find(m => m.code === selectedModel);

  const handleModelClick = (modelCode: string) => {
    setSelectedModel(modelCode);
  };

  const handleViewFullDetails = (modelCode: string) => {
    navigate(`/object-model/${modelCode}`);
  };

  if (isLoading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100%' }}>
        <CircularProgress />
      </Box>
    );
  }

  if (error) {
    return (
      <Alert severity="error">
        Failed to load object models. Please check if the metadata service is running.
      </Alert>
    );
  }

  const leftPanel = (
    <Box sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
      {/* Header */}
      <Box sx={{ p: 2, borderBottom: 1, borderColor: 'divider' }}>
        <Stack direction="row" spacing={1} alignItems="center" sx={{ mb: 2 }}>
          <AccountTreeIcon color="primary" />
          <Typography variant="h5" fontWeight="bold">
            Object Models
          </Typography>
        </Stack>
        
        {/* Search */}
        <TextField
          fullWidth
          size="small"
          placeholder="Search object models..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <SearchIcon />
              </InputAdornment>
            ),
          }}
        />
        
        {/* Stats */}
        <Typography variant="caption" color="text.secondary" sx={{ mt: 1, display: 'block' }}>
          {filteredModels?.length || 0} object models
        </Typography>
      </Box>

      {/* Models List */}
      <Box sx={{ flex: 1, overflow: 'auto' }}>
        {modelsByModule && Object.entries(modelsByModule).map(([module, models]) => (
          <Box key={module}>
            <Box sx={{ px: 2, py: 1, bgcolor: 'grey.50', borderBottom: 1, borderColor: 'divider' }}>
              <Typography variant="subtitle2" fontWeight="bold" color="primary">
                {module}
              </Typography>
            </Box>
            <List dense>
              {models.map((model) => (
                <ListItem key={model.code} disablePadding>
                  <ListItemButton
                    selected={selectedModel === model.code}
                    onClick={() => handleModelClick(model.code)}
                  >
                    <ListItemText
                      primary={
                        <Stack direction="row" spacing={1} alignItems="center">
                          <StorageIcon fontSize="small" color="action" />
                          <Typography variant="body2" fontWeight="medium">
                            {model.display_name || model.name}
                          </Typography>
                        </Stack>
                      }
                      secondary={
                        <Typography variant="caption" color="text.secondary" noWrap>
                          {model.description}
                        </Typography>
                      }
                    />
                  </ListItemButton>
                </ListItem>
              ))}
            </List>
          </Box>
        ))}
      </Box>
    </Box>
  );

  const rightPanel = selectedModelData ? (
    <Box sx={{ height: '100%', overflow: 'auto', p: 3 }}>
      {/* Header */}
      <Stack spacing={2}>
        <Stack direction="row" justifyContent="space-between" alignItems="flex-start">
          <Box>
            <Typography variant="h5" fontWeight="bold" gutterBottom>
              {selectedModelData.display_name || selectedModelData.name}
            </Typography>
            <Typography variant="body2" color="text.secondary" paragraph>
              {selectedModelData.description}
            </Typography>
          </Box>
          <Chip label={selectedModelData.code} size="small" />
        </Stack>

        {/* Modules */}
        {selectedModelData.metadata_?.modules && selectedModelData.metadata_.modules.length > 0 && (
          <Box>
            <Typography variant="subtitle2" color="text.secondary" gutterBottom>
              Used in Modules
            </Typography>
            <Stack direction="row" spacing={1} flexWrap="wrap">
              {selectedModelData.metadata_.modules.map((module) => (
                <Chip key={module} label={module} size="small" variant="outlined" />
              ))}
            </Stack>
          </Box>
        )}

        <Divider />

        {/* Technical Details */}
        <Box>
          <Typography variant="subtitle2" fontWeight="bold" gutterBottom>
            Technical Details
          </Typography>
          <Stack spacing={1}>
            <Box>
              <Typography variant="caption" color="text.secondary">
                Table Name
              </Typography>
              <Typography variant="body2" fontFamily="monospace">
                {selectedModelData.table_name}
              </Typography>
            </Box>
            <Box>
              <Typography variant="caption" color="text.secondary">
                Schema
              </Typography>
              <Typography variant="body2" fontFamily="monospace">
                {typeof selectedModelData.table_schema === 'string' 
                  ? selectedModelData.table_schema 
                  : 'public'}
              </Typography>
            </Box>
          </Stack>
        </Box>

        <Divider />

        {/* Relationships Table */}
        {selectedModelData.schema_definition && (() => {
          const relationships = parseRelationships(selectedModelData.schema_definition, selectedModelData.code);
          return relationships.length > 0 && (
            <Box>
              <Typography variant="subtitle2" fontWeight="bold" gutterBottom>
                Relationships ({relationships.length})
              </Typography>
              <TableContainer component={Paper} variant="outlined">
                <Table size="small">
                  <TableHead>
                    <TableRow>
                      <TableCell><strong>From</strong></TableCell>
                      <TableCell align="center"><strong>Direction</strong></TableCell>
                      <TableCell><strong>To</strong></TableCell>
                      <TableCell><strong>Type</strong></TableCell>
                      <TableCell><strong>Cardinality</strong></TableCell>
                      <TableCell><strong>Relationship</strong></TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {relationships.map((rel, index) => (
                      <TableRow key={index} hover>
                        <TableCell>
                          <Typography variant="body2" fontWeight="medium">
                            {rel.from}
                          </Typography>
                        </TableCell>
                        <TableCell align="center">
                          {rel.direction === 'forward' && <ArrowForwardIcon fontSize="small" color="action" />}
                          {rel.direction === 'backward' && <ArrowBackIcon fontSize="small" color="action" />}
                          {rel.direction === 'bidirectional' && <SwapHorizIcon fontSize="small" color="action" />}
                        </TableCell>
                        <TableCell>
                          <Typography variant="body2" fontWeight="medium">
                            {rel.to}
                          </Typography>
                        </TableCell>
                        <TableCell>
                          <Chip 
                            label={rel.type} 
                            size="small" 
                            color={
                              rel.type === 'composition' ? 'error' :
                              rel.type === 'aggregation' ? 'warning' :
                              rel.type === 'generalization' ? 'info' :
                              rel.type === 'dependency' ? 'secondary' :
                              'default'
                            }
                            variant="outlined" 
                          />
                        </TableCell>
                        <TableCell>
                          <Typography variant="caption" color="text.secondary" fontFamily="monospace">
                            {rel.cardinality || '-'}
                          </Typography>
                        </TableCell>
                        <TableCell>
                          <Typography variant="body2" color="text.secondary">
                            {rel.label || '-'}
                          </Typography>
                        </TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </TableContainer>
            </Box>
          );
        })()}

        <Divider />

        {/* UML Diagram */}
        {selectedModelData.schema_definition && (
          <Box>
            <Typography variant="subtitle2" fontWeight="bold" gutterBottom>
              Entity Relationships Diagram
            </Typography>
            <Paper variant="outlined" sx={{ p: 2, bgcolor: 'grey.50' }}>
              <ObjectModelDiagram
                schemaDefinition={selectedModelData.schema_definition}
                highlightEntity={selectedModelData.code}
              />
            </Paper>
          </Box>
        )}

        {/* View Full Details Button */}
        <Box sx={{ pt: 2 }}>
          <Typography
            variant="body2"
            color="primary"
            sx={{ cursor: 'pointer', textDecoration: 'underline' }}
            onClick={() => handleViewFullDetails(selectedModelData.code)}
          >
            View Full Details →
          </Typography>
        </Box>
      </Stack>
    </Box>
  ) : (
    <Box sx={{ height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <Stack spacing={2} alignItems="center">
        <AccountTreeIcon sx={{ fontSize: 64, color: 'text.disabled' }} />
        <Typography variant="h6" color="text.secondary">
          Select an object model to view details
        </Typography>
      </Stack>
    </Box>
  );

  return (
    <Box sx={{ height: '100%' }}>
      <ResizableSplitPanel
        leftPanel={leftPanel}
        rightPanel={rightPanel}
        defaultLeftWidth={50}
        minLeftWidth={30}
      />
    </Box>
  );
}
