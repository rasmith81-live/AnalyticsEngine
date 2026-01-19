import React, { useState } from 'react';
import {
  Typography,
  Paper,
  Box,
  Tabs,
  Tab,
  Grid,
  Card,
  CardContent,
  CardHeader,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  LinearProgress,
  Chip,
  Button,
  List,
  ListItem,
  ListItemText,
  ListItemIcon,
  Avatar,
  TextField,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Divider,
} from '@mui/material';
import {
  VerifiedUser as QualityIcon,
  AccountTree as LineageIcon,
  Security as AccessIcon,
  CheckCircle as PassIcon,
  Warning as WarningIcon,
  Error as FailIcon,
  Add as AddIcon,
  Edit as EditIcon,
  Delete as DeleteIcon,
} from '@mui/icons-material';
import { governanceApi, QualityMetric, User, LineageGraph as ILineageGraph } from '../api/governanceApi';
import LineageGraph from '../components/LineageGraph';

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
      id={`governance-tabpanel-${index}`}
      aria-labelledby={`governance-tab-${index}`}
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

const ROLES = ['Admin', 'Editor', 'Viewer', 'Analyst'];

export default function GovernancePage() {
  const [value, setValue] = useState(0);
  const [qualityMetrics, setQualityMetrics] = useState<QualityMetric[]>([]);
  const [users, setUsers] = useState<User[]>([]);
  const [lineageData, setLineageData] = useState<ILineageGraph | null>(null);
  const [loading, setLoading] = useState(false);
  
  const [openUserDialog, setOpenUserDialog] = useState(false);
  const [newUser, setNewUser] = useState({ name: '', email: '', role: 'Viewer' });

  React.useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    setLoading(true);
    try {
      const [metricsData, usersData, lineage] = await Promise.all([
        governanceApi.getQualityMetrics(),
        governanceApi.getUsers(),
        governanceApi.getLineage()
      ]);
      setQualityMetrics(metricsData);
      setUsers(usersData);
      setLineageData(lineage);
    } catch (error) {
      console.error('Failed to load governance data:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (_: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
  };

  const handleAddUser = async () => {
    try {
      const added = await governanceApi.addUser({
        name: newUser.name,
        email: newUser.email,
        role: newUser.role as any
      });
      setUsers([...users, added]);
      setOpenUserDialog(false);
      setNewUser({ name: '', email: '', role: 'Viewer' });
    } catch (error) {
      console.error('Failed to add user:', error);
    }
  };

  const handleDeleteUser = async (id: number) => {
    if (!window.confirm('Are you sure you want to delete this user?')) return;
    try {
      await governanceApi.deleteUser(id);
      setUsers(users.filter(u => u.id !== id));
    } catch (error) {
      console.error('Failed to delete user:', error);
    }
  };

  const getQualityColor = (value: number) => {
    if (value >= 98) return 'success';
    if (value >= 90) return 'warning';
    return 'error';
  };

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'pass': return <PassIcon color="success" />;
      case 'warning': return <WarningIcon color="warning" />;
      case 'fail': return <FailIcon color="error" />;
      default: return <PassIcon />;
    }
  };

  return (
    <Box sx={{ width: '100%' }}>
      <Typography variant="h4" gutterBottom>
        Data Governance
      </Typography>
      
      {loading && <LinearProgress sx={{ mb: 2 }} />}

      <Paper sx={{ width: '100%', mb: 2 }}>
        <Tabs value={value} onChange={handleChange} aria-label="governance tabs">
          <Tab icon={<QualityIcon />} label="Data Quality" />
          <Tab icon={<LineageIcon />} label="Data Lineage" />
          <Tab icon={<AccessIcon />} label="Access Control" />
        </Tabs>
      </Paper>

      {/* Data Quality */}
      <TabPanel value={value} index={0}>
        <Grid container spacing={3}>
          <Grid item xs={12}>
            <Card>
              <CardHeader title="Data Quality Overview" />
              <CardContent>
                <Grid container spacing={3} sx={{ mb: 4 }}>
                  <Grid item xs={12} md={3}>
                    <Paper sx={{ p: 2, textAlign: 'center', bgcolor: 'success.light', color: 'success.contrastText' }}>
                      <Typography variant="h4">96.5%</Typography>
                      <Typography variant="body2">Overall Score</Typography>
                    </Paper>
                  </Grid>
                  <Grid item xs={12} md={3}>
                    <Paper sx={{ p: 2, textAlign: 'center' }}>
                      <Typography variant="h4">12</Typography>
                      <Typography variant="body2" color="text.secondary">Tables Monitored</Typography>
                    </Paper>
                  </Grid>
                  <Grid item xs={12} md={3}>
                    <Paper sx={{ p: 2, textAlign: 'center' }}>
                      <Typography variant="h4">45k</Typography>
                      <Typography variant="body2" color="text.secondary">Rows Validated</Typography>
                    </Paper>
                  </Grid>
                  <Grid item xs={12} md={3}>
                    <Paper sx={{ p: 2, textAlign: 'center' }}>
                      <Typography variant="h4">3</Typography>
                      <Typography variant="body2" color="text.secondary">Open Issues</Typography>
                    </Paper>
                  </Grid>
                </Grid>

                <TableContainer>
                  <Table>
                    <TableHead>
                      <TableRow>
                        <TableCell>Table Name</TableCell>
                        <TableCell align="center">Completeness</TableCell>
                        <TableCell align="center">Accuracy</TableCell>
                        <TableCell align="center">Consistency</TableCell>
                        <TableCell align="center">Timeliness</TableCell>
                        <TableCell align="center">Status</TableCell>
                      </TableRow>
                    </TableHead>
                    <TableBody>
                      {qualityMetrics.map((row) => (
                        <TableRow key={row.table}>
                          <TableCell component="th" scope="row">
                            {row.table}
                          </TableCell>
                          <TableCell align="center">
                            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                              <LinearProgress variant="determinate" value={row.completeness} color={getQualityColor(row.completeness)} sx={{ flexGrow: 1 }} />
                              <Typography variant="body2">{row.completeness}%</Typography>
                            </Box>
                          </TableCell>
                          <TableCell align="center">
                            <Typography variant="body2" color={`text.${getQualityColor(row.accuracy)}`}>
                              {row.accuracy}%
                            </Typography>
                          </TableCell>
                          <TableCell align="center">
                            <Typography variant="body2" color={`text.${getQualityColor(row.consistency)}`}>
                              {row.consistency}%
                            </Typography>
                          </TableCell>
                          <TableCell align="center">
                            <Typography variant="body2" color={`text.${getQualityColor(row.timeliness)}`}>
                              {row.timeliness}%
                            </Typography>
                          </TableCell>
                          <TableCell align="center">
                            {getStatusIcon(row.status)}
                          </TableCell>
                        </TableRow>
                      ))}
                    </TableBody>
                  </Table>
                </TableContainer>
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      </TabPanel>

      {/* Data Lineage */}
      <TabPanel value={value} index={1}>
        <Card>
          <CardHeader title="Data Lineage Explorer" />
          <CardContent>
            {lineageData ? (
              <LineageGraph data={lineageData} />
            ) : (
              <Box sx={{ p: 5, textAlign: 'center' }}>
                <Typography>Loading Lineage Data...</Typography>
              </Box>
            )}
          </CardContent>
        </Card>
      </TabPanel>

      {/* Access Control */}
      <TabPanel value={value} index={2}>
        <Box sx={{ display: 'flex', justifyContent: 'flex-end', mb: 2 }}>
          <Button variant="contained" startIcon={<AddIcon />} onClick={() => setOpenUserDialog(true)}>
            Add User
          </Button>
        </Box>
        <Card>
          <CardHeader title="User Management" />
          <CardContent>
            <List>
              {users.map((user) => (
                <React.Fragment key={user.id}>
                  <ListItem
                    secondaryAction={
                      <Box>
                        <Button startIcon={<EditIcon />} size="small">Edit</Button>
                        <Button 
                          startIcon={<DeleteIcon />} 
                          size="small" 
                          color="error"
                          onClick={() => handleDeleteUser(user.id)}
                        >
                          Remove
                        </Button>
                      </Box>
                    }
                  >
                    <ListItemIcon>
                      <Avatar>{user.name[0]}</Avatar>
                    </ListItemIcon>
                    <ListItemText
                      primary={
                        <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
                          {user.name}
                          <Chip label={user.role} size="small" color="primary" variant="outlined" />
                          <Chip 
                            label={user.status} 
                            size="small" 
                            color={user.status === 'Active' ? 'success' : 'default'} 
                            variant="outlined" 
                          />
                        </Box>
                      }
                      secondary={user.email}
                    />
                  </ListItem>
                  <Divider component="li" />
                </React.Fragment>
              ))}
            </List>
          </CardContent>
        </Card>
      </TabPanel>

      {/* Add User Dialog */}
      <Dialog open={openUserDialog} onClose={() => setOpenUserDialog(false)}>
        <DialogTitle>Add New User</DialogTitle>
        <DialogContent sx={{ minWidth: 400 }}>
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2, mt: 1 }}>
            <TextField
              label="Full Name"
              fullWidth
              value={newUser.name}
              onChange={(e) => setNewUser({ ...newUser, name: e.target.value })}
            />
            <TextField
              label="Email Address"
              fullWidth
              value={newUser.email}
              onChange={(e) => setNewUser({ ...newUser, email: e.target.value })}
            />
            <FormControl fullWidth>
              <InputLabel>Role</InputLabel>
              <Select
                value={newUser.role}
                label="Role"
                onChange={(e) => setNewUser({ ...newUser, role: e.target.value })}
              >
                {ROLES.map((role) => (
                  <MenuItem key={role} value={role}>{role}</MenuItem>
                ))}
              </Select>
            </FormControl>
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenUserDialog(false)}>Cancel</Button>
          <Button variant="contained" onClick={handleAddUser}>Add User</Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
}
