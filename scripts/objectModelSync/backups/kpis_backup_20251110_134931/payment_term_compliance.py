"""
Payment Term Compliance

The rate at which payments to suppliers are made within the agreed-upon payment terms.
"""

PAYMENT_TERM_COMPLIANCE = {
    "code": "PAYMENT_TERM_COMPLIANCE",
    "name": "Payment Term Compliance",
    "description": "The rate at which payments to suppliers are made within the agreed-upon payment terms.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Payment Term Compliance to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Payment", "PurchaseOrder", "Supplier"], "last_validated": "2025-11-10T13:43:23.914486"},
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
                        523.17,
                        629.24,
                        592.78,
                        561.19,
                        634.26,
                        535.22,
                        631.72,
                        602.61,
                        566.15,
                        591.05,
                        537.49,
                        540.61
                ],
                "unit": "units"
        },
        "current": {
                "value": 540.61,
                "unit": "units",
                "change": 3.12,
                "change_percent": 0.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 578.79,
                "min": 523.17,
                "max": 634.26,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 141.58,
                        "percentage": 26.2
                },
                {
                        "category": "Category B",
                        "value": 116.73,
                        "percentage": 21.6
                },
                {
                        "category": "Category C",
                        "value": 58.72,
                        "percentage": 10.9
                },
                {
                        "category": "Category D",
                        "value": 42.22,
                        "percentage": 7.8
                },
                {
                        "category": "Other",
                        "value": 181.36,
                        "percentage": 33.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.914486",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Payment Term Compliance"
        }
    },
}
