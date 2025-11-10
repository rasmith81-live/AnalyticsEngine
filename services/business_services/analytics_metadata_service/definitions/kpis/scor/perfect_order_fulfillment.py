"""
Perfect Order Fulfillment KPI

SCOR Metric: RL.1.1
Performance Attribute: Reliability
Level: Level 1 - Strategic

Percentage of orders delivered on time, complete, damage-free, with correct documentation

Formula:
(Perfect Orders / Total Orders) * 100

Calculation Details:

        Perfect Order = Order that meets ALL criteria:
        - Delivered on time (by customer requested date)
        - Complete (all items, correct quantities)
        - Damage-free (no defects, proper condition)
        - Correct documentation (invoice, packing slip, etc.)
        

Required Objects: Order, Shipment, Delivery, OrderLine
"""

from analytics_models import KPI

PERFECT_ORDER_FULFILLMENT = KPI(
    code="PERFECT_ORDER_FULFILLMENT",
    name="Perfect Order Fulfillment",
    category="Supply Chain Reliability",
    description="Percentage of orders delivered on time, complete, damage-free, with correct documentation",
    
    formula="""
(Perfect Orders / Total Orders) * 100
    """,
    
    metadata_={
        # SCOR Framework Reference
        "scor_reference": {
            "metric_id": "RL.1.1",
            "performance_attribute": "Reliability",
            "level": "Level 1 - Strategic",
            "scor_version": "14.0"
        },
        
        # Required Business Objects
        "required_objects": ["Order", "Shipment", "Delivery", "OrderLine"],
        
        # Module Assignment
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN"],
        
        # Calculation Configuration
        "unit": "percentage",
        "aggregation_methods": ["percentage"],
        "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
        
        # Dimensional Analysis
        "dimensions": ["region", "customer_segment", "product_line", "facility", "carrier"],
        
        # Benchmarks (SCOR Industry Standards)
        "target_benchmark": {
            "superior": 99.0,
            "advantage": 95.0,
            "parity": 90.0,
            "disadvantage": 85.0
        },
        
        # Calculation Details
        "calculation_detail": """

        Perfect Order = Order that meets ALL criteria:
        - Delivered on time (by customer requested date)
        - Complete (all items, correct quantities)
        - Damage-free (no defects, proper condition)
        - Correct documentation (invoice, packing slip, etc.)
        
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
