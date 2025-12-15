from typing import Dict, Any, List, Optional
from ..ontology_models import RowLevelSecurityDefinition

class RowLevelSecurityService:
    """
    Service to handle Row Level Security (RLS) logic, including
    generating dynamic SQL filters from definitions.
    """

    OPERATORS = {
        "eq": "=",
        "ne": "!=",
        "gt": ">",
        "gte": ">=",
        "lt": "<",
        "lte": "<=",
        "in": "IN",
        "not_in": "NOT IN",
        "contains": "LIKE",
        "startswith": "LIKE",
        "between": "BETWEEN"
    }

    def generate_sql_filter(self, rls_def: RowLevelSecurityDefinition) -> str:
        """
        Generate a SQL WHERE clause fragment from an RLS definition.
        
        Args:
            rls_def: The RowLevelSecurityDefinition containing filters.
            
        Returns:
            A string containing the SQL condition (e.g. "region = 'US-WEST' AND segment = 'SMB'")
            Returns "1=1" if no filters are defined (allow all).
        """
        if not rls_def.attribute_filters:
            return "1=1"

        conditions = []
        for attribute, filter_condition in rls_def.attribute_filters.items():
            # filter_condition is a dict like {"eq": "value"} or {"between": [1, 10]}
            if not isinstance(filter_condition, dict):
                # Fallback for simple key-value equality: "REGION": "US-WEST"
                conditions.append(self._format_condition(attribute, "eq", filter_condition))
                continue

            for op, value in filter_condition.items():
                if op not in self.OPERATORS:
                    raise ValueError(f"Unsupported operator: {op}")
                
                conditions.append(self._format_condition(attribute, op, value))

        logic = f" {rls_def.filter_logic} "  # " AND " or " OR "
        return logic.join(conditions)

    def _format_condition(self, attribute: str, op: str, value: Any) -> str:
        """Format a single SQL condition safely."""
        # Sanitize attribute name to prevent SQL injection (basic check)
        if not attribute.isidentifier():
            raise ValueError(f"Invalid attribute name: {attribute}")

        sql_op = self.OPERATORS[op]

        if op == "in" or op == "not_in":
            if not isinstance(value, list):
                raise ValueError(f"Value for {op} must be a list")
            formatted_values = ", ".join(self._quote_value(v) for v in value)
            return f"{attribute} {sql_op} ({formatted_values})"
        
        elif op == "between":
            if not isinstance(value, list) or len(value) != 2:
                raise ValueError(f"Value for {op} must be a list of 2 elements")
            return f"{attribute} {sql_op} {self._quote_value(value[0])} AND {self._quote_value(value[1])}"
        
        elif op == "contains":
            return f"{attribute} {sql_op} {self._quote_value(f'%{value}%')}"
        
        elif op == "startswith":
            return f"{attribute} {sql_op} {self._quote_value(f'{value}%')}"
            
        else:
            return f"{attribute} {sql_op} {self._quote_value(value)}"

    def _quote_value(self, value: Any) -> str:
        """Quote string values, format dates, leave numbers alone."""
        if isinstance(value, str):
            # Basic escaping for single quotes
            escaped = value.replace("'", "''")
            return f"'{escaped}'"
        elif isinstance(value, (int, float)):
            return str(value)
        elif value is None:
            return "NULL"
        else:
            return f"'{str(value)}'"
