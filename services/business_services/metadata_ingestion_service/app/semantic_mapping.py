from typing import Dict, List, Optional, Any, Set, Tuple
import re
import logging
import sys
import os

from .formula_parser import parse_formula_to_math

logger = logging.getLogger(__name__)

# Lazy-loaded spaCy NLP model (loaded on first use)
_nlp = None
_spacy_initialized = False


def _get_nlp():
    """Lazy-load spaCy NLP model on first use."""
    global _nlp, _spacy_initialized
    
    if _spacy_initialized:
        return _nlp
    
    _spacy_initialized = True
    
    # Ensure user-installed packages are in path
    _user_site = os.path.expanduser("~/.local/lib/python3.11/site-packages")
    if _user_site not in sys.path:
        sys.path.insert(0, _user_site)
    
    try:
        import spacy
        # Try direct module import first (more reliable for pip-installed models)
        try:
            import en_core_web_lg
            _nlp = en_core_web_lg.load()
            logger.info("spaCy LARGE model loaded successfully via direct module import")
        except ImportError:
            # Fall back to spacy.load()
            try:
                _nlp = spacy.load("en_core_web_lg")
                logger.info("spaCy LARGE model loaded successfully via spacy.load()")
            except OSError as e:
                logger.warning(f"spaCy model not found: {e}")
                _nlp = None
    except ImportError as e:
        logger.warning(f"spaCy not available: {e}, using regex-based noun extraction")
        _nlp = None
    
    return _nlp


class KPIDecomposer:
    """
    Decomposes KPI formulas and definitions into their component Ontology parts
    (Entities, Attributes) and ensures referential integrity.
    
    Uses spaCy NLP for accurate noun extraction without requiring OpenAI.
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
        "new", "old", "all", "each", "end", "start", "beginning",
        # Math operators as words
        "plus", "minus", "times", "divided", "multiplied", "equals",
        # Common non-entity words
        "growth", "change", "difference", "comparison", "result",
        # Measure/attribute words - these are properties, not entities
        "score", "scores", "rating", "ratings", "level", "levels",
        "index", "factor", "coefficient", "weight", "cost", "costs",
        "price", "prices", "margin", "margins",
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
    
    # Mathematical operation keywords to convert to symbols
    MATH_KEYWORDS: Dict[str, str] = {
        "divided by": "/",
        "multiplied by": "*",
        "times": "*",
        "plus": "+",
        "minus": "-",
        "less": "-",
        "over": "/",
        "per": "/",
    }

    def __init__(self, entity_resolution_service_url: str):
        self.entity_resolution_url = entity_resolution_service_url
        self._nlp_loaded = False

    @property
    def nlp(self):
        """Lazy-load spaCy NLP model on first access."""
        if not self._nlp_loaded:
            self._nlp_loaded = True
        return _get_nlp()

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

    # Common adjective suffixes - words ending in these are likely adjectives, not entities
    ADJECTIVE_SUFFIXES: tuple = (
        "ant", "ent",  # compliant, dependent
        "ive", "ative", "itive",  # active, creative
        "ous", "ious", "eous",  # various, precious
        "ful", "less",  # helpful, helpless
        "able", "ible",  # available, visible
        "al", "ial", "ical",  # total, financial (but not "capital" which is a noun)
        "ed",  # completed, approved
        "ing",  # pending, running
    )
    
    # Words that end in adjective suffixes but ARE actually nouns
    NOUN_EXCEPTIONS: Set[str] = {
        "capital", "principal", "terminal", "material", "potential",
        "credential", "differential", "essential", "ential",
        "agent", "client", "patient", "student", "parent",
        "event", "segment", "element", "document", "payment",
        "native", "representative", "executive", "objective",
        "inventory", "category", "territory",
    }

    def _is_likely_adjective(self, word: str) -> bool:
        """Check if a word is likely an adjective based on its suffix."""
        word_lower = word.lower()
        # Check if it's a known noun exception
        if word_lower in self.NOUN_EXCEPTIONS:
            return False
        # Check adjective suffixes
        for suffix in self.ADJECTIVE_SUFFIXES:
            if word_lower.endswith(suffix) and len(word_lower) > len(suffix) + 2:
                return True
        return False

    def _singularize(self, word: str) -> str:
        """
        Convert a plural noun to singular form.
        Simple rule-based approach since spaCy's lemmatization can be unreliable.
        """
        word_lower = word.lower()
        
        # Common irregular plurals
        irregulars = {
            "children": "child", "people": "person", "men": "man", "women": "woman",
            "feet": "foot", "teeth": "tooth", "geese": "goose", "mice": "mouse",
            "data": "datum", "criteria": "criterion", "analyses": "analysis",
        }
        if word_lower in irregulars:
            return irregulars[word_lower].title()
        
        # Words ending in 'ies' -> 'y' (e.g., categories -> category)
        if word_lower.endswith("ies") and len(word_lower) > 4:
            return (word_lower[:-3] + "y").title()
        
        # Words ending in 'es' after s, x, z, ch, sh -> remove 'es'
        if word_lower.endswith("es") and len(word_lower) > 3:
            if word_lower[-3] in "sxz" or word_lower[-4:-2] in ("ch", "sh"):
                return word_lower[:-2].title()
        
        # Words ending in 'us' are typically Latin singular (status, radius, census, etc.)
        if word_lower.endswith("us"):
            return word.title()
        
        # Words ending in 's' -> remove 's' (most common case)
        if word_lower.endswith("s") and not word_lower.endswith("ss") and len(word_lower) > 3:
            return word_lower[:-1].title()
        
        return word.title()

    def _clean_noun_phrase(self, tokens: list) -> str:
        """
        Clean a noun phrase by filtering stop words and singularizing.
        Returns the cleaned phrase or empty string.
        """
        meaningful_words = []
        for token in tokens:
            # Only include nouns and proper nouns
            if token.pos_ not in ("NOUN", "PROPN"):
                continue
            word_lower = token.text.lower()
            # Skip stop words and short words
            if word_lower in self.STOP_WORDS or len(word_lower) <= 2:
                continue
            # Skip likely adjectives
            if self._is_likely_adjective(word_lower):
                continue
            # Singularize and add
            meaningful_words.append(self._singularize(token.text))
        
        return " ".join(meaningful_words)

    def extract_nouns_with_spacy(self, text: str) -> List[str]:
        """
        Extract business entity noun phrases from text using spaCy NLP.
        
        Uses the LARGE spaCy model for better noun phrase detection.
        Extracts FULL NOUN PHRASES as business entities (e.g., "Audit Category").
        
        Key approach:
        - Split on math operators first to isolate noun phrases
        - Normalize underscores to spaces for consistent parsing
        - Extract noun chunks as complete business entities
        - Filter out stop words and measure words from phrases
        - Singularize words for canonical entity names
        """
        if not self.nlp or not text:
            return []
        
        entities = set()
        
        # Normalize: replace underscores with spaces for better NLP parsing
        normalized_text = text.replace('_', ' ')
        
        # Split on math operators to isolate noun phrases
        # This prevents spaCy from treating "A / B" as one chunk
        segments = re.split(r'[\+\-\*\/\(\)\=\<\>\,]', normalized_text)
        
        for segment in segments:
            segment = segment.strip()
            if not segment:
                continue
                
            doc = self.nlp(segment)
            
            # Extract noun chunks as business entities
            for chunk in doc.noun_chunks:
                # Clean the noun phrase (filter stop words, singularize)
                cleaned_phrase = self._clean_noun_phrase(list(chunk))
                if cleaned_phrase:
                    entities.add(cleaned_phrase)
        
        return sorted(list(entities))
    
    def extract_nouns_regex(self, text: str) -> List[str]:
        """
        Fallback regex-based noun extraction when spaCy is not available.
        """
        nouns = set()
        
        # Pattern 1: Capitalized words (likely proper nouns/entities)
        capitalized = re.findall(r'\b([A-Z][a-z]+(?:[A-Z][a-z]+)*)\b', text)
        for word in capitalized:
            if word.lower() not in self.STOP_WORDS and len(word) > 2:
                nouns.add(word)
        
        # Pattern 2: Words after "of" (e.g., "Number of Customers")
        of_matches = re.findall(r'\bof\s+([A-Za-z]+)', text, re.IGNORECASE)
        for word in of_matches:
            if word.lower() not in self.STOP_WORDS and len(word) > 2:
                nouns.add(word.title())
        
        # Pattern 3: Entity.Attribute notation
        entity_attr = re.findall(r'\b([A-Z][a-zA-Z]+)\.([A-Z][a-zA-Z]+)\b', text)
        for entity, attr in entity_attr:
            nouns.add(entity)
            nouns.add(attr)
        
        return sorted(list(nouns))
    
    async def decompose_formula(self, formula: str) -> Dict[str, Any]:
        """
        Parses a formula string into a set_based_definition for the calculation engine.
        
        This method:
        1. Normalizes time modifiers to generic 'period' for time-agnostic definitions
        2. Extracts entities using spaCy NLP
        3. Attempts to generate a set_based_definition for complex KPIs
        4. Falls back to simple formula for basic arithmetic expressions
        
        Returns:
            Dict with set_based_definition (for set-based KPIs) or 
            identified_attributes (for simple formulas)
        """
        # First, normalize time modifiers
        normalized_formula = self.normalize_time_modifiers(formula)
        
        # Extract nouns using spaCy (primary) or regex (fallback)
        if self.nlp is not None:
            entities = self.extract_nouns_with_spacy(normalized_formula)
            extraction_method = "spacy"
        else:
            entities = self.extract_nouns_regex(normalized_formula)
            extraction_method = "regex"
        
        # Also extract using regex patterns for Entity.Attribute notation
        entity_attr_matches = re.findall(r'\b([A-Z][a-zA-Z]+)\.([A-Z][a-zA-Z]+)\b', normalized_formula)
        for entity, attr in entity_attr_matches:
            if entity not in entities:
                entities.append(entity)
            if attr not in entities:
                entities.append(attr)
        
        # Sort for consistent output
        entities = sorted(set(entities))
        
        # Try to generate set_based_definition for complex KPIs
        set_based_definition = None
        try:
            set_based_definition = self._try_generate_set_based_definition(
                formula=normalized_formula,
                entities=entities
            )
        except Exception as e:
            logger.debug(f"Set-based definition generation failed: {e}")
        
        if set_based_definition:
            logger.info(f"Formula decomposed to set_based_definition: '{formula}' -> {len(set_based_definition.get('steps', []))} steps")
            return {
                "original_formula": formula,
                "normalized_formula": normalized_formula,
                "set_based_definition": set_based_definition,
                "identified_attributes": entities,
                "extraction_method": extraction_method,
                "status": "set_based"
            }
        
        # Fall back to simple formula parsing
        math_expression = parse_formula_to_math(normalized_formula, entities)
        
        logger.info(f"Formula decomposition ({extraction_method}): '{formula}' -> entities={entities}")
        
        return {
            "original_formula": formula,
            "normalized_formula": normalized_formula,
            "identified_attributes": entities,
            "extraction_method": extraction_method,
            "status": "resolved" if entities else "no_entities_found"
        }
    
    def _try_generate_set_based_definition(
        self,
        formula: str,
        entities: List[str]
    ) -> Optional[Dict[str, Any]]:
        """
        Try to generate a set_based_definition for complex KPI formulas.
        
        Detects patterns like:
        - Churn Rate: (Lost / Start) * 100
        - Retention Rate: (Retained / Start) * 100
        - Growth Rate: (New / Start) * 100
        - Period-over-Period: (Current - Previous) / Previous * 100
        - Conversion Rate: (Converted / Total) * 100
        - Net Change: End - Start
        - Active Count: Count of active entities at a point in time
        
        Returns None if the formula doesn't match a known set-based pattern.
        """
        formula_lower = formula.lower()
        
        # Common entity candidates for all patterns
        entity_candidates = ["customer", "policy", "subscription", "user", "member", "account", "client"]
        transaction_candidates = ["order", "sale", "transaction", "deal", "lead", "opportunity"]
        
        # 1. Detect churn rate pattern
        churn_indicators = ["churn", "lost", "cancelled", "terminated", "left", "departed", "attrition"]
        if any(ind in formula_lower for ind in churn_indicators):
            base_entity = self._infer_base_entity(entities, entity_candidates)
            if base_entity:
                return self._build_churn_definition(base_entity, entities)
        
        # 2. Detect retention rate pattern
        retention_indicators = ["retain", "kept", "stayed", "remained", "continuing", "loyalty"]
        if any(ind in formula_lower for ind in retention_indicators):
            base_entity = self._infer_base_entity(entities, entity_candidates)
            if base_entity:
                return self._build_retention_definition(base_entity, entities)
        
        # 3. Detect growth rate pattern
        growth_indicators = ["growth", "new", "acquired", "gained", "added"]
        if any(ind in formula_lower for ind in growth_indicators) and "rate" in formula_lower:
            base_entity = self._infer_base_entity(entities, entity_candidates)
            if base_entity:
                return self._build_growth_definition(base_entity, entities)
        
        # 4. Detect Period-over-Period (PoP) pattern - YoY, MoM, WoW, QoQ
        pop_indicators = ["period over period", "year over year", "month over month", 
                         "week over week", "quarter over quarter", "yoy", "mom", "wow", "qoq",
                         "compared to previous", "vs previous", "versus last"]
        if any(ind in formula_lower for ind in pop_indicators):
            # Try entity-based PoP first
            base_entity = self._infer_base_entity(entities, entity_candidates)
            if base_entity:
                return self._build_pop_count_definition(base_entity, entities)
            # Try transaction-based PoP (for revenue, sales)
            base_entity = self._infer_base_entity(entities, transaction_candidates)
            if base_entity:
                return self._build_pop_sum_definition(base_entity, entities)
        
        # 5. Detect Conversion Rate pattern
        conversion_indicators = ["conversion", "converted", "convert", "funnel", "win rate", 
                                "close rate", "success rate", "completion rate"]
        if any(ind in formula_lower for ind in conversion_indicators):
            # Conversion typically involves leads/opportunities -> deals/customers
            source_entity = self._infer_base_entity(entities, ["lead", "opportunity", "prospect", "visitor"])
            target_entity = self._infer_base_entity(entities, ["customer", "deal", "sale", "conversion", "won"])
            if source_entity:
                return self._build_conversion_definition(source_entity, target_entity, entities)
        
        # 6. Detect Net Change pattern
        net_change_indicators = ["net change", "net growth", "net increase", "net decrease", 
                                "difference", "delta", "change in"]
        if any(ind in formula_lower for ind in net_change_indicators):
            base_entity = self._infer_base_entity(entities, entity_candidates)
            if base_entity:
                return self._build_net_change_definition(base_entity, entities)
        
        # 7. Detect Active/Current Count pattern
        active_indicators = ["active", "current", "existing", "total", "count of", "number of"]
        if any(ind in formula_lower for ind in active_indicators) and not any(x in formula_lower for x in ["rate", "ratio", "percent"]):
            base_entity = self._infer_base_entity(entities, entity_candidates)
            if base_entity:
                return self._build_active_count_definition(base_entity, entities)
        
        # 8. Detect Ratio/Percentage pattern (generic A/B * 100)
        ratio_indicators = ["ratio", "percentage", "percent of", "proportion", "share"]
        if any(ind in formula_lower for ind in ratio_indicators):
            base_entity = self._infer_base_entity(entities, entity_candidates + transaction_candidates)
            if base_entity:
                return self._build_ratio_definition(base_entity, entities, formula_lower)
        
        return None
    
    def _infer_base_entity(self, entities: List[str], candidates: List[str]) -> Optional[str]:
        """Infer the base entity from extracted entities."""
        for entity in entities:
            entity_lower = entity.lower()
            for candidate in candidates:
                if candidate in entity_lower:
                    return entity_lower + "s"  # Pluralize for table name
        return None
    
    def _build_churn_definition(self, base_entity: str, entities: List[str]) -> Dict[str, Any]:
        """Build set_based_definition for churn rate."""
        key_col = f"{base_entity.rstrip('s')}_id"
        return {
            "base_entity": base_entity,
            "key_column": key_col,
            "period_parameters": ["PeriodStart", "PeriodEnd"],
            "steps": [
                {
                    "step_number": 1,
                    "name": "StartPeriodSet",
                    "description": f"All {base_entity} active at the start of the period",
                    "set_definition": {
                        "name": "StartPeriodSet",
                        "base_entity": base_entity,
                        "key_column": key_col,
                        "filter_conditions": {
                            "conditions": [
                                {"column": "active_date", "operator": "LE", "value": "@PeriodStart"},
                                {
                                    "conditions": [
                                        {"column": "inactive_date", "operator": "IS_NULL"},
                                        {"column": "inactive_date", "operator": "GE", "value": "@PeriodStart"}
                                    ],
                                    "logical_operator": "OR"
                                }
                            ],
                            "logical_operator": "AND"
                        }
                    }
                },
                {
                    "step_number": 2,
                    "name": "EndPeriodSet",
                    "description": f"All {base_entity} active at the end of the period",
                    "set_definition": {
                        "name": "EndPeriodSet",
                        "base_entity": base_entity,
                        "key_column": key_col,
                        "filter_conditions": {
                            "conditions": [
                                {"column": "active_date", "operator": "LE", "value": "@PeriodEnd"},
                                {
                                    "conditions": [
                                        {"column": "inactive_date", "operator": "IS_NULL"},
                                        {"column": "inactive_date", "operator": "GE", "value": "@PeriodEnd"}
                                    ],
                                    "logical_operator": "OR"
                                }
                            ],
                            "logical_operator": "AND"
                        }
                    }
                },
                {
                    "step_number": 3,
                    "name": "LostDuringPeriodSet",
                    "description": f"{base_entity} who were active at start but not at end",
                    "set_definition": {
                        "name": "LostDuringPeriodSet",
                        "operation": "EXCEPT",
                        "source_sets": ["StartPeriodSet", "EndPeriodSet"],
                        "key_column": key_col
                    }
                },
                {
                    "step_number": 4,
                    "name": "StartCount",
                    "description": "Count of starting set",
                    "aggregation": {
                        "name": "StartCount",
                        "set_name": "StartPeriodSet",
                        "aggregation_type": "COUNTROWS"
                    }
                },
                {
                    "step_number": 5,
                    "name": "LostCount",
                    "description": "Count of lost set",
                    "aggregation": {
                        "name": "LostCount",
                        "set_name": "LostDuringPeriodSet",
                        "aggregation_type": "COUNTROWS"
                    }
                }
            ],
            "final_formula": "CASE WHEN StartCount > 0 THEN (LostCount::float / StartCount::float) * 100 ELSE 0 END"
        }
    
    def _build_retention_definition(self, base_entity: str, entities: List[str]) -> Dict[str, Any]:
        """Build set_based_definition for retention rate."""
        key_col = f"{base_entity.rstrip('s')}_id"
        return {
            "base_entity": base_entity,
            "key_column": key_col,
            "period_parameters": ["PeriodStart", "PeriodEnd"],
            "steps": [
                {
                    "step_number": 1,
                    "name": "StartPeriodSet",
                    "description": f"All {base_entity} active at the start of the period",
                    "set_definition": {
                        "name": "StartPeriodSet",
                        "base_entity": base_entity,
                        "key_column": key_col,
                        "filter_conditions": {
                            "conditions": [
                                {"column": "active_date", "operator": "LE", "value": "@PeriodStart"},
                                {
                                    "conditions": [
                                        {"column": "inactive_date", "operator": "IS_NULL"},
                                        {"column": "inactive_date", "operator": "GE", "value": "@PeriodStart"}
                                    ],
                                    "logical_operator": "OR"
                                }
                            ],
                            "logical_operator": "AND"
                        }
                    }
                },
                {
                    "step_number": 2,
                    "name": "EndPeriodSet",
                    "description": f"All {base_entity} active at the end of the period",
                    "set_definition": {
                        "name": "EndPeriodSet",
                        "base_entity": base_entity,
                        "key_column": key_col,
                        "filter_conditions": {
                            "conditions": [
                                {"column": "active_date", "operator": "LE", "value": "@PeriodEnd"},
                                {
                                    "conditions": [
                                        {"column": "inactive_date", "operator": "IS_NULL"},
                                        {"column": "inactive_date", "operator": "GE", "value": "@PeriodEnd"}
                                    ],
                                    "logical_operator": "OR"
                                }
                            ],
                            "logical_operator": "AND"
                        }
                    }
                },
                {
                    "step_number": 3,
                    "name": "RetainedSet",
                    "description": f"{base_entity} who were active at both start and end",
                    "set_definition": {
                        "name": "RetainedSet",
                        "operation": "INTERSECT",
                        "source_sets": ["StartPeriodSet", "EndPeriodSet"],
                        "key_column": key_col
                    }
                },
                {
                    "step_number": 4,
                    "name": "StartCount",
                    "description": "Count of starting set",
                    "aggregation": {
                        "name": "StartCount",
                        "set_name": "StartPeriodSet",
                        "aggregation_type": "COUNTROWS"
                    }
                },
                {
                    "step_number": 5,
                    "name": "RetainedCount",
                    "description": "Count of retained set",
                    "aggregation": {
                        "name": "RetainedCount",
                        "set_name": "RetainedSet",
                        "aggregation_type": "COUNTROWS"
                    }
                }
            ],
            "final_formula": "CASE WHEN StartCount > 0 THEN (RetainedCount::float / StartCount::float) * 100 ELSE 0 END"
        }
    
    def _build_growth_definition(self, base_entity: str, entities: List[str]) -> Dict[str, Any]:
        """Build set_based_definition for growth rate."""
        key_col = f"{base_entity.rstrip('s')}_id"
        return {
            "base_entity": base_entity,
            "key_column": key_col,
            "period_parameters": ["PeriodStart", "PeriodEnd"],
            "steps": [
                {
                    "step_number": 1,
                    "name": "StartPeriodSet",
                    "description": f"All {base_entity} active at the start of the period",
                    "set_definition": {
                        "name": "StartPeriodSet",
                        "base_entity": base_entity,
                        "key_column": key_col,
                        "filter_conditions": {
                            "conditions": [
                                {"column": "active_date", "operator": "LE", "value": "@PeriodStart"},
                                {
                                    "conditions": [
                                        {"column": "inactive_date", "operator": "IS_NULL"},
                                        {"column": "inactive_date", "operator": "GE", "value": "@PeriodStart"}
                                    ],
                                    "logical_operator": "OR"
                                }
                            ],
                            "logical_operator": "AND"
                        }
                    }
                },
                {
                    "step_number": 2,
                    "name": "NewDuringPeriodSet",
                    "description": f"New {base_entity} acquired during the period",
                    "set_definition": {
                        "name": "NewDuringPeriodSet",
                        "base_entity": base_entity,
                        "key_column": key_col,
                        "filter_conditions": {
                            "conditions": [
                                {"column": "active_date", "operator": "GT", "value": "@PeriodStart"},
                                {"column": "active_date", "operator": "LE", "value": "@PeriodEnd"}
                            ],
                            "logical_operator": "AND"
                        }
                    }
                },
                {
                    "step_number": 3,
                    "name": "StartCount",
                    "description": "Count of starting set",
                    "aggregation": {
                        "name": "StartCount",
                        "set_name": "StartPeriodSet",
                        "aggregation_type": "COUNTROWS"
                    }
                },
                {
                    "step_number": 4,
                    "name": "NewCount",
                    "description": "Count of new set",
                    "aggregation": {
                        "name": "NewCount",
                        "set_name": "NewDuringPeriodSet",
                        "aggregation_type": "COUNTROWS"
                    }
                }
            ],
            "final_formula": "CASE WHEN StartCount > 0 THEN (NewCount::float / StartCount::float) * 100 ELSE 0 END"
        }
    
    def _build_pop_count_definition(self, base_entity: str, entities: List[str]) -> Dict[str, Any]:
        """
        Build set_based_definition for Period-over-Period count comparison.
        
        Calculates: ((CurrentPeriodCount - PreviousPeriodCount) / PreviousPeriodCount) * 100
        
        Uses @PeriodStart, @PeriodEnd for current period
        Uses @PreviousPeriodStart, @PreviousPeriodEnd for previous period
        """
        key_col = f"{base_entity.rstrip('s')}_id"
        return {
            "base_entity": base_entity,
            "key_column": key_col,
            "period_parameters": ["PeriodStart", "PeriodEnd", "PreviousPeriodStart", "PreviousPeriodEnd"],
            "steps": [
                {
                    "step_number": 1,
                    "name": "CurrentPeriodSet",
                    "description": f"All {base_entity} active during the current period",
                    "set_definition": {
                        "name": "CurrentPeriodSet",
                        "base_entity": base_entity,
                        "key_column": key_col,
                        "filter_conditions": {
                            "conditions": [
                                {"column": "active_date", "operator": "LE", "value": "@PeriodEnd"},
                                {
                                    "conditions": [
                                        {"column": "inactive_date", "operator": "IS_NULL"},
                                        {"column": "inactive_date", "operator": "GE", "value": "@PeriodStart"}
                                    ],
                                    "logical_operator": "OR"
                                }
                            ],
                            "logical_operator": "AND"
                        }
                    }
                },
                {
                    "step_number": 2,
                    "name": "PreviousPeriodSet",
                    "description": f"All {base_entity} active during the previous period",
                    "set_definition": {
                        "name": "PreviousPeriodSet",
                        "base_entity": base_entity,
                        "key_column": key_col,
                        "filter_conditions": {
                            "conditions": [
                                {"column": "active_date", "operator": "LE", "value": "@PreviousPeriodEnd"},
                                {
                                    "conditions": [
                                        {"column": "inactive_date", "operator": "IS_NULL"},
                                        {"column": "inactive_date", "operator": "GE", "value": "@PreviousPeriodStart"}
                                    ],
                                    "logical_operator": "OR"
                                }
                            ],
                            "logical_operator": "AND"
                        }
                    }
                },
                {
                    "step_number": 3,
                    "name": "CurrentCount",
                    "description": "Count of current period set",
                    "aggregation": {
                        "name": "CurrentCount",
                        "set_name": "CurrentPeriodSet",
                        "aggregation_type": "COUNTROWS"
                    }
                },
                {
                    "step_number": 4,
                    "name": "PreviousCount",
                    "description": "Count of previous period set",
                    "aggregation": {
                        "name": "PreviousCount",
                        "set_name": "PreviousPeriodSet",
                        "aggregation_type": "COUNTROWS"
                    }
                }
            ],
            "final_formula": "CASE WHEN PreviousCount > 0 THEN ((CurrentCount::float - PreviousCount::float) / PreviousCount::float) * 100 ELSE 0 END"
        }
    
    def _build_pop_sum_definition(self, base_entity: str, entities: List[str]) -> Dict[str, Any]:
        """
        Build set_based_definition for Period-over-Period sum comparison (e.g., Revenue YoY).
        
        Calculates: ((CurrentPeriodSum - PreviousPeriodSum) / PreviousPeriodSum) * 100
        """
        key_col = f"{base_entity.rstrip('s')}_id"
        amount_col = "amount"  # Default amount column
        return {
            "base_entity": base_entity,
            "key_column": key_col,
            "period_parameters": ["PeriodStart", "PeriodEnd", "PreviousPeriodStart", "PreviousPeriodEnd"],
            "steps": [
                {
                    "step_number": 1,
                    "name": "CurrentPeriodSet",
                    "description": f"All {base_entity} in the current period",
                    "set_definition": {
                        "name": "CurrentPeriodSet",
                        "base_entity": base_entity,
                        "key_column": key_col,
                        "filter_conditions": {
                            "conditions": [
                                {"column": "created_at", "operator": "GE", "value": "@PeriodStart"},
                                {"column": "created_at", "operator": "LE", "value": "@PeriodEnd"}
                            ],
                            "logical_operator": "AND"
                        }
                    }
                },
                {
                    "step_number": 2,
                    "name": "PreviousPeriodSet",
                    "description": f"All {base_entity} in the previous period",
                    "set_definition": {
                        "name": "PreviousPeriodSet",
                        "base_entity": base_entity,
                        "key_column": key_col,
                        "filter_conditions": {
                            "conditions": [
                                {"column": "created_at", "operator": "GE", "value": "@PreviousPeriodStart"},
                                {"column": "created_at", "operator": "LE", "value": "@PreviousPeriodEnd"}
                            ],
                            "logical_operator": "AND"
                        }
                    }
                },
                {
                    "step_number": 3,
                    "name": "CurrentSum",
                    "description": "Sum of current period",
                    "aggregation": {
                        "name": "CurrentSum",
                        "set_name": "CurrentPeriodSet",
                        "aggregation_type": "SUMX",
                        "column": amount_col
                    }
                },
                {
                    "step_number": 4,
                    "name": "PreviousSum",
                    "description": "Sum of previous period",
                    "aggregation": {
                        "name": "PreviousSum",
                        "set_name": "PreviousPeriodSet",
                        "aggregation_type": "SUMX",
                        "column": amount_col
                    }
                }
            ],
            "final_formula": "CASE WHEN PreviousSum > 0 THEN ((CurrentSum::float - PreviousSum::float) / PreviousSum::float) * 100 ELSE 0 END"
        }
    
    def _build_conversion_definition(
        self, 
        source_entity: str, 
        target_entity: Optional[str],
        entities: List[str]
    ) -> Dict[str, Any]:
        """
        Build set_based_definition for Conversion Rate.
        
        Calculates: (Converted / Total) * 100
        
        Example: Lead Conversion Rate = (Leads that became Customers / Total Leads) * 100
        """
        key_col = f"{source_entity.rstrip('s')}_id"
        return {
            "base_entity": source_entity,
            "key_column": key_col,
            "period_parameters": ["PeriodStart", "PeriodEnd"],
            "steps": [
                {
                    "step_number": 1,
                    "name": "TotalSet",
                    "description": f"All {source_entity} created during the period",
                    "set_definition": {
                        "name": "TotalSet",
                        "base_entity": source_entity,
                        "key_column": key_col,
                        "filter_conditions": {
                            "conditions": [
                                {"column": "created_at", "operator": "GE", "value": "@PeriodStart"},
                                {"column": "created_at", "operator": "LE", "value": "@PeriodEnd"}
                            ],
                            "logical_operator": "AND"
                        }
                    }
                },
                {
                    "step_number": 2,
                    "name": "ConvertedSet",
                    "description": f"{source_entity} that converted during the period",
                    "set_definition": {
                        "name": "ConvertedSet",
                        "base_entity": source_entity,
                        "key_column": key_col,
                        "filter_conditions": {
                            "conditions": [
                                {"column": "created_at", "operator": "GE", "value": "@PeriodStart"},
                                {"column": "created_at", "operator": "LE", "value": "@PeriodEnd"},
                                {"column": "converted_at", "operator": "IS_NOT_NULL"},
                                {"column": "converted_at", "operator": "LE", "value": "@PeriodEnd"}
                            ],
                            "logical_operator": "AND"
                        }
                    }
                },
                {
                    "step_number": 3,
                    "name": "TotalCount",
                    "description": "Count of total set",
                    "aggregation": {
                        "name": "TotalCount",
                        "set_name": "TotalSet",
                        "aggregation_type": "COUNTROWS"
                    }
                },
                {
                    "step_number": 4,
                    "name": "ConvertedCount",
                    "description": "Count of converted set",
                    "aggregation": {
                        "name": "ConvertedCount",
                        "set_name": "ConvertedSet",
                        "aggregation_type": "COUNTROWS"
                    }
                }
            ],
            "final_formula": "CASE WHEN TotalCount > 0 THEN (ConvertedCount::float / TotalCount::float) * 100 ELSE 0 END"
        }
    
    def _build_net_change_definition(self, base_entity: str, entities: List[str]) -> Dict[str, Any]:
        """
        Build set_based_definition for Net Change.
        
        Calculates: EndCount - StartCount
        
        Can also be expressed as: NewCount - LostCount
        """
        key_col = f"{base_entity.rstrip('s')}_id"
        return {
            "base_entity": base_entity,
            "key_column": key_col,
            "period_parameters": ["PeriodStart", "PeriodEnd"],
            "steps": [
                {
                    "step_number": 1,
                    "name": "StartPeriodSet",
                    "description": f"All {base_entity} active at the start of the period",
                    "set_definition": {
                        "name": "StartPeriodSet",
                        "base_entity": base_entity,
                        "key_column": key_col,
                        "filter_conditions": {
                            "conditions": [
                                {"column": "active_date", "operator": "LE", "value": "@PeriodStart"},
                                {
                                    "conditions": [
                                        {"column": "inactive_date", "operator": "IS_NULL"},
                                        {"column": "inactive_date", "operator": "GE", "value": "@PeriodStart"}
                                    ],
                                    "logical_operator": "OR"
                                }
                            ],
                            "logical_operator": "AND"
                        }
                    }
                },
                {
                    "step_number": 2,
                    "name": "EndPeriodSet",
                    "description": f"All {base_entity} active at the end of the period",
                    "set_definition": {
                        "name": "EndPeriodSet",
                        "base_entity": base_entity,
                        "key_column": key_col,
                        "filter_conditions": {
                            "conditions": [
                                {"column": "active_date", "operator": "LE", "value": "@PeriodEnd"},
                                {
                                    "conditions": [
                                        {"column": "inactive_date", "operator": "IS_NULL"},
                                        {"column": "inactive_date", "operator": "GE", "value": "@PeriodEnd"}
                                    ],
                                    "logical_operator": "OR"
                                }
                            ],
                            "logical_operator": "AND"
                        }
                    }
                },
                {
                    "step_number": 3,
                    "name": "StartCount",
                    "description": "Count at start of period",
                    "aggregation": {
                        "name": "StartCount",
                        "set_name": "StartPeriodSet",
                        "aggregation_type": "COUNTROWS"
                    }
                },
                {
                    "step_number": 4,
                    "name": "EndCount",
                    "description": "Count at end of period",
                    "aggregation": {
                        "name": "EndCount",
                        "set_name": "EndPeriodSet",
                        "aggregation_type": "COUNTROWS"
                    }
                }
            ],
            "final_formula": "EndCount - StartCount"
        }
    
    def _build_active_count_definition(self, base_entity: str, entities: List[str]) -> Dict[str, Any]:
        """
        Build set_based_definition for Active/Current Count.
        
        Calculates: Count of entities active at @PeriodEnd
        """
        key_col = f"{base_entity.rstrip('s')}_id"
        return {
            "base_entity": base_entity,
            "key_column": key_col,
            "period_parameters": ["PeriodEnd"],
            "steps": [
                {
                    "step_number": 1,
                    "name": "ActiveSet",
                    "description": f"All {base_entity} active at the point in time",
                    "set_definition": {
                        "name": "ActiveSet",
                        "base_entity": base_entity,
                        "key_column": key_col,
                        "filter_conditions": {
                            "conditions": [
                                {"column": "active_date", "operator": "LE", "value": "@PeriodEnd"},
                                {
                                    "conditions": [
                                        {"column": "inactive_date", "operator": "IS_NULL"},
                                        {"column": "inactive_date", "operator": "GT", "value": "@PeriodEnd"}
                                    ],
                                    "logical_operator": "OR"
                                }
                            ],
                            "logical_operator": "AND"
                        }
                    }
                },
                {
                    "step_number": 2,
                    "name": "ActiveCount",
                    "description": "Count of active set",
                    "aggregation": {
                        "name": "ActiveCount",
                        "set_name": "ActiveSet",
                        "aggregation_type": "COUNTROWS"
                    }
                }
            ],
            "final_formula": "ActiveCount"
        }
    
    def _build_ratio_definition(
        self, 
        base_entity: str, 
        entities: List[str],
        formula_lower: str
    ) -> Dict[str, Any]:
        """
        Build set_based_definition for generic Ratio/Percentage.
        
        Calculates: (SubsetCount / TotalCount) * 100
        
        Tries to infer the subset condition from the formula.
        """
        key_col = f"{base_entity.rstrip('s')}_id"
        
        # Try to infer subset condition from formula
        subset_condition = "status = 'active'"  # Default
        if "premium" in formula_lower:
            subset_condition = "tier = 'premium'"
        elif "paid" in formula_lower:
            subset_condition = "payment_status = 'paid'"
        elif "verified" in formula_lower:
            subset_condition = "verified = true"
        elif "complete" in formula_lower:
            subset_condition = "status = 'complete'"
        
        return {
            "base_entity": base_entity,
            "key_column": key_col,
            "period_parameters": ["PeriodEnd"],
            "steps": [
                {
                    "step_number": 1,
                    "name": "TotalSet",
                    "description": f"All {base_entity} at the point in time",
                    "set_definition": {
                        "name": "TotalSet",
                        "base_entity": base_entity,
                        "key_column": key_col,
                        "filter_conditions": {
                            "conditions": [
                                {"column": "active_date", "operator": "LE", "value": "@PeriodEnd"},
                                {
                                    "conditions": [
                                        {"column": "inactive_date", "operator": "IS_NULL"},
                                        {"column": "inactive_date", "operator": "GT", "value": "@PeriodEnd"}
                                    ],
                                    "logical_operator": "OR"
                                }
                            ],
                            "logical_operator": "AND"
                        }
                    }
                },
                {
                    "step_number": 2,
                    "name": "SubsetSet",
                    "description": f"{base_entity} matching subset criteria",
                    "set_definition": {
                        "name": "SubsetSet",
                        "base_entity": base_entity,
                        "key_column": key_col,
                        "filter_conditions": {
                            "conditions": [
                                {"column": "active_date", "operator": "LE", "value": "@PeriodEnd"},
                                {
                                    "conditions": [
                                        {"column": "inactive_date", "operator": "IS_NULL"},
                                        {"column": "inactive_date", "operator": "GT", "value": "@PeriodEnd"}
                                    ],
                                    "logical_operator": "OR"
                                }
                            ],
                            "logical_operator": "AND",
                            "raw_sql_condition": subset_condition
                        }
                    }
                },
                {
                    "step_number": 3,
                    "name": "TotalCount",
                    "description": "Count of total set",
                    "aggregation": {
                        "name": "TotalCount",
                        "set_name": "TotalSet",
                        "aggregation_type": "COUNTROWS"
                    }
                },
                {
                    "step_number": 4,
                    "name": "SubsetCount",
                    "description": "Count of subset",
                    "aggregation": {
                        "name": "SubsetCount",
                        "set_name": "SubsetSet",
                        "aggregation_type": "COUNTROWS"
                    }
                }
            ],
            "final_formula": "CASE WHEN TotalCount > 0 THEN (SubsetCount::float / TotalCount::float) * 100 ELSE 0 END"
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
