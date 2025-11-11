"""
Average Delivery Distance KPI Definition
"""

DELIVERY_DISTANCE = {
    "code": "DELIVERY_DISTANCE",
    "name": "Average Delivery Distance",
    "display_name": "Average Delivery Distance",
    "description": "The average distance covered per delivery.",
    "formula": "Total Distance for All Deliveries / Number of Deliveries",
    "unit": "count",
    "category": "Logistics",
    "aggregation_methods": ["average", "sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Delivery"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
