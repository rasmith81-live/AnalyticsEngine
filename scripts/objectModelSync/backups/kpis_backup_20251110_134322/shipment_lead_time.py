"""
Shipment Lead Time KPI Definition
"""

SHIPMENT_LEAD_TIME = {
    "code": "SHIPMENT_LEAD_TIME",
    "name": "Shipment Lead Time",
    "display_name": "Shipment Lead Time",
    "description": "The time it takes for a shipment to be delivered from the time it is ordered. A shorter lead time indicates more efficient transportation operations.",
    "formula": "Average Time from Shipment Ready to Delivery",
    "unit": "count",
    "category": "Logistics",
    "aggregation_methods": ["average"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Delivery", "Lead", "Order", "PurchaseOrder", "Shipment"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
