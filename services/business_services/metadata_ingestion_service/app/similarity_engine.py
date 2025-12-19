from typing import List, Dict, Any, Tuple
from rapidfuzz import process, fuzz

class SimilarityEngine:
    """
    Identifies potential duplicate KPIs based on semantic similarity of names and descriptions.
    """

    def __init__(self, threshold: float = 85.0):
        self.threshold = threshold

    def find_potential_duplicates(
        self, 
        new_kpi: Dict[str, Any], 
        existing_kpis: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Compare a new KPI definition against a list of existing KPIs to find potential duplicates.
        
        Args:
            new_kpi: Dictionary containing 'name', 'description', and optionally 'formula'.
            existing_kpis: List of dictionaries of existing KPIs.
            
        Returns:
            List of matches with similarity scores.
        """
        matches = []
        
        new_name = new_kpi.get("name", "")
        new_desc = new_kpi.get("description", "")
        
        # 1. Check Name Similarity
        # Extract names from existing KPIs
        existing_names = [k.get("name", "") for k in existing_kpis]
        
        # Get top matches for name
        name_matches = process.extract(
            new_name, 
            existing_names, 
            scorer=fuzz.token_sort_ratio, 
            limit=5,
            score_cutoff=self.threshold
        )
        
        for match_name, score, index in name_matches:
            matched_kpi = existing_kpis[index]
            matches.append({
                "candidate_code": matched_kpi.get("code"),
                "candidate_name": matched_kpi.get("name"),
                "similarity_score": score,
                "match_type": "name_similarity",
                "reason": f"Name similarity: {score:.1f}%"
            })

        # 2. Check Description Similarity (if name didn't match perfectly)
        # Only check if description is substantial enough
        if len(new_desc) > 10:
            existing_descs = [k.get("description", "") or "" for k in existing_kpis]
            
            desc_matches = process.extract(
                new_desc,
                existing_descs,
                scorer=fuzz.token_set_ratio, # Better for partial set matches (keywords)
                limit=3,
                score_cutoff=self.threshold - 10 # Slightly lower threshold for description
            )
            
            for match_desc, score, index in desc_matches:
                matched_kpi = existing_kpis[index]
                # Avoid duplicates if already found by name
                if not any(m["candidate_code"] == matched_kpi.get("code") for m in matches):
                    matches.append({
                        "candidate_code": matched_kpi.get("code"),
                        "candidate_name": matched_kpi.get("name"),
                        "similarity_score": score,
                        "match_type": "description_similarity",
                        "reason": f"Description similarity: {score:.1f}%"
                    })
        
        # Sort by score descending
        matches.sort(key=lambda x: x["similarity_score"], reverse=True)
        
        return matches
