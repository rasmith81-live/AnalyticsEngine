"""
Early Payment Discounts Captured

The percentage of available early payment discounts that are successfully obtained.
"""

EARLY_PAYMENT_DISCOUNTS_CAPTURED = {
    "code": "EARLY_PAYMENT_DISCOUNTS_CAPTURED",
    "name": "Early Payment Discounts Captured",
    "description": "The percentage of available early payment discounts that are successfully obtained.",
    "formula": "Total Amount of Discounts for Early Payments / Total Number of Payments",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Early Payment Discounts Captured to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Payment"], "last_validated": "2025-11-10T13:49:32.937326"},
    "required_objects": [],
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
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
                        271,
                        305,
                        286,
                        291,
                        304,
                        270,
                        280,
                        280,
                        263,
                        262,
                        287,
                        287
                ],
                "unit": "count"
        },
        "current": {
                "value": 287,
                "unit": "count",
                "change": 0,
                "change_percent": 0.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 282.17,
                "min": 262,
                "max": 305,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 94.98,
                        "percentage": 33.1
                },
                {
                        "category": "Segment B",
                        "value": 61.45,
                        "percentage": 21.4
                },
                {
                        "category": "Segment C",
                        "value": 21.02,
                        "percentage": 7.3
                },
                {
                        "category": "Segment D",
                        "value": 29.99,
                        "percentage": 10.4
                },
                {
                        "category": "Other",
                        "value": 79.56,
                        "percentage": 27.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.946957",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Early Payment Discounts Captured"
        }
    },
}
