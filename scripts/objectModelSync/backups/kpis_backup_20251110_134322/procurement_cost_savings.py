"""
Procurement Cost Savings KPI Definition
"""

PROCUREMENT_COST_SAVINGS = {
    "code": "PROCUREMENT_COST_SAVINGS",
    "name": "Procurement Cost Savings",
    "display_name": "Procurement Cost Savings",
    "description": "The total cost savings achieved through the procurement process, including negotiated discounts, bulk purchasing, and efficient supply chain management. Reflects the direct financial impact of procurement activities and supports budget optimization.",
    "formula": "Baseline Spend - Current Spend",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["sum", "average"],
    "time_periods": ["monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Supplier", "PurchaseOrder", "Contract"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
