"""
Packing Error Resolution Time

The average time taken to resolve packing errors, impacting customer satisfaction and operational efficiency.
"""

PACKING_ERROR_RESOLUTION_TIME = {
    "code": "PACKING_ERROR_RESOLUTION_TIME",
    "name": "Packing Error Resolution Time",
    "description": "The average time taken to resolve packing errors, impacting customer satisfaction and operational efficiency.",
    "formula": "Total Time to Resolve Errors / Total Number of Errors",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Error Resolution Time to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Customer"], "last_validated": "2025-11-10T13:43:23.812924"},
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
                        106,
                        85,
                        84,
                        76,
                        86,
                        107,
                        88,
                        98,
                        108,
                        64,
                        98,
                        110
                ],
                "unit": "count"
        },
        "current": {
                "value": 110,
                "unit": "count",
                "change": 12,
                "change_percent": 12.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 92.5,
                "min": 64,
                "max": 110,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 29.01,
                        "percentage": 26.4
                },
                {
                        "category": "Category B",
                        "value": 27.33,
                        "percentage": 24.8
                },
                {
                        "category": "Category C",
                        "value": 17.12,
                        "percentage": 15.6
                },
                {
                        "category": "Category D",
                        "value": 7.24,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 29.3,
                        "percentage": 26.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.812924",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Packing Error Resolution Time"
        }
    },
}
