"""
Supplier Rationalization KPI Definition
"""

SUPPLIER_RATIONALIZATION = {
    "code": "SUPPLIER_RATIONALIZATION",
    "name": "Supplier Rationalization",
    "display_name": "Supplier Rationalization",
    "description": "The process of analyzing and streamlining the supplier base to reduce complexity and costs.",
    "formula": "Qualitative Assessment Score based on Rationalization Criteria",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["average", "sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Supplier"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
