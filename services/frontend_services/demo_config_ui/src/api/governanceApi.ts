// Types
export interface QualityMetric {
  table: string;
  completeness: number;
  accuracy: number;
  consistency: number;
  timeliness: number;
  status: 'pass' | 'warning' | 'fail';
}

export interface LineageNode {
  id: string;
  label: string;
  type: 'source' | 'ingestion' | 'process' | 'model' | 'kpi';
  status: 'active' | 'inactive' | 'error';
}

export interface LineageEdge {
  from: string;
  to: string;
}

export interface LineageGraph {
  nodes: LineageNode[];
  edges: LineageEdge[];
}

export interface User {
  id: number;
  name: string;
  email: string;
  role: 'Admin' | 'Editor' | 'Viewer' | 'Analyst';
  status: 'Active' | 'Inactive';
}

// Mock Data
const MOCK_QUALITY_METRICS: QualityMetric[] = [
  { table: 'sales_transactions', completeness: 98.5, accuracy: 99.2, consistency: 100, timeliness: 95.0, status: 'pass' },
  { table: 'customer_master', completeness: 92.1, accuracy: 88.5, consistency: 94.2, timeliness: 99.1, status: 'warning' },
  { table: 'product_catalog', completeness: 100, accuracy: 100, consistency: 100, timeliness: 100, status: 'pass' },
  { table: 'inventory_levels', completeness: 85.4, accuracy: 91.2, consistency: 89.5, timeliness: 78.3, status: 'fail' },
];

const MOCK_LINEAGE: LineageGraph = {
  nodes: [
    { id: 'src_pg', label: 'Source: PostgreSQL', type: 'source', status: 'active' },
    { id: 'ing_raw', label: 'Ingestion: Raw Zone', type: 'ingestion', status: 'active' },
    { id: 'proc_cln', label: 'Process: Cleaned', type: 'process', status: 'active' },
    { id: 'mod_fact', label: 'Model: Fact Tables', type: 'model', status: 'active' },
    { id: 'kpi_rev', label: 'KPI: Revenue', type: 'kpi', status: 'active' },
  ],
  edges: [
    { from: 'src_pg', to: 'ing_raw' },
    { from: 'ing_raw', to: 'proc_cln' },
    { from: 'proc_cln', to: 'mod_fact' },
    { from: 'mod_fact', to: 'kpi_rev' },
  ]
};

const MOCK_USERS: User[] = [
  { id: 1, name: 'Alice Johnson', email: 'alice@example.com', role: 'Admin', status: 'Active' },
  { id: 2, name: 'Bob Smith', email: 'bob@example.com', role: 'Editor', status: 'Active' },
  { id: 3, name: 'Carol Williams', email: 'carol@example.com', role: 'Viewer', status: 'Active' },
  { id: 4, name: 'David Brown', email: 'david@example.com', role: 'Viewer', status: 'Inactive' },
];

// API Service
export const governanceApi = {
  getQualityMetrics: async (): Promise<QualityMetric[]> => {
    // Simulate API call
    return new Promise((resolve) => {
      setTimeout(() => resolve(MOCK_QUALITY_METRICS), 500);
    });
  },

  getLineage: async (): Promise<LineageGraph> => {
    // Simulate API call
    return new Promise((resolve) => {
      setTimeout(() => resolve(MOCK_LINEAGE), 500);
    });
  },

  getUsers: async (): Promise<User[]> => {
    // Simulate API call
    return new Promise((resolve) => {
      setTimeout(() => resolve([...MOCK_USERS]), 500);
    });
  },

  addUser: async (user: Omit<User, 'id' | 'status'>): Promise<User> => {
    // Simulate API call
    return new Promise((resolve) => {
      setTimeout(() => {
        const newUser = { ...user, id: Date.now(), status: 'Active' as const };
        MOCK_USERS.push(newUser); // Update mock store
        resolve(newUser);
      }, 500);
    });
  },

  deleteUser: async (id: number): Promise<void> => {
    // Simulate API call
    return new Promise((resolve) => {
      setTimeout(() => {
        const index = MOCK_USERS.findIndex(u => u.id === id);
        if (index !== -1) MOCK_USERS.splice(index, 1);
        resolve();
      }, 500);
    });
  },
  
  updateUserStatus: async (id: number, status: 'Active' | 'Inactive'): Promise<void> => {
     // Simulate API call
     return new Promise((resolve) => {
      setTimeout(() => {
        const user = MOCK_USERS.find(u => u.id === id);
        if (user) user.status = status;
        resolve();
      }, 300);
    });
  }
};
