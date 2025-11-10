"""
Validate system integrity.
Check for missing references, orphaned objects, and inconsistencies.
"""

import re
import json
import shutil
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def archive_old_validation_report(output_dir):
    """Archive existing validation report before creating new one."""
    output_dir = Path(output_dir)
    archive_dir = output_dir / "archive"
    archive_dir.mkdir(exist_ok=True)
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # File to archive
    validation_file = output_dir / "validation_report.json"
    
    if validation_file.exists():
        archive_name = f"validation_report_{timestamp}.json"
        archive_path = archive_dir / archive_name
        shutil.move(str(validation_file), str(archive_path))
        print(f"📦 Archived: validation_report.json → archive/{archive_name}")
        print(f"✓ Archived old validation report\n")
        return 1
    
    return 0

def validate_system_integrity(config):
    """Validate the complete system integrity."""
    print("Validating system integrity...")
    
    # Archive old validation report first
    output_dir = Path(config['paths']['output_dir'])
    archive_old_validation_report(output_dir)
    
    issues = {
        'errors': [],
        'warnings': [],
        'info': []
    }
    
    kpi_dir = Path(config['paths']['kpis_dir'])
    obj_dir = Path(config['paths']['objects_dir'])
    
    # Load all KPIs and objects
    kpis = {}
    objects = {}
    
    # Load KPIs
    for kpi_file in kpi_dir.glob('*.py'):
        if kpi_file.name in ['__init__.py', 'registry.py']:
            continue
        
        with open(kpi_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        code_match = re.search(r'code="([^"]+)"', content)
        req_obj_match = re.search(r'"required_objects":\s*\[([^\]]+)\]', content)
        
        if code_match:
            code = code_match.group(1)
            required_objects = []
            if req_obj_match:
                objects_str = req_obj_match.group(1)
                required_objects = [obj.strip().strip('"') for obj in objects_str.split(',')]
            
            kpis[code] = {
                'file': kpi_file.name,
                'required_objects': required_objects
            }
    
    # Load objects
    for obj_file in obj_dir.glob('*.py'):
        if obj_file.name in ['__init__.py', 'registry.py']:
            continue
        
        with open(obj_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        name_match = re.search(r'name="([^"]+)"', content)
        if name_match:
            name = name_match.group(1)
            objects[name] = {
                'file': obj_file.name
            }
    
    # Validation checks
    print(f"  Loaded {len(kpis)} KPIs and {len(objects)} objects")
    
    # Check 1: KPIs without required_objects
    kpis_without_objects = [code for code, data in kpis.items() if not data['required_objects']]
    if kpis_without_objects:
        issues['errors'].append({
            'type': 'missing_required_objects',
            'count': len(kpis_without_objects),
            'items': kpis_without_objects[:10]
        })
    
    # Check 2: KPIs referencing non-existent objects
    all_object_names = set(objects.keys())
    for kpi_code, kpi_data in kpis.items():
        for req_obj in kpi_data['required_objects']:
            if req_obj not in all_object_names and req_obj != "TBD":
                issues['warnings'].append({
                    'type': 'missing_object_reference',
                    'kpi': kpi_code,
                    'object': req_obj
                })
    
    # Check 3: Orphaned objects (not referenced by any KPI)
    referenced_objects = set()
    for kpi_data in kpis.values():
        referenced_objects.update(kpi_data['required_objects'])
    
    orphaned = all_object_names - referenced_objects
    if orphaned:
        issues['info'].append({
            'type': 'orphaned_objects',
            'count': len(orphaned),
            'items': sorted(list(orphaned))
        })
    
    # Print summary
    print(f"\n  Validation Results:")
    print(f"    Errors: {len(issues['errors'])}")
    print(f"    Warnings: {len(issues['warnings'])}")
    print(f"    Info: {len(issues['info'])}")
    
    if issues['errors']:
        print(f"\n  Errors found:")
        for error in issues['errors']:
            print(f"    - {error['type']}: {error.get('count', 1)} items")
    
    # Save validation report
    output_dir = Path(config['paths']['output_dir'])
    report_file = output_dir / 'validation_report.json'
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(issues, f, indent=2)
    
    print(f"\n  Validation report saved to: {report_file}")
    
    return issues

if __name__ == '__main__':
    import json
    with open('config.json', 'r') as f:
        config = json.load(f)
    validate_system_integrity(config)
