"""
Migrate KPI definitions from BaseKPI class format to dictionary format
"""

import os
import re
from pathlib import Path

# Path to KPI definitions
KPI_DIR = Path(__file__).parent.parent / "services" / "business_services" / "analytics_metadata_service" / "definitions" / "kpis"

def convert_basekpi_to_dict(file_path: Path) -> str:
    """Convert a BaseKPI class definition to dictionary format."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if it's already a dictionary format
    if 'BaseKPI' not in content:
        print(f"  ✓ Already in dictionary format: {file_path.name}")
        return None
    
    # Extract class name
    class_match = re.search(r'class\s+(\w+)\(BaseKPI\)', content)
    if not class_match:
        print(f"  ✗ Could not find class definition: {file_path.name}")
        return None
    
    class_name = class_match.group(1)
    
    # Extract __init__ parameters
    init_match = re.search(r'super\(\).__init__\((.*?)\)', content, re.DOTALL)
    if not init_match:
        print(f"  ✗ Could not find __init__ call: {file_path.name}")
        return None
    
    init_params = init_match.group(1)
    
    # Parse parameters
    params = {}
    
    # Extract code
    code_match = re.search(r'code\s*=\s*["\']([^"\']+)["\']', init_params)
    if code_match:
        params['code'] = code_match.group(1)
    
    # Extract name
    name_match = re.search(r'name_\s*=\s*["\']([^"\']+)["\']', init_params)
    if name_match:
        params['name'] = name_match.group(1)
    
    # Extract description
    desc_match = re.search(r'description_\s*=\s*["\']([^"\']+)["\']', init_params)
    if desc_match:
        params['description'] = desc_match.group(1)
    
    # Extract category
    cat_match = re.search(r'category_\s*=\s*["\']([^"\']+)["\']', init_params)
    if cat_match:
        params['category'] = cat_match.group(1)
    
    # Extract modules
    mod_match = re.search(r'modules_\s*=\s*\[([^\]]+)\]', init_params)
    if mod_match:
        modules_str = mod_match.group(1)
        modules = [m.strip().strip('"\'') for m in modules_str.split(',')]
        params['modules'] = modules
    
    # Extract required_objects
    obj_match = re.search(r'required_objects\s*=\s*\[([^\]]*)\]', init_params)
    if obj_match:
        objects_str = obj_match.group(1).strip()
        if objects_str:
            required_objects = [o.strip().strip('"\'') for o in objects_str.split(',')]
            params['required_objects'] = required_objects
        else:
            params['required_objects'] = []
    
    # Extract formula
    formula_match = re.search(r'formula_\s*=\s*["\']([^"\']+)["\']', init_params)
    if formula_match:
        params['formula'] = formula_match.group(1)
    
    # Extract unit
    unit_match = re.search(r'unit_\s*=\s*["\']([^"\']+)["\']', init_params)
    if unit_match:
        params['unit'] = unit_match.group(1)
    
    # Extract aggregation_methods
    agg_match = re.search(r'aggregation_methods\s*=\s*\[([^\]]+)\]', init_params)
    if agg_match:
        agg_str = agg_match.group(1)
        aggregation_methods = [a.strip().strip('"\'') for a in agg_str.split(',')]
        params['aggregation_methods'] = aggregation_methods
    
    # Extract time_periods
    time_match = re.search(r'time_periods\s*=\s*\[([^\]]+)\]', init_params)
    if time_match:
        time_str = time_match.group(1)
        time_periods = [t.strip().strip('"\'') for t in time_str.split(',')]
        params['time_periods'] = time_periods
    
    # Build dictionary format
    dict_name = params['code']
    
    new_content = f'''"""
{params.get('name', '')} KPI Definition
"""

{dict_name} = {{
    "code": "{params['code']}",
    "name": "{params.get('name', '')}",
    "display_name": "{params.get('name', '')}",
    "description": "{params.get('description', '')}",
    "formula": "{params.get('formula', '')}",
    "unit": "{params.get('unit', 'count')}",
'''
    
    if 'category' in params:
        new_content += f'''    "category": "{params['category']}",
'''
    
    if 'aggregation_methods' in params:
        agg_list = ', '.join([f'"{a}"' for a in params['aggregation_methods']])
        new_content += f'''    "aggregation_methods": [{agg_list}],
'''
    
    if 'time_periods' in params:
        time_list = ', '.join([f'"{t}"' for t in params['time_periods']])
        new_content += f'''    "time_periods": [{time_list}],
'''
    
    # Add required_objects to metadata_
    req_objs = params.get('required_objects', [])
    req_objs_str = ', '.join([f'"{obj}"' for obj in req_objs]) if req_objs else ''
    
    modules_list = ', '.join([f'"{m}"' for m in params.get('modules', [])])
    
    new_content += f'''    "metadata_": {{
        "modules": [{modules_list}],
        "required_objects": [{req_objs_str}]
    }},
    "modules": [{modules_list}],
    "module_code": "{params.get('modules', [''])[0]}",
}}
'''
    
    return new_content


def migrate_all_kpis():
    """Migrate all KPI definitions in the directory."""
    
    print(f"\n🔄 Migrating KPI definitions from BaseKPI to dictionary format...")
    print(f"📁 Directory: {KPI_DIR}\n")
    
    # Find all Python files
    kpi_files = list(KPI_DIR.glob("*.py"))
    
    # Exclude base_kpi.py and __init__.py
    kpi_files = [f for f in kpi_files if f.name not in ['base_kpi.py', '__init__.py']]
    
    migrated_count = 0
    skipped_count = 0
    error_count = 0
    
    for kpi_file in sorted(kpi_files):
        print(f"Processing: {kpi_file.name}")
        
        try:
            new_content = convert_basekpi_to_dict(kpi_file)
            
            if new_content:
                # Backup original
                backup_path = kpi_file.with_suffix('.py.bak')
                kpi_file.rename(backup_path)
                
                # Write new content
                with open(kpi_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"  ✓ Migrated successfully")
                migrated_count += 1
            else:
                skipped_count += 1
        
        except Exception as e:
            print(f"  ✗ Error: {e}")
            error_count += 1
    
    print(f"\n📊 Migration Summary:")
    print(f"  ✓ Migrated: {migrated_count}")
    print(f"  ⊘ Skipped: {skipped_count}")
    print(f"  ✗ Errors: {error_count}")
    print(f"  📝 Total: {len(kpi_files)}")
    
    if migrated_count > 0:
        print(f"\n💾 Backups created with .bak extension")
        print(f"⚠️  Please review the migrated files and test before deleting backups")


if __name__ == "__main__":
    migrate_all_kpis()
