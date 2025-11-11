"""
Supplier Compliance to Quality Standards

The percentage of suppliers that comply with predefined quality standards, ensuring consistency and reliability in the supply chain.
"""

SUPPLIER_COMPLIANCE_TO_QUALITY_STANDARDS = {
    "code": "SUPPLIER_COMPLIANCE_TO_QUALITY_STANDARDS",
    "name": "Supplier Compliance to Quality Standards",
    "description": "The percentage of suppliers that comply with predefined quality standards, ensuring consistency and reliability in the supply chain.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Compliance to Quality Standards to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["QualityMetric", "Supplier"], "last_validated": "2025-11-10T13:43:24.846274"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        939.99,
                        1003.98,
                        977.39,
                        1073.43,
                        955.69,
                        994.32,
                        1052.41,
                        1071.03,
                        969.49,
                        961.05,
                        1083.07,
                        961.85
                ],
                "unit": "units"
        },
        "current": {
                "value": 961.85,
                "unit": "units",
                "change": -121.22,
                "change_percent": -11.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 1003.64,
                "min": 939.99,
                "max": 1083.07,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 241.98,
                        "percentage": 25.2
                },
                {
                        "category": "Category B",
                        "value": 127.83,
                        "percentage": 13.3
                },
                {
                        "category": "Category C",
                        "value": 171.79,
                        "percentage": 17.9
                },
                {
                        "category": "Category D",
                        "value": 66.38,
                        "percentage": 6.9
                },
                {
                        "category": "Other",
                        "value": 353.87,
                        "percentage": 36.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.846274",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supplier Compliance to Quality Standards"
        }
    },
}
