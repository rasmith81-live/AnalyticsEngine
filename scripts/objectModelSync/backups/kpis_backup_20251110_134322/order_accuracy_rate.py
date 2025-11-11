"""
Order Accuracy Rate KPI Definition
"""

ORDER_ACCURACY_RATE = {
    "code": "ORDER_ACCURACY_RATE",
    "name": "Order Accuracy Rate",
    "display_name": "Order Accuracy Rate",
    "description": "The percentage of orders that are accurately fulfilled without errors, such as wrong items, wrong quantities, or damaged products. It helps assess the effectiveness of inventory management and order processing, and identify areas for improvement in the supply chain process.",
    "formula": "",
    "unit": "count",
    "category": "Inventory Management",
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Inventory", "Order", "Product"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
