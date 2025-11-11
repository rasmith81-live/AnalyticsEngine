"""
Supplier Collaboration Level KPI Definition
"""

SUPPLIER_COLLABORATION_LEVEL = {
    "code": "SUPPLIER_COLLABORATION_LEVEL",
    "name": "Supplier Collaboration Level",
    "display_name": "Supplier Collaboration Level",
    "description": "The extent to which the buying organization works with suppliers to achieve mutual benefits.",
    "formula": "Qualitative Assessment Score based on Predefined Collaboration Criteria",
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
