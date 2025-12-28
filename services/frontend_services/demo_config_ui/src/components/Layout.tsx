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
  Divider,
  Collapse
} from '@mui/material';
import { ReactNode, useState } from 'react';
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
import BarChartIcon from '@mui/icons-material/BarChart';
import ChatIcon from '@mui/icons-material/Chat';
import CategoryIcon from '@mui/icons-material/Category';
import SlideshowIcon from '@mui/icons-material/Slideshow';
import TuneIcon from '@mui/icons-material/Tune';
import InsightsIcon from '@mui/icons-material/Insights';
import RocketLaunchIcon from '@mui/icons-material/RocketLaunch';
import TransformIcon from '@mui/icons-material/Transform';
import TerminalIcon from '@mui/icons-material/Terminal';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';

interface LayoutProps {
  children: ReactNode;
}

const drawerWidth = 280;

interface MenuItem {
  text: string;
  icon: ReactNode;
  path?: string;
  children?: MenuItem[];
}

const menuItems: MenuItem[] = [
  { text: 'Start', icon: <DashboardIcon />, path: '/demo' },
  {
    text: 'KPI Management',
    icon: <BarChartIcon />,
    children: [
      { text: 'Excel Import', icon: <UploadFileIcon />, path: '/excel-import' },
      { text: 'Ontology Studio', icon: <AccountTreeIcon />, path: '/ontology-studio' },
      { text: 'ML Model Registry', icon: <ModelTrainingIcon />, path: '/ml-registry' },
    ]
  },
  {
    text: 'Client Configuration',
    icon: <SettingsIcon />,
    children: [
      { text: 'Conversation Service', icon: <ChatIcon />, path: '/conversation-service' },
      { text: 'KPI Configuration', icon: <SettingsIcon />, path: '/config' },
      { text: 'Object Models', icon: <CategoryIcon />, path: '/object-models' },
    ]
  },
  {
    text: 'Client Demo',
    icon: <SlideshowIcon />,
    children: [
      { text: 'Data Sources', icon: <StorageIcon />, path: '/data-sources' },
      { text: 'Simulation Controller', icon: <TuneIcon />, path: '/simulation' },
      { text: 'Analytics Demo', icon: <InsightsIcon />, path: '/analytics-demo' },
      { text: 'Service Proposal', icon: <AssignmentIcon />, path: '/proposal' },
    ]
  },
  {
    text: 'Deployment',
    icon: <RocketLaunchIcon />,
    children: [
      { text: 'Source to Target Mapping', icon: <TransformIcon />, path: '/mapping' },
      { text: 'Governance', icon: <PolicyIcon />, path: '/governance' },
      { text: 'Admin', icon: <AdminPanelSettingsIcon />, path: '/admin' },
      { text: 'SQL', icon: <TerminalIcon />, path: '/sql' },
    ]
  },
  { text: 'System Monitor', icon: <MonitorHeartIcon />, path: '/system-monitor' },
];

export default function Layout({ children }: LayoutProps) {
  const navigate = useNavigate();
  const location = useLocation();
  const [openMenus, setOpenMenus] = useState<{ [key: string]: boolean }>({
    'KPI Management': true,
    'Client Configuration': false,
    'Client Demo': false,
    'Deployment': false,
  });

  const handleToggle = (text: string) => {
    setOpenMenus(prev => ({
      ...prev,
      [text]: !prev[text]
    }));
  };

  const handleNavigation = (path?: string) => {
    if (path) navigate(path);
  };

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
              <Box key={item.text}>
                <ListItem disablePadding>
                  <ListItemButton
                    selected={!!item.path && location.pathname === item.path}
                    onClick={() => item.children ? handleToggle(item.text) : handleNavigation(item.path)}
                  >
                    <ListItemIcon>
                      {item.icon}
                    </ListItemIcon>
                    <ListItemText primary={item.text} />
                    {item.children && (openMenus[item.text] ? <ExpandLess /> : <ExpandMore />)}
                  </ListItemButton>
                </ListItem>
                {item.children && (
                  <Collapse in={openMenus[item.text]} timeout="auto" unmountOnExit>
                    <List component="div" disablePadding>
                      {item.children.map((child) => (
                        <ListItemButton
                          key={child.text}
                          sx={{ pl: 4 }}
                          selected={!!child.path && location.pathname === child.path}
                          onClick={() => handleNavigation(child.path)}
                        >
                          <ListItemIcon>
                            {child.icon}
                          </ListItemIcon>
                          <ListItemText primary={child.text} />
                        </ListItemButton>
                      ))}
                    </List>
                  </Collapse>
                )}
              </Box>
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
