"""
Generate SQLAlchemy Models from Object Model Dictionary Definitions

This script reads object model definitions from the metadata service and generates
SQLAlchemy model classes in base_models.py for the database service.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Any
import importlib.util

# Paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
OBJECT_MODELS_DIR = PROJECT_ROOT / "services" / "business_services" / "analytics_metadata_service" / "definitions" / "object_models"
BASE_MODELS_FILE = PROJECT_ROOT / "services" / "backend_services" / "database_service" / "app" / "base_models.py"

# Type mapping from object model definitions to SQLAlchemy types
TYPE_MAPPING = {
    "String": "String",
    "Integer": "Integer",
    "Float": "Float",
    "Boolean": "Boolean",
    "DateTime": "DateTime",
    "Date": "Date",
    "Time": "Time",
    "Text": "Text",
    "JSON": "JSON",
    "ARRAY": "ARRAY",
    "Decimal": "Numeric",
}


def load_object_model(file_path: Path) -> Dict[str, Any]:
    """Load an object model definition from a Python file."""
    try:
        spec = importlib.util.spec_from_file_location("module", file_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Find the dictionary definition (uppercase variable)
            for attr_name in dir(module):
                if attr_name.isupper() and not attr_name.startswith('_'):
                    obj = getattr(module, attr_name)
                    if isinstance(obj, dict) and 'code' in obj:
                        return obj
        return None
    except Exception as e:
        print(f"  ✗ Error loading {file_path.name}: {e}")
        return None


def generate_column_definition(column: Dict[str, Any]) -> str:
    """Generate SQLAlchemy column definition from object model column spec."""
    col_name = column['name']
    col_type = column['type']
    
    # Map type
    sa_type = TYPE_MAPPING.get(col_type, col_type)
    
    # Build type with parameters
    type_params = []
    if 'length' in column:
        type_params.append(str(column['length']))
    
    if type_params:
        type_str = f"{sa_type}({', '.join(type_params)})"
    else:
        type_str = sa_type
    
    # Add timezone for DateTime
    if col_type == "DateTime":
        type_str = "DateTime(timezone=True)"
    
    # Build column parameters
    params = []
    
    if column.get('nullable') is False:
        params.append("nullable=False")
    elif column.get('nullable') is True:
        params.append("nullable=True")
    
    if column.get('unique'):
        params.append("unique=True")
    
    if column.get('index'):
        params.append("index=True")
    
    if column.get('primary_key'):
        params.append("primary_key=True")
    
    if 'default' in column:
        default_val = column['default']
        if default_val == "now()":
            params.append("server_default=func.now()")
        else:
            params.append(f"default={repr(default_val)}")
    
    if 'onupdate' in column:
        if column['onupdate'] == "now()":
            params.append("onupdate=func.now()")
    
    # Build the full column definition
    if params:
        return f"    {col_name}: Mapped[{get_python_type(col_type)}] = mapped_column({type_str}, {', '.join(params)})"
    else:
        return f"    {col_name}: Mapped[{get_python_type(col_type)}] = mapped_column({type_str})"


def get_python_type(col_type: str) -> str:
    """Get Python type hint for a column type."""
    type_map = {
        "String": "str",
        "Integer": "int",
        "Float": "float",
        "Boolean": "bool",
        "DateTime": "datetime",
        "Date": "date",
        "Time": "time",
        "Text": "str",
        "JSON": "dict",
        "ARRAY": "List",
        "Decimal": "Decimal",
    }
    return type_map.get(col_type, "Any")


def generate_model_class(obj_model: Dict[str, Any]) -> str:
    """Generate a complete SQLAlchemy model class from object model definition."""
    table_schema = obj_model.get('table_schema', {})
    
    if not table_schema:
        return None
    
    class_name = table_schema.get('class_name', obj_model['name'])
    table_name = table_schema.get('table_name', obj_model['code'].lower())
    columns = table_schema.get('columns', [])
    indexes = table_schema.get('indexes', [])
    
    # Start building the class
    lines = []
    lines.append(f"class {class_name}(BaseModel):")
    lines.append(f"    __tablename__ = '{table_name}'")
    lines.append("")
    
    # Add columns
    for column in columns:
        # Skip columns that are already in BaseModel (id, uuid, created_at, updated_at)
        if column['name'] in ['id', 'uuid', 'created_at', 'updated_at']:
            continue
        
        col_def = generate_column_definition(column)
        lines.append(col_def)
    
    # Add indexes if any
    if indexes:
        lines.append("")
        index_defs = []
        for idx in indexes:
            idx_name = idx.get('name', f"ix_{table_name}")
            idx_cols = idx.get('columns', [])
            if idx_cols:
                cols_str = ', '.join([f"'{col}'" for col in idx_cols])
                index_defs.append(f"Index('{idx_name}', {cols_str})")
        
        if index_defs:
            lines.append(f"    __table_args__ = ({', '.join(index_defs)},)")
    
    return '\n'.join(lines)


def generate_base_models_file(models: List[str]) -> str:
    """Generate the complete base_models.py file content."""
    header = '''"""
Base Models - Auto-generated from Object Model Definitions

DO NOT EDIT THIS FILE MANUALLY!
This file is auto-generated by scripts/objectModelSync/generate_sqlalchemy_models.py
To make changes, update the object model definitions and re-run the script.

Generated: {timestamp}
"""

import uuid
from datetime import datetime, date, time
from decimal import Decimal
from typing import Any, Dict, List, Optional, TypeVar, Generic

from sqlalchemy import Column, DateTime, Integer, String, func, Text, Index, Float, Boolean, Date, Time, JSON, Numeric
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

T = TypeVar('T')

class Base(AsyncAttrs, DeclarativeBase):
    """Base class for all SQLAlchemy models."""
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        """Generate __tablename__ automatically from class name."""
        return cls.__name__.lower()

class TimestampMixin:
    """Mixin for created_at and updated_at columns."""
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

class IdMixin:
    """Mixin for id column."""
    
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

class UUIDMixin:
    """Mixin for UUID column."""
    
    uuid: Mapped[str] = mapped_column(
        String(36),
        default=lambda: str(uuid.uuid4()),
        nullable=False,
        unique=True
    )

class BaseModel(Base, IdMixin, TimestampMixin, UUIDMixin):
    """Base model with ID, UUID, and timestamps."""
    
    __abstract__ = True


class CommandBase:
    """Base class for CQRS commands."""
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert command to dictionary."""
        return {{
            key: value for key, value in self.__dict__.items()
            if not key.startswith('_')
        }}


class QueryBase(Generic[T]):
    """Base class for CQRS queries."""
    
    def __init__(self, entity: T):
        self.entity = entity
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert query result to dictionary."""
        if hasattr(self.entity, '__dict__'):
            return {{
                key: value for key, value in self.entity.__dict__.items()
                if not key.startswith('_')
            }}
        return {{'entity': str(self.entity)}}


class ReadBase(Generic[T]):
    """Base class for read models."""
    
    def __init__(self, entity: T):
        self.entity = entity
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        if hasattr(self.entity, '__dict__'):
            return {{
                key: value for key, value in self.entity.__dict__.items()
                if not key.startswith('_')
            }}
        return {{'entity': str(self.entity)}}
    
    @classmethod
    def from_entities(cls, entities: List[T]) -> List['ReadBase[T]']:
        """Create read models from entities."""
        return [cls(entity) for entity in entities]


# ============================================================================
# AUTO-GENERATED MODELS
# ============================================================================

'''
    
    from datetime import datetime as dt
    timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    header = header.format(timestamp=timestamp)
    
    # Combine header with models
    content = header + '\n\n'.join(models)
    
    return content


def main():
    """Main execution function."""
    print("\n🔄 Generating SQLAlchemy Models from Object Model Definitions")
    print("=" * 70)
    print(f"📁 Source: {OBJECT_MODELS_DIR}")
    print(f"📝 Target: {BASE_MODELS_FILE}\n")
    
    # Load all object model definitions
    object_models = []
    skipped = []
    errors = []
    
    for file_path in sorted(OBJECT_MODELS_DIR.glob("*.py")):
        if file_path.name in ['__init__.py', 'registry.py']:
            continue
        
        print(f"Processing: {file_path.name}")
        obj_model = load_object_model(file_path)
        
        if obj_model:
            if 'table_schema' in obj_model and obj_model['table_schema']:
                object_models.append(obj_model)
                print(f"  ✓ Loaded: {obj_model['name']}")
            else:
                skipped.append(file_path.name)
                print(f"  ⊘ Skipped: No table_schema defined")
        else:
            errors.append(file_path.name)
    
    print(f"\n📊 Summary:")
    print(f"  ✓ Loaded: {len(object_models)} object models")
    print(f"  ⊘ Skipped: {len(skipped)} (no table schema)")
    print(f"  ✗ Errors: {len(errors)}")
    
    if not object_models:
        print("\n⚠️  No object models with table schemas found!")
        return
    
    # Generate model classes
    print(f"\n🔨 Generating SQLAlchemy model classes...")
    models = []
    generated_count = 0
    
    for obj_model in object_models:
        model_class = generate_model_class(obj_model)
        if model_class:
            models.append(model_class)
            generated_count += 1
            print(f"  ✓ Generated: {obj_model['name']}")
    
    print(f"\n✅ Generated {generated_count} model classes")
    
    # Generate the complete file
    print(f"\n📝 Writing to {BASE_MODELS_FILE}...")
    file_content = generate_base_models_file(models)
    
    # Backup existing file
    if BASE_MODELS_FILE.exists():
        backup_file = BASE_MODELS_FILE.with_suffix('.py.bak')
        BASE_MODELS_FILE.rename(backup_file)
        print(f"  💾 Backup created: {backup_file.name}")
    
    # Write new file
    with open(BASE_MODELS_FILE, 'w', encoding='utf-8') as f:
        f.write(file_content)
    
    print(f"  ✓ File written successfully")
    
    print(f"\n🎉 SQLAlchemy models generated successfully!")
    print(f"\n⚠️  Next steps:")
    print(f"  1. Review the generated {BASE_MODELS_FILE.name}")
    print(f"  2. Run Alembic autogenerate to create migrations:")
    print(f"     alembic revision --autogenerate -m 'Add object models'")
    print(f"  3. Review and apply migrations:")
    print(f"     alembic upgrade head")
    print(f"  4. If everything works, delete the .bak file\n")


if __name__ == "__main__":
    main()
