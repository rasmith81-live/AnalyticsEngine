"""
Supplier Diversity

The diversity of the company
"""

SUPPLIER_DIVERSITY = {
    "code": "SUPPLIER_DIVERSITY",
    "name": "Supplier Diversity",
    "description": "The diversity of the company",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Diversity to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:43:24.855969"},
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
                        302.36,
                        286.6,
                        314.33,
                        331.87,
                        336.06,
                        331.09,
                        224.83,
                        313.0,
                        332.62,
                        280.7,
                        257.28,
                        236.84
                ],
                "unit": "units"
        },
        "current": {
                "value": 236.84,
                "unit": "units",
                "change": -20.44,
                "change_percent": -7.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 295.63,
                "min": 224.83,
                "max": 336.06,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 63.8,
                        "percentage": 26.9
                },
                {
                        "category": "Category B",
                        "value": 57.43,
                        "percentage": 24.2
                },
                {
                        "category": "Category C",
                        "value": 30.61,
                        "percentage": 12.9
                },
                {
                        "category": "Category D",
                        "value": 22.41,
                        "percentage": 9.5
                },
                {
                        "category": "Other",
                        "value": 62.59,
                        "percentage": 26.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.855969",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supplier Diversity"
        }
    },
}
