"""
Demand Forecast Accuracy KPI Definition
"""

DEMAND_FORECAST_ACCURACY = {
    "code": "DEMAND_FORECAST_ACCURACY",
    "name": "Demand Forecast Accuracy",
    "display_name": "Demand Forecast Accuracy",
    "description": "The accuracy of prediction for future demand compared to actual demand, impacting inventory levels and customer satisfaction.",
    "formula": "",
    "unit": "count",
    "category": "Iso 22004",
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["Customer", "Inventory"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
