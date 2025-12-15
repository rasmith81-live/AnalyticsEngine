
from typing import Dict, Any, List, Optional, Tuple
import re

class QueryBuilder:
    """
    Secure SQL Query Builder for Ad-Hoc Queries.
    Converts high-level API parameters into secure SQLAlchemy text objects.
    """

    ALLOWED_OPERATORS = {
        'eq': '=',
        'neq': '!=',
        'gt': '>',
        'gte': '>=',
        'lt': '<',
        'lte': '<=',
        'like': 'LIKE',
        'ilike': 'ILIKE'
    }

    def __init__(self):
        pass

    def build_select(
        self,
        table_name: str,
        columns: List[str] = None,
        filters: List[Dict[str, Any]] = None,
        time_range: Dict[str, Any] = None,
        group_by: List[str] = None,
        order_by: str = None,
        order_direction: str = "DESC",
        limit: int = 100,
        offset: int = 0
    ) -> Tuple[str, Dict[str, Any]]:
        """
        Builds a SELECT query string and parameters dictionary.
        
        Args:
            table_name: Name of the table to query.
            columns: List of columns to select. Defaults to "*".
            filters: List of filter dictionaries.
                     Format: {"field": "col", "op": "eq", "value": "val"}
            time_range: Dict with 'start' and 'end' keys and 'column' key.
            group_by: List of columns to group by.
            order_by: Column to order by.
            order_direction: "ASC" or "DESC".
            limit: Limit of rows.
            offset: Offset of rows.
            
        Returns:
            Tuple containing (sql_string, parameters_dict)
        """
        # 1. Validate Table Name (Simple check to prevent injection)
        if not re.match(r'^[a-zA-Z0-9_.]+$', table_name):
            raise ValueError("Invalid table name")

        params = {}
        
        # 2. Select Clause
        if columns:
            # Validate columns
            for col in columns:
                if not re.match(r'^[a-zA-Z0-9_.*()]+$', col):
                    raise ValueError(f"Invalid column name: {col}")
            select_clause = ", ".join(columns)
        else:
            select_clause = "*"
            
        sql = [f"SELECT {select_clause} FROM {table_name}"]
        where_conditions = []

        # 3. Filters
        if filters:
            for idx, f in enumerate(filters):
                field = f.get('field')
                op = f.get('op', 'eq')
                value = f.get('value')
                
                if not re.match(r'^[a-zA-Z0-9_.]+$', field):
                    raise ValueError(f"Invalid field name: {field}")
                
                if op not in self.ALLOWED_OPERATORS:
                    raise ValueError(f"Unsupported operator: {op}")
                
                param_name = f"filter_{idx}"
                operator = self.ALLOWED_OPERATORS[op]
                
                where_conditions.append(f"{field} {operator} :{param_name}")
                params[param_name] = value

        # 4. Time Range
        if time_range:
            start = time_range.get('start')
            end = time_range.get('end')
            time_col = time_range.get('column', 'timestamp')
            
            if not re.match(r'^[a-zA-Z0-9_.]+$', time_col):
                raise ValueError(f"Invalid time column: {time_col}")

            if start:
                where_conditions.append(f"{time_col} >= :time_start")
                params['time_start'] = start
            if end:
                where_conditions.append(f"{time_col} <= :time_end")
                params['time_end'] = end

        if where_conditions:
            sql.append("WHERE " + " AND ".join(where_conditions))

        # 5. Group By
        if group_by:
            for col in group_by:
                if not re.match(r'^[a-zA-Z0-9_.]+$', col):
                    raise ValueError(f"Invalid group column: {col}")
            sql.append("GROUP BY " + ", ".join(group_by))

        # 6. Order By
        if order_by:
            if not re.match(r'^[a-zA-Z0-9_.]+$', order_by):
                raise ValueError(f"Invalid order column: {order_by}")
            
            direction = order_direction.upper()
            if direction not in ['ASC', 'DESC']:
                direction = 'DESC'
            
            sql.append(f"ORDER BY {order_by} {direction}")

        # 7. Limit/Offset
        sql.append("LIMIT :limit OFFSET :offset")
        params['limit'] = limit
        params['offset'] = offset

        return " ".join(sql), params
