"""
Update ALL object models with comprehensive metadata from thorough KPI analysis.
"""

import re
import json
from pathlib import Path
from collections import defaultdict

def load_analysis_results():
    """Load the comprehensive analysis results."""
    results_file = Path('object_model_analysis_results.json')
    
    if not results_file.exists():
        print("Error: Run comprehensive_object_analysis.py first!")
        return None
    
    with open(results_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_object_info(obj_file):
    """Extract object model information."""
    with open(obj_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    name_match = re.search(r'name="([^"]+)"', content)
    code_match = re.search(r'code="([^"]+)"', content)
    
    return {
        'name': name_match.group(1) if name_match else None,
        'code': code_match.group(1) if code_match else None,
        'content': content
    }

def infer_key_attributes(obj_name, kpi_list):
    """Infer key attributes based on object name and KPIs that use it."""
    attributes = set()
    obj_lower = obj_name.lower()
    
    # Always include these
    attributes.add('id')
    attributes.add('created_date')
    attributes.add('updated_date')
    
    # Object-specific attributes based on type
    if 'sale' in obj_lower or 'deal' in obj_lower:
        attributes.update(['amount', 'close_date', 'status', 'sales_rep_id', 'customer_id', 
                          'product_id', 'discount', 'revenue'])
    
    if 'lead' in obj_lower or 'prospect' in obj_lower:
        attributes.update(['status', 'source', 'score', 'converted_date', 'sales_rep_id',
                          'qualification_status'])
    
    if 'opportunity' in obj_lower or 'opp' in obj_lower:
        attributes.update(['status', 'amount', 'probability', 'close_date', 'stage',
                          'sales_rep_id', 'account_id'])
    
    if 'customer' in obj_lower or 'client' in obj_lower or 'account' in obj_lower:
        attributes.update(['name', 'type', 'status', 'segment', 'value', 'health_score',
                          'satisfaction_score', 'churn_risk'])
    
    if 'product' in obj_lower:
        attributes.update(['name', 'price', 'category', 'sku', 'description'])
    
    if 'representative' in obj_lower or 'rep' in obj_lower or 'manager' in obj_lower:
        attributes.update(['name', 'email', 'team_id', 'quota', 'hire_date', 'status'])
    
    if 'team' in obj_lower:
        attributes.update(['name', 'manager_id', 'region', 'quota', 'size'])
    
    if 'quota' in obj_lower or 'target' in obj_lower:
        attributes.update(['target_amount', 'period', 'sales_rep_id', 'achieved_amount'])
    
    if 'territory' in obj_lower or 'region' in obj_lower:
        attributes.update(['name', 'sales_rep_id', 'quota', 'boundaries'])
    
    if 'contract' in obj_lower or 'agreement' in obj_lower:
        attributes.update(['start_date', 'end_date', 'value', 'status', 'customer_id'])
    
    if 'training' in obj_lower or 'coaching' in obj_lower:
        attributes.update(['title', 'date', 'duration', 'participants', 'trainer_id'])
    
    if 'content' in obj_lower or 'playbook' in obj_lower:
        attributes.update(['title', 'type', 'category', 'usage_count', 'effectiveness_score'])
    
    if 'call' in obj_lower or 'email' in obj_lower or 'meeting' in obj_lower or 'appointment' in obj_lower:
        attributes.update(['date', 'duration', 'sales_rep_id', 'customer_id', 'outcome'])
    
    if 'forecast' in obj_lower:
        attributes.update(['period', 'amount', 'confidence', 'sales_rep_id'])
    
    if 'subscription' in obj_lower:
        attributes.update(['start_date', 'end_date', 'amount', 'status', 'customer_id', 'renewal_date'])
    
    if 'feedback' in obj_lower or 'review' in obj_lower:
        attributes.update(['date', 'rating', 'comments', 'customer_id'])
    
    if 'partner' in obj_lower or 'channel' in obj_lower:
        attributes.update(['name', 'type', 'status', 'tier', 'revenue_share'])
    
    return sorted(list(attributes))

def get_related_objects(obj_name, analysis_results):
    """Get objects that appear together in KPIs."""
    related = set()
    
    if obj_name not in analysis_results:
        return []
    
    # Get KPIs that reference this object
    obj_kpis = set(kpi['code'] for kpi in analysis_results[obj_name]['kpis'])
    
    # Find other objects that appear in the same KPIs
    for other_obj, data in analysis_results.items():
        if other_obj != obj_name:
            other_kpis = set(kpi['code'] for kpi in data['kpis'])
            # If they share KPIs, they're related
            if obj_kpis & other_kpis:  # Intersection
                related.add(other_obj)
    
    # Limit to top 20 most frequently co-occurring
    return sorted(list(related))[:20]

def update_object_model_comprehensive(obj_file, analysis_results):
    """Update object model with comprehensive metadata."""
    obj_info = extract_object_info(obj_file)
    obj_name = obj_info['name']
    content = obj_info['content']
    
    if not obj_name:
        return False, "No object name found"
    
    # Get analysis data
    if obj_name not in analysis_results:
        return False, f"No KPI references found for {obj_name}"
    
    data = analysis_results[obj_name]
    
    # Prepare metadata
    modules = sorted(data['modules'])
    kpi_codes = sorted([kpi['code'] for kpi in data['kpis']])
    attributes = infer_key_attributes(obj_name, data['kpis'])
    related_objects = get_related_objects(obj_name, analysis_results)
    
    # Check what's already in metadata
    has_modules = '"modules"' in content
    has_related_kpis = '"related_kpis"' in content
    has_key_attributes = '"key_attributes"' in content
    has_related_objects = '"related_objects"' in content
    
    # Find metadata section
    metadata_pattern = r'(metadata_=\{[^}]*?)(}[\s\n]*\))'
    
    def update_metadata(match):
        metadata_content = match.group(1)
        closing = match.group(2)
        
        # Remove trailing comma
        metadata_content = metadata_content.rstrip()
        if metadata_content.endswith(','):
            metadata_content = metadata_content[:-1]
        
        updates = []
        
        # Update or add modules
        if has_modules and modules:
            # Replace existing modules
            modules_pattern = r'"modules":\s*\[[^\]]*\]'
            modules_str = ', '.join([f'"{m}"' for m in modules])
            metadata_content = re.sub(modules_pattern, f'"modules": [{modules_str}]', metadata_content)
        elif modules:
            modules_str = ', '.join([f'"{m}"' for m in modules])
            updates.append(f'"modules": [{modules_str}]')
        
        # Add related_kpis if not present
        if not has_related_kpis and kpi_codes:
            kpis_str = ', '.join([f'"{code}"' for code in kpi_codes[:30]])  # Limit to 30
            updates.append(f'"related_kpis": [{kpis_str}]')
        
        # Add key_attributes if not present
        if not has_key_attributes and attributes:
            attrs_str = ', '.join([f'"{attr}"' for attr in attributes[:20]])  # Limit to 20
            updates.append(f'"key_attributes": [{attrs_str}]')
        
        # Add related_objects if not present
        if not has_related_objects and related_objects:
            objs_str = ', '.join([f'"{obj}"' for obj in related_objects])
            updates.append(f'"related_objects": [{objs_str}]')
        
        if updates:
            updates_str = ',\n        '.join(updates)
            return f'{metadata_content},\n        {updates_str}{closing}'
        
        return match.group(0)
    
    updated_content = re.sub(metadata_pattern, update_metadata, content, flags=re.DOTALL)
    
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
    print("COMPREHENSIVE OBJECT MODEL METADATA UPDATE")
    print("=" * 80)
    print()
    
    # Load analysis results
    print("Step 1: Loading comprehensive analysis results...")
    analysis_results = load_analysis_results()
    
    if not analysis_results:
        return
    
    print(f"  Loaded data for {len(analysis_results)} objects")
    print()
    
    # Update all object models
    print("Step 2: Updating all object model files...")
    obj_dir = Path('object_models')
    obj_files = list(obj_dir.glob('*.py'))
    
    updated_count = 0
    skipped_count = 0
    error_count = 0
    
    for obj_file in sorted(obj_files):
        if obj_file.name in ['__init__.py', 'registry.py']:
            continue
        
        try:
            success, result = update_object_model_comprehensive(obj_file, analysis_results)
            
            if success:
                updated_count += 1
                if updated_count <= 25:
                    print(f"✅ {obj_file.name}")
                    if isinstance(result, dict):
                        print(f"   Modules: {result['modules']}, KPIs: {result['kpis']}, "
                              f"Attrs: {result['attributes']}, Related: {result['related_objects']}")
            else:
                skipped_count += 1
                if "No KPI references" not in str(result):
                    if skipped_count <= 5:
                        print(f"⚠️  {obj_file.name}: {result}")
        
        except Exception as e:
            error_count += 1
            print(f"❌ {obj_file.name}: {str(e)}")
    
    if updated_count > 25:
        print(f"... and {updated_count - 25} more files updated")
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"✅ Updated: {updated_count}")
    print(f"⏭️  Skipped: {skipped_count}")
    print(f"❌ Errors: {error_count}")
    print(f"📊 Total object files: {len(obj_files)}")
    print()
    print("All object models now have comprehensive metadata from thorough KPI analysis!")
    print("=" * 80)

if __name__ == '__main__':
    main()
