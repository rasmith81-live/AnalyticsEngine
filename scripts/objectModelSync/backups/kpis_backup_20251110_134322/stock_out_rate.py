"""
Stock-out Rate KPI Definition
"""

STOCK_OUT_RATE = {
    "code": "STOCK_OUT_RATE",
    "name": "Stock-out Rate",
    "display_name": "Stock-out Rate",
    "description": "The percentage of orders that cannot be fulfilled because the requested item is out of stock. A low stock-out rate indicates good inventory management and strong relationships with suppliers.",
    "formula": "",
    "unit": "count",
    "category": "Sourcing",
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Inventory", "Order", "Product", "Supplier"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
