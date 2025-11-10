"""
Definition Loader for Dictionary-Based Definitions

Loads KPIs, Modules, Value Chains, and Object Models from the new
dictionary format (post-conversion from class-based format).
"""

import ast
import re
from pathlib import Path
from typing import Dict, Any, List, Optional
import logging

logger = logging.getLogger(__name__)


def load_definition_file(file_path: Path) -> Optional[Dict[str, Any]]:
    """
    Load a definition from a Python file in dictionary format.
    
    Args:
        file_path: Path to the definition file
        
    Returns:
        Dictionary containing the definition, or None if failed
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse the Python file as AST
        tree = ast.parse(content)
        
        # Find dictionary assignments
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                # Check if it's a dictionary assignment
                if isinstance(node.value, ast.Dict):
                    try:
                        # Evaluate the dictionary
                        definition = ast.literal_eval(node.value)
                        return definition
                    except:
                        pass
                # Check if it's a variable assignment with uppercase name
                elif isinstance(node.targets[0], ast.Name):
                    var_name = node.targets[0].id
                    if var_name.isupper():
                        try:
                            # Try to evaluate the value
                            definition = ast.literal_eval(node.value)
                            if isinstance(definition, dict):
                                return definition
                        except:
                            pass
        
        logger.warning(f"Could not parse definition from {file_path.name}")
        return None
        
    except Exception as e:
        logger.error(f"Error loading {file_path.name}: {e}")
        return None


def load_all_kpis(kpis_dir: Path) -> Dict[str, Dict[str, Any]]:
    """
    Load all KPI definitions from directory.
    
    Args:
        kpis_dir: Path to KPIs directory
        
    Returns:
        Dictionary mapping KPI codes to their definitions
    """
    kpis = {}
    
    for kpi_file in kpis_dir.glob('*.py'):
        if kpi_file.name in ['__init__.py', 'registry.py', 'base_kpi.py']:
            continue
        
        definition = load_definition_file(kpi_file)
        if definition and 'code' in definition:
            kpis[definition['code']] = {
                **definition,
                '_file': kpi_file.name,
                '_path': str(kpi_file)
            }
    
    return kpis


def load_all_object_models(objects_dir: Path) -> Dict[str, Dict[str, Any]]:
    """
    Load all Object Model definitions from directory.
    
    Args:
        objects_dir: Path to object models directory
        
    Returns:
        Dictionary mapping object model codes to their definitions
    """
    objects = {}
    
    for obj_file in objects_dir.glob('*.py'):
        if obj_file.name in ['__init__.py', 'registry.py']:
            continue
        
        definition = load_definition_file(obj_file)
        if definition and 'code' in definition:
            objects[definition['code']] = {
                **definition,
                '_file': obj_file.name,
                '_path': str(obj_file)
            }
    
    return objects


def load_all_modules(modules_dir: Path) -> Dict[str, Dict[str, Any]]:
    """
    Load all Module definitions from directory.
    
    Args:
        modules_dir: Path to modules directory
        
    Returns:
        Dictionary mapping module codes to their definitions
    """
    modules = {}
    
    for module_file in modules_dir.glob('*.py'):
        if module_file.name in ['__init__.py', 'registry.py']:
            continue
        
        definition = load_definition_file(module_file)
        if definition and 'code' in definition:
            modules[definition['code']] = {
                **definition,
                '_file': module_file.name,
                '_path': str(module_file)
            }
    
    return modules


def load_all_value_chains(value_chains_dir: Path) -> Dict[str, Dict[str, Any]]:
    """
    Load all Value Chain definitions from directory.
    
    Args:
        value_chains_dir: Path to value chains directory
        
    Returns:
        Dictionary mapping value chain codes to their definitions
    """
    value_chains = {}
    
    for vc_file in value_chains_dir.glob('*.py'):
        if vc_file.name in ['__init__.py', 'registry.py']:
            continue
        
        definition = load_definition_file(vc_file)
        if definition and 'code' in definition:
            value_chains[definition['code']] = {
                **definition,
                '_file': vc_file.name,
                '_path': str(vc_file)
            }
    
    return value_chains


def update_definition_field(file_path: Path, field_name: str, new_value: Any) -> bool:
    """
    Update a specific field in a definition file.
    
    Args:
        file_path: Path to the definition file
        field_name: Name of the field to update
        new_value: New value for the field
        
    Returns:
        True if updated successfully, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Format the new value
        if isinstance(new_value, str):
            formatted_value = f'"{new_value}"'
        elif isinstance(new_value, list):
            if all(isinstance(v, str) for v in new_value):
                formatted_value = '[' + ', '.join(f'"{v}"' for v in new_value) + ']'
            else:
                formatted_value = str(new_value)
        elif isinstance(new_value, dict):
            formatted_value = str(new_value)
        else:
            formatted_value = str(new_value)
        
        # Try to find and replace the field
        pattern = rf'"{field_name}":\s*[^,\n}}]+([,\n}}])'
        replacement = f'"{field_name}": {formatted_value}\\1'
        
        updated_content = re.sub(pattern, replacement, content)
        
        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True
        
        return False
        
    except Exception as e:
        logger.error(f"Error updating {file_path.name}: {e}")
        return False


def add_definition_field(file_path: Path, field_name: str, value: Any, 
                        after_field: Optional[str] = None) -> bool:
    """
    Add a new field to a definition file.
    
    Args:
        file_path: Path to the definition file
        field_name: Name of the field to add
        value: Value for the field
        after_field: Optional field name to insert after
        
    Returns:
        True if added successfully, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Format the new value
        if isinstance(value, str):
            formatted_value = f'"{value}"'
        elif isinstance(value, list):
            if all(isinstance(v, str) for v in value):
                formatted_value = '[' + ', '.join(f'"{v}"' for v in value) + ']'
            else:
                formatted_value = str(value)
        elif isinstance(value, dict):
            formatted_value = str(value)
        else:
            formatted_value = str(value)
        
        new_field = f'    "{field_name}": {formatted_value},'
        
        if after_field:
            # Insert after specific field
            pattern = rf'("{after_field}":\s*[^,\n}}]+,)'
            replacement = f'\\1\n{new_field}'
            updated_content = re.sub(pattern, replacement, content)
        else:
            # Insert before closing brace
            pattern = r'(\n})'
            replacement = f'\n{new_field}\\1'
            updated_content = re.sub(pattern, replacement, content)
        
        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True
        
        return False
        
    except Exception as e:
        logger.error(f"Error adding field to {file_path.name}: {e}")
        return False
