from typing import Dict, Any, List
from ..ontology_models import EntityDefinition, MetricDefinition

class CodeGenerator:
    """
    Generates execution artifacts (Code/Schema) from Ontology Definitions.
    """

    def generate_pydantic_model(self, entity: EntityDefinition) -> str:
        """
        Generates Python code for a Pydantic v2 model representing the entity.
        """
        lines = [
            "from pydantic import BaseModel, Field",
            "from typing import Optional",
            "from datetime import datetime",
            "",
            f"class {entity.name}(BaseModel):",
            f'    """{entity.description or "Auto-generated model"}"""',
        ]
        
        # Use table_schema if available
        if entity.table_schema and entity.table_schema.columns:
            for col in entity.table_schema.columns:
                py_type = self._map_type_to_python(col.type)
                desc = col.description or ""
                lines.append(f"    {col.name}: {py_type} = Field(description='{desc}')")
        
        return "\n".join(lines)

    def generate_timescaledb_ddl(self, entity: EntityDefinition) -> str:
        """
        Generates SQL DDL to create a hypertable for the entity.
        """
        table_name = entity.code.lower()
        if entity.table_schema and entity.table_schema.table_name:
            table_name = entity.table_schema.table_name

        lines = [f"CREATE TABLE IF NOT EXISTS {table_name} ("]
        
        # Standard columns
        lines.append("    time TIMESTAMPTZ NOT NULL,")
        
        if entity.table_schema and entity.table_schema.columns:
            for col in entity.table_schema.columns:
                sql_type = self._map_type_to_sql(col.type)
                lines.append(f"    {col.name} {sql_type},")
        
        lines.append("    PRIMARY KEY (time, id)") # Assuming 'id' exists or is handled
        lines.append(");")
        
        # Hypertable conversion
        lines.append(f"SELECT create_hypertable('{table_name}', 'time', if_not_exists => TRUE);")
        
        return "\n".join(lines)

    def _map_type_to_python(self, attr_type: str) -> str:
        mapping = {
            "string": "str", "integer": "int", "decimal": "float", 
            "boolean": "bool", "timestamp": "datetime"
        }
        return mapping.get(attr_type.lower(), "Any")

    def _map_type_to_sql(self, attr_type: str) -> str:
        mapping = {
            "string": "TEXT", "integer": "INTEGER", "decimal": "NUMERIC", 
            "boolean": "BOOLEAN", "timestamp": "TIMESTAMPTZ"
        }
        return mapping.get(attr_type.lower(), "TEXT")
