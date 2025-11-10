"""
Sales Operations Module

Focuses on sales process optimization, data management, analytics, forecasting,
and operational support to drive sales efficiency and effectiveness.
"""

from analytics_models import Module

SALES_OPERATIONS = Module(
    name="Sales Operations",
    code="SALES_OPERATIONS",
    description="Sales process optimization, data management, analytics, and operational support",
    is_active=True,
    display_order=10,
    metadata_={
        "value_chains": ["SALES_MGMT", "OPERATIONS"],
        "industries": ["ALL"],
        "focus_areas": [
            "Sales Analytics & Reporting",
            "Sales Forecasting",
            "Territory & Quota Management",
            "Sales Process Optimization",
            "CRM & Data Management",
            "Performance Metrics",
            "Sales Compensation"
        ]
    }
)
