"""
Validate and Enhance KPI Definitions

This script ensures all KPIs have the required fields and generates sample data
for robust visualization on the configuration page.

Required KPI Fields:
- code, name, description, formula, calculation_formula, category, is_active
- full_kpi_definition, trend_analysis, diagnostic_questions, actionable_tips
- visualization_suggestions, risk_warnings, tracking_tools, integration_points
- change_impact_analysis, metadata_, required_objects, modules, module_code
- sample_data (NEW)
"""

import os
import sys
import json
import random
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import importlib.util

# Paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
KPIS_DIR = PROJECT_ROOT / "services" / "business_services" / "analytics_metadata_service" / "definitions" / "kpis"
OUTPUT_DIR = Path(__file__).parent / "output"
BACKUP_DIR = Path(__file__).parent / "backups"

# Ensure directories exist
OUTPUT_DIR.mkdir(exist_ok=True)
BACKUP_DIR.mkdir(exist_ok=True)

# Required fields for each KPI
REQUIRED_FIELDS = [
    "code",
    "name",
    "description",
    "formula",
    "calculation_formula",
    "category",
    "is_active",
    "full_kpi_definition",
    "trend_analysis",
    "diagnostic_questions",
    "actionable_tips",
    "visualization_suggestions",
    "risk_warnings",
    "tracking_tools",
    "integration_points",
    "change_impact_analysis",
    "metadata_",
    "required_objects",
    "modules",
    "module_code",
    "sample_data"  # NEW
]


def load_kpi(file_path: Path) -> Optional[Dict[str, Any]]:
    """Load a KPI definition from a Python file."""
    try:
        spec = importlib.util.spec_from_file_location("module", file_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Find the dictionary definition (uppercase variable)
            for attr_name in dir(module):
                if attr_name.isupper() and not attr_name.startswith('_'):
                    obj = getattr(module, attr_name)
                    if isinstance(obj, dict) and 'code' in obj:
                        return obj
        return None
    except Exception as e:
        print(f"  ✗ Error loading {file_path.name}: {e}")
        return None


def detect_kpi_type(kpi: Dict[str, Any]) -> str:
    """Detect the type of KPI based on formula and name."""
    formula = kpi.get('formula', '').lower()
    name = kpi.get('name', '').lower()
    
    # Percentage/Rate KPIs
    if any(x in name for x in ['rate', 'ratio', 'percentage', '%']):
        return 'percentage'
    
    # Count KPIs
    if any(x in formula for x in ['count', 'number of', 'total number']):
        return 'count'
    
    # Currency KPIs
    if any(x in name for x in ['revenue', 'cost', 'price', 'value', 'amount', 'margin']):
        return 'currency'
    
    # Time KPIs
    if any(x in name for x in ['time', 'duration', 'days', 'hours', 'cycle']):
        return 'time'
    
    # Score KPIs
    if any(x in name for x in ['score', 'index', 'rating']):
        return 'score'
    
    # Default to metric
    return 'metric'


def analyze_formula(formula: str) -> Dict[str, Any]:
    """Analyze formula to understand what it calculates."""
    formula_lower = formula.lower()
    
    # Check for division (ratio/rate)
    has_division = '/' in formula or 'divided by' in formula_lower
    
    # Check for multiplication by 100 (percentage)
    is_percentage = '* 100' in formula or '× 100' in formula or 'percentage' in formula_lower
    
    # Check for sum/total
    is_sum = 'sum' in formula_lower or 'total' in formula_lower
    
    # Check for average
    is_average = 'average' in formula_lower or 'mean' in formula_lower
    
    # Check for count
    is_count = 'count' in formula_lower or 'number of' in formula_lower
    
    return {
        'has_division': has_division,
        'is_percentage': is_percentage,
        'is_sum': is_sum,
        'is_average': is_average,
        'is_count': is_count
    }


def generate_sample_data(kpi: Dict[str, Any]) -> Dict[str, Any]:
    """Generate sample data for a KPI based on its type and formula."""
    kpi_type = detect_kpi_type(kpi)
    kpi_name = kpi.get('name', 'Unknown KPI')
    formula = kpi.get('formula', '')
    
    # Analyze the formula
    formula_analysis = analyze_formula(formula)
    
    # Generate time series data (last 12 months)
    end_date = datetime.now()
    dates = [(end_date - timedelta(days=30*i)).strftime('%Y-%m-%d') for i in range(12)]
    dates.reverse()
    
    # Generate values based on KPI type and formula analysis
    if kpi_type == 'percentage' or formula_analysis['is_percentage']:
        # Percentage values (0-100)
        # If it's a ratio/rate, use realistic percentage ranges
        if formula_analysis['has_division']:
            base_value = random.uniform(50, 75)  # More realistic for ratios
        else:
            base_value = random.uniform(40, 80)
        values = [round(base_value + random.uniform(-10, 10), 2) for _ in range(12)]
        values = [max(0, min(100, v)) for v in values]  # Clamp to 0-100
        unit = '%'
        
    elif kpi_type == 'count':
        # Count values (integers)
        base_value = random.randint(50, 500)
        values = [base_value + random.randint(-20, 30) for _ in range(12)]
        values = [max(0, v) for v in values]  # No negative counts
        unit = 'count'
        
    elif kpi_type == 'currency':
        # Currency values
        base_value = random.uniform(10000, 100000)
        values = [round(base_value + random.uniform(-5000, 10000), 2) for _ in range(12)]
        values = [max(0, v) for v in values]  # No negative currency
        unit = '$'
        
    elif kpi_type == 'time':
        # Time values (days)
        base_value = random.uniform(5, 30)
        values = [round(base_value + random.uniform(-3, 5), 1) for _ in range(12)]
        values = [max(0, v) for v in values]  # No negative time
        unit = 'days'
        
    elif kpi_type == 'score':
        # Score values (0-100)
        base_value = random.uniform(60, 90)
        values = [round(base_value + random.uniform(-5, 8), 1) for _ in range(12)]
        values = [max(0, min(100, v)) for v in values]  # Clamp to 0-100
        unit = 'score'
        
    else:
        # Generic metric
        base_value = random.uniform(100, 1000)
        values = [round(base_value + random.uniform(-50, 100), 2) for _ in range(12)]
        unit = 'units'
    
    # Calculate statistics
    current_value = values[-1]
    previous_value = values[-2] if len(values) > 1 else current_value
    change = current_value - previous_value
    change_percent = (change / previous_value * 100) if previous_value != 0 else 0
    
    avg_value = sum(values) / len(values)
    min_value = min(values)
    max_value = max(values)
    
    # Determine trend
    if len(values) >= 3:
        recent_avg = sum(values[-3:]) / 3
        older_avg = sum(values[:3]) / 3
        if recent_avg > older_avg * 1.05:
            trend = 'increasing'
        elif recent_avg < older_avg * 0.95:
            trend = 'decreasing'
        else:
            trend = 'stable'
    else:
        trend = 'stable'
    
    # Generate breakdown data (by category) - more meaningful based on formula
    # Try to infer category names from formula or KPI name
    formula_lower = formula.lower()
    kpi_name_lower = kpi_name.lower()
    
    # Smart category naming based on context
    if 'account' in formula_lower or 'account' in kpi_name_lower:
        categories = ['Enterprise Accounts', 'Mid-Market', 'Small Business', 'Strategic Partners', 'Other']
    elif 'customer' in formula_lower or 'customer' in kpi_name_lower:
        categories = ['New Customers', 'Existing Customers', 'VIP Customers', 'At-Risk Customers', 'Other']
    elif 'product' in formula_lower or 'product' in kpi_name_lower:
        categories = ['Product Line A', 'Product Line B', 'Product Line C', 'Services', 'Other']
    elif 'sales' in formula_lower or 'sales' in kpi_name_lower or 'revenue' in kpi_name_lower:
        categories = ['Direct Sales', 'Channel Sales', 'Online Sales', 'Enterprise Sales', 'Other']
    elif 'region' in formula_lower or 'territory' in formula_lower:
        categories = ['North America', 'EMEA', 'APAC', 'LATAM', 'Other']
    else:
        categories = ['Segment A', 'Segment B', 'Segment C', 'Segment D', 'Other']
    
    total = current_value
    breakdown_values = []
    remaining = total
    
    for i, cat in enumerate(categories[:-1]):
        if i < len(categories) - 2:
            val = round(remaining * random.uniform(0.15, 0.35), 2)
        else:
            val = round(remaining * random.uniform(0.1, 0.3), 2)
        breakdown_values.append(val)
        remaining -= val
    
    breakdown_values.append(round(max(0, remaining), 2))  # Remaining goes to "Other"
    
    breakdown = [
        {'category': cat, 'value': val, 'percentage': round(val / total * 100, 1) if total > 0 else 0}
        for cat, val in zip(categories, breakdown_values)
    ]
    
    return {
        'time_series': {
            'dates': dates,
            'values': values,
            'unit': unit
        },
        'current': {
            'value': round(current_value, 2),
            'unit': unit,
            'change': round(change, 2),
            'change_percent': round(change_percent, 1),
            'trend': trend
        },
        'statistics': {
            'average': round(avg_value, 2),
            'min': round(min_value, 2),
            'max': round(max_value, 2),
            'unit': unit
        },
        'breakdown': breakdown,
        'metadata': {
            'generated_date': datetime.now().isoformat(),
            'data_points': len(values),
            'kpi_type': kpi_type,
            'kpi_name': kpi_name
        }
    }


def get_default_value(field: str, kpi: Dict[str, Any]) -> Any:
    """Get default value for a missing field."""
    defaults = {
        'is_active': True,
        'category': 'General',
        'formula': 'To be defined',
        'calculation_formula': 'To be defined',
        'full_kpi_definition': f"Complete definition for {kpi.get('name', 'this KPI')} to be added.",
        'trend_analysis': 'Trend analysis to be defined.',
        'diagnostic_questions': '* What factors are influencing this metric?\n* Are there any anomalies in the data?',
        'actionable_tips': '* Monitor this KPI regularly\n* Set appropriate targets and thresholds',
        'visualization_suggestions': '* Line chart for time series analysis\n* Bar chart for comparisons',
        'risk_warnings': '* Monitor for significant deviations from expected values',
        'tracking_tools': '* CRM or analytics platform',
        'integration_points': '* Integrate with related business metrics',
        'change_impact_analysis': 'Changes in this KPI may impact related business processes.',
        'required_objects': [],
        'modules': [],
        'module_code': 'GENERAL'
    }
    
    return defaults.get(field, '')


def validate_and_enhance_kpi(kpi: Dict[str, Any], file_path: Path) -> tuple[Dict[str, Any], List[str]]:
    """Validate KPI and add missing fields with defaults."""
    missing_fields = []
    enhanced_kpi = kpi.copy()
    
    # Check for missing fields
    for field in REQUIRED_FIELDS:
        # Only add default if field is truly missing or empty
        # Don't overwrite existing non-empty values
        field_value = enhanced_kpi.get(field)
        
        # Check if field is missing or empty
        is_missing = (
            field not in enhanced_kpi or 
            field_value is None or 
            (isinstance(field_value, str) and field_value.strip() == '') or
            (isinstance(field_value, list) and len(field_value) == 0)
        )
        
        if is_missing:
            missing_fields.append(field)
            
            # Add default value
            if field == 'sample_data':
                enhanced_kpi[field] = generate_sample_data(enhanced_kpi)
            else:
                enhanced_kpi[field] = get_default_value(field, enhanced_kpi)
    
    # Ensure metadata_ is a dict
    if 'metadata_' not in enhanced_kpi or not isinstance(enhanced_kpi['metadata_'], dict):
        enhanced_kpi['metadata_'] = {}
    
    # Add validation timestamp
    enhanced_kpi['metadata_']['last_validated'] = datetime.now().isoformat()
    
    return enhanced_kpi, missing_fields


def write_kpi_file(kpi: Dict[str, Any], file_path: Path):
    """Write enhanced KPI back to file."""
    kpi_var_name = kpi['code']
    
    # Build the file content
    lines = ['"""', f"{kpi['name']}", '', kpi.get('description', ''), '"""', '']
    lines.append(f"{kpi_var_name} = {{")
    
    # Write each field
    for field in REQUIRED_FIELDS:
        value = kpi.get(field)
        
        if field == 'sample_data':
            # Write sample_data as formatted JSON
            lines.append(f'    "{field}": {json.dumps(value, indent=8)[:-1]}    }},')
        elif isinstance(value, str):
            # Multi-line strings
            if '\n' in value:
                lines.append(f'    "{field}": """')
                lines.append(value)
                lines.append('    """,')
            else:
                lines.append(f'    "{field}": {json.dumps(value)},')
        elif isinstance(value, (list, dict)):
            lines.append(f'    "{field}": {json.dumps(value)},')
        elif isinstance(value, bool):
            lines.append(f'    "{field}": {str(value)},')
        else:
            lines.append(f'    "{field}": {json.dumps(value)},')
    
    lines.append('}')
    lines.append('')
    
    # Write to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


def create_backup():
    """Create a timestamped backup of all KPI definitions."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = BACKUP_DIR / f"kpis_backup_{timestamp}"
    backup_path.mkdir(exist_ok=True)
    
    import shutil
    for file_path in KPIS_DIR.glob("*.py"):
        if file_path.name not in ['__init__.py', 'base_kpi.py']:
            shutil.copy2(file_path, backup_path / file_path.name)
    
    print(f"  💾 Backup created: {backup_path.name}")
    return backup_path


def main():
    """Main execution function."""
    print("\n🔍 KPI Validation and Enhancement")
    print("=" * 70)
    print(f"📁 KPIs Directory: {KPIS_DIR}\n")
    
    # Create backup
    print("📦 Creating backup...")
    create_backup()
    
    # Load all KPIs
    kpi_files = sorted([f for f in KPIS_DIR.glob("*.py") 
                       if f.name not in ['__init__.py', 'base_kpi.py']])
    
    print(f"\n🔄 Processing {len(kpi_files)} KPI files...\n")
    
    results = {
        'total': len(kpi_files),
        'valid': 0,
        'enhanced': 0,
        'errors': 0,
        'missing_fields_summary': {},
        'details': []
    }
    
    for file_path in kpi_files:
        print(f"Processing: {file_path.name}")
        
        # Load KPI
        kpi = load_kpi(file_path)
        if not kpi:
            results['errors'] += 1
            print(f"  ✗ Failed to load")
            continue
        
        # Validate and enhance
        enhanced_kpi, missing_fields = validate_and_enhance_kpi(kpi, file_path)
        
        if missing_fields:
            results['enhanced'] += 1
            print(f"  ⚠️  Enhanced: Added {len(missing_fields)} missing fields")
            for field in missing_fields:
                results['missing_fields_summary'][field] = results['missing_fields_summary'].get(field, 0) + 1
            
            # Write enhanced KPI back to file
            write_kpi_file(enhanced_kpi, file_path)
            print(f"  ✓ Updated file")
        else:
            results['valid'] += 1
            print(f"  ✓ Valid (all fields present)")
        
        results['details'].append({
            'file': file_path.name,
            'kpi_code': kpi.get('code'),
            'kpi_name': kpi.get('name'),
            'missing_fields': missing_fields,
            'status': 'enhanced' if missing_fields else 'valid'
        })
    
    # Generate report
    print(f"\n📊 Summary:")
    print(f"  Total KPIs: {results['total']}")
    print(f"  ✓ Valid: {results['valid']}")
    print(f"  ⚠️  Enhanced: {results['enhanced']}")
    print(f"  ✗ Errors: {results['errors']}")
    
    if results['missing_fields_summary']:
        print(f"\n📋 Missing Fields Summary:")
        for field, count in sorted(results['missing_fields_summary'].items(), key=lambda x: x[1], reverse=True):
            print(f"  • {field}: {count} KPIs")
    
    # Save detailed report
    report_path = OUTPUT_DIR / f"kpi_validation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📄 Detailed report saved: {report_path.name}")
    print(f"\n🎉 Validation and enhancement complete!")


if __name__ == "__main__":
    main()
