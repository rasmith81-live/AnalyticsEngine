"""
Packing Space Utilization

The percentage of available packing space that is effectively used, highlighting space management efficiency in packing areas.
"""

PACKING_SPACE_UTILIZATION = {
    "code": "PACKING_SPACE_UTILIZATION",
    "name": "Packing Space Utilization",
    "description": "The percentage of available packing space that is effectively used, highlighting space management efficiency in packing areas.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Space Utilization to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:43:23.838000"},
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
                        518.18,
                        491.13,
                        520.62,
                        437.86,
                        452.3,
                        398.26,
                        468.13,
                        531.89,
                        459.0,
                        416.68,
                        407.09,
                        467.43
                ],
                "unit": "units"
        },
        "current": {
                "value": 467.43,
                "unit": "units",
                "change": 60.34,
                "change_percent": 14.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 464.05,
                "min": 398.26,
                "max": 531.89,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 89.63,
                        "percentage": 19.2
                },
                {
                        "category": "Category B",
                        "value": 72.89,
                        "percentage": 15.6
                },
                {
                        "category": "Category C",
                        "value": 55.63,
                        "percentage": 11.9
                },
                {
                        "category": "Category D",
                        "value": 58.41,
                        "percentage": 12.5
                },
                {
                        "category": "Other",
                        "value": 190.87,
                        "percentage": 40.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.838000",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Packing Space Utilization"
        }
    },
}
