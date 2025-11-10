"""
Convert all definition files from class-based to dictionary format.

This script converts KPIs, Modules, Value Chains, Object Models, Industries,
Benchmarks, Attributes, and Mappings from the old analytics_models class format
to simple dictionary format for more robust loading.
"""

import ast
import re
from pathlib import Path
from typing import Dict, Any, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DefinitionConverter:
    """Converts definition files from class-based to dictionary format."""
    
    # Map of class names to their dictionary variable naming convention
    CLASS_TYPES = {
        'KPI': 'KPI',
        'Module': 'Module',
        'ValueChain': 'Value Chain',
        'ObjectModel': 'Object Model',
        'Industry': 'Industry',
        'Benchmark': 'Benchmark',
        'Attribute': 'Attribute',
        'Mapping': 'Mapping'
    }
    
    def __init__(self, definitions_path: Path):
        self.definitions_path = Path(definitions_path)
        self.stats = {
            'processed': 0,
            'converted': 0,
            'skipped': 0,
            'errors': 0
        }
    
    def convert_all(self):
        """Convert all definition files in all subdirectories."""
        logger.info(f"Starting conversion in {self.definitions_path}")
        
        # Process each subdirectory
        for subdir in ['kpis', 'modules', 'value_chains', 'object_models', 
                       'industries', 'benchmarks', 'attributes', 'mappings']:
            subdir_path = self.definitions_path / subdir
            if subdir_path.exists():
                logger.info(f"\n{'='*60}")
                logger.info(f"Processing {subdir}/")
                logger.info(f"{'='*60}")
                self.convert_directory(subdir_path)
        
        # Print summary
        logger.info(f"\n{'='*60}")
        logger.info("CONVERSION SUMMARY")
        logger.info(f"{'='*60}")
        logger.info(f"Files processed: {self.stats['processed']}")
        logger.info(f"Files converted: {self.stats['converted']}")
        logger.info(f"Files skipped:   {self.stats['skipped']}")
        logger.info(f"Errors:          {self.stats['errors']}")
    
    def convert_directory(self, directory: Path):
        """Convert all Python files in a directory."""
        for file_path in directory.glob('*.py'):
            # Skip __init__.py and registry.py
            if file_path.name in ['__init__.py', 'registry.py']:
                continue
            
            self.convert_file(file_path)
    
    def convert_file(self, file_path: Path) -> bool:
        """
        Convert a single file from class-based to dictionary format.
        
        Returns:
            True if converted, False if skipped or error
        """
        self.stats['processed'] += 1
        
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Check if already in dictionary format
            if 'from analytics_models import' not in content:
                logger.info(f"✓ SKIP: {file_path.name} (already dictionary format)")
                self.stats['skipped'] += 1
                return False
            
            # Parse the file
            tree = ast.parse(content)
            
            # Find the assignment with class instantiation
            converted_content = self._convert_ast(tree, content, file_path)
            
            if converted_content:
                # Write back to file
                file_path.write_text(converted_content, encoding='utf-8')
                logger.info(f"✓ CONVERTED: {file_path.name}")
                self.stats['converted'] += 1
                return True
            else:
                logger.warning(f"✗ SKIP: {file_path.name} (no conversion needed)")
                self.stats['skipped'] += 1
                return False
                
        except Exception as e:
            logger.error(f"✗ ERROR: {file_path.name} - {e}")
            self.stats['errors'] += 1
            return False
    
    def _convert_ast(self, tree: ast.AST, original_content: str, file_path: Path) -> Optional[str]:
        """Convert AST to dictionary format."""
        
        # Find the class instantiation
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                if isinstance(node.value, ast.Call):
                    if isinstance(node.value.func, ast.Name):
                        class_name = node.value.func.id
                        
                        if class_name in self.CLASS_TYPES:
                            # Get variable name
                            var_name = node.targets[0].id if isinstance(node.targets[0], ast.Name) else None
                            
                            if not var_name:
                                continue
                            
                            # Extract all keyword arguments
                            definition_dict = {}
                            for keyword in node.value.keywords:
                                key = keyword.arg
                                try:
                                    value = ast.literal_eval(keyword.value)
                                    definition_dict[key] = value
                                except:
                                    # Can't evaluate - skip this field
                                    pass
                            
                            # Build the new dictionary format
                            new_content = self._build_dict_content(
                                original_content, 
                                var_name, 
                                definition_dict,
                                class_name
                            )
                            
                            return new_content
        
        return None
    
    def _build_dict_content(self, original_content: str, var_name: str, 
                           definition_dict: Dict[str, Any], class_name: str) -> str:
        """Build new file content with dictionary format."""
        
        # Extract docstring if present
        docstring_match = re.search(r'^"""(.*?)"""', original_content, re.DOTALL | re.MULTILINE)
        docstring = docstring_match.group(0) if docstring_match else '"""\nConverted definition\n"""'
        
        # Start building new content
        lines = [docstring, ""]
        
        # Build dictionary
        lines.append(f"{var_name} = {{")
        
        # Add fields in a logical order
        field_order = [
            'code', 'name', 'display_name', 'description', 
            'formula', 'calculation_formula', 'unit', 'data_type',
            'category', 'is_active', 'display_order'
        ]
        
        # Add ordered fields first
        for field in field_order:
            if field in definition_dict:
                value = definition_dict[field]
                lines.append(f'    "{field}": {self._format_value(value)},')
        
        # Add remaining fields
        for key, value in definition_dict.items():
            if key not in field_order:
                lines.append(f'    "{key}": {self._format_value(value)},')
        
        # Handle special extractions from metadata_
        if 'metadata_' in definition_dict and isinstance(definition_dict['metadata_'], dict):
            metadata = definition_dict['metadata_']
            
            # Extract modules for KPIs
            if 'modules' in metadata and class_name == 'KPI':
                modules = metadata['modules']
                lines.append(f'    "modules": {self._format_value(modules)},')
                if modules:
                    lines.append(f'    "module_code": {self._format_value(modules[0])},')
            
            # Extract value_chains for Modules
            if 'value_chains' in metadata and class_name == 'Module':
                value_chains = metadata['value_chains']
                lines.append(f'    "value_chains": {self._format_value(value_chains)},')
        
        lines.append("}")
        
        return "\n".join(lines) + "\n"
    
    def _format_value(self, value: Any) -> str:
        """Format a Python value for dictionary representation."""
        if isinstance(value, str):
            # Escape quotes and handle multiline strings
            if '\n' in value:
                return '"""' + value + '"""'
            else:
                return '"' + value.replace('"', '\\"') + '"'
        elif isinstance(value, bool):
            return str(value)
        elif isinstance(value, (int, float)):
            return str(value)
        elif isinstance(value, list):
            return '[' + ', '.join(self._format_value(v) for v in value) + ']'
        elif isinstance(value, dict):
            items = [f'"{k}": {self._format_value(v)}' for k, v in value.items()]
            return '{' + ', '.join(items) + '}'
        elif value is None:
            return 'None'
        else:
            return repr(value)


def main():
    """Main conversion function."""
    definitions_path = Path(__file__).parent / "definitions"
    
    if not definitions_path.exists():
        logger.error(f"Definitions path not found: {definitions_path}")
        return
    
    converter = DefinitionConverter(definitions_path)
    converter.convert_all()
    
    logger.info("\n✓ Conversion complete!")


if __name__ == "__main__":
    main()
