"""
Empty Miles

The number of miles a vehicle travels empty without carrying any load.
"""

EMPTY_MILES = {
    "code": "EMPTY_MILES",
    "name": "Empty Miles",
    "description": "The number of miles a vehicle travels empty without carrying any load.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Empty Miles to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": [], "last_validated": "2025-11-10T13:43:23.467381"},
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
                        877.19,
                        928.59,
                        979.44,
                        869.24,
                        889.27,
                        937.63,
                        852.8,
                        859.36,
                        947.04,
                        950.89,
                        930.74,
                        851.13
                ],
                "unit": "units"
        },
        "current": {
                "value": 851.13,
                "unit": "units",
                "change": -79.61,
                "change_percent": -8.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 906.11,
                "min": 851.13,
                "max": 979.44,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 230.29,
                        "percentage": 27.1
                },
                {
                        "category": "Category B",
                        "value": 181.87,
                        "percentage": 21.4
                },
                {
                        "category": "Category C",
                        "value": 132.98,
                        "percentage": 15.6
                },
                {
                        "category": "Category D",
                        "value": 35.67,
                        "percentage": 4.2
                },
                {
                        "category": "Other",
                        "value": 270.32,
                        "percentage": 31.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.467381",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Empty Miles"
        }
    },
}
