"""
Supplier Consolidation Rate

The extent to which the buying organization has decreased its number of suppliers to optimize the supply base.
"""

SUPPLIER_CONSOLIDATION_RATE = {
    "code": "SUPPLIER_CONSOLIDATION_RATE",
    "name": "Supplier Consolidation Rate",
    "description": "The extent to which the buying organization has decreased its number of suppliers to optimize the supply base.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Consolidation Rate to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:43:24.848848"},
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
                        87.58,
                        82.35,
                        88.55,
                        81.14,
                        82.06,
                        75.34,
                        83.14,
                        72.94,
                        70.26,
                        73.81,
                        75.71,
                        86.18
                ],
                "unit": "%"
        },
        "current": {
                "value": 86.18,
                "unit": "%",
                "change": 10.47,
                "change_percent": 13.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 79.92,
                "min": 70.26,
                "max": 88.55,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.07,
                        "percentage": 18.6
                },
                {
                        "category": "Category B",
                        "value": 15.27,
                        "percentage": 17.7
                },
                {
                        "category": "Category C",
                        "value": 15.64,
                        "percentage": 18.1
                },
                {
                        "category": "Category D",
                        "value": 10.0,
                        "percentage": 11.6
                },
                {
                        "category": "Other",
                        "value": 29.2,
                        "percentage": 33.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.848848",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Consolidation Rate"
        }
    },
}
