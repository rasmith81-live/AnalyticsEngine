"""
Security Incident Impact Scale

A scale that rates the impact of security incidents, helping to prioritize response efforts and allocate resources effectively.
"""

SECURITY_INCIDENT_IMPACT_SCALE = {
    "code": "SECURITY_INCIDENT_IMPACT_SCALE",
    "name": "Security Incident Impact Scale",
    "description": "A scale that rates the impact of security incidents, helping to prioritize response efforts and allocate resources effectively.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Security Incident Impact Scale to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.550586"},
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
                        300.75,
                        198.12,
                        237.81,
                        199.4,
                        293.59,
                        223.97,
                        223.56,
                        261.59,
                        319.1,
                        190.91,
                        186.13,
                        319.2
                ],
                "unit": "units"
        },
        "current": {
                "value": 319.2,
                "unit": "units",
                "change": 133.07,
                "change_percent": 71.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 246.18,
                "min": 186.13,
                "max": 319.2,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 83.52,
                        "percentage": 26.2
                },
                {
                        "category": "Segment B",
                        "value": 71.76,
                        "percentage": 22.5
                },
                {
                        "category": "Segment C",
                        "value": 54.81,
                        "percentage": 17.2
                },
                {
                        "category": "Segment D",
                        "value": 24.72,
                        "percentage": 7.7
                },
                {
                        "category": "Other",
                        "value": 84.39,
                        "percentage": 26.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.323771",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Security Incident Impact Scale"
        }
    },
}
