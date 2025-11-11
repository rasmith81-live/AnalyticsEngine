"""
Security Process Automation Rate

The extent to which security processes are automated, demonstrating the organization
"""

SECURITY_PROCESS_AUTOMATION_RATE = {
    "code": "SECURITY_PROCESS_AUTOMATION_RATE",
    "name": "Security Process Automation Rate",
    "description": "The extent to which security processes are automated, demonstrating the organization",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Security Process Automation Rate to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.559198"},
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
                        70.93,
                        87.24,
                        81.14,
                        77.01,
                        80.27,
                        76.92,
                        89.89,
                        84.32,
                        85.04,
                        81.97,
                        81.91,
                        86.14
                ],
                "unit": "%"
        },
        "current": {
                "value": 86.14,
                "unit": "%",
                "change": 4.23,
                "change_percent": 5.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 81.9,
                "min": 70.93,
                "max": 89.89,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 26.62,
                        "percentage": 30.9
                },
                {
                        "category": "Segment B",
                        "value": 10.15,
                        "percentage": 11.8
                },
                {
                        "category": "Segment C",
                        "value": 13.12,
                        "percentage": 15.2
                },
                {
                        "category": "Segment D",
                        "value": 9.75,
                        "percentage": 11.3
                },
                {
                        "category": "Other",
                        "value": 26.5,
                        "percentage": 30.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.345305",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Security Process Automation Rate"
        }
    },
}
