"""
Delivery Route Optimization Rate KPI Definition
"""

DELIVERY_ROUTE_OPTIMIZATION_RATE = {
    "code": "DELIVERY_ROUTE_OPTIMIZATION_RATE",
    "name": "Delivery Route Optimization Rate",
    "display_name": "Delivery Route Optimization Rate",
    "description": "The percentage of delivery routes that are optimized for cost, time, and fuel efficiency.",
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
