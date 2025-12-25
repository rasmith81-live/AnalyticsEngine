"""
Strategic Recommender
Maps business context to recommended value chains using NLP-based semantic search.
Integrates with Entity Resolution Service for vector embeddings and semantic similarity.
"""

from typing import List, Dict, Any, Optional, Set
from pydantic import BaseModel
import logging
import httpx

logger = logging.getLogger(__name__)


class ValueChainSet(BaseModel):
    """Value chain definition with processes and activities."""
    industry_code: str
    name: str
    description: str = ""
    processes: List[str]
    activities: List[str]
    domain_entities: List[str] = []  # Extracted entities for semantic matching


class StrategyScore(BaseModel):
    """Recommendation score with semantic evidence."""
    value_chain_name: str
    industry_code: str
    relevance_score: float
    rationale: str
    matched_entities: List[str] = []
    matched_phrases: List[str] = []


class StrategicRecommender:
    """
    Maps business context to recommended value chains using semantic search.
    Uses Entity Resolution Service for NLP-based vector embeddings and similarity.
    """
    
    def __init__(
        self, 
        entity_resolution_url: str = "http://entity_resolution_service:8000",
        metadata_service_url: str = "http://business_metadata:8000"
    ):
        self.entity_resolution_url = entity_resolution_url
        self.metadata_service_url = metadata_service_url
        self.timeout = 30.0
        self._value_chain_cache: Dict[str, ValueChainSet] = {}
        self._initialized = False
        
    async def _initialize_value_chains(self):
        """Load and index value chains from metadata service."""
        if self._initialized:
            return
            
        # Try to fetch from metadata service
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.metadata_service_url}/api/v1/metadata/value-chains"
                )
                if response.status_code == 200:
                    chains = response.json()
                    for chain in chains:
                        vc = ValueChainSet(
                            industry_code=chain.get("code", ""),
                            name=chain.get("name", ""),
                            description=chain.get("description", ""),
                            processes=chain.get("processes", []),
                            activities=chain.get("activities", [])
                        )
                        # Extract semantic entities for this value chain
                        vc.domain_entities = await self._extract_domain_entities(vc)
                        self._value_chain_cache[vc.industry_code] = vc
                    self._initialized = True
                    return
        except Exception as e:
            logger.warning(f"Could not fetch value chains from metadata service: {e}")
        
        # Fallback to built-in value chains
        await self._load_default_value_chains()
        self._initialized = True
    
    async def _load_default_value_chains(self):
        """Load default value chain definitions."""
        default_chains = [
            ValueChainSet(
                industry_code="62",
                name="Standard Model for Healthcare",
                description="Healthcare delivery and patient management including clinical operations, revenue cycle, and care coordination.",
                processes=["Patient Admission", "Care Delivery", "Discharge Planning", "Revenue Cycle Management"],
                activities=["Triage", "Diagnosis", "Treatment", "Billing", "Claims Processing"]
            ),
            ValueChainSet(
                industry_code="31-33",
                name="Standard Model for Supply Chain",
                description="Manufacturing and supply chain operations including procurement, production, quality control, and logistics.",
                processes=["Procurement", "Production", "Quality Control", "Logistics"],
                activities=["Sourcing", "Assembly", "Testing", "Shipping", "Inventory Management"]
            ),
            ValueChainSet(
                industry_code="52",
                name="Standard Model for Finance",
                description="Financial services including banking, investment management, risk analysis, and regulatory compliance.",
                processes=["Account Management", "Transaction Processing", "Risk Assessment", "Compliance"],
                activities=["Lending", "Trading", "Underwriting", "Auditing", "Reporting"]
            ),
            ValueChainSet(
                industry_code="44-45",
                name="Standard Model for Retail",
                description="Retail operations including merchandising, sales, customer service, and omnichannel fulfillment.",
                processes=["Merchandising", "Sales", "Customer Service", "Fulfillment"],
                activities=["Assortment Planning", "Pricing", "Promotions", "Order Management", "Returns"]
            ),
            ValueChainSet(
                industry_code="54",
                name="Standard Model for Professional Services",
                description="Professional and business services including consulting, project delivery, and client management.",
                processes=["Business Development", "Project Delivery", "Resource Management", "Client Success"],
                activities=["Proposal Development", "Engagement Planning", "Deliverable Creation", "Knowledge Management"]
            )
        ]
        
        for vc in default_chains:
            # Extract semantic entities using Entity Resolution Service
            vc.domain_entities = await self._extract_domain_entities(vc)
            self._value_chain_cache[vc.industry_code] = vc
    
    async def _extract_domain_entities(self, vc: ValueChainSet) -> List[str]:
        """Extract semantic entities from a value chain definition."""
        # Combine all text from the value chain
        text_parts = [
            vc.name,
            vc.description,
            " ".join(vc.processes),
            " ".join(vc.activities)
        ]
        combined_text = " ".join(text_parts)
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.entity_resolution_url}/api/v1/entity-resolution/semantic/extract",
                    json={
                        "text": combined_text,
                        "name": vc.name,
                        "description": vc.description
                    }
                )
                response.raise_for_status()
                result = response.json()
                
                # Collect entities and noun phrases
                entities = [e.get("lemma", "") for e in result.get("entities", [])]
                phrases = result.get("noun_phrases", [])
                return list(set(entities + phrases))
                
        except Exception as e:
            logger.warning(f"Entity extraction failed for {vc.name}: {e}")
            # Fallback: extract simple words
            words = combined_text.lower().split()
            return [w for w in words if len(w) > 3][:20]
    
    async def _extract_query_semantics(self, business_description: str, use_cases: List[str]) -> Dict[str, Any]:
        """Extract semantic representation from user query."""
        combined_text = f"{business_description} {' '.join(use_cases)}"
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.entity_resolution_url}/api/v1/entity-resolution/semantic/extract",
                    json={
                        "text": combined_text,
                        "name": "User Query",
                        "description": business_description
                    }
                )
                response.raise_for_status()
                result = response.json()
                
                return {
                    "entities": set(e.get("lemma", "") for e in result.get("entities", [])),
                    "phrases": set(result.get("noun_phrases", [])),
                    "domain": result.get("domain"),
                    "domain_confidence": result.get("domain_confidence", 0.0)
                }
                
        except Exception as e:
            logger.warning(f"Query semantic extraction failed: {e}")
            # Fallback
            words = combined_text.lower().split()
            return {
                "entities": set(w for w in words if len(w) > 3),
                "phrases": set(),
                "domain": None,
                "domain_confidence": 0.0
            }
    
    def _calculate_semantic_similarity(
        self, 
        query_entities: Set[str], 
        query_phrases: Set[str],
        vc_entities: List[str]
    ) -> tuple[float, List[str], List[str]]:
        """
        Calculate semantic similarity using Jaccard coefficient on extracted entities.
        Returns (score, matched_entities, matched_phrases).
        """
        vc_entity_set = set(e.lower() for e in vc_entities)
        query_entity_set = set(e.lower() for e in query_entities)
        query_phrase_set = set(p.lower() for p in query_phrases)
        
        # Entity overlap
        entity_intersection = query_entity_set & vc_entity_set
        entity_union = query_entity_set | vc_entity_set
        entity_similarity = len(entity_intersection) / len(entity_union) if entity_union else 0.0
        
        # Phrase overlap (partial matching)
        phrase_matches = []
        for qp in query_phrase_set:
            for ve in vc_entity_set:
                if qp in ve or ve in qp:
                    phrase_matches.append(qp)
                    break
        phrase_similarity = len(phrase_matches) / len(query_phrase_set) if query_phrase_set else 0.0
        
        # Combined score (weighted)
        combined_score = (entity_similarity * 0.7) + (phrase_similarity * 0.3)
        
        return combined_score, list(entity_intersection), phrase_matches
        
    async def recommend_value_chains(
        self, 
        business_description: str, 
        use_cases: List[str]
    ) -> List[StrategyScore]:
        """
        Analyzes description and use cases to recommend Value Chain Sets
        using NLP-based semantic search via Entity Resolution Service.
        """
        # Initialize value chains if not done
        await self._initialize_value_chains()
        
        # Extract semantic representation of user query
        query_semantics = await self._extract_query_semantics(business_description, use_cases)
        query_entities = query_semantics["entities"]
        query_phrases = query_semantics["phrases"]
        inferred_domain = query_semantics.get("domain")
        
        recommendations = []
        
        # Compare against all value chains
        for industry_code, vc in self._value_chain_cache.items():
            score, matched_entities, matched_phrases = self._calculate_semantic_similarity(
                query_entities, 
                query_phrases,
                vc.domain_entities
            )
            
            # Boost score if domain matches
            if inferred_domain and inferred_domain.lower() in vc.name.lower():
                score = min(1.0, score + 0.2)
            
            if score > 0.1:  # Minimum threshold
                # Build rationale from matched concepts
                rationale_parts = []
                if matched_entities:
                    rationale_parts.append(f"Matched entities: {', '.join(matched_entities[:5])}")
                if matched_phrases:
                    rationale_parts.append(f"Matched concepts: {', '.join(matched_phrases[:5])}")
                if inferred_domain:
                    rationale_parts.append(f"Inferred domain: {inferred_domain}")
                
                rationale = ". ".join(rationale_parts) if rationale_parts else "Semantic similarity match"
                
                recommendations.append(StrategyScore(
                    value_chain_name=vc.name,
                    industry_code=vc.industry_code,
                    relevance_score=round(score, 3),
                    rationale=rationale,
                    matched_entities=matched_entities[:10],
                    matched_phrases=matched_phrases[:10]
                ))
        
        # Sort by score descending
        recommendations.sort(key=lambda x: x.relevance_score, reverse=True)
        return recommendations[:5]  # Return top 5

    async def get_strategy_alignment(
        self, 
        industry_code: str, 
        strategy_type: str
    ) -> Dict[str, Any]:
        """
        Calculates alignment score between an industry and a strategy type
        using semantic similarity of strategy concepts.
        
        Strategy types: "Operational Efficiency", "Growth", "Risk Management"
        """
        await self._initialize_value_chains()
        
        vc = self._value_chain_cache.get(industry_code)
        if not vc:
            return {"score": 0.5, "rationale": "Industry not found"}
        
        # Define strategy concept sets
        strategy_concepts = {
            "Operational Efficiency": [
                "efficiency", "optimization", "cost reduction", "automation",
                "productivity", "throughput", "cycle time", "waste reduction"
            ],
            "Growth": [
                "growth", "expansion", "revenue", "market share", "acquisition",
                "new markets", "customer acquisition", "scaling"
            ],
            "Risk Management": [
                "risk", "compliance", "security", "audit", "control",
                "governance", "mitigation", "resilience", "continuity"
            ]
        }
        
        strategy_terms = set(strategy_concepts.get(strategy_type, []))
        vc_terms = set(e.lower() for e in vc.domain_entities)
        
        # Calculate overlap
        overlap = strategy_terms & vc_terms
        score = len(overlap) / len(strategy_terms) if strategy_terms else 0.5
        
        # Normalize to 0.5-1.0 range (minimum 0.5 for unknown)
        normalized_score = 0.5 + (score * 0.5)
        
        return {
            "score": round(normalized_score, 2),
            "strategy_type": strategy_type,
            "industry": vc.name,
            "matched_concepts": list(overlap),
            "rationale": f"Found {len(overlap)} strategy-aligned concepts in {vc.name}"
        }
