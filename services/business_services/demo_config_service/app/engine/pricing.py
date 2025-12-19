
"""
Pricing Calculator Engine
"""
from typing import Dict, Any, List
import math

class PricingCalculator:
    """Calculates pricing and estimates for service proposals."""
    
    def __init__(self):
        # Base constants could be loaded from config
        self.base_license_fee = 5000.00
        self.user_license_fee = 100.00
        self.infrastructure_base_cost = 500.00
        
    def calculate_proposal(
        self,
        num_objects: int,
        integration_method: str,
        hourly_rate: float
    ) -> Dict[str, Any]:
        """
        Calculate proposal estimates.
        
        Args:
            num_objects: Number of data objects/entities
            integration_method: 'batch' or 'realtime'
            hourly_rate: Implementation hourly rate
            
        Returns:
            Dictionary with estimated costs and timeline
        """
        # Effort estimation logic
        base_hours_per_object = 8 if integration_method == "batch" else 12
        complexity_factor = 1.2 # Buffer for testing/management
        
        estimated_hours = math.ceil(num_objects * base_hours_per_object * complexity_factor)
        
        # Minimum engagement
        if estimated_hours < 40:
            estimated_hours = 40
            
        # Cost calculation
        implementation_cost = estimated_hours * hourly_rate
        
        # Timeline estimation (assuming 2 FTEs working in parallel)
        weekly_capacity = 80 # 40 hours * 2 people
        timeline_weeks = math.ceil(estimated_hours / weekly_capacity)
        
        if timeline_weeks < 4:
            timeline_weeks = 4 # Minimum timeline for process
            
        return {
            "estimated_hours": estimated_hours,
            "estimated_cost": implementation_cost,
            "timeline_weeks": timeline_weeks,
            "infrastructure_monthly": self._calculate_infra_cost(num_objects),
            "license_annual": self.base_license_fee
        }
        
    def _calculate_infra_cost(self, num_objects: int) -> float:
        """Estimate monthly infrastructure cost based on scale."""
        # Simple tiered model
        if num_objects < 10:
            return self.infrastructure_base_cost
        elif num_objects < 50:
            return self.infrastructure_base_cost * 2
        else:
            return self.infrastructure_base_cost * 5
