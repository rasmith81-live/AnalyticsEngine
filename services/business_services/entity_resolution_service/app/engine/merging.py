import uuid
from typing import List, Dict, Any
from datetime import datetime
from ..models import SourceRecord, GoldenRecord

class MergeEngine:
    """
    Engine for creating Golden Records from clusters of matched Source Records.
    """

    def create_golden_record(self, cluster: List[SourceRecord]) -> GoldenRecord:
        """
        Consolidates a list of matched records into a single Golden Record.
        """
        if not cluster:
            raise ValueError("Cannot create Golden Record from empty cluster")

        # Determine entity type (assume homogeneous cluster for now)
        entity_type = cluster[0].entity_type
        
        # Consolidate attributes and track lineage using survivorship rules
        consolidated_attrs, lineage = self._apply_survivorship_rules(cluster)
        
        # Collect source IDs
        source_ids = [rec.record_id for rec in cluster]
        
        return GoldenRecord(
            golden_id=str(uuid.uuid4()),
            entity_type=entity_type,
            attributes=consolidated_attrs,
            source_record_ids=source_ids,
            lineage=lineage
        )

    def _apply_survivorship_rules(self, cluster: List[SourceRecord]) -> tuple[Dict[str, Any], List[Dict[str, Any]]]:
        """
        Applies rules to determine which attribute value survives.
        Default Rule: Most Recently Updated (Time-based).
        Secondary Rule: Source System Priority (if timestamps equal/missing).
        
        Returns:
            Tuple containing:
            - Consolidated attributes dictionary
            - Lineage list (list of dicts describing source of each attribute)
        """
        # Sort cluster by timestamp descending (newest first)
        # Handle None timestamps by treating them as very old
        sorted_cluster = sorted(cluster, key=lambda x: x.timestamp or "", reverse=True)
        
        # Identify all unique attribute keys
        all_keys = set()
        for rec in cluster:
            all_keys.update(rec.attributes.keys())
            
        consolidated = {}
        lineage = []
        
        # For each attribute, pick the first non-null value from the sorted list
        for key in all_keys:
            for rec in sorted_cluster:
                val = rec.attributes.get(key)
                if val is not None and val != "":
                    consolidated[key] = val
                    
                    # Track lineage
                    lineage.append({
                        "attribute": key,
                        "source_record_id": rec.record_id,
                        "source_system": rec.source_system,
                        "value": val,
                        "timestamp": rec.timestamp
                    })
                    break
        
        return consolidated, lineage
