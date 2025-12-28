"""
Formula Parser for KPI Math Expression Generation

Uses pyparsing to parse natural language KPI formulas into proper mathematical expressions.
Integrates with spaCy-extracted entities to produce calculation-engine-ready expressions.

Examples:
    Input:  "(Number of On-site Supplier Audits / Total Number of Suppliers) * 100"
    Output: "(Count(Supplier Audit) / Count(Supplier)) * 100"
    
    Input:  "Value of Spend Compliant with Contracts / Total Value of Spend"
    Output: "Sum(Spend) / Sum(Spend)"
"""

from typing import List, Dict, Any, Optional, Tuple
import re
import logging

logger = logging.getLogger(__name__)

# Lazy load pyparsing
_pyparsing_loaded = False
_pp = None


def _get_pyparsing():
    """Lazy load pyparsing module."""
    global _pyparsing_loaded, _pp
    if _pyparsing_loaded:
        return _pp
    _pyparsing_loaded = True
    try:
        import pyparsing as pp
        _pp = pp
        return pp
    except ImportError:
        logger.warning("pyparsing not available, formula parsing will be limited")
        return None


class FormulaParser:
    """
    Parses natural language KPI formulas into mathematical expressions.
    
    Uses a two-phase approach:
    1. Tokenize and identify structure (operators, parentheses, numbers)
    2. Map noun phrases to entities with appropriate aggregation functions
    """
    
    # Aggregation trigger phrases mapped to functions
    AGGREGATION_TRIGGERS = {
        # Count triggers
        "number of": "Count",
        "count of": "Count",
        "total number of": "Count",
        "# of": "Count",
        
        # Sum triggers  
        "value of": "Sum",
        "sum of": "Sum",
        "total value of": "Sum",
        "amount of": "Sum",
        
        # Average triggers
        "average of": "Avg",
        "avg of": "Avg",
        "mean of": "Avg",
        "average": "Avg",
        
        # Min/Max triggers
        "minimum of": "Min",
        "min of": "Min",
        "maximum of": "Max",
        "max of": "Max",
        
        # Total without "of" implies Sum
        "total": "Sum",
    }
    
    # Math operator keywords to symbols
    OPERATOR_KEYWORDS = {
        "divided by": "/",
        "over": "/",
        "per": "/",
        "multiplied by": "*",
        "times": "*",
        "plus": "+",
        "added to": "+",
        "minus": "-",
        "less": "-",
        "subtracted by": "-",
    }
    
    def __init__(self, entities: List[str] = None):
        """
        Initialize parser with optional list of known entities.
        
        Args:
            entities: List of entity names extracted by spaCy (e.g., ["Supplier Audit", "Supplier"])
        """
        self.entities = entities or []
        self._parser = None
        
    def _build_parser(self):
        """Build the pyparsing grammar for formula parsing."""
        pp = _get_pyparsing()
        if not pp:
            return None
            
        # Basic tokens
        number = pp.Regex(r'\d+\.?\d*').setParseAction(lambda t: float(t[0]) if '.' in t[0] else int(t[0]))
        
        # Operators
        plus = pp.Literal("+")
        minus = pp.Literal("-")
        mult = pp.Literal("*")
        div = pp.Literal("/")
        lpar = pp.Literal("(").suppress()
        rpar = pp.Literal(")").suppress()
        
        # Forward declaration for recursive grammar
        expr = pp.Forward()
        
        # Aggregation function: Count(Entity), Sum(Entity), etc.
        agg_func = pp.oneOf("Count Sum Avg Min Max", caseless=True)
        entity_name = pp.Regex(r'[A-Za-z][A-Za-z\s]*[A-Za-z]|[A-Za-z]')
        aggregation = pp.Group(agg_func + lpar + entity_name + rpar)
        
        # Atom: number, aggregation, or parenthesized expression
        atom = number | aggregation | pp.Group(lpar + expr + rpar)
        
        # Expression with operator precedence
        term = atom + pp.ZeroOrMore((mult | div) + atom)
        expr <<= term + pp.ZeroOrMore((plus | minus) + term)
        
        return expr
    
    def _normalize_formula(self, formula: str) -> str:
        """
        Normalize the formula text for consistent parsing.
        
        - Replace underscores with spaces
        - Normalize whitespace
        - Convert operator keywords to symbols
        """
        normalized = formula.replace('_', ' ')
        
        # Replace operator keywords with symbols (longer phrases first)
        for keyword, symbol in sorted(self.OPERATOR_KEYWORDS.items(), key=lambda x: -len(x[0])):
            pattern = re.compile(r'\b' + re.escape(keyword) + r'\b', re.IGNORECASE)
            normalized = pattern.sub(f' {symbol} ', normalized)
        
        # Normalize whitespace
        normalized = re.sub(r'\s+', ' ', normalized).strip()
        
        return normalized
    
    def _normalize_word(self, word: str) -> str:
        """Normalize a word to its base form (simple singularization)."""
        word_lower = word.lower()
        # Handle common plural endings
        if word_lower.endswith('ies') and len(word_lower) > 4:
            return word_lower[:-3] + 'y'
        if word_lower.endswith('es') and len(word_lower) > 3:
            if word_lower[-3] in 'sxz' or word_lower[-4:-2] in ('ch', 'sh'):
                return word_lower[:-2]
        if word_lower.endswith('s') and not word_lower.endswith('ss') and len(word_lower) > 3:
            # Don't singularize words ending in 'us' (status, radius)
            if not word_lower.endswith('us'):
                return word_lower[:-1]
        return word_lower
    
    def _normalize_words(self, words: set) -> set:
        """Normalize a set of words to their base forms."""
        return {self._normalize_word(w) for w in words}
    
    def _split_and_normalize(self, text: str) -> set:
        """Split text into words, handling hyphens, and normalize each word."""
        # Replace hyphens with spaces to split hyphenated words
        text_clean = text.lower().replace('-', ' ')
        words = set(text_clean.split())
        return self._normalize_words(words)
    
    def _find_matching_entity(self, text: str) -> str:
        """
        Find the best matching entity for a text segment.
        
        Requires ALL entity words to be present in the text (normalized).
        Prefers longer/more specific entity matches over shorter ones.
        Handles singular/plural variations and hyphenated words.
        
        Args:
            text: The noun phrase text to match
            
        Returns:
            The matched entity name, or a cleaned version of the input
        """
        text_words_normalized = self._split_and_normalize(text)
        
        best_match = None
        best_score = 0
        
        # Sort entities by length (longest first) to prefer more specific matches
        for entity in sorted(self.entities, key=len, reverse=True):
            entity_lower = entity.lower()
            entity_words = set(entity_lower.split())
            entity_words_normalized = self._normalize_words(entity_words)
            
            # REQUIRE all entity words to be present in text (normalized)
            # This prevents "Supplier" from matching "Site Supplier Audit" text
            # when the text is just "Suppliers"
            if not entity_words_normalized.issubset(text_words_normalized):
                continue
            
            # Score by number of entity words matched (prefer longer entities)
            score = len(entity_words)
            
            if score > best_score:
                best_score = score
                best_match = entity
        
        if best_match:
            return best_match
        
        # Fallback: return cleaned text
        return text.strip().title()
    
    def _find_first_matching_entity(self, text: str) -> str:
        """
        Find the first entity that appears in the text (by position).
        
        This ensures "Spend Compliant with Contracts" matches "Spend" not "Contract"
        because "Spend" appears first.
        """
        text_lower = text.lower().strip()
        # Split on spaces, but also expand hyphenated words
        text_words = []
        for word in text_lower.split():
            if '-' in word:
                # Add both the parts and the combined form
                parts = word.split('-')
                text_words.extend(parts)
            else:
                text_words.append(word)
        
        best_match = None
        best_position = float('inf')
        
        for entity in self.entities:
            entity_lower = entity.lower()
            entity_first_word = entity_lower.split()[0]
            entity_first_word_normalized = self._normalize_word(entity_first_word)
            
            # Find position of first entity word in text
            for i, word in enumerate(text_words):
                word_normalized = self._normalize_word(word)
                if word_normalized == entity_first_word_normalized:
                    # Verify all entity words are present
                    entity_words_normalized = self._normalize_words(set(entity_lower.split()))
                    text_words_normalized = self._split_and_normalize(text)
                    
                    if entity_words_normalized.issubset(text_words_normalized):
                        if i < best_position:
                            best_position = i
                            best_match = entity
                    break
        
        if best_match:
            return best_match
        
        # Fallback to regular matching
        return self._find_matching_entity(text)
    
    def _clean_entity_phrase(self, text: str) -> str:
        """
        Clean an entity phrase for use in math expression.
        
        - Title case each word
        - Remove filler words (of, with, the, a, an)
        - Singularize words
        - Handle hyphenated words (On-site -> On-Site)
        """
        filler_words = {'of', 'with', 'the', 'a', 'an', 'for', 'by', 'to', 'in', 'on'}
        
        words = text.strip().split()
        cleaned = []
        for word in words:
            word_lower = word.lower()
            # Skip filler words (but not if part of hyphenated word)
            if word_lower in filler_words and '-' not in word:
                continue
            
            # Handle hyphenated words
            if '-' in word:
                parts = word.split('-')
                # Title case each part, skip filler parts
                cleaned_parts = []
                for part in parts:
                    part_lower = part.lower()
                    if part_lower not in filler_words:
                        cleaned_parts.append(part_lower.title())
                if cleaned_parts:
                    cleaned.append('-'.join(cleaned_parts))
            else:
                # Singularize the word
                singular = self._normalize_word(word_lower)
                cleaned.append(singular.title())
        
        return ' '.join(cleaned) if cleaned else text.strip().title()
    
    def _build_qualified_entity(self, entity_text: str) -> str:
        """
        Build a qualified entity name using extracted entities plus qualifiers.
        
        For "Spend Compliant with Contracts":
        - Base entity: "Spend" (from extracted entities)
        - Qualifiers: "Compliant", "Contract"
        - Result: "Compliant Contract Spend"
        
        For "On-site Supplier Audits":
        - Base entity: "Site Supplier Audit" (from extracted entities)
        - Result: "Site Supplier Audit"
        """
        # First, find the matching base entity
        base_entity = self._find_first_matching_entity(entity_text)
        
        # Get all meaningful words from the text (excluding filler words)
        filler_words = {'of', 'with', 'the', 'a', 'an', 'for', 'by', 'to', 'in', 'on'}
        text_words = []
        for word in entity_text.lower().replace('-', ' ').split():
            if word not in filler_words:
                text_words.append(self._normalize_word(word))
        
        # Get words from the base entity
        base_words = set(self._normalize_word(w) for w in base_entity.lower().split())
        
        # Find qualifier words (words in text but not in base entity)
        qualifiers = []
        for word in text_words:
            if word not in base_words and len(word) > 2:
                qualifiers.append(word.title())
        
        # Build the qualified entity: qualifiers + base entity
        if qualifiers:
            return ' '.join(qualifiers) + ' ' + base_entity
        return base_entity
    
    def _identify_aggregation(self, text: str) -> Tuple[str, str]:
        """
        Identify aggregation function and entity from a text segment.
        
        Uses extracted entities as the base, with qualifiers from the formula text.
        Example: "Spend Compliant with Contracts" -> "Compliant Contract Spend"
        
        Args:
            text: Text like "Number of On-site Supplier Audits"
            
        Returns:
            Tuple of (aggregation_function, entity_phrase)
            e.g., ("Count", "Site Supplier Audit")
        """
        text_lower = text.lower().strip()
        
        # Check for aggregation triggers (longer phrases first)
        for trigger, agg_func in sorted(self.AGGREGATION_TRIGGERS.items(), key=lambda x: -len(x[0])):
            if text_lower.startswith(trigger):
                # Extract the entity part after the trigger
                entity_text = text[len(trigger):].strip()
                entity_phrase = self._build_qualified_entity(entity_text)
                return (agg_func, entity_phrase)
            
            # Also check for trigger anywhere in text (for cases like "the total number of")
            pattern = re.compile(r'\b' + re.escape(trigger) + r'\b', re.IGNORECASE)
            match = pattern.search(text_lower)
            if match:
                # Extract entity after the trigger
                entity_text = text[match.end():].strip()
                if entity_text:
                    entity_phrase = self._build_qualified_entity(entity_text)
                    return (agg_func, entity_phrase)
        
        # No aggregation trigger found - build qualified entity
        entity_phrase = self._build_qualified_entity(text)
        return (None, entity_phrase)
    
    def _tokenize_formula(self, formula: str) -> List[Dict[str, Any]]:
        """
        Tokenize the formula into structured tokens.
        
        Returns list of tokens with types:
        - operator: +, -, *, /
        - number: numeric constant
        - paren_open, paren_close: parentheses
        - phrase: noun phrase (to be converted to aggregation)
        """
        tokens = []
        normalized = self._normalize_formula(formula)
        
        # Pattern to match tokens
        # Order matters: operators first, then numbers, then words/phrases
        token_pattern = re.compile(
            r'(\()|'                           # Open paren
            r'(\))|'                           # Close paren
            r'([+\-*/])|'                      # Operators
            r'(\d+\.?\d*)|'                    # Numbers
            r'([A-Za-z][A-Za-z\s\-]*[A-Za-z]|[A-Za-z])'  # Word phrases
        )
        
        pos = 0
        current_phrase = []
        
        for match in token_pattern.finditer(normalized):
            paren_open, paren_close, operator, number, phrase = match.groups()
            
            if paren_open:
                if current_phrase:
                    tokens.append({"type": "phrase", "value": " ".join(current_phrase)})
                    current_phrase = []
                tokens.append({"type": "paren_open", "value": "("})
            elif paren_close:
                if current_phrase:
                    tokens.append({"type": "phrase", "value": " ".join(current_phrase)})
                    current_phrase = []
                tokens.append({"type": "paren_close", "value": ")"})
            elif operator:
                if current_phrase:
                    tokens.append({"type": "phrase", "value": " ".join(current_phrase)})
                    current_phrase = []
                tokens.append({"type": "operator", "value": operator})
            elif number:
                if current_phrase:
                    tokens.append({"type": "phrase", "value": " ".join(current_phrase)})
                    current_phrase = []
                tokens.append({"type": "number", "value": number})
            elif phrase:
                current_phrase.append(phrase)
        
        # Don't forget trailing phrase
        if current_phrase:
            tokens.append({"type": "phrase", "value": " ".join(current_phrase)})
        
        return tokens
    
    def parse(self, formula: str) -> str:
        """
        Parse a natural language formula into a mathematical expression.
        
        Args:
            formula: Natural language formula like 
                     "(Number of On-site Supplier Audits / Total Number of Suppliers) * 100"
        
        Returns:
            Mathematical expression like "(Count(Supplier Audit) / Count(Supplier)) * 100"
        """
        if not formula:
            return ""
        
        tokens = self._tokenize_formula(formula)
        
        # Build output expression
        output_parts = []
        
        for token in tokens:
            if token["type"] == "operator":
                output_parts.append(f" {token['value']} ")
            elif token["type"] == "number":
                output_parts.append(token["value"])
            elif token["type"] == "paren_open":
                output_parts.append("(")
            elif token["type"] == "paren_close":
                output_parts.append(")")
            elif token["type"] == "phrase":
                # Convert phrase to aggregation(entity)
                agg_func, entity = self._identify_aggregation(token["value"])
                if agg_func:
                    output_parts.append(f"{agg_func}({entity})")
                else:
                    # No aggregation - just use entity name
                    output_parts.append(entity)
        
        result = "".join(output_parts)
        
        # Clean up spacing around operators and parentheses
        result = re.sub(r'\s+', ' ', result)
        result = re.sub(r'\(\s+', '(', result)
        result = re.sub(r'\s+\)', ')', result)
        result = re.sub(r'\s*([+\-*/])\s*', r' \1 ', result)
        
        return result.strip()


def parse_formula_to_math(formula: str, entities: List[str] = None) -> str:
    """
    Convenience function to parse a formula with given entities.
    
    Args:
        formula: Natural language formula
        entities: List of entity names extracted by spaCy
        
    Returns:
        Mathematical expression string
    """
    parser = FormulaParser(entities=entities)
    return parser.parse(formula)
