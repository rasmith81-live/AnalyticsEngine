"""
Damage-Free Delivery Rate

The percentage of deliveries made without any damage to the goods.
"""

DAMAGE_FREE_DELIVERY_RATE = {
    "code": "DAMAGE_FREE_DELIVERY_RATE",
    "name": "Damage-Free Delivery Rate",
    "description": "The percentage of deliveries made without any damage to the goods.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Damage-Free Delivery Rate to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery"], "last_validated": "2025-11-10T13:43:23.396619"},
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
                        69.05,
                        65.96,
                        53.49,
                        50.13,
                        66.12,
                        63.54,
                        67.09,
                        52.09,
                        55.01,
                        54.06,
                        66.04,
                        68.14
                ],
                "unit": "%"
        },
        "current": {
                "value": 68.14,
                "unit": "%",
                "change": 2.1,
                "change_percent": 3.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 60.89,
                "min": 50.13,
                "max": 69.05,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 22.69,
                        "percentage": 33.3
                },
                {
                        "category": "Category B",
                        "value": 13.49,
                        "percentage": 19.8
                },
                {
                        "category": "Category C",
                        "value": 5.56,
                        "percentage": 8.2
                },
                {
                        "category": "Category D",
                        "value": 5.7,
                        "percentage": 8.4
                },
                {
                        "category": "Other",
                        "value": 20.7,
                        "percentage": 30.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.396619",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Damage-Free Delivery Rate"
        }
    },
}
