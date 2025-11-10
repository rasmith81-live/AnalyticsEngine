"""
Cash-to-Cash Cycle Time KPI

SCOR Metric: AM.1.1
Performance Attribute: Asset Management
Level: Level 1 - Strategic

Time between paying suppliers and receiving payment from customers

Formula:
Days Inventory Outstanding + Days Sales Outstanding - Days Payable Outstanding

Calculation Details:

        C2C = Working capital efficiency
        DIO: Avg days inventory held
        DSO: Avg days to collect receivables
        DPO: Avg days to pay suppliers
        Lower is better (faster cash conversion)
        

Required Objects: Inventory, Payment, Receipt, Invoice
"""

from analytics_models import KPI

CASH_TO_CASH_CYCLE_TIME = KPI(
    code="CASH_TO_CASH_CYCLE_TIME",
    name="Cash-to-Cash Cycle Time",
    category="Supply Chain Asset Management",
    description="Time between paying suppliers and receiving payment from customers",
    
    formula="""
Days Inventory Outstanding + Days Sales Outstanding - Days Payable Outstanding
    """,
    
    metadata_={
        # SCOR Framework Reference
        "scor_reference": {
            "metric_id": "AM.1.1",
            "performance_attribute": "Asset Management",
            "level": "Level 1 - Strategic",
            "scor_version": "14.0"
        },
        
        # Required Business Objects
        "required_objects": ["Inventory", "Payment", "Receipt", "Invoice"],
        
        # Module Assignment
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN"],
        
        # Calculation Configuration
        "unit": "days",
        "aggregation_methods": ["average"],
        "time_periods": ["monthly", "quarterly", "annually"],
        
        # Dimensional Analysis
        "dimensions": ["product_line", "customer_segment", "supplier"],
        
        # Benchmarks (SCOR Industry Standards)
        "target_benchmark": {
            "superior": 30,
            "advantage": 45,
            "parity": 60,
            "disadvantage": 90
        },
        
        # Calculation Details
        "calculation_detail": """

        C2C = Working capital efficiency
        DIO: Avg days inventory held
        DSO: Avg days to collect receivables
        DPO: Avg days to pay suppliers
        Lower is better (faster cash conversion)
        
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
