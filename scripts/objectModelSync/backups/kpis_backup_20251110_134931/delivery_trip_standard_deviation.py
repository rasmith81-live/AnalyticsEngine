"""
Delivery Trip Standard Deviation

The variability in delivery trip duration.
"""

DELIVERY_TRIP_STANDARD_DEVIATION = {
    "code": "DELIVERY_TRIP_STANDARD_DEVIATION",
    "name": "Delivery Trip Standard Deviation",
    "description": "The variability in delivery trip duration.",
    "formula": "Standard Deviation of Delivery Trip Distances or Times",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Delivery Trip Standard Deviation to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery"], "last_validated": "2025-11-10T13:43:23.429578"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
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
                        801.79,
                        731.02,
                        817.16,
                        704.8,
                        768.79,
                        749.4,
                        785.84,
                        679.12,
                        695.25,
                        806.22,
                        746.0,
                        682.74
                ],
                "unit": "units"
        },
        "current": {
                "value": 682.74,
                "unit": "units",
                "change": -63.26,
                "change_percent": -8.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 747.34,
                "min": 679.12,
                "max": 817.16,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 122.12,
                        "percentage": 17.9
                },
                {
                        "category": "Category B",
                        "value": 132.18,
                        "percentage": 19.4
                },
                {
                        "category": "Category C",
                        "value": 95.81,
                        "percentage": 14.0
                },
                {
                        "category": "Category D",
                        "value": 53.97,
                        "percentage": 7.9
                },
                {
                        "category": "Other",
                        "value": 278.66,
                        "percentage": 40.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.429578",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Delivery Trip Standard Deviation"
        }
    },
}
