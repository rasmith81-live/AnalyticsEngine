"""
Update Shared Object Models with New Module Relationships

This script updates shared object models to include relationships from a new module.
Should be run after generating KPIs for a new module.
"""

import os
import re

# Directory containing object model files
object_models_dir = r"C:\Users\Arthu\CascadeProjects\AnalyticsEngine\services\business_services\analytics_models\definitions\object_models"

def update_object_model_with_module(filepath, module_code):
    """Update an object model file to add a new module reference."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if module already exists
    if f'"{module_code}"' in content:
        return False, "Already has module"
    
    # Update modules list in metadata
    pattern = r'("modules":\s*\[)([^\]]*?)(\])'
    
    def add_module(match):
        prefix = match.group(1)
        existing_modules = match.group(2)
        suffix = match.group(3)
        
        if existing_modules.strip():
            return f'{prefix}{existing_modules}, "{module_code}"{suffix}'
        else:
            return f'{prefix}"{module_code}"{suffix}'
    
    updated_content = re.sub(pattern, add_module, content)
    
    if updated_content == content:
        return False, "No metadata found"
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    return True, "Updated"

def add_uml_relationships(filepath, new_relationships):
    """
    Add new UML relationships to an object model.
    
    Args:
        filepath: Path to the object model file
        new_relationships: String containing new UML relationship definitions
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the end of the UML diagram (before @enduml)
    pattern = r'(@enduml)'
    
    def add_relationships(match):
        return f'\n{new_relationships}\n\n{match.group(1)}'
    
    updated_content = re.sub(pattern, add_relationships, content)
    
    if updated_content == content:
        return False, "Could not find UML diagram"
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    return True, "Added relationships"

def update_shared_models_for_module(module_code, shared_models_map):
    """
    Update shared object models when adding a new module.
    
    Args:
        module_code: Code of the new module (e.g., "KEY_ACCOUNT_MANAGEMENT")
        shared_models_map: Dict mapping object model codes to their relationship additions
                          Example: {
                              "CUSTOMER": "' Relationships - New Module\nNewEntity -- Customer",
                              "PRODUCT": "' Relationships - New Module\nProduct -- NewEntity"
                          }
    """
    print(f"\nUpdating shared object models for module: {module_code}\n")
    
    updated_count = 0
    skipped_count = 0
    
    for model_code, relationships in shared_models_map.items():
        filename = model_code.lower() + ".py"
        filepath = os.path.join(object_models_dir, filename)
        
        if not os.path.exists(filepath):
            print(f"  SKIP: {filename} - File not found")
            skipped_count += 1
            continue
        
        # Update module reference
        success, msg = update_object_model_with_module(filepath, module_code)
        
        if success:
            print(f"  UPDATED: {filename} - Added module reference")
            
            # Add UML relationships if provided
            if relationships:
                success_uml, msg_uml = add_uml_relationships(filepath, relationships)
                if success_uml:
                    print(f"           {filename} - Added UML relationships")
                else:
                    print(f"           {filename} - Could not add UML: {msg_uml}")
            
            updated_count += 1
        else:
            print(f"  SKIP: {filename} - {msg}")
            skipped_count += 1
    
    print(f"\n{'=' * 60}")
    print(f"Summary:")
    print(f"  Models updated: {updated_count}")
    print(f"  Models skipped: {skipped_count}")
    print(f"{'=' * 60}\n")

# Example usage for a new module
if __name__ == "__main__":
    # Example: Adding a new module called "NEW_MODULE"
    # Define which shared models it uses and what relationships to add
    
    example_shared_models = {
        "CUSTOMER": """' Relationships - New Module Example
NewEntity "1" -- "0..*" Customer : interacts with >""",
        
        "PRODUCT": """' Relationships - New Module Example
Product "0..*" -- "0..*" NewEntity : used in >"""
    }
    
    # Uncomment to run:
    # update_shared_models_for_module("NEW_MODULE", example_shared_models)
    
    print("This is a utility script. Import and call update_shared_models_for_module() with your module details.")
