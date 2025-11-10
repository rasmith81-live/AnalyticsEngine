"""
Downside Supply Chain Adaptability KPI

SCOR Metric: AG.1.2
Performance Attribute: Agility
Level: Level 1 - Strategic

Percentage reduction in cost for 20% decrease in delivered quantity

Formula:
(Cost Reduction / Original Cost) * 100 for 20% volume decrease

Calculation Details:

        Measures ability to reduce costs when demand drops
        Cost flexibility when volume decreases by 20%
        Includes: Variable costs, fixed cost reduction
        

Required Objects: Cost, Production, Capacity
"""

from analytics_models import KPI

DOWNSIDE_SUPPLY_CHAIN_ADAPTABILITY = KPI(
    code="DOWNSIDE_SUPPLY_CHAIN_ADAPTABILITY",
    name="Downside Supply Chain Adaptability",
    category="Supply Chain Agility",
    description="Percentage reduction in cost for 20% decrease in delivered quantity",
    
    formula="""
(Cost Reduction / Original Cost) * 100 for 20% volume decrease
    """,
    
    metadata_={
        # SCOR Framework Reference
        "scor_reference": {
            "metric_id": "AG.1.2",
            "performance_attribute": "Agility",
            "level": "Level 1 - Strategic",
            "scor_version": "14.0"
        },
        
        # Required Business Objects
        "required_objects": ["Cost", "Production", "Capacity"],
        
        # Module Assignment
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN"],
        
        # Calculation Configuration
        "unit": "percentage",
        "aggregation_methods": ["percentage"],
        "time_periods": ["quarterly", "annually"],
        
        # Dimensional Analysis
        "dimensions": ["product_line", "facility", "cost_center"],
        
        # Benchmarks (SCOR Industry Standards)
        "target_benchmark": {
            "superior": 15.0,
            "advantage": 12.0,
            "parity": 8.0,
            "disadvantage": 5.0
        },
        
        # Calculation Details
        "calculation_detail": """

        Measures ability to reduce costs when demand drops
        Cost flexibility when volume decreases by 20%
        Includes: Variable costs, fixed cost reduction
        
        """,
        
        # Data Quality
        "data_quality_requirements": {
            "completeness": 0.95,
            "accuracy": 0.98,
            "timeliness": "daily"
        },
        
        # Reporting
        "reporting_frequency": ["daily", "weekly", "monthly", "quarterly", "annually"],
        "dashboard_priority": "high",
        "executive_visibility": True
    }
)
