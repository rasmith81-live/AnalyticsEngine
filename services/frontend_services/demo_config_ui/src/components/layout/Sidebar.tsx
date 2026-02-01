import { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { cn } from '../../lib/utils';
import {
  LayoutDashboard,
  Palette,
  BarChart3,
  Lightbulb,
  FileText,
  Rocket,
  FileSpreadsheet,
  MessageSquare,
  Settings,
  Boxes,
  SlidersHorizontal,
  TrendingUp,
  FileCheck,
  Database,
  ArrowRightLeft,
  Shield,
  Brain,
  UserCog,
  Terminal,
  Activity,
  ChevronDown,
  ChevronRight,
  Upload,
  Network,
  FlaskConical,
  HelpCircle,
  Play,
  GitBranch,
  Video,
  Workflow,
  PieChart,
  ClipboardCheck,
  ShieldCheck,
  Users,
  Plus,
  ScrollText,
} from 'lucide-react';

interface MenuItem {
  text: string;
  icon: React.ReactNode;
  path?: string;
  children?: MenuItem[];
}

const menuItems: MenuItem[] = [
  {
    text: 'Demo',
    icon: <Play className="w-5 h-5" />,
    children: [
      { text: 'Value Chain Explorer', icon: <GitBranch className="w-4 h-4" />, path: '/demo/value-chains' },
      { text: 'Training Video', icon: <Video className="w-4 h-4" />, path: '/demo/training' },
      { text: 'AI Interview', icon: <MessageSquare className="w-4 h-4" />, path: '/demo/interview' },
      { text: 'Data Simulator', icon: <Workflow className="w-4 h-4" />, path: '/demo/simulator' },
      { text: 'Sample Analytics', icon: <PieChart className="w-4 h-4" />, path: '/demo/analytics' },
      { text: 'Executive Summary', icon: <ClipboardCheck className="w-4 h-4" />, path: '/demo/summary' },
    ],
  },
  {
    text: 'Strategy Center',
    icon: <LayoutDashboard className="w-5 h-5" />,
    path: '/',
  },
  {
    text: 'Design Studio',
    icon: <Palette className="w-5 h-5" />,
    children: [
      { text: 'AI Interview', icon: <MessageSquare className="w-4 h-4" />, path: '/design/interview' },
      { text: 'Business Model', icon: <Network className="w-4 h-4" />, path: '/design/business-model' },
      { text: 'KPI Configuration', icon: <Settings className="w-4 h-4" />, path: '/design/kpis' },
      { text: 'Object Models', icon: <Boxes className="w-4 h-4" />, path: '/design/objects' },
      { text: 'Gap Analysis', icon: <HelpCircle className="w-4 h-4" />, path: '/design/gaps' },
      { text: 'Import', icon: <Upload className="w-4 h-4" />, path: '/design/import' },
    ],
  },
  {
    text: 'Analytics Hub',
    icon: <BarChart3 className="w-5 h-5" />,
    children: [
      { text: 'Simulation', icon: <SlidersHorizontal className="w-4 h-4" />, path: '/analytics/simulation' },
      { text: 'Live Dashboards', icon: <TrendingUp className="w-4 h-4" />, path: '/analytics/dashboards' },
      { text: 'Process Modeler', icon: <FlaskConical className="w-4 h-4" />, path: '/analytics/process-modeler' },
      { text: 'What-If Analysis', icon: <HelpCircle className="w-4 h-4" />, path: '/analytics/what-if' },
      { text: 'ML Models', icon: <Brain className="w-4 h-4" />, path: '/analytics/ml' },
    ],
  },
  {
    text: 'Insights Feed',
    icon: <Lightbulb className="w-5 h-5" />,
    path: '/insights',
  },
  {
    text: 'Strategy Documents',
    icon: <FileText className="w-5 h-5" />,
    path: '/documents',
  },
  {
    text: 'Deployment Center',
    icon: <Rocket className="w-5 h-5" />,
    children: [
      { text: 'Data Sources', icon: <Database className="w-4 h-4" />, path: '/deployment/sources' },
      { text: 'Mapping', icon: <ArrowRightLeft className="w-4 h-4" />, path: '/deployment/mapping' },
      { text: 'Governance', icon: <Shield className="w-4 h-4" />, path: '/deployment/governance' },
      { text: 'Admin', icon: <UserCog className="w-4 h-4" />, path: '/deployment/admin' },
      { text: 'System Monitor', icon: <Activity className="w-4 h-4" />, path: '/deployment/monitor' },
      { text: 'SQL Console', icon: <Terminal className="w-4 h-4" />, path: '/deployment/sql' },
    ],
  },
  {
    text: 'Proposal Center',
    icon: <FileSpreadsheet className="w-5 h-5" />,
    children: [
      { text: 'Estimate', icon: <FileCheck className="w-4 h-4" />, path: '/proposal/estimate' },
      { text: 'Contract', icon: <FileText className="w-4 h-4" />, path: '/proposal/contract' },
      { text: 'Project Plan', icon: <BarChart3 className="w-4 h-4" />, path: '/proposal/project' },
    ],
  },
  {
    text: 'Admin',
    icon: <ShieldCheck className="w-5 h-5" />,
    children: [
      { text: 'Agent Profiles', icon: <Users className="w-4 h-4" />, path: '/admin/agents' },
      { text: 'Agent Workflows', icon: <Network className="w-4 h-4" />, path: '/admin/workflows' },
      { text: 'New Agent', icon: <Plus className="w-4 h-4" />, path: '/admin/agents/new' },
      { text: 'Contract Rules', icon: <ScrollText className="w-4 h-4" />, path: '/admin/contracts' },
      { text: 'System Settings', icon: <Settings className="w-4 h-4" />, path: '/admin/settings' },
    ],
  },
];

export function Sidebar() {
  const navigate = useNavigate();
  const location = useLocation();
  const [openMenus, setOpenMenus] = useState<Record<string, boolean>>({
    'Demo': true,
    'Design Studio': false,
    'Analytics Hub': false,
    'Deployment Center': false,
    'Admin': false,
    'Proposal Center': false,
  });

  const handleToggle = (text: string) => {
    setOpenMenus((prev) => ({
      ...prev,
      [text]: !prev[text],
    }));
  };

  const handleNavigation = (path?: string) => {
    if (path) navigate(path);
  };

  const isActive = (path?: string) => {
    if (!path) return false;
    return location.pathname === path;
  };

  const isParentActive = (children?: MenuItem[]) => {
    if (!children) return false;
    return children.some((child) => child.path && location.pathname === child.path);
  };

  return (
    <aside className="fixed left-0 top-0 z-40 h-screen w-72 theme-sidebar-bg border-r theme-border overflow-hidden flex flex-col">
      {/* Logo */}
      <div className="h-16 flex items-center px-6 border-b theme-border">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-alpha-500 to-alpha-700 flex items-center justify-center">
            <span className="text-white font-bold text-sm">N</span>
          </div>
          <span className="text-xl font-semibold theme-text-title tracking-wide">Northstar</span>
        </div>
      </div>

      {/* Navigation */}
      <nav className="flex-1 overflow-y-auto py-4 px-3">
        <ul className="space-y-1">
          {menuItems.map((item) => (
            <li key={item.text}>
              {item.children ? (
                <>
                  <button
                    onClick={() => handleToggle(item.text)}
                    className={cn(
                      'w-full flex items-center justify-between px-4 py-3 rounded-xl transition-all duration-200',
                      'theme-text-nav hover:bg-[var(--sidebar-item-hover)]',
                      isParentActive(item.children) && 'bg-[var(--sidebar-item-hover)]'
                    )}
                  >
                    <div className="flex items-center gap-3">
                      <span className={cn(isParentActive(item.children) && 'theme-text-vibrant')}>
                        {item.icon}
                      </span>
                      <span className="font-medium">{item.text}</span>
                    </div>
                    {openMenus[item.text] ? (
                      <ChevronDown className="w-4 h-4" />
                    ) : (
                      <ChevronRight className="w-4 h-4" />
                    )}
                  </button>
                  {openMenus[item.text] && (
                    <ul className="mt-1 ml-4 space-y-1 animate-fade-in">
                      {item.children.map((child) => (
                        <li key={child.text}>
                          <button
                            onClick={() => handleNavigation(child.path)}
                            className={cn(
                              'w-full flex items-center gap-3 px-4 py-2.5 rounded-lg transition-all duration-200',
                              'theme-text-nav hover:bg-[var(--sidebar-item-hover)]',
                              isActive(child.path) && 'bg-[var(--sidebar-item-active)] theme-text-vibrant font-medium'
                            )}
                          >
                            {child.icon}
                            <span className="text-sm">{child.text}</span>
                          </button>
                        </li>
                      ))}
                    </ul>
                  )}
                </>
              ) : (
                <button
                  onClick={() => handleNavigation(item.path)}
                  className={cn(
                    'w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200',
                    'theme-text-nav hover:bg-[var(--sidebar-item-hover)]',
                    isActive(item.path) && 'bg-[var(--sidebar-item-active)] theme-text-vibrant font-medium'
                  )}
                >
                  {item.icon}
                  <span className="font-medium">{item.text}</span>
                </button>
              )}
            </li>
          ))}
        </ul>
      </nav>

      {/* Footer */}
      <div className="p-4 border-t theme-border">
        <div className="text-xs theme-text-muted">
          <p className="font-medium mb-1">Backend Services</p>
          <p>• Metadata: :8020</p>
          <p>• Calc Engine: :8021</p>
          <p>• Config: :8022</p>
        </div>
      </div>
    </aside>
  );
}
