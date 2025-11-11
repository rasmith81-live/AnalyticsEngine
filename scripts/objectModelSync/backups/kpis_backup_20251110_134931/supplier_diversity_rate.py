"""
Supplier Diversity Rate

The percentage of the supplier base that is composed of diverse businesses, promoting diversity as per ISO 20400
"""

SUPPLIER_DIVERSITY_RATE = {
    "code": "SUPPLIER_DIVERSITY_RATE",
    "name": "Supplier Diversity Rate",
    "description": "The percentage of the supplier base that is composed of diverse businesses, promoting diversity as per ISO 20400",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Diversity Rate to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["PurchaseOrder", "Supplier"], "last_validated": "2025-11-10T13:43:24.858742"},
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
                        70.74,
                        72.92,
                        65.93,
                        65.07,
                        72.74,
                        79.08,
                        79.52,
                        73.61,
                        75.28,
                        73.9,
                        62.98,
                        63.83
                ],
                "unit": "%"
        },
        "current": {
                "value": 63.83,
                "unit": "%",
                "change": 0.85,
                "change_percent": 1.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 71.3,
                "min": 62.98,
                "max": 79.52,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 10.71,
                        "percentage": 16.8
                },
                {
                        "category": "Category B",
                        "value": 17.33,
                        "percentage": 27.2
                },
                {
                        "category": "Category C",
                        "value": 11.85,
                        "percentage": 18.6
                },
                {
                        "category": "Category D",
                        "value": 6.69,
                        "percentage": 10.5
                },
                {
                        "category": "Other",
                        "value": 17.25,
                        "percentage": 27.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.858742",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Diversity Rate"
        }
    },
}
