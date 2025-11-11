"""
Packing Station Utilization

The percentage of packing stations that are actively in use, reflecting the operational efficiency of packing facilities.
"""

PACKING_STATION_UTILIZATION = {
    "code": "PACKING_STATION_UTILIZATION",
    "name": "Packing Station Utilization",
    "description": "The percentage of packing stations that are actively in use, reflecting the operational efficiency of packing facilities.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Station Utilization to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:43:23.840077"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        196.69,
                        250.01,
                        190.99,
                        212.52,
                        287.24,
                        293.25,
                        255.14,
                        240.71,
                        278.42,
                        276.74,
                        245.15,
                        295.93
                ],
                "unit": "units"
        },
        "current": {
                "value": 295.93,
                "unit": "units",
                "change": 50.78,
                "change_percent": 20.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 251.9,
                "min": 190.99,
                "max": 295.93,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 93.42,
                        "percentage": 31.6
                },
                {
                        "category": "Category B",
                        "value": 41.17,
                        "percentage": 13.9
                },
                {
                        "category": "Category C",
                        "value": 37.35,
                        "percentage": 12.6
                },
                {
                        "category": "Category D",
                        "value": 25.35,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 98.64,
                        "percentage": 33.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.840077",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Packing Station Utilization"
        }
    },
}
