"""
Average Sales Pitch Length KPI Definition
"""

SALES_PITCH_LENGTH = {
    "code": "SALES_PITCH_LENGTH",
    "name": "Average Sales Pitch Length",
    "display_name": "Average Sales Pitch Length",
    "description": "The average duration of sales pitches or presentations, which can influence customer engagement and decision-making.",
    "formula": "Total Duration of All Sales Pitches / Number of Sales Pitches",
    "unit": "count",
    "category": "Business Development",
    "aggregation_methods": ["average", "sum", "count"],
    "time_periods": ["custom"],
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Customer"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
