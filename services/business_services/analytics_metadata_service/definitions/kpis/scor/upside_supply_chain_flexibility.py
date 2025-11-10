"""
Upside Supply Chain Flexibility KPI

SCOR Metric: AG.1.1
Performance Attribute: Agility
Level: Level 1 - Strategic

Number of days to achieve 20% increase in delivered quantity

Formula:
Days to achieve 20% sustained increase

Calculation Details:

        Measures ability to respond to demand spikes
        Time to ramp up production/delivery by 20%
        Sustained increase (not one-time spike)
        

Required Objects: Capacity, Production, Inventory, Supplier
"""

from analytics_models import KPI

UPSIDE_SUPPLY_CHAIN_FLEXIBILITY = KPI(
    code="UPSIDE_SUPPLY_CHAIN_FLEXIBILITY",
    name="Upside Supply Chain Flexibility",
    category="Supply Chain Agility",
    description="Number of days to achieve 20% increase in delivered quantity",
    
    formula="""
Days to achieve 20% sustained increase
    """,
    
    metadata_={
        # SCOR Framework Reference
        "scor_reference": {
            "metric_id": "AG.1.1",
            "performance_attribute": "Agility",
            "level": "Level 1 - Strategic",
            "scor_version": "14.0"
        },
        
        # Required Business Objects
        "required_objects": ["Capacity", "Production", "Inventory", "Supplier"],
        
        # Module Assignment
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN"],
        
        # Calculation Configuration
        "unit": "days",
        "aggregation_methods": ["average", "min"],
        "time_periods": ["quarterly", "annually"],
        
        # Dimensional Analysis
        "dimensions": ["product_line", "facility", "supplier"],
        
        # Benchmarks (SCOR Industry Standards)
        "target_benchmark": {
            "superior": 7,
            "advantage": 14,
            "parity": 30,
            "disadvantage": 60
        },
        
        # Calculation Details
        "calculation_detail": """

        Measures ability to respond to demand spikes
        Time to ramp up production/delivery by 20%
        Sustained increase (not one-time spike)
        
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
