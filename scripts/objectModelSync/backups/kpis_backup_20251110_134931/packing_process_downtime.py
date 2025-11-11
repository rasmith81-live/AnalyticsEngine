"""
Packing Process Downtime

The total time when packing operations are halted due to equipment failure or other disruptions, impacting operational efficiency.
"""

PACKING_PROCESS_DOWNTIME = {
    "code": "PACKING_PROCESS_DOWNTIME",
    "name": "Packing Process Downtime",
    "description": "The total time when packing operations are halted due to equipment failure or other disruptions, impacting operational efficiency.",
    "formula": "Total Downtime / Total Packing Time",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Process Downtime to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:43:23.830995"},
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
                        25.8,
                        19.5,
                        21.3,
                        21.8,
                        19.1,
                        22.9,
                        21.1,
                        19.9,
                        18.6,
                        20.7,
                        24.2,
                        22.0
                ],
                "unit": "days"
        },
        "current": {
                "value": 22.0,
                "unit": "days",
                "change": -2.2,
                "change_percent": -9.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 21.41,
                "min": 18.6,
                "max": 25.8,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 5.01,
                        "percentage": 22.8
                },
                {
                        "category": "Category B",
                        "value": 4.64,
                        "percentage": 21.1
                },
                {
                        "category": "Category C",
                        "value": 2.03,
                        "percentage": 9.2
                },
                {
                        "category": "Category D",
                        "value": 1.91,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 8.41,
                        "percentage": 38.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.830995",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Packing Process Downtime"
        }
    },
}
