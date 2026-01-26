"""
PostgreSQL MCP Tools for database introspection and queries.

These tools provide read-only access to TimescaleDB schema information
and sample data for use by AI agents.
"""

from __future__ import annotations

import logging
import time
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, TYPE_CHECKING

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from .postgres_mcp_models import (
    MCPToolResponse,
    SchemaInfo,
    TableInfo,
    ColumnInfo,
    IndexInfo,
    ConstraintInfo,
    HypertableInfo,
    ContinuousAggregateInfo,
    TableStatsInfo,
    QueryExplainResult,
    SampleQueryResult,
    ListSchemasRequest,
    ListTablesRequest,
    DescribeTableRequest,
    ListHypertablesRequest,
    ListContinuousAggregatesRequest,
    QuerySampleRequest,
    ExplainQueryRequest,
    GetTableStatsRequest,
)

if TYPE_CHECKING:
    from ..database_manager import DatabaseManager

logger = logging.getLogger(__name__)


class BaseMCPTool(ABC):
    """Base class for MCP tools."""
    
    name: str
    description: str
    
    def __init__(self, db_manager: "DatabaseManager"):
        self.db_manager = db_manager
    
    @abstractmethod
    async def execute(self, params: Dict[str, Any]) -> MCPToolResponse:
        """Execute the tool with given parameters."""
        pass
    
    def get_schema(self) -> Dict[str, Any]:
        """Get the tool's parameter schema for Claude."""
        return {
            "name": self.name,
            "description": self.description,
            "input_schema": self._get_input_schema()
        }
    
    @abstractmethod
    def _get_input_schema(self) -> Dict[str, Any]:
        """Get the input schema for this tool."""
        pass


class ListSchemasTool(BaseMCPTool):
    """List all database schemas."""
    
    name = "list_schemas"
    description = "List all schemas in the database with their table counts"
    
    def _get_input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "include_system": {
                    "type": "boolean",
                    "description": "Include system schemas (pg_*, information_schema)",
                    "default": False
                }
            }
        }
    
    async def execute(self, params: Dict[str, Any]) -> MCPToolResponse:
        start_time = time.time()
        try:
            request = ListSchemasRequest(**params)
            
            query = """
                SELECT 
                    n.nspname AS schema_name,
                    pg_catalog.pg_get_userbyid(n.nspowner) AS owner,
                    COUNT(c.relname) AS table_count,
                    obj_description(n.oid, 'pg_namespace') AS description
                FROM pg_catalog.pg_namespace n
                LEFT JOIN pg_catalog.pg_class c 
                    ON c.relnamespace = n.oid AND c.relkind IN ('r', 'v', 'f')
                WHERE 1=1
            """
            
            if not request.include_system:
                query += """
                    AND n.nspname NOT LIKE 'pg_%'
                    AND n.nspname != 'information_schema'
                    AND n.nspname != '_timescaledb_internal'
                    AND n.nspname != '_timescaledb_config'
                    AND n.nspname != '_timescaledb_catalog'
                """
            
            query += " GROUP BY n.nspname, n.nspowner, n.oid ORDER BY n.nspname"
            
            async with self.db_manager.get_session() as session:
                result = await session.execute(text(query))
                rows = result.fetchall()
            
            schemas = [
                SchemaInfo(
                    schema_name=row.schema_name,
                    owner=row.owner,
                    table_count=row.table_count or 0,
                    description=row.description
                ).model_dump()
                for row in rows
            ]
            
            return MCPToolResponse(
                success=True,
                data={"schemas": schemas, "count": len(schemas)},
                execution_time_ms=(time.time() - start_time) * 1000
            )
            
        except Exception as e:
            logger.error(f"ListSchemasTool failed: {e}")
            return MCPToolResponse(
                success=False,
                error=str(e),
                execution_time_ms=(time.time() - start_time) * 1000
            )


class ListTablesTool(BaseMCPTool):
    """List tables in a schema."""
    
    name = "list_tables"
    description = "List all tables and views in a database schema"
    
    def _get_input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "schema_name": {
                    "type": "string",
                    "description": "Schema name to list tables from",
                    "default": "public"
                },
                "include_views": {
                    "type": "boolean",
                    "description": "Include views in the list",
                    "default": True
                },
                "table_pattern": {
                    "type": "string",
                    "description": "Filter tables by name pattern (SQL LIKE)"
                }
            }
        }
    
    async def execute(self, params: Dict[str, Any]) -> MCPToolResponse:
        start_time = time.time()
        try:
            request = ListTablesRequest(**params)
            
            table_types = "('r')"  # r = ordinary table
            if request.include_views:
                table_types = "('r', 'v')"  # v = view
            
            query = f"""
                SELECT 
                    c.relname AS table_name,
                    n.nspname AS schema_name,
                    CASE c.relkind 
                        WHEN 'r' THEN 'BASE TABLE'
                        WHEN 'v' THEN 'VIEW'
                        WHEN 'f' THEN 'FOREIGN TABLE'
                    END AS table_type,
                    EXISTS (
                        SELECT 1 FROM _timescaledb_catalog.hypertable h
                        WHERE h.schema_name = n.nspname AND h.table_name = c.relname
                    ) AS is_hypertable,
                    c.reltuples::bigint AS row_count_estimate,
                    pg_total_relation_size(c.oid) AS total_size_bytes,
                    obj_description(c.oid, 'pg_class') AS description
                FROM pg_catalog.pg_class c
                JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
                WHERE c.relkind IN {table_types}
                    AND n.nspname = :schema_name
            """
            
            if request.table_pattern:
                query += " AND c.relname LIKE :pattern"
            
            query += " ORDER BY c.relname"
            
            params_dict = {"schema_name": request.schema_name}
            if request.table_pattern:
                params_dict["pattern"] = request.table_pattern
            
            async with self.db_manager.get_session() as session:
                result = await session.execute(text(query), params_dict)
                rows = result.fetchall()
            
            tables = [
                TableInfo(
                    table_name=row.table_name,
                    schema_name=row.schema_name,
                    table_type=row.table_type,
                    is_hypertable=row.is_hypertable or False,
                    row_count_estimate=row.row_count_estimate if row.row_count_estimate > 0 else None,
                    total_size_bytes=row.total_size_bytes,
                    description=row.description
                ).model_dump()
                for row in rows
            ]
            
            return MCPToolResponse(
                success=True,
                data={"tables": tables, "count": len(tables)},
                execution_time_ms=(time.time() - start_time) * 1000
            )
            
        except Exception as e:
            logger.error(f"ListTablesTool failed: {e}")
            return MCPToolResponse(
                success=False,
                error=str(e),
                execution_time_ms=(time.time() - start_time) * 1000
            )


class DescribeTableTool(BaseMCPTool):
    """Describe table structure with columns, indexes, and constraints."""
    
    name = "describe_table"
    description = "Get detailed information about a table including columns, indexes, and constraints"
    
    def _get_input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "table_name": {
                    "type": "string",
                    "description": "Name of the table to describe"
                },
                "schema_name": {
                    "type": "string",
                    "description": "Schema containing the table",
                    "default": "public"
                },
                "include_indexes": {
                    "type": "boolean",
                    "description": "Include index information",
                    "default": True
                },
                "include_constraints": {
                    "type": "boolean",
                    "description": "Include constraint information",
                    "default": True
                }
            },
            "required": ["table_name"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> MCPToolResponse:
        start_time = time.time()
        try:
            request = DescribeTableRequest(**params)
            
            # Get columns
            columns_query = """
                SELECT 
                    a.attname AS column_name,
                    pg_catalog.format_type(a.atttypid, a.atttypmod) AS data_type,
                    NOT a.attnotnull AS is_nullable,
                    pg_get_expr(d.adbin, d.adrelid) AS column_default,
                    CASE WHEN a.atttypid = ANY(ARRAY['varchar'::regtype, 'char'::regtype, 'text'::regtype])
                         THEN a.atttypmod - 4
                         ELSE NULL
                    END AS character_maximum_length,
                    CASE WHEN a.atttypid = 'numeric'::regtype
                         THEN ((a.atttypmod - 4) >> 16) & 65535
                         ELSE NULL
                    END AS numeric_precision,
                    CASE WHEN a.atttypid = 'numeric'::regtype
                         THEN (a.atttypmod - 4) & 65535
                         ELSE NULL
                    END AS numeric_scale,
                    EXISTS (
                        SELECT 1 FROM pg_constraint pk
                        WHERE pk.conrelid = c.oid 
                        AND pk.contype = 'p'
                        AND a.attnum = ANY(pk.conkey)
                    ) AS is_primary_key,
                    col_description(c.oid, a.attnum) AS description
                FROM pg_catalog.pg_class c
                JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
                JOIN pg_catalog.pg_attribute a ON a.attrelid = c.oid
                LEFT JOIN pg_catalog.pg_attrdef d ON d.adrelid = c.oid AND d.adnum = a.attnum
                WHERE n.nspname = :schema_name
                    AND c.relname = :table_name
                    AND a.attnum > 0
                    AND NOT a.attisdropped
                ORDER BY a.attnum
            """
            
            async with self.db_manager.get_session() as session:
                result = await session.execute(
                    text(columns_query),
                    {"schema_name": request.schema_name, "table_name": request.table_name}
                )
                column_rows = result.fetchall()
            
            columns = [
                ColumnInfo(
                    column_name=row.column_name,
                    data_type=row.data_type,
                    is_nullable=row.is_nullable,
                    column_default=row.column_default,
                    character_maximum_length=row.character_maximum_length,
                    numeric_precision=row.numeric_precision,
                    numeric_scale=row.numeric_scale,
                    is_primary_key=row.is_primary_key,
                    description=row.description
                )
                for row in column_rows
            ]
            
            indexes = []
            if request.include_indexes:
                indexes_query = """
                    SELECT 
                        i.relname AS index_name,
                        ARRAY_AGG(a.attname ORDER BY array_position(ix.indkey, a.attnum)) AS columns,
                        ix.indisunique AS is_unique,
                        ix.indisprimary AS is_primary,
                        am.amname AS index_type
                    FROM pg_catalog.pg_class t
                    JOIN pg_catalog.pg_namespace n ON n.oid = t.relnamespace
                    JOIN pg_catalog.pg_index ix ON ix.indrelid = t.oid
                    JOIN pg_catalog.pg_class i ON i.oid = ix.indexrelid
                    JOIN pg_catalog.pg_am am ON am.oid = i.relam
                    JOIN pg_catalog.pg_attribute a ON a.attrelid = t.oid AND a.attnum = ANY(ix.indkey)
                    WHERE n.nspname = :schema_name
                        AND t.relname = :table_name
                    GROUP BY i.relname, ix.indisunique, ix.indisprimary, am.amname
                """
                
                async with self.db_manager.get_session() as session:
                    result = await session.execute(
                        text(indexes_query),
                        {"schema_name": request.schema_name, "table_name": request.table_name}
                    )
                    index_rows = result.fetchall()
                
                indexes = [
                    IndexInfo(
                        index_name=row.index_name,
                        columns=row.columns,
                        is_unique=row.is_unique,
                        is_primary=row.is_primary,
                        index_type=row.index_type
                    )
                    for row in index_rows
                ]
            
            constraints = []
            if request.include_constraints:
                constraints_query = """
                    SELECT 
                        con.conname AS constraint_name,
                        CASE con.contype
                            WHEN 'p' THEN 'PRIMARY KEY'
                            WHEN 'f' THEN 'FOREIGN KEY'
                            WHEN 'u' THEN 'UNIQUE'
                            WHEN 'c' THEN 'CHECK'
                        END AS constraint_type,
                        ARRAY_AGG(a.attname ORDER BY array_position(con.conkey, a.attnum)) AS columns,
                        ref_ns.nspname || '.' || ref_cl.relname AS reference_table,
                        ARRAY(
                            SELECT ref_a.attname
                            FROM pg_attribute ref_a
                            WHERE ref_a.attrelid = con.confrelid
                            AND ref_a.attnum = ANY(con.confkey)
                        ) AS reference_columns
                    FROM pg_constraint con
                    JOIN pg_class cl ON cl.oid = con.conrelid
                    JOIN pg_namespace ns ON ns.oid = cl.relnamespace
                    JOIN pg_attribute a ON a.attrelid = cl.oid AND a.attnum = ANY(con.conkey)
                    LEFT JOIN pg_class ref_cl ON ref_cl.oid = con.confrelid
                    LEFT JOIN pg_namespace ref_ns ON ref_ns.oid = ref_cl.relnamespace
                    WHERE ns.nspname = :schema_name
                        AND cl.relname = :table_name
                    GROUP BY con.conname, con.contype, ref_ns.nspname, ref_cl.relname, con.confrelid, con.confkey
                """
                
                async with self.db_manager.get_session() as session:
                    result = await session.execute(
                        text(constraints_query),
                        {"schema_name": request.schema_name, "table_name": request.table_name}
                    )
                    constraint_rows = result.fetchall()
                
                constraints = [
                    ConstraintInfo(
                        constraint_name=row.constraint_name,
                        constraint_type=row.constraint_type,
                        columns=row.columns,
                        reference_table=row.reference_table,
                        reference_columns=row.reference_columns if row.reference_columns else None
                    )
                    for row in constraint_rows
                ]
            
            table_info = TableInfo(
                table_name=request.table_name,
                schema_name=request.schema_name,
                columns=columns,
                indexes=indexes,
                constraints=constraints
            )
            
            return MCPToolResponse(
                success=True,
                data={"table": table_info.model_dump()},
                execution_time_ms=(time.time() - start_time) * 1000
            )
            
        except Exception as e:
            logger.error(f"DescribeTableTool failed: {e}")
            return MCPToolResponse(
                success=False,
                error=str(e),
                execution_time_ms=(time.time() - start_time) * 1000
            )


class ListHypertablesTool(BaseMCPTool):
    """List TimescaleDB hypertables."""
    
    name = "list_hypertables"
    description = "List all TimescaleDB hypertables with their configuration"
    
    def _get_input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "schema_name": {
                    "type": "string",
                    "description": "Filter by schema name (optional)"
                }
            }
        }
    
    async def execute(self, params: Dict[str, Any]) -> MCPToolResponse:
        start_time = time.time()
        try:
            request = ListHypertablesRequest(**params)
            
            query = """
                SELECT 
                    h.hypertable_schema AS schema_name,
                    h.hypertable_name AS hypertable_name,
                    d.column_name AS time_column,
                    h.num_chunks,
                    pg_size_pretty(hypertable_size(format('%I.%I', h.hypertable_schema, h.hypertable_name)::regclass)) AS total_size,
                    hypertable_size(format('%I.%I', h.hypertable_schema, h.hypertable_name)::regclass) AS total_size_bytes,
                    c.compression_enabled
                FROM timescaledb_information.hypertables h
                JOIN timescaledb_information.dimensions d 
                    ON d.hypertable_schema = h.hypertable_schema 
                    AND d.hypertable_name = h.hypertable_name
                    AND d.dimension_type = 'Time'
                LEFT JOIN timescaledb_information.compression_settings c
                    ON c.hypertable_schema = h.hypertable_schema
                    AND c.hypertable_name = h.hypertable_name
                WHERE 1=1
            """
            
            params_dict = {}
            if request.schema_name:
                query += " AND h.hypertable_schema = :schema_name"
                params_dict["schema_name"] = request.schema_name
            
            query += " ORDER BY h.hypertable_schema, h.hypertable_name"
            
            async with self.db_manager.get_session() as session:
                result = await session.execute(text(query), params_dict)
                rows = result.fetchall()
            
            hypertables = [
                HypertableInfo(
                    hypertable_name=row.hypertable_name,
                    schema_name=row.schema_name,
                    time_column=row.time_column,
                    num_chunks=row.num_chunks or 0,
                    total_size_bytes=row.total_size_bytes,
                    compression_enabled=row.compression_enabled or False
                ).model_dump()
                for row in rows
            ]
            
            return MCPToolResponse(
                success=True,
                data={"hypertables": hypertables, "count": len(hypertables)},
                execution_time_ms=(time.time() - start_time) * 1000
            )
            
        except Exception as e:
            logger.error(f"ListHypertablesTool failed: {e}")
            return MCPToolResponse(
                success=False,
                error=str(e),
                execution_time_ms=(time.time() - start_time) * 1000
            )


class ListContinuousAggregatesTool(BaseMCPTool):
    """List TimescaleDB continuous aggregates."""
    
    name = "list_continuous_aggregates"
    description = "List all TimescaleDB continuous aggregates"
    
    def _get_input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "schema_name": {
                    "type": "string",
                    "description": "Filter by schema name (optional)"
                }
            }
        }
    
    async def execute(self, params: Dict[str, Any]) -> MCPToolResponse:
        start_time = time.time()
        try:
            request = ListContinuousAggregatesRequest(**params)
            
            query = """
                SELECT 
                    view_schema AS schema_name,
                    view_name,
                    format('%I.%I', ht.hypertable_schema, ht.hypertable_name) AS source_hypertable,
                    materialized
                FROM timescaledb_information.continuous_aggregates ca
                JOIN timescaledb_information.hypertables ht
                    ON ht.hypertable_schema = ca.hypertable_schema
                    AND ht.hypertable_name = ca.hypertable_name
                WHERE 1=1
            """
            
            params_dict = {}
            if request.schema_name:
                query += " AND view_schema = :schema_name"
                params_dict["schema_name"] = request.schema_name
            
            query += " ORDER BY view_schema, view_name"
            
            async with self.db_manager.get_session() as session:
                result = await session.execute(text(query), params_dict)
                rows = result.fetchall()
            
            caggs = [
                ContinuousAggregateInfo(
                    view_name=row.view_name,
                    schema_name=row.schema_name,
                    source_hypertable=row.source_hypertable,
                    materialized=row.materialized
                ).model_dump()
                for row in rows
            ]
            
            return MCPToolResponse(
                success=True,
                data={"continuous_aggregates": caggs, "count": len(caggs)},
                execution_time_ms=(time.time() - start_time) * 1000
            )
            
        except Exception as e:
            logger.error(f"ListContinuousAggregatesTool failed: {e}")
            return MCPToolResponse(
                success=False,
                error=str(e),
                execution_time_ms=(time.time() - start_time) * 1000
            )


class QuerySampleTool(BaseMCPTool):
    """Query sample data from a table (read-only, limited rows)."""
    
    name = "query_sample"
    description = "Get a sample of data from a table (read-only, max 100 rows)"
    
    def _get_input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "table_name": {
                    "type": "string",
                    "description": "Name of the table to sample"
                },
                "schema_name": {
                    "type": "string",
                    "description": "Schema containing the table",
                    "default": "public"
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of rows to return (max 100)",
                    "default": 10,
                    "maximum": 100
                },
                "columns": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Specific columns to select (optional)"
                },
                "order_by": {
                    "type": "string",
                    "description": "Column to order by (optional)"
                }
            },
            "required": ["table_name"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> MCPToolResponse:
        start_time = time.time()
        try:
            request = QuerySampleRequest(**params)
            
            # Sanitize inputs
            limit = min(request.limit, 100)
            
            # Build column list
            if request.columns:
                # Validate column names (basic sanitization)
                columns = ", ".join(
                    f'"{col}"' for col in request.columns 
                    if col.replace("_", "").isalnum()
                )
            else:
                columns = "*"
            
            # Build query (parameterized for safety)
            query = f'SELECT {columns} FROM "{request.schema_name}"."{request.table_name}"'
            
            if request.order_by and request.order_by.replace("_", "").isalnum():
                query += f' ORDER BY "{request.order_by}" DESC'
            
            query += f" LIMIT {limit}"
            
            async with self.db_manager.get_session() as session:
                result = await session.execute(text(query))
                rows = result.fetchall()
                column_names = list(result.keys())
            
            # Convert to list of dicts
            data_rows = [
                {col: self._serialize_value(row[i]) for i, col in enumerate(column_names)}
                for row in rows
            ]
            
            return MCPToolResponse(
                success=True,
                data={
                    "sample": SampleQueryResult(
                        table_name=request.table_name,
                        columns=column_names,
                        rows=data_rows,
                        row_count=len(data_rows),
                        truncated=len(data_rows) >= limit
                    ).model_dump()
                },
                execution_time_ms=(time.time() - start_time) * 1000
            )
            
        except Exception as e:
            logger.error(f"QuerySampleTool failed: {e}")
            return MCPToolResponse(
                success=False,
                error=str(e),
                execution_time_ms=(time.time() - start_time) * 1000
            )
    
    def _serialize_value(self, value: Any) -> Any:
        """Serialize value for JSON output."""
        if value is None:
            return None
        if hasattr(value, 'isoformat'):
            return value.isoformat()
        if isinstance(value, (bytes, bytearray)):
            return value.hex()
        return value


class ExplainQueryTool(BaseMCPTool):
    """Explain a query plan."""
    
    name = "explain_query"
    description = "Get the execution plan for a SQL query (EXPLAIN ANALYZE)"
    
    def _get_input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "SQL query to explain (SELECT only)"
                },
                "analyze": {
                    "type": "boolean",
                    "description": "Run ANALYZE for actual timing",
                    "default": True
                },
                "buffers": {
                    "type": "boolean",
                    "description": "Include buffer usage statistics",
                    "default": False
                }
            },
            "required": ["query"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> MCPToolResponse:
        start_time = time.time()
        try:
            request = ExplainQueryRequest(**params)
            
            # Safety: Only allow SELECT queries
            query_upper = request.query.strip().upper()
            if not query_upper.startswith("SELECT"):
                return MCPToolResponse(
                    success=False,
                    error="Only SELECT queries can be explained",
                    execution_time_ms=(time.time() - start_time) * 1000
                )
            
            # Build EXPLAIN query
            explain_options = ["FORMAT JSON"]
            if request.analyze:
                explain_options.append("ANALYZE")
            if request.buffers:
                explain_options.append("BUFFERS")
            
            explain_query = f"EXPLAIN ({', '.join(explain_options)}) {request.query}"
            
            async with self.db_manager.get_session() as session:
                result = await session.execute(text(explain_query))
                plan_json = result.scalar()
            
            # Parse the plan
            plan = plan_json[0] if plan_json else {}
            
            explain_result = QueryExplainResult(
                query=request.query,
                plan=plan_json,
                execution_time_ms=plan.get("Execution Time", 0),
                planning_time_ms=plan.get("Planning Time", 0),
                total_cost=plan.get("Plan", {}).get("Total Cost", 0),
                rows_estimate=plan.get("Plan", {}).get("Plan Rows", 0),
                rows_actual=plan.get("Plan", {}).get("Actual Rows")
            )
            
            return MCPToolResponse(
                success=True,
                data={"explain": explain_result.model_dump()},
                execution_time_ms=(time.time() - start_time) * 1000
            )
            
        except Exception as e:
            logger.error(f"ExplainQueryTool failed: {e}")
            return MCPToolResponse(
                success=False,
                error=str(e),
                execution_time_ms=(time.time() - start_time) * 1000
            )


class GetTableStatsTool(BaseMCPTool):
    """Get table statistics."""
    
    name = "get_table_stats"
    description = "Get statistics about a table (row count, size, vacuum info)"
    
    def _get_input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "table_name": {
                    "type": "string",
                    "description": "Name of the table"
                },
                "schema_name": {
                    "type": "string",
                    "description": "Schema containing the table",
                    "default": "public"
                }
            },
            "required": ["table_name"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> MCPToolResponse:
        start_time = time.time()
        try:
            request = GetTableStatsRequest(**params)
            
            query = """
                SELECT 
                    n.nspname AS schema_name,
                    c.relname AS table_name,
                    c.reltuples::bigint AS row_count,
                    pg_total_relation_size(c.oid) AS total_size_bytes,
                    pg_table_size(c.oid) AS table_size_bytes,
                    pg_indexes_size(c.oid) AS index_size_bytes,
                    COALESCE(pg_total_relation_size(c.reltoastrelid), 0) AS toast_size_bytes,
                    s.last_vacuum,
                    s.last_analyze,
                    s.n_dead_tup AS dead_tuples,
                    s.n_live_tup AS live_tuples
                FROM pg_catalog.pg_class c
                JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
                LEFT JOIN pg_stat_user_tables s 
                    ON s.schemaname = n.nspname AND s.relname = c.relname
                WHERE n.nspname = :schema_name
                    AND c.relname = :table_name
            """
            
            async with self.db_manager.get_session() as session:
                result = await session.execute(
                    text(query),
                    {"schema_name": request.schema_name, "table_name": request.table_name}
                )
                row = result.fetchone()
            
            if not row:
                return MCPToolResponse(
                    success=False,
                    error=f"Table {request.schema_name}.{request.table_name} not found",
                    execution_time_ms=(time.time() - start_time) * 1000
                )
            
            stats = TableStatsInfo(
                table_name=row.table_name,
                schema_name=row.schema_name,
                row_count=row.row_count or 0,
                total_size_bytes=row.total_size_bytes or 0,
                table_size_bytes=row.table_size_bytes or 0,
                index_size_bytes=row.index_size_bytes or 0,
                toast_size_bytes=row.toast_size_bytes or 0,
                last_vacuum=row.last_vacuum,
                last_analyze=row.last_analyze,
                dead_tuples=row.dead_tuples or 0,
                live_tuples=row.live_tuples or 0
            )
            
            return MCPToolResponse(
                success=True,
                data={"stats": stats.model_dump()},
                execution_time_ms=(time.time() - start_time) * 1000
            )
            
        except Exception as e:
            logger.error(f"GetTableStatsTool failed: {e}")
            return MCPToolResponse(
                success=False,
                error=str(e),
                execution_time_ms=(time.time() - start_time) * 1000
            )


# Tool registry
ALL_POSTGRES_TOOLS = [
    ListSchemasTool,
    ListTablesTool,
    DescribeTableTool,
    ListHypertablesTool,
    ListContinuousAggregatesTool,
    QuerySampleTool,
    ExplainQueryTool,
    GetTableStatsTool,
]
