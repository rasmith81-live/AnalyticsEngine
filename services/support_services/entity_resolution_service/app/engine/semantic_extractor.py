"""
Semantic Entity Extractor
LLM-based extraction of business entities from text.
No spaCy - uses pure LLM analysis for accurate business entity extraction.
"""

import logging
import time
from typing import List, Dict, Any, Optional, Tuple
from ..models import ExtractedEntity, SemanticExtractionResponse

logger = logging.getLogger(__name__)



class SemanticExtractor:
    """
    LLM-based semantic entity extractor.
    Extracts business entities and infers domain using LLM.
    """
    
    def __init__(self):
        """Initialize the semantic extractor (LLM-only, no spaCy)."""
        pass
    
    async def extract(
        self,
        text: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        formula: Optional[str] = None,
        source_file: Optional[str] = None
    ) -> SemanticExtractionResponse:
        """
        Extract entities and infer domain from text using LLM (primary) or spaCy (fallback).
        
        Args:
            text: Primary text to analyze
            name: Optional name for additional context
            description: Optional description for additional context
            formula: Optional formula to parse for entity references
            source_file: Optional source file name for context
            
        Returns:
            SemanticExtractionResponse with extracted entities and inferred domain
        """
        start_time = time.time()
        
        # Combine all text sources
        all_text = " ".join(filter(None, [text, name, description]))
        
        if not all_text.strip():
            return SemanticExtractionResponse(
                entities=[],
                processing_time_ms=0.0
            )
        
        # Use LLM-based extraction (no spaCy fallback)
        entities, noun_phrases = await self._extract_with_llm(all_text, formula)
        
        # Infer domain from extracted entities and source file
        domain, domain_confidence = self._infer_domain(entities, noun_phrases, source_file)
        
        # Infer module from source file or entities
        module = self._infer_module(entities, noun_phrases, source_file)
        
        processing_time = (time.time() - start_time) * 1000
        
        return SemanticExtractionResponse(
            entities=entities,
            domain=domain,
            domain_confidence=domain_confidence,
            module=module,
            noun_phrases=noun_phrases,
            processing_time_ms=processing_time
        )
    
    async def _extract_with_llm(self, text: str, formula: Optional[str] = None) -> Tuple[List[ExtractedEntity], List[str]]:
        """
        Extract business entities using LLM.
        Returns only concrete business nouns (objects, people, things).
        """
        import os
        import json
        import openai
        
        # Mock mode for testing - returns dummy entities without calling LLM
        if os.getenv("MOCK_LLM", "").lower() in ("true", "1", "yes"):
            mock_entities = [
                ExtractedEntity(text="Customer", lemma="customer", entity_type=None, confidence=0.95, pos_tag="LLM"),
                ExtractedEntity(text="Revenue", lemma="revenue", entity_type=None, confidence=0.95, pos_tag="LLM"),
            ]
            logger.info(f"MOCK_LLM enabled - returning mock entities")
            return mock_entities, ["customer", "revenue"]
        
        api_key = os.getenv("OPENAI_API_KEY") or os.getenv("AZURE_OPENAI_API_KEY")
        if not api_key:
            logger.debug("No LLM API key configured, skipping LLM extraction")
            return [], []
        
        # Build prompt
        prompt_text = text
        if formula:
            prompt_text += f"\nFormula: {formula}"
        
        prompt = f"""Extract only concrete business entity nouns from this KPI text.

Rules:
- Return ONLY nouns that represent real business objects, people, or things
- Examples of valid entities: Customer, Order, Invoice, Payment, Supplier, Product, Employee, Shipment, Inventory, Revenue, Cost, Payable, Receivable
- Do NOT include: adjectives (qualitative, weighted, reverse), verbs (derived, distributed), modifiers (global, expected), or abstract concepts (ratio, percentage, metric)
- Return as JSON array of strings, lowercase
- Maximum 5 most important entities

Text: {prompt_text}

Return ONLY a JSON array like: ["customer", "order", "payment"]"""

        try:
            # Configure OpenAI client
            azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
            if azure_endpoint:
                client = openai.AzureOpenAI(
                    api_key=api_key,
                    api_version="2024-02-15-preview",
                    azure_endpoint=azure_endpoint
                )
                model = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4")
            else:
                client = openai.OpenAI(api_key=api_key)
                model = "gpt-4o-mini"
            
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
                max_tokens=100
            )
            
            result_text = response.choices[0].message.content.strip()
            
            # Parse JSON array
            if result_text.startswith("["):
                entity_names = json.loads(result_text)
            else:
                # Try to extract JSON from response
                import re
                match = re.search(r'\[.*?\]', result_text, re.DOTALL)
                if match:
                    entity_names = json.loads(match.group())
                else:
                    entity_names = []
            
            # Convert to ExtractedEntity objects
            entities = []
            for name in entity_names:
                if isinstance(name, str) and name.strip():
                    lemma = name.strip().lower()
                    entities.append(ExtractedEntity(
                        text=lemma.title(),
                        lemma=lemma,
                        entity_type=None,
                        confidence=0.95,
                        pos_tag="LLM"
                    ))
            
            logger.info(f"LLM extracted entities: {[e.lemma for e in entities]}")
            return entities, [e.lemma for e in entities]
            
        except Exception as e:
            logger.warning(f"LLM entity extraction failed: {e}")
            return [], []
    
    async def extract_batch(self, kpi_texts: List[str]) -> List[str]:
        """
        Extract distinct entities from multiple KPIs in a single LLM call.
        Much more efficient than calling extract() for each KPI.
        
        Args:
            kpi_texts: List of KPI text strings (name + description + formula)
            
        Returns:
            List of distinct entity names (lowercase)
        """
        import os
        import json
        import openai
        
        if not kpi_texts:
            return []
        
        # Mock mode for testing - returns dummy entities without calling LLM
        if os.getenv("MOCK_LLM", "").lower() in ("true", "1", "yes"):
            mock_entities = ["customer", "order", "revenue", "inventory", "supplier", "product"]
            logger.info(f"MOCK_LLM enabled - returning mock entities: {mock_entities}")
            return mock_entities
        
        api_key = os.getenv("OPENAI_API_KEY") or os.getenv("AZURE_OPENAI_API_KEY")
        if not api_key:
            logger.warning("No LLM API key configured for batch extraction")
            return []
        
        # Combine all KPI texts
        combined_text = "\n".join([f"- {text}" for text in kpi_texts[:100]])  # Limit to 100 KPIs
        
        prompt = f"""Extract all distinct business entity nouns from these KPIs.

Rules:
- Return ONLY nouns that represent real business objects, people, or things
- Examples of valid entities: Customer, Order, Invoice, Payment, Supplier, Product, Employee, Shipment, Inventory, Revenue, Cost, Payable, Receivable
- Do NOT include: adjectives, verbs, modifiers, or abstract concepts (ratio, percentage, metric, rate, total)
- Return DISTINCT entities only (no duplicates)
- Return as JSON array of strings, lowercase
- Maximum 20 most important entities across all KPIs

KPIs:
{combined_text}

Return ONLY a JSON array like: ["customer", "order", "payment", "supplier"]"""

        try:
            azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
            if azure_endpoint:
                client = openai.AzureOpenAI(
                    api_key=api_key,
                    api_version="2024-02-15-preview",
                    azure_endpoint=azure_endpoint
                )
                model = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4")
            else:
                client = openai.OpenAI(api_key=api_key)
                model = "gpt-4o-mini"
            
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
                max_tokens=200
            )
            
            result_text = response.choices[0].message.content.strip()
            
            # Parse JSON array
            if result_text.startswith("["):
                entity_names = json.loads(result_text)
            else:
                import re
                match = re.search(r'\[.*?\]', result_text, re.DOTALL)
                if match:
                    entity_names = json.loads(match.group())
                else:
                    entity_names = []
            
            # Clean and dedupe
            entities = list(set([
                name.strip().lower() 
                for name in entity_names 
                if isinstance(name, str) and name.strip()
            ]))
            
            logger.info(f"LLM batch extracted {len(entities)} distinct entities: {entities}")
            return entities
            
        except Exception as e:
            logger.warning(f"LLM batch entity extraction failed: {e}")
            return []
    
    def _extract_from_formula(self, formula: str) -> List[ExtractedEntity]:
        """Extract entity references from formula syntax."""
        import re
        
        entities = []
        seen = set()
        
        # Pattern: Entity.Attribute (e.g., "Order.Revenue", "Customer.Count")
        entity_attr_pattern = r'\b([A-Z][a-zA-Z]+)\.([A-Z][a-zA-Z]+)\b'
        for entity, attr in re.findall(entity_attr_pattern, formula):
            lemma = entity.lower()
            if lemma not in seen:
                seen.add(lemma)
                entities.append(ExtractedEntity(
                    text=entity,
                    lemma=lemma,
                    entity_type="FormulaRef",
                    confidence=1.0,
                    pos_tag="FORMULA"
                ))
        
        # Pattern: "Number/Count of X"
        count_pattern = r'(?:Number|Count|Total|Sum)\s+of\s+([A-Z][a-zA-Z]+)'
        for entity in re.findall(count_pattern, formula, re.IGNORECASE):
            lemma = entity.lower()
            if lemma not in seen:
                seen.add(lemma)
                entities.append(ExtractedEntity(
                    text=entity,
                    lemma=lemma,
                    entity_type="FormulaRef",
                    confidence=0.9,
                    pos_tag="FORMULA"
                ))
        
        return entities
    
    def _fetch_value_chains(self) -> List[Dict[str, Any]]:
        """Fetch value chain definitions from Business Metadata Service."""
        import os
        import httpx
        
        bms_url = os.getenv("BUSINESS_METADATA_URL", "http://business_metadata:8000")
        
        try:
            with httpx.Client(timeout=5.0) as client:
                response = client.get(
                    f"{bms_url}/api/v1/metadata/definitions/value_chain_pattern_definition",
                    params={"limit": 50}
                )
                if response.status_code == 200:
                    return response.json()
        except Exception as e:
            logger.warning(f"Failed to fetch value chains from BMS: {e}")
        
        return []
    
    def _infer_domain(
        self,
        entities: List[ExtractedEntity],
        noun_phrases: List[str],
        source_file: Optional[str]
    ) -> Tuple[Optional[str], float]:
        """
        Infer business domain using semantic similarity of extracted entities.
        Dynamically queries value chains from Business Metadata Service.
        Uses word vectors if available, otherwise LLM fallback.
        """
        # Fetch value chains first - needed for source file matching
        value_chains = self._fetch_value_chains()
        domain_codes = [vc.get("code", "") for vc in value_chains if vc.get("code")]
        
        # Priority 1: Check if source_file path indicates a domain (folder or filename)
        if source_file:
            # Normalize path separators and convert to lowercase with underscores
            source_normalized = source_file.lower().replace("\\", "/").replace("-", "_").replace(" ", "_")
            
            # Check each domain code against the full path (folder takes precedence)
            for code in domain_codes:
                # Check if domain code appears in path (e.g., "supply_chain" in "Supply_Chain/file.csv")
                if code in source_normalized:
                    logger.info(f"Source path match: {code} found in '{source_file}'")
                    return code, 0.95  # High confidence for path-based match
        
        # Use LLM for domain inference (no spaCy)
        return self._infer_domain_heuristic(entities, noun_phrases, source_file)
    
    def _infer_domain_heuristic(
        self,
        entities: List[ExtractedEntity],
        noun_phrases: List[str],
        source_file: Optional[str]
    ) -> Tuple[Optional[str], float]:
        """Domain inference using LLM."""
        # Build context from entities and source file
        entity_text = ", ".join([e.lemma for e in entities[:20]])  # Limit entities
        context = f"Entities: {entity_text}"
        if source_file:
            context += f"\nSource file: {source_file}"
        if noun_phrases:
            context += f"\nKey phrases: {', '.join(noun_phrases[:10])}"
        
        # Try LLM-based inference
        try:
            domain, confidence = self._infer_domain_with_llm(context)
            if domain:
                return domain, confidence
        except Exception as e:
            logger.warning(f"LLM domain inference failed: {e}")
        
        return None, 0.0
    
    def _infer_domain_with_llm(self, context: str) -> Tuple[Optional[str], float]:
        """Use LLM to infer business domain from context. Queries BMS for valid domains."""
        import os
        import openai
        
        api_key = os.getenv("OPENAI_API_KEY") or os.getenv("AZURE_OPENAI_API_KEY")
        if not api_key:
            logger.warning("No OpenAI API key configured for LLM fallback")
            return None, 0.0
        
        # Configure client
        if os.getenv("AZURE_OPENAI_ENDPOINT"):
            client = openai.AzureOpenAI(
                api_key=api_key,
                api_version="2023-12-01-preview",
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
            )
            model = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4")
        else:
            client = openai.OpenAI(api_key=api_key)
            model = os.getenv("LLM_MODEL", "gpt-4o-mini")
        
        # Fetch valid domains dynamically from Business Metadata Service
        value_chains = self._fetch_value_chains()
        if value_chains:
            valid_domains = [vc.get("code") for vc in value_chains if vc.get("code")]
            domain_descriptions = "\n".join([
                f"- {vc.get('code')}: {vc.get('description', vc.get('name', ''))}"
                for vc in value_chains if vc.get("code")
            ])
        else:
            # No value chains available - let LLM suggest a new domain
            valid_domains = []
            domain_descriptions = "No existing domains found. You may suggest a new domain code."
        
        prompt = f"""Analyze the following context and determine the most appropriate business domain/value chain.

{context}

Available domains:
{domain_descriptions}

If an existing domain matches well, use it. If none match, suggest a new domain code (lowercase, underscore-separated).

Respond with ONLY a JSON object: {{"domain": "<domain_code>", "confidence": <0.0-1.0>, "is_new": <true/false>}}
If uncertain, use confidence < 0.5."""

        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=100
            )
            
            import json
            result = json.loads(response.choices[0].message.content)
            domain = result.get("domain")
            confidence = float(result.get("confidence", 0.0))
            is_new = result.get("is_new", False)
            
            if domain:
                if is_new:
                    logger.info(f"LLM suggested new domain: {domain} (confidence: {confidence})")
                else:
                    logger.info(f"LLM matched existing domain: {domain} (confidence: {confidence})")
                return domain, confidence
            
        except Exception as e:
            logger.warning(f"LLM inference error: {e}")
        
        return None, 0.0
    
    def _infer_module(
        self,
        entities: List[ExtractedEntity],
        noun_phrases: List[str],
        source_file: Optional[str]
    ) -> Optional[str]:
        """Infer module/category from context."""
        if source_file:
            # Extract module from filename
            import re
            # Remove common prefixes and extensions
            module = source_file
            module = re.sub(r'\.csv$|\.xlsx?$', '', module, flags=re.IGNORECASE)
            module = re.sub(r'^kpidepot\.com[-_]?', '', module, flags=re.IGNORECASE)
            module = re.sub(r'[-\s]+', '_', module).lower()
            if module:
                return module
        
        # Use most common noun phrase as module hint
        if noun_phrases:
            return noun_phrases[0].replace(' ', '_')
        
        return None
    
    async def extract_intent(
        self,
        text: str,
        context: Optional[List[str]] = None,
        source_file: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Extract structured business intent using LLM.
        Used when metadata is sparse or for conversation-style queries.
        
        Returns domain, entities, action, metrics via LLM analysis.
        """
        import os
        import time
        import json
        import openai
        
        start_time = time.time()
        
        # No spaCy - entities will be extracted by LLM
        entities = []
        noun_phrases = []
        
        # Build context for LLM
        full_context = text
        if context:
            full_context += "\nContext: " + " | ".join(context)
        if source_file:
            full_context += f"\nSource: {source_file}"
        if noun_phrases:
            full_context += f"\nKey phrases: {', '.join(noun_phrases[:10])}"
        
        # Fetch available domains from BMS
        value_chains = self._fetch_value_chains()
        if value_chains:
            domain_list = [vc.get("code") for vc in value_chains if vc.get("code")]
            domain_descriptions = "\n".join([
                f"- {vc.get('code')}: {vc.get('description', vc.get('name', ''))}"
                for vc in value_chains if vc.get("code")
            ])
        else:
            domain_list = []
            domain_descriptions = "No existing domains. Suggest a new domain code if needed."
        
        # LLM extraction
        api_key = os.getenv("OPENAI_API_KEY") or os.getenv("AZURE_OPENAI_API_KEY")
        if not api_key:
            logger.warning("No OpenAI API key for intent extraction")
            return {
                "intent": {
                    "domain": "general_business",
                    "domain_confidence": 0.3,
                    "target_entities": [e.lemma for e in entities[:10]],
                    "action": None,
                    "metrics": [],
                    "time_horizon": None,
                    "is_new_domain": False
                },
                "raw_entities": entities,
                "noun_phrases": noun_phrases,
                "processing_time_ms": (time.time() - start_time) * 1000
            }
        
        # Configure client
        if os.getenv("AZURE_OPENAI_ENDPOINT"):
            client = openai.AzureOpenAI(
                api_key=api_key,
                api_version="2023-12-01-preview",
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
            )
            model = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4")
        else:
            client = openai.OpenAI(api_key=api_key)
            model = os.getenv("LLM_MODEL", "gpt-4o-mini")
        
        prompt = f"""Analyze the following business text and extract structured intent.

Text: {full_context}

Available domains in system:
{domain_descriptions}

Extract:
1. domain: Best matching domain code, or suggest new one (lowercase, underscores)
2. domain_confidence: 0.0-1.0
3. target_entities: List of business entities (Customer, Order, Product, etc.)
4. action: What action is implied (monitor, optimize, predict, measure, analyze)
5. metrics: Any KPI/metric names mentioned
6. time_horizon: real_time, historical, forecast, or null
7. is_new_domain: true if domain doesn't exist in system

Respond with ONLY valid JSON:
{{"domain": "...", "domain_confidence": 0.8, "target_entities": [...], "action": "...", "metrics": [...], "time_horizon": "...", "is_new_domain": false}}"""

        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=300
            )
            
            result = json.loads(response.choices[0].message.content)
            
            # Validate domain
            if result.get("domain") and result["domain"] not in domain_list:
                result["is_new_domain"] = True
            
            logger.info(f"LLM intent extraction: domain={result.get('domain')}, entities={result.get('target_entities', [])}")
            
            return {
                "intent": result,
                "raw_entities": entities,
                "noun_phrases": noun_phrases,
                "processing_time_ms": (time.time() - start_time) * 1000
            }
            
        except Exception as e:
            logger.error(f"LLM intent extraction error: {e}")
            return {
                "intent": {
                    "domain": "general_business",
                    "domain_confidence": 0.3,
                    "target_entities": [e.lemma for e in entities[:10]],
                    "action": None,
                    "metrics": [],
                    "time_horizon": None,
                    "is_new_domain": False
                },
                "raw_entities": entities,
                "noun_phrases": noun_phrases,
                "processing_time_ms": (time.time() - start_time) * 1000
            }


# Singleton instance
semantic_extractor = SemanticExtractor()
