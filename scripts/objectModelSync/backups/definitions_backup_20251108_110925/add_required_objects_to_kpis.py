"""
Add required_objects field to KPI metadata.

This script analyzes KPI definitions and adds a list of object models
required to calculate each KPI to the metadata.
"""

import re
from pathlib import Path

# Common object mappings based on KPI naming patterns and formulas
OBJECT_PATTERNS = {
    # Sales Process Objects
    'lead': ['Lead'],
    'opportunity': ['Opportunity'],
    'deal': ['Deal'],
    'sale': ['Sale'],
    'contract': ['Contract'],
    'proposal': ['Proposal'],
    'demo': ['Demo'],
    'appointment': ['Appointment'],
    'meeting': ['Meeting'],
    'call': ['Call'],
    'email': ['Email'],
    'pipeline': ['Sales Pipeline'],
    
    # Customer Objects
    'customer': ['Customer'],
    'account': ['Account'],
    'client': ['Customer'],
    'user': ['Customer'],
    
    # Product Objects
    'product': ['Product'],
    'service': ['Product'],
    'item': ['Product'],
    
    # People Objects
    'rep': ['Sales Representative'],
    'representative': ['Sales Representative'],
    'sales_rep': ['Sales Representative'],
    'salesperson': ['Sales Representative'],
    'team': ['Sales Team'],
    'manager': ['Sales Representative'],
    
    # Channel Objects
    'partner': ['Channel Partner'],
    'channel': ['Channel Partner'],
    
    # Support Objects
    'ticket': ['Support Ticket'],
    'support': ['Support Ticket'],
    'issue': ['Support Ticket'],
    
    # Training Objects
    'training': ['Training Program'],
    'coaching': ['Coaching Session'],
    'assessment': ['Assessment'],
    'certification': ['Certification'],
    
    # Performance Objects
    'quota': ['Sales Quota'],
    'target': ['Sales Quota'],
    'goal': ['Goal'],
    'forecast': ['Revenue Forecast'],
    'benchmark': ['Benchmark'],
    'scorecard': ['Performance Scorecard'],
    
    # Financial Objects
    'revenue': ['Sale', 'Customer'],
    'cost': ['Sale'],
    'profit': ['Sale'],
    'price': ['Product'],
    'discount': ['Deal', 'Sale'],
    'commission': ['Sale', 'Sales Representative'],
    
    # Time-based
    'cycle': ['Lead', 'Opportunity', 'Deal'],
    'time': ['Lead', 'Opportunity', 'Deal'],
    'duration': ['Lead', 'Opportunity', 'Deal'],
    
    # Conversion/Rate metrics
    'conversion': ['Lead', 'Opportunity'],
    'win_rate': ['Opportunity', 'Deal'],
    'close': ['Opportunity', 'Deal'],
    'churn': ['Customer', 'Subscription'],
    'retention': ['Customer'],
    'renewal': ['Contract', 'Customer'],
    
    # Activity metrics
    'activity': ['Sales Representative'],
    'engagement': ['Customer', 'Lead'],
    'outreach': ['Lead', 'Sales Representative'],
    'follow_up': ['Lead', 'Opportunity'],
    
    # Content/Enablement
    'content': ['Sales Content'],
    'playbook': ['Sales Playbook'],
    'collateral': ['Sales Content'],
    
    # Territory
    'territory': ['Sales Territory'],
    'region': ['Sales Territory'],
}

def infer_required_objects(kpi_name, kpi_code, description, formula):
    """Infer required objects from KPI name, code, description, and formula."""
    objects = set()
    
    # Combine all text to search
    search_text = f"{kpi_name} {kpi_code} {description} {formula}".lower()
    
    # Check each pattern
    for pattern, obj_list in OBJECT_PATTERNS.items():
        if pattern in search_text:
            objects.update(obj_list)
    
    # Remove duplicates and sort
    return sorted(list(objects))

def extract_kpi_info(file_path):
    """Extract KPI information from file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract key fields
    name_match = re.search(r'name="([^"]+)"', content)
    code_match = re.search(r'code="([^"]+)"', content)
    desc_match = re.search(r'description="([^"]+)"', content)
    formula_match = re.search(r'formula="([^"]+)"', content)
    
    name = name_match.group(1) if name_match else ""
    code = code_match.group(1) if code_match else ""
    description = desc_match.group(1) if desc_match else ""
    formula = formula_match.group(1) if formula_match else ""
    
    return name, code, description, formula

def add_required_objects_to_file(file_path):
    """Add required_objects to KPI metadata if not present."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if required_objects already exists
    if '"required_objects"' in content:
        return False, "Already has required_objects"
    
    # Extract KPI info
    name, code, description, formula = extract_kpi_info(file_path)
    
    # Infer required objects
    required_objects = infer_required_objects(name, code, description, formula)
    
    if not required_objects:
        required_objects = ["TBD"]  # Mark for manual review
    
    # Find metadata section and add required_objects
    metadata_pattern = r'(metadata_=\{[^}]*?)([\s\n]*}[\s\n]*\))'
    
    def add_field(match):
        metadata_content = match.group(1)
        closing = match.group(2)
        
        # Remove trailing comma if present
        metadata_content = metadata_content.rstrip()
        if metadata_content.endswith(','):
            metadata_content = metadata_content[:-1]
        
        # Add required_objects before closing brace
        objects_str = ', '.join([f'"{obj}"' for obj in required_objects])
        new_field = f',\n        "required_objects": [{objects_str}]'
        
        return metadata_content + new_field + closing
    
    updated_content = re.sub(metadata_pattern, add_field, content, flags=re.DOTALL)
    
    if updated_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True, required_objects
    
    return False, "No metadata found"

def main():
    kpi_dir = Path('kpis')
    kpi_files = list(kpi_dir.glob('*.py'))
    
    print("=" * 80)
    print("ADDING REQUIRED_OBJECTS TO KPI METADATA")
    print("=" * 80)
    print(f"\nTotal KPI files: {len(kpi_files)}")
    print()
    
    updated_count = 0
    skipped_count = 0
    error_count = 0
    
    for file_path in sorted(kpi_files):
        try:
            success, result = add_required_objects_to_file(file_path)
            
            if success:
                updated_count += 1
                if updated_count <= 10:  # Show first 10
                    print(f"✅ {file_path.name}")
                    print(f"   Objects: {result}")
            else:
                skipped_count += 1
                if "Already has" in str(result):
                    pass  # Don't print already updated files
                else:
                    print(f"⚠️  {file_path.name}: {result}")
        except Exception as e:
            error_count += 1
            print(f"❌ {file_path.name}: {str(e)}")
    
    if updated_count > 10:
        print(f"... and {updated_count - 10} more files updated")
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"✅ Updated: {updated_count}")
    print(f"⏭️  Skipped: {skipped_count}")
    print(f"❌ Errors: {error_count}")
    print(f"📊 Total: {len(kpi_files)}")
    
    print("\n⚠️  NOTE: Some objects may be marked as 'TBD' and need manual review.")
    print("Review the inferred objects and update as needed.")

if __name__ == '__main__':
    main()
