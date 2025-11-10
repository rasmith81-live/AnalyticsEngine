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
        "associated_object_models": ["PRODUCT", "WAREHOUSE"],
        "associated_kpis": [
            "backorder_level",
            "carrying_cost",
            "carrying_cost_of_inventory",
            "cost_of_carry",
            "cost_per_order_picked",
            "days_of_inventory",
            "dock_to_stock_time",
            "equipment_utilization_rate",
            "excess_inventory_rate",
            "fill_rate"
            # ... and 37 more
        ]
    }
)
