/**
 * Industry Value Chain Reference Data
 * 
 * Pre-defined value chains, modules, and KPIs for common industries.
 * Used by DemoInterviewPage to provide industry-specific analytics designs.
 */

export interface IndustryKPI {
  code: string;
  name: string;
  category: string;
  unit: 'currency' | 'percent' | 'number' | 'time' | 'ratio';
  description: string;
  formula?: string;
  target?: number;
  icon?: string;
}

export interface IndustryEntity {
  code: string;
  name: string;
  description: string;
  recordsPerMinute: number;
}

export interface IndustryModule {
  code: string;
  name: string;
  description: string;
  kpis: IndustryKPI[];
  entities: IndustryEntity[];
}

export interface IndustryValueChain {
  code: string;
  name: string;
  description: string;
  icon: string;
  modules: IndustryModule[];
}

export interface IndustryDefinition {
  code: string;
  name: string;
  description: string;
  valueChains: IndustryValueChain[];
}

// =============================================================================
// RETAIL INDUSTRY
// =============================================================================

export const retailIndustry: IndustryDefinition = {
  code: 'RETAIL',
  name: 'Retail & E-Commerce',
  description: 'Omnichannel retail, e-commerce, and consumer goods',
  valueChains: [
    {
      code: 'RETAIL_CUSTOMER',
      name: 'Customer Acquisition & Retention',
      description: 'Customer lifecycle from acquisition through loyalty',
      icon: 'users',
      modules: [
        {
          code: 'CUSTOMER_ACQUISITION',
          name: 'Customer Acquisition',
          description: 'Attracting and converting new customers',
          kpis: [
            { code: 'cac', name: 'Customer Acquisition Cost', category: 'Customer', unit: 'currency', description: 'Cost to acquire a new customer', icon: 'dollar' },
            { code: 'conversion_rate', name: 'Conversion Rate', category: 'Sales', unit: 'percent', description: 'Visitors who become customers', target: 3.5, icon: 'trending' },
            { code: 'traffic', name: 'Site Traffic', category: 'Marketing', unit: 'number', description: 'Unique visitors per period', icon: 'activity' },
            { code: 'bounce_rate', name: 'Bounce Rate', category: 'Marketing', unit: 'percent', description: 'Single-page session rate', icon: 'chart' },
          ],
          entities: [
            { code: 'visitors', name: 'Visitors', description: 'Website and store visitor data', recordsPerMinute: 500 },
            { code: 'campaigns', name: 'Marketing Campaigns', description: 'Campaign performance data', recordsPerMinute: 10 },
          ],
        },
        {
          code: 'CUSTOMER_RETENTION',
          name: 'Customer Retention',
          description: 'Keeping customers engaged and loyal',
          kpis: [
            { code: 'clv', name: 'Customer Lifetime Value', category: 'Customer', unit: 'currency', description: 'Total expected revenue from customer', icon: 'dollar' },
            { code: 'retention_rate', name: 'Customer Retention Rate', category: 'Customer', unit: 'percent', description: 'Customers retained period over period', target: 85, icon: 'users' },
            { code: 'nps', name: 'Net Promoter Score', category: 'Customer', unit: 'number', description: 'Customer satisfaction and loyalty score', target: 50, icon: 'target' },
            { code: 'repeat_purchase_rate', name: 'Repeat Purchase Rate', category: 'Sales', unit: 'percent', description: 'Customers making multiple purchases', icon: 'trending' },
          ],
          entities: [
            { code: 'customers', name: 'Customers', description: 'Customer profiles and segments', recordsPerMinute: 100 },
            { code: 'loyalty_programs', name: 'Loyalty Programs', description: 'Points and rewards data', recordsPerMinute: 50 },
          ],
        },
      ],
    },
    {
      code: 'RETAIL_ORDERS',
      name: 'Order Management',
      description: 'Order processing and fulfillment',
      icon: 'package',
      modules: [
        {
          code: 'ORDER_PROCESSING',
          name: 'Order Processing',
          description: 'Order capture and validation',
          kpis: [
            { code: 'aov', name: 'Average Order Value', category: 'Sales', unit: 'currency', description: 'Average revenue per order', icon: 'dollar' },
            { code: 'orders_per_day', name: 'Orders Per Day', category: 'Operations', unit: 'number', description: 'Daily order volume', icon: 'package' },
            { code: 'cart_abandonment', name: 'Cart Abandonment Rate', category: 'Sales', unit: 'percent', description: 'Carts not converted to orders', icon: 'chart' },
          ],
          entities: [
            { code: 'orders', name: 'Orders', description: 'Sales orders and transactions', recordsPerMinute: 200 },
            { code: 'order_items', name: 'Order Items', description: 'Line items in orders', recordsPerMinute: 600 },
          ],
        },
        {
          code: 'FULFILLMENT',
          name: 'Fulfillment',
          description: 'Order picking, packing, and shipping',
          kpis: [
            { code: 'fulfillment_rate', name: 'Order Fulfillment Rate', category: 'Operations', unit: 'percent', description: 'Orders shipped on time', target: 98, icon: 'target' },
            { code: 'delivery_time', name: 'Average Delivery Time', category: 'Operations', unit: 'time', description: 'Days from order to delivery', icon: 'activity' },
            { code: 'return_rate', name: 'Return Rate', category: 'Operations', unit: 'percent', description: 'Orders returned by customers', icon: 'chart' },
          ],
          entities: [
            { code: 'shipments', name: 'Shipments', description: 'Shipping and tracking data', recordsPerMinute: 150 },
            { code: 'returns', name: 'Returns', description: 'Return requests and processing', recordsPerMinute: 20 },
          ],
        },
      ],
    },
    {
      code: 'RETAIL_INVENTORY',
      name: 'Inventory Management',
      description: 'Stock control and optimization',
      icon: 'database',
      modules: [
        {
          code: 'INVENTORY_CONTROL',
          name: 'Inventory Control',
          description: 'Stock levels and replenishment',
          kpis: [
            { code: 'inventory_turnover', name: 'Inventory Turnover', category: 'Operations', unit: 'ratio', description: 'Times inventory sold per year', target: 12, icon: 'activity' },
            { code: 'stockout_rate', name: 'Stockout Rate', category: 'Operations', unit: 'percent', description: 'Items out of stock', icon: 'chart' },
            { code: 'days_on_hand', name: 'Days of Inventory', category: 'Operations', unit: 'number', description: 'Days of stock on hand', icon: 'package' },
            { code: 'carrying_cost', name: 'Inventory Carrying Cost', category: 'Financial', unit: 'currency', description: 'Cost to hold inventory', icon: 'dollar' },
          ],
          entities: [
            { code: 'products', name: 'Products', description: 'Product catalog and inventory', recordsPerMinute: 50 },
            { code: 'stock_movements', name: 'Stock Movements', description: 'Inventory transactions', recordsPerMinute: 300 },
          ],
        },
      ],
    },
  ],
};

// =============================================================================
// MANUFACTURING INDUSTRY
// =============================================================================

export const manufacturingIndustry: IndustryDefinition = {
  code: 'MANUFACTURING',
  name: 'Manufacturing',
  description: 'Discrete and process manufacturing operations',
  valueChains: [
    {
      code: 'MFG_PRODUCTION',
      name: 'Production Operations',
      description: 'Manufacturing execution and efficiency',
      icon: 'zap',
      modules: [
        {
          code: 'PRODUCTION_EFFICIENCY',
          name: 'Production Efficiency',
          description: 'Equipment and process performance',
          kpis: [
            { code: 'oee', name: 'Overall Equipment Effectiveness', category: 'Efficiency', unit: 'percent', description: 'Availability × Performance × Quality', target: 85, icon: 'zap' },
            { code: 'availability', name: 'Equipment Availability', category: 'Efficiency', unit: 'percent', description: 'Uptime vs planned production time', target: 95, icon: 'activity' },
            { code: 'cycle_time', name: 'Cycle Time', category: 'Performance', unit: 'time', description: 'Time to produce one unit', icon: 'activity' },
            { code: 'throughput', name: 'Throughput', category: 'Performance', unit: 'number', description: 'Units produced per hour', icon: 'trending' },
          ],
          entities: [
            { code: 'equipment', name: 'Equipment', description: 'Machine status and sensors', recordsPerMinute: 1000 },
            { code: 'production_runs', name: 'Production Runs', description: 'Batch and job data', recordsPerMinute: 50 },
          ],
        },
        {
          code: 'QUALITY_CONTROL',
          name: 'Quality Control',
          description: 'Product quality and defect management',
          kpis: [
            { code: 'fpy', name: 'First Pass Yield', category: 'Quality', unit: 'percent', description: 'Units passing quality first time', target: 98, icon: 'target' },
            { code: 'defect_rate', name: 'Defect Rate', category: 'Quality', unit: 'percent', description: 'Percentage of defective units', icon: 'chart' },
            { code: 'scrap_rate', name: 'Scrap Rate', category: 'Quality', unit: 'percent', description: 'Material scrapped in production', icon: 'chart' },
            { code: 'rework_rate', name: 'Rework Rate', category: 'Quality', unit: 'percent', description: 'Units requiring rework', icon: 'activity' },
          ],
          entities: [
            { code: 'quality_records', name: 'Quality Records', description: 'Inspection and test results', recordsPerMinute: 200 },
            { code: 'defects', name: 'Defects', description: 'Defect tracking and root cause', recordsPerMinute: 20 },
          ],
        },
      ],
    },
    {
      code: 'MFG_SUPPLY_CHAIN',
      name: 'Supply Chain',
      description: 'Materials and supplier management',
      icon: 'package',
      modules: [
        {
          code: 'SUPPLIER_MANAGEMENT',
          name: 'Supplier Management',
          description: 'Supplier performance and relationships',
          kpis: [
            { code: 'supplier_otd', name: 'Supplier On-Time Delivery', category: 'Operations', unit: 'percent', description: 'Supplier deliveries on time', target: 95, icon: 'target' },
            { code: 'supplier_quality', name: 'Supplier Quality Rate', category: 'Quality', unit: 'percent', description: 'Incoming material quality', target: 99, icon: 'target' },
            { code: 'lead_time', name: 'Supplier Lead Time', category: 'Operations', unit: 'time', description: 'Days from order to receipt', icon: 'activity' },
          ],
          entities: [
            { code: 'suppliers', name: 'Suppliers', description: 'Supplier master data', recordsPerMinute: 5 },
            { code: 'purchase_orders', name: 'Purchase Orders', description: 'PO and receipt data', recordsPerMinute: 30 },
          ],
        },
        {
          code: 'MATERIALS_MANAGEMENT',
          name: 'Materials Management',
          description: 'Raw materials and WIP inventory',
          kpis: [
            { code: 'material_turnover', name: 'Material Turnover', category: 'Operations', unit: 'ratio', description: 'Times materials used per year', icon: 'activity' },
            { code: 'wip_value', name: 'WIP Value', category: 'Financial', unit: 'currency', description: 'Work in progress inventory value', icon: 'dollar' },
            { code: 'material_variance', name: 'Material Usage Variance', category: 'Financial', unit: 'percent', description: 'Actual vs standard usage', icon: 'chart' },
          ],
          entities: [
            { code: 'materials', name: 'Materials', description: 'Raw material inventory', recordsPerMinute: 100 },
            { code: 'bom', name: 'Bill of Materials', description: 'Product structure data', recordsPerMinute: 10 },
          ],
        },
      ],
    },
    {
      code: 'MFG_MAINTENANCE',
      name: 'Maintenance',
      description: 'Equipment maintenance and reliability',
      icon: 'activity',
      modules: [
        {
          code: 'PREDICTIVE_MAINTENANCE',
          name: 'Predictive Maintenance',
          description: 'AI-driven maintenance optimization',
          kpis: [
            { code: 'mtbf', name: 'Mean Time Between Failures', category: 'Efficiency', unit: 'time', description: 'Average time between equipment failures', icon: 'activity' },
            { code: 'mttr', name: 'Mean Time To Repair', category: 'Efficiency', unit: 'time', description: 'Average repair duration', icon: 'activity' },
            { code: 'planned_maintenance', name: 'Planned Maintenance %', category: 'Operations', unit: 'percent', description: 'Maintenance that is planned vs reactive', target: 80, icon: 'target' },
            { code: 'maintenance_cost', name: 'Maintenance Cost', category: 'Financial', unit: 'currency', description: 'Total maintenance spend', icon: 'dollar' },
          ],
          entities: [
            { code: 'work_orders', name: 'Work Orders', description: 'Maintenance work orders', recordsPerMinute: 15 },
            { code: 'sensor_data', name: 'Sensor Data', description: 'IoT sensor readings', recordsPerMinute: 5000 },
          ],
        },
      ],
    },
  ],
};

// =============================================================================
// HEALTHCARE INDUSTRY
// =============================================================================

export const healthcareIndustry: IndustryDefinition = {
  code: 'HEALTHCARE',
  name: 'Healthcare',
  description: 'Healthcare providers, payers, and life sciences',
  valueChains: [
    {
      code: 'HC_PATIENT_CARE',
      name: 'Patient Care',
      description: 'Clinical care delivery and outcomes',
      icon: 'users',
      modules: [
        {
          code: 'PATIENT_OUTCOMES',
          name: 'Patient Outcomes',
          description: 'Clinical quality and patient health',
          kpis: [
            { code: 'readmission_rate', name: '30-Day Readmission Rate', category: 'Quality', unit: 'percent', description: 'Patients readmitted within 30 days', icon: 'chart' },
            { code: 'patient_satisfaction', name: 'Patient Satisfaction', category: 'Quality', unit: 'percent', description: 'HCAHPS satisfaction score', target: 85, icon: 'target' },
            { code: 'mortality_rate', name: 'Mortality Rate', category: 'Quality', unit: 'percent', description: 'Patient mortality rate', icon: 'chart' },
            { code: 'infection_rate', name: 'Hospital Infection Rate', category: 'Quality', unit: 'percent', description: 'HAI rate per 1000 patient days', icon: 'chart' },
          ],
          entities: [
            { code: 'patients', name: 'Patients', description: 'Patient demographics and history', recordsPerMinute: 50 },
            { code: 'encounters', name: 'Encounters', description: 'Patient visits and admissions', recordsPerMinute: 100 },
          ],
        },
        {
          code: 'CLINICAL_EFFICIENCY',
          name: 'Clinical Efficiency',
          description: 'Care delivery efficiency',
          kpis: [
            { code: 'los', name: 'Average Length of Stay', category: 'Efficiency', unit: 'number', description: 'Average patient stay in days', icon: 'activity' },
            { code: 'bed_utilization', name: 'Bed Utilization Rate', category: 'Efficiency', unit: 'percent', description: 'Occupied beds vs available', target: 85, icon: 'target' },
            { code: 'ed_wait_time', name: 'ED Wait Time', category: 'Efficiency', unit: 'time', description: 'Average emergency dept wait', icon: 'activity' },
            { code: 'door_to_doctor', name: 'Door to Doctor Time', category: 'Efficiency', unit: 'time', description: 'Time from arrival to physician', icon: 'activity' },
          ],
          entities: [
            { code: 'beds', name: 'Beds', description: 'Bed availability and status', recordsPerMinute: 20 },
            { code: 'staff', name: 'Clinical Staff', description: 'Staff scheduling and assignments', recordsPerMinute: 30 },
          ],
        },
      ],
    },
    {
      code: 'HC_REVENUE_CYCLE',
      name: 'Revenue Cycle',
      description: 'Billing and reimbursement',
      icon: 'dollar',
      modules: [
        {
          code: 'CLAIMS_MANAGEMENT',
          name: 'Claims Management',
          description: 'Claims submission and processing',
          kpis: [
            { code: 'clean_claim_rate', name: 'Clean Claim Rate', category: 'Financial', unit: 'percent', description: 'Claims accepted first submission', target: 95, icon: 'target' },
            { code: 'denial_rate', name: 'Claim Denial Rate', category: 'Financial', unit: 'percent', description: 'Claims denied by payers', icon: 'chart' },
            { code: 'days_in_ar', name: 'Days in A/R', category: 'Financial', unit: 'number', description: 'Average days to collect', icon: 'activity' },
            { code: 'net_collection_rate', name: 'Net Collection Rate', category: 'Financial', unit: 'percent', description: 'Collections vs expected', target: 98, icon: 'dollar' },
          ],
          entities: [
            { code: 'claims', name: 'Claims', description: 'Insurance claims data', recordsPerMinute: 80 },
            { code: 'payments', name: 'Payments', description: 'Payment and remittance', recordsPerMinute: 40 },
          ],
        },
      ],
    },
    {
      code: 'HC_POPULATION_HEALTH',
      name: 'Population Health',
      description: 'Population health management',
      icon: 'activity',
      modules: [
        {
          code: 'RISK_MANAGEMENT',
          name: 'Risk Management',
          description: 'Patient risk stratification',
          kpis: [
            { code: 'high_risk_patients', name: 'High Risk Patient %', category: 'Quality', unit: 'percent', description: 'Patients in high risk category', icon: 'chart' },
            { code: 'chronic_care_compliance', name: 'Chronic Care Compliance', category: 'Quality', unit: 'percent', description: 'Chronic patients following care plans', target: 80, icon: 'target' },
            { code: 'preventive_care_rate', name: 'Preventive Care Rate', category: 'Quality', unit: 'percent', description: 'Patients receiving preventive care', target: 70, icon: 'target' },
            { code: 'cost_per_member', name: 'Cost Per Member', category: 'Financial', unit: 'currency', description: 'Healthcare cost per member per month', icon: 'dollar' },
          ],
          entities: [
            { code: 'risk_scores', name: 'Risk Scores', description: 'Patient risk stratification', recordsPerMinute: 25 },
            { code: 'care_plans', name: 'Care Plans', description: 'Patient care management plans', recordsPerMinute: 15 },
          ],
        },
      ],
    },
  ],
};

// =============================================================================
// INDUSTRY REGISTRY
// =============================================================================

export const industries: Record<string, IndustryDefinition> = {
  RETAIL: retailIndustry,
  MANUFACTURING: manufacturingIndustry,
  HEALTHCARE: healthcareIndustry,
};

export const getIndustryByName = (name: string): IndustryDefinition | null => {
  const lower = name.toLowerCase();
  if (lower.includes('retail') || lower.includes('ecommerce') || lower.includes('commerce')) {
    return retailIndustry;
  }
  if (lower.includes('manufactur') || lower.includes('production') || lower.includes('factory')) {
    return manufacturingIndustry;
  }
  if (lower.includes('health') || lower.includes('medical') || lower.includes('hospital') || lower.includes('clinical')) {
    return healthcareIndustry;
  }
  return null;
};

export const getAllKPIsForIndustry = (industry: IndustryDefinition): IndustryKPI[] => {
  return industry.valueChains.flatMap(vc => 
    vc.modules.flatMap(m => m.kpis)
  );
};

export const getAllEntitiesForIndustry = (industry: IndustryDefinition): IndustryEntity[] => {
  return industry.valueChains.flatMap(vc => 
    vc.modules.flatMap(m => m.entities)
  );
};

export default industries;
