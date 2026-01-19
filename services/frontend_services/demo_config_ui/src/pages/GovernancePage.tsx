import React, { useState, useEffect } from 'react';
import {
  ShieldCheck,
  GitBranch,
  Lock,
  CheckCircle,
  AlertTriangle,
  XCircle,
  Plus,
  Edit,
  Trash2,
  X,
  RefreshCw,
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { cn } from '../lib/utils';
import { governanceApi, QualityMetric, User, LineageGraph as ILineageGraph } from '../api/governanceApi';
import LineageGraph from '../components/LineageGraph';

const ROLES = ['Admin', 'Editor', 'Viewer', 'Analyst'];

function TabButton({ active, onClick, icon, children }: { 
  active: boolean; 
  onClick: () => void; 
  icon: React.ReactNode;
  children: React.ReactNode;
}) {
  return (
    <button
      onClick={onClick}
      className={cn(
        "flex items-center gap-2 px-4 py-3 text-sm font-medium transition-colors border-b-2",
        active 
          ? "text-alpha-500 border-alpha-500" 
          : "theme-text-muted border-transparent hover:theme-text"
      )}
    >
      {icon}
      {children}
    </button>
  );
}

export default function GovernancePage() {
  const [tabValue, setTabValue] = useState(0);
  const [qualityMetrics, setQualityMetrics] = useState<QualityMetric[]>([]);
  const [users, setUsers] = useState<User[]>([]);
  const [lineageData, setLineageData] = useState<ILineageGraph | null>(null);
  const [loading, setLoading] = useState(false);
  const [openUserDialog, setOpenUserDialog] = useState(false);
  const [newUser, setNewUser] = useState({ name: '', email: '', role: 'Viewer' });

  useEffect(() => {
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
    if (value >= 98) return 'text-green-400';
    if (value >= 90) return 'text-amber-400';
    return 'text-red-400';
  };

  const getQualityBg = (value: number) => {
    if (value >= 98) return 'bg-green-500';
    if (value >= 90) return 'bg-amber-500';
    return 'bg-red-500';
  };

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'pass': return <CheckCircle className="w-5 h-5 text-green-500" />;
      case 'warning': return <AlertTriangle className="w-5 h-5 text-amber-500" />;
      case 'fail': return <XCircle className="w-5 h-5 text-red-500" />;
      default: return <CheckCircle className="w-5 h-5 text-green-500" />;
    }
  };

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold theme-text-title tracking-wide">Data Governance</h1>
        <p className="theme-text-muted mt-1">Monitor data quality, lineage, and access control</p>
      </div>

      {loading && (
        <div className="h-1 bg-alpha-faded-200 dark:bg-alpha-faded-800 rounded overflow-hidden">
          <div className="h-full bg-alpha-500 animate-pulse" style={{ width: '60%' }} />
        </div>
      )}

      {/* Tabs */}
      <div className="border-b theme-border">
        <div className="flex">
          <TabButton active={tabValue === 0} onClick={() => setTabValue(0)} icon={<ShieldCheck className="w-4 h-4" />}>
            Data Quality
          </TabButton>
          <TabButton active={tabValue === 1} onClick={() => setTabValue(1)} icon={<GitBranch className="w-4 h-4" />}>
            Data Lineage
          </TabButton>
          <TabButton active={tabValue === 2} onClick={() => setTabValue(2)} icon={<Lock className="w-4 h-4" />}>
            Access Control
          </TabButton>
        </div>
      </div>

      {/* Data Quality Tab */}
      {tabValue === 0 && (
        <div className="space-y-6">
          {/* Summary Cards */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <Card className="bg-green-500/10 border-green-500/30">
              <CardContent className="p-5 text-center">
                <p className="text-4xl font-bold text-green-400">96.5%</p>
                <p className="text-sm text-green-400/80">Overall Score</p>
              </CardContent>
            </Card>
            <Card>
              <CardContent className="p-5 text-center">
                <p className="text-4xl font-bold theme-text-title">12</p>
                <p className="text-sm theme-text-muted">Tables Monitored</p>
              </CardContent>
            </Card>
            <Card>
              <CardContent className="p-5 text-center">
                <p className="text-4xl font-bold theme-text-title">45k</p>
                <p className="text-sm theme-text-muted">Rows Validated</p>
              </CardContent>
            </Card>
            <Card>
              <CardContent className="p-5 text-center">
                <p className="text-4xl font-bold theme-text-title">3</p>
                <p className="text-sm theme-text-muted">Open Issues</p>
              </CardContent>
            </Card>
          </div>

          {/* Quality Table */}
          <Card>
            <CardHeader>
              <CardTitle>Data Quality Overview</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="overflow-x-auto">
                <table className="w-full text-sm">
                  <thead>
                    <tr className="border-b theme-border">
                      <th className="px-4 py-3 text-left theme-text-muted font-medium">Table Name</th>
                      <th className="px-4 py-3 text-center theme-text-muted font-medium">Completeness</th>
                      <th className="px-4 py-3 text-center theme-text-muted font-medium">Accuracy</th>
                      <th className="px-4 py-3 text-center theme-text-muted font-medium">Consistency</th>
                      <th className="px-4 py-3 text-center theme-text-muted font-medium">Timeliness</th>
                      <th className="px-4 py-3 text-center theme-text-muted font-medium">Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    {qualityMetrics.map((row) => (
                      <tr key={row.table} className="border-b theme-border hover:theme-card-bg-hover">
                        <td className="px-4 py-3 font-medium theme-text">{row.table}</td>
                        <td className="px-4 py-3">
                          <div className="flex items-center gap-2">
                            <div className="flex-1 h-2 rounded-full bg-alpha-faded-200 dark:bg-alpha-faded-800 overflow-hidden">
                              <div className={cn("h-full transition-all", getQualityBg(row.completeness))} style={{ width: `${row.completeness}%` }} />
                            </div>
                            <span className="text-xs theme-text-muted w-10">{row.completeness}%</span>
                          </div>
                        </td>
                        <td className="px-4 py-3 text-center">
                          <span className={getQualityColor(row.accuracy)}>{row.accuracy}%</span>
                        </td>
                        <td className="px-4 py-3 text-center">
                          <span className={getQualityColor(row.consistency)}>{row.consistency}%</span>
                        </td>
                        <td className="px-4 py-3 text-center">
                          <span className={getQualityColor(row.timeliness)}>{row.timeliness}%</span>
                        </td>
                        <td className="px-4 py-3 text-center">
                          {getStatusIcon(row.status)}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </CardContent>
          </Card>
        </div>
      )}

      {/* Data Lineage Tab */}
      {tabValue === 1 && (
        <Card>
          <CardHeader>
            <CardTitle>Data Lineage Explorer</CardTitle>
          </CardHeader>
          <CardContent>
            {lineageData ? (
              <LineageGraph data={lineageData} />
            ) : (
              <div className="py-16 text-center">
                <RefreshCw className="w-12 h-12 mx-auto theme-text-muted animate-spin mb-4" />
                <p className="theme-text-muted">Loading Lineage Data...</p>
              </div>
            )}
          </CardContent>
        </Card>
      )}

      {/* Access Control Tab */}
      {tabValue === 2 && (
        <div className="space-y-4">
          <div className="flex justify-end">
            <Button onClick={() => setOpenUserDialog(true)}>
              <Plus className="w-4 h-4 mr-2" />
              Add User
            </Button>
          </div>

          <Card>
            <CardHeader>
              <CardTitle>User Management</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="divide-y theme-border">
                {users.map((user) => (
                  <div key={user.id} className="py-4 flex items-center justify-between">
                    <div className="flex items-center gap-4">
                      <div className="w-10 h-10 rounded-full bg-alpha-500/20 flex items-center justify-center text-alpha-500 font-semibold">
                        {user.name[0]}
                      </div>
                      <div>
                        <div className="flex items-center gap-2">
                          <span className="font-medium theme-text-title">{user.name}</span>
                          <span className="px-2 py-0.5 rounded-full text-xs border border-alpha-500/30 text-alpha-400">
                            {user.role}
                          </span>
                          <span className={cn(
                            "px-2 py-0.5 rounded-full text-xs border",
                            user.status === 'Active' 
                              ? "border-green-500/30 text-green-400" 
                              : "border-gray-500/30 text-gray-400"
                          )}>
                            {user.status}
                          </span>
                        </div>
                        <p className="text-sm theme-text-muted">{user.email}</p>
                      </div>
                    </div>
                    <div className="flex items-center gap-2">
                      <button className="p-2 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 transition-colors">
                        <Edit className="w-4 h-4 theme-text-muted" />
                      </button>
                      <button 
                        onClick={() => handleDeleteUser(user.id)}
                        className="p-2 rounded-lg hover:bg-red-500/20 text-red-400 transition-colors"
                      >
                        <Trash2 className="w-4 h-4" />
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>
      )}

      {/* Add User Dialog */}
      {openUserDialog && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="w-full max-w-md mx-4 rounded-2xl theme-card-bg border theme-border shadow-2xl">
            <div className="p-6 border-b theme-border flex items-center justify-between">
              <h2 className="text-xl font-bold theme-text-title">Add New User</h2>
              <button onClick={() => setOpenUserDialog(false)} className="p-2 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800">
                <X className="w-5 h-5 theme-text-muted" />
              </button>
            </div>
            <div className="p-6 space-y-4">
              <div>
                <label className="text-sm font-medium theme-text-title block mb-2">Full Name</label>
                <input
                  type="text"
                  value={newUser.name}
                  onChange={(e) => setNewUser({ ...newUser, name: e.target.value })}
                  className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                />
              </div>
              <div>
                <label className="text-sm font-medium theme-text-title block mb-2">Email Address</label>
                <input
                  type="email"
                  value={newUser.email}
                  onChange={(e) => setNewUser({ ...newUser, email: e.target.value })}
                  className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                />
              </div>
              <div>
                <label className="text-sm font-medium theme-text-title block mb-2">Role</label>
                <select
                  value={newUser.role}
                  onChange={(e) => setNewUser({ ...newUser, role: e.target.value })}
                  className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                >
                  {ROLES.map((role) => (
                    <option key={role} value={role}>{role}</option>
                  ))}
                </select>
              </div>
            </div>
            <div className="p-6 border-t theme-border flex justify-end gap-3">
              <Button variant="outline" onClick={() => setOpenUserDialog(false)}>Cancel</Button>
              <Button onClick={handleAddUser}>Add User</Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
