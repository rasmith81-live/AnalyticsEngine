"""
Perfect Order Rate

The percentage of orders that are delivered on time, complete, and without damage, indicating flawless execution.
"""

PERFECT_ORDER_RATE = {
    "code": "PERFECT_ORDER_RATE",
    "name": "Perfect Order Rate",
    "description": "The percentage of orders that are delivered on time, complete, and without damage, indicating flawless execution.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Perfect Order Rate to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:43:23.926123"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        75.24,
                        68.74,
                        82.01,
                        82.56,
                        86.9,
                        76.11,
                        84.18,
                        71.47,
                        84.35,
                        77.89,
                        69.95,
                        78.11
                ],
                "unit": "%"
        },
        "current": {
                "value": 78.11,
                "unit": "%",
                "change": 8.16,
                "change_percent": 11.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 78.13,
                "min": 68.74,
                "max": 86.9,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.71,
                        "percentage": 21.4
                },
                {
                        "category": "Category B",
                        "value": 12.02,
                        "percentage": 15.4
                },
                {
                        "category": "Category C",
                        "value": 8.37,
                        "percentage": 10.7
                },
                {
                        "category": "Category D",
                        "value": 12.02,
                        "percentage": 15.4
                },
                {
                        "category": "Other",
                        "value": 28.99,
                        "percentage": 37.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.926123",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Perfect Order Rate"
        }
    },
}
