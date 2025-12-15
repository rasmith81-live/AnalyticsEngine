
from typing import List, Dict, Any, Tuple
import logging
from ..models import EntityRecord

logger = logging.getLogger(__name__)

class MatchingEngine:
    """
    Core engine for entity resolution matching.
    Implements fuzzy matching algorithms (Levenshtein, Jaro-Winkler via libraries)
    and blocking strategies.
    """

    def __init__(self, threshold: float = 0.85):
        self.threshold = threshold

    def _levenshtein_distance(self, s1: str, s2: str) -> int:
        """Simple Levenshtein distance implementation."""
        if len(s1) < len(s2):
            return self._levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        
        return previous_row[-1]

    def _similarity_score(self, s1: str, s2: str) -> float:
        """Calculate normalized similarity score (0.0 to 1.0)."""
        if not s1 and not s2:
            return 1.0
        if not s1 or not s2:
            return 0.0
            
        dist = self._levenshtein_distance(s1.lower(), s2.lower())
        max_len = max(len(s1), len(s2))
        if max_len == 0:
            return 1.0
            
        return 1.0 - (dist / max_len)

    async def find_matches(self, source_record: EntityRecord, candidates: List[EntityRecord]) -> List[Dict[str, Any]]:
        """
        Find matches for a source record within a list of candidates.
        """
        matches = []
        # Access name from attributes dictionary
        source_name = source_record.attributes.get("name", "")
        
        for candidate in candidates:
            candidate_name = candidate.attributes.get("name", "")
            score = self._similarity_score(source_name, candidate_name)
            
            if score >= self.threshold:
                matches.append({
                    "candidate": candidate,
                    "score": score,
                    "match_type": "fuzzy"
                })
                
        # Sort by score descending
        matches.sort(key=lambda x: x["score"], reverse=True)
        return matches

    async def process_batch(self, records: List[EntityRecord]) -> List[Dict[str, Any]]:
        """
        Process a batch of records to identify duplicates within the batch.
        Returns matched groups.
        """
        # Simple O(N^2) for scaffolding - in prod use blocking
        groups = []
        processed_indices = set()
        
        for i in range(len(records)):
            if i in processed_indices:
                continue
                
            current_group = [records[i]]
            processed_indices.add(i)
            
            for j in range(i + 1, len(records)):
                if j in processed_indices:
                    continue
                
                name_i = records[i].attributes.get("name", "")
                name_j = records[j].attributes.get("name", "")
                
                score = self._similarity_score(name_i, name_j)
                if score >= self.threshold:
                    current_group.append(records[j])
                    processed_indices.add(j)
            
            if len(current_group) > 1:
                groups.append({
                    "group_id": f"group_{i}",
                    "records": current_group,
                    "match_type": "intra_batch"
                })
                
        return groups
