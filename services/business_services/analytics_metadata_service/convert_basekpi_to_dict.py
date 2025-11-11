"""
Convert all BaseKPI class-based definitions to dictionary format
"""
import ast
import re
from pathlib import Path

def convert_basekpi_file(file_path: Path) -> bool:
    """Convert a single BaseKPI file to dictionary format"""
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Check if it's already dictionary format
        if 'class ' not in content or 'BaseKPI' not in content:
            return False
            
        # Parse the file
        tree = ast.parse(content)
        
        # Find the class definition
        class_def = None
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and any(
                base.id == 'BaseKPI' if isinstance(base, ast.Name) else False
                for base in node.bases
            ):
                class_def = node
                break
        
        if not class_def:
            return False
        
        # Find the __init__ method
        init_method = None
        for item in class_def.body:
            if isinstance(item, ast.FunctionDef) and item.name == '__init__':
                init_method = item
                break
        
        if not init_method:
            return False
        
        # Find the super().__init__() call
        super_call = None
        for stmt in init_method.body:
            if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
                if isinstance(stmt.value.func, ast.Attribute):
                    if stmt.value.func.attr == '__init__':
                        super_call = stmt.value
                        break
        
        if not super_call:
            return False
        
        # Extract arguments
        kpi_dict = {}
        
        # Get keyword arguments
        for keyword in super_call.keywords:
            key = keyword.arg
            value = keyword.value
            
            # Convert AST value to Python value
            if isinstance(value, ast.Constant):
                kpi_dict[key] = value.value
            elif isinstance(value, ast.List):
                kpi_dict[key] = [
                    elt.value if isinstance(elt, ast.Constant) else ast.unparse(elt)
                    for elt in value.elts
                ]
            elif isinstance(value, ast.Dict):
                dict_value = {}
                for k, v in zip(value.keys, value.values):
                    dict_key = k.value if isinstance(k, ast.Constant) else ast.unparse(k)
                    dict_val = v.value if isinstance(v, ast.Constant) else ast.unparse(v)
                    dict_value[dict_key] = dict_val
                kpi_dict[key] = dict_value
            else:
                kpi_dict[key] = ast.unparse(value)
        
        # Map old field names to new field names
        field_mapping = {
            'name_': 'name',
            'description_': 'description',
            'category_': 'category',
            'modules_': 'modules',
            'metadata_': 'metadata',
        }
        
        # Create new dictionary with proper field names
        new_dict = {}
        for old_key, value in kpi_dict.items():
            new_key = field_mapping.get(old_key, old_key)
            new_dict[new_key] = value
        
        # Ensure required fields
        if 'code' not in new_dict:
            print(f"Warning: No code found in {file_path}")
            return False
        
        # Set module_code from modules list
        if 'modules' in new_dict and isinstance(new_dict['modules'], list) and new_dict['modules']:
            new_dict['module_code'] = new_dict['modules'][0]
        
        # Generate the new file content
        code_var_name = new_dict['code']
        
        new_content = f"# KPI Definition: {new_dict.get('name', code_var_name)}\n\n"
        new_content += f"{code_var_name} = {{\n"
        
        # Add fields in order
        field_order = ['code', 'name', 'description', 'category', 'modules', 'module_code', 
                      'required_objects', 'formula', 'aggregation_methods', 'time_periods',
                      'metadata', 'benchmarks', 'dimensions']
        
        for field in field_order:
            if field in new_dict:
                value = new_dict[field]
                if isinstance(value, str):
                    # Escape quotes in strings
                    value = value.replace('"', '\\"')
                    new_content += f'    "{field}": "{value}",\n'
                elif isinstance(value, list):
                    new_content += f'    "{field}": {value},\n'
                elif isinstance(value, dict):
                    new_content += f'    "{field}": {value},\n'
                else:
                    new_content += f'    "{field}": {repr(value)},\n'
        
        new_content += "}\n"
        
        # Write the new file
        file_path.write_text(new_content, encoding='utf-8')
        print(f"✅ Converted: {file_path.name}")
        return True
        
    except Exception as e:
        print(f"❌ Error converting {file_path.name}: {e}")
        return False

def main():
    """Convert all BaseKPI files"""
    kpis_dir = Path(__file__).parent / 'definitions' / 'kpis'
    
    if not kpis_dir.exists():
        print(f"Error: KPIs directory not found: {kpis_dir}")
        return
    
    print(f"Scanning {kpis_dir}...")
    
    converted = 0
    skipped = 0
    errors = 0
    
    for file_path in sorted(kpis_dir.glob('*.py')):
        if file_path.name in ['__init__.py', 'base_kpi.py']:
            continue
        
        result = convert_basekpi_file(file_path)
        if result:
            converted += 1
        elif result is False:
            skipped += 1
        else:
            errors += 1
    
    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"✅ Converted: {converted}")
    print(f"⏭️  Skipped: {skipped}")
    print(f"❌ Errors: {errors}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
