from typing import List, Dict, Any
from ..intent_extractor import BusinessIntent

class PatternMatcher:
    """Matches business intent to Ontology Patterns."""
    
    def match_intent(self, intent: BusinessIntent) -> List[Dict[str, Any]]:
        """
        Matches intent to value chain patterns.
        """
        matches = []
        
        # Simple heuristic matching
        if "supply_chain" in intent.domain or "inventory" in intent.target_entities:
            matches.append({
                "pattern_id": "SCOR_Model",
                "name": "Supply Chain Operations Reference",
                "relevance_score": 0.95
            })
            
        if "sales" in intent.domain or "revenue" in intent.requested_metrics:
            matches.append({
                "pattern_id": "Sales_Pipeline",
                "name": "B2B Sales Pipeline",
                "relevance_score": 0.90
            })
            
        return matches

class DesignSuggester:
    """Generates design suggestions based on matched patterns."""
    
    def suggest_design(self, pattern_id: str) -> Dict[str, Any]:
        if pattern_id == "SCOR_Model":
            return {
                "entities": ["Product", "Warehouse", "Supplier"],
                "kpis": ["Inventory Turnover", "Perfect Order Fulfillment"]
            }
        elif pattern_id == "Sales_Pipeline":
            return {
                "entities": ["Lead", "Opportunity", "Customer"],
                "kpis": ["Win Rate", "Pipeline Velocity"]
            }
        return {}
