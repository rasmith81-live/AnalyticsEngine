from typing import Dict, Any
import ast

class SQLGenerator:
    """
    Compiles Abstract Syntax Trees (AST) into optimized TimescaleDB SQL queries.
    """
    
    def generate_query(self, parsed_formula: Dict[str, Any], table_name: str, group_by: str = None, approximate: bool = False, bucket_interval: str = '1 day') -> str:
        """
        Generates a SELECT query for the given formula.
        
        Args:
            parsed_formula: Output from FormulaParser
            table_name: Target table name
            group_by: Column(s) to group by
            approximate: Whether to use approximate aggregation functions
            bucket_interval: Time bucket interval (e.g., '1 hour', '1 day')
        """
        self.use_approximate = approximate
        formula_ast = parsed_formula['ast']
        sql_expression = self._ast_to_sql(formula_ast.body)
        
        query = f"SELECT time_bucket('{bucket_interval}', time) as bucket, {sql_expression} as value FROM {table_name}"
        
        if group_by:
            query += f" GROUP BY bucket, {group_by}"
        else:
            query += " GROUP BY bucket"
            
        return query

    def _ast_to_sql(self, node: ast.AST) -> str:
        """
        Recursively converts AST nodes to SQL string fragments.
        """
        if isinstance(node, ast.BinOp):
            left = self._ast_to_sql(node.left)
            right = self._ast_to_sql(node.right)
            op = self._map_operator(node.op)
            return f"({left} {op} {right})"
        
        elif isinstance(node, ast.Call):
            # Handle function calls
            func_name = node.func.id.lower()
            args = [self._ast_to_sql(arg) for arg in node.args]
            
            if func_name == "count_distinct":
                if len(args) != 1:
                    raise ValueError("count_distinct takes exactly 1 argument")
                
                if self.use_approximate:
                    return f"approx_count_distinct({args[0]})"
                else:
                    return f"COUNT(DISTINCT {args[0]})"
            
            elif func_name == "percentile":
                if len(args) != 2:
                    raise ValueError("percentile takes exactly 2 arguments (column, percentile)")
                
                if self.use_approximate:
                    # TimescaleDB Toolkit / UDDSketch or t-digest
                    return f"approx_percentile({args[0]}, {args[1]})"
                else:
                    # Standard Postgres
                    return f"percentile_cont({args[1]}) WITHIN GROUP (ORDER BY {args[0]})"
                
            elif func_name == "approx_distinct":
                # Explicit approximate call
                if len(args) != 1:
                    raise ValueError("approx_distinct takes exactly 1 argument")
                return f"approx_count_distinct({args[0]})"
                
            elif func_name in ["last", "first"]:
                if len(args) != 2:
                    raise ValueError(f"{func_name} takes exactly 2 arguments (value, time_column)")
                return f"{func_name.upper()}({args[0]}, {args[1]})"

            elif func_name in ["sum", "avg", "min", "max", "count"]:
                if len(args) != 1:
                    raise ValueError(f"{func_name} takes exactly 1 argument")
                return f"{func_name.upper()}({args[0]})"
            
            else:
                raise ValueError(f"Unsupported function: {func_name}")

        elif isinstance(node, ast.Name):
            # In a real engine, we'd look up the column name from a mapping
            # e.g., 'Revenue' -> 'revenue_amt'
            # If used inside a function call, it returns the column name
            # If used standalone (implicit aggregation), default to SUM? 
            # Better to require explicit aggregation in formulas or handle contextually.
            # For now, returning column name directly to let parent Call node handle it,
            # or default to SUM if top level (handled in generate_query if needed, 
            # but usually formulas like "Revenue / Cost" imply SUM(Revenue) / SUM(Cost) 
            # OR row-level calc then SUM.
            # Let's assume the AST structure handles aggregation explicitly for now
            # or names refer to pre-aggregated metrics.
            return node.id 
            
        elif isinstance(node, ast.Constant):
            return str(node.value)
            
        raise ValueError(f"Unsupported AST node: {type(node)}")

    def _map_operator(self, op: ast.operator) -> str:
        if isinstance(op, ast.Add): return "+"
        if isinstance(op, ast.Sub): return "-"
        if isinstance(op, ast.Mult): return "*"
        if isinstance(op, ast.Div): return "/"
        return "+"
