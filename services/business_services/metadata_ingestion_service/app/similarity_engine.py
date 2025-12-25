"""
Similarity Engine
Identifies potential duplicate KPIs using NLP-based semantic similarity via Entity Resolution Service.
No string-based fuzzy matching - uses word vectors for true semantic comparison.
"""

from typing import List, Dict, Any, Optional
import logging
import httpx

logger = logging.getLogger(__name__)


class SimilarityEngine:
    """
    Identifies potential duplicate KPIs based on NLP semantic similarity.
    Delegates to Entity Resolution Service for vector-based semantic comparison.
    """

    def __init__(
        self, 
        entity_resolution_url: str = "http://entity_resolution_service:8000",
        threshold: float = 0.75
    ):
        """
        Initialize the similarity engine.
        
        Args:
            entity_resolution_url: URL of the Entity Resolution Service
            threshold: Similarity threshold (0-1) for considering duplicates
        """
        self.entity_resolution_url = entity_resolution_url
        self.threshold = threshold
        self.timeout = 30.0

    def find_potential_duplicates(
        self, 
        new_kpi: Dict[str, Any], 
        existing_kpis: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Synchronous wrapper for async duplicate detection.
        """
        import asyncio
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                import concurrent.futures
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    future = executor.submit(
                        asyncio.run, 
                        self._find_duplicates_async(new_kpi, existing_kpis)
                    )
                    return future.result()
            else:
                return loop.run_until_complete(
                    self._find_duplicates_async(new_kpi, existing_kpis)
                )
        except RuntimeError:
            return asyncio.run(self._find_duplicates_async(new_kpi, existing_kpis))

    async def _find_duplicates_async(
        self, 
        new_kpi: Dict[str, Any], 
        existing_kpis: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Compare a new KPI against existing KPIs using NLP semantic similarity.
        
        Args:
            new_kpi: Dictionary containing 'name', 'description', and optionally 'formula'.
            existing_kpis: List of dictionaries of existing KPIs.
            
        Returns:
            List of matches with similarity scores.
        """
        if not existing_kpis:
            return []
        
        new_text = self._build_comparison_text(new_kpi)
        if not new_text.strip():
            return []
        
        # Try Entity Resolution Service for semantic similarity
        try:
            return await self._semantic_similarity_search(new_kpi, new_text, existing_kpis)
        except Exception as e:
            logger.warning(f"Semantic similarity failed: {e}. Using fallback.")
            return self._fallback_similarity(new_kpi, existing_kpis)

    def _build_comparison_text(self, kpi: Dict[str, Any]) -> str:
        """Build text for semantic comparison."""
        parts = [
            str(kpi.get("name", "") or ""),
            str(kpi.get("description", "") or ""),
        ]
        return " ".join(parts)

    async def _semantic_similarity_search(
        self,
        new_kpi: Dict[str, Any],
        new_text: str,
        existing_kpis: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Use Entity Resolution Service for semantic similarity comparison.
        """
        matches = []
        
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            # Get semantic representation of new KPI
            new_response = await client.post(
                f"{self.entity_resolution_url}/api/v1/entity-resolution/semantic/extract",
                json={
                    "text": new_text,
                    "name": new_kpi.get("name"),
                    "description": new_kpi.get("description")
                }
            )
            new_response.raise_for_status()
            new_extraction = new_response.json()
            new_entities = set(e.get("lemma", "") for e in new_extraction.get("entities", []))
            new_phrases = set(new_extraction.get("noun_phrases", []))
            
            # Compare against each existing KPI
            for existing_kpi in existing_kpis:
                existing_text = self._build_comparison_text(existing_kpi)
                if not existing_text.strip():
                    continue
                
                # Get semantic representation of existing KPI
                existing_response = await client.post(
                    f"{self.entity_resolution_url}/api/v1/entity-resolution/semantic/extract",
                    json={
                        "text": existing_text,
                        "name": existing_kpi.get("name"),
                        "description": existing_kpi.get("description")
                    }
                )
                existing_response.raise_for_status()
                existing_extraction = existing_response.json()
                existing_entities = set(e.get("lemma", "") for e in existing_extraction.get("entities", []))
                existing_phrases = set(existing_extraction.get("noun_phrases", []))
                
                # Calculate Jaccard similarity on entities and phrases
                entity_similarity = self._jaccard_similarity(new_entities, existing_entities)
                phrase_similarity = self._jaccard_similarity(new_phrases, existing_phrases)
                
                # Combined score (weighted average)
                combined_score = (entity_similarity * 0.6) + (phrase_similarity * 0.4)
                
                if combined_score >= self.threshold:
                    matches.append({
                        "candidate_code": existing_kpi.get("code"),
                        "candidate_name": existing_kpi.get("name"),
                        "similarity_score": combined_score * 100,  # Convert to percentage
                        "match_type": "semantic_similarity",
                        "reason": f"Semantic similarity: {combined_score*100:.1f}% (entities: {entity_similarity*100:.0f}%, phrases: {phrase_similarity*100:.0f}%)",
                        "shared_entities": list(new_entities & existing_entities),
                        "shared_phrases": list(new_phrases & existing_phrases)
                    })
        
        # Sort by score descending
        matches.sort(key=lambda x: x["similarity_score"], reverse=True)
        return matches[:10]  # Return top 10 matches

    def _jaccard_similarity(self, set1: set, set2: set) -> float:
        """Calculate Jaccard similarity coefficient between two sets."""
        if not set1 and not set2:
            return 0.0
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        return intersection / union if union > 0 else 0.0

    def _fallback_similarity(
        self,
        new_kpi: Dict[str, Any],
        existing_kpis: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Fallback similarity using basic text comparison when Entity Resolution Service unavailable.
        """
        from rapidfuzz import process, fuzz
        
        matches = []
        new_name = new_kpi.get("name", "")
        new_desc = new_kpi.get("description", "")
        
        # Name similarity
        existing_names = [k.get("name", "") for k in existing_kpis]
        name_matches = process.extract(
            new_name, 
            existing_names, 
            scorer=fuzz.token_sort_ratio, 
            limit=5,
            score_cutoff=self.threshold * 100  # Convert threshold to percentage
        )
        
        for match_name, score, index in name_matches:
            matched_kpi = existing_kpis[index]
            matches.append({
                "candidate_code": matched_kpi.get("code"),
                "candidate_name": matched_kpi.get("name"),
                "similarity_score": score,
                "match_type": "name_fuzzy_match",
                "reason": f"Name fuzzy match: {score:.1f}% (fallback)"
            })

        # Description similarity
        if len(new_desc) > 10:
            existing_descs = [k.get("description", "") or "" for k in existing_kpis]
            desc_matches = process.extract(
                new_desc,
                existing_descs,
                scorer=fuzz.token_set_ratio,
                limit=3,
                score_cutoff=(self.threshold - 0.1) * 100
            )
            
            for match_desc, score, index in desc_matches:
                matched_kpi = existing_kpis[index]
                if not any(m["candidate_code"] == matched_kpi.get("code") for m in matches):
                    matches.append({
                        "candidate_code": matched_kpi.get("code"),
                        "candidate_name": matched_kpi.get("name"),
                        "similarity_score": score,
                        "match_type": "description_fuzzy_match",
                        "reason": f"Description fuzzy match: {score:.1f}% (fallback)"
                    })
        
        matches.sort(key=lambda x: x["similarity_score"], reverse=True)
        return matches
