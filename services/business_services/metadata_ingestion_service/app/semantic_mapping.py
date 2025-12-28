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
        Parses a formula string (e.g., "(Revenue - Cost) / Revenue") into
        required entities/attributes for calculation.
        
        Extracts ALL nouns as entities using spaCy NLP (no OpenAI).
        Also normalizes time modifiers to generic 'period' for time-agnostic definitions.
        Also generates a mathematical formula expression for the calculation engine.
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
        
        # Parse the formula into a mathematical expression using pyparsing-based parser
        math_expression = parse_formula_to_math(normalized_formula, entities)
        
        # Sort for consistent output
        entities = sorted(set(entities))
        
        logger.info(f"Formula decomposition ({extraction_method}): '{formula}' -> entities={entities}, math='{math_expression}'")
        
        return {
            "original_formula": formula,
            "normalized_formula": normalized_formula,
            "math_expression": math_expression,
            "identified_attributes": entities,
            "extraction_method": extraction_method,
            "status": "resolved" if entities else "no_entities_found"
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
