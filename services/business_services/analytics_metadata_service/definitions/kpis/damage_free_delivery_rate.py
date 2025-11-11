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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery"], "last_validated": "2025-11-10T13:49:32.899049"},
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
                        72.86,
                        61.52,
                        58.93,
                        74.92,
                        61.03,
                        62.88,
                        69.86,
                        59.38,
                        76.77,
                        64.1,
                        69.71,
                        74.59
                ],
                "unit": "%"
        },
        "current": {
                "value": 74.59,
                "unit": "%",
                "change": 4.88,
                "change_percent": 7.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 67.21,
                "min": 58.93,
                "max": 76.77,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 17.75,
                        "percentage": 23.8
                },
                {
                        "category": "Segment B",
                        "value": 18.9,
                        "percentage": 25.3
                },
                {
                        "category": "Segment C",
                        "value": 11.31,
                        "percentage": 15.2
                },
                {
                        "category": "Segment D",
                        "value": 7.56,
                        "percentage": 10.1
                },
                {
                        "category": "Other",
                        "value": 19.07,
                        "percentage": 25.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.863921",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Damage-Free Delivery Rate"
        }
    },
}
