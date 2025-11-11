"""
Restore Formulas from Backup

This script restores formula and calculation_formula fields from the backup
taken before validation, preserving the original formula data while keeping
the newly added fields like sample_data.
"""

import os
import sys
from pathlib import Path
from typing import Dict, Any, Optional
import importlib.util

# Paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
KPIS_DIR = PROJECT_ROOT / "services" / "business_services" / "analytics_metadata_service" / "definitions" / "kpis"
BACKUP_DIR = Path(__file__).parent / "backups" / "kpis_backup_20251110_134322"

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
    print("\n🔄 Restoring Formulas from Backup")
    print("=" * 70)
    print(f"📁 Current KPIs: {KPIS_DIR}")
    print(f"📁 Backup KPIs: {BACKUP_DIR}\n")
    
    if not BACKUP_DIR.exists():
        print(f"❌ Backup directory not found: {BACKUP_DIR}")
        return
    
    # Get all KPI files
    current_files = {f.name: f for f in KPIS_DIR.glob("*.py") 
                     if f.name not in ['__init__.py', 'base_kpi.py']}
    backup_files = {f.name: f for f in BACKUP_DIR.glob("*.py") 
                    if f.name not in ['__init__.py', 'base_kpi.py']}
    
    print(f"🔄 Processing {len(current_files)} KPI files...\n")
    
    restored_count = 0
    no_backup_count = 0
    no_change_count = 0
    errors = 0
    
    for filename, current_path in sorted(current_files.items()):
        print(f"Processing: {filename}")
        
        # Load current KPI
        current_kpi = load_kpi(current_path)
        if not current_kpi:
            errors += 1
            print(f"  ✗ Failed to load current KPI")
            continue
        
        # Check if backup exists
        if filename not in backup_files:
            no_backup_count += 1
            print(f"  ⊘ No backup found")
            continue
        
        # Load backup KPI
        backup_kpi = load_kpi(backup_files[filename])
        if not backup_kpi:
            errors += 1
            print(f"  ✗ Failed to load backup KPI")
            continue
        
        # Check if formula needs restoration
        current_formula = current_kpi.get('formula', '')
        backup_formula = backup_kpi.get('formula', '')
        
        current_calc = current_kpi.get('calculation_formula', '')
        backup_calc = backup_kpi.get('calculation_formula', '')
        
        needs_restore = False
        
        # Restore formula if current is default and backup has real value
        if (current_formula in ['', 'To be defined'] and 
            backup_formula and backup_formula not in ['', 'To be defined']):
            current_kpi['formula'] = backup_formula
            needs_restore = True
            print(f"  ✓ Restored formula: {backup_formula[:50]}...")
        
        # Restore calculation_formula if current is default and backup has real value
        if (current_calc in ['', 'To be defined'] and 
            backup_calc and backup_calc not in ['', 'To be defined']):
            current_kpi['calculation_formula'] = backup_calc
            needs_restore = True
            print(f"  ✓ Restored calculation_formula: {backup_calc[:50]}...")
        
        if needs_restore:
            # Write updated KPI
            write_kpi_file(current_kpi, current_path)
            restored_count += 1
            print(f"  ✓ File updated")
        else:
            no_change_count += 1
            print(f"  ⊘ No restoration needed")
    
    # Summary
    print(f"\n📊 Summary:")
    print(f"  Total KPIs: {len(current_files)}")
    print(f"  ✓ Formulas Restored: {restored_count}")
    print(f"  ⊘ No Changes: {no_change_count}")
    print(f"  ⊘ No Backup: {no_backup_count}")
    print(f"  ✗ Errors: {errors}")
    
    print(f"\n🎉 Formula restoration complete!")


if __name__ == "__main__":
    main()
