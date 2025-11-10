"""
Validate and update required_objects for every KPI based on comprehensive object analysis.
Ensures every KPI has proper references to the object models needed for calculation.
"""

import re
import json
from pathlib import Path
from collections import defaultdict

def load_object_analysis():
    """Load the comprehensive object analysis results."""
    results_file = Path('object_model_analysis_results.json')
    
    if not results_file.exists():
        print("Error: Run comprehensive_object_analysis.py first!")
        return None
    
    with open(results_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_all_object_models():
    """Load all object model names."""
    obj_dir = Path('object_models')
    obj_files = list(obj_dir.glob('*.py'))
    
    objects = {}
    
    for obj_file in obj_files:
        if obj_file.name in ['__init__.py', 'registry.py']:
            continue
        
        with open(obj_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        name_match = re.search(r'name="([^"]+)"', content)
        if name_match:
            name = name_match.group(1)
            objects[name] = {
                'file': obj_file.name,
                'variations': generate_name_variations(name)
            }
    
    return objects

def generate_name_variations(name):
    """Generate variations of object name for matching."""
    variations = set()
    variations.add(name.lower())
    variations.add(name.lower().replace(' ', ''))
    variations.add(name.lower().replace(' ', '_'))
    
    words = name.lower().split()
    for word in words:
        variations.add(word)
        if word.endswith('s'):
            variations.add(word[:-1])
        if word.endswith('es'):
            variations.add(word[:-2])
        if word.endswith('ies'):
            variations.add(word[:-3] + 'y')
    
    # Common abbreviations
    abbrev_map = {
        'representative': ['rep', 'reps'],
        'opportunity': ['opp', 'opps'],
        'customer': ['cust', 'client'],
        'account': ['acct'],
    }
    
    for full, abbrevs in abbrev_map.items():
        if full in name.lower():
            variations.update(abbrevs)
    
    return variations

def extract_kpi_content(kpi_file):
    """Extract KPI content for analysis."""
    with open(kpi_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fields = {}
    
    # Extract basic fields
    for field in ['code', 'name', 'description', 'kpi_definition', 'formula', 
                  'calculation_formula', 'measurement_approach', 'category']:
        pattern = rf'{field}=["\']([^"\']+)["\']'
        match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
        if match:
            fields[field] = match.group(1)
        else:
            pattern = rf'{field}="""(.*?)"""'
            match = re.search(pattern, content, re.DOTALL)
            if match:
                fields[field] = match.group(1)
    
    # Extract current required_objects
    req_obj_match = re.search(r'"required_objects":\s*\[([^\]]+)\]', content)
    if req_obj_match:
        objects_str = req_obj_match.group(1)
        fields['current_required_objects'] = [obj.strip().strip('"') for obj in objects_str.split(',')]
    else:
        fields['current_required_objects'] = []
    
    return fields, content

def find_required_objects(kpi_content, object_models):
    """Find all object models required for this KPI."""
    required_objects = set()
    
    # Combine all text content
    search_text = ' '.join([
        str(kpi_content.get('name', '')),
        str(kpi_content.get('description', '')),
        str(kpi_content.get('kpi_definition', '')),
        str(kpi_content.get('formula', '')),
        str(kpi_content.get('calculation_formula', '')),
        str(kpi_content.get('measurement_approach', '')),
        str(kpi_content.get('category', ''))
    ]).lower()
    
    # Check each object model
    for obj_name, obj_data in object_models.items():
        for variation in obj_data['variations']:
            if len(variation) >= 3:
                pattern = r'\b' + re.escape(variation) + r'\b'
                if re.search(pattern, search_text):
                    required_objects.add(obj_name)
                    break
    
    return sorted(list(required_objects))

def update_kpi_required_objects(kpi_file, required_objects):
    """Update or add required_objects to KPI metadata."""
    kpi_content, content = extract_kpi_content(kpi_file)
    
    if not required_objects:
        required_objects = ["TBD"]  # Mark for manual review
    
    # Check if required_objects already exists
    has_required_objects = '"required_objects"' in content
    
    if has_required_objects:
        # Update existing required_objects
        current_objects = kpi_content.get('current_required_objects', [])
        
        # Merge with new objects (keep unique)
        merged_objects = sorted(list(set(current_objects + required_objects)))
        
        # Replace in content
        pattern = r'"required_objects":\s*\[[^\]]*\]'
        objects_str = ', '.join([f'"{obj}"' for obj in merged_objects])
        updated_content = re.sub(pattern, f'"required_objects": [{objects_str}]', content)
        
        if updated_content != content:
            with open(kpi_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True, len(merged_objects)
        
        return False, "Already up to date"
    else:
        # Add required_objects to metadata
        metadata_pattern = r'(metadata_=\{[^}]*?)(}[\s\n]*\))'
        
        def add_field(match):
            metadata_content = match.group(1)
            closing = match.group(2)
            
            metadata_content = metadata_content.rstrip()
            if metadata_content.endswith(','):
                metadata_content = metadata_content[:-1]
            
            objects_str = ', '.join([f'"{obj}"' for obj in required_objects])
            new_field = f',\n        "required_objects": [{objects_str}]'
            
            return metadata_content + new_field + closing
        
        updated_content = re.sub(metadata_pattern, add_field, content, flags=re.DOTALL)
        
        if updated_content != content:
            with open(kpi_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True, len(required_objects)
        
        return False, "No metadata found"

def main():
    print("=" * 80)
    print("VALIDATING AND UPDATING KPI REQUIRED_OBJECTS")
    print("=" * 80)
    print()
    
    # Load object models
    print("Step 1: Loading object models...")
    object_models = load_all_object_models()
    print(f"  Found {len(object_models)} object models")
    print()
    
    # Load object analysis
    print("Step 2: Loading object analysis results...")
    object_analysis = load_object_analysis()
    if not object_analysis:
        return
    print(f"  Loaded analysis for {len(object_analysis)} objects")
    print()
    
    # Process all KPIs
    print("Step 3: Validating and updating all KPI files...")
    kpi_dir = Path('kpis')
    kpi_files = list(kpi_dir.glob('*.py'))
    
    updated_count = 0
    already_good_count = 0
    added_count = 0
    error_count = 0
    
    stats = {
        'total_kpis': 0,
        'with_required_objects': 0,
        'without_required_objects': 0,
        'objects_added': 0,
        'objects_updated': 0
    }
    
    for kpi_file in sorted(kpi_files):
        if kpi_file.name in ['__init__.py', 'registry.py']:
            continue
        
        try:
            stats['total_kpis'] += 1
            
            # Extract current content
            kpi_content, content = extract_kpi_content(kpi_file)
            
            if not kpi_content.get('code'):
                continue
            
            # Find required objects
            required_objects = find_required_objects(kpi_content, object_models)
            
            # Update KPI
            success, result = update_kpi_required_objects(kpi_file, required_objects)
            
            if success:
                if '"required_objects"' in content:
                    updated_count += 1
                    stats['objects_updated'] += 1
                    if updated_count <= 20:
                        print(f"✅ Updated: {kpi_file.name} ({result} objects)")
                else:
                    added_count += 1
                    stats['objects_added'] += 1
                    if added_count <= 10:
                        print(f"➕ Added: {kpi_file.name} ({result} objects)")
            else:
                already_good_count += 1
                if "Already up to date" in str(result):
                    stats['with_required_objects'] += 1
        
        except Exception as e:
            error_count += 1
            print(f"❌ Error in {kpi_file.name}: {str(e)}")
    
    if updated_count > 20:
        print(f"... and {updated_count - 20} more KPIs updated")
    if added_count > 10:
        print(f"... and {added_count - 10} more KPIs had required_objects added")
    
    print("\n" + "=" * 80)
    print("VALIDATION SUMMARY")
    print("=" * 80)
    print(f"Total KPIs processed: {stats['total_kpis']}")
    print(f"✅ Already had required_objects: {already_good_count}")
    print(f"🔄 Updated required_objects: {updated_count}")
    print(f"➕ Added required_objects: {added_count}")
    print(f"❌ Errors: {error_count}")
    print()
    print(f"📊 Final Status:")
    print(f"   - KPIs with required_objects: {already_good_count + updated_count + added_count}")
    print(f"   - Coverage: {((already_good_count + updated_count + added_count) / stats['total_kpis'] * 100):.1f}%")
    print("=" * 80)

if __name__ == '__main__':
    main()
