"""
Pickup and Delivery Productivity

The number of pickups and deliveries made in a given period relative to the resource used.
"""

PICKUP_AND_DELIVERY_PRODUCTIVITY = {
    "code": "PICKUP_AND_DELIVERY_PRODUCTIVITY",
    "name": "Pickup and Delivery Productivity",
    "description": "The number of pickups and deliveries made in a given period relative to the resource used.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Pickup and Delivery Productivity to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery", "Product"], "last_validated": "2025-11-10T13:49:33.237999"},
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
                        427.81,
                        428.48,
                        370.68,
                        395.94,
                        379.4,
                        398.14,
                        475.95,
                        375.52,
                        373.19,
                        440.58,
                        426.33,
                        456.53
                ],
                "unit": "units"
        },
        "current": {
                "value": 456.53,
                "unit": "units",
                "change": 30.2,
                "change_percent": 7.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 412.38,
                "min": 370.68,
                "max": 475.95,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 88.51,
                        "percentage": 19.4
                },
                {
                        "category": "Category B",
                        "value": 125.39,
                        "percentage": 27.5
                },
                {
                        "category": "Category C",
                        "value": 42.37,
                        "percentage": 9.3
                },
                {
                        "category": "Category D",
                        "value": 59.17,
                        "percentage": 13.0
                },
                {
                        "category": "Other",
                        "value": 141.09,
                        "percentage": 30.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.931903",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Pickup and Delivery Productivity"
        }
    },
}
