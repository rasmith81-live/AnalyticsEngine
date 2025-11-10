"""
Update object model UML schema_definition to include all related objects.
"""

import re
from pathlib import Path

def extract_related_objects(obj_file):
    """Extract related_objects from metadata."""
    with open(obj_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract related_objects
    related_match = re.search(r'"related_objects":\s*\[([^\]]+)\]', content)
    
    if not related_match:
        return None, content
    
    objects_str = related_match.group(1)
    related_objects = [obj.strip().strip('"') for obj in objects_str.split(',')]
    
    return related_objects, content

def normalize_object_name(name):
    """Convert object name to class name format."""
    # Remove spaces and convert to PascalCase
    return ''.join(word.capitalize() for word in name.split())

def update_uml_schema(obj_file):
    """Update UML schema to include all related objects."""
    related_objects, content = extract_related_objects(obj_file)
    
    if not related_objects:
        return False, "No related_objects found"
    
    # Extract current schema_definition
    schema_pattern = r'schema_definition="""(.*?)"""'
    schema_match = re.search(schema_pattern, content, re.DOTALL)
    
    if not schema_match:
        return False, "No schema_definition found"
    
    current_schema = schema_match.group(1)
    
    # Check which related objects are already in the schema
    missing_objects = []
    for obj in related_objects:
        class_name = normalize_object_name(obj)
        if f'class {class_name}' not in current_schema:
            missing_objects.append(class_name)
    
    if not missing_objects:
        return False, "All related objects already in schema"
    
    # Find the end of the schema (before the closing """)
    # Add missing objects as class declarations
    new_classes = []
    for obj_name in missing_objects:
        new_classes.append(f"class {obj_name} {{\n}}")
    
    # Insert new classes before the last relationship section or at the end
    updated_schema = current_schema.rstrip()
    
    # Add a section for related objects if not present
    if "' Related Objects" not in updated_schema:
        updated_schema += "\n\n' Related Objects\n"
    
    updated_schema += "\n" + "\n\n".join(new_classes) + "\n"
    
    # Update the content
    updated_content = content.replace(
        f'schema_definition="""{current_schema}"""',
        f'schema_definition="""{updated_schema}"""'
    )
    
    if updated_content != content:
        with open(obj_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True, len(missing_objects)
    
    return False, "No changes made"

def main():
    print("=" * 80)
    print("UPDATING OBJECT MODEL UML SCHEMAS")
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
            success, result = update_uml_schema(obj_file)
            
            if success:
                updated_count += 1
                if updated_count <= 20:
                    print(f"✅ {obj_file.name}")
                    print(f"   Added {result} related object classes to UML")
            else:
                skipped_count += 1
                if "No related_objects" in str(result):
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
    print("=" * 80)

if __name__ == '__main__':
    main()
