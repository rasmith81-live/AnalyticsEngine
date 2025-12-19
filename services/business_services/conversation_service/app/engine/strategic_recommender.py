from typing import List, Dict, Any, Optional
from pydantic import BaseModel

# In a real microservices setup, we would import a client or define models here.
# For simplicity, we redefine necessary models or fetch them.
class ValueChainSet(BaseModel):
    industry_code: str
    name: str
    processes: List[str]
    activities: List[str]

class StrategyScore(BaseModel):
    value_chain_name: str
    relevance_score: float
    rationale: str

class StrategicRecommender:
    """
    Maps business context to recommended value chains and strategies.
    Uses Metadata Ingestion Service for industry knowledge.
    """
    
    def __init__(self, metadata_client=None):
        self.metadata_client = metadata_client
        # Cache for demo performance
        self._cache_vc = {}
        
    async def _get_value_chain_set(self, code: str) -> Optional[ValueChainSet]:
        """Fetch from Metadata Service (Mocked for now)."""
        if code in self._cache_vc:
            return self._cache_vc[code]
            
        # Placeholder for external API call:
        # vc = await self.metadata_client.get_industry_value_chain(code)
        
        # Mock Data (replicating what was in industry_knowledge.py for continuity)
        if code == "62":
            vc = ValueChainSet(
                industry_code="62",
                name="Standard Model for Healthcare",
                processes=["Patient Admission", "Care Delivery", "Discharge Planning", "Revenue Cycle Management"],
                activities=["Triage", "Diagnosis", "Treatment", "Billing", "Claims Processing"]
            )
        elif code == "31-33":
            vc = ValueChainSet(
                industry_code="31-33",
                name="Standard Model for Supply Chain",
                processes=["Procurement", "Production", "Quality Control", "Logistics"],
                activities=["Sourcing", "Assembly", "Testing", "Shipping"]
            )
        else:
            vc = None
            
        if vc:
            self._cache_vc[code] = vc
        return vc
        
    async def recommend_value_chains(self, business_description: str, use_cases: List[str]) -> List[StrategyScore]:
        """
        Analyzes description and use cases to recommend Value Chain Sets.
        """
        recommendations = []
        
        # Simple keyword-based heuristic for demo purposes
        # In production, this would use vector embeddings and semantic search
        
        description_lower = business_description.lower()
        use_cases_lower = " ".join(use_cases).lower()
        
        # Check Healthcare
        healthcare_score = 0.0
        if "patient" in description_lower or "hospital" in description_lower:
            healthcare_score += 0.5
        if "care" in use_cases_lower or "clinical" in use_cases_lower:
            healthcare_score += 0.4
            
        if healthcare_score > 0.3:
            vc = await self._get_value_chain_set("62")
            if vc:
                recommendations.append(StrategyScore(
                    value_chain_name=vc.name,
                    relevance_score=min(1.0, healthcare_score),
                    rationale="Matched terms related to healthcare delivery and patient management."
                ))
                
        # Check Supply Chain / Manufacturing
        sc_score = 0.0
        if "manufacturing" in description_lower or "factory" in description_lower:
            sc_score += 0.5
        if "logistics" in use_cases_lower or "inventory" in use_cases_lower:
            sc_score += 0.4
            
        if sc_score > 0.3:
            vc = await self._get_value_chain_set("31-33")
            if vc:
                recommendations.append(StrategyScore(
                    value_chain_name=vc.name,
                    relevance_score=min(1.0, sc_score),
                    rationale="Matched terms related to production, logistics, and inventory."
                ))
                
        # Sort by score
        recommendations.sort(key=lambda x: x.relevance_score, reverse=True)
        return recommendations

    def get_strategy_alignment(self, industry_code: str, strategy_type: str) -> float:
        """
        Calculates alignment score between an industry and a strategy type.
        Strategy types: "Operational Efficiency", "Growth", "Risk Management"
        """
        # Matrix of Industry vs Strategy alignment (Mock)
        alignment_matrix = {
            "62": { # Healthcare
                "Operational Efficiency": 0.9,
                "Growth": 0.7,
                "Risk Management": 0.95
            },
            "31-33": { # Manufacturing
                "Operational Efficiency": 0.95,
                "Growth": 0.8,
                "Risk Management": 0.6
            }
        }
        
        industry_strategies = alignment_matrix.get(industry_code, {})
        return industry_strategies.get(strategy_type, 0.5)
