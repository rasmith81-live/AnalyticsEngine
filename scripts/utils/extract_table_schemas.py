"""
Extract table_schema from object models and generate JSON files for CQRS scripts.

This script reads object model definitions, extracts their table_schema,
and writes them to JSON files that can be consumed by add_cqrs_schema.ps1.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

def extract_schema_from_object_model(object_model) -> Dict[str, Any]:
    """
    Extract table_schema from an ObjectModel instance.
    
    Args:
        object_model: ObjectModel instance with table_schema attribute
        
    Returns:
        Dictionary containing the table schema
    """
    if not hasattr(object_model, 'table_schema'):
        raise ValueError(f"Object model {object_model.name} does not have table_schema")
    
    schema = object_model.table_schema
    
    # Validate required fields
    required_fields = ['table_name', 'class_name', 'columns']
    for field in required_fields:
        if field not in schema:
            raise ValueError(f"Schema for {object_model.name} missing required field: {field}")
    
    return schema

def save_schema_to_json(schema: Dict[str, Any], output_path: Path) -> None:
    """
    Save schema to JSON file.
    
    Args:
        schema: Schema dictionary
        output_path: Path to output JSON file
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(schema, f, indent=2, ensure_ascii=False)
    
    print(f"[SUCCESS] Saved schema to {output_path}")

def load_object_model_from_file(file_path: Path):
    """
    Load an ObjectModel instance from a Python file by executing it.
    
    Args:
        file_path: Path to the object model Python file
        
    Returns:
        The ObjectModel instance
    """
    import importlib.util
    
    spec = importlib.util.spec_from_file_location("temp_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Find the ObjectModel instance (usually uppercase constant)
    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        if hasattr(attr, 'table_schema') and hasattr(attr, 'name'):
            return attr
    
    raise ValueError(f"No ObjectModel found in {file_path}")

def extract_scor_schemas():
    """Extract schemas for all SCOR object models."""
    
    print("=" * 80)
    print("EXTRACTING SCOR TABLE SCHEMAS")
    print("=" * 80)
    print()
    
    # Define SCOR object model files
    object_models_dir = project_root / 'services' / 'business_services' / 'analytics_models' / 'definitions' / 'object_models'
    
    scor_files = [
        ('scor_process', object_models_dir / 'scor_process.py'),
        ('scor_metric', object_models_dir / 'scor_metric.py'),
        ('scor_practice', object_models_dir / 'scor_practice.py'),
        ('scor_skill', object_models_dir / 'scor_skill.py')
    ]
    
    print("[INFO] Loading SCOR object models from files...")
    scor_models = []
    
    for file_name, file_path in scor_files:
        if not file_path.exists():
            print(f"[ERROR] File not found: {file_path}")
            sys.exit(1)
        
        try:
            object_model = load_object_model_from_file(file_path)
            scor_models.append((file_name, object_model))
            print(f"  - Loaded {object_model.name}")
        except Exception as e:
            print(f"[ERROR] Failed to load {file_name}: {e}")
            sys.exit(1)
    
    print()
    
    # Create schemas directory
    schemas_dir = project_root / 'schemas' / 'scor'
    schemas_dir.mkdir(parents=True, exist_ok=True)
    print(f"[INFO] Schemas will be saved to: {schemas_dir}")
    print()
    
    # Extract and save each schema
    success_count = 0
    error_count = 0
    
    for file_name, object_model in scor_models:
        try:
            print(f"[INFO] Processing {object_model.name} ({object_model.code})...")
            
            # Extract schema
            schema = extract_schema_from_object_model(object_model)
            
            # Add metadata
            schema['_metadata'] = {
                'object_model_name': object_model.name,
                'object_model_code': object_model.code,
                'description': object_model.description,
                'module': 'ASCM_SCOR'
            }
            
            # Save to JSON
            output_path = schemas_dir / f"{file_name}.json"
            save_schema_to_json(schema, output_path)
            
            # Print summary
            column_count = len(schema['columns'])
            print(f"  - Table: {schema['table_name']}")
            print(f"  - Columns: {column_count}")
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
    print(f"Total:   {len(scor_models)}")
    print()
    
    if success_count > 0:
        print(f"[INFO] Schemas saved to: {schemas_dir}")
        print()
        print("Next steps:")
        print("1. Review the generated JSON files")
        print("2. Run CQRS scripts to create tables:")
        print()
        for file_name, _ in scor_models:
            table_name = file_name.replace('_', '')  # scor_process -> scorprocess
            print(f"   .\\scripts\\utils\\add_cqrs_schema.ps1 -ServiceName analytics_service \\")
            print(f"       -TableName {table_name}s \\")
            print(f"       -Domain scor \\")
            print(f"       -SchemaDefinition .\\schemas\\scor\\{file_name}.json")
            print()
    
    print("=" * 80)
    
    return success_count == len(scor_models)

def extract_all_schemas():
    """Extract schemas for ALL object models (optional - for future use)."""
    
    print("=" * 80)
    print("EXTRACTING ALL OBJECT MODEL SCHEMAS")
    print("=" * 80)
    print()
    
    # This would iterate through all object models
    # For now, we'll just do SCOR
    print("[INFO] Full extraction not implemented yet")
    print("[INFO] Use extract_scor_schemas() for SCOR models")
    print()

def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Extract table_schema from object models to JSON files'
    )
    parser.add_argument(
        '--scor',
        action='store_true',
        help='Extract SCOR object model schemas'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Extract all object model schemas (not implemented)'
    )
    
    args = parser.parse_args()
    
    if args.scor:
        success = extract_scor_schemas()
        sys.exit(0 if success else 1)
    elif args.all:
        extract_all_schemas()
        sys.exit(1)  # Not implemented
    else:
        print("Usage: python extract_table_schemas.py --scor")
        print("       python extract_table_schemas.py --all")
        sys.exit(1)

if __name__ == '__main__':
    main()
