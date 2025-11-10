"""
Object Model Restructuring Script

Converts existing object model files from UML-only format to JSON schema + UML format.

UPDATED: Now works with dictionary-based definitions.

This script:
1. Parses existing object model files
2. Extracts column definitions from UML
3. Generates JSON table_schema
4. Preserves UML for relationships only
5. Updates files with new format

Usage:
    python restructure_object_models.py --dry-run  # Preview changes
    python restructure_object_models.py            # Apply changes
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
import sys
from definition_loader import load_definition_file, update_definition_field, add_definition_field

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))


class ObjectModelRestructurer:
    """Restructures object model files to include JSON schema."""
    
    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
        self.object_models_dir = project_root / "services" / "business_services" / "analytics_metadata_service" / "definitions" / "object_models"
        self.results = {
            "processed": 0,
            "updated": 0,
            "errors": 0,
            "skipped": 0
        }
    
    def parse_key_attributes(self, content: str) -> List[str]:
        """
        Extract key_attributes from metadata if present.
        
        Example:
            "key_attributes": [
                "subscription_id",
                "customer_id",
                "start_date"
            ]
        """
        match = re.search(r'"key_attributes":\s*\[(.*?)\]', content, re.DOTALL)
        if not match:
            return []
        
        attrs_text = match.group(1)
        # Extract quoted strings
        attrs = re.findall(r'"([^"]+)"', attrs_text)
        return attrs
    
    def infer_column_type(self, attr_name: str) -> Dict[str, Any]:
        """
        Infer column type from attribute name.
        
        Common patterns:
        - *_id: Integer or String FK
        - *_date, *_at: DateTime
        - *_count, *_number: Integer
        - *_rate, *_percentage, *_value, *_amount: Float
        - *_status, *_type, *_name: String
        - is_*, has_*: Boolean
        """
        attr_lower = attr_name.lower()
        
        column = {"name": attr_name}
        
        # ID fields
        if attr_name.endswith('_id') or attr_name == 'id':
            if attr_name == 'id':
                column["type"] = "Integer"
                column["primary_key"] = True
                column["autoincrement"] = True
            else:
                column["type"] = "Integer"
                column["index"] = True
        
        # Date/Time fields
        elif any(x in attr_lower for x in ['_date', '_at', '_time']):
            column["type"] = "DateTime"
            column["index"] = True
        
        # Numeric fields
        elif any(x in attr_lower for x in ['_count', '_number', '_quantity', '_qty']):
            column["type"] = "Integer"
        
        # Float fields
        elif any(x in attr_lower for x in ['_rate', '_percentage', '_value', '_amount', '_score', '_ratio']):
            column["type"] = "Float"
        
        # Boolean fields
        elif attr_lower.startswith('is_') or attr_lower.startswith('has_'):
            column["type"] = "Boolean"
            column["default"] = "False"
        
        # Status/Type fields
        elif any(x in attr_lower for x in ['_status', '_type', '_category', '_level']):
            column["type"] = "String"
            column["length"] = 50
            column["index"] = True
        
        # Email
        elif 'email' in attr_lower:
            column["type"] = "String"
            column["length"] = 255
            column["unique"] = True
        
        # Name fields
        elif any(x in attr_lower for x in ['_name', '_title', '_description']):
            if 'description' in attr_lower:
                column["type"] = "Text"
            else:
                column["type"] = "String"
                column["length"] = 255
        
        # Default to String
        else:
            column["type"] = "String"
            column["length"] = 255
        
        return column
    
    def parse_uml_columns(self, uml_text: str) -> List[Dict[str, Any]]:
        """
        Parse column definitions from UML class diagram.
        
        Example UML:
            +id: Integer PK
            +name: String(255)
            +email: String(255) UNIQUE
            +created_at: DateTime
            +parent_id: Integer FK
        """
        columns = []
        
        # Pattern to match UML attribute lines
        # Format: +name: Type(length) constraints
        pattern = r'\+(\w+):\s*(\w+)(?:\((\d+)\))?\s*(.*?)$'
        
        for line in uml_text.split('\n'):
            line = line.strip()
            match = re.match(pattern, line)
            
            if match:
                name, col_type, length, constraints = match.groups()
                
                column = {
                    "name": name,
                    "type": col_type
                }
                
                # Add length if specified
                if length:
                    column["length"] = int(length)
                
                # Parse constraints
                constraints_upper = constraints.upper()
                
                if "PK" in constraints_upper or "PRIMARY KEY" in constraints_upper:
                    column["primary_key"] = True
                    column["autoincrement"] = True
                
                if "FK" in constraints_upper or "FOREIGN KEY" in constraints_upper:
                    # Try to extract FK reference
                    fk_match = re.search(r'FK\s*\(([^)]+)\)', constraints)
                    if fk_match:
                        column["foreign_key"] = fk_match.group(1)
                
                if "UNIQUE" in constraints_upper:
                    column["unique"] = True
                
                if "NOT NULL" in constraints_upper:
                    column["nullable"] = False
                elif "NULLABLE" in constraints_upper:
                    column["nullable"] = True
                
                if "INDEX" in constraints_upper:
                    column["index"] = True
                
                columns.append(column)
        
        return columns
    
    def extract_relationships_from_uml(self, uml_text: str) -> str:
        """
        Extract only relationship lines from UML, remove class definitions.
        
        Keep lines like:
            Customer "1" -- "*" Order : places
            Customer "1" -- "1" CustomerHealthRecord : has
        
        Remove lines like:
            class Customer {
            +id: Integer PK
            }
        """
        lines = []
        in_class_definition = False
        
        for line in uml_text.split('\n'):
            stripped = line.strip()
            
            # Skip empty lines and PlantUML markers
            if not stripped or stripped in ['@startuml', '@enduml']:
                continue
            
            # Track class definition blocks
            if stripped.startswith('class ') and '{' in stripped:
                in_class_definition = True
                continue
            
            if in_class_definition:
                if '}' in stripped:
                    in_class_definition = False
                continue
            
            # Keep relationship lines (contain -- or ..)
            if '--' in stripped or '..' in stripped:
                lines.append(line)
            
            # Keep comments and notes
            elif stripped.startswith("'") or stripped.startswith('note'):
                lines.append(line)
        
        if not lines:
            return ""
        
        return "@startuml\n" + '\n'.join(lines) + "\n@enduml"
    
    def generate_table_schema(self, object_name: str, code: str, columns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate JSON table schema from parsed columns."""
        
        # Convert object code to table name (lowercase, underscores)
        table_name = code.lower()
        
        # Add standard timestamp columns if not present
        column_names = [col["name"] for col in columns]
        if "created_at" not in column_names:
            columns.append({
                "name": "created_at",
                "type": "DateTime",
                "default": "now()",
                "nullable": False
            })
        
        if "updated_at" not in column_names:
            columns.append({
                "name": "updated_at",
                "type": "DateTime",
                "default": "now()",
                "onupdate": "now()",
                "nullable": False
            })
        
        # Generate indexes for common columns
        indexes = []
        for col in columns:
            if col.get("unique"):
                indexes.append({
                    "name": f"ix_{table_name}_{col['name']}",
                    "columns": [col["name"]],
                    "unique": True
                })
            elif col.get("index"):
                indexes.append({
                    "name": f"ix_{table_name}_{col['name']}",
                    "columns": [col["name"]]
                })
        
        # Add index for created_at (common query pattern)
        if "created_at" in column_names:
            indexes.append({
                "name": f"ix_{table_name}_created_at",
                "columns": ["created_at"]
            })
        
        return {
            "table_name": table_name,
            "class_name": object_name,
            "columns": columns,
            "indexes": indexes if indexes else []
        }
    
    def restructure_file(self, file_path: Path) -> bool:
        """
        Restructure a single object model file.
        
        Returns True if file was updated, False if skipped or error.
        """
        try:
            print(f"\n{'='*80}")
            print(f"Processing: {file_path.name}")
            print(f"{'='*80}")
            
            # Read file
            content = file_path.read_text(encoding='utf-8')
            
            # Skip registry and utility files
            if 'Registry' in content or 'BaseRegistry' in content:
                print(f"[SKIP] {file_path.name} is a registry/utility file")
                self.results["skipped"] += 1
                return False
            
            # Check if already has table_schema
            if 'table_schema=' in content or 'table_schema =' in content:
                print(f"[SKIP] {file_path.name} already has table_schema")
                self.results["skipped"] += 1
                return False
            
            # Extract object name and code
            name_match = re.search(r'name="([^"]+)"', content)
            code_match = re.search(r'code="([^"]+)"', content)
            desc_match = re.search(r'description="([^"]+)"', content)
            
            if not name_match or not code_match:
                print(f"[ERROR] Could not extract name/code from {file_path.name}")
                self.results["errors"] += 1
                return False
            
            object_name = name_match.group(1)
            object_code = code_match.group(1)
            description = desc_match.group(1) if desc_match else ""
            
            print(f"[INFO] Object: {object_name} ({object_code})")
            
            # Extract UML
            uml_match = re.search(r'schema_definition\s*=\s*"""(.*?)"""', content, re.DOTALL)
            if not uml_match:
                print(f"[WARN] No UML found in {file_path.name}")
                # Create minimal schema
                columns = []
                relationships_uml = ""
            else:
                uml_text = uml_match.group(1)
                
                # Parse columns from UML
                columns = self.parse_uml_columns(uml_text)
                print(f"[INFO] Extracted {len(columns)} columns from UML")
                
                # Extract relationships only
                relationships_uml = self.extract_relationships_from_uml(uml_text)
            
            # If no columns from UML, try key_attributes from metadata
            if not columns:
                key_attrs = self.parse_key_attributes(content)
                if key_attrs:
                    print(f"[INFO] Using {len(key_attrs)} key_attributes from metadata")
                    columns = [self.infer_column_type(attr) for attr in key_attrs]
                else:
                    print(f"[WARN] No columns or key_attributes found, using minimal schema")
            
            # Generate table schema
            table_schema = self.generate_table_schema(object_name, object_code, columns)
            
            # Format table_schema as Python dict string
            table_schema_str = self.format_table_schema(table_schema)
            
            # Build new content
            new_content = self.build_new_file_content(
                file_path,
                content,
                object_name,
                object_code,
                description,
                table_schema_str,
                relationships_uml if uml_match else ""
            )
            
            if self.dry_run:
                print(f"[DRY RUN] Would update {file_path.name}")
                print(f"\nTable Schema Preview:")
                print(table_schema_str[:500] + "..." if len(table_schema_str) > 500 else table_schema_str)
            else:
                # Write updated file
                file_path.write_text(new_content, encoding='utf-8')
                print(f"[SUCCESS] UPDATED: {file_path.name}")
                self.results["updated"] += 1
            
            self.results["processed"] += 1
            return True
            
        except Exception as e:
            print(f"[ERROR] processing {file_path.name}: {str(e)}")
            self.results["errors"] += 1
            return False
    
    def format_table_schema(self, schema: Dict[str, Any]) -> str:
        """Format table schema as Python dict string."""
        lines = ["table_schema={"]
        
        # Table name and class name
        lines.append(f'        "table_name": "{schema["table_name"]}",')
        lines.append(f'        "class_name": "{schema["class_name"]}",')
        
        # Columns
        lines.append('        "columns": [')
        for i, col in enumerate(schema["columns"]):
            col_lines = ["            {"]
            for key, value in col.items():
                if isinstance(value, str):
                    col_lines.append(f'                "{key}": "{value}",')
                elif isinstance(value, bool):
                    col_lines.append(f'                "{key}": {str(value)},')
                elif isinstance(value, int):
                    col_lines.append(f'                "{key}": {value},')
            # Remove trailing comma from last item
            col_lines[-1] = col_lines[-1].rstrip(',')
            col_lines.append("            }" + ("," if i < len(schema["columns"]) - 1 else ""))
            lines.extend(col_lines)
        lines.append("        ],")
        
        # Indexes
        if schema.get("indexes"):
            lines.append('        "indexes": [')
            for i, idx in enumerate(schema["indexes"]):
                lines.append("            {")
                lines.append(f'                "name": "{idx["name"]}",')
                lines.append(f'                "columns": {json.dumps(idx["columns"])},')
                if idx.get("unique"):
                    lines.append(f'                "unique": True')
                else:
                    lines[-1] = lines[-1].rstrip(',')
                lines.append("            }" + ("," if i < len(schema["indexes"]) - 1 else ""))
            lines.append("        ]")
        
        lines.append("    },")
        
        return '\n'.join(lines)
    
    def build_new_file_content(
        self,
        file_path: Path,
        original_content: str,
        object_name: str,
        object_code: str,
        description: str,
        table_schema_str: str,
        relationships_uml: str
    ) -> str:
        """Build new file content with table_schema and updated UML."""
        
        # Extract docstring
        docstring_match = re.search(r'"""(.*?)"""', original_content, re.DOTALL)
        docstring = docstring_match.group(0) if docstring_match else f'"""\n{object_name} Object Model\n\n{description}\n"""'
        
        # Extract metadata if present
        metadata_match = re.search(r'metadata_\s*=\s*{(.*?)}', original_content, re.DOTALL)
        metadata_str = f"metadata_={{{metadata_match.group(1)}}}" if metadata_match else ""
        
        # Build new content
        lines = [
            docstring,
            "",
            "from analytics_models import ObjectModel",
            "",
            f"{object_code} = ObjectModel(",
            f'    name="{object_name}",',
            f'    code="{object_code}",',
            f'    description="{description}",',
            "",
            "    # Table Schema - For CQRS table creation",
            f"    {table_schema_str}",
            ""
        ]
        
        # Add UML if relationships exist
        if relationships_uml and relationships_uml.strip():
            lines.extend([
                "    # UML Relationships - For documentation",
                f'    schema_definition="""',
                f'    {relationships_uml.strip()}',
                '    """,',
                ""
            ])
        
        # Add metadata if present
        if metadata_str:
            lines.extend([
                f"    {metadata_str}",
                ""
            ])
        
        lines.append(")")
        
        return '\n'.join(lines) + '\n'
    
    def run(self):
        """Run restructuring on all object model files."""
        print(f"\n{'='*80}")
        print(f"Object Model Restructuring Script")
        print(f"{'='*80}")
        print(f"Mode: {'DRY RUN' if self.dry_run else 'LIVE'}")
        print(f"Directory: {self.object_models_dir}")
        print(f"{'='*80}\n")
        
        # Get all Python files except __init__.py
        files = sorted([
            f for f in self.object_models_dir.glob("*.py")
            if f.name != "__init__.py"
        ])
        
        print(f"Found {len(files)} object model files to process\n")
        
        # Process each file
        for file_path in files:
            self.restructure_file(file_path)
        
        # Print summary
        print(f"\n{'='*80}")
        print(f"SUMMARY")
        print(f"{'='*80}")
        print(f"Processed: {self.results['processed']}")
        print(f"Updated:   {self.results['updated']}")
        print(f"Skipped:   {self.results['skipped']}")
        print(f"Errors:    {self.results['errors']}")
        print(f"{'='*80}\n")
        
        if self.dry_run:
            print("[INFO] DRY RUN MODE - No files were modified")
            print("Run without --dry-run to apply changes\n")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Restructure object model files")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without modifying files"
    )
    
    args = parser.parse_args()
    
    restructurer = ObjectModelRestructurer(dry_run=args.dry_run)
    restructurer.run()


if __name__ == "__main__":
    main()
