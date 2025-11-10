"""
Generate SCOR-based KPI definitions from SCOR metrics.

This script reads SCOR metrics from the framework and generates KPI Python files
with proper SCOR metadata enrichment.

SCOR Metrics → KPIs → Required Objects → Layer 2 Tables
"""

import json
from pathlib import Path
from typing import Dict, List, Any

# SCOR Level 1 Strategic Metrics
# Source: SCOR 14.0 Framework
SCOR_LEVEL_1_METRICS = {
    # Reliability (RL) - Perfect Order Fulfillment
    "RL.1.1": {
        "name": "Perfect Order Fulfillment",
        "description": "Percentage of orders delivered on time, complete, damage-free, with correct documentation",
        "performance_attribute": "Reliability",
        "level": "Level 1 - Strategic",
        "unit": "percentage",
        "formula": "(Perfect Orders / Total Orders) * 100",
        "calculation_detail": """
        Perfect Order = Order that meets ALL criteria:
        - Delivered on time (by customer requested date)
        - Complete (all items, correct quantities)
        - Damage-free (no defects, proper condition)
        - Correct documentation (invoice, packing slip, etc.)
        """,
        "required_objects": ["Order", "Shipment", "Delivery", "OrderLine"],
        "aggregation_methods": ["percentage"],
        "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
        "dimensions": ["region", "customer_segment", "product_line", "facility", "carrier"],
        "target_benchmark": {
            "superior": 99.0,
            "advantage": 95.0,
            "parity": 90.0,
            "disadvantage": 85.0
        }
    },
    
    # Responsiveness (RS) - Order Fulfillment Cycle Time
    "RS.1.1": {
        "name": "Order Fulfillment Cycle Time",
        "description": "Average time from order receipt to customer delivery",
        "performance_attribute": "Responsiveness",
        "level": "Level 1 - Strategic",
        "unit": "days",
        "formula": "AVG(Delivery Date - Order Receipt Date)",
        "calculation_detail": """
        Cycle Time = Time from order receipt to delivery
        Measured in business days or calendar days
        Includes: Order processing, picking, packing, shipping, delivery
        """,
        "required_objects": ["Order", "Shipment", "Delivery"],
        "aggregation_methods": ["average", "median", "percentile_90"],
        "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
        "dimensions": ["region", "customer_segment", "product_line", "order_type", "priority"],
        "target_benchmark": {
            "superior": 1.0,
            "advantage": 2.0,
            "parity": 3.0,
            "disadvantage": 5.0
        }
    },
    
    # Agility (AG) - Upside Supply Chain Flexibility
    "AG.1.1": {
        "name": "Upside Supply Chain Flexibility",
        "description": "Number of days to achieve 20% increase in delivered quantity",
        "performance_attribute": "Agility",
        "level": "Level 1 - Strategic",
        "unit": "days",
        "formula": "Days to achieve 20% sustained increase",
        "calculation_detail": """
        Measures ability to respond to demand spikes
        Time to ramp up production/delivery by 20%
        Sustained increase (not one-time spike)
        """,
        "required_objects": ["Capacity", "Production", "Inventory", "Supplier"],
        "aggregation_methods": ["average", "min"],
        "time_periods": ["quarterly", "annually"],
        "dimensions": ["product_line", "facility", "supplier"],
        "target_benchmark": {
            "superior": 7,
            "advantage": 14,
            "parity": 30,
            "disadvantage": 60
        }
    },
    
    # Agility (AG) - Downside Supply Chain Adaptability
    "AG.1.2": {
        "name": "Downside Supply Chain Adaptability",
        "description": "Percentage reduction in cost for 20% decrease in delivered quantity",
        "performance_attribute": "Agility",
        "level": "Level 1 - Strategic",
        "unit": "percentage",
        "formula": "(Cost Reduction / Original Cost) * 100 for 20% volume decrease",
        "calculation_detail": """
        Measures ability to reduce costs when demand drops
        Cost flexibility when volume decreases by 20%
        Includes: Variable costs, fixed cost reduction
        """,
        "required_objects": ["Cost", "Production", "Capacity"],
        "aggregation_methods": ["percentage"],
        "time_periods": ["quarterly", "annually"],
        "dimensions": ["product_line", "facility", "cost_center"],
        "target_benchmark": {
            "superior": 15.0,
            "advantage": 12.0,
            "parity": 8.0,
            "disadvantage": 5.0
        }
    },
    
    # Costs (CO) - Total Supply Chain Management Cost
    "CO.1.1": {
        "name": "Total Supply Chain Management Cost",
        "description": "Sum of all costs to plan, source, make, deliver, and return",
        "performance_attribute": "Costs",
        "level": "Level 1 - Strategic",
        "unit": "dollars",
        "formula": "SUM(Plan Cost + Source Cost + Make Cost + Deliver Cost + Return Cost)",
        "calculation_detail": """
        Total SC Cost = All supply chain costs
        - Plan: Planning, forecasting, S&OP
        - Source: Procurement, supplier management
        - Make: Manufacturing, production
        - Deliver: Warehousing, transportation, order management
        - Return: Reverse logistics, warranty
        """,
        "required_objects": ["Cost", "Activity", "CostCenter"],
        "aggregation_methods": ["sum", "average"],
        "time_periods": ["monthly", "quarterly", "annually"],
        "dimensions": ["process", "cost_center", "product_line", "facility"],
        "target_benchmark": {
            "superior": "< 5% of revenue",
            "advantage": "5-7% of revenue",
            "parity": "7-10% of revenue",
            "disadvantage": "> 10% of revenue"
        }
    },
    
    # Costs (CO) - Cost of Goods Sold
    "CO.1.2": {
        "name": "Cost of Goods Sold",
        "description": "Direct costs attributable to production of goods sold",
        "performance_attribute": "Costs",
        "level": "Level 1 - Strategic",
        "unit": "dollars",
        "formula": "SUM(Material Cost + Labor Cost + Manufacturing Overhead)",
        "calculation_detail": """
        COGS = Direct production costs
        - Material: Raw materials, components
        - Labor: Direct manufacturing labor
        - Overhead: Factory overhead allocated to production
        """,
        "required_objects": ["Cost", "Product", "Production", "Material"],
        "aggregation_methods": ["sum", "average"],
        "time_periods": ["monthly", "quarterly", "annually"],
        "dimensions": ["product_line", "facility", "cost_category"],
        "target_benchmark": {
            "superior": "< 60% of revenue",
            "advantage": "60-70% of revenue",
            "parity": "70-80% of revenue",
            "disadvantage": "> 80% of revenue"
        }
    },
    
    # Profit (PR) - Return on Supply Chain Fixed Assets
    "PR.1.1": {
        "name": "Return on Supply Chain Fixed Assets",
        "description": "Return generated from supply chain fixed assets",
        "performance_attribute": "Profit",
        "level": "Level 1 - Strategic",
        "unit": "percentage",
        "formula": "(Supply Chain Revenue - COGS - SC Operating Expense) / SC Fixed Assets * 100",
        "calculation_detail": """
        ROSCFA = Profitability of SC assets
        Numerator: SC contribution margin
        Denominator: SC fixed assets (property, plant, equipment)
        """,
        "required_objects": ["Revenue", "Cost", "Asset"],
        "aggregation_methods": ["percentage"],
        "time_periods": ["quarterly", "annually"],
        "dimensions": ["facility", "asset_category"],
        "target_benchmark": {
            "superior": 25.0,
            "advantage": 20.0,
            "parity": 15.0,
            "disadvantage": 10.0
        }
    },
    
    # Asset Management (AM) - Cash-to-Cash Cycle Time
    "AM.1.1": {
        "name": "Cash-to-Cash Cycle Time",
        "description": "Time between paying suppliers and receiving payment from customers",
        "performance_attribute": "Asset Management",
        "level": "Level 1 - Strategic",
        "unit": "days",
        "formula": "Days Inventory Outstanding + Days Sales Outstanding - Days Payable Outstanding",
        "calculation_detail": """
        C2C = Working capital efficiency
        DIO: Avg days inventory held
        DSO: Avg days to collect receivables
        DPO: Avg days to pay suppliers
        Lower is better (faster cash conversion)
        """,
        "required_objects": ["Inventory", "Payment", "Receipt", "Invoice"],
        "aggregation_methods": ["average"],
        "time_periods": ["monthly", "quarterly", "annually"],
        "dimensions": ["product_line", "customer_segment", "supplier"],
        "target_benchmark": {
            "superior": 30,
            "advantage": 45,
            "parity": 60,
            "disadvantage": 90
        }
    },
    
    # Asset Management (AM) - Return on Working Capital
    "AM.1.2": {
        "name": "Return on Working Capital",
        "description": "Return generated from working capital invested in supply chain",
        "performance_attribute": "Asset Management",
        "level": "Level 1 - Strategic",
        "unit": "percentage",
        "formula": "(Supply Chain Revenue - COGS - SC Operating Expense) / (Inventory + AR - AP) * 100",
        "calculation_detail": """
        ROWC = Efficiency of working capital
        Numerator: SC contribution margin
        Denominator: Working capital (Inventory + Receivables - Payables)
        """,
        "required_objects": ["Revenue", "Cost", "Inventory", "AccountsReceivable", "AccountsPayable"],
        "aggregation_methods": ["percentage"],
        "time_periods": ["quarterly", "annually"],
        "dimensions": ["product_line", "facility"],
        "target_benchmark": {
            "superior": 50.0,
            "advantage": 35.0,
            "parity": 25.0,
            "disadvantage": 15.0
        }
    },
    
    # Environmental (EV) - Carbon Emissions
    "EV.1.1": {
        "name": "Carbon Emissions per Unit",
        "description": "Total greenhouse gas emissions per unit produced/delivered",
        "performance_attribute": "Environmental",
        "level": "Level 1 - Strategic",
        "unit": "kg_co2e",
        "formula": "Total CO2 Equivalent Emissions / Units Produced",
        "calculation_detail": """
        Carbon Footprint = GHG emissions per unit
        Includes: Scope 1, 2, and 3 emissions
        - Scope 1: Direct emissions (manufacturing)
        - Scope 2: Indirect (electricity, heating)
        - Scope 3: Supply chain (suppliers, logistics)
        """,
        "required_objects": ["Emission", "Production", "Energy", "Transportation"],
        "aggregation_methods": ["average", "sum"],
        "time_periods": ["monthly", "quarterly", "annually"],
        "dimensions": ["product_line", "facility", "scope", "source"],
        "target_benchmark": {
            "superior": "< 5 kg CO2e/unit",
            "advantage": "5-10 kg CO2e/unit",
            "parity": "10-20 kg CO2e/unit",
            "disadvantage": "> 20 kg CO2e/unit"
        }
    },
    
    # Social (SC) - Worker Safety Incident Rate
    "SC.1.1": {
        "name": "Worker Safety Incident Rate",
        "description": "Number of recordable safety incidents per 100 workers",
        "performance_attribute": "Social",
        "level": "Level 1 - Strategic",
        "unit": "incidents_per_100_workers",
        "formula": "(Number of Recordable Incidents / Total Hours Worked) * 200,000",
        "calculation_detail": """
        TRIR = Total Recordable Incident Rate
        OSHA standard calculation
        200,000 = hours for 100 workers (50 weeks * 40 hours)
        Includes: Injuries, illnesses requiring medical treatment
        """,
        "required_objects": ["SafetyIncident", "Employee", "WorkHours"],
        "aggregation_methods": ["rate"],
        "time_periods": ["monthly", "quarterly", "annually"],
        "dimensions": ["facility", "department", "shift", "incident_type"],
        "target_benchmark": {
            "superior": 0.5,
            "advantage": 1.0,
            "parity": 2.0,
            "disadvantage": 3.0
        }
    }
}

def generate_kpi_file(scor_id: str, metric_data: Dict[str, Any], output_dir: Path) -> None:
    """Generate a KPI Python file from SCOR metric data."""
    
    # Create KPI code from name
    kpi_code = metric_data["name"].upper().replace(" ", "_").replace("-", "_")
    file_name = metric_data["name"].lower().replace(" ", "_").replace("-", "_") + ".py"
    
    # Generate required objects list
    required_objects_str = ", ".join([f'"{obj}"' for obj in metric_data["required_objects"]])
    
    # Generate dimensions list
    dimensions_str = ", ".join([f'"{dim}"' for dim in metric_data["dimensions"]])
    
    # Generate aggregation methods
    aggregation_str = ", ".join([f'"{agg}"' for agg in metric_data["aggregation_methods"]])
    
    # Generate time periods
    time_periods_str = ", ".join([f'"{period}"' for period in metric_data["time_periods"]])
    
    # Generate benchmark dict
    benchmark = metric_data["target_benchmark"]
    if isinstance(benchmark["superior"], str):
        benchmark_str = f"""{{
            "superior": "{benchmark['superior']}",
            "advantage": "{benchmark['advantage']}",
            "parity": "{benchmark['parity']}",
            "disadvantage": "{benchmark['disadvantage']}"
        }}"""
    else:
        benchmark_str = f"""{{
            "superior": {benchmark['superior']},
            "advantage": {benchmark['advantage']},
            "parity": {benchmark['parity']},
            "disadvantage": {benchmark['disadvantage']}
        }}"""
    
    # Generate KPI file content
    content = f'''"""
{metric_data["name"]} KPI

SCOR Metric: {scor_id}
Performance Attribute: {metric_data["performance_attribute"]}
Level: {metric_data["level"]}

{metric_data["description"]}

Formula:
{metric_data["formula"]}

Calculation Details:
{metric_data["calculation_detail"]}

Required Objects: {", ".join(metric_data["required_objects"])}
"""

from analytics_models import KPI

{kpi_code} = KPI(
    code="{kpi_code}",
    name="{metric_data["name"]}",
    category="Supply Chain {metric_data["performance_attribute"]}",
    description="{metric_data["description"]}",
    
    formula="""
{metric_data["formula"]}
    """,
    
    metadata_={{
        # SCOR Framework Reference
        "scor_reference": {{
            "metric_id": "{scor_id}",
            "performance_attribute": "{metric_data["performance_attribute"]}",
            "level": "{metric_data["level"]}",
            "scor_version": "14.0"
        }},
        
        # Required Business Objects
        "required_objects": [{required_objects_str}],
        
        # Module Assignment
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN"],
        
        # Calculation Configuration
        "unit": "{metric_data["unit"]}",
        "aggregation_methods": [{aggregation_str}],
        "time_periods": [{time_periods_str}],
        
        # Dimensional Analysis
        "dimensions": [{dimensions_str}],
        
        # Benchmarks (SCOR Industry Standards)
        "target_benchmark": {benchmark_str},
        
        # Calculation Details
        "calculation_detail": """
{metric_data["calculation_detail"]}
        """,
        
        # Data Quality
        "data_quality_requirements": {{
            "completeness": 0.95,
            "accuracy": 0.98,
            "timeliness": "daily"
        }},
        
        # Reporting
        "reporting_frequency": ["daily", "weekly", "monthly", "quarterly", "annually"],
        "dashboard_priority": "high",
        "executive_visibility": True
    }}
)
'''
    
    # Write to file
    output_path = output_dir / file_name
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"[SUCCESS] Generated {file_name}")
    print(f"  - KPI Code: {kpi_code}")
    print(f"  - SCOR ID: {scor_id}")
    print(f"  - Required Objects: {len(metric_data['required_objects'])}")
    print()

def main():
    """Generate all SCOR Level 1 KPIs."""
    
    print("=" * 80)
    print("GENERATING SCOR-BASED KPI DEFINITIONS")
    print("=" * 80)
    print()
    
    # Create output directory
    project_root = Path(__file__).parent.parent.parent
    output_dir = project_root / 'services' / 'business_services' / 'analytics_models' / 'definitions' / 'kpis' / 'scor'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"[INFO] Output directory: {output_dir}")
    print(f"[INFO] Generating {len(SCOR_LEVEL_1_METRICS)} Level 1 SCOR KPIs")
    print()
    
    # Generate KPI for each SCOR metric
    success_count = 0
    all_required_objects = set()
    
    for scor_id, metric_data in SCOR_LEVEL_1_METRICS.items():
        try:
            generate_kpi_file(scor_id, metric_data, output_dir)
            success_count += 1
            all_required_objects.update(metric_data["required_objects"])
        except Exception as e:
            print(f"[ERROR] Failed to generate KPI for {scor_id}: {e}")
            print()
    
    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"KPIs Generated: {success_count}/{len(SCOR_LEVEL_1_METRICS)}")
    print(f"Output Directory: {output_dir}")
    print()
    
    print("Required Object Models:")
    for obj in sorted(all_required_objects):
        print(f"  - {obj}")
    print()
    
    print(f"Total Unique Objects: {len(all_required_objects)}")
    print()
    
    print("Next Steps:")
    print("1. Review generated KPI files in definitions/kpis/scor/")
    print("2. Check which object models already exist")
    print("3. Create missing object models")
    print("4. Run CQRS scripts for new object models")
    print()
    print("=" * 80)
    
    return success_count == len(SCOR_LEVEL_1_METRICS)

if __name__ == '__main__':
    import sys
    success = main()
    sys.exit(0 if success else 1)
