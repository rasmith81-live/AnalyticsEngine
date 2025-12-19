import React, { useState } from 'react';
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
  List,
  ListItem,
  ListItemText,
  IconButton,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Chip,
  Divider,
  Stack
} from '@mui/material';
import {
  Edit as EditIcon,
  Delete as DeleteIcon,
  Add as AddIcon,
  History as HistoryIcon,
  AccountTree as GraphIcon,
  Schema as SchemaIcon,
  Save as SaveIcon
} from '@mui/icons-material';

// Mock Data
const INITIAL_ENTITIES = [
  { id: 'ent_customer', name: 'Customer', attributes: ['customer_id', 'name', 'segment', 'signup_date'] },
  { id: 'ent_order', name: 'Order', attributes: ['order_id', 'customer_id', 'order_date', 'total_amount'] },
  { id: 'ent_product', name: 'Product', attributes: ['product_id', 'sku', 'price', 'category'] },
  { id: 'ent_inventory', name: 'Inventory', attributes: ['inventory_id', 'product_id', 'warehouse_id', 'quantity'] },
];

const INITIAL_RELATIONSHIPS = [
  { id: 'rel_cust_ord', source: 'Customer', target: 'Order', type: 'One-to-Many' },
  { id: 'rel_ord_prod', source: 'Order', target: 'Product', type: 'Many-to-Many' },
  { id: 'rel_prod_inv', source: 'Product', target: 'Inventory', type: 'One-to-Many' },
];

const HISTORY_LOG = [
  { id: 1, action: 'Added Attribute', detail: 'added "email" to Customer', user: 'admin', timestamp: '2023-12-18 10:30' },
  { id: 2, action: 'Created Entity', detail: 'created "Supplier" entity', user: 'admin', timestamp: '2023-12-17 14:15' },
  { id: 3, action: 'Modified Relationship', detail: 'changed Order-Product to Many-to-Many', user: 'system', timestamp: '2023-12-16 09:00' },
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
  const [value, setValue] = useState(0);
  const [entities, setEntities] = useState(INITIAL_ENTITIES);
  const [relationships, setRelationships] = useState(INITIAL_RELATIONSHIPS);
  
  // Entity Dialog State
  const [openEntityDialog, setOpenEntityDialog] = useState(false);
  const [currentEntity, setCurrentEntity] = useState({ name: '', attributes: '' });
  const [editingId, setEditingId] = useState<string | null>(null);

  // Relationship Dialog State
  const [openRelDialog, setOpenRelDialog] = useState(false);
  const [currentRel, setCurrentRel] = useState({ source: '', target: '', type: 'One-to-Many' });

  const handleChange = (_: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
  };

  const handleSaveEntity = () => {
    const attributesArray = currentEntity.attributes.split(',').map(s => s.trim()).filter(Boolean);
    
    if (editingId) {
      setEntities(entities.map(e => e.id === editingId ? { ...e, name: currentEntity.name, attributes: attributesArray } : e));
    } else {
      setEntities([...entities, {
        id: `ent_${currentEntity.name.toLowerCase().replace(/\s+/g, '_')}`,
        name: currentEntity.name,
        attributes: attributesArray
      }]);
    }
    setOpenEntityDialog(false);
    setEditingId(null);
    setCurrentEntity({ name: '', attributes: '' });
  };

  const handleEditEntity = (entity: any) => {
    setEditingId(entity.id);
    setCurrentEntity({ name: entity.name, attributes: entity.attributes.join(', ') });
    setOpenEntityDialog(true);
  };

  const handleDeleteEntity = (id: string) => {
    if (window.confirm('Delete this entity?')) {
      setEntities(entities.filter(e => e.id !== id));
    }
  };

  const handleSaveRelationship = () => {
    setRelationships([...relationships, {
      id: `rel_${Date.now()}`,
      source: currentRel.source,
      target: currentRel.target,
      type: currentRel.type
    }]);
    setOpenRelDialog(false);
    setCurrentRel({ source: '', target: '', type: 'One-to-Many' });
  };

  const handleDeleteRelationship = (id: string) => {
    setRelationships(relationships.filter(r => r.id !== id));
  };

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
        <Typography variant="h4">
          Ontology Studio
        </Typography>
        <Button variant="outlined" startIcon={<SaveIcon />}>
          Commit Changes
        </Button>
      </Box>

      <Paper sx={{ width: '100%', mb: 2 }}>
        <Tabs value={value} onChange={handleChange} aria-label="ontology tabs">
          <Tab icon={<SchemaIcon />} label="Entities" />
          <Tab icon={<GraphIcon />} label="Relationships" />
          <Tab icon={<HistoryIcon />} label="Version History" />
        </Tabs>
      </Paper>

      {/* Entity Editor */}
      <TabPanel value={value} index={0}>
        <Box sx={{ display: 'flex', justifyContent: 'flex-end', mb: 2 }}>
          <Button variant="contained" startIcon={<AddIcon />} onClick={() => {
            setEditingId(null);
            setCurrentEntity({ name: '', attributes: '' });
            setOpenEntityDialog(true);
          }}>
            New Entity
          </Button>
        </Box>
        <Grid container spacing={3}>
          {entities.map((entity) => (
            <Grid item xs={12} md={6} lg={4} key={entity.id}>
              <Card variant="outlined">
                <CardContent>
                  <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 1 }}>
                    <Typography variant="h6">{entity.name}</Typography>
                    <Box>
                      <IconButton size="small" onClick={() => handleEditEntity(entity)}>
                        <EditIcon fontSize="small" />
                      </IconButton>
                      <IconButton size="small" onClick={() => handleDeleteEntity(entity.id)} color="error">
                        <DeleteIcon fontSize="small" />
                      </IconButton>
                    </Box>
                  </Box>
                  <Typography variant="caption" color="text.secondary" gutterBottom>
                    ID: {entity.id}
                  </Typography>
                  <Divider sx={{ my: 1 }} />
                  <Typography variant="subtitle2" sx={{ mb: 1 }}>Attributes:</Typography>
                  <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
                    {entity.attributes.map(attr => (
                      <Chip key={attr} label={attr} size="small" variant="outlined" />
                    ))}
                  </Box>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      </TabPanel>

      {/* Relationship Builder */}
      <TabPanel value={value} index={1}>
        <Box sx={{ display: 'flex', justifyContent: 'flex-end', mb: 2 }}>
          <Button variant="contained" startIcon={<AddIcon />} onClick={() => setOpenRelDialog(true)}>
            Add Relationship
          </Button>
        </Box>
        <Paper variant="outlined">
          <List>
            {relationships.map((rel) => (
              <React.Fragment key={rel.id}>
                <ListItem
                  secondaryAction={
                    <IconButton edge="end" aria-label="delete" onClick={() => handleDeleteRelationship(rel.id)}>
                      <DeleteIcon />
                    </IconButton>
                  }
                >
                  <ListItemText
                    primary={
                      <Stack direction="row" alignItems="center" spacing={2}>
                        <Typography variant="subtitle1" fontWeight="bold">{rel.source}</Typography>
                        <Chip label={rel.type} size="small" color="primary" variant="outlined" />
                        <Typography variant="subtitle1" fontWeight="bold">{rel.target}</Typography>
                      </Stack>
                    }
                    secondary={`ID: ${rel.id}`}
                  />
                </ListItem>
                <Divider />
              </React.Fragment>
            ))}
            {relationships.length === 0 && (
              <ListItem>
                <ListItemText primary="No relationships defined." />
              </ListItem>
            )}
          </List>
        </Paper>
      </TabPanel>

      {/* Version History */}
      <TabPanel value={value} index={2}>
        <List>
          {HISTORY_LOG.map((log) => (
            <ListItem key={log.id}>
              <ListItemText 
                primary={log.action} 
                secondary={
                  <React.Fragment>
                    <Typography component="span" variant="body2" color="text.primary">
                      {log.user}
                    </Typography>
                    {` — ${log.detail} (${log.timestamp})`}
                  </React.Fragment>
                } 
              />
            </ListItem>
          ))}
        </List>
      </TabPanel>

      {/* Entity Dialog */}
      <Dialog open={openEntityDialog} onClose={() => setOpenEntityDialog(false)} maxWidth="sm" fullWidth>
        <DialogTitle>{editingId ? 'Edit Entity' : 'New Entity'}</DialogTitle>
        <DialogContent>
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2, mt: 1 }}>
            <TextField
              label="Entity Name"
              value={currentEntity.name}
              onChange={(e) => setCurrentEntity({ ...currentEntity, name: e.target.value })}
              fullWidth
            />
            <TextField
              label="Attributes (comma separated)"
              value={currentEntity.attributes}
              onChange={(e) => setCurrentEntity({ ...currentEntity, attributes: e.target.value })}
              fullWidth
              multiline
              rows={3}
              helperText="e.g. id, name, created_at"
            />
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenEntityDialog(false)}>Cancel</Button>
          <Button variant="contained" onClick={handleSaveEntity}>Save</Button>
        </DialogActions>
      </Dialog>

      {/* Relationship Dialog */}
      <Dialog open={openRelDialog} onClose={() => setOpenRelDialog(false)} maxWidth="xs" fullWidth>
        <DialogTitle>Add Relationship</DialogTitle>
        <DialogContent>
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2, mt: 1 }}>
            <FormControl fullWidth>
              <InputLabel>Source Entity</InputLabel>
              <Select
                value={currentRel.source}
                label="Source Entity"
                onChange={(e) => setCurrentRel({ ...currentRel, source: e.target.value })}
              >
                {entities.map(e => <MenuItem key={e.id} value={e.name}>{e.name}</MenuItem>)}
              </Select>
            </FormControl>

            <FormControl fullWidth>
              <InputLabel>Relationship Type</InputLabel>
              <Select
                value={currentRel.type}
                label="Relationship Type"
                onChange={(e) => setCurrentRel({ ...currentRel, type: e.target.value })}
              >
                <MenuItem value="One-to-One">One-to-One</MenuItem>
                <MenuItem value="One-to-Many">One-to-Many</MenuItem>
                <MenuItem value="Many-to-One">Many-to-One</MenuItem>
                <MenuItem value="Many-to-Many">Many-to-Many</MenuItem>
              </Select>
            </FormControl>

            <FormControl fullWidth>
              <InputLabel>Target Entity</InputLabel>
              <Select
                value={currentRel.target}
                label="Target Entity"
                onChange={(e) => setCurrentRel({ ...currentRel, target: e.target.value })}
              >
                {entities.map(e => <MenuItem key={e.id} value={e.name}>{e.name}</MenuItem>)}
              </Select>
            </FormControl>
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenRelDialog(false)}>Cancel</Button>
          <Button variant="contained" onClick={handleSaveRelationship}>Add</Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
}
