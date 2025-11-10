"""
Sales Management Value Chain

Used by: Retail, Manufacturing, Financial Services, Technology
"""

from analytics_models import ValueChain

SALES_MANAGEMENT = ValueChain(
    name="Sales Management",
    code="SALES_MGMT",
    description="Sales pipeline, forecasting, and performance management",
    display_order=1,
    is_active=True,
    metadata_={
        "category": "cross_industry",
        "industries": ["RETAIL", "MANUFACTURING"],
        "modules": ["SALES_FORECASTING", "PIPELINE_MGMT", "SALES_ANALYTICS"]
    }
)
