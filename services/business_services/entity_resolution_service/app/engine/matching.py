from typing import List, Dict, Tuple
from difflib import SequenceMatcher
from ..models import SourceRecord, MatchCandidate

class BatchMatcher:
    """
    Engine for identifying duplicate records using fuzzy matching.
    """
    
    def __init__(self, threshold: float = 0.85):
        self.threshold = threshold

    def _calculate_similarity(self, str1: str, str2: str) -> float:
        """
        Calculates similarity between two strings using SequenceMatcher.
        Returns a float between 0.0 and 1.0.
        """
        if not str1 or not str2:
            return 0.0
        return SequenceMatcher(None, str(str1).lower(), str(str2).lower()).ratio()

    def _generate_blocks(self, records: List[SourceRecord]) -> Dict[str, List[SourceRecord]]:
        """
        Implements a blocking strategy to optimize search space.
        Simple strategy: Block by first letter of 'name' attribute or 'entity_type'.
        """
        blocks = {}
        for record in records:
            # Blocking key: Entity Type + First char of Name (if exists)
            name = record.attributes.get('name', '')
            block_key = f"{record.entity_type}_{name[0].upper() if name else 'X'}"
            
            if block_key not in blocks:
                blocks[block_key] = []
            blocks[block_key].append(record)
        return blocks

    def find_matches(self, records: List[SourceRecord]) -> List[MatchCandidate]:
        """
        Runs matching algorithm on a batch of records.
        """
        candidates = []
        blocks = self._generate_blocks(records)
        
        for block_key, block_records in blocks.items():
            # Compare every pair in the block
            n = len(block_records)
            for i in range(n):
                for j in range(i + 1, n):
                    rec_a = block_records[i]
                    rec_b = block_records[j]
                    
                    # Calculate aggregate score based on key attributes
                    score = self._compute_record_similarity(rec_a, rec_b)
                    
                    if score >= self.threshold:
                        candidates.append(MatchCandidate(
                            record_a_id=rec_a.record_id,
                            record_b_id=rec_b.record_id,
                            score=score,
                            match_reasons=[f"High similarity ({score:.2f}) in block {block_key}"]
                        ))
                        
        return candidates

    def _compute_record_similarity(self, rec_a: SourceRecord, rec_b: SourceRecord) -> float:
        """
        Computes weighted average similarity across attributes.
        """
        # Attributes to compare
        attrs = ['name', 'email', 'phone', 'address']
        total_score = 0.0
        weights = 0.0
        
        # Weights definition
        attr_weights = {
            'name': 0.4,
            'email': 0.4, # Exact match usually expected, but fuzzy allowed here
            'phone': 0.1,
            'address': 0.1
        }
        
        for attr in attrs:
            val_a = rec_a.attributes.get(attr)
            val_b = rec_b.attributes.get(attr)
            
            if val_a and val_b:
                sim = self._calculate_similarity(val_a, val_b)
                weight = attr_weights.get(attr, 0.1)
                total_score += sim * weight
                weights += weight
                
        if weights == 0:
            return 0.0
            
        return total_score / weights
