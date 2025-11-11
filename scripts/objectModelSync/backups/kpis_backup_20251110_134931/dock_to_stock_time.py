"""
Dock to Stock Time

The time it takes for goods to move from the receiving dock to available inventory.
"""

DOCK_TO_STOCK_TIME = {
    "code": "DOCK_TO_STOCK_TIME",
    "name": "Dock to Stock Time",
    "description": "The time it takes for goods to move from the receiving dock to available inventory.",
    "formula": "Total Dock to Stock Time / Total Number of Shipments",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Dock to Stock Time to be added.",
    "trend_analysis": "Trend analysis to be defined.",
    "diagnostic_questions": """
* What factors are influencing this metric?
* Are there any anomalies in the data?
    """,
    "actionable_tips": """
* Monitor this KPI regularly
* Set appropriate targets and thresholds
    """,
    "visualization_suggestions": """
* Line chart for time series analysis
* Bar chart for comparisons
    """,
    "risk_warnings": "* Monitor for significant deviations from expected values",
    "tracking_tools": "* CRM or analytics platform",
    "integration_points": "* Integrate with related business metrics",
    "change_impact_analysis": "Changes in this KPI may impact related business processes.",
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "Shipment"], "last_validated": "2025-11-10T13:43:23.448867"},
    "required_objects": [],
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
    "sample_data": {
        "time_series": {
                "dates": [
                        "2024-12-15",
                        "2025-01-14",
                        "2025-02-13",
                        "2025-03-15",
                        "2025-04-14",
                        "2025-05-14",
                        "2025-06-13",
                        "2025-07-13",
                        "2025-08-12",
                        "2025-09-11",
                        "2025-10-11",
                        "2025-11-10"
                ],
                "values": [
                        151,
                        135,
                        137,
                        178,
                        172,
                        167,
                        166,
                        150,
                        145,
                        144,
                        175,
                        133
                ],
                "unit": "count"
        },
        "current": {
                "value": 133,
                "unit": "count",
                "change": -42,
                "change_percent": -24.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 154.42,
                "min": 133,
                "max": 178,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 23.95,
                        "percentage": 18.0
                },
                {
                        "category": "Category B",
                        "value": 35.49,
                        "percentage": 26.7
                },
                {
                        "category": "Category C",
                        "value": 19.25,
                        "percentage": 14.5
                },
                {
                        "category": "Category D",
                        "value": 13.5,
                        "percentage": 10.2
                },
                {
                        "category": "Other",
                        "value": 40.81,
                        "percentage": 30.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.448867",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Dock to Stock Time"
        }
    },
}
