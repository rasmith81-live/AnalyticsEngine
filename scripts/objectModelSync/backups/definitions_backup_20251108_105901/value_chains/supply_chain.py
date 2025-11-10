"""
Supply Chain Management Value Chain

Used by: Retail, Manufacturing, Healthcare
"""

from analytics_models import ValueChain

SUPPLY_CHAIN = ValueChain(
    name="Supply Chain Management",
    code="SUPPLY_CHAIN",
    description="End-to-end supply chain operations and optimization",
    display_order=3,
    is_active=True,
    metadata_={
        "category": "cross_industry",
        "industries": ["RETAIL", "MANUFACTURING"],
        "modules": ["INVENTORY_MGMT", "LOGISTICS", "PROCUREMENT"]
    }
)
