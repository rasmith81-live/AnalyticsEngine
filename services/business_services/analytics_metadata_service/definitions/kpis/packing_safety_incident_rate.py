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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.171808"},
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
                        43.55,
                        49.18,
                        49.15,
                        50.25,
                        41.2,
                        59.29,
                        57.48,
                        59.22,
                        48.45,
                        56.1,
                        52.43,
                        51.38
                ],
                "unit": "%"
        },
        "current": {
                "value": 51.38,
                "unit": "%",
                "change": -1.05,
                "change_percent": -2.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 51.47,
                "min": 41.2,
                "max": 59.29,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 8.16,
                        "percentage": 15.9
                },
                {
                        "category": "Segment B",
                        "value": 7.14,
                        "percentage": 13.9
                },
                {
                        "category": "Segment C",
                        "value": 7.21,
                        "percentage": 14.0
                },
                {
                        "category": "Segment D",
                        "value": 5.21,
                        "percentage": 10.1
                },
                {
                        "category": "Other",
                        "value": 23.66,
                        "percentage": 46.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.427041",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packing Safety Incident Rate"
        }
    },
}
