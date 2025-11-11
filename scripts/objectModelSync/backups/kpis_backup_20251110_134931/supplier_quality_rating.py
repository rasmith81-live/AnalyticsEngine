"""
Supplier Quality Rating

The average score of suppliers
"""

SUPPLIER_QUALITY_RATING = {
    "code": "SUPPLIER_QUALITY_RATING",
    "name": "Supplier Quality Rating",
    "description": "The average score of suppliers",
    "formula": "Sum of Supplier Quality Scores / Number of Suppliers",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Quality Rating to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["QualityMetric", "Supplier"], "last_validated": "2025-11-10T13:43:24.879135"},
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
                        276,
                        305,
                        311,
                        267,
                        269,
                        269,
                        272,
                        310,
                        266,
                        287,
                        305,
                        291
                ],
                "unit": "count"
        },
        "current": {
                "value": 291,
                "unit": "count",
                "change": -14,
                "change_percent": -4.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 285.67,
                "min": 266,
                "max": 311,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 98.07,
                        "percentage": 33.7
                },
                {
                        "category": "Category B",
                        "value": 65.32,
                        "percentage": 22.4
                },
                {
                        "category": "Category C",
                        "value": 30.14,
                        "percentage": 10.4
                },
                {
                        "category": "Category D",
                        "value": 26.56,
                        "percentage": 9.1
                },
                {
                        "category": "Other",
                        "value": 70.91,
                        "percentage": 24.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.879135",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Supplier Quality Rating"
        }
    },
}
