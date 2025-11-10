"""
SCOR Metrics Excel Processor

Reads SCOR metrics from Excel file and generates KPI Python files.

Usage:
    python process_scor_excel.py --input data/scor_metrics_complete.xlsx
"""

import pandas as pd
import json
from pathlib import Path
from typing import Dict, List, Any
import re


def clean_text(text: Any) -> str:
    """Clean and normalize text fields."""
    if pd.isna(text) or text is None:
        return ""
    return str(text).strip()


def parse_list_field(text: str) -> List[str]:
    """Parse comma-separated list fields."""
    if not text:
        return []
    return [item.strip() for item in text.split(',') if item.strip()]


def read_scor_metrics_excel(file_path: str) -> List[Dict[str, Any]]:
    """
    Read SCOR metrics from Excel file.
    
    Args:
        file_path: Path to Excel file
    
    Returns:
        List of metric dictionaries
    """
    print(f"📖 Reading Excel file: {file_path}")
    
    # Read the Metrics sheet
    df = pd.read_excel(file_path, sheet_name='Metrics')
    
    print(f"✅ Found {len(df)} metrics in Excel file")
    
    metrics = []
    for idx, row in df.iterrows():
        metric = {
            "id": clean_text(row['metric_id']),
            "name": clean_text(row['metric_name']),
            "attribute": clean_text(row['attribute']).lower(),
            "level": clean_text(row['level']).lower(),
            "definition": clean_text(row['definition']),
            "calculation": clean_text(row['calculation']),
            "calculation_notes": clean_text(row.get('calculation_notes', '')),
            "unit": clean_text(row['unit']),
            "dimension": clean_text(row.get('dimension', '')),
            "data_collection": clean_text(row.get('data_collection', '')),
            "primary_source": clean_text(row.get('primary_source', '')),
            "discussion": clean_text(row.get('discussion', '')),
            "component_metrics": parse_list_field(clean_text(row.get('component_metrics', ''))),
            "parent_metric": clean_text(row.get('parent_metric', '')),
            "related_processes": parse_list_field(clean_text(row.get('related_processes', ''))),
            "url": clean_text(row.get('url', ''))
        }
        
        # Validate required fields
        if not metric['id'] or not metric['name']:
            print(f"⚠️  Skipping row {idx + 2}: Missing metric_id or metric_name")
            continue
        
        metrics.append(metric)
    
    print(f"✅ Processed {len(metrics)} valid metrics")
    return metrics


def read_benchmarks_excel(file_path: str) -> Dict[str, Dict[str, Any]]:
    """
    Read benchmark data from Excel file.
    
    Args:
        file_path: Path to Excel file
    
    Returns:
        Dictionary of benchmarks by metric_id
    """
    try:
        df = pd.read_excel(file_path, sheet_name='Benchmarks')
        print(f"✅ Found {len(df)} benchmark entries")
        
        benchmarks = {}
        for idx, row in df.iterrows():
            metric_id = clean_text(row['metric_id'])
            if not metric_id:
                continue
            
            if metric_id not in benchmarks:
                benchmarks[metric_id] = []
            
            benchmarks[metric_id].append({
                "industry": clean_text(row.get('industry', 'General')),
                "percentile_10": float(row['percentile_10']) if pd.notna(row.get('percentile_10')) else None,
                "percentile_25": float(row['percentile_25']) if pd.notna(row.get('percentile_25')) else None,
                "percentile_50": float(row['percentile_50']) if pd.notna(row.get('percentile_50')) else None,
                "percentile_75": float(row['percentile_75']) if pd.notna(row.get('percentile_75')) else None,
                "percentile_90": float(row['percentile_90']) if pd.notna(row.get('percentile_90')) else None,
                "best_in_class": float(row['best_in_class']) if pd.notna(row.get('best_in_class')) else None,
                "source": clean_text(row.get('source', 'SCOR'))
            })
        
        return benchmarks
    
    except Exception as e:
        print(f"⚠️  No benchmarks sheet found or error reading: {e}")
        return {}


def generate_kpi_file(metric: Dict[str, Any], benchmarks: Dict[str, Any], output_dir: Path):
    """
    Generate a KPI Python file from metric data.
    
    Args:
        metric: Metric dictionary
        benchmarks: Benchmarks for this metric
        output_dir: Output directory for KPI files
    """
    metric_id = metric['id']
    file_name = metric_id.lower().replace('.', '_') + '.py'
    file_path = output_dir / file_name
    
    # Convert metric name to Python variable name
    kpi_code = metric['name'].upper().replace(' ', '_').replace('-', '_')
    kpi_code = re.sub(r'[^A-Z0-9_]', '', kpi_code)
    
    # Build required objects list from data sources
    required_objects = []
    if metric['primary_source']:
        required_objects.append(metric['primary_source'])
    
    # Add objects from component metrics (infer from discussion/data_collection)
    discussion_lower = metric['discussion'].lower()
    data_collection_lower = metric['data_collection'].lower()
    
    common_objects = ['Order', 'OrderLine', 'Shipment', 'Delivery', 'Invoice', 'Payment', 
                     'Inventory', 'Supplier', 'Product', 'Customer', 'Cost', 'Revenue']
    
    for obj in common_objects:
        if obj.lower() in discussion_lower or obj.lower() in data_collection_lower:
            if obj not in required_objects:
                required_objects.append(obj)
    
    # Generate Python file content
    content = f'''"""
{metric['name']} KPI

SCOR Metric: {metric_id}
Level: {metric['level'].replace('_', ' ').title()}
Attribute: {metric['attribute'].title()}

{metric['definition'][:200]}...
"""

from analytics_models import KPI

{kpi_code} = KPI(
    name="{metric['name']}",
    code="{kpi_code}",
    description="""{metric['definition']}""",
    
    calculation="""{metric['calculation']}""",
    
    unit="{metric['unit']}",
    
    metadata_={{
        "modules": ["ASCM_SCOR"],
        "value_chains": ["SUPPLY_CHAIN"],
        
        # SCOR Framework Metadata
        "scor_metric_id": "{metric_id}",
        "scor_level": "{metric['level']}",
        "scor_attribute": "{metric['attribute']}",
        "scor_url": "{metric['url']}",
        
        # Hierarchy
'''
    
    if metric['parent_metric']:
        content += f'''        "parent_metric": "{metric['parent_metric']}",
'''
    
    if metric['component_metrics']:
        content += f'''        "component_metrics": {json.dumps(metric['component_metrics'])},
'''
    
    content += f'''        
        # Calculation Details
        "calculation_method": """{metric['calculation']}""",
'''
    
    if metric['calculation_notes']:
        content += f'''        "calculation_notes": """{metric['calculation_notes']}""",
'''
    
    if metric['dimension']:
        content += f'''        "dimension": "{metric['dimension']}",
'''
    
    content += f'''        
        # Data Collection
'''
    
    if metric['data_collection']:
        content += f'''        "data_collection": """{metric['data_collection']}""",
'''
    
    if metric['primary_source']:
        content += f'''        "primary_source": "{metric['primary_source']}",
'''
    
    if required_objects:
        content += f'''        "required_objects": {json.dumps(required_objects)},
'''
    
    if metric['related_processes']:
        content += f'''        "related_processes": {json.dumps(metric['related_processes'])},
'''
    
    # Add benchmarks if available
    if benchmarks:
        content += f'''        
        # Industry Benchmarks
        "benchmarks": {json.dumps(benchmarks, indent=12)},
'''
    
    if metric['discussion']:
        # Truncate discussion if too long
        discussion = metric['discussion']
        if len(discussion) > 500:
            discussion = discussion[:500] + "..."
        content += f'''        
        # Discussion
        "implementation_notes": """{discussion}""",
'''
    
    content += f'''        
        # Aggregation
        "aggregation_methods": ["average", "sum", "count"],
        "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
        "dimensions": ["product", "customer", "region", "facility"]
    }}
)
'''
    
    # Write file
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return file_path


def main():
    """Main processing function."""
    print("🚀 SCOR Metrics Excel Processor")
    print("=" * 60)
    
    # File paths
    excel_file = Path("C:/Users/Arthu/CascadeProjects/AnalyticsEngine/data/scor_metrics_complete.xlsx")
    output_dir = Path("C:/Users/Arthu/CascadeProjects/AnalyticsEngine/services/business_services/analytics_models/definitions/kpis/scor")
    
    if not excel_file.exists():
        print(f"❌ Excel file not found: {excel_file}")
        print(f"   Please create the file using the template in:")
        print(f"   data/SCOR_METRICS_TEMPLATE.md")
        return
    
    # Read metrics and benchmarks
    metrics = read_scor_metrics_excel(str(excel_file))
    benchmarks_dict = read_benchmarks_excel(str(excel_file))
    
    # Group metrics by level
    by_level = {"level_1": [], "level_2": [], "level_3": []}
    for metric in metrics:
        level = metric.get('level', 'level_1')
        if level in by_level:
            by_level[level].append(metric)
    
    print()
    print("📊 Metrics by Level:")
    print(f"   Level 1 (Strategic): {len(by_level['level_1'])}")
    print(f"   Level 2 (Diagnostic): {len(by_level['level_2'])}")
    print(f"   Level 3 (Operational): {len(by_level['level_3'])}")
    print()
    
    # Generate KPI files
    print("📝 Generating KPI files...")
    generated_files = []
    
    for metric in metrics:
        metric_id = metric['id']
        benchmarks = benchmarks_dict.get(metric_id, [])
        
        try:
            file_path = generate_kpi_file(metric, benchmarks, output_dir)
            generated_files.append(file_path)
            print(f"   ✅ {metric_id}: {metric['name']}")
        except Exception as e:
            print(f"   ❌ {metric_id}: Error - {e}")
    
    print()
    print(f"✅ Generated {len(generated_files)} KPI files")
    print(f"   Location: {output_dir}")
    print()
    print("🎉 Processing complete!")
    print()
    print("Next steps:")
    print("1. Review generated KPI files")
    print("2. Update ASCM_SCOR module with new KPIs")
    print("3. Run gap analysis to identify missing objects")


if __name__ == "__main__":
    main()
