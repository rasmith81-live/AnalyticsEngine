"""
Supplier Development Program Effectiveness

The effectiveness of programs aimed at improving suppliers
"""

SUPPLIER_DEVELOPMENT_PROGRAM_EFFECTIVENESS = {
    "code": "SUPPLIER_DEVELOPMENT_PROGRAM_EFFECTIVENESS",
    "name": "Supplier Development Program Effectiveness",
    "description": "The effectiveness of programs aimed at improving suppliers",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Development Program Effectiveness to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:43:24.852126"},
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
                        908.03,
                        860.18,
                        883.81,
                        879.41,
                        927.59,
                        947.29,
                        876.13,
                        842.14,
                        949.41,
                        878.53,
                        825.48,
                        879.16
                ],
                "unit": "units"
        },
        "current": {
                "value": 879.16,
                "unit": "units",
                "change": 53.68,
                "change_percent": 6.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 888.1,
                "min": 825.48,
                "max": 949.41,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 234.98,
                        "percentage": 26.7
                },
                {
                        "category": "Category B",
                        "value": 111.7,
                        "percentage": 12.7
                },
                {
                        "category": "Category C",
                        "value": 131.06,
                        "percentage": 14.9
                },
                {
                        "category": "Category D",
                        "value": 69.11,
                        "percentage": 7.9
                },
                {
                        "category": "Other",
                        "value": 332.31,
                        "percentage": 37.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.852126",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supplier Development Program Effectiveness"
        }
    },
}
