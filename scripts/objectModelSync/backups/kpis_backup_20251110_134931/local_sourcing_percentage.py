"""
Local Sourcing Percentage

The proportion of materials and services sourced locally, supporting local economies and reducing transportation emissions as suggested by ISO 20400.
"""

LOCAL_SOURCING_PERCENTAGE = {
    "code": "LOCAL_SOURCING_PERCENTAGE",
    "name": "Local Sourcing Percentage",
    "description": "The proportion of materials and services sourced locally, supporting local economies and reducing transportation emissions as suggested by ISO 20400.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Local Sourcing Percentage to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["PurchaseOrder", "Supplier"], "last_validated": "2025-11-10T13:43:23.614824"},
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
                        81.82,
                        76.45,
                        65.13,
                        67.76,
                        70.98,
                        69.74,
                        62.61,
                        74.28,
                        72.53,
                        71.24,
                        65.3,
                        65.6
                ],
                "unit": "%"
        },
        "current": {
                "value": 65.6,
                "unit": "%",
                "change": 0.3,
                "change_percent": 0.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 70.29,
                "min": 62.61,
                "max": 81.82,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 14.65,
                        "percentage": 22.3
                },
                {
                        "category": "Category B",
                        "value": 12.46,
                        "percentage": 19.0
                },
                {
                        "category": "Category C",
                        "value": 7.9,
                        "percentage": 12.0
                },
                {
                        "category": "Category D",
                        "value": 5.17,
                        "percentage": 7.9
                },
                {
                        "category": "Other",
                        "value": 25.42,
                        "percentage": 38.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.614824",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Local Sourcing Percentage"
        }
    },
}
