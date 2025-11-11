"""
Emergency Procedure Testing Frequency

The frequency at which emergency procedures are tested, indicating the preparedness for potential supply chain disruptions.
"""

EMERGENCY_PROCEDURE_TESTING_FREQUENCY = {
    "code": "EMERGENCY_PROCEDURE_TESTING_FREQUENCY",
    "name": "Emergency Procedure Testing Frequency",
    "description": "The frequency at which emergency procedures are tested, indicating the preparedness for potential supply chain disruptions.",
    "formula": "Total Number of Emergency Tests and Drills / Time Period",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Emergency Procedure Testing Frequency to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.463704"},
    "required_objects": [],
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
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
                        370,
                        417,
                        383,
                        408,
                        376,
                        385,
                        402,
                        399,
                        371,
                        381,
                        378,
                        400
                ],
                "unit": "count"
        },
        "current": {
                "value": 400,
                "unit": "count",
                "change": 22,
                "change_percent": 5.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 389.17,
                "min": 370,
                "max": 417,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 126.76,
                        "percentage": 31.7
                },
                {
                        "category": "Category B",
                        "value": 45.27,
                        "percentage": 11.3
                },
                {
                        "category": "Category C",
                        "value": 71.89,
                        "percentage": 18.0
                },
                {
                        "category": "Category D",
                        "value": 45.35,
                        "percentage": 11.3
                },
                {
                        "category": "Other",
                        "value": 110.73,
                        "percentage": 27.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.463704",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Emergency Procedure Testing Frequency"
        }
    },
}
