"""
Packing Safety Incident Rate

The number of safety incidents occurring during packing operations, reflecting the safety and risk management of the packing process.
"""

PACKING_SAFETY_INCIDENT_RATE = {
    "code": "PACKING_SAFETY_INCIDENT_RATE",
    "name": "Packing Safety Incident Rate",
    "description": "The number of safety incidents occurring during packing operations, reflecting the safety and risk management of the packing process.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Safety Incident Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:43:23.835298"},
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
                        66.49,
                        62.86,
                        51.68,
                        54.25,
                        48.98,
                        56.9,
                        57.36,
                        63.11,
                        52.1,
                        54.12,
                        58.77,
                        62.64
                ],
                "unit": "%"
        },
        "current": {
                "value": 62.64,
                "unit": "%",
                "change": 3.87,
                "change_percent": 6.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 57.44,
                "min": 48.98,
                "max": 66.49,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9.96,
                        "percentage": 15.9
                },
                {
                        "category": "Category B",
                        "value": 8.3,
                        "percentage": 13.3
                },
                {
                        "category": "Category C",
                        "value": 9.99,
                        "percentage": 15.9
                },
                {
                        "category": "Category D",
                        "value": 6.43,
                        "percentage": 10.3
                },
                {
                        "category": "Other",
                        "value": 27.96,
                        "percentage": 44.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.835298",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packing Safety Incident Rate"
        }
    },
}
