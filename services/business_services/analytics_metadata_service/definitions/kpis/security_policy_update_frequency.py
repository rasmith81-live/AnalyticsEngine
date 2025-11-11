"""
Security Policy Update Frequency

The frequency with which security policies are reviewed and updated, showing the organization
"""

SECURITY_POLICY_UPDATE_FREQUENCY = {
    "code": "SECURITY_POLICY_UPDATE_FREQUENCY",
    "name": "Security Policy Update Frequency",
    "description": "The frequency with which security policies are reviewed and updated, showing the organization",
    "formula": "Total Number of Security Policy Updates / Time Period",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Security Policy Update Frequency to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.557536"},
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
                        312,
                        332,
                        299,
                        292,
                        329,
                        330,
                        315,
                        338,
                        336,
                        301,
                        322,
                        317
                ],
                "unit": "count"
        },
        "current": {
                "value": 317,
                "unit": "count",
                "change": -5,
                "change_percent": -1.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 318.58,
                "min": 292,
                "max": 338,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 62.62,
                        "percentage": 19.8
                },
                {
                        "category": "Segment B",
                        "value": 70.27,
                        "percentage": 22.2
                },
                {
                        "category": "Segment C",
                        "value": 63.67,
                        "percentage": 20.1
                },
                {
                        "category": "Segment D",
                        "value": 14.32,
                        "percentage": 4.5
                },
                {
                        "category": "Other",
                        "value": 106.12,
                        "percentage": 33.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.340816",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Security Policy Update Frequency"
        }
    },
}
