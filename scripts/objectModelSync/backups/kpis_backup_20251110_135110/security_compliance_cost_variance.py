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
                        86411.54,
                        82366.8,
                        80631.06,
                        86658.11,
                        78541.05,
                        80572.28,
                        83478.53,
                        87458.33,
                        86750.92,
                        80176.89,
                        75012.47,
                        74156.81
                ],
                "unit": "$"
        },
        "current": {
                "value": 74156.81,
                "unit": "$",
                "change": -855.66,
                "change_percent": -1.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 81851.23,
                "min": 74156.81,
                "max": 87458.33,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16465.14,
                        "percentage": 22.2
                },
                {
                        "category": "Category B",
                        "value": 18927.59,
                        "percentage": 25.5
                },
                {
                        "category": "Category C",
                        "value": 9074.6,
                        "percentage": 12.2
                },
                {
                        "category": "Category D",
                        "value": 5090.32,
                        "percentage": 6.9
                },
                {
                        "category": "Other",
                        "value": 24599.16,
                        "percentage": 33.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.708218",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Security Compliance Cost Variance"
        }
    },
}
