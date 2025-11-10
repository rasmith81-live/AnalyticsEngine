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
import DescriptionIcon from '@mui/icons-material/Description';
import AccountTreeIcon from '@mui/icons-material/AccountTree';
import AnalyticsIcon from '@mui/icons-material/Analytics';
import StorageIcon from '@mui/icons-material/Storage';
import AssignmentIcon from '@mui/icons-material/Assignment';

interface LayoutProps {
  children: ReactNode;
}

const drawerWidth = 240;

const menuItems = [
  { text: 'Demo', icon: <DashboardIcon />, path: '/demo' },
  { text: 'Configuration', icon: <SettingsIcon />, path: '/config' },
  { text: 'KPI Details', icon: <DescriptionIcon />, path: '/kpi/PERFECT_ORDER_FULFILLMENT' },
  { text: 'Object Models', icon: <AccountTreeIcon />, path: '/object-model/ORDER' },
  { text: 'Required Objects', icon: <AnalyticsIcon />, path: '/required-objects' },
  { text: 'Data Sources', icon: <StorageIcon />, path: '/data-sources' },
  { text: 'Service Proposal', icon: <AssignmentIcon />, path: '/proposal' },
];

export default function Layout({ children }: LayoutProps) {
  const navigate = useNavigate();
  const location = useLocation();

  return (
    <Box sx={{ display: 'flex', minHeight: '100vh' }}>
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
      
      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
        <Toolbar />
        {children}
      </Box>
    </Box>
  );
}
