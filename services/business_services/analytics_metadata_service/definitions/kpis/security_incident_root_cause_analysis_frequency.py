"""
Security Incident Root Cause Analysis Frequency

The regularity with which root cause analyses are conducted following security incidents, which is critical for preventing future occurrences.
"""

SECURITY_INCIDENT_ROOT_CAUSE_ANALYSIS_FREQUENCY = {
    "code": "SECURITY_INCIDENT_ROOT_CAUSE_ANALYSIS_FREQUENCY",
    "name": "Security Incident Root Cause Analysis Frequency",
    "description": "The regularity with which root cause analyses are conducted following security incidents, which is critical for preventing future occurrences.",
    "formula": "Total Number of Root Cause Analyses / Number of Security Incidents",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Security Incident Root Cause Analysis Frequency to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.554304"},
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
                        471,
                        439,
                        438,
                        439,
                        435,
                        455,
                        438,
                        464,
                        456,
                        470,
                        446,
                        469
                ],
                "unit": "count"
        },
        "current": {
                "value": 469,
                "unit": "count",
                "change": 23,
                "change_percent": 5.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 451.67,
                "min": 435,
                "max": 471,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 111.01,
                        "percentage": 23.7
                },
                {
                        "category": "Segment B",
                        "value": 94.59,
                        "percentage": 20.2
                },
                {
                        "category": "Segment C",
                        "value": 85.32,
                        "percentage": 18.2
                },
                {
                        "category": "Segment D",
                        "value": 31.56,
                        "percentage": 6.7
                },
                {
                        "category": "Other",
                        "value": 146.52,
                        "percentage": 31.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.333035",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Security Incident Root Cause Analysis Frequency"
        }
    },
}
