"""
Supplier Engagement Score

The level of supplier involvement in sustainability initiatives, supporting the goals of ISO 20400.
"""

SUPPLIER_ENGAGEMENT_SCORE = {
    "code": "SUPPLIER_ENGAGEMENT_SCORE",
    "name": "Supplier Engagement Score",
    "description": "The level of supplier involvement in sustainability initiatives, supporting the goals of ISO 20400.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Engagement Score to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["PurchaseOrder", "Supplier"], "last_validated": "2025-11-10T13:49:33.634843"},
    "required_objects": [],
    "modules": ["ISO_20400"],
    "module_code": "ISO_20400",
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
                        82.4,
                        91.2,
                        80.8,
                        88.4,
                        89.6,
                        86.9,
                        82.4,
                        87.3,
                        91.5,
                        86.3,
                        81.7,
                        87.4
                ],
                "unit": "score"
        },
        "current": {
                "value": 87.4,
                "unit": "score",
                "change": 5.7,
                "change_percent": 7.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 86.33,
                "min": 80.8,
                "max": 91.5,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 20.04,
                        "percentage": 22.9
                },
                {
                        "category": "Segment B",
                        "value": 18.06,
                        "percentage": 20.7
                },
                {
                        "category": "Segment C",
                        "value": 8.44,
                        "percentage": 9.7
                },
                {
                        "category": "Segment D",
                        "value": 4.55,
                        "percentage": 5.2
                },
                {
                        "category": "Other",
                        "value": 36.31,
                        "percentage": 41.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.550851",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Supplier Engagement Score"
        }
    },
}
