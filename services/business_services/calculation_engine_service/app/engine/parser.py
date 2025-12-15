import ast
from typing import List, Set, Any, Dict

class FormulaParser:
    """
    Parses string-based KPI formulas into structured ASTs.
    Example: "(Revenue - Cost) / Revenue" -> Division(Subtraction(Ref('Revenue'), Ref('Cost')), Ref('Revenue'))
    """
    
    def parse(self, formula: str) -> Dict[str, Any]:
        """
        Parses formula and returns metadata about required variables.
        """
        try:
            tree = ast.parse(formula, mode='eval')
            variables = self._extract_variables(tree)
            return {
                "ast": tree,
                "variables": list(variables),
                "original": formula
            }
        except SyntaxError as e:
            raise ValueError(f"Invalid formula syntax: {e}")

    def _extract_variables(self, tree: ast.AST) -> Set[str]:
        variables = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                variables.add(node.id)
        return variables
