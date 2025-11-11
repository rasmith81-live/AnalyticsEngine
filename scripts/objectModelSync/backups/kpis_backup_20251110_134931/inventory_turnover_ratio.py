"""
Inventory Turnover Ratio

The rate at which inventory is used and replaced over a certain period.
"""

INVENTORY_TURNOVER_RATIO = {
    "code": "INVENTORY_TURNOVER_RATIO",
    "name": "Inventory Turnover Ratio",
    "description": "The rate at which inventory is used and replaced over a certain period.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Inventory Turnover Ratio to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Inventory"], "last_validated": "2025-11-10T13:43:23.557909"},
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
                        69.13,
                        60.73,
                        59.83,
                        55.68,
                        66.83,
                        57.03,
                        54.55,
                        56.61,
                        63.05,
                        59.34,
                        68.05,
                        64.31
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.31,
                "unit": "%",
                "change": -3.74,
                "change_percent": -5.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 61.26,
                "min": 54.55,
                "max": 69.13,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 17.75,
                        "percentage": 27.6
                },
                {
                        "category": "Category B",
                        "value": 12.64,
                        "percentage": 19.7
                },
                {
                        "category": "Category C",
                        "value": 8.98,
                        "percentage": 14.0
                },
                {
                        "category": "Category D",
                        "value": 3.01,
                        "percentage": 4.7
                },
                {
                        "category": "Other",
                        "value": 21.93,
                        "percentage": 34.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.557909",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Inventory Turnover Ratio"
        }
    },
}
