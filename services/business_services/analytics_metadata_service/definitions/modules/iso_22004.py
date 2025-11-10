"""
ISO 22004 - Food Safety Management Systems Module

ISO 22004 provides guidance on the application of ISO 22000 for food safety management.
Focuses on supply chain management, quality control, and food safety compliance.
"""

ISO_22004 = {
    "code": "ISO_22004",
    "name": "ISO 22004 - Food Safety Management",
    "description": "Food safety management and supply chain optimization aligned with ISO 22004 standards",
    "is_active": True,
    "display_order": 11,
    "metadata_": {"value_chains": ["SUPPLY_CHAIN"], "industries": ["FOOD_SERVICES", "MANUFACTURING", "RETAIL", "HEALTHCARE"], "associated_object_models": ["SUPPLIER", "PRODUCT", "INVENTORY", "WAREHOUSE", "SHIPMENT"], "associated_kpis": ["cash_to_cash_cycle_time", "demand_forecast_accuracy", "inventory_turnover_ratio", "perfect_order_rate", "supplier_on_time_delivery_rate", "supply_chain_resilience_index", "warehouse_utilization_rate"], "standards": ["ISO_22004", "ISO_22000"], "focus_areas": ["food_safety", "supply_chain_management", "quality_control", "traceability"]},
    "value_chains": ["SUPPLY_CHAIN"],
}
