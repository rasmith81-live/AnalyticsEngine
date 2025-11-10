"""
Order Fulfillment Cycle Time KPI

SCOR Metric: RS.1.1
Performance Attribute: Responsiveness
Level: Level 1 - Strategic

Average time from order receipt to customer delivery

Formula:
AVG(Delivery Date - Order Receipt Date)

Calculation Details:

        Cycle Time = Time from order receipt to delivery
        Measured in business days or calendar days
        Includes: Order processing, picking, packing, shipping, delivery
        

Required Objects: Order, Shipment, Delivery
"""

from analytics_models import KPI

ORDER_FULFILLMENT_CYCLE_TIME = KPI(
    code="ORDER_FULFILLMENT_CYCLE_TIME",
    name="Order Fulfillment Cycle Time",
    category="Supply Chain Responsiveness",
    description="Average time from order receipt to customer delivery",
    
    formula="""
AVG(Delivery Date - Order Receipt Date)
    """,
    
    metadata_={
        # SCOR Framework Reference
        "scor_reference": {
            "metric_id": "RS.1.1",
            "performance_attribute": "Responsiveness",
            "level": "Level 1 - Strategic",
            "scor_version": "14.0"
        },
        
        # Required Business Objects
        "required_objects": ["Order", "Shipment", "Delivery"],
        
        # Module Assignment
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN"],
        
        # Calculation Configuration
        "unit": "days",
        "aggregation_methods": ["average", "median", "percentile_90"],
        "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
        
        # Dimensional Analysis
        "dimensions": ["region", "customer_segment", "product_line", "order_type", "priority"],
        
        # Benchmarks (SCOR Industry Standards)
        "target_benchmark": {
            "superior": 1.0,
            "advantage": 2.0,
            "parity": 3.0,
            "disadvantage": 5.0
        },
        
        # Calculation Details
        "calculation_detail": """

        Cycle Time = Time from order receipt to delivery
        Measured in business days or calendar days
        Includes: Order processing, picking, packing, shipping, delivery
        
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
