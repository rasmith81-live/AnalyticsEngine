"""
Cost of Goods Sold KPI

SCOR Metric: CO.1.2
Performance Attribute: Costs
Level: Level 1 - Strategic

Direct costs attributable to production of goods sold

Formula:
SUM(Material Cost + Labor Cost + Manufacturing Overhead)

Calculation Details:

        COGS = Direct production costs
        - Material: Raw materials, components
        - Labor: Direct manufacturing labor
        - Overhead: Factory overhead allocated to production
        

Required Objects: Cost, Product, Production, Material
"""

from analytics_models import KPI

COST_OF_GOODS_SOLD = KPI(
    code="COST_OF_GOODS_SOLD",
    name="Cost of Goods Sold",
    category="Supply Chain Costs",
    description="Direct costs attributable to production of goods sold",
    
    formula="""
SUM(Material Cost + Labor Cost + Manufacturing Overhead)
    """,
    
    metadata_={
        # SCOR Framework Reference
        "scor_reference": {
            "metric_id": "CO.1.2",
            "performance_attribute": "Costs",
            "level": "Level 1 - Strategic",
            "scor_version": "14.0"
        },
        
        # Required Business Objects
        "required_objects": ["Cost", "Product", "Production", "Material"],
        
        # Module Assignment
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN"],
        
        # Calculation Configuration
        "unit": "dollars",
        "aggregation_methods": ["sum", "average"],
        "time_periods": ["monthly", "quarterly", "annually"],
        
        # Dimensional Analysis
        "dimensions": ["product_line", "facility", "cost_category"],
        
        # Benchmarks (SCOR Industry Standards)
        "target_benchmark": {
            "superior": "< 60% of revenue",
            "advantage": "60-70% of revenue",
            "parity": "70-80% of revenue",
            "disadvantage": "> 80% of revenue"
        },
        
        # Calculation Details
        "calculation_detail": """

        COGS = Direct production costs
        - Material: Raw materials, components
        - Labor: Direct manufacturing labor
        - Overhead: Factory overhead allocated to production
        
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
