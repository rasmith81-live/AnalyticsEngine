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

    def generate_kpi_view_ddl(self, metric: MetricDefinition, source_table: str) -> str:
        """
        Generates TimescaleDB Continuous Aggregate view for a KPI.
        """
        view_name = f"kpi_{metric.code.lower()}_daily"
        
        # Determine aggregation function
        agg_func = metric.default_aggregation.upper()
        allowed_aggs = ["SUM", "AVG", "MIN", "MAX", "COUNT"]
        if agg_func not in allowed_aggs:
            agg_func = "SUM"
            
        # Parse column from formula (basic assumption: raw column name or simple path)
        column = "value"
        if metric.formula:
            # Handle Entity.Attribute or just Attribute
            column = metric.formula.split(".")[-1]
            
        lines = [
            f"CREATE MATERIALIZED VIEW {view_name}",
            "WITH (timescaledb.continuous) AS",
            f"SELECT time_bucket('1 day', time) AS bucket,"
        ]
        
        # Add dimensions to SELECT
        for dim in metric.dimensions:
            lines.append(f"    {dim},")
            
        lines.append(f"    {agg_func}({column}) as value")
        lines.append(f"FROM {source_table}")
        
        # Group By
        group_cols = ["bucket"] + metric.dimensions
        lines.append(f"GROUP BY {', '.join(group_cols)}")
        lines.append("WITH NO DATA;")
        
        # Policy
        lines.append(f"SELECT add_continuous_aggregate_policy('{view_name}',")
        lines.append("    start_offset => INTERVAL '1 month',")
        lines.append("    end_offset => INTERVAL '1 hour',")
        lines.append("    schedule_interval => INTERVAL '1 hour');")
        
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
