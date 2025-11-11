"""
Supply Chain Transparency Index

A measure of the visibility and traceability of products and materials throughout the supply chain, as recommended by ISO 20400.
"""

SUPPLY_CHAIN_TRANSPARENCY_INDEX = {
    "code": "SUPPLY_CHAIN_TRANSPARENCY_INDEX",
    "name": "Supply Chain Transparency Index",
    "description": "A measure of the visibility and traceability of products and materials throughout the supply chain, as recommended by ISO 20400.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Transparency Index to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["Product"], "last_validated": "2025-11-10T13:43:24.949635"},
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
                        64.1,
                        69.1,
                        62.3,
                        64.1,
                        73.9,
                        71.4,
                        67.0,
                        69.5,
                        71.6,
                        72.9,
                        66.7,
                        63.1
                ],
                "unit": "score"
        },
        "current": {
                "value": 63.1,
                "unit": "score",
                "change": -3.6,
                "change_percent": -5.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 67.98,
                "min": 62.3,
                "max": 73.9,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.03,
                        "percentage": 25.4
                },
                {
                        "category": "Category B",
                        "value": 13.27,
                        "percentage": 21.0
                },
                {
                        "category": "Category C",
                        "value": 7.03,
                        "percentage": 11.1
                },
                {
                        "category": "Category D",
                        "value": 5.07,
                        "percentage": 8.0
                },
                {
                        "category": "Other",
                        "value": 21.7,
                        "percentage": 34.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.949635",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Supply Chain Transparency Index"
        }
    },
}
