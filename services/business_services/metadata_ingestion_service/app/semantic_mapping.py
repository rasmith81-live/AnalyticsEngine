from typing import Dict, List, Optional, Any, Set
import re

class KPIDecomposer:
    """
    Decomposes KPI formulas and definitions into their component Ontology parts
    (Entities, Attributes) and ensures referential integrity.
    """
    
    # Common words to filter out - not meaningful entities for calculation
    STOP_WORDS: Set[str] = {
        # Math/formula terms
        "sum", "count", "total", "number", "average", "avg", "mean", "median",
        "min", "max", "rate", "ratio", "percent", "percentage", "of", "per",
        "by", "from", "to", "and", "or", "the", "a", "an", "in", "on", "at",
        "for", "with", "as", "is", "are", "was", "were", "be", "been", "being",
        # Generic terms
        "value", "amount", "quantity", "measure", "metric", "kpi", "indicator",
        "time", "period", "date", "current", "previous", "last", "first", 
        "new", "old", "all", "each",
        # Math operators as words
        "plus", "minus", "times", "divided", "multiplied", "equals",
    }
    
    # Time modifiers to replace with generic "period" - makes formulas time-agnostic
    TIME_MODIFIERS: Set[str] = {
        # Duration units
        "second", "seconds", "minute", "minutes", "hour", "hours",
        "day", "days", "daily",
        "week", "weeks", "weekly",
        "month", "months", "monthly",
        "quarter", "quarters", "quarterly",
        "year", "years", "yearly", "annual", "annually",
        # To-date terms (become "Period to Date")
        "ytd", "mtd", "wtd", "qtd",  # Year/Month/Week/Quarter to date
    }
    
    # Over-period terms that become "Period over Period" (e.g., YoY -> PoP)
    OVER_PERIOD_MODIFIERS: Set[str] = {
        "yoy", "mom", "wow", "qoq",  # Year/Month/Week/Quarter over X
    }

    def __init__(self, entity_resolution_service_url: str):
        self.entity_resolution_url = entity_resolution_service_url

    def normalize_time_modifiers(self, formula: str) -> str:
        """
        Replace all time-specific modifiers with generic 'period' placeholder.
        This makes formulas time-agnostic so they can be applied to any time period.
        
        Examples:
            "Revenue per day" -> "Revenue per period"
            "Monthly Sales" -> "Period Sales"
            "YoY Growth" -> "Period over Period Growth"
            "YTD Revenue" -> "Period to Date Revenue"
        """
        normalized = formula
        
        # First, handle over-period modifiers (YoY -> Period over Period)
        for over_word in self.OVER_PERIOD_MODIFIERS:
            pattern = re.compile(r'\b' + re.escape(over_word) + r'\b', re.IGNORECASE)
            
            def replace_with_pop(match):
                original = match.group(0)
                # Preserve capitalization
                if original[0].isupper():
                    return "Period over Period"
                return "period over period"
            
            normalized = pattern.sub(replace_with_pop, normalized)
        
        # Handle to-date modifiers (YTD -> Period to Date)
        to_date_modifiers = {"ytd", "mtd", "wtd", "qtd"}
        for td_word in to_date_modifiers:
            pattern = re.compile(r'\b' + re.escape(td_word) + r'\b', re.IGNORECASE)
            
            def replace_with_ptd(match):
                original = match.group(0)
                if original[0].isupper():
                    return "Period to Date"
                return "period to date"
            
            normalized = pattern.sub(replace_with_ptd, normalized)
        
        # Handle regular time modifiers (day -> period, days -> periods, monthly -> period)
        # Separate plural and singular forms
        plural_time_words = {"seconds", "minutes", "hours", "days", "weeks", "months", "quarters", "years"}
        regular_time_words = self.TIME_MODIFIERS - to_date_modifiers
        
        for time_word in regular_time_words:
            pattern = re.compile(r'\b' + re.escape(time_word) + r'\b', re.IGNORECASE)
            
            # Determine if this is a plural form
            is_plural = time_word.lower() in plural_time_words
            
            def make_replacement(match, plural=is_plural):
                original = match.group(0)
                # Preserve capitalization and plurality
                if plural:
                    return "Periods" if original[0].isupper() else "periods"
                else:
                    return "Period" if original[0].isupper() else "period"
            
            normalized = pattern.sub(make_replacement, normalized)
        
        return normalized

    async def decompose_formula(self, formula: str) -> Dict[str, Any]:
        """
        Parses a formula string (e.g., "(Revenue - Cost) / Revenue") into
        required entities/attributes for calculation.
        
        Extracts meaningful business entities, filtering out common terms.
        Also normalizes time modifiers to generic 'period' for time-agnostic definitions.
        """
        # First, normalize time modifiers
        normalized_formula = self.normalize_time_modifiers(formula)
        
        entities = set()
        
        # Pattern 1: Entity.Attribute notation (e.g., "Order.Revenue", "Customer.Count")
        entity_attr_matches = re.findall(r'\b([A-Z][a-zA-Z]+)\.([A-Z][a-zA-Z]+)\b', normalized_formula)
        for entity, attr in entity_attr_matches:
            entities.add(entity)
        
        # Pattern 2: "X of Y" patterns (e.g., "Number of Customers", "Total Sales")
        of_pattern_matches = re.findall(r'(?:Number|Count|Total|Sum|Average)\s+of\s+([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)?)', normalized_formula, re.IGNORECASE)
        for match in of_pattern_matches:
            # Take the main noun (last capitalized word)
            words = match.split()
            for word in words:
                if word[0].isupper() and word.lower() not in self.STOP_WORDS:
                    entities.add(word)
        
        # Pattern 3: Capitalized words (likely business entities)
        capitalized = re.findall(r'\b([A-Z][a-z]+(?:[A-Z][a-z]+)*)\b', normalized_formula)
        for word in capitalized:
            if word.lower() not in self.STOP_WORDS and len(word) > 2:
                entities.add(word)
        
        # Pattern 4: Multi-word terms in quotes or parentheses
        quoted = re.findall(r'["\']([^"\']+)["\']', normalized_formula)
        for phrase in quoted:
            words = phrase.split()
            for word in words:
                if word[0].isupper() if word else False:
                    if word.lower() not in self.STOP_WORDS:
                        entities.add(word)
        
        # Convert to sorted list for consistent output
        result_entities = sorted(list(entities))
        
        return {
            "original_formula": formula,
            "normalized_formula": normalized_formula,
            "identified_attributes": result_entities,
            "status": "resolved" if result_entities else "no_entities_found"
        }

    async def resolve_components(self, attributes: List[str]) -> Dict[str, str]:
        """
        Calls Entity Resolution Service to map attributes to canonical Entity.Attribute IDs.
        """
        resolved_map = {}
        for attr in attributes:
            # Placeholder for external service call
            # response = await requests.post(f"{self.entity_resolution_url}/resolve", json={"term": attr})
            resolved_map[attr] = f"Canonical_{attr}" # Mock resolution
            
        return resolved_map

    async def validate_integrity(self, decomposed_kpi: Dict[str, Any]) -> bool:
        """
        Ensures all components map to valid objects in the Ontology.
        """
        return True # Placeholder
