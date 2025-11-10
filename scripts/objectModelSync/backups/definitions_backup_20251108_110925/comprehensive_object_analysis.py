"""
Comprehensive analysis of ALL object models by thoroughly analyzing every KPI.
Finds object references in KPI names, descriptions, formulas, and content.
"""

import re
from pathlib import Path
from collections import defaultdict
import json

def extract_all_kpi_content(kpi_file):
    """Extract all content from KPI file for analysis."""
    with open(kpi_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract all fields
    fields = {}
    
    # Basic fields
    for field in ['code', 'name', 'category', 'description', 'kpi_definition', 
                  'formula', 'calculation_formula', 'measurement_approach',
                  'expected_business_insights', 'trend_analysis']:
        pattern = rf'{field}=["\']([^"\']+)["\']'
        match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
        if match:
            fields[field] = match.group(1)
        else:
            # Try multi-line string
            pattern = rf'{field}="""(.*?)"""'
            match = re.search(pattern, content, re.DOTALL)
            if match:
                fields[field] = match.group(1)
    
    # Extract modules
    modules_match = re.search(r'"modules":\s*\[([^\]]+)\]', content)
    if modules_match:
        modules_str = modules_match.group(1)
        fields['modules'] = [m.strip().strip('"') for m in modules_str.split(',')]
    else:
        fields['modules'] = []
    
    # Extract required_objects if present
    req_obj_match = re.search(r'"required_objects":\s*\[([^\]]+)\]', content)
    if req_obj_match:
        objects_str = req_obj_match.group(1)
        fields['required_objects'] = [obj.strip().strip('"') for obj in objects_str.split(',')]
    else:
        fields['required_objects'] = []
    
    return fields

def load_all_object_models():
    """Load all object model names and codes."""
    obj_dir = Path('object_models')
    obj_files = list(obj_dir.glob('*.py'))
    
    objects = {}
    
    for obj_file in obj_files:
        if obj_file.name in ['__init__.py', 'registry.py']:
            continue
        
        with open(obj_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract name and code
        name_match = re.search(r'name="([^"]+)"', content)
        code_match = re.search(r'code="([^"]+)"', content)
        
        if name_match:
            name = name_match.group(1)
            code = code_match.group(1) if code_match else name.upper().replace(' ', '_')
            
            objects[obj_file.stem] = {
                'name': name,
                'code': code,
                'file': obj_file.name,
                'variations': generate_name_variations(name)
            }
    
    return objects

def generate_name_variations(name):
    """Generate variations of object name for matching."""
    variations = set()
    
    # Original name
    variations.add(name.lower())
    
    # Without spaces
    variations.add(name.lower().replace(' ', ''))
    
    # With underscores
    variations.add(name.lower().replace(' ', '_'))
    
    # Singular/plural variations
    words = name.lower().split()
    
    # Try removing common suffixes
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
        'territory': ['terr'],
        'forecast': ['fcst'],
    }
    
    for full, abbrevs in abbrev_map.items():
        if full in name.lower():
            variations.update(abbrevs)
    
    return variations

def find_object_references_in_kpi(kpi_content, object_models):
    """Find all object model references in KPI content."""
    referenced_objects = set()
    
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
    for obj_key, obj_data in object_models.items():
        # Check if any variation appears in the text
        for variation in obj_data['variations']:
            if len(variation) >= 3:  # Avoid very short matches
                # Use word boundaries to avoid partial matches
                pattern = r'\b' + re.escape(variation) + r'\b'
                if re.search(pattern, search_text):
                    referenced_objects.add(obj_data['name'])
                    break
    
    # Also include objects from required_objects field
    if kpi_content.get('required_objects'):
        referenced_objects.update(kpi_content['required_objects'])
    
    return list(referenced_objects)

def analyze_all_kpis():
    """Analyze all KPIs to find object references."""
    print("=" * 80)
    print("COMPREHENSIVE OBJECT MODEL ANALYSIS")
    print("=" * 80)
    print()
    
    # Load all object models
    print("Step 1: Loading object models...")
    object_models = load_all_object_models()
    print(f"  Found {len(object_models)} object models")
    print()
    
    # Initialize tracking
    object_to_kpis = defaultdict(lambda: {
        'kpis': [],
        'modules': set(),
        'kpi_count': 0
    })
    
    # Analyze all KPIs
    print("Step 2: Analyzing all KPI files...")
    kpi_dir = Path('kpis')
    kpi_files = list(kpi_dir.glob('*.py'))
    
    processed = 0
    for kpi_file in kpi_files:
        if kpi_file.name in ['__init__.py', 'registry.py']:
            continue
        
        try:
            kpi_content = extract_all_kpi_content(kpi_file)
            
            if not kpi_content.get('code'):
                continue
            
            # Find all object references
            referenced_objects = find_object_references_in_kpi(kpi_content, object_models)
            
            # Update tracking for each referenced object
            for obj_name in referenced_objects:
                object_to_kpis[obj_name]['kpis'].append({
                    'code': kpi_content.get('code'),
                    'name': kpi_content.get('name'),
                    'file': kpi_file.name
                })
                object_to_kpis[obj_name]['modules'].update(kpi_content.get('modules', []))
                object_to_kpis[obj_name]['kpi_count'] += 1
            
            processed += 1
            if processed % 50 == 0:
                print(f"  Processed {processed} KPIs...")
        
        except Exception as e:
            print(f"  Error processing {kpi_file.name}: {e}")
    
    print(f"  Completed: {processed} KPIs analyzed")
    print()
    
    # Save results
    print("Step 3: Saving analysis results...")
    results_file = Path('object_model_analysis_results.json')
    
    # Convert sets to lists for JSON serialization
    results = {}
    for obj_name, data in object_to_kpis.items():
        results[obj_name] = {
            'kpi_count': data['kpi_count'],
            'modules': sorted(list(data['modules'])),
            'kpis': data['kpis'][:50]  # Limit to first 50 for file size
        }
    
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"  Results saved to: {results_file}")
    print()
    
    # Print summary
    print("=" * 80)
    print("ANALYSIS SUMMARY")
    print("=" * 80)
    print(f"Total object models: {len(object_models)}")
    print(f"Objects referenced in KPIs: {len(object_to_kpis)}")
    print(f"Objects not referenced: {len(object_models) - len(object_to_kpis)}")
    print()
    
    # Top 20 most referenced objects
    print("Top 20 Most Referenced Objects:")
    sorted_objects = sorted(object_to_kpis.items(), key=lambda x: x[1]['kpi_count'], reverse=True)
    for i, (obj_name, data) in enumerate(sorted_objects[:20], 1):
        print(f"  {i:2d}. {obj_name:40s} - {data['kpi_count']:3d} KPIs, {len(data['modules']):2d} modules")
    
    print()
    
    # Objects with no references
    unreferenced = set(obj_data['name'] for obj_data in object_models.values()) - set(object_to_kpis.keys())
    if unreferenced:
        print(f"Objects with no KPI references ({len(unreferenced)}):")
        for obj in sorted(unreferenced)[:20]:
            print(f"  - {obj}")
        if len(unreferenced) > 20:
            print(f"  ... and {len(unreferenced) - 20} more")
    
    print()
    print("=" * 80)
    
    return object_to_kpis, object_models

if __name__ == '__main__':
    object_to_kpis, object_models = analyze_all_kpis()
