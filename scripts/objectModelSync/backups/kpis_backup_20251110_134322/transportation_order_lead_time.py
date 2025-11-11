"""
Transportation Order Lead Time KPI Definition
"""

TRANSPORTATION_ORDER_LEAD_TIME = {
    "code": "TRANSPORTATION_ORDER_LEAD_TIME",
    "name": "Transportation Order Lead Time",
    "display_name": "Transportation Order Lead Time",
    "description": "The time from placing a transport order to the execution of the shipment.",
    "formula": "Average Time from Transportation Order Placement to Shipment Movement",
    "unit": "count",
    "category": "Logistics",
    "aggregation_methods": ["average"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Lead", "Order", "PurchaseOrder", "Shipment"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
