"""
Return on Supply Chain Fixed Assets KPI

SCOR Metric: PR.1.1
Performance Attribute: Profit
Level: Level 1 - Strategic

Return generated from supply chain fixed assets

Formula:
(Supply Chain Revenue - COGS - SC Operating Expense) / SC Fixed Assets * 100

Calculation Details:

        ROSCFA = Profitability of SC assets
        Numerator: SC contribution margin
        Denominator: SC fixed assets (property, plant, equipment)
        

Required Objects: Revenue, Cost, Asset
"""

from analytics_models import KPI

RETURN_ON_SUPPLY_CHAIN_FIXED_ASSETS = KPI(
    code="RETURN_ON_SUPPLY_CHAIN_FIXED_ASSETS",
    name="Return on Supply Chain Fixed Assets",
    category="Supply Chain Profit",
    description="Return generated from supply chain fixed assets",
    
    formula="""
(Supply Chain Revenue - COGS - SC Operating Expense) / SC Fixed Assets * 100
    """,
    
    metadata_={
        # SCOR Framework Reference
        "scor_reference": {
            "metric_id": "PR.1.1",
            "performance_attribute": "Profit",
            "level": "Level 1 - Strategic",
            "scor_version": "14.0"
        },
        
        # Required Business Objects
        "required_objects": ["Revenue", "Cost", "Asset"],
        
        # Module Assignment
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN"],
        
        # Calculation Configuration
        "unit": "percentage",
        "aggregation_methods": ["percentage"],
        "time_periods": ["quarterly", "annually"],
        
        # Dimensional Analysis
        "dimensions": ["facility", "asset_category"],
        
        # Benchmarks (SCOR Industry Standards)
        "target_benchmark": {
            "superior": 25.0,
            "advantage": 20.0,
            "parity": 15.0,
            "disadvantage": 10.0
        },
        
        # Calculation Details
        "calculation_detail": """

        ROSCFA = Profitability of SC assets
        Numerator: SC contribution margin
        Denominator: SC fixed assets (property, plant, equipment)
        
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
