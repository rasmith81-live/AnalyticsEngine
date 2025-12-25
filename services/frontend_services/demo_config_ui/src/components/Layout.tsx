import { 
  Box, 
  AppBar, 
  Toolbar, 
  Typography, 
  Drawer, 
  List, 
  ListItem, 
  ListItemButton, 
  ListItemIcon, 
  ListItemText,
  Divider
} from '@mui/material';
import { ReactNode } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import DashboardIcon from '@mui/icons-material/Dashboard';
import SettingsIcon from '@mui/icons-material/Settings';
import AccountTreeIcon from '@mui/icons-material/AccountTree';
import StorageIcon from '@mui/icons-material/Storage';
import AssignmentIcon from '@mui/icons-material/Assignment';
import AdminPanelSettingsIcon from '@mui/icons-material/AdminPanelSettings';
import PolicyIcon from '@mui/icons-material/Policy';
import ModelTrainingIcon from '@mui/icons-material/ModelTraining';
import MonitorHeartIcon from '@mui/icons-material/MonitorHeart';
import UploadFileIcon from '@mui/icons-material/UploadFile';

interface LayoutProps {
  children: ReactNode;
}

const drawerWidth = 240;

const menuItems = [
  { text: 'Demo', icon: <DashboardIcon />, path: '/demo' },
  { text: 'KPI Configuration', icon: <SettingsIcon />, path: '/config' },
  { text: 'Excel Import', icon: <UploadFileIcon />, path: '/excel-import' },
  { text: 'Ontology Studio', icon: <AccountTreeIcon />, path: '/ontology-studio' },
  { text: 'Simulation Controller', icon: <SettingsIcon />, path: '/simulation' },
  { text: 'ML Model Registry', icon: <ModelTrainingIcon />, path: '/ml-registry' },
  { text: 'System Monitor', icon: <MonitorHeartIcon />, path: '/system-monitor' },
  { text: 'Object Models', icon: <AccountTreeIcon />, path: '/object-models' },
  { text: 'Data Sources', icon: <StorageIcon />, path: '/data-sources' },
  { text: 'Service Proposal', icon: <AssignmentIcon />, path: '/proposal' },
  { text: 'Governance', icon: <PolicyIcon />, path: '/governance' },
  { text: 'Admin', icon: <AdminPanelSettingsIcon />, path: '/admin' },
];

export default function Layout({ children }: LayoutProps) {
  const navigate = useNavigate();
  const location = useLocation();

  return (
    <Box sx={{ display: 'flex', minHeight: '100vh', width: '100vw', maxWidth: '100%', overflow: 'hidden' }}>
      <AppBar position="fixed" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Analytics Engine - Demo & Config
          </Typography>
          <Typography variant="body2" sx={{ mr: 2 }}>
            v1.0.0
          </Typography>
        </Toolbar>
      </AppBar>
      
      <Drawer
        variant="permanent"
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          '& .MuiDrawer-paper': {
            width: drawerWidth,
            boxSizing: 'border-box',
          },
        }}
      >
        <Toolbar />
        <Box sx={{ overflow: 'auto' }}>
          <List>
            {menuItems.map((item) => (
              <ListItem key={item.text} disablePadding>
                <ListItemButton
                  selected={location.pathname === item.path}
                  onClick={() => navigate(item.path)}
                >
                  <ListItemIcon>
                    {item.icon}
                  </ListItemIcon>
                  <ListItemText primary={item.text} />
                </ListItemButton>
              </ListItem>
            ))}
          </List>
          <Divider />
          <Box sx={{ p: 2 }}>
            <Typography variant="caption" color="text.secondary">
              Backend Services
            </Typography>
            <Typography variant="body2" sx={{ fontSize: '0.75rem', mt: 1 }}>
              • Metadata: :8020
            </Typography>
            <Typography variant="body2" sx={{ fontSize: '0.75rem' }}>
              • Calc Engine: :8021
            </Typography>
            <Typography variant="body2" sx={{ fontSize: '0.75rem' }}>
              • Config: :8022
            </Typography>
          </Box>
        </Box>
      </Drawer>
      
      <Box component="main" sx={{ flexGrow: 1, p: 3, minWidth: 0, overflow: 'hidden' }}>
        <Toolbar />
        {children}
      </Box>
    </Box>
  );
}
