"""
Buyer Efficiency KPI Definition
"""

BUYER_EFFICIENCY = {
    "code": "BUYER_EFFICIENCY",
    "name": "Buyer Efficiency",
    "display_name": "Buyer Efficiency",
    "description": "The number of purchase orders processed per buyer, indicating the efficiency of the",
    "formula": "Total Orders Processed or Cost Savings / Number of Buyers",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Employee", "Order", "PurchaseOrder"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
