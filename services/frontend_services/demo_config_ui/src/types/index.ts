/**
 * Core type definitions for Demo/Config UI
 */

export interface KPI {
  code: string;
  name: string;
  display_name?: string;
  formula: string;
  calculation_formula?: string;
  unit?: string;
  description?: string;
  category?: string;
  is_active?: boolean;
  full_kpi_definition?: string;
  trend_analysis?: string;
  diagnostic_questions?: string;
  actionable_tips?: string;
  visualization_suggestions?: string;
  risk_warnings?: string;
  tracking_tools?: string;
  integration_points?: string;
  change_impact_analysis?: string;
  calculation_logic?: string;
  required_objects: string[];
  benchmarks?: Record<string, any>;
  modules?: string[];
  module_code?: string;
  metadata_: {
    modules: string[];
    value_chains?: string[];
    industries?: string[];
    level?: number;
    category?: string;
    last_validated?: string;
  };
  sample_data?: {
    time_series: {
      dates: string[];
      values: number[];
      unit: string;
    };
    current: {
      value: number;
      unit: string;
      change: number;
      change_percent: number;
      trend: string;
    };
    statistics: {
      average: number;
      min: number;
      max: number;
      unit: string;
    };
    breakdown: Array<{
      category: string;
      value: number;
      percentage: number;
    }>;
    metadata: {
      generated_date: string;
      data_points: number;
      kpi_type: string;
      kpi_name: string;
    };
  };
}

export interface ObjectModel {
  code: string;
  name: string;
  display_name?: string;
  description?: string;
  table_name?: string;
  table_schema?: TableSchema;
  schema_definition?: string; // UML PlantUML format
  metadata_: {
    modules: string[];
    value_chains?: string[];
    is_hypertable?: boolean;
  };
}

export interface TableSchema {
  columns: Column[];
  indexes?: Index[];
  constraints?: Constraint[];
}

export interface Column {
  name: string;
  type: string;
  nullable?: boolean;
  primary_key?: boolean;
  unique?: boolean;
  index?: boolean;
  default?: string;
  foreign_key?: {
    table: string;
    column: string;
  };
}

export interface Index {
  name: string;
  columns: string[];
}

export interface Constraint {
  type: string;
  name: string;
  expression: string;
}

export interface Module {
  code: string;
  name: string;
  display_name?: string;
  description?: string;
  associated_kpis: string[];
  associated_object_models: string[];
  metadata_?: {
    value_chain?: string;
    industry?: string;
  };
}

export interface ValueChain {
  code: string;
  name: string;
  display_name?: string;
  description?: string;
  associated_modules: string[];
  metadata_?: {
    industries?: string[];
  };
}

export interface Industry {
  code: string;
  name: string;
  display_name?: string;
  description?: string;
  associated_value_chains?: string[];
}

export interface TreeNode {
  id: string;
  name: string;
  type: 'industry' | 'value_chain' | 'module' | 'kpi' | 'object_model';
  data: any;
  children?: TreeNode[];
  selected?: boolean;
  expanded?: boolean;
}

export interface ClientConfig {
  id?: string;
  client_id: string;
  client_name: string;
  selected_kpis: string[];
  custom_kpis?: CustomKPI[];
  data_sources?: DataSource[];
  deployment_config?: Record<string, any>;
  license_key?: string;
  license_expiration?: string;
  created_at?: string;
  updated_at?: string;
}

export interface CustomKPI extends KPI {
  source_kpi_code: string;
  created_by: string;
  created_at: string;
}

export interface DataSource {
  id?: string;
  name: string;
  type: 'batch' | 'api' | 'event';
  connector_type: string;
  config: Record<string, any>;
  status?: string;
}

export interface ServiceProposal {
  id?: string;
  client_id: string;
  required_objects: string[];
  integration_method: 'batch' | 'realtime';
  estimated_hours: number;
  estimated_cost: number;
  timeline_weeks: number;
  status: 'draft' | 'sent' | 'signed';
  created_at?: string;
}

export interface UMLRelationship {
  from: string;
  to: string;
  type: 'association' | 'aggregation' | 'composition' | 'inheritance';
  label?: string;
  multiplicity?: string;
}
