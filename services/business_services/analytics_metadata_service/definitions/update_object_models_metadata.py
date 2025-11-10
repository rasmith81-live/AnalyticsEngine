"""
Update all object models with complete metadata:
- Associated modules
- Related KPIs
- Key attributes needed for KPI calculations
- UML relationships to related objects
"""

import re
from pathlib import Path
from collections import defaultdict

def extract_kpi_info(kpi_file):
    """Extract KPI code, name, modules, and required objects."""
    with open(kpi_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract fields
    code_match = re.search(r'code="([^"]+)"', content)
    name_match = re.search(r'name="([^"]+)"', content)
    modules_match = re.search(r'"modules":\s*\[([^\]]+)\]', content)
    required_objects_match = re.search(r'"required_objects":\s*\[([^\]]+)\]', content)
    
    code = code_match.group(1) if code_match else None
    name = name_match.group(1) if name_match else None
    
    modules = []
    if modules_match:
        modules_str = modules_match.group(1)
        modules = [m.strip().strip('"') for m in modules_str.split(',')]
    
    required_objects = []
    if required_objects_match:
        objects_str = required_objects_match.group(1)
        required_objects = [obj.strip().strip('"') for obj in objects_str.split(',')]
    
    return {
        'code': code,
        'name': name,
        'modules': modules,
        'required_objects': required_objects,
        'file': kpi_file.name
    }

def build_object_to_kpi_mapping():
    """Build mapping of object models to KPIs that use them."""
    kpi_dir = Path('kpis')
    kpi_files = list(kpi_dir.glob('*.py'))
    
    object_to_kpis = defaultdict(lambda: {
        'kpis': [],
        'modules': set(),
        'attributes_needed': set()
    })
    
    print(f"Analyzing {len(kpi_files)} KPI files...")
    
    for kpi_file in kpi_files:
        if kpi_file.name in ['__init__.py', 'registry.py']:
            continue
        
        try:
            kpi_info = extract_kpi_info(kpi_file)
            
            if not kpi_info['required_objects']:
                continue
            
            for obj in kpi_info['required_objects']:
                object_to_kpis[obj]['kpis'].append({
                    'code': kpi_info['code'],
                    'name': kpi_info['name']
                })
                object_to_kpis[obj]['modules'].update(kpi_info['modules'])
                
                # Infer attributes based on KPI name
                attributes = infer_attributes_from_kpi(kpi_info['name'], obj)
                object_to_kpis[obj]['attributes_needed'].update(attributes)
        
        except Exception as e:
            print(f"  Error processing {kpi_file.name}: {e}")
    
    return object_to_kpis

def infer_attributes_from_kpi(kpi_name, object_name):
    """Infer which attributes are needed based on KPI name and object."""
    attributes = set()
    kpi_lower = kpi_name.lower()
    obj_lower = object_name.lower()
    
    # Common attribute patterns
    attribute_patterns = {
        'revenue': ['revenue', 'amount', 'value'],
        'cost': ['cost', 'expense'],
        'price': ['price', 'unit_price'],
        'discount': ['discount', 'discount_percentage'],
        'date': ['date', 'created_date', 'closed_date', 'start_date', 'end_date'],
        'time': ['timestamp', 'duration', 'time'],
        'status': ['status', 'state'],
        'count': ['count', 'quantity'],
        'rate': ['rate', 'percentage'],
        'score': ['score', 'rating'],
        'name': ['name', 'title'],
        'id': ['id', 'identifier'],
        'owner': ['owner_id', 'assigned_to'],
        'source': ['source', 'channel'],
        'type': ['type', 'category'],
    }
    
    # Add common attributes for all objects
    attributes.add('id')
    attributes.add('created_date')
    
    # Add specific attributes based on KPI keywords
    for keyword, attrs in attribute_patterns.items():
        if keyword in kpi_lower:
            attributes.update(attrs)
    
    # Object-specific attributes
    if 'sale' in obj_lower or 'deal' in obj_lower:
        attributes.update(['amount', 'close_date', 'status', 'sales_rep_id'])
    
    if 'lead' in obj_lower or 'opportunity' in obj_lower:
        attributes.update(['status', 'source', 'score', 'created_date', 'converted_date'])
    
    if 'customer' in obj_lower or 'account' in obj_lower:
        attributes.update(['name', 'account_value', 'status', 'segment'])
    
    if 'product' in obj_lower:
        attributes.update(['name', 'price', 'category', 'sku'])
    
    if 'representative' in obj_lower or 'rep' in obj_lower:
        attributes.update(['name', 'team_id', 'quota', 'hire_date'])
    
    if 'quota' in obj_lower or 'target' in obj_lower:
        attributes.update(['target_amount', 'period', 'sales_rep_id'])
    
    return attributes

def get_related_objects(object_name, object_to_kpis):
    """Get objects that are commonly used together with this object."""
    related = set()
    
    # Find KPIs that use this object
    if object_name in object_to_kpis:
        for kpi in object_to_kpis[object_name]['kpis']:
            # For each KPI, find other objects it uses
            for obj, data in object_to_kpis.items():
                if obj != object_name:
                    for kpi_data in data['kpis']:
                        if kpi_data['code'] == kpi['code']:
                            related.add(obj)
    
    return sorted(list(related))

def extract_object_model_info(obj_file):
    """Extract current object model information."""
    with open(obj_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract code
    code_match = re.search(r'code="([^"]+)"', content)
    name_match = re.search(r'name="([^"]+)"', content)
    
    return {
        'code': code_match.group(1) if code_match else None,
        'name': name_match.group(1) if name_match else None,
        'content': content
    }

def update_object_model_metadata(obj_file, object_to_kpis):
    """Update object model with complete metadata."""
    obj_info = extract_object_model_info(obj_file)
    obj_name = obj_info['name']
    
    if not obj_name or obj_name not in object_to_kpis:
        return False, "Object not found in KPI mappings"
    
    data = object_to_kpis[obj_name]
    content = obj_info['content']
    
    # Prepare metadata updates
    modules = sorted(list(data['modules']))
    kpi_codes = sorted([kpi['code'] for kpi in data['kpis']])
    attributes = sorted(list(data['attributes_needed']))
    related_objects = get_related_objects(obj_name, object_to_kpis)
    
    # Check if metadata already has these fields
    has_related_kpis = '"related_kpis"' in content
    has_key_attributes = '"key_attributes"' in content
    has_related_objects = '"related_objects"' in content
    
    if has_related_kpis and has_key_attributes and has_related_objects:
        return False, "Already has complete metadata"
    
    # Find metadata section
    metadata_pattern = r'(metadata_=\{[^}]*?)(}[\s\n]*\))'
    
    def add_fields(match):
        metadata_content = match.group(1)
        closing = match.group(2)
        
        # Remove trailing comma if present
        metadata_content = metadata_content.rstrip()
        if metadata_content.endswith(','):
            metadata_content = metadata_content[:-1]
        
        new_fields = []
        
        # Add related_kpis if not present
        if not has_related_kpis and kpi_codes:
            kpis_str = ', '.join([f'"{code}"' for code in kpi_codes[:20]])  # Limit to 20
            if len(kpi_codes) > 20:
                kpis_str += f'  # ... and {len(kpi_codes) - 20} more'
            new_fields.append(f'"related_kpis": [{kpis_str}]')
        
        # Add key_attributes if not present
        if not has_key_attributes and attributes:
            attrs_str = ', '.join([f'"{attr}"' for attr in attributes[:15]])  # Limit to 15
            new_fields.append(f'"key_attributes": [{attrs_str}]')
        
        # Add related_objects if not present
        if not has_related_objects and related_objects:
            objs_str = ', '.join([f'"{obj}"' for obj in related_objects[:15]])  # Limit to 15
            new_fields.append(f'"related_objects": [{objs_str}]')
        
        if new_fields:
            fields_str = ',\n        '.join(new_fields)
            return f'{metadata_content},\n        {fields_str}{closing}'
        
        return match.group(0)
    
    updated_content = re.sub(metadata_pattern, add_fields, content, flags=re.DOTALL)
    
    if updated_content != content:
        with open(obj_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True, {
            'modules': len(modules),
            'kpis': len(kpi_codes),
            'attributes': len(attributes),
            'related_objects': len(related_objects)
        }
    
    return False, "No changes needed"

def main():
    print("=" * 80)
    print("UPDATING OBJECT MODEL METADATA")
    print("=" * 80)
    print()
    
    # Step 1: Build object-to-KPI mapping
    print("Step 1: Building object-to-KPI mappings...")
    object_to_kpis = build_object_to_kpi_mapping()
    print(f"  Found {len(object_to_kpis)} unique objects referenced in KPIs")
    print()
    
    # Step 2: Update object model files
    print("Step 2: Updating object model files...")
    obj_dir = Path('object_models')
    obj_files = list(obj_dir.glob('*.py'))
    
    updated_count = 0
    skipped_count = 0
    error_count = 0
    
    for obj_file in sorted(obj_files):
        if obj_file.name in ['__init__.py', 'registry.py']:
            continue
        
        try:
            success, result = update_object_model_metadata(obj_file, object_to_kpis)
            
            if success:
                updated_count += 1
                if updated_count <= 15:
                    print(f"✅ {obj_file.name}")
                    if isinstance(result, dict):
                        print(f"   Modules: {result['modules']}, KPIs: {result['kpis']}, "
                              f"Attributes: {result['attributes']}, Related: {result['related_objects']}")
            else:
                skipped_count += 1
                if "not found" in str(result):
                    print(f"⚠️  {obj_file.name}: {result}")
        
        except Exception as e:
            error_count += 1
            print(f"❌ {obj_file.name}: {str(e)}")
    
    if updated_count > 15:
        print(f"... and {updated_count - 15} more files updated")
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"✅ Updated: {updated_count}")
    print(f"⏭️  Skipped: {skipped_count}")
    print(f"❌ Errors: {error_count}")
    print(f"📊 Total object files: {len(obj_files)}")
    print()
    print("Next step: Review and refine the added metadata as needed.")
    print("=" * 80)

if __name__ == '__main__':
    main()
