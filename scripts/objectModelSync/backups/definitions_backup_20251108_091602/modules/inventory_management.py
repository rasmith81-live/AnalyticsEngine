"""
Inventory Management Module

Used by: Supply Chain value chain
Industries: Retail, Manufacturing
"""

from analytics_models import Module

INVENTORY_MANAGEMENT = Module(
    name="Inventory Management",
    code="INVENTORY_MGMT",
    description="Inventory tracking, optimization, and replenishment",
    display_order=1,
    is_active=True,
    metadata_={
        "value_chains": ["SUPPLY_CHAIN"],
        "industries": ["RETAIL", "MANUFACTURING"],
        "typical_object_models": ["PRODUCT", "WAREHOUSE"],
        "typical_kpis": ["inventory_turnover", "stockout_rate", "carrying_cost"]
    }
)
