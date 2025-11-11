"""
Critical Incident Recovery Time

The average time it takes to recover from a critical security incident in the supply chain, demonstrating the resilience of the supply chain operations.
"""

CRITICAL_INCIDENT_RECOVERY_TIME = {
    "code": "CRITICAL_INCIDENT_RECOVERY_TIME",
    "name": "Critical Incident Recovery Time",
    "description": "The average time it takes to recover from a critical security incident in the supply chain, demonstrating the resilience of the supply chain operations.",
    "formula": "Sum of Recovery Times for Critical Incidents / Number of Critical Incidents",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Critical Incident Recovery Time to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:49:32.738831"},
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
                        187,
                        200,
                        197,
                        195,
                        168,
                        163,
                        194,
                        194,
                        168,
                        180,
                        170,
                        157
                ],
                "unit": "count"
        },
        "current": {
                "value": 157,
                "unit": "count",
                "change": -13,
                "change_percent": -7.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 181.08,
                "min": 157,
                "max": 200,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 43.65,
                        "percentage": 27.8
                },
                {
                        "category": "Segment B",
                        "value": 22.48,
                        "percentage": 14.3
                },
                {
                        "category": "Segment C",
                        "value": 26.0,
                        "percentage": 16.6
                },
                {
                        "category": "Segment D",
                        "value": 12.77,
                        "percentage": 8.1
                },
                {
                        "category": "Other",
                        "value": 52.1,
                        "percentage": 33.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.567306",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Critical Incident Recovery Time"
        }
    },
}
