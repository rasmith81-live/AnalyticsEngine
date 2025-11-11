"""
Cross-Border Security Compliance Rate

The rate at which the organization complies with cross-border security regulations, reflecting the ability to operate internationally without security-related disruptions.
"""

CROSS_BORDER_SECURITY_COMPLIANCE_RATE = {
    "code": "CROSS_BORDER_SECURITY_COMPLIANCE_RATE",
    "name": "Cross-Border Security Compliance Rate",
    "description": "The rate at which the organization complies with cross-border security regulations, reflecting the ability to operate internationally without security-related disruptions.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cross-Border Security Compliance Rate to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["Order", "Shipment"], "last_validated": "2025-11-10T13:49:32.784772"},
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
                        37.4,
                        39.19,
                        39.82,
                        34.86,
                        50.68,
                        41.95,
                        43.33,
                        46.32,
                        41.14,
                        40.88,
                        43.01,
                        52.73
                ],
                "unit": "%"
        },
        "current": {
                "value": 52.73,
                "unit": "%",
                "change": 9.72,
                "change_percent": 22.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 42.61,
                "min": 34.86,
                "max": 52.73,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 16.73,
                        "percentage": 31.7
                },
                {
                        "category": "Segment B",
                        "value": 8.23,
                        "percentage": 15.6
                },
                {
                        "category": "Segment C",
                        "value": 5.22,
                        "percentage": 9.9
                },
                {
                        "category": "Segment D",
                        "value": 3.49,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 19.06,
                        "percentage": 36.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.573735",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Cross-Border Security Compliance Rate"
        }
    },
}
