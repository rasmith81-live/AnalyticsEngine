"""
Entity Extraction Module
Integrates with Entity Resolution Service for NLP-based semantic entity extraction.
No keyword matching - uses pure NLP analysis via the Entity Resolution Service.
"""

from typing import List, Dict, Any, Optional
import logging
import os
import httpx

logger = logging.getLogger(__name__)


class EntityExtractor:
    """
    Extracts entity references from KPI names, descriptions, and formulas.
    Delegates to Entity Resolution Service for NLP-based semantic extraction.
    """
    
    def __init__(self, entity_resolution_url: str = None):
        """
        Initialize the entity extractor.
        
        Args:
            entity_resolution_url: URL of the Entity Resolution Service
        """
        self.entity_resolution_url = entity_resolution_url or os.getenv(
            "ENTITY_RESOLUTION_SERVICE_URL", 
            "http://entity_resolution_service:8000"
        )
        self.timeout = 30.0
    
    def extract_entities(self, kpi_data: Dict[str, Any]) -> List[str]:
        """
        Extract entity references from KPI data using Entity Resolution Service.
        Uses synchronous httpx to avoid Docker DNS resolution issues with async threads.
        
        Args:
            kpi_data: Dictionary containing KPI name, description, formula, etc.
            
        Returns:
            List of extracted entity names
        """
        # Build request for Entity Resolution Service
        text = " ".join([
            str(kpi_data.get("name", "") or ""),
            str(kpi_data.get("description", "") or ""),
        ])
        
        if not text.strip():
            return []
        
        request_data = {
            "text": text,
            "name": kpi_data.get("name"),
            "description": kpi_data.get("description"),
            "formula": kpi_data.get("formula"),
            "source_file": kpi_data.get("metadata", {}).get("source_file")
        }
        
        try:
            with httpx.Client(timeout=self.timeout) as client:
                response = client.post(
                    f"{self.entity_resolution_url}/api/v1/entity-resolution/semantic/extract",
                    json=request_data
                )
                response.raise_for_status()
                result = response.json()
                
                # Extract entity names from response
                entities = []
                for entity in result.get("entities", []):
                    # Use entity_type if available, otherwise use lemma
                    entity_name = entity.get("entity_type") or entity.get("lemma", "").title()
                    if entity_name and entity_name not in entities:
                        entities.append(entity_name)
                
                logger.info(f"Entity Resolution Service extracted: {entities}")
                return entities
                
        except httpx.HTTPError as e:
            logger.warning(f"Entity Resolution Service call failed: {e}. Using fallback.")
            return self._extract_fallback(kpi_data)
        except Exception as e:
            logger.warning(f"Entity extraction error: {e}. Using fallback.")
            return self._extract_fallback(kpi_data)
    
    def _extract_fallback(self, kpi_data: Dict[str, Any]) -> List[str]:
        """
        Fallback extraction when Entity Resolution Service is unavailable.
        Uses basic regex to extract capitalized words as potential entities.
        """
        import re
        
        text = " ".join([
            str(kpi_data.get("name", "") or ""),
            str(kpi_data.get("description", "") or ""),
        ])
        
        # Extract capitalized words (likely proper nouns/entities)
        entities = []
        words = re.findall(r'\b[A-Z][a-z]+\b', text)
        for word in words:
            if word not in entities and len(word) > 2:
                entities.append(word)
        
        return entities[:20]  # Limit to top 20
    
    def extract_with_domain(self, kpi_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract entities and infer domain/module using Entity Resolution Service.
        Uses synchronous httpx to avoid Docker DNS resolution issues.
        
        Args:
            kpi_data: Dictionary containing KPI metadata
            
        Returns:
            Dict with entities, domain, and module
        """
        text = " ".join([
            str(kpi_data.get("name", "") or ""),
            str(kpi_data.get("description", "") or ""),
        ])
        
        request_data = {
            "text": text,
            "name": kpi_data.get("name"),
            "description": kpi_data.get("description"),
            "formula": kpi_data.get("formula"),
            "source_file": kpi_data.get("metadata", {}).get("source_file")
        }
        
        try:
            with httpx.Client(timeout=self.timeout) as client:
                response = client.post(
                    f"{self.entity_resolution_url}/api/v1/entity-resolution/semantic/extract",
                    json=request_data
                )
                response.raise_for_status()
                result = response.json()
                
                entities = [
                    e.get("entity_type") or e.get("lemma", "").title()
                    for e in result.get("entities", [])
                ]
                
                return {
                    "entities": [e for e in entities if e],
                    "domain": result.get("domain"),
                    "domain_confidence": result.get("domain_confidence", 0.0),
                    "module": result.get("module"),
                    "noun_phrases": result.get("noun_phrases", [])
                }
                
        except Exception as e:
            logger.warning(f"Full extraction failed: {e}")
            return {
                "entities": self._extract_fallback(kpi_data),
                "domain": None,
                "domain_confidence": 0.0,
                "module": None,
                "noun_phrases": []
            }
    
    def infer_domain(self, kpi_data: Dict[str, Any]) -> str:
        """
        Infer domain using Entity Resolution Service.
        Falls back to LLM intent extraction if semantic matching confidence is low.
        """
        result = self.extract_with_domain(kpi_data)
        domain = result.get("domain")
        confidence = result.get("domain_confidence", 0.0)
        
        # If confidence is low, use LLM intent extraction
        if not domain or confidence < 0.5:
            logger.info(f"Low confidence ({confidence}) for domain, using intent extraction")
            intent_result = self._extract_intent(kpi_data)
            if intent_result and intent_result.get("domain"):
                return intent_result["domain"]
        
        return domain or "general_business"
    
    def _extract_intent(self, kpi_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Use LLM-based intent extraction for better domain inference.
        Called when semantic matching confidence is low.
        """
        text = " ".join([
            str(kpi_data.get("name", "") or ""),
            str(kpi_data.get("description", "") or ""),
        ])
        
        request_data = {
            "text": text,
            "context": [kpi_data.get("formula", "")] if kpi_data.get("formula") else [],
            "source_file": kpi_data.get("metadata", {}).get("source_file")
        }
        
        try:
            with httpx.Client(timeout=self.timeout) as client:
                response = client.post(
                    f"{self.entity_resolution_url}/api/v1/entity-resolution/semantic/extract-intent",
                    json=request_data
                )
                response.raise_for_status()
                result = response.json()
                intent = result.get("intent", {})
                logger.info(f"Intent extraction returned domain: {intent.get('domain')}")
                return intent
        except Exception as e:
            logger.warning(f"Intent extraction failed: {e}")
            return None
    
    def infer_module(self, kpi_data: Dict[str, Any]) -> str:
        """
        Infer module using Entity Resolution Service.
        """
        result = self.extract_with_domain(kpi_data)
        return result.get("module") or self._fallback_module(kpi_data)
    
    def _fallback_module(self, kpi_data: Dict[str, Any]) -> str:
        """Fallback module inference from source file."""
        import re
        source_file = kpi_data.get("metadata", {}).get("source_file", "")
        if source_file:
            module = source_file
            module = re.sub(r'\.csv$|\.xlsx?$', '', module, flags=re.IGNORECASE)
            module = re.sub(r'^kpidepot\.com[-_]?', '', module, flags=re.IGNORECASE)
            module = re.sub(r'[-\s]+', '_', module).lower()
            return module or "general"
        return "general"
