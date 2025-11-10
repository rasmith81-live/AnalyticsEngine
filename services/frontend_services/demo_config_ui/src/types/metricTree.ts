/**
 * Metric Tree Type Definitions
 * Supports dual navigation: Industry-based and Value Chain-based
 */

export interface KPI {
  code: string;
  name: string;
  display_name: string;
  description: string;
  formula?: string;
  unit?: string;
  data_type?: string;
  aggregation_methods?: string[];
  time_periods?: string[];
  required_objects?: string[];
  module_code: string;
}

export interface Module {
  code: string;
  name: string;
  display_name: string;
  description?: string;
  value_chain_code: string;
  kpis: KPI[];
  kpi_count?: number;
}

export interface ValueChain {
  code: string;
  name: string;
  display_name: string;
  description?: string;
  industry_codes?: string[];
  modules: Module[];
  module_count?: number;
}

export interface Industry {
  code: string;
  name: string;
  display_name: string;
  description?: string;
  value_chains: ValueChain[];
  value_chain_count?: number;
}

// Tree navigation modes
export type TreeMode = 'industry' | 'value-chain';

// Tree node types
export type NodeType = 'industry' | 'value-chain' | 'module' | 'kpi';

// Selection state
export interface TreeSelection {
  selectedKPIs: string[];
  expandedNodes: string[];
  mode: TreeMode;
}

// API response types
export interface IndustryTreeResponse {
  industries: Industry[];
  total_count: number;
}

export interface ValueChainTreeResponse {
  value_chains: ValueChain[];
  total_count: number;
}

export interface KPIStatsResponse {
  total_kpis: number;
  total_modules: number;
  total_value_chains: number;
  total_industries: number;
}

// Search and filter types
export interface TreeSearchParams {
  query?: string;
  value_chain_code?: string;
  module_code?: string;
  industry_code?: string;
}

export interface TreeFilterOptions {
  industries?: string[];
  valueChains?: string[];
  modules?: string[];
}
