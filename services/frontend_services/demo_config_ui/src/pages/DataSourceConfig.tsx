import { useState, useEffect } from 'react';
import {
  Plus,
  RefreshCw,
  Database,
  Code,
  FileSpreadsheet,
  CheckCircle,
  XCircle,
  Search,
  Trash2,
  Edit,
  Clock,
  X,
  Eye,
} from 'lucide-react';
import { Card, CardContent } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { cn } from '../lib/utils';
import { connectorApi, ConnectionProfile, TableDefinition } from '../api/connectorApi';

const CONNECTION_TYPES = [
  { value: 'sql_postgres', label: 'PostgreSQL', icon: <Database className="w-4 h-4" /> },
  { value: 'sql_mssql', label: 'SQL Server', icon: <Database className="w-4 h-4" /> },
  { value: 'rest_api', label: 'REST API', icon: <Code className="w-4 h-4" /> },
  { value: 'excel_file', label: 'Excel File', icon: <FileSpreadsheet className="w-4 h-4" /> },
];

export default function DataSourceConfig() {
  const [connections, setConnections] = useState<ConnectionProfile[]>([]);
  const [openDialog, setOpenDialog] = useState(false);
  const [testStatus, setTestStatus] = useState<Record<string, boolean | null>>({});
  const [testingConnection, setTestingConnection] = useState<string | null>(null);
  const [discoveringSchema, setDiscoveringSchema] = useState<string | null>(null);
  const [schemaResult, setSchemaResult] = useState<{ connectionId: string; tables: TableDefinition[] } | null>(null);
  const [openSchemaDialog, setOpenSchemaDialog] = useState(false);
  const [selectedTables, setSelectedTables] = useState<string[]>([]);
  const [editingId, setEditingId] = useState<string | null>(null);
  const [previewData, setPreviewData] = useState<{ tableName: string; rows: any[] } | null>(null);
  const [loadingPreview, setLoadingPreview] = useState<string | null>(null);

  const [newConnection, setNewConnection] = useState<Partial<ConnectionProfile>>({
    name: '',
    type: 'sql_postgres',
    host: 'localhost',
    port: 5432,
    username: '',
    password: '',
    database: '',
    api_url: '',
    file_path: '',
    schedule: { frequency: 'manual', active: false },
    selected_tables: [],
  });

  const handleCreateOrUpdateConnection = async () => {
    try {
      if (editingId) {
        setConnections(prev => prev.map(c => c.id === editingId ? { ...c, ...newConnection } as ConnectionProfile : c));
      } else {
        const id = `conn_${Date.now()}`;
        const profile: ConnectionProfile = { id, ...newConnection as any };
        await connectorApi.createConnection(profile);
        setConnections([...connections, profile]);
      }
      setOpenDialog(false);
      resetForm();
    } catch (error) {
      console.error('Failed to save connection:', error);
      alert('Failed to save connection');
    }
  };

  const handleDeleteConnection = async (id: string) => {
    if (!window.confirm('Are you sure you want to delete this connection?')) return;
    try {
      setConnections(prev => prev.filter(c => c.id !== id));
    } catch (error) {
      console.error('Failed to delete connection:', error);
    }
  };

  const resetForm = () => {
    setNewConnection({
      name: '',
      type: 'sql_postgres',
      host: 'localhost',
      port: 5432,
      username: '',
      password: '',
      database: '',
      api_url: '',
      file_path: '',
      schedule: { frequency: 'manual', active: false },
      selected_tables: [],
    });
    setEditingId(null);
  };

  const handleEditConnection = (conn: ConnectionProfile) => {
    setNewConnection({
      ...conn,
      schedule: conn.schedule || { frequency: 'manual', active: false },
      selected_tables: conn.selected_tables || [],
    });
    setEditingId(conn.id);
    setOpenDialog(true);
  };

  const handleTestConnection = async (profile: ConnectionProfile) => {
    setTestingConnection(profile.id);
    try {
      const result = await connectorApi.testConnection(profile);
      setTestStatus((prev) => ({ ...prev, [profile.id]: result.success }));
    } catch (error) {
      setTestStatus((prev) => ({ ...prev, [profile.id]: false }));
    } finally {
      setTestingConnection(null);
    }
  };

  const handleDiscoverSchema = async (profile: ConnectionProfile) => {
    setDiscoveringSchema(profile.id);
    try {
      const tables = await connectorApi.discoverSchema(profile.id);
      setSchemaResult({ connectionId: profile.id, tables });
      setSelectedTables(profile.selected_tables || []);
      setOpenSchemaDialog(true);
    } catch (error) {
      alert('Schema discovery failed. Check connection settings.');
    } finally {
      setDiscoveringSchema(null);
    }
  };

  const handleToggleTable = (tableName: string) => {
    setSelectedTables(prev => 
      prev.includes(tableName) ? prev.filter(t => t !== tableName) : [...prev, tableName]
    );
  };

  const handleSaveSchemaSelection = async () => {
    if (!schemaResult) return;
    try {
      const connectionId = schemaResult.connectionId;
      setConnections(prev => prev.map(c => 
        c.id === connectionId ? { ...c, selected_tables: selectedTables } : c
      ));
      await connectorApi.updateConnection(connectionId, { selected_tables: selectedTables });
      setOpenSchemaDialog(false);
    } catch (error) {
      alert('Failed to save schema selection');
    }
  };

  const handlePreviewData = async (connectionId: string, tableName: string) => {
    setLoadingPreview(tableName);
    try {
      const rows = await connectorApi.previewData(connectionId, tableName, 5);
      setPreviewData({ tableName, rows });
    } catch (error) {
      alert('Failed to preview data');
    } finally {
      setLoadingPreview(null);
    }
  };

  const getConnectionIcon = (type: string) => {
    const config = CONNECTION_TYPES.find(t => t.value === type);
    return config?.icon || <Database className="w-4 h-4" />;
  };

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold theme-text-title tracking-wide">Data Sources</h1>
          <p className="theme-text-muted mt-1">Configure and manage your data connections</p>
        </div>
        <Button onClick={() => { resetForm(); setOpenDialog(true); }}>
          <Plus className="w-4 h-4 mr-2" />
          Add Data Source
        </Button>
      </div>

      {/* Connections Grid */}
      {connections.length === 0 ? (
        <Card className="p-12 text-center">
          <Database className="w-16 h-16 mx-auto theme-text-muted mb-4" />
          <h3 className="text-lg font-semibold theme-text-title mb-2">No data sources configured</h3>
          <p className="theme-text-muted mb-4">Add a connection to start ingesting data.</p>
          <Button onClick={() => { resetForm(); setOpenDialog(true); }}>
            <Plus className="w-4 h-4 mr-2" />
            Add Data Source
          </Button>
        </Card>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {connections.map((conn) => (
            <Card key={conn.id} className="overflow-hidden">
              <CardContent className="p-5">
                <div className="flex items-start justify-between mb-3">
                  <div className="flex items-center gap-2">
                    <div className="p-2 rounded-lg bg-alpha-500/20">
                      {getConnectionIcon(conn.type)}
                    </div>
                    <div>
                      <h3 className="font-semibold theme-text-title">{conn.name}</h3>
                      <span className="text-xs theme-text-muted">
                        {conn.type.replace('_', ' ').toUpperCase()}
                      </span>
                    </div>
                  </div>
                </div>

                <p className="text-sm theme-text-muted mb-3">
                  {conn.type.includes('sql') ? `${conn.host}:${conn.port} / ${conn.database}` : 
                   conn.type === 'rest_api' ? conn.api_url : conn.file_path}
                </p>

                {testStatus[conn.id] !== undefined && (
                  <div className={cn(
                    "p-2 rounded-lg mb-3 flex items-center gap-2 text-sm",
                    testStatus[conn.id] 
                      ? "bg-green-500/10 text-green-400 border border-green-500/30"
                      : "bg-red-500/10 text-red-400 border border-red-500/30"
                  )}>
                    {testStatus[conn.id] ? (
                      <><CheckCircle className="w-4 h-4" /> Connection Successful</>
                    ) : (
                      <><XCircle className="w-4 h-4" /> Connection Failed</>
                    )}
                  </div>
                )}

                <div className="flex items-center justify-between pt-3 border-t theme-border">
                  <div className="flex gap-1">
                    <button
                      onClick={() => handleEditConnection(conn)}
                      className="p-2 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 transition-colors"
                      title="Edit"
                    >
                      <Edit className="w-4 h-4 theme-text-muted" />
                    </button>
                    <button
                      onClick={() => handleDeleteConnection(conn.id)}
                      className="p-2 rounded-lg hover:bg-red-500/20 text-red-400 transition-colors"
                      title="Delete"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </div>
                  <div className="flex gap-1">
                    <Button
                      variant="outline"
                      size="sm"
                      onClick={() => handleTestConnection(conn)}
                      disabled={testingConnection === conn.id}
                    >
                      {testingConnection === conn.id ? (
                        <RefreshCw className="w-4 h-4 animate-spin" />
                      ) : (
                        <RefreshCw className="w-4 h-4" />
                      )}
                    </Button>
                    <Button
                      variant="outline"
                      size="sm"
                      onClick={() => handleDiscoverSchema(conn)}
                      disabled={discoveringSchema === conn.id}
                    >
                      {discoveringSchema === conn.id ? (
                        <RefreshCw className="w-4 h-4 animate-spin" />
                      ) : (
                        <Search className="w-4 h-4" />
                      )}
                    </Button>
                  </div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      )}

      {/* Add/Edit Connection Dialog */}
      {openDialog && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="w-full max-w-lg mx-4 rounded-2xl theme-card-bg border theme-border shadow-2xl max-h-[90vh] overflow-y-auto">
            <div className="p-6 border-b theme-border flex items-center justify-between">
              <h2 className="text-xl font-bold theme-text-title">
                {editingId ? 'Edit Data Source' : 'Add New Data Source'}
              </h2>
              <button onClick={() => setOpenDialog(false)} className="p-2 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800">
                <X className="w-5 h-5 theme-text-muted" />
              </button>
            </div>
            <div className="p-6 space-y-4">
              <div>
                <label className="text-sm font-medium theme-text-title block mb-2">Connection Name</label>
                <input
                  type="text"
                  value={newConnection.name}
                  onChange={(e) => setNewConnection({ ...newConnection, name: e.target.value })}
                  className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                  placeholder="My Database"
                />
              </div>

              <div>
                <label className="text-sm font-medium theme-text-title block mb-2">Connection Type</label>
                <select
                  value={newConnection.type}
                  onChange={(e) => setNewConnection({ ...newConnection, type: e.target.value as any })}
                  className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                >
                  {CONNECTION_TYPES.map((type) => (
                    <option key={type.value} value={type.value}>{type.label}</option>
                  ))}
                </select>
              </div>

              {(newConnection.type === 'sql_postgres' || newConnection.type === 'sql_mssql') && (
                <>
                  <div className="grid grid-cols-3 gap-3">
                    <div className="col-span-2">
                      <label className="text-sm font-medium theme-text-title block mb-2">Host</label>
                      <input
                        type="text"
                        value={newConnection.host}
                        onChange={(e) => setNewConnection({ ...newConnection, host: e.target.value })}
                        className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                      />
                    </div>
                    <div>
                      <label className="text-sm font-medium theme-text-title block mb-2">Port</label>
                      <input
                        type="number"
                        value={newConnection.port}
                        onChange={(e) => setNewConnection({ ...newConnection, port: parseInt(e.target.value) })}
                        className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                      />
                    </div>
                  </div>
                  <div>
                    <label className="text-sm font-medium theme-text-title block mb-2">Database Name</label>
                    <input
                      type="text"
                      value={newConnection.database}
                      onChange={(e) => setNewConnection({ ...newConnection, database: e.target.value })}
                      className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                    />
                  </div>
                  <div>
                    <label className="text-sm font-medium theme-text-title block mb-2">Username</label>
                    <input
                      type="text"
                      value={newConnection.username}
                      onChange={(e) => setNewConnection({ ...newConnection, username: e.target.value })}
                      className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                    />
                  </div>
                  <div>
                    <label className="text-sm font-medium theme-text-title block mb-2">Password</label>
                    <input
                      type="password"
                      value={newConnection.password}
                      onChange={(e) => setNewConnection({ ...newConnection, password: e.target.value })}
                      className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                    />
                  </div>
                </>
              )}

              {newConnection.type === 'rest_api' && (
                <div>
                  <label className="text-sm font-medium theme-text-title block mb-2">API Base URL</label>
                  <input
                    type="text"
                    value={newConnection.api_url}
                    onChange={(e) => setNewConnection({ ...newConnection, api_url: e.target.value })}
                    className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                    placeholder="https://api.example.com"
                  />
                </div>
              )}

              {newConnection.type === 'excel_file' && (
                <div>
                  <label className="text-sm font-medium theme-text-title block mb-2">File Path</label>
                  <input
                    type="text"
                    value={newConnection.file_path}
                    onChange={(e) => setNewConnection({ ...newConnection, file_path: e.target.value })}
                    className="w-full px-4 py-3 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500"
                    placeholder="/path/to/file.xlsx"
                  />
                  <p className="text-xs theme-text-muted mt-1">Absolute path to the Excel file on the server</p>
                </div>
              )}

              {/* Schedule Section */}
              <div className="border-t theme-border pt-4">
                <div className="flex items-center gap-2 mb-3">
                  <Clock className="w-4 h-4 theme-info-icon" />
                  <span className="font-medium theme-text-title">Ingestion Schedule</span>
                </div>
                
                <label className="flex items-center gap-3 cursor-pointer mb-3">
                  <div className="relative">
                    <input
                      type="checkbox"
                      checked={newConnection.schedule?.active || false}
                      onChange={(e) => setNewConnection({
                        ...newConnection,
                        schedule: { ...(newConnection.schedule || { frequency: 'manual' }), active: e.target.checked }
                      })}
                      className="sr-only peer"
                    />
                    <div className="w-10 h-6 rounded-full bg-alpha-faded-300 dark:bg-alpha-faded-700 peer-checked:bg-alpha-500 transition-colors"></div>
                    <div className="absolute left-1 top-1 w-4 h-4 rounded-full bg-white peer-checked:translate-x-4 transition-transform"></div>
                  </div>
                  <span className="text-sm theme-text">Enable Scheduled Ingestion</span>
                </label>

                {newConnection.schedule?.active && (
                  <div className="ml-4 pl-4 border-l-2 border-alpha-faded-300 dark:border-alpha-faded-700 space-y-3">
                    <div>
                      <label className="text-sm font-medium theme-text-title block mb-2">Frequency</label>
                      <select
                        value={newConnection.schedule?.frequency || 'manual'}
                        onChange={(e) => setNewConnection({
                          ...newConnection,
                          schedule: { ...newConnection.schedule!, frequency: e.target.value as any }
                        })}
                        className="w-full px-4 py-2 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500 text-sm"
                      >
                        <option value="manual">Manual Trigger Only</option>
                        <option value="daily">Daily</option>
                        <option value="weekly">Weekly</option>
                        <option value="custom">Custom Cron Expression</option>
                      </select>
                    </div>

                    {(newConnection.schedule?.frequency === 'daily' || newConnection.schedule?.frequency === 'weekly') && (
                      <div>
                        <label className="text-sm font-medium theme-text-title block mb-2">Time (HH:MM)</label>
                        <input
                          type="time"
                          value={newConnection.schedule?.time || '00:00'}
                          onChange={(e) => setNewConnection({
                            ...newConnection,
                            schedule: { ...newConnection.schedule!, time: e.target.value }
                          })}
                          className="w-full px-4 py-2 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500 text-sm"
                        />
                      </div>
                    )}

                    {newConnection.schedule?.frequency === 'custom' && (
                      <div>
                        <label className="text-sm font-medium theme-text-title block mb-2">Cron Expression</label>
                        <input
                          type="text"
                          placeholder="0 0 * * *"
                          value={newConnection.schedule?.cron_expression || ''}
                          onChange={(e) => setNewConnection({
                            ...newConnection,
                            schedule: { ...newConnection.schedule!, cron_expression: e.target.value }
                          })}
                          className="w-full px-4 py-2 rounded-xl theme-card-bg border theme-border theme-text focus:outline-none focus:ring-2 focus:ring-alpha-500 text-sm"
                        />
                        <p className="text-xs theme-text-muted mt-1">Standard cron format</p>
                      </div>
                    )}
                  </div>
                )}
              </div>
            </div>
            <div className="p-6 border-t theme-border flex justify-end gap-3">
              <Button variant="outline" onClick={() => setOpenDialog(false)}>Cancel</Button>
              <Button onClick={handleCreateOrUpdateConnection}>
                {editingId ? 'Save Changes' : 'Add Connection'}
              </Button>
            </div>
          </div>
        </div>
      )}

      {/* Schema Discovery Dialog */}
      {openSchemaDialog && schemaResult && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="w-full max-w-4xl mx-4 rounded-2xl theme-card-bg border theme-border shadow-2xl max-h-[90vh] overflow-hidden flex flex-col">
            <div className="p-6 border-b theme-border flex items-center justify-between">
              <h2 className="text-xl font-bold theme-text-title">Discovered Schema</h2>
              <button onClick={() => setOpenSchemaDialog(false)} className="p-2 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800">
                <X className="w-5 h-5 theme-text-muted" />
              </button>
            </div>
            <div className="p-6 overflow-y-auto flex-1">
              {schemaResult.tables.length === 0 ? (
                <p className="theme-text-muted text-center py-8">No tables or schema information found.</p>
              ) : (
                <div className="space-y-6">
                  {schemaResult.tables.map((table) => (
                    <div key={table.name} className="rounded-xl border theme-border overflow-hidden">
                      <div className="p-4 theme-card-bg flex items-center justify-between">
                        <label className="flex items-center gap-3 cursor-pointer">
                          <input
                            type="checkbox"
                            checked={selectedTables.includes(table.name)}
                            onChange={() => handleToggleTable(table.name)}
                            className="w-4 h-4 rounded border-gray-500 text-alpha-500 focus:ring-alpha-500"
                          />
                          <span className="font-semibold theme-text-vibrant">Table: {table.name}</span>
                        </label>
                        <Button
                          variant="outline"
                          size="sm"
                          onClick={() => handlePreviewData(schemaResult.connectionId, table.name)}
                          disabled={loadingPreview === table.name}
                        >
                          {loadingPreview === table.name ? (
                            <RefreshCw className="w-4 h-4 animate-spin mr-1" />
                          ) : (
                            <Eye className="w-4 h-4 mr-1" />
                          )}
                          Preview
                        </Button>
                      </div>
                      <div className="overflow-x-auto">
                        <table className="w-full text-sm">
                          <thead className="theme-card-bg border-t theme-border">
                            <tr>
                              <th className="px-4 py-2 text-left theme-text-muted font-medium">Column Name</th>
                              <th className="px-4 py-2 text-left theme-text-muted font-medium">Data Type</th>
                              <th className="px-4 py-2 text-center theme-text-muted font-medium">Nullable</th>
                              <th className="px-4 py-2 text-center theme-text-muted font-medium">Primary Key</th>
                            </tr>
                          </thead>
                          <tbody>
                            {table.columns.map((col) => (
                              <tr key={col.name} className="border-t theme-border">
                                <td className="px-4 py-2 theme-text">{col.name}</td>
                                <td className="px-4 py-2 theme-text-muted">{col.data_type}</td>
                                <td className="px-4 py-2 text-center theme-text-muted">{col.is_nullable ? 'Yes' : 'No'}</td>
                                <td className="px-4 py-2 text-center theme-text-muted">{col.is_primary_key ? 'Yes' : '-'}</td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>

                      {previewData && previewData.tableName === table.name && (
                        <div className="p-4 border-t theme-border bg-[var(--background)]">
                          <h4 className="text-sm font-medium theme-text-title mb-2">Data Preview (First 5 Rows)</h4>
                          <div className="overflow-x-auto rounded-lg border theme-border">
                            <table className="w-full text-sm">
                              <thead className="theme-card-bg">
                                <tr>
                                  {Object.keys(previewData.rows[0] || {}).map(key => (
                                    <th key={key} className="px-3 py-2 text-left theme-text-muted font-medium">{key}</th>
                                  ))}
                                </tr>
                              </thead>
                              <tbody>
                                {previewData.rows.map((row, idx) => (
                                  <tr key={idx} className="border-t theme-border">
                                    {Object.values(row).map((val: any, i) => (
                                      <td key={i} className="px-3 py-2 theme-text">{String(val)}</td>
                                    ))}
                                  </tr>
                                ))}
                              </tbody>
                            </table>
                          </div>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              )}
            </div>
            <div className="p-6 border-t theme-border flex justify-end gap-3">
              <Button variant="outline" onClick={() => setOpenSchemaDialog(false)}>Cancel</Button>
              <Button onClick={handleSaveSchemaSelection}>
                Save Selection ({selectedTables.length})
              </Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
