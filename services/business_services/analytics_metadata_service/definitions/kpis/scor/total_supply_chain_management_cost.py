"""
Total Supply Chain Management Cost KPI

SCOR Metric: CO.1.1
Performance Attribute: Costs
Level: Level 1 - Strategic

Sum of all costs to plan, source, make, deliver, and return

Formula:
SUM(Plan Cost + Source Cost + Make Cost + Deliver Cost + Return Cost)

Calculation Details:

        Total SC Cost = All supply chain costs
        - Plan: Planning, forecasting, S&OP
        - Source: Procurement, supplier management
        - Make: Manufacturing, production
        - Deliver: Warehousing, transportation, order management
        - Return: Reverse logistics, warranty
        

Required Objects: Cost, Activity, CostCenter
"""

from analytics_models import KPI

TOTAL_SUPPLY_CHAIN_MANAGEMENT_COST = KPI(
    code="TOTAL_SUPPLY_CHAIN_MANAGEMENT_COST",
    name="Total Supply Chain Management Cost",
    category="Supply Chain Costs",
    description="Sum of all costs to plan, source, make, deliver, and return",
    
    formula="""
SUM(Plan Cost + Source Cost + Make Cost + Deliver Cost + Return Cost)
    """,
    
    metadata_={
        # SCOR Framework Reference
        "scor_reference": {
            "metric_id": "CO.1.1",
            "performance_attribute": "Costs",
            "level": "Level 1 - Strategic",
            "scor_version": "14.0"
        },
        
        # Required Business Objects
        "required_objects": ["Cost", "Activity", "CostCenter"],
        
        # Module Assignment
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN"],
        
        # Calculation Configuration
        "unit": "dollars",
        "aggregation_methods": ["sum", "average"],
        "time_periods": ["monthly", "quarterly", "annually"],
        
        # Dimensional Analysis
        "dimensions": ["process", "cost_center", "product_line", "facility"],
        
        # Benchmarks (SCOR Industry Standards)
        "target_benchmark": {
            "superior": "< 5% of revenue",
            "advantage": "5-7% of revenue",
            "parity": "7-10% of revenue",
            "disadvantage": "> 10% of revenue"
        },
        
        # Calculation Details
        "calculation_detail": """

        Total SC Cost = All supply chain costs
        - Plan: Planning, forecasting, S&OP
        - Source: Procurement, supplier management
        - Make: Manufacturing, production
        - Deliver: Warehousing, transportation, order management
        - Return: Reverse logistics, warranty
        
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
