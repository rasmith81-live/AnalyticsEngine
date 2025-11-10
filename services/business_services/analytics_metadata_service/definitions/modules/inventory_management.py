"""
Inventory Management Module

Used by: Supply Chain value chain
Industries: Retail, Manufacturing
"""

INVENTORY_MANAGEMENT = {
    "code": "INVENTORY_MGMT",
    "name": "Inventory Management",
    "description": "Inventory tracking, optimization, and replenishment",
    "is_active": True,
    "display_order": 1,
    "metadata_": {"value_chains": ["SUPPLY_CHAIN"], "industries": ["RETAIL", "MANUFACTURING"], "associated_object_models": ["PRODUCT", "WAREHOUSE"], "associated_kpis": ["backorder_level", "carrying_cost", "carrying_cost_of_inventory", "cost_of_carry", "cost_per_order_picked", "days_of_inventory", "dock_to_stock_time", "equipment_utilization_rate", "excess_inventory_rate", "fill_rate", "fill_ratefulfillment_cost_per_order", "inbound_orders_processed_per_hour", "internal_order_cycle_time", "inventory_accuracy", "inventory_health_index", "inventory_to_sales_ratio", "inventory_turnover_rate", "labor_cost_per_picking_hour", "loading_efficiency", "on_time_shipment_rate", "order_accuracy_rate", "order_cycle_time", "order_lead_time", "order_picking_accuracy_rate", "order_value_aov", "outbound_orders_processed_per_hour", "packing_efficiency", "picking_productivity", "putaway_time", "quality_inspection_rate", "receiving_efficiency", "returns_processing_efficiency", "shipping_accuracy", "shrinkage_rate", "stock_rotation_efficiency", "stockout_frequency", "stockout_rate", "time_to_pick", "time_to_receive", "time_to_ship", "training_hours_per_employee", "value_of_backorders", "warehouse_capacity", "warehouse_energy_costs_per_square_foot", "warehouse_labor_efficiency", "warehouse_operating_costs"]},
    "value_chains": ["SUPPLY_CHAIN"],
}
