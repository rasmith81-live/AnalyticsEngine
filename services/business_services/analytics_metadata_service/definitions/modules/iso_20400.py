"""
ISO 20400 - Sustainable Procurement Module

ISO 20400 provides guidance on integrating sustainability into procurement processes.
Focuses on ethical sourcing, environmental responsibility, and social accountability.
"""

from analytics_models import Module

ISO_20400 = Module(
    name="ISO 20400 - Sustainable Procurement",
    code="ISO_20400",
    description="Sustainable and ethical procurement practices aligned with ISO 20400 standards",
    display_order=10,
    is_active=True,
    metadata_={
        "value_chains": ["SUPPLY_CHAIN"],
        "industries": ["RETAIL", "MANUFACTURING", "HEALTHCARE", "FOOD_SERVICES"],
        "associated_object_models": ["SUPPLIER", "PRODUCT", "CONTRACT", "PURCHASE_ORDER"],
        "associated_kpis": [
            "carbon_footprint_of_procurement",
            "ethical_sourcing_index",
            "green_procurement_spend_share",
            "supplier_diversity_rate",
            "supply_chain_transparency_index",
            "sustainable_procurement_cost_savings"
        ],
        "standards": ["ISO_20400"],
        "focus_areas": ["sustainability", "ethical_sourcing", "environmental_responsibility"]
    }
)
