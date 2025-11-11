"""
Order Fill Rate KPI Definition
"""

ORDER_FILL_RATE = {
    "code": "ORDER_FILL_RATE",
    "name": "Order Fill Rate",
    "display_name": "Order Fill Rate",
    "description": "The percentage of orders that are filled completely and on time. A high fill rate indicates good relationships with suppliers and efficient order processing.",
    "formula": "",
    "unit": "count",
    "category": "Sourcing",
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Order", "Supplier"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
