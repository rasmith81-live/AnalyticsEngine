"""
Business Development Module

Used by: Sales Management value chain
Industries: Retail, Manufacturing, Financial Services, Technology
"""

from analytics_models import Module

BUSINESS_DEVELOPMENT = Module(
    name="Business Development",
    code="BUS_DEV",
    description="Business development activities including lead generation, opportunity management, and customer acquisition",
    display_order=2,
    is_active=True,
    metadata_={
        "value_chains": ["SALES_MGMT"],
        "industries": ["RETAIL", "MANUFACTURING", "FINANCIAL_SERVICES", "TECHNOLOGY"],
        "typical_object_models": ["LEAD", "OPPORTUNITY", "ACCOUNT"],
        "kpi_count": 60
    }
)
