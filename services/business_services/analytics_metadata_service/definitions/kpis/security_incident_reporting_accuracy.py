"""
Security Incident Reporting Accuracy

The accuracy of security incident reporting, which is crucial for effective incident management and continuous improvement.
"""

SECURITY_INCIDENT_REPORTING_ACCURACY = {
    "code": "SECURITY_INCIDENT_REPORTING_ACCURACY",
    "name": "Security Incident Reporting Accuracy",
    "description": "The accuracy of security incident reporting, which is crucial for effective incident management and continuous improvement.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Security Incident Reporting Accuracy to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.552162"},
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
                        891.6,
                        995.1,
                        998.67,
                        903.58,
                        883.58,
                        996.88,
                        860.01,
                        938.99,
                        896.11,
                        972.35,
                        884.95,
                        871.76
                ],
                "unit": "units"
        },
        "current": {
                "value": 871.76,
                "unit": "units",
                "change": -13.19,
                "change_percent": -1.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 924.47,
                "min": 860.01,
                "max": 998.67,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 141.3,
                        "percentage": 16.2
                },
                {
                        "category": "Segment B",
                        "value": 240.16,
                        "percentage": 27.5
                },
                {
                        "category": "Segment C",
                        "value": 77.57,
                        "percentage": 8.9
                },
                {
                        "category": "Segment D",
                        "value": 110.66,
                        "percentage": 12.7
                },
                {
                        "category": "Other",
                        "value": 302.07,
                        "percentage": 34.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.328248",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Security Incident Reporting Accuracy"
        }
    },
}
