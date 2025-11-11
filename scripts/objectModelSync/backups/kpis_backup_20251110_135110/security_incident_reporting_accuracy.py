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
                        115.3,
                        152.24,
                        121.93,
                        213.86,
                        149.29,
                        125.71,
                        209.08,
                        214.49,
                        203.35,
                        134.64,
                        197.53,
                        212.35
                ],
                "unit": "units"
        },
        "current": {
                "value": 212.35,
                "unit": "units",
                "change": 14.82,
                "change_percent": 7.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 170.81,
                "min": 115.3,
                "max": 214.49,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 59.8,
                        "percentage": 28.2
                },
                {
                        "category": "Category B",
                        "value": 34.63,
                        "percentage": 16.3
                },
                {
                        "category": "Category C",
                        "value": 38.46,
                        "percentage": 18.1
                },
                {
                        "category": "Category D",
                        "value": 23.52,
                        "percentage": 11.1
                },
                {
                        "category": "Other",
                        "value": 55.94,
                        "percentage": 26.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.714542",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Security Incident Reporting Accuracy"
        }
    },
}
