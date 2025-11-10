"""
Add proper UML relationships for all related objects in object models.

UPDATED: Now works with dictionary-based definitions.
"""

import re
from pathlib import Path
from definition_loader import load_definition_file, update_definition_field, add_definition_field

def extract_object_info(obj_file):
    """Extract object name and related objects from file."""
    obj_data = load_definition_file(Path(obj_file))
    
    if not obj_data:
        return None, None, [], {}
    
    name = obj_data.get('name')
    code = obj_data.get('code')
    related_objects = obj_data.get('related_objects', [])
    
    return name, code, related_objects, obj_data

def normalize_object_name(name):
    """Convert object name to class name format."""
    return ''.join(word.capitalize() for word in name.split())

def infer_relationship_type(from_obj, to_obj):
    """Infer the type of relationship between two objects."""
    from_lower = from_obj.lower()
    to_lower = to_obj.lower()
    
    # Composition relationships (strong ownership)
    composition_patterns = [
        ('account', 'contact'),
        ('customer', 'subscription'),
        ('deal', 'proposal'),
        ('opportunity', 'quote'),
    ]
    
    for pattern in composition_patterns:
        if pattern[0] in from_lower and pattern[1] in to_lower:
            return '*--', 'has'
    
    # Aggregation relationships (weak ownership)
    aggregation_patterns = [
        ('account', 'deal'),
        ('customer', 'sale'),
        ('lead', 'opportunity'),
        ('opportunity', 'deal'),
        ('sales representative', 'sale'),
        ('sales team', 'sales representative'),
    ]
    
    for pattern in aggregation_patterns:
        if pattern[0] in from_lower and pattern[1] in to_lower:
            return 'o--', 'manages'
    
    # Association relationships (general connection)
    return '--', 'relates to'

def create_relationship_line(from_obj, to_obj, from_class, to_class):
    """Create a UML relationship line."""
    rel_type, verb = infer_relationship_type(from_obj, to_obj)
    
    # Determine cardinality
    cardinality = '"1" -- "*"'  # Default: one-to-many
    
    # Special cases
    if 'representative' in from_obj.lower() and 'team' in to_obj.lower():
        cardinality = '"*" -- "1"'  # Many reps to one team
    elif 'team' in from_obj.lower() and 'representative' in to_obj.lower():
        cardinality = '"1" -- "*"'  # One team to many reps
    
    return f'{from_class} {cardinality} {to_class} : {verb}'

def update_uml_with_relationships(obj_file):
    """Add proper UML relationships to object model."""
    name, code, related_objects, content = extract_object_info(obj_file)
    
    if not name or not related_objects:
        return False, "No name or related objects"
    
    # Extract current schema
    schema_pattern = r'schema_definition="""(.*?)"""'
    schema_match = re.search(schema_pattern, content, re.DOTALL)
    
    if not schema_match:
        return False, "No schema_definition found"
    
    current_schema = schema_match.group(1)
    
    # Check if relationships section already exists
    if "' Relationships to Related Objects" in current_schema:
        return False, "Relationships already added"
    
    # Normalize the main object name
    main_class = normalize_object_name(name)
    
    # Create relationships for each related object
    relationships = []
    relationships.append("\n' Relationships to Related Objects")
    
    for related_obj in related_objects:
        related_class = normalize_object_name(related_obj)
        rel_line = create_relationship_line(name, related_obj, main_class, related_class)
        relationships.append(rel_line)
    
    # Add relationships before the closing of schema
    updated_schema = current_schema.rstrip() + "\n" + "\n".join(relationships) + "\n"
    
    # Update content
    updated_content = content.replace(
        f'schema_definition="""{current_schema}"""',
        f'schema_definition="""{updated_schema}"""'
    )
    
    if updated_content != content:
        with open(obj_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True, len(related_objects)
    
    return False, "No changes made"

def sync_uml_relationships(config, analysis_results=None):
    """Sync UML relationships - callable from orchestrator."""
    return main_internal(config, analysis_results)

def main_internal(config=None, analysis_results=None):
    print("=" * 80)
    print("ADDING UML RELATIONSHIPS TO OBJECT MODELS")
    print("=" * 80)
    print()
    
    obj_dir = Path('object_models')
    obj_files = list(obj_dir.glob('*.py'))
    
    updated_count = 0
    skipped_count = 0
    error_count = 0
    
    for obj_file in sorted(obj_files):
        if obj_file.name in ['__init__.py', 'registry.py']:
            continue
        
        try:
            success, result = update_uml_with_relationships(obj_file)
            
            if success:
                updated_count += 1
                if updated_count <= 20:
                    print(f"✅ {obj_file.name}")
                    print(f"   Added {result} relationship lines")
            else:
                skipped_count += 1
                if "No name" in str(result) or "No schema" in str(result):
                    if skipped_count <= 5:
                        print(f"⚠️  {obj_file.name}: {result}")
        
        except Exception as e:
            error_count += 1
            print(f"❌ {obj_file.name}: {str(e)}")
    
    if updated_count > 20:
        print(f"... and {updated_count - 20} more files updated")
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"✅ Updated: {updated_count}")
    print(f"⏭️  Skipped: {skipped_count}")
    print(f"❌ Errors: {error_count}")
    print(f"📊 Total: {len(obj_files)}")
    print("\n💡 Relationships added using UML notation:")
    print("   -- : Association (general relationship)")
    print("   o-- : Aggregation (weak ownership)")
    print("   *-- : Composition (strong ownership)")
    print("=" * 80)

def main():
    """Main entry point when run directly."""
    main_internal()

if __name__ == '__main__':
    main()
