"""
Security Compliance Cost Variance

The variance between budgeted and actual costs of maintaining compliance with security standards, which reflects financial management efficiency in security matters.
"""

SECURITY_COMPLIANCE_COST_VARIANCE = {
    "code": "SECURITY_COMPLIANCE_COST_VARIANCE",
    "name": "Security Compliance Cost Variance",
    "description": "The variance between budgeted and actual costs of maintaining compliance with security standards, which reflects financial management efficiency in security matters.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Security Compliance Cost Variance to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.548075"},
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
                        99005.83,
                        93939.08,
                        88273.98,
                        91020.04,
                        100707.67,
                        89004.83,
                        94602.7,
                        96422.82,
                        88247.31,
                        92635.41,
                        91890.19,
                        92995.79
                ],
                "unit": "$"
        },
        "current": {
                "value": 92995.79,
                "unit": "$",
                "change": 1105.6,
                "change_percent": 1.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 93228.8,
                "min": 88247.31,
                "max": 100707.67,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 20359.61,
                        "percentage": 21.9
                },
                {
                        "category": "Segment B",
                        "value": 11911.07,
                        "percentage": 12.8
                },
                {
                        "category": "Segment C",
                        "value": 11539.97,
                        "percentage": 12.4
                },
                {
                        "category": "Segment D",
                        "value": 7479.49,
                        "percentage": 8.0
                },
                {
                        "category": "Other",
                        "value": 41705.65,
                        "percentage": 44.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.319705",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Security Compliance Cost Variance"
        }
    },
}
