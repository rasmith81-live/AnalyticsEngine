"""
ISO 20400 - Sustainable Procurement Module

ISO 20400 provides guidance on integrating sustainability into procurement processes.
Focuses on ethical sourcing, environmental responsibility, and social accountability.
"""

ISO_20400 = {
    "code": "ISO_20400",
    "name": "ISO 20400 - Sustainable Procurement",
    "description": "Sustainable and ethical procurement practices aligned with ISO 20400 standards",
    "is_active": True,
    "display_order": 10,
    "metadata_": {"value_chains": ["SUPPLY_CHAIN"], "industries": ["RETAIL", "MANUFACTURING", "HEALTHCARE", "FOOD_SERVICES"], "associated_object_models": ["SUPPLIER", "PRODUCT", "CONTRACT", "PURCHASE_ORDER"], "associated_kpis": ["carbon_footprint_of_procurement", "ethical_sourcing_index", "green_procurement_spend_share", "supplier_diversity_rate", "supply_chain_transparency_index", "sustainable_procurement_cost_savings"], "standards": ["ISO_20400"], "focus_areas": ["sustainability", "ethical_sourcing", "environmental_responsibility"]},
    "value_chains": ["SUPPLY_CHAIN"],
}
