"""
Supply Chain Carbon Footprint

The total amount of greenhouse gases produced directly or indirectly by supply chain activities, measured in carbon dioxide equivalent.
"""

SUPPLY_CHAIN_CARBON_FOOTPRINT = {
    "code": "SUPPLY_CHAIN_CARBON_FOOTPRINT",
    "name": "Supply Chain Carbon Footprint",
    "description": "The total amount of greenhouse gases produced directly or indirectly by supply chain activities, measured in carbon dioxide equivalent.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Carbon Footprint to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": [], "last_validated": "2025-11-10T13:43:24.897102"},
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
                        463.29,
                        540.36,
                        564.15,
                        529.35,
                        571.32,
                        501.11,
                        538.81,
                        492.1,
                        600.96,
                        605.14,
                        495.59,
                        541.47
                ],
                "unit": "units"
        },
        "current": {
                "value": 541.47,
                "unit": "units",
                "change": 45.88,
                "change_percent": 9.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 536.97,
                "min": 463.29,
                "max": 605.14,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 122.32,
                        "percentage": 22.6
                },
                {
                        "category": "Category B",
                        "value": 70.32,
                        "percentage": 13.0
                },
                {
                        "category": "Category C",
                        "value": 86.31,
                        "percentage": 15.9
                },
                {
                        "category": "Category D",
                        "value": 65.1,
                        "percentage": 12.0
                },
                {
                        "category": "Other",
                        "value": 197.42,
                        "percentage": 36.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.897102",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supply Chain Carbon Footprint"
        }
    },
}
