"""
Return on Working Capital KPI

SCOR Metric: AM.1.2
Performance Attribute: Asset Management
Level: Level 1 - Strategic

Return generated from working capital invested in supply chain

Formula:
(Supply Chain Revenue - COGS - SC Operating Expense) / (Inventory + AR - AP) * 100

Calculation Details:

        ROWC = Efficiency of working capital
        Numerator: SC contribution margin
        Denominator: Working capital (Inventory + Receivables - Payables)
        

Required Objects: Revenue, Cost, Inventory, AccountsReceivable, AccountsPayable
"""

from analytics_models import KPI

RETURN_ON_WORKING_CAPITAL = KPI(
    code="RETURN_ON_WORKING_CAPITAL",
    name="Return on Working Capital",
    category="Supply Chain Asset Management",
    description="Return generated from working capital invested in supply chain",
    
    formula="""
(Supply Chain Revenue - COGS - SC Operating Expense) / (Inventory + AR - AP) * 100
    """,
    
    metadata_={
        # SCOR Framework Reference
        "scor_reference": {
            "metric_id": "AM.1.2",
            "performance_attribute": "Asset Management",
            "level": "Level 1 - Strategic",
            "scor_version": "14.0"
        },
        
        # Required Business Objects
        "required_objects": ["Revenue", "Cost", "Inventory", "AccountsReceivable", "AccountsPayable"],
        
        # Module Assignment
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN"],
        
        # Calculation Configuration
        "unit": "percentage",
        "aggregation_methods": ["percentage"],
        "time_periods": ["quarterly", "annually"],
        
        # Dimensional Analysis
        "dimensions": ["product_line", "facility"],
        
        # Benchmarks (SCOR Industry Standards)
        "target_benchmark": {
            "superior": 50.0,
            "advantage": 35.0,
            "parity": 25.0,
            "disadvantage": 15.0
        },
        
        # Calculation Details
        "calculation_detail": """

        ROWC = Efficiency of working capital
        Numerator: SC contribution margin
        Denominator: Working capital (Inventory + Receivables - Payables)
        
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
