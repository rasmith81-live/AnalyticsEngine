"""
Carbon Footprint of Procurement

The total greenhouse gas emissions associated with procurement activities, aiming to measure and reduce the carbon footprint as per ISO 20400 guidance.
"""

CARBON_FOOTPRINT_OF_PROCUREMENT = {
    "code": "CARBON_FOOTPRINT_OF_PROCUREMENT",
    "name": "Carbon Footprint of Procurement",
    "description": "The total greenhouse gas emissions associated with procurement activities, aiming to measure and reduce the carbon footprint as per ISO 20400 guidance.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Carbon Footprint of Procurement to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": [], "last_validated": "2025-11-10T13:43:23.067756"},
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
                        570.85,
                        555.82,
                        670.24,
                        641.31,
                        669.48,
                        552.94,
                        696.78,
                        581.84,
                        634.88,
                        625.36,
                        666.89,
                        558.29
                ],
                "unit": "units"
        },
        "current": {
                "value": 558.29,
                "unit": "units",
                "change": -108.6,
                "change_percent": -16.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 618.72,
                "min": 552.94,
                "max": 696.78,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 105.92,
                        "percentage": 19.0
                },
                {
                        "category": "Category B",
                        "value": 78.15,
                        "percentage": 14.0
                },
                {
                        "category": "Category C",
                        "value": 119.26,
                        "percentage": 21.4
                },
                {
                        "category": "Category D",
                        "value": 73.38,
                        "percentage": 13.1
                },
                {
                        "category": "Other",
                        "value": 181.58,
                        "percentage": 32.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.067756",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Carbon Footprint of Procurement"
        }
    },
}
