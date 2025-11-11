"""
Restore Formulas from Old Backup

This script restores formula fields from the old class-based KPI definitions
in the November 8th backup, which contain the original formulas.
"""

import os
import sys
import re
from pathlib import Path
from typing import Dict, Any, Optional
import importlib.util

# Paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
KPIS_DIR = PROJECT_ROOT / "services" / "business_services" / "analytics_metadata_service" / "definitions" / "kpis"
OLD_BACKUP_DIR = Path(__file__).parent / "backups" / "definitions_backup_20251108_091602" / "kpis"

def load_current_kpi(file_path: Path) -> Optional[Dict[str, Any]]:
    """Load a KPI definition from current dictionary format."""
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


def extract_formula_from_old_format(file_path: Path) -> Optional[str]:
    """Extract formula from old class-based KPI format."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for formula= pattern
        formula_match = re.search(r'formula\s*=\s*["\']([^"\']+)["\']', content)
        if formula_match:
            return formula_match.group(1)
        
        return None
    except Exception as e:
        print(f"  ✗ Error reading old format {file_path.name}: {e}")
        return None


def write_kpi_file(kpi: Dict[str, Any], file_path: Path):
    """Write KPI back to file."""
    kpi_var_name = kpi['code']
    
    # Build the file content
    lines = ['"""', f"{kpi.get('name', kpi_var_name)}", '']
    if 'description' in kpi and kpi['description']:
        lines.append(kpi['description'])
    lines.extend(['"""', ''])
    
    lines.append(f"{kpi_var_name} = {{")
    
    # Define field order
    field_order = [
        'code', 'name', 'description', 'formula', 'calculation_formula',
        'category', 'is_active', 'full_kpi_definition', 'trend_analysis',
        'diagnostic_questions', 'actionable_tips', 'visualization_suggestions',
        'risk_warnings', 'tracking_tools', 'integration_points',
        'change_impact_analysis', 'metadata_', 'required_objects',
        'modules', 'module_code', 'sample_data'
    ]
    
    # Write fields in order
    for field in field_order:
        if field not in kpi:
            continue
            
        value = kpi[field]
        
        if field == 'sample_data':
            # Write sample_data as formatted JSON
            import json
            lines.append(f'    "{field}": {json.dumps(value, indent=8)[:-1]}    }},')
        elif isinstance(value, str):
            # Multi-line strings
            if '\n' in value:
                lines.append(f'    "{field}": """')
                lines.append(value)
                lines.append('    """,')
            else:
                import json
                lines.append(f'    "{field}": {json.dumps(value)},')
        elif isinstance(value, (list, dict)):
            import json
            lines.append(f'    "{field}": {json.dumps(value)},')
        elif isinstance(value, bool):
            lines.append(f'    "{field}": {str(value)},')
        else:
            import json
            lines.append(f'    "{field}": {json.dumps(value)},')
    
    lines.append('}')
    lines.append('')
    
    # Write to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


def main():
    """Main execution function."""
    print("\n🔄 Restoring Formulas from Old Backup (Nov 8)")
    print("=" * 70)
    print(f"📁 Current KPIs: {KPIS_DIR}")
    print(f"📁 Old Backup: {OLD_BACKUP_DIR}\n")
    
    if not OLD_BACKUP_DIR.exists():
        print(f"❌ Old backup directory not found: {OLD_BACKUP_DIR}")
        return
    
    # Get all KPI files
    current_files = {f.name: f for f in KPIS_DIR.glob("*.py") 
                     if f.name not in ['__init__.py', 'base_kpi.py']}
    old_backup_files = {f.name: f for f in OLD_BACKUP_DIR.glob("*.py") 
                        if f.name not in ['__init__.py', 'base_kpi.py']}
    
    print(f"🔄 Processing {len(current_files)} KPI files...\n")
    
    restored_count = 0
    no_backup_count = 0
    no_formula_count = 0
    no_change_count = 0
    errors = 0
    
    for filename, current_path in sorted(current_files.items()):
        print(f"Processing: {filename}")
        
        # Load current KPI
        current_kpi = load_current_kpi(current_path)
        if not current_kpi:
            errors += 1
            print(f"  ✗ Failed to load current KPI")
            continue
        
        # Check if old backup exists
        if filename not in old_backup_files:
            no_backup_count += 1
            print(f"  ⊘ No old backup found")
            continue
        
        # Extract formula from old format
        old_formula = extract_formula_from_old_format(old_backup_files[filename])
        if not old_formula:
            no_formula_count += 1
            print(f"  ⊘ No formula in old backup")
            continue
        
        # Check if current formula needs restoration
        current_formula = current_kpi.get('formula', '')
        
        if current_formula in ['', 'To be defined']:
            # Restore formula
            current_kpi['formula'] = old_formula
            
            # Also set calculation_formula if it's empty
            if current_kpi.get('calculation_formula', '') in ['', 'To be defined']:
                current_kpi['calculation_formula'] = old_formula
            
            # Write updated KPI
            write_kpi_file(current_kpi, current_path)
            restored_count += 1
            print(f"  ✓ Restored formula: {old_formula[:60]}...")
            print(f"  ✓ File updated")
        else:
            no_change_count += 1
            print(f"  ⊘ Formula already present")
    
    # Summary
    print(f"\n📊 Summary:")
    print(f"  Total KPIs: {len(current_files)}")
    print(f"  ✓ Formulas Restored: {restored_count}")
    print(f"  ⊘ No Changes Needed: {no_change_count}")
    print(f"  ⊘ No Old Backup: {no_backup_count}")
    print(f"  ⊘ No Formula in Backup: {no_formula_count}")
    print(f"  ✗ Errors: {errors}")
    
    print(f"\n🎉 Formula restoration complete!")


if __name__ == "__main__":
    main()
