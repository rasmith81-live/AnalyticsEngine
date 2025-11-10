"""
Sync KPI required_objects metadata.
Ensures every KPI has complete list of required object models.

UPDATED: Now works with dictionary-based definitions.
"""

import re
import json
from pathlib import Path
from definition_loader import load_definition_file, update_definition_field, add_definition_field

def load_analysis_results(config):
    """Load the analysis results."""
    results_file = Path(config['paths']['output_dir']) / 'analysis_results.json'
    
    if not results_file.exists():
        raise FileNotFoundError("Analysis results not found. Run analyze_objects.py first.")
    
    with open(results_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_object_models(config):
    """Load all object model names."""
    from analyze_objects import load_all_object_models_with_variations
    return load_all_object_models_with_variations(config)

def extract_kpi_content(kpi_file):
    """Extract KPI content."""
    kpi_data = load_definition_file(Path(kpi_file))
    
    if not kpi_data:
        return {}, ''
    
    # Get current required_objects
    kpi_data['current_required_objects'] = kpi_data.get('required_objects', [])
    
    return kpi_data, ''

def find_required_objects(kpi_content, object_models):
    """Find all object models required for this KPI."""
    from analyze_objects import find_object_references_in_kpi
    return find_object_references_in_kpi(kpi_content, object_models)

def update_kpi_required_objects(kpi_file, required_objects, config):
    """Update or add required_objects to KPI metadata."""
    kpi_content, _ = extract_kpi_content(kpi_file)
    
    if not kpi_content:
        return False, "Could not load KPI"
    
    if not required_objects:
        required_objects = ["TBD"]
    
    # Merge with existing
    current_objects = kpi_content.get('required_objects', [])
    merged_objects = sorted(list(set(current_objects + required_objects)))
    
    # Check if update needed
    if set(current_objects) == set(merged_objects):
        return False, "Already up to date"
    
    # Update the field
    if not config['sync_options']['dry_run']:
        if 'required_objects' in kpi_content:
            success = update_definition_field(Path(kpi_file), 'required_objects', merged_objects)
        else:
            success = add_definition_field(Path(kpi_file), 'required_objects', merged_objects)
        
        if success:
            return True, len(merged_objects)
        else:
            return False, "Update failed"
    
    return True, len(merged_objects)

def sync_kpi_objects(config, analysis_results=None):
    """Sync all KPI required_objects."""
    print("Syncing KPI required objects...")
    
    if analysis_results is None:
        analysis_results = load_analysis_results(config)
    
    object_models = load_object_models(config)
    
    kpi_dir = Path(config['paths']['kpis_dir'])
    kpi_files = list(kpi_dir.glob('*.py'))
    
    updated_count = 0
    already_good_count = 0
    error_count = 0
    
    for kpi_file in kpi_files:
        if kpi_file.name in ['__init__.py', 'registry.py']:
            continue
        
        try:
            kpi_content, _ = extract_kpi_content(kpi_file)
            
            if not kpi_content.get('code'):
                continue
            
            required_objects = find_required_objects(kpi_content, object_models)
            success, result = update_kpi_required_objects(kpi_file, required_objects, config)
            
            if success:
                updated_count += 1
            else:
                already_good_count += 1
        
        except Exception as e:
            error_count += 1
            print(f"  Error in {kpi_file.name}: {e}")
    
    print(f"  Updated: {updated_count}")
    print(f"  Already good: {already_good_count}")
    print(f"  Errors: {error_count}")
    
    return {
        'updated': updated_count,
        'already_good': already_good_count,
        'errors': error_count,
        'total': len(kpi_files) - 2
    }

if __name__ == '__main__':
    import json
    with open('config.json', 'r') as f:
        config = json.load(f)
    sync_kpi_objects(config)
