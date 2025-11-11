"""
Non-Compliant Spend

The amount of spending that does not comply with procurement policies or contracts.
"""

NON_COMPLIANT_SPEND = {
    "code": "NON_COMPLIANT_SPEND",
    "name": "Non-Compliant Spend",
    "description": "The amount of spending that does not comply with procurement policies or contracts.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Non-Compliant Spend to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Contract", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.694267"},
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
                        143.14,
                        164.12,
                        181.22,
                        100.66,
                        70.71,
                        67.76,
                        141.39,
                        70.55,
                        190.66,
                        134.21,
                        184.15,
                        151.09
                ],
                "unit": "units"
        },
        "current": {
                "value": 151.09,
                "unit": "units",
                "change": -33.06,
                "change_percent": -18.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 133.31,
                "min": 67.76,
                "max": 190.66,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 31.57,
                        "percentage": 20.9
                },
                {
                        "category": "Category B",
                        "value": 35.54,
                        "percentage": 23.5
                },
                {
                        "category": "Category C",
                        "value": 22.56,
                        "percentage": 14.9
                },
                {
                        "category": "Category D",
                        "value": 12.62,
                        "percentage": 8.4
                },
                {
                        "category": "Other",
                        "value": 48.8,
                        "percentage": 32.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.694267",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Non-Compliant Spend"
        }
    },
}
