"""
Supplier Risk Assessment Coverage

The extent to which the supply base has been assessed for risks related to social, environmental, and economic factors as per ISO 20400.
"""

SUPPLIER_RISK_ASSESSMENT_COVERAGE = {
    "code": "SUPPLIER_RISK_ASSESSMENT_COVERAGE",
    "name": "Supplier Risk Assessment Coverage",
    "description": "The extent to which the supply base has been assessed for risks related to social, environmental, and economic factors as per ISO 20400.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Risk Assessment Coverage to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:43:24.888123"},
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
                        828.35,
                        726.09,
                        840.15,
                        786.5,
                        743.48,
                        805.36,
                        720.56,
                        840.97,
                        716.76,
                        728.79,
                        784.53,
                        803.45
                ],
                "unit": "units"
        },
        "current": {
                "value": 803.45,
                "unit": "units",
                "change": 18.92,
                "change_percent": 2.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 777.08,
                "min": 716.76,
                "max": 840.97,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 263.36,
                        "percentage": 32.8
                },
                {
                        "category": "Category B",
                        "value": 145.41,
                        "percentage": 18.1
                },
                {
                        "category": "Category C",
                        "value": 72.08,
                        "percentage": 9.0
                },
                {
                        "category": "Category D",
                        "value": 80.92,
                        "percentage": 10.1
                },
                {
                        "category": "Other",
                        "value": 241.68,
                        "percentage": 30.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.888123",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supplier Risk Assessment Coverage"
        }
    },
}
