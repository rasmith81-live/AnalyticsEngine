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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["PurchaseOrder", "Supplier"], "last_validated": "2025-11-10T13:43:24.861071"},
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
                        80.0,
                        77.0,
                        88.0,
                        84.9,
                        78.2,
                        82.5,
                        83.7,
                        82.6,
                        84.6,
                        82.0,
                        87.3,
                        78.0
                ],
                "unit": "score"
        },
        "current": {
                "value": 78.0,
                "unit": "score",
                "change": -9.3,
                "change_percent": -10.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 82.4,
                "min": 77.0,
                "max": 88.0,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 20.05,
                        "percentage": 25.7
                },
                {
                        "category": "Category B",
                        "value": 14.6,
                        "percentage": 18.7
                },
                {
                        "category": "Category C",
                        "value": 9.06,
                        "percentage": 11.6
                },
                {
                        "category": "Category D",
                        "value": 9.65,
                        "percentage": 12.4
                },
                {
                        "category": "Other",
                        "value": 24.64,
                        "percentage": 31.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.861071",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Supplier Engagement Score"
        }
    },
}
