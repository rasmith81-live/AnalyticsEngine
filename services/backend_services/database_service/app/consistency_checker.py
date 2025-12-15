
import logging
from typing import List, Dict, Any, Optional, Set
from sqlalchemy import text, inspect
from sqlalchemy.ext.asyncio import AsyncEngine
from datetime import datetime
import asyncio

from .models import ModelInfo, ValidationIssue

logger = logging.getLogger(__name__)

class ConsistencyChecker:
    """
    Background job to reconcile EntityDefinitions against actual database tables.
    Implements Zone 2 (Dynamic Layer) governance by checking 'analytics_data' schema
    tables against their definitions.
    """

    def __init__(self, engine: AsyncEngine):
        self.engine = engine
        self.analytics_schema = "analytics_data"

    async def run_check(self, entity_definitions: List[ModelInfo]) -> List[ValidationIssue]:
        """
        Run consistency check between definitions and actual DB state.
        
        Args:
            entity_definitions: List of model definitions to check.
            
        Returns:
            List of validation issues found.
        """
        issues = []
        
        try:
            # Ensure analytics schema exists
            await self._ensure_schema_exists()
            
            # Get existing tables in the analytics schema
            existing_tables = await self._get_existing_tables()
            
            for entity in entity_definitions:
                # Check if table exists
                if entity.table_name not in existing_tables:
                    issues.append(ValidationIssue(
                        severity="high",
                        category="schema_drift",
                        description=f"Table '{entity.table_name}' defined in model but missing in database schema '{self.analytics_schema}'.",
                        location=f"{self.analytics_schema}.{entity.table_name}",
                        suggestion="Run model registration or migration to create the table."
                    ))
                    continue
                
                # Check columns/fields consistency
                table_columns = existing_tables[entity.table_name]
                for field_name, field_type in entity.fields.items():
                    if field_name not in table_columns:
                        issues.append(ValidationIssue(
                            severity="medium",
                            category="schema_drift",
                            description=f"Column '{field_name}' missing in table '{entity.table_name}'.",
                            location=f"{self.analytics_schema}.{entity.table_name}.{field_name}",
                            suggestion=f"Alter table to add column '{field_name}'."
                        ))
                    # Note: Type checking could be added here, but mapping Python types to SQL types is complex
            
            # Check for orphaned tables (tables in DB but not in definitions)
            defined_table_names = {e.table_name for e in entity_definitions}
            for table_name in existing_tables:
                if table_name not in defined_table_names:
                    issues.append(ValidationIssue(
                        severity="low",
                        category="schema_drift",
                        description=f"Orphaned table '{table_name}' found in database.",
                        location=f"{self.analytics_schema}.{table_name}",
                        suggestion="Delete table if obsolete or add to entity definitions."
                    ))
                    
        except Exception as e:
            logger.error(f"Consistency check failed: {e}")
            issues.append(ValidationIssue(
                severity="critical",
                category="system_error",
                description=f"Consistency check failed: {str(e)}",
                location="ConsistencyChecker"
            ))
            
        return issues

    async def reconcile(self, entity_definitions: List[ModelInfo], auto_repair: bool = False):
        """
        Run check and optionally repair issues (Self-Healing).
        """
        issues = await self.run_check(entity_definitions)
        
        if not issues:
            logger.info("Schema consistency check passed. No drift detected.")
            return

        logger.warning(f"Schema consistency check found {len(issues)} issues.")
        
        if auto_repair:
            await self._repair_issues(issues, entity_definitions)

    async def _ensure_schema_exists(self):
        async with self.engine.begin() as conn:
            await conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {self.analytics_schema}"))

    async def _get_existing_tables(self) -> Dict[str, Set[str]]:
        """
        Returns a dictionary of table_name -> set of column_names for tables in analytics_schema.
        """
        tables = {}
        async with self.engine.connect() as conn:
            # Query information_schema
            query = text(f"""
                SELECT table_name, column_name 
                FROM information_schema.columns 
                WHERE table_schema = :schema
            """)
            result = await conn.execute(query, {"schema": self.analytics_schema})
            rows = result.fetchall()
            
            for row in rows:
                table_name = row[0]
                col_name = row[1]
                if table_name not in tables:
                    tables[table_name] = set()
                tables[table_name].add(col_name)
                
        return tables

    async def _repair_issues(self, issues: List[ValidationIssue], definitions: List[ModelInfo]):
        """
        Attempt to auto-repair drift.
        This is a simplified implementation. Complex repairs (like column type changes) are risky.
        """
        logger.info("Attempting auto-repair of schema drift...")
        
        definitions_map = {d.table_name: d for d in definitions}
        
        async with self.engine.begin() as conn:
            for issue in issues:
                try:
                    # Missing Table
                    if "missing in database schema" in issue.description:
                        # Find definition
                        table_name = issue.location.split('.')[-1]
                        if table_name in definitions_map:
                            definition = definitions_map[table_name]
                            # Create table SQL
                            # Using a simple text column default for simplicity in this example
                            # In prod, this would need a robust Type mapping
                            columns_sql = ", ".join([f"{k} TEXT" for k in definition.fields.keys()])
                            create_sql = f"CREATE TABLE IF NOT EXISTS {self.analytics_schema}.{table_name} (id SERIAL PRIMARY KEY, {columns_sql})"
                            await conn.execute(text(create_sql))
                            logger.info(f"Repaired: Created missing table {table_name}")
                    
                    # Missing Column
                    elif "missing in table" in issue.description:
                         parts = issue.location.split('.')
                         table_name = parts[-2]
                         col_name = parts[-1]
                         
                         alter_sql = f"ALTER TABLE {self.analytics_schema}.{table_name} ADD COLUMN IF NOT EXISTS {col_name} TEXT"
                         await conn.execute(text(alter_sql))
                         logger.info(f"Repaired: Added missing column {col_name} to {table_name}")
                         
                except Exception as e:
                    logger.error(f"Failed to repair issue '{issue.description}': {e}")
