"""
Picking Accuracy

The percentage of orders picked without errors from inventory.
"""

PICKING_ACCURACY = {
    "code": "PICKING_ACCURACY",
    "name": "Picking Accuracy",
    "description": "The percentage of orders picked without errors from inventory.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Picking Accuracy to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Inventory", "Order"], "last_validated": "2025-11-10T13:43:23.928272"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
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
                        849.86,
                        788.37,
                        872.41,
                        799.58,
                        830.47,
                        828.13,
                        872.19,
                        875.17,
                        904.13,
                        781.3,
                        868.28,
                        798.51
                ],
                "unit": "units"
        },
        "current": {
                "value": 798.51,
                "unit": "units",
                "change": -69.77,
                "change_percent": -8.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 839.03,
                "min": 781.3,
                "max": 904.13,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 191.29,
                        "percentage": 24.0
                },
                {
                        "category": "Category B",
                        "value": 129.92,
                        "percentage": 16.3
                },
                {
                        "category": "Category C",
                        "value": 79.23,
                        "percentage": 9.9
                },
                {
                        "category": "Category D",
                        "value": 44.71,
                        "percentage": 5.6
                },
                {
                        "category": "Other",
                        "value": 353.36,
                        "percentage": 44.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.928272",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Picking Accuracy"
        }
    },
}
