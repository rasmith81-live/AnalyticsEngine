"""
Damage-Free Delivery Rate KPI Definition
"""

DAMAGE_FREE_DELIVERY_RATE = {
    "code": "DAMAGE_FREE_DELIVERY_RATE",
    "name": "Damage-Free Delivery Rate",
    "display_name": "Damage-Free Delivery Rate",
    "description": "The percentage of deliveries made without any damage to the goods.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Delivery"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
