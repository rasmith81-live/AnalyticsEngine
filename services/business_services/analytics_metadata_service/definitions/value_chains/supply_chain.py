"""
Supply Chain Management Value Chain

Used by: Retail, Manufacturing, Healthcare
"""

SUPPLY_CHAIN = {
    "code": "SUPPLY_CHAIN",
    "name": "Supply Chain Management",
    "display_name": "Supply Chain",
    "description": "End-to-end supply chain operations and optimization",
    "associated_modules": ["INVENTORY_MGMT", "LOGISTICS", "PROCUREMENT"],
    "metadata_": {
        "category": "cross_industry",
        "industries": ["RETAIL", "MANUFACTURING", "HEALTHCARE"],
        "display_order": 3,
        "is_active": True
    }
}
