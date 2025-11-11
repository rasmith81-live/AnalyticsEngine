"""
Packing Error Rate

The ratio of incorrectly packed items to the total number of items packed, highlighting the accuracy of the packing process.
"""

PACKING_ERROR_RATE = {
    "code": "PACKING_ERROR_RATE",
    "name": "Packing Error Rate",
    "description": "The ratio of incorrectly packed items to the total number of items packed, highlighting the accuracy of the packing process.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Error Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Order", "Product"], "last_validated": "2025-11-10T13:43:23.810481"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        43.31,
                        45.03,
                        42.55,
                        52.9,
                        45.67,
                        45.96,
                        49.49,
                        51.7,
                        51.71,
                        60.11,
                        47.13,
                        51.93
                ],
                "unit": "%"
        },
        "current": {
                "value": 51.93,
                "unit": "%",
                "change": 4.8,
                "change_percent": 10.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 48.96,
                "min": 42.55,
                "max": 60.11,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 10.29,
                        "percentage": 19.8
                },
                {
                        "category": "Category B",
                        "value": 7.68,
                        "percentage": 14.8
                },
                {
                        "category": "Category C",
                        "value": 8.57,
                        "percentage": 16.5
                },
                {
                        "category": "Category D",
                        "value": 6.66,
                        "percentage": 12.8
                },
                {
                        "category": "Other",
                        "value": 18.73,
                        "percentage": 36.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.810481",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packing Error Rate"
        }
    },
}
