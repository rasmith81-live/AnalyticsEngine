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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.173375"},
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
                        230.07,
                        318.31,
                        244.11,
                        262.77,
                        342.95,
                        347.74,
                        318.72,
                        326.19,
                        306.83,
                        220.27,
                        241.17,
                        332.17
                ],
                "unit": "units"
        },
        "current": {
                "value": 332.17,
                "unit": "units",
                "change": 91.0,
                "change_percent": 37.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 290.94,
                "min": 220.27,
                "max": 347.74,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 50.16,
                        "percentage": 15.1
                },
                {
                        "category": "Segment B",
                        "value": 69.48,
                        "percentage": 20.9
                },
                {
                        "category": "Segment C",
                        "value": 52.06,
                        "percentage": 15.7
                },
                {
                        "category": "Segment D",
                        "value": 26.21,
                        "percentage": 7.9
                },
                {
                        "category": "Other",
                        "value": 134.26,
                        "percentage": 40.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.430138",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Packing Space Utilization"
        }
    },
}
