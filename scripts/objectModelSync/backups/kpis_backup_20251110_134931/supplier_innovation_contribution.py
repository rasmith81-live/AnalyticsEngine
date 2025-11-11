"""
Supplier Innovation Contribution

The extent to which suppliers contribute to innovation in products, processes, or services, enhancing competitiveness and value creation.
"""

SUPPLIER_INNOVATION_CONTRIBUTION = {
    "code": "SUPPLIER_INNOVATION_CONTRIBUTION",
    "name": "Supplier Innovation Contribution",
    "description": "The extent to which suppliers contribute to innovation in products, processes, or services, enhancing competitiveness and value creation.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Innovation Contribution to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Product", "Supplier"], "last_validated": "2025-11-10T13:43:24.863172"},
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
                        420.61,
                        380.07,
                        361.66,
                        494.63,
                        345.72,
                        413.35,
                        394.86,
                        357.43,
                        442.09,
                        492.63,
                        384.06,
                        348.88
                ],
                "unit": "units"
        },
        "current": {
                "value": 348.88,
                "unit": "units",
                "change": -35.18,
                "change_percent": -9.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 403.0,
                "min": 345.72,
                "max": 494.63,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 83.64,
                        "percentage": 24.0
                },
                {
                        "category": "Category B",
                        "value": 45.87,
                        "percentage": 13.1
                },
                {
                        "category": "Category C",
                        "value": 52.14,
                        "percentage": 14.9
                },
                {
                        "category": "Category D",
                        "value": 33.02,
                        "percentage": 9.5
                },
                {
                        "category": "Other",
                        "value": 134.21,
                        "percentage": 38.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.863172",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supplier Innovation Contribution"
        }
    },
}
