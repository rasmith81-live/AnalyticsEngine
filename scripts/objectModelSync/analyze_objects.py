"""
Analyze all KPIs to find object references.
Comprehensive text analysis to identify all object model dependencies.

UPDATED: Now works with dictionary-based definitions (post-conversion).
"""

import re
import json
from pathlib import Path
from collections import defaultdict
from definition_loader import load_all_kpis, load_all_object_models

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
        'territory': ['terr'],
        'forecast': ['fcst'],
    }
    
    for full, abbrevs in abbrev_map.items():
        if full in name.lower():
            variations.update(abbrevs)
    
    return variations

def load_all_object_models_with_variations(config):
    """Load all object model names and codes with name variations."""
    obj_dir = Path(config['paths']['objects_dir'])
    
    # Use the new loader
    objects_dict = load_all_object_models(obj_dir)
    
    # Add name variations
    objects = {}
    for code, obj_def in objects_dict.items():
        name = obj_def.get('name', code)
        objects[code] = {
            'name': name,
            'code': code,
            'file': obj_def.get('_file', ''),
            'variations': generate_name_variations(name)
        }
    
    return objects

def extract_kpi_content(kpi_file):
    """Extract all content from KPI file for analysis."""
    from definition_loader import load_definition_file
    
    # Load using the new dictionary loader
    definition = load_definition_file(Path(kpi_file))
    
    if not definition:
        return {}
    
    # The definition is already a dictionary with all fields
    fields = definition.copy()
    
    # Ensure modules field exists
    if 'modules' not in fields and 'module_code' in fields:
        fields['modules'] = []
    
    return fields

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
        for variation in obj_data['variations']:
            if len(variation) >= 3:
                pattern = r'\b' + re.escape(variation) + r'\b'
                if re.search(pattern, search_text):
                    referenced_objects.add(obj_data['name'])
                    break
    
    return list(referenced_objects)

def analyze_all_objects(config):
    """Analyze all KPIs to find object references."""
    print("Analyzing all objects...")
    
    # Load all object models
    object_models = load_all_object_models_with_variations(config)
    print(f"  Found {len(object_models)} object models")
    
    # Initialize tracking
    object_to_kpis = defaultdict(lambda: {
        'kpis': [],
        'modules': set(),
        'kpi_count': 0
    })
    
    # Analyze all KPIs
    kpi_dir = Path(config['paths']['kpis_dir'])
    kpi_files = list(kpi_dir.glob('*.py'))
    
    processed = 0
    for kpi_file in kpi_files:
        if kpi_file.name in ['__init__.py', 'registry.py']:
            continue
        
        try:
            kpi_content = extract_kpi_content(kpi_file)
            
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
        
        except Exception as e:
            print(f"  Error processing {kpi_file.name}: {e}")
    
    print(f"  Processed {processed} KPIs")
    print(f"  Found {len(object_to_kpis)} objects referenced in KPIs")
    
    # Convert sets to lists for JSON serialization
    results = {}
    for obj_name, data in object_to_kpis.items():
        results[obj_name] = {
            'kpi_count': data['kpi_count'],
            'modules': sorted(list(data['modules'])),
            'kpis': data['kpis'][:config['sync_options']['max_related_kpis']]
        }
    
    # Save results
    output_dir = Path(config['paths']['output_dir'])
    output_dir.mkdir(parents=True, exist_ok=True)
    
    results_file = output_dir / 'analysis_results.json'
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"  Results saved to: {results_file}")
    
    return results

if __name__ == '__main__':
    import json
    with open('config.json', 'r') as f:
        config = json.load(f)
    analyze_all_objects(config)
