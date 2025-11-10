"""
Simple schema extractor that reads table_schema directly from Python files.
Extracts the table_schema dictionary using AST parsing.
"""

import ast
import json
from pathlib import Path

def extract_table_schema_from_file(file_path: Path) -> dict:
    """
    Extract table_schema dictionary from a Python file using AST parsing.
    
    Args:
        file_path: Path to the object model Python file
        
    Returns:
        Dictionary containing the table schema
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse the Python file
    tree = ast.parse(content)
    
    # Find the assignment that contains table_schema
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            # Look for keyword arguments
            for keyword in node.keywords:
                if keyword.arg == 'table_schema':
                    # Convert the AST node to a dictionary
                    schema = ast.literal_eval(keyword.value)
                    return schema
    
    raise ValueError(f"No table_schema found in {file_path}")

def main():
    """Extract SCOR schemas."""
    
    print("=" * 80)
    print("EXTRACTING SCOR TABLE SCHEMAS")
    print("=" * 80)
    print()
    
    # Define paths
    project_root = Path(__file__).parent.parent.parent
    object_models_dir = project_root / 'services' / 'business_services' / 'analytics_models' / 'definitions' / 'object_models'
    schemas_dir = project_root / 'schemas' / 'scor'
    
    # Create schemas directory
    schemas_dir.mkdir(parents=True, exist_ok=True)
    print(f"[INFO] Schemas will be saved to: {schemas_dir}")
    print()
    
    # Define SCOR files
    scor_files = {
        'scor_process': 'scor_process.py',
        'scor_metric': 'scor_metric.py',
        'scor_practice': 'scor_practice.py',
        'scor_skill': 'scor_skill.py',
        'scor_metric_observation': 'scor_metric_observation.py'
    }
    
    success_count = 0
    error_count = 0
    
    for schema_name, file_name in scor_files.items():
        file_path = object_models_dir / file_name
        
        if not file_path.exists():
            print(f"[ERROR] File not found: {file_path}")
            error_count += 1
            continue
        
        try:
            print(f"[INFO] Processing {file_name}...")
            
            # Extract schema
            schema = extract_table_schema_from_file(file_path)
            
            # Save to JSON
            output_path = schemas_dir / f"{schema_name}.json"
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(schema, f, indent=2, ensure_ascii=False)
            
            print(f"[SUCCESS] Saved to {output_path.name}")
            print(f"  - Table: {schema['table_name']}")
            print(f"  - Columns: {len(schema['columns'])}")
            print()
            
            success_count += 1
            
        except Exception as e:
            print(f"[ERROR] Failed to process {file_name}: {e}")
            error_count += 1
            print()
    
    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Success: {success_count}")
    print(f"Errors:  {error_count}")
    print(f"Total:   {len(scor_files)}")
    print()
    
    if success_count > 0:
        print(f"[INFO] Schemas saved to: {schemas_dir}")
        print()
        print("Next steps:")
        print("1. Review the generated JSON files in schemas/scor/")
        print("2. Run CQRS scripts to create tables (see commands below)")
        print()
        print("=" * 80)
    
    return success_count == len(scor_files)

if __name__ == '__main__':
    import sys
    success = main()
    sys.exit(0 if success else 1)
