from typing import Any, Dict, List
import pandas as pd

class TransformationEngine:
    """
    Handles conditional mapping and data refinement using SQL-like expressions
    or sandboxed Python scripts.
    """

    async def apply_transformations(self, df: pd.DataFrame, rules: List[Dict[str, Any]]) -> pd.DataFrame:
        """
        Applies a sequence of transformation rules to a Pandas DataFrame.
        """
        for rule in rules:
            if rule['type'] == 'sql_expression':
                df = self._apply_sql_expression(df, rule)
            elif rule['type'] == 'python_script':
                df = self._apply_python_script(df, rule)
        
        return df

    def _apply_sql_expression(self, df: pd.DataFrame, rule: Dict[str, Any]) -> pd.DataFrame:
        """
        Uses pandas 'eval' or 'query' to mimic SQL behavior.
        Example: target_col = "CONCAT(col1, col2)"
        """
        target_col = rule['target_column']
        expression = rule['expression']
        
        # Simple mappings
        # In a real engine, we'd use a parser to translate SQL CASE WHEN to numpy.select
        try:
            df[target_col] = df.eval(expression)
        except Exception as e:
            print(f"Transformation Error: {e}")
            
        return df

    def _apply_python_script(self, df: pd.DataFrame, rule: Dict[str, Any]) -> pd.DataFrame:
        """
        Executes a custom Python script.
        WARNING: Needs strict sandboxing in production (e.g., Pyodide/WASM).
        """
        script = rule['script']
        local_scope = {"df": df}
        
        try:
            exec(script, {}, local_scope)
            return local_scope['df']
        except Exception as e:
            print(f"Script Error: {e}")
            return df
